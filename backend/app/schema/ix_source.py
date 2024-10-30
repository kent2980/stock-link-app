from typing import List, Optional

from app.models import Field, SQLModel


class IxSourceFileCreate(SQLModel):
    """iXBRLのソースファイル情報を作成するためのクラス"""

    id: Optional[str] = Field(max_length=36)
    item_key: Optional[str] = Field(max_length=36, min_length=36)
    name: str = Field(max_length=255)
    type: str = Field(max_length=255)
    xbrl_id: Optional[str] = Field(max_length=36)
    url: Optional[str] = Field(max_length=255)


class IxSourceFileCreateList(SQLModel):
    """iXBRLのソースファイル情報を作成するためのクラス"""

    data: List[IxSourceFileCreate]


class IxSourceFilePublic(SQLModel):
    """iXBRLのソースファイル情報を公開するためのクラス"""

    item_key: Optional[str]
    name: str
    type: str
    xbrl_id: str
    url: str


class IxSourceFilePublicList(SQLModel):
    """iXBRLのソースファイル情報を公開するためのクラス"""

    data: List[IxSourceFilePublic]
    count: int
