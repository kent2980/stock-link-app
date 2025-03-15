from fastapi import APIRouter, HTTPException
from sqlalchemy.exc import IntegrityError

from app.api.deps import SessionDep

from . import crud
from . import schema as sc

router = APIRouter()


@router.post("/", response_model=sc.StockWikiCreate, include_in_schema=True)
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


@router.get("/{code}", response_model=sc.StockWikiPublic)
def get_stock_wiki_item(*, code: str, session: SessionDep) -> sc.StockWikiPublic:
    """
    Get item.
    """
    item = crud.get_stock_wiki_item(code=code, session=session)

    if item is None:
        return sc.StockWikiPublic(
            code=code,
            error="企業情報が見つかりませんでした。",
        )
    else:
        return sc.StockWikiPublic(
            code=item.code,
            name=item.name,
            description=item.description,
            url=item.url,
        )


@router.get("/", response_model=sc.StockWikisPublicList)
def get_stock_wiki_items(*, session: SessionDep) -> sc.StockWikisPublicList:
    """
    Get all items.
    """

    items = crud.get_stock_wiki_items(session=session)

    return items
