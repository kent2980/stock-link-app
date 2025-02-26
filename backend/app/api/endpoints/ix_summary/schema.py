import datetime
from typing import Any, Dict, List, Optional

from sqlmodel import Field, SQLModel


class TreeItem(SQLModel):
    """ツリーアイテムを表すクラス"""

    id: int
    xlink_from: str
    xlink_to: str
    to_label: str
    attr_value: str
    xlink_arcrole: str
    xlink_order: float
    level: int
    has_children: bool


class TreeItemsList(SQLModel):
    """ツリーアイテムのリストを表すクラス"""

    count: int
    data: List[TreeItem]


class FinValueBase(SQLModel):
    """メトリック情報を表すクラス"""

    name: str
    value: Optional[float]
    unit: Optional[str]


class FinValueAbstractBase(SQLModel):
    """メトリック親情報を表すクラス"""

    name: str
    order: float
    label: str
    value: Optional[FinValueBase] = Field(default=None)
    change: Optional[FinValueBase] = Field(default=None)


class PeriodSchemaBase(SQLModel):
    """期間情報を表すクラス"""

    accountingStandard: str
    fiscalYear: str
    period: str


class FinItemsBase(SQLModel):
    """メトリック情報のリストを表すクラス"""

    is_active: bool = Field(default=False)
    data: Optional[List[FinValueAbstractBase]] = Field(default=[])


class FinStructBase(SQLModel):
    """ファイナンシャルレスポンス情報を表すクラス"""

    period: PeriodSchemaBase
    result: FinItemsBase
    forecast: FinItemsBase
    upper: FinItemsBase
    lower: FinItemsBase


class LabelBase(SQLModel):

    label: str


class FinResponseBase(SQLModel):

    count: int
    labels: List[LabelBase]
    data: List[FinStructBase]
