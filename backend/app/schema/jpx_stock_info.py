from datetime import date
from typing import List, Optional

import sqlmodel

from app.models import Field, SQLModel


class JpxStockInfoCreate(SQLModel):

    input_date: str = Field(max_length=8)
    code: str = Field(max_length=5)
    name: str = Field(max_length=255)
    market_or_type: str = Field(max_length=255)
    industry_33_code: Optional[int] = Field(nullable=True)
    industry_33_name: Optional[str] = Field(max_length=255, nullable=True)
    industry_17_code: Optional[int] = Field(nullable=True)
    industry_17_name: Optional[str] = Field(max_length=255, nullable=True)
    scale_code: Optional[int] = Field(nullable=True)
    scale_name: Optional[str] = Field(max_length=255, nullable=True)


class JpxStockInfosCreateList(SQLModel):

    data: List[JpxStockInfoCreate]


class JpxStockInfoPublic(SQLModel):

    input_date: str
    code: str
    name: str
    market_or_type: str
    industry_33_code: Optional[int]
    industry_33_name: Optional[str]
    industry_17_code: Optional[int]
    industry_17_name: Optional[str]
    scale_code: Optional[int]
    scale_name: Optional[str]


class JpxStockInfosPublicList(SQLModel):

    count: int
    data: List[JpxStockInfoPublic]


class Industry(SQLModel):

    code: int
    name: str


class IndustriesList(SQLModel):

    data: List[Industry]
