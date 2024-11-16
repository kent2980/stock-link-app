from enum import Enum

class AnnualSecuritiesReportFilingDateAsPlanned(Enum):
    """"有価証券報告書提出予定日"""
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class ChangesInAccountingEstimatesIFRS(Enum):
    """"会計上の見積りの変更、IFRS"""
    CURRENT_ACCUMULATED_Q1_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ1Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第１四半期間連結実績 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間連結実績 """
    CURRENT_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間連結実績 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ResultMember'
    """ 当年度会計期間連結実績 """


class ChangesInAccountingPoliciesOtherThanIFRSRequirementsIFRS(Enum):
    """"IFRSにより要求される会計方針の変更以外の会計方針の変更、IFRS"""
    CURRENT_ACCUMULATED_Q1_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ1Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第１四半期間連結実績 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間連結実績 """
    CURRENT_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間連結実績 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ResultMember'
    """ 当年度会計期間連結実績 """


class ChangesInAccountingPoliciesRequiredByIFRSIFRS(Enum):
    """"IFRSにより要求される会計方針の変更、IFRS"""
    CURRENT_ACCUMULATED_Q1_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ1Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第１四半期間連結実績 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間連結実績 """
    CURRENT_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間連結実績 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ResultMember'
    """ 当年度会計期間連結実績 """


class CompanyName(Enum):
    """"上場会社名"""
    CURRENT_ACCUMULATED_Q1_INSTANT = 'CurrentAccumulatedQ1Instant'
    """ 当年度期初から第１四半期間時点 """
    CURRENT_ACCUMULATED_Q2_INSTANT = 'CurrentAccumulatedQ2Instant'
    """ 当年度期初から第２四半期間時点 """
    CURRENT_ACCUMULATED_Q3_INSTANT = 'CurrentAccumulatedQ3Instant'
    """ 当年度期初から第３四半期間時点 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class ConveningBriefingOfAnnualResults(Enum):
    """"決算説明会開催の有無"""
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class ConveningBriefingOfResults(Enum):
    """"決算説明会開催の有無、期中"""
    CURRENT_ACCUMULATED_Q1_INSTANT = 'CurrentAccumulatedQ1Instant'
    """ 当年度期初から第１四半期間時点 """
    CURRENT_ACCUMULATED_Q2_INSTANT = 'CurrentAccumulatedQ2Instant'
    """ 当年度期初から第２四半期間時点 """
    CURRENT_ACCUMULATED_Q3_INSTANT = 'CurrentAccumulatedQ3Instant'
    """ 当年度期初から第３四半期間時点 """


class CorrectionOfConsolidatedFinancialForecastInThisQuarter(Enum):
    """"直近に公表されている業績予想からの修正の有無、連結"""
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ForecastMember'
    """ 当年度会計期間連結予想 """


class CorrectionOfDividendForecastInThisQuarter(Enum):
    """"直近に公表されている配当予想からの修正の有無"""
    CURRENT_YEAR_DURATION__ANNUAL_MEMBER__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_AnnualMember_NonConsolidatedMember_ResultMember'
    """ 当年度会計期間年間個別又は非連結実績 """


class DateOfGeneralShareholdersMeetingAsPlanned(Enum):
    """"定時株主総会開催予定日"""
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class DividendPayableDateAsPlanned(Enum):
    """"配当支払開始予定日"""
    CURRENT_ACCUMULATED_Q2_INSTANT = 'CurrentAccumulatedQ2Instant'
    """ 当年度期初から第２四半期間時点 """
    CURRENT_ACCUMULATED_Q3_INSTANT = 'CurrentAccumulatedQ3Instant'
    """ 当年度期初から第３四半期間時点 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class DocumentName(Enum):
    """"文書名"""
    CURRENT_ACCUMULATED_Q1_INSTANT = 'CurrentAccumulatedQ1Instant'
    """ 当年度期初から第１四半期間時点 """
    CURRENT_ACCUMULATED_Q2_INSTANT = 'CurrentAccumulatedQ2Instant'
    """ 当年度期初から第２四半期間時点 """
    CURRENT_ACCUMULATED_Q3_INSTANT = 'CurrentAccumulatedQ3Instant'
    """ 当年度期初から第３四半期間時点 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class FASFMemberMark(Enum):
    """"財務会計基準機構会員マーク"""
    CURRENT_ACCUMULATED_Q1_INSTANT = 'CurrentAccumulatedQ1Instant'
    """ 当年度期初から第１四半期間時点 """
    CURRENT_ACCUMULATED_Q2_INSTANT = 'CurrentAccumulatedQ2Instant'
    """ 当年度期初から第２四半期間時点 """
    CURRENT_ACCUMULATED_Q3_INSTANT = 'CurrentAccumulatedQ3Instant'
    """ 当年度期初から第３四半期間時点 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class FilingDate(Enum):
    """"提出日"""
    CURRENT_ACCUMULATED_Q1_INSTANT = 'CurrentAccumulatedQ1Instant'
    """ 当年度期初から第１四半期間時点 """
    CURRENT_ACCUMULATED_Q2_INSTANT = 'CurrentAccumulatedQ2Instant'
    """ 当年度期初から第２四半期間時点 """
    CURRENT_ACCUMULATED_Q3_INSTANT = 'CurrentAccumulatedQ3Instant'
    """ 当年度期初から第３四半期間時点 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class FiscalYearEnd(Enum):
    """"決算期"""
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class FukuokaStockExchange(Enum):
    """"福岡証券取引所"""
    CURRENT_ACCUMULATED_Q1_INSTANT = 'CurrentAccumulatedQ1Instant'
    """ 当年度期初から第１四半期間時点 """
    CURRENT_ACCUMULATED_Q2_INSTANT = 'CurrentAccumulatedQ2Instant'
    """ 当年度期初から第２四半期間時点 """
    CURRENT_ACCUMULATED_Q3_INSTANT = 'CurrentAccumulatedQ3Instant'
    """ 当年度期初から第３四半期間時点 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class FukuokaStockExchangeEstablished(Enum):
    """"福岡証券取引所 既存市場"""
    CURRENT_ACCUMULATED_Q1_INSTANT = 'CurrentAccumulatedQ1Instant'
    """ 当年度期初から第１四半期間時点 """
    CURRENT_ACCUMULATED_Q2_INSTANT = 'CurrentAccumulatedQ2Instant'
    """ 当年度期初から第２四半期間時点 """
    CURRENT_ACCUMULATED_Q3_INSTANT = 'CurrentAccumulatedQ3Instant'
    """ 当年度期初から第３四半期間時点 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class FukuokaStockExchangeOthers(Enum):
    """"福岡証券取引所 その他"""
    CURRENT_ACCUMULATED_Q1_INSTANT = 'CurrentAccumulatedQ1Instant'
    """ 当年度期初から第１四半期間時点 """
    CURRENT_ACCUMULATED_Q2_INSTANT = 'CurrentAccumulatedQ2Instant'
    """ 当年度期初から第２四半期間時点 """
    CURRENT_ACCUMULATED_Q3_INSTANT = 'CurrentAccumulatedQ3Instant'
    """ 当年度期初から第３四半期間時点 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class FukuokaStockExchangeQBoard(Enum):
    """"福岡証券取引所 Q-Board"""
    CURRENT_ACCUMULATED_Q1_INSTANT = 'CurrentAccumulatedQ1Instant'
    """ 当年度期初から第１四半期間時点 """
    CURRENT_ACCUMULATED_Q2_INSTANT = 'CurrentAccumulatedQ2Instant'
    """ 当年度期初から第２四半期間時点 """
    CURRENT_ACCUMULATED_Q3_INSTANT = 'CurrentAccumulatedQ3Instant'
    """ 当年度期初から第３四半期間時点 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class GeneralBusiness(Enum):
    """"一般事業会社"""
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class JapanSecuritiesDealersAssociation(Enum):
    """"フェニックス"""
    CURRENT_ACCUMULATED_Q1_INSTANT = 'CurrentAccumulatedQ1Instant'
    """ 当年度期初から第１四半期間時点 """
    CURRENT_ACCUMULATED_Q2_INSTANT = 'CurrentAccumulatedQ2Instant'
    """ 当年度期初から第２四半期間時点 """
    CURRENT_ACCUMULATED_Q3_INSTANT = 'CurrentAccumulatedQ3Instant'
    """ 当年度期初から第３四半期間時点 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class JapanSecuritiesDealersAssociationGreenSheet(Enum):
    """"日本証券業協会 フェニックス"""
    CURRENT_ACCUMULATED_Q1_INSTANT = 'CurrentAccumulatedQ1Instant'
    """ 当年度期初から第１四半期間時点 """
    CURRENT_ACCUMULATED_Q2_INSTANT = 'CurrentAccumulatedQ2Instant'
    """ 当年度期初から第２四半期間時点 """
    CURRENT_ACCUMULATED_Q3_INSTANT = 'CurrentAccumulatedQ3Instant'
    """ 当年度期初から第３四半期間時点 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class NagoyaStockExchange(Enum):
    """"名古屋証券取引所"""
    CURRENT_ACCUMULATED_Q1_INSTANT = 'CurrentAccumulatedQ1Instant'
    """ 当年度期初から第１四半期間時点 """
    CURRENT_ACCUMULATED_Q2_INSTANT = 'CurrentAccumulatedQ2Instant'
    """ 当年度期初から第２四半期間時点 """
    CURRENT_ACCUMULATED_Q3_INSTANT = 'CurrentAccumulatedQ3Instant'
    """ 当年度期初から第３四半期間時点 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class NagoyaStockExchange1stSection(Enum):
    """"名古屋証券取引所 プレミア"""
    CURRENT_ACCUMULATED_Q1_INSTANT = 'CurrentAccumulatedQ1Instant'
    """ 当年度期初から第１四半期間時点 """
    CURRENT_ACCUMULATED_Q2_INSTANT = 'CurrentAccumulatedQ2Instant'
    """ 当年度期初から第２四半期間時点 """
    CURRENT_ACCUMULATED_Q3_INSTANT = 'CurrentAccumulatedQ3Instant'
    """ 当年度期初から第３四半期間時点 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class NagoyaStockExchange2ndSection(Enum):
    """"名古屋証券取引所 メイン"""
    CURRENT_ACCUMULATED_Q1_INSTANT = 'CurrentAccumulatedQ1Instant'
    """ 当年度期初から第１四半期間時点 """
    CURRENT_ACCUMULATED_Q2_INSTANT = 'CurrentAccumulatedQ2Instant'
    """ 当年度期初から第２四半期間時点 """
    CURRENT_ACCUMULATED_Q3_INSTANT = 'CurrentAccumulatedQ3Instant'
    """ 当年度期初から第３四半期間時点 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class NagoyaStockExchangeCentrex(Enum):
    """"名古屋証券取引所 ネクスト"""
    CURRENT_ACCUMULATED_Q1_INSTANT = 'CurrentAccumulatedQ1Instant'
    """ 当年度期初から第１四半期間時点 """
    CURRENT_ACCUMULATED_Q2_INSTANT = 'CurrentAccumulatedQ2Instant'
    """ 当年度期初から第２四半期間時点 """
    CURRENT_ACCUMULATED_Q3_INSTANT = 'CurrentAccumulatedQ3Instant'
    """ 当年度期初から第３四半期間時点 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class NagoyaStockExchangeOthers(Enum):
    """"名古屋証券取引所 その他"""
    CURRENT_ACCUMULATED_Q1_INSTANT = 'CurrentAccumulatedQ1Instant'
    """ 当年度期初から第１四半期間時点 """
    CURRENT_ACCUMULATED_Q2_INSTANT = 'CurrentAccumulatedQ2Instant'
    """ 当年度期初から第２四半期間時点 """
    CURRENT_ACCUMULATED_Q3_INSTANT = 'CurrentAccumulatedQ3Instant'
    """ 当年度期初から第３四半期間時点 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class NameInquiries(Enum):
    """"氏名、問合せ先責任者"""
    CURRENT_ACCUMULATED_Q1_INSTANT = 'CurrentAccumulatedQ1Instant'
    """ 当年度期初から第１四半期間時点 """
    CURRENT_ACCUMULATED_Q2_INSTANT = 'CurrentAccumulatedQ2Instant'
    """ 当年度期初から第２四半期間時点 """
    CURRENT_ACCUMULATED_Q3_INSTANT = 'CurrentAccumulatedQ3Instant'
    """ 当年度期初から第３四半期間時点 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class NameOfSubsidiariesExcludedFromConsolidationIFRS(Enum):
    """"社名、除外、IFRS"""
    CURRENT_ACCUMULATED_Q1_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ1Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第１四半期間連結実績 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間連結実績 """
    CURRENT_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間連結実績 """


class NameOfSubsidiariesNewlyConsolidatedIFRS(Enum):
    """"社名、新規、IFRS"""
    CURRENT_ACCUMULATED_Q1_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ1Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第１四半期間連結実績 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間連結実績 """
    CURRENT_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間連結実績 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ResultMember'
    """ 当年度会計期間連結実績 """


class NameRepresentative(Enum):
    """"氏名、代表者"""
    CURRENT_ACCUMULATED_Q1_INSTANT = 'CurrentAccumulatedQ1Instant'
    """ 当年度期初から第１四半期間時点 """
    CURRENT_ACCUMULATED_Q2_INSTANT = 'CurrentAccumulatedQ2Instant'
    """ 当年度期初から第２四半期間時点 """
    CURRENT_ACCUMULATED_Q3_INSTANT = 'CurrentAccumulatedQ3Instant'
    """ 当年度期初から第３四半期間時点 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class NoteToCashFlows(Enum):
    """"キャッシュ・フローの状況に関する注記"""
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ResultMember'
    """ 当年度会計期間連結実績 """


class NoteToChangesInAccountingPoliciesAndAccountingEstimatesIFRS(Enum):
    """"会計方針の変更・会計上の見積りの変更に関する注記、IFRS"""
    CURRENT_ACCUMULATED_Q1_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ1Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第１四半期間連結実績 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間連結実績 """
    CURRENT_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間連結実績 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ResultMember'
    """ 当年度会計期間連結実績 """


class NoteToConsolidatedFinancialResults(Enum):
    """"連結業績に関する注記"""
    CURRENT_ACCUMULATED_Q1_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ1Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第１四半期間連結実績 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間連結実績 """
    CURRENT_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間連結実績 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ResultMember'
    """ 当年度会計期間連結実績 """


class NoteToDividends(Enum):
    """"配当の状況に関する注記"""
    CURRENT_ACCUMULATED_Q1_DURATION__ANNUAL_MEMBER__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ1Duration_AnnualMember_NonConsolidatedMember_ResultMember'
    """ 当年度期初から第１四半期間年間個別又は非連結実績 """
    CURRENT_ACCUMULATED_Q2_DURATION__ANNUAL_MEMBER__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Duration_AnnualMember_NonConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間年間個別又は非連結実績 """
    CURRENT_ACCUMULATED_Q3_DURATION__ANNUAL_MEMBER__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Duration_AnnualMember_NonConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間年間個別又は非連結実績 """
    CURRENT_YEAR_DURATION__ANNUAL_MEMBER__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_AnnualMember_NonConsolidatedMember_ResultMember'
    """ 当年度会計期間年間個別又は非連結実績 """


class NoteToFinancialPositions(Enum):
    """"財政状態に関する注記"""
    CURRENT_ACCUMULATED_Q1_INSTANT__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ1Instant_ConsolidatedMember_ResultMember'
    """ 当年度期初から第１四半期間時点連結実績 """
    CURRENT_ACCUMULATED_Q2_INSTANT__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Instant_ConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間時点連結実績 """
    CURRENT_ACCUMULATED_Q3_INSTANT__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Instant_ConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間時点連結実績 """
    CURRENT_YEAR_INSTANT__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearInstant_ConsolidatedMember_ResultMember'
    """ 当年度時点連結実績 """


class NoteToForecasts(Enum):
    """"業績予想に関する事項、注記"""
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ForecastMember'
    """ 当年度会計期間連結予想 """
    NEXT_YEAR_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'NextYearDuration_ConsolidatedMember_ForecastMember'
    """ 次年度会計期間連結予想 """


class NoteToFractionProcessingMethod(Enum):
    """"端数処理方法に関する注記"""
    CURRENT_ACCUMULATED_Q1_INSTANT = 'CurrentAccumulatedQ1Instant'
    """ 当年度期初から第１四半期間時点 """
    CURRENT_ACCUMULATED_Q2_INSTANT = 'CurrentAccumulatedQ2Instant'
    """ 当年度期初から第２四半期間時点 """
    CURRENT_ACCUMULATED_Q3_INSTANT = 'CurrentAccumulatedQ3Instant'
    """ 当年度期初から第３四半期間時点 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class NoteToNumberOfIssuedAndOutstandingSharesCommonStock(Enum):
    """"発行済株式数（普通株式）に関する注記"""
    CURRENT_ACCUMULATED_Q1_INSTANT__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ1Instant_NonConsolidatedMember_ResultMember'
    """ 当年度期初から第１四半期間時点個別又は非連結実績 """
    CURRENT_ACCUMULATED_Q2_INSTANT__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Instant_NonConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間時点個別又は非連結実績 """
    CURRENT_ACCUMULATED_Q3_INSTANT__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Instant_NonConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間時点個別又は非連結実績 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearInstant_NonConsolidatedMember_ResultMember'
    """ 当年度時点個別又は非連結実績 """


class NoteToOperatingResults(Enum):
    """"経営成績に関する注記"""
    CURRENT_ACCUMULATED_Q1_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ1Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第１四半期間連結実績 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間連結実績 """
    CURRENT_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間連結実績 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ResultMember'
    """ 当年度会計期間連結実績 """


class NoteToSignificantChangesInTheScopeOfConsolidationDuringThePeriod(Enum):
    """"期中における連結範囲の重要な変更に関する注記"""
    CURRENT_ACCUMULATED_Q1_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ1Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第１四半期間連結実績 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間連結実績 """
    CURRENT_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間連結実績 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ResultMember'
    """ 当年度会計期間連結実績 """


class NotesForUsingForecastedInformationAndOthers(Enum):
    """"業績予想の適切な利用に関する説明、その他特記事項"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    NEXT_YEAR_DURATION = 'NextYearDuration'
    """ 次年度会計期間 """


class PreambleToForecasts(Enum):
    """"業績予想に関する事項"""
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ForecastMember'
    """ 当年度会計期間連結予想 """
    NEXT_YEAR_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'NextYearDuration_ConsolidatedMember_ForecastMember'
    """ 次年度会計期間連結予想 """


class ReviewOfAttachedConsolidatedQuarterlyFinancialStatementsByACertifiedPublicAccountantOrAnAuditFirm(Enum):
    """"添付される四半期連結財務諸表に対する公認会計士又は監査法人によるレビュー"""
    CURRENT_ACCUMULATED_Q1_DURATION = 'CurrentAccumulatedQ1Duration'
    """ 当年度期初から第１四半期間 """
    CURRENT_ACCUMULATED_Q3_DURATION = 'CurrentAccumulatedQ3Duration'
    """ 当年度期初から第３四半期間 """


class SapporoStockExchange(Enum):
    """"札幌証券取引所"""
    CURRENT_ACCUMULATED_Q1_INSTANT = 'CurrentAccumulatedQ1Instant'
    """ 当年度期初から第１四半期間時点 """
    CURRENT_ACCUMULATED_Q2_INSTANT = 'CurrentAccumulatedQ2Instant'
    """ 当年度期初から第２四半期間時点 """
    CURRENT_ACCUMULATED_Q3_INSTANT = 'CurrentAccumulatedQ3Instant'
    """ 当年度期初から第３四半期間時点 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class SapporoStockExchangeAmbitious(Enum):
    """"札幌証券取引所 アンビシャス"""
    CURRENT_ACCUMULATED_Q1_INSTANT = 'CurrentAccumulatedQ1Instant'
    """ 当年度期初から第１四半期間時点 """
    CURRENT_ACCUMULATED_Q2_INSTANT = 'CurrentAccumulatedQ2Instant'
    """ 当年度期初から第２四半期間時点 """
    CURRENT_ACCUMULATED_Q3_INSTANT = 'CurrentAccumulatedQ3Instant'
    """ 当年度期初から第３四半期間時点 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class SapporoStockExchangeEstablished(Enum):
    """"札幌証券取引所 既存市場"""
    CURRENT_ACCUMULATED_Q1_INSTANT = 'CurrentAccumulatedQ1Instant'
    """ 当年度期初から第１四半期間時点 """
    CURRENT_ACCUMULATED_Q2_INSTANT = 'CurrentAccumulatedQ2Instant'
    """ 当年度期初から第２四半期間時点 """
    CURRENT_ACCUMULATED_Q3_INSTANT = 'CurrentAccumulatedQ3Instant'
    """ 当年度期初から第３四半期間時点 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class SapporoStockExchangeOthers(Enum):
    """"札幌証券取引所 その他"""
    CURRENT_ACCUMULATED_Q1_INSTANT = 'CurrentAccumulatedQ1Instant'
    """ 当年度期初から第１四半期間時点 """
    CURRENT_ACCUMULATED_Q2_INSTANT = 'CurrentAccumulatedQ2Instant'
    """ 当年度期初から第２四半期間時点 """
    CURRENT_ACCUMULATED_Q3_INSTANT = 'CurrentAccumulatedQ3Instant'
    """ 当年度期初から第３四半期間時点 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class SecuritiesCode(Enum):
    """"コード番号"""
    CURRENT_ACCUMULATED_Q1_INSTANT = 'CurrentAccumulatedQ1Instant'
    """ 当年度期初から第１四半期間時点 """
    CURRENT_ACCUMULATED_Q2_INSTANT = 'CurrentAccumulatedQ2Instant'
    """ 当年度期初から第２四半期間時点 """
    CURRENT_ACCUMULATED_Q3_INSTANT = 'CurrentAccumulatedQ3Instant'
    """ 当年度期初から第３四半期間時点 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class SemiAnnualStatementFilingDateAsPlanned(Enum):
    """"半期報告書提出予定日"""
    CURRENT_ACCUMULATED_Q2_INSTANT = 'CurrentAccumulatedQ2Instant'
    """ 当年度期初から第２四半期間時点 """


class SignificantChangesInTheScopeOfConsolidationDuringThePeriodIFRS(Enum):
    """"期中における連結範囲の重要な変更、IFRS"""
    CURRENT_ACCUMULATED_Q1_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ1Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第１四半期間連結実績 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間連結実績 """
    CURRENT_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間連結実績 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ResultMember'
    """ 当年度会計期間連結実績 """


class SpecificBusiness(Enum):
    """"特定事業会社"""
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class SupplementalMaterialOfAnnualResults(Enum):
    """"決算補足説明資料作成の有無"""
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class SupplementalMaterialOfResults(Enum):
    """"決算補足説明資料作成の有無、期中"""
    CURRENT_ACCUMULATED_Q1_INSTANT = 'CurrentAccumulatedQ1Instant'
    """ 当年度期初から第１四半期間時点 """
    CURRENT_ACCUMULATED_Q2_INSTANT = 'CurrentAccumulatedQ2Instant'
    """ 当年度期初から第２四半期間時点 """
    CURRENT_ACCUMULATED_Q3_INSTANT = 'CurrentAccumulatedQ3Instant'
    """ 当年度期初から第３四半期間時点 """


class TargetAudienceBriefingOfAnnualResults(Enum):
    """"対象者、決算説明会"""
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class TargetForBriefingOfResults(Enum):
    """"決算説明会の対象者"""
    CURRENT_ACCUMULATED_Q1_INSTANT = 'CurrentAccumulatedQ1Instant'
    """ 当年度期初から第１四半期間時点 """
    CURRENT_ACCUMULATED_Q2_INSTANT = 'CurrentAccumulatedQ2Instant'
    """ 当年度期初から第２四半期間時点 """
    CURRENT_ACCUMULATED_Q3_INSTANT = 'CurrentAccumulatedQ3Instant'
    """ 当年度期初から第３四半期間時点 """


class Tel(Enum):
    """"TEL"""
    CURRENT_ACCUMULATED_Q1_INSTANT = 'CurrentAccumulatedQ1Instant'
    """ 当年度期初から第１四半期間時点 """
    CURRENT_ACCUMULATED_Q2_INSTANT = 'CurrentAccumulatedQ2Instant'
    """ 当年度期初から第２四半期間時点 """
    CURRENT_ACCUMULATED_Q3_INSTANT = 'CurrentAccumulatedQ3Instant'
    """ 当年度期初から第３四半期間時点 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class TitleForForecasts(Enum):
    """"業績予想タイトル名称"""
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ForecastMember'
    """ 当年度会計期間連結予想 """
    NEXT_YEAR_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'NextYearDuration_ConsolidatedMember_ForecastMember'
    """ 次年度会計期間連結予想 """


class TitleInquiries(Enum):
    """"役職名、問合せ先責任者"""
    CURRENT_ACCUMULATED_Q1_INSTANT = 'CurrentAccumulatedQ1Instant'
    """ 当年度期初から第１四半期間時点 """
    CURRENT_ACCUMULATED_Q2_INSTANT = 'CurrentAccumulatedQ2Instant'
    """ 当年度期初から第２四半期間時点 """
    CURRENT_ACCUMULATED_Q3_INSTANT = 'CurrentAccumulatedQ3Instant'
    """ 当年度期初から第３四半期間時点 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class TitleRepresentative(Enum):
    """"役職名、代表者"""
    CURRENT_ACCUMULATED_Q1_INSTANT = 'CurrentAccumulatedQ1Instant'
    """ 当年度期初から第１四半期間時点 """
    CURRENT_ACCUMULATED_Q2_INSTANT = 'CurrentAccumulatedQ2Instant'
    """ 当年度期初から第２四半期間時点 """
    CURRENT_ACCUMULATED_Q3_INSTANT = 'CurrentAccumulatedQ3Instant'
    """ 当年度期初から第３四半期間時点 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class TokyoStockExchange(Enum):
    """"東京証券取引所"""
    CURRENT_ACCUMULATED_Q1_INSTANT = 'CurrentAccumulatedQ1Instant'
    """ 当年度期初から第１四半期間時点 """
    CURRENT_ACCUMULATED_Q2_INSTANT = 'CurrentAccumulatedQ2Instant'
    """ 当年度期初から第２四半期間時点 """
    CURRENT_ACCUMULATED_Q3_INSTANT = 'CurrentAccumulatedQ3Instant'
    """ 当年度期初から第３四半期間時点 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class TokyoStockExchange1stSection(Enum):
    """"東京証券取引所 第一部"""
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class TokyoStockExchange2ndSection(Enum):
    """"東京証券取引所 第二部"""
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class TokyoStockExchangeGrowth(Enum):
    """"東京証券取引所 グロース"""
    CURRENT_ACCUMULATED_Q1_INSTANT = 'CurrentAccumulatedQ1Instant'
    """ 当年度期初から第１四半期間時点 """
    CURRENT_ACCUMULATED_Q2_INSTANT = 'CurrentAccumulatedQ2Instant'
    """ 当年度期初から第２四半期間時点 """
    CURRENT_ACCUMULATED_Q3_INSTANT = 'CurrentAccumulatedQ3Instant'
    """ 当年度期初から第３四半期間時点 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class TokyoStockExchangeJASDAQ(Enum):
    """"東京証券取引所 JASDAQ"""
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class TokyoStockExchangeMothers(Enum):
    """"東京証券取引所 マザーズ"""
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class TokyoStockExchangeOthers(Enum):
    """"東京証券取引所 その他"""
    CURRENT_ACCUMULATED_Q1_INSTANT = 'CurrentAccumulatedQ1Instant'
    """ 当年度期初から第１四半期間時点 """
    CURRENT_ACCUMULATED_Q2_INSTANT = 'CurrentAccumulatedQ2Instant'
    """ 当年度期初から第２四半期間時点 """
    CURRENT_ACCUMULATED_Q3_INSTANT = 'CurrentAccumulatedQ3Instant'
    """ 当年度期初から第３四半期間時点 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class TokyoStockExchangePROMarket(Enum):
    """"東京証券取引所 PRO Market"""
    CURRENT_ACCUMULATED_Q1_INSTANT = 'CurrentAccumulatedQ1Instant'
    """ 当年度期初から第１四半期間時点 """
    CURRENT_ACCUMULATED_Q2_INSTANT = 'CurrentAccumulatedQ2Instant'
    """ 当年度期初から第２四半期間時点 """
    CURRENT_ACCUMULATED_Q3_INSTANT = 'CurrentAccumulatedQ3Instant'
    """ 当年度期初から第３四半期間時点 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class TokyoStockExchangePrime(Enum):
    """"東京証券取引所 プライム"""
    CURRENT_ACCUMULATED_Q1_INSTANT = 'CurrentAccumulatedQ1Instant'
    """ 当年度期初から第１四半期間時点 """
    CURRENT_ACCUMULATED_Q2_INSTANT = 'CurrentAccumulatedQ2Instant'
    """ 当年度期初から第２四半期間時点 """
    CURRENT_ACCUMULATED_Q3_INSTANT = 'CurrentAccumulatedQ3Instant'
    """ 当年度期初から第３四半期間時点 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class TokyoStockExchangeStandard(Enum):
    """"東京証券取引所 スタンダード"""
    CURRENT_ACCUMULATED_Q1_INSTANT = 'CurrentAccumulatedQ1Instant'
    """ 当年度期初から第１四半期間時点 """
    CURRENT_ACCUMULATED_Q2_INSTANT = 'CurrentAccumulatedQ2Instant'
    """ 当年度期初から第２四半期間時点 """
    CURRENT_ACCUMULATED_Q3_INSTANT = 'CurrentAccumulatedQ3Instant'
    """ 当年度期初から第３四半期間時点 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class URL(Enum):
    """"URL"""
    CURRENT_ACCUMULATED_Q1_INSTANT = 'CurrentAccumulatedQ1Instant'
    """ 当年度期初から第１四半期間時点 """
    CURRENT_ACCUMULATED_Q2_INSTANT = 'CurrentAccumulatedQ2Instant'
    """ 当年度期初から第２四半期間時点 """
    CURRENT_ACCUMULATED_Q3_INSTANT = 'CurrentAccumulatedQ3Instant'
    """ 当年度期初から第３四半期間時点 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class WayOfGettingSupplementalMaterialOfAnnualResults(Enum):
    """"入手方法等、決算補足説明資料"""
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class WayOfGettingSupplementalMaterialOfResults(Enum):
    """"入手方法等、決算補足説明資料、期中"""
    CURRENT_ACCUMULATED_Q1_INSTANT = 'CurrentAccumulatedQ1Instant'
    """ 当年度期初から第１四半期間時点 """
    CURRENT_ACCUMULATED_Q2_INSTANT = 'CurrentAccumulatedQ2Instant'
    """ 当年度期初から第２四半期間時点 """
    CURRENT_ACCUMULATED_Q3_INSTANT = 'CurrentAccumulatedQ3Instant'
    """ 当年度期初から第３四半期間時点 """


