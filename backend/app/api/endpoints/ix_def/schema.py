from decimal import Decimal

from sqlalchemy import DECIMAL, Column

from app.models import Field, SQLModel


class IxDefinitionLocCreate(SQLModel):
    """XBRLの表示リンクロケーションを表すクラス"""

    item_key: str | None = Field(max_length=36, min_length=36)
    head_item_key: str = Field(foreign_key="ix_head_title.item_key", nullable=False)
    attr_value: str | None = Field(max_length=255)
    xlink_href: str | None = Field(nullable=False)
    xlink_type: str | None = Field(max_length=255)
    xlink_schema: str | None = Field(max_length=255)
    xlink_label: str | None = Field(default=None)
    source_file_id: str | None = Field(max_length=36)


class IxDefinitionArcCreate(SQLModel):
    """XBRLの表示リンクアークを表すクラス"""

    item_key: str | None = Field(max_length=36, min_length=36)
    head_item_key: str = Field(foreign_key="ix_head_title.item_key", nullable=False)
    attr_value: str | None = Field(max_length=255)
    xlink_order: Decimal = Field(sa_column=Column(DECIMAL(5, 2)))
    xlink_weight: Decimal | None = Field(default=None, sa_column=Column(DECIMAL(5, 2)))
    xlink_type: str | None = Field(max_length=255)
    xlink_arcrole: str | None = Field(max_length=255)
    xlink_to: str
    xlink_from: str
    source_file_id: str | None = Field(max_length=36)


class IxDefinitionLocCreateList(SQLModel):
    """XBRLの表示リンクロケーションを作成するためのクラス"""

    data: list[IxDefinitionLocCreate]


class IxDefinitionArcCreateList(SQLModel):
    """XBRLの表示リンクアークを作成するためのクラス"""

    data: list[IxDefinitionArcCreate]
