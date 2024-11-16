from enum import Enum

class AmountChangeNetIncome(Enum):
    """"増減額、当期純利益"""
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度期初から第２四半期間連結今回予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度期初から第２四半期間連結今回下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度期初から第２四半期間連結今回上限 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度期初から第２四半期間個別又は非連結今回予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度期初から第２四半期間個別又は非連結今回下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度期初から第２四半期間個別又は非連結今回上限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度会計期間連結今回予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度会計期間連結今回下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度会計期間連結今回上限 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度会計期間個別又は非連結今回予想 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度会計期間個別又は非連結今回下限 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度会計期間個別又は非連結今回上限 """


class AmountChangeNetSales(Enum):
    """"増減額、売上高"""
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度期初から第２四半期間連結今回予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度期初から第２四半期間連結今回下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度期初から第２四半期間連結今回上限 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度期初から第２四半期間個別又は非連結今回予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度期初から第２四半期間個別又は非連結今回下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度期初から第２四半期間個別又は非連結今回上限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度会計期間連結今回予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度会計期間連結今回下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度会計期間連結今回上限 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度会計期間個別又は非連結今回予想 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度会計期間個別又は非連結今回下限 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度会計期間個別又は非連結今回上限 """


class AmountChangeOperatingIncome(Enum):
    """"増減額、営業利益"""
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度期初から第２四半期間連結今回予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度期初から第２四半期間連結今回下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度期初から第２四半期間連結今回上限 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度期初から第２四半期間個別又は非連結今回予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度期初から第２四半期間個別又は非連結今回下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度期初から第２四半期間個別又は非連結今回上限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度会計期間連結今回予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度会計期間連結今回下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度会計期間連結今回上限 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度会計期間個別又は非連結今回予想 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度会計期間個別又は非連結今回下限 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度会計期間個別又は非連結今回上限 """


class AmountChangeOperatingIncomeIFRS(Enum):
    """"増減額、営業利益、IFRS"""
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度会計期間連結今回予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度会計期間連結今回下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度会計期間連結今回上限 """


class AmountChangeOperatingRevenues(Enum):
    """"増減額、営業収益"""
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度会計期間個別又は非連結今回予想 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度会計期間個別又は非連結今回下限 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度会計期間個別又は非連結今回上限 """


class AmountChangeOrdinaryIncome(Enum):
    """"増減額、経常利益"""
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度期初から第２四半期間連結今回予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度期初から第２四半期間連結今回下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度期初から第２四半期間連結今回上限 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度期初から第２四半期間個別又は非連結今回予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度期初から第２四半期間個別又は非連結今回下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度期初から第２四半期間個別又は非連結今回上限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度会計期間連結今回予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度会計期間連結今回下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度会計期間連結今回上限 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度会計期間個別又は非連結今回予想 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度会計期間個別又は非連結今回下限 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度会計期間個別又は非連結今回上限 """


class AmountChangeOrdinaryRevenuesBK(Enum):
    """"増減額、経常収益、銀行"""
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度期初から第２四半期間連結今回予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度期初から第２四半期間連結今回下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度期初から第２四半期間連結今回上限 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度期初から第２四半期間個別又は非連結今回予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度期初から第２四半期間個別又は非連結今回下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度期初から第２四半期間個別又は非連結今回上限 """


class AmountChangeProfitAttributableToOwnersOfParent(Enum):
    """"増減額、親会社株主に帰属する当期純利益"""
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度期初から第２四半期間連結今回予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度期初から第２四半期間連結今回下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度期初から第２四半期間連結今回上限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度会計期間連結今回予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度会計期間連結今回下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度会計期間連結今回上限 """


class AmountChangeProfitAttributableToOwnersOfParentIFRS(Enum):
    """"増減額、親会社の所有者に帰属する当期利益、IFRS"""
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度期初から第２四半期間連結今回予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度期初から第２四半期間連結今回下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度期初から第２四半期間連結今回上限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度会計期間連結今回予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度会計期間連結今回下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度会計期間連結今回上限 """


class AmountChangeProfitBeforeTaxIFRS(Enum):
    """"増減額、税引前利益、IFRS"""
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度期初から第２四半期間連結今回予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度期初から第２四半期間連結今回下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度期初から第２四半期間連結今回上限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度会計期間連結今回予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度会計期間連結今回下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度会計期間連結今回上限 """


class AmountChangeProfitIFRS(Enum):
    """"増減額、当期利益、IFRS"""
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度会計期間連結今回予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度会計期間連結今回下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度会計期間連結今回上限 """


class AmountChangeRevenue(Enum):
    """"増減額、売上収益"""
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度期初から第２四半期間連結今回予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度期初から第２四半期間連結今回下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度期初から第２四半期間連結今回上限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度会計期間連結今回予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度会計期間連結今回下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度会計期間連結今回上限 """


class AmountChangeSalesIFRS(Enum):
    """"増減額、売上収益、IFRS"""
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度会計期間連結今回予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度会計期間連結今回下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度会計期間連結今回上限 """


class BasicEarningsPerShareIFRS(Enum):
    """"基本的1株当たり当期利益、IFRS"""
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度期初から第２四半期間連結今回予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度期初から第２四半期間連結今回下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度期初から第２四半期間連結今回上限 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_PreviousMember_ForecastMember'
    """ 当年度期初から第２四半期間連結前回予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_PreviousMember_LowerMember'
    """ 当年度期初から第２四半期間連結前回下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_PreviousMember_UpperMember'
    """ 当年度期初から第２四半期間連結前回上限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度会計期間連結今回予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度会計期間連結今回下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度会計期間連結今回上限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_PreviousMember_ForecastMember'
    """ 当年度会計期間連結前回予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_PreviousMember_LowerMember'
    """ 当年度会計期間連結前回下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_PreviousMember_UpperMember'
    """ 当年度会計期間連結前回上限 """
    PRIOR_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_ResultMember'
    """ 前年度期初から第２四半期間連結今回実績 """
    PRIOR_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__RESULT_MEMBER = 'PriorYearDuration_ConsolidatedMember_CurrentMember_ResultMember'
    """ 前年度会計期間連結今回実績 """


class ChangeInNetIncome(Enum):
    """"増減率、当期純利益"""
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度期初から第２四半期間連結今回予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度期初から第２四半期間連結今回下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度期初から第２四半期間連結今回上限 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度期初から第２四半期間個別又は非連結今回予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度期初から第２四半期間個別又は非連結今回下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度期初から第２四半期間個別又は非連結今回上限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度会計期間連結今回予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度会計期間連結今回下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度会計期間連結今回上限 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度会計期間個別又は非連結今回予想 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度会計期間個別又は非連結今回下限 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度会計期間個別又は非連結今回上限 """


class ChangeInNetSales(Enum):
    """"増減率、売上高"""
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度期初から第２四半期間連結今回予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度期初から第２四半期間連結今回下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度期初から第２四半期間連結今回上限 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度期初から第２四半期間個別又は非連結今回予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度期初から第２四半期間個別又は非連結今回下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度期初から第２四半期間個別又は非連結今回上限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度会計期間連結今回予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度会計期間連結今回下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度会計期間連結今回上限 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度会計期間個別又は非連結今回予想 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度会計期間個別又は非連結今回下限 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度会計期間個別又は非連結今回上限 """


class ChangeInOperatingIncome(Enum):
    """"増減率、営業利益"""
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度期初から第２四半期間連結今回予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度期初から第２四半期間連結今回下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度期初から第２四半期間連結今回上限 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度期初から第２四半期間個別又は非連結今回予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度期初から第２四半期間個別又は非連結今回下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度期初から第２四半期間個別又は非連結今回上限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度会計期間連結今回予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度会計期間連結今回下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度会計期間連結今回上限 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度会計期間個別又は非連結今回予想 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度会計期間個別又は非連結今回下限 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度会計期間個別又は非連結今回上限 """


class ChangeInOperatingIncomeIFRS(Enum):
    """"増減率、営業利益、IFRS"""
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度会計期間連結今回予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度会計期間連結今回下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度会計期間連結今回上限 """


class ChangeInOperatingRevenues(Enum):
    """"増減率、営業収益"""
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度会計期間個別又は非連結今回予想 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度会計期間個別又は非連結今回下限 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度会計期間個別又は非連結今回上限 """


class ChangeInOrdinaryIncome(Enum):
    """"増減率、経常利益"""
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度期初から第２四半期間連結今回予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度期初から第２四半期間連結今回下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度期初から第２四半期間連結今回上限 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度期初から第２四半期間個別又は非連結今回予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度期初から第２四半期間個別又は非連結今回下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度期初から第２四半期間個別又は非連結今回上限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度会計期間連結今回予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度会計期間連結今回下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度会計期間連結今回上限 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度会計期間個別又は非連結今回予想 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度会計期間個別又は非連結今回下限 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度会計期間個別又は非連結今回上限 """


class ChangeInOrdinaryRevenuesBK(Enum):
    """"増減率、経常収益、銀行"""
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度期初から第２四半期間連結今回予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度期初から第２四半期間連結今回下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度期初から第２四半期間連結今回上限 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度期初から第２四半期間個別又は非連結今回予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度期初から第２四半期間個別又は非連結今回下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度期初から第２四半期間個別又は非連結今回上限 """


class ChangeInProfitAttributableToOwnersOfParent(Enum):
    """"増減率、親会社株主に帰属する当期純利益"""
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度期初から第２四半期間連結今回予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度期初から第２四半期間連結今回下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度期初から第２四半期間連結今回上限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度会計期間連結今回予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度会計期間連結今回下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度会計期間連結今回上限 """


class ChangeInProfitAttributableToOwnersOfParentIFRS(Enum):
    """"増減率、親会社の所有者に帰属する当期利益、IFRS"""
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度期初から第２四半期間連結今回予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度期初から第２四半期間連結今回下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度期初から第２四半期間連結今回上限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度会計期間連結今回予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度会計期間連結今回下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度会計期間連結今回上限 """


class ChangeInProfitBeforeTaxIFRS(Enum):
    """"増減率、税引前利益、IFRS"""
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度期初から第２四半期間連結今回予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度期初から第２四半期間連結今回下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度期初から第２四半期間連結今回上限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度会計期間連結今回予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度会計期間連結今回下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度会計期間連結今回上限 """


class ChangeInProfitIFRS(Enum):
    """"増減率、当期利益、IFRS"""
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度会計期間連結今回予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度会計期間連結今回下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度会計期間連結今回上限 """


class ChangeInRevenue(Enum):
    """"増減率、売上収益"""
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度期初から第２四半期間連結今回予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度期初から第２四半期間連結今回下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度期初から第２四半期間連結今回上限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度会計期間連結今回予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度会計期間連結今回下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度会計期間連結今回上限 """


class ChangeInSalesIFRS(Enum):
    """"増減率、売上収益、IFRS"""
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度会計期間連結今回予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度会計期間連結今回下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度会計期間連結今回上限 """


class DividendPerShare(Enum):
    """"1株当たり配当金"""
    CURRENT_YEAR_DURATION__ANNUAL_MEMBER__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_AnnualMember_NonConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度会計期間年間個別又は非連結今回予想 """
    CURRENT_YEAR_DURATION__ANNUAL_MEMBER__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_AnnualMember_NonConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度会計期間年間個別又は非連結今回下限 """
    CURRENT_YEAR_DURATION__ANNUAL_MEMBER__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_AnnualMember_NonConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度会計期間年間個別又は非連結今回上限 """
    CURRENT_YEAR_DURATION__ANNUAL_MEMBER__NON_CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_AnnualMember_NonConsolidatedMember_PreviousMember_ForecastMember'
    """ 当年度会計期間年間個別又は非連結前回予想 """
    CURRENT_YEAR_DURATION__ANNUAL_MEMBER__NON_CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_AnnualMember_NonConsolidatedMember_PreviousMember_LowerMember'
    """ 当年度会計期間年間個別又は非連結前回下限 """
    CURRENT_YEAR_DURATION__ANNUAL_MEMBER__NON_CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_AnnualMember_NonConsolidatedMember_PreviousMember_UpperMember'
    """ 当年度会計期間年間個別又は非連結前回上限 """
    CURRENT_YEAR_DURATION__FIRST_QUARTER_MEMBER__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_FirstQuarterMember_NonConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度会計期間1Q個別又は非連結今回予想 """
    CURRENT_YEAR_DURATION__FIRST_QUARTER_MEMBER__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_FirstQuarterMember_NonConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度会計期間1Q個別又は非連結今回下限 """
    CURRENT_YEAR_DURATION__FIRST_QUARTER_MEMBER__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_FirstQuarterMember_NonConsolidatedMember_CurrentMember_ResultMember'
    """ 当年度会計期間1Q個別又は非連結今回実績 """
    CURRENT_YEAR_DURATION__FIRST_QUARTER_MEMBER__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_FirstQuarterMember_NonConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度会計期間1Q個別又は非連結今回上限 """
    CURRENT_YEAR_DURATION__FIRST_QUARTER_MEMBER__NON_CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_FirstQuarterMember_NonConsolidatedMember_PreviousMember_ForecastMember'
    """ 当年度会計期間1Q個別又は非連結前回予想 """
    CURRENT_YEAR_DURATION__FIRST_QUARTER_MEMBER__NON_CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_FirstQuarterMember_NonConsolidatedMember_PreviousMember_LowerMember'
    """ 当年度会計期間1Q個別又は非連結前回下限 """
    CURRENT_YEAR_DURATION__FIRST_QUARTER_MEMBER__NON_CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_FirstQuarterMember_NonConsolidatedMember_PreviousMember_UpperMember'
    """ 当年度会計期間1Q個別又は非連結前回上限 """
    CURRENT_YEAR_DURATION__SECOND_QUARTER_MEMBER__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_SecondQuarterMember_NonConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度会計期間2Q個別又は非連結今回予想 """
    CURRENT_YEAR_DURATION__SECOND_QUARTER_MEMBER__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_SecondQuarterMember_NonConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度会計期間2Q個別又は非連結今回下限 """
    CURRENT_YEAR_DURATION__SECOND_QUARTER_MEMBER__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_SecondQuarterMember_NonConsolidatedMember_CurrentMember_ResultMember'
    """ 当年度会計期間2Q個別又は非連結今回実績 """
    CURRENT_YEAR_DURATION__SECOND_QUARTER_MEMBER__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_SecondQuarterMember_NonConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度会計期間2Q個別又は非連結今回上限 """
    CURRENT_YEAR_DURATION__SECOND_QUARTER_MEMBER__NON_CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_SecondQuarterMember_NonConsolidatedMember_PreviousMember_ForecastMember'
    """ 当年度会計期間2Q個別又は非連結前回予想 """
    CURRENT_YEAR_DURATION__SECOND_QUARTER_MEMBER__NON_CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_SecondQuarterMember_NonConsolidatedMember_PreviousMember_LowerMember'
    """ 当年度会計期間2Q個別又は非連結前回下限 """
    CURRENT_YEAR_DURATION__SECOND_QUARTER_MEMBER__NON_CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_SecondQuarterMember_NonConsolidatedMember_PreviousMember_UpperMember'
    """ 当年度会計期間2Q個別又は非連結前回上限 """
    CURRENT_YEAR_DURATION__THIRD_QUARTER_MEMBER__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ThirdQuarterMember_NonConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度会計期間3Q個別又は非連結今回予想 """
    CURRENT_YEAR_DURATION__THIRD_QUARTER_MEMBER__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ThirdQuarterMember_NonConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度会計期間3Q個別又は非連結今回下限 """
    CURRENT_YEAR_DURATION__THIRD_QUARTER_MEMBER__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__RESULT_MEMBER = 'CurrentYearDuration_ThirdQuarterMember_NonConsolidatedMember_CurrentMember_ResultMember'
    """ 当年度会計期間3Q個別又は非連結今回実績 """
    CURRENT_YEAR_DURATION__THIRD_QUARTER_MEMBER__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ThirdQuarterMember_NonConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度会計期間3Q個別又は非連結今回上限 """
    CURRENT_YEAR_DURATION__THIRD_QUARTER_MEMBER__NON_CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ThirdQuarterMember_NonConsolidatedMember_PreviousMember_ForecastMember'
    """ 当年度会計期間3Q個別又は非連結前回予想 """
    CURRENT_YEAR_DURATION__THIRD_QUARTER_MEMBER__NON_CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ThirdQuarterMember_NonConsolidatedMember_PreviousMember_LowerMember'
    """ 当年度会計期間3Q個別又は非連結前回下限 """
    CURRENT_YEAR_DURATION__THIRD_QUARTER_MEMBER__NON_CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ThirdQuarterMember_NonConsolidatedMember_PreviousMember_UpperMember'
    """ 当年度会計期間3Q個別又は非連結前回上限 """
    CURRENT_YEAR_DURATION__YEAR_END_MEMBER__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_YearEndMember_NonConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度会計期間期末個別又は非連結今回予想 """
    CURRENT_YEAR_DURATION__YEAR_END_MEMBER__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_YearEndMember_NonConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度会計期間期末個別又は非連結今回下限 """
    CURRENT_YEAR_DURATION__YEAR_END_MEMBER__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_YearEndMember_NonConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度会計期間期末個別又は非連結今回上限 """
    CURRENT_YEAR_DURATION__YEAR_END_MEMBER__NON_CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_YearEndMember_NonConsolidatedMember_PreviousMember_ForecastMember'
    """ 当年度会計期間期末個別又は非連結前回予想 """
    CURRENT_YEAR_DURATION__YEAR_END_MEMBER__NON_CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_YearEndMember_NonConsolidatedMember_PreviousMember_LowerMember'
    """ 当年度会計期間期末個別又は非連結前回下限 """
    CURRENT_YEAR_DURATION__YEAR_END_MEMBER__NON_CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_YearEndMember_NonConsolidatedMember_PreviousMember_UpperMember'
    """ 当年度会計期間期末個別又は非連結前回上限 """
    PRIOR_YEAR_DURATION__ANNUAL_MEMBER__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__RESULT_MEMBER = 'PriorYearDuration_AnnualMember_NonConsolidatedMember_CurrentMember_ResultMember'
    """ 前年度会計期間年間個別又は非連結今回実績 """
    PRIOR_YEAR_DURATION__FIRST_QUARTER_MEMBER__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__RESULT_MEMBER = 'PriorYearDuration_FirstQuarterMember_NonConsolidatedMember_CurrentMember_ResultMember'
    """ 前年度会計期間1Q個別又は非連結今回実績 """
    PRIOR_YEAR_DURATION__SECOND_QUARTER_MEMBER__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__RESULT_MEMBER = 'PriorYearDuration_SecondQuarterMember_NonConsolidatedMember_CurrentMember_ResultMember'
    """ 前年度会計期間2Q個別又は非連結今回実績 """
    PRIOR_YEAR_DURATION__THIRD_QUARTER_MEMBER__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__RESULT_MEMBER = 'PriorYearDuration_ThirdQuarterMember_NonConsolidatedMember_CurrentMember_ResultMember'
    """ 前年度会計期間3Q個別又は非連結今回実績 """
    PRIOR_YEAR_DURATION__YEAR_END_MEMBER__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__RESULT_MEMBER = 'PriorYearDuration_YearEndMember_NonConsolidatedMember_CurrentMember_ResultMember'
    """ 前年度会計期間期末個別又は非連結今回実績 """


class NetIncome(Enum):
    """"当期純利益"""
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度期初から第２四半期間連結今回予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度期初から第２四半期間連結今回下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度期初から第２四半期間連結今回上限 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_PreviousMember_ForecastMember'
    """ 当年度期初から第２四半期間連結前回予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_PreviousMember_LowerMember'
    """ 当年度期初から第２四半期間連結前回下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_PreviousMember_UpperMember'
    """ 当年度期初から第２四半期間連結前回上限 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度期初から第２四半期間個別又は非連結今回予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度期初から第２四半期間個別又は非連結今回下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度期初から第２四半期間個別又は非連結今回上限 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_PreviousMember_ForecastMember'
    """ 当年度期初から第２四半期間個別又は非連結前回予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_PreviousMember_LowerMember'
    """ 当年度期初から第２四半期間個別又は非連結前回下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_PreviousMember_UpperMember'
    """ 当年度期初から第２四半期間個別又は非連結前回上限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度会計期間連結今回予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度会計期間連結今回下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度会計期間連結今回上限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_PreviousMember_ForecastMember'
    """ 当年度会計期間連結前回予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_PreviousMember_LowerMember'
    """ 当年度会計期間連結前回下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_PreviousMember_UpperMember'
    """ 当年度会計期間連結前回上限 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度会計期間個別又は非連結今回予想 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度会計期間個別又は非連結今回下限 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度会計期間個別又は非連結今回上限 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_PreviousMember_ForecastMember'
    """ 当年度会計期間個別又は非連結前回予想 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_PreviousMember_LowerMember'
    """ 当年度会計期間個別又は非連結前回下限 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_PreviousMember_UpperMember'
    """ 当年度会計期間個別又は非連結前回上限 """
    PRIOR_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_ResultMember'
    """ 前年度期初から第２四半期間連結今回実績 """
    PRIOR_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ2Duration_NonConsolidatedMember_CurrentMember_ResultMember'
    """ 前年度期初から第２四半期間個別又は非連結今回実績 """
    PRIOR_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__RESULT_MEMBER = 'PriorYearDuration_ConsolidatedMember_CurrentMember_ResultMember'
    """ 前年度会計期間連結今回実績 """
    PRIOR_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__RESULT_MEMBER = 'PriorYearDuration_NonConsolidatedMember_CurrentMember_ResultMember'
    """ 前年度会計期間個別又は非連結今回実績 """


class NetIncomePerShare(Enum):
    """"1株当たり当期純利益"""
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度期初から第２四半期間連結今回予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度期初から第２四半期間連結今回下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度期初から第２四半期間連結今回上限 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_PreviousMember_ForecastMember'
    """ 当年度期初から第２四半期間連結前回予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_PreviousMember_LowerMember'
    """ 当年度期初から第２四半期間連結前回下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_PreviousMember_UpperMember'
    """ 当年度期初から第２四半期間連結前回上限 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度期初から第２四半期間個別又は非連結今回予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度期初から第２四半期間個別又は非連結今回下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度期初から第２四半期間個別又は非連結今回上限 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_PreviousMember_ForecastMember'
    """ 当年度期初から第２四半期間個別又は非連結前回予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_PreviousMember_LowerMember'
    """ 当年度期初から第２四半期間個別又は非連結前回下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_PreviousMember_UpperMember'
    """ 当年度期初から第２四半期間個別又は非連結前回上限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度会計期間連結今回予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度会計期間連結今回下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度会計期間連結今回上限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_PreviousMember_ForecastMember'
    """ 当年度会計期間連結前回予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_PreviousMember_LowerMember'
    """ 当年度会計期間連結前回下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_PreviousMember_UpperMember'
    """ 当年度会計期間連結前回上限 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度会計期間個別又は非連結今回予想 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度会計期間個別又は非連結今回下限 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度会計期間個別又は非連結今回上限 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_PreviousMember_ForecastMember'
    """ 当年度会計期間個別又は非連結前回予想 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_PreviousMember_LowerMember'
    """ 当年度会計期間個別又は非連結前回下限 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_PreviousMember_UpperMember'
    """ 当年度会計期間個別又は非連結前回上限 """
    PRIOR_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_ResultMember'
    """ 前年度期初から第２四半期間連結今回実績 """
    PRIOR_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ2Duration_NonConsolidatedMember_CurrentMember_ResultMember'
    """ 前年度期初から第２四半期間個別又は非連結今回実績 """
    PRIOR_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__RESULT_MEMBER = 'PriorYearDuration_ConsolidatedMember_CurrentMember_ResultMember'
    """ 前年度会計期間連結今回実績 """
    PRIOR_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__RESULT_MEMBER = 'PriorYearDuration_NonConsolidatedMember_CurrentMember_ResultMember'
    """ 前年度会計期間個別又は非連結今回実績 """


class NetSales(Enum):
    """"売上高"""
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度期初から第２四半期間連結今回予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度期初から第２四半期間連結今回下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度期初から第２四半期間連結今回上限 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_PreviousMember_ForecastMember'
    """ 当年度期初から第２四半期間連結前回予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_PreviousMember_LowerMember'
    """ 当年度期初から第２四半期間連結前回下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_PreviousMember_UpperMember'
    """ 当年度期初から第２四半期間連結前回上限 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度期初から第２四半期間個別又は非連結今回予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度期初から第２四半期間個別又は非連結今回下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度期初から第２四半期間個別又は非連結今回上限 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_PreviousMember_ForecastMember'
    """ 当年度期初から第２四半期間個別又は非連結前回予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_PreviousMember_LowerMember'
    """ 当年度期初から第２四半期間個別又は非連結前回下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_PreviousMember_UpperMember'
    """ 当年度期初から第２四半期間個別又は非連結前回上限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度会計期間連結今回予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度会計期間連結今回下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度会計期間連結今回上限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_PreviousMember_ForecastMember'
    """ 当年度会計期間連結前回予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_PreviousMember_LowerMember'
    """ 当年度会計期間連結前回下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_PreviousMember_UpperMember'
    """ 当年度会計期間連結前回上限 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度会計期間個別又は非連結今回予想 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度会計期間個別又は非連結今回下限 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度会計期間個別又は非連結今回上限 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_PreviousMember_ForecastMember'
    """ 当年度会計期間個別又は非連結前回予想 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_PreviousMember_LowerMember'
    """ 当年度会計期間個別又は非連結前回下限 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_PreviousMember_UpperMember'
    """ 当年度会計期間個別又は非連結前回上限 """
    PRIOR_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_ResultMember'
    """ 前年度期初から第２四半期間連結今回実績 """
    PRIOR_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ2Duration_NonConsolidatedMember_CurrentMember_ResultMember'
    """ 前年度期初から第２四半期間個別又は非連結今回実績 """
    PRIOR_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__RESULT_MEMBER = 'PriorYearDuration_ConsolidatedMember_CurrentMember_ResultMember'
    """ 前年度会計期間連結今回実績 """
    PRIOR_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__RESULT_MEMBER = 'PriorYearDuration_NonConsolidatedMember_CurrentMember_ResultMember'
    """ 前年度会計期間個別又は非連結今回実績 """


class OperatingIncome(Enum):
    """"営業利益"""
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度期初から第２四半期間連結今回予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度期初から第２四半期間連結今回下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度期初から第２四半期間連結今回上限 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_PreviousMember_ForecastMember'
    """ 当年度期初から第２四半期間連結前回予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_PreviousMember_LowerMember'
    """ 当年度期初から第２四半期間連結前回下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_PreviousMember_UpperMember'
    """ 当年度期初から第２四半期間連結前回上限 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度期初から第２四半期間個別又は非連結今回予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度期初から第２四半期間個別又は非連結今回下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度期初から第２四半期間個別又は非連結今回上限 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_PreviousMember_ForecastMember'
    """ 当年度期初から第２四半期間個別又は非連結前回予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_PreviousMember_LowerMember'
    """ 当年度期初から第２四半期間個別又は非連結前回下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_PreviousMember_UpperMember'
    """ 当年度期初から第２四半期間個別又は非連結前回上限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度会計期間連結今回予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度会計期間連結今回下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度会計期間連結今回上限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_PreviousMember_ForecastMember'
    """ 当年度会計期間連結前回予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_PreviousMember_LowerMember'
    """ 当年度会計期間連結前回下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_PreviousMember_UpperMember'
    """ 当年度会計期間連結前回上限 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度会計期間個別又は非連結今回予想 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度会計期間個別又は非連結今回下限 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度会計期間個別又は非連結今回上限 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_PreviousMember_ForecastMember'
    """ 当年度会計期間個別又は非連結前回予想 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_PreviousMember_LowerMember'
    """ 当年度会計期間個別又は非連結前回下限 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_PreviousMember_UpperMember'
    """ 当年度会計期間個別又は非連結前回上限 """
    PRIOR_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_ResultMember'
    """ 前年度期初から第２四半期間連結今回実績 """
    PRIOR_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ2Duration_NonConsolidatedMember_CurrentMember_ResultMember'
    """ 前年度期初から第２四半期間個別又は非連結今回実績 """
    PRIOR_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__RESULT_MEMBER = 'PriorYearDuration_ConsolidatedMember_CurrentMember_ResultMember'
    """ 前年度会計期間連結今回実績 """
    PRIOR_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__RESULT_MEMBER = 'PriorYearDuration_NonConsolidatedMember_CurrentMember_ResultMember'
    """ 前年度会計期間個別又は非連結今回実績 """


class OperatingIncomeIFRS(Enum):
    """"営業利益、IFRS"""
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度会計期間連結今回予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度会計期間連結今回下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度会計期間連結今回上限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_PreviousMember_ForecastMember'
    """ 当年度会計期間連結前回予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_PreviousMember_LowerMember'
    """ 当年度会計期間連結前回下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_PreviousMember_UpperMember'
    """ 当年度会計期間連結前回上限 """
    PRIOR_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__RESULT_MEMBER = 'PriorYearDuration_ConsolidatedMember_CurrentMember_ResultMember'
    """ 前年度会計期間連結今回実績 """


class OperatingRevenues(Enum):
    """"営業収益"""
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度会計期間個別又は非連結今回予想 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度会計期間個別又は非連結今回下限 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度会計期間個別又は非連結今回上限 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_PreviousMember_ForecastMember'
    """ 当年度会計期間個別又は非連結前回予想 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_PreviousMember_LowerMember'
    """ 当年度会計期間個別又は非連結前回下限 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_PreviousMember_UpperMember'
    """ 当年度会計期間個別又は非連結前回上限 """
    PRIOR_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__RESULT_MEMBER = 'PriorYearDuration_NonConsolidatedMember_CurrentMember_ResultMember'
    """ 前年度会計期間個別又は非連結今回実績 """


class OrdinaryIncome(Enum):
    """"経常利益"""
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度期初から第２四半期間連結今回予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度期初から第２四半期間連結今回下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度期初から第２四半期間連結今回上限 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_PreviousMember_ForecastMember'
    """ 当年度期初から第２四半期間連結前回予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_PreviousMember_LowerMember'
    """ 当年度期初から第２四半期間連結前回下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_PreviousMember_UpperMember'
    """ 当年度期初から第２四半期間連結前回上限 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度期初から第２四半期間個別又は非連結今回予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度期初から第２四半期間個別又は非連結今回下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度期初から第２四半期間個別又は非連結今回上限 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_PreviousMember_ForecastMember'
    """ 当年度期初から第２四半期間個別又は非連結前回予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_PreviousMember_LowerMember'
    """ 当年度期初から第２四半期間個別又は非連結前回下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_PreviousMember_UpperMember'
    """ 当年度期初から第２四半期間個別又は非連結前回上限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度会計期間連結今回予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度会計期間連結今回下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度会計期間連結今回上限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_PreviousMember_ForecastMember'
    """ 当年度会計期間連結前回予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_PreviousMember_LowerMember'
    """ 当年度会計期間連結前回下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_PreviousMember_UpperMember'
    """ 当年度会計期間連結前回上限 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度会計期間個別又は非連結今回予想 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度会計期間個別又は非連結今回下限 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度会計期間個別又は非連結今回上限 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_PreviousMember_ForecastMember'
    """ 当年度会計期間個別又は非連結前回予想 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_PreviousMember_LowerMember'
    """ 当年度会計期間個別又は非連結前回下限 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_PreviousMember_UpperMember'
    """ 当年度会計期間個別又は非連結前回上限 """
    PRIOR_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_ResultMember'
    """ 前年度期初から第２四半期間連結今回実績 """
    PRIOR_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ2Duration_NonConsolidatedMember_CurrentMember_ResultMember'
    """ 前年度期初から第２四半期間個別又は非連結今回実績 """
    PRIOR_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__RESULT_MEMBER = 'PriorYearDuration_ConsolidatedMember_CurrentMember_ResultMember'
    """ 前年度会計期間連結今回実績 """
    PRIOR_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__RESULT_MEMBER = 'PriorYearDuration_NonConsolidatedMember_CurrentMember_ResultMember'
    """ 前年度会計期間個別又は非連結今回実績 """


class OrdinaryRevenuesBK(Enum):
    """"経常収益、銀行"""
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度期初から第２四半期間連結今回予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度期初から第２四半期間連結今回下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度期初から第２四半期間連結今回上限 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_PreviousMember_ForecastMember'
    """ 当年度期初から第２四半期間連結前回予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_PreviousMember_LowerMember'
    """ 当年度期初から第２四半期間連結前回下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_PreviousMember_UpperMember'
    """ 当年度期初から第２四半期間連結前回上限 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度期初から第２四半期間個別又は非連結今回予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度期初から第２四半期間個別又は非連結今回下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度期初から第２四半期間個別又は非連結今回上限 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_PreviousMember_ForecastMember'
    """ 当年度期初から第２四半期間個別又は非連結前回予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_PreviousMember_LowerMember'
    """ 当年度期初から第２四半期間個別又は非連結前回下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_NonConsolidatedMember_PreviousMember_UpperMember'
    """ 当年度期初から第２四半期間個別又は非連結前回上限 """
    PRIOR_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_ResultMember'
    """ 前年度期初から第２四半期間連結今回実績 """
    PRIOR_ACCUMULATED_Q2_DURATION__NON_CONSOLIDATED_MEMBER__CURRENT_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ2Duration_NonConsolidatedMember_CurrentMember_ResultMember'
    """ 前年度期初から第２四半期間個別又は非連結今回実績 """


class ProfitAttributableToOwnersOfParent(Enum):
    """"親会社株主に帰属する当期純利益"""
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度期初から第２四半期間連結今回予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度期初から第２四半期間連結今回下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度期初から第２四半期間連結今回上限 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_PreviousMember_ForecastMember'
    """ 当年度期初から第２四半期間連結前回予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_PreviousMember_LowerMember'
    """ 当年度期初から第２四半期間連結前回下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_PreviousMember_UpperMember'
    """ 当年度期初から第２四半期間連結前回上限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度会計期間連結今回予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度会計期間連結今回下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度会計期間連結今回上限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_PreviousMember_ForecastMember'
    """ 当年度会計期間連結前回予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_PreviousMember_LowerMember'
    """ 当年度会計期間連結前回下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_PreviousMember_UpperMember'
    """ 当年度会計期間連結前回上限 """
    PRIOR_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_ResultMember'
    """ 前年度期初から第２四半期間連結今回実績 """
    PRIOR_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__RESULT_MEMBER = 'PriorYearDuration_ConsolidatedMember_CurrentMember_ResultMember'
    """ 前年度会計期間連結今回実績 """


class ProfitAttributableToOwnersOfParentIFRS(Enum):
    """"親会社の所有者に帰属する当期利益、IFRS"""
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度期初から第２四半期間連結今回予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度期初から第２四半期間連結今回下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度期初から第２四半期間連結今回上限 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_PreviousMember_ForecastMember'
    """ 当年度期初から第２四半期間連結前回予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_PreviousMember_LowerMember'
    """ 当年度期初から第２四半期間連結前回下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_PreviousMember_UpperMember'
    """ 当年度期初から第２四半期間連結前回上限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度会計期間連結今回予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度会計期間連結今回下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度会計期間連結今回上限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_PreviousMember_ForecastMember'
    """ 当年度会計期間連結前回予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_PreviousMember_LowerMember'
    """ 当年度会計期間連結前回下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_PreviousMember_UpperMember'
    """ 当年度会計期間連結前回上限 """
    PRIOR_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_ResultMember'
    """ 前年度期初から第２四半期間連結今回実績 """
    PRIOR_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__RESULT_MEMBER = 'PriorYearDuration_ConsolidatedMember_CurrentMember_ResultMember'
    """ 前年度会計期間連結今回実績 """


class ProfitBeforeTaxIFRS(Enum):
    """"税引前利益、IFRS"""
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度期初から第２四半期間連結今回予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度期初から第２四半期間連結今回下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度期初から第２四半期間連結今回上限 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_PreviousMember_ForecastMember'
    """ 当年度期初から第２四半期間連結前回予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_PreviousMember_LowerMember'
    """ 当年度期初から第２四半期間連結前回下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_PreviousMember_UpperMember'
    """ 当年度期初から第２四半期間連結前回上限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度会計期間連結今回予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度会計期間連結今回下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度会計期間連結今回上限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_PreviousMember_ForecastMember'
    """ 当年度会計期間連結前回予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_PreviousMember_LowerMember'
    """ 当年度会計期間連結前回下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_PreviousMember_UpperMember'
    """ 当年度会計期間連結前回上限 """
    PRIOR_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_ResultMember'
    """ 前年度期初から第２四半期間連結今回実績 """
    PRIOR_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__RESULT_MEMBER = 'PriorYearDuration_ConsolidatedMember_CurrentMember_ResultMember'
    """ 前年度会計期間連結今回実績 """


class ProfitIFRS(Enum):
    """"当期利益、IFRS"""
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度会計期間連結今回予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度会計期間連結今回下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度会計期間連結今回上限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_PreviousMember_ForecastMember'
    """ 当年度会計期間連結前回予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_PreviousMember_LowerMember'
    """ 当年度会計期間連結前回下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_PreviousMember_UpperMember'
    """ 当年度会計期間連結前回上限 """
    PRIOR_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__RESULT_MEMBER = 'PriorYearDuration_ConsolidatedMember_CurrentMember_ResultMember'
    """ 前年度会計期間連結今回実績 """


class Revenue(Enum):
    """"売上収益"""
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度期初から第２四半期間連結今回予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度期初から第２四半期間連結今回下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度期初から第２四半期間連結今回上限 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__FORECAST_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_PreviousMember_ForecastMember'
    """ 当年度期初から第２四半期間連結前回予想 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__LOWER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_PreviousMember_LowerMember'
    """ 当年度期初から第２四半期間連結前回下限 """
    CURRENT_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__UPPER_MEMBER = 'CurrentAccumulatedQ2Duration_ConsolidatedMember_PreviousMember_UpperMember'
    """ 当年度期初から第２四半期間連結前回上限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度会計期間連結今回予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度会計期間連結今回下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度会計期間連結今回上限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_PreviousMember_ForecastMember'
    """ 当年度会計期間連結前回予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_PreviousMember_LowerMember'
    """ 当年度会計期間連結前回下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_PreviousMember_UpperMember'
    """ 当年度会計期間連結前回上限 """
    PRIOR_ACCUMULATED_Q2_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__RESULT_MEMBER = 'PriorAccumulatedQ2Duration_ConsolidatedMember_CurrentMember_ResultMember'
    """ 前年度期初から第２四半期間連結今回実績 """
    PRIOR_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__RESULT_MEMBER = 'PriorYearDuration_ConsolidatedMember_CurrentMember_ResultMember'
    """ 前年度会計期間連結今回実績 """


class SalesIFRS(Enum):
    """"売上収益、IFRS"""
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_ForecastMember'
    """ 当年度会計期間連結今回予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_LowerMember'
    """ 当年度会計期間連結今回下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_CurrentMember_UpperMember'
    """ 当年度会計期間連結今回上限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__FORECAST_MEMBER = 'CurrentYearDuration_ConsolidatedMember_PreviousMember_ForecastMember'
    """ 当年度会計期間連結前回予想 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__LOWER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_PreviousMember_LowerMember'
    """ 当年度会計期間連結前回下限 """
    CURRENT_YEAR_DURATION__CONSOLIDATED_MEMBER__PREVIOUS_MEMBER__UPPER_MEMBER = 'CurrentYearDuration_ConsolidatedMember_PreviousMember_UpperMember'
    """ 当年度会計期間連結前回上限 """
    PRIOR_YEAR_DURATION__CONSOLIDATED_MEMBER__CURRENT_MEMBER__RESULT_MEMBER = 'PriorYearDuration_ConsolidatedMember_CurrentMember_ResultMember'
    """ 前年度会計期間連結今回実績 """


