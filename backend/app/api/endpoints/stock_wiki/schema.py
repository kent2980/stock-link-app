from typing import List, Optional

from app.models import Field, SQLModel


class StockWikiCreate(SQLModel):
    """
    StockWikiCreate
    """

    code: str = Field(max_length=5)
    name: str = Field(max_length=255)
    description: Optional[str]
    url: Optional[str] = Field(max_length=255)


class StockWikiPublic(SQLModel):
    """
    StockWikiPublic
    """

    code: str
    name: str
    description: Optional[str]
    url: Optional[str]


class StockWikisPublicList(SQLModel):
    """
    StockWikisPublicList
    """

    count: int
    data: List[StockWikiPublic]
