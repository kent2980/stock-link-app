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


class IxNonFractionPublic(SQLModel):
    """iXBRLの非分数情報を表すクラス"""

    id: int
    context: List[str]
    name: str
    display_numeric: Optional[str]
    display_scale: Optional[str]
    from_name: str


class IxNonFractionsPublicList(SQLModel):
    """iXBRLの非分数情報のリストを表すクラス"""

    count: int
    data: Dict[str, List[IxNonFractionPublic]]


# region Operating Group
class MetricSchema(SQLModel):
    key: str
    name: str
    value: Optional[float]
    unit: Optional[str]


class MetricParentSchema(SQLModel):
    name: str
    order: float
    label: str
    value: Optional[MetricSchema] = Field(default=None)
    change: Optional[MetricSchema] = Field(default=None)


class PeriodSchema(SQLModel):

    accountingStandard: str
    fiscalYear: str
    period: str


class LabelItemSchema(SQLModel):

    label: str


class MetricItems(SQLModel):
    is_active: bool = Field(default=False)
    data: Optional[List[MetricParentSchema]] = Field(default=[])


class FinancialResponseSchema(SQLModel):
    period: PeriodSchema
    result: MetricItems
    forecast: MetricItems
    upper: MetricItems
    lower: MetricItems


class FinancialResponseListSchema(SQLModel):
    count: int
    labels: List[LabelItemSchema]
    data: List[FinancialResponseSchema]


# endregion
