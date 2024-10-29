from typing import List, Optional

from app.models import Field, SQLModel


class IxQualitativeCreate(SQLModel):
    """定性的情報を登録するためのモデル"""

    id: str = Field(default=None, max_length=36, description="ID")
    currentId: str = Field(default=None, max_length=36, description="現在のID")
    parentId: Optional[str] = Field(default=None, max_length=36, description="親ID")
    type: Optional[str] = Field(default=None, max_length=255, description="タイプ")
    content: Optional[str] = Field(default=None, description="内容")
    order: Optional[int] = Field(default=None, description="順序")
    xbrl_id: Optional[str] = Field(default=None, max_length=36, description="XBRL-ID")
    source_file_id: Optional[str] = Field(
        default=None, max_length=36, description="ソースファイルID"
    )
    photo_url: Optional[str] = Field(default=None, description="写真URL")


class IxQualitativeCreates(SQLModel):
    """複数の定性的情報を登録するためのモデル"""

    data: List[IxQualitativeCreate]


class IxQualitativePublic(SQLModel):
    """定性的情報を取得するためのモデル"""

    currentId: str
    parentId: Optional[str]
    type: Optional[str]
    content: Optional[str]
    order: Optional[int]
    xbrl_id: Optional[str]
    photo_url: Optional[str]


class IxQualitativePublics(SQLModel):
    """複数の定性的情報を取得するためのモデル"""

    count: int
    data: List[IxQualitativePublic]


class QualitativeInfoHeader(SQLModel):
    """定性的情報のヘッダー情報を取得するためのモデル"""

    class QualitativeInfoSubTitle(SQLModel):
        """定性的情報を取得するためのモデル"""

        operating_result_info: Optional[str] = Field(
            default=None, description="経営成績に関する説明"
        )
        segment_info_key: Optional[List[str]] = Field(
            default=None, description="セグメント情報"
        )
        segment_info: dict = Field(default_factory=dict, description="セグメント情報")
        segment_photo_url: dict = Field(
            default_factory=dict, description="セグメント画像URL"
        )
        explanation_of_financial_position: Optional[str] = Field(
            default=None, description="財政状態の説明"
        )
        forecast_info: Optional[str] = Field(
            default=None, description="将来予測に関する説明"
        )

    qualitative_info: Optional[QualitativeInfoSubTitle] = Field(
        default_factory=QualitativeInfoSubTitle,
        description="当四半期決算に関する定性的情報",
    )
