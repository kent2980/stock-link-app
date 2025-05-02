from typing import Any

from fastapi import APIRouter

from app.api.deps import SessionDep
from app.models import IxDefinitionArc

from . import crud
from . import schema as sc

router = APIRouter()


@router.post(
    "/link/def/loc/",
    response_model=sc.IxDefinitionLocCreate,
    include_in_schema=False,
)
def create_ix_def_loc_item(
    *, session: SessionDep, item_in: sc.IxDefinitionLocCreate
) -> IxDefinitionArc:
    """
    Create new item.
    """

    item = crud.create_ix_def_loc_item(session=session, item_in=item_in)

    return item


@router.post(
    "/link/def/arc/",
    response_model=sc.IxDefinitionArcCreate,
    include_in_schema=False,
)
def create_ix_def_arc_item(
    *, session: SessionDep, item_in: sc.IxDefinitionArcCreate
) -> IxDefinitionArc:
    """
    Create new item.
    """
    item = crud.create_ix_def_arc_item(session=session, item_in=item_in)

    return item


@router.post("/link/def/loc/list/", response_model=str, include_in_schema=False)
def create_ix_def_loc_items(
    *, session: SessionDep, items_in: sc.IxDefinitionLocCreateList
) -> Any:
    """
    Create new items.(Insert Select ... Not Exists)
    """
    msg = crud.create_ix_def_loc_items(session=session, items_in=items_in)

    return msg


@router.post("/link/def/arc/list/", response_model=str, include_in_schema=False)
def create_ix_def_arc_items(
    *, session: SessionDep, items_in: sc.IxDefinitionArcCreateList
) -> Any:
    """
    Create new items.(Insert Select ... Not Exists)
    """
    msg = crud.create_ix_def_arc_items(session=session, items_in=items_in)

    return msg


3
