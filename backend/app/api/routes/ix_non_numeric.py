from typing import Any

from fastapi import APIRouter
from sqlmodel import select

import app.schema as sc
from app.api.deps import SessionDep
from app.models import IxNonNumeric

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
            IxNonNumeric.xbrl_id == item.xbrl_id,
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
