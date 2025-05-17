from decimal import Decimal

from sqlalchemy import DECIMAL, Column

from app.models import Field, SQLModel


class IxPresentationLocCreate(SQLModel):
    """XBRLの表示リンクロケーションを表すクラス"""

    item_key: str | None = Field(max_length=36, min_length=36)
    head_item_key: str = Field(foreign_key="ix_head_title.item_key", nullable=False)
    attr_value: str | None = Field(max_length=255)
    xlink_href: str | None = Field(nullable=False)
    xlink_type: str | None = Field(max_length=255)
    xlink_schema: str | None = Field(max_length=255)
    xlink_label: str | None = Field(default=None)
    source_file_id: str | None = Field(max_length=36)


class IxPresentationArcCreate(SQLModel):
    """XBRLの表示リンクアークを表すクラス"""

    item_key: str | None = Field(max_length=36, min_length=36)
    head_item_key: str = Field(foreign_key="ix_head_title.item_key", nullable=False)
    attr_value: str | None = Field(max_length=255)
    xlink_order: Decimal | None = Field(default=None, sa_column=Column(DECIMAL(5, 2)))
    xlink_weight: Decimal | None = Field(default=None, sa_column=Column(DECIMAL(5, 2)))
    xlink_type: str | None = Field(max_length=255)
    xlink_arcrole: str | None = Field(max_length=255)
    xlink_to: str | None = Field(default=None)
    xlink_from: str | None = Field(default=None)
    source_file_id: str | None = Field(max_length=36)


class IxPresentationLocCreateList(SQLModel):
    """XBRLの表示リンクロケーションを作成するためのクラス"""

    data: list[IxPresentationLocCreate]


class IxPresentationArcCreateList(SQLModel):
    """XBRLの表示リンクアークを作成するためのクラス"""

    data: list[IxPresentationArcCreate]
