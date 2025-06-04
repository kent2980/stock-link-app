
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
    data: list[TreeItem]


class FinValueBase(SQLModel):
    """メトリック情報を表すクラス"""

    name: str
    value: float | None
    unit: str | None
    display_scale: str | None
    scale: int | None


class FinValueWithChange(SQLModel):
    isActive: bool | None = Field(default=False)
    curValue: FinValueBase | None = Field(default=None)
    curChange: FinValueBase | None = Field(default=None)
    preValue: FinValueBase | None = Field(default=None)
    preChange: FinValueBase | None = Field(default=None)
    context: str | None = Field(default=None)


class FinValueAbstractBase(SQLModel):
    """メトリック親情報を表すクラス"""

    name: str
    order: float
    label: str | None = Field(default=None)


class FinValueFinance(FinValueAbstractBase):
    """メトリック親情報を表すクラス"""

    result: FinValueWithChange | None = Field(
        default=FinValueWithChange(context="ResultMember")
    )
    forecast: FinValueWithChange | None = Field(
        default=FinValueWithChange(context="ForecastMember")
    )
    upper: FinValueWithChange | None = Field(
        default=FinValueWithChange(context="UpperMember")
    )
    lower: FinValueWithChange | None = Field(
        default=FinValueWithChange(context="LowerMember")
    )


class FinValueWithDividends(SQLModel):
    """配当のメトリック情報を表すクラス"""

    isActive: bool | None = Field(default=False)
    label: str | None = Field(default=None)
    result: FinValueWithChange | None = Field(
        default=FinValueWithChange(context="ResultMember")
    )
    forecast: FinValueWithChange | None = Field(
        default=FinValueWithChange(context="ForecastMember")
    )
    upper: FinValueWithChange | None = Field(
        default=FinValueWithChange(context="UpperMember")
    )
    lower: FinValueWithChange | None = Field(
        default=FinValueWithChange(context="LowerMember")
    )
    context: str | None = Field(default=None)


class FinValueDividends(FinValueAbstractBase):
    """配当の期間情報を表すクラス"""

    FirstQuarterMember: FinValueWithDividends | None = Field(
        default=FinValueWithDividends(context="FirstQuarterMember", label="第1四半期末")
    )
    SecondQuarterMember: FinValueWithDividends | None = Field(
        default=FinValueWithDividends(
            context="SecondQuarterMember", label="第2四半期末"
        )
    )
    ThirdQuarterMember: FinValueWithDividends | None = Field(
        default=FinValueWithDividends(context="ThirdQuarterMember", label="第3四半期末")
    )
    YearEndMember: FinValueWithDividends | None = Field(
        default=FinValueWithDividends(context="YearEndMember", label="期末")
    )
    AnnualMember: FinValueWithDividends | None = Field(
        default=FinValueWithDividends(context="AnnualMember", label="合計")
    )
    TotalDividendPaidAnnual: FinValueWithDividends | None = Field(
        default=FinValueWithDividends(context="AnnualMember", label="年間配当金総額")
    )
    PayoutRatio: FinValueWithDividends | None = Field(
        default=FinValueWithDividends(context="AnnualMember", label="配当性向")
    )
    RatioTotalAmountOfDividendTotalNetAssets: FinValueWithDividends | None = Field(
        default=FinValueWithDividends(context="AnnualMember", label="純資産配当率")
    )


class PeriodSchemaBase(SQLModel):
    """期間情報を表すクラス"""

    accountingStandard: str
    fiscalYear: str
    period: str


class FinStructBase(SQLModel):
    """ファイナンシャルレスポンス情報を表すクラス"""

    period: PeriodSchemaBase | None = Field(default=None)
    head_item_key: str | None = Field(default=None)


class FinItemsResponse(FinStructBase):
    """メトリック情報のリストを表すクラス"""

    data: list[FinValueFinance] | None = Field(default=[])


class FinItemsDividendsResponse(FinStructBase):
    """配当のメトリック情報のリストを表すクラス"""

    data: FinValueDividends | None = Field(default=None)


class DisclosureItem(SQLModel):
    """開示項目を表すクラス"""

    id: int
    company: str
    code: str
    date: str
    title: str
    summary: str
    category: str
    important: bool


class DisclosureItemsList(SQLModel):
    """開示項目のリストを表すクラス"""

    offset: int = Field(default=0, description="オフセット")
    count: int
    data: list[DisclosureItem] = Field(default=[])
