from app.models import IxNonNumeric
from sqlmodel import Session, select

def annual_securities_report_filing_date_as_planned(*, session: Session, head_item_key:str, context:str):
    """
    有価証券報告書提出予定日
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_AnnualSecuritiesReportFilingDateAsPlanned',
            IxNonNumeric.head_item_key == head_item_key,
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def changes_in_accounting_estimates_ifrs(*, session: Session, head_item_key:str, context:str):
    """
    会計上の見積りの変更、IFRS
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_ChangesInAccountingEstimatesIFRS',
            IxNonNumeric.head_item_key == head_item_key,
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def changes_in_accounting_policies_other_than_ifrs_requirements_ifrs(*, session: Session, head_item_key:str, context:str):
    """
    IFRSにより要求される会計方針の変更以外の会計方針の変更、IFRS
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_ChangesInAccountingPoliciesOtherThanIFRSRequirementsIFRS',
            IxNonNumeric.head_item_key == head_item_key,
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def changes_in_accounting_policies_required_by_ifrsifrs(*, session: Session, head_item_key:str, context:str):
    """
    IFRSにより要求される会計方針の変更、IFRS
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_ChangesInAccountingPoliciesRequiredByIFRSIFRS',
            IxNonNumeric.head_item_key == head_item_key,
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

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

def convening_briefing_of_annual_results(*, session: Session, head_item_key:str, context:str):
    """
    決算説明会開催の有無
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_ConveningBriefingOfAnnualResults',
            IxNonNumeric.head_item_key == head_item_key,
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def convening_briefing_of_results(*, session: Session, head_item_key:str, context:str):
    """
    決算説明会開催の有無、期中
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_ConveningBriefingOfResults',
            IxNonNumeric.head_item_key == head_item_key,
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def correction_of_consolidated_financial_forecast_in_this_quarter(*, session: Session, head_item_key:str, context:str):
    """
    直近に公表されている業績予想からの修正の有無、連結
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_CorrectionOfConsolidatedFinancialForecastInThisQuarter',
            IxNonNumeric.head_item_key == head_item_key,
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def correction_of_dividend_forecast_in_this_quarter(*, session: Session, head_item_key:str, context:str):
    """
    直近に公表されている配当予想からの修正の有無
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_CorrectionOfDividendForecastInThisQuarter',
            IxNonNumeric.head_item_key == head_item_key,
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def date_of_general_shareholders_meeting_as_planned(*, session: Session, head_item_key:str, context:str):
    """
    定時株主総会開催予定日
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_DateOfGeneralShareholdersMeetingAsPlanned',
            IxNonNumeric.head_item_key == head_item_key,
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def dividend_payable_date_as_planned(*, session: Session, head_item_key:str, context:str):
    """
    配当支払開始予定日
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_DividendPayableDateAsPlanned',
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

def filing_date(*, session: Session, head_item_key:str, context:str):
    """
    提出日
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_FilingDate',
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

def name_of_subsidiaries_excluded_from_consolidation_ifrs(*, session: Session, head_item_key:str, context:str):
    """
    社名、除外、IFRS
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_NameOfSubsidiariesExcludedFromConsolidationIFRS',
            IxNonNumeric.head_item_key == head_item_key,
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def name_of_subsidiaries_newly_consolidated_ifrs(*, session: Session, head_item_key:str, context:str):
    """
    社名、新規、IFRS
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_NameOfSubsidiariesNewlyConsolidatedIFRS',
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

def note_to_cash_flows(*, session: Session, head_item_key:str, context:str):
    """
    キャッシュ・フローの状況に関する注記
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_NoteToCashFlows',
            IxNonNumeric.head_item_key == head_item_key,
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def note_to_changes_in_accounting_policies_and_accounting_estimates_ifrs(*, session: Session, head_item_key:str, context:str):
    """
    会計方針の変更・会計上の見積りの変更に関する注記、IFRS
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_NoteToChangesInAccountingPoliciesAndAccountingEstimatesIFRS',
            IxNonNumeric.head_item_key == head_item_key,
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def note_to_consolidated_financial_results(*, session: Session, head_item_key:str, context:str):
    """
    連結業績に関する注記
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_NoteToConsolidatedFinancialResults',
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

def note_to_financial_positions(*, session: Session, head_item_key:str, context:str):
    """
    財政状態に関する注記
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_NoteToFinancialPositions',
            IxNonNumeric.head_item_key == head_item_key,
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def note_to_forecasts(*, session: Session, head_item_key:str, context:str):
    """
    業績予想に関する事項、注記
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_NoteToForecasts',
            IxNonNumeric.head_item_key == head_item_key,
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def note_to_fraction_processing_method(*, session: Session, head_item_key:str, context:str):
    """
    端数処理方法に関する注記
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_NoteToFractionProcessingMethod',
            IxNonNumeric.head_item_key == head_item_key,
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def note_to_number_of_issued_and_outstanding_shares_common_stock(*, session: Session, head_item_key:str, context:str):
    """
    発行済株式数（普通株式）に関する注記
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_NoteToNumberOfIssuedAndOutstandingSharesCommonStock',
            IxNonNumeric.head_item_key == head_item_key,
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def note_to_operating_results(*, session: Session, head_item_key:str, context:str):
    """
    経営成績に関する注記
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_NoteToOperatingResults',
            IxNonNumeric.head_item_key == head_item_key,
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def note_to_significant_changes_in_the_scope_of_consolidation_during_the_period(*, session: Session, head_item_key:str, context:str):
    """
    期中における連結範囲の重要な変更に関する注記
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_NoteToSignificantChangesInTheScopeOfConsolidationDuringThePeriod',
            IxNonNumeric.head_item_key == head_item_key,
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def notes_for_using_forecasted_information_and_others(*, session: Session, head_item_key:str, context:str):
    """
    業績予想の適切な利用に関する説明、その他特記事項
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_NotesForUsingForecastedInformationAndOthers',
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

def review_of_attached_consolidated_quarterly_financial_statements_by_a_certified_public_accountant_or_an_audit_firm(*, session: Session, head_item_key:str, context:str):
    """
    添付される四半期連結財務諸表に対する公認会計士又は監査法人によるレビュー
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_ReviewOfAttachedConsolidatedQuarterlyFinancialStatementsByACertifiedPublicAccountantOrAnAuditFirm',
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

def semi_annual_statement_filing_date_as_planned(*, session: Session, head_item_key:str, context:str):
    """
    半期報告書提出予定日
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_SemiAnnualStatementFilingDateAsPlanned',
            IxNonNumeric.head_item_key == head_item_key,
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def significant_changes_in_the_scope_of_consolidation_during_the_period_ifrs(*, session: Session, head_item_key:str, context:str):
    """
    期中における連結範囲の重要な変更、IFRS
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_SignificantChangesInTheScopeOfConsolidationDuringThePeriodIFRS',
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

def supplemental_material_of_annual_results(*, session: Session, head_item_key:str, context:str):
    """
    決算補足説明資料作成の有無
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_SupplementalMaterialOfAnnualResults',
            IxNonNumeric.head_item_key == head_item_key,
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def supplemental_material_of_results(*, session: Session, head_item_key:str, context:str):
    """
    決算補足説明資料作成の有無、期中
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_SupplementalMaterialOfResults',
            IxNonNumeric.head_item_key == head_item_key,
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def target_audience_briefing_of_annual_results(*, session: Session, head_item_key:str, context:str):
    """
    対象者、決算説明会
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_TargetAudienceBriefingOfAnnualResults',
            IxNonNumeric.head_item_key == head_item_key,
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def target_for_briefing_of_results(*, session: Session, head_item_key:str, context:str):
    """
    決算説明会の対象者
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_TargetForBriefingOfResults',
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

def title_for_forecasts(*, session: Session, head_item_key:str, context:str):
    """
    業績予想タイトル名称
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_TitleForForecasts',
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

def tokyo_stock_exchange1st_section(*, session: Session, head_item_key:str, context:str):
    """
    東京証券取引所 第一部
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_TokyoStockExchange1stSection',
            IxNonNumeric.head_item_key == head_item_key,
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def tokyo_stock_exchange2nd_section(*, session: Session, head_item_key:str, context:str):
    """
    東京証券取引所 第二部
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_TokyoStockExchange2ndSection',
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

def tokyo_stock_exchange_jasdaq(*, session: Session, head_item_key:str, context:str):
    """
    東京証券取引所 JASDAQ
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_TokyoStockExchangeJASDAQ',
            IxNonNumeric.head_item_key == head_item_key,
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def tokyo_stock_exchange_mothers(*, session: Session, head_item_key:str, context:str):
    """
    東京証券取引所 マザーズ
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_TokyoStockExchangeMothers',
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

def URL(*, session: Session, head_item_key:str, context:str):
    """
    URL
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_URL',
            IxNonNumeric.head_item_key == head_item_key,
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def way_of_getting_supplemental_material_of_annual_results(*, session: Session, head_item_key:str, context:str):
    """
    入手方法等、決算補足説明資料
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_WayOfGettingSupplementalMaterialOfAnnualResults',
            IxNonNumeric.head_item_key == head_item_key,
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def way_of_getting_supplemental_material_of_results(*, session: Session, head_item_key:str, context:str):
    """
    入手方法等、決算補足説明資料、期中
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-ed-t_WayOfGettingSupplementalMaterialOfResults',
            IxNonNumeric.head_item_key == head_item_key,
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

