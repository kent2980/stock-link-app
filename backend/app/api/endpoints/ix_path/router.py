from typing import Any, Optional

from fastapi import APIRouter, HTTPException, Query
from sqlmodel import select

from app.api.deps import SessionDep
from app.models import IxFilePath

from . import schema as sc

router = APIRouter()


@router.post(
    "/ix/file_path/",
    response_model=sc.IxFilePathPublic,
    include_in_schema=False,
)
def create_ix_file_path_item(
    *, session: SessionDep, item_in: sc.IxFilePathCreate
) -> Any:
    """
    Create new item.
    """
    item = IxFilePath.model_validate(item_in)
    session.add(item)
    session.commit()
    session.refresh(item)

    return item


@router.get("/is/file_path/", response_model=bool)
def is_ix_file_path_item_exists(
    *,
    session: SessionDep,
    head_item_key: Optional[str] = Query(None),
    file_path: Optional[str] = Query(None),
) -> Any:
    """head_item_keyまたは、ファイルパスを指定して、レコードが存在するか確認する"""

    if head_item_key is None and file_path is None:
        raise HTTPException(
            status_code=400,
            detail="head_item_keyまたは、ファイルパスを指定してください",
        )

    if head_item_key is not None and file_path is not None:
        raise HTTPException(
            status_code=400,
            detail="head_item_keyまたは、ファイルパスのどちらか一方を指定してください",
        )

    if head_item_key is not None:
        statement = select(IxFilePath).where(IxFilePath.head_item_key == head_item_key)

    if file_path is not None:
        statement = select(IxFilePath).where(IxFilePath.path == file_path)

    result = session.exec(statement)
    item_exists = result.first()

    if item_exists:
        return True

    return False


@router.delete("/ix/file_path/delete/", response_model=bool, include_in_schema=False)
def delete_ix_file_path_item(
    *, session: SessionDep, file_path: str = Query(...)
) -> Any:
    """
    Delete item.
    """
    statement = select(IxFilePath).where(IxFilePath.path == file_path)
    result = session.exec(statement)
    item = result.first()

    if item is None:
        return False

    try:
        session.delete(item)
        session.commit()
    except Exception as e:
        raise HTTPException(status_code=400, detail="削除に失敗しました")

    return True
