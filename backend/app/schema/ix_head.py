import datetime
from typing import Optional

from app.models import Field, SQLModel


class IxHeadTitlePublic(SQLModel):
    """iXBRLのヘッダー情報を表すクラス"""

    insert_date: datetime.datetime = Field(description="作成日時")
    update_date: datetime.datetime = Field(description="更新日時")
    item_key: str = Field(description="アイテムキー")
    company_name: Optional[str] = Field(description="会社名")
    securities_code: Optional[str] = Field(description="証券コード")
    document_name: Optional[str] = Field(description="書類名")
    reporting_date: Optional[datetime.date] = Field(description="報告日")
    current_period: Optional[str] = Field(description="現在の期間")
    report_type: Optional[str] = Field(description="報告書タイプ")
    listed_market: Optional[str] = Field(description="上場市場")
    market_section: Optional[str] = Field(description="市場区分")
    url: Optional[str] = Field(description="URL")
    is_bs: Optional[bool] = Field(description="貸借対照表フラグ")
    is_pl: Optional[bool] = Field(description="損益計算書フラグ")
    is_cf: Optional[bool] = Field(description="キャッシュフロー計算書フラグ")
    is_ci: Optional[bool] = Field(description="包括利益計算書フラグ")
    is_sce: Optional[bool] = Field(description="株主資本等変動計算書フラグ")
    is_sfp: Optional[bool] = Field(description="財政状態計算書フラグ")
    fy_year_end: Optional[str] = Field(description="会計年度末")
    tel: Optional[str] = Field(description="電話番号")
    is_div_rev: Optional[bool] = Field(description="配当修正フラグ")
    div_inc_rt: Optional[str] = Field(description="配当収益率")
    is_fcst_rev: Optional[bool] = Field(description="業績予測修正フラグ")
    fcst_oi_gr_rt: Optional[str] = Field(description="予測営業利益成長率")
    oi_prog_rt: Optional[float] = Field(description="営業利益進捗率")
    specific_business: Optional[bool] = Field(description="特定事業フラグ")
    is_consolidated: Optional[bool] = Field(description="連結決算フラグ")
    change_in_net_sales: Optional[float] = Field(description="売上高増減率")
    change_in_ordinary_income: Optional[float] = Field(description="経常利益増減率")
    change_in_net_income: Optional[float] = Field(description="当期純利益増減率")
    change_in_fore_net_sales: Optional[float] = Field(description="予想売上高増減率")
    change_in_fore_ordinary_income: Optional[float] = Field(
        description="予想経常利益増減率"
    )
    change_in_fore_net_income: Optional[float] = Field(description="予想純利益増減率")


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
    specific_business: Optional[bool] = Field(default=None)
    is_consolidated: Optional[bool] = Field(default=None)
    change_in_net_sales: Optional[float] = Field(default=None)
    change_in_ordinary_income: Optional[float] = Field(default=None)
    change_in_net_income: Optional[float] = Field(default=None)
    change_in_fore_net_sales: Optional[float] = Field(default=None)
    change_in_fore_ordinary_income: Optional[float] = Field(default=None)
    change_in_fore_net_income: Optional[float] = Field(default=None)


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


class IxHeadDocumentInfo(SQLModel):

    item_key: str
    document_name: str
    reporting_date: datetime.date
    current_period: str


class IxHeadDocumentInfoList(SQLModel):

    data: list[IxHeadDocumentInfo]
    count: int
