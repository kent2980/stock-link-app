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
def is_model_checking(*, session: SessionDep, xbrl_id: str = Query(...)) -> bool:
    """XBRL_IDがすべてのテーブルに存在するか確認します

    Properties:
    - session: SessionDep
    - xbrl_id: str

    Returns:
    - bool

    Raises:
    - HTTPException: テーブルにXBRL_IDが存在しない場合
    """

    is_exists(session, IxHeadTitle, xbrl_id)
    is_exists(session, IxFilePath, xbrl_id)
    is_exists(session, IxNonNumeric, xbrl_id)
    is_exists(session, IxNonFraction, xbrl_id)
    is_exists(session, IxSourceFile, xbrl_id)
    is_exists(session, ScLinkBaseRef, xbrl_id)

    return True


def is_exists(session: Session, model: Any, xbrl_id: str) -> bool:
    """モデルにXBRL_IDが存在するか確認する"""
    statement = select(model).where(model.xbrl_id == xbrl_id)
    result = session.exec(statement)
    item_exists = result.first()

    if not item_exists:
        raise HTTPException(
            status_code=400, detail=f"{model.__name__}にXBRL_IDが存在しません"
        )
