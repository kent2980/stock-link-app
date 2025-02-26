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


class MetricSchema(SQLModel):
    """メトリック情報を表すクラス"""

    name: str
    value: Optional[float]
    unit: Optional[str]


class MetricParentSchema(SQLModel):
    """メトリック親情報を表すクラス"""

    name: str
    order: float
    label: str
    value: Optional[MetricSchema] = Field(default=None)
    change: Optional[MetricSchema] = Field(default=None)


class PeriodSchema(SQLModel):
    """期間情報を表すクラス"""

    accountingStandard: str
    fiscalYear: str
    period: str


class MetricItems(SQLModel):
    """メトリック情報のリストを表すクラス"""

    is_active: bool = Field(default=False)
    data: Optional[List[MetricParentSchema]] = Field(default=[])


class FinancialResponseSchema(SQLModel):
    """ファイナンシャルレスポンス情報を表すクラス"""

    period: PeriodSchema
    result: MetricItems
    forecast: MetricItems
    upper: MetricItems
    lower: MetricItems


class LabelItemSchema(SQLModel):

    label: str


class FinancialResponseListSchema(SQLModel):

    count: int
    labels: List[LabelItemSchema]
    data: List[FinancialResponseSchema]
