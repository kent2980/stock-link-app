from app.models import Field, SQLModel


class IxFilePathCreate(SQLModel):
    """iXBRLのファイルパス情報を作成するためのクラス"""

    item_key: str | None = Field(max_length=36, min_length=36)
    path: str = Field(default=None)
    head_item_key: str | None = Field(
        max_length=36, foreign_key="ix_head_title.item_key"
    )


class IxFilePathCreateList(SQLModel):
    """iXBRLのファイルパス情報を作成するためのクラス"""

    data: list[IxFilePathCreate]


class IxFilePathPublic(SQLModel):
    """iXBRLのファイルパス情報を公開するためのクラス"""

    path: str
    head_item_key: str


class IxFilePathPublicList(SQLModel):
    """iXBRLのファイルパス情報を公開するためのクラス"""

    data: list[IxFilePathPublic]
    count: int
