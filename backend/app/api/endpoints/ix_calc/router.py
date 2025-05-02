from typing import Any

from fastapi import APIRouter

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
def create_ix_cal_loc_items(
    *, session: SessionDep, items_in: sc.IxCalculationLocCreateList
) -> Any:
    """
    Create new items.(Insert Select ... Not Exists)
    """
    msg = crud.create_ix_cal_loc_items(session, items_in)

    return msg


@router.post("/link/cal/arc/list/", response_model=str, include_in_schema=False)
def create_ix_cal_arc_items(
    *, session: SessionDep, items_in: sc.IxCalculationArcCreateList
) -> Any:
    """
    Create new items.(Insert Select ... Not Exists)
    """
    msg = crud.create_ix_cal_arc_items(session, items_in)

    return msg
