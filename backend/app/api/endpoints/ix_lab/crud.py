from sqlalchemy.exc import IntegrityError
from sqlmodel import Session, select

from app.models import IxLabelArc, IxLabelLoc, IxLabelValue

from . import schema as sc


def create_ix_label_loc_item(
    *, session: Session, item_in: sc.IxLabelLocCreate
) -> IxLabelLoc:
    """
    #### IxLabelLocの新規作成
    - **機能**: IxLabelLocの新規作成
    - **戻り値**: IxLabelLoc
    - **例外**: sqlalchemy.exc.IntegrityError
    - **param1**: session: Session
    - **param2**: item_in: sc.IxLabelLocCreate
    """

    item = IxLabelLoc.model_validate(item_in)
    session.add(item)
    session.commit()
    session.refresh(item)

    return item


def create_ix_label_arc_item(
    *, session: Session, item_in: sc.IxLabelArcCreate
) -> IxLabelArc:
    """
    #### IxLabelArcの新規作成
    - **機能**: IxLabelArcの新規作成
    - **戻り値**: IxLabelArc
    - **例外**: sqlalchemy.exc.IntegrityError
    - **param1**: session: Session
    - **param2**: item_in: sc.IxLabelArcCreate
    """

    item = IxLabelArc.model_validate(item_in)
    session.add(item)
    session.commit()
    session.refresh(item)

    return item


def create_ix_label_value_item(
    *, session: Session, item_in: sc.IxLabelValueCreate
) -> IxLabelValue:
    """
    #### IxLabelValueの新規作成
    - **機能**: IxLabelValueの新規作成
    - **戻り値**: IxLabelValue
    - **例外**: sqlalchemy.exc.IntegrityError
    - **param1**: session: Session
    - **param2**: item_in: sc.IxLabelValueCreate
    """

    item = IxLabelValue.model_validate(item_in)
    session.add(item)
    session.commit()
    session.refresh(item)

    return item


def create_ix_label_loc_items(
    *, session: Session, items_in: sc.IxLabelLocCreateList
) -> str:
    """
    #### 複数のIxLabelLocの新規作成
    - **機能**: 複数のIxLabelLocの新規作成
    - **戻り値**: str
    - **param1**: session: Session
    - **param2**: items_in: sc.IxLabelLocCreateList
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


def create_ix_label_arc_items(
    *, session: Session, items_in: sc.IxLabelArcCreateList
) -> str:
    """
    #### 複数のIxLabelArcの新規作成
    - **機能**: 複数のIxLabelArcの新規作成
    - **戻り値**: str
    - **param1**: session: Session
    - **param2**: items_in: sc.IxLabelArcCreateList
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


def create_ix_label_value_items(
    *, session: Session, items_in: sc.IxLabelValueCreateList
) -> str:
    """
    #### 複数のIxLabelValueの新規作成
    - **機能**: 複数のIxLabelValueの新規作成
    - **戻り値**: str
    - **param1**: session: Session
    - **param2**: items_in: sc.IxLabelValueCreateList
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
