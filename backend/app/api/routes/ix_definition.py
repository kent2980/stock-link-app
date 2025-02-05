from typing import Any

import sqlalchemy
import sqlalchemy.orm
from fastapi import APIRouter, HTTPException, Query
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import aliased
from sqlalchemy.sql import func
from sqlmodel import and_, select

import app.schema as sc
from app.api.deps import SessionDep
from app.models import IxDefinitionArc, IxDefinitionLoc, IxLabelValue, ScLinkBaseRef
from app.schema.ix_schema import IxSchemaLinkBasePublic

router = APIRouter()


@router.post("/link/def/loc/", response_model=sc.ix_def.IxDefinitionLocCreate)
def create_ix_def_loc_item(
    *, session: SessionDep, item_in: sc.ix_def.IxDefinitionLocCreate
) -> Any:
    """
    Create new item.
    """

    item = IxDefinitionLoc.model_validate(item_in)
    session.add(item)
    session.commit()
    session.refresh(item)

    return item


@router.post("/link/def/arc/", response_model=sc.ix_def.IxDefinitionArcCreate)
def create_ix_def_arc_item(
    *, session: SessionDep, item_in: sc.ix_def.IxDefinitionArcCreate
) -> Any:
    """
    Create new item.
    """
    item = IxDefinitionArc.model_validate(item_in)
    session.add(item)
    session.commit()
    session.refresh(item)

    return item


@router.post("/link/def/loc/list/", response_model=str)
def create_ix_def_loc_items_exists(
    *, session: SessionDep, items_in: sc.ix_def.IxDefinitionLocCreateList
) -> Any:
    """
    Create new items.(Insert Select ... Not Exists)
    """
    new_items = [IxDefinitionLoc.model_validate(item) for item in items_in.data]

    try:
        session.bulk_save_objects(new_items)
        session.commit()
    except IntegrityError:
        session.rollback()
        # 一意制約違反が発生した場合、個別に追加を試みる
        new_items = []
        for item in items_in.data:
            new_item = IxDefinitionLoc.model_validate(item)
            session.add(new_item)
            try:
                session.commit()
                session.refresh(new_item)
                new_items.append(new_item)
            except IntegrityError:
                session.rollback()  # コミット失敗時にロールバック

    return f"{len(new_items)} items created."


@router.post("/link/def/arc/list/", response_model=str)
def create_ix_def_arc_items_exists(
    *, session: SessionDep, items_in: sc.ix_def.IxDefinitionArcCreateList
) -> Any:
    """
    Create new items.(Insert Select ... Not Exists)
    """
    new_items = [IxDefinitionArc.model_validate(item) for item in items_in.data]

    try:
        session.bulk_save_objects(new_items)
        session.commit()
    except IntegrityError:
        session.rollback()
        # 一意制約違反が発生した場合、個別に追加を試みる
        new_items = []
        for item in items_in.data:
            new_item = IxDefinitionArc.model_validate(item)
            session.add(new_item)
            try:
                session.commit()
                session.refresh(new_item)
                new_items.append(new_item)
            except IntegrityError:
                session.rollback()

    return f"{len(new_items)} items created."


@router.get("/link/def/loc/is/{source_file_id}/", response_model=bool)
def get_ix_def_loc_item(*, session: SessionDep, source_file_id: str) -> Any:
    """
    Get item.
    """
    statement = select(IxDefinitionLoc).where(
        IxDefinitionLoc.source_file_id == source_file_id
    )
    result = session.exec(statement)
    item = result.first()

    if item:
        return True

    return False


@router.get("/link/def/arc/is/{source_file_id}/", response_model=bool)
def get_ix_def_arc_item(*, session: SessionDep, source_file_id: str) -> Any:
    """
    Get item.
    """
    statement = select(IxDefinitionArc).where(
        IxDefinitionArc.source_file_id == source_file_id
    )
    result = session.exec(statement)
    item = result.first()

    if item:
        return True

    return False


@router.delete("/link/def/loc/delete/", response_model=bool)
def delete_ix_def_loc_item(
    *, session: SessionDep, head_item_key: str = Query(...)
) -> Any:
    """
    Delete item.
    """
    statement = select(IxDefinitionLoc).where(
        IxDefinitionLoc.head_item_key == head_item_key
    )
    result = session.exec(statement)
    items = result.all()

    if items is None:
        return False

    for item in items:
        session.delete(item)

    session.commit()

    return True


@router.delete("/link/def/arc/delete/", response_model=bool)
def delete_ix_def_arc_item(
    *, session: SessionDep, head_item_key: str = Query(...)
) -> Any:
    """
    Delete item.
    """
    statement = select(IxDefinitionArc).where(
        IxDefinitionArc.head_item_key == head_item_key
    )
    result = session.exec(statement)
    items = result.all()

    if items is None:
        return False

    for item in items:
        session.delete(item)

    session.commit()

    return True


@router.get("/menu_labels/{head_item_key}", response_model=sc.ix_def.MenuLabelList)
def read_menu_labels(
    *, head_item_key: str, session: SessionDep
) -> sc.ix_def.MenuLabelList:
    """
    Get all items.
    """

    statement1 = (
        select(ScLinkBaseRef.href_source_file_id)
        .where(
            ScLinkBaseRef.head_item_key == head_item_key,
            ScLinkBaseRef.xbrl_type == "sm",
            ScLinkBaseRef.xlink_role
            == "http://www.xbrl.org/2003/role/definitionLinkbaseRef",
        )
        .subquery()
    )
    statement = (
        select(IxDefinitionArc.xlink_from, IxLabelValue.label)
        .join(
            statement1,
            IxDefinitionArc.source_file_id == statement1.c.href_source_file_id,
        )
        .join(
            IxLabelValue,
            IxLabelValue.xlink_label.startswith(
                "label_" + func.replace(IxDefinitionArc.xlink_from, "tse-ed-t_", "")
            ),
        )
        .where(
            IxDefinitionArc.xlink_arcrole == "http://xbrl.org/int/dim/arcrole/all",
            IxLabelValue.xlink_role == "http://www.xbrl.org/2003/role/label",
            IxDefinitionArc.xlink_from.not_like("%DocumentEntityInformationHeading%"),
        )
        .order_by(IxDefinitionArc.id)
    )

    result = session.exec(statement)
    items = result.all()

    if items is None:
        return sc.ix_def.MenuLabelList(data=[])

    return sc.ix_def.MenuLabelList(data=items, count=len(items))


@router.get(
    "/record_filter_items/{head_item_key}",
    response_model=sc.ix_def.RecordFilterItemsList,
)
def read_record_filter_items(
    *, head_item_key: str, attr_value: str = Query(None), session: SessionDep
) -> sc.ix_def.RecordFilterItemsList:
    """
    Get all items.
    """
    loc2 = aliased(IxDefinitionLoc)
    statement = (
        select(IxDefinitionArc, IxDefinitionLoc, loc2)
        .join(
            ScLinkBaseRef,
            IxDefinitionArc.source_file_id == ScLinkBaseRef.href_source_file_id,
        )
        .join(
            IxDefinitionLoc,
            and_(
                IxDefinitionArc.source_file_id == IxDefinitionLoc.source_file_id,
                IxDefinitionArc.xlink_to == IxDefinitionLoc.xlink_label,
                IxDefinitionArc.attr_value == IxDefinitionLoc.attr_value,
            ),
        )
        .join(
            loc2,
            and_(
                IxDefinitionArc.source_file_id == loc2.source_file_id,
                IxDefinitionArc.xlink_from == loc2.xlink_label,
                IxDefinitionArc.attr_value == loc2.attr_value,
            ),
        )
        .where(
            ScLinkBaseRef.head_item_key == head_item_key,
            ScLinkBaseRef.xbrl_type == "sm",
            ~IxDefinitionArc.xlink_arcrole.in_(
                [
                    "http://xbrl.org/int/dim/arcrole/all",
                    "http://xbrl.org/int/dim/arcrole/hypercube-dimension",
                ]
            ),
        )
    )
    if attr_value:
        statement = statement.where(IxDefinitionArc.attr_value == attr_value)
    result = session.exec(statement)
    items = result.all()

    if items is None:
        raise HTTPException(status_code=404, detail="Items not found")

    records = []
    contexts = {}
    names = {}
    attr_values = set()
    for item in items:
        attr_value = item[0].attr_value
        xlink_to = item[1].xlink_href
        xlink_from = item[2].xlink_href.split("_")[-1]
        arcrole = item[0].xlink_arcrole
        attr_values.add(attr_value)
        if contexts.get(attr_value) is None:
            contexts[attr_value] = {}
        if names.get(attr_value) is None:
            names[attr_value] = []
        arcrole = item[0].xlink_arcrole
        if arcrole == "http://xbrl.org/int/dim/arcrole/dimension-domain":
            if contexts[attr_value].get(xlink_from) is None:
                contexts[attr_value][xlink_from] = []
            contexts[attr_value][xlink_from].append(xlink_to.split("_")[-1])
        elif arcrole == "http://xbrl.org/int/dim/arcrole/domain-member":
            names[attr_value].append(xlink_to)

    for attr_value in attr_values:
        # ContextItemのリストに変換
        context_items_list = [
            {"axis": k, "contexts": v} for k, v in contexts[attr_value].items()
        ]
        records.append(
            {
                "attr_value": attr_value,
                "contextItems": context_items_list,
                "names": names[attr_value],
            }
        )

    return sc.ix_def.RecordFilterItemsList(data=records, count=len(records))
