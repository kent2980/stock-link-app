from decimal import Decimal
from typing import List, Optional

from app.models import Field, SQLModel
from sqlalchemy import DECIMAL, Column


class IxPresentationLocCreate(SQLModel):
    """XBRLの表示リンクロケーションを表すクラス"""

    id: str = Field(max_length=36, min_length=36)
    xbrl_id: str = Field(foreign_key="ix_head_title.xbrl_id", nullable=False)
    attr_value: Optional[str] = Field(max_length=255)
    xlink_href: Optional[str] = Field(nullable=False)
    xlink_type: Optional[str] = Field(max_length=255)
    xlink_schema: Optional[str] = Field(max_length=255)
    xlink_label: Optional[str] = Field(default=None)
    source_file_id: Optional[str] = Field(max_length=36)


class IxPresentationArcCreate(SQLModel):
    """XBRLの表示リンクアークを表すクラス"""

    id: str = Field(max_length=36, min_length=36)
    xbrl_id: str = Field(foreign_key="ix_head_title.xbrl_id", nullable=False)
    attr_value: Optional[str] = Field(max_length=255)
    xlink_order: Optional[Decimal] = Field(
        default=None, sa_column=Column(DECIMAL(5, 2))
    )
    xlink_weight: Optional[Decimal] = Field(
        default=None, sa_column=Column(DECIMAL(5, 2))
    )
    xlink_type: Optional[str] = Field(max_length=255)
    xlink_arcrole: Optional[str] = Field(max_length=255)
    xlink_to: Optional[str] = Field(default=None)
    xlink_from: Optional[str] = Field(default=None)
    source_file_id: Optional[str] = Field(max_length=36)


class IxPresentationLocCreateList(SQLModel):
    """XBRLの表示リンクロケーションを作成するためのクラス"""

    data: List[IxPresentationLocCreate]


class IxPresentationArcCreateList(SQLModel):
    """XBRLの表示リンクアークを作成するためのクラス"""

    data: List[IxPresentationArcCreate]
