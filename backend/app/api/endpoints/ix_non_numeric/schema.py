from app.models import Field, SQLModel


class IxNonNumericCreate(SQLModel):
    """iXBRLの非数値情報を表すクラス"""

    item_key: str | None = Field(max_length=36, min_length=36)
    head_item_key: str = Field(max_length=255)
    context: list[str] = Field(max_length=255)
    name: str = Field(default=None)
    xsi_nil: bool | None = Field(default=None)
    escape: bool = Field(default=False)
    format: str | None = Field(default=None, max_length=255)
    value: str | None = Field(default=None)
    report_type: str | None = Field(max_length=4)
    ixbrl_role: str | None = Field(max_length=255)
    source_file_id: str | None = Field(max_length=36)
    xbrl_type: str = Field(max_length=255)


class IxNonNumericPublic(SQLModel):
    """iXBRLの非数値情報を表すクラス"""

    head_item_key: str | None
    context: list[str]
    name: str
    xsi_nil: bool | None
    escape: bool | None
    format: str | None
    value: str | None
    report_type: str | None
    ixbrl_role: str | None
    source_file_id: str | None
    xbrl_type: str | None


class IxNonNumericsPublic(SQLModel):
    """iXBRLの非数値情報を表すクラス"""

    count: int
    data: list[IxNonNumericPublic]


class IxNonNumericCreateList(SQLModel):
    """iXBRLの非数値情報を作成するためのクラス"""

    data: list[IxNonNumericCreate]


class IxNonNumericAddLabelItemPublic(IxNonNumericPublic):
    """iXBRLの非数値情報を作成するためのクラス"""

    label: str


class IxNonNumericAddLabelItemsPublic(SQLModel):
    count: int
    data: list[IxNonNumericAddLabelItemPublic]
