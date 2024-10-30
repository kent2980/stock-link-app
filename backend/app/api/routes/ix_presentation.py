from typing import Any

import app.schema as sc
from app.api.deps import SessionDep
from app.models import IxPresentationArc, IxPresentationLoc
from fastapi import APIRouter, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlmodel import select

router = APIRouter()


@router.post("/link/pre/loc/", response_model=sc.ix_pre.IxPresentationLocCreate)
def create_ix_pre_loc_item(
    *, session: SessionDep, item_in: sc.ix_pre.IxPresentationLocCreate
) -> Any:
    """
    Create new item.
    """
    item = IxPresentationLoc.model_validate(item_in)
    session.add(item)
    session.commit()
    session.refresh(item)

    return item


@router.post("/link/pre/arc/", response_model=sc.ix_pre.IxPresentationArcCreate)
def create_ix_pre_arc_item(
    *, session: SessionDep, item_in: sc.ix_pre.IxPresentationArcCreate
) -> Any:
    """
    Create new item.
    """
    item = IxPresentationArc.model_validate(item_in)
    session.add(item)
    session.commit()
    session.refresh(item)

    return item


@router.post("/link/pre/loc/list/", response_model=str)
def create_ix_pre_loc_items_exists(
    *, session: SessionDep, items_in: sc.ix_pre.IxPresentationLocCreateList
) -> Any:
    """
    Create new items.(Insert Select ... Not Exists)
    """

    new_items = []
    for item in items_in.data:
        statement = select(IxPresentationLoc).where(
            IxPresentationLoc.xlink_label == item.xlink_label,
            IxPresentationLoc.xlink_href == item.xlink_href,
            IxPresentationLoc.xlink_schema == item.xlink_schema,
            IxPresentationLoc.source_file_id == item.source_file_id,
        )
        result = session.exec(statement)
        item_exists = result.first()

        if not item_exists:
            new_item = IxPresentationLoc.model_validate(item)
            session.add(new_item)
            new_items.append(new_item)

    if new_items:
        session.commit()
        return f"Items {new_items} created"

    return "Items already exists"


@router.post("/link/pre/arc/list/", response_model=str)
def create_ix_pre_arc_items_exists(
    *, session: SessionDep, items_in: sc.ix_pre.IxPresentationArcCreateList
) -> Any:
    """
    Create new items.(Insert Select ... Not Exists)
    """

    new_items = []
    for item in items_in.data:
        statement = select(IxPresentationArc).where(
            IxPresentationArc.xlink_to == item.xlink_to,
            IxPresentationArc.xlink_from == item.xlink_from,
            IxPresentationArc.source_file_id == item.source_file_id,
        )
        result = session.exec(statement)
        item_exists = result.first()

        if not item_exists:
            new_item = IxPresentationArc.model_validate(item)
            session.add(new_item)
            new_items.append(new_item)

    if new_items:
        session.commit()
        return f"Items {new_items} created"

    return "Items already exists"


@router.get("/link/pre/loc/is/{source_file_id}/", response_model=bool)
def get_ix_pre_loc_item(*, session: SessionDep, source_file_id: str) -> Any:
    """
    Check if item exists.
    """
    statement = select(IxPresentationLoc).where(
        IxPresentationLoc.source_file_id == source_file_id
    )
    result = session.exec(statement)
    item_exists = result.first()

    return bool(item_exists)


@router.get("/link/pre/arc/is/{source_file_id}/", response_model=bool)
def get_ix_pre_arc_item(*, session: SessionDep, source_file_id: str) -> Any:
    """
    Check if item exists.
    """
    statement = select(IxPresentationArc).where(
        IxPresentationArc.source_file_id == source_file_id
    )
    result = session.exec(statement)
    item_exists = result.first()

    return bool(item_exists)
