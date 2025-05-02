from fastapi import APIRouter

from app.api.deps import SessionDep
from app.models import IxPresentationArc, IxPresentationLoc

from . import crud
from . import schema as sc

router = APIRouter()


@router.post(
    "/link/pre/loc/",
    response_model=sc.IxPresentationLocCreate,
    include_in_schema=False,
)
def create_ix_pre_loc_item(
    *, session: SessionDep, item_in: sc.IxPresentationLocCreate
) -> IxPresentationLoc:
    """
    Create new item.
    """
    item = crud.create_ix_pre_loc_item(session=session, item_in=item_in)

    return item


@router.post(
    "/link/pre/arc/",
    response_model=sc.IxPresentationArcCreate,
    include_in_schema=False,
)
def create_ix_pre_arc_item(
    *, session: SessionDep, item_in: sc.IxPresentationArcCreate
) -> IxPresentationArc:
    """
    Create new item.
    """
    item = crud.create_ix_pre_arc_item(session=session, item_in=item_in)

    return item


@router.post("/link/pre/loc/list/", response_model=str, include_in_schema=False)
def create_ix_pre_loc_items(
    *, session: SessionDep, items_in: sc.IxPresentationLocCreateList
) -> str:
    """
    Create new items.(Insert Select ... Not Exists)
    """

    msg = crud.create_ix_pre_loc_items(session=session, items_in=items_in)

    return msg


@router.post("/link/pre/arc/list/", response_model=str, include_in_schema=False)
def create_ix_pre_arc_items(
    *, session: SessionDep, items_in: sc.IxPresentationArcCreateList
) -> str:
    """
    Create new items.(Insert Select ... Not Exists)
    """

    msg = crud.create_ix_pre_arc_items(session=session, items_in=items_in)

    return msg
