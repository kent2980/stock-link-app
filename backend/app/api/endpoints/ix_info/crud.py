from sqlmodel import Session, select

from app.models import IxHeadTitle


def read_ix_head_title_item(*, session: Session, head_item_key: str) -> IxHeadTitle:
    """
    Get item by head_item_key.
    """
    statement = select(IxHeadTitle).where(IxHeadTitle.item_key == head_item_key)
    result = session.exec(statement)
    item = result.first()

    return item
