from typing import Any

from app.api.deps import SessionDep
from app.models import (
    IxFilePath,
    IxHeadTitle,
    IxNonFraction,
    IxNonNumeric,
    IxSourceFile,
    ScLinkBaseRef,
)
from fastapi import APIRouter, HTTPException, Query
from sqlmodel import Session, select

router = APIRouter()


@router.get("/model/", response_model=bool)
def is_model_checking(*, session: SessionDep, head_item_key: str = Query(...)) -> bool:
    """head_item_keyがすべてのテーブルに存在するか確認します

    Properties:
    - session: SessionDep
    - head_item_key: str

    Returns:
    - bool

    Raises:
    - HTTPException: テーブルにhead_item_keyが存在しない場合
    """

    is_exists(session, IxHeadTitle, head_item_key)
    is_exists(session, IxFilePath, head_item_key)
    is_exists(session, IxNonNumeric, head_item_key)
    is_exists(session, IxNonFraction, head_item_key)
    is_exists(session, IxSourceFile, head_item_key)
    is_exists(session, ScLinkBaseRef, head_item_key)

    return True


def is_exists(session: Session, model: Any, head_item_key: str) -> bool:
    """モデルにhead_item_keyが存在するか確認する"""
    statement = select(model).where(model.head_item_key == head_item_key)
    result = session.exec(statement)
    item_exists = result.first()

    if not item_exists:
        raise HTTPException(
            status_code=400, detail=f"{model.__name__}にhead_item_keyが存在しません"
        )
