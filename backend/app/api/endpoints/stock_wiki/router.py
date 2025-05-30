from fastapi import APIRouter, HTTPException
from sqlalchemy.exc import IntegrityError

from app.api.deps import SessionDep

from . import crud
from . import schema as sc

router = APIRouter()


@router.post(
    "/",
    response_model=sc.StockWikiCreate,
    include_in_schema=False,
    summary="Wiki概要を挿入する",
)
def create_stock_wiki_item(
    *, item_in: sc.StockWikiCreate, session: SessionDep
) -> sc.StockWikiCreate:
    """
    Create new item.
    """

    try:
        item = crud.create_stock_wiki_item(item_in=item_in, session=session)

        return item
    except IntegrityError as e:
        raise HTTPException(status_code=400, detail="Stock already exists") from e


@router.get(
    "/{code}",
    response_model=sc.StockWikiPublic,
    summary="銘柄コードを指定してWiki概要を取得",
)
def get_stock_wiki_item(*, code: str, session: SessionDep) -> sc.StockWikiPublic:
    """
    Get item.
    """
    item = crud.get_stock_wiki_item(code=code, session=session)

    if item is None:
        raise HTTPException(status_code=404, detail="Stock not found")
    else:
        return sc.StockWikiPublic(
            code=item.code,
            name=item.name,
            description=item.description,
            url=item.url,
        )


@router.get(
    "/", response_model=sc.StockWikisPublicList, summary="全銘柄のWiki概要を取得"
)
def get_stock_wiki_items(*, session: SessionDep) -> sc.StockWikisPublicList:
    """
    Get all items.
    """

    items = crud.get_stock_wiki_items(session=session)

    return items
