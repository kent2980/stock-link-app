from fastapi import APIRouter, HTTPException
from sqlmodel import select

from app.api.deps import SessionDep
from app.models import StockWiki

from . import crud
from . import schema as sc

router = APIRouter()


@router.post("/", response_model=sc.StockWikiCreate, include_in_schema=True)
def create_stock_wiki_item(
    *, item_in: sc.StockWikiCreate, session: SessionDep
) -> sc.StockWikiCreate:
    """
    Create new item.
    """
    item = crud.create_stock_wiki_item(item_in=item_in, session=session)

    return item


@router.get("/{code}", response_model=sc.StockWikiPublic)
def get_stock_wiki_item(*, code: str, session: SessionDep) -> sc.StockWikiPublic:
    """
    Get item.
    """
    item = crud.get_stock_wiki_item(code=code, session=session)

    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    return item


@router.get("/", response_model=sc.StockWikisPublicList)
def get_stock_wiki_items(*, session: SessionDep) -> sc.StockWikisPublicList:
    """
    Get all items.
    """

    items = crud.get_stock_wiki_items(session=session)

    return items
