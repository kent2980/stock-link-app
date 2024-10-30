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

    item_key: Optional[str] = Field(max_length=36, min_length=36)
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
    is_dividend_revision: Optional[bool] = Field(
        default=False, description="配当予想の修正"
    )
    dividend_increase_rate: Optional[str] = Field(default=None, description="増配率")
    is_earnings_forecast_revision: Optional[bool] = Field(
        default=False, description="業績予想の修正"
    )
    forecast_ordinary_income_growth_rate: Optional[str] = Field(
        default=None, description="予想経常利益増益率"
    )


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
