import datetime
import re
from decimal import Decimal
from typing import Any, List, Optional

from fastapi import APIRouter, HTTPException, Query
from sqlalchemy.exc import IntegrityError
from sqlmodel import func, select, update

import app.schema as sc
from app.api.deps import SessionDep
from app.models import IxHeadTitle, IxNonFraction, IxNonNumeric

router = APIRouter()


@router.post(
    "/ix/head/", response_model=sc.ix_head.IxHeadTitlePublic, include_in_schema=False
)
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


@router.post("/ix/head/exist/", response_model=str, include_in_schema=False)
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


@router.post("/ix/head/list/", response_model=str, include_in_schema=False)
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
    "/head/select/date/",
    response_model=sc.ix_head.IxHeadTitlesPublic,
)
def select_ix_head_title_items(
    *, session: SessionDep, date_str: str
) -> sc.ix_head.IxHeadTitlesPublic:
    """
    指定した日付の報告書を取得します。
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


@router.delete("/ix/head/delete/", response_model=bool, include_in_schema=False)
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


@router.patch("/ix/head/active/", response_model=bool, include_in_schema=False)
def update_is_active_ix_head_title_item(
    *, session: SessionDep, head_item_key: str = Query(...)
) -> Any:
    """
    Active item.
    """
    statement = select(IxHeadTitle).where(IxHeadTitle.item_key == head_item_key)
    result = session.exec(statement)
    item = result.first()

    is_active = True

    if item is None:
        is_active = False

    if item.report_type.startswith("ed"):
        if item.current_period is None:
            is_active = False

    item.is_active = is_active
    session.add(item)
    session.commit()

    return is_active


@router.patch("/ix/head/generate/", response_model=bool, include_in_schema=False)
def active_is_generate(*, session: SessionDep, head_item_key: str = Query(...)) -> Any:
    """
    Generate item.
    """
    statement = select(IxHeadTitle).where(IxHeadTitle.item_key == head_item_key)
    result = session.exec(statement)
    item = result.first()

    if item is None:
        return False

    item.is_generate = True
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


@router.patch("/upgrade/is_consolidated/", response_model=str, include_in_schema=False)
def update_is_consolidated(*, session: SessionDep) -> str:
    """
    Upgrade is_consolidated.
    """
    name = "jpdei_cor_WhetherConsolidatedFinancialStatementsArePreparedDEI"
    statement = (
        select(IxHeadTitle.id, IxNonNumeric.head_item_key, IxNonNumeric.value)
        .join(IxHeadTitle, IxNonNumeric.head_item_key == IxHeadTitle.item_key)
        .where(IxNonNumeric.name == name, IxHeadTitle.is_consolidated == None)
    )
    result = session.exec(statement)
    items = result.all()

    update_data = []
    for item in items:
        is_value = item.value == "true"
        update_data.append(
            {"id": item.id, "item_key": item.head_item_key, "is_consolidated": is_value}
        )

    if update_data:
        session.bulk_update_mappings(IxHeadTitle, update_data)
        session.commit()

    if len(items) == 0:
        return "No items to update."
    else:
        return f"{len(items)} items updated."


@router.get("/select/head_item_key/", response_model=sc.ix_head.IxHeadTitlePublic)
def select_ix_head_title_item(
    *, session: SessionDep, head_item_key: str
) -> sc.ix_head.IxHeadTitlePublic:
    """
    Select item.
    """
    statement = select(IxHeadTitle).where(IxHeadTitle.item_key == head_item_key)
    result = session.exec(statement)
    item = result.first()

    return item


@router.patch("/ix/head/update/", response_model=str, include_in_schema=False)
def update_ix_head_title_item(
    *,
    session: SessionDep,
    head_item_key: Optional[str] = None,
    date_str: Optional[str] = None,
) -> Any:
    """
    Update item.
    """

    def update_change_in_items(
        session: SessionDep,
        head_item_key: Optional[str] = None,
        date_str: Optional[str] = None,
    ) -> Any:
        """
        経営実績の増減率を更新する。
        """
        statement = select(IxNonFraction).where(
            IxNonFraction.name.like("tse-ed-t_ChangeIn%"),
        )
        if head_item_key:
            statement = statement.where(IxNonFraction.head_item_key == head_item_key)
        if date_str:
            date_value = datetime.datetime.strptime(date_str, "%Y%m%d")
            statement = statement.join(IxHeadTitle).where(
                IxHeadTitle.reporting_date == date_value.date()
            )
        result = session.exec(statement)
        items = result.all()

        head_item_keys = [item.head_item_key for item in items]
        head_item_keys = list(set(head_item_keys))
        for item in items:
            head_item_key = item.head_item_key
            name = item.name
            context = item.context
            numeric = item.numeric

            if numeric is None:
                continue

            statement = select(IxHeadTitle).where(IxHeadTitle.item_key == head_item_key)
            result = session.exec(statement)
            head_item = result.first()

            if numeric:
                value = float(numeric)
            if head_item.is_consolidated:
                if re.search(r"NonConsolidated", item.context):
                    continue

            update_fields = {
                "tse-ed-t_ChangeInNetSales": {
                    "result": "change_in_net_sales",
                    "forecast": "change_in_fore_net_sales",
                },  # 売上高増減率
                "tse-ed-t_ChangeInOrdinaryRevenue": {
                    "result": "change_in_net_sales",
                    "forecast": "change_in_fore_net_sales",
                },  # 経常収益増減率
                "tse-ed-t_ChangeInSales": {
                    "result": "change_in_net_sales",
                    "forecast": "change_in_fore_net_sales",
                },  # 売上収益増減率
                "tse-ed-t_ChangeInRevenue": {
                    "result": "change_in_net_sales",
                    "forecast": "change_in_fore_net_sales",
                },  # 収益増減率
                "tse-ed-t_ChangeInOperatingRevenues": {
                    "result": "change_in_net_sales",
                    "forecast": "change_in_fore_net_sales",
                },  # 営業収益増減率
                "tse-ed-t_ChangeInOrdinaryIncome": {
                    "result": "change_in_ordinary_income",
                    "forecast": "change_in_fore_ordinary_income",
                },  # 経常利益増減率
                "tse-ed-t_ChangeInProfitBeforeTax": {
                    "result": "change_in_net_income",
                    "forecast": "change_in_fore_net_income",
                },  # 税引前利益増減率
                "tse-ed-t_ChangeInProfitAttributableToOwnersOfParent": {
                    "result": "change_in_net_income",
                    "forecast": "change_in_fore_net_income",
                },  # 当期純利益増減率
            }

            for prefix, fields in update_fields.items():
                if name.startswith(prefix):
                    if re.search(r"(?=.*Current)(?=.*Result)", context):
                        statement = (
                            update(IxHeadTitle)
                            .where(IxHeadTitle.item_key == head_item_key)
                            .values({fields["result"]: value})
                        )
                    elif re.search(r"(?=.*Forecast)(?=.*Year)", context):
                        statement = (
                            update(IxHeadTitle)
                            .where(IxHeadTitle.item_key == head_item_key)
                            .values({fields["forecast"]: value})
                        )
                    session.exec(statement)
                    session.commit()
                    break

        return f"{len(head_item_keys)} items updated."

    def update_non_numeric_items(
        session: SessionDep,
        head_item_key: Optional[str] = None,
        date_str: Optional[str] = None,
    ) -> Any:
        """
        非数値情報を更新する。
        """
        statement = select(IxNonNumeric)
        if head_item_key:
            statement = statement.where(
                IxNonNumeric.head_item_key == head_item_key,
                IxNonNumeric.name.like("tse-ed-t_CorrectionOf%"),
            )
        if date_str:
            date_value = datetime.datetime.strptime(date_str, "%Y%m%d")
            statement = statement.join(IxHeadTitle).where(
                IxHeadTitle.reporting_date == date_value.date()
            )
        result = session.exec(statement)
        items = result.all()

        for item in items:
            head_item_key = item.head_item_key
            value = True if item.value == "true" else False

            update_items = {
                r"tse-ed-t_CorrectionOf.*FinancialForecast.*": "is_fcst_rev",
                r"tse-ed-t_CorrectionOfDividendForecast.*": "is_div_rev",
            }

            for prefix, field in update_items.items():
                if re.match(prefix, item.name):
                    statement = (
                        update(IxHeadTitle)
                        .where(IxHeadTitle.item_key == head_item_key)
                        .values({field: value})
                    )
                    session.exec(statement)
                    session.commit()
                    break

        return f"{len(items)} items updated."

    def update_ordinary_income_progress_rate(
        session: SessionDep,
        head_item_key: Optional[str] = None,
        date_str: Optional[str] = None,
    ) -> Any:
        """
        経常利益進捗率を更新する。
        """
        resultStatement = (
            select(IxNonFraction.head_item_key, IxNonFraction.numeric)
            .where(
                IxNonFraction.name == "tse-ed-t_OrdinaryIncome",
                IxNonFraction.context.like("%ResultMember"),
                ~IxNonFraction.context.like("Prior%"),
            )
            .group_by(IxNonFraction.head_item_key, IxNonFraction.numeric)
            .subquery()
        )
        forecastStatement = (
            select(IxNonFraction.head_item_key, IxNonFraction.numeric)
            .where(
                IxNonFraction.name == "tse-ed-t_OrdinaryIncome",
                IxNonFraction.context.like("%ForecastMember"),
                ~IxNonFraction.context.like("Prior%"),
            )
            .group_by(IxNonFraction.head_item_key, IxNonFraction.numeric)
            .subquery()
        )

        statement = (
            select(
                resultStatement.c.head_item_key,
                (
                    func.round(
                        resultStatement.c.numeric / forecastStatement.c.numeric * 100, 1
                    )
                ).label("progress_rate"),
            )
            .select_from(resultStatement)
            .join(
                forecastStatement,
                resultStatement.c.head_item_key == forecastStatement.c.head_item_key,
            )
        )

        if head_item_key:
            statement = statement.where(result.c.head_item_key == head_item_key)
        if date_str:
            date_value = datetime.datetime.strptime(date_str, "%Y%m%d")
            statement = statement.join(IxHeadTitle).where(
                IxHeadTitle.reporting_date == date_value.date()
            )
        result = session.exec(statement)
        items = result.all()

        for item in items:
            head_item_key = item.head_item_key
            progress_rate = item.progress_rate

            statement = (
                update(IxHeadTitle)
                .where(IxHeadTitle.item_key == head_item_key)
                .values({"oi_prog_rt": progress_rate})
            )
            session.exec(statement)
            session.commit()

        return f"{len(items)} items updated."

    # 経営実績の増減率を更新
    result = update_change_in_items(session, head_item_key, date_str)
    # 非数値情報を更新
    result = update_non_numeric_items(session, head_item_key, date_str)
    # 経常利益進捗率を更新
    result = update_ordinary_income_progress_rate(session, head_item_key, date_str)

    return result


@router.get("/document_info/{code}", response_model=sc.ix_head.IxHeadDocumentInfoList)
def get_document_info(
    *, session: SessionDep, code: str
) -> sc.ix_head.IxHeadDocumentInfoList:
    """
    Select item.
    """
    statement = select(IxHeadTitle).where(IxHeadTitle.securities_code == code)
    result = session.exec(statement)
    items = result.all()

    return sc.ix_head.IxHeadDocumentInfoList(data=items, count=len(items))
