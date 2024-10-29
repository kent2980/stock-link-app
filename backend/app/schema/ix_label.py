from typing import List

from app.models import Field, SQLModel


class IxLabelLocCreate(SQLModel):
    """iXBRLのラベルロケーション情報を作成するためのクラス"""

    id: str = Field(max_length=36, min_length=36)
    xlink_href: str = Field(default=None)
    xlink_label: str = Field(default=None)
    xlink_type: str = Field(max_length=255)
    xlink_schema: str = Field(max_length=255)
    source_file_id: str = Field(max_length=36)


class IxLabelLocPublic(SQLModel):
    """iXBRLのラベルロケーション情報を公開するためのクラス"""

    xlink_href: str
    xlink_label: str
    xlink_type: str
    xlink_schema: str


class IxLabelLocsPublic(SQLModel):
    """iXBRLのラベルロケーション情報を公開するためのクラス"""

    data: list[IxLabelLocPublic]
    count: int


class IxLabelArcCreate(SQLModel):
    """iXBRLのラベルアーク情報を作成するためのクラス"""

    id: str = Field(max_length=36, min_length=36)
    xlink_type: str = Field(max_length=255)
    xlink_arcrole: str = Field(max_length=255)
    xlink_from: str = Field(default=None)
    xlink_to: str = Field(default=None)
    source_file_id: str = Field(max_length=36)


class IxLabelArcCreateList(SQLModel):
    """iXBRLのラベルアーク情報を作成するためのクラス"""

    data: List[IxLabelArcCreate]


class IxLabelArcPublic(SQLModel):
    """iXBRLのラベルアーク情報を公開するためのクラス"""

    xlink_type: str
    xlink_arcrole: str
    xlink_from: str
    xlink_to: str


class IxLabelArcsPublic(SQLModel):
    """iXBRLのラベルアーク情報を公開するためのクラス"""

    data: list[IxLabelArcPublic]
    count: int


class IxLabelValueCreate(SQLModel):
    """iXBRLのラベルリンク情報を作成するためのクラス"""

    id: str = Field(max_length=36, min_length=36)
    xlink_type: str = Field(max_length=255)
    xlink_label: str = Field(default=None)
    xlink_role: str = Field(max_length=255)
    xml_lang: str = Field(max_length=255)
    label: str = Field(default=None)
    source_file_id: str = Field(max_length=36)


class IxLabelValueCreateList(SQLModel):
    """iXBRLのラベルリンク情報を作成するためのクラス"""

    data: List[IxLabelValueCreate]


class IxLabelValuePublic(SQLModel):
    """iXBRLのラベルリンク情報を公開するためのクラス"""

    xlink_type: str
    xlink_label: str
    xlink_role: str
    xml_lang: str
    label: str


class IxLabelValuesPublic(SQLModel):
    """iXBRLのラベルリンク情報を公開するためのクラス"""

    data: list[IxLabelValuePublic]
    count: int


class IxLabelLocCreateList(SQLModel):
    """iXBRLのラベルロケーション情報を作成するためのクラス"""

    data: List[IxLabelLocCreate]


class IxLabelValuesCreateList(SQLModel):
    """iXBRLのラベルリンク情報を作成するためのクラス"""

    data: List[IxLabelValueCreate]


class IxLabelArcCreateList(SQLModel):
    """iXBRLの計算アーク情報を作成するためのクラス"""

    data: List[IxLabelArcCreate]
