from enum import Enum

class AverageNumberOfShares(Enum):
    """"期中平均株式数"""
    CURRENT_ACCUMULATED_Q1_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ1Duration_NonConsolidatedMember_ResultMember'
    """ 当年度期初から第１四半期間個別又は非連結実績 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間個別又は非連結実績 """
    CURRENT_ACCUMULATED_Q3_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Duration_NonConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間個別又は非連結実績 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_ResultMember'
    """ 当年度会計期間個別又は非連結実績 """
    PRIOR_ACCUMULATED_Q1_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ1Duration_NonConsolidatedMember_ResultMember'
    """ 前年度期初から第１四半期間個別又は非連結実績 """
    PRIOR_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ2Duration_NonConsolidatedMember_ResultMember'
    """ 前年度期初から第２四半期間個別又は非連結実績 """
    PRIOR_ACCUMULATED_Q3_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ3Duration_NonConsolidatedMember_ResultMember'
    """ 前年度期初から第３四半期間個別又は非連結実績 """
    PRIOR_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearDuration_NonConsolidatedMember_ResultMember'
    """ 前年度会計期間個別又は非連結実績 """


class BasicEarningsPerShareIFRS(Enum):
    """"基本的1株当たり当期利益、IFRS"""
    CURRENT_ACCUMULATED_Q1_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ1Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第１四半期間連結実績 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間連結実績 """
    CURRENT_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間連結実績 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ForecastMember'
    """ 当年度会計期間連結予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_LowerMember'
    """ 当年度会計期間連結下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ResultMember'
    """ 当年度会計期間連結実績 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_UpperMember'
    """ 当年度会計期間連結上限 """
    NEXT_YEAR_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'NextYearDuration_ConsolidatedMember_ForecastMember'
    """ 次年度会計期間連結予想 """
    NEXT_YEAR_DURATION__CONSOLIDATED_MEMBER__LOWER_MEMBER = 'NextYearDuration_ConsolidatedMember_LowerMember'
    """ 次年度会計期間連結下限 """
    NEXT_YEAR_DURATION__CONSOLIDATED_MEMBER__UPPER_MEMBER = 'NextYearDuration_ConsolidatedMember_UpperMember'
    """ 次年度会計期間連結上限 """
    PRIOR_ACCUMULATED_Q1_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ1Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第１四半期間連結実績 """
    PRIOR_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第２四半期間連結実績 """
    PRIOR_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第３四半期間連結実績 """
    PRIOR_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearDuration_ConsolidatedMember_ResultMember'
    """ 前年度会計期間連結実績 """


class CashAndCashEquivalentsAtEndOfPeriodIFRS(Enum):
    """"現金及び現金同等物期末残高、IFRS"""
    CURRENT_YEAR_INSTANT__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearInstant_ConsolidatedMember_ResultMember'
    """ 当年度時点連結実績 """
    PRIOR_YEAR_INSTANT__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearInstant_ConsolidatedMember_ResultMember'
    """ 前年度時点連結実績 """


class CashFlowsFromFinancingActivitiesIFRS(Enum):
    """"財務活動によるキャッシュ・フロー、IFRS"""
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ResultMember'
    """ 当年度会計期間連結実績 """
    PRIOR_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearDuration_ConsolidatedMember_ResultMember'
    """ 前年度会計期間連結実績 """


class CashFlowsFromInvestingActivitiesIFRS(Enum):
    """"投資活動によるキャッシュ・フロー、IFRS"""
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ResultMember'
    """ 当年度会計期間連結実績 """
    PRIOR_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearDuration_ConsolidatedMember_ResultMember'
    """ 前年度会計期間連結実績 """


class CashFlowsFromOperatingActivitiesIFRS(Enum):
    """"営業活動によるキャッシュ・フロー、IFRS"""
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ResultMember'
    """ 当年度会計期間連結実績 """
    PRIOR_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearDuration_ConsolidatedMember_ResultMember'
    """ 前年度会計期間連結実績 """


class ChangeInNetSalesIFRS(Enum):
    """"増減率、売上高、IFRS"""
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


class ChangeInOperatingIncomeIFRS(Enum):
    """"増減率、営業利益、IFRS"""
    CURRENT_ACCUMULATED_Q1_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ1Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第１四半期間連結実績 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間連結実績 """
    CURRENT_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間連結実績 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ForecastMember'
    """ 当年度会計期間連結予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_LowerMember'
    """ 当年度会計期間連結下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ResultMember'
    """ 当年度会計期間連結実績 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_UpperMember'
    """ 当年度会計期間連結上限 """
    NEXT_YEAR_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'NextYearDuration_ConsolidatedMember_ForecastMember'
    """ 次年度会計期間連結予想 """
    NEXT_YEAR_DURATION__CONSOLIDATED_MEMBER__LOWER_MEMBER = 'NextYearDuration_ConsolidatedMember_LowerMember'
    """ 次年度会計期間連結下限 """
    NEXT_YEAR_DURATION__CONSOLIDATED_MEMBER__UPPER_MEMBER = 'NextYearDuration_ConsolidatedMember_UpperMember'
    """ 次年度会計期間連結上限 """
    PRIOR_ACCUMULATED_Q1_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ1Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第１四半期間連結実績 """
    PRIOR_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第２四半期間連結実績 """
    PRIOR_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第３四半期間連結実績 """
    PRIOR_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearDuration_ConsolidatedMember_ResultMember'
    """ 前年度会計期間連結実績 """


class ChangeInProfitAttributableToOwnersOfParentIFRS(Enum):
    """"増減率、親会社の所有者に帰属する当期利益、IFRS"""
    CURRENT_ACCUMULATED_Q1_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ1Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第１四半期間連結実績 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間連結実績 """
    CURRENT_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間連結実績 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ForecastMember'
    """ 当年度会計期間連結予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_LowerMember'
    """ 当年度会計期間連結下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ResultMember'
    """ 当年度会計期間連結実績 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_UpperMember'
    """ 当年度会計期間連結上限 """
    NEXT_YEAR_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'NextYearDuration_ConsolidatedMember_ForecastMember'
    """ 次年度会計期間連結予想 """
    NEXT_YEAR_DURATION__CONSOLIDATED_MEMBER__LOWER_MEMBER = 'NextYearDuration_ConsolidatedMember_LowerMember'
    """ 次年度会計期間連結下限 """
    NEXT_YEAR_DURATION__CONSOLIDATED_MEMBER__UPPER_MEMBER = 'NextYearDuration_ConsolidatedMember_UpperMember'
    """ 次年度会計期間連結上限 """
    PRIOR_ACCUMULATED_Q1_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ1Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第１四半期間連結実績 """
    PRIOR_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第２四半期間連結実績 """
    PRIOR_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第３四半期間連結実績 """
    PRIOR_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearDuration_ConsolidatedMember_ResultMember'
    """ 前年度会計期間連結実績 """


class ChangeInProfitBeforeTaxIFRS(Enum):
    """"増減率、税引前利益、IFRS"""
    CURRENT_ACCUMULATED_Q1_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ1Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第１四半期間連結実績 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間連結実績 """
    CURRENT_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間連結実績 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ForecastMember'
    """ 当年度会計期間連結予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_LowerMember'
    """ 当年度会計期間連結下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ResultMember'
    """ 当年度会計期間連結実績 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_UpperMember'
    """ 当年度会計期間連結上限 """
    PRIOR_ACCUMULATED_Q1_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ1Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第１四半期間連結実績 """
    PRIOR_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第２四半期間連結実績 """
    PRIOR_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第３四半期間連結実績 """
    PRIOR_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearDuration_ConsolidatedMember_ResultMember'
    """ 前年度会計期間連結実績 """


class ChangeInProfitIFRS(Enum):
    """"増減率、当期利益、IFRS"""
    CURRENT_ACCUMULATED_Q1_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ1Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第１四半期間連結実績 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間連結実績 """
    CURRENT_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間連結実績 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ForecastMember'
    """ 当年度会計期間連結予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_LowerMember'
    """ 当年度会計期間連結下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ResultMember'
    """ 当年度会計期間連結実績 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_UpperMember'
    """ 当年度会計期間連結上限 """
    PRIOR_ACCUMULATED_Q1_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ1Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第１四半期間連結実績 """
    PRIOR_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第２四半期間連結実績 """
    PRIOR_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第３四半期間連結実績 """
    PRIOR_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearDuration_ConsolidatedMember_ResultMember'
    """ 前年度会計期間連結実績 """


class ChangeInRevenueIFRS(Enum):
    """"増減率、収益、IFRS"""
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間連結実績 """
    PRIOR_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第２四半期間連結実績 """


class ChangeInSalesIFRS(Enum):
    """"増減率、売上収益、IFRS"""
    CURRENT_ACCUMULATED_Q1_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ1Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第１四半期間連結実績 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間連結実績 """
    CURRENT_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間連結実績 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ForecastMember'
    """ 当年度会計期間連結予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_LowerMember'
    """ 当年度会計期間連結下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ResultMember'
    """ 当年度会計期間連結実績 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_UpperMember'
    """ 当年度会計期間連結上限 """
    NEXT_YEAR_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'NextYearDuration_ConsolidatedMember_ForecastMember'
    """ 次年度会計期間連結予想 """
    NEXT_YEAR_DURATION__CONSOLIDATED_MEMBER__LOWER_MEMBER = 'NextYearDuration_ConsolidatedMember_LowerMember'
    """ 次年度会計期間連結下限 """
    NEXT_YEAR_DURATION__CONSOLIDATED_MEMBER__UPPER_MEMBER = 'NextYearDuration_ConsolidatedMember_UpperMember'
    """ 次年度会計期間連結上限 """
    PRIOR_ACCUMULATED_Q1_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ1Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第１四半期間連結実績 """
    PRIOR_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第２四半期間連結実績 """
    PRIOR_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第３四半期間連結実績 """
    PRIOR_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearDuration_ConsolidatedMember_ResultMember'
    """ 前年度会計期間連結実績 """


class ChangesInTotalComprehensiveIncomeIFRS(Enum):
    """"当期包括利益合計額増減率、IFRS"""
    CURRENT_ACCUMULATED_Q1_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ1Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第１四半期間連結実績 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間連結実績 """
    CURRENT_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間連結実績 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ResultMember'
    """ 当年度会計期間連結実績 """
    PRIOR_ACCUMULATED_Q1_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ1Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第１四半期間連結実績 """
    PRIOR_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第２四半期間連結実績 """
    PRIOR_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第３四半期間連結実績 """
    PRIOR_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearDuration_ConsolidatedMember_ResultMember'
    """ 前年度会計期間連結実績 """


class DilutedEarningsPerShareIFRS(Enum):
    """"希薄化後1株当たり当期利益、IFRS"""
    CURRENT_ACCUMULATED_Q1_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ1Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第１四半期間連結実績 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間連結実績 """
    CURRENT_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間連結実績 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ResultMember'
    """ 当年度会計期間連結実績 """
    PRIOR_ACCUMULATED_Q1_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ1Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第１四半期間連結実績 """
    PRIOR_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第２四半期間連結実績 """
    PRIOR_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第３四半期間連結実績 """
    PRIOR_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearDuration_ConsolidatedMember_ResultMember'
    """ 前年度会計期間連結実績 """


class DividendPerShare(Enum):
    """"1株当たり配当金"""
    CURRENT_YEAR_DURATION__ANNUAL_MEMBER__NON_CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_AnnualMember_NonConsolidatedMember_ForecastMember'
    """ 当年度会計期間年間個別又は非連結予想 """
    CURRENT_YEAR_DURATION__ANNUAL_MEMBER__NON_CONSOLIDATED_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_AnnualMember_NonConsolidatedMember_LowerMember'
    """ 当年度会計期間年間個別又は非連結下限 """
    CURRENT_YEAR_DURATION__ANNUAL_MEMBER__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_AnnualMember_NonConsolidatedMember_ResultMember'
    """ 当年度会計期間年間個別又は非連結実績 """
    CURRENT_YEAR_DURATION__ANNUAL_MEMBER__NON_CONSOLIDATED_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_AnnualMember_NonConsolidatedMember_UpperMember'
    """ 当年度会計期間年間個別又は非連結上限 """
    CURRENT_YEAR_DURATION__FIRST_QUARTER_MEMBER__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_FirstQuarterMember_NonConsolidatedMember_ResultMember'
    """ 当年度会計期間1Q個別又は非連結実績 """
    CURRENT_YEAR_DURATION__SECOND_QUARTER_MEMBER__NON_CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_SecondQuarterMember_NonConsolidatedMember_ForecastMember'
    """ 当年度会計期間2Q個別又は非連結予想 """
    CURRENT_YEAR_DURATION__SECOND_QUARTER_MEMBER__NON_CONSOLIDATED_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_SecondQuarterMember_NonConsolidatedMember_LowerMember'
    """ 当年度会計期間2Q個別又は非連結下限 """
    CURRENT_YEAR_DURATION__SECOND_QUARTER_MEMBER__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_SecondQuarterMember_NonConsolidatedMember_ResultMember'
    """ 当年度会計期間2Q個別又は非連結実績 """
    CURRENT_YEAR_DURATION__SECOND_QUARTER_MEMBER__NON_CONSOLIDATED_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_SecondQuarterMember_NonConsolidatedMember_UpperMember'
    """ 当年度会計期間2Q個別又は非連結上限 """
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
    CURRENT_YEAR_DURATION__YEAR_END_MEMBER__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_YearEndMember_NonConsolidatedMember_ResultMember'
    """ 当年度会計期間期末個別又は非連結実績 """
    CURRENT_YEAR_DURATION__YEAR_END_MEMBER__NON_CONSOLIDATED_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_YearEndMember_NonConsolidatedMember_UpperMember'
    """ 当年度会計期間期末個別又は非連結上限 """
    NEXT_YEAR_DURATION__ANNUAL_MEMBER__NON_CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'NextYearDuration_AnnualMember_NonConsolidatedMember_ForecastMember'
    """ 次年度会計期間年間個別又は非連結予想 """
    NEXT_YEAR_DURATION__ANNUAL_MEMBER__NON_CONSOLIDATED_MEMBER__LOWER_MEMBER = 'NextYearDuration_AnnualMember_NonConsolidatedMember_LowerMember'
    """ 次年度会計期間年間個別又は非連結下限 """
    NEXT_YEAR_DURATION__ANNUAL_MEMBER__NON_CONSOLIDATED_MEMBER__UPPER_MEMBER = 'NextYearDuration_AnnualMember_NonConsolidatedMember_UpperMember'
    """ 次年度会計期間年間個別又は非連結上限 """
    NEXT_YEAR_DURATION__FIRST_QUARTER_MEMBER__NON_CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'NextYearDuration_FirstQuarterMember_NonConsolidatedMember_ForecastMember'
    """ 次年度会計期間1Q個別又は非連結予想 """
    NEXT_YEAR_DURATION__FIRST_QUARTER_MEMBER__NON_CONSOLIDATED_MEMBER__LOWER_MEMBER = 'NextYearDuration_FirstQuarterMember_NonConsolidatedMember_LowerMember'
    """ 次年度会計期間1Q個別又は非連結下限 """
    NEXT_YEAR_DURATION__FIRST_QUARTER_MEMBER__NON_CONSOLIDATED_MEMBER__UPPER_MEMBER = 'NextYearDuration_FirstQuarterMember_NonConsolidatedMember_UpperMember'
    """ 次年度会計期間1Q個別又は非連結上限 """
    NEXT_YEAR_DURATION__SECOND_QUARTER_MEMBER__NON_CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'NextYearDuration_SecondQuarterMember_NonConsolidatedMember_ForecastMember'
    """ 次年度会計期間2Q個別又は非連結予想 """
    NEXT_YEAR_DURATION__SECOND_QUARTER_MEMBER__NON_CONSOLIDATED_MEMBER__LOWER_MEMBER = 'NextYearDuration_SecondQuarterMember_NonConsolidatedMember_LowerMember'
    """ 次年度会計期間2Q個別又は非連結下限 """
    NEXT_YEAR_DURATION__SECOND_QUARTER_MEMBER__NON_CONSOLIDATED_MEMBER__UPPER_MEMBER = 'NextYearDuration_SecondQuarterMember_NonConsolidatedMember_UpperMember'
    """ 次年度会計期間2Q個別又は非連結上限 """
    NEXT_YEAR_DURATION__THIRD_QUARTER_MEMBER__NON_CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'NextYearDuration_ThirdQuarterMember_NonConsolidatedMember_ForecastMember'
    """ 次年度会計期間3Q個別又は非連結予想 """
    NEXT_YEAR_DURATION__THIRD_QUARTER_MEMBER__NON_CONSOLIDATED_MEMBER__LOWER_MEMBER = 'NextYearDuration_ThirdQuarterMember_NonConsolidatedMember_LowerMember'
    """ 次年度会計期間3Q個別又は非連結下限 """
    NEXT_YEAR_DURATION__THIRD_QUARTER_MEMBER__NON_CONSOLIDATED_MEMBER__UPPER_MEMBER = 'NextYearDuration_ThirdQuarterMember_NonConsolidatedMember_UpperMember'
    """ 次年度会計期間3Q個別又は非連結上限 """
    NEXT_YEAR_DURATION__YEAR_END_MEMBER__NON_CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'NextYearDuration_YearEndMember_NonConsolidatedMember_ForecastMember'
    """ 次年度会計期間期末個別又は非連結予想 """
    NEXT_YEAR_DURATION__YEAR_END_MEMBER__NON_CONSOLIDATED_MEMBER__LOWER_MEMBER = 'NextYearDuration_YearEndMember_NonConsolidatedMember_LowerMember'
    """ 次年度会計期間期末個別又は非連結下限 """
    NEXT_YEAR_DURATION__YEAR_END_MEMBER__NON_CONSOLIDATED_MEMBER__UPPER_MEMBER = 'NextYearDuration_YearEndMember_NonConsolidatedMember_UpperMember'
    """ 次年度会計期間期末個別又は非連結上限 """
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


class EquityAttributableToOwnersOfParentIFRS(Enum):
    """"親会社の所有者に帰属する持分、IFRS"""
    CURRENT_ACCUMULATED_Q1_INSTANT__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ1Instant_ConsolidatedMember_ResultMember'
    """ 当年度期初から第１四半期間時点連結実績 """
    CURRENT_ACCUMULATED_Q2_INSTANT__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Instant_ConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間時点連結実績 """
    CURRENT_ACCUMULATED_Q3_INSTANT__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Instant_ConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間時点連結実績 """
    CURRENT_YEAR_INSTANT__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearInstant_ConsolidatedMember_ResultMember'
    """ 当年度時点連結実績 """
    PRIOR_YEAR_INSTANT__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearInstant_ConsolidatedMember_ResultMember'
    """ 前年度時点連結実績 """


class EquityAttributableToOwnersOfParentPerShareIFRS(Enum):
    """"1株当たり親会社所有者帰属持分、IFRS"""
    CURRENT_ACCUMULATED_Q2_INSTANT__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Instant_ConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間時点連結実績 """
    CURRENT_ACCUMULATED_Q3_INSTANT__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Instant_ConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間時点連結実績 """
    CURRENT_YEAR_INSTANT__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearInstant_ConsolidatedMember_ResultMember'
    """ 当年度時点連結実績 """
    PRIOR_YEAR_INSTANT__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearInstant_ConsolidatedMember_ResultMember'
    """ 前年度時点連結実績 """


class EquityAttributableToOwnersOfParentToTotalAssetsRatioIFRS(Enum):
    """"親会社所有者帰属持分比率、IFRS"""
    CURRENT_ACCUMULATED_Q1_INSTANT__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ1Instant_ConsolidatedMember_ResultMember'
    """ 当年度期初から第１四半期間時点連結実績 """
    CURRENT_ACCUMULATED_Q2_INSTANT__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Instant_ConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間時点連結実績 """
    CURRENT_ACCUMULATED_Q3_INSTANT__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Instant_ConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間時点連結実績 """
    CURRENT_YEAR_INSTANT__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearInstant_ConsolidatedMember_ResultMember'
    """ 当年度時点連結実績 """
    PRIOR_YEAR_INSTANT__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearInstant_ConsolidatedMember_ResultMember'
    """ 前年度時点連結実績 """


class InvestmentsAccountedForUsingEquityMethodIFRS(Enum):
    """"持分法による投資損益、IFRS"""
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ResultMember'
    """ 当年度会計期間連結実績 """
    PRIOR_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearDuration_ConsolidatedMember_ResultMember'
    """ 前年度会計期間連結実績 """


class NetSalesIFRS(Enum):
    """"売上高、IFRS"""
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


class NumberOfIssuedAndOutstandingSharesAtTheEndOfFiscalYearIncludingTreasuryStock(Enum):
    """"期末発行済株式数（自己株式を含む）"""
    CURRENT_ACCUMULATED_Q1_INSTANT__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ1Instant_NonConsolidatedMember_ResultMember'
    """ 当年度期初から第１四半期間時点個別又は非連結実績 """
    CURRENT_ACCUMULATED_Q2_INSTANT__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Instant_NonConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間時点個別又は非連結実績 """
    CURRENT_ACCUMULATED_Q3_INSTANT__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Instant_NonConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間時点個別又は非連結実績 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearInstant_NonConsolidatedMember_ResultMember'
    """ 当年度時点個別又は非連結実績 """
    PRIOR_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearInstant_NonConsolidatedMember_ResultMember'
    """ 前年度時点個別又は非連結実績 """


class NumberOfSubsidiariesExcludedFromConsolidationIFRS(Enum):
    """"除外、IFRS"""
    CURRENT_ACCUMULATED_Q1_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ1Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第１四半期間連結実績 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間連結実績 """
    CURRENT_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間連結実績 """


class NumberOfSubsidiariesNewlyConsolidatedIFRS(Enum):
    """"新規、IFRS"""
    CURRENT_ACCUMULATED_Q1_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ1Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第１四半期間連結実績 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間連結実績 """
    CURRENT_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間連結実績 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ResultMember'
    """ 当年度会計期間連結実績 """


class NumberOfTreasuryStockAtTheEndOfFiscalYear(Enum):
    """"期末自己株式数"""
    CURRENT_ACCUMULATED_Q1_INSTANT__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ1Instant_NonConsolidatedMember_ResultMember'
    """ 当年度期初から第１四半期間時点個別又は非連結実績 """
    CURRENT_ACCUMULATED_Q2_INSTANT__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Instant_NonConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間時点個別又は非連結実績 """
    CURRENT_ACCUMULATED_Q3_INSTANT__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Instant_NonConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間時点個別又は非連結実績 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearInstant_NonConsolidatedMember_ResultMember'
    """ 当年度時点個別又は非連結実績 """
    PRIOR_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearInstant_NonConsolidatedMember_ResultMember'
    """ 前年度時点個別又は非連結実績 """


class OperatingIncomeIFRS(Enum):
    """"営業利益、IFRS"""
    CURRENT_ACCUMULATED_Q1_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ1Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第１四半期間連結実績 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間連結実績 """
    CURRENT_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間連結実績 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ForecastMember'
    """ 当年度会計期間連結予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_LowerMember'
    """ 当年度会計期間連結下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ResultMember'
    """ 当年度会計期間連結実績 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_UpperMember'
    """ 当年度会計期間連結上限 """
    NEXT_YEAR_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'NextYearDuration_ConsolidatedMember_ForecastMember'
    """ 次年度会計期間連結予想 """
    NEXT_YEAR_DURATION__CONSOLIDATED_MEMBER__LOWER_MEMBER = 'NextYearDuration_ConsolidatedMember_LowerMember'
    """ 次年度会計期間連結下限 """
    NEXT_YEAR_DURATION__CONSOLIDATED_MEMBER__UPPER_MEMBER = 'NextYearDuration_ConsolidatedMember_UpperMember'
    """ 次年度会計期間連結上限 """
    PRIOR_ACCUMULATED_Q1_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ1Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第１四半期間連結実績 """
    PRIOR_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第２四半期間連結実績 """
    PRIOR_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第３四半期間連結実績 """
    PRIOR_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearDuration_ConsolidatedMember_ResultMember'
    """ 前年度会計期間連結実績 """


class OperatingIncomeToSalesRatioIFRS(Enum):
    """"売上収益営業利益率、IFRS"""
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ResultMember'
    """ 当年度会計期間連結実績 """
    PRIOR_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearDuration_ConsolidatedMember_ResultMember'
    """ 前年度会計期間連結実績 """


class PayoutRatioIFRS(Enum):
    """"配当性向、IFRS"""
    CURRENT_YEAR_DURATION__ANNUAL_MEMBER__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_AnnualMember_ConsolidatedMember_ResultMember'
    """ 当年度会計期間年間連結実績 """
    NEXT_YEAR_DURATION__ANNUAL_MEMBER__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'NextYearDuration_AnnualMember_ConsolidatedMember_ForecastMember'
    """ 次年度会計期間年間連結予想 """
    PRIOR_YEAR_DURATION__ANNUAL_MEMBER__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearDuration_AnnualMember_ConsolidatedMember_ResultMember'
    """ 前年度会計期間年間連結実績 """


class ProfitAttributableToOwnersOfParentIFRS(Enum):
    """"親会社の所有者に帰属する当期利益、IFRS"""
    CURRENT_ACCUMULATED_Q1_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ1Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第１四半期間連結実績 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間連結実績 """
    CURRENT_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間連結実績 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ForecastMember'
    """ 当年度会計期間連結予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_LowerMember'
    """ 当年度会計期間連結下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ResultMember'
    """ 当年度会計期間連結実績 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_UpperMember'
    """ 当年度会計期間連結上限 """
    NEXT_YEAR_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'NextYearDuration_ConsolidatedMember_ForecastMember'
    """ 次年度会計期間連結予想 """
    NEXT_YEAR_DURATION__CONSOLIDATED_MEMBER__LOWER_MEMBER = 'NextYearDuration_ConsolidatedMember_LowerMember'
    """ 次年度会計期間連結下限 """
    NEXT_YEAR_DURATION__CONSOLIDATED_MEMBER__UPPER_MEMBER = 'NextYearDuration_ConsolidatedMember_UpperMember'
    """ 次年度会計期間連結上限 """
    PRIOR_ACCUMULATED_Q1_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ1Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第１四半期間連結実績 """
    PRIOR_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第２四半期間連結実績 """
    PRIOR_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第３四半期間連結実績 """
    PRIOR_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearDuration_ConsolidatedMember_ResultMember'
    """ 前年度会計期間連結実績 """


class ProfitBeforeTaxIFRS(Enum):
    """"税引前利益、IFRS"""
    CURRENT_ACCUMULATED_Q1_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ1Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第１四半期間連結実績 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間連結実績 """
    CURRENT_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間連結実績 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ForecastMember'
    """ 当年度会計期間連結予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_LowerMember'
    """ 当年度会計期間連結下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ResultMember'
    """ 当年度会計期間連結実績 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_UpperMember'
    """ 当年度会計期間連結上限 """
    PRIOR_ACCUMULATED_Q1_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ1Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第１四半期間連結実績 """
    PRIOR_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第２四半期間連結実績 """
    PRIOR_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第３四半期間連結実績 """
    PRIOR_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearDuration_ConsolidatedMember_ResultMember'
    """ 前年度会計期間連結実績 """


class ProfitBeforeTaxToTotalAssetsRatioIFRS(Enum):
    """"資産合計税引前利益率、IFRS"""
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ResultMember'
    """ 当年度会計期間連結実績 """
    PRIOR_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearDuration_ConsolidatedMember_ResultMember'
    """ 前年度会計期間連結実績 """


class ProfitIFRS(Enum):
    """"当期利益、IFRS"""
    CURRENT_ACCUMULATED_Q1_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ1Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第１四半期間連結実績 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間連結実績 """
    CURRENT_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間連結実績 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ForecastMember'
    """ 当年度会計期間連結予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_LowerMember'
    """ 当年度会計期間連結下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ResultMember'
    """ 当年度会計期間連結実績 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_UpperMember'
    """ 当年度会計期間連結上限 """
    PRIOR_ACCUMULATED_Q1_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ1Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第１四半期間連結実績 """
    PRIOR_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第２四半期間連結実績 """
    PRIOR_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第３四半期間連結実績 """
    PRIOR_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearDuration_ConsolidatedMember_ResultMember'
    """ 前年度会計期間連結実績 """


class ProfitToEquityAttributableToOwnersOfParentRatioIFRS(Enum):
    """"親会社所有者帰属持分当期利益率、IFRS"""
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ResultMember'
    """ 当年度会計期間連結実績 """
    PRIOR_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearDuration_ConsolidatedMember_ResultMember'
    """ 前年度会計期間連結実績 """


class QuarterlyPeriod(Enum):
    """"四半期"""
    CURRENT_ACCUMULATED_Q1_INSTANT = 'CurrentAccumulatedQ1Instant'
    """ 当年度期初から第１四半期間時点 """
    CURRENT_ACCUMULATED_Q2_INSTANT = 'CurrentAccumulatedQ2Instant'
    """ 当年度期初から第２四半期間時点 """
    CURRENT_ACCUMULATED_Q3_INSTANT = 'CurrentAccumulatedQ3Instant'
    """ 当年度期初から第３四半期間時点 """


class RatioOfTotalAmountOfDividendsToEquityAttributableToOwnerOfParentConsolidatedIFRS(Enum):
    """"親会社所有者帰属持分配当率（連結）、IFRS"""
    CURRENT_YEAR_DURATION__ANNUAL_MEMBER__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_AnnualMember_ConsolidatedMember_ResultMember'
    """ 当年度会計期間年間連結実績 """
    PRIOR_YEAR_DURATION__ANNUAL_MEMBER__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearDuration_AnnualMember_ConsolidatedMember_ResultMember'
    """ 前年度会計期間年間連結実績 """


class RevenueIFRS(Enum):
    """"収益、IFRS"""
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間連結実績 """
    PRIOR_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第２四半期間連結実績 """


class SalesIFRS(Enum):
    """"売上収益、IFRS"""
    CURRENT_ACCUMULATED_Q1_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ1Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第１四半期間連結実績 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間連結実績 """
    CURRENT_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間連結実績 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ForecastMember'
    """ 当年度会計期間連結予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_LowerMember'
    """ 当年度会計期間連結下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ResultMember'
    """ 当年度会計期間連結実績 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_UpperMember'
    """ 当年度会計期間連結上限 """
    NEXT_YEAR_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'NextYearDuration_ConsolidatedMember_ForecastMember'
    """ 次年度会計期間連結予想 """
    NEXT_YEAR_DURATION__CONSOLIDATED_MEMBER__LOWER_MEMBER = 'NextYearDuration_ConsolidatedMember_LowerMember'
    """ 次年度会計期間連結下限 """
    NEXT_YEAR_DURATION__CONSOLIDATED_MEMBER__UPPER_MEMBER = 'NextYearDuration_ConsolidatedMember_UpperMember'
    """ 次年度会計期間連結上限 """
    PRIOR_ACCUMULATED_Q1_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ1Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第１四半期間連結実績 """
    PRIOR_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第２四半期間連結実績 """
    PRIOR_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第３四半期間連結実績 """
    PRIOR_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearDuration_ConsolidatedMember_ResultMember'
    """ 前年度会計期間連結実績 """


class TotalAssetsIFRS(Enum):
    """"資産合計、IFRS"""
    CURRENT_ACCUMULATED_Q1_INSTANT__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ1Instant_ConsolidatedMember_ResultMember'
    """ 当年度期初から第１四半期間時点連結実績 """
    CURRENT_ACCUMULATED_Q2_INSTANT__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Instant_ConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間時点連結実績 """
    CURRENT_ACCUMULATED_Q3_INSTANT__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Instant_ConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間時点連結実績 """
    CURRENT_YEAR_INSTANT__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearInstant_ConsolidatedMember_ResultMember'
    """ 当年度時点連結実績 """
    PRIOR_YEAR_INSTANT__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearInstant_ConsolidatedMember_ResultMember'
    """ 前年度時点連結実績 """


class TotalComprehensiveIncomeIFRS(Enum):
    """"当期包括利益合計額、IFRS"""
    CURRENT_ACCUMULATED_Q1_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ1Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第１四半期間連結実績 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間連結実績 """
    CURRENT_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間連結実績 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ResultMember'
    """ 当年度会計期間連結実績 """
    PRIOR_ACCUMULATED_Q1_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ1Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第１四半期間連結実績 """
    PRIOR_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第２四半期間連結実績 """
    PRIOR_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第３四半期間連結実績 """
    PRIOR_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearDuration_ConsolidatedMember_ResultMember'
    """ 前年度会計期間連結実績 """


class TotalDividendPaidAnnual(Enum):
    """"配当金総額（合計）"""
    CURRENT_YEAR_DURATION__ANNUAL_MEMBER__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_AnnualMember_NonConsolidatedMember_ResultMember'
    """ 当年度会計期間年間個別又は非連結実績 """
    PRIOR_YEAR_DURATION__ANNUAL_MEMBER__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearDuration_AnnualMember_NonConsolidatedMember_ResultMember'
    """ 前年度会計期間年間個別又は非連結実績 """


class TotalEquityIFRS(Enum):
    """"資本合計、IFRS"""
    CURRENT_ACCUMULATED_Q1_INSTANT__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ1Instant_ConsolidatedMember_ResultMember'
    """ 当年度期初から第１四半期間時点連結実績 """
    CURRENT_ACCUMULATED_Q2_INSTANT__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Instant_ConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間時点連結実績 """
    CURRENT_ACCUMULATED_Q3_INSTANT__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Instant_ConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間時点連結実績 """
    CURRENT_YEAR_INSTANT__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearInstant_ConsolidatedMember_ResultMember'
    """ 当年度時点連結実績 """
    PRIOR_YEAR_INSTANT__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearInstant_ConsolidatedMember_ResultMember'
    """ 前年度時点連結実績 """


