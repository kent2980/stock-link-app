from typing import Any, List, Optional

from fastapi import APIRouter, HTTPException, Path, Query
from sqlmodel import select

from app.api.deps import SessionDep
from app.models import JpxStockInfo

from . import crud
from . import schema as sc

router = APIRouter()


@router.post("/", response_model=sc.JpxStockInfoCreate, include_in_schema=False)
def create_jpx_stock_info_item(
    *, item_in: sc.JpxStockInfoCreate, session: SessionDep
) -> JpxStockInfo:
    """
    Create new item.
    """
    item = crud.create_jpx_stock_info_item(item_in=item_in, session=session)

    return item


@router.post(
    "/list/",
    response_model=sc.JpxStockInfosCreateList,
    include_in_schema=False,
)
def create_jpx_stock_info_items_exists(
    *, items_in: sc.JpxStockInfosCreateList, session: SessionDep
) -> List[JpxStockInfo]:
    """
    Create new items.(Insert Select ... Not Exists)
    """

    items = crud.create_jpx_stock_info_items_exists(items_in=items_in, session=session)

    return items


@router.get("/code/{code}", response_model=sc.JpxStockInfoPublic)
def read_jpx_stock_info_item(*, code: str, session: SessionDep) -> JpxStockInfo:
    """
    Get item by code.
    """
    item = crud.read_jpx_stock_info_item(code=code, session=session)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.get("/", response_model=sc.JpxStockInfosPublicList)
def read_jpx_stock_info_items(*, session: SessionDep) -> sc.JpxStockInfosPublicList:
    """
    Get all items.
    """

    items = crud.read_jpx_stock_info_items(session=session)

    return items


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

    items = crud.read_jpx_stock_info_items_tcs(
        industry_17_code=industry_17_code,
        industry_33_code=industry_33_code,
        isItems=isItems,
        session=session,
        limit=limit,
    )

    return items


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

    items = crud.read_jpx_stock_info_item_tcs(market=market, session=session)

    if len(items) == 0:
        raise HTTPException(status_code=404, detail="Item not found")

    return sc.JpxStockInfosPublicList(data=items, count=len(items))


@router.get("/industries/{type}", response_model=sc.IndustriesList)
def read_jpx_stock_info_industry_names(
    *, type: int, session: SessionDep
) -> sc.IndustriesList:
    """
    Get all industries.
    """

    items = crud.read_jpx_stock_info_industry_names(type=type, session=session)

    return items


@router.get(
    "/industries",
    response_model=sc.IndustriesList,
)
def read_select_industries(
    *, industry_17_code: Optional[int] = Query(None), session: SessionDep
) -> sc.IndustriesList:
    """
    Get all industries.
    """

    items = crud.read_select_industries(
        industry_17_code=industry_17_code, session=session
    )

    return items


@router.get("/industry_17_list/", response_model=sc.industry_17_count_list)
def read_industry_17_count(
    *,
    session: SessionDep,
) -> sc.industry_17_count_list:
    """
    Get industry_17_list.
    """

    items = crud.read_industry_17_count(session=session)

    if len(items.data) == 0:
        raise HTTPException(status_code=404, detail="Items not found")

    return items
