from typing import Any, List, Optional

from fastapi import APIRouter, HTTPException, Path, Query
from sqlmodel import select

from app.api.deps import SessionDep
from app.models import JpxStockInfo

from . import schema as sc

router = APIRouter()


@router.post("/", response_model=sc.JpxStockInfoCreate, include_in_schema=False)
def create_jpx_stock_info_item(
    *, item_in: sc.JpxStockInfoCreate, session: SessionDep
) -> Any:
    """
    Create new item.
    """
    item = JpxStockInfo.model_validate(item_in)
    session.add(item)
    session.commit()
    session.refresh(item)

    return item


@router.post(
    "/list/",
    response_model=sc.JpxStockInfosCreateList,
    include_in_schema=False,
)
def create_jpx_stock_info_items_exists(
    *, items_in: sc.JpxStockInfosCreateList, session: SessionDep
) -> Any:
    """
    Create new items.(Insert Select ... Not Exists)
    """

    print("add list start")

    new_items = [JpxStockInfo.model_validate(item) for item in items_in.data]

    print("item add")

    try:
        session.bulk_save_objects(new_items)
        session.commit()
    except Exception as e:
        session.rollback()
        new_items = []
        for item in items_in.data:
            new_item = JpxStockInfo.model_validate(item)
            session.add(new_item)
            session.commit()
            session.refresh(new_item)
            new_items.append(new_item)

    return new_items


@router.get("/code/{code}", response_model=sc.JpxStockInfoPublic)
def read_jpx_stock_info_item(*, code: str, session: SessionDep) -> Any:
    """
    Get item by code.
    """
    statement = select(JpxStockInfo).where(JpxStockInfo.code == code)
    result = session.exec(statement)
    item = result.first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.get("/", response_model=sc.JpxStockInfosPublicList)
def read_jpx_stock_info_items(*, session: SessionDep) -> sc.JpxStockInfosPublicList:
    """
    Get all items.
    """
    statement = select(JpxStockInfo)
    result = session.exec(statement)
    items = result.all()
    return sc.JpxStockInfosPublicList(data=items, count=len(items))


@router.get("/tcs", response_model=sc.JpxStockInfosPublicList)
def read_jpx_stock_info_items_tcs(
    *,
    industry_17_code: Optional[int] = Query(None),
    industry_33_code: Optional[List[int]] = Query(None),
    isItems: bool = Query(True),
    session: SessionDep,
    limit: int = Query(100),
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


@router.get("/tcs/{market}", response_model=sc.JpxStockInfosPublicList)
def read_jpx_stock_info_item_tcs(
    *, market: str, session: SessionDep
) -> sc.JpxStockInfosPublicList:
    """
    Get item by market.
    """
    if market not in ["pr", "gh", "st"]:
        raise HTTPException(
            status_code=404, detail="market is valid, select [pr, gh, st]"
        )
    market_dict = {"pr": "プライム", "gh": "グロース", "st": "スタンダード"}
    statement = (
        select(JpxStockInfo)
        .where(JpxStockInfo.market_or_type.like(f"%{market_dict[market]}%"))
        .order_by(JpxStockInfo.code)
    )
    result = session.exec(statement)
    item = result.all()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return sc.JpxStockInfosPublicList(data=item, count=len(item))


@router.get("/industries/{type}", response_model=sc.IndustriesList)
def read_jpx_stock_info_industry_names(*, type: int, session: SessionDep) -> Any:
    """
    Get all industries.
    """
    if type not in [17, 33]:
        raise HTTPException(
            status_code=404, detail="industry type is valid, select [17, 33]"
        )
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


@router.get(
    "/industries",
    response_model=sc.IndustriesList,
)
def read_select_industries(
    *, industry_17_code: Optional[int] = Query(None), session: SessionDep
) -> Any:
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
