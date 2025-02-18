from typing import Any

from fastapi import APIRouter, HTTPException, Query
from sqlmodel import Session, select

from app.api.deps import SessionDep
from app.models import (
    IxFilePath,
    IxHeadTitle,
    IxNonFraction,
    IxNonNumeric,
    IxSourceFile,
    ScLinkBaseRef,
)

from . import crud

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
    models = [
        IxHeadTitle,
        IxFilePath,
        IxNonNumeric,
        IxNonFraction,
        IxSourceFile,
        ScLinkBaseRef,
    ]

    for model in models:
        if not crud.is_exists(
            session=session, model=model, head_item_key=head_item_key
        ):
            raise HTTPException(
                status_code=404,
                detail=f"{model.__name__}に{head_item_key}が存在しません",
            )
    return True
