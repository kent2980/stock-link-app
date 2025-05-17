import re
from datetime import date
from typing import List, Optional

from fastapi import APIRouter, HTTPException, Query
from sqlmodel import desc, func, select

from app.api.deps import SessionDep
from app.models import IxHeadTitle, JpxStockInfo

from . import crud
from . import schema as sc

router = APIRouter()


@router.get(
    "/document/count", summary="条件を指定してXBRL文書数を取得", response_model=int
)
def get_document_count(
    *,
    session: SessionDep,
    date_str: Optional[str] = Query(None),
    report_types: Optional[List[str]] = Query(None),
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
    if report_types:
        statement = statement.where(
            IxHeadTitle.report_type.in_(report_types),
            IxHeadTitle.current_period != None,
        )
    results = session.exec(statement)
    items = results.all()
    count = len(items)

    return count


@router.get(
    "/document/latest/title",
    summary="最も新しいXBRL文書のタイトルを取得",
    response_model=str,
)
def get_latest_document_title(*, session: SessionDep) -> str:

    statement = select(IxHeadTitle).order_by(desc(IxHeadTitle.insert_date))
    results = session.exec(statement)
    item = results.first()
    latest_title = f"{item.securities_code} {item.company_name} {item.document_name}"

    return latest_title


@router.get(
    "/ix/head/",
    response_model=sc.DocumentListPublic,
    summary="指定したIDのXBRL文書の詳細を取得",
)
def read_ix_head_title_item(
    *, session: SessionDep, head_item_key: str = Query(...)
) -> IxHeadTitle:
    """
    Get item by head_item_key.
    """
    item = crud.read_ix_head_title_item(session=session, head_item_key=head_item_key)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return sc.DocumentListPublic(
        id=item.id,
        head_item_key=item.item_key,
        insert_date=item.insert_date,
        securities_code=item.securities_code,
        company_name=item.company_name,
        document_name=item.document_name,
        report_type=item.report_type,
        url=item.url,
        current_period=item.current_period,
        report_date=item.reporting_date,
    )


@router.get(
    "/document/list",
    summary="条件抽出したXBRL文書のリストを取得",
    response_model=sc.DocumentListPublics,
)
def get_document_list(
    *,
    session: SessionDep,
    report_types: Optional[List[str]] = Query(None),
    date_str: Optional[str] = Query(None),
    industry_17_code: Optional[int] = Query(None),
    industry_33_code: Optional[int] = Query(None),
) -> sc.DocumentListPublics:

    if date_str and not re.match(r"^\d{4}-\d{2}-\d{2}$", date_str):
        raise HTTPException(
            status_code=400,
            detail="日付の形式が正しくありません。YYYY-MM-DD形式で指定してください。",
        )
    convert_date = None
    if date_str:
        convert_date = date.fromisoformat(date_str) if date_str else None

    statement = (
        select(IxHeadTitle)
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
    if industry_33_code:
        statement = statement.where(
            JpxStockInfo.industry_33_code == industry_33_code,
            IxHeadTitle.securities_code != None,
        )
    results = session.exec(statement)
    items = results.all()

    count = len(items)

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


@router.get(
    "/url_list/", response_model=sc.UrlSchemaList, summary="企業URLのリストを取得"
)
def read_ix_head_title_items_url_list(
    *,
    session: SessionDep,
) -> sc.UrlSchemaList:
    """
    Get items.
    """
    statement = (
        select(IxHeadTitle.securities_code, IxHeadTitle.url)
        .where(IxHeadTitle.url is not None, IxHeadTitle.securities_code is not None)
        .order_by(IxHeadTitle.securities_code.asc())
        .distinct(IxHeadTitle.securities_code)
    )
    results = session.exec(statement)
    items = results.all()

    if not items:
        raise HTTPException(status_code=404, detail="Items not found")

    url_list = []
    for item in items:
        if item.securities_code and item.url:
            url_list.append(
                sc.UrlSchema(securities_code=item.securities_code, url=item.url)
            )
    return sc.UrlSchemaList(data=url_list, count=len(url_list))


@router.get(
    "/calendar", summary="XBRLカレンダーを取得", response_model=sc.PublicCalenders
)
def get_calendar(*, session: SessionDep) -> sc.PublicCalenders:

    statement = (
        select(
            IxHeadTitle.reporting_date,
            func.count(IxHeadTitle.reporting_date).label("count"),
        )
        .where(IxHeadTitle.securities_code != None)
        .group_by(IxHeadTitle.reporting_date)
        .order_by(desc(IxHeadTitle.reporting_date))
    )
    results = session.exec(statement)
    items = results.all()
    print(statement)
    return sc.PublicCalenders(
        count=len(items),
        data=[
            sc.PublicCalender(
                reporting_date=item[0],
                count=item[1],
            )
            for item in items
        ],
    )


@router.get(
    "/latest_reporting_date",
    response_model=sc.PublicLatestReportingDate,
    summary="最新の報告日を取得",
)
def get_latest_reporting_date(*, session: SessionDep) -> sc.PublicLatestReportingDate:
    """
    Get latest reporting date.
    """

    statement = (
        select(
            IxHeadTitle.reporting_date,
            func.count(IxHeadTitle.reporting_date).label("count"),
        )
        .where(IxHeadTitle.reporting_date != None)
        .order_by(desc(IxHeadTitle.reporting_date))
        .group_by(IxHeadTitle.reporting_date)
    )
    results = session.exec(statement)
    item = results.first()

    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    return sc.PublicLatestReportingDate(
        reporting_date=item[0],
        count=item[1],
    )
