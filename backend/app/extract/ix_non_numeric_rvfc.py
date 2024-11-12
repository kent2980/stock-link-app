from app.models import IxNonNumeric
from sqlmodel import Session, select

def company_name(*, session: Session, head_item_key:str, context:str):
    """
    上場会社名
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_CompanyName',
            IxNonNumeric.head_item_key == head_item_key,
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def document_name(*, session: Session, head_item_key:str, context:str):
    """
    文書名
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_DocumentName',
            IxNonNumeric.head_item_key == head_item_key,
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def fasf_member_mark(*, session: Session, head_item_key:str, context:str):
    """
    財務会計基準機構会員マーク
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_FASFMemberMark',
            IxNonNumeric.head_item_key == head_item_key,
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def fiscal_year_end(*, session: Session, head_item_key:str, context:str):
    """
    決算期
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_FiscalYearEnd',
            IxNonNumeric.head_item_key == head_item_key,
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def fukuoka_stock_exchange(*, session: Session, head_item_key:str, context:str):
    """
    福岡証券取引所
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_FukuokaStockExchange',
            IxNonNumeric.head_item_key == head_item_key,
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def fukuoka_stock_exchange_established(*, session: Session, head_item_key:str, context:str):
    """
    福岡証券取引所 既存市場
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_FukuokaStockExchangeEstablished',
            IxNonNumeric.head_item_key == head_item_key,
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def fukuoka_stock_exchange_others(*, session: Session, head_item_key:str, context:str):
    """
    福岡証券取引所 その他
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_FukuokaStockExchangeOthers',
            IxNonNumeric.head_item_key == head_item_key,
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def fukuoka_stock_exchange_q_board(*, session: Session, head_item_key:str, context:str):
    """
    福岡証券取引所 Q-Board
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_FukuokaStockExchangeQBoard',
            IxNonNumeric.head_item_key == head_item_key,
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def general_business(*, session: Session, head_item_key:str, context:str):
    """
    一般事業会社
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_GeneralBusiness',
            IxNonNumeric.head_item_key == head_item_key,
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def japan_securities_dealers_association(*, session: Session, head_item_key:str, context:str):
    """
    フェニックス
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_JapanSecuritiesDealersAssociation',
            IxNonNumeric.head_item_key == head_item_key,
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def japan_securities_dealers_association_green_sheet(*, session: Session, head_item_key:str, context:str):
    """
    日本証券業協会 フェニックス
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_JapanSecuritiesDealersAssociationGreenSheet',
            IxNonNumeric.head_item_key == head_item_key,
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def nagoya_stock_exchange(*, session: Session, head_item_key:str, context:str):
    """
    名古屋証券取引所
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_NagoyaStockExchange',
            IxNonNumeric.head_item_key == head_item_key,
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def nagoya_stock_exchange1st_section(*, session: Session, head_item_key:str, context:str):
    """
    名古屋証券取引所 プレミア
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_NagoyaStockExchange1stSection',
            IxNonNumeric.head_item_key == head_item_key,
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def nagoya_stock_exchange2nd_section(*, session: Session, head_item_key:str, context:str):
    """
    名古屋証券取引所 メイン
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_NagoyaStockExchange2ndSection',
            IxNonNumeric.head_item_key == head_item_key,
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def nagoya_stock_exchange_centrex(*, session: Session, head_item_key:str, context:str):
    """
    名古屋証券取引所 ネクスト
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_NagoyaStockExchangeCentrex',
            IxNonNumeric.head_item_key == head_item_key,
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def nagoya_stock_exchange_others(*, session: Session, head_item_key:str, context:str):
    """
    名古屋証券取引所 その他
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_NagoyaStockExchangeOthers',
            IxNonNumeric.head_item_key == head_item_key,
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def name_inquiries(*, session: Session, head_item_key:str, context:str):
    """
    氏名、問合せ先責任者
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_NameInquiries',
            IxNonNumeric.head_item_key == head_item_key,
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def name_representative(*, session: Session, head_item_key:str, context:str):
    """
    氏名、代表者
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_NameRepresentative',
            IxNonNumeric.head_item_key == head_item_key,
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def note_to_dividends(*, session: Session, head_item_key:str, context:str):
    """
    配当の状況に関する注記
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_NoteToDividends',
            IxNonNumeric.head_item_key == head_item_key,
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def note_to_financial_forecast(*, session: Session, head_item_key:str, context:str):
    """
    業績予想の状況に関する注記
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_NoteToFinancialForecast',
            IxNonNumeric.head_item_key == head_item_key,
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def notice_of_forecast_correction(*, session: Session, head_item_key:str, context:str):
    """
    予想修正に関するお知らせ
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_NoticeOfForecastCorrection',
            IxNonNumeric.head_item_key == head_item_key,
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def preamble_to_forecasts(*, session: Session, head_item_key:str, context:str):
    """
    業績予想に関する事項
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_PreambleToForecasts',
            IxNonNumeric.head_item_key == head_item_key,
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def previous_reporting_date_of_dividend_forecast(*, session: Session, head_item_key:str, context:str):
    """
    前回予想発表日、配当予想の修正について
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_PreviousReportingDateOfDividendForecast',
            IxNonNumeric.head_item_key == head_item_key,
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def reason_for_dividend_forecast_correction(*, session: Session, head_item_key:str, context:str):
    """
    配当予想修正の理由
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_ReasonForDividendForecastCorrection',
            IxNonNumeric.head_item_key == head_item_key,
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def reason_for_forecast_correction(*, session: Session, head_item_key:str, context:str):
    """
    業績予想修正の理由
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_ReasonForForecastCorrection',
            IxNonNumeric.head_item_key == head_item_key,
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def reporting_date_of_financial_forecast_correction(*, session: Session, head_item_key:str, context:str):
    """
    予想修正報告日
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_ReportingDateOfFinancialForecastCorrection',
            IxNonNumeric.head_item_key == head_item_key,
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def sapporo_stock_exchange(*, session: Session, head_item_key:str, context:str):
    """
    札幌証券取引所
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_SapporoStockExchange',
            IxNonNumeric.head_item_key == head_item_key,
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def sapporo_stock_exchange_ambitious(*, session: Session, head_item_key:str, context:str):
    """
    札幌証券取引所 アンビシャス
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_SapporoStockExchangeAmbitious',
            IxNonNumeric.head_item_key == head_item_key,
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def sapporo_stock_exchange_established(*, session: Session, head_item_key:str, context:str):
    """
    札幌証券取引所 既存市場
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_SapporoStockExchangeEstablished',
            IxNonNumeric.head_item_key == head_item_key,
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def sapporo_stock_exchange_others(*, session: Session, head_item_key:str, context:str):
    """
    札幌証券取引所 その他
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_SapporoStockExchangeOthers',
            IxNonNumeric.head_item_key == head_item_key,
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def securities_code(*, session: Session, head_item_key:str, context:str):
    """
    コード番号
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_SecuritiesCode',
            IxNonNumeric.head_item_key == head_item_key,
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def specific_business(*, session: Session, head_item_key:str, context:str):
    """
    特定事業会社
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_SpecificBusiness',
            IxNonNumeric.head_item_key == head_item_key,
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def tel(*, session: Session, head_item_key:str, context:str):
    """
    TEL
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_Tel',
            IxNonNumeric.head_item_key == head_item_key,
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def title_inquiries(*, session: Session, head_item_key:str, context:str):
    """
    役職名、問合せ先責任者
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_TitleInquiries',
            IxNonNumeric.head_item_key == head_item_key,
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def title_representative(*, session: Session, head_item_key:str, context:str):
    """
    役職名、代表者
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_TitleRepresentative',
            IxNonNumeric.head_item_key == head_item_key,
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def tokyo_stock_exchange(*, session: Session, head_item_key:str, context:str):
    """
    東京証券取引所
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_TokyoStockExchange',
            IxNonNumeric.head_item_key == head_item_key,
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def tokyo_stock_exchange_growth(*, session: Session, head_item_key:str, context:str):
    """
    東京証券取引所 グロース
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_TokyoStockExchangeGrowth',
            IxNonNumeric.head_item_key == head_item_key,
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def tokyo_stock_exchange_others(*, session: Session, head_item_key:str, context:str):
    """
    東京証券取引所 その他
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_TokyoStockExchangeOthers',
            IxNonNumeric.head_item_key == head_item_key,
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def tokyo_stock_exchange_pro_market(*, session: Session, head_item_key:str, context:str):
    """
    東京証券取引所 PRO Market
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_TokyoStockExchangePROMarket',
            IxNonNumeric.head_item_key == head_item_key,
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def tokyo_stock_exchange_prime(*, session: Session, head_item_key:str, context:str):
    """
    東京証券取引所 プライム
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_TokyoStockExchangePrime',
            IxNonNumeric.head_item_key == head_item_key,
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def tokyo_stock_exchange_standard(*, session: Session, head_item_key:str, context:str):
    """
    東京証券取引所 スタンダード
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_TokyoStockExchangeStandard',
            IxNonNumeric.head_item_key == head_item_key,
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

