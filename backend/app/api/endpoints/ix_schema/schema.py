
from app.models import Field, SQLModel


class IxSchemaLinkBaseCreate(SQLModel):
    """iXBRLのスキーマリンクベース情報を作成するためのクラス"""

    item_key: str | None = Field(max_length=36, min_length=36)
    head_item_key: str = Field(foreign_key="ix_head_title.item_key", nullable=False)
    xlink_arcrole: str | None = Field(max_length=255)
    xlink_href: str | None = Field(max_length=255)
    xlink_role: str | None = Field(max_length=255)
    xlink_type: str | None = Field(max_length=255)
    source_file_id: str | None = Field(max_length=36)
    xbrl_type: str | None = Field(max_length=255)
    href_source_file_id: str | None = Field(max_length=36)


class IxSchemaLinkBaseCreateList(SQLModel):
    """iXBRLのスキーマリンクベース情報を作成するためのクラス"""

    data: list[IxSchemaLinkBaseCreate]


class IxSchemaLinkBasePublic(SQLModel):
    """iXBRLのスキーマリンクベース情報を公開するためのクラス"""

    head_item_key: str
    xlink_arcrole: str
    xlink_href: str
    xlink_role: str
    xlink_type: str
    source_file_id: str
    xbrl_type: str
    href_source_file_id: str


class IxSchemaLinkBasePublicList(SQLModel):
    """iXBRLのスキーマリンクベース情報を公開するためのクラス"""

    data: list[IxSchemaLinkBasePublic]
    count: int
