from enum import Enum

class CompanyName(Enum):
    """"上場会社名"""
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class DocumentName(Enum):
    """"文書名"""
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class FASFMemberMark(Enum):
    """"財務会計基準機構会員マーク"""
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class FiscalYearEnd(Enum):
    """"決算期"""
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class FukuokaStockExchange(Enum):
    """"福岡証券取引所"""
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class FukuokaStockExchangeEstablished(Enum):
    """"福岡証券取引所 既存市場"""
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class FukuokaStockExchangeOthers(Enum):
    """"福岡証券取引所 その他"""
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class FukuokaStockExchangeQBoard(Enum):
    """"福岡証券取引所 Q-Board"""
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class GeneralBusiness(Enum):
    """"一般事業会社"""
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class JapanSecuritiesDealersAssociation(Enum):
    """"フェニックス"""
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class JapanSecuritiesDealersAssociationGreenSheet(Enum):
    """"日本証券業協会 フェニックス"""
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class NagoyaStockExchange(Enum):
    """"名古屋証券取引所"""
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class NagoyaStockExchange1stSection(Enum):
    """"名古屋証券取引所 プレミア"""
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class NagoyaStockExchange2ndSection(Enum):
    """"名古屋証券取引所 メイン"""
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class NagoyaStockExchangeCentrex(Enum):
    """"名古屋証券取引所 ネクスト"""
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class NagoyaStockExchangeOthers(Enum):
    """"名古屋証券取引所 その他"""
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class NameInquiries(Enum):
    """"氏名、問合せ先責任者"""
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class NameRepresentative(Enum):
    """"氏名、代表者"""
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class NoteToDividends(Enum):
    """"配当の状況に関する注記"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """


class NoteToFinancialForecast(Enum):
    """"業績予想の状況に関する注記"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """


class NoticeOfForecastCorrection(Enum):
    """"予想修正に関するお知らせ"""
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class PreambleToForecasts(Enum):
    """"業績予想に関する事項"""
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度期初から第２四半期間連結今回予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度期初から第２四半期間個別又は非連結今回予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度会計期間連結今回予想 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度会計期間個別又は非連結今回予想 """


class PreviousReportingDateOfDividendForecast(Enum):
    """"前回予想発表日、配当予想の修正について"""
    CURRENT_YEAR_INSTANT__ANNUAL_MEMBER__NON_CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__RESULT_MEMBER = 'CurrentYearInstant_AnnualMember_NonConsolidatedMember_PreviousMember_ResultMember'
    """ 当年度時点年間個別又は非連結前回実績 """


class ReasonForDividendForecastCorrection(Enum):
    """"配当予想修正の理由"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """


class ReasonForForecastCorrection(Enum):
    """"業績予想修正の理由"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """


class ReportingDateOfFinancialForecastCorrection(Enum):
    """"予想修正報告日"""
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class SapporoStockExchange(Enum):
    """"札幌証券取引所"""
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class SapporoStockExchangeAmbitious(Enum):
    """"札幌証券取引所 アンビシャス"""
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class SapporoStockExchangeEstablished(Enum):
    """"札幌証券取引所 既存市場"""
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class SapporoStockExchangeOthers(Enum):
    """"札幌証券取引所 その他"""
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class SecuritiesCode(Enum):
    """"コード番号"""
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class SpecificBusiness(Enum):
    """"特定事業会社"""
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class Tel(Enum):
    """"TEL"""
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class TitleInquiries(Enum):
    """"役職名、問合せ先責任者"""
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class TitleRepresentative(Enum):
    """"役職名、代表者"""
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class TokyoStockExchange(Enum):
    """"東京証券取引所"""
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class TokyoStockExchangeGrowth(Enum):
    """"東京証券取引所 グロース"""
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class TokyoStockExchangeOthers(Enum):
    """"東京証券取引所 その他"""
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class TokyoStockExchangePROMarket(Enum):
    """"東京証券取引所 PRO Market"""
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class TokyoStockExchangePrime(Enum):
    """"東京証券取引所 プライム"""
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class TokyoStockExchangeStandard(Enum):
    """"東京証券取引所 スタンダード"""
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


