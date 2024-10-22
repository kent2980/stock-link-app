from typing import List, Optional

from app.models import Field, SQLModel


# region read_finance_item method
class IxViewFinance(SQLModel):
    """iXBRLの財務情報を公開するためのクラス"""

    is_numeric: Optional[bool] = Field(default=False, description="数値データの有無")
    type: Optional[str] = Field(default=None, description="数値データの種別")
    context: Optional[str] = Field(default=None, description="コンテキスト")
    numeric: Optional[float] = Field(default=None, description="数値データ")
    value: Optional[str] = Field(default=None, description="非数値データ")
    display_scale: Optional[str] = Field(default=None, description="表示スケール")


class IxViewFinances(SQLModel):
    """iXBRLの財務情報を表すクラス"""

    count: int
    data: List[IxViewFinance]


# endregion


# region create_menu_item_tree method
class MenuItem(SQLModel):
    id: int = Field(default=None)
    from_id: Optional[int] = Field(default=None)
    xlink_to: str = Field(default=None)
    xlink_from: Optional[str] = Field(default=None)
    attr_value: str = Field(default=None)
    xlink_arcrole: str = Field(default=None)
    to_href: Optional[str] = Field(default=None)
    from_href: Optional[str] = Field(default=None)
    xlink_order: Optional[float] = Field(default=None)


class MenuItems(SQLModel):
    count: int
    data: List[MenuItem]


class IxViewItems(SQLModel):
    """iXBRLのアイテム情報を公開するためのクラス"""

    label: Optional[str] = Field(default=None, description="ラベル")
    order: Optional[float] = Field(default=None, description="順序")
    arcrole: Optional[str] = Field(default=None, description="アークロール")
    items: Optional[IxViewFinances] = Field(default=None, description="財務情報")


# endregion


class TreeLabel(SQLModel):
    """ツリーラベルを表すクラス"""

    tag: str = Field(default=None, description="treeタグ")
    label: str = Field(default=None, description="日本語ラベル")


class TreeLabels(SQLModel):
    """ツリーラベルのリストを表すクラス"""

    count: int
    data: List[TreeLabel]
