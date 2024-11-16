from app.models import Field, SQLModel
from app.schema.ix_non_numeric import IxNonNumericPublic
from typing import Optional

class IxNonNumericRvfcSm(SQLModel):
    company_name: Optional[IxNonNumericPublic] = Field(default=None, description='上場会社名')
    """ 上場会社名 """
    document_name: Optional[IxNonNumericPublic] = Field(default=None, description='文書名')
    """ 文書名 """
    fasf_member_mark: Optional[IxNonNumericPublic] = Field(default=None, description='財務会計基準機構会員マーク')
    """ 財務会計基準機構会員マーク """
    fiscal_year_end: Optional[IxNonNumericPublic] = Field(default=None, description='決算期')
    """ 決算期 """
    fukuoka_stock_exchange: Optional[IxNonNumericPublic] = Field(default=None, description='福岡証券取引所')
    """ 福岡証券取引所 """
    fukuoka_stock_exchange_established: Optional[IxNonNumericPublic] = Field(default=None, description='福岡証券取引所 既存市場')
    """ 福岡証券取引所 既存市場 """
    fukuoka_stock_exchange_others: Optional[IxNonNumericPublic] = Field(default=None, description='福岡証券取引所 その他')
    """ 福岡証券取引所 その他 """
    fukuoka_stock_exchange_q_board: Optional[IxNonNumericPublic] = Field(default=None, description='福岡証券取引所 Q-Board')
    """ 福岡証券取引所 Q-Board """
    general_business: Optional[IxNonNumericPublic] = Field(default=None, description='一般事業会社')
    """ 一般事業会社 """
    japan_securities_dealers_association: Optional[IxNonNumericPublic] = Field(default=None, description='フェニックス')
    """ フェニックス """
    japan_securities_dealers_association_green_sheet: Optional[IxNonNumericPublic] = Field(default=None, description='日本証券業協会 フェニックス')
    """ 日本証券業協会 フェニックス """
    nagoya_stock_exchange: Optional[IxNonNumericPublic] = Field(default=None, description='名古屋証券取引所')
    """ 名古屋証券取引所 """
    nagoya_stock_exchange1st_section: Optional[IxNonNumericPublic] = Field(default=None, description='名古屋証券取引所 プレミア')
    """ 名古屋証券取引所 プレミア """
    nagoya_stock_exchange2nd_section: Optional[IxNonNumericPublic] = Field(default=None, description='名古屋証券取引所 メイン')
    """ 名古屋証券取引所 メイン """
    nagoya_stock_exchange_centrex: Optional[IxNonNumericPublic] = Field(default=None, description='名古屋証券取引所 ネクスト')
    """ 名古屋証券取引所 ネクスト """
    nagoya_stock_exchange_others: Optional[IxNonNumericPublic] = Field(default=None, description='名古屋証券取引所 その他')
    """ 名古屋証券取引所 その他 """
    name_inquiries: Optional[IxNonNumericPublic] = Field(default=None, description='氏名、問合せ先責任者')
    """ 氏名、問合せ先責任者 """
    name_representative: Optional[IxNonNumericPublic] = Field(default=None, description='氏名、代表者')
    """ 氏名、代表者 """
    note_to_dividends: Optional[IxNonNumericPublic] = Field(default=None, description='配当の状況に関する注記')
    """ 配当の状況に関する注記 """
    note_to_financial_forecast: Optional[IxNonNumericPublic] = Field(default=None, description='業績予想の状況に関する注記')
    """ 業績予想の状況に関する注記 """
    notice_of_forecast_correction: Optional[IxNonNumericPublic] = Field(default=None, description='予想修正に関するお知らせ')
    """ 予想修正に関するお知らせ """
    preamble_to_forecasts: Optional[IxNonNumericPublic] = Field(default=None, description='業績予想に関する事項')
    """ 業績予想に関する事項 """
    previous_reporting_date_of_dividend_forecast: Optional[IxNonNumericPublic] = Field(default=None, description='前回予想発表日、配当予想の修正について')
    """ 前回予想発表日、配当予想の修正について """
    reason_for_dividend_forecast_correction: Optional[IxNonNumericPublic] = Field(default=None, description='配当予想修正の理由')
    """ 配当予想修正の理由 """
    reason_for_forecast_correction: Optional[IxNonNumericPublic] = Field(default=None, description='業績予想修正の理由')
    """ 業績予想修正の理由 """
    reporting_date_of_financial_forecast_correction: Optional[IxNonNumericPublic] = Field(default=None, description='予想修正報告日')
    """ 予想修正報告日 """
    sapporo_stock_exchange: Optional[IxNonNumericPublic] = Field(default=None, description='札幌証券取引所')
    """ 札幌証券取引所 """
    sapporo_stock_exchange_ambitious: Optional[IxNonNumericPublic] = Field(default=None, description='札幌証券取引所 アンビシャス')
    """ 札幌証券取引所 アンビシャス """
    sapporo_stock_exchange_established: Optional[IxNonNumericPublic] = Field(default=None, description='札幌証券取引所 既存市場')
    """ 札幌証券取引所 既存市場 """
    sapporo_stock_exchange_others: Optional[IxNonNumericPublic] = Field(default=None, description='札幌証券取引所 その他')
    """ 札幌証券取引所 その他 """
    securities_code: Optional[IxNonNumericPublic] = Field(default=None, description='コード番号')
    """ コード番号 """
    specific_business: Optional[IxNonNumericPublic] = Field(default=None, description='特定事業会社')
    """ 特定事業会社 """
    tel: Optional[IxNonNumericPublic] = Field(default=None, description='TEL')
    """ TEL """
    title_inquiries: Optional[IxNonNumericPublic] = Field(default=None, description='役職名、問合せ先責任者')
    """ 役職名、問合せ先責任者 """
    title_representative: Optional[IxNonNumericPublic] = Field(default=None, description='役職名、代表者')
    """ 役職名、代表者 """
    tokyo_stock_exchange: Optional[IxNonNumericPublic] = Field(default=None, description='東京証券取引所')
    """ 東京証券取引所 """
    tokyo_stock_exchange_growth: Optional[IxNonNumericPublic] = Field(default=None, description='東京証券取引所 グロース')
    """ 東京証券取引所 グロース """
    tokyo_stock_exchange_others: Optional[IxNonNumericPublic] = Field(default=None, description='東京証券取引所 その他')
    """ 東京証券取引所 その他 """
    tokyo_stock_exchange_pro_market: Optional[IxNonNumericPublic] = Field(default=None, description='東京証券取引所 PRO Market')
    """ 東京証券取引所 PRO Market """
    tokyo_stock_exchange_prime: Optional[IxNonNumericPublic] = Field(default=None, description='東京証券取引所 プライム')
    """ 東京証券取引所 プライム """
    tokyo_stock_exchange_standard: Optional[IxNonNumericPublic] = Field(default=None, description='東京証券取引所 スタンダード')
    """ 東京証券取引所 スタンダード """

