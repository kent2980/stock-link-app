from datetime import datetime
from decimal import Decimal

from sqlalchemy import DECIMAL, Column

from app.models import Field, SQLModel


class IxNonFractionCreate(SQLModel):
    """iXBRLの非分数情報を表すクラス"""

    item_key: str | None = Field(max_length=36, min_length=36)
    head_item_key: str = Field(max_length=255)
    context: list[str] = Field(max_length=255)
    decimals: Decimal | None = Field(default=None, sa_column=Column(DECIMAL(5, 2)))
    format: str | None = Field(max_length=255)
    name: str = Field(default=None)
    scale: Decimal | None = Field(default=None, sa_column=Column(DECIMAL(5, 2)))
    sign: str | None = Field(default=None, max_length=255)
    unit_ref: str = Field(max_length=255)
    xsi_nil: bool | None = Field(default=None)
    numeric: Decimal | None = Field(default=None, sa_column=Column(DECIMAL(20, 2)))
    report_type: str | None = Field(max_length=4)
    ixbrl_role: str | None = Field(max_length=255)
    source_file_id: str | None = Field(max_length=36)
    xbrl_type: str = Field(max_length=255)
    display_numeric: str | None = Field(max_length=255)
    display_scale: str | None = Field(max_length=255)


class IxNonFractionPublic(SQLModel):
    """iXBRLの非分数情報を表すクラス"""

    id: int | None
    insert_date: datetime
    update_date: datetime
    head_item_key: str | None
    context: list[str]
    decimals: float | None
    format: str | None
    name: str
    scale: float | None
    sign: str | None
    unit_ref: str | None
    xsi_nil: bool | None
    numeric: float | None
    report_type: str | None
    ixbrl_role: str | None
    source_file_id: str | None
    xbrl_type: str | None
    display_numeric: str | None
    display_scale: str | None


class IxNonFractionsPublic(SQLModel):
    """iXBRLの非分数情報を表すクラス"""

    count: int
    data: list[IxNonFractionPublic]


class IxNonFractionCreateList(SQLModel):
    """iXBRLの非分数情報を作成するためのクラス"""

    data: list[IxNonFractionCreate]


class IxNonFractionAddLabelItemPublic(IxNonFractionPublic):
    """iXBRLの非分数情報を作成するためのクラス"""

    label: str


class IxNonFractionAddLabelItemsPublic(SQLModel):

    count: int
    data: list[IxNonFractionAddLabelItemPublic]
