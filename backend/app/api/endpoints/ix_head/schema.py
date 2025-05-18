import datetime

from app.models import Field, SQLModel


class IxHeadTitlePublic(SQLModel):
    """iXBRLのヘッダー情報を表すクラス"""

    insert_date: datetime.datetime = Field(description="作成日時")
    update_date: datetime.datetime = Field(description="更新日時")
    item_key: str = Field(description="アイテムキー")
    company_name: str | None = Field(description="会社名")
    securities_code: str | None = Field(description="証券コード")
    document_name: str | None = Field(description="書類名")
    reporting_date: datetime.date | None = Field(description="報告日")
    current_period: str | None = Field(description="現在の期間")
    report_type: str | None = Field(description="報告書タイプ")
    listed_market: str | None = Field(description="上場市場")
    market_section: str | None = Field(description="市場区分")
    url: str | None = Field(description="URL")
    is_bs: bool | None = Field(description="貸借対照表フラグ")
    is_pl: bool | None = Field(description="損益計算書フラグ")
    is_cf: bool | None = Field(description="キャッシュフロー計算書フラグ")
    is_ci: bool | None = Field(description="包括利益計算書フラグ")
    is_sce: bool | None = Field(description="株主資本等変動計算書フラグ")
    is_sfp: bool | None = Field(description="財政状態計算書フラグ")
    fy_year_end: str | None = Field(description="会計年度末")
    tel: str | None = Field(description="電話番号")
    is_div_rev: bool | None = Field(description="配当修正フラグ")
    div_inc_rt: str | None = Field(description="配当収益率")
    is_fcst_rev: bool | None = Field(description="業績予測修正フラグ")
    fcst_oi_gr_rt: str | None = Field(description="予測営業利益成長率")
    oi_prog_rt: float | None = Field(description="営業利益進捗率")
    specific_business: bool | None = Field(description="特定事業フラグ")
    is_consolidated: bool | None = Field(description="連結決算フラグ")
    change_in_net_sales: float | None = Field(description="売上高増減率")
    change_in_ordinary_income: float | None = Field(description="経常利益増減率")
    change_in_net_income: float | None = Field(description="当期純利益増減率")
    change_in_fore_net_sales: float | None = Field(description="予想売上高増減率")
    change_in_fore_ordinary_income: float | None = Field(
        description="予想経常利益増減率"
    )
    change_in_fore_net_income: float | None = Field(description="予想純利益増減率")


class IxHeadTitleCreate(SQLModel):
    """iXBRLのヘッダー情報を表すクラス"""

    item_key: str = Field(max_length=36, min_length=36, unique=True)
    company_name: str | None = Field(default=None)
    securities_code: str | None = Field(default=None)
    document_name: str | None = Field(default=None)
    reporting_date: datetime.date | None = Field(default=None)
    current_period: str | None = Field(default=None)
    report_type: str | None = Field(default=None)
    listed_market: str | None = Field(default=None)
    market_section: str | None = Field(default=None)
    url: str | None = Field(default=None)
    is_bs: bool | None = Field(default=None)
    is_pl: bool | None = Field(default=None)
    is_cf: bool | None = Field(default=None)
    is_ci: bool | None = Field(default=None)
    is_sce: bool | None = Field(default=None)
    is_sfp: bool | None = Field(default=None)
    fy_year_end: str | None = Field(default=None)
    tel: str | None = Field(default=None)
    specific_business: bool | None = Field(default=None)
    is_consolidated: bool | None = Field(default=None)
    change_in_net_sales: float | None = Field(default=None)
    change_in_ordinary_income: float | None = Field(default=None)
    change_in_net_income: float | None = Field(default=None)
    change_in_fore_net_sales: float | None = Field(default=None)
    change_in_fore_ordinary_income: float | None = Field(default=None)
    change_in_fore_net_income: float | None = Field(default=None)


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
