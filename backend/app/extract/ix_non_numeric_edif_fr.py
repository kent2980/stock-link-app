from app.models import IxNonNumeric
from sqlmodel import Session, select

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

def condensed_quarter_period_consolidated_statement_of_comprehensive_income_ifrs_text_block(session: Session, head_item_key:str):
    """
    四半期連結会計期間、要約四半期連結包括利益計算書（IFRS） [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpigp_cor_CondensedQuarterPeriodConsolidatedStatementOfComprehensiveIncomeIFRSTextBlock',
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

def condensed_quarter_period_consolidated_statement_of_profit_or_loss_ifrs_text_block(session: Session, head_item_key:str):
    """
    四半期連結会計期間、要約四半期連結損益計算書（IFRS） [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpigp_cor_CondensedQuarterPeriodConsolidatedStatementOfProfitOrLossIFRSTextBlock',
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

def condensed_quarterly_consolidated_statement_of_cash_flows_ifrs_text_block(session: Session, head_item_key:str):
    """
    要約四半期連結キャッシュ・フロー計算書（IFRS） [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpigp_cor_CondensedQuarterlyConsolidatedStatementOfCashFlowsIFRSTextBlock',
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

def condensed_quarterly_consolidated_statement_of_changes_in_equity_ifrs_text_block(session: Session, head_item_key:str):
    """
    要約四半期連結持分変動計算書（IFRS） [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpigp_cor_CondensedQuarterlyConsolidatedStatementOfChangesInEquityIFRSTextBlock',
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

def condensed_quarterly_consolidated_statement_of_financial_position_ifrs_text_block(session: Session, head_item_key:str):
    """
    要約四半期連結財政状態計算書（IFRS） [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpigp_cor_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRSTextBlock',
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

def condensed_year_to_quarter_end_consolidated_statement_of_comprehensive_income_ifrs_text_block(session: Session, head_item_key:str):
    """
    四半期連結累計期間、要約四半期連結包括利益計算書（IFRS） [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpigp_cor_CondensedYearToQuarterEndConsolidatedStatementOfComprehensiveIncomeIFRSTextBlock',
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

def condensed_year_to_quarter_end_consolidated_statement_of_comprehensive_income_single_statement_ifrs_text_block(session: Session, head_item_key:str):
    """
    四半期連結累計期間、要約四半期連結包括利益計算書（１計算書）（IFRS） [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpigp_cor_CondensedYearToQuarterEndConsolidatedStatementOfComprehensiveIncomeSingleStatementIFRSTextBlock',
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

def condensed_year_to_quarter_end_consolidated_statement_of_profit_or_loss_ifrs_text_block(session: Session, head_item_key:str):
    """
    四半期連結累計期間、要約四半期連結損益計算書（IFRS） [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpigp_cor_CondensedYearToQuarterEndConsolidatedStatementOfProfitOrLossIFRSTextBlock',
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

def consolidated_statement_of_cash_flows_ifrs_text_block(session: Session, head_item_key:str):
    """
    連結キャッシュ・フロー計算書（IFRS） [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpigp_cor_ConsolidatedStatementOfCashFlowsIFRSTextBlock',
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

def consolidated_statement_of_changes_in_equity_ifrs_text_block(session: Session, head_item_key:str):
    """
    連結持分変動計算書（IFRS） [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpigp_cor_ConsolidatedStatementOfChangesInEquityIFRSTextBlock',
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

def consolidated_statement_of_comprehensive_income_ifrs_text_block(session: Session, head_item_key:str):
    """
    連結包括利益計算書（IFRS） [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpigp_cor_ConsolidatedStatementOfComprehensiveIncomeIFRSTextBlock',
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

def consolidated_statement_of_financial_position_ifrs_text_block(session: Session, head_item_key:str):
    """
    連結財政状態計算書（IFRS） [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpigp_cor_ConsolidatedStatementOfFinancialPositionIFRSTextBlock',
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

def consolidated_statement_of_profit_or_loss_ifrs_text_block(session: Session, head_item_key:str):
    """
    連結損益計算書（IFRS） [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpigp_cor_ConsolidatedStatementOfProfitOrLossIFRSTextBlock',
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

def description_of_fact_that_companys_business_comprises_single_segment_ifrs(session: Session, head_item_key:str):
    """
    単一セグメントである旨（IFRS）
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpigp_cor_DescriptionOfFactThatCompanysBusinessComprisesSingleSegmentIFRS',
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

def disclosure_of_changes_in_reportable_segments_ifrs_text_block(session: Session, head_item_key:str):
    """
    報告セグメントの変更に関する事項（IFRS） [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpigp_cor_DisclosureOfChangesInReportableSegmentsIFRSTextBlock',
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

def information_about_geographical_areas_ifrs_text_block(session: Session, head_item_key:str):
    """
    地域に関する情報（IFRS） [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpigp_cor_InformationAboutGeographicalAreasIFRSTextBlock',
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

def information_about_major_customers_ifrs_text_block(session: Session, head_item_key:str):
    """
    主要な顧客に関する情報（IFRS） [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpigp_cor_InformationAboutMajorCustomersIFRSTextBlock',
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

def information_about_products_and_services_ifrs_text_block(session: Session, head_item_key:str):
    """
    製品及びサービスに関する情報（IFRS） [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpigp_cor_InformationAboutProductsAndServicesIFRSTextBlock',
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

def notes_segment_information_condensed_quarterly_consolidated_financial_statements_ifrs_text_block(session: Session, head_item_key:str):
    """
    注記事項－セグメント情報、要約四半期連結財務諸表（IFRS） [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpigp_cor_NotesSegmentInformationCondensedQuarterlyConsolidatedFinancialStatementsIFRSTextBlock',
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

def notes_segment_information_consolidated_financial_statements_ifrs_text_block(session: Session, head_item_key:str):
    """
    注記事項－セグメント情報、連結財務諸表（IFRS） [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpigp_cor_NotesSegmentInformationConsolidatedFinancialStatementsIFRSTextBlock',
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

