import datetime
from typing import Optional

from app.models import Field, SQLModel


class IxHeadTitlePublic(SQLModel):
    """iXBRLのヘッダー情報を表すクラス"""

    xbrl_id: str
    company_name: str
    securities_code: str
    document_name: str
    reporting_date: datetime.date
    current_period: Optional[str]
    report_type: Optional[str]
    listed_market: Optional[str]
    market_section: Optional[str]
    url: Optional[str]
    is_bs: Optional[bool]
    is_pl: Optional[bool]
    is_cf: Optional[bool]
    is_ci: Optional[bool]
    is_sce: Optional[bool]
    is_sfp: Optional[bool]
    fiscal_year_end: Optional[str]
    tel: Optional[str]


class IxHeadTitleCreate(SQLModel):
    """iXBRLのヘッダー情報を表すクラス"""

    company_name: Optional[str] = Field(max_length=255)
    securities_code: Optional[str] = Field(max_length=4)
    document_name: Optional[str] = Field(max_length=255)
    reporting_date: datetime.date
    current_period: Optional[str] = Field(max_length=255)
    xbrl_id: Optional[str] = Field(max_length=255, unique=True)
    report_type: Optional[str] = Field(max_length=4)
    listed_market: Optional[str] = Field(default=None)
    market_section: Optional[str] = Field(default=None)
    url: Optional[str] = Field(default=None)
    is_bs: bool = Field(default=False)
    is_pl: bool = Field(default=False)
    is_cf: bool = Field(default=False)
    is_ci: bool = Field(default=False)
    is_sce: bool = Field(default=False)
    is_sfp: bool = Field(default=False)
    fiscal_year_end: Optional[str] = Field(default=None)
    tel: Optional[str] = Field(default=None)


class IxHeadTitlesPublic(SQLModel):
    """iXBRLのヘッダー情報のリストを表すクラス"""

    data: list[IxHeadTitlePublic]
    count: int


class IxHeadTitleCreateList(SQLModel):
    """iXBRLのヘッダー情報のリストを表すクラス"""

    data: list[IxHeadTitleCreate]
