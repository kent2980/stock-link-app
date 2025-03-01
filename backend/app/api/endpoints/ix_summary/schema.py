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
    context: Optional[str] = Field(default=None)


class FinStructBase(SQLModel):
    """ファイナンシャルレスポンス情報を表すクラス"""

    period: Optional[PeriodSchemaBase] = Field(default=None)
    upper: Optional[FinItemsBase] = Field(default=FinItemsBase(context="UpperMember"))
    lower: Optional[FinItemsBase] = Field(default=FinItemsBase(context="LowerMember"))


class FinResultStruct(FinStructBase):

    result: Optional[FinItemsBase] = Field(default=FinItemsBase(context="ResultMember"))


class FinForecastStruct(FinStructBase):

    forecast: Optional[FinItemsBase] = Field(
        default=FinItemsBase(context="ForecastMember")
    )


class LabelBase(SQLModel):

    label: str


class FinResponseBase(SQLModel):

    count: int
    labels: List[LabelBase]
    data: List[FinStructBase]


class FinResultResponse(FinResponseBase):

    data: List[FinResultStruct]


class FinForecastResponse(FinResponseBase):

    data: List[FinForecastStruct]
