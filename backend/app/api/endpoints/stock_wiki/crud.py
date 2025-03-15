from typing import Optional

from sqlalchemy.exc import IntegrityError
from sqlmodel import Session, select

from app.models import StockWiki

from . import schema as sc


def create_stock_wiki_item(
    *, item_in: sc.StockWikiCreate, session: Session
) -> sc.StockWikiCreate:
    """
    Create new item.
    """

    try:
        item = StockWiki.model_validate(item_in)
        session.add(item)
        session.commit()
        session.refresh(item)

        return item
    except IntegrityError as e:
        session.rollback()
        raise IntegrityError(statement=e.statement, orig=e.orig, params=e.params) from e


def get_stock_wiki_item(*, code: str, session: Session) -> Optional[StockWiki]:
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
