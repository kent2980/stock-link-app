from datetime import datetime
from decimal import Decimal
from typing import List, Optional

from sqlalchemy import DECIMAL, Column

from app.models import Field, IxDefinitionArc, SQLModel


class IxDefinitionLocCreate(SQLModel):
    """XBRLの表示リンクロケーションを表すクラス"""

    item_key: Optional[str] = Field(max_length=36, min_length=36)
    head_item_key: str = Field(foreign_key="ix_head_title.item_key", nullable=False)
    attr_value: Optional[str] = Field(max_length=255)
    xlink_href: Optional[str] = Field(nullable=False)
    xlink_type: Optional[str] = Field(max_length=255)
    xlink_schema: Optional[str] = Field(max_length=255)
    xlink_label: Optional[str] = Field(default=None)
    source_file_id: Optional[str] = Field(max_length=36)


class IxDefinitionArcCreate(SQLModel):
    """XBRLの表示リンクアークを表すクラス"""

    item_key: Optional[str] = Field(max_length=36, min_length=36)
    head_item_key: str = Field(foreign_key="ix_head_title.item_key", nullable=False)
    attr_value: Optional[str] = Field(max_length=255)
    xlink_order: Decimal = Field(sa_column=Column(DECIMAL(5, 2)))
    xlink_weight: Optional[Decimal] = Field(
        default=None, sa_column=Column(DECIMAL(5, 2))
    )
    xlink_type: Optional[str] = Field(max_length=255)
    xlink_arcrole: Optional[str] = Field(max_length=255)
    xlink_to: str
    xlink_from: str
    source_file_id: Optional[str] = Field(max_length=36)


class IxDefinitionLocCreateList(SQLModel):
    """XBRLの表示リンクロケーションを作成するためのクラス"""

    data: List[IxDefinitionLocCreate]


class IxDefinitionArcCreateList(SQLModel):
    """XBRLの表示リンクアークを作成するためのクラス"""

    data: List[IxDefinitionArcCreate]


class IxDefinitionArcByAttrValue(SQLModel):
    """XBRLの表示リンクアークを属性値で検索するためのクラス"""

    attr_value: str


class IxDefinitionArcByAttrValueList(SQLModel):
    """XBRLの表示リンクアークを属性値で検索するためのクラス"""

    data: List[str]
    count: int


class IxDefinitionArcPublic(SQLModel):
    """XBRLの表示リンクアークを公開するためのクラス"""

    id: Optional[int]
    insert_date: datetime
    update_date: datetime
    head_item_key: Optional[str]
    attr_value: Optional[str]
    xlink_order: Decimal
    xlink_weight: Optional[Decimal]
    xlink_type: Optional[str]
    xlink_arcrole: Optional[str]
    xlink_to: str
    xlink_from: str
    source_file_id: Optional[str]


class IxDefinitionArcsPublic(SQLModel):
    """XBRLの表示リンクアークを公開するためのクラス"""

    data: list[IxDefinitionArcPublic]
    count: int


class IxDefinitionArcTree(SQLModel):
    """XBRLの表示リンクアークをツリー形式で公開するためのクラス"""

    xlink_from: str
    children: IxDefinitionArc


class ReadElementArc(SQLModel):
    """XBRLの表示リンクアークを読み取るためのクラス"""

    id: int
    from_id: int
    head_item_key: str
    attr_value: str
    xlink_order: Decimal
    xlink_weight: Optional[Decimal]
    xlink_arcrole: str
    arc_xlink_to: str
    xlink_to: str
    xlink_from: str


class MenuLabel(SQLModel):
    """メニューラベルを表すクラス"""

    xlink_from: str
    label: str


class MenuLabelList(SQLModel):
    """メニューラベルのリストを表すクラス"""

    data: List[MenuLabel]
    count: int


class ContextItem(SQLModel):
    """コンテキストアイテムを表すクラス"""

    axis: str
    contexts: List[str]


class RecordFilterItems(SQLModel):
    """レコードフィルターアイテムを表すクラス"""

    attr_value: str
    contextItems: List[ContextItem]
    names: List[str]


class RecordFilterItemsList(SQLModel):
    """レコードフィルターアイテムのリストを表すクラス"""

    data: List[RecordFilterItems]
    count: int
