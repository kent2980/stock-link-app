from typing import Any

import app.schema as sc
from app.api.deps import SessionDep
from app.models import IxDefinitionArc, IxDefinitionLoc
from fastapi import APIRouter, HTTPException
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
        statement = select(IxDefinitionLoc).where(
            IxDefinitionLoc.xlink_label == item.xlink_label,
            IxDefinitionLoc.xlink_href == item.xlink_href,
            IxDefinitionLoc.attr_value == item.attr_value,
            IxDefinitionLoc.xlink_schema == item.xlink_schema,
            IxDefinitionLoc.source_file_id == item.source_file_id,
        )
        result = session.exec(statement)
        item_exists = result.first()

        if not item_exists:
            new_item = IxDefinitionLoc.model_validate(item)
            session.add(new_item)
            new_items.append(new_item)

    if new_items:
        session.commit()
        for new_item in new_items:
            session.refresh(new_item)

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
        statement = select(IxDefinitionArc).where(
            IxDefinitionArc.xlink_to == item.xlink_to,
            IxDefinitionArc.xlink_from == item.xlink_from,
            IxDefinitionArc.attr_value == item.attr_value,
            IxDefinitionArc.source_file_id == item.source_file_id,
        )
        result = session.exec(statement)
        item_exists = result.first()

        if not item_exists:
            new_item = IxDefinitionArc.model_validate(item)
            session.add(new_item)
            new_items.append(new_item)

    if new_items:
        session.commit()
        for new_item in new_items:
            session.refresh(new_item)

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
