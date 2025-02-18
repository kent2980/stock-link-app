from typing import Any

from sqlmodel import Session, select


def is_exists(session: Session, model: Any, head_item_key: str) -> bool:
    """モデルにhead_item_keyが存在するか確認する"""
    statement = select(model).where(model.head_item_key == head_item_key)
    result = session.exec(statement)
    item_exists = result.first()

    if item_exists:
        return True
    else:
        return False
