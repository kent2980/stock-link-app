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
    new_items = [IxNonFraction.model_validate(item) for item in items_in.data]

    try:
        session.bulk_save_objects(new_items)
        session.commit()
    except IntegrityError:
        session.rollback()
        return "Some items already exist or an error occurred."

    return f"{len(new_items)} items created."


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


@router.get("/isConsolidated/{head_item_key}/", response_model=bool)
def is_consolidated(*, session: SessionDep, head_item_key: str) -> Any:
    """
    Check if item exists.
    """
    statement = select(IxNonFraction).where(
        IxNonFraction.head_item_key == head_item_key,
        IxNonFraction.context.like("%_Consolidated%"),
    )
    result = session.exec(statement)
    item_exists = result.first()

    if item_exists:
        return True

    return False


@router.delete("/ix/non_fraction/delete/", response_model=bool)
def delete_ix_non_fraction_item(
    *, session: SessionDep, head_item_key: str = Query(...)
) -> Any:
    """
    Delete item.
    """
    statement = select(IxNonFraction).where(
        IxNonFraction.head_item_key == head_item_key
    )
    result = session.exec(statement)
    items = result.all()

    if items:
        for item in items:
            session.delete(item)
        session.commit()
        return True

    return False
