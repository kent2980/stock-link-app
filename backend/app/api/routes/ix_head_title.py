import datetime
import re
from decimal import Decimal
from typing import Any, List, Optional

import app.schema as sc
from app.api.deps import SessionDep

# from app.extract import (
#     ix_non_fraction_edif,
#     ix_non_fraction_edjp,
#     ix_non_fraction_edus,
#     ix_non_numeric_edif,
#     ix_non_numeric_edjp,
#     ix_non_numeric_edus,
# )
from app.models import IxHeadTitle, IxNonFraction, IxNonNumeric
from fastapi import APIRouter, HTTPException, Query
from sqlalchemy.exc import IntegrityError
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
    statement = select(IxHeadTitle).where(IxHeadTitle.item_key == item_in.item_key)
    result = session.exec(statement)
    item_exists = result.first()

    if not item_exists:
        new_item = IxHeadTitle.model_validate(item_in)
        session.add(new_item)
        session.commit()
        session.refresh(new_item)
        return f"Item {new_item.name} created"

    return f"Item {item_in.name} already exists for head_item_key {item_in.item_key}"


@router.post("/ix/head/list/", response_model=str)
def create_ix_head_title_items_exists(
    *, session: SessionDep, items_in: sc.ix_head.IxHeadTitleCreateList
) -> Any:
    """
    Create new items.(Insert Select ... Not Exists)
    """
    new_items = [IxHeadTitle.model_validate(item) for item in items_in.data]

    try:
        session.bulk_save_objects(new_items)
        session.commit()
    except IntegrityError:
        session.rollback()
        # 一意制約違反の場合は、既存のデータを更新する
        new_items = []
        for item in items_in.data:
            new_item = IxHeadTitle.model_validate(item)
            session.add(new_item)
            try:
                session.commit()
                session.refresh(new_item)
                new_items.append(new_item)
            except IntegrityError:
                session.rollback()  # コミット失敗時にロールバック

    return f"{len(new_items)} items created."


@router.get("/ix/head/is/{head_item_key}/", response_model=bool)
def is_ix_head_title_item_exists(*, session: SessionDep, head_item_key: str) -> Any:
    """
    Check if item exists.
    """
    statement = select(IxHeadTitle).where(
        IxHeadTitle.item_key == head_item_key, IxHeadTitle.is_active == True
    )
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
        .where(IxHeadTitle.reporting_date == date, IxHeadTitle.is_active == True)
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
        .where(IxHeadTitle.reporting_date == date, IxHeadTitle.is_active == True)
        .order_by(IxHeadTitle.securities_code)
    )
    result = session.exec(statement)
    items = result.all()

    return sc.ix_head.IxHeadTitlesPublic(data=items, count=len(items))


@router.delete("/ix/head/delete/", response_model=bool)
def delete_ix_head_title_item(
    *, session: SessionDep, head_item_key: str = Query(...)
) -> Any:
    """
    Delete item.
    """
    statement = select(IxHeadTitle).where(IxHeadTitle.item_key == head_item_key)
    result = session.exec(statement)
    item = result.first()

    if item is None:
        return False

    try:
        session.delete(item)
        session.commit()
    except Exception:
        raise HTTPException(status_code=400, detail="削除に失敗しました")

    return True


@router.put("/ix/head/active/", response_model=bool)
def active_ix_head_title_item(
    *, session: SessionDep, head_item_key: str = Query(...)
) -> Any:
    """
    Active item.
    """
    statement = select(IxHeadTitle).where(IxHeadTitle.item_key == head_item_key)
    result = session.exec(statement)
    item = result.first()

    if item is None:
        return False

    item.is_active = True
    session.add(item)
    session.commit()

    return True


@router.get("/ix/head/is_active/", response_model=bool)
def is_ix_head_title_item_active(*, session: SessionDep, head_item_key: str) -> Any:
    """
    Check if item is active.
    """
    statement = select(IxHeadTitle).where(IxHeadTitle.item_key == head_item_key)
    result = session.exec(statement)
    item = result.first()

    if item:
        if item.is_active:
            return True

    return False


# @router.put("/ix/head/generate/")
# def ix_head_generate(
#     *, session: SessionDep, head_item_key: Optional[str] = Query(None)
# ) -> Any:
#     """
#     Extraction item.
#     """
#     if head_item_key is None:
#         statement = select(IxHeadTitle).where(
#             IxHeadTitle.is_active == True, IxHeadTitle.is_generated == False
#         )
#     else:
#         statement = select(IxHeadTitle).where(
#             IxHeadTitle.is_active == True,
#             IxHeadTitle.is_generated == False,
#             IxHeadTitle.item_key == head_item_key,
#         )

#     result = session.exec(statement)
#     items = result.all()

#     for item in items:
#         period = item.current_period
#         report_type = item.report_type
#         document_name = item.document_name
#         consolidated = (
#             "_NonConsolidated" if "非連結" in document_name else "_Consolidated"
#         )
#         if not report_type in ["edjp", "edif", "edus"]:
#             continue
#         result_regex = f"(?=.*Current)(?=.*\{consolidated}.*)(?=Result.*)"
#         if period == "FY":
#             forecast_regex = f"(?=.*Next)(?=.*\{consolidated}.*)(?=Forecast.*)"
#         else:
#             forecast_regex = f"(?=.*Current)(?=.*\{consolidated}.*)(?=Forecast.*)"

#         ord_income = None
#         try:
#             if report_type == "edjp":
#                 try:
#                     ord_income = ix_non_fraction_edjp.ordinary_income(
#                         session, item.item_key, result_regex
#                     )
#                 except ValueError:
#                     try:
#                         ord_income = ix_non_fraction_edjp.ordinary_revenues_bk(
#                             session, item.item_key, result_regex
#                         )
#                     except ValueError:
#                         ord_income = ix_non_fraction_edjp.ordinary_revenues_in(
#                             session, item.item_key, result_regex
#                         )
#             elif report_type == "edif":
#                 ord_income = ix_non_fraction_edif.profit_before_tax_ifrs(
#                     session, item.item_key, result_regex
#                 )
#             elif report_type == "edus":
#                 ord_income = ix_non_fraction_edus.income_before_income_taxes_us(
#                     session, item.item_key, result_regex
#                 )
#         except ValueError:
#             ord_income = None

#         return ord_income
