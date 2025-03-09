from sqlalchemy.exc import IntegrityError
from sqlmodel import Session, select

from app.models import IxHeadTitle, IxNonFraction, IxNonNumeric

from . import schema as sc


def create_ix_head_title_item(
    *, session: Session, item_in: sc.IxHeadTitleCreate
) -> IxHeadTitle:
    """
    Create new item.
    """
    item = IxHeadTitle.model_validate(item_in)
    session.add(item)
    session.commit()
    session.refresh(item)

    return item


def create_ix_head_title_items(
    *, session: Session, items_in: sc.IxHeadTitleCreateList
) -> str:
    """
    Create new items.(Insert Select ... Not Exists)
    """
    new_items = [IxHeadTitle.model_validate(item) for item in items_in.data]

    try:
        session.bulk_save_objects(new_items)
        session.commit()
    except IntegrityError:
        session.rollback()
        # 一意制約違反の場合は、既存のデータを更新する
        new_items = []
        for item in items_in.data:
            new_item = IxHeadTitle.model_validate(item)
            session.add(new_item)
            try:
                session.commit()
                session.refresh(new_item)
                new_items.append(new_item)
            except IntegrityError:
                session.rollback()  # コミット失敗時にロールバック

    return f"{len(new_items)} items created."


def update_is_active_ix_head_title_item(
    *, session: Session, head_item_key: str
) -> bool:
    """
    Active item.
    """
    statement = select(IxHeadTitle).where(IxHeadTitle.item_key == head_item_key)
    result = session.exec(statement)
    item = result.first()

    is_active = True

    if item is None:
        is_active = False

    if item.report_type.startswith("ed"):
        if item.current_period is None:
            is_active = False

    item.is_active = is_active
    session.add(item)
    session.commit()

    return is_active


def active_is_generate(*, session: Session, head_item_key: str) -> bool:
    """
    Generate item.
    """
    statement = select(IxHeadTitle).where(IxHeadTitle.item_key == head_item_key)
    result = session.exec(statement)
    item = result.first()

    if item is None:
        return False

    item.is_generate = True
    session.add(item)
    session.commit()

    return True


def is_ix_head_title_item_active(*, session: Session, head_item_key: str) -> bool:
    """
    Check if item is active.
    """
    statement = select(IxHeadTitle).where(IxHeadTitle.item_key == head_item_key)
    result = session.exec(statement)
    item = result.first()

    if item:
        if item.is_active:
            return True

    return False


def read_ix_head_title_item(*, session: Session, head_item_key: str) -> IxHeadTitle:
    """
    Get item by head_item_key.
    """
    statement = select(IxHeadTitle).where(IxHeadTitle.item_key == head_item_key)
    result = session.exec(statement)
    item = result.first()

    return item
