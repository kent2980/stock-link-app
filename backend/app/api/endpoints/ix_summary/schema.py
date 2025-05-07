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


class FinValueWithChange(SQLModel):

    curValue: Optional[FinValueBase] = Field(default=None)
    curChange: Optional[FinValueBase] = Field(default=None)
    preValue: Optional[FinValueBase] = Field(default=None)
    preChange: Optional[FinValueBase] = Field(default=None)


class FinValueAbstractBase(SQLModel):
    """メトリック親情報を表すクラス"""

    name: str
    order: float
    label: str
    result: Optional[FinValueWithChange] = Field(default=None)
    forecast: Optional[FinValueWithChange] = Field(default=None)
    upper: Optional[FinValueWithChange] = Field(default=None)
    lower: Optional[FinValueWithChange] = Field(default=None)


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

    context: Optional[str] = Field(default=None)
    data: Optional[List[FinValueAbstractBase]] = Field(default=[])
