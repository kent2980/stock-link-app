from typing import Any

import app.schema as sc
from app.api.deps import SessionDep
from app.models import ScLinkBaseRef
from fastapi import APIRouter, HTTPException, Query
from sqlalchemy.exc import IntegrityError
from sqlmodel import select

router = APIRouter()


@router.post("/schema/linkbase/", response_model=sc.ix_schema.IxSchemaLinkBaseCreate)
def create_ix_schema_linkbase_item(
    *, session: SessionDep, item_in: sc.ix_schema.IxSchemaLinkBaseCreate
) -> Any:
    """
    Create new item.
    """
    item = ScLinkBaseRef.model_validate(item_in)
    session.add(item)
    session.commit()
    session.refresh(item)

    return item


@router.post("/schema/linkbase/list/", response_model=str)
def create_ix_schema_linkbase_items_exists(
    *, session: SessionDep, items_in: sc.ix_schema.IxSchemaLinkBaseCreateList
) -> Any:
    """
    Create new items.(Insert Select ... Not Exists)
    """
    new_items = []
    for item in items_in.data:
        new_item = ScLinkBaseRef.model_validate(item)
        session.add(new_item)
        try:
            session.commit()
            session.refresh(new_item)
            new_items.append(new_item)
        except IntegrityError:
            session.rollback()

    return f"{len(new_items)} items created."


@router.get("/schema/linkbase/is/{head_item_key}/", response_model=bool)
def is_ix_schema_item_exists(*, session: SessionDep, head_item_key: str) -> Any:
    """
    Check if item exists.
    """
    statement = select(ScLinkBaseRef).where(
        ScLinkBaseRef.head_item_key == head_item_key
    )
    result = session.exec(statement)
    item_exists = result.first()

    if item_exists:
        return True

    return False


@router.delete("/schema/linkbase/delete/", response_model=bool)
def delete_ix_schema_item(
    *, session: SessionDep, head_item_key: str = Query(...)
) -> Any:
    """
    Delete item.
    """
    statement = select(ScLinkBaseRef).where(
        ScLinkBaseRef.head_item_key == head_item_key
    )
    result = session.exec(statement)
    item_exists = result.all()

    if item_exists:
        for item in item_exists:
            session.delete(item)
        session.commit()
        return True

    return False
