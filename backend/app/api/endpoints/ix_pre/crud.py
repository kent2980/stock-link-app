from sqlalchemy.exc import IntegrityError
from sqlmodel import Session, select

from app.models import IxPresentationArc, IxPresentationLoc

from . import schema as sc


def create_ix_pre_loc_item(
    *, session: Session, item_in: sc.IxPresentationLocCreate
) -> IxPresentationLoc:
    """
    Create new item.
    """
    item = IxPresentationLoc.model_validate(item_in)
    session.add(item)
    session.commit()
    session.refresh(item)

    return item


def create_ix_pre_arc_item(
    *, session: Session, item_in: sc.IxPresentationArcCreate
) -> IxPresentationArc:
    """
    Create new item.
    """
    item = IxPresentationArc.model_validate(item_in)
    session.add(item)
    session.commit()
    session.refresh(item)

    return item


def create_ix_pre_loc_items(
    *, session: Session, items_in: sc.IxPresentationLocCreateList
) -> str:
    """
    Create new items.(Insert Select ... Not Exists)
    """

    new_items = [IxPresentationLoc.model_validate(item) for item in items_in.data]

    try:
        session.bulk_save_objects(new_items)
        session.commit()
    except IntegrityError:
        session.rollback()
        new_items = []
        for item in items_in.data:
            new_item = IxPresentationLoc.model_validate(item)
            session.add(new_item)
            try:
                session.commit()
                session.refresh(new_item)
                new_items.append(new_item)
            except IntegrityError:
                session.rollback()

    return f"{len(new_items)} items created."


def create_ix_pre_arc_items(
    *, session: Session, items_in: sc.IxPresentationArcCreateList
) -> str:
    """
    Create new items.(Insert Select ... Not Exists)
    """

    new_items = [IxPresentationArc.model_validate(item) for item in items_in.data]

    try:
        session.bulk_save_objects(new_items)
        session.commit()
    except IntegrityError:
        session.rollback()
        new_items = []
        for item in items_in.data:
            new_item = IxPresentationArc.model_validate(item)
            session.add(new_item)
            try:
                session.commit()
                session.refresh(new_item)
                new_items.append(new_item)
            except IntegrityError:
                session.rollback()

    return f"{len(new_items)} items created."
