
from app.models import Field, SQLModel


class IxQualitativeCreate(SQLModel):
    """定性的情報を登録するためのモデル"""

    item_key: str | None = Field(default=None, max_length=36, description="ID")
    currentId: str = Field(default=None, max_length=36, description="現在のID")
    parentId: str | None = Field(default=None, max_length=36, description="親ID")
    type: str | None = Field(default=None, max_length=255, description="タイプ")
    content: str | None = Field(default=None, description="内容")
    order: int | None = Field(default=None, description="順序")
    head_item_key: str | None = Field(
        default=None, max_length=36, description="XBRL-ID"
    )
    source_file_id: str | None = Field(
        default=None, max_length=36, description="ソースファイルID"
    )
    photo_url: str | None = Field(default=None, description="写真URL")


class IxQualitativeCreates(SQLModel):
    """複数の定性的情報を登録するためのモデル"""

    data: list[IxQualitativeCreate]


class IxQualitativePublic(SQLModel):
    """定性的情報を取得するためのモデル"""

    currentId: str
    parentId: str | None
    type: str | None
    content: str | None
    order: int | None
    head_item_key: str | None
    photo_url: str | None


class IxQualitativePublics(SQLModel):
    """複数の定性的情報を取得するためのモデル"""

    count: int
    data: list[IxQualitativePublic]


class QualitativeInfoHeader(SQLModel):
    """定性的情報のヘッダー情報を取得するためのモデル"""

    class QualitativeInfoSubTitle(SQLModel):
        """定性的情報を取得するためのモデル"""

        operating_result_info: str | None = Field(
            default=None, description="経営成績に関する説明"
        )
        segment_info_key: list[str] | None = Field(
            default=None, description="セグメント情報"
        )
        segment_info: dict = Field(default_factory=dict, description="セグメント情報")
        segment_photo_url: dict = Field(
            default_factory=dict, description="セグメント画像URL"
        )
        explanation_of_financial_position: str | None = Field(
            default=None, description="財政状態の説明"
        )
        forecast_info: str | None = Field(
            default=None, description="将来予測に関する説明"
        )

    qualitative_info: QualitativeInfoSubTitle | None = Field(
        default_factory=QualitativeInfoSubTitle,
        description="当四半期決算に関する定性的情報",
    )
