from typing import Any

from fastapi import APIRouter
from sqlmodel import select

import app.schema as sc
from app.api.deps import SessionDep
from app.models import IxFilePath

router = APIRouter()


@router.post("/ix/file_path/", response_model=sc.ix_file_path.IxFilePathPublic)
def create_ix_file_path_item(*, session: SessionDep, item_in: sc.ix_file_path.IxFilePathCreate) -> Any:
    """
    Create new item.
    """
    item = IxFilePath.model_validate(item_in)
    session.add(item)
    session.commit()
    session.refresh(item)

    return item


@router.get("/ix/file_path/is/{xbrl_id}", response_model=bool)
def is_ix_file_path_item_exists(*, session: SessionDep, xbrl_id: str) -> Any:
    """
    Check if item exists.
    """
    statement = select(IxFilePath).where(IxFilePath.xbrl_id == xbrl_id)
    result = session.exec(statement)
    item_exists = result.first()

    if item_exists:
        return True

    return False
