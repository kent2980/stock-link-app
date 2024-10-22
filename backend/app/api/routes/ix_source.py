from typing import Any

from fastapi import APIRouter, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlmodel import select

import app.schema as sc
from app.api.deps import SessionDep
from app.models import IxSourceFile

router = APIRouter()


@router.post("/source/", response_model=str)
def create_ix_source_file_item(
    *, session: SessionDep, item_in: sc.ix_source.IxSourceFileCreate
) -> Any:
    """
    Create new item.
    """
    item = IxSourceFile.model_validate(item_in)
    session.add(item)
    session.commit()
    session.refresh(item)

    return f"Item {item.name} created"


@router.post("/source/exist/", response_model=bool)
def create_ix_source_file_item_exists(
    *, session: SessionDep, item_in: sc.ix_source.IxSourceFileCreate
) -> Any:
    """
    Create new item.
    """
    statement = select(IxSourceFile).where(IxSourceFile.name == item_in.name)
    result = session.exec(statement)
    item_exists = result.first()

    if not item_exists:
        new_item = IxSourceFile.model_validate(item_in)
        session.add(new_item)
        session.commit()
        session.refresh(new_item)
        return True

    return False


@router.post("/source/list/", response_model=str)
def create_ix_source_file_items_exists(
    *, session: SessionDep, items_in: sc.ix_source.IxSourceFileCreateList
) -> Any:
    """
    Create new items.(Insert Select ... Not Exists)
    """
    try:

        new_items = []
        for item in items_in.data:
            statement = select(IxSourceFile).where(IxSourceFile.id == item.id)
            result = session.exec(statement)
            item_exists = result.first()

            if not item_exists:
                new_item = IxSourceFile.model_validate(item)
                session.add(new_item)
                new_items.append(new_item)
                session.commit()

        if new_items:
            return f"{len(new_items)} items created"

    except IntegrityError as e:
        session.rollback()
        if "foreign key constraint" in str(e):
            raise HTTPException(status_code=400, detail="Foreign key constraint violated")
        raise HTTPException(status_code=500, detail="Internal Server Error")

    return f"Items already exists"


@router.get("/source/is/{source_file_id}/", response_model=bool)
def get_ix_source_file_item(*, session: SessionDep, source_file_id: str) -> Any:
    """
    Get item.
    """
    statement = select(IxSourceFile).where(IxSourceFile.id == source_file_id)
    result = session.exec(statement)
    item_exists = result.first()

    if item_exists:
        return True

    return False
