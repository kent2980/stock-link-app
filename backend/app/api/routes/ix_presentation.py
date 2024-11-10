from typing import Any

import app.schema as sc
from app.api.deps import SessionDep
from app.models import IxPresentationArc, IxPresentationLoc
from fastapi import APIRouter, HTTPException, Query
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
        new_item = IxPresentationLoc.model_validate(item)
        session.add(new_item)
        try:
            session.commit()
            session.refresh(new_item)
            new_items.append(new_item)
        except IntegrityError:
            session.rollback()

    return f"{len(new_items)} items created."


@router.post("/link/pre/arc/list/", response_model=str)
def create_ix_pre_arc_items_exists(
    *, session: SessionDep, items_in: sc.ix_pre.IxPresentationArcCreateList
) -> Any:
    """
    Create new items.(Insert Select ... Not Exists)
    """

    new_items = []
    for item in items_in.data:
        new_item = IxPresentationArc.model_validate(item)
        session.add(new_item)
        try:
            session.commit()
            session.refresh(new_item)
            new_items.append(new_item)
        except IntegrityError:
            session.rollback()

    return f"{len(new_items)} items created."


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


@router.delete("/link/pre/loc/delete/", response_model=bool)
def delete_ix_pre_loc_item(
    *, session: SessionDep, head_item_key: str = Query(...)
) -> Any:
    """
    Delete item.
    """
    statement = select(IxPresentationLoc).where(
        IxPresentationLoc.head_item_key == head_item_key
    )
    result = session.exec(statement)
    items = result.all()

    if items:
        for item in items:
            session.delete(item)
        session.commit()
        return True

    return False


@router.delete("/link/pre/arc/delete/", response_model=bool)
def delete_ix_pre_arc_item(
    *, session: SessionDep, head_item_key: str = Query(...)
) -> Any:
    """
    Delete item.
    """
    statement = select(IxPresentationArc).where(
        IxPresentationArc.head_item_key == head_item_key
    )
    result = session.exec(statement)
    items = result.all()

    if items:
        for item in items:
            session.delete(item)
        session.commit()
        return True

    return False
