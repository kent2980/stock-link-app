from fastapi import APIRouter
from sqlmodel import select

import app.schema as sc
from app.api.deps import SessionDep
from app.models import StockWiki

router = APIRouter()


@router.post("/", response_model=sc.stock_wiki.StockWikiCreate, include_in_schema=True)
def create_stock_wiki_item(
    *, item_in: sc.stock_wiki.StockWikiCreate, session: SessionDep
) -> sc.stock_wiki.StockWikiCreate:
    """
    Create new item.
    """
    item = StockWiki.model_validate(item_in)
    session.add(item)
    session.commit()
    session.refresh(item)

    return item


@router.get("/{code}", response_model=sc.stock_wiki.StockWikiPublic)
def get_stock_wiki_item(
    *, code: str, session: SessionDep
) -> sc.stock_wiki.StockWikiPublic:
    """
    Get item.
    """
    statement = select(StockWiki).where(StockWiki.code == code)
    item = session.exec(statement).first()
    return item


@router.get("/", response_model=sc.stock_wiki.StockWikisPublicList)
def get_stock_wiki_items(*, session: SessionDep) -> sc.stock_wiki.StockWikisPublicList:
    """
    Get all items.
    """
    statement = select(StockWiki)
    items = session.exec(statement).all()
    return sc.stock_wiki.StockWikisPublicList(count=len(items), data=items)
