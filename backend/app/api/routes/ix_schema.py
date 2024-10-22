from typing import Any

from fastapi import APIRouter, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlmodel import select

import app.schema as sc
from app.api.deps import SessionDep
from app.models import ScLinkBaseRef

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
    try:

        new_items = []

        for item in items_in.data:
            statement = select(ScLinkBaseRef).where(
                ScLinkBaseRef.xlink_href == item.xlink_href,
                ScLinkBaseRef.xbrl_id == item.xbrl_id,
                ScLinkBaseRef.href_source_file_id == item.href_source_file_id,
                ScLinkBaseRef.source_file_id == item.source_file_id,
                ScLinkBaseRef.xbrl_type == item.xbrl_type,
            )
            result = session.exec(statement)
            item_exists = result.first()

            if not item_exists:
                new_item = ScLinkBaseRef.model_validate(item)
                session.add(new_item)
                new_items.append(new_item)

        if new_items:
            session.commit()
            return f"Items {new_items} created"

    except IntegrityError as e:
        session.rollback()
        if "foreign key constraint" in str(e):
            raise HTTPException(status_code=400, detail="Foreign key constraint violated")
        raise HTTPException(status_code=500, detail="Internal Server Error")

    return "Items already exists"


@router.get("/schema/linkbase/is/{xbrl_id}/", response_model=bool)
def is_ix_schema_item_exists(*, session: SessionDep, xbrl_id: str) -> Any:
    """
    Check if item exists.
    """
    statement = select(ScLinkBaseRef).where(ScLinkBaseRef.xbrl_id == xbrl_id)
    result = session.exec(statement)
    item_exists = result.first()

    if item_exists:
        return True

    return False
