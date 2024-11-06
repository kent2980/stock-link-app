from typing import Any, Optional

import app.schema as sc
from app.api.deps import SessionDep
from app.models import IxFilePath
from fastapi import APIRouter, HTTPException, Query
from sqlmodel import select

router = APIRouter()


@router.post("/ix/file_path/", response_model=sc.ix_file_path.IxFilePathPublic)
def create_ix_file_path_item(
    *, session: SessionDep, item_in: sc.ix_file_path.IxFilePathCreate
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
    xbrl_id: Optional[str] = Query(None),
    file_path: Optional[str] = Query(None),
) -> Any:
    """XBRL_IDまたは、ファイルパスを指定して、レコードが存在するか確認する"""

    if xbrl_id is None and file_path is None:
        raise HTTPException(
            status_code=400, detail="XBRL_IDまたは、ファイルパスを指定してください"
        )

    if xbrl_id is not None and file_path is not None:
        raise HTTPException(
            status_code=400,
            detail="XBRL_IDまたは、ファイルパスのどちらか一方を指定してください",
        )

    if xbrl_id is not None:
        statement = select(IxFilePath).where(IxFilePath.xbrl_id == xbrl_id)

    if file_path is not None:
        statement = select(IxFilePath).where(IxFilePath.path == file_path)

    result = session.exec(statement)
    item_exists = result.first()

    if item_exists:
        return True

    return False


@router.delete("/ix/file_path/delete/", response_model=bool)
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
