from sqlalchemy.exc import IntegrityError
from sqlmodel import Session

from app.models import IxNonNumeric

from . import schema as sc


def create_ix_non_numeric_item(
    *, session: Session, item_in: sc.IxNonNumericCreate
) -> IxNonNumeric:
    """
    Create new item.
    """
    item = IxNonNumeric.model_validate(item_in)
    session.add(item)
    session.commit()
    session.refresh(item)

    return item


def create_ix_non_numeric_items(
    *, session: Session, items_in: sc.IxNonNumericCreateList
) -> str:
    """
    Create new items.(Insert Select ... Not Exists)
    """
    new_items = [IxNonNumeric.model_validate(item) for item in items_in.data]

    try:
        session.bulk_save_objects(new_items)
        session.commit()
    except IntegrityError:
        session.rollback()
        new_items = []
        for item in items_in.data:
            new_item = IxNonNumeric.model_validate(item)
            session.add(new_item)
            try:
                session.commit()
                session.refresh(new_item)
                new_items.append(new_item)
            except IntegrityError:
                session.rollback()

    return f"{len(new_items)} items created."
