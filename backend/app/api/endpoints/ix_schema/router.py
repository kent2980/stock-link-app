from typing import Any

from fastapi import APIRouter, HTTPException, Query
from sqlalchemy.exc import IntegrityError
from sqlmodel import select

from app.api.deps import SessionDep
from app.models import ScLinkBaseRef

from . import crud
from . import schema as sc

router = APIRouter()


@router.post(
    "/schema/linkbase/",
    response_model=sc.IxSchemaLinkBaseCreate,
    include_in_schema=False,
)
def create_ix_schema_linkbase_item(
    *, session: SessionDep, item_in: sc.IxSchemaLinkBaseCreate
) -> ScLinkBaseRef:
    """
    Create new item.
    """
    item = crud.create_ix_schema_linkbase_item(session=session, item_in=item_in)

    return item


@router.post("/schema/linkbase/list/", response_model=str, include_in_schema=False)
def create_ix_schema_linkbase_items(
    *, session: SessionDep, items_in: sc.IxSchemaLinkBaseCreateList
) -> str:
    """
    Create new items.(Insert Select ... Not Exists)
    """

    msg = crud.create_ix_schema_linkbase_items(session=session, items_in=items_in)

    return msg
