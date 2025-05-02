from fastapi import APIRouter, HTTPException
from sqlalchemy.exc import IntegrityError

from app.api.deps import SessionDep
from app.models import IxLabelArc, IxLabelLoc, IxLabelValue

from . import crud
from . import schema as sc

router = APIRouter()


@router.post(
    "/link/lab/loc/",
    response_model=sc.IxLabelLocCreate,
    include_in_schema=False,
)
def create_ix_label_loc_item(
    *, session: SessionDep, item_in: sc.IxLabelLocCreate
) -> IxLabelLoc:
    """
    Create new item.
    """

    try:
        item = crud.create_ix_label_loc_item(session=session, item_in=item_in)
    except IntegrityError:
        raise HTTPException(status_code=400, detail="Item already")

    return item


@router.post(
    "/link/lab/arc/",
    response_model=sc.IxLabelArcCreate,
    include_in_schema=False,
)
def create_ix_label_arc_item(
    *, session: SessionDep, item_in: sc.IxLabelArcCreate
) -> IxLabelArc:
    """
    Create new item.
    """

    try:
        item = crud.create_ix_label_arc_item(session=session, item_in=item_in)
    except IntegrityError:
        raise HTTPException(status_code=400, detail="Item already")

    return item


@router.post(
    "/link/lab/value/",
    response_model=sc.IxLabelValueCreate,
    include_in_schema=False,
)
def create_ix_label_value_item(
    *, session: SessionDep, item_in: sc.IxLabelValueCreate
) -> IxLabelValue:
    """
    Create new item.
    """

    try:
        item = crud.create_ix_label_value_item(session=session, item_in=item_in)
    except IntegrityError:
        raise HTTPException(status_code=400, detail="Item already")

    return item


@router.post("/link/lab/loc/list/", response_model=str, include_in_schema=False)
def create_ix_label_loc_items(
    *, session: SessionDep, items_in: sc.IxLabelLocCreateList
) -> str:
    """
    Create new items.(Insert Select ... Not Exists)
    """
    msg = crud.create_ix_label_loc_items(session=session, items_in=items_in)
    return msg


@router.post("/link/lab/arc/list/", response_model=str, include_in_schema=False)
def create_ix_label_arc_items(
    *, session: SessionDep, items_in: sc.IxLabelArcCreateList
) -> str:
    """
    Create new items.(Insert Select ... Not Exists)
    """
    msg = crud.create_ix_label_arc_items(session=session, items_in=items_in)

    return msg


@router.post("/link/lab/value/list/", response_model=str, include_in_schema=False)
def create_ix_label_value_items(
    *, session: SessionDep, items_in: sc.IxLabelValueCreateList
) -> str:
    """
    Create new items.(Insert Select ... Not Exists)
    """
    msg = crud.create_ix_label_value_items(session=session, items_in=items_in)

    return msg
