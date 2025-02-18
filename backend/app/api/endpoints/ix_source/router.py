from typing import Any, List

from fastapi import APIRouter, HTTPException, Query
from sqlalchemy.exc import IntegrityError
from sqlmodel import select

from app.api.deps import SessionDep
from app.models import IxSourceFile

from . import crud
from . import schema as sc

router = APIRouter()


@router.post("/source/", response_model=str, include_in_schema=False)
def create_ix_source_file_item(
    *, session: SessionDep, item_in: sc.IxSourceFileCreate
) -> IxSourceFile:
    """
    Create new item.
    """
    item = crud.create_ix_source_file_item(session=session, item_in=item_in)

    return item


@router.post("/source/list/", response_model=str, include_in_schema=False)
def create_ix_source_file_items(
    *, session: SessionDep, items_in: sc.IxSourceFileCreateList
) -> str:
    """
    Create new items.(Insert Select ... Not Exists)
    """
    msg = crud.create_ix_source_file_items(session=session, items_in=items_in)

    return msg


@router.get("/is/exits/source_file_id/", response_model=bool)
def get_ix_source_file_item(
    *, session: SessionDep, source_file_id: str = Query(...)
) -> bool:
    """
    Get item.
    """

    item_exists = crud.get_ix_source_file_item(
        session=session, source_file_id=source_file_id
    )

    if not item_exists:
        raise HTTPException(status_code=404, detail="Item not found")

    return item_exists
