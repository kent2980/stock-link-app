from typing import List

from app.models import SQLModel


class MenuLabel(SQLModel):
    """メニューラベルを表すクラス"""

    xlink_from: str
    label: str


class MenuLabelList(SQLModel):
    """メニューラベルのリストを表すクラス"""

    data: List[MenuLabel]
    count: int


class TreeItem(SQLModel):
    """ツリーアイテムを表すクラス"""

    id: int
    xlink_from: str
    xlink_to: str
    attr_value: str
    xlink_arcrole: str
    xlink_order: float
    level: int
    has_children: bool


class TreeItemsList(SQLModel):
    """ツリーアイテムのリストを表すクラス"""

    count: int
    data: List[TreeItem]
