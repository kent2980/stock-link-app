import re
from datetime import date
from typing import Optional

from fastapi import APIRouter, HTTPException, Query
from sqlmodel import select

from app.api.deps import SessionDep
from app.models import IxHeadTitle

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
    date_str: Optional[str] = Query(None),
    limit: Optional[int] = Query(None),
    page: Optional[int] = Query(1),
) -> sc.DocumentListPublics:

    if date_str and not re.match(r"^\d{4}-\d{2}-\d{2}$", date_str):
        raise HTTPException(
            status_code=400,
            detail="日付の形式が正しくありません。YYYY-MM-DD形式で指定してください。",
        )

    convert_date = date.fromisoformat(date_str) if date_str else None

    statement = (
        select(IxHeadTitle)
        .where(IxHeadTitle.securities_code != None)
        .order_by(IxHeadTitle.id)
    )
    if convert_date:
        statement = statement.where(IxHeadTitle.reporting_date == convert_date)
    results = session.exec(statement)
    items = results.all()

    count = len(items)

    if limit and page:
        items = items[(page - 1) * limit : page * limit]

    if limit:
        items = items[:limit]

    return sc.DocumentListPublics(
        count=count,
        data=items,
    )
