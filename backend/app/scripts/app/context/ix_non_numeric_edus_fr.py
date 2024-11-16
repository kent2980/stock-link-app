from enum import Enum

class QuarterlyConsolidatedBalanceSheetUSGAAPTextBlock(Enum):
    """"四半期連結貸借対照表（US GAAP） [テキストブロック]"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'


class YearToQuarterEndConsolidatedStatementOfComprehensiveIncomeUSGAAPTextBlock(Enum):
    """"四半期連結累計期間、四半期連結包括利益計算書（US GAAP） [テキストブロック]"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'


class YearToQuarterEndConsolidatedStatementOfIncomeUSGAAPTextBlock(Enum):
    """"四半期連結累計期間、四半期連結損益計算書（US GAAP） [テキストブロック]"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'


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


