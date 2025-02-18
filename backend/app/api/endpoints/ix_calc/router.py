from typing import Any, Optional

from fastapi import APIRouter, HTTPException, Query
from sqlalchemy.exc import IntegrityError
from sqlmodel import select

from app.api.deps import SessionDep
from app.models import IxCalculationArc, IxCalculationLoc

from . import crud
from . import schema as sc

router = APIRouter()


@router.post(
    "/link/cal/loc/",
    response_model=sc.IxCalculationLocCreate,
    include_in_schema=False,
)
def create_ix_cal_loc_item(
    *, session: SessionDep, item_in: sc.IxCalculationLocCreate
) -> IxCalculationLoc:
    """
    Create new item.
    """
    item = crud.create_ix_cal_loc_item(session, item_in)

    return item


@router.post(
    "/link/cal/arc/",
    response_model=sc.IxCalculationArcCreate,
    include_in_schema=False,
)
def create_ix_cal_arc_item(
    *, session: SessionDep, item_in: sc.IxCalculationArcCreate
) -> IxCalculationArc:
    """
    Create new item.
    """
    item = crud.create_ix_cal_arc_item(session, item_in)

    return item


@router.post("/link/cal/loc/list/", response_model=str, include_in_schema=False)
def create_ix_cal_loc_items_exists(
    *, session: SessionDep, items_in: sc.IxCalculationLocCreateList
) -> Any:
    """
    Create new items.(Insert Select ... Not Exists)
    """
    msg = crud.create_ix_cal_loc_items(session, items_in)

    return msg


@router.post("/link/cal/arc/list/", response_model=str, include_in_schema=False)
def create_ix_cal_arc_items_exists(
    *, session: SessionDep, items_in: sc.IxCalculationArcCreateList
) -> Any:
    """
    Create new items.(Insert Select ... Not Exists)
    """
    msg = crud.create_ix_cal_arc_items(session, items_in)

    return msg


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


@router.delete("/link/cal/loc/delete/", response_model=bool, include_in_schema=False)
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


@router.delete("/link/cal/arc/delete/", response_model=bool, include_in_schema=False)
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
