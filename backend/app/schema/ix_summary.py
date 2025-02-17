import datetime
from typing import Dict, List, Optional

import alembic

from app.models import SQLModel


class IxDocumentInfo(SQLModel):

    item_key: str
    document_name: str
    reporting_date: datetime.date
    current_period: Optional[str]
    report_type: str


class IxDocumentInfoList(SQLModel):

    data: list[IxDocumentInfo]
    count: int


class MenuLabel(SQLModel):
    """メニューラベルを表すクラス"""

    attr_value: str
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
class CompanySchema(SQLModel):
    code: str
    name: str
    accountingStandard: str
    fiscalYear: str
    fiscalQuarter: str


class MetricSchema(SQLModel):
    key: str
    name: str
    value: Optional[float]
    unit: Optional[str]


class MetricParentSchema(SQLModel):
    name: str
    order: float
    label: str
    value: Optional[MetricSchema]
    change: Optional[MetricSchema]


class FinancialResponseSchema(SQLModel):
    company: CompanySchema
    metrics: List[MetricParentSchema]


# endregion
