from typing import Any, Optional

import app.schema as sc
from app.api.deps import SessionDep
from app.models import IxCalculationArc, IxCalculationLoc
from fastapi import APIRouter, HTTPException, Query
from sqlmodel import select

router = APIRouter()


@router.post("/link/cal/loc/", response_model=sc.ix_cal.IxCalculationLocCreate)
def create_ix_cal_loc_item(
    *, session: SessionDep, item_in: sc.ix_cal.IxCalculationLocCreate
) -> Any:
    """
    Create new item.
    """
    item = IxCalculationLoc.model_validate(item_in)
    session.add(item)
    session.commit()
    session.refresh(item)

    return item


@router.post("/link/cal/arc/", response_model=sc.ix_cal.IxCalculationArcCreate)
def create_ix_cal_arc_item(
    *, session: SessionDep, item_in: sc.ix_cal.IxCalculationArcCreate
) -> Any:
    """
    Create new item.
    """
    item = IxCalculationArc.model_validate(item_in)
    session.add(item)
    session.commit()
    session.refresh(item)

    return item


@router.post("/link/cal/loc/list/", response_model=str)
def create_ix_cal_loc_items_exists(
    *, session: SessionDep, items_in: sc.ix_cal.IxCalculationLocCreateList
) -> Any:
    """
    Create new items.(Insert Select ... Not Exists)
    """

    new_items = []
    for item in items_in.data:
        statement = select(IxCalculationLoc).where(
            IxCalculationLoc.xlink_label == item.xlink_label,
            IxCalculationLoc.xlink_href == item.xlink_href,
            IxCalculationLoc.xlink_schema == item.xlink_schema,
            IxCalculationLoc.source_file_id == item.source_file_id,
        )
        result = session.exec(statement)
        item_exists = result.first()

        if not item_exists:
            new_item = IxCalculationLoc.model_validate(item)
            session.add(new_item)
            new_items.append(new_item)

    if new_items:
        session.commit()
        for new_item in new_items:
            session.refresh(new_item)

    return f"{len(new_items)} items created."


@router.post("/link/cal/arc/list/", response_model=str)
def create_ix_cal_arc_items_exists(
    *, session: SessionDep, items_in: sc.ix_cal.IxCalculationArcCreateList
) -> Any:
    """
    Create new items.(Insert Select ... Not Exists)
    """

    new_items = []
    for item in items_in.data:
        statement = select(IxCalculationArc).where(
            IxCalculationArc.xlink_from == item.xlink_from,
            IxCalculationArc.xlink_to == item.xlink_to,
            IxCalculationArc.source_file_id == item.source_file_id,
        )
        result = session.exec(statement)
        item_exists = result.first()

        if not item_exists:
            new_item = IxCalculationArc.model_validate(item)
            session.add(new_item)
            new_items.append(new_item)

    if new_items:
        session.commit()
        for new_item in new_items:
            session.refresh(new_item)

    return f"{len(new_items)} items created."


@router.get("/link/cal/loc/is/{source_file_id}/", response_model=bool)
def get_ix_cal_loc_item(*, session: SessionDep, source_file_id: str) -> Any:
    """
    Get item.
    """
    statement = select(IxCalculationLoc).where(
        IxCalculationLoc.source_file_id == source_file_id
    )
    result = session.exec(statement)
    item_exists = result.first()

    if item_exists:
        return True

    return False


@router.get("/link/cal/arc/is/{source_file_id}/", response_model=bool)
def get_ix_cal_arc_item(*, session: SessionDep, source_file_id: str) -> Any:
    """
    Get item.
    """
    statement = select(IxCalculationArc).where(
        IxCalculationArc.source_file_id == source_file_id
    )
    result = session.exec(statement)
    item_exists = result.first()

    if item_exists:
        return True

    return False


@router.delete("/link/cal/loc/delete/", response_model=bool)
def delete_ix_cal_loc_item(
    *, session: SessionDep, head_item_key: Optional[str] = Query(...)
) -> Any:
    """
    Delete item.
    """
    statement = select(IxCalculationLoc).where(
        IxCalculationLoc.head_item_key == head_item_key
    )
    result = session.exec(statement)
    items = result.all()

    if items is None:
        return False

    for item in items:
        session.delete(item)
    session.commit()

    return True


@router.delete("/link/cal/arc/delete/", response_model=bool)
def delete_ix_cal_arc_item(
    *, session: SessionDep, head_item_key: Optional[str] = Query(...)
) -> Any:
    """
    Delete item.
    """
    statement = select(IxCalculationArc).where(
        IxCalculationArc.head_item_key == head_item_key
    )
    result = session.exec(statement)
    items = result.all()

    if items is None:
        return False

    for item in items:
        session.delete(item)
    session.commit()

    return True
