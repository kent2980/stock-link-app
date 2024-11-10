from typing import Any

import app.schema as sc
from app.api.deps import SessionDep
from app.models import IxDefinitionArc, IxDefinitionLoc
from fastapi import APIRouter, HTTPException, Query
from sqlalchemy.exc import IntegrityError
from sqlmodel import select

router = APIRouter()


@router.post("/link/def/loc/", response_model=sc.ix_def.IxDefinitionLocCreate)
def create_ix_def_loc_item(
    *, session: SessionDep, item_in: sc.ix_def.IxDefinitionLocCreate
) -> Any:
    """
    Create new item.
    """

    item = IxDefinitionLoc.model_validate(item_in)
    session.add(item)
    session.commit()
    session.refresh(item)

    return item


@router.post("/link/def/arc/", response_model=sc.ix_def.IxDefinitionArcCreate)
def create_ix_def_arc_item(
    *, session: SessionDep, item_in: sc.ix_def.IxDefinitionArcCreate
) -> Any:
    """
    Create new item.
    """
    item = IxDefinitionArc.model_validate(item_in)
    session.add(item)
    session.commit()
    session.refresh(item)

    return item


@router.post("/link/def/loc/list/", response_model=str)
def create_ix_def_loc_items_exists(
    *, session: SessionDep, items_in: sc.ix_def.IxDefinitionLocCreateList
) -> Any:
    """
    Create new items.(Insert Select ... Not Exists)
    """

    new_items = []
    for item in items_in.data:
        new_item = IxDefinitionLoc.model_validate(item)
        session.add(new_item)
        try:
            session.commit()
            session.refresh(new_item)
            new_items.append(new_item)
        except IntegrityError:
            session.rollback()
    return f"{len(new_items)} items created."


@router.post("/link/def/arc/list/", response_model=str)
def create_ix_def_arc_items_exists(
    *, session: SessionDep, items_in: sc.ix_def.IxDefinitionArcCreateList
) -> Any:
    """
    Create new items.(Insert Select ... Not Exists)
    """

    new_items = []
    for item in items_in.data:
        new_item = IxDefinitionArc.model_validate(item)
        session.add(new_item)
        try:
            session.commit()
            session.refresh(new_item)
            new_items.append(new_item)
        except IntegrityError:
            session.rollback()
    return f"{len(new_items)} items created."


@router.get("/link/def/loc/is/{source_file_id}/", response_model=bool)
def get_ix_def_loc_item(*, session: SessionDep, source_file_id: str) -> Any:
    """
    Get item.
    """
    statement = select(IxDefinitionLoc).where(
        IxDefinitionLoc.source_file_id == source_file_id
    )
    result = session.exec(statement)
    item = result.first()

    if item:
        return True

    return False


@router.get("/link/def/arc/is/{source_file_id}/", response_model=bool)
def get_ix_def_arc_item(*, session: SessionDep, source_file_id: str) -> Any:
    """
    Get item.
    """
    statement = select(IxDefinitionArc).where(
        IxDefinitionArc.source_file_id == source_file_id
    )
    result = session.exec(statement)
    item = result.first()

    if item:
        return True

    return False


@router.delete("/link/def/loc/delete/", response_model=bool)
def delete_ix_def_loc_item(
    *, session: SessionDep, head_item_key: str = Query(...)
) -> Any:
    """
    Delete item.
    """
    statement = select(IxDefinitionLoc).where(
        IxDefinitionLoc.head_item_key == head_item_key
    )
    result = session.exec(statement)
    items = result.all()

    if items is None:
        return False

    for item in items:
        session.delete(item)

    session.commit()

    return True


@router.delete("/link/def/arc/delete/", response_model=bool)
def delete_ix_def_arc_item(
    *, session: SessionDep, head_item_key: str = Query(...)
) -> Any:
    """
    Delete item.
    """
    statement = select(IxDefinitionArc).where(
        IxDefinitionArc.head_item_key == head_item_key
    )
    result = session.exec(statement)
    items = result.all()

    if items is None:
        return False

    for item in items:
        session.delete(item)

    session.commit()

    return True
