from sqlalchemy import func
from sqlmodel import Session, select

from app.models import JpxStockInfo

from . import schema as sc


def create_jpx_stock_info_item(
    *, item_in: sc.JpxStockInfoCreate, session: Session
) -> JpxStockInfo:
    """
    Create new item.
    """
    item = JpxStockInfo.model_validate(item_in)
    session.add(item)
    session.commit()
    session.refresh(item)

    return item


def create_jpx_stock_info_items_exists(
    *, items_in: sc.JpxStockInfosCreateList, session: Session
) -> list[JpxStockInfo]:
    """
    Create new items.(Insert Select ... Not Exists)
    """

    new_items = [JpxStockInfo.model_validate(item) for item in items_in.data]

    try:
        session.bulk_save_objects(new_items)
        session.commit()
    except Exception:
        session.rollback()
        new_items = []
        for item in items_in.data:
            new_item = JpxStockInfo.model_validate(item)
            session.add(new_item)
            session.commit()
            session.refresh(new_item)
            new_items.append(new_item)

    return new_items


def read_jpx_stock_info_item(*, code: str, session: Session) -> JpxStockInfo | None:
    """
    Get item by code.
    """
    statement = select(JpxStockInfo).where(JpxStockInfo.code == code)
    result = session.exec(statement)
    item = result.first()

    return item


def read_jpx_stock_info_items(*, session: Session) -> sc.JpxStockInfosPublicList:
    """
    Get all items.
    """
    statement = select(JpxStockInfo)
    result = session.exec(statement)
    items = result.all()
    return sc.JpxStockInfosPublicList(data=items, count=len(items))


def read_jpx_stock_info_items_tcs(
    *,
    industry_17_code: int | None,
    industry_33_code: list[int] | None,
    isItems: bool = True,
    session: Session,
    limit: int = 100,
) -> sc.JpxStockInfosPublicList:
    """
    Get all items.
    """
    if isItems is False:
        return sc.JpxStockInfosPublicList(data=[], count=0)
    statement = (
        select(JpxStockInfo)
        .where(
            JpxStockInfo.market_or_type.like("%内国株式%"),
        )
        .order_by(JpxStockInfo.code)
    )
    if industry_17_code:
        statement = statement.where(JpxStockInfo.industry_17_code == industry_17_code)
    if industry_33_code:
        statement = statement.where(JpxStockInfo.industry_33_code.in_(industry_33_code))
    if limit:
        statement = statement.limit(limit)
    result = session.exec(statement)
    items = result.all()
    return sc.JpxStockInfosPublicList(data=items, count=len(items))


def read_jpx_stock_info_item_tcs(
    *, market: str, session: Session
) -> list[JpxStockInfo]:
    """
    Get item by market.
    """

    market_dict = {"pr": "プライム", "gh": "グロース", "st": "スタンダード"}
    statement = (
        select(JpxStockInfo)
        .where(JpxStockInfo.market_or_type.like(f"%{market_dict[market]}%"))
        .order_by(JpxStockInfo.code)
    )
    result = session.exec(statement)
    items = result.all()

    return items


def read_jpx_stock_info_industry_names(
    *, type: int, session: Session
) -> sc.IndustriesList:
    """
    Get all industries.
    """

    if type == 17:
        statement = (
            select(
                JpxStockInfo.industry_17_name.label("name"),
                JpxStockInfo.industry_17_code.label("code"),
            )
            .where(
                JpxStockInfo.industry_17_name.is_not(None),
                JpxStockInfo.industry_17_code.is_not(None),
            )
            .order_by(JpxStockInfo.industry_17_code)
            .distinct()
        )
    elif type == 33:
        statement = (
            select(
                JpxStockInfo.industry_33_name.label("name"),
                JpxStockInfo.industry_33_code.label("code"),
            )
            .where(
                JpxStockInfo.industry_33_name.is_not(None),
                JpxStockInfo.industry_33_code.is_not(None),
            )
            .order_by(JpxStockInfo.industry_33_code)
            .distinct()
        )
    result = session.exec(statement)
    items = result.all()
    # itemsの要素からNoneを除外
    items = [item for item in items if item[0] is not None]
    items = [item for item in items if item[1] is not None]
    return sc.IndustriesList(data=items)


def read_select_industries(
    *, industry_17_code: int | None, session: Session
) -> sc.IndustriesList:
    """
    Get all industries.
    """
    statement = (
        select(
            JpxStockInfo.industry_33_name.label("name"),
            JpxStockInfo.industry_33_code.label("code"),
        )
        .order_by(JpxStockInfo.industry_33_code)
        .distinct()
    )
    if industry_17_code:
        statement = statement.where(
            JpxStockInfo.industry_17_code == industry_17_code,
            JpxStockInfo.industry_33_code.is_not(None),
        )
    result = session.exec(statement)
    items = result.all()
    # itemsの要素からNoneを除外
    items = [item for item in items if item[0] is not None]
    items = [item for item in items if item[1] is not None]
    return sc.IndustriesList(data=items)


def read_industry_count(*, session: Session, type: int) -> sc.industry_count_list:
    """
    Get all industries.
    """

    if type not in [17, 33]:
        raise ValueError("type must be 17 or 33")

    if type == 17:
        statement = (
            select(
                JpxStockInfo.industry_17_name.label("name"),
                JpxStockInfo.industry_17_code.label("code"),
                func.count(JpxStockInfo.code).label("count"),
            )
            .where(
                JpxStockInfo.industry_17_name.is_not(None),
                JpxStockInfo.industry_17_code.is_not(None),
            )
            .group_by(
                JpxStockInfo.industry_17_name,
                JpxStockInfo.industry_17_code,
            )
            .order_by(JpxStockInfo.industry_17_code)
        )
    elif type == 33:
        statement = (
            select(
                JpxStockInfo.industry_33_name.label("name"),
                JpxStockInfo.industry_33_code.label("code"),
                func.count(JpxStockInfo.code).label("count"),
            )
            .where(
                JpxStockInfo.industry_33_name.is_not(None),
                JpxStockInfo.industry_33_code.is_not(None),
            )
            .group_by(
                JpxStockInfo.industry_33_name,
                JpxStockInfo.industry_33_code,
            )
            .order_by(JpxStockInfo.industry_33_code)
        )
    result = session.exec(statement)
    items = result.all()

    return sc.industry_count_list(data=items)


def read_industry_name(
    *,
    type: int,
    code: int,
    session: Session,
) -> str:
    if type not in [17, 33]:
        raise ValueError("type must be 17 or 33")
    if type == 17:
        statement = (
            select(JpxStockInfo.industry_17_name)
            .where(
                JpxStockInfo.industry_17_code == code,
                JpxStockInfo.industry_17_name.is_not(None),
            )
            .order_by(JpxStockInfo.industry_17_code)
        )
    elif type == 33:
        statement = (
            select(JpxStockInfo.industry_33_name)
            .where(
                JpxStockInfo.industry_33_code == code,
                JpxStockInfo.industry_33_name.is_not(None),
            )
            .order_by(JpxStockInfo.industry_33_code)
        )
    result = session.exec(statement)
    item = result.first()
    if item is None:
        raise ValueError("item not found")
    return item
