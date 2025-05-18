from app.models import Field, SQLModel


class IxSourceFileCreate(SQLModel):
    """iXBRLのソースファイル情報を作成するためのクラス"""

    source_file_id: str | None = Field(max_length=36)
    item_key: str | None = Field(max_length=36, min_length=36)
    name: str = Field(max_length=255)
    type: str = Field(max_length=255)
    head_item_key: str | None = Field(max_length=36)
    url: str | None = Field(max_length=255)


class IxSourceFileCreateList(SQLModel):
    """iXBRLのソースファイル情報を作成するためのクラス"""

    data: list[IxSourceFileCreate]


class IxSourceFilePublic(SQLModel):
    """iXBRLのソースファイル情報を公開するためのクラス"""

    source_file_id: str | None
    item_key: str | None
    name: str
    type: str
    head_item_key: str
    url: str


class IxSourceFilePublicList(SQLModel):
    """iXBRLのソースファイル情報を公開するためのクラス"""

    data: list[IxSourceFilePublic]
    count: int
