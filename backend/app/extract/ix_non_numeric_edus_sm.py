from app.models import IxNonNumeric
from sqlmodel import Session, select

def applying_of_simplified_method_of_accounting_and_specific_accounting_of_the_consolidated_quarterly_financial_statements(session: Session, head_item_key:str):
    """
    簡便な会計処理及び特有の会計処理の適用、四半期、連結
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_ApplyingOfSimplifiedMethodOfAccountingAndSpecificAccountingOfTheConsolidatedQuarterlyFinancialStatements',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def changes_based_on_revisions_of_accounting_standard_us(session: Session, head_item_key:str):
    """
    会計基準等の改正に伴う会計方針の変更、米国基準
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_ChangesBasedOnRevisionsOfAccountingStandardUS',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def changes_other_than_ones_based_on_revisions_of_accounting_standard_us(session: Session, head_item_key:str):
    """
    会計基準等の改正に伴う変更以外の会計方針の変更、米国基準
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_ChangesOtherThanOnesBasedOnRevisionsOfAccountingStandardUS',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def company_name(session: Session, head_item_key:str):
    """
    上場会社名
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_CompanyName',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def convening_briefing_of_results(session: Session, head_item_key:str):
    """
    決算説明会開催の有無、期中
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_ConveningBriefingOfResults',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def correction_of_consolidated_financial_forecast_in_this_quarter(session: Session, head_item_key:str):
    """
    直近に公表されている業績予想からの修正の有無、連結
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_CorrectionOfConsolidatedFinancialForecastInThisQuarter',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def correction_of_dividend_forecast_in_this_quarter(session: Session, head_item_key:str):
    """
    直近に公表されている配当予想からの修正の有無
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_CorrectionOfDividendForecastInThisQuarter',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def dividend_payable_date_as_planned(session: Session, head_item_key:str):
    """
    配当支払開始予定日
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_DividendPayableDateAsPlanned',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def document_name(session: Session, head_item_key:str):
    """
    文書名
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_DocumentName',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def fasf_member_mark(session: Session, head_item_key:str):
    """
    財務会計基準機構会員マーク
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_FASFMemberMark',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def filing_date(session: Session, head_item_key:str):
    """
    提出日
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_FilingDate',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def fiscal_year_end(session: Session, head_item_key:str):
    """
    決算期
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_FiscalYearEnd',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def fukuoka_stock_exchange(session: Session, head_item_key:str):
    """
    福岡証券取引所
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_FukuokaStockExchange',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def fukuoka_stock_exchange_established(session: Session, head_item_key:str):
    """
    福岡証券取引所 既存市場
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_FukuokaStockExchangeEstablished',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def fukuoka_stock_exchange_others(session: Session, head_item_key:str):
    """
    福岡証券取引所 その他
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_FukuokaStockExchangeOthers',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def fukuoka_stock_exchange_q_board(session: Session, head_item_key:str):
    """
    福岡証券取引所 Q-Board
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_FukuokaStockExchangeQBoard',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def general_business(session: Session, head_item_key:str):
    """
    一般事業会社
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_GeneralBusiness',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def japan_securities_dealers_association(session: Session, head_item_key:str):
    """
    フェニックス
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_JapanSecuritiesDealersAssociation',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def japan_securities_dealers_association_green_sheet(session: Session, head_item_key:str):
    """
    日本証券業協会 フェニックス
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_JapanSecuritiesDealersAssociationGreenSheet',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def nagoya_stock_exchange(session: Session, head_item_key:str):
    """
    名古屋証券取引所
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_NagoyaStockExchange',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def nagoya_stock_exchange1st_section(session: Session, head_item_key:str):
    """
    名古屋証券取引所 プレミア
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_NagoyaStockExchange1stSection',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def nagoya_stock_exchange2nd_section(session: Session, head_item_key:str):
    """
    名古屋証券取引所 メイン
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_NagoyaStockExchange2ndSection',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def nagoya_stock_exchange_centrex(session: Session, head_item_key:str):
    """
    名古屋証券取引所 ネクスト
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_NagoyaStockExchangeCentrex',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def nagoya_stock_exchange_others(session: Session, head_item_key:str):
    """
    名古屋証券取引所 その他
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_NagoyaStockExchangeOthers',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def name_inquiries(session: Session, head_item_key:str):
    """
    氏名、問合せ先責任者
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_NameInquiries',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def name_of_subsidiaries_excluded_from_consolidation_us(session: Session, head_item_key:str):
    """
    社名、除外、米国基準
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_NameOfSubsidiariesExcludedFromConsolidationUS',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def name_of_subsidiaries_newly_consolidated_us(session: Session, head_item_key:str):
    """
    社名、新規、米国基準
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_NameOfSubsidiariesNewlyConsolidatedUS',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def name_representative(session: Session, head_item_key:str):
    """
    氏名、代表者
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_NameRepresentative',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def note_to_applying_of_simplified_method_of_accounting_and_specific_accounting_of_the_consolidated_quarterly_financial_statements(session: Session, head_item_key:str):
    """
    簡便な会計処理及び特有の会計処理の適用に関する注記、四半期、連結
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_NoteToApplyingOfSimplifiedMethodOfAccountingAndSpecificAccountingOfTheConsolidatedQuarterlyFinancialStatements',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def note_to_changes_in_accounting_principles_procedures_and_the_presentation_of_the_consolidated_quarterly_financial_statements(session: Session, head_item_key:str):
    """
    会計方針の変更に関する注記、四半期、連結
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_NoteToChangesInAccountingPrinciplesProceduresAndThePresentationOfTheConsolidatedQuarterlyFinancialStatements',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def note_to_consolidated_financial_results(session: Session, head_item_key:str):
    """
    連結業績に関する注記
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_NoteToConsolidatedFinancialResults',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def note_to_consolidated_income_statements_information_us(session: Session, head_item_key:str):
    """
    連結損益計算書情報に関する注記、米国基準
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_NoteToConsolidatedIncomeStatementsInformationUS',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def note_to_dividends(session: Session, head_item_key:str):
    """
    配当の状況に関する注記
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_NoteToDividends',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def note_to_financial_positions(session: Session, head_item_key:str):
    """
    財政状態に関する注記
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_NoteToFinancialPositions',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def note_to_forecasts(session: Session, head_item_key:str):
    """
    業績予想に関する事項、注記
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_NoteToForecasts',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def note_to_fraction_processing_method(session: Session, head_item_key:str):
    """
    端数処理方法に関する注記
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_NoteToFractionProcessingMethod',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def note_to_number_of_issued_and_outstanding_shares_common_stock(session: Session, head_item_key:str):
    """
    発行済株式数（普通株式）に関する注記
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_NoteToNumberOfIssuedAndOutstandingSharesCommonStock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def note_to_operating_results(session: Session, head_item_key:str):
    """
    経営成績に関する注記
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_NoteToOperatingResults',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def note_to_significant_changes_in_the_scope_of_consolidation_during_the_period(session: Session, head_item_key:str):
    """
    期中における連結範囲の重要な変更に関する注記
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_NoteToSignificantChangesInTheScopeOfConsolidationDuringThePeriod',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def notes_for_using_forecasted_information_and_others(session: Session, head_item_key:str):
    """
    業績予想の適切な利用に関する説明、その他特記事項
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_NotesForUsingForecastedInformationAndOthers',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def preamble_to_forecasts(session: Session, head_item_key:str):
    """
    業績予想に関する事項
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_PreambleToForecasts',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def review_of_attached_consolidated_quarterly_financial_statements_by_a_certified_public_accountant_or_an_audit_firm(session: Session, head_item_key:str):
    """
    添付される四半期連結財務諸表に対する公認会計士又は監査法人によるレビュー
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_ReviewOfAttachedConsolidatedQuarterlyFinancialStatementsByACertifiedPublicAccountantOrAnAuditFirm',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def sapporo_stock_exchange(session: Session, head_item_key:str):
    """
    札幌証券取引所
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_SapporoStockExchange',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def sapporo_stock_exchange_ambitious(session: Session, head_item_key:str):
    """
    札幌証券取引所 アンビシャス
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_SapporoStockExchangeAmbitious',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def sapporo_stock_exchange_established(session: Session, head_item_key:str):
    """
    札幌証券取引所 既存市場
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_SapporoStockExchangeEstablished',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def sapporo_stock_exchange_others(session: Session, head_item_key:str):
    """
    札幌証券取引所 その他
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_SapporoStockExchangeOthers',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def securities_code(session: Session, head_item_key:str):
    """
    コード番号
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_SecuritiesCode',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def semi_annual_statement_filing_date_as_planned(session: Session, head_item_key:str):
    """
    半期報告書提出予定日
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_SemiAnnualStatementFilingDateAsPlanned',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def significant_changes_in_the_scope_of_consolidation_during_the_period_us(session: Session, head_item_key:str):
    """
    期中における連結範囲の重要な変更、米国基準
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_SignificantChangesInTheScopeOfConsolidationDuringThePeriodUS',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def specific_business(session: Session, head_item_key:str):
    """
    特定事業会社
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_SpecificBusiness',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def supplemental_material_of_results(session: Session, head_item_key:str):
    """
    決算補足説明資料作成の有無、期中
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_SupplementalMaterialOfResults',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def target_for_briefing_of_results(session: Session, head_item_key:str):
    """
    決算説明会の対象者
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_TargetForBriefingOfResults',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def tel(session: Session, head_item_key:str):
    """
    TEL
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_Tel',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def title_for_forecasts(session: Session, head_item_key:str):
    """
    業績予想タイトル名称
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_TitleForForecasts',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def title_inquiries(session: Session, head_item_key:str):
    """
    役職名、問合せ先責任者
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_TitleInquiries',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def title_representative(session: Session, head_item_key:str):
    """
    役職名、代表者
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_TitleRepresentative',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def tokyo_stock_exchange(session: Session, head_item_key:str):
    """
    東京証券取引所
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_TokyoStockExchange',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def tokyo_stock_exchange_growth(session: Session, head_item_key:str):
    """
    東京証券取引所 グロース
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_TokyoStockExchangeGrowth',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def tokyo_stock_exchange_others(session: Session, head_item_key:str):
    """
    東京証券取引所 その他
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_TokyoStockExchangeOthers',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def tokyo_stock_exchange_pro_market(session: Session, head_item_key:str):
    """
    東京証券取引所 PRO Market
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_TokyoStockExchangePROMarket',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def tokyo_stock_exchange_prime(session: Session, head_item_key:str):
    """
    東京証券取引所 プライム
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_TokyoStockExchangePrime',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def tokyo_stock_exchange_standard(session: Session, head_item_key:str):
    """
    東京証券取引所 スタンダード
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_TokyoStockExchangeStandard',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def URL(session: Session, head_item_key:str):
    """
    URL
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_URL',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def way_of_getting_supplemental_material_of_results(session: Session, head_item_key:str):
    """
    入手方法等、決算補足説明資料、期中
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_WayOfGettingSupplementalMaterialOfResults',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

