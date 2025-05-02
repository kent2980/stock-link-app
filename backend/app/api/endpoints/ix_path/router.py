from fastapi import APIRouter

from app.api.deps import SessionDep
from app.models import IxFilePath

from . import crud
from . import schema as sc

router = APIRouter()


@router.post(
    "/ix/file_path/",
    response_model=sc.IxFilePathPublic,
    include_in_schema=False,
)
def create_ix_file_path_item(
    *, session: SessionDep, item_in: sc.IxFilePathCreate
) -> IxFilePath:
    """
    Create new item.
    """
    item = crud.create_ix_file_path_item(session=session, item_in=item_in)

    return item
