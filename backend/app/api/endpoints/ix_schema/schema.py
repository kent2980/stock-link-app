from typing import List, Optional

from app.models import Field, SQLModel


class IxSchemaLinkBaseCreate(SQLModel):
    """iXBRLのスキーマリンクベース情報を作成するためのクラス"""

    item_key: Optional[str] = Field(max_length=36, min_length=36)
    head_item_key: str = Field(foreign_key="ix_head_title.item_key", nullable=False)
    xlink_arcrole: Optional[str] = Field(max_length=255)
    xlink_href: Optional[str] = Field(max_length=255)
    xlink_role: Optional[str] = Field(max_length=255)
    xlink_type: Optional[str] = Field(max_length=255)
    source_file_id: Optional[str] = Field(max_length=36)
    xbrl_type: Optional[str] = Field(max_length=255)
    href_source_file_id: Optional[str] = Field(max_length=36)


class IxSchemaLinkBaseCreateList(SQLModel):
    """iXBRLのスキーマリンクベース情報を作成するためのクラス"""

    data: List[IxSchemaLinkBaseCreate]


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

    data: List[IxSchemaLinkBasePublic]
    count: int
