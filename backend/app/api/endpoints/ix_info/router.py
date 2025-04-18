import re
from datetime import date
from typing import List, Optional

from app.api.deps import SessionDep
from app.api.endpoints.jpx_info.schema import industry_17_count
from app.models import IxHeadTitle, JpxStockInfo
from fastapi import APIRouter, HTTPException, Query
from sqlalchemy import func
from sqlmodel import select

from . import schema as sc

router = APIRouter()


@router.get("/document/count", summary="XBRL文書数を取得", response_model=int)
def get_document_count(
    *, session: SessionDep, date_str: Optional[str] = Query(None)
) -> int:

    if date_str and not re.match(r"^\d{4}-\d{2}-\d{2}$", date_str):
        raise HTTPException(
            status_code=400,
            detail="日付の形式が正しくありません。YYYY-MM-DD形式で指定してください。",
        )

    convert_date = date.fromisoformat(date_str) if date_str else None

    statement = select(IxHeadTitle)
    if convert_date:
        statement = statement.where(IxHeadTitle.reporting_date == convert_date)
    results = session.exec(statement)
    items = results.all()
    count = len(items)

    return count


@router.get(
    "/document/latest/title", summary="最新XBRL文書のタイトルを取得", response_model=str
)
def get_latest_document_title(*, session: SessionDep) -> str:

    statement = select(IxHeadTitle).order_by(IxHeadTitle.insert_date.desc())
    results = session.exec(statement)
    item = results.first()
    latest_title = f"{item.securities_code} {item.company_name} {item.document_name}"

    return latest_title


@router.get(
    "/document/list",
    summary="XBRL文書のリストを取得",
    response_model=sc.DocumentListPublics,
)
def get_document_list(
    *,
    session: SessionDep,
    report_types: Optional[List[str]] = Query(None),
    date_str: Optional[str] = Query(None),
    industry_17_code: Optional[int] = Query(None),
    limit: Optional[int] = Query(None),
    page: Optional[int] = Query(1),
) -> sc.DocumentListPublics:

    if date_str and not re.match(r"^\d{4}-\d{2}-\d{2}$", date_str):
        raise HTTPException(
            status_code=400,
            detail="日付の形式が正しくありません。YYYY-MM-DD形式で指定してください。",
        )
    if date_str is None and industry_17_code is None:
        statement = (
            select(IxHeadTitle)
            .where(IxHeadTitle.reporting_date != None)
            .order_by(IxHeadTitle.reporting_date.desc())
        )
        if report_types:
            statement = statement.where(
                IxHeadTitle.report_type.in_(report_types),
                IxHeadTitle.current_period != None,
            )
        results = session.exec(statement)
        item = results.first()

        if item is None:
            raise HTTPException(status_code=404, detail="No documents found.")

        reporting_date = item.reporting_date
        date_str = reporting_date.strftime("%Y-%m-%d")

    convert_date = date.fromisoformat(date_str) if date_str else None

    statement = (
        select(IxHeadTitle)
        .join(JpxStockInfo, IxHeadTitle.securities_code == JpxStockInfo.code)
        .where(IxHeadTitle.securities_code != None)
        .order_by(IxHeadTitle.id)
    )
    if report_types:
        statement = statement.where(
            IxHeadTitle.report_type.in_(report_types),
            IxHeadTitle.current_period != None,
        )
    if convert_date:
        statement = statement.where(IxHeadTitle.reporting_date == convert_date)
    if industry_17_code:
        statement = statement.where(
            JpxStockInfo.industry_17_code == industry_17_code,
            IxHeadTitle.securities_code != None,
        )
    results = session.exec(statement)
    items = results.all()

    count = len(items)

    if limit and page:
        items = items[(page - 1) * limit : page * limit]

    if limit:
        items = items[:limit]

    schemas = []
    report_type = {
        "edjp": "決算短信(日本基準)",
        "edus": "決算短信(米国基準)",
        "edif": "決算短信(IFRS)",
    }
    period = {
        "Q1": "第1四半期",
        "Q2": "第2四半期",
        "Q3": "第3四半期",
        "HY": "中間",
        "FY": "通期",
    }
    period_index = {
        "Q1": 0,
        "Q2": 1,
        "Q3": 2,
        "HY": 2,
        "FY": 3,
    }
    for item in items:
        try:
            document_short_name = f"{item.reporting_date.year}年{period[item.current_period]} {report_type[item.report_type]}"
        except KeyError:
            document_short_name = item.document_name
        schema = sc.DocumentListPublic(
            id=item.id,
            head_item_key=item.item_key,
            insert_date=item.insert_date,
            securities_code=item.securities_code,
            company_name=item.company_name,
            document_name=item.document_name,
            document_short_name=document_short_name,
            report_type=item.report_type,
            url=item.url,
            current_period=item.current_period,
            period_index=(
                period_index[item.current_period]
                if item.current_period in period_index
                else None
            ),
            report_date=item.reporting_date,
        )
        schemas.append(schema)

    return sc.DocumentListPublics(
        count=count,
        data=schemas,
    )
