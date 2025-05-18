from sqlalchemy.exc import IntegrityError
from sqlmodel import Session, select

from app.models import IxSourceFile

from . import schema as sc


def create_ix_source_file_item(
    *, session: Session, item_in: sc.IxSourceFileCreate
) -> IxSourceFile:
    """
    Create new item.
    """
    item = IxSourceFile.model_validate(item_in)
    session.add(item)
    session.commit()
    session.refresh(item)

    return item


def create_ix_source_file_items(
    *, session: Session, items_in: sc.IxSourceFileCreateList
) -> str:
    """
    Create new items.(Insert Select ... Not Exists)
    """
    new_items = [IxSourceFile.model_validate(item) for item in items_in.data]

    try:
        session.bulk_save_objects(new_items)
        session.commit()
    except IntegrityError:
        session.rollback()
        new_items = []
        for item in items_in.data:
            new_item = IxSourceFile.model_validate(item)
            session.add(new_item)
            try:
                session.commit()
                session.refresh(new_item)
                new_items.append(new_item)
            except IntegrityError:
                session.rollback()

    return f"{len(new_items)} items created."


def get_ix_source_file_item(*, session: Session, source_file_id: str) -> bool:
    """
    Get item.
    """
    statement = select(IxSourceFile).where(
        IxSourceFile.source_file_id == source_file_id
    )
    result = session.exec(statement)
    item_exists = result.first()

    if item_exists:
        return True
    else:
        return False
