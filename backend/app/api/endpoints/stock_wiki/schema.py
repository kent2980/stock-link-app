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
    name: Optional[str] = Field(default=None)
    description: Optional[str] = Field(default=None)
    url: Optional[str] = Field(default=None)
    error: Optional[str] = Field(default=None)


class StockWikisPublicList(SQLModel):
    """
    StockWikisPublicList
    """

    count: int
    data: List[StockWikiPublic]
