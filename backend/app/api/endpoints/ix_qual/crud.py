from sqlalchemy.exc import IntegrityError
from sqlmodel import Session

from app.models import IxQualitative

from . import schema as sc


def create_ix_qualitative_item(
    *, session: Session, item_in: sc.IxQualitativeCreate
) -> sc.IxQualitativePublic:
    """
    提携情報をIxQualitativeテーブルに登録する

    Raises:
        HTTPException: アイテムが既に存在する場合

    Returns:
        sc.IxQualitativePublic: 登録したアイテム
    """

    item = IxQualitative.model_validate(item_in)
    session.add(item)
    session.commit()
    session.refresh(item)

    return item


def create_ix_qualitative_items(
    *, session: Session, items_in: sc.IxQualitativeCreates
) -> sc.IxQualitativePublics:
    """
    提携情報をIxQualitativeテーブルに登録する

    Raises:
        HTTPException: アイテムが既に存在する場合

    Returns:
        sc.IxQualitativePublics: 登録したアイテム
    """

    new_items = [IxQualitative.model_validate(item) for item in items_in.data]

    try:
        session.bulk_save_objects(new_items)
        session.commit()
    except IntegrityError:
        session.rollback()
        new_items = []
        for item in items_in.data:
            new_item = IxQualitative.model_validate(item)
            session.add(new_item)
            try:
                session.commit()
                session.refresh(new_item)
                new_items.append(new_item)
            except IntegrityError:
                session.rollback()  # コミット失敗時にロールバック

    return sc.IxQualitativePublics(count=len(new_items), data=new_items)
