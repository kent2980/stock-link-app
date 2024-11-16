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


class CapitalAdequacyRatio(Enum):
    """"自己資本比率"""
    CURRENT_ACCUMULATED_Q1_INSTANT__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ1Instant_ConsolidatedMember_ResultMember'
    """ 当年度期初から第１四半期間時点連結実績 """
    CURRENT_ACCUMULATED_Q1_INSTANT__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ1Instant_NonConsolidatedMember_ResultMember'
    """ 当年度期初から第１四半期間時点個別又は非連結実績 """
    CURRENT_ACCUMULATED_Q2_INSTANT__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Instant_ConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間時点連結実績 """
    CURRENT_ACCUMULATED_Q2_INSTANT__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Instant_NonConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間時点個別又は非連結実績 """
    CURRENT_ACCUMULATED_Q3_INSTANT__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Instant_ConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間時点連結実績 """
    CURRENT_ACCUMULATED_Q3_INSTANT__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Instant_NonConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間時点個別又は非連結実績 """
    CURRENT_YEAR_INSTANT__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearInstant_ConsolidatedMember_ResultMember'
    """ 当年度時点連結実績 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearInstant_NonConsolidatedMember_ResultMember'
    """ 当年度時点個別又は非連結実績 """
    PRIOR_YEAR_INSTANT__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearInstant_ConsolidatedMember_ResultMember'
    """ 前年度時点連結実績 """
    PRIOR_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearInstant_NonConsolidatedMember_ResultMember'
    """ 前年度時点個別又は非連結実績 """


class CashAndEquivalentsEndOfPeriod(Enum):
    """"現金及び現金同等物期末残高"""
    CURRENT_YEAR_INSTANT__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearInstant_ConsolidatedMember_ResultMember'
    """ 当年度時点連結実績 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearInstant_NonConsolidatedMember_ResultMember'
    """ 当年度時点個別又は非連結実績 """
    PRIOR_YEAR_INSTANT__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearInstant_ConsolidatedMember_ResultMember'
    """ 前年度時点連結実績 """
    PRIOR_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearInstant_NonConsolidatedMember_ResultMember'
    """ 前年度時点個別又は非連結実績 """


class CashFlowsFromFinancingActivities(Enum):
    """"財務活動によるキャッシュ・フロー"""
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ResultMember'
    """ 当年度会計期間連結実績 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_ResultMember'
    """ 当年度会計期間個別又は非連結実績 """
    PRIOR_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearDuration_ConsolidatedMember_ResultMember'
    """ 前年度会計期間連結実績 """
    PRIOR_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearDuration_NonConsolidatedMember_ResultMember'
    """ 前年度会計期間個別又は非連結実績 """


class CashFlowsFromInvestingActivities(Enum):
    """"投資活動によるキャッシュ・フロー"""
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ResultMember'
    """ 当年度会計期間連結実績 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_ResultMember'
    """ 当年度会計期間個別又は非連結実績 """
    PRIOR_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearDuration_ConsolidatedMember_ResultMember'
    """ 前年度会計期間連結実績 """
    PRIOR_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearDuration_NonConsolidatedMember_ResultMember'
    """ 前年度会計期間個別又は非連結実績 """


class CashFlowsFromOperatingActivities(Enum):
    """"営業活動によるキャッシュ・フロー"""
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ResultMember'
    """ 当年度会計期間連結実績 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_ResultMember'
    """ 当年度会計期間個別又は非連結実績 """
    PRIOR_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearDuration_ConsolidatedMember_ResultMember'
    """ 前年度会計期間連結実績 """
    PRIOR_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearDuration_NonConsolidatedMember_ResultMember'
    """ 前年度会計期間個別又は非連結実績 """


class ChangeInComprehensiveIncome(Enum):
    """"包括利益増減率"""
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


class ChangeInNetIncome(Enum):
    """"増減率、当期純利益"""
    CURRENT_ACCUMULATED_Q1_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ1Duration_NonConsolidatedMember_ResultMember'
    """ 当年度期初から第１四半期間個別又は非連結実績 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_ForecastMember'
    """ 当年度期初から第２四半期間連結予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_LowerMember'
    """ 当年度期初から第２四半期間連結下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_UpperMember'
    """ 当年度期初から第２四半期間連結上限 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_ForecastMember'
    """ 当年度期初から第２四半期間個別又は非連結予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_LowerMember'
    """ 当年度期初から第２四半期間個別又は非連結下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間個別又は非連結実績 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_UpperMember'
    """ 当年度期初から第２四半期間個別又は非連結上限 """
    CURRENT_ACCUMULATED_Q3_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Duration_NonConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間個別又は非連結実績 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ForecastMember'
    """ 当年度会計期間連結予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_LowerMember'
    """ 当年度会計期間連結下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_UpperMember'
    """ 当年度会計期間連結上限 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_ForecastMember'
    """ 当年度会計期間個別又は非連結予想 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_LowerMember'
    """ 当年度会計期間個別又は非連結下限 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_ResultMember'
    """ 当年度会計期間個別又は非連結実績 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_UpperMember'
    """ 当年度会計期間個別又は非連結上限 """
    NEXT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'NextAccumulatedQ2Duration_NonConsolidatedMember_ForecastMember'
    """ 次年度期初から第２四半期間個別又は非連結予想 """
    NEXT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__LOWER_MEMBER = 'NextAccumulatedQ2Duration_NonConsolidatedMember_LowerMember'
    """ 次年度期初から第２四半期間個別又は非連結下限 """
    NEXT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__UPPER_MEMBER = 'NextAccumulatedQ2Duration_NonConsolidatedMember_UpperMember'
    """ 次年度期初から第２四半期間個別又は非連結上限 """
    NEXT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'NextYearDuration_NonConsolidatedMember_ForecastMember'
    """ 次年度会計期間個別又は非連結予想 """
    NEXT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__LOWER_MEMBER = 'NextYearDuration_NonConsolidatedMember_LowerMember'
    """ 次年度会計期間個別又は非連結下限 """
    NEXT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__UPPER_MEMBER = 'NextYearDuration_NonConsolidatedMember_UpperMember'
    """ 次年度会計期間個別又は非連結上限 """
    PRIOR_ACCUMULATED_Q1_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ1Duration_NonConsolidatedMember_ResultMember'
    """ 前年度期初から第１四半期間個別又は非連結実績 """
    PRIOR_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ2Duration_NonConsolidatedMember_ResultMember'
    """ 前年度期初から第２四半期間個別又は非連結実績 """
    PRIOR_ACCUMULATED_Q3_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ3Duration_NonConsolidatedMember_ResultMember'
    """ 前年度期初から第３四半期間個別又は非連結実績 """
    PRIOR_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearDuration_NonConsolidatedMember_ResultMember'
    """ 前年度会計期間個別又は非連結実績 """


class ChangeInNetSales(Enum):
    """"増減率、売上高"""
    CURRENT_ACCUMULATED_Q1_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ1Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第１四半期間連結実績 """
    CURRENT_ACCUMULATED_Q1_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ1Duration_NonConsolidatedMember_ResultMember'
    """ 当年度期初から第１四半期間個別又は非連結実績 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_ForecastMember'
    """ 当年度期初から第２四半期間連結予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_LowerMember'
    """ 当年度期初から第２四半期間連結下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間連結実績 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_UpperMember'
    """ 当年度期初から第２四半期間連結上限 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_ForecastMember'
    """ 当年度期初から第２四半期間個別又は非連結予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_LowerMember'
    """ 当年度期初から第２四半期間個別又は非連結下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間個別又は非連結実績 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_UpperMember'
    """ 当年度期初から第２四半期間個別又は非連結上限 """
    CURRENT_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間連結実績 """
    CURRENT_ACCUMULATED_Q3_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Duration_NonConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間個別又は非連結実績 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ForecastMember'
    """ 当年度会計期間連結予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_LowerMember'
    """ 当年度会計期間連結下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ResultMember'
    """ 当年度会計期間連結実績 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_UpperMember'
    """ 当年度会計期間連結上限 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_ForecastMember'
    """ 当年度会計期間個別又は非連結予想 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_LowerMember'
    """ 当年度会計期間個別又は非連結下限 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_ResultMember'
    """ 当年度会計期間個別又は非連結実績 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_UpperMember'
    """ 当年度会計期間個別又は非連結上限 """
    NEXT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'NextAccumulatedQ2Duration_ConsolidatedMember_ForecastMember'
    """ 次年度期初から第２四半期間連結予想 """
    NEXT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__LOWER_MEMBER = 'NextAccumulatedQ2Duration_ConsolidatedMember_LowerMember'
    """ 次年度期初から第２四半期間連結下限 """
    NEXT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__UPPER_MEMBER = 'NextAccumulatedQ2Duration_ConsolidatedMember_UpperMember'
    """ 次年度期初から第２四半期間連結上限 """
    NEXT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'NextAccumulatedQ2Duration_NonConsolidatedMember_ForecastMember'
    """ 次年度期初から第２四半期間個別又は非連結予想 """
    NEXT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__LOWER_MEMBER = 'NextAccumulatedQ2Duration_NonConsolidatedMember_LowerMember'
    """ 次年度期初から第２四半期間個別又は非連結下限 """
    NEXT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__UPPER_MEMBER = 'NextAccumulatedQ2Duration_NonConsolidatedMember_UpperMember'
    """ 次年度期初から第２四半期間個別又は非連結上限 """
    NEXT_YEAR_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'NextYearDuration_ConsolidatedMember_ForecastMember'
    """ 次年度会計期間連結予想 """
    NEXT_YEAR_DURATION__CONSOLIDATED_MEMBER__LOWER_MEMBER = 'NextYearDuration_ConsolidatedMember_LowerMember'
    """ 次年度会計期間連結下限 """
    NEXT_YEAR_DURATION__CONSOLIDATED_MEMBER__UPPER_MEMBER = 'NextYearDuration_ConsolidatedMember_UpperMember'
    """ 次年度会計期間連結上限 """
    NEXT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'NextYearDuration_NonConsolidatedMember_ForecastMember'
    """ 次年度会計期間個別又は非連結予想 """
    NEXT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__LOWER_MEMBER = 'NextYearDuration_NonConsolidatedMember_LowerMember'
    """ 次年度会計期間個別又は非連結下限 """
    NEXT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__UPPER_MEMBER = 'NextYearDuration_NonConsolidatedMember_UpperMember'
    """ 次年度会計期間個別又は非連結上限 """
    PRIOR_ACCUMULATED_Q1_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ1Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第１四半期間連結実績 """
    PRIOR_ACCUMULATED_Q1_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ1Duration_NonConsolidatedMember_ResultMember'
    """ 前年度期初から第１四半期間個別又は非連結実績 """
    PRIOR_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第２四半期間連結実績 """
    PRIOR_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ2Duration_NonConsolidatedMember_ResultMember'
    """ 前年度期初から第２四半期間個別又は非連結実績 """
    PRIOR_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第３四半期間連結実績 """
    PRIOR_ACCUMULATED_Q3_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ3Duration_NonConsolidatedMember_ResultMember'
    """ 前年度期初から第３四半期間個別又は非連結実績 """
    PRIOR_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearDuration_ConsolidatedMember_ResultMember'
    """ 前年度会計期間連結実績 """
    PRIOR_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearDuration_NonConsolidatedMember_ResultMember'
    """ 前年度会計期間個別又は非連結実績 """


class ChangeInOperatingIncome(Enum):
    """"増減率、営業利益"""
    CURRENT_ACCUMULATED_Q1_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ1Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第１四半期間連結実績 """
    CURRENT_ACCUMULATED_Q1_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ1Duration_NonConsolidatedMember_ResultMember'
    """ 当年度期初から第１四半期間個別又は非連結実績 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_ForecastMember'
    """ 当年度期初から第２四半期間連結予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_LowerMember'
    """ 当年度期初から第２四半期間連結下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間連結実績 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_UpperMember'
    """ 当年度期初から第２四半期間連結上限 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_ForecastMember'
    """ 当年度期初から第２四半期間個別又は非連結予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_LowerMember'
    """ 当年度期初から第２四半期間個別又は非連結下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間個別又は非連結実績 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_UpperMember'
    """ 当年度期初から第２四半期間個別又は非連結上限 """
    CURRENT_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間連結実績 """
    CURRENT_ACCUMULATED_Q3_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Duration_NonConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間個別又は非連結実績 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ForecastMember'
    """ 当年度会計期間連結予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_LowerMember'
    """ 当年度会計期間連結下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ResultMember'
    """ 当年度会計期間連結実績 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_UpperMember'
    """ 当年度会計期間連結上限 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_ForecastMember'
    """ 当年度会計期間個別又は非連結予想 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_LowerMember'
    """ 当年度会計期間個別又は非連結下限 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_ResultMember'
    """ 当年度会計期間個別又は非連結実績 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_UpperMember'
    """ 当年度会計期間個別又は非連結上限 """
    NEXT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'NextAccumulatedQ2Duration_ConsolidatedMember_ForecastMember'
    """ 次年度期初から第２四半期間連結予想 """
    NEXT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__LOWER_MEMBER = 'NextAccumulatedQ2Duration_ConsolidatedMember_LowerMember'
    """ 次年度期初から第２四半期間連結下限 """
    NEXT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__UPPER_MEMBER = 'NextAccumulatedQ2Duration_ConsolidatedMember_UpperMember'
    """ 次年度期初から第２四半期間連結上限 """
    NEXT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'NextAccumulatedQ2Duration_NonConsolidatedMember_ForecastMember'
    """ 次年度期初から第２四半期間個別又は非連結予想 """
    NEXT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__LOWER_MEMBER = 'NextAccumulatedQ2Duration_NonConsolidatedMember_LowerMember'
    """ 次年度期初から第２四半期間個別又は非連結下限 """
    NEXT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__UPPER_MEMBER = 'NextAccumulatedQ2Duration_NonConsolidatedMember_UpperMember'
    """ 次年度期初から第２四半期間個別又は非連結上限 """
    NEXT_YEAR_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'NextYearDuration_ConsolidatedMember_ForecastMember'
    """ 次年度会計期間連結予想 """
    NEXT_YEAR_DURATION__CONSOLIDATED_MEMBER__LOWER_MEMBER = 'NextYearDuration_ConsolidatedMember_LowerMember'
    """ 次年度会計期間連結下限 """
    NEXT_YEAR_DURATION__CONSOLIDATED_MEMBER__UPPER_MEMBER = 'NextYearDuration_ConsolidatedMember_UpperMember'
    """ 次年度会計期間連結上限 """
    NEXT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'NextYearDuration_NonConsolidatedMember_ForecastMember'
    """ 次年度会計期間個別又は非連結予想 """
    NEXT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__LOWER_MEMBER = 'NextYearDuration_NonConsolidatedMember_LowerMember'
    """ 次年度会計期間個別又は非連結下限 """
    NEXT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__UPPER_MEMBER = 'NextYearDuration_NonConsolidatedMember_UpperMember'
    """ 次年度会計期間個別又は非連結上限 """
    PRIOR_ACCUMULATED_Q1_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ1Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第１四半期間連結実績 """
    PRIOR_ACCUMULATED_Q1_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ1Duration_NonConsolidatedMember_ResultMember'
    """ 前年度期初から第１四半期間個別又は非連結実績 """
    PRIOR_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第２四半期間連結実績 """
    PRIOR_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ2Duration_NonConsolidatedMember_ResultMember'
    """ 前年度期初から第２四半期間個別又は非連結実績 """
    PRIOR_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第３四半期間連結実績 """
    PRIOR_ACCUMULATED_Q3_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ3Duration_NonConsolidatedMember_ResultMember'
    """ 前年度期初から第３四半期間個別又は非連結実績 """
    PRIOR_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearDuration_ConsolidatedMember_ResultMember'
    """ 前年度会計期間連結実績 """
    PRIOR_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearDuration_NonConsolidatedMember_ResultMember'
    """ 前年度会計期間個別又は非連結実績 """


class ChangeInOperatingRevenues(Enum):
    """"増減率、営業収益"""
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間連結実績 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間個別又は非連結実績 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ForecastMember'
    """ 当年度会計期間連結予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_LowerMember'
    """ 当年度会計期間連結下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ResultMember'
    """ 当年度会計期間連結実績 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_UpperMember'
    """ 当年度会計期間連結上限 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_ResultMember'
    """ 当年度会計期間個別又は非連結実績 """
    NEXT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'NextAccumulatedQ2Duration_ConsolidatedMember_ForecastMember'
    """ 次年度期初から第２四半期間連結予想 """
    NEXT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__LOWER_MEMBER = 'NextAccumulatedQ2Duration_ConsolidatedMember_LowerMember'
    """ 次年度期初から第２四半期間連結下限 """
    NEXT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__UPPER_MEMBER = 'NextAccumulatedQ2Duration_ConsolidatedMember_UpperMember'
    """ 次年度期初から第２四半期間連結上限 """
    NEXT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'NextAccumulatedQ2Duration_NonConsolidatedMember_ForecastMember'
    """ 次年度期初から第２四半期間個別又は非連結予想 """
    NEXT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__LOWER_MEMBER = 'NextAccumulatedQ2Duration_NonConsolidatedMember_LowerMember'
    """ 次年度期初から第２四半期間個別又は非連結下限 """
    NEXT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__UPPER_MEMBER = 'NextAccumulatedQ2Duration_NonConsolidatedMember_UpperMember'
    """ 次年度期初から第２四半期間個別又は非連結上限 """
    NEXT_YEAR_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'NextYearDuration_ConsolidatedMember_ForecastMember'
    """ 次年度会計期間連結予想 """
    NEXT_YEAR_DURATION__CONSOLIDATED_MEMBER__LOWER_MEMBER = 'NextYearDuration_ConsolidatedMember_LowerMember'
    """ 次年度会計期間連結下限 """
    NEXT_YEAR_DURATION__CONSOLIDATED_MEMBER__UPPER_MEMBER = 'NextYearDuration_ConsolidatedMember_UpperMember'
    """ 次年度会計期間連結上限 """
    NEXT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'NextYearDuration_NonConsolidatedMember_ForecastMember'
    """ 次年度会計期間個別又は非連結予想 """
    NEXT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__LOWER_MEMBER = 'NextYearDuration_NonConsolidatedMember_LowerMember'
    """ 次年度会計期間個別又は非連結下限 """
    NEXT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__UPPER_MEMBER = 'NextYearDuration_NonConsolidatedMember_UpperMember'
    """ 次年度会計期間個別又は非連結上限 """
    PRIOR_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第２四半期間連結実績 """
    PRIOR_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ2Duration_NonConsolidatedMember_ResultMember'
    """ 前年度期初から第２四半期間個別又は非連結実績 """
    PRIOR_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearDuration_ConsolidatedMember_ResultMember'
    """ 前年度会計期間連結実績 """
    PRIOR_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearDuration_NonConsolidatedMember_ResultMember'
    """ 前年度会計期間個別又は非連結実績 """


class ChangeInOrdinaryIncome(Enum):
    """"増減率、経常利益"""
    CURRENT_ACCUMULATED_Q1_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ1Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第１四半期間連結実績 """
    CURRENT_ACCUMULATED_Q1_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ1Duration_NonConsolidatedMember_ResultMember'
    """ 当年度期初から第１四半期間個別又は非連結実績 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_ForecastMember'
    """ 当年度期初から第２四半期間連結予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_LowerMember'
    """ 当年度期初から第２四半期間連結下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間連結実績 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_UpperMember'
    """ 当年度期初から第２四半期間連結上限 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_ForecastMember'
    """ 当年度期初から第２四半期間個別又は非連結予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_LowerMember'
    """ 当年度期初から第２四半期間個別又は非連結下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間個別又は非連結実績 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_UpperMember'
    """ 当年度期初から第２四半期間個別又は非連結上限 """
    CURRENT_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間連結実績 """
    CURRENT_ACCUMULATED_Q3_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Duration_NonConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間個別又は非連結実績 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ForecastMember'
    """ 当年度会計期間連結予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_LowerMember'
    """ 当年度会計期間連結下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ResultMember'
    """ 当年度会計期間連結実績 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_UpperMember'
    """ 当年度会計期間連結上限 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_ForecastMember'
    """ 当年度会計期間個別又は非連結予想 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_LowerMember'
    """ 当年度会計期間個別又は非連結下限 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_ResultMember'
    """ 当年度会計期間個別又は非連結実績 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_UpperMember'
    """ 当年度会計期間個別又は非連結上限 """
    NEXT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'NextAccumulatedQ2Duration_ConsolidatedMember_ForecastMember'
    """ 次年度期初から第２四半期間連結予想 """
    NEXT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__LOWER_MEMBER = 'NextAccumulatedQ2Duration_ConsolidatedMember_LowerMember'
    """ 次年度期初から第２四半期間連結下限 """
    NEXT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__UPPER_MEMBER = 'NextAccumulatedQ2Duration_ConsolidatedMember_UpperMember'
    """ 次年度期初から第２四半期間連結上限 """
    NEXT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'NextAccumulatedQ2Duration_NonConsolidatedMember_ForecastMember'
    """ 次年度期初から第２四半期間個別又は非連結予想 """
    NEXT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__LOWER_MEMBER = 'NextAccumulatedQ2Duration_NonConsolidatedMember_LowerMember'
    """ 次年度期初から第２四半期間個別又は非連結下限 """
    NEXT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__UPPER_MEMBER = 'NextAccumulatedQ2Duration_NonConsolidatedMember_UpperMember'
    """ 次年度期初から第２四半期間個別又は非連結上限 """
    NEXT_YEAR_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'NextYearDuration_ConsolidatedMember_ForecastMember'
    """ 次年度会計期間連結予想 """
    NEXT_YEAR_DURATION__CONSOLIDATED_MEMBER__LOWER_MEMBER = 'NextYearDuration_ConsolidatedMember_LowerMember'
    """ 次年度会計期間連結下限 """
    NEXT_YEAR_DURATION__CONSOLIDATED_MEMBER__UPPER_MEMBER = 'NextYearDuration_ConsolidatedMember_UpperMember'
    """ 次年度会計期間連結上限 """
    NEXT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'NextYearDuration_NonConsolidatedMember_ForecastMember'
    """ 次年度会計期間個別又は非連結予想 """
    NEXT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__LOWER_MEMBER = 'NextYearDuration_NonConsolidatedMember_LowerMember'
    """ 次年度会計期間個別又は非連結下限 """
    NEXT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__UPPER_MEMBER = 'NextYearDuration_NonConsolidatedMember_UpperMember'
    """ 次年度会計期間個別又は非連結上限 """
    PRIOR_ACCUMULATED_Q1_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ1Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第１四半期間連結実績 """
    PRIOR_ACCUMULATED_Q1_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ1Duration_NonConsolidatedMember_ResultMember'
    """ 前年度期初から第１四半期間個別又は非連結実績 """
    PRIOR_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第２四半期間連結実績 """
    PRIOR_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ2Duration_NonConsolidatedMember_ResultMember'
    """ 前年度期初から第２四半期間個別又は非連結実績 """
    PRIOR_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第３四半期間連結実績 """
    PRIOR_ACCUMULATED_Q3_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ3Duration_NonConsolidatedMember_ResultMember'
    """ 前年度期初から第３四半期間個別又は非連結実績 """
    PRIOR_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearDuration_ConsolidatedMember_ResultMember'
    """ 前年度会計期間連結実績 """
    PRIOR_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearDuration_NonConsolidatedMember_ResultMember'
    """ 前年度会計期間個別又は非連結実績 """


class ChangeInOrdinaryRevenuesBK(Enum):
    """"増減率、経常収益、銀行"""
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間連結実績 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間個別又は非連結実績 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ForecastMember'
    """ 当年度会計期間連結予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_LowerMember'
    """ 当年度会計期間連結下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_UpperMember'
    """ 当年度会計期間連結上限 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_ForecastMember'
    """ 当年度会計期間個別又は非連結予想 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_LowerMember'
    """ 当年度会計期間個別又は非連結下限 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_UpperMember'
    """ 当年度会計期間個別又は非連結上限 """
    PRIOR_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第２四半期間連結実績 """
    PRIOR_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ2Duration_NonConsolidatedMember_ResultMember'
    """ 前年度期初から第２四半期間個別又は非連結実績 """


class ChangeInOrdinaryRevenuesIN(Enum):
    """"増減率、経常収益、保険"""
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間連結実績 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ForecastMember'
    """ 当年度会計期間連結予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_LowerMember'
    """ 当年度会計期間連結下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_UpperMember'
    """ 当年度会計期間連結上限 """
    PRIOR_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第２四半期間連結実績 """


class ChangeInProfitAttributableToOwnersOfParent(Enum):
    """"増減率、親会社株主に帰属する当期純利益"""
    CURRENT_ACCUMULATED_Q1_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ1Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第１四半期間連結実績 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_ForecastMember'
    """ 当年度期初から第２四半期間連結予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_LowerMember'
    """ 当年度期初から第２四半期間連結下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間連結実績 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_UpperMember'
    """ 当年度期初から第２四半期間連結上限 """
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
    NEXT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'NextAccumulatedQ2Duration_ConsolidatedMember_ForecastMember'
    """ 次年度期初から第２四半期間連結予想 """
    NEXT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__LOWER_MEMBER = 'NextAccumulatedQ2Duration_ConsolidatedMember_LowerMember'
    """ 次年度期初から第２四半期間連結下限 """
    NEXT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__UPPER_MEMBER = 'NextAccumulatedQ2Duration_ConsolidatedMember_UpperMember'
    """ 次年度期初から第２四半期間連結上限 """
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


class ChangeInRevenue(Enum):
    """"増減率、売上収益"""
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間連結実績 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ForecastMember'
    """ 当年度会計期間連結予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_LowerMember'
    """ 当年度会計期間連結下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_UpperMember'
    """ 当年度会計期間連結上限 """
    PRIOR_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第２四半期間連結実績 """


class CommemorativeDividend(Enum):
    """"記念配当"""
    CURRENT_ACCUMULATED_Q1_DURATION__ANNUAL_MEMBER__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ1Duration_AnnualMember_NonConsolidatedMember_ResultMember'
    """ 当年度期初から第１四半期間年間個別又は非連結実績 """


class ComprehensiveIncome(Enum):
    """"包括利益"""
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


class DilutedNetIncomePerShare(Enum):
    """"潜在株式調整後1株当たり当期純利益"""
    CURRENT_ACCUMULATED_Q1_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ1Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第１四半期間連結実績 """
    CURRENT_ACCUMULATED_Q1_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ1Duration_NonConsolidatedMember_ResultMember'
    """ 当年度期初から第１四半期間個別又は非連結実績 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間連結実績 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間個別又は非連結実績 """
    CURRENT_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間連結実績 """
    CURRENT_ACCUMULATED_Q3_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Duration_NonConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間個別又は非連結実績 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ResultMember'
    """ 当年度会計期間連結実績 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_ResultMember'
    """ 当年度会計期間個別又は非連結実績 """
    PRIOR_ACCUMULATED_Q1_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ1Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第１四半期間連結実績 """
    PRIOR_ACCUMULATED_Q1_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ1Duration_NonConsolidatedMember_ResultMember'
    """ 前年度期初から第１四半期間個別又は非連結実績 """
    PRIOR_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第２四半期間連結実績 """
    PRIOR_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ2Duration_NonConsolidatedMember_ResultMember'
    """ 前年度期初から第２四半期間個別又は非連結実績 """
    PRIOR_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第３四半期間連結実績 """
    PRIOR_ACCUMULATED_Q3_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ3Duration_NonConsolidatedMember_ResultMember'
    """ 前年度期初から第３四半期間個別又は非連結実績 """
    PRIOR_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearDuration_ConsolidatedMember_ResultMember'
    """ 前年度会計期間連結実績 """
    PRIOR_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearDuration_NonConsolidatedMember_ResultMember'
    """ 前年度会計期間個別又は非連結実績 """


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


class ExtraDividend(Enum):
    """"特別配当"""
    CURRENT_ACCUMULATED_Q1_DURATION__ANNUAL_MEMBER__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ1Duration_AnnualMember_NonConsolidatedMember_ResultMember'
    """ 当年度期初から第１四半期間年間個別又は非連結実績 """


class InvestmentProfitLossOnEquityMethod(Enum):
    """"持分法投資損益"""
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ResultMember'
    """ 当年度会計期間連結実績 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_ResultMember'
    """ 当年度会計期間個別又は非連結実績 """
    PRIOR_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearDuration_ConsolidatedMember_ResultMember'
    """ 前年度会計期間連結実績 """
    PRIOR_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearDuration_NonConsolidatedMember_ResultMember'
    """ 前年度会計期間個別又は非連結実績 """


class NetAssets(Enum):
    """"純資産"""
    CURRENT_ACCUMULATED_Q1_INSTANT__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ1Instant_ConsolidatedMember_ResultMember'
    """ 当年度期初から第１四半期間時点連結実績 """
    CURRENT_ACCUMULATED_Q1_INSTANT__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ1Instant_NonConsolidatedMember_ResultMember'
    """ 当年度期初から第１四半期間時点個別又は非連結実績 """
    CURRENT_ACCUMULATED_Q2_INSTANT__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Instant_ConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間時点連結実績 """
    CURRENT_ACCUMULATED_Q2_INSTANT__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Instant_NonConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間時点個別又は非連結実績 """
    CURRENT_ACCUMULATED_Q3_INSTANT__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Instant_ConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間時点連結実績 """
    CURRENT_ACCUMULATED_Q3_INSTANT__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Instant_NonConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間時点個別又は非連結実績 """
    CURRENT_YEAR_INSTANT__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearInstant_ConsolidatedMember_ResultMember'
    """ 当年度時点連結実績 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearInstant_NonConsolidatedMember_ResultMember'
    """ 当年度時点個別又は非連結実績 """
    PRIOR_YEAR_INSTANT__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearInstant_ConsolidatedMember_ResultMember'
    """ 前年度時点連結実績 """
    PRIOR_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearInstant_NonConsolidatedMember_ResultMember'
    """ 前年度時点個別又は非連結実績 """


class NetAssetsPerShare(Enum):
    """"1株当たり純資産"""
    CURRENT_ACCUMULATED_Q1_INSTANT__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ1Instant_ConsolidatedMember_ResultMember'
    """ 当年度期初から第１四半期間時点連結実績 """
    CURRENT_ACCUMULATED_Q1_INSTANT__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ1Instant_NonConsolidatedMember_ResultMember'
    """ 当年度期初から第１四半期間時点個別又は非連結実績 """
    CURRENT_ACCUMULATED_Q2_INSTANT__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Instant_ConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間時点連結実績 """
    CURRENT_ACCUMULATED_Q2_INSTANT__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Instant_NonConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間時点個別又は非連結実績 """
    CURRENT_ACCUMULATED_Q3_INSTANT__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Instant_ConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間時点連結実績 """
    CURRENT_ACCUMULATED_Q3_INSTANT__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Instant_NonConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間時点個別又は非連結実績 """
    CURRENT_YEAR_INSTANT__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearInstant_ConsolidatedMember_ResultMember'
    """ 当年度時点連結実績 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearInstant_NonConsolidatedMember_ResultMember'
    """ 当年度時点個別又は非連結実績 """
    PRIOR_YEAR_INSTANT__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearInstant_ConsolidatedMember_ResultMember'
    """ 前年度時点連結実績 """
    PRIOR_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearInstant_NonConsolidatedMember_ResultMember'
    """ 前年度時点個別又は非連結実績 """


class NetIncome(Enum):
    """"当期純利益"""
    CURRENT_ACCUMULATED_Q1_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ1Duration_NonConsolidatedMember_ResultMember'
    """ 当年度期初から第１四半期間個別又は非連結実績 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_ForecastMember'
    """ 当年度期初から第２四半期間連結予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_LowerMember'
    """ 当年度期初から第２四半期間連結下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_UpperMember'
    """ 当年度期初から第２四半期間連結上限 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_ForecastMember'
    """ 当年度期初から第２四半期間個別又は非連結予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_LowerMember'
    """ 当年度期初から第２四半期間個別又は非連結下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間個別又は非連結実績 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_UpperMember'
    """ 当年度期初から第２四半期間個別又は非連結上限 """
    CURRENT_ACCUMULATED_Q3_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Duration_NonConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間個別又は非連結実績 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ForecastMember'
    """ 当年度会計期間連結予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_LowerMember'
    """ 当年度会計期間連結下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_UpperMember'
    """ 当年度会計期間連結上限 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_ForecastMember'
    """ 当年度会計期間個別又は非連結予想 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_LowerMember'
    """ 当年度会計期間個別又は非連結下限 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_ResultMember'
    """ 当年度会計期間個別又は非連結実績 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_UpperMember'
    """ 当年度会計期間個別又は非連結上限 """
    NEXT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'NextAccumulatedQ2Duration_NonConsolidatedMember_ForecastMember'
    """ 次年度期初から第２四半期間個別又は非連結予想 """
    NEXT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__LOWER_MEMBER = 'NextAccumulatedQ2Duration_NonConsolidatedMember_LowerMember'
    """ 次年度期初から第２四半期間個別又は非連結下限 """
    NEXT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__UPPER_MEMBER = 'NextAccumulatedQ2Duration_NonConsolidatedMember_UpperMember'
    """ 次年度期初から第２四半期間個別又は非連結上限 """
    NEXT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'NextYearDuration_NonConsolidatedMember_ForecastMember'
    """ 次年度会計期間個別又は非連結予想 """
    NEXT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__LOWER_MEMBER = 'NextYearDuration_NonConsolidatedMember_LowerMember'
    """ 次年度会計期間個別又は非連結下限 """
    NEXT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__UPPER_MEMBER = 'NextYearDuration_NonConsolidatedMember_UpperMember'
    """ 次年度会計期間個別又は非連結上限 """
    PRIOR_ACCUMULATED_Q1_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ1Duration_NonConsolidatedMember_ResultMember'
    """ 前年度期初から第１四半期間個別又は非連結実績 """
    PRIOR_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ2Duration_NonConsolidatedMember_ResultMember'
    """ 前年度期初から第２四半期間個別又は非連結実績 """
    PRIOR_ACCUMULATED_Q3_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ3Duration_NonConsolidatedMember_ResultMember'
    """ 前年度期初から第３四半期間個別又は非連結実績 """
    PRIOR_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearDuration_NonConsolidatedMember_ResultMember'
    """ 前年度会計期間個別又は非連結実績 """


class NetIncomePerShare(Enum):
    """"1株当たり当期純利益"""
    CURRENT_ACCUMULATED_Q1_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ1Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第１四半期間連結実績 """
    CURRENT_ACCUMULATED_Q1_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ1Duration_NonConsolidatedMember_ResultMember'
    """ 当年度期初から第１四半期間個別又は非連結実績 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_ForecastMember'
    """ 当年度期初から第２四半期間連結予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_LowerMember'
    """ 当年度期初から第２四半期間連結下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間連結実績 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_UpperMember'
    """ 当年度期初から第２四半期間連結上限 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_ForecastMember'
    """ 当年度期初から第２四半期間個別又は非連結予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_LowerMember'
    """ 当年度期初から第２四半期間個別又は非連結下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間個別又は非連結実績 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_UpperMember'
    """ 当年度期初から第２四半期間個別又は非連結上限 """
    CURRENT_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間連結実績 """
    CURRENT_ACCUMULATED_Q3_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Duration_NonConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間個別又は非連結実績 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ForecastMember'
    """ 当年度会計期間連結予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_LowerMember'
    """ 当年度会計期間連結下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ResultMember'
    """ 当年度会計期間連結実績 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_UpperMember'
    """ 当年度会計期間連結上限 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_ForecastMember'
    """ 当年度会計期間個別又は非連結予想 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_LowerMember'
    """ 当年度会計期間個別又は非連結下限 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_ResultMember'
    """ 当年度会計期間個別又は非連結実績 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_UpperMember'
    """ 当年度会計期間個別又は非連結上限 """
    NEXT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'NextAccumulatedQ2Duration_ConsolidatedMember_ForecastMember'
    """ 次年度期初から第２四半期間連結予想 """
    NEXT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__LOWER_MEMBER = 'NextAccumulatedQ2Duration_ConsolidatedMember_LowerMember'
    """ 次年度期初から第２四半期間連結下限 """
    NEXT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__UPPER_MEMBER = 'NextAccumulatedQ2Duration_ConsolidatedMember_UpperMember'
    """ 次年度期初から第２四半期間連結上限 """
    NEXT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'NextAccumulatedQ2Duration_NonConsolidatedMember_ForecastMember'
    """ 次年度期初から第２四半期間個別又は非連結予想 """
    NEXT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__LOWER_MEMBER = 'NextAccumulatedQ2Duration_NonConsolidatedMember_LowerMember'
    """ 次年度期初から第２四半期間個別又は非連結下限 """
    NEXT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__UPPER_MEMBER = 'NextAccumulatedQ2Duration_NonConsolidatedMember_UpperMember'
    """ 次年度期初から第２四半期間個別又は非連結上限 """
    NEXT_YEAR_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'NextYearDuration_ConsolidatedMember_ForecastMember'
    """ 次年度会計期間連結予想 """
    NEXT_YEAR_DURATION__CONSOLIDATED_MEMBER__LOWER_MEMBER = 'NextYearDuration_ConsolidatedMember_LowerMember'
    """ 次年度会計期間連結下限 """
    NEXT_YEAR_DURATION__CONSOLIDATED_MEMBER__UPPER_MEMBER = 'NextYearDuration_ConsolidatedMember_UpperMember'
    """ 次年度会計期間連結上限 """
    NEXT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'NextYearDuration_NonConsolidatedMember_ForecastMember'
    """ 次年度会計期間個別又は非連結予想 """
    NEXT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__LOWER_MEMBER = 'NextYearDuration_NonConsolidatedMember_LowerMember'
    """ 次年度会計期間個別又は非連結下限 """
    NEXT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__UPPER_MEMBER = 'NextYearDuration_NonConsolidatedMember_UpperMember'
    """ 次年度会計期間個別又は非連結上限 """
    PRIOR_ACCUMULATED_Q1_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ1Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第１四半期間連結実績 """
    PRIOR_ACCUMULATED_Q1_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ1Duration_NonConsolidatedMember_ResultMember'
    """ 前年度期初から第１四半期間個別又は非連結実績 """
    PRIOR_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第２四半期間連結実績 """
    PRIOR_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ2Duration_NonConsolidatedMember_ResultMember'
    """ 前年度期初から第２四半期間個別又は非連結実績 """
    PRIOR_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第３四半期間連結実績 """
    PRIOR_ACCUMULATED_Q3_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ3Duration_NonConsolidatedMember_ResultMember'
    """ 前年度期初から第３四半期間個別又は非連結実績 """
    PRIOR_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearDuration_ConsolidatedMember_ResultMember'
    """ 前年度会計期間連結実績 """
    PRIOR_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearDuration_NonConsolidatedMember_ResultMember'
    """ 前年度会計期間個別又は非連結実績 """


class NetIncomeToShareholdersEquityRatio(Enum):
    """"自己資本当期純利益率"""
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ResultMember'
    """ 当年度会計期間連結実績 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_ResultMember'
    """ 当年度会計期間個別又は非連結実績 """
    PRIOR_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearDuration_ConsolidatedMember_ResultMember'
    """ 前年度会計期間連結実績 """
    PRIOR_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearDuration_NonConsolidatedMember_ResultMember'
    """ 前年度会計期間個別又は非連結実績 """


class NetSales(Enum):
    """"売上高"""
    CURRENT_ACCUMULATED_Q1_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ1Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第１四半期間連結実績 """
    CURRENT_ACCUMULATED_Q1_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ1Duration_NonConsolidatedMember_ResultMember'
    """ 当年度期初から第１四半期間個別又は非連結実績 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_ForecastMember'
    """ 当年度期初から第２四半期間連結予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_LowerMember'
    """ 当年度期初から第２四半期間連結下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間連結実績 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_UpperMember'
    """ 当年度期初から第２四半期間連結上限 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_ForecastMember'
    """ 当年度期初から第２四半期間個別又は非連結予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_LowerMember'
    """ 当年度期初から第２四半期間個別又は非連結下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間個別又は非連結実績 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_UpperMember'
    """ 当年度期初から第２四半期間個別又は非連結上限 """
    CURRENT_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間連結実績 """
    CURRENT_ACCUMULATED_Q3_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Duration_NonConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間個別又は非連結実績 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ForecastMember'
    """ 当年度会計期間連結予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_LowerMember'
    """ 当年度会計期間連結下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ResultMember'
    """ 当年度会計期間連結実績 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_UpperMember'
    """ 当年度会計期間連結上限 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_ForecastMember'
    """ 当年度会計期間個別又は非連結予想 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_LowerMember'
    """ 当年度会計期間個別又は非連結下限 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_ResultMember'
    """ 当年度会計期間個別又は非連結実績 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_UpperMember'
    """ 当年度会計期間個別又は非連結上限 """
    NEXT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'NextAccumulatedQ2Duration_ConsolidatedMember_ForecastMember'
    """ 次年度期初から第２四半期間連結予想 """
    NEXT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__LOWER_MEMBER = 'NextAccumulatedQ2Duration_ConsolidatedMember_LowerMember'
    """ 次年度期初から第２四半期間連結下限 """
    NEXT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__UPPER_MEMBER = 'NextAccumulatedQ2Duration_ConsolidatedMember_UpperMember'
    """ 次年度期初から第２四半期間連結上限 """
    NEXT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'NextAccumulatedQ2Duration_NonConsolidatedMember_ForecastMember'
    """ 次年度期初から第２四半期間個別又は非連結予想 """
    NEXT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__LOWER_MEMBER = 'NextAccumulatedQ2Duration_NonConsolidatedMember_LowerMember'
    """ 次年度期初から第２四半期間個別又は非連結下限 """
    NEXT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__UPPER_MEMBER = 'NextAccumulatedQ2Duration_NonConsolidatedMember_UpperMember'
    """ 次年度期初から第２四半期間個別又は非連結上限 """
    NEXT_YEAR_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'NextYearDuration_ConsolidatedMember_ForecastMember'
    """ 次年度会計期間連結予想 """
    NEXT_YEAR_DURATION__CONSOLIDATED_MEMBER__LOWER_MEMBER = 'NextYearDuration_ConsolidatedMember_LowerMember'
    """ 次年度会計期間連結下限 """
    NEXT_YEAR_DURATION__CONSOLIDATED_MEMBER__UPPER_MEMBER = 'NextYearDuration_ConsolidatedMember_UpperMember'
    """ 次年度会計期間連結上限 """
    NEXT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'NextYearDuration_NonConsolidatedMember_ForecastMember'
    """ 次年度会計期間個別又は非連結予想 """
    NEXT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__LOWER_MEMBER = 'NextYearDuration_NonConsolidatedMember_LowerMember'
    """ 次年度会計期間個別又は非連結下限 """
    NEXT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__UPPER_MEMBER = 'NextYearDuration_NonConsolidatedMember_UpperMember'
    """ 次年度会計期間個別又は非連結上限 """
    PRIOR_ACCUMULATED_Q1_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ1Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第１四半期間連結実績 """
    PRIOR_ACCUMULATED_Q1_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ1Duration_NonConsolidatedMember_ResultMember'
    """ 前年度期初から第１四半期間個別又は非連結実績 """
    PRIOR_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第２四半期間連結実績 """
    PRIOR_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ2Duration_NonConsolidatedMember_ResultMember'
    """ 前年度期初から第２四半期間個別又は非連結実績 """
    PRIOR_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第３四半期間連結実績 """
    PRIOR_ACCUMULATED_Q3_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ3Duration_NonConsolidatedMember_ResultMember'
    """ 前年度期初から第３四半期間個別又は非連結実績 """
    PRIOR_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearDuration_ConsolidatedMember_ResultMember'
    """ 前年度会計期間連結実績 """
    PRIOR_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearDuration_NonConsolidatedMember_ResultMember'
    """ 前年度会計期間個別又は非連結実績 """


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


class NumberOfSubsidiariesExcludedFromConsolidation(Enum):
    """"除外"""
    CURRENT_ACCUMULATED_Q1_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ1Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第１四半期間連結実績 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間連結実績 """
    CURRENT_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間連結実績 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ResultMember'
    """ 当年度会計期間連結実績 """


class NumberOfSubsidiariesNewlyConsolidated(Enum):
    """"新規"""
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


class OperatingIncome(Enum):
    """"営業利益"""
    CURRENT_ACCUMULATED_Q1_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ1Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第１四半期間連結実績 """
    CURRENT_ACCUMULATED_Q1_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ1Duration_NonConsolidatedMember_ResultMember'
    """ 当年度期初から第１四半期間個別又は非連結実績 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_ForecastMember'
    """ 当年度期初から第２四半期間連結予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_LowerMember'
    """ 当年度期初から第２四半期間連結下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間連結実績 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_UpperMember'
    """ 当年度期初から第２四半期間連結上限 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_ForecastMember'
    """ 当年度期初から第２四半期間個別又は非連結予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_LowerMember'
    """ 当年度期初から第２四半期間個別又は非連結下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間個別又は非連結実績 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_UpperMember'
    """ 当年度期初から第２四半期間個別又は非連結上限 """
    CURRENT_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間連結実績 """
    CURRENT_ACCUMULATED_Q3_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Duration_NonConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間個別又は非連結実績 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ForecastMember'
    """ 当年度会計期間連結予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_LowerMember'
    """ 当年度会計期間連結下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ResultMember'
    """ 当年度会計期間連結実績 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_UpperMember'
    """ 当年度会計期間連結上限 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_ForecastMember'
    """ 当年度会計期間個別又は非連結予想 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_LowerMember'
    """ 当年度会計期間個別又は非連結下限 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_ResultMember'
    """ 当年度会計期間個別又は非連結実績 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_UpperMember'
    """ 当年度会計期間個別又は非連結上限 """
    NEXT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'NextAccumulatedQ2Duration_ConsolidatedMember_ForecastMember'
    """ 次年度期初から第２四半期間連結予想 """
    NEXT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__LOWER_MEMBER = 'NextAccumulatedQ2Duration_ConsolidatedMember_LowerMember'
    """ 次年度期初から第２四半期間連結下限 """
    NEXT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__UPPER_MEMBER = 'NextAccumulatedQ2Duration_ConsolidatedMember_UpperMember'
    """ 次年度期初から第２四半期間連結上限 """
    NEXT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'NextAccumulatedQ2Duration_NonConsolidatedMember_ForecastMember'
    """ 次年度期初から第２四半期間個別又は非連結予想 """
    NEXT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__LOWER_MEMBER = 'NextAccumulatedQ2Duration_NonConsolidatedMember_LowerMember'
    """ 次年度期初から第２四半期間個別又は非連結下限 """
    NEXT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__UPPER_MEMBER = 'NextAccumulatedQ2Duration_NonConsolidatedMember_UpperMember'
    """ 次年度期初から第２四半期間個別又は非連結上限 """
    NEXT_YEAR_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'NextYearDuration_ConsolidatedMember_ForecastMember'
    """ 次年度会計期間連結予想 """
    NEXT_YEAR_DURATION__CONSOLIDATED_MEMBER__LOWER_MEMBER = 'NextYearDuration_ConsolidatedMember_LowerMember'
    """ 次年度会計期間連結下限 """
    NEXT_YEAR_DURATION__CONSOLIDATED_MEMBER__UPPER_MEMBER = 'NextYearDuration_ConsolidatedMember_UpperMember'
    """ 次年度会計期間連結上限 """
    NEXT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'NextYearDuration_NonConsolidatedMember_ForecastMember'
    """ 次年度会計期間個別又は非連結予想 """
    NEXT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__LOWER_MEMBER = 'NextYearDuration_NonConsolidatedMember_LowerMember'
    """ 次年度会計期間個別又は非連結下限 """
    NEXT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__UPPER_MEMBER = 'NextYearDuration_NonConsolidatedMember_UpperMember'
    """ 次年度会計期間個別又は非連結上限 """
    PRIOR_ACCUMULATED_Q1_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ1Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第１四半期間連結実績 """
    PRIOR_ACCUMULATED_Q1_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ1Duration_NonConsolidatedMember_ResultMember'
    """ 前年度期初から第１四半期間個別又は非連結実績 """
    PRIOR_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第２四半期間連結実績 """
    PRIOR_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ2Duration_NonConsolidatedMember_ResultMember'
    """ 前年度期初から第２四半期間個別又は非連結実績 """
    PRIOR_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第３四半期間連結実績 """
    PRIOR_ACCUMULATED_Q3_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ3Duration_NonConsolidatedMember_ResultMember'
    """ 前年度期初から第３四半期間個別又は非連結実績 """
    PRIOR_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearDuration_ConsolidatedMember_ResultMember'
    """ 前年度会計期間連結実績 """
    PRIOR_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearDuration_NonConsolidatedMember_ResultMember'
    """ 前年度会計期間個別又は非連結実績 """


class OperatingIncomeToNetSalesRatio(Enum):
    """"売上高営業利益率"""
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ResultMember'
    """ 当年度会計期間連結実績 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_ResultMember'
    """ 当年度会計期間個別又は非連結実績 """
    PRIOR_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearDuration_ConsolidatedMember_ResultMember'
    """ 前年度会計期間連結実績 """
    PRIOR_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearDuration_NonConsolidatedMember_ResultMember'
    """ 前年度会計期間個別又は非連結実績 """


class OperatingIncomeToOperatingRevenuesRatio(Enum):
    """"営業収益営業利益率"""
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ResultMember'
    """ 当年度会計期間連結実績 """
    PRIOR_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearDuration_ConsolidatedMember_ResultMember'
    """ 前年度会計期間連結実績 """


class OperatingRevenues(Enum):
    """"営業収益"""
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間連結実績 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間個別又は非連結実績 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ForecastMember'
    """ 当年度会計期間連結予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_LowerMember'
    """ 当年度会計期間連結下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ResultMember'
    """ 当年度会計期間連結実績 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_UpperMember'
    """ 当年度会計期間連結上限 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_ResultMember'
    """ 当年度会計期間個別又は非連結実績 """
    NEXT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'NextAccumulatedQ2Duration_ConsolidatedMember_ForecastMember'
    """ 次年度期初から第２四半期間連結予想 """
    NEXT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__LOWER_MEMBER = 'NextAccumulatedQ2Duration_ConsolidatedMember_LowerMember'
    """ 次年度期初から第２四半期間連結下限 """
    NEXT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__UPPER_MEMBER = 'NextAccumulatedQ2Duration_ConsolidatedMember_UpperMember'
    """ 次年度期初から第２四半期間連結上限 """
    NEXT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'NextAccumulatedQ2Duration_NonConsolidatedMember_ForecastMember'
    """ 次年度期初から第２四半期間個別又は非連結予想 """
    NEXT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__LOWER_MEMBER = 'NextAccumulatedQ2Duration_NonConsolidatedMember_LowerMember'
    """ 次年度期初から第２四半期間個別又は非連結下限 """
    NEXT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__UPPER_MEMBER = 'NextAccumulatedQ2Duration_NonConsolidatedMember_UpperMember'
    """ 次年度期初から第２四半期間個別又は非連結上限 """
    NEXT_YEAR_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'NextYearDuration_ConsolidatedMember_ForecastMember'
    """ 次年度会計期間連結予想 """
    NEXT_YEAR_DURATION__CONSOLIDATED_MEMBER__LOWER_MEMBER = 'NextYearDuration_ConsolidatedMember_LowerMember'
    """ 次年度会計期間連結下限 """
    NEXT_YEAR_DURATION__CONSOLIDATED_MEMBER__UPPER_MEMBER = 'NextYearDuration_ConsolidatedMember_UpperMember'
    """ 次年度会計期間連結上限 """
    NEXT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'NextYearDuration_NonConsolidatedMember_ForecastMember'
    """ 次年度会計期間個別又は非連結予想 """
    NEXT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__LOWER_MEMBER = 'NextYearDuration_NonConsolidatedMember_LowerMember'
    """ 次年度会計期間個別又は非連結下限 """
    NEXT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__UPPER_MEMBER = 'NextYearDuration_NonConsolidatedMember_UpperMember'
    """ 次年度会計期間個別又は非連結上限 """
    PRIOR_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第２四半期間連結実績 """
    PRIOR_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ2Duration_NonConsolidatedMember_ResultMember'
    """ 前年度期初から第２四半期間個別又は非連結実績 """
    PRIOR_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearDuration_ConsolidatedMember_ResultMember'
    """ 前年度会計期間連結実績 """
    PRIOR_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearDuration_NonConsolidatedMember_ResultMember'
    """ 前年度会計期間個別又は非連結実績 """


class OrdinaryIncome(Enum):
    """"経常利益"""
    CURRENT_ACCUMULATED_Q1_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ1Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第１四半期間連結実績 """
    CURRENT_ACCUMULATED_Q1_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ1Duration_NonConsolidatedMember_ResultMember'
    """ 当年度期初から第１四半期間個別又は非連結実績 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_ForecastMember'
    """ 当年度期初から第２四半期間連結予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_LowerMember'
    """ 当年度期初から第２四半期間連結下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間連結実績 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_UpperMember'
    """ 当年度期初から第２四半期間連結上限 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_ForecastMember'
    """ 当年度期初から第２四半期間個別又は非連結予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_LowerMember'
    """ 当年度期初から第２四半期間個別又は非連結下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間個別又は非連結実績 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_UpperMember'
    """ 当年度期初から第２四半期間個別又は非連結上限 """
    CURRENT_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間連結実績 """
    CURRENT_ACCUMULATED_Q3_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Duration_NonConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間個別又は非連結実績 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ForecastMember'
    """ 当年度会計期間連結予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_LowerMember'
    """ 当年度会計期間連結下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ResultMember'
    """ 当年度会計期間連結実績 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_UpperMember'
    """ 当年度会計期間連結上限 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_ForecastMember'
    """ 当年度会計期間個別又は非連結予想 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_LowerMember'
    """ 当年度会計期間個別又は非連結下限 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_ResultMember'
    """ 当年度会計期間個別又は非連結実績 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_UpperMember'
    """ 当年度会計期間個別又は非連結上限 """
    NEXT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'NextAccumulatedQ2Duration_ConsolidatedMember_ForecastMember'
    """ 次年度期初から第２四半期間連結予想 """
    NEXT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__LOWER_MEMBER = 'NextAccumulatedQ2Duration_ConsolidatedMember_LowerMember'
    """ 次年度期初から第２四半期間連結下限 """
    NEXT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__UPPER_MEMBER = 'NextAccumulatedQ2Duration_ConsolidatedMember_UpperMember'
    """ 次年度期初から第２四半期間連結上限 """
    NEXT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'NextAccumulatedQ2Duration_NonConsolidatedMember_ForecastMember'
    """ 次年度期初から第２四半期間個別又は非連結予想 """
    NEXT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__LOWER_MEMBER = 'NextAccumulatedQ2Duration_NonConsolidatedMember_LowerMember'
    """ 次年度期初から第２四半期間個別又は非連結下限 """
    NEXT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__UPPER_MEMBER = 'NextAccumulatedQ2Duration_NonConsolidatedMember_UpperMember'
    """ 次年度期初から第２四半期間個別又は非連結上限 """
    NEXT_YEAR_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'NextYearDuration_ConsolidatedMember_ForecastMember'
    """ 次年度会計期間連結予想 """
    NEXT_YEAR_DURATION__CONSOLIDATED_MEMBER__LOWER_MEMBER = 'NextYearDuration_ConsolidatedMember_LowerMember'
    """ 次年度会計期間連結下限 """
    NEXT_YEAR_DURATION__CONSOLIDATED_MEMBER__UPPER_MEMBER = 'NextYearDuration_ConsolidatedMember_UpperMember'
    """ 次年度会計期間連結上限 """
    NEXT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'NextYearDuration_NonConsolidatedMember_ForecastMember'
    """ 次年度会計期間個別又は非連結予想 """
    NEXT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__LOWER_MEMBER = 'NextYearDuration_NonConsolidatedMember_LowerMember'
    """ 次年度会計期間個別又は非連結下限 """
    NEXT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__UPPER_MEMBER = 'NextYearDuration_NonConsolidatedMember_UpperMember'
    """ 次年度会計期間個別又は非連結上限 """
    PRIOR_ACCUMULATED_Q1_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ1Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第１四半期間連結実績 """
    PRIOR_ACCUMULATED_Q1_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ1Duration_NonConsolidatedMember_ResultMember'
    """ 前年度期初から第１四半期間個別又は非連結実績 """
    PRIOR_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第２四半期間連結実績 """
    PRIOR_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ2Duration_NonConsolidatedMember_ResultMember'
    """ 前年度期初から第２四半期間個別又は非連結実績 """
    PRIOR_ACCUMULATED_Q3_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ3Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第３四半期間連結実績 """
    PRIOR_ACCUMULATED_Q3_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ3Duration_NonConsolidatedMember_ResultMember'
    """ 前年度期初から第３四半期間個別又は非連結実績 """
    PRIOR_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearDuration_ConsolidatedMember_ResultMember'
    """ 前年度会計期間連結実績 """
    PRIOR_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearDuration_NonConsolidatedMember_ResultMember'
    """ 前年度会計期間個別又は非連結実績 """


class OrdinaryIncomeToTotalAssetsRatio(Enum):
    """"総資産経常利益率"""
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ResultMember'
    """ 当年度会計期間連結実績 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_ResultMember'
    """ 当年度会計期間個別又は非連結実績 """
    PRIOR_YEAR_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearDuration_ConsolidatedMember_ResultMember'
    """ 前年度会計期間連結実績 """
    PRIOR_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearDuration_NonConsolidatedMember_ResultMember'
    """ 前年度会計期間個別又は非連結実績 """


class OrdinaryRevenuesBK(Enum):
    """"経常収益、銀行"""
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間連結実績 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間個別又は非連結実績 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ForecastMember'
    """ 当年度会計期間連結予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_LowerMember'
    """ 当年度会計期間連結下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_UpperMember'
    """ 当年度会計期間連結上限 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_ForecastMember'
    """ 当年度会計期間個別又は非連結予想 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_LowerMember'
    """ 当年度会計期間個別又は非連結下限 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_UpperMember'
    """ 当年度会計期間個別又は非連結上限 """
    PRIOR_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第２四半期間連結実績 """
    PRIOR_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ2Duration_NonConsolidatedMember_ResultMember'
    """ 前年度期初から第２四半期間個別又は非連結実績 """


class OrdinaryRevenuesIN(Enum):
    """"経常収益、保険"""
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間連結実績 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ForecastMember'
    """ 当年度会計期間連結予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_LowerMember'
    """ 当年度会計期間連結下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_UpperMember'
    """ 当年度会計期間連結上限 """
    PRIOR_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第２四半期間連結実績 """


class OwnersEquity(Enum):
    """"自己資本"""
    CURRENT_ACCUMULATED_Q1_INSTANT__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ1Instant_ConsolidatedMember_ResultMember'
    """ 当年度期初から第１四半期間時点連結実績 """
    CURRENT_ACCUMULATED_Q1_INSTANT__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ1Instant_NonConsolidatedMember_ResultMember'
    """ 当年度期初から第１四半期間時点個別又は非連結実績 """
    CURRENT_ACCUMULATED_Q2_INSTANT__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Instant_ConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間時点連結実績 """
    CURRENT_ACCUMULATED_Q2_INSTANT__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Instant_NonConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間時点個別又は非連結実績 """
    CURRENT_ACCUMULATED_Q3_INSTANT__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Instant_ConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間時点連結実績 """
    CURRENT_ACCUMULATED_Q3_INSTANT__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Instant_NonConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間時点個別又は非連結実績 """
    CURRENT_YEAR_INSTANT__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearInstant_ConsolidatedMember_ResultMember'
    """ 当年度時点連結実績 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearInstant_NonConsolidatedMember_ResultMember'
    """ 当年度時点個別又は非連結実績 """
    PRIOR_YEAR_INSTANT__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearInstant_ConsolidatedMember_ResultMember'
    """ 前年度時点連結実績 """
    PRIOR_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearInstant_NonConsolidatedMember_ResultMember'
    """ 前年度時点個別又は非連結実績 """


class PayoutRatio(Enum):
    """"配当性向"""
    CURRENT_YEAR_DURATION__ANNUAL_MEMBER__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_AnnualMember_ConsolidatedMember_ResultMember'
    """ 当年度会計期間年間連結実績 """
    CURRENT_YEAR_DURATION__ANNUAL_MEMBER__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_AnnualMember_NonConsolidatedMember_ResultMember'
    """ 当年度会計期間年間個別又は非連結実績 """
    NEXT_YEAR_DURATION__ANNUAL_MEMBER__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'NextYearDuration_AnnualMember_ConsolidatedMember_ForecastMember'
    """ 次年度会計期間年間連結予想 """
    NEXT_YEAR_DURATION__ANNUAL_MEMBER__NON_CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'NextYearDuration_AnnualMember_NonConsolidatedMember_ForecastMember'
    """ 次年度会計期間年間個別又は非連結予想 """
    PRIOR_YEAR_DURATION__ANNUAL_MEMBER__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearDuration_AnnualMember_ConsolidatedMember_ResultMember'
    """ 前年度会計期間年間連結実績 """
    PRIOR_YEAR_DURATION__ANNUAL_MEMBER__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearDuration_AnnualMember_NonConsolidatedMember_ResultMember'
    """ 前年度会計期間年間個別又は非連結実績 """


class ProfitAttributableToOwnersOfParent(Enum):
    """"親会社株主に帰属する当期純利益"""
    CURRENT_ACCUMULATED_Q1_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ1Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第１四半期間連結実績 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_ForecastMember'
    """ 当年度期初から第２四半期間連結予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_LowerMember'
    """ 当年度期初から第２四半期間連結下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間連結実績 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_UpperMember'
    """ 当年度期初から第２四半期間連結上限 """
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
    NEXT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'NextAccumulatedQ2Duration_ConsolidatedMember_ForecastMember'
    """ 次年度期初から第２四半期間連結予想 """
    NEXT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__LOWER_MEMBER = 'NextAccumulatedQ2Duration_ConsolidatedMember_LowerMember'
    """ 次年度期初から第２四半期間連結下限 """
    NEXT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__UPPER_MEMBER = 'NextAccumulatedQ2Duration_ConsolidatedMember_UpperMember'
    """ 次年度期初から第２四半期間連結上限 """
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


class QuarterlyPeriod(Enum):
    """"四半期"""
    CURRENT_ACCUMULATED_Q1_INSTANT = 'CurrentAccumulatedQ1Instant'
    """ 当年度期初から第１四半期間時点 """
    CURRENT_ACCUMULATED_Q2_INSTANT = 'CurrentAccumulatedQ2Instant'
    """ 当年度期初から第２四半期間時点 """
    CURRENT_ACCUMULATED_Q3_INSTANT = 'CurrentAccumulatedQ3Instant'
    """ 当年度期初から第３四半期間時点 """


class RatioOfTotalAmountOfDividendsToNetAssets(Enum):
    """"純資産配当率"""
    CURRENT_YEAR_DURATION__ANNUAL_MEMBER__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_AnnualMember_ConsolidatedMember_ResultMember'
    """ 当年度会計期間年間連結実績 """
    CURRENT_YEAR_DURATION__ANNUAL_MEMBER__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_AnnualMember_NonConsolidatedMember_ResultMember'
    """ 当年度会計期間年間個別又は非連結実績 """
    PRIOR_YEAR_DURATION__ANNUAL_MEMBER__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearDuration_AnnualMember_ConsolidatedMember_ResultMember'
    """ 前年度会計期間年間連結実績 """
    PRIOR_YEAR_DURATION__ANNUAL_MEMBER__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearDuration_AnnualMember_NonConsolidatedMember_ResultMember'
    """ 前年度会計期間年間個別又は非連結実績 """


class Revenue(Enum):
    """"売上収益"""
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間連結実績 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_ForecastMember'
    """ 当年度会計期間連結予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_LowerMember'
    """ 当年度会計期間連結下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_UpperMember'
    """ 当年度会計期間連結上限 """
    PRIOR_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ2Duration_ConsolidatedMember_ResultMember'
    """ 前年度期初から第２四半期間連結実績 """


class TotalAssets(Enum):
    """"総資産"""
    CURRENT_ACCUMULATED_Q1_INSTANT__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ1Instant_ConsolidatedMember_ResultMember'
    """ 当年度期初から第１四半期間時点連結実績 """
    CURRENT_ACCUMULATED_Q1_INSTANT__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ1Instant_NonConsolidatedMember_ResultMember'
    """ 当年度期初から第１四半期間時点個別又は非連結実績 """
    CURRENT_ACCUMULATED_Q2_INSTANT__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Instant_ConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間時点連結実績 """
    CURRENT_ACCUMULATED_Q2_INSTANT__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ2Instant_NonConsolidatedMember_ResultMember'
    """ 当年度期初から第２四半期間時点個別又は非連結実績 """
    CURRENT_ACCUMULATED_Q3_INSTANT__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Instant_ConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間時点連結実績 """
    CURRENT_ACCUMULATED_Q3_INSTANT__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentAccumulatedQ3Instant_NonConsolidatedMember_ResultMember'
    """ 当年度期初から第３四半期間時点個別又は非連結実績 """
    CURRENT_YEAR_INSTANT__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearInstant_ConsolidatedMember_ResultMember'
    """ 当年度時点連結実績 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearInstant_NonConsolidatedMember_ResultMember'
    """ 当年度時点個別又は非連結実績 """
    PRIOR_YEAR_INSTANT__CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearInstant_ConsolidatedMember_ResultMember'
    """ 前年度時点連結実績 """
    PRIOR_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearInstant_NonConsolidatedMember_ResultMember'
    """ 前年度時点個別又は非連結実績 """


class TotalDividendPaidAnnual(Enum):
    """"配当金総額（合計）"""
    CURRENT_YEAR_DURATION__ANNUAL_MEMBER__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_AnnualMember_NonConsolidatedMember_ResultMember'
    """ 当年度会計期間年間個別又は非連結実績 """
    PRIOR_YEAR_DURATION__ANNUAL_MEMBER__NON_CONSOLIDATED_MEMBER__RESULT_MEMBER = 'PriorYearDuration_AnnualMember_NonConsolidatedMember_ResultMember'
    """ 前年度会計期間年間個別又は非連結実績 """


