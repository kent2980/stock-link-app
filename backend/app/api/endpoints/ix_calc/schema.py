from decimal import Decimal

from sqlalchemy import DECIMAL, Column

from app.models import Field, SQLModel


class IxCalculationLocCreate(SQLModel):
    """iXBRLの計算ロケーション情報を表すクラス"""

    item_key: str | None = Field(max_length=36, min_length=36)
    head_item_key: str = Field(foreign_key="ix_head_title.item_key", nullable=False)
    attr_value: str | None = Field(max_length=255)
    xlink_href: str | None = Field(nullable=False)
    xlink_type: str | None = Field(max_length=255)
    xlink_schema: str | None = Field(max_length=255)
    xlink_label: str | None = Field(default=None)
    source_file_id: str | None = Field(max_length=36)


class IxCalculationArcCreate(SQLModel):
    """iXBRLの計算アーク情報を表すクラス"""

    item_key: str | None = Field(max_length=36, min_length=36)
    head_item_key: str = Field(foreign_key="ix_head_title.item_key", nullable=False)
    attr_value: str | None = Field(max_length=255)
    xlink_order: Decimal | None = Field(
        default=None, sa_column=Column(DECIMAL(5, 2))
    )
    xlink_weight: Decimal | None = Field(
        default=None, sa_column=Column(DECIMAL(5, 2))
    )
    xlink_type: str | None = Field(max_length=255)
    xlink_arcrole: str | None = Field(max_length=255)
    xlink_to: str | None = Field(default=None)
    xlink_from: str | None = Field(default=None)
    source_file_id: str | None = Field(max_length=36)


class IxCalculationLocCreateList(SQLModel):
    """iXBRLの計算ロケーション情報を作成するためのクラス"""

    data: list[IxCalculationLocCreate]


class IxCalculationArcCreateList(SQLModel):
    """iXBRLの計算アーク情報を作成するためのクラス"""

    data: list[IxCalculationArcCreate]
