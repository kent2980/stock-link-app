from sqlmodel import Session, select

from app.models import IxFilePath

from . import schema as sc


def create_ix_file_path_item(
    *, session: Session, item_in: sc.IxFilePathCreate
) -> IxFilePath:
    """
    Create new item.
    """
    item = IxFilePath.model_validate(item_in)
    session.add(item)
    session.commit()
    session.refresh(item)

    return item
