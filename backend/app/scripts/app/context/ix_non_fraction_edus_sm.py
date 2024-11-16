from enum import Enum

class AverageNumberOfShares(Enum):
    """"期中平均株式数"""
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間個別又は非連結実績 """
    CURRENT_ACCUMULATED_Q3_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Duration_NonConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間個別又は非連結実績 """
    PRIOR_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ2Duration_NonConsolidatedMember_ResultMember'
    """ 前年度期初から第２四半期間個別又は非連結実績 """
    PRIOR_ACCUMULATED_Q3_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ3Duration_NonConsolidatedMember_ResultMember'
    """ 前年度期初から第３四半期間個別又は非連結実績 """


class BasicNetIncomePerShareUS(Enum):
    """"基本的1株当たり当社株主に帰属する当期純利益、米国基準"""
    CURRENT_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間連結実績 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ForecastMember'
    """ 当年度会計期間連結予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_LowerMember'
    """ 当年度会計期間連結下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_UpperMember'
    """ 当年度会計期間連結上限 """
    PRIOR_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第３四半期間連結実績 """


class ChangeInComprehensiveIncomeNetOfTaxIncludingPortionAttributableToNoncontrollingInterest5US(Enum):
    """"当社株主に帰属する包括利益増減率、米国基準"""
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間連結実績 """
    PRIOR_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第２四半期間連結実績 """


class ChangeInComprehensiveIncomeNetOfTaxIncludingPortionAttributableToNoncontrollingInterestUS(Enum):
    """"当期包括利益増減率、米国基準"""
    CURRENT_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間連結実績 """
    PRIOR_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第３四半期間連結実績 """


class ChangeInIncomeBeforeIncomeTaxesUS(Enum):
    """"増減率、税引前当期純利益、米国基準"""
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間連結実績 """
    CURRENT_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間連結実績 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ForecastMember'
    """ 当年度会計期間連結予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_LowerMember'
    """ 当年度会計期間連結下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_UpperMember'
    """ 当年度会計期間連結上限 """
    PRIOR_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第２四半期間連結実績 """
    PRIOR_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第３四半期間連結実績 """


class ChangeInNetIncomeUS(Enum):
    """"増減率、当社株主に帰属する当期純利益、米国基準"""
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間連結実績 """
    CURRENT_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間連結実績 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ForecastMember'
    """ 当年度会計期間連結予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_LowerMember'
    """ 当年度会計期間連結下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_UpperMember'
    """ 当年度会計期間連結上限 """
    PRIOR_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第２四半期間連結実績 """
    PRIOR_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第３四半期間連結実績 """


class ChangeInNetSalesUS(Enum):
    """"増減率、売上高、米国基準"""
    CURRENT_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間連結実績 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ForecastMember'
    """ 当年度会計期間連結予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_LowerMember'
    """ 当年度会計期間連結下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_UpperMember'
    """ 当年度会計期間連結上限 """
    PRIOR_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第３四半期間連結実績 """


class ChangeInOperatingIncomeUS(Enum):
    """"増減率、営業利益、米国基準"""
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間連結実績 """
    CURRENT_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間連結実績 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ForecastMember'
    """ 当年度会計期間連結予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_LowerMember'
    """ 当年度会計期間連結下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_UpperMember'
    """ 当年度会計期間連結上限 """
    PRIOR_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第２四半期間連結実績 """
    PRIOR_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第３四半期間連結実績 """


class ChangeInOperatingRevenuesUS(Enum):
    """"増減率、営業収益、米国基準"""
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間連結実績 """
    PRIOR_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第２四半期間連結実績 """


class ComprehensiveIncomeNetOfTaxIncludingPortionAttributableToNoncontrollingInterest5US(Enum):
    """"当社株主に帰属する包括利益、米国基準"""
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間連結実績 """
    PRIOR_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第２四半期間連結実績 """


class ComprehensiveIncomeNetOfTaxIncludingPortionAttributableToNoncontrollingInterestUS(Enum):
    """"当期包括利益、米国基準"""
    CURRENT_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間連結実績 """
    PRIOR_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第３四半期間連結実績 """


class DilutedNetIncomePerShare2US(Enum):
    """"潜在株式調整後1株当たり当社株主に帰属する当期純利益、米国基準"""
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間連結実績 """
    PRIOR_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第２四半期間連結実績 """


class DilutedNetIncomePerShareUS(Enum):
    """"希薄化後1株当たり当社株主に帰属する当期純利益、米国基準"""
    CURRENT_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間連結実績 """
    PRIOR_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第３四半期間連結実績 """


class DividendPerShare(Enum):
    """"1株当たり配当金"""
    CURRENT_YEAR_DURATION__ANNUAL_MEMBER__NON_CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_AnnualMember_NonConsolidatedMember_ForecastMember'
    """ 当年度会計期間年間個別又は非連結予想 """
    CURRENT_YEAR_DURATION__ANNUAL_MEMBER__NON_CONSOLIDATED_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_AnnualMember_NonConsolidatedMember_LowerMember'
    """ 当年度会計期間年間個別又は非連結下限 """
    CURRENT_YEAR_DURATION__ANNUAL_MEMBER__NON_CONSOLIDATED_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_AnnualMember_NonConsolidatedMember_UpperMember'
    """ 当年度会計期間年間個別又は非連結上限 """
    CURRENT_YEAR_DURATION__FIRST_QUARTER_MEMBER__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_FirstQuarterMember_NonConsolidatedMember_ResultMember'
    """ 当年度会計期間1Q個別又は非連結実績 """
    CURRENT_YEAR_DURATION__SECOND_QUARTER_MEMBER__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_SecondQuarterMember_NonConsolidatedMember_ResultMember'
    """ 当年度会計期間2Q個別又は非連結実績 """
    CURRENT_YEAR_DURATION__THIRD_QUARTER_MEMBER__NON_CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ThirdQuarterMember_NonConsolidatedMember_ForecastMember'
    """ 当年度会計期間3Q個別又は非連結予想 """
    CURRENT_YEAR_DURATION__THIRD_QUARTER_MEMBER__NON_CONSOLIDATED_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ThirdQuarterMember_NonConsolidatedMember_LowerMember'
    """ 当年度会計期間3Q個別又は非連結下限 """
    CURRENT_YEAR_DURATION__THIRD_QUARTER_MEMBER__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_ThirdQuarterMember_NonConsolidatedMember_ResultMember'
    """ 当年度会計期間3Q個別又は非連結実績 """
    CURRENT_YEAR_DURATION__THIRD_QUARTER_MEMBER__NON_CONSOLIDATED_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ThirdQuarterMember_NonConsolidatedMember_UpperMember'
    """ 当年度会計期間3Q個別又は非連結上限 """
    CURRENT_YEAR_DURATION__YEAR_END_MEMBER__NON_CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_YearEndMember_NonConsolidatedMember_ForecastMember'
    """ 当年度会計期間期末個別又は非連結予想 """
    CURRENT_YEAR_DURATION__YEAR_END_MEMBER__NON_CONSOLIDATED_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_YearEndMember_NonConsolidatedMember_LowerMember'
    """ 当年度会計期間期末個別又は非連結下限 """
    CURRENT_YEAR_DURATION__YEAR_END_MEMBER__NON_CONSOLIDATED_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_YearEndMember_NonConsolidatedMember_UpperMember'
    """ 当年度会計期間期末個別又は非連結上限 """
    PRIOR_YEAR_DURATION__ANNUAL_MEMBER__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearDuration_AnnualMember_NonConsolidatedMember_ResultMember'
    """ 前年度会計期間年間個別又は非連結実績 """
    PRIOR_YEAR_DURATION__FIRST_QUARTER_MEMBER__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearDuration_FirstQuarterMember_NonConsolidatedMember_ResultMember'
    """ 前年度会計期間1Q個別又は非連結実績 """
    PRIOR_YEAR_DURATION__SECOND_QUARTER_MEMBER__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearDuration_SecondQuarterMember_NonConsolidatedMember_ResultMember'
    """ 前年度会計期間2Q個別又は非連結実績 """
    PRIOR_YEAR_DURATION__THIRD_QUARTER_MEMBER__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearDuration_ThirdQuarterMember_NonConsolidatedMember_ResultMember'
    """ 前年度会計期間3Q個別又は非連結実績 """
    PRIOR_YEAR_DURATION__YEAR_END_MEMBER__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearDuration_YearEndMember_NonConsolidatedMember_ResultMember'
    """ 前年度会計期間期末個別又は非連結実績 """


class IncomeBeforeIncomeTaxesUS(Enum):
    """"税引前当期純利益、米国基準"""
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間連結実績 """
    CURRENT_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間連結実績 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ForecastMember'
    """ 当年度会計期間連結予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_LowerMember'
    """ 当年度会計期間連結下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_UpperMember'
    """ 当年度会計期間連結上限 """
    PRIOR_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第２四半期間連結実績 """
    PRIOR_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第３四半期間連結実績 """


class NetAssetsUS(Enum):
    """"資本合計（純資産）、米国基準"""
    CURRENT_ACCUMULATED_Q2_INSTANT__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Instant_ConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間時点連結実績 """
    CURRENT_ACCUMULATED_Q3_INSTANT__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Instant_ConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間時点連結実績 """
    PRIOR_YEAR_INSTANT__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearInstant_ConsolidatedMember_ResultMember'
    """ 前年度時点連結実績 """


class NetIncomePerShareUS(Enum):
    """"1株当たり当社株主に帰属する当期純利益、米国基準"""
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間連結実績 """
    PRIOR_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第２四半期間連結実績 """


class NetIncomeUS(Enum):
    """"当社株主に帰属する当期純利益、米国基準"""
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間連結実績 """
    CURRENT_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間連結実績 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ForecastMember'
    """ 当年度会計期間連結予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_LowerMember'
    """ 当年度会計期間連結下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_UpperMember'
    """ 当年度会計期間連結上限 """
    PRIOR_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第２四半期間連結実績 """
    PRIOR_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第３四半期間連結実績 """


class NetSalesUS(Enum):
    """"売上高、米国基準"""
    CURRENT_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間連結実績 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ForecastMember'
    """ 当年度会計期間連結予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_LowerMember'
    """ 当年度会計期間連結下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_UpperMember'
    """ 当年度会計期間連結上限 """
    PRIOR_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第３四半期間連結実績 """


class NumberOfIssuedAndOutstandingSharesAtTheEndOfFiscalYearIncludingTreasuryStock(Enum):
    """"期末発行済株式数（自己株式を含む）"""
    CURRENT_ACCUMULATED_Q2_INSTANT__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Instant_NonConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間時点個別又は非連結実績 """
    CURRENT_ACCUMULATED_Q3_INSTANT__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Instant_NonConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間時点個別又は非連結実績 """
    PRIOR_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearInstant_NonConsolidatedMember_ResultMember'
    """ 前年度時点個別又は非連結実績 """


class NumberOfSubsidiariesExcludedFromConsolidationUS(Enum):
    """"除外、米国基準"""
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間連結実績 """
    CURRENT_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間連結実績 """


class NumberOfSubsidiariesNewlyConsolidatedUS(Enum):
    """"新規、米国基準"""
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間連結実績 """
    CURRENT_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間連結実績 """


class NumberOfTreasuryStockAtTheEndOfFiscalYear(Enum):
    """"期末自己株式数"""
    CURRENT_ACCUMULATED_Q2_INSTANT__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Instant_NonConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間時点個別又は非連結実績 """
    CURRENT_ACCUMULATED_Q3_INSTANT__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Instant_NonConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間時点個別又は非連結実績 """
    PRIOR_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearInstant_NonConsolidatedMember_ResultMember'
    """ 前年度時点個別又は非連結実績 """


class OperatingIncomeUS(Enum):
    """"営業利益、米国基準"""
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間連結実績 """
    CURRENT_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間連結実績 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ForecastMember'
    """ 当年度会計期間連結予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_LowerMember'
    """ 当年度会計期間連結下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_UpperMember'
    """ 当年度会計期間連結上限 """
    PRIOR_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第２四半期間連結実績 """
    PRIOR_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第３四半期間連結実績 """


class OperatingRevenuesUS(Enum):
    """"営業収益、米国基準"""
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間連結実績 """
    PRIOR_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第２四半期間連結実績 """


class QuarterlyPeriod(Enum):
    """"四半期"""
    CURRENT_ACCUMULATED_Q2_INSTANT = 'CurrentAccumulatedQ2Instant'
    """ 当年度期初から第２四半期間時点 """
    CURRENT_ACCUMULATED_Q3_INSTANT = 'CurrentAccumulatedQ3Instant'
    """ 当年度期初から第３四半期間時点 """


class ShareholdersEquityRatioUS(Enum):
    """"株主資本比率、米国基準"""
    CURRENT_ACCUMULATED_Q2_INSTANT__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Instant_ConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間時点連結実績 """
    CURRENT_ACCUMULATED_Q3_INSTANT__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Instant_ConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間時点連結実績 """
    PRIOR_YEAR_INSTANT__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearInstant_ConsolidatedMember_ResultMember'
    """ 前年度時点連結実績 """


class ShareholdersEquityUS(Enum):
    """"株主資本、米国基準"""
    CURRENT_ACCUMULATED_Q2_INSTANT__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Instant_ConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間時点連結実績 """
    CURRENT_ACCUMULATED_Q3_INSTANT__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Instant_ConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間時点連結実績 """
    PRIOR_YEAR_INSTANT__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearInstant_ConsolidatedMember_ResultMember'
    """ 前年度時点連結実績 """


class TotalAssetsUS(Enum):
    """"総資産、米国基準"""
    CURRENT_ACCUMULATED_Q2_INSTANT__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Instant_ConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間時点連結実績 """
    CURRENT_ACCUMULATED_Q3_INSTANT__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Instant_ConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間時点連結実績 """
    PRIOR_YEAR_INSTANT__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearInstant_ConsolidatedMember_ResultMember'
    """ 前年度時点連結実績 """


