from typing import List, Optional

import alembic
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


class FinValueWithChange(SQLModel):

    isActive: Optional[bool] = Field(default=False)
    curValue: Optional[FinValueBase] = Field(default=None)
    curChange: Optional[FinValueBase] = Field(default=None)
    preValue: Optional[FinValueBase] = Field(default=None)
    preChange: Optional[FinValueBase] = Field(default=None)
    context: Optional[str] = Field(default=None)


class FinValueAbstractBase(SQLModel):
    """メトリック親情報を表すクラス"""

    name: str
    order: float
    label: str


class FinValueFinance(FinValueAbstractBase):
    """メトリック親情報を表すクラス"""

    result: Optional[FinValueWithChange] = Field(
        default=FinValueWithChange(context="ResultMember")
    )
    forecast: Optional[FinValueWithChange] = Field(
        default=FinValueWithChange(context="ForecastMember")
    )
    upper: Optional[FinValueWithChange] = Field(
        default=FinValueWithChange(context="UpperMember")
    )
    lower: Optional[FinValueWithChange] = Field(
        default=FinValueWithChange(context="LowerMember")
    )


class FinValueWithDividends(SQLModel):
    """配当のメトリック情報を表すクラス"""

    isActive: Optional[bool] = Field(default=False)
    label: Optional[str] = Field(default=None)
    result: Optional[FinValueWithChange] = Field(
        default=FinValueWithChange(context="ResultMember")
    )
    forecast: Optional[FinValueWithChange] = Field(
        default=FinValueWithChange(context="ForecastMember")
    )
    upper: Optional[FinValueWithChange] = Field(
        default=FinValueWithChange(context="UpperMember")
    )
    lower: Optional[FinValueWithChange] = Field(
        default=FinValueWithChange(context="LowerMember")
    )
    context: Optional[str] = Field(default=None)


class FinValueDividends(FinValueAbstractBase):
    """配当の期間情報を表すクラス"""

    FirstQuarterMember: Optional[FinValueWithDividends] = Field(
        default=FinValueWithDividends(context="FirstQuarterMember", label="第1四半期末")
    )
    SecondQuarterMember: Optional[FinValueWithDividends] = Field(
        default=FinValueWithDividends(
            context="SecondQuarterMember", label="第2四半期末"
        )
    )
    ThirdQuarterMember: Optional[FinValueWithDividends] = Field(
        default=FinValueWithDividends(context="ThirdQuarterMember", label="第3四半期末")
    )
    YearEndMember: Optional[FinValueWithDividends] = Field(
        default=FinValueWithDividends(context="YearEndMember", label="期末")
    )
    AnnualMember: Optional[FinValueWithDividends] = Field(
        default=FinValueWithDividends(context="AnnualMember", label="合計")
    )


class PeriodSchemaBase(SQLModel):
    """期間情報を表すクラス"""

    accountingStandard: str
    fiscalYear: str
    period: str


class FinStructBase(SQLModel):
    """ファイナンシャルレスポンス情報を表すクラス"""

    period: Optional[PeriodSchemaBase] = Field(default=None)
    head_item_key: Optional[str] = Field(default=None)


class FinItemsResponse(FinStructBase):
    """メトリック情報のリストを表すクラス"""

    data: Optional[List[FinValueFinance]] = Field(default=[])


class FinItemsDividendsResponse(FinStructBase):
    """配当のメトリック情報のリストを表すクラス"""

    data: Optional[FinValueDividends] = Field(default=None)
