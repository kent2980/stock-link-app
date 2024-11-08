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
    fiscal_year_end: Optional[str]
    tel: Optional[str]
    is_dividend_revision: Optional[bool]
    dividend_increase_rate: Optional[str]
    is_earnings_forecast_revision: Optional[bool]
    forecast_ordinary_income_growth_rate: Optional[str]


class IxHeadTitleCreate(SQLModel):
    """iXBRLのヘッダー情報を表すクラス"""

    item_key: str = Field(max_length=36, min_length=36, unique=True)


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
