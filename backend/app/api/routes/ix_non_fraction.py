from typing import Any

import app.schema as sc
from app.api.deps import SessionDep
from app.models import IxNonFraction
from fastapi import APIRouter, Query
from sqlalchemy.exc import IntegrityError
from sqlmodel import select

router = APIRouter()


@router.post("/ix/non_fraction/", response_model=sc.ix_non_fraction.IxNonFractionCreate)
def create_ix_non_fraction_item(
    *, session: SessionDep, item_in: sc.ix_non_fraction.IxNonFractionCreate
) -> Any:
    """
    Create new item.
    """

    item = IxNonFraction.model_validate(item_in)
    session.add(item)
    session.commit()
    session.refresh(item)

    return item


@router.post("/ix/non_fraction/list/", response_model=str)
def create_ix_non_fraction_items_exists(
    *, session: SessionDep, items_in: sc.ix_non_fraction.IxNonFractionCreateList
) -> Any:
    """
    Create new items.(Insert Select ... Not Exists)
    """
    new_items = []
    for item in items_in.data:
        statement = select(IxNonFraction).where(
            IxNonFraction.context == item.context,
            IxNonFraction.name == item.name,
            IxNonFraction.xbrl_id == item.xbrl_id,
        )
        result = session.exec(statement)
        item_exists = result.first()

        if not item_exists:
            new_item = IxNonFraction.model_validate(item)
            session.add(new_item)
            new_items.append(new_item)

    if new_items:
        session.commit()
        return f"Items {len(new_items)} created"

    return "Items already exists"


@router.get("/ix/non_fraction/is/{source_file_id}/", response_model=bool)
def is_ix_non_fraction_item_exists(*, session: SessionDep, source_file_id: str) -> Any:
    """
    Check if item exists.
    """
    statement = select(IxNonFraction).where(
        IxNonFraction.source_file_id == source_file_id
    )
    result = session.exec(statement)
    item_exists = result.first()

    if item_exists:
        return True

    return False


@router.get("/isConsolidated/{xbrl_id}/", response_model=bool)
def is_consolidated(*, session: SessionDep, xbrl_id: str) -> Any:
    """
    Check if item exists.
    """
    statement = select(IxNonFraction).where(
        IxNonFraction.xbrl_id == xbrl_id, IxNonFraction.context.like("%_Consolidated%")
    )
    result = session.exec(statement)
    item_exists = result.first()

    if item_exists:
        return True

    return False


@router.delete("/ix/non_fraction/delete/", response_model=bool)
def delete_ix_non_fraction_item(
    *, session: SessionDep, xbrl_id: str = Query(...)
) -> Any:
    """
    Delete item.
    """
    statement = select(IxNonFraction).where(IxNonFraction.xbrl_id == xbrl_id)
    result = session.exec(statement)
    items = result.all()

    if items:
        for item in items:
            session.delete(item)
        session.commit()
        return True

    return False
