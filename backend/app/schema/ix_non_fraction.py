from datetime import datetime
from decimal import Decimal
from typing import List, Optional

from sqlalchemy import DECIMAL, Column

from app.models import Field, SQLModel


class IxNonFractionCreate(SQLModel):
    """iXBRLの非分数情報を表すクラス"""

    xbrl_id: str = Field(max_length=255)
    context: str = Field(max_length=255)
    decimals: Optional[Decimal] = Field(default=None, sa_column=Column(DECIMAL(5, 2)))
    format: Optional[str] = Field(max_length=255)
    name: str = Field(default=None)
    scale: Optional[Decimal] = Field(default=None, sa_column=Column(DECIMAL(5, 2)))
    sign: Optional[str] = Field(default=None, max_length=255)
    unit_ref: str = Field(max_length=255)
    xsi_nil: Optional[bool] = Field(default=None)
    numeric: Optional[Decimal] = Field(default=None, sa_column=Column(DECIMAL(20, 2)))
    report_type: Optional[str] = Field(max_length=4)
    ixbrl_role: Optional[str] = Field(max_length=255)
    source_file_id: Optional[str] = Field(max_length=36)
    xbrl_type: str = Field(max_length=255)
    display_numeric: Optional[str] = Field(max_length=255)
    display_scale: Optional[str] = Field(max_length=255)


class IxNonFractionPublic(SQLModel):
    """iXBRLの非分数情報を表すクラス"""

    id: Optional[int]
    insert_date: datetime
    update_date: datetime
    xbrl_id: Optional[str]
    context: str
    decimals: Optional[Decimal]
    format: Optional[str]
    name: str
    scale: Optional[Decimal]
    sign: Optional[str]
    unit_ref: Optional[str]
    xsi_nil: Optional[bool]
    numeric: Optional[Decimal]
    report_type: Optional[str]
    ixbrl_role: Optional[str]
    source_file_id: Optional[str]
    xbrl_type: Optional[str]
    display_numeric: Optional[str]
    display_scale: Optional[str]


class IxNonFractionsPublic(SQLModel):
    """iXBRLの非分数情報を表すクラス"""

    data: List[IxNonFractionPublic]
    count: int


class IxNonFractionCreateList(SQLModel):
    """iXBRLの非分数情報を作成するためのクラス"""

    data: List[IxNonFractionCreate]


class IxNonFractionAddLabelItemPublic(IxNonFractionPublic):
    """iXBRLの非分数情報を作成するためのクラス"""

    label: str


class IxNonFractionAddLabelItemsPublic(SQLModel):

    data: list[IxNonFractionAddLabelItemPublic]
    count: int
