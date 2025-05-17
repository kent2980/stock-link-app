from fastapi import APIRouter

from app.api.deps import SessionDep
from app.models import IxNonFraction

from . import crud
from . import schema as sc

router = APIRouter()


@router.post(
    "/ix/non_fraction/",
    response_model=sc.IxNonFractionCreate,
    include_in_schema=False,
)
def create_ix_non_fraction_item(
    *, session: SessionDep, item_in: sc.IxNonFractionCreate
) -> IxNonFraction:
    """
    Create new item.
    """

    item = crud.create_ix_non_fraction_item(session=session, item_in=item_in)

    return item


@router.post("/ix/non_fraction/list/", response_model=str, include_in_schema=False)
def create_ix_non_fraction_items(
    *, session: SessionDep, items_in: sc.IxNonFractionCreateList
) -> str:
    msg = crud.create_ix_non_fraction_items(session=session, items_in=items_in)

    return msg
