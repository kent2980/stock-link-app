from fastapi import APIRouter, HTTPException, Query

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
) -> list[JpxStockInfo]:
    """
    Create new items.(Insert Select ... Not Exists)
    """

    items = crud.create_jpx_stock_info_items_exists(items_in=items_in, session=session)

    return items


@router.get(
    "/code/{code}",
    response_model=sc.JpxStockInfoPublic,
    summary="コードを指定してマーケット情報を取得",
)
def read_jpx_stock_info_item(*, code: str, session: SessionDep) -> JpxStockInfo:
    """
    Get item by code.
    """
    item = crud.read_jpx_stock_info_item(code=code, session=session)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.get(
    "/",
    response_model=sc.JpxStockInfosPublicList,
    summary="全銘柄のマーケット情報を取得",
)
def read_jpx_stock_info_items(*, session: SessionDep) -> sc.JpxStockInfosPublicList:
    """
    Get all items.
    """

    items = crud.read_jpx_stock_info_items(session=session)

    return items


@router.get(
    "/tcs",
    response_model=sc.JpxStockInfosPublicList,
    summary="業種コードを指定してマーケット情報を取得",
)
def read_jpx_stock_info_items_tcs(
    *,
    industry_17_code: int | None = Query(None),
    industry_33_code: list[int] | None = Query(None),
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


@router.get(
    "/tcs/{market}",
    response_model=sc.JpxStockInfosPublicList,
    summary="上場市場を指定してマーケット情報を取得",
)
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


@router.get(
    "/industries/{type}",
    response_model=sc.IndustriesList,
    summary="[17] または [33] を入力して業種の名称とコードを取得",
)
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
    summary="17業種分類のコードを指定して33業種の名称とコードを取得",
)
def read_select_industries(
    *, industry_17_code: int | None = Query(None), session: SessionDep
) -> sc.IndustriesList:
    """
    Get all industries.
    """

    items = crud.read_select_industries(
        industry_17_code=industry_17_code, session=session
    )

    return items


@router.get(
    "/industry_list/",
    response_model=sc.industry_count_list,
    summary="業種別で上場銘柄数を取得",
)
def read_industry_count(
    *,
    session: SessionDep,
    type: int = Query(17, description="業種品類コード"),
) -> sc.industry_count_list:
    """
    Get industry_list.
    """

    try:
        items = crud.read_industry_count(session=session, type=type)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

    if len(items.data) == 0:
        raise HTTPException(status_code=404, detail="Items not found")

    return items


@router.get(
    "/industry_name", response_model=str, summary="業種コードを指定して業種名を取得"
)
def read_industry_name(
    *, session: SessionDep, type: int = Query(...), code: int = Query(...)
) -> str:
    """
    Get industry name by code.
    """
    try:
        item = crud.read_industry_name(type=type, code=code, session=session)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

    return item
