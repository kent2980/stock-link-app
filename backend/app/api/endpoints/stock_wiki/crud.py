from sqlmodel import Session, select

from app.models import StockWiki

from . import schema as sc


def create_stock_wiki_item(
    *, item_in: sc.StockWikiCreate, session: Session
) -> sc.StockWikiCreate:
    """
    Create new item.
    """
    item = StockWiki.model_validate(item_in)
    session.add(item)
    session.commit()
    session.refresh(item)

    return item


def get_stock_wiki_item(*, code: str, session: Session) -> sc.StockWikiPublic:
    """
    Get item.
    """
    statement = select(StockWiki).where(StockWiki.code == code)
    item = session.exec(statement).first()
    return item


def get_stock_wiki_items(*, session: Session) -> sc.StockWikisPublicList:
    """
    Get all items.
    """
    statement = select(StockWiki)
    items = session.exec(statement).all()
    return sc.StockWikisPublicList(count=len(items), data=items)
