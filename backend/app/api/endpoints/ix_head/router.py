import datetime
import re
from decimal import Decimal
from typing import Any, List, Optional

from fastapi import APIRouter, HTTPException, Query
from sqlalchemy.exc import IntegrityError
from sqlmodel import func, select, update

from app.api.deps import SessionDep
from app.models import IxHeadTitle, IxNonFraction, IxNonNumeric

from . import crud
from . import schema as sc

router = APIRouter()


@router.post("/ix/head/", response_model=sc.IxHeadTitlePublic, include_in_schema=False)
def create_ix_head_title_item(
    *, session: SessionDep, item_in: sc.IxHeadTitleCreate
) -> Any:
    """
    Create new item.
    """
    item = crud.create_ix_head_title_item(session=session, item_in=item_in)

    return item


@router.post("/ix/head/list/", response_model=str, include_in_schema=False)
def create_ix_head_title_items(
    *, session: SessionDep, items_in: sc.IxHeadTitleCreateList
) -> Any:
    """
    Create new items.(Insert Select ... Not Exists)
    """
    msg = crud.create_ix_head_title_items(session=session, items_in=items_in)

    return msg


@router.patch("/ix/head/active/", response_model=bool, include_in_schema=False)
def update_is_active_ix_head_title_item(
    *, session: SessionDep, head_item_key: str = Query(...)
) -> bool:

    is_active = crud.update_is_active_ix_head_title_item(
        session=session, head_item_key=head_item_key
    )

    return is_active


@router.patch("/ix/head/generate/", response_model=bool, include_in_schema=False)
def active_is_generate(*, session: SessionDep, head_item_key: str = Query(...)) -> bool:
    """
    Generate item.
    """
    is_item = crud.active_is_generate(session=session, head_item_key=head_item_key)

    return is_item


@router.get("/ix/head/is_active/", response_model=bool)
def is_ix_head_title_item_active(*, session: SessionDep, head_item_key: str) -> bool:
    """
    Check if item is active.
    """
    is_active = crud.is_ix_head_title_item_active(
        session=session, head_item_key=head_item_key
    )

    return is_active


@router.get("/ix/head/", response_model=sc.IxHeadTitlePublic)
def read_ix_head_title_item(
    *, session: SessionDep, head_item_key: str = Query(...)
) -> IxHeadTitle:
    """
    Get item by head_item_key.
    """
    item = crud.read_ix_head_title_item(session=session, head_item_key=head_item_key)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item
