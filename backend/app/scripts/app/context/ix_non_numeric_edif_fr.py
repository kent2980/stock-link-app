from enum import Enum

class AccountingStandardsDEI(Enum):
    """"会計基準、DEI"""
    FILING_DATE_INSTANT = 'FilingDateInstant'


class AmendmentFlagDEI(Enum):
    """"訂正の有無、DEI"""
    FILING_DATE_INSTANT = 'FilingDateInstant'


class CabinetOfficeOrdinanceDEI(Enum):
    """"府令、DEI"""
    FILING_DATE_INSTANT = 'FilingDateInstant'


class ComparativePeriodEndDateDEI(Enum):
    """"比較対象会計期間終了日、DEI"""
    FILING_DATE_INSTANT = 'FilingDateInstant'


class CurrentFiscalYearEndDateDEI(Enum):
    """"当事業年度終了日、DEI"""
    FILING_DATE_INSTANT = 'FilingDateInstant'


class CurrentFiscalYearStartDateDEI(Enum):
    """"当事業年度開始日、DEI"""
    FILING_DATE_INSTANT = 'FilingDateInstant'


class CurrentPeriodEndDateDEI(Enum):
    """"当会計期間終了日、DEI"""
    FILING_DATE_INSTANT = 'FilingDateInstant'


class DocumentTypeDEI(Enum):
    """"様式、DEI"""
    FILING_DATE_INSTANT = 'FilingDateInstant'


class EDINETCodeDEI(Enum):
    """"EDINETコード、DEI"""
    FILING_DATE_INSTANT = 'FilingDateInstant'


class EndDateOfQuarterlyOrSemiAnnualPeriodOfNextFiscalYearDEI(Enum):
    """"次の四半期又は中間期の会計期間終了日、DEI"""
    FILING_DATE_INSTANT = 'FilingDateInstant'


class FilerNameInEnglishDEI(Enum):
    """"提出者名（英語表記）、DEI"""
    FILING_DATE_INSTANT = 'FilingDateInstant'


class FilerNameInJapaneseDEI(Enum):
    """"提出者名（日本語表記）、DEI"""
    FILING_DATE_INSTANT = 'FilingDateInstant'


class FundCodeDEI(Enum):
    """"ファンドコード、DEI"""
    FILING_DATE_INSTANT = 'FilingDateInstant'


class FundNameInEnglishDEI(Enum):
    """"ファンド名称（英語表記）、DEI"""
    FILING_DATE_INSTANT = 'FilingDateInstant'


class FundNameInJapaneseDEI(Enum):
    """"ファンド名称（日本語表記）、DEI"""
    FILING_DATE_INSTANT = 'FilingDateInstant'


class IdentificationOfDocumentSubjectToAmendmentDEI(Enum):
    """"訂正対象書類の書類管理番号、DEI"""
    FILING_DATE_INSTANT = 'FilingDateInstant'


class IndustryCodeWhenConsolidatedFinancialStatementsArePreparedInAccordanceWithIndustrySpecificRegulationsDEI(Enum):
    """"別記事業（連結）、DEI"""
    FILING_DATE_INSTANT = 'FilingDateInstant'


class IndustryCodeWhenFinancialStatementsArePreparedInAccordanceWithIndustrySpecificRegulationsDEI(Enum):
    """"別記事業（個別）、DEI"""
    FILING_DATE_INSTANT = 'FilingDateInstant'


class NextFiscalYearStartDateDEI(Enum):
    """"次の事業年度開始日、DEI"""
    FILING_DATE_INSTANT = 'FilingDateInstant'


class PreviousFiscalYearEndDateDEI(Enum):
    """"前事業年度終了日、DEI"""
    FILING_DATE_INSTANT = 'FilingDateInstant'


class PreviousFiscalYearStartDateDEI(Enum):
    """"前事業年度開始日、DEI"""
    FILING_DATE_INSTANT = 'FilingDateInstant'


class ReportAmendmentFlagDEI(Enum):
    """"記載事項訂正のフラグ、DEI"""
    FILING_DATE_INSTANT = 'FilingDateInstant'


class SecurityCodeDEI(Enum):
    """"証券コード、DEI"""
    FILING_DATE_INSTANT = 'FilingDateInstant'


class TypeOfCurrentPeriodDEI(Enum):
    """"当会計期間の種類、DEI"""
    FILING_DATE_INSTANT = 'FilingDateInstant'


class WhetherConsolidatedFinancialStatementsArePreparedDEI(Enum):
    """"連結決算の有無、DEI"""
    FILING_DATE_INSTANT = 'FilingDateInstant'


class XBRLAmendmentFlagDEI(Enum):
    """"XBRL訂正のフラグ、DEI"""
    FILING_DATE_INSTANT = 'FilingDateInstant'


class CondensedQuarterPeriodConsolidatedStatementOfComprehensiveIncomeIFRSTextBlock(Enum):
    """"四半期連結会計期間、要約四半期連結包括利益計算書（IFRS） [テキストブロック]"""
    CURRENT_QUARTER_DURATION = 'CurrentQuarterDuration'


class CondensedQuarterPeriodConsolidatedStatementOfProfitOrLossIFRSTextBlock(Enum):
    """"四半期連結会計期間、要約四半期連結損益計算書（IFRS） [テキストブロック]"""
    CURRENT_QUARTER_DURATION = 'CurrentQuarterDuration'


class CondensedQuarterlyConsolidatedStatementOfCashFlowsIFRSTextBlock(Enum):
    """"要約四半期連結キャッシュ・フロー計算書（IFRS） [テキストブロック]"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'


class CondensedQuarterlyConsolidatedStatementOfChangesInEquityIFRSTextBlock(Enum):
    """"要約四半期連結持分変動計算書（IFRS） [テキストブロック]"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'


class CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRSTextBlock(Enum):
    """"要約四半期連結財政状態計算書（IFRS） [テキストブロック]"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'


class CondensedYearToQuarterEndConsolidatedStatementOfComprehensiveIncomeIFRSTextBlock(Enum):
    """"四半期連結累計期間、要約四半期連結包括利益計算書（IFRS） [テキストブロック]"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'


class CondensedYearToQuarterEndConsolidatedStatementOfComprehensiveIncomeSingleStatementIFRSTextBlock(Enum):
    """"四半期連結累計期間、要約四半期連結包括利益計算書（１計算書）（IFRS） [テキストブロック]"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'


class CondensedYearToQuarterEndConsolidatedStatementOfProfitOrLossIFRSTextBlock(Enum):
    """"四半期連結累計期間、要約四半期連結損益計算書（IFRS） [テキストブロック]"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'


class ConsolidatedStatementOfCashFlowsIFRSTextBlock(Enum):
    """"連結キャッシュ・フロー計算書（IFRS） [テキストブロック]"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """


class ConsolidatedStatementOfChangesInEquityIFRSTextBlock(Enum):
    """"連結持分変動計算書（IFRS） [テキストブロック]"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """


class ConsolidatedStatementOfComprehensiveIncomeIFRSTextBlock(Enum):
    """"連結包括利益計算書（IFRS） [テキストブロック]"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """


class ConsolidatedStatementOfFinancialPositionIFRSTextBlock(Enum):
    """"連結財政状態計算書（IFRS） [テキストブロック]"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """


class ConsolidatedStatementOfProfitOrLossIFRSTextBlock(Enum):
    """"連結損益計算書（IFRS） [テキストブロック]"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """


class DescriptionOfFactThatCompanysBusinessComprisesSingleSegmentIFRS(Enum):
    """"単一セグメントである旨（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'


class DisclosureOfChangesInReportableSegmentsIFRSTextBlock(Enum):
    """"報告セグメントの変更に関する事項（IFRS） [テキストブロック]"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class InformationAboutGeographicalAreasIFRSTextBlock(Enum):
    """"地域に関する情報（IFRS） [テキストブロック]"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """


class InformationAboutMajorCustomersIFRSTextBlock(Enum):
    """"主要な顧客に関する情報（IFRS） [テキストブロック]"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """


class InformationAboutProductsAndServicesIFRSTextBlock(Enum):
    """"製品及びサービスに関する情報（IFRS） [テキストブロック]"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """


class NotesSegmentInformationCondensedQuarterlyConsolidatedFinancialStatementsIFRSTextBlock(Enum):
    """"注記事項－セグメント情報、要約四半期連結財務諸表（IFRS） [テキストブロック]"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'


class NotesSegmentInformationConsolidatedFinancialStatementsIFRSTextBlock(Enum):
    """"注記事項－セグメント情報、連結財務諸表（IFRS） [テキストブロック]"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """


