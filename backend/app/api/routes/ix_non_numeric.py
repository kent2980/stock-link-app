from typing import Any

import app.schema as sc
from app.api.deps import SessionDep
from app.models import IxNonNumeric
from fastapi import APIRouter, Query
from sqlmodel import select

router = APIRouter()


@router.post("/ix/non_numeric/", response_model=sc.ix_non_numeric.IxNonNumericCreate)
def create_ix_non_numeric_item(
    *, session: SessionDep, item_in: sc.ix_non_numeric.IxNonNumericCreate
) -> Any:
    """
    Create new item.
    """
    item = IxNonNumeric.model_validate(item_in)
    session.add(item)
    session.commit()
    session.refresh(item)

    return item


@router.post("/ix/non_numeric/list/", response_model=str)
def create_ix_non_numeric_items_exists(
    *, session: SessionDep, items_in: sc.ix_non_numeric.IxNonNumericCreateList
) -> Any:
    """
    Create new items.(Insert Select ... Not Exists)
    """
    new_items = []
    for item in items_in.data:
        statement = select(IxNonNumeric).where(
            IxNonNumeric.context == item.context,
            IxNonNumeric.name == item.name,
            IxNonNumeric.head_item_key == item.head_item_key,
        )
        result = session.exec(statement)
        item_exists = result.first()

        if not item_exists:
            new_item = IxNonNumeric.model_validate(item)
            session.add(new_item)
            new_items.append(new_item)

    if new_items:
        session.commit()
        return f"Items {len(new_items)} created"

    return "Items already exists"


@router.get("/ix/non_numeric/is/{source_file_id}/", response_model=bool)
def is_ix_non_numeric_item_exists(*, session: SessionDep, source_file_id: str) -> Any:
    """
    Check if item exists.
    """
    statement = select(IxNonNumeric).where(
        IxNonNumeric.source_file_id == source_file_id
    )
    result = session.exec(statement)
    item_exists = result.first()

    if item_exists:
        return True

    return False


@router.delete("/ix/non_numeric/delete/", response_model=bool)
def delete_ix_non_numeric_item(
    *, session: SessionDep, head_item_key: str = Query(...)
) -> Any:
    """
    Delete item.
    """
    statement = select(IxNonNumeric).where(IxNonNumeric.head_item_key == head_item_key)
    result = session.exec(statement)
    items = result.all()

    if items:
        for item in items:
            session.delete(item)
        session.commit()
        return True

    return False
