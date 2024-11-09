import datetime
from typing import Optional

from app.models import Field, SQLModel


class IxHeadTitlePublic(SQLModel):
    """iXBRLのヘッダー情報を表すクラス"""

    item_key: str
    company_name: Optional[str]
    securities_code: Optional[str]
    document_name: Optional[str]
    reporting_date: Optional[datetime.date]
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
    fy_year_end: Optional[str]
    tel: Optional[str]
    is_div_rev: Optional[bool]
    div_inc_rt: Optional[str]
    is_fcst_rev: Optional[bool]
    fcst_oi_gr_rt: Optional[str]
    oi_prog_rt: Optional[float]


class IxHeadTitleCreate(SQLModel):
    """iXBRLのヘッダー情報を表すクラス"""

    item_key: str = Field(max_length=36, min_length=36, unique=True)
    company_name: Optional[str] = Field(default=None)
    securities_code: Optional[str] = Field(default=None)
    document_name: Optional[str] = Field(default=None)
    reporting_date: Optional[datetime.date] = Field(default=None)
    current_period: Optional[str] = Field(default=None)
    report_type: Optional[str] = Field(default=None)
    listed_market: Optional[str] = Field(default=None)
    market_section: Optional[str] = Field(default=None)
    url: Optional[str] = Field(default=None)
    is_bs: Optional[bool] = Field(default=None)
    is_pl: Optional[bool] = Field(default=None)
    is_cf: Optional[bool] = Field(default=None)
    is_ci: Optional[bool] = Field(default=None)
    is_sce: Optional[bool] = Field(default=None)
    is_sfp: Optional[bool] = Field(default=None)
    fy_year_end: Optional[str] = Field(default=None)
    tel: Optional[str] = Field(default=None)


class IxHeadTitlesPublic(SQLModel):
    """iXBRLのヘッダー情報のリストを表すクラス"""

    data: list[IxHeadTitlePublic]
    count: int


class IxHeadTitleCreateList(SQLModel):
    """iXBRLのヘッダー情報のリストを表すクラス"""

    data: list[IxHeadTitleCreate]


class IxReportTypeCount(SQLModel):
    """報告書タイプのカウントを表すクラス"""

    report_type: str
    report_type_jp: str
    count: int


class IxReportTypeCountList(SQLModel):
    """報告書タイプのカウントのリストを表すクラス"""

    data: list[IxReportTypeCount]
    count: int
