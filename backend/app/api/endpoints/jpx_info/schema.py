
from app.models import Field, SQLModel


class JpxStockInfoCreate(SQLModel):

    input_date: str = Field(max_length=8)
    code: str = Field(max_length=5)
    name: str = Field(max_length=255)
    market_or_type: str = Field(max_length=255)
    industry_33_code: int | None = Field(nullable=True)
    industry_33_name: str | None = Field(max_length=255, nullable=True)
    industry_17_code: int | None = Field(nullable=True)
    industry_17_name: str | None = Field(max_length=255, nullable=True)
    scale_code: int | None = Field(nullable=True)
    scale_name: str | None = Field(max_length=255, nullable=True)


class JpxStockInfosCreateList(SQLModel):

    data: list[JpxStockInfoCreate]


class JpxStockInfoPublic(SQLModel):

    input_date: str
    code: str
    name: str
    market_or_type: str
    industry_33_code: int | None
    industry_33_name: str | None
    industry_17_code: int | None
    industry_17_name: str | None
    scale_code: int | None
    scale_name: str | None


class JpxStockInfosPublicList(SQLModel):

    count: int
    data: list[JpxStockInfoPublic]


class Industry(SQLModel):

    code: int
    name: str


class IndustriesList(SQLModel):

    data: list[Industry]


class industry_count(SQLModel):
    code: int
    name: str
    count: int


class industry_count_list(SQLModel):
    data: list[industry_count]
