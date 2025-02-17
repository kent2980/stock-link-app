from typing import Any, List

from fastapi import APIRouter, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlmodel import select

import app.schema as sc
from app.api.deps import SessionDep
from app.models import IxLabelArc, IxLabelLoc, IxLabelValue

router = APIRouter()


@router.post(
    "/link/lab/loc/",
    response_model=sc.ix_label.IxLabelLocCreate,
    include_in_schema=False,
)
def create_ix_label_loc_item(
    *, session: SessionDep, item_in: sc.ix_label.IxLabelLocCreate
) -> Any:
    """
    Create new item.
    """

    source_file_id = item_in.source_file_id

    statement = select(IxLabelLoc).where(IxLabelLoc.source_file_id == source_file_id)
    result = session.exec(statement)
    item_exists = result.first()

    if item_exists:
        raise HTTPException(status_code=400, detail="Item already")

    item = IxLabelLoc.model_validate(item_in)
    session.add(item)
    session.commit()
    session.refresh(item)

    return item


@router.post(
    "/link/lab/arc/",
    response_model=sc.ix_label.IxLabelArcCreate,
    include_in_schema=False,
)
def create_ix_label_arc_item(
    *, session: SessionDep, item_in: sc.ix_label.IxLabelArcCreate
) -> Any:
    """
    Create new item.
    """

    source_file_id = item_in.source_file_id

    statement = select(IxLabelArc).where(IxLabelArc.source_file_id == source_file_id)
    result = session.exec(statement)
    item_exists = result.first()

    if item_exists:
        raise HTTPException(status_code=400, detail="Item already")

    item = IxLabelArc.model_validate(item_in)
    session.add(item)
    session.commit()
    session.refresh(item)

    return item


@router.post(
    "/link/lab/value/",
    response_model=sc.ix_label.IxLabelValueCreate,
    include_in_schema=False,
)
def create_ix_label_value_item(
    *, session: SessionDep, item_in: sc.ix_label.IxLabelValueCreate
) -> Any:
    """
    Create new item.
    """

    source_file_id = item_in.source_file_id

    statement = select(IxLabelValue).where(
        IxLabelValue.source_file_id == source_file_id
    )
    result = session.exec(statement)
    item_exists = result.first()

    if item_exists:
        raise HTTPException(status_code=400, detail="Item already")

    item = IxLabelValue.model_validate(item_in)
    session.add(item)
    session.commit()
    session.refresh(item)

    return item


@router.post("/link/lab/loc/list/", response_model=str, include_in_schema=False)
def create_ix_label_loc_items_exists(
    *, session: SessionDep, items_in: sc.ix_label.IxLabelLocCreateList
) -> Any:
    """
    Create new items.(Insert Select ... Not Exists)
    """
    new_items = [IxLabelLoc.model_validate(item) for item in items_in.data]

    try:
        session.bulk_save_objects(new_items)
        session.commit()
    except IntegrityError:
        session.rollback()
        new_items = []
        for item in items_in.data:
            new_item = IxLabelLoc.model_validate(item)
            session.add(new_item)
            try:
                session.commit()
                session.refresh(new_item)
                new_items.append(new_item)
            except IntegrityError:
                session.rollback()  # コミット失敗時にロールバック

    return f"{len(new_items)} items created."


@router.post("/link/lab/arc/list/", response_model=str, include_in_schema=False)
def create_ix_label_arc_items_exists(
    *, session: SessionDep, items_in: sc.ix_label.IxLabelArcCreateList
) -> Any:
    """
    Create new items.(Insert Select ... Not Exists)
    """
    new_items = [IxLabelArc.model_validate(item) for item in items_in.data]

    try:
        session.bulk_save_objects(new_items)
        session.commit()
    except IntegrityError:
        session.rollback()
        new_items = []
        for item in items_in.data:
            new_item = IxLabelArc.model_validate(item)
            session.add(new_item)
            try:
                session.commit()
                session.refresh(new_item)
                new_items.append(new_item)
            except IntegrityError:
                session.rollback()

    return f"{len(new_items)} items created."


@router.post("/link/lab/value/list/", response_model=str, include_in_schema=False)
def create_ix_label_value_items_exists(
    *, session: SessionDep, items_in: sc.ix_label.IxLabelValueCreateList
) -> Any:
    """
    Create new items.(Insert Select ... Not Exists)
    """
    new_items = [IxLabelValue.model_validate(item) for item in items_in.data]

    try:
        session.bulk_save_objects(new_items)
        session.commit()
    except IntegrityError:
        session.rollback()
        new_items = []
        for item in items_in.data:
            new_item = IxLabelValue.model_validate(item)
            session.add(new_item)
            try:
                session.commit()
                session.refresh(new_item)
                new_items.append(new_item)
            except IntegrityError:
                session.rollback()

    return f"{len(new_items)} items created."


@router.get("/link/lab/loc/is/{source_file_id}/", response_model=bool)
def get_ix_label_loc_item(*, session: SessionDep, source_file_id: str) -> Any:
    """
    Get item.
    """
    statement = select(IxLabelLoc).where(IxLabelLoc.source_file_id == source_file_id)
    result = session.exec(statement)
    item_exists = result.first()

    if item_exists:
        return True

    return False


@router.get("/link/lab/arc/is/{source_file_id}/", response_model=bool)
def get_ix_label_arc_item(*, session: SessionDep, source_file_id: str) -> Any:
    """
    Get item.
    """
    statement = select(IxLabelArc).where(IxLabelArc.source_file_id == source_file_id)
    result = session.exec(statement)
    item_exists = result.first()

    if item_exists:
        return True

    return False


@router.get("/link/lab/value/is/{source_file_id}/", response_model=bool)
def get_ix_label_value_item(*, session: SessionDep, source_file_id: str) -> Any:
    """
    Get item.
    """
    statement = select(IxLabelValue).where(
        IxLabelValue.source_file_id == source_file_id
    )
    result = session.exec(statement)
    item_exists = result.first()

    if item_exists:
        return True

    return False


@router.delete("/link/lab/loc/delete/", response_model=bool, include_in_schema=False)
def delete_ix_label_loc_item(
    *, session: SessionDep, source_file_id_list: List[str]
) -> bool:
    """
    Delete item.
    """
    for source_file_id in source_file_id_list:
        statement = select(IxLabelLoc).where(
            IxLabelLoc.source_file_id == source_file_id
        )
        result = session.exec(statement)
        items = result.all()

        if items:
            for item in items:
                session.delete(item)
            session.commit()

    return True


@router.delete("/link/lab/arc/delete/", response_model=bool, include_in_schema=False)
def delete_ix_label_arc_item(
    *, session: SessionDep, source_file_id_list: List[str]
) -> bool:
    """
    Delete item.
    """
    for source_file_id in source_file_id_list:
        statement = select(IxLabelArc).where(
            IxLabelArc.source_file_id == source_file_id
        )
        result = session.exec(statement)
        items = result.all()

        if items:
            for item in items:
                session.delete(item)
            session.commit()

    return True


@router.delete("/link/lab/value/delete/", response_model=bool, include_in_schema=False)
def delete_ix_label_value_item(
    *, session: SessionDep, source_file_id_list: List[str]
) -> bool:
    """
    Delete item.
    """
    for source_file_id in source_file_id_list:
        statement = select(IxLabelValue).where(
            IxLabelValue.source_file_id == source_file_id
        )
        result = session.exec(statement)
        items = result.all()

        if items:
            for item in items:
                session.delete(item)
            session.commit()

    return True
