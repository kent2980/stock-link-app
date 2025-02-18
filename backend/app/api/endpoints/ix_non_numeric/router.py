from typing import Any

from fastapi import APIRouter, Query
from sqlalchemy.exc import IntegrityError
from sqlmodel import select

from app.api.deps import SessionDep
from app.models import IxNonNumeric

from . import crud
from . import schema as sc

router = APIRouter()


@router.post(
    "/ix/non_numeric/",
    response_model=sc.IxNonNumericCreate,
    include_in_schema=False,
)
def create_ix_non_numeric_item(
    *, session: SessionDep, item_in: sc.IxNonNumericCreate
) -> IxNonNumeric:
    """
    Create new item.
    """
    item = crud.create_ix_non_numeric_item(session=session, item_in=item_in)

    return item


@router.post("/ix/non_numeric/list/", response_model=str, include_in_schema=False)
def create_ix_non_numeric_items(
    *, session: SessionDep, items_in: sc.IxNonNumericCreateList
) -> str:
    """
    Create new items.(Insert Select ... Not Exists)
    """

    msg = crud.create_ix_non_numeric_items(session=session, items_in=items_in)

    return msg
