from app.models import IxNonNumeric
from sqlmodel import Session, select

def quarterly_consolidated_balance_sheet_usgaap_text_block(session: Session, head_item_key:str):
    """
    四半期連結貸借対照表（US GAAP） [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpcrp_cor_QuarterlyConsolidatedBalanceSheetUSGAAPTextBlock',
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

def year_to_quarter_end_consolidated_statement_of_comprehensive_income_usgaap_text_block(session: Session, head_item_key:str):
    """
    四半期連結累計期間、四半期連結包括利益計算書（US GAAP） [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpcrp_cor_YearToQuarterEndConsolidatedStatementOfComprehensiveIncomeUSGAAPTextBlock',
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

def year_to_quarter_end_consolidated_statement_of_income_usgaap_text_block(session: Session, head_item_key:str):
    """
    四半期連結累計期間、四半期連結損益計算書（US GAAP） [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpcrp_cor_YearToQuarterEndConsolidatedStatementOfIncomeUSGAAPTextBlock',
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

def accounting_standards_dei(session: Session, head_item_key:str):
    """
    会計基準、DEI
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpdei_cor_AccountingStandardsDEI',
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

def amendment_flag_dei(session: Session, head_item_key:str):
    """
    訂正の有無、DEI
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpdei_cor_AmendmentFlagDEI',
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

def cabinet_office_ordinance_dei(session: Session, head_item_key:str):
    """
    府令、DEI
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpdei_cor_CabinetOfficeOrdinanceDEI',
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

def comparative_period_end_date_dei(session: Session, head_item_key:str):
    """
    比較対象会計期間終了日、DEI
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpdei_cor_ComparativePeriodEndDateDEI',
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

def current_fiscal_year_end_date_dei(session: Session, head_item_key:str):
    """
    当事業年度終了日、DEI
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpdei_cor_CurrentFiscalYearEndDateDEI',
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

def current_fiscal_year_start_date_dei(session: Session, head_item_key:str):
    """
    当事業年度開始日、DEI
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpdei_cor_CurrentFiscalYearStartDateDEI',
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

def current_period_end_date_dei(session: Session, head_item_key:str):
    """
    当会計期間終了日、DEI
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpdei_cor_CurrentPeriodEndDateDEI',
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

def document_type_dei(session: Session, head_item_key:str):
    """
    様式、DEI
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpdei_cor_DocumentTypeDEI',
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

def edinet_code_dei(session: Session, head_item_key:str):
    """
    EDINETコード、DEI
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpdei_cor_EDINETCodeDEI',
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

def end_date_of_quarterly_or_semi_annual_period_of_next_fiscal_year_dei(session: Session, head_item_key:str):
    """
    次の四半期又は中間期の会計期間終了日、DEI
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpdei_cor_EndDateOfQuarterlyOrSemiAnnualPeriodOfNextFiscalYearDEI',
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

def filer_name_in_english_dei(session: Session, head_item_key:str):
    """
    提出者名（英語表記）、DEI
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpdei_cor_FilerNameInEnglishDEI',
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

def filer_name_in_japanese_dei(session: Session, head_item_key:str):
    """
    提出者名（日本語表記）、DEI
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpdei_cor_FilerNameInJapaneseDEI',
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

def fund_code_dei(session: Session, head_item_key:str):
    """
    ファンドコード、DEI
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpdei_cor_FundCodeDEI',
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

def fund_name_in_english_dei(session: Session, head_item_key:str):
    """
    ファンド名称（英語表記）、DEI
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpdei_cor_FundNameInEnglishDEI',
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

def fund_name_in_japanese_dei(session: Session, head_item_key:str):
    """
    ファンド名称（日本語表記）、DEI
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpdei_cor_FundNameInJapaneseDEI',
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

def identification_of_document_subject_to_amendment_dei(session: Session, head_item_key:str):
    """
    訂正対象書類の書類管理番号、DEI
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpdei_cor_IdentificationOfDocumentSubjectToAmendmentDEI',
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

def industry_code_when_consolidated_financial_statements_are_prepared_in_accordance_with_industry_specific_regulations_dei(session: Session, head_item_key:str):
    """
    別記事業（連結）、DEI
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpdei_cor_IndustryCodeWhenConsolidatedFinancialStatementsArePreparedInAccordanceWithIndustrySpecificRegulationsDEI',
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

def industry_code_when_financial_statements_are_prepared_in_accordance_with_industry_specific_regulations_dei(session: Session, head_item_key:str):
    """
    別記事業（個別）、DEI
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpdei_cor_IndustryCodeWhenFinancialStatementsArePreparedInAccordanceWithIndustrySpecificRegulationsDEI',
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

def next_fiscal_year_start_date_dei(session: Session, head_item_key:str):
    """
    次の事業年度開始日、DEI
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpdei_cor_NextFiscalYearStartDateDEI',
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

def previous_fiscal_year_end_date_dei(session: Session, head_item_key:str):
    """
    前事業年度終了日、DEI
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpdei_cor_PreviousFiscalYearEndDateDEI',
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

def previous_fiscal_year_start_date_dei(session: Session, head_item_key:str):
    """
    前事業年度開始日、DEI
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpdei_cor_PreviousFiscalYearStartDateDEI',
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

def report_amendment_flag_dei(session: Session, head_item_key:str):
    """
    記載事項訂正のフラグ、DEI
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpdei_cor_ReportAmendmentFlagDEI',
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

def security_code_dei(session: Session, head_item_key:str):
    """
    証券コード、DEI
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpdei_cor_SecurityCodeDEI',
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

def type_of_current_period_dei(session: Session, head_item_key:str):
    """
    当会計期間の種類、DEI
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpdei_cor_TypeOfCurrentPeriodDEI',
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

def whether_consolidated_financial_statements_are_prepared_dei(session: Session, head_item_key:str):
    """
    連結決算の有無、DEI
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpdei_cor_WhetherConsolidatedFinancialStatementsArePreparedDEI',
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

def xbrl_amendment_flag_dei(session: Session, head_item_key:str):
    """
    XBRL訂正のフラグ、DEI
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpdei_cor_XBRLAmendmentFlagDEI',
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

