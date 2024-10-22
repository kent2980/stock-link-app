from datetime import datetime
from typing import Any, List

import app.schema as sc
from app.api.deps import SessionDep
from app.models import IxHeadTitle
from fastapi import APIRouter, HTTPException, Query
from sqlmodel import select

router = APIRouter()


@router.post("/ix/head/", response_model=sc.ix_head.IxHeadTitlePublic)
def create_ix_head_title_item(
    *, session: SessionDep, item_in: sc.ix_head.IxHeadTitleCreate
) -> Any:
    """
    Create new item.
    """
    item = IxHeadTitle.model_validate(item_in)
    session.add(item)
    session.commit()
    session.refresh(item)

    return item


@router.post("/ix/head/exist/", response_model=str)
def create_ix_head_title_item_exists(
    *, session: SessionDep, item_in: sc.ix_head.IxHeadTitleCreate
) -> Any:
    """
    Create new item.
    """
    statement = select(IxHeadTitle).where(IxHeadTitle.xbrl_id == item_in.xbrl_id)
    result = session.exec(statement)
    item_exists = result.first()

    if not item_exists:
        new_item = IxHeadTitle.model_validate(item_in)
        session.add(new_item)
        session.commit()
        session.refresh(new_item)
        return f"Item {new_item.name} created"

    return f"Item {item_in.name} already exists for xbrl_id {item_in.xbrl_id}"


@router.post("/ix/head/list/", response_model=str)
def create_ix_head_title_items_exists(
    *, session: SessionDep, items_in: sc.ix_head.IxHeadTitleCreateList
) -> Any:
    """
    Create new items.(Insert Select ... Not Exists)
    """
    new_items = []
    for item in items_in.data:
        statement = select(IxHeadTitle).where(IxHeadTitle.xbrl_id == item.xbrl_id)
        result = session.exec(statement)
        item_exists = result.first()

        if not item_exists:
            new_item = IxHeadTitle.model_validate(item)
            session.add(new_item)
            new_items.append(new_item)

    if new_items:
        session.commit()
        return f"Items {len(new_items)} created"

    return "Items already exists"


@router.get("/ix/head/is/{xbrl_id}/", response_model=bool)
def is_ix_head_title_item_exists(*, session: SessionDep, xbrl_id: str) -> Any:
    """
    Check if item exists.
    """
    statement = select(IxHeadTitle).where(IxHeadTitle.xbrl_id == xbrl_id)
    result = session.exec(statement)
    item_exists = result.first()

    if item_exists:
        return True

    return False
