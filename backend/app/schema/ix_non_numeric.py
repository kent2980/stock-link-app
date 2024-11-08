from typing import List, Optional

from app.models import Field, SQLModel


class IxNonNumericCreate(SQLModel):
    """iXBRLの非数値情報を表すクラス"""

    item_key: Optional[str] = Field(max_length=36, min_length=36)
    head_item_key: str = Field(max_length=255)
    context: Optional[str] = Field(max_length=255)
    name: str = Field(default=None)
    xsi_nil: Optional[bool] = Field(default=None)
    escape: bool = Field(default=False)
    format: Optional[str] = Field(default=None, max_length=255)
    value: Optional[str] = Field(default=None)
    report_type: Optional[str] = Field(max_length=4)
    ixbrl_role: Optional[str] = Field(max_length=255)
    source_file_id: Optional[str] = Field(max_length=36)
    xbrl_type: str = Field(max_length=255)


class IxNonNumericPublic(SQLModel):
    """iXBRLの非数値情報を表すクラス"""

    head_item_key: Optional[str]
    context: str
    name: str
    xsi_nil: Optional[bool]
    escape: Optional[bool]
    format: Optional[str]
    value: Optional[str]
    report_type: Optional[str]
    ixbrl_role: Optional[str]
    source_file_id: Optional[str]
    xbrl_type: Optional[str]


class IxNonNumericsPublic(SQLModel):
    """iXBRLの非数値情報を表すクラス"""

    data: List[IxNonNumericPublic]
    count: int


class IxNonNumericCreateList(SQLModel):
    """iXBRLの非数値情報を作成するためのクラス"""

    data: List[IxNonNumericCreate]


class IxNonNumericAddLabelItemPublic(IxNonNumericPublic):
    """iXBRLの非数値情報を作成するためのクラス"""

    label: str


class IxNonNumericAddLabelItemsPublic(SQLModel):

    data: list[IxNonNumericAddLabelItemPublic]
    count: int
