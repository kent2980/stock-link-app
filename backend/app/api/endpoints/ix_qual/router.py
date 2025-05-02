from fastapi import APIRouter

from app.api.deps import SessionDep

from . import crud
from . import schema as sc

router = APIRouter()


@router.post(
    "/qualitative/",
    response_model=sc.IxQualitativePublic,
    include_in_schema=False,
)
def create_ix_qualitative_item(
    *, session: SessionDep, item_in: sc.IxQualitativeCreate
) -> sc.IxQualitativePublic:
    """
    提携情報をIxQualitativeテーブルに登録する

    Raises:
        HTTPException: アイテムが既に存在する場合

    Returns:
        sc.IxQualitativePublic: 登録したアイテム
    """

    item = crud.create_ix_qualitative_item(session=session, item_in=item_in)

    return item


@router.post(
    "/qualitative/list/",
    response_model=sc.IxQualitativePublics,
    include_in_schema=False,
)
def create_ix_qualitative_items(
    *, session: SessionDep, items_in: sc.IxQualitativeCreates
) -> sc.IxQualitativePublics:
    """
    提携情報をIxQualitativeテーブルに登録する

    Raises:
        HTTPException: アイテムが既に存在する場合

    Returns:
        sc.IxQualitativePublics: 登録したアイテム
    """

    items = crud.create_ix_qualitative_items(session=session, items_in=items_in)

    return items
