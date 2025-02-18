from sqlalchemy.exc import IntegrityError
from sqlmodel import Session, select

from app.models import IxCalculationArc, IxCalculationLoc

from . import schema as sc


def create_ix_cal_loc_item(session: Session, item_in: sc.IxCalculationLocCreate):
    item = IxCalculationLoc.model_validate(item_in)
    session.add(item)
    session.commit()
    session.refresh(item)
    return item


def create_ix_cal_arc_item(session: Session, item_in: sc.IxCalculationArcCreate):
    item = IxCalculationArc.model_validate(item_in)
    session.add(item)
    session.commit()
    session.refresh(item)
    return item


def create_ix_cal_loc_items(
    session: Session, items_in: sc.IxCalculationLocCreateList
) -> str:
    new_items = [IxCalculationLoc.model_validate(item) for item in items_in.data]

    try:
        session.bulk_save_objects(new_items)
        session.commit()
    except IntegrityError:
        session.rollback()
        # 一意制約違反が発生した場合、個別に追加を試みる
        new_items = []
        for item in items_in.data:
            new_item = IxCalculationLoc.model_validate(item)
            session.add(new_item)
            try:
                session.commit()
                session.refresh(new_item)
                new_items.append(new_item)
            except IntegrityError:
                session.rollback()  # コミット失敗時にロールバック

    return f"{len(new_items)} items created."


def create_ix_cal_arc_items(
    session: Session, items_in: sc.IxCalculationArcCreateList
) -> str:
    new_items = [IxCalculationArc.model_validate(item) for item in items_in.data]

    try:
        session.bulk_save_objects(new_items)
        session.commit()
    except IntegrityError:
        session.rollback()
        # 一意制約違反が発生した場合、個別に追加を試みる
        new_items = []
        for item in items_in.data:
            new_item = IxCalculationArc.model_validate(item)
            session.add(new_item)
            try:
                session.commit()
                session.refresh(new_item)
                new_items.append(new_item)
            except IntegrityError:
                session.rollback()

    return f"{len(new_items)} items created."
