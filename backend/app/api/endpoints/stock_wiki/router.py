from fastapi import APIRouter
from sqlmodel import select

from app.api.deps import SessionDep
from app.models import StockWiki

from . import schema as sc

router = APIRouter()


@router.post("/", response_model=sc.StockWikiCreate, include_in_schema=True)
def create_stock_wiki_item(
    *, item_in: sc.StockWikiCreate, session: SessionDep
) -> sc.StockWikiCreate:
    """
    Create new item.
    """
    item = StockWiki.model_validate(item_in)
    session.add(item)
    session.commit()
    session.refresh(item)

    return item


@router.get("/{code}", response_model=sc.StockWikiPublic)
def get_stock_wiki_item(*, code: str, session: SessionDep) -> sc.StockWikiPublic:
    """
    Get item.
    """
    statement = select(StockWiki).where(StockWiki.code == code)
    item = session.exec(statement).first()
    return item


@router.get("/", response_model=sc.StockWikisPublicList)
def get_stock_wiki_items(*, session: SessionDep) -> sc.StockWikisPublicList:
    """
    Get all items.
    """
    statement = select(StockWiki)
    items = session.exec(statement).all()
    return sc.StockWikisPublicList(count=len(items), data=items)
