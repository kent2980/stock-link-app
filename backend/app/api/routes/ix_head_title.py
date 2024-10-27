import datetime
import re
from typing import Any

import app.schema as sc
from app.api.deps import SessionDep
from app.models import IxHeadTitle
from fastapi import APIRouter, HTTPException
from sqlmodel import func, select

router = APIRouter()


@router.post("/ix/head/", response_model=sc.ix_head.IxHeadTitlePublic)
def create_ix_head_title_item(
    *, session: SessionDep, item_in: sc.ix_head.IxHeadTitleCreate
) -> Any:
    """
    Create new item.
    """
    item = IxHeadTitle.model_validate(item_in)
    session.add(item)
    session.commit()
    session.refresh(item)

    return item


@router.post("/ix/head/exist/", response_model=str)
def create_ix_head_title_item_exists(
    *, session: SessionDep, item_in: sc.ix_head.IxHeadTitleCreate
) -> Any:
    """
    Create new item.
    """
    statement = select(IxHeadTitle).where(IxHeadTitle.xbrl_id == item_in.xbrl_id)
    result = session.exec(statement)
    item_exists = result.first()

    if not item_exists:
        new_item = IxHeadTitle.model_validate(item_in)
        session.add(new_item)
        session.commit()
        session.refresh(new_item)
        return f"Item {new_item.name} created"

    return f"Item {item_in.name} already exists for xbrl_id {item_in.xbrl_id}"


@router.post("/ix/head/list/", response_model=str)
def create_ix_head_title_items_exists(
    *, session: SessionDep, items_in: sc.ix_head.IxHeadTitleCreateList
) -> Any:
    """
    Create new items.(Insert Select ... Not Exists)
    """
    new_items = []
    for item in items_in.data:
        statement = select(IxHeadTitle).where(IxHeadTitle.xbrl_id == item.xbrl_id)
        result = session.exec(statement)
        item_exists = result.first()

        if not item_exists:
            new_item = IxHeadTitle.model_validate(item)
            session.add(new_item)
            new_items.append(new_item)

    if new_items:
        session.commit()
        return f"Items {len(new_items)} created"

    return "Items already exists"


@router.get("/ix/head/is/{xbrl_id}/", response_model=bool)
def is_ix_head_title_item_exists(*, session: SessionDep, xbrl_id: str) -> Any:
    """
    Check if item exists.
    """
    statement = select(IxHeadTitle).where(IxHeadTitle.xbrl_id == xbrl_id)
    result = session.exec(statement)
    item_exists = result.first()

    if item_exists:
        return True

    return False


@router.get(
    "/head/count-report-type/",
    response_model=sc.ix_head.IxReportTypeCountList,
)
def get_count_report_type(
    *, session: SessionDep, date_str: str
) -> sc.ix_head.IxReportTypeCountList:
    """
    指定した日付の報告書タイプごとの件数を取得する。
    """

    # date_strが"YYYY-MM-DD"の形式であることを確認
    if not re.match(r"\d{4}-\d{2}-\d{2}", date_str):
        raise HTTPException(
            status_code=400,
            detail="日付の形式が正しくありません。YYYY-MM-DDの形式で指定してください。",
        )

    # date_strをDate型に変換
    date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    date = date.date()

    statement = (
        select(
            IxHeadTitle.report_type, func.count(IxHeadTitle.report_type).label("count")
        )
        .where(IxHeadTitle.reporting_date == date)
        .group_by(IxHeadTitle.report_type)
    )
    result = session.exec(statement)
    items = result.all()

    items_list = []
    for item in items:
        if item.report_type == "edif":
            items_list.append(
                sc.ix_head.IxReportTypeCount(
                    report_type=item.report_type,
                    report_type_jp="決算短信[国際会計基準]",
                    count=item.count,
                )
            )
        elif item.report_type == "edjp":
            items_list.append(
                sc.ix_head.IxReportTypeCount(
                    report_type=item.report_type,
                    report_type_jp="決算短信[日本基準]",
                    count=item.count,
                )
            )
        elif item.report_type == "edus":
            items_list.append(
                sc.ix_head.IxReportTypeCount(
                    report_type=item.report_type,
                    report_type_jp="決算短信[米国基準]",
                    count=item.count,
                )
            )
        elif item.report_type == "edit":
            items_list.append(
                sc.ix_head.IxReportTypeCount(
                    report_type=item.report_type,
                    report_type_jp="決算短信[国際会計基準]",
                    count=item.count,
                )
            )
        elif item.report_type == "rvfc":
            items_list.append(
                sc.ix_head.IxReportTypeCount(
                    report_type=item.report_type,
                    report_type_jp="業績予想修正に関するお知らせ",
                    count=item.count,
                )
            )
        elif item.report_type == "rvdf":
            items_list.append(
                sc.ix_head.IxReportTypeCount(
                    report_type=item.report_type,
                    report_type_jp="配当予想修正に関するお知らせ",
                    count=item.count,
                )
            )
        elif item.report_type == "rejp":
            items_list.append(
                sc.ix_head.IxReportTypeCount(
                    report_type=item.report_type,
                    report_type_jp="REIT決算短信（日本基準）",
                    count=item.count,
                )
            )
        elif item.report_type == "rrdf":
            items_list.append(
                sc.ix_head.IxReportTypeCount(
                    report_type=item.report_type,
                    report_type_jp="分配予想の修正に関するお知らせ",
                    count=item.count,
                )
            )
        elif item.report_type == "rrfc":
            items_list.append(
                sc.ix_head.IxReportTypeCount(
                    report_type=item.report_type,
                    report_type_jp="運用状況の予想の修正に関するお知らせ",
                    count=item.count,
                )
            )
        elif item.report_type == "efjp":
            items_list.append(
                sc.ix_head.IxReportTypeCount(
                    report_type=item.report_type,
                    report_type_jp="ETF決算短信（日本基準）",
                    count=item.count,
                )
            )

    return sc.ix_head.IxReportTypeCountList(data=items_list, count=len(items_list))


@router.get(
    "/head/select/",
    response_model=sc.ix_head.IxHeadTitlesPublic,
)
def select_ix_head_title_items(
    *, session: SessionDep, date_str: str
) -> sc.ix_head.IxHeadTitlesPublic:
    """
    指定した日付の報告書タイプごとの件数を取得する。
    """

    # date_strが"YYYY-MM-DD"の形式であることを確認
    if not re.match(r"\d{4}-\d{2}-\d{2}", date_str):
        raise HTTPException(
            status_code=400,
            detail="日付の形式が正しくありません。YYYY-MM-DDの形式で指定してください。",
        )

    # date_strをDate型に変換
    date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    date = date.date()

    statement = (
        select(IxHeadTitle)
        .where(IxHeadTitle.reporting_date == date)
        .order_by(IxHeadTitle.securities_code)
    )
    result = session.exec(statement)
    items = result.all()

    return sc.ix_head.IxHeadTitlesPublic(data=items, count=len(items))
