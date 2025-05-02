from typing import List, Optional

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
    display_scale: Optional[str]
    scale: Optional[int]


class FinValueAbstractBase(SQLModel):
    """メトリック親情報を表すクラス"""

    name: str
    order: float
    label: str
    curValue: Optional[FinValueBase] = Field(default=None)
    curChange: Optional[FinValueBase] = Field(default=None)
    preValue: Optional[FinValueBase] = Field(default=None)
    preChange: Optional[FinValueBase] = Field(default=None)


class FinValueWithProgressRate(FinValueAbstractBase):
    """メトリック親情報を表すクラス"""

    progress_rate: Optional[float]


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
    head_item_key: Optional[str] = Field(default=None)


class FinUpperAndLower(FinStructBase):
    """メトリックの上下限情報を表すクラス"""

    upper: Optional[FinItemsBase] = Field(default=FinItemsBase(context="UpperMember"))
    lower: Optional[FinItemsBase] = Field(default=FinItemsBase(context="LowerMember"))


class FinResultStruct(FinUpperAndLower):

    result: Optional[FinItemsBase] = Field(default=FinItemsBase(context="ResultMember"))


class FinResultOnlyStruct(FinStructBase):

    result: Optional[FinItemsBase] = Field(default=FinItemsBase(context="ResultMember"))


class FinForecastStruct(FinUpperAndLower):

    forecast: Optional[FinItemsBase] = Field(
        default=FinItemsBase(context="ForecastMember")
    )


class LabelBase(SQLModel):

    label: str


class FinResponseBase(SQLModel):

    count: int
    # labels: List[LabelBase]
    data: List[FinStructBase]


class FinResultResponse(FinResponseBase):

    data: List[FinResultStruct]


class FinResultOnlyResponse(FinResponseBase):

    data: List[FinResultOnlyStruct]


class FinForecastResponse(FinResponseBase):

    data: List[FinForecastStruct]


class ForecastProgressRate(SQLModel):

    name: str
    label: str
    value: Optional[float]


class ForecastProgressRateResponse(SQLModel):

    forecast: Optional[List[ForecastProgressRate]]
    upper: Optional[List[ForecastProgressRate]]
    lower: Optional[List[ForecastProgressRate]]


class ForecastAndProgressRate(ForecastProgressRate):

    data: Optional[List[FinValueAbstractBase]]


class ForecastAndProgressRateResponse(SQLModel):

    forecast: Optional[List[ForecastAndProgressRate]]
    lower: Optional[List[ForecastAndProgressRate]]
    upper: Optional[List[ForecastAndProgressRate]]
