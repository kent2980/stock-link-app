from typing import List, Optional

from app.models import Field, SQLModel


class IxFilePathCreate(SQLModel):
    """iXBRLのファイルパス情報を作成するためのクラス"""

    path: str = Field(default=None)
    xbrl_id: Optional[str] = Field(max_length=36)


class IxFilePathCreateList(SQLModel):
    """iXBRLのファイルパス情報を作成するためのクラス"""

    data: List[IxFilePathCreate]


class IxFilePathPublic(SQLModel):
    """iXBRLのファイルパス情報を公開するためのクラス"""

    path: str
    xbrl_id: str


class IxFilePathPublicList(SQLModel):
    """iXBRLのファイルパス情報を公開するためのクラス"""

    data: List[IxFilePathPublic]
    count: int
