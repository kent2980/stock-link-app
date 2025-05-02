from sqlalchemy.exc import IntegrityError
from sqlmodel import Session

from app.models import IxNonFraction

from . import schema as sc


def create_ix_non_fraction_item(
    *, session: Session, item_in: sc.IxNonFractionCreate
) -> IxNonFraction:
    """
    Create new item.
    """

    item = IxNonFraction.model_validate(item_in)
    session.add(item)
    session.commit()
    session.refresh(item)

    return item


def create_ix_non_fraction_items(
    *, session: Session, items_in: sc.IxNonFractionCreateList
) -> str:
    """
    Create new items.(Insert Select ... Not Exists)
    """
    new_items = [IxNonFraction.model_validate(item) for item in items_in.data]

    try:
        session.bulk_save_objects(new_items)
        session.commit()
    except IntegrityError:
        session.rollback()
        new_items = []
        for item in items_in.data:
            new_item = IxNonFraction.model_validate(item)
            session.add(new_item)
            try:
                session.commit()
                session.refresh(new_item)
                new_items.append(new_item)
            except IntegrityError:
                session.rollback()

    return f"{len(new_items)} items created."
