from sqlalchemy.exc import IntegrityError
from sqlmodel import Session

from app.models import IxDefinitionArc, IxDefinitionLoc

from . import schema as sc


def create_ix_def_loc_item(
    *, session: Session, item_in: sc.IxDefinitionLocCreate
) -> IxDefinitionLoc:
    """
    Create new item.
    """

    item = IxDefinitionLoc.model_validate(item_in)
    session.add(item)
    session.commit()
    session.refresh(item)

    return item


def create_ix_def_arc_item(
    *, session: Session, item_in: sc.IxDefinitionArcCreate
) -> IxDefinitionArc:
    """
    Create new item.
    """
    item = IxDefinitionArc.model_validate(item_in)
    session.add(item)
    session.commit()
    session.refresh(item)

    return item


def create_ix_def_loc_items(
    *, session: Session, items_in: sc.IxDefinitionLocCreateList
) -> str:
    """
    Create new items.(Insert Select ... Not Exists)
    """
    new_items = [IxDefinitionLoc.model_validate(item) for item in items_in.data]

    try:
        session.bulk_save_objects(new_items)
        session.commit()
    except IntegrityError:
        session.rollback()
        # 一意制約違反が発生した場合、個別に追加を試みる
        new_items = []
        for item in items_in.data:
            new_item = IxDefinitionLoc.model_validate(item)
            session.add(new_item)
            try:
                session.commit()
                session.refresh(new_item)
                new_items.append(new_item)
            except IntegrityError:
                session.rollback()  # コミット失敗時にロールバック

    return f"{len(new_items)} items created."


def create_ix_def_arc_items(
    *, session: Session, items_in: sc.IxDefinitionArcCreateList
) -> str:
    """
    Create new items.(Insert Select ... Not Exists)
    """
    new_items = [IxDefinitionArc.model_validate(item) for item in items_in.data]

    try:
        session.bulk_save_objects(new_items)
        session.commit()
    except IntegrityError:
        session.rollback()
        # 一意制約違反が発生した場合、個別に追加を試みる
        new_items = []
        for item in items_in.data:
            new_item = IxDefinitionArc.model_validate(item)
            session.add(new_item)
            try:
                session.commit()
                session.refresh(new_item)
                new_items.append(new_item)
            except IntegrityError:
                session.rollback()

    return f"{len(new_items)} items created."
