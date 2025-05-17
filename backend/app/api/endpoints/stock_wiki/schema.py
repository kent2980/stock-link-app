from app.models import Field, SQLModel


class StockWikiCreate(SQLModel):
    """
    StockWikiCreate
    """

    code: str = Field(max_length=5)
    name: str = Field(max_length=255)
    description: str | None
    url: str | None = Field(max_length=255)


class StockWikiPublic(SQLModel):
    """
    StockWikiPublic
    """

    code: str
    name: str | None = Field(default=None)
    description: str | None = Field(default=None)
    url: str | None = Field(default=None)
    error: str | None = Field(default=None)


class StockWikisPublicList(SQLModel):
    """
    StockWikisPublicList
    """

    count: int
    data: list[StockWikiPublic]
