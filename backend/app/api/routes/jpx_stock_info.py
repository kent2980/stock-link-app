import re
from typing import Any

from fastapi import APIRouter, HTTPException, Path
from sqlmodel import select

import app.schema as sc
from app.api.deps import SessionDep
from app.models import JpxStockInfo

router = APIRouter()


@router.post("/", response_model=sc.jpx_stock_info.JpxStockInfoCreate)
def create_jpx_stock_info_item(
    *, item_in: sc.jpx_stock_info.JpxStockInfoCreate, session: SessionDep
) -> Any:
    """
    Create new item.
    """
    item = JpxStockInfo.model_validate(item_in)
    session.add(item)
    session.commit()
    session.refresh(item)

    return item


@router.post("/list/", response_model=sc.jpx_stock_info.JpxStockInfosCreateList)
def create_jpx_stock_info_items_exists(
    *, items_in: sc.jpx_stock_info.JpxStockInfosCreateList, session: SessionDep
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


@router.get("/code/{code}", response_model=sc.jpx_stock_info.JpxStockInfoPublic)
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


@router.get("/", response_model=sc.jpx_stock_info.JpxStockInfosPublicList)
def read_jpx_stock_info_items(
    *, session: SessionDep
) -> sc.jpx_stock_info.JpxStockInfosPublicList:
    """
    Get all items.
    """
    statement = select(JpxStockInfo)
    result = session.exec(statement)
    items = result.all()
    return sc.jpx_stock_info.JpxStockInfosPublicList(data=items, count=len(items))


@router.get("/tcs", response_model=sc.jpx_stock_info.JpxStockInfosPublicList)
def read_jpx_stock_info_items_tcs(
    *, session: SessionDep
) -> sc.jpx_stock_info.JpxStockInfosPublicList:
    """
    Get all items.
    """
    print("tcs")
    statement = (
        select(JpxStockInfo)
        .where(JpxStockInfo.market_or_type.like("%内国株式%"))
        .order_by(JpxStockInfo.code)
    )
    result = session.exec(statement)
    items = result.all()
    return sc.jpx_stock_info.JpxStockInfosPublicList(data=items, count=len(items))


@router.get("/tcs/{market}", response_model=sc.jpx_stock_info.JpxStockInfosPublicList)
def read_jpx_stock_info_item_tcs(
    *, market: str, session: SessionDep
) -> sc.jpx_stock_info.JpxStockInfosPublicList:
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
    return sc.jpx_stock_info.JpxStockInfosPublicList(data=item, count=len(item))
