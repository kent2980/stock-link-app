from enum import Enum

class DepreciationSegmentInformation(Enum):
    """"減価償却費、セグメント情報"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__OTHER_REPORTABLE_SEGMENTS_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_OtherReportableSegmentsMember'
    """ 当年度会計期間個別又は非連結その他 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RECONCILING_ITEMS_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_ReconcilingItemsMember'
    """ 当年度会計期間個別又は非連結調整項目 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__REPORTABLE_SEGMENTS_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_ReportableSegmentsMember'
    """ 当年度会計期間個別又は非連結報告セグメント """
    CURRENT_YEAR_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'CurrentYearDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ 当年度会計期間その他 """
    CURRENT_YEAR_DURATION__RECONCILING_ITEMS_MEMBER = 'CurrentYearDuration_ReconcilingItemsMember'
    """ 当年度会計期間調整項目 """
    CURRENT_YEAR_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'CurrentYearDuration_ReportableSegmentsMember'
    """ 当年度会計期間報告セグメント """
    CURRENT_YEAR_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'CurrentYearDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 当年度会計期間事業セグメント合計 """
    INTERIM_DURATION = 'InterimDuration'
    INTERIM_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'InterimDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    INTERIM_DURATION__RECONCILING_ITEMS_MEMBER = 'InterimDuration_ReconcilingItemsMember'
    """ 調整項目 """
    INTERIM_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'InterimDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    INTERIM_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'InterimDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_INTERIM_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'Prior1InterimDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    PRIOR1_INTERIM_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1InterimDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_INTERIM_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'Prior1InterimDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    PRIOR1_INTERIM_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1InterimDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__OTHER_REPORTABLE_SEGMENTS_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_OtherReportableSegmentsMember'
    """ 個別又は非連結その他 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RECONCILING_ITEMS_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_ReconcilingItemsMember'
    """ 個別又は非連結調整項目 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__REPORTABLE_SEGMENTS_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_ReportableSegmentsMember'
    """ 個別又は非連結報告セグメント """
    PRIOR1_YEAR_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'Prior1YearDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    PRIOR1_YEAR_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1YearDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_YEAR_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'Prior1YearDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    PRIOR1_YEAR_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1YearDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """


class EquityInEarningsLossesOfAffiliates(Enum):
    """"持分法投資利益又は損失（△）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'CurrentYTDDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    CURRENT_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'CurrentYTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    CURRENT_YTD_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'CurrentYTDDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    CURRENT_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'CurrentYTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    INTERIM_DURATION = 'InterimDuration'
    INTERIM_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'InterimDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    INTERIM_DURATION__RECONCILING_ITEMS_MEMBER = 'InterimDuration_ReconcilingItemsMember'
    """ 調整項目 """
    INTERIM_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'InterimDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    INTERIM_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'InterimDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_INTERIM_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'Prior1InterimDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    PRIOR1_INTERIM_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1InterimDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_INTERIM_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'Prior1InterimDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    PRIOR1_INTERIM_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1InterimDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'Prior1YTDDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    PRIOR1_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1YTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_YTD_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'Prior1YTDDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    PRIOR1_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1YTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """


class GoodwillBeforeOffsetting(Enum):
    """"のれん（相殺前）"""
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__REPORTABLE_SEGMENTS_MEMBER = 'CurrentYearInstant_ReportableSegmentsMember'
    """ 当年度時点報告セグメント """
    CURRENT_YEAR_INSTANT__UNALLOCATED_AMOUNTS_AND_ELIMINATION_MEMBER = 'CurrentYearInstant_UnallocatedAmountsAndEliminationMember'
    """ 当年度時点全社・消去 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__REPORTABLE_SEGMENTS_MEMBER = 'Prior1YearInstant_ReportableSegmentsMember'
    """ 報告セグメント """
    PRIOR1_YEAR_INSTANT__UNALLOCATED_AMOUNTS_AND_ELIMINATION_MEMBER = 'Prior1YearInstant_UnallocatedAmountsAndEliminationMember'
    """ 全社・消去 """


class IncomeTaxExpense(Enum):
    """"税金費用"""
    INTERIM_DURATION = 'InterimDuration'
    INTERIM_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'InterimDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    INTERIM_DURATION__RECONCILING_ITEMS_MEMBER = 'InterimDuration_ReconcilingItemsMember'
    """ 調整項目 """
    INTERIM_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'InterimDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    INTERIM_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'InterimDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_INTERIM_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'Prior1InterimDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    PRIOR1_INTERIM_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1InterimDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_INTERIM_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'Prior1InterimDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    PRIOR1_INTERIM_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1InterimDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """


class IncreaseInPropertyPlantAndEquipmentAndIntangibleAssets(Enum):
    """"有形固定資産及び無形固定資産の増加額"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__OTHER_REPORTABLE_SEGMENTS_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_OtherReportableSegmentsMember'
    """ 当年度会計期間個別又は非連結その他 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RECONCILING_ITEMS_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_ReconcilingItemsMember'
    """ 当年度会計期間個別又は非連結調整項目 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__REPORTABLE_SEGMENTS_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_ReportableSegmentsMember'
    """ 当年度会計期間個別又は非連結報告セグメント """
    CURRENT_YEAR_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'CurrentYearDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ 当年度会計期間その他 """
    CURRENT_YEAR_DURATION__RECONCILING_ITEMS_MEMBER = 'CurrentYearDuration_ReconcilingItemsMember'
    """ 当年度会計期間調整項目 """
    CURRENT_YEAR_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'CurrentYearDuration_ReportableSegmentsMember'
    """ 当年度会計期間報告セグメント """
    CURRENT_YEAR_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'CurrentYearDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 当年度会計期間事業セグメント合計 """
    INTERIM_DURATION = 'InterimDuration'
    INTERIM_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'InterimDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    INTERIM_DURATION__RECONCILING_ITEMS_MEMBER = 'InterimDuration_ReconcilingItemsMember'
    """ 調整項目 """
    INTERIM_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'InterimDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    INTERIM_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'InterimDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_INTERIM_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'Prior1InterimDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    PRIOR1_INTERIM_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1InterimDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_INTERIM_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'Prior1InterimDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    PRIOR1_INTERIM_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1InterimDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__OTHER_REPORTABLE_SEGMENTS_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_OtherReportableSegmentsMember'
    """ 個別又は非連結その他 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RECONCILING_ITEMS_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_ReconcilingItemsMember'
    """ 個別又は非連結調整項目 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__REPORTABLE_SEGMENTS_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_ReportableSegmentsMember'
    """ 個別又は非連結報告セグメント """
    PRIOR1_YEAR_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'Prior1YearDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    PRIOR1_YEAR_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1YearDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_YEAR_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'Prior1YearDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    PRIOR1_YEAR_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1YearDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """


class InvestmentsInEntitiesAccountedForUsingEquityMethod(Enum):
    """"持分法適用会社への投資額"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'CurrentYTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    CURRENT_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'CurrentYTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'CurrentYearDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ 当年度会計期間その他 """
    CURRENT_YEAR_DURATION__RECONCILING_ITEMS_MEMBER = 'CurrentYearDuration_ReconcilingItemsMember'
    """ 当年度会計期間調整項目 """
    CURRENT_YEAR_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'CurrentYearDuration_ReportableSegmentsMember'
    """ 当年度会計期間報告セグメント """
    CURRENT_YEAR_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'CurrentYearDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 当年度会計期間事業セグメント合計 """
    INTERIM_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'InterimDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    INTERIM_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'InterimDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    INTERIM_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'InterimDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    PRIOR1_INTERIM_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'Prior1InterimDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    PRIOR1_INTERIM_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'Prior1InterimDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    PRIOR1_INTERIM_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1InterimDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1YTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1YTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'Prior1YearDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    PRIOR1_YEAR_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1YearDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_YEAR_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'Prior1YearDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    PRIOR1_YEAR_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1YearDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """


class ResearchAndDevelopmentExpensesIncludedInGeneralAndAdministrativeExpensesAndManufacturingCostForCurrentPeriod(Enum):
    """"一般管理費及び当期製造費用に含まれる研究開発費"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class RevenuesFromExternalCustomers(Enum):
    """"外部顧客への売上高"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ 個別又は非連結その他 """
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER__OTHER_REPORTABLE_SEGMENTS_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember_OtherReportableSegmentsMember'
    """ 個別又は非連結その他 """
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER__RECONCILING_ITEMS_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember_ReconcilingItemsMember'
    """ 個別又は非連結調整項目 """
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER__REPORTABLE_SEGMENTS_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember_ReportableSegmentsMember'
    """ 個別又は非連結報告セグメント """
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember_TotalOfReportableSegmentsAndOthersMember'
    """ 個別又は非連結事業セグメント合計 """
    CURRENT_YTD_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'CurrentYTDDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    CURRENT_YTD_DURATION__OTHER_REPORTABLE_SEGMENTS_MEMBER = 'CurrentYTDDuration_OtherReportableSegmentsMember'
    """ その他 """
    CURRENT_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'CurrentYTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    CURRENT_YTD_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'CurrentYTDDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    CURRENT_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'CurrentYTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__OTHER_REPORTABLE_SEGMENTS_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_OtherReportableSegmentsMember'
    """ 当年度会計期間個別又は非連結その他 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RECONCILING_ITEMS_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_ReconcilingItemsMember'
    """ 当年度会計期間個別又は非連結調整項目 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__REPORTABLE_SEGMENTS_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_ReportableSegmentsMember'
    """ 当年度会計期間個別又は非連結報告セグメント """
    CURRENT_YEAR_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'CurrentYearDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ 当年度会計期間その他 """
    CURRENT_YEAR_DURATION__OTHER_REPORTABLE_SEGMENTS_MEMBER = 'CurrentYearDuration_OtherReportableSegmentsMember'
    """ 当年度会計期間その他 """
    CURRENT_YEAR_DURATION__RECONCILING_ITEMS_MEMBER = 'CurrentYearDuration_ReconcilingItemsMember'
    """ 当年度会計期間調整項目 """
    CURRENT_YEAR_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'CurrentYearDuration_ReportableSegmentsMember'
    """ 当年度会計期間報告セグメント """
    CURRENT_YEAR_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'CurrentYearDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 当年度会計期間事業セグメント合計 """
    INTERIM_DURATION = 'InterimDuration'
    INTERIM_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'InterimDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    INTERIM_DURATION__RECONCILING_ITEMS_MEMBER = 'InterimDuration_ReconcilingItemsMember'
    """ 調整項目 """
    INTERIM_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'InterimDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    INTERIM_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'InterimDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_INTERIM_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'Prior1InterimDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    PRIOR1_INTERIM_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1InterimDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_INTERIM_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'Prior1InterimDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    PRIOR1_INTERIM_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1InterimDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ 個別又は非連結その他 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER__RECONCILING_ITEMS_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember_ReconcilingItemsMember'
    """ 個別又は非連結調整項目 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER__REPORTABLE_SEGMENTS_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember_ReportableSegmentsMember'
    """ 個別又は非連結報告セグメント """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember_TotalOfReportableSegmentsAndOthersMember'
    """ 個別又は非連結事業セグメント合計 """
    PRIOR1_YTD_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'Prior1YTDDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    PRIOR1_YTD_DURATION__OTHER_REPORTABLE_SEGMENTS_MEMBER = 'Prior1YTDDuration_OtherReportableSegmentsMember'
    """ その他 """
    PRIOR1_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1YTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_YTD_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'Prior1YTDDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    PRIOR1_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1YTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__OTHER_REPORTABLE_SEGMENTS_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_OtherReportableSegmentsMember'
    """ 個別又は非連結その他 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RECONCILING_ITEMS_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_ReconcilingItemsMember'
    """ 個別又は非連結調整項目 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__REPORTABLE_SEGMENTS_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_ReportableSegmentsMember'
    """ 個別又は非連結報告セグメント """
    PRIOR1_YEAR_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'Prior1YearDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    PRIOR1_YEAR_DURATION__OTHER_REPORTABLE_SEGMENTS_MEMBER = 'Prior1YearDuration_OtherReportableSegmentsMember'
    """ その他 """
    PRIOR1_YEAR_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1YearDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_YEAR_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'Prior1YearDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    PRIOR1_YEAR_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1YearDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """


class TransactionsWithOtherSegments(Enum):
    """"セグメント間の内部売上高又は振替高"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ 個別又は非連結その他 """
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER__OTHER_REPORTABLE_SEGMENTS_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember_OtherReportableSegmentsMember'
    """ 個別又は非連結その他 """
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER__RECONCILING_ITEMS_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember_ReconcilingItemsMember'
    """ 個別又は非連結調整項目 """
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER__REPORTABLE_SEGMENTS_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember_ReportableSegmentsMember'
    """ 個別又は非連結報告セグメント """
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember_TotalOfReportableSegmentsAndOthersMember'
    """ 個別又は非連結事業セグメント合計 """
    CURRENT_YTD_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'CurrentYTDDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    CURRENT_YTD_DURATION__OTHER_REPORTABLE_SEGMENTS_MEMBER = 'CurrentYTDDuration_OtherReportableSegmentsMember'
    """ その他 """
    CURRENT_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'CurrentYTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    CURRENT_YTD_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'CurrentYTDDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    CURRENT_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'CurrentYTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__OTHER_REPORTABLE_SEGMENTS_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_OtherReportableSegmentsMember'
    """ 当年度会計期間個別又は非連結その他 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RECONCILING_ITEMS_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_ReconcilingItemsMember'
    """ 当年度会計期間個別又は非連結調整項目 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__REPORTABLE_SEGMENTS_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_ReportableSegmentsMember'
    """ 当年度会計期間個別又は非連結報告セグメント """
    CURRENT_YEAR_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'CurrentYearDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ 当年度会計期間その他 """
    CURRENT_YEAR_DURATION__OTHER_REPORTABLE_SEGMENTS_MEMBER = 'CurrentYearDuration_OtherReportableSegmentsMember'
    """ 当年度会計期間その他 """
    CURRENT_YEAR_DURATION__RECONCILING_ITEMS_MEMBER = 'CurrentYearDuration_ReconcilingItemsMember'
    """ 当年度会計期間調整項目 """
    CURRENT_YEAR_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'CurrentYearDuration_ReportableSegmentsMember'
    """ 当年度会計期間報告セグメント """
    CURRENT_YEAR_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'CurrentYearDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 当年度会計期間事業セグメント合計 """
    INTERIM_DURATION = 'InterimDuration'
    INTERIM_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'InterimDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    INTERIM_DURATION__RECONCILING_ITEMS_MEMBER = 'InterimDuration_ReconcilingItemsMember'
    """ 調整項目 """
    INTERIM_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'InterimDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    INTERIM_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'InterimDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_INTERIM_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'Prior1InterimDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    PRIOR1_INTERIM_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1InterimDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_INTERIM_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'Prior1InterimDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    PRIOR1_INTERIM_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1InterimDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ 個別又は非連結その他 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER__RECONCILING_ITEMS_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember_ReconcilingItemsMember'
    """ 個別又は非連結調整項目 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER__REPORTABLE_SEGMENTS_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember_ReportableSegmentsMember'
    """ 個別又は非連結報告セグメント """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember_TotalOfReportableSegmentsAndOthersMember'
    """ 個別又は非連結事業セグメント合計 """
    PRIOR1_YTD_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'Prior1YTDDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    PRIOR1_YTD_DURATION__OTHER_REPORTABLE_SEGMENTS_MEMBER = 'Prior1YTDDuration_OtherReportableSegmentsMember'
    """ その他 """
    PRIOR1_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1YTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_YTD_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'Prior1YTDDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    PRIOR1_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1YTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__OTHER_REPORTABLE_SEGMENTS_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_OtherReportableSegmentsMember'
    """ 個別又は非連結その他 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RECONCILING_ITEMS_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_ReconcilingItemsMember'
    """ 個別又は非連結調整項目 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__REPORTABLE_SEGMENTS_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_ReportableSegmentsMember'
    """ 個別又は非連結報告セグメント """
    PRIOR1_YEAR_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'Prior1YearDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    PRIOR1_YEAR_DURATION__OTHER_REPORTABLE_SEGMENTS_MEMBER = 'Prior1YearDuration_OtherReportableSegmentsMember'
    """ その他 """
    PRIOR1_YEAR_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1YearDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_YEAR_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'Prior1YearDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    PRIOR1_YEAR_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1YearDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """


class NumberOfSubmissionDEI(Enum):
    """"提出回数、DEI"""
    FILING_DATE_INSTANT = 'FilingDateInstant'


class AcceptancesAndGuaranteesLiabilitiesBNK(Enum):
    """"支払承諾、負債の部、銀行業"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    INTERIM_INSTANT = 'InterimInstant'
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class AccountsPayableConsignment(Enum):
    """"受託販売未払金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class AccountsPayableFacilities(Enum):
    """"設備関係未払金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class AccountsPayableForConstructionContractsCNS(Enum):
    """"工事未払金、建設業"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class AccountsPayableOther(Enum):
    """"未払金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class AccountsPayableOtherAndAccruedExpenses(Enum):
    """"未払金及び未払費用"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class AccountsPayableRealEstate(Enum):
    """"不動産事業未払金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class AccountsPayableTrade(Enum):
    """"買掛金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class AccountsReceivableAssetsINS(Enum):
    """"未収金、資産の部、保険業"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class AccountsReceivableFromCompletedConstructionContractsCNS(Enum):
    """"完成工事未収入金、建設業"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class AccountsReceivableInstallment(Enum):
    """"割賦売掛金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class AccountsReceivableInstallmentSalesCALEA(Enum):
    """"割賦債権、流動資産、リース事業"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class AccountsReceivableLeaseCALEA(Enum):
    """"賃貸料等未収入金、流動資産、リース事業"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class AccountsReceivableOperatingLoansCALEA(Enum):
    """"営業貸付金、流動資産、リース事業"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class AccountsReceivableOther(Enum):
    """"未収入金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class AccountsReceivableOtherLoansToCustomersCALEA(Enum):
    """"その他の営業貸付債権、流動資産、リース事業"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class AccountsReceivableTrade(Enum):
    """"売掛金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class AccountsReceivableTradeAndContractAssets(Enum):
    """"売掛金及び契約資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class AccruedAlcoholTax(Enum):
    """"未払酒税"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class AccruedBusinessOfficeTaxes(Enum):
    """"未払事業所税"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class AccruedConsumptionTaxes(Enum):
    """"未払消費税等"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class AccruedExpenses(Enum):
    """"未払費用"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class AccruedIncome(Enum):
    """"未収収益"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class AccruedPremiumsAssetsINS(Enum):
    """"未収保険料、資産の部、保険業"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class AccumulatedDepreciationAndImpairmentLossBuildingsAndStructures(Enum):
    """"減価償却累計額及び減損損失累計額、建物及び構築物"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class AccumulatedDepreciationAndImpairmentLossLeaseAssetsPPE(Enum):
    """"減価償却累計額及び減損損失累計額、リース資産、有形固定資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class AccumulatedDepreciationAndImpairmentLossMachineryEquipmentAndVehicles(Enum):
    """"減価償却累計額及び減損損失累計額、機械装置及び運搬具"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class AccumulatedDepreciationAndImpairmentLossOtherPPE(Enum):
    """"減価償却累計額及び減損損失累計額、その他、有形固定資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class AccumulatedDepreciationAndImpairmentLossPPEByGroup(Enum):
    """"減価償却累計額及び減損損失累計額、有形固定資産、一括控除"""
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class AccumulatedDepreciationAndImpairmentLossRealEstateForInvestment(Enum):
    """"減価償却累計額及び減損損失累計額、投資不動産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class AccumulatedDepreciationAndImpairmentLossToolsFurnitureAndFixtures(Enum):
    """"減価償却累計額及び減損損失累計額、工具、器具及び備品"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class AccumulatedDepreciationBuildings(Enum):
    """"減価償却累計額、建物"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class AccumulatedDepreciationBuildingsAndStructures(Enum):
    """"減価償却累計額、建物及び構築物"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class AccumulatedDepreciationLeaseAssetsPPE(Enum):
    """"減価償却累計額、リース資産、有形固定資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class AccumulatedDepreciationMachineryAndEquipment(Enum):
    """"減価償却累計額、機械及び装置"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class AccumulatedDepreciationMachineryEquipmentAndVehicles(Enum):
    """"減価償却累計額、機械装置及び運搬具"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class AccumulatedDepreciationOtherPPE(Enum):
    """"減価償却累計額、その他、有形固定資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class AccumulatedDepreciationPPEByGroup(Enum):
    """"減価償却累計額、有形固定資産、一括控除"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class AccumulatedDepreciationRealEstateForInvestment(Enum):
    """"減価償却累計額、投資不動産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class AccumulatedDepreciationRightOfUseAssets(Enum):
    """"減価償却累計額、使用権資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class AccumulatedDepreciationStructures(Enum):
    """"減価償却累計額、構築物"""
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class AccumulatedDepreciationToolsFurnitureAndFixtures(Enum):
    """"減価償却累計額、工具、器具及び備品"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class AccumulatedDepreciationVehicles(Enum):
    """"減価償却累計額、車両運搬具"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class AccumulatedDepreciationVessels(Enum):
    """"減価償却累計額、船舶"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class AccumulatedImpairmentLossBuildingsAndStructures(Enum):
    """"減損損失累計額、建物及び構築物"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class AccumulatedImpairmentLossMachineryEquipmentAndVehicles(Enum):
    """"減損損失累計額、機械装置及び運搬具"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class AccumulatedImpairmentLossOtherPPE(Enum):
    """"減損損失累計額、その他、有形固定資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class AdvancePaymentsOther(Enum):
    """"前払金"""
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class AdvancePaymentsTrade(Enum):
    """"前渡金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class AdvancesForPurchasesAtLeasedAssetsPPELEA(Enum):
    """"賃貸資産前渡金、有形固定資産、リース事業"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class AdvancesPaid(Enum):
    """"立替金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class AdvancesReceived(Enum):
    """"前受金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class AdvancesReceivedOnUncompletedConstructionContractsCNS(Enum):
    """"未成工事受入金、建設業"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class AdvertisingAndPromotionExpensesSGA(Enum):
    """"広告宣伝費及び販売促進費、販売費及び一般管理費"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class AdvertisingExpensesSGA(Enum):
    """"広告宣伝費、販売費及び一般管理費"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class AgentFeeSGA(Enum):
    """"代理店手数料、販売費及び一般管理費"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class AllowanceForDoubtfulAccountsAssetsINS(Enum):
    """"貸倒引当金、資産の部、保険業"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class AllowanceForDoubtfulAccountsCA(Enum):
    """"貸倒引当金、流動資産、一括控除"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class AllowanceForDoubtfulAccountsIOAByGroup(Enum):
    """"貸倒引当金、投資その他の資産、一括控除"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class AllowanceForInvestmentLoss(Enum):
    """"投資損失引当金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class AllowanceForInvestmentLossAssetsBNK(Enum):
    """"投資損失引当金、資産の部、銀行業"""
    INTERIM_INSTANT = 'InterimInstant'
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class AllowanceForLoanLossesAssetsBNK(Enum):
    """"貸倒引当金、資産の部、銀行業"""
    INTERIM_INSTANT = 'InterimInstant'
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class AmortizationOfBondIssuanceCostNOE(Enum):
    """"社債発行費償却、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class AmortizationOfBondIssuanceCostOpeCF(Enum):
    """"社債発行費償却、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class AmortizationOfDeferredAssetsOpeCF(Enum):
    """"繰延資産償却額、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class AmortizationOfGoodwillOpeCF(Enum):
    """"のれん償却額、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class AmortizationOfGoodwillSGA(Enum):
    """"のれん償却額、販売費及び一般管理費"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'CurrentYearDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ 当年度会計期間その他 """
    CURRENT_YEAR_DURATION__OTHER_REPORTABLE_SEGMENTS_MEMBER = 'CurrentYearDuration_OtherReportableSegmentsMember'
    """ 当年度会計期間その他 """
    CURRENT_YEAR_DURATION__RECONCILING_ITEMS_MEMBER = 'CurrentYearDuration_ReconcilingItemsMember'
    """ 当年度会計期間調整項目 """
    CURRENT_YEAR_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'CurrentYearDuration_ReportableSegmentsMember'
    """ 当年度会計期間報告セグメント """
    CURRENT_YEAR_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'CurrentYearDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 当年度会計期間事業セグメント合計 """
    CURRENT_YEAR_DURATION__UNALLOCATED_AMOUNTS_AND_ELIMINATION_MEMBER = 'CurrentYearDuration_UnallocatedAmountsAndEliminationMember'
    """ 当年度会計期間全社・消去 """
    INTERIM_DURATION = 'InterimDuration'
    INTERIM_DURATION__RECONCILING_ITEMS_MEMBER = 'InterimDuration_ReconcilingItemsMember'
    """ 調整項目 """
    INTERIM_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'InterimDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_INTERIM_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1InterimDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_INTERIM_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1InterimDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'Prior1YearDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    PRIOR1_YEAR_DURATION__OTHER_REPORTABLE_SEGMENTS_MEMBER = 'Prior1YearDuration_OtherReportableSegmentsMember'
    """ その他 """
    PRIOR1_YEAR_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1YearDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_YEAR_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'Prior1YearDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    PRIOR1_YEAR_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1YearDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    PRIOR1_YEAR_DURATION__UNALLOCATED_AMOUNTS_AND_ELIMINATION_MEMBER = 'Prior1YearDuration_UnallocatedAmountsAndEliminationMember'
    """ 全社・消去 """


class AmortizationOfGuaranteeDepositsOpeCF(Enum):
    """"差入保証金償却額、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class AmortizationOfLongTermPrepaidExpensesOpeCF(Enum):
    """"長期前払費用償却額、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class AmortizationOfNegativeGoodwillNOI(Enum):
    """"負ののれん償却額、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class AmortizationOfNegativeGoodwillOpeCF(Enum):
    """"負ののれん償却額、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class AmortizationOfStockIssuanceCostNOE(Enum):
    """"株式交付費償却、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class AssetRetirementObligationsCL(Enum):
    """"資産除去債務、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class AssetRetirementObligationsLiabilities(Enum):
    """"資産除去債務、負債の部"""
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class AssetRetirementObligationsNCL(Enum):
    """"資産除去債務、固定負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class Assets(Enum):
    """"資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__OTHER_REPORTABLE_SEGMENTS_MEMBER = 'CurrentYearInstant_NonConsolidatedMember_OtherReportableSegmentsMember'
    """ 当年度時点個別又は非連結その他 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__RECONCILING_ITEMS_MEMBER = 'CurrentYearInstant_NonConsolidatedMember_ReconcilingItemsMember'
    """ 当年度時点個別又は非連結調整項目 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__REPORTABLE_SEGMENTS_MEMBER = 'CurrentYearInstant_NonConsolidatedMember_ReportableSegmentsMember'
    """ 当年度時点個別又は非連結報告セグメント """
    CURRENT_YEAR_INSTANT__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'CurrentYearInstant_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ 当年度時点その他 """
    CURRENT_YEAR_INSTANT__RECONCILING_ITEMS_MEMBER = 'CurrentYearInstant_ReconcilingItemsMember'
    """ 当年度時点調整項目 """
    CURRENT_YEAR_INSTANT__REPORTABLE_SEGMENTS_MEMBER = 'CurrentYearInstant_ReportableSegmentsMember'
    """ 当年度時点報告セグメント """
    CURRENT_YEAR_INSTANT__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'CurrentYearInstant_TotalOfReportableSegmentsAndOthersMember'
    """ 当年度時点事業セグメント合計 """
    INTERIM_INSTANT = 'InterimInstant'
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    INTERIM_INSTANT__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'InterimInstant_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    INTERIM_INSTANT__RECONCILING_ITEMS_MEMBER = 'InterimInstant_ReconcilingItemsMember'
    """ 調整項目 """
    INTERIM_INSTANT__REPORTABLE_SEGMENTS_MEMBER = 'InterimInstant_ReportableSegmentsMember'
    """ 報告セグメント """
    INTERIM_INSTANT__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'InterimInstant_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    PRIOR1_INTERIM_INSTANT = 'Prior1InterimInstant'
    PRIOR1_INTERIM_INSTANT__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'Prior1InterimInstant_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    PRIOR1_INTERIM_INSTANT__RECONCILING_ITEMS_MEMBER = 'Prior1InterimInstant_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_INTERIM_INSTANT__REPORTABLE_SEGMENTS_MEMBER = 'Prior1InterimInstant_ReportableSegmentsMember'
    """ 報告セグメント """
    PRIOR1_INTERIM_INSTANT__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1InterimInstant_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__OTHER_REPORTABLE_SEGMENTS_MEMBER = 'Prior1YearInstant_NonConsolidatedMember_OtherReportableSegmentsMember'
    """ 個別又は非連結その他 """
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__RECONCILING_ITEMS_MEMBER = 'Prior1YearInstant_NonConsolidatedMember_ReconcilingItemsMember'
    """ 個別又は非連結調整項目 """
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__REPORTABLE_SEGMENTS_MEMBER = 'Prior1YearInstant_NonConsolidatedMember_ReportableSegmentsMember'
    """ 個別又は非連結報告セグメント """
    PRIOR1_YEAR_INSTANT__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'Prior1YearInstant_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    PRIOR1_YEAR_INSTANT__RECONCILING_ITEMS_MEMBER = 'Prior1YearInstant_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_YEAR_INSTANT__REPORTABLE_SEGMENTS_MEMBER = 'Prior1YearInstant_ReportableSegmentsMember'
    """ 報告セグメント """
    PRIOR1_YEAR_INSTANT__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1YearInstant_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """


class AssetsForRentNet(Enum):
    """"貸与資産（純額）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class BadDebtsExpensesNOE(Enum):
    """"貸倒損失、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class BadDebtsExpensesSGA(Enum):
    """"貸倒損失、販売費及び一般管理費"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class BadDebtsWrittenOffEL(Enum):
    """"貸倒損失、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class BeginningFinishedGoodsCOS(Enum):
    """"製品期首棚卸高、売上原価"""
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class BeginningMerchandiseAndFinishedGoodsCOS(Enum):
    """"商品及び製品期首棚卸高、売上原価"""
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class BondIssuanceCostDA(Enum):
    """"社債発行費、繰延資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class BondIssuanceCostNOE(Enum):
    """"社債発行費、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class BondIssuanceCostOpeCF(Enum):
    """"社債発行費、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class BondsPayable(Enum):
    """"社債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    INTERIM_INSTANT = 'InterimInstant'
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class BonusesAndAllowanceSGA(Enum):
    """"賞与及び手当、販売費及び一般管理費"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class BonusesSGA(Enum):
    """"賞与、販売費及び一般管理費"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class BorrowedMoneyFromTrustAccountLiabilitiesBNK(Enum):
    """"信託勘定借、負債の部、銀行業"""
    INTERIM_INSTANT = 'InterimInstant'
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class BorrowedMoneyLiabilitiesBNK(Enum):
    """"借用金、負債の部、銀行業"""
    INTERIM_INSTANT = 'InterimInstant'
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class BrokerageIncomeORCMD(Enum):
    """"受取手数料、営業収益、商品先物取引業"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class Buildings(Enum):
    """"建物"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class BuildingsAndAccompanyingFacilities(Enum):
    """"建物附属設備"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class BuildingsAndAccompanyingFacilitiesNet(Enum):
    """"建物附属設備（純額）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class BuildingsAndStructures(Enum):
    """"建物及び構築物"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class BuildingsAndStructuresNet(Enum):
    """"建物及び構築物（純額）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class BuildingsNet(Enum):
    """"建物（純額）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class BusinessAdvisoryFeeNOI(Enum):
    """"経営指導料、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class BusinessCommencementExpensesDA(Enum):
    """"開業費、繰延資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class BusinessConsignmentExpensesSGA(Enum):
    """"業務委託費、販売費及び一般管理費"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class BusinessStructureImprovementExpensesEL(Enum):
    """"事業構造改善費用、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class BusinessStructureImprovementExpensesOpeCF(Enum):
    """"事業構造改善費用、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class CallLoansAndBillsBoughtAssetsBNK(Enum):
    """"コールローン及び買入手形、資産の部、銀行業"""
    INTERIM_INSTANT = 'InterimInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class CallLoansAssetsBNK(Enum):
    """"コールローン、資産の部、銀行業"""
    INTERIM_INSTANT = 'InterimInstant'
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class CallMoneyAndBillsSoldLiabilitiesBNK(Enum):
    """"コールマネー及び売渡手形、負債の部、銀行業"""
    INTERIM_INSTANT = 'InterimInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class CallMoneyLiabilitiesBNK(Enum):
    """"コールマネー、負債の部、銀行業"""
    INTERIM_INSTANT = 'InterimInstant'
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class CapitalStock(Enum):
    """"資本金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    INTERIM_INSTANT = 'InterimInstant'
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class CapitalSurplus(Enum):
    """"資本剰余金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    INTERIM_INSTANT = 'InterimInstant'
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class CashAndCashEquivalents(Enum):
    """"現金及び現金同等物の残高"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    INTERIM_INSTANT = 'InterimInstant'
    PRIOR1_INTERIM_INSTANT = 'Prior1InterimInstant'
    PRIOR1_QUARTER_INSTANT = 'Prior1QuarterInstant'
    PRIOR1_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1QuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR2_YEAR_INSTANT = 'Prior2YearInstant'
    PRIOR2_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior2YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class CashAndDeposits(Enum):
    """"現金及び預金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class CashAndDepositsAssetsINS(Enum):
    """"現金及び預貯金、資産の部、保険業"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class CashAndDueFromBanksAssetsBNK(Enum):
    """"現金預け金、資産の部、銀行業"""
    INTERIM_INSTANT = 'InterimInstant'
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class CashDividendsPaidFinCF(Enum):
    """"配当金の支払額、財務活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class ChangeInTreasurySharesOfParentArisingFromTransactionsWithNonControllingShareholders(Enum):
    """"非支配株主との取引に係る親会社の持分変動"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__CAPITAL_SURPLUS_MEMBER = 'CurrentYearDuration_CapitalSurplusMember'
    """ 当年度会計期間資本剰余金 """
    CURRENT_YEAR_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'CurrentYearDuration_ShareholdersEquityMember'
    """ 当年度会計期間株主資本 """
    CURRENT_YEAR_DURATION__VALUATION_AND_TRANSLATION_ADJUSTMENTS_MEMBER = 'CurrentYearDuration_ValuationAndTranslationAdjustmentsMember'
    """ 当年度会計期間評価・換算差額等 """
    INTERIM_DURATION = 'InterimDuration'
    INTERIM_DURATION__CAPITAL_SURPLUS_MEMBER = 'InterimDuration_CapitalSurplusMember'
    """ 資本剰余金 """
    INTERIM_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'InterimDuration_ShareholdersEquityMember'
    """ 株主資本 """
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_INTERIM_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1InterimDuration_ShareholdersEquityMember'
    """ 株主資本 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__CAPITAL_SURPLUS_MEMBER = 'Prior1YearDuration_CapitalSurplusMember'
    """ 資本剰余金 """
    PRIOR1_YEAR_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1YearDuration_ShareholdersEquityMember'
    """ 株主資本 """
    PRIOR1_YEAR_DURATION__VALUATION_AND_TRANSLATION_ADJUSTMENTS_MEMBER = 'Prior1YearDuration_ValuationAndTranslationAdjustmentsMember'
    """ 評価・換算差額等 """


class ChangeOfScopeOfConsolidation(Enum):
    """"連結範囲の変動"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'CurrentYearDuration_ShareholdersEquityMember'
    """ 当年度会計期間株主資本 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__RETAINED_EARNINGS_MEMBER = 'Prior1YearDuration_RetainedEarningsMember'
    """ 利益剰余金 """
    PRIOR1_YEAR_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1YearDuration_ShareholdersEquityMember'
    """ 株主資本 """
    PRIOR1_YEAR_DURATION__VALUATION_AND_TRANSLATION_ADJUSTMENTS_MEMBER = 'Prior1YearDuration_ValuationAndTranslationAdjustmentsMember'
    """ 評価・換算差額等 """


class ChangeOfScopeOfEquityMethod(Enum):
    """"持分法の適用範囲の変動"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__RETAINED_EARNINGS_MEMBER = 'CurrentYearDuration_RetainedEarningsMember'
    """ 当年度会計期間利益剰余金 """
    CURRENT_YEAR_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'CurrentYearDuration_ShareholdersEquityMember'
    """ 当年度会計期間株主資本 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1YearDuration_ShareholdersEquityMember'
    """ 株主資本 """


class ClaimsProvableInBankruptcyClaimsProvableInRehabilitationAndOther(Enum):
    """"破産更生債権等"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class CoSponsorFeeNOI(Enum):
    """"協賛金収入、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class CoinsuranceAccountsReceivableAssetsINS(Enum):
    """"共同保険貸、資産の部、保険業"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class CollectionOfInvestmentAndLoansReceivableInvCF(Enum):
    """"投融資の回収による収入、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class CollectionOfLeaseDepositsInvCF(Enum):
    """"敷金の回収による収入、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class CollectionOfLoansReceivableInvCF(Enum):
    """"貸付金の回収による収入、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class CollectionOfLoansReceivableToEmployeesInvCF(Enum):
    """"従業員に対する貸付金の回収による収入、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class CollectionOfLongTermLoansReceivableInvCF(Enum):
    """"長期貸付金の回収による収入、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class CollectionOfLongTermLoansReceivableToEmployeesInvCF(Enum):
    """"従業員に対する長期貸付金の回収による収入、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class CollectionOfShortTermLoansReceivableInvCF(Enum):
    """"短期貸付金の回収による収入、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class CommercialPapersLiabilities(Enum):
    """"コマーシャル・ペーパー"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    INTERIM_INSTANT = 'InterimInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class CommissionFeeNOE(Enum):
    """"支払手数料、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class CommissionFeeNOI(Enum):
    """"受取手数料、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class CommissionFeeOpeCF(Enum):
    """"支払手数料、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class CommissionFeeSGA(Enum):
    """"支払手数料、販売費及び一般管理費"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class CommissionForPurchaseOfTreasuryStockNOE(Enum):
    """"自己株式取得費用、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class CommissionForSyndicateLoanNOE(Enum):
    """"シンジケートローン手数料、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class CommissionIncomeRevOA(Enum):
    """"手数料収入、営業活動による収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class CommissionsAndCollectionFeesOEINS(Enum):
    """"諸手数料及び集金費、経常費用、保険業"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class CommissionsFromSubsidiariesAndAffiliatesRevOA(Enum):
    """"関係会社受入手数料、営業活動による収益"""
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class CommitmentFeeNOE(Enum):
    """"コミットメントフィー、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class CommunicationExpensesSGA(Enum):
    """"通信費、販売費及び一般管理費"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class CompensationExpensesNOE(Enum):
    """"支払補償費、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class CompensationForDamageEL(Enum):
    """"損害賠償金、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class CompensationForDamagePaidOpeCF(Enum):
    """"損害賠償金の支払額、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class CompensationForRemovalOpeCF(Enum):
    """"移転補償金、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class CompensationForTransferEI(Enum):
    """"移転補償金、特別利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    INTERIM_DURATION = 'InterimDuration'
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class CompensationIncomeEI(Enum):
    """"受取補償金、特別利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class CompensationIncomeForExpropriationEI(Enum):
    """"収用補償金、特別利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class CompensationIncomeForExpropriationOpeCF(Enum):
    """"収用補償金、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class CompensationIncomeNOI(Enum):
    """"受取補償金、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class CompensationIncomeOpeCF(Enum):
    """"受取補償金、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class CompensationsSGA(Enum):
    """"支払報酬、販売費及び一般管理費"""
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class CompensationsSalariesAndAllowancesSGA(Enum):
    """"報酬及び給料手当、販売費及び一般管理費"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ComprehensiveIncome(Enum):
    """"包括利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class ComprehensiveIncomeAttributableToNonControllingInterests(Enum):
    """"非支配株主に係る包括利益、包括利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class ComprehensiveIncomeAttributableToOwnersOfTheParent(Enum):
    """"親会社株主に係る包括利益、包括利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class ConstructionAssistanceFundReceivables(Enum):
    """"建設協力金"""
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class ConstructionInProgress(Enum):
    """"建設仮勘定"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class ConsumptionTaxesReceivable(Enum):
    """"未収消費税等"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class ContractAssets(Enum):
    """"契約資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class ContractLiabilities(Enum):
    """"契約負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class ContributionForConstructionEI(Enum):
    """"工事負担金等受入額、特別利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ContributionNOE(Enum):
    """"寄付金、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ContributionSGA(Enum):
    """"寄付金、販売費及び一般管理費"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class ConvertibleBondTypeBondsWithSubscriptionRightsToShares(Enum):
    """"転換社債型新株予約権付社債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class CorrespondenceAndTransportationExpensesSGA(Enum):
    """"通信交通費、販売費及び一般管理費"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class CostOfFinishedGoodsSold(Enum):
    """"製品売上原価"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class CostOfGoodsSold(Enum):
    """"商品売上原価"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class CostOfLeaseRevenueNOE(Enum):
    """"賃貸収入原価、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class CostOfMerchandiseAndFinishedGoodsSoldCOS(Enum):
    """"商品及び製品売上原価、売上原価"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class CostOfProductsManufactured(Enum):
    """"当期製品製造原価"""
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class CostOfPurchasedGoods(Enum):
    """"当期商品仕入高"""
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class CostOfSales(Enum):
    """"売上原価"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class CostOfSalesOfCompletedConstructionContractsCNS(Enum):
    """"完成工事原価、建設業"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class CostOfSalesOnOtherBusinessCOSExpOA(Enum):
    """"その他の事業売上原価、営業活動による費用・売上原価"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class CostOfSalesOnRealEstateBusinessAndOtherCNS(Enum):
    """"不動産事業等売上原価、建設業"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class CostOfSalesOnRealEstateBusinessCOSExpOA(Enum):
    """"不動産事業売上原価、営業活動による費用・売上原価"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class CostOfSalesOnSideLineBusinessCNS(Enum):
    """"兼業事業売上原価、建設業"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class CostsOnRealEstateBusiness(Enum):
    """"不動産事業支出金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class CostsOnUncompletedConstructionContractsAndOtherCNS(Enum):
    """"未成工事支出金等、建設業"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class CostsOnUncompletedConstructionContractsCNS(Enum):
    """"未成工事支出金、建設業"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class CostsOnUncompletedServices(Enum):
    """"未成業務支出金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class CreditCardRevenueRevOA(Enum):
    """"包括信用購入あっせん収益、営業活動による収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class CumulativeEffectsOfChangesInAccountingPolicies(Enum):
    """"会計方針の変更による累積的影響額"""
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1YearInstant_ShareholdersEquityMember'
    """ 株主資本 """
    PRIOR2_YEAR_INSTANT = 'Prior2YearInstant'
    PRIOR2_YEAR_INSTANT__RETAINED_EARNINGS_MEMBER = 'Prior2YearInstant_RetainedEarningsMember'
    """ 利益剰余金 """
    PRIOR2_YEAR_INSTANT__SHAREHOLDERS_EQUITY_MEMBER = 'Prior2YearInstant_ShareholdersEquityMember'
    """ 株主資本 """


class CurrentAssets(Enum):
    """"流動資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class CurrentLiabilities(Enum):
    """"流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class CurrentPortionOfBonds(Enum):
    """"１年内償還予定の社債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class CurrentPortionOfBondsWithSubscriptionRightsToShares(Enum):
    """"１年内償還予定の新株予約権付社債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class CurrentPortionOfConvertibleBonds(Enum):
    """"１年内償還予定の転換社債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class CurrentPortionOfLongTermLoansPayable(Enum):
    """"１年内返済予定の長期借入金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class CurrentPortionOfLongTermLoansPayableToSubsidiariesAndAffiliates(Enum):
    """"１年内返済予定の関係会社長期借入金"""
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class CurrentPortionOfLongTermLoansReceivable(Enum):
    """"１年内回収予定の長期貸付金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class CurrentPortionOfLongTermPayablesUnderFluidityLeaseReceivablesCLLEA(Enum):
    """"１年内支払予定の債権流動化に伴う長期支払債務、流動負債、リース事業"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class CurrentPortionOfNoncurrentLiabilitiesCLGAS(Enum):
    """"１年以内に期限到来の固定負債、流動負債、ガス事業"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class CurrentPortionOfOtherNoncurrentLiabilities(Enum):
    """"１年内期限到来予定のその他の固定負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class CustomerRelatedIntangibleAssets(Enum):
    """"顧客関連資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class CustomersDepositsReceivedForCommodityFuturesTransactionCLCMD(Enum):
    """"預り証拠金、流動負債、商品先物取引業"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class CustomersLiabilitiesForAcceptancesAndGuaranteesAssetsBNK(Enum):
    """"支払承諾見返、資産の部、銀行業"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    INTERIM_INSTANT = 'InterimInstant'
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class DecreaseByCorporateDivisionsplitoffType(Enum):
    """"分割型の会社分割による減少"""
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_BROUGHT_FORWARD_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_RetainedEarningsBroughtForwardMember'
    """ 当年度会計期間個別又は非連結繰越利益剰余金 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_RetainedEarningsMember'
    """ 当年度会計期間個別又は非連結利益剰余金 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__SHAREHOLDERS_EQUITY_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_ShareholdersEquityMember'
    """ 当年度会計期間個別又は非連結株主資本 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_ShareholdersEquityMember'
    """ 個別又は非連結株主資本 """


class DecreaseInCashAndCashEquivalentsResultingFromExclusionOfSubsidiariesFromConsolidationCCE(Enum):
    """"連結除外に伴う現金及び現金同等物の減少額"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DecreaseInMoneyHeldInTrustInvCFBNK(Enum):
    """"金銭の信託の減少による収入、投資活動によるキャッシュ・フロー、銀行業"""
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'


class DecreaseInShortTermLoansPayableFinCF(Enum):
    """"短期借入金の返済による支出、財務活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class DecreaseIncreaseInAccountsReceivableInstallmentOpeCF(Enum):
    """"割賦売掛金の増減額（△は増加）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DecreaseIncreaseInAccountsReceivableOtherOpeCF(Enum):
    """"未収入金の増減額（△は増加）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class DecreaseIncreaseInAccountsReceivableTradeAndContractAssetsOpeCF(Enum):
    """"売上債権及び契約資産の増減額（△は増加）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class DecreaseIncreaseInAdvancePaymentsOpeCF(Enum):
    """"前渡金の増減額（△は増加）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class DecreaseIncreaseInAdvancesPaidOpeCF(Enum):
    """"立替金の増減額（△は増加）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DecreaseIncreaseInClaimsProvableInBankruptcyClaimsProvableInRehabilitationOpeCF(Enum):
    """"破産更生債権等の増減額（△は増加）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class DecreaseIncreaseInConsumptionTaxesReceivablePayableOpeCF(Enum):
    """"未払又は未収消費税等の増減額、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class DecreaseIncreaseInConsumptionTaxesRefundReceivableOpeCF(Enum):
    """"未収消費税等の増減額（△は増加）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class DecreaseIncreaseInCostsOnUncompletedConstructionContractsAndOtherOpeCFCNS(Enum):
    """"未成工事支出金等の増減額（△は増加）、営業活動によるキャッシュ・フロー、建設業"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DecreaseIncreaseInCostsOnUncompletedConstructionContractsOpeCFCNS(Enum):
    """"未成工事支出金の増減額（△は増加）、営業活動によるキャッシュ・フロー、建設業"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class DecreaseIncreaseInDepositsPaidOpeCF(Enum):
    """"預け金の増減額（△は増加）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class DecreaseIncreaseInGuaranteeDepositsOpeCF(Enum):
    """"差入保証金の増減額（△は増加）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DecreaseIncreaseInInventoriesOpeCF(Enum):
    """"棚卸資産の増減額（△は増加）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class DecreaseIncreaseInInvestmentSecuritiesForSaleOpeCF(Enum):
    """"営業投資有価証券の増減額（△は増加）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DecreaseIncreaseInLeaseInvestmentAssetsOpeCF(Enum):
    """"リース投資資産の増減額（△は増加）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class DecreaseIncreaseInLongTermPrepaidExpensesOpeCF(Enum):
    """"長期前払費用の増減額（△は増加）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class DecreaseIncreaseInNotesAndAccountsReceivableTradeOpeCF(Enum):
    """"売上債権の増減額（△は増加）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class DecreaseIncreaseInOperatingLoansReceivableOpeCF(Enum):
    """"営業貸付金の増減額（△は増加）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DecreaseIncreaseInOtherAssetsOpeCF(Enum):
    """"その他の資産の増減額（△は増加）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class DecreaseIncreaseInOtherCurrentAssetsOpeCF(Enum):
    """"その他の流動資産の増減額（△は増加）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class DecreaseIncreaseInOtherInventoriesOpeCFCNS(Enum):
    """"その他の棚卸資産の増減額（△は増加）、営業活動によるキャッシュ・フロー、建設業"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DecreaseIncreaseInOtherInvestingAndFinancingActivitiesAssetsOpeCFINS(Enum):
    """"その他資産（除く投資活動関連、財務活動関連）の増減額（△は増加）、営業活動によるキャッシュ・フロー、保険業"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DecreaseIncreaseInOtherInvestmentsInvCF(Enum):
    """"投資その他の資産の増減額（△は増加）、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DecreaseIncreaseInOtherNoncurrentAssetsOpeCF(Enum):
    """"その他の固定資産の増減額（△は増加）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DecreaseIncreaseInPrepaidExpensesOpeCF(Enum):
    """"前払費用の増減額（△は増加）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class DecreaseIncreaseInPrepaidPensionCostsOpeCF(Enum):
    """"前払年金費用の増減額（△は増加）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class DecreaseIncreaseInRealEstateForSaleOpeCF(Enum):
    """"販売用不動産の増減額（△は増加）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DecreaseIncreaseInShortTermInvestmentSecuritiesInvCF(Enum):
    """"有価証券の増減額（△は増加）、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DecreaseIncreaseInShortTermLoansReceivableInvCF(Enum):
    """"短期貸付金の増減額（△は増加）、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class DecreaseIncreaseInSuppliesOpeCF(Enum):
    """"貯蔵品の増減額（△は増加）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DecreaseIncreaseInTimeDepositsInvCF(Enum):
    """"定期預金の増減額（△は増加）、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class DecreaseIncreaseInTreasuryStockFinCF(Enum):
    """"自己株式の増減額（△は増加）、財務活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class DeferredAndPrepaidExpensesCAWAT(Enum):
    """"繰延及び前払費用、流動資産、海運業"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class DeferredAssets(Enum):
    """"繰延資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class DeferredGainsOrLossesOnHedges(Enum):
    """"繰延ヘッジ損益"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    INTERIM_INSTANT = 'InterimInstant'
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class DeferredGainsOrLossesOnHedgesBeforeTaxOCI(Enum):
    """"繰延ヘッジ損益（税引前）、その他の包括利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DeferredGainsOrLossesOnHedgesNetOfTaxOCI(Enum):
    """"繰延ヘッジ損益（税引後）、その他の包括利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class DeferredOrganizationExpensesDA(Enum):
    """"創立費、繰延資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class DeferredProfitOnInstallmentSalesCLLEA(Enum):
    """"割賦未実現利益、流動負債、リース事業"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class DeferredTaxAssets(Enum):
    """"繰延税金資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    INTERIM_INSTANT = 'InterimInstant'
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class DeferredTaxAssetsForLandRevaluation(Enum):
    """"再評価に係る繰延税金資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class DeferredTaxLiabilities(Enum):
    """"繰延税金負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    INTERIM_INSTANT = 'InterimInstant'
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class DeferredTaxLiabilitiesForLandRevaluation(Enum):
    """"再評価に係る繰延税金負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    INTERIM_INSTANT = 'InterimInstant'
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class DepositReceivedRealEstate(Enum):
    """"不動産事業受入金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class DepositsLiabilitiesBNK(Enum):
    """"預金、負債の部、銀行業"""
    INTERIM_INSTANT = 'InterimInstant'
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class DepositsPaid(Enum):
    """"預け金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class DepositsReceived(Enum):
    """"預り金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class DepositsReceivedFromEmployees(Enum):
    """"従業員預り金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class DepositsReceivedFromMembers(Enum):
    """"会員預り金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class DepreciationAndAmortizationOnOtherOpeCF(Enum):
    """"その他の償却額、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class DepreciationAndAmortizationOpeCF(Enum):
    """"減価償却費、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class DepreciationAndOtherAmortizationOpeCF(Enum):
    """"減価償却費及びその他の償却費、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class DepreciationNOE(Enum):
    """"減価償却費、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class DepreciationOfAssetsForRentNOE(Enum):
    """"貸与資産減価償却費、営業外費用"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class DepreciationOfIntangibleAssetsOpeCF(Enum):
    """"無形固定資産償却費、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DepreciationOfSoftwareOpeCF(Enum):
    """"ソフトウエア償却費、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DepreciationSGA(Enum):
    """"減価償却費、販売費及び一般管理費"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class DirectorsCompensationsSGA(Enum):
    """"役員報酬、販売費及び一般管理費"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class DirectorsCompensationsSalariesAndAllowancesSGA(Enum):
    """"役員報酬及び給料手当、販売費及び一般管理費"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DirectorsRetirementBenefitsEL(Enum):
    """"役員退職慰労金、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class DirectorsRetirementBenefitsSGA(Enum):
    """"役員退職慰労金、販売費及び一般管理費"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class DisposalOfTreasuryStock(Enum):
    """"自己株式の処分"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__CAPITAL_SURPLUS_MEMBER = 'CurrentYearDuration_CapitalSurplusMember'
    """ 当年度会計期間資本剰余金 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CAPITAL_SURPLUS_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_CapitalSurplusMember'
    """ 当年度会計期間個別又は非連結資本剰余金 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__OTHER_CAPITAL_SURPLUS_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_OtherCapitalSurplusMember'
    """ 当年度会計期間個別又は非連結その他資本剰余金 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_BROUGHT_FORWARD_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_RetainedEarningsBroughtForwardMember'
    """ 当年度会計期間個別又は非連結繰越利益剰余金 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_RetainedEarningsMember'
    """ 当年度会計期間個別又は非連結利益剰余金 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__SHAREHOLDERS_EQUITY_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_ShareholdersEquityMember'
    """ 当年度会計期間個別又は非連結株主資本 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__TREASURY_STOCK_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_TreasuryStockMember'
    """ 当年度会計期間個別又は非連結自己株式 """
    CURRENT_YEAR_DURATION__RETAINED_EARNINGS_MEMBER = 'CurrentYearDuration_RetainedEarningsMember'
    """ 当年度会計期間利益剰余金 """
    CURRENT_YEAR_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'CurrentYearDuration_ShareholdersEquityMember'
    """ 当年度会計期間株主資本 """
    CURRENT_YEAR_DURATION__TREASURY_STOCK_MEMBER = 'CurrentYearDuration_TreasuryStockMember'
    """ 当年度会計期間自己株式 """
    CURRENT_YEAR_DURATION__VALUATION_AND_TRANSLATION_ADJUSTMENTS_MEMBER = 'CurrentYearDuration_ValuationAndTranslationAdjustmentsMember'
    """ 当年度会計期間評価・換算差額等 """
    INTERIM_DURATION = 'InterimDuration'
    INTERIM_DURATION__CAPITAL_SURPLUS_MEMBER = 'InterimDuration_CapitalSurplusMember'
    """ 資本剰余金 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__CAPITAL_SURPLUS_MEMBER = 'InterimDuration_NonConsolidatedMember_CapitalSurplusMember'
    """ 個別又は非連結資本剰余金 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__OTHER_CAPITAL_SURPLUS_MEMBER = 'InterimDuration_NonConsolidatedMember_OtherCapitalSurplusMember'
    """ 個別又は非連結その他資本剰余金 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_BROUGHT_FORWARD_MEMBER = 'InterimDuration_NonConsolidatedMember_RetainedEarningsBroughtForwardMember'
    """ 個別又は非連結繰越利益剰余金 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_MEMBER = 'InterimDuration_NonConsolidatedMember_RetainedEarningsMember'
    """ 個別又は非連結利益剰余金 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__SHAREHOLDERS_EQUITY_MEMBER = 'InterimDuration_NonConsolidatedMember_ShareholdersEquityMember'
    """ 個別又は非連結株主資本 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__TREASURY_STOCK_MEMBER = 'InterimDuration_NonConsolidatedMember_TreasuryStockMember'
    """ 個別又は非連結自己株式 """
    INTERIM_DURATION__RETAINED_EARNINGS_MEMBER = 'InterimDuration_RetainedEarningsMember'
    """ 利益剰余金 """
    INTERIM_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'InterimDuration_ShareholdersEquityMember'
    """ 株主資本 """
    INTERIM_DURATION__TREASURY_STOCK_MEMBER = 'InterimDuration_TreasuryStockMember'
    """ 自己株式 """
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_INTERIM_DURATION__CAPITAL_SURPLUS_MEMBER = 'Prior1InterimDuration_CapitalSurplusMember'
    """ 資本剰余金 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__CAPITAL_SURPLUS_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_CapitalSurplusMember'
    """ 個別又は非連結資本剰余金 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__OTHER_CAPITAL_SURPLUS_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_OtherCapitalSurplusMember'
    """ 個別又は非連結その他資本剰余金 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_BROUGHT_FORWARD_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_RetainedEarningsBroughtForwardMember'
    """ 個別又は非連結繰越利益剰余金 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_RetainedEarningsMember'
    """ 個別又は非連結利益剰余金 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_ShareholdersEquityMember'
    """ 個別又は非連結株主資本 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__TREASURY_STOCK_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_TreasuryStockMember'
    """ 個別又は非連結自己株式 """
    PRIOR1_INTERIM_DURATION__RETAINED_EARNINGS_MEMBER = 'Prior1InterimDuration_RetainedEarningsMember'
    """ 利益剰余金 """
    PRIOR1_INTERIM_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1InterimDuration_ShareholdersEquityMember'
    """ 株主資本 """
    PRIOR1_INTERIM_DURATION__TREASURY_STOCK_MEMBER = 'Prior1InterimDuration_TreasuryStockMember'
    """ 自己株式 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__CAPITAL_SURPLUS_MEMBER = 'Prior1YearDuration_CapitalSurplusMember'
    """ 資本剰余金 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CAPITAL_SURPLUS_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_CapitalSurplusMember'
    """ 個別又は非連結資本剰余金 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__OTHER_CAPITAL_SURPLUS_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_OtherCapitalSurplusMember'
    """ 個別又は非連結その他資本剰余金 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_ShareholdersEquityMember'
    """ 個別又は非連結株主資本 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__TREASURY_STOCK_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_TreasuryStockMember'
    """ 個別又は非連結自己株式 """
    PRIOR1_YEAR_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1YearDuration_ShareholdersEquityMember'
    """ 株主資本 """
    PRIOR1_YEAR_DURATION__TREASURY_STOCK_MEMBER = 'Prior1YearDuration_TreasuryStockMember'
    """ 自己株式 """
    PRIOR1_YEAR_DURATION__VALUATION_AND_TRANSLATION_ADJUSTMENTS_MEMBER = 'Prior1YearDuration_ValuationAndTranslationAdjustmentsMember'
    """ 評価・換算差額等 """


class DistributionExpensesSGA(Enum):
    """"配送費、販売費及び一般管理費"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DistributionFacilitiesPPEGAS(Enum):
    """"供給設備、有形固定資産、ガス事業"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class DividendsDistributionFromSilentPartnership(Enum):
    """"匿名組合損益分配額"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DividendsFromSubsidiariesAndAffiliatesRevOA(Enum):
    """"関係会社受取配当金、営業活動による収益"""
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class DividendsFromSurplus(Enum):
    """"剰余金の配当"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__CAPITAL_STOCK_MEMBER = 'CurrentYearDuration_CapitalStockMember'
    """ 当年度会計期間資本金 """
    CURRENT_YEAR_DURATION__CAPITAL_SURPLUS_MEMBER = 'CurrentYearDuration_CapitalSurplusMember'
    """ 当年度会計期間資本剰余金 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CAPITAL_STOCK_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_CapitalStockMember'
    """ 当年度会計期間個別又は非連結資本金 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CAPITAL_SURPLUS_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_CapitalSurplusMember'
    """ 当年度会計期間個別又は非連結資本剰余金 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__LEGAL_CAPITAL_SURPLUS_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_LegalCapitalSurplusMember'
    """ 当年度会計期間個別又は非連結資本準備金 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_BROUGHT_FORWARD_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_RetainedEarningsBroughtForwardMember'
    """ 当年度会計期間個別又は非連結繰越利益剰余金 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_RetainedEarningsMember'
    """ 当年度会計期間個別又は非連結利益剰余金 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__SHAREHOLDERS_EQUITY_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_ShareholdersEquityMember'
    """ 当年度会計期間個別又は非連結株主資本 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__SUBSCRIPTION_RIGHTS_TO_SHARES_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_SubscriptionRightsToSharesMember'
    """ 当年度会計期間個別又は非連結新株予約権 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__TREASURY_STOCK_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_TreasuryStockMember'
    """ 当年度会計期間個別又は非連結自己株式 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__VALUATION_AND_TRANSLATION_ADJUSTMENTS_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_ValuationAndTranslationAdjustmentsMember'
    """ 当年度会計期間個別又は非連結評価・換算差額等 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__VALUATION_DIFFERENCE_ON_AVAILABLE_FOR_SALE_SECURITIES_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_ValuationDifferenceOnAvailableForSaleSecuritiesMember'
    """ 当年度会計期間個別又は非連結その他有価証券評価差額金 """
    CURRENT_YEAR_DURATION__NON_CONTROLLING_INTERESTS_MEMBER = 'CurrentYearDuration_NonControllingInterestsMember'
    """ 当年度会計期間非支配株主持分 """
    CURRENT_YEAR_DURATION__RETAINED_EARNINGS_MEMBER = 'CurrentYearDuration_RetainedEarningsMember'
    """ 当年度会計期間利益剰余金 """
    CURRENT_YEAR_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'CurrentYearDuration_ShareholdersEquityMember'
    """ 当年度会計期間株主資本 """
    CURRENT_YEAR_DURATION__SUBSCRIPTION_RIGHTS_TO_SHARES_MEMBER = 'CurrentYearDuration_SubscriptionRightsToSharesMember'
    """ 当年度会計期間新株予約権 """
    CURRENT_YEAR_DURATION__TREASURY_STOCK_MEMBER = 'CurrentYearDuration_TreasuryStockMember'
    """ 当年度会計期間自己株式 """
    CURRENT_YEAR_DURATION__VALUATION_AND_TRANSLATION_ADJUSTMENTS_MEMBER = 'CurrentYearDuration_ValuationAndTranslationAdjustmentsMember'
    """ 当年度会計期間評価・換算差額等 """
    INTERIM_DURATION = 'InterimDuration'
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__GENERAL_RESERVE_MEMBER = 'InterimDuration_NonConsolidatedMember_GeneralReserveMember'
    """ 個別又は非連結別途積立金 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__LEGAL_RETAINED_EARNINGS_MEMBER = 'InterimDuration_NonConsolidatedMember_LegalRetainedEarningsMember'
    """ 個別又は非連結利益準備金 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_BROUGHT_FORWARD_MEMBER = 'InterimDuration_NonConsolidatedMember_RetainedEarningsBroughtForwardMember'
    """ 個別又は非連結繰越利益剰余金 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_MEMBER = 'InterimDuration_NonConsolidatedMember_RetainedEarningsMember'
    """ 個別又は非連結利益剰余金 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__SHAREHOLDERS_EQUITY_MEMBER = 'InterimDuration_NonConsolidatedMember_ShareholdersEquityMember'
    """ 個別又は非連結株主資本 """
    INTERIM_DURATION__RETAINED_EARNINGS_MEMBER = 'InterimDuration_RetainedEarningsMember'
    """ 利益剰余金 """
    INTERIM_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'InterimDuration_ShareholdersEquityMember'
    """ 株主資本 """
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__GENERAL_RESERVE_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_GeneralReserveMember'
    """ 個別又は非連結別途積立金 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__LEGAL_RETAINED_EARNINGS_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_LegalRetainedEarningsMember'
    """ 個別又は非連結利益準備金 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_BROUGHT_FORWARD_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_RetainedEarningsBroughtForwardMember'
    """ 個別又は非連結繰越利益剰余金 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_RetainedEarningsMember'
    """ 個別又は非連結利益剰余金 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_ShareholdersEquityMember'
    """ 個別又は非連結株主資本 """
    PRIOR1_INTERIM_DURATION__RETAINED_EARNINGS_MEMBER = 'Prior1InterimDuration_RetainedEarningsMember'
    """ 利益剰余金 """
    PRIOR1_INTERIM_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1InterimDuration_ShareholdersEquityMember'
    """ 株主資本 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__CAPITAL_STOCK_MEMBER = 'Prior1YearDuration_CapitalStockMember'
    """ 資本金 """
    PRIOR1_YEAR_DURATION__CAPITAL_SURPLUS_MEMBER = 'Prior1YearDuration_CapitalSurplusMember'
    """ 資本剰余金 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CAPITAL_STOCK_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_CapitalStockMember'
    """ 個別又は非連結資本金 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CAPITAL_SURPLUS_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_CapitalSurplusMember'
    """ 個別又は非連結資本剰余金 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__LEGAL_CAPITAL_SURPLUS_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_LegalCapitalSurplusMember'
    """ 個別又は非連結資本準備金 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_BROUGHT_FORWARD_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_RetainedEarningsBroughtForwardMember'
    """ 個別又は非連結繰越利益剰余金 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_RetainedEarningsMember'
    """ 個別又は非連結利益剰余金 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_ShareholdersEquityMember'
    """ 個別又は非連結株主資本 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__SUBSCRIPTION_RIGHTS_TO_SHARES_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_SubscriptionRightsToSharesMember'
    """ 個別又は非連結新株予約権 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__TREASURY_STOCK_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_TreasuryStockMember'
    """ 個別又は非連結自己株式 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__VALUATION_AND_TRANSLATION_ADJUSTMENTS_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_ValuationAndTranslationAdjustmentsMember'
    """ 個別又は非連結評価・換算差額等 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__VALUATION_DIFFERENCE_ON_AVAILABLE_FOR_SALE_SECURITIES_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_ValuationDifferenceOnAvailableForSaleSecuritiesMember'
    """ 個別又は非連結その他有価証券評価差額金 """
    PRIOR1_YEAR_DURATION__NON_CONTROLLING_INTERESTS_MEMBER = 'Prior1YearDuration_NonControllingInterestsMember'
    """ 非支配株主持分 """
    PRIOR1_YEAR_DURATION__RETAINED_EARNINGS_MEMBER = 'Prior1YearDuration_RetainedEarningsMember'
    """ 利益剰余金 """
    PRIOR1_YEAR_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1YearDuration_ShareholdersEquityMember'
    """ 株主資本 """
    PRIOR1_YEAR_DURATION__SUBSCRIPTION_RIGHTS_TO_SHARES_MEMBER = 'Prior1YearDuration_SubscriptionRightsToSharesMember'
    """ 新株予約権 """
    PRIOR1_YEAR_DURATION__TREASURY_STOCK_MEMBER = 'Prior1YearDuration_TreasuryStockMember'
    """ 自己株式 """
    PRIOR1_YEAR_DURATION__VALUATION_AND_TRANSLATION_ADJUSTMENTS_MEMBER = 'Prior1YearDuration_ValuationAndTranslationAdjustmentsMember'
    """ 評価・換算差額等 """


class DividendsIncomeNOI(Enum):
    """"受取配当金、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class DividendsIncomeOfInsuranceNOI(Enum):
    """"保険配当金、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class DividendsIncomeOfLifeInsuranceNOI(Enum):
    """"生命保険配当金、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class DividendsPaidToNonControllingInterestsFinCF(Enum):
    """"非支配株主への配当金の支払額、財務活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class DividendsPayable(Enum):
    """"未払配当金"""
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class EarlyExtraRetirementPaymentsEL(Enum):
    """"早期割増退職金、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class EffectOfExchangeRateChangeOnCashAndCashEquivalents(Enum):
    """"現金及び現金同等物に係る換算差額"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class ElectricitySaleExpensesNOE(Enum):
    """"売電費用、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class ElectricitySaleIncomeNOI(Enum):
    """"売電収入、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class ElectronicallyRecordedMonetaryClaimsOperatingCA(Enum):
    """"電子記録債権、流動資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class ElectronicallyRecordedObligationsFacilitiesCL(Enum):
    """"設備関係電子記録債務、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class ElectronicallyRecordedObligationsNonOperatingCL(Enum):
    """"営業外電子記録債務、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ElectronicallyRecordedObligationsOperatingCL(Enum):
    """"電子記録債務、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class EmployeesBonusesSGA(Enum):
    """"従業員賞与、販売費及び一般管理費"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class EmployeesSalariesAndAllowancesSGA(Enum):
    """"従業員給料及び手当、販売費及び一般管理費"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class EmployeesSalariesAndAllowancesSGACNS(Enum):
    """"従業員給料手当、販売費及び一般管理費、建設業"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class EmployeesSalariesAndBonusesSGA(Enum):
    """"従業員給料及び賞与、販売費及び一般管理費"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class EmployeesSalariesSGA(Enum):
    """"従業員給料、販売費及び一般管理費"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class EndingFinishedGoodsCOS(Enum):
    """"製品期末棚卸高、売上原価"""
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class EndingMerchandiseAndFinishedGoodsCOS(Enum):
    """"商品及び製品期末棚卸高、売上原価"""
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class EnterpriseTaxSGA(Enum):
    """"事業税、販売費及び一般管理費"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class EntertainmentExpensesSGA(Enum):
    """"交際費、販売費及び一般管理費"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class EnvironmentalExpensesEL(Enum):
    """"環境対策費、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class EquityInEarningsLossesOfAffiliatesOpeCF(Enum):
    """"持分法による投資損益（△は益）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class EquityInEarningsOfAffiliatesNOI(Enum):
    """"持分法による投資利益、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class EquityInLossesOfAffiliatesNOE(Enum):
    """"持分法による投資損失、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ExerciseOfSubscriptionRightsToShares(Enum):
    """"新株予約権の行使"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'CurrentYearDuration_ShareholdersEquityMember'
    """ 当年度会計期間株主資本 """
    CURRENT_YEAR_DURATION__SUBSCRIPTION_RIGHTS_TO_SHARES_MEMBER = 'CurrentYearDuration_SubscriptionRightsToSharesMember'
    """ 当年度会計期間新株予約権 """
    CURRENT_YEAR_DURATION__VALUATION_AND_TRANSLATION_ADJUSTMENTS_MEMBER = 'CurrentYearDuration_ValuationAndTranslationAdjustmentsMember'
    """ 当年度会計期間評価・換算差額等 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1YearDuration_ShareholdersEquityMember'
    """ 株主資本 """
    PRIOR1_YEAR_DURATION__SUBSCRIPTION_RIGHTS_TO_SHARES_MEMBER = 'Prior1YearDuration_SubscriptionRightsToSharesMember'
    """ 新株予約権 """
    PRIOR1_YEAR_DURATION__VALUATION_AND_TRANSLATION_ADJUSTMENTS_MEMBER = 'Prior1YearDuration_ValuationAndTranslationAdjustmentsMember'
    """ 評価・換算差額等 """


class ExtraRetirementPaymentOpeCF(Enum):
    """"特別退職金、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ExtraRetirementPaymentsEL(Enum):
    """"割増退職金、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ExtraRetirementPaymentsNOE(Enum):
    """"割増退職金、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ExtraordinaryIncome(Enum):
    """"特別利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    INTERIM_DURATION = 'InterimDuration'
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    INTERIM_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'InterimDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    INTERIM_DURATION__RECONCILING_ITEMS_MEMBER = 'InterimDuration_ReconcilingItemsMember'
    """ 調整項目 """
    INTERIM_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'InterimDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    INTERIM_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'InterimDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_INTERIM_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'Prior1InterimDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    PRIOR1_INTERIM_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1InterimDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_INTERIM_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'Prior1InterimDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    PRIOR1_INTERIM_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1InterimDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class ExtraordinaryLoss(Enum):
    """"特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    INTERIM_DURATION = 'InterimDuration'
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    INTERIM_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'InterimDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    INTERIM_DURATION__RECONCILING_ITEMS_MEMBER = 'InterimDuration_ReconcilingItemsMember'
    """ 調整項目 """
    INTERIM_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'InterimDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    INTERIM_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'InterimDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_INTERIM_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'Prior1InterimDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    PRIOR1_INTERIM_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1InterimDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_INTERIM_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'Prior1InterimDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    PRIOR1_INTERIM_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1InterimDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class FeesAndCommissionsOIBNK(Enum):
    """"役務取引等収益、経常収益、銀行業"""
    INTERIM_DURATION = 'InterimDuration'
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class FeesAndCommissionsPaymentsOEBNK(Enum):
    """"役務取引等費用、経常費用、銀行業"""
    INTERIM_DURATION = 'InterimDuration'
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class FiduciaryObligationFeeNOI(Enum):
    """"業務受託料、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class FinancialExpenses(Enum):
    """"金融費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class FinancingExpensesNOE(Enum):
    """"資金調達費用、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class FinancingExpensesOpeCFBNK(Enum):
    """"資金調達費用、営業活動によるキャッシュ・フロー、銀行業"""
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'


class FinishedGoods(Enum):
    """"製品"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class ForeignCurrencyTranslationAdjustment(Enum):
    """"為替換算調整勘定"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    INTERIM_INSTANT = 'InterimInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ForeignCurrencyTranslationAdjustmentNetOfTaxOCI(Enum):
    """"為替換算調整勘定（税引後）、その他の包括利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class ForeignExchangeGainsNOI(Enum):
    """"為替差益、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class ForeignExchangeLossesGainsOpeCF(Enum):
    """"為替差損益（△は益）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class ForeignExchangeLossesNOE(Enum):
    """"為替差損、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class ForeignExchangesAssetsBNK(Enum):
    """"外国為替、資産の部、銀行業"""
    INTERIM_INSTANT = 'InterimInstant'
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class ForeignExchangesLiabilitiesBNK(Enum):
    """"外国為替、負債の部、銀行業"""
    INTERIM_INSTANT = 'InterimInstant'
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class FreightageAndPackingExpensesSGA(Enum):
    """"運賃及び荷造費、販売費及び一般管理費"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class FreightageExpensesSGA(Enum):
    """"運賃、販売費及び一般管理費"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class GainOnAdjustmentOfAccountPayableNOI(Enum):
    """"債務勘定整理益、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class GainOnBadDebtsRecoveredNOI(Enum):
    """"償却債権取立益、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class GainOnChangeInEquityEI(Enum):
    """"持分変動利益、特別利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class GainOnDisposalOfNoncurrentAssetsEI(Enum):
    """"固定資産処分益、特別利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    INTERIM_DURATION = 'InterimDuration'
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    INTERIM_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'InterimDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    INTERIM_DURATION__RECONCILING_ITEMS_MEMBER = 'InterimDuration_ReconcilingItemsMember'
    """ 調整項目 """
    INTERIM_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'InterimDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    INTERIM_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'InterimDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_INTERIM_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'Prior1InterimDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    PRIOR1_INTERIM_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1InterimDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_INTERIM_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'Prior1InterimDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    PRIOR1_INTERIM_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1InterimDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class GainOnDisposalOfNoncurrentAssetsNOI(Enum):
    """"固定資産処分益、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class GainOnDonationOfNoncurrentAssetsEI(Enum):
    """"固定資産受贈益、特別利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class GainOnDonationOfNoncurrentAssetsNOI(Enum):
    """"固定資産受贈益、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class GainOnDonationOfNoncurrentAssetsOpeCF(Enum):
    """"固定資産受贈益、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class GainOnExtinguishmentOfTieInSharesEI(Enum):
    """"抱合せ株式消滅差益、特別利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class GainOnForfeitureOfUnclaimedDividendsNOI(Enum):
    """"未払配当金除斥益、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class GainOnForgivenessOfDebtOpeCF(Enum):
    """"債務免除益、営業活動によるキャッシュ・フロー"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class GainOnForgivenessOfDebtsEI(Enum):
    """"債務免除益、特別利益"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class GainOnFundManagementOpeCFBNK(Enum):
    """"資金運用収益、営業活動によるキャッシュ・フロー、銀行業"""
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'


class GainOnInsuranceAdjustmentEI(Enum):
    """"保険差益、特別利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class GainOnInvestmentOfSecuritiesNOI(Enum):
    """"有価証券運用益、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class GainOnInvestmentsInCapitalNOI(Enum):
    """"出資金運用益、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class GainOnInvestmentsInPartnershipNOI(Enum):
    """"投資事業組合運用益、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class GainOnInvestmentsInSilentPartnershipNOI(Enum):
    """"匿名組合投資利益、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class GainOnLiquidationOfSubsidiariesAndAffiliatesEI(Enum):
    """"関係会社清算益、特別利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class GainOnLiquidationOfSubsidiariesEI(Enum):
    """"子会社清算益、特別利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class GainOnNegativeGoodwillEI(Enum):
    """"負ののれん発生益、特別利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class GainOnNegativeGoodwillOpeCF(Enum):
    """"負ののれん発生益、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class GainOnRedemptionOfInvestmentSecuritiesEI(Enum):
    """"投資有価証券償還益、特別利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class GainOnRedemptionOfSecuritiesNOI(Enum):
    """"有価証券償還益、営業外収益"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class GainOnReversalOfAssetRetirementObligationsEI(Enum):
    """"資産除去債務戻入益、特別利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class GainOnReversalOfProvisionForLossOnDisasterEI(Enum):
    """"災害損失引当金戻入額、特別利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class GainOnReversalOfSubscriptionRightsToSharesEI(Enum):
    """"新株予約権戻入益、特別利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class GainOnReversalOfSubscriptionRightsToSharesOpeCF(Enum):
    """"新株予約権戻入益、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class GainOnRevisionOfRetirementBenefitPlanEI(Enum):
    """"退職給付制度改定益、特別利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class GainOnSalesOfGolfMembershipsEI(Enum):
    """"ゴルフ会員権売却益、特別利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class GainOnSalesOfGoodsNOI(Enum):
    """"物品売却益、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class GainOnSalesOfInvestmentSecuritiesEI(Enum):
    """"投資有価証券売却益、特別利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class GainOnSalesOfInvestmentSecuritiesNOI(Enum):
    """"投資有価証券売却益、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class GainOnSalesOfMembershipsEI(Enum):
    """"会員権売却益、特別利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class GainOnSalesOfNonCurrentAssetsOpeCF(Enum):
    """"固定資産売却益、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class GainOnSalesOfNoncurrentAssetsEI(Enum):
    """"固定資産売却益、特別利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class GainOnSalesOfNoncurrentAssetsNOI(Enum):
    """"固定資産売却益、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class GainOnSalesOfPropertyPlantAndEquipmentEI(Enum):
    """"有形固定資産売却益、特別利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class GainOnSalesOfScraps1NOI(Enum):
    """"作業くず売却益、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class GainOnSalesOfScraps2NOI(Enum):
    """"スクラップ売却益、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class GainOnSalesOfSecuritiesOIINS(Enum):
    """"有価証券売却益、経常収益、保険業"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class GainOnSalesOfSubsidiariesAndAffiliatesStocksEI(Enum):
    """"関係会社株式売却益、特別利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    INTERIM_DURATION = 'InterimDuration'
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class GainOnSalesOfSubsidiariesStocksEI(Enum):
    """"子会社株式売却益、特別利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class GainOnStepAcquisitionsEI(Enum):
    """"段階取得に係る差益、特別利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class GainOnTransferOfBusinessEI(Enum):
    """"事業譲渡益、特別利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    INTERIM_DURATION = 'InterimDuration'
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class GainOnValuationOfCompoundFinancialInstrumentsNOI(Enum):
    """"複合金融商品評価益、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class GainOnValuationOfDerivativesNOI(Enum):
    """"デリバティブ評価益、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class GainOnValuationOfInvestmentSecuritiesNOI(Enum):
    """"投資有価証券評価益、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class GainOnValuationOfSecuritiesNOI(Enum):
    """"有価証券評価益、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class GeneralAndAdministrativeExpensesOEBNK(Enum):
    """"営業経費、経常費用、銀行業"""
    INTERIM_DURATION = 'InterimDuration'
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class GeneralAndAdministrativeExpensesSGA(Enum):
    """"一般管理費、販売費及び一般管理費"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class GeneralReserve(Enum):
    """"別途積立金"""
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class GolfClubMembership(Enum):
    """"ゴルフ会員権"""
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class GolfCourses(Enum):
    """"コース勘定"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class Goodwill(Enum):
    """"のれん"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'CurrentYearInstant_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ 当年度時点その他 """
    CURRENT_YEAR_INSTANT__OTHER_REPORTABLE_SEGMENTS_MEMBER = 'CurrentYearInstant_OtherReportableSegmentsMember'
    """ 当年度時点その他 """
    CURRENT_YEAR_INSTANT__REPORTABLE_SEGMENTS_MEMBER = 'CurrentYearInstant_ReportableSegmentsMember'
    """ 当年度時点報告セグメント """
    CURRENT_YEAR_INSTANT__UNALLOCATED_AMOUNTS_AND_ELIMINATION_MEMBER = 'CurrentYearInstant_UnallocatedAmountsAndEliminationMember'
    """ 当年度時点全社・消去 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'Prior1YearInstant_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    PRIOR1_YEAR_INSTANT__OTHER_REPORTABLE_SEGMENTS_MEMBER = 'Prior1YearInstant_OtherReportableSegmentsMember'
    """ その他 """
    PRIOR1_YEAR_INSTANT__UNALLOCATED_AMOUNTS_AND_ELIMINATION_MEMBER = 'Prior1YearInstant_UnallocatedAmountsAndEliminationMember'
    """ 全社・消去 """


class GrossProfit(Enum):
    """"売上総利益又は売上総損失（△）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YTD_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'CurrentYTDDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    CURRENT_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'CurrentYTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    CURRENT_YTD_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'CurrentYTDDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    CURRENT_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'CurrentYTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'Prior1YTDDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    PRIOR1_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1YTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_YTD_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'Prior1YTDDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    PRIOR1_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1YTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class GrossProfitMerchandiseGP(Enum):
    """"商品売上総利益又は商品売上総損失（△）、売上総利益"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class GrossProfitOnCompletedConstructionContractsCNS(Enum):
    """"完成工事総利益又は完成工事総損失（△）、建設業"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class GrossProfitOnRealEstateBusinessAndOtherCNS(Enum):
    """"不動産事業等総利益又は不動産事業等総損失（△）、建設業"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class GrossProfitOnSideLineBusinessCNS(Enum):
    """"兼業事業総利益又は兼業事業総損失（△）、建設業"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class GrossProfitOtherBusinessGP(Enum):
    """"その他の事業総利益又はその他の事業総損失（△）、売上総利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class GrossProfitRealEstateBusinessGP(Enum):
    """"不動産事業総利益又は不動産事業総損失（△）、売上総利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class GuaranteeCommissionNOE(Enum):
    """"支払保証料、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class GuaranteeCommissionReceivedNOI(Enum):
    """"受取保証料、営業外収益"""
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class GuaranteeDepositsCACMD(Enum):
    """"差入保証金、流動資産、商品先物取引業"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class GuaranteeDepositsIOA(Enum):
    """"差入保証金、投資その他の資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class GuaranteeDepositsReceived2NCL(Enum):
    """"預り保証金、固定負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class GuaranteeDepositsReceivedCLSEC(Enum):
    """"受入保証金、流動負債、第一種金融商品取引業"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class GuaranteeDepositsReceivedNCL(Enum):
    """"受入保証金、固定負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class GuaranteeReceivedNCLLEA(Enum):
    """"受取保証金、固定負債、リース事業"""
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class HaulageExpensesSGA(Enum):
    """"運搬費、販売費及び一般管理費"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class HeadOfficeTransferCostEL(Enum):
    """"本社移転費用、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class HouseRentIncomeNOI(Enum):
    """"受取家賃、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class ImpairmentLossEL(Enum):
    """"減損損失、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__OTHER_REPORTABLE_SEGMENTS_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_OtherReportableSegmentsMember'
    """ 当年度会計期間個別又は非連結その他 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__UNALLOCATED_AMOUNTS_AND_ELIMINATION_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_UnallocatedAmountsAndEliminationMember'
    """ 当年度会計期間個別又は非連結全社・消去 """
    CURRENT_YEAR_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'CurrentYearDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ 当年度会計期間その他 """
    CURRENT_YEAR_DURATION__RECONCILING_ITEMS_MEMBER = 'CurrentYearDuration_ReconcilingItemsMember'
    """ 当年度会計期間調整項目 """
    CURRENT_YEAR_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'CurrentYearDuration_ReportableSegmentsMember'
    """ 当年度会計期間報告セグメント """
    CURRENT_YEAR_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'CurrentYearDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 当年度会計期間事業セグメント合計 """
    CURRENT_YEAR_DURATION__UNALLOCATED_AMOUNTS_AND_ELIMINATION_MEMBER = 'CurrentYearDuration_UnallocatedAmountsAndEliminationMember'
    """ 当年度会計期間全社・消去 """
    INTERIM_DURATION = 'InterimDuration'
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    INTERIM_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'InterimDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    INTERIM_DURATION__RECONCILING_ITEMS_MEMBER = 'InterimDuration_ReconcilingItemsMember'
    """ 調整項目 """
    INTERIM_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'InterimDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    INTERIM_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'InterimDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_INTERIM_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'Prior1InterimDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    PRIOR1_INTERIM_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1InterimDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_INTERIM_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'Prior1InterimDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    PRIOR1_INTERIM_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1InterimDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__OTHER_REPORTABLE_SEGMENTS_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_OtherReportableSegmentsMember'
    """ 個別又は非連結その他 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__UNALLOCATED_AMOUNTS_AND_ELIMINATION_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_UnallocatedAmountsAndEliminationMember'
    """ 個別又は非連結全社・消去 """
    PRIOR1_YEAR_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'Prior1YearDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    PRIOR1_YEAR_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1YearDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_YEAR_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'Prior1YearDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    PRIOR1_YEAR_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1YearDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """


class ImpairmentLossOpeCF(Enum):
    """"減損損失、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class IncomeBeforeDividendsDistributionFromSilentPartnershipIncomeTaxes(Enum):
    """"匿名組合損益分配前税引前当期純利益又は純損失（△）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncomeBeforeIncomeTaxes(Enum):
    """"税引前当期純利益又は税引前当期純損失（△）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    INTERIM_DURATION = 'InterimDuration'
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class IncomeTaxes(Enum):
    """"法人税等"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    INTERIM_DURATION = 'InterimDuration'
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class IncomeTaxesCurrent(Enum):
    """"法人税、住民税及び事業税"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    INTERIM_DURATION = 'InterimDuration'
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class IncomeTaxesCurrentConsolidatedINS(Enum):
    """"法人税及び住民税等、保険業"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncomeTaxesDeferred(Enum):
    """"法人税等調整額"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    INTERIM_DURATION = 'InterimDuration'
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class IncomeTaxesPaidOpeCF(Enum):
    """"法人税等の支払額、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class IncomeTaxesPaidRefundOpeCF(Enum):
    """"法人税等の支払額又は還付額（△は支払）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class IncomeTaxesPayable(Enum):
    """"未払法人税等"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class IncomeTaxesReceivable(Enum):
    """"未収還付法人税等"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class IncomeTaxesRefundOpeCF(Enum):
    """"法人税等の還付額、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class IncreaseDecreaseInAccountsPayableOtherAndAccruedExpensesOpeCF(Enum):
    """"未払金及び未払費用の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class IncreaseDecreaseInAccountsPayableOtherOpeCF(Enum):
    """"未払金の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class IncreaseDecreaseInAccruedConsumptionTaxesOpeCF(Enum):
    """"未払消費税等の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class IncreaseDecreaseInAccruedExpensesOpeCF(Enum):
    """"未払費用の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class IncreaseDecreaseInAccruedLiabilitiesOpeCF(Enum):
    """"未払債務の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInAdvancesReceivedOnUncompletedConstructionContractsOpeCFCNS(Enum):
    """"未成工事受入金の増減額（△は減少）、営業活動によるキャッシュ・フロー、建設業"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class IncreaseDecreaseInAdvancesReceivedOpeCF(Enum):
    """"前受金の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class IncreaseDecreaseInAllowanceForDoubtfulAccountsOpeCF(Enum):
    """"貸倒引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class IncreaseDecreaseInAllowanceForInvestmentLossOpeCF(Enum):
    """"投資損失引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInAllowanceForLoanLossesOpeCFBNK(Enum):
    """"貸倒引当金の増減（△）、営業活動によるキャッシュ・フロー、銀行業"""
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'


class IncreaseDecreaseInCashAndCashEquivalentsResultingFromChangeOfScopeOfConsolidationCCE(Enum):
    """"連結の範囲の変更に伴う現金及び現金同等物の増減額（△は減少）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class IncreaseDecreaseInCommercialPapersFinCF(Enum):
    """"コマーシャル・ペーパーの増減額（△は減少）、財務活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInContractLiabilitiesOpeCF(Enum):
    """"契約負債の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class IncreaseDecreaseInCustomersDepositsReceivedForCommodityFuturesTransactionOpeCFCMD(Enum):
    """"預り証拠金の増減額（△は減少）、営業活動によるキャッシュ・フロー、商品先物取引業"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInDepositsReceivedOpeCF(Enum):
    """"預り金の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class IncreaseDecreaseInGuaranteeDepositsReceivedOpeCF(Enum):
    """"預り保証金の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class IncreaseDecreaseInGuaranteeDepositsReceivedOpeCFSEC(Enum):
    """"受入保証金の増減額（△は減少）、営業活動によるキャッシュ・フロー、第一種金融商品取引業"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInIncomeTaxesPayableTheFactorBasedTaxOpeCF(Enum):
    """"未払法人税等（外形標準課税）の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class IncreaseDecreaseInLeaseAndGuaranteeDepositsReceivedOpeCF(Enum):
    """"預り敷金及び保証金の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInLongTermAccountsPayableOtherOpeCF(Enum):
    """"長期未払金の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class IncreaseDecreaseInNetDefinedBenefitAssetOpeCF(Enum):
    """"退職給付に係る資産の増減額（△は増加）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class IncreaseDecreaseInNetDefinedBenefitLiabilityOpeCF(Enum):
    """"退職給付に係る負債の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class IncreaseDecreaseInNotesAndAccountsPayableTradeOpeCF(Enum):
    """"仕入債務の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class IncreaseDecreaseInNotesDiscountedOpeCF(Enum):
    """"割引手形の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class IncreaseDecreaseInOperatingDebtOpeCF(Enum):
    """"営業債務の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInOtherAssetsLiabilitiesOpeCF(Enum):
    """"その他の資産・負債の増減額、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInOtherCurrentLiabilitiesOpeCF(Enum):
    """"その他の流動負債の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class IncreaseDecreaseInOtherInvestingAndFinancingActivitiesLiabilitiesOpeCFINS(Enum):
    """"その他負債（除く投資活動関連、財務活動関連）の増減額（△は減少）、営業活動によるキャッシュ・フロー、保険業"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInOtherLiabilitiesOpeCF(Enum):
    """"その他の負債の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class IncreaseDecreaseInOtherNoncurrentLiabilitiesOpeCF(Enum):
    """"その他の固定負債の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInOtherProvisionOpeCF(Enum):
    """"その他の引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class IncreaseDecreaseInOutstandingClaimsOpeCFINS(Enum):
    """"支払備金の増減額（△は減少）、営業活動によるキャッシュ・フロー、保険業"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInPolicyReserveOpeCFINS(Enum):
    """"責任準備金の増減額（△は減少）、営業活動によるキャッシュ・フロー、保険業"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInProvisionForBonusesOpeCF(Enum):
    """"賞与引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class IncreaseDecreaseInProvisionForContingentLossOpeCF(Enum):
    """"偶発損失引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInProvisionForDirectorsBonusesOpeCF(Enum):
    """"役員賞与引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class IncreaseDecreaseInProvisionForDirectorsRetirementBenefitsOpeCF(Enum):
    """"役員退職慰労引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class IncreaseDecreaseInProvisionForEnvironmentalMeasuresOpeCF(Enum):
    """"環境対策引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInProvisionForLossOnConstructionContractsOpeCF(Enum):
    """"工事損失引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class IncreaseDecreaseInProvisionForLossOnGuaranteesOpeCF(Enum):
    """"債務保証損失引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class IncreaseDecreaseInProvisionForLossOnInterestRepaymentOpeCF(Enum):
    """"利息返還損失引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInProvisionForLossOnLiquidationOfSubsidiariesAndAffiliatesOpeCF(Enum):
    """"関係会社整理損失引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInProvisionForLossOnLitigationOpeCF(Enum):
    """"訴訟損失引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInProvisionForLossOnOrderReceivedOpeCF(Enum):
    """"受注損失引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class IncreaseDecreaseInProvisionForLossOnStoreClosingOpeCF(Enum):
    """"店舗閉鎖損失引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class IncreaseDecreaseInProvisionForPointCardCertificatesOpeCF(Enum):
    """"ポイント引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInProvisionForProductWarrantiesOpeCF(Enum):
    """"製品保証引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class IncreaseDecreaseInProvisionForReimbursementOfDepositsOpeCFBNK(Enum):
    """"睡眠預金払戻損失引当金の増減（△）、営業活動によるキャッシュ・フロー、銀行業"""
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'


class IncreaseDecreaseInProvisionForRepairsOpeCF(Enum):
    """"修繕引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInProvisionForRetirementBenefitsAndDirectorsRetirementBenefitsOpeCF(Enum):
    """"退職給付及び役員退職慰労引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInProvisionForRetirementBenefitsOpeCF(Enum):
    """"退職給付引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class IncreaseDecreaseInProvisionForSalesPromotionExpensesOpeCF(Enum):
    """"販売促進引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class IncreaseDecreaseInProvisionForShareBasedPaymentsOpeCF(Enum):
    """"株式報酬引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class IncreaseDecreaseInProvisionForShareBasedRemunerationForDirectorsAndOtherOfficersOpeCF(Enum):
    """"役員株式給付引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class IncreaseDecreaseInProvisionForShareBasedRemunerationOpeCF(Enum):
    """"株式給付引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class IncreaseDecreaseInProvisionForShareholderBenefitProgramOpeCF(Enum):
    """"株主優待引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class IncreaseDecreaseInProvisionForSpecialRepairsOpeCF(Enum):
    """"特別修繕引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInProvisionForWarrantiesForCompletedConstructionOpeCF(Enum):
    """"完成工事補償引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInProvisionOpeCF(Enum):
    """"引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class IncreaseDecreaseInReserveForPriceFluctuationOpeCFINS(Enum):
    """"価格変動準備金の増減額（△は減少）、営業活動によるキャッシュ・フロー、保険業"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInReservesUnderTheSpecialLaws2OpeCF(Enum):
    """"特別法上の引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'


class IncreaseDecreaseInShortTermBankLoansAndCommercialPapersFinCF(Enum):
    """"短期借入金及びコマーシャル・ペーパーの増減額（△は減少）、財務活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInShortTermLoansPayableFinCF(Enum):
    """"短期借入金の増減額（△は減少）、財務活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class IncreaseDecreaseInUnearnedRevenueOpeCF(Enum):
    """"前受収益の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class IncreaseInCashAndCashEquivalentsFromNewlyConsolidatedSubsidiaryCCE(Enum):
    """"新規連結に伴う現金及び現金同等物の増加額"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class IncreaseInCashAndCashEquivalentsResultingFromMergerCCE(Enum):
    """"合併に伴う現金及び現金同等物の増加額"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class IncreaseInCashAndCashEquivalentsResultingFromMergerWithUnconsolidatedSubsidiariesCCE(Enum):
    """"非連結子会社との合併に伴う現金及び現金同等物の増加額"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class IncreaseInMoneyHeldInTrustInvCFBNK(Enum):
    """"金銭の信託の増加による支出、投資活動によるキャッシュ・フロー、銀行業"""
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'


class IncreaseInShortTermLoansPayableFinCF(Enum):
    """"短期借入れによる収入、財務活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class InsuranceAndDividendsIncomeNOI(Enum):
    """"受取保険金及び配当金、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class InsuranceExpensesSGA(Enum):
    """"保険料、販売費及び一般管理費"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class InsuranceFeeNOI(Enum):
    """"受取保険料、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class InsuranceFunds(Enum):
    """"保険積立金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class InsuranceFundsForDirectors(Enum):
    """"役員に対する保険積立金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class InsuranceIncomeEI(Enum):
    """"受取保険金、特別利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class InsuranceIncomeNOI(Enum):
    """"受取保険金、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class InsuranceIncomeOpeCF(Enum):
    """"受取保険金、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class InsurancePremiumsRefundedCancellationNOI(Enum):
    """"保険解約返戻金、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class InsuranceReturnNOI(Enum):
    """"保険返戻金、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IntangibleAssets(Enum):
    """"無形固定資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    INTERIM_INSTANT = 'InterimInstant'
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class InterestAndDividendsIncomeNOI(Enum):
    """"受取利息及び配当金、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class InterestAndDividendsIncomeOIINS(Enum):
    """"利息及び配当金収入、経常収益、保険業"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class InterestAndDividendsIncomeOpeCF(Enum):
    """"受取利息及び受取配当金、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class InterestAndDividendsIncomeOpeCFINSNonlife(Enum):
    """"利息及び配当金収入、営業活動によるキャッシュ・フロー、保険業、損害保険"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class InterestAndDividendsIncomeReceivedOpeCFInvCF(Enum):
    """"利息及び配当金の受取額、営業活動によるキャッシュ・フロー又は投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class InterestAndDividendsOnSecuritiesOIBNK(Enum):
    """"有価証券利息配当金、経常収益、銀行業"""
    INTERIM_DURATION = 'InterimDuration'
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class InterestExpensesAndLossOnSalesOfNotesReceivableTradeOpeCF(Enum):
    """"支払利息及び手形売却損、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class InterestExpensesNOE(Enum):
    """"支払利息、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    CURRENT_YEAR_DURATION__RECONCILING_ITEMS_MEMBER = 'CurrentYearDuration_ReconcilingItemsMember'
    """ 当年度会計期間調整項目 """
    CURRENT_YEAR_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'CurrentYearDuration_ReportableSegmentsMember'
    """ 当年度会計期間報告セグメント """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1YearDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_YEAR_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'Prior1YearDuration_ReportableSegmentsMember'
    """ 報告セグメント """


class InterestExpensesOEBNK(Enum):
    """"資金調達費用、経常費用、銀行業"""
    INTERIM_DURATION = 'InterimDuration'
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    INTERIM_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'InterimDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    INTERIM_DURATION__RECONCILING_ITEMS_MEMBER = 'InterimDuration_ReconcilingItemsMember'
    """ 調整項目 """
    INTERIM_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'InterimDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    INTERIM_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'InterimDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_INTERIM_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'Prior1InterimDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    PRIOR1_INTERIM_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1InterimDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_INTERIM_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'Prior1InterimDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    PRIOR1_INTERIM_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1InterimDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """


class InterestExpensesOEINS(Enum):
    """"支払利息、経常費用、保険業"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class InterestExpensesOpeCF(Enum):
    """"支払利息、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class InterestExpensesPaidOnLoansAndBondsOpeCF(Enum):
    """"支払利息及び社債利息、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class InterestExpensesPaidOpeCFFinCF(Enum):
    """"利息の支払額、営業活動によるキャッシュ・フロー又は財務活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class InterestIncomeNOI(Enum):
    """"受取利息、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    CURRENT_YEAR_DURATION__RECONCILING_ITEMS_MEMBER = 'CurrentYearDuration_ReconcilingItemsMember'
    """ 当年度会計期間調整項目 """
    CURRENT_YEAR_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'CurrentYearDuration_ReportableSegmentsMember'
    """ 当年度会計期間報告セグメント """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1YearDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_YEAR_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'Prior1YearDuration_ReportableSegmentsMember'
    """ 報告セグメント """


class InterestIncomeOIBNK(Enum):
    """"資金運用収益、経常収益、銀行業"""
    INTERIM_DURATION = 'InterimDuration'
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    INTERIM_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'InterimDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    INTERIM_DURATION__RECONCILING_ITEMS_MEMBER = 'InterimDuration_ReconcilingItemsMember'
    """ 調整項目 """
    INTERIM_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'InterimDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    INTERIM_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'InterimDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_INTERIM_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'Prior1InterimDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    PRIOR1_INTERIM_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1InterimDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_INTERIM_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'Prior1InterimDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    PRIOR1_INTERIM_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1InterimDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """


class InterestIncomeOnSecuritiesOpeCF(Enum):
    """"有価証券利息、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class InterestIncomeOpeCF(Enum):
    """"受取利息、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class InterestIncomeReceivedOpeCF(Enum):
    """"利息の受取額、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class InterestOnBondsNOE(Enum):
    """"社債利息、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class InterestOnBondsOpeCF(Enum):
    """"社債利息、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class InterestOnDepositsOEBNK(Enum):
    """"預金利息、経常費用、銀行業"""
    INTERIM_DURATION = 'InterimDuration'
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class InterestOnLoansAndDiscountsOIBNK(Enum):
    """"貸出金利息、経常収益、銀行業"""
    INTERIM_DURATION = 'InterimDuration'
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class InterestOnOperatingLoansSPF(Enum):
    """"営業貸付金利息、特定金融業"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class InterestOnPayablesUnderSecuritiesLendingTransactionsOEBNK(Enum):
    """"債券貸借取引支払利息、経常費用、銀行業"""
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'


class InterestOnRefundNOI(Enum):
    """"還付加算金、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class InterestOnSecuritiesNOI(Enum):
    """"有価証券利息、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class Inventories(Enum):
    """"棚卸資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class InvestmentExpensesOEINS(Enum):
    """"資産運用費用、経常費用、保険業"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class InvestmentIncomeOIINS(Enum):
    """"資産運用収益、経常収益、保険業"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class InvestmentSecurities(Enum):
    """"投資有価証券"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class InvestmentsAndOtherAssets(Enum):
    """"投資その他の資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class InvestmentsAndOtherAssetsGross(Enum):
    """"投資その他の資産（総額）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class InvestmentsInCapital(Enum):
    """"出資金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class InvestmentsInCapitalOfSubsidiariesAndAffiliates(Enum):
    """"関係会社出資金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class IssuanceOfNewShares(Enum):
    """"新株の発行"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__CAPITAL_STOCK_MEMBER = 'CurrentYearDuration_CapitalStockMember'
    """ 当年度会計期間資本金 """
    CURRENT_YEAR_DURATION__CAPITAL_SURPLUS_MEMBER = 'CurrentYearDuration_CapitalSurplusMember'
    """ 当年度会計期間資本剰余金 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CAPITAL_STOCK_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_CapitalStockMember'
    """ 当年度会計期間個別又は非連結資本金 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CAPITAL_SURPLUS_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_CapitalSurplusMember'
    """ 当年度会計期間個別又は非連結資本剰余金 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__LEGAL_CAPITAL_SURPLUS_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_LegalCapitalSurplusMember'
    """ 当年度会計期間個別又は非連結資本準備金 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_BROUGHT_FORWARD_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_RetainedEarningsBroughtForwardMember'
    """ 当年度会計期間個別又は非連結繰越利益剰余金 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_RetainedEarningsMember'
    """ 当年度会計期間個別又は非連結利益剰余金 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__SHAREHOLDERS_EQUITY_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_ShareholdersEquityMember'
    """ 当年度会計期間個別又は非連結株主資本 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__SUBSCRIPTION_RIGHTS_TO_SHARES_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_SubscriptionRightsToSharesMember'
    """ 当年度会計期間個別又は非連結新株予約権 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__TREASURY_STOCK_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_TreasuryStockMember'
    """ 当年度会計期間個別又は非連結自己株式 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__VALUATION_AND_TRANSLATION_ADJUSTMENTS_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_ValuationAndTranslationAdjustmentsMember'
    """ 当年度会計期間個別又は非連結評価・換算差額等 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__VALUATION_DIFFERENCE_ON_AVAILABLE_FOR_SALE_SECURITIES_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_ValuationDifferenceOnAvailableForSaleSecuritiesMember'
    """ 当年度会計期間個別又は非連結その他有価証券評価差額金 """
    CURRENT_YEAR_DURATION__NON_CONTROLLING_INTERESTS_MEMBER = 'CurrentYearDuration_NonControllingInterestsMember'
    """ 当年度会計期間非支配株主持分 """
    CURRENT_YEAR_DURATION__RETAINED_EARNINGS_MEMBER = 'CurrentYearDuration_RetainedEarningsMember'
    """ 当年度会計期間利益剰余金 """
    CURRENT_YEAR_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'CurrentYearDuration_ShareholdersEquityMember'
    """ 当年度会計期間株主資本 """
    CURRENT_YEAR_DURATION__SUBSCRIPTION_RIGHTS_TO_SHARES_MEMBER = 'CurrentYearDuration_SubscriptionRightsToSharesMember'
    """ 当年度会計期間新株予約権 """
    CURRENT_YEAR_DURATION__TREASURY_STOCK_MEMBER = 'CurrentYearDuration_TreasuryStockMember'
    """ 当年度会計期間自己株式 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__CAPITAL_STOCK_MEMBER = 'Prior1YearDuration_CapitalStockMember'
    """ 資本金 """
    PRIOR1_YEAR_DURATION__CAPITAL_SURPLUS_MEMBER = 'Prior1YearDuration_CapitalSurplusMember'
    """ 資本剰余金 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CAPITAL_STOCK_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_CapitalStockMember'
    """ 個別又は非連結資本金 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CAPITAL_SURPLUS_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_CapitalSurplusMember'
    """ 個別又は非連結資本剰余金 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__LEGAL_CAPITAL_SURPLUS_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_LegalCapitalSurplusMember'
    """ 個別又は非連結資本準備金 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_BROUGHT_FORWARD_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_RetainedEarningsBroughtForwardMember'
    """ 個別又は非連結繰越利益剰余金 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_RetainedEarningsMember'
    """ 個別又は非連結利益剰余金 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_ShareholdersEquityMember'
    """ 個別又は非連結株主資本 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__SUBSCRIPTION_RIGHTS_TO_SHARES_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_SubscriptionRightsToSharesMember'
    """ 個別又は非連結新株予約権 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__TREASURY_STOCK_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_TreasuryStockMember'
    """ 個別又は非連結自己株式 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__VALUATION_AND_TRANSLATION_ADJUSTMENTS_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_ValuationAndTranslationAdjustmentsMember'
    """ 個別又は非連結評価・換算差額等 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__VALUATION_DIFFERENCE_ON_AVAILABLE_FOR_SALE_SECURITIES_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_ValuationDifferenceOnAvailableForSaleSecuritiesMember'
    """ 個別又は非連結その他有価証券評価差額金 """
    PRIOR1_YEAR_DURATION__NON_CONTROLLING_INTERESTS_MEMBER = 'Prior1YearDuration_NonControllingInterestsMember'
    """ 非支配株主持分 """
    PRIOR1_YEAR_DURATION__RETAINED_EARNINGS_MEMBER = 'Prior1YearDuration_RetainedEarningsMember'
    """ 利益剰余金 """
    PRIOR1_YEAR_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1YearDuration_ShareholdersEquityMember'
    """ 株主資本 """
    PRIOR1_YEAR_DURATION__SUBSCRIPTION_RIGHTS_TO_SHARES_MEMBER = 'Prior1YearDuration_SubscriptionRightsToSharesMember'
    """ 新株予約権 """
    PRIOR1_YEAR_DURATION__TREASURY_STOCK_MEMBER = 'Prior1YearDuration_TreasuryStockMember'
    """ 自己株式 """


class IssuanceOfNewSharesexerciseOfSubscriptionRightsToShares(Enum):
    """"新株の発行（新株予約権の行使）"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__CAPITAL_STOCK_MEMBER = 'CurrentYearDuration_CapitalStockMember'
    """ 当年度会計期間資本金 """
    CURRENT_YEAR_DURATION__CAPITAL_SURPLUS_MEMBER = 'CurrentYearDuration_CapitalSurplusMember'
    """ 当年度会計期間資本剰余金 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CAPITAL_STOCK_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_CapitalStockMember'
    """ 当年度会計期間個別又は非連結資本金 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CAPITAL_SURPLUS_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_CapitalSurplusMember'
    """ 当年度会計期間個別又は非連結資本剰余金 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__LEGAL_CAPITAL_SURPLUS_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_LegalCapitalSurplusMember'
    """ 当年度会計期間個別又は非連結資本準備金 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__SHAREHOLDERS_EQUITY_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_ShareholdersEquityMember'
    """ 当年度会計期間個別又は非連結株主資本 """
    CURRENT_YEAR_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'CurrentYearDuration_ShareholdersEquityMember'
    """ 当年度会計期間株主資本 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CAPITAL_STOCK_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_CapitalStockMember'
    """ 個別又は非連結資本金 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CAPITAL_SURPLUS_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_CapitalSurplusMember'
    """ 個別又は非連結資本剰余金 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__LEGAL_CAPITAL_SURPLUS_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_LegalCapitalSurplusMember'
    """ 個別又は非連結資本準備金 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_ShareholdersEquityMember'
    """ 個別又は非連結株主資本 """


class IssuanceOfSubscriptionRightsToShares(Enum):
    """"新株予約権の発行"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__SUBSCRIPTION_RIGHTS_TO_SHARES_MEMBER = 'CurrentYearDuration_SubscriptionRightsToSharesMember'
    """ 当年度会計期間新株予約権 """


class Land(Enum):
    """"土地"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class LandAndBuildingsForSaleCARWY(Enum):
    """"販売土地及び建物、流動資産、鉄道事業"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class LandAndBuildingsForSaleInLots(Enum):
    """"分譲土地建物"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class LandAndHouseRentReceivedNOI(Enum):
    """"受取地代家賃、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class LandInTrust(Enum):
    """"信託土地"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class LapseOfSubscriptionRightsToShares(Enum):
    """"新株予約権の失効"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'CurrentYearDuration_ShareholdersEquityMember'
    """ 当年度会計期間株主資本 """
    CURRENT_YEAR_DURATION__SUBSCRIPTION_RIGHTS_TO_SHARES_MEMBER = 'CurrentYearDuration_SubscriptionRightsToSharesMember'
    """ 当年度会計期間新株予約権 """
    CURRENT_YEAR_DURATION__VALUATION_AND_TRANSLATION_ADJUSTMENTS_MEMBER = 'CurrentYearDuration_ValuationAndTranslationAdjustmentsMember'
    """ 当年度会計期間評価・換算差額等 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1YearDuration_ShareholdersEquityMember'
    """ 株主資本 """
    PRIOR1_YEAR_DURATION__SUBSCRIPTION_RIGHTS_TO_SHARES_MEMBER = 'Prior1YearDuration_SubscriptionRightsToSharesMember'
    """ 新株予約権 """
    PRIOR1_YEAR_DURATION__VALUATION_AND_TRANSLATION_ADJUSTMENTS_MEMBER = 'Prior1YearDuration_ValuationAndTranslationAdjustmentsMember'
    """ 評価・換算差額等 """


class LeaseAndGuaranteeDeposits(Enum):
    """"敷金及び保証金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class LeaseAndGuaranteeDepositsReceived(Enum):
    """"受入敷金保証金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class LeaseAssetsIA(Enum):
    """"リース資産、無形固定資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class LeaseAssetsNetPPE(Enum):
    """"リース資産（純額）、有形固定資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class LeaseAssetsPPE(Enum):
    """"リース資産、有形固定資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class LeaseDepositsIOA(Enum):
    """"敷金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class LeaseInvestmentAssetsCA(Enum):
    """"リース投資資産、流動資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class LeaseInvestmentAssetsIOA(Enum):
    """"リース投資資産、投資その他の資産"""
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class LeaseObligationsCL(Enum):
    """"リース債務、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class LeaseObligationsLiabilities(Enum):
    """"リース債務、負債の部"""
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class LeaseObligationsNCL(Enum):
    """"リース債務、固定負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class LeasePropertyIALEA(Enum):
    """"賃貸資産、無形固定資産、リース事業"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class LeaseReceivablesAndInvestmentAssetsCA(Enum):
    """"リース債権及びリース投資資産、流動資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    INTERIM_INSTANT = 'InterimInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class LeasedAssetsPPELEA(Enum):
    """"賃貸資産、合計、有形固定資産、リース事業"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class LeaseholdRight(Enum):
    """"借地権"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class LegalAndEmployeeBenefitsExpensesSGA(Enum):
    """"法定福利及び厚生費、販売費及び一般管理費"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LegalCapitalSurplus(Enum):
    """"資本準備金"""
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class LegalRetainedEarnings(Enum):
    """"利益準備金"""
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class LegalWelfareExpensesSGA(Enum):
    """"法定福利費、販売費及び一般管理費"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class Liabilities(Enum):
    """"負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    CURRENT_YEAR_INSTANT__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'CurrentYearInstant_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ 当年度時点その他 """
    CURRENT_YEAR_INSTANT__RECONCILING_ITEMS_MEMBER = 'CurrentYearInstant_ReconcilingItemsMember'
    """ 当年度時点調整項目 """
    CURRENT_YEAR_INSTANT__REPORTABLE_SEGMENTS_MEMBER = 'CurrentYearInstant_ReportableSegmentsMember'
    """ 当年度時点報告セグメント """
    CURRENT_YEAR_INSTANT__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'CurrentYearInstant_TotalOfReportableSegmentsAndOthersMember'
    """ 当年度時点事業セグメント合計 """
    INTERIM_INSTANT = 'InterimInstant'
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    INTERIM_INSTANT__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'InterimInstant_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    INTERIM_INSTANT__RECONCILING_ITEMS_MEMBER = 'InterimInstant_ReconcilingItemsMember'
    """ 調整項目 """
    INTERIM_INSTANT__REPORTABLE_SEGMENTS_MEMBER = 'InterimInstant_ReportableSegmentsMember'
    """ 報告セグメント """
    INTERIM_INSTANT__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'InterimInstant_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    PRIOR1_INTERIM_INSTANT = 'Prior1InterimInstant'
    PRIOR1_INTERIM_INSTANT__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'Prior1InterimInstant_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    PRIOR1_INTERIM_INSTANT__RECONCILING_ITEMS_MEMBER = 'Prior1InterimInstant_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_INTERIM_INSTANT__REPORTABLE_SEGMENTS_MEMBER = 'Prior1InterimInstant_ReportableSegmentsMember'
    """ 報告セグメント """
    PRIOR1_INTERIM_INSTANT__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1InterimInstant_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'Prior1YearInstant_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    PRIOR1_YEAR_INSTANT__RECONCILING_ITEMS_MEMBER = 'Prior1YearInstant_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_YEAR_INSTANT__REPORTABLE_SEGMENTS_MEMBER = 'Prior1YearInstant_ReportableSegmentsMember'
    """ 報告セグメント """
    PRIOR1_YEAR_INSTANT__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1YearInstant_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """


class LiabilitiesAndNetAssets(Enum):
    """"負債純資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    INTERIM_INSTANT = 'InterimInstant'
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class LiabilitiesFromApplicationOfEquityMethodNCL(Enum):
    """"持分法適用に伴う負債、固定負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ListingExpensesNOE(Enum):
    """"上場関連費用、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class ListingExpensesOpeCF(Enum):
    """"上場関連費用、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class LitigationExpensesNOE(Enum):
    """"訴訟関連費用、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class LitigationSettlementEL(Enum):
    """"訴訟和解金、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LoansAndBillsDiscountedAssetsBNK(Enum):
    """"貸出金、資産の部、銀行業"""
    INTERIM_INSTANT = 'InterimInstant'
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class LoansReceivablesAssetsINS(Enum):
    """"貸付金、資産の部、保険業"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class LongTermAccountsPayableOther(Enum):
    """"長期未払金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class LongTermAccountsReceivableOther(Enum):
    """"長期未収入金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class LongTermAdvancesReceived(Enum):
    """"長期前受金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class LongTermDeferredContributionForConstruction(Enum):
    """"長期前受工事負担金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class LongTermDepositsReceived(Enum):
    """"長期預り金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class LongTermGuaranteeDeposited(Enum):
    """"長期預り保証金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class LongTermLeaseAndGuaranteeDeposited(Enum):
    """"長期預り敷金保証金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class LongTermLeaseDeposited(Enum):
    """"長期預り敷金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class LongTermLoansPayable(Enum):
    """"長期借入金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class LongTermLoansPayableToSubsidiariesAndAffiliates(Enum):
    """"関係会社長期借入金"""
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class LongTermLoansReceivable(Enum):
    """"長期貸付金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class LongTermLoansReceivableFromDirectorsAndEmployees(Enum):
    """"役員及び従業員に対する長期貸付金"""
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class LongTermLoansReceivableFromEmployees(Enum):
    """"従業員に対する長期貸付金"""
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class LongTermLoansReceivableFromSubsidiariesAndAffiliates(Enum):
    """"関係会社長期貸付金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class LongTermPayablesUnderFluidityLeaseReceivablesNCLLEA(Enum):
    """"債権流動化に伴う長期支払債務、固定負債、リース事業"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class LongTermPrepaidExpenses(Enum):
    """"長期前払費用"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class LongTermTimeDeposits(Enum):
    """"長期預金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class LongTermUnearnedRevenue(Enum):
    """"長期前受収益"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class LossAdjustmentExpensesOEINS(Enum):
    """"損害調査費、経常費用、保険業"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossGainOnCancellationOfInsuranceContractOpeCF(Enum):
    """"保険解約損益（△は益）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class LossGainOnChangeInEquityOpeCF(Enum):
    """"持分変動損益（△は益）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossGainOnDisposalOfNoncurrentAssetsOpeCF(Enum):
    """"固定資産処分損益（△は益）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossGainOnDisposalOfPropertyPlantAndEquipmentOpeCF(Enum):
    """"有形固定資産処分損益（△は益）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossGainOnExtinguishmentOfTieInSharesOpeCF(Enum):
    """"抱合せ株式消滅差損益（△は益）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class LossGainOnInvestmentsInPartnershipOpeCF(Enum):
    """"投資事業組合運用損益（△は益）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class LossGainOnLiquidationOfSubsidiariesAndAffiliatesOpeCF(Enum):
    """"関係会社清算損益（△は益）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossGainOnLiquidationOfSubsidiariesOpeCF(Enum):
    """"子会社清算損益（△は益）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossGainOnMoneyHeldInTrustOpeCFBNK(Enum):
    """"金銭の信託の運用損益（△は運用益）、営業活動によるキャッシュ・フロー、銀行業"""
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'


class LossGainOnOperationOfInvestmentsInCapitalOpeCF(Enum):
    """"出資金運用損益（△は益）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class LossGainOnRedemptionOfInvestmentSecuritiesOpeCF(Enum):
    """"投資有価証券償還損益（△は益）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossGainOnRedemptionOfSecuritiesOpeCF(Enum):
    """"有価証券償還損益（△は益）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossGainOnSalesAndRetirementOfNoncurrentAssetsOpeCF(Enum):
    """"固定資産除売却損益（△は益）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class LossGainOnSalesAndRetirementOfPropertyPlantAndEquipmentAndIntangibleAssetsOpeCF(Enum):
    """"有形及び無形固定資産除売却損益（△は益）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class LossGainOnSalesAndRetirementOfPropertyPlantAndEquipmentOpeCF(Enum):
    """"有形固定資産除売却損益（△は益）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class LossGainOnSalesAndValuationOfInvestmentSecuritiesOpeCF(Enum):
    """"投資有価証券売却及び評価損益（△は益）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class LossGainOnSalesOfGolfClubMembershipsOpeCF(Enum):
    """"ゴルフ会員権売却損益（△は益）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossGainOnSalesOfInvestmentSecuritiesOpeCF(Enum):
    """"投資有価証券売却損益（△は益）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class LossGainOnSalesOfMembershipOpeCF(Enum):
    """"会員権売却損益（△は益）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossGainOnSalesOfNoncurrentAssetsOpeCF(Enum):
    """"固定資産売却損益（△は益）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class LossGainOnSalesOfPropertyPlantAndEquipmentOpeCF(Enum):
    """"有形固定資産売却損益（△は益）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class LossGainOnSalesOfSecuritiesOpeCF(Enum):
    """"有価証券売却損益（△は益）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossGainOnSalesOfShortTermAndLongTermInvestmentSecuritiesOpeCF(Enum):
    """"有価証券及び投資有価証券売却損益（△は益）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossGainOnSalesOfStocksOfSubsidiariesAndAffiliatesOpeCF(Enum):
    """"関係会社株式売却損益（△は益）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossGainOnSalesOfSubsidiariesStocksOpeCF(Enum):
    """"子会社株式売却損益（△は益）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossGainOnStepAcquisitionsOpeCF(Enum):
    """"段階取得に係る差損益（△は益）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class LossGainOnTransferOfBusinessOpeCF(Enum):
    """"事業譲渡損益（△は益）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossGainOnValuationOfCompoundFinancialInstrumentsOpeCF(Enum):
    """"複合金融商品評価損益（△は益）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossGainOnValuationOfDerivativesOpeCF(Enum):
    """"デリバティブ評価損益（△は益）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class LossGainOnValuationOfInvestmentSecuritiesOpeCF(Enum):
    """"投資有価証券評価損益（△は益）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class LossGainOnValuationOfSecuritiesOpeCF(Enum):
    """"有価証券評価損益（△は益）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossGainOnValuationOfShortTermAndLongTermInvestmentSecuritiesOpeCF(Enum):
    """"有価証券及び投資有価証券評価損益（△は益）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossGainRelatedToPropertyPlantAndEquipmentOpeCFINS(Enum):
    """"有形固定資産関係損益（△は益）、営業活動によるキャッシュ・フロー、保険業"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossGainRelatedToSecuritiesOpeCFBNK(Enum):
    """"有価証券関係損益（△）、営業活動によるキャッシュ・フロー、銀行業"""
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'


class LossGainRelatedToSecuritiesOpeCFINS(Enum):
    """"有価証券関係損益（△は益）、営業活動によるキャッシュ・フロー、保険業"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnAbandonmentOfInventoriesEL(Enum):
    """"棚卸資産廃棄損、特別損失"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class LossOnAbandonmentOfInventoriesNOE(Enum):
    """"棚卸資産廃棄損、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class LossOnAbandonmentOfInventoriesOpeCF(Enum):
    """"棚卸資産廃棄損、営業活動によるキャッシュ・フロー"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class LossOnAbandonmentOfNoncurrentAssetsEL(Enum):
    """"固定資産廃棄損、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class LossOnAbandonmentOfNoncurrentAssetsNOE(Enum):
    """"固定資産廃棄損、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnAbandonmentOfNoncurrentAssetsOpeCF(Enum):
    """"固定資産廃棄損、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class LossOnBusinessRestructuringOpeCF(Enum):
    """"事業再編損、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class LossOnBusinessWithdrawalEL(Enum):
    """"事業撤退損、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnCancelOfLeaseContractsNOE(Enum):
    """"リース解約損、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnCancellationOfLeaseContractsEL(Enum):
    """"リース解約損、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class LossOnCancellationOfLeaseholdContractsEL(Enum):
    """"賃貸借契約解約損、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnCancellationOfLeasesOpeCF(Enum):
    """"リース解約損、営業活動によるキャッシュ・フロー"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class LossOnCancellationOfRentalContractOpeCF(Enum):
    """"賃貸借契約解約損、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnChangeInEquityEL(Enum):
    """"持分変動損失、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnClosingOfStoresEL(Enum):
    """"店舗閉鎖損失、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class LossOnDisaster2OpeCF(Enum):
    """"災害による損失、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class LossOnDisasterEL(Enum):
    """"災害による損失、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class LossOnDisposalOfInventoriesEL(Enum):
    """"棚卸資産処分損、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnDisposalOfInventoriesNOE(Enum):
    """"棚卸資産処分損、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnDisposalOfNoncurrentAssetsEL(Enum):
    """"固定資産処分損、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    INTERIM_DURATION = 'InterimDuration'
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    INTERIM_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'InterimDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    INTERIM_DURATION__RECONCILING_ITEMS_MEMBER = 'InterimDuration_ReconcilingItemsMember'
    """ 調整項目 """
    INTERIM_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'InterimDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    INTERIM_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'InterimDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_INTERIM_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'Prior1InterimDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    PRIOR1_INTERIM_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1InterimDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_INTERIM_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'Prior1InterimDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    PRIOR1_INTERIM_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1InterimDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnDisposalOfNoncurrentAssetsNOE(Enum):
    """"固定資産処分損、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnExtinguishmentOfTieInSharesEL(Enum):
    """"抱合せ株式消滅差損、特別損失"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class LossOnInsuranceCancellationEL(Enum):
    """"保険解約損、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnInsuranceCancellationNOE(Enum):
    """"保険解約損、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class LossOnInvestmentsInCapitalNOE(Enum):
    """"出資金運用損、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnInvestmentsInPartnershipNOE(Enum):
    """"投資事業組合運用損、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class LossOnLiquidationOfBusinessEL(Enum):
    """"事業整理損、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class LossOnLiquidationOfBusinessOpeCF(Enum):
    """"事業整理損、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnLiquidationOfSubsidiariesAndAffiliatesEL(Enum):
    """"関係会社清算損、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnLiquidationOfSubsidiariesAndAffiliatesGeneralEL(Enum):
    """"関係会社整理損、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class LossOnLiquidationOfSubsidiariesAndAffiliatesOpeCF(Enum):
    """"関係会社整理損、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnLiquidationOfSubsidiariesEL(Enum):
    """"子会社清算損、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnLiquidationOfSubsidiariesGeneralEL(Enum):
    """"子会社整理損、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnLiquidationOfSubsidiariesOpeCF(Enum):
    """"子会社整理損、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnLitigationEL(Enum):
    """"訴訟関連損失、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnRedemptionOfSecuritiesNOE(Enum):
    """"有価証券償還損、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class LossOnReductionOfNoncurrentAssetsEL(Enum):
    """"固定資産圧縮損、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class LossOnReductionOfNoncurrentAssetsNOE(Enum):
    """"固定資産圧縮損、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnReductionOfNoncurrentAssetsOpeCF(Enum):
    """"固定資産圧縮損、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnRetirementOfInventoriesOpeCF(Enum):
    """"棚卸資産除却損、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnRetirementOfNoncurrentAssetsEL(Enum):
    """"固定資産除却損、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class LossOnRetirementOfNoncurrentAssetsNOE(Enum):
    """"固定資産除却損、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class LossOnRetirementOfNoncurrentAssetsOpeCF(Enum):
    """"固定資産除却損、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class LossOnRetirementOfPropertyPlantAndEquipmentEL(Enum):
    """"有形固定資産除却損、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnRetirementOfPropertyPlantAndEquipmentOpeCF(Enum):
    """"有形固定資産除却損、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class LossOnSalesAndRetirementOfNoncurrentAssetsEL(Enum):
    """"固定資産除売却損、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class LossOnSalesAndRetirementOfNoncurrentAssetsNOE(Enum):
    """"固定資産除売却損、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnSalesOfAccountsReceivableNOE(Enum):
    """"売上債権売却損、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnSalesOfElectronicallyRecordedMonetaryClaimsNOE(Enum):
    """"電子記録債権売却損、営業外費用"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class LossOnSalesOfInvestmentSecuritiesEL(Enum):
    """"投資有価証券売却損、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class LossOnSalesOfInvestmentSecuritiesNOE(Enum):
    """"投資有価証券売却損、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class LossOnSalesOfMembershipEL(Enum):
    """"会員権売却損、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnSalesOfNoncurrentAssetsEL(Enum):
    """"固定資産売却損、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class LossOnSalesOfNotesPayableNOE(Enum):
    """"手形売却損、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class LossOnSalesOfSecuritiesNOE(Enum):
    """"有価証券売却損、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnSalesOfStocksOfSubsidiariesAndAffiliatesEL(Enum):
    """"関係会社株式売却損、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnSalesOfSubsidiariesStocksEL(Enum):
    """"子会社株式売却損、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnStepAcquisitionsEL(Enum):
    """"段階取得に係る差損、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class LossOnStoreClosingsOpeCF(Enum):
    """"店舗閉鎖損失、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class LossOnSupportToSubsidiariesAndSubsidiariesAndAffiliatesEL(Enum):
    """"関係会社支援損、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnTransferOfBusinessEL(Enum):
    """"事業譲渡損、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnTransferOfReceivablesNOE(Enum):
    """"債権売却損、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class LossOnValuationOfCompoundFinancialInstrumentsNOE(Enum):
    """"複合金融商品評価損、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnValuationOfDerivativesNOE(Enum):
    """"デリバティブ評価損、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class LossOnValuationOfGolfClubMembershipEL(Enum):
    """"ゴルフ会員権評価損、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnValuationOfGolfClubMembershipsOpeCF(Enum):
    """"ゴルフ会員権評価損、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnValuationOfInventoriesEL(Enum):
    """"棚卸資産評価損、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnValuationOfInventoriesNOE(Enum):
    """"棚卸資産評価損、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnValuationOfInvestmentSecuritiesEL(Enum):
    """"投資有価証券評価損、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class LossOnValuationOfInvestmentSecuritiesNOE(Enum):
    """"投資有価証券評価損、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnValuationOfMembershipEL(Enum):
    """"会員権評価損、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnValuationOfMembershipOpeCF(Enum):
    """"会員権評価損、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnValuationOfSecuritiesOEINS(Enum):
    """"有価証券評価損、経常費用、保険業"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnValuationOfStocksOfSubsidiariesAndAffiliatesEL(Enum):
    """"関係会社株式評価損、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class LossOnValuationOfStocksOfSubsidiariesAndAffiliatesOpeCF(Enum):
    """"関係会社株式評価損、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class MachineryAndEquipment(Enum):
    """"機械及び装置"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class MachineryAndEquipmentNet(Enum):
    """"機械及び装置（純額）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class MachineryEquipmentAndVehicles(Enum):
    """"機械装置及び運搬具"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class MachineryEquipmentAndVehiclesNet(Enum):
    """"機械装置及び運搬具（純額）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class MachineryVehiclesToolsFurnitureAndFixtures(Enum):
    """"機械、運搬具及び工具器具備品"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class MachineryVehiclesToolsFurnitureAndFixturesNet(Enum):
    """"機械、運搬具及び工具器具備品（純額）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class MedicalExpensesSGA(Enum):
    """"衛生費、販売費及び一般管理費"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class Membership(Enum):
    """"会員権"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class Merchandise(Enum):
    """"商品"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class MerchandiseAndFinishedGoods(Enum):
    """"商品及び製品"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class MiscellaneousExpensesGAS(Enum):
    """"雑支出、ガス事業"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class MiscellaneousExpensesNOE(Enum):
    """"雑支出、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class MiscellaneousExpensesNOERWY(Enum):
    """"雑支出、営業外費用、鉄道事業"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class MiscellaneousExpensesSGA(Enum):
    """"雑費、販売費及び一般管理費"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class MiscellaneousIncomeGAS(Enum):
    """"雑収入、ガス事業"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class MiscellaneousIncomeNOI(Enum):
    """"雑収入、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class MiscellaneousIncomeNOIRWY(Enum):
    """"雑収入、営業外収益、鉄道事業"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class MiscellaneousLossNOE(Enum):
    """"雑損失、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class MonetaryClaimsBoughtAssetsBNK(Enum):
    """"買入金銭債権、資産の部、銀行業"""
    INTERIM_INSTANT = 'InterimInstant'
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class MoneyHeldInTrustAssetsBNK(Enum):
    """"金銭の信託、資産の部、銀行業"""
    INTERIM_INSTANT = 'InterimInstant'
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class NegativeGoodwill(Enum):
    """"負ののれん"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class NegotiableCertificatesOfDepositLiabilitiesBNK(Enum):
    """"譲渡性預金、負債の部、銀行業"""
    INTERIM_INSTANT = 'InterimInstant'
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class NetAssets(Enum):
    """"純資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__CAPITAL_STOCK_MEMBER = 'CurrentYearInstant_CapitalStockMember'
    """ 当年度時点資本金 """
    CURRENT_YEAR_INSTANT__CAPITAL_SURPLUS_MEMBER = 'CurrentYearInstant_CapitalSurplusMember'
    """ 当年度時点資本剰余金 """
    CURRENT_YEAR_INSTANT__DEFERRED_GAINS_OR_LOSSES_ON_HEDGES_MEMBER = 'CurrentYearInstant_DeferredGainsOrLossesOnHedgesMember'
    """ 当年度時点繰延ヘッジ損益 """
    CURRENT_YEAR_INSTANT__FOREIGN_CURRENCY_TRANSLATION_ADJUSTMENT_MEMBER = 'CurrentYearInstant_ForeignCurrencyTranslationAdjustmentMember'
    """ 当年度時点為替換算調整勘定 """
    CURRENT_YEAR_INSTANT__LEGAL_CAPITAL_SURPLUS_MEMBER = 'CurrentYearInstant_LegalCapitalSurplusMember'
    """ 当年度時点資本準備金 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__CAPITAL_STOCK_MEMBER = 'CurrentYearInstant_NonConsolidatedMember_CapitalStockMember'
    """ 当年度時点個別又は非連結資本金 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__CAPITAL_SURPLUS_MEMBER = 'CurrentYearInstant_NonConsolidatedMember_CapitalSurplusMember'
    """ 当年度時点個別又は非連結資本剰余金 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__DEFERRED_GAINS_OR_LOSSES_ON_HEDGES_MEMBER = 'CurrentYearInstant_NonConsolidatedMember_DeferredGainsOrLossesOnHedgesMember'
    """ 当年度時点個別又は非連結繰延ヘッジ損益 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__GENERAL_RESERVE_MEMBER = 'CurrentYearInstant_NonConsolidatedMember_GeneralReserveMember'
    """ 当年度時点個別又は非連結別途積立金 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__LEGAL_CAPITAL_SURPLUS_MEMBER = 'CurrentYearInstant_NonConsolidatedMember_LegalCapitalSurplusMember'
    """ 当年度時点個別又は非連結資本準備金 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__LEGAL_RETAINED_EARNINGS_MEMBER = 'CurrentYearInstant_NonConsolidatedMember_LegalRetainedEarningsMember'
    """ 当年度時点個別又は非連結利益準備金 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__OTHER_CAPITAL_SURPLUS_MEMBER = 'CurrentYearInstant_NonConsolidatedMember_OtherCapitalSurplusMember'
    """ 当年度時点個別又は非連結その他資本剰余金 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__RESERVE_FOR_ADVANCED_DEPRECIATION_OF_NONCURRENT_ASSETS_MEMBER = 'CurrentYearInstant_NonConsolidatedMember_ReserveForAdvancedDepreciationOfNoncurrentAssetsMember'
    """ 当年度時点個別又は非連結固定資産圧縮積立金 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__RESERVE_FOR_DIVIDENDS3_MEMBER = 'CurrentYearInstant_NonConsolidatedMember_ReserveForDividends3Member'
    """ 当年度時点個別又は非連結配当準備積立金 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__RESERVE_FOR_SPECIAL_DEPRECIATION_MEMBER = 'CurrentYearInstant_NonConsolidatedMember_ReserveForSpecialDepreciationMember'
    """ 当年度時点個別又は非連結特別償却準備金 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_BROUGHT_FORWARD_MEMBER = 'CurrentYearInstant_NonConsolidatedMember_RetainedEarningsBroughtForwardMember'
    """ 当年度時点個別又は非連結繰越利益剰余金 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_MEMBER = 'CurrentYearInstant_NonConsolidatedMember_RetainedEarningsMember'
    """ 当年度時点個別又は非連結利益剰余金 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__SHAREHOLDERS_EQUITY_MEMBER = 'CurrentYearInstant_NonConsolidatedMember_ShareholdersEquityMember'
    """ 当年度時点個別又は非連結株主資本 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__SUBSCRIPTION_RIGHTS_TO_SHARES_MEMBER = 'CurrentYearInstant_NonConsolidatedMember_SubscriptionRightsToSharesMember'
    """ 当年度時点個別又は非連結新株予約権 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__TREASURY_STOCK_MEMBER = 'CurrentYearInstant_NonConsolidatedMember_TreasuryStockMember'
    """ 当年度時点個別又は非連結自己株式 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__VALUATION_AND_TRANSLATION_ADJUSTMENTS_MEMBER = 'CurrentYearInstant_NonConsolidatedMember_ValuationAndTranslationAdjustmentsMember'
    """ 当年度時点個別又は非連結評価・換算差額等 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__VALUATION_DIFFERENCE_ON_AVAILABLE_FOR_SALE_SECURITIES_MEMBER = 'CurrentYearInstant_NonConsolidatedMember_ValuationDifferenceOnAvailableForSaleSecuritiesMember'
    """ 当年度時点個別又は非連結その他有価証券評価差額金 """
    CURRENT_YEAR_INSTANT__NON_CONTROLLING_INTERESTS_MEMBER = 'CurrentYearInstant_NonControllingInterestsMember'
    """ 当年度時点非支配株主持分 """
    CURRENT_YEAR_INSTANT__OTHER_CAPITAL_SURPLUS_MEMBER = 'CurrentYearInstant_OtherCapitalSurplusMember'
    """ 当年度時点その他資本剰余金 """
    CURRENT_YEAR_INSTANT__REMEASUREMENTS_OF_DEFINED_BENEFIT_PLANS_MEMBER = 'CurrentYearInstant_RemeasurementsOfDefinedBenefitPlansMember'
    """ 当年度時点退職給付に係る調整累計額 """
    CURRENT_YEAR_INSTANT__RETAINED_EARNINGS_BROUGHT_FORWARD_MEMBER = 'CurrentYearInstant_RetainedEarningsBroughtForwardMember'
    """ 当年度時点繰越利益剰余金 """
    CURRENT_YEAR_INSTANT__RETAINED_EARNINGS_MEMBER = 'CurrentYearInstant_RetainedEarningsMember'
    """ 当年度時点利益剰余金 """
    CURRENT_YEAR_INSTANT__SHAREHOLDERS_EQUITY_MEMBER = 'CurrentYearInstant_ShareholdersEquityMember'
    """ 当年度時点株主資本 """
    CURRENT_YEAR_INSTANT__SUBSCRIPTION_RIGHTS_TO_SHARES_MEMBER = 'CurrentYearInstant_SubscriptionRightsToSharesMember'
    """ 当年度時点新株予約権 """
    CURRENT_YEAR_INSTANT__TREASURY_STOCK_MEMBER = 'CurrentYearInstant_TreasuryStockMember'
    """ 当年度時点自己株式 """
    CURRENT_YEAR_INSTANT__VALUATION_AND_TRANSLATION_ADJUSTMENTS_MEMBER = 'CurrentYearInstant_ValuationAndTranslationAdjustmentsMember'
    """ 当年度時点評価・換算差額等 """
    CURRENT_YEAR_INSTANT__VALUATION_DIFFERENCE_ON_AVAILABLE_FOR_SALE_SECURITIES_MEMBER = 'CurrentYearInstant_ValuationDifferenceOnAvailableForSaleSecuritiesMember'
    """ 当年度時点その他有価証券評価差額金 """
    INTERIM_INSTANT = 'InterimInstant'
    INTERIM_INSTANT__CAPITAL_STOCK_MEMBER = 'InterimInstant_CapitalStockMember'
    """ 資本金 """
    INTERIM_INSTANT__CAPITAL_SURPLUS_MEMBER = 'InterimInstant_CapitalSurplusMember'
    """ 資本剰余金 """
    INTERIM_INSTANT__DEFERRED_GAINS_OR_LOSSES_ON_HEDGES_MEMBER = 'InterimInstant_DeferredGainsOrLossesOnHedgesMember'
    """ 繰延ヘッジ損益 """
    INTERIM_INSTANT__FOREIGN_CURRENCY_TRANSLATION_ADJUSTMENT_MEMBER = 'InterimInstant_ForeignCurrencyTranslationAdjustmentMember'
    """ 為替換算調整勘定 """
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER__CAPITAL_STOCK_MEMBER = 'InterimInstant_NonConsolidatedMember_CapitalStockMember'
    """ 個別又は非連結資本金 """
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER__CAPITAL_SURPLUS_MEMBER = 'InterimInstant_NonConsolidatedMember_CapitalSurplusMember'
    """ 個別又は非連結資本剰余金 """
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER__DEFERRED_GAINS_OR_LOSSES_ON_HEDGES_MEMBER = 'InterimInstant_NonConsolidatedMember_DeferredGainsOrLossesOnHedgesMember'
    """ 個別又は非連結繰延ヘッジ損益 """
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER__GENERAL_RESERVE_MEMBER = 'InterimInstant_NonConsolidatedMember_GeneralReserveMember'
    """ 個別又は非連結別途積立金 """
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER__LEGAL_CAPITAL_SURPLUS_MEMBER = 'InterimInstant_NonConsolidatedMember_LegalCapitalSurplusMember'
    """ 個別又は非連結資本準備金 """
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER__LEGAL_RETAINED_EARNINGS_MEMBER = 'InterimInstant_NonConsolidatedMember_LegalRetainedEarningsMember'
    """ 個別又は非連結利益準備金 """
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER__OTHER_CAPITAL_SURPLUS_MEMBER = 'InterimInstant_NonConsolidatedMember_OtherCapitalSurplusMember'
    """ 個別又は非連結その他資本剰余金 """
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER__RESERVE_FOR_ADVANCED_DEPRECIATION_OF_NONCURRENT_ASSETS_MEMBER = 'InterimInstant_NonConsolidatedMember_ReserveForAdvancedDepreciationOfNoncurrentAssetsMember'
    """ 個別又は非連結固定資産圧縮積立金 """
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER__RESERVE_FOR_REDUCTION_ENTRY2_MEMBER = 'InterimInstant_NonConsolidatedMember_ReserveForReductionEntry2Member'
    """ 個別又は非連結圧縮積立金 """
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER__RESERVE_FOR_REDUCTION_ENTRY_OF_REAL_ESTATE_MEMBER = 'InterimInstant_NonConsolidatedMember_ReserveForReductionEntryOfRealEstateMember'
    """ 個別又は非連結不動産圧縮積立金 """
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER__RESERVE_FOR_SPECIAL_ACCOUNT_FOR_ADVANCED_DEPRECIATION_OF_NONCURRENT_ASSETS_MEMBER = 'InterimInstant_NonConsolidatedMember_ReserveForSpecialAccountForAdvancedDepreciationOfNoncurrentAssetsMember'
    """ 個別又は非連結固定資産圧縮特別勘定積立金 """
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_BROUGHT_FORWARD_MEMBER = 'InterimInstant_NonConsolidatedMember_RetainedEarningsBroughtForwardMember'
    """ 個別又は非連結繰越利益剰余金 """
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_MEMBER = 'InterimInstant_NonConsolidatedMember_RetainedEarningsMember'
    """ 個別又は非連結利益剰余金 """
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER__REVALUATION_RESERVE_FOR_LAND_MEMBER = 'InterimInstant_NonConsolidatedMember_RevaluationReserveForLandMember'
    """ 個別又は非連結土地再評価差額金 """
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER__SHAREHOLDERS_EQUITY_MEMBER = 'InterimInstant_NonConsolidatedMember_ShareholdersEquityMember'
    """ 個別又は非連結株主資本 """
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER__SUBSCRIPTION_RIGHTS_TO_SHARES_MEMBER = 'InterimInstant_NonConsolidatedMember_SubscriptionRightsToSharesMember'
    """ 個別又は非連結新株予約権 """
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER__TREASURY_STOCK_MEMBER = 'InterimInstant_NonConsolidatedMember_TreasuryStockMember'
    """ 個別又は非連結自己株式 """
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER__VALUATION_AND_TRANSLATION_ADJUSTMENTS_MEMBER = 'InterimInstant_NonConsolidatedMember_ValuationAndTranslationAdjustmentsMember'
    """ 個別又は非連結評価・換算差額等 """
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER__VALUATION_DIFFERENCE_ON_AVAILABLE_FOR_SALE_SECURITIES_MEMBER = 'InterimInstant_NonConsolidatedMember_ValuationDifferenceOnAvailableForSaleSecuritiesMember'
    """ 個別又は非連結その他有価証券評価差額金 """
    INTERIM_INSTANT__NON_CONTROLLING_INTERESTS_MEMBER = 'InterimInstant_NonControllingInterestsMember'
    """ 非支配株主持分 """
    INTERIM_INSTANT__REMEASUREMENTS_OF_DEFINED_BENEFIT_PLANS_MEMBER = 'InterimInstant_RemeasurementsOfDefinedBenefitPlansMember'
    """ 退職給付に係る調整累計額 """
    INTERIM_INSTANT__RETAINED_EARNINGS_MEMBER = 'InterimInstant_RetainedEarningsMember'
    """ 利益剰余金 """
    INTERIM_INSTANT__REVALUATION_RESERVE_FOR_LAND_MEMBER = 'InterimInstant_RevaluationReserveForLandMember'
    """ 土地再評価差額金 """
    INTERIM_INSTANT__SHAREHOLDERS_EQUITY_MEMBER = 'InterimInstant_ShareholdersEquityMember'
    """ 株主資本 """
    INTERIM_INSTANT__SUBSCRIPTION_RIGHTS_TO_SHARES_MEMBER = 'InterimInstant_SubscriptionRightsToSharesMember'
    """ 新株予約権 """
    INTERIM_INSTANT__TREASURY_STOCK_MEMBER = 'InterimInstant_TreasuryStockMember'
    """ 自己株式 """
    INTERIM_INSTANT__VALUATION_AND_TRANSLATION_ADJUSTMENTS_MEMBER = 'InterimInstant_ValuationAndTranslationAdjustmentsMember'
    """ 評価・換算差額等 """
    INTERIM_INSTANT__VALUATION_DIFFERENCE_ON_AVAILABLE_FOR_SALE_SECURITIES_MEMBER = 'InterimInstant_ValuationDifferenceOnAvailableForSaleSecuritiesMember'
    """ その他有価証券評価差額金 """
    PRIOR1_INTERIM_INSTANT = 'Prior1InterimInstant'
    PRIOR1_INTERIM_INSTANT__CAPITAL_STOCK_MEMBER = 'Prior1InterimInstant_CapitalStockMember'
    """ 資本金 """
    PRIOR1_INTERIM_INSTANT__CAPITAL_SURPLUS_MEMBER = 'Prior1InterimInstant_CapitalSurplusMember'
    """ 資本剰余金 """
    PRIOR1_INTERIM_INSTANT__DEFERRED_GAINS_OR_LOSSES_ON_HEDGES_MEMBER = 'Prior1InterimInstant_DeferredGainsOrLossesOnHedgesMember'
    """ 繰延ヘッジ損益 """
    PRIOR1_INTERIM_INSTANT__FOREIGN_CURRENCY_TRANSLATION_ADJUSTMENT_MEMBER = 'Prior1InterimInstant_ForeignCurrencyTranslationAdjustmentMember'
    """ 為替換算調整勘定 """
    PRIOR1_INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER__CAPITAL_STOCK_MEMBER = 'Prior1InterimInstant_NonConsolidatedMember_CapitalStockMember'
    """ 個別又は非連結資本金 """
    PRIOR1_INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER__CAPITAL_SURPLUS_MEMBER = 'Prior1InterimInstant_NonConsolidatedMember_CapitalSurplusMember'
    """ 個別又は非連結資本剰余金 """
    PRIOR1_INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER__DEFERRED_GAINS_OR_LOSSES_ON_HEDGES_MEMBER = 'Prior1InterimInstant_NonConsolidatedMember_DeferredGainsOrLossesOnHedgesMember'
    """ 個別又は非連結繰延ヘッジ損益 """
    PRIOR1_INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER__GENERAL_RESERVE_MEMBER = 'Prior1InterimInstant_NonConsolidatedMember_GeneralReserveMember'
    """ 個別又は非連結別途積立金 """
    PRIOR1_INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER__LEGAL_CAPITAL_SURPLUS_MEMBER = 'Prior1InterimInstant_NonConsolidatedMember_LegalCapitalSurplusMember'
    """ 個別又は非連結資本準備金 """
    PRIOR1_INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER__LEGAL_RETAINED_EARNINGS_MEMBER = 'Prior1InterimInstant_NonConsolidatedMember_LegalRetainedEarningsMember'
    """ 個別又は非連結利益準備金 """
    PRIOR1_INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER__OTHER_CAPITAL_SURPLUS_MEMBER = 'Prior1InterimInstant_NonConsolidatedMember_OtherCapitalSurplusMember'
    """ 個別又は非連結その他資本剰余金 """
    PRIOR1_INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER__RESERVE_FOR_ADVANCED_DEPRECIATION_OF_NONCURRENT_ASSETS_MEMBER = 'Prior1InterimInstant_NonConsolidatedMember_ReserveForAdvancedDepreciationOfNoncurrentAssetsMember'
    """ 個別又は非連結固定資産圧縮積立金 """
    PRIOR1_INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER__RESERVE_FOR_REDUCTION_ENTRY2_MEMBER = 'Prior1InterimInstant_NonConsolidatedMember_ReserveForReductionEntry2Member'
    """ 個別又は非連結圧縮積立金 """
    PRIOR1_INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER__RESERVE_FOR_REDUCTION_ENTRY_OF_REAL_ESTATE_MEMBER = 'Prior1InterimInstant_NonConsolidatedMember_ReserveForReductionEntryOfRealEstateMember'
    """ 個別又は非連結不動産圧縮積立金 """
    PRIOR1_INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER__RESERVE_FOR_SPECIAL_ACCOUNT_FOR_ADVANCED_DEPRECIATION_OF_NONCURRENT_ASSETS_MEMBER = 'Prior1InterimInstant_NonConsolidatedMember_ReserveForSpecialAccountForAdvancedDepreciationOfNoncurrentAssetsMember'
    """ 個別又は非連結固定資産圧縮特別勘定積立金 """
    PRIOR1_INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_BROUGHT_FORWARD_MEMBER = 'Prior1InterimInstant_NonConsolidatedMember_RetainedEarningsBroughtForwardMember'
    """ 個別又は非連結繰越利益剰余金 """
    PRIOR1_INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_MEMBER = 'Prior1InterimInstant_NonConsolidatedMember_RetainedEarningsMember'
    """ 個別又は非連結利益剰余金 """
    PRIOR1_INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER__REVALUATION_RESERVE_FOR_LAND_MEMBER = 'Prior1InterimInstant_NonConsolidatedMember_RevaluationReserveForLandMember'
    """ 個別又は非連結土地再評価差額金 """
    PRIOR1_INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1InterimInstant_NonConsolidatedMember_ShareholdersEquityMember'
    """ 個別又は非連結株主資本 """
    PRIOR1_INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER__SUBSCRIPTION_RIGHTS_TO_SHARES_MEMBER = 'Prior1InterimInstant_NonConsolidatedMember_SubscriptionRightsToSharesMember'
    """ 個別又は非連結新株予約権 """
    PRIOR1_INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER__TREASURY_STOCK_MEMBER = 'Prior1InterimInstant_NonConsolidatedMember_TreasuryStockMember'
    """ 個別又は非連結自己株式 """
    PRIOR1_INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER__VALUATION_AND_TRANSLATION_ADJUSTMENTS_MEMBER = 'Prior1InterimInstant_NonConsolidatedMember_ValuationAndTranslationAdjustmentsMember'
    """ 個別又は非連結評価・換算差額等 """
    PRIOR1_INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER__VALUATION_DIFFERENCE_ON_AVAILABLE_FOR_SALE_SECURITIES_MEMBER = 'Prior1InterimInstant_NonConsolidatedMember_ValuationDifferenceOnAvailableForSaleSecuritiesMember'
    """ 個別又は非連結その他有価証券評価差額金 """
    PRIOR1_INTERIM_INSTANT__NON_CONTROLLING_INTERESTS_MEMBER = 'Prior1InterimInstant_NonControllingInterestsMember'
    """ 非支配株主持分 """
    PRIOR1_INTERIM_INSTANT__REMEASUREMENTS_OF_DEFINED_BENEFIT_PLANS_MEMBER = 'Prior1InterimInstant_RemeasurementsOfDefinedBenefitPlansMember'
    """ 退職給付に係る調整累計額 """
    PRIOR1_INTERIM_INSTANT__RETAINED_EARNINGS_MEMBER = 'Prior1InterimInstant_RetainedEarningsMember'
    """ 利益剰余金 """
    PRIOR1_INTERIM_INSTANT__REVALUATION_RESERVE_FOR_LAND_MEMBER = 'Prior1InterimInstant_RevaluationReserveForLandMember'
    """ 土地再評価差額金 """
    PRIOR1_INTERIM_INSTANT__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1InterimInstant_ShareholdersEquityMember'
    """ 株主資本 """
    PRIOR1_INTERIM_INSTANT__SUBSCRIPTION_RIGHTS_TO_SHARES_MEMBER = 'Prior1InterimInstant_SubscriptionRightsToSharesMember'
    """ 新株予約権 """
    PRIOR1_INTERIM_INSTANT__TREASURY_STOCK_MEMBER = 'Prior1InterimInstant_TreasuryStockMember'
    """ 自己株式 """
    PRIOR1_INTERIM_INSTANT__VALUATION_AND_TRANSLATION_ADJUSTMENTS_MEMBER = 'Prior1InterimInstant_ValuationAndTranslationAdjustmentsMember'
    """ 評価・換算差額等 """
    PRIOR1_INTERIM_INSTANT__VALUATION_DIFFERENCE_ON_AVAILABLE_FOR_SALE_SECURITIES_MEMBER = 'Prior1InterimInstant_ValuationDifferenceOnAvailableForSaleSecuritiesMember'
    """ その他有価証券評価差額金 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__CAPITAL_STOCK_MEMBER = 'Prior1YearInstant_CapitalStockMember'
    """ 資本金 """
    PRIOR1_YEAR_INSTANT__CAPITAL_SURPLUS_MEMBER = 'Prior1YearInstant_CapitalSurplusMember'
    """ 資本剰余金 """
    PRIOR1_YEAR_INSTANT__DEFERRED_GAINS_OR_LOSSES_ON_HEDGES_MEMBER = 'Prior1YearInstant_DeferredGainsOrLossesOnHedgesMember'
    """ 繰延ヘッジ損益 """
    PRIOR1_YEAR_INSTANT__FOREIGN_CURRENCY_TRANSLATION_ADJUSTMENT_MEMBER = 'Prior1YearInstant_ForeignCurrencyTranslationAdjustmentMember'
    """ 為替換算調整勘定 """
    PRIOR1_YEAR_INSTANT__LEGAL_CAPITAL_SURPLUS_MEMBER = 'Prior1YearInstant_LegalCapitalSurplusMember'
    """ 資本準備金 """
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__CAPITAL_STOCK_MEMBER = 'Prior1YearInstant_NonConsolidatedMember_CapitalStockMember'
    """ 個別又は非連結資本金 """
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__CAPITAL_SURPLUS_MEMBER = 'Prior1YearInstant_NonConsolidatedMember_CapitalSurplusMember'
    """ 個別又は非連結資本剰余金 """
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__DEFERRED_GAINS_OR_LOSSES_ON_HEDGES_MEMBER = 'Prior1YearInstant_NonConsolidatedMember_DeferredGainsOrLossesOnHedgesMember'
    """ 個別又は非連結繰延ヘッジ損益 """
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__GENERAL_RESERVE_MEMBER = 'Prior1YearInstant_NonConsolidatedMember_GeneralReserveMember'
    """ 個別又は非連結別途積立金 """
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__LEGAL_CAPITAL_SURPLUS_MEMBER = 'Prior1YearInstant_NonConsolidatedMember_LegalCapitalSurplusMember'
    """ 個別又は非連結資本準備金 """
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__LEGAL_RETAINED_EARNINGS_MEMBER = 'Prior1YearInstant_NonConsolidatedMember_LegalRetainedEarningsMember'
    """ 個別又は非連結利益準備金 """
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__OTHER_CAPITAL_SURPLUS_MEMBER = 'Prior1YearInstant_NonConsolidatedMember_OtherCapitalSurplusMember'
    """ 個別又は非連結その他資本剰余金 """
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__RESERVE_FOR_ADVANCED_DEPRECIATION_OF_NONCURRENT_ASSETS_MEMBER = 'Prior1YearInstant_NonConsolidatedMember_ReserveForAdvancedDepreciationOfNoncurrentAssetsMember'
    """ 個別又は非連結固定資産圧縮積立金 """
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__RESERVE_FOR_DIVIDENDS3_MEMBER = 'Prior1YearInstant_NonConsolidatedMember_ReserveForDividends3Member'
    """ 個別又は非連結配当準備積立金 """
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__RESERVE_FOR_REDUCTION_ENTRY2_MEMBER = 'Prior1YearInstant_NonConsolidatedMember_ReserveForReductionEntry2Member'
    """ 個別又は非連結圧縮積立金 """
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__RESERVE_FOR_REDUCTION_ENTRY_OF_REAL_ESTATE_MEMBER = 'Prior1YearInstant_NonConsolidatedMember_ReserveForReductionEntryOfRealEstateMember'
    """ 個別又は非連結不動産圧縮積立金 """
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__RESERVE_FOR_SPECIAL_ACCOUNT_FOR_ADVANCED_DEPRECIATION_OF_NONCURRENT_ASSETS_MEMBER = 'Prior1YearInstant_NonConsolidatedMember_ReserveForSpecialAccountForAdvancedDepreciationOfNoncurrentAssetsMember'
    """ 個別又は非連結固定資産圧縮特別勘定積立金 """
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__RESERVE_FOR_SPECIAL_DEPRECIATION_MEMBER = 'Prior1YearInstant_NonConsolidatedMember_ReserveForSpecialDepreciationMember'
    """ 個別又は非連結特別償却準備金 """
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_BROUGHT_FORWARD_MEMBER = 'Prior1YearInstant_NonConsolidatedMember_RetainedEarningsBroughtForwardMember'
    """ 個別又は非連結繰越利益剰余金 """
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_MEMBER = 'Prior1YearInstant_NonConsolidatedMember_RetainedEarningsMember'
    """ 個別又は非連結利益剰余金 """
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__REVALUATION_RESERVE_FOR_LAND_MEMBER = 'Prior1YearInstant_NonConsolidatedMember_RevaluationReserveForLandMember'
    """ 個別又は非連結土地再評価差額金 """
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1YearInstant_NonConsolidatedMember_ShareholdersEquityMember'
    """ 個別又は非連結株主資本 """
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__SUBSCRIPTION_RIGHTS_TO_SHARES_MEMBER = 'Prior1YearInstant_NonConsolidatedMember_SubscriptionRightsToSharesMember'
    """ 個別又は非連結新株予約権 """
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__TREASURY_STOCK_MEMBER = 'Prior1YearInstant_NonConsolidatedMember_TreasuryStockMember'
    """ 個別又は非連結自己株式 """
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__VALUATION_AND_TRANSLATION_ADJUSTMENTS_MEMBER = 'Prior1YearInstant_NonConsolidatedMember_ValuationAndTranslationAdjustmentsMember'
    """ 個別又は非連結評価・換算差額等 """
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__VALUATION_DIFFERENCE_ON_AVAILABLE_FOR_SALE_SECURITIES_MEMBER = 'Prior1YearInstant_NonConsolidatedMember_ValuationDifferenceOnAvailableForSaleSecuritiesMember'
    """ 個別又は非連結その他有価証券評価差額金 """
    PRIOR1_YEAR_INSTANT__NON_CONTROLLING_INTERESTS_MEMBER = 'Prior1YearInstant_NonControllingInterestsMember'
    """ 非支配株主持分 """
    PRIOR1_YEAR_INSTANT__OTHER_CAPITAL_SURPLUS_MEMBER = 'Prior1YearInstant_OtherCapitalSurplusMember'
    """ その他資本剰余金 """
    PRIOR1_YEAR_INSTANT__REMEASUREMENTS_OF_DEFINED_BENEFIT_PLANS_MEMBER = 'Prior1YearInstant_RemeasurementsOfDefinedBenefitPlansMember'
    """ 退職給付に係る調整累計額 """
    PRIOR1_YEAR_INSTANT__RETAINED_EARNINGS_BROUGHT_FORWARD_MEMBER = 'Prior1YearInstant_RetainedEarningsBroughtForwardMember'
    """ 繰越利益剰余金 """
    PRIOR1_YEAR_INSTANT__RETAINED_EARNINGS_MEMBER = 'Prior1YearInstant_RetainedEarningsMember'
    """ 利益剰余金 """
    PRIOR1_YEAR_INSTANT__REVALUATION_RESERVE_FOR_LAND_MEMBER = 'Prior1YearInstant_RevaluationReserveForLandMember'
    """ 土地再評価差額金 """
    PRIOR1_YEAR_INSTANT__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1YearInstant_ShareholdersEquityMember'
    """ 株主資本 """
    PRIOR1_YEAR_INSTANT__SUBSCRIPTION_RIGHTS_TO_SHARES_MEMBER = 'Prior1YearInstant_SubscriptionRightsToSharesMember'
    """ 新株予約権 """
    PRIOR1_YEAR_INSTANT__TREASURY_STOCK_MEMBER = 'Prior1YearInstant_TreasuryStockMember'
    """ 自己株式 """
    PRIOR1_YEAR_INSTANT__VALUATION_AND_TRANSLATION_ADJUSTMENTS_MEMBER = 'Prior1YearInstant_ValuationAndTranslationAdjustmentsMember'
    """ 評価・換算差額等 """
    PRIOR1_YEAR_INSTANT__VALUATION_DIFFERENCE_ON_AVAILABLE_FOR_SALE_SECURITIES_MEMBER = 'Prior1YearInstant_ValuationDifferenceOnAvailableForSaleSecuritiesMember'
    """ その他有価証券評価差額金 """
    PRIOR2_YEAR_INSTANT = 'Prior2YearInstant'
    PRIOR2_YEAR_INSTANT__CAPITAL_STOCK_MEMBER = 'Prior2YearInstant_CapitalStockMember'
    """ 資本金 """
    PRIOR2_YEAR_INSTANT__CAPITAL_SURPLUS_MEMBER = 'Prior2YearInstant_CapitalSurplusMember'
    """ 資本剰余金 """
    PRIOR2_YEAR_INSTANT__DEFERRED_GAINS_OR_LOSSES_ON_HEDGES_MEMBER = 'Prior2YearInstant_DeferredGainsOrLossesOnHedgesMember'
    """ 繰延ヘッジ損益 """
    PRIOR2_YEAR_INSTANT__FOREIGN_CURRENCY_TRANSLATION_ADJUSTMENT_MEMBER = 'Prior2YearInstant_ForeignCurrencyTranslationAdjustmentMember'
    """ 為替換算調整勘定 """
    PRIOR2_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior2YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR2_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__CAPITAL_STOCK_MEMBER = 'Prior2YearInstant_NonConsolidatedMember_CapitalStockMember'
    """ 個別又は非連結資本金 """
    PRIOR2_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__CAPITAL_SURPLUS_MEMBER = 'Prior2YearInstant_NonConsolidatedMember_CapitalSurplusMember'
    """ 個別又は非連結資本剰余金 """
    PRIOR2_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__DEFERRED_GAINS_OR_LOSSES_ON_HEDGES_MEMBER = 'Prior2YearInstant_NonConsolidatedMember_DeferredGainsOrLossesOnHedgesMember'
    """ 個別又は非連結繰延ヘッジ損益 """
    PRIOR2_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__GENERAL_RESERVE_MEMBER = 'Prior2YearInstant_NonConsolidatedMember_GeneralReserveMember'
    """ 個別又は非連結別途積立金 """
    PRIOR2_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__LEGAL_CAPITAL_SURPLUS_MEMBER = 'Prior2YearInstant_NonConsolidatedMember_LegalCapitalSurplusMember'
    """ 個別又は非連結資本準備金 """
    PRIOR2_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__LEGAL_RETAINED_EARNINGS_MEMBER = 'Prior2YearInstant_NonConsolidatedMember_LegalRetainedEarningsMember'
    """ 個別又は非連結利益準備金 """
    PRIOR2_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__OTHER_CAPITAL_SURPLUS_MEMBER = 'Prior2YearInstant_NonConsolidatedMember_OtherCapitalSurplusMember'
    """ 個別又は非連結その他資本剰余金 """
    PRIOR2_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__RESERVE_FOR_ADVANCED_DEPRECIATION_OF_NONCURRENT_ASSETS_MEMBER = 'Prior2YearInstant_NonConsolidatedMember_ReserveForAdvancedDepreciationOfNoncurrentAssetsMember'
    """ 個別又は非連結固定資産圧縮積立金 """
    PRIOR2_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__RESERVE_FOR_DIVIDENDS3_MEMBER = 'Prior2YearInstant_NonConsolidatedMember_ReserveForDividends3Member'
    """ 個別又は非連結配当準備積立金 """
    PRIOR2_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__RESERVE_FOR_REDUCTION_ENTRY2_MEMBER = 'Prior2YearInstant_NonConsolidatedMember_ReserveForReductionEntry2Member'
    """ 個別又は非連結圧縮積立金 """
    PRIOR2_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__RESERVE_FOR_REDUCTION_ENTRY_OF_REAL_ESTATE_MEMBER = 'Prior2YearInstant_NonConsolidatedMember_ReserveForReductionEntryOfRealEstateMember'
    """ 個別又は非連結不動産圧縮積立金 """
    PRIOR2_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__RESERVE_FOR_SPECIAL_ACCOUNT_FOR_ADVANCED_DEPRECIATION_OF_NONCURRENT_ASSETS_MEMBER = 'Prior2YearInstant_NonConsolidatedMember_ReserveForSpecialAccountForAdvancedDepreciationOfNoncurrentAssetsMember'
    """ 個別又は非連結固定資産圧縮特別勘定積立金 """
    PRIOR2_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__RESERVE_FOR_SPECIAL_DEPRECIATION_MEMBER = 'Prior2YearInstant_NonConsolidatedMember_ReserveForSpecialDepreciationMember'
    """ 個別又は非連結特別償却準備金 """
    PRIOR2_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_BROUGHT_FORWARD_MEMBER = 'Prior2YearInstant_NonConsolidatedMember_RetainedEarningsBroughtForwardMember'
    """ 個別又は非連結繰越利益剰余金 """
    PRIOR2_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_MEMBER = 'Prior2YearInstant_NonConsolidatedMember_RetainedEarningsMember'
    """ 個別又は非連結利益剰余金 """
    PRIOR2_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__REVALUATION_RESERVE_FOR_LAND_MEMBER = 'Prior2YearInstant_NonConsolidatedMember_RevaluationReserveForLandMember'
    """ 個別又は非連結土地再評価差額金 """
    PRIOR2_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__SHAREHOLDERS_EQUITY_MEMBER = 'Prior2YearInstant_NonConsolidatedMember_ShareholdersEquityMember'
    """ 個別又は非連結株主資本 """
    PRIOR2_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__SUBSCRIPTION_RIGHTS_TO_SHARES_MEMBER = 'Prior2YearInstant_NonConsolidatedMember_SubscriptionRightsToSharesMember'
    """ 個別又は非連結新株予約権 """
    PRIOR2_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__TREASURY_STOCK_MEMBER = 'Prior2YearInstant_NonConsolidatedMember_TreasuryStockMember'
    """ 個別又は非連結自己株式 """
    PRIOR2_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__VALUATION_AND_TRANSLATION_ADJUSTMENTS_MEMBER = 'Prior2YearInstant_NonConsolidatedMember_ValuationAndTranslationAdjustmentsMember'
    """ 個別又は非連結評価・換算差額等 """
    PRIOR2_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER__VALUATION_DIFFERENCE_ON_AVAILABLE_FOR_SALE_SECURITIES_MEMBER = 'Prior2YearInstant_NonConsolidatedMember_ValuationDifferenceOnAvailableForSaleSecuritiesMember'
    """ 個別又は非連結その他有価証券評価差額金 """
    PRIOR2_YEAR_INSTANT__NON_CONTROLLING_INTERESTS_MEMBER = 'Prior2YearInstant_NonControllingInterestsMember'
    """ 非支配株主持分 """
    PRIOR2_YEAR_INSTANT__REMEASUREMENTS_OF_DEFINED_BENEFIT_PLANS_MEMBER = 'Prior2YearInstant_RemeasurementsOfDefinedBenefitPlansMember'
    """ 退職給付に係る調整累計額 """
    PRIOR2_YEAR_INSTANT__RETAINED_EARNINGS_MEMBER = 'Prior2YearInstant_RetainedEarningsMember'
    """ 利益剰余金 """
    PRIOR2_YEAR_INSTANT__REVALUATION_RESERVE_FOR_LAND_MEMBER = 'Prior2YearInstant_RevaluationReserveForLandMember'
    """ 土地再評価差額金 """
    PRIOR2_YEAR_INSTANT__SHAREHOLDERS_EQUITY_MEMBER = 'Prior2YearInstant_ShareholdersEquityMember'
    """ 株主資本 """
    PRIOR2_YEAR_INSTANT__SUBSCRIPTION_RIGHTS_TO_SHARES_MEMBER = 'Prior2YearInstant_SubscriptionRightsToSharesMember'
    """ 新株予約権 """
    PRIOR2_YEAR_INSTANT__TREASURY_STOCK_MEMBER = 'Prior2YearInstant_TreasuryStockMember'
    """ 自己株式 """
    PRIOR2_YEAR_INSTANT__VALUATION_AND_TRANSLATION_ADJUSTMENTS_MEMBER = 'Prior2YearInstant_ValuationAndTranslationAdjustmentsMember'
    """ 評価・換算差額等 """
    PRIOR2_YEAR_INSTANT__VALUATION_DIFFERENCE_ON_AVAILABLE_FOR_SALE_SECURITIES_MEMBER = 'Prior2YearInstant_ValuationDifferenceOnAvailableForSaleSecuritiesMember'
    """ その他有価証券評価差額金 """


class NetCashProvidedByUsedInFinancingActivities(Enum):
    """"財務活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class NetCashProvidedByUsedInInvestmentActivities(Enum):
    """"投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class NetCashProvidedByUsedInOperatingActivities(Enum):
    """"営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class NetChangesOfItemsOtherThanShareholdersEquity(Enum):
    """"株主資本以外の項目の当期変動額（純額）"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__CAPITAL_STOCK_MEMBER = 'CurrentYearDuration_CapitalStockMember'
    """ 当年度会計期間資本金 """
    CURRENT_YEAR_DURATION__CAPITAL_SURPLUS_MEMBER = 'CurrentYearDuration_CapitalSurplusMember'
    """ 当年度会計期間資本剰余金 """
    CURRENT_YEAR_DURATION__DEFERRED_GAINS_OR_LOSSES_ON_HEDGES_MEMBER = 'CurrentYearDuration_DeferredGainsOrLossesOnHedgesMember'
    """ 当年度会計期間繰延ヘッジ損益 """
    CURRENT_YEAR_DURATION__FOREIGN_CURRENCY_TRANSLATION_ADJUSTMENT_MEMBER = 'CurrentYearDuration_ForeignCurrencyTranslationAdjustmentMember'
    """ 当年度会計期間為替換算調整勘定 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CAPITAL_STOCK_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_CapitalStockMember'
    """ 当年度会計期間個別又は非連結資本金 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CAPITAL_SURPLUS_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_CapitalSurplusMember'
    """ 当年度会計期間個別又は非連結資本剰余金 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__DEFERRED_GAINS_OR_LOSSES_ON_HEDGES_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_DeferredGainsOrLossesOnHedgesMember'
    """ 当年度会計期間個別又は非連結繰延ヘッジ損益 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__LEGAL_CAPITAL_SURPLUS_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_LegalCapitalSurplusMember'
    """ 当年度会計期間個別又は非連結資本準備金 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_BROUGHT_FORWARD_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_RetainedEarningsBroughtForwardMember'
    """ 当年度会計期間個別又は非連結繰越利益剰余金 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_RetainedEarningsMember'
    """ 当年度会計期間個別又は非連結利益剰余金 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__SHAREHOLDERS_EQUITY_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_ShareholdersEquityMember'
    """ 当年度会計期間個別又は非連結株主資本 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__SUBSCRIPTION_RIGHTS_TO_SHARES_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_SubscriptionRightsToSharesMember'
    """ 当年度会計期間個別又は非連結新株予約権 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__TREASURY_STOCK_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_TreasuryStockMember'
    """ 当年度会計期間個別又は非連結自己株式 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__VALUATION_AND_TRANSLATION_ADJUSTMENTS_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_ValuationAndTranslationAdjustmentsMember'
    """ 当年度会計期間個別又は非連結評価・換算差額等 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__VALUATION_DIFFERENCE_ON_AVAILABLE_FOR_SALE_SECURITIES_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_ValuationDifferenceOnAvailableForSaleSecuritiesMember'
    """ 当年度会計期間個別又は非連結その他有価証券評価差額金 """
    CURRENT_YEAR_DURATION__NON_CONTROLLING_INTERESTS_MEMBER = 'CurrentYearDuration_NonControllingInterestsMember'
    """ 当年度会計期間非支配株主持分 """
    CURRENT_YEAR_DURATION__REMEASUREMENTS_OF_DEFINED_BENEFIT_PLANS_MEMBER = 'CurrentYearDuration_RemeasurementsOfDefinedBenefitPlansMember'
    """ 当年度会計期間退職給付に係る調整累計額 """
    CURRENT_YEAR_DURATION__RETAINED_EARNINGS_MEMBER = 'CurrentYearDuration_RetainedEarningsMember'
    """ 当年度会計期間利益剰余金 """
    CURRENT_YEAR_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'CurrentYearDuration_ShareholdersEquityMember'
    """ 当年度会計期間株主資本 """
    CURRENT_YEAR_DURATION__SUBSCRIPTION_RIGHTS_TO_SHARES_MEMBER = 'CurrentYearDuration_SubscriptionRightsToSharesMember'
    """ 当年度会計期間新株予約権 """
    CURRENT_YEAR_DURATION__TREASURY_STOCK_MEMBER = 'CurrentYearDuration_TreasuryStockMember'
    """ 当年度会計期間自己株式 """
    CURRENT_YEAR_DURATION__VALUATION_AND_TRANSLATION_ADJUSTMENTS_MEMBER = 'CurrentYearDuration_ValuationAndTranslationAdjustmentsMember'
    """ 当年度会計期間評価・換算差額等 """
    CURRENT_YEAR_DURATION__VALUATION_DIFFERENCE_ON_AVAILABLE_FOR_SALE_SECURITIES_MEMBER = 'CurrentYearDuration_ValuationDifferenceOnAvailableForSaleSecuritiesMember'
    """ 当年度会計期間その他有価証券評価差額金 """
    INTERIM_DURATION = 'InterimDuration'
    INTERIM_DURATION__DEFERRED_GAINS_OR_LOSSES_ON_HEDGES_MEMBER = 'InterimDuration_DeferredGainsOrLossesOnHedgesMember'
    """ 繰延ヘッジ損益 """
    INTERIM_DURATION__FOREIGN_CURRENCY_TRANSLATION_ADJUSTMENT_MEMBER = 'InterimDuration_ForeignCurrencyTranslationAdjustmentMember'
    """ 為替換算調整勘定 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__DEFERRED_GAINS_OR_LOSSES_ON_HEDGES_MEMBER = 'InterimDuration_NonConsolidatedMember_DeferredGainsOrLossesOnHedgesMember'
    """ 個別又は非連結繰延ヘッジ損益 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__REVALUATION_RESERVE_FOR_LAND_MEMBER = 'InterimDuration_NonConsolidatedMember_RevaluationReserveForLandMember'
    """ 個別又は非連結土地再評価差額金 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__SUBSCRIPTION_RIGHTS_TO_SHARES_MEMBER = 'InterimDuration_NonConsolidatedMember_SubscriptionRightsToSharesMember'
    """ 個別又は非連結新株予約権 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__VALUATION_AND_TRANSLATION_ADJUSTMENTS_MEMBER = 'InterimDuration_NonConsolidatedMember_ValuationAndTranslationAdjustmentsMember'
    """ 個別又は非連結評価・換算差額等 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__VALUATION_DIFFERENCE_ON_AVAILABLE_FOR_SALE_SECURITIES_MEMBER = 'InterimDuration_NonConsolidatedMember_ValuationDifferenceOnAvailableForSaleSecuritiesMember'
    """ 個別又は非連結その他有価証券評価差額金 """
    INTERIM_DURATION__NON_CONTROLLING_INTERESTS_MEMBER = 'InterimDuration_NonControllingInterestsMember'
    """ 非支配株主持分 """
    INTERIM_DURATION__REMEASUREMENTS_OF_DEFINED_BENEFIT_PLANS_MEMBER = 'InterimDuration_RemeasurementsOfDefinedBenefitPlansMember'
    """ 退職給付に係る調整累計額 """
    INTERIM_DURATION__REVALUATION_RESERVE_FOR_LAND_MEMBER = 'InterimDuration_RevaluationReserveForLandMember'
    """ 土地再評価差額金 """
    INTERIM_DURATION__SUBSCRIPTION_RIGHTS_TO_SHARES_MEMBER = 'InterimDuration_SubscriptionRightsToSharesMember'
    """ 新株予約権 """
    INTERIM_DURATION__VALUATION_AND_TRANSLATION_ADJUSTMENTS_MEMBER = 'InterimDuration_ValuationAndTranslationAdjustmentsMember'
    """ 評価・換算差額等 """
    INTERIM_DURATION__VALUATION_DIFFERENCE_ON_AVAILABLE_FOR_SALE_SECURITIES_MEMBER = 'InterimDuration_ValuationDifferenceOnAvailableForSaleSecuritiesMember'
    """ その他有価証券評価差額金 """
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_INTERIM_DURATION__DEFERRED_GAINS_OR_LOSSES_ON_HEDGES_MEMBER = 'Prior1InterimDuration_DeferredGainsOrLossesOnHedgesMember'
    """ 繰延ヘッジ損益 """
    PRIOR1_INTERIM_DURATION__FOREIGN_CURRENCY_TRANSLATION_ADJUSTMENT_MEMBER = 'Prior1InterimDuration_ForeignCurrencyTranslationAdjustmentMember'
    """ 為替換算調整勘定 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__DEFERRED_GAINS_OR_LOSSES_ON_HEDGES_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_DeferredGainsOrLossesOnHedgesMember'
    """ 個別又は非連結繰延ヘッジ損益 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__REVALUATION_RESERVE_FOR_LAND_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_RevaluationReserveForLandMember'
    """ 個別又は非連結土地再評価差額金 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__SUBSCRIPTION_RIGHTS_TO_SHARES_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_SubscriptionRightsToSharesMember'
    """ 個別又は非連結新株予約権 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__VALUATION_AND_TRANSLATION_ADJUSTMENTS_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_ValuationAndTranslationAdjustmentsMember'
    """ 個別又は非連結評価・換算差額等 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__VALUATION_DIFFERENCE_ON_AVAILABLE_FOR_SALE_SECURITIES_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_ValuationDifferenceOnAvailableForSaleSecuritiesMember'
    """ 個別又は非連結その他有価証券評価差額金 """
    PRIOR1_INTERIM_DURATION__NON_CONTROLLING_INTERESTS_MEMBER = 'Prior1InterimDuration_NonControllingInterestsMember'
    """ 非支配株主持分 """
    PRIOR1_INTERIM_DURATION__REMEASUREMENTS_OF_DEFINED_BENEFIT_PLANS_MEMBER = 'Prior1InterimDuration_RemeasurementsOfDefinedBenefitPlansMember'
    """ 退職給付に係る調整累計額 """
    PRIOR1_INTERIM_DURATION__REVALUATION_RESERVE_FOR_LAND_MEMBER = 'Prior1InterimDuration_RevaluationReserveForLandMember'
    """ 土地再評価差額金 """
    PRIOR1_INTERIM_DURATION__SUBSCRIPTION_RIGHTS_TO_SHARES_MEMBER = 'Prior1InterimDuration_SubscriptionRightsToSharesMember'
    """ 新株予約権 """
    PRIOR1_INTERIM_DURATION__VALUATION_AND_TRANSLATION_ADJUSTMENTS_MEMBER = 'Prior1InterimDuration_ValuationAndTranslationAdjustmentsMember'
    """ 評価・換算差額等 """
    PRIOR1_INTERIM_DURATION__VALUATION_DIFFERENCE_ON_AVAILABLE_FOR_SALE_SECURITIES_MEMBER = 'Prior1InterimDuration_ValuationDifferenceOnAvailableForSaleSecuritiesMember'
    """ その他有価証券評価差額金 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__CAPITAL_STOCK_MEMBER = 'Prior1YearDuration_CapitalStockMember'
    """ 資本金 """
    PRIOR1_YEAR_DURATION__CAPITAL_SURPLUS_MEMBER = 'Prior1YearDuration_CapitalSurplusMember'
    """ 資本剰余金 """
    PRIOR1_YEAR_DURATION__DEFERRED_GAINS_OR_LOSSES_ON_HEDGES_MEMBER = 'Prior1YearDuration_DeferredGainsOrLossesOnHedgesMember'
    """ 繰延ヘッジ損益 """
    PRIOR1_YEAR_DURATION__FOREIGN_CURRENCY_TRANSLATION_ADJUSTMENT_MEMBER = 'Prior1YearDuration_ForeignCurrencyTranslationAdjustmentMember'
    """ 為替換算調整勘定 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CAPITAL_STOCK_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_CapitalStockMember'
    """ 個別又は非連結資本金 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CAPITAL_SURPLUS_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_CapitalSurplusMember'
    """ 個別又は非連結資本剰余金 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__DEFERRED_GAINS_OR_LOSSES_ON_HEDGES_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_DeferredGainsOrLossesOnHedgesMember'
    """ 個別又は非連結繰延ヘッジ損益 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__LEGAL_CAPITAL_SURPLUS_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_LegalCapitalSurplusMember'
    """ 個別又は非連結資本準備金 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_BROUGHT_FORWARD_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_RetainedEarningsBroughtForwardMember'
    """ 個別又は非連結繰越利益剰余金 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_RetainedEarningsMember'
    """ 個別又は非連結利益剰余金 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_ShareholdersEquityMember'
    """ 個別又は非連結株主資本 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__SUBSCRIPTION_RIGHTS_TO_SHARES_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_SubscriptionRightsToSharesMember'
    """ 個別又は非連結新株予約権 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__TREASURY_STOCK_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_TreasuryStockMember'
    """ 個別又は非連結自己株式 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__VALUATION_AND_TRANSLATION_ADJUSTMENTS_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_ValuationAndTranslationAdjustmentsMember'
    """ 個別又は非連結評価・換算差額等 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__VALUATION_DIFFERENCE_ON_AVAILABLE_FOR_SALE_SECURITIES_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_ValuationDifferenceOnAvailableForSaleSecuritiesMember'
    """ 個別又は非連結その他有価証券評価差額金 """
    PRIOR1_YEAR_DURATION__NON_CONTROLLING_INTERESTS_MEMBER = 'Prior1YearDuration_NonControllingInterestsMember'
    """ 非支配株主持分 """
    PRIOR1_YEAR_DURATION__REMEASUREMENTS_OF_DEFINED_BENEFIT_PLANS_MEMBER = 'Prior1YearDuration_RemeasurementsOfDefinedBenefitPlansMember'
    """ 退職給付に係る調整累計額 """
    PRIOR1_YEAR_DURATION__RETAINED_EARNINGS_MEMBER = 'Prior1YearDuration_RetainedEarningsMember'
    """ 利益剰余金 """
    PRIOR1_YEAR_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1YearDuration_ShareholdersEquityMember'
    """ 株主資本 """
    PRIOR1_YEAR_DURATION__SUBSCRIPTION_RIGHTS_TO_SHARES_MEMBER = 'Prior1YearDuration_SubscriptionRightsToSharesMember'
    """ 新株予約権 """
    PRIOR1_YEAR_DURATION__TREASURY_STOCK_MEMBER = 'Prior1YearDuration_TreasuryStockMember'
    """ 自己株式 """
    PRIOR1_YEAR_DURATION__VALUATION_AND_TRANSLATION_ADJUSTMENTS_MEMBER = 'Prior1YearDuration_ValuationAndTranslationAdjustmentsMember'
    """ 評価・換算差額等 """
    PRIOR1_YEAR_DURATION__VALUATION_DIFFERENCE_ON_AVAILABLE_FOR_SALE_SECURITIES_MEMBER = 'Prior1YearDuration_ValuationDifferenceOnAvailableForSaleSecuritiesMember'
    """ その他有価証券評価差額金 """


class NetDecreaseIncreaseInCallLoansOpeCFBNK(Enum):
    """"コールローン等の純増（△）減、営業活動によるキャッシュ・フロー、銀行業"""
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'


class NetDecreaseIncreaseInDepositExcludingDepositPaidToBankOfJapanOpeCFBNK(Enum):
    """"預け金（日銀預け金を除く）の純増（△）減、営業活動によるキャッシュ・フロー、銀行業"""
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'


class NetDecreaseIncreaseInForeignExchangesAssetsOpeCFBNK(Enum):
    """"外国為替（資産）の純増（△）減、営業活動によるキャッシュ・フロー、銀行業"""
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'


class NetDecreaseIncreaseInLeaseReceivablesAndInvestmentAssetsOpeCFBNK(Enum):
    """"リース債権及びリース投資資産の純増（△）減、営業活動によるキャッシュ・フロー、銀行業"""
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'


class NetDecreaseIncreaseInLoansAndBillsDiscountedOpeCFBNK(Enum):
    """"貸出金の純増（△）減、営業活動によるキャッシュ・フロー、銀行業"""
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'


class NetDecreaseIncreaseInReceivablesUnderSecuritiesBorrowingTransactionsOpeCFBNK(Enum):
    """"債券貸借取引支払保証金の純増（△）減、営業活動によるキャッシュ・フロー、銀行業"""
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'


class NetDecreaseIncreaseInShortTermInvestmentSecuritiesInvCF(Enum):
    """"有価証券の純増減額（△は増加）、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class NetDecreaseIncreaseInShortTermLoansReceivableInvCF(Enum):
    """"短期貸付金の純増減額（△は増加）、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class NetDecreaseIncreaseInTimeDepositsInvCF(Enum):
    """"定期預金の純増減額（△は増加）、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class NetDecreaseIncreaseInTradingAccountSecuritiesOpeCFBNK(Enum):
    """"商品有価証券の純増（△）減、営業活動によるキャッシュ・フロー、銀行業"""
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'


class NetDecreaseIncreaseInTreasuryStockFinCF(Enum):
    """"自己株式の純増減額（△は増加）、財務活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class NetDefinedBenefitAsset(Enum):
    """"退職給付に係る資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    INTERIM_INSTANT = 'InterimInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class NetDefinedBenefitLiability(Enum):
    """"退職給付に係る負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    INTERIM_INSTANT = 'InterimInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class NetIncreaseDecreaseInBorrowedMoneyExcludingSubordinatedBorrowingsOpeCFBNK(Enum):
    """"借用金（劣後特約付借入金を除く）の純増減（△）、営業活動によるキャッシュ・フロー、銀行業"""
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'


class NetIncreaseDecreaseInBorrowedMoneyFromTrustAccountOpeCFBNK(Enum):
    """"信託勘定借の純増減（△）、営業活動によるキャッシュ・フロー、銀行業"""
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'


class NetIncreaseDecreaseInCallMoneyOpeCFBNK(Enum):
    """"コールマネー等の純増減（△）、営業活動によるキャッシュ・フロー、銀行業"""
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'


class NetIncreaseDecreaseInCashAndCashEquivalents(Enum):
    """"現金及び現金同等物の増減額（△は減少）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class NetIncreaseDecreaseInCashAndDepositsInvCFINS(Enum):
    """"預貯金の純増減額（△は増加）、投資活動によるキャッシュ・フロー、保険業"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class NetIncreaseDecreaseInCommercialPapersFinCF(Enum):
    """"コマーシャル・ペーパーの純増減額（△は減少）、財務活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class NetIncreaseDecreaseInDepositOpeCFBNK(Enum):
    """"預金の純増減（△）、営業活動によるキャッシュ・フロー、銀行業"""
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'


class NetIncreaseDecreaseInForeignExchangesLiabilitiesOpeCFBNK(Enum):
    """"外国為替（負債）の純増減（△）、営業活動によるキャッシュ・フロー、銀行業"""
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'


class NetIncreaseDecreaseInNegotiableCertificatesOfDepositOpeCFBNK(Enum):
    """"譲渡性預金の純増減（△）、営業活動によるキャッシュ・フロー、銀行業"""
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'


class NetIncreaseDecreaseInPayablesUnderSecuritiesLendingTransactionsOpeCFBNK(Enum):
    """"債券貸借取引受入担保金の純増減（△）、営業活動によるキャッシュ・フロー、銀行業"""
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'


class NetIncreaseDecreaseInShortTermLoansPayableFinCF(Enum):
    """"短期借入金の純増減額（△は減少）、財務活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class NetLossPaidOEINS(Enum):
    """"正味支払保険金、経常費用、保険業"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class NetPremiumsWrittenOIINS(Enum):
    """"正味収入保険料、経常収益、保険業"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class NetSales(Enum):
    """"売上高"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ 個別又は非連結その他 """
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER__OTHER_REPORTABLE_SEGMENTS_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember_OtherReportableSegmentsMember'
    """ 個別又は非連結その他 """
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER__RECONCILING_ITEMS_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember_ReconcilingItemsMember'
    """ 個別又は非連結調整項目 """
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER__REPORTABLE_SEGMENTS_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember_ReportableSegmentsMember'
    """ 個別又は非連結報告セグメント """
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember_TotalOfReportableSegmentsAndOthersMember'
    """ 個別又は非連結事業セグメント合計 """
    CURRENT_YTD_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'CurrentYTDDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    CURRENT_YTD_DURATION__OTHER_REPORTABLE_SEGMENTS_MEMBER = 'CurrentYTDDuration_OtherReportableSegmentsMember'
    """ その他 """
    CURRENT_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'CurrentYTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    CURRENT_YTD_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'CurrentYTDDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    CURRENT_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'CurrentYTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__OTHER_REPORTABLE_SEGMENTS_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_OtherReportableSegmentsMember'
    """ 当年度会計期間個別又は非連結その他 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RECONCILING_ITEMS_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_ReconcilingItemsMember'
    """ 当年度会計期間個別又は非連結調整項目 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__REPORTABLE_SEGMENTS_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_ReportableSegmentsMember'
    """ 当年度会計期間個別又は非連結報告セグメント """
    CURRENT_YEAR_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'CurrentYearDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ 当年度会計期間その他 """
    CURRENT_YEAR_DURATION__OTHER_REPORTABLE_SEGMENTS_MEMBER = 'CurrentYearDuration_OtherReportableSegmentsMember'
    """ 当年度会計期間その他 """
    CURRENT_YEAR_DURATION__RECONCILING_ITEMS_MEMBER = 'CurrentYearDuration_ReconcilingItemsMember'
    """ 当年度会計期間調整項目 """
    CURRENT_YEAR_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'CurrentYearDuration_ReportableSegmentsMember'
    """ 当年度会計期間報告セグメント """
    CURRENT_YEAR_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'CurrentYearDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 当年度会計期間事業セグメント合計 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ 個別又は非連結その他 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER__RECONCILING_ITEMS_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember_ReconcilingItemsMember'
    """ 個別又は非連結調整項目 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER__REPORTABLE_SEGMENTS_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember_ReportableSegmentsMember'
    """ 個別又は非連結報告セグメント """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember_TotalOfReportableSegmentsAndOthersMember'
    """ 個別又は非連結事業セグメント合計 """
    PRIOR1_YTD_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'Prior1YTDDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    PRIOR1_YTD_DURATION__OTHER_REPORTABLE_SEGMENTS_MEMBER = 'Prior1YTDDuration_OtherReportableSegmentsMember'
    """ その他 """
    PRIOR1_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1YTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_YTD_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'Prior1YTDDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    PRIOR1_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1YTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__OTHER_REPORTABLE_SEGMENTS_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_OtherReportableSegmentsMember'
    """ 個別又は非連結その他 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RECONCILING_ITEMS_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_ReconcilingItemsMember'
    """ 個別又は非連結調整項目 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__REPORTABLE_SEGMENTS_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_ReportableSegmentsMember'
    """ 個別又は非連結報告セグメント """
    PRIOR1_YEAR_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'Prior1YearDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    PRIOR1_YEAR_DURATION__OTHER_REPORTABLE_SEGMENTS_MEMBER = 'Prior1YearDuration_OtherReportableSegmentsMember'
    """ その他 """
    PRIOR1_YEAR_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1YearDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_YEAR_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'Prior1YearDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    PRIOR1_YEAR_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1YearDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """


class NetSalesOfCompletedConstructionContractsCNS(Enum):
    """"完成工事高、建設業"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class NetSalesOfFinishedGoodsRevOA(Enum):
    """"製品売上高、営業活動による収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class NetSalesOfGoodsRevOA(Enum):
    """"商品売上高、営業活動による収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class NetSalesOfMerchandiseAndFinishedGoodsRevOA(Enum):
    """"商品及び製品売上高、営業活動による収益"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class NetSalesOfRealEstateBusinessAndOtherCNS(Enum):
    """"不動産事業等売上高、建設業"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class NetSalesOfSideLineBusinessCNS(Enum):
    """"兼業事業売上高、建設業"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class NonControllingInterests(Enum):
    """"非支配株主持分"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    INTERIM_INSTANT = 'InterimInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class NonOperatingExpenses(Enum):
    """"営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class NonOperatingIncome(Enum):
    """"営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class NoncurrentAssets(Enum):
    """"固定資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class NoncurrentLiabilities(Enum):
    """"固定負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class NotesAndAccountsPayableTrade(Enum):
    """"支払手形及び買掛金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class NotesAndAccountsReceivableTrade(Enum):
    """"受取手形及び売掛金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class NotesAndAccountsReceivableTradeAndContractAssets(Enum):
    """"受取手形、売掛金及び契約資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class NotesAndAccountsReceivableTradeNet(Enum):
    """"受取手形及び売掛金（純額）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class NotesAndOperatingAccountsPayableTrade(Enum):
    """"支払手形及び営業未払金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class NotesAndOperatingAccountsReceivableCA(Enum):
    """"受取手形及び営業未収入金、流動資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class NotesPayableAccountsPayableForConstructionContractsAndOtherCNS(Enum):
    """"支払手形・工事未払金等、建設業"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class NotesPayableAccountsPayableForConstructionContractsCNS(Enum):
    """"支払手形・工事未払金、建設業"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class NotesPayableFacilities(Enum):
    """"設備関係支払手形"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class NotesPayableTrade(Enum):
    """"支払手形"""
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class NotesReceivableAccountsReceivableFromCompletedConstructionContractsAndOtherCNS(Enum):
    """"受取手形・完成工事未収入金等、建設業"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class NotesReceivableAccountsReceivableFromCompletedConstructionContractsCNS(Enum):
    """"受取手形・完成工事未収入金、建設業"""
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class NotesReceivableTrade(Enum):
    """"受取手形"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class OfficeTransferExpensesEL(Enum):
    """"事務所移転費用、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class OfficeTransferExpensesNOE(Enum):
    """"事務所移転費用、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class OfficeWorkFeeNOI(Enum):
    """"受取事務手数料、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class OperatingAccountsPayable(Enum):
    """"営業未払金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class OperatingAccountsReceivableCA(Enum):
    """"営業未収入金、流動資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class OperatingCost(Enum):
    """"営業原価"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class OperatingExpenses(Enum):
    """"営業費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class OperatingExpensesAndCostOfSalesOfTransportationRWY(Enum):
    """"運輸業等営業費及び売上原価、鉄道事業"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class OperatingExpensesINS(Enum):
    """"経常費用、保険業"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class OperatingExpensesRWY(Enum):
    """"営業費、鉄道事業"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class OperatingGrossProfit(Enum):
    """"営業総利益又は営業総損失（△）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class OperatingIncome(Enum):
    """"営業利益又は営業損失（△）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ 個別又は非連結その他 """
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER__OTHER_REPORTABLE_SEGMENTS_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember_OtherReportableSegmentsMember'
    """ 個別又は非連結その他 """
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER__RECONCILING_ITEMS_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember_ReconcilingItemsMember'
    """ 個別又は非連結調整項目 """
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER__REPORTABLE_SEGMENTS_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember_ReportableSegmentsMember'
    """ 個別又は非連結報告セグメント """
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember_TotalOfReportableSegmentsAndOthersMember'
    """ 個別又は非連結事業セグメント合計 """
    CURRENT_YTD_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'CurrentYTDDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    CURRENT_YTD_DURATION__OTHER_REPORTABLE_SEGMENTS_MEMBER = 'CurrentYTDDuration_OtherReportableSegmentsMember'
    """ その他 """
    CURRENT_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'CurrentYTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    CURRENT_YTD_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'CurrentYTDDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    CURRENT_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'CurrentYTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__OTHER_REPORTABLE_SEGMENTS_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_OtherReportableSegmentsMember'
    """ 当年度会計期間個別又は非連結その他 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RECONCILING_ITEMS_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_ReconcilingItemsMember'
    """ 当年度会計期間個別又は非連結調整項目 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__REPORTABLE_SEGMENTS_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_ReportableSegmentsMember'
    """ 当年度会計期間個別又は非連結報告セグメント """
    CURRENT_YEAR_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'CurrentYearDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ 当年度会計期間その他 """
    CURRENT_YEAR_DURATION__OTHER_REPORTABLE_SEGMENTS_MEMBER = 'CurrentYearDuration_OtherReportableSegmentsMember'
    """ 当年度会計期間その他 """
    CURRENT_YEAR_DURATION__RECONCILING_ITEMS_MEMBER = 'CurrentYearDuration_ReconcilingItemsMember'
    """ 当年度会計期間調整項目 """
    CURRENT_YEAR_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'CurrentYearDuration_ReportableSegmentsMember'
    """ 当年度会計期間報告セグメント """
    CURRENT_YEAR_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'CurrentYearDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 当年度会計期間事業セグメント合計 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ 個別又は非連結その他 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER__RECONCILING_ITEMS_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember_ReconcilingItemsMember'
    """ 個別又は非連結調整項目 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER__REPORTABLE_SEGMENTS_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember_ReportableSegmentsMember'
    """ 個別又は非連結報告セグメント """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember_TotalOfReportableSegmentsAndOthersMember'
    """ 個別又は非連結事業セグメント合計 """
    PRIOR1_YTD_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'Prior1YTDDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    PRIOR1_YTD_DURATION__OTHER_REPORTABLE_SEGMENTS_MEMBER = 'Prior1YTDDuration_OtherReportableSegmentsMember'
    """ その他 """
    PRIOR1_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1YTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_YTD_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'Prior1YTDDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    PRIOR1_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1YTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__OTHER_REPORTABLE_SEGMENTS_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_OtherReportableSegmentsMember'
    """ 個別又は非連結その他 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RECONCILING_ITEMS_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_ReconcilingItemsMember'
    """ 個別又は非連結調整項目 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__REPORTABLE_SEGMENTS_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_ReportableSegmentsMember'
    """ 個別又は非連結報告セグメント """
    PRIOR1_YEAR_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'Prior1YearDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    PRIOR1_YEAR_DURATION__OTHER_REPORTABLE_SEGMENTS_MEMBER = 'Prior1YearDuration_OtherReportableSegmentsMember'
    """ その他 """
    PRIOR1_YEAR_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1YearDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_YEAR_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'Prior1YearDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    PRIOR1_YEAR_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1YearDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """


class OperatingIncomeINS(Enum):
    """"経常収益、保険業"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'CurrentYTDDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    CURRENT_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'CurrentYTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    CURRENT_YTD_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'CurrentYTDDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    CURRENT_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'CurrentYTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'Prior1YTDDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    PRIOR1_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1YTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_YTD_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'Prior1YTDDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    PRIOR1_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1YTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """


class OperatingIncomeOpeCF(Enum):
    """"営業収入、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class OperatingLoansCA(Enum):
    """"営業貸付金、流動資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class OperatingRevenue1(Enum):
    """"営業収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'CurrentYTDDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    CURRENT_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'CurrentYTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    CURRENT_YTD_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'CurrentYTDDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    CURRENT_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'CurrentYTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    CURRENT_YEAR_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'CurrentYearDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ 当年度会計期間その他 """
    CURRENT_YEAR_DURATION__RECONCILING_ITEMS_MEMBER = 'CurrentYearDuration_ReconcilingItemsMember'
    """ 当年度会計期間調整項目 """
    CURRENT_YEAR_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'CurrentYearDuration_ReportableSegmentsMember'
    """ 当年度会計期間報告セグメント """
    CURRENT_YEAR_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'CurrentYearDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 当年度会計期間事業セグメント合計 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'Prior1YTDDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    PRIOR1_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1YTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_YTD_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'Prior1YTDDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    PRIOR1_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1YTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'Prior1YearDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    PRIOR1_YEAR_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1YearDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_YEAR_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'Prior1YearDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    PRIOR1_YEAR_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1YearDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """


class OperatingRevenueCMD(Enum):
    """"営業収益、商品先物取引業"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class OperatingRevenueRWY(Enum):
    """"営業収益、鉄道事業"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class OperationalInvestmentSecuritiesCA(Enum):
    """"営業投資有価証券、流動資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class OrdinaryExpensesBNK(Enum):
    """"経常費用、銀行業"""
    INTERIM_DURATION = 'InterimDuration'
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class OrdinaryIncome(Enum):
    """"経常利益又は経常損失（△）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YTD_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'CurrentYTDDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    CURRENT_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'CurrentYTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    CURRENT_YTD_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'CurrentYTDDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    CURRENT_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'CurrentYTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    INTERIM_DURATION = 'InterimDuration'
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    INTERIM_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'InterimDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    INTERIM_DURATION__RECONCILING_ITEMS_MEMBER = 'InterimDuration_ReconcilingItemsMember'
    """ 調整項目 """
    INTERIM_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'InterimDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    INTERIM_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'InterimDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_INTERIM_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'Prior1InterimDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    PRIOR1_INTERIM_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1InterimDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_INTERIM_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'Prior1InterimDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    PRIOR1_INTERIM_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1InterimDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'Prior1YTDDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    PRIOR1_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1YTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_YTD_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'Prior1YTDDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    PRIOR1_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1YTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class OrdinaryIncomeBNK(Enum):
    """"経常収益、銀行業"""
    INTERIM_DURATION = 'InterimDuration'
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    INTERIM_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'InterimDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    INTERIM_DURATION__RECONCILING_ITEMS_MEMBER = 'InterimDuration_ReconcilingItemsMember'
    """ 調整項目 """
    INTERIM_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'InterimDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    INTERIM_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'InterimDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_INTERIM_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'Prior1InterimDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    PRIOR1_INTERIM_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1InterimDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_INTERIM_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'Prior1InterimDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    PRIOR1_INTERIM_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1InterimDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """


class OtherAssetsAssetsBNK(Enum):
    """"その他資産、資産の部、銀行業"""
    INTERIM_INSTANT = 'InterimInstant'
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class OtherAssetsAssetsINS(Enum):
    """"その他資産、資産の部、保険業"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class OtherCA(Enum):
    """"その他、流動資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class OtherCL(Enum):
    """"その他、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class OtherCOSExpOA(Enum):
    """"その他、営業活動による費用・売上原価"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class OtherCapitalSurplus(Enum):
    """"その他資本剰余金"""
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class OtherComprehensiveIncome(Enum):
    """"その他の包括利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class OtherCostCOSExpOA(Enum):
    """"その他の原価、営業活動による費用・売上原価"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class OtherEI(Enum):
    """"その他、特別利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class OtherEL(Enum):
    """"その他、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    INTERIM_DURATION = 'InterimDuration'
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class OtherExpensesOEBNK(Enum):
    """"その他経常費用、経常費用、銀行業"""
    INTERIM_DURATION = 'InterimDuration'
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class OtherExpensesSGA(Enum):
    """"その他の経費、販売費及び一般管理費"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class OtherFacilitiesPPEGAS(Enum):
    """"その他の設備、有形固定資産、ガス事業"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class OtherFinancialRevenueRevOA(Enum):
    """"その他の金融収益、営業活動による収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class OtherGeneralAndAdministrativeExpensesSGA(Enum):
    """"その他の一般管理費、販売費及び一般管理費"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class OtherIA(Enum):
    """"その他、無形固定資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class OtherIOA(Enum):
    """"その他、投資その他の資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class OtherIncomeOIBNK(Enum):
    """"その他経常収益、経常収益、銀行業"""
    INTERIM_DURATION = 'InterimDuration'
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class OtherIntangibleAssetsLEA(Enum):
    """"その他の無形固定資産、リース事業"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class OtherInventories(Enum):
    """"その他の棚卸資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class OtherLiabilitiesLiabilitiesBNK(Enum):
    """"その他負債、負債の部、銀行業"""
    INTERIM_INSTANT = 'InterimInstant'
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class OtherLiabilitiesLiabilitiesINS(Enum):
    """"その他負債、負債の部、保険業"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class OtherLossGainOpeCF(Enum):
    """"その他の損益（△は益）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class OtherNCL(Enum):
    """"その他、固定負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class OtherNOE(Enum):
    """"その他、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class OtherNOI(Enum):
    """"その他、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class OtherNetFinCF(Enum):
    """"その他、財務活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class OtherNetInvCF(Enum):
    """"その他、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class OtherNetInvCFSubtotalINS(Enum):
    """"その他、投資活動によるキャッシュ・フロー、小計の下、保険業"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class OtherNetOpeCF(Enum):
    """"その他、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class OtherNetOpeCFSubtotal(Enum):
    """"その他、営業活動によるキャッシュ・フロー、小計の下"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class OtherNetPPE(Enum):
    """"その他（純額）、有形固定資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class OtherNonOperatingExpensesIncomeOpeCF(Enum):
    """"その他の営業外損益（△は益）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class OtherOperatingAssetsCALEA(Enum):
    """"その他の営業資産、流動資産、リース事業"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class OtherOperatingExpensesOEINS(Enum):
    """"その他経常費用、経常費用、保険業"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class OtherOperatingExpensesSPF(Enum):
    """"その他の営業費用、特定金融業"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class OtherOperatingIncomeOIINS(Enum):
    """"その他経常収益、経常収益、保険業"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class OtherOperatingRevenue1RevOA(Enum):
    """"その他の営業収益、営業活動による収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class OtherOperatingRevenueCMD(Enum):
    """"その他、営業収益、商品先物取引業"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class OtherOrdinaryExpensesOEBNK(Enum):
    """"その他業務費用、経常費用、銀行業"""
    INTERIM_DURATION = 'InterimDuration'
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class OtherOrdinaryIncomeOIBNK(Enum):
    """"その他業務収益、経常収益、銀行業"""
    INTERIM_DURATION = 'InterimDuration'
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class OtherOtherAssetsAssetsBNK(Enum):
    """"その他の資産、その他資産、資産の部、銀行業"""
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class OtherOtherLiabilitiesLiabilitiesBNK(Enum):
    """"その他の負債、その他負債、負債の部、銀行業"""
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class OtherPPE(Enum):
    """"その他、有形固定資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class OtherPaymentsFinCF(Enum):
    """"その他の支出、財務活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class OtherPaymentsInvCF(Enum):
    """"その他の支出、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class OtherPaymentsOpeCF(Enum):
    """"その他の支出、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class OtherPersonalExpensesSGA(Enum):
    """"その他の人件費、販売費及び一般管理費"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class OtherProceedsInvCF(Enum):
    """"その他の収入、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class OtherProceedsOpeCF(Enum):
    """"その他の収入、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class OtherProvisionCL(Enum):
    """"その他の引当金、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class OtherProvisionNCL(Enum):
    """"その他の引当金、固定負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class OtherRetainedEarnings(Enum):
    """"その他利益剰余金"""
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class OtherRevOA(Enum):
    """"その他、営業活動による収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class OtherRevenue1RevOA(Enum):
    """"その他の収益、営業活動による収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'CurrentYTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    CURRENT_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'CurrentYTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1YTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1YTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """


class OtherRevenue2RevOA(Enum):
    """"その他の収入、営業活動による収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class OtherSGA(Enum):
    """"その他、販売費及び一般管理費"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class OtherSellingExpensesSGA(Enum):
    """"その他の販売費、販売費及び一般管理費"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class OutstandingClaimsLiabilitiesINS(Enum):
    """"支払備金、負債の部、保険業"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class OwnUsedAssetsPPELEA(Enum):
    """"社用資産、有形固定資産、リース事業"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class PackingAndTransportationExpensesSGA(Enum):
    """"荷造運搬費、販売費及び一般管理費"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class PatentRight(Enum):
    """"特許権"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class PayablesUnderFluidityLeaseReceivablesCLLEA(Enum):
    """"債権流動化に伴う支払債務、流動負債、リース事業"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class PayablesUnderRepurchaseAgreementsLiabilitiesBNK(Enum):
    """"売現先勘定、負債の部、銀行業"""
    INTERIM_INSTANT = 'InterimInstant'
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class PayablesUnderSecuritiesLendingTransactionsLiabilitiesBNK(Enum):
    """"債券貸借取引受入担保金、負債の部、銀行業"""
    INTERIM_INSTANT = 'InterimInstant'
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class PaymentsAssociatedWithDisasterLoss2OpeCF(Enum):
    """"災害による損失の支払額、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class PaymentsForAssetRetirementObligationsInvCF(Enum):
    """"資産除去債務の履行による支出、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class PaymentsForBusinessRestructuringOpeCF(Enum):
    """"事業再編による支出、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class PaymentsForDirectorsRetirementBenefitsOpeCF(Enum):
    """"役員退職慰労金の支払額、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PaymentsForExtraRetirementPaymentsOpeCF(Enum):
    """"特別退職金の支払額、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PaymentsForFinanceOpeCFBNK(Enum):
    """"資金調達による支出、営業活動によるキャッシュ・フロー、銀行業"""
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'


class PaymentsForGuaranteeDepositsInvCF(Enum):
    """"差入保証金の差入による支出、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class PaymentsForInvestmentsInCapitalInvCF(Enum):
    """"出資金の払込による支出、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PaymentsForInvestmentsInRealEstatesInvCF(Enum):
    """"投資不動産の取得による支出、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class PaymentsForIssuanceOfCommonStockFinCF(Enum):
    """"株式の発行による支出、財務活動によるキャッシュ・フロー"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class PaymentsForLeaseAndGuaranteeDepositsInvCF(Enum):
    """"敷金及び保証金の差入による支出、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class PaymentsForLeaseDepositsInvCF(Enum):
    """"敷金の差入による支出、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class PaymentsForLongTermAccountsPayableOtherFinCF(Enum):
    """"長期未払金の返済による支出、財務活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PaymentsForOtherOperatingActivityOpeCF(Enum):
    """"その他の営業支出、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class PaymentsForPayrollOpeCF(Enum):
    """"人件費の支出、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class PaymentsForRawMaterialsAndGoodsOpeCF(Enum):
    """"原材料又は商品の仕入れによる支出、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class PaymentsForRemovalExpensesOpeCF(Enum):
    """"移転費用の支払額、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PaymentsForRetirementOfNoncurrentAssetsInvCF(Enum):
    """"固定資産の除却による支出、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class PaymentsForRetirementOfPropertyPlantAndEquipmentInvCF(Enum):
    """"有形固定資産の除却による支出、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class PaymentsForSalesOfInvestmentsInSubsidiariesResultingInChangeInScopeOfConsolidationInvCF(Enum):
    """"連結の範囲の変更を伴う子会社株式の売却による支出、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PaymentsForSalesOfNotesReceivableTradeOpeCF(Enum):
    """"手形売却に伴う支払額、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PaymentsForTransferOfBusiness2InvCF(Enum):
    """"事業譲受による支出、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PaymentsFromChangesInOwnershipInterestsInSubsidiariesThatDoNotResultInChangeInScopeOfConsolidationFinCF(Enum):
    """"連結の範囲の変更を伴わない子会社株式の取得による支出、財務活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class PaymentsIntoTimeDepositsInvCF(Enum):
    """"定期預金の預入による支出、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class PaymentsOfInvestmentAndLoansReceivableInvCF(Enum):
    """"投融資による支出、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class PaymentsOfListingExpensesFinCF(Enum):
    """"上場関連費用の支出、財務活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class PaymentsOfLoansReceivableInvCF(Enum):
    """"貸付けによる支出、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class PaymentsOfLoansReceivableToEmployeesInvCF(Enum):
    """"従業員に対する貸付けによる支出、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class PaymentsOfLongTermLoansReceivableInvCF(Enum):
    """"長期貸付けによる支出、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class PaymentsOfShortTermLoansReceivableInvCF(Enum):
    """"短期貸付けによる支出、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PenaltyIncomeEI(Enum):
    """"違約金収入、特別利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PenaltyIncomeNOI(Enum):
    """"違約金収入、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PerItemRevenueRevOA(Enum):
    """"個別信用購入あっせん収益、営業活動による収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PersonalExpensesSGA(Enum):
    """"人件費、販売費及び一般管理費"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PolicyReserveLiabilitiesINS(Enum):
    """"責任準備金、負債の部、保険業"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class PowerUtilitiesExpensesSGA(Enum):
    """"動力用水光熱費、販売費及び一般管理費"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class PrepaidExpenses(Enum):
    """"前払費用"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class PrepaidPensionCostAssets(Enum):
    """"前払年金費用、資産の部"""
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class PrepaidPensionCostIOA(Enum):
    """"前払年金費用、投資その他の資産"""
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class ProceedsFromCancellationOfInsuranceFundsInvCF(Enum):
    """"保険積立金の解約による収入、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class ProceedsFromChangesInOwnershipInterestsInSubsidiariesThatDoNotResultInChangeInScopeOfConsolidationFinCF(Enum):
    """"連結の範囲の変更を伴わない子会社株式の売却による収入、財務活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromCollectionOfGuaranteeDepositsInvCF(Enum):
    """"差入保証金の回収による収入、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class ProceedsFromCollectionOfLeaseAndGuaranteeDepositsInvCF(Enum):
    """"敷金及び保証金の回収による収入、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class ProceedsFromCompensationForExpropriationOpeCF(Enum):
    """"収用補償金の受取額、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromCompensationForRemovalOpeCF(Enum):
    """"移転補償金の受取額、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromCompensationOpeCF(Enum):
    """"補償金の受取額、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromContributionForConstructionOpeCF(Enum):
    """"工事負担金等受入額、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromContributionReceivedForConstructionInvCF(Enum):
    """"工事負担金等受入による収入、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromDisposalOfTreasuryStockFinCF(Enum):
    """"自己株式の処分による収入、財務活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class ProceedsFromDistributionOfInvestmentInPartnershipsInvCF(Enum):
    """"投資事業組合からの分配による収入、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class ProceedsFromDividendsIncomeFromEquityMethodAffiliateOpeCF(Enum):
    """"持分法適用会社からの配当金の受取額、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromExerciseOfStockOptionFinCF(Enum):
    """"ストックオプションの行使による収入、財務活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromFundManagementOpeCFBNK(Enum):
    """"資金運用による収入、営業活動によるキャッシュ・フロー、銀行業"""
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'


class ProceedsFromGuaranteeDepositsReceivedInvCF(Enum):
    """"預り保証金の受入による収入、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromInsuranceIncomeOpeCF(Enum):
    """"保険金の受取額、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class ProceedsFromIssuanceOfBondsFinCF(Enum):
    """"社債の発行による収入、財務活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class ProceedsFromIssuanceOfCommercialPapersFinCF(Enum):
    """"コマーシャル・ペーパーの発行による収入、財務活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromIssuanceOfCommonStockFinCF(Enum):
    """"株式の発行による収入、財務活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class ProceedsFromIssuanceOfStockResultingFromExerciseOfSubscriptionRightsToSharesFinCF(Enum):
    """"新株予約権の行使による株式の発行による収入、財務活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class ProceedsFromIssuanceOfSubscriptionRightsToSharesFinCF(Enum):
    """"新株予約権の発行による収入、財務活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class ProceedsFromLiquidationOfSubsidiariesInvCF(Enum):
    """"子会社の清算による収入、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromLongTermLoansPayableFinCF(Enum):
    """"長期借入れによる収入、財務活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class ProceedsFromMaturityOfInsuranceFundsInvCF(Enum):
    """"保険積立金の払戻による収入、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromPurchaseOfInvestmentsInSubsidiariesResultingInChangeInScopeOfConsolidationInvCF(Enum):
    """"連結の範囲の変更を伴う子会社株式の取得による収入、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class ProceedsFromRedemptionOfInvestmentSecuritiesInvCF(Enum):
    """"投資有価証券の償還による収入、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class ProceedsFromRedemptionOfSecuritiesInvCF(Enum):
    """"有価証券の償還による収入、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class ProceedsFromRedemptionOfSecuritiesInvCFBNK(Enum):
    """"有価証券の償還による収入、投資活動によるキャッシュ・フロー、銀行業"""
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'


class ProceedsFromRentIncomeOpeCF(Enum):
    """"賃貸料の受取額、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromRentalOfRealEstateForInvestmentInvCF(Enum):
    """"投資不動産の賃貸による収入、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromSaleAndLeasebackFinCF(Enum):
    """"セール・アンド・リースバックによる収入、財務活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromSalesAndRedemptionOfInvestmentSecuritiesInvCF(Enum):
    """"投資有価証券の売却及び償還による収入、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class ProceedsFromSalesAndRedemptionOfSecuritiesInvCFINS(Enum):
    """"有価証券の売却・償還による収入、投資活動によるキャッシュ・フロー、保険業"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromSalesAndRedemptionOfShortTermAndLongTermInvestmentSecuritiesInvCF(Enum):
    """"有価証券及び投資有価証券の売却及び償還による収入、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class ProceedsFromSalesOfGolfClubMembershipsInvCF(Enum):
    """"ゴルフ会員権の売却による収入、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromSalesOfIntangibleAssetsInvCF(Enum):
    """"無形固定資産の売却による収入、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromSalesOfInvestmentSecuritiesInvCF(Enum):
    """"投資有価証券の売却による収入、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class ProceedsFromSalesOfInvestmentsInRealEstatesInvCF(Enum):
    """"投資不動産の売却による収入、投資活動によるキャッシュ・フロー"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class ProceedsFromSalesOfInvestmentsInSubsidiariesInvCF(Enum):
    """"子会社株式の売却による収入、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromSalesOfInvestmentsInSubsidiariesResultingInChangeInScopeOfConsolidationInvCF(Enum):
    """"連結の範囲の変更を伴う子会社株式の売却による収入、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class ProceedsFromSalesOfNoncurrentAssetsInvCF(Enum):
    """"固定資産の売却による収入、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class ProceedsFromSalesOfPropertyPlantAndEquipmentAndIntangibleAssetsInvCF(Enum):
    """"有形及び無形固定資産の売却による収入、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class ProceedsFromSalesOfPropertyPlantAndEquipmentInvCF(Enum):
    """"有形固定資産の売却による収入、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class ProceedsFromSalesOfSecuritiesInvCFBNK(Enum):
    """"有価証券の売却による収入、投資活動によるキャッシュ・フロー、銀行業"""
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'


class ProceedsFromSalesOfShortTermInvestmentSecuritiesInvCF(Enum):
    """"有価証券の売却による収入、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromSalesOfStocksOfSubsidiariesAndAffiliatesInvCF(Enum):
    """"関係会社株式の売却による収入、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class ProceedsFromSalesOfTreasuryStockFinCF(Enum):
    """"自己株式の売却による収入、財務活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class ProceedsFromSalesOfTrustBeneficiaryRightInvCF(Enum):
    """"信託受益権の売却による収入、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromShareIssuanceToNonControllingShareholdersFinCF(Enum):
    """"非支配株主からの払込みによる収入、財務活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromShareOfProfitsOnInvestmentsInCapitalInvCF(Enum):
    """"出資金の分配による収入、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromSubsidiesForEmploymentAdjustmentOpeCF(Enum):
    """"雇用調整助成金の受取額、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromSubsidyIncome2OpeCF(Enum):
    """"助成金の受取額、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class ProceedsFromSubsidyOpeCF(Enum):
    """"補助金の受取額、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class ProceedsFromTransferOfBusinessInvCF(Enum):
    """"事業譲渡による収入、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class ProceedsFromWithdrawalOfInvestmentsInSilentPartnershipInvCF(Enum):
    """"匿名組合出資金の払戻による収入、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromWithdrawalOfTimeDepositsInvCF(Enum):
    """"定期預金の払戻による収入、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class ProductionFacilitiesPPEGAS(Enum):
    """"製造設備、有形固定資産、ガス事業"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ProfitLoss(Enum):
    """"当期純利益又は当期純損失（△）（平成26年3月28日財規等改正後）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CAPITAL_STOCK_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_CapitalStockMember'
    """ 当年度会計期間個別又は非連結資本金 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CAPITAL_SURPLUS_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_CapitalSurplusMember'
    """ 当年度会計期間個別又は非連結資本剰余金 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__LEGAL_CAPITAL_SURPLUS_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_LegalCapitalSurplusMember'
    """ 当年度会計期間個別又は非連結資本準備金 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_BROUGHT_FORWARD_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_RetainedEarningsBroughtForwardMember'
    """ 当年度会計期間個別又は非連結繰越利益剰余金 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_RetainedEarningsMember'
    """ 当年度会計期間個別又は非連結利益剰余金 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__SHAREHOLDERS_EQUITY_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_ShareholdersEquityMember'
    """ 当年度会計期間個別又は非連結株主資本 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__SUBSCRIPTION_RIGHTS_TO_SHARES_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_SubscriptionRightsToSharesMember'
    """ 当年度会計期間個別又は非連結新株予約権 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__TREASURY_STOCK_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_TreasuryStockMember'
    """ 当年度会計期間個別又は非連結自己株式 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__VALUATION_AND_TRANSLATION_ADJUSTMENTS_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_ValuationAndTranslationAdjustmentsMember'
    """ 当年度会計期間個別又は非連結評価・換算差額等 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__VALUATION_DIFFERENCE_ON_AVAILABLE_FOR_SALE_SECURITIES_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_ValuationDifferenceOnAvailableForSaleSecuritiesMember'
    """ 当年度会計期間個別又は非連結その他有価証券評価差額金 """
    INTERIM_DURATION = 'InterimDuration'
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_BROUGHT_FORWARD_MEMBER = 'InterimDuration_NonConsolidatedMember_RetainedEarningsBroughtForwardMember'
    """ 個別又は非連結繰越利益剰余金 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_MEMBER = 'InterimDuration_NonConsolidatedMember_RetainedEarningsMember'
    """ 個別又は非連結利益剰余金 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__SHAREHOLDERS_EQUITY_MEMBER = 'InterimDuration_NonConsolidatedMember_ShareholdersEquityMember'
    """ 個別又は非連結株主資本 """
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_BROUGHT_FORWARD_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_RetainedEarningsBroughtForwardMember'
    """ 個別又は非連結繰越利益剰余金 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_RetainedEarningsMember'
    """ 個別又は非連結利益剰余金 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_ShareholdersEquityMember'
    """ 個別又は非連結株主資本 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CAPITAL_STOCK_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_CapitalStockMember'
    """ 個別又は非連結資本金 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CAPITAL_SURPLUS_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_CapitalSurplusMember'
    """ 個別又は非連結資本剰余金 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__LEGAL_CAPITAL_SURPLUS_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_LegalCapitalSurplusMember'
    """ 個別又は非連結資本準備金 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_BROUGHT_FORWARD_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_RetainedEarningsBroughtForwardMember'
    """ 個別又は非連結繰越利益剰余金 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_RetainedEarningsMember'
    """ 個別又は非連結利益剰余金 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_ShareholdersEquityMember'
    """ 個別又は非連結株主資本 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__SUBSCRIPTION_RIGHTS_TO_SHARES_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_SubscriptionRightsToSharesMember'
    """ 個別又は非連結新株予約権 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__TREASURY_STOCK_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_TreasuryStockMember'
    """ 個別又は非連結自己株式 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__VALUATION_AND_TRANSLATION_ADJUSTMENTS_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_ValuationAndTranslationAdjustmentsMember'
    """ 個別又は非連結評価・換算差額等 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__VALUATION_DIFFERENCE_ON_AVAILABLE_FOR_SALE_SECURITIES_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_ValuationDifferenceOnAvailableForSaleSecuritiesMember'
    """ 個別又は非連結その他有価証券評価差額金 """


class ProfitLossAttributableToNonControllingInterests(Enum):
    """"非支配株主に帰属する当期純利益又は非支配株主に帰属する当期純損失（△）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class ProfitLossAttributableToOwnersOfParent(Enum):
    """"親会社株主に帰属する当期純利益又は親会社株主に帰属する当期純損失（△）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'CurrentYTDDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    CURRENT_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'CurrentYTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    CURRENT_YTD_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'CurrentYTDDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    CURRENT_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'CurrentYTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__CAPITAL_STOCK_MEMBER = 'CurrentYearDuration_CapitalStockMember'
    """ 当年度会計期間資本金 """
    CURRENT_YEAR_DURATION__CAPITAL_SURPLUS_MEMBER = 'CurrentYearDuration_CapitalSurplusMember'
    """ 当年度会計期間資本剰余金 """
    CURRENT_YEAR_DURATION__NON_CONTROLLING_INTERESTS_MEMBER = 'CurrentYearDuration_NonControllingInterestsMember'
    """ 当年度会計期間非支配株主持分 """
    CURRENT_YEAR_DURATION__RETAINED_EARNINGS_BROUGHT_FORWARD_MEMBER = 'CurrentYearDuration_RetainedEarningsBroughtForwardMember'
    """ 当年度会計期間繰越利益剰余金 """
    CURRENT_YEAR_DURATION__RETAINED_EARNINGS_MEMBER = 'CurrentYearDuration_RetainedEarningsMember'
    """ 当年度会計期間利益剰余金 """
    CURRENT_YEAR_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'CurrentYearDuration_ShareholdersEquityMember'
    """ 当年度会計期間株主資本 """
    CURRENT_YEAR_DURATION__SUBSCRIPTION_RIGHTS_TO_SHARES_MEMBER = 'CurrentYearDuration_SubscriptionRightsToSharesMember'
    """ 当年度会計期間新株予約権 """
    CURRENT_YEAR_DURATION__TREASURY_STOCK_MEMBER = 'CurrentYearDuration_TreasuryStockMember'
    """ 当年度会計期間自己株式 """
    CURRENT_YEAR_DURATION__VALUATION_AND_TRANSLATION_ADJUSTMENTS_MEMBER = 'CurrentYearDuration_ValuationAndTranslationAdjustmentsMember'
    """ 当年度会計期間評価・換算差額等 """
    INTERIM_DURATION = 'InterimDuration'
    INTERIM_DURATION__RETAINED_EARNINGS_MEMBER = 'InterimDuration_RetainedEarningsMember'
    """ 利益剰余金 """
    INTERIM_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'InterimDuration_ShareholdersEquityMember'
    """ 株主資本 """
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_INTERIM_DURATION__RETAINED_EARNINGS_MEMBER = 'Prior1InterimDuration_RetainedEarningsMember'
    """ 利益剰余金 """
    PRIOR1_INTERIM_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1InterimDuration_ShareholdersEquityMember'
    """ 株主資本 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'Prior1YTDDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    PRIOR1_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1YTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_YTD_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'Prior1YTDDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    PRIOR1_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1YTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__CAPITAL_STOCK_MEMBER = 'Prior1YearDuration_CapitalStockMember'
    """ 資本金 """
    PRIOR1_YEAR_DURATION__CAPITAL_SURPLUS_MEMBER = 'Prior1YearDuration_CapitalSurplusMember'
    """ 資本剰余金 """
    PRIOR1_YEAR_DURATION__NON_CONTROLLING_INTERESTS_MEMBER = 'Prior1YearDuration_NonControllingInterestsMember'
    """ 非支配株主持分 """
    PRIOR1_YEAR_DURATION__RETAINED_EARNINGS_MEMBER = 'Prior1YearDuration_RetainedEarningsMember'
    """ 利益剰余金 """
    PRIOR1_YEAR_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1YearDuration_ShareholdersEquityMember'
    """ 株主資本 """
    PRIOR1_YEAR_DURATION__SUBSCRIPTION_RIGHTS_TO_SHARES_MEMBER = 'Prior1YearDuration_SubscriptionRightsToSharesMember'
    """ 新株予約権 """
    PRIOR1_YEAR_DURATION__TREASURY_STOCK_MEMBER = 'Prior1YearDuration_TreasuryStockMember'
    """ 自己株式 """
    PRIOR1_YEAR_DURATION__VALUATION_AND_TRANSLATION_ADJUSTMENTS_MEMBER = 'Prior1YearDuration_ValuationAndTranslationAdjustmentsMember'
    """ 評価・換算差額等 """


class PromotionExpensesSGA(Enum):
    """"販売促進費、販売費及び一般管理費"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class PropertyForLeasePPELEA(Enum):
    """"賃貸資産、有形固定資産、リース事業"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class PropertyPlantAndEquipment(Enum):
    """"有形固定資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    INTERIM_INSTANT = 'InterimInstant'
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class ProvisionCL(Enum):
    """"引当金、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class ProvisionForBonuses(Enum):
    """"賞与引当金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    INTERIM_INSTANT = 'InterimInstant'
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class ProvisionForBonusesSGA(Enum):
    """"賞与引当金繰入額、販売費及び一般管理費"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class ProvisionForBusinessStructureImprovementCL(Enum):
    """"事業構造改善引当金、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ProvisionForBusinessStructureImprovementEL(Enum):
    """"事業構造改善引当金繰入額、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProvisionForBusinessStructureImprovementNCL(Enum):
    """"事業構造改善引当金、固定負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ProvisionForContingentLossCL(Enum):
    """"偶発損失引当金、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    INTERIM_INSTANT = 'InterimInstant'
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class ProvisionForContingentLossEL(Enum):
    """"偶発損失引当金繰入額、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProvisionForContingentLossLiabilitiesBNK(Enum):
    """"偶発損失引当金、負債の部、銀行業"""
    INTERIM_INSTANT = 'InterimInstant'
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class ProvisionForContingentLossNCL(Enum):
    """"偶発損失引当金、固定負債"""
    INTERIM_INSTANT = 'InterimInstant'
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class ProvisionForDirectorsBonuses(Enum):
    """"役員賞与引当金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    INTERIM_INSTANT = 'InterimInstant'
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class ProvisionForDirectorsBonusesSGA(Enum):
    """"役員賞与引当金繰入額、販売費及び一般管理費"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class ProvisionForDirectorsRetirementBenefits(Enum):
    """"役員退職慰労引当金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    INTERIM_INSTANT = 'InterimInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class ProvisionForDirectorsRetirementBenefitsEL(Enum):
    """"役員退職慰労引当金繰入額、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProvisionForDirectorsRetirementBenefitsSGA(Enum):
    """"役員退職慰労引当金繰入額、販売費及び一般管理費"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class ProvisionForEnvironmentalMeasuresCL(Enum):
    """"環境対策引当金、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ProvisionForEnvironmentalMeasuresNCL(Enum):
    """"環境対策引当金、固定負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ProvisionForGasHolderRepairsGAS(Enum):
    """"ガスホルダー修繕引当金、ガス事業"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ProvisionForLossOnBusinessLiquidationEL(Enum):
    """"事業整理損失引当金繰入額、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProvisionForLossOnBusinessOfSubsidiariesAndAffiliatesEL(Enum):
    """"関係会社事業損失引当金繰入額、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class ProvisionForLossOnBusinessOfSubsidiariesAndAffiliatesNCL(Enum):
    """"関係会社事業損失引当金、固定負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class ProvisionForLossOnConstructionContracts(Enum):
    """"工事損失引当金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class ProvisionForLossOnDisasterCL(Enum):
    """"災害損失引当金、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class ProvisionForLossOnDisasterEL(Enum):
    """"災害損失引当金繰入額、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProvisionForLossOnGuarantees(Enum):
    """"債務保証損失引当金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class ProvisionForLossOnGuaranteesCL(Enum):
    """"債務保証損失引当金、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    INTERIM_INSTANT = 'InterimInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ProvisionForLossOnGuaranteesEL(Enum):
    """"債務保証損失引当金繰入額、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProvisionForLossOnInterestRepaymentLiabilitiesBNK(Enum):
    """"利息返還損失引当金、負債の部、銀行業"""
    INTERIM_INSTANT = 'InterimInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ProvisionForLossOnInterestRepaymentNCL(Enum):
    """"利息返還損失引当金、固定負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ProvisionForLossOnLiquidationOfSubsidiariesAndAffiliatesCL(Enum):
    """"関係会社整理損失引当金、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ProvisionForLossOnLiquidationOfSubsidiariesAndAffiliatesNCL(Enum):
    """"関係会社整理損失引当金、固定負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ProvisionForLossOnLitigationCL(Enum):
    """"訴訟損失引当金、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    INTERIM_INSTANT = 'InterimInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class ProvisionForLossOnLitigationEL(Enum):
    """"訴訟損失引当金繰入額、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProvisionForLossOnLitigationNCL(Enum):
    """"訴訟損失引当金、固定負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ProvisionForLossOnOrderReceivedCL(Enum):
    """"受注損失引当金、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class ProvisionForLossOnStoreClosing(Enum):
    """"店舗閉鎖損失引当金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class ProvisionForLossOnStoreClosingEL(Enum):
    """"店舗閉鎖損失引当金繰入額、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class ProvisionForPointCardCertificatesCL(Enum):
    """"ポイント引当金、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    INTERIM_INSTANT = 'InterimInstant'
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class ProvisionForPointCardCertificatesNCL(Enum):
    """"ポイント引当金、固定負債"""
    INTERIM_INSTANT = 'InterimInstant'
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class ProvisionForProductWarranties(Enum):
    """"製品保証引当金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class ProvisionForProductWarrantiesNCL(Enum):
    """"製品保証引当金、固定負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ProvisionForProductWarrantiesSGA(Enum):
    """"製品保証引当金繰入額、販売費及び一般管理費"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProvisionForReimbursementOfDepositsLiabilitiesBNK(Enum):
    """"睡眠預金払戻損失引当金、負債の部、銀行業"""
    INTERIM_INSTANT = 'InterimInstant'
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class ProvisionForRepairsNCL(Enum):
    """"修繕引当金、固定負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ProvisionForRetirementBenefits(Enum):
    """"退職給付引当金"""
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class ProvisionForRetirementBenefitsSGA(Enum):
    """"退職給付引当金繰入額、販売費及び一般管理費"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class ProvisionForSafetyMeasuresGAS(Enum):
    """"保安対策引当金、ガス事業"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ProvisionForSalesPromotionExpenses(Enum):
    """"販売促進引当金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class ProvisionForShareBasedPaymentsCL(Enum):
    """"株式報酬引当金、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ProvisionForShareBasedPaymentsNCL(Enum):
    """"株式報酬引当金、固定負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    INTERIM_INSTANT = 'InterimInstant'
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class ProvisionForShareBasedPaymentsSGA(Enum):
    """"株式報酬引当金繰入額、販売費及び一般管理費"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProvisionForShareBasedRemunerationCL(Enum):
    """"株式給付引当金、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class ProvisionForShareBasedRemunerationForDirectorsAndOtherOfficersCL(Enum):
    """"役員株式給付引当金、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    INTERIM_INSTANT = 'InterimInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ProvisionForShareBasedRemunerationForDirectorsAndOtherOfficersNCL(Enum):
    """"役員株式給付引当金、固定負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    INTERIM_INSTANT = 'InterimInstant'
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class ProvisionForShareBasedRemunerationNCL(Enum):
    """"株式給付引当金、固定負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    INTERIM_INSTANT = 'InterimInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class ProvisionForShareBasedRemunerationSGA(Enum):
    """"株式給付引当金繰入額、販売費及び一般管理費"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class ProvisionForShareholderBenefitProgramCL(Enum):
    """"株主優待引当金、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class ProvisionForSpecialRepairs(Enum):
    """"特別修繕引当金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ProvisionForSpecialRepairsNCLWAT(Enum):
    """"特別修繕引当金、固定負債、海運業"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ProvisionForWarrantiesForCompletedConstruction(Enum):
    """"完成工事補償引当金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ProvisionNCL(Enum):
    """"引当金、固定負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class ProvisionOfAllowanceForDoubtfulAccountsEL(Enum):
    """"貸倒引当金繰入額、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProvisionOfAllowanceForDoubtfulAccountsNOE(Enum):
    """"貸倒引当金繰入額、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class ProvisionOfAllowanceForDoubtfulAccountsSGA(Enum):
    """"貸倒引当金繰入額、販売費及び一般管理費"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class ProvisionOfAllowanceForInvestmentLossEL(Enum):
    """"投資損失引当金繰入額、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class ProvisionOfGeneralReserve(Enum):
    """"別途積立金の積立"""
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__GENERAL_RESERVE_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_GeneralReserveMember'
    """ 当年度会計期間個別又は非連結別途積立金 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_BROUGHT_FORWARD_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_RetainedEarningsBroughtForwardMember'
    """ 当年度会計期間個別又は非連結繰越利益剰余金 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_RetainedEarningsMember'
    """ 当年度会計期間個別又は非連結利益剰余金 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__SHAREHOLDERS_EQUITY_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_ShareholdersEquityMember'
    """ 当年度会計期間個別又は非連結株主資本 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__GENERAL_RESERVE_MEMBER = 'InterimDuration_NonConsolidatedMember_GeneralReserveMember'
    """ 個別又は非連結別途積立金 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_BROUGHT_FORWARD_MEMBER = 'InterimDuration_NonConsolidatedMember_RetainedEarningsBroughtForwardMember'
    """ 個別又は非連結繰越利益剰余金 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_MEMBER = 'InterimDuration_NonConsolidatedMember_RetainedEarningsMember'
    """ 個別又は非連結利益剰余金 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__SHAREHOLDERS_EQUITY_MEMBER = 'InterimDuration_NonConsolidatedMember_ShareholdersEquityMember'
    """ 個別又は非連結株主資本 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__GENERAL_RESERVE_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_GeneralReserveMember'
    """ 個別又は非連結別途積立金 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_BROUGHT_FORWARD_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_RetainedEarningsBroughtForwardMember'
    """ 個別又は非連結繰越利益剰余金 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_RetainedEarningsMember'
    """ 個別又は非連結利益剰余金 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_ShareholdersEquityMember'
    """ 個別又は非連結株主資本 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__GENERAL_RESERVE_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_GeneralReserveMember'
    """ 個別又は非連結別途積立金 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_BROUGHT_FORWARD_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_RetainedEarningsBroughtForwardMember'
    """ 個別又は非連結繰越利益剰余金 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_RetainedEarningsMember'
    """ 個別又は非連結利益剰余金 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_ShareholdersEquityMember'
    """ 個別又は非連結株主資本 """


class ProvisionOfLegalRetainedEarnings(Enum):
    """"利益準備金の積立"""
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__LEGAL_RETAINED_EARNINGS_MEMBER = 'InterimDuration_NonConsolidatedMember_LegalRetainedEarningsMember'
    """ 個別又は非連結利益準備金 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_BROUGHT_FORWARD_MEMBER = 'InterimDuration_NonConsolidatedMember_RetainedEarningsBroughtForwardMember'
    """ 個別又は非連結繰越利益剰余金 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_MEMBER = 'InterimDuration_NonConsolidatedMember_RetainedEarningsMember'
    """ 個別又は非連結利益剰余金 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__SHAREHOLDERS_EQUITY_MEMBER = 'InterimDuration_NonConsolidatedMember_ShareholdersEquityMember'
    """ 個別又は非連結株主資本 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__LEGAL_RETAINED_EARNINGS_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_LegalRetainedEarningsMember'
    """ 個別又は非連結利益準備金 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_BROUGHT_FORWARD_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_RetainedEarningsBroughtForwardMember'
    """ 個別又は非連結繰越利益剰余金 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_RetainedEarningsMember'
    """ 個別又は非連結利益剰余金 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_ShareholdersEquityMember'
    """ 個別又は非連結株主資本 """


class ProvisionOfOutstandingClaimsOEINS(Enum):
    """"支払備金繰入額、経常費用、保険業"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProvisionOfPolicyReserveOEINS(Enum):
    """"責任準備金繰入額、経常費用、保険業"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProvisionOfReserveForAdvancedDepreciationOfNoncurrentAssets(Enum):
    """"固定資産圧縮積立金の積立"""
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RESERVE_FOR_ADVANCED_DEPRECIATION_OF_NONCURRENT_ASSETS_MEMBER = 'InterimDuration_NonConsolidatedMember_ReserveForAdvancedDepreciationOfNoncurrentAssetsMember'
    """ 個別又は非連結固定資産圧縮積立金 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_BROUGHT_FORWARD_MEMBER = 'InterimDuration_NonConsolidatedMember_RetainedEarningsBroughtForwardMember'
    """ 個別又は非連結繰越利益剰余金 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_MEMBER = 'InterimDuration_NonConsolidatedMember_RetainedEarningsMember'
    """ 個別又は非連結利益剰余金 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__SHAREHOLDERS_EQUITY_MEMBER = 'InterimDuration_NonConsolidatedMember_ShareholdersEquityMember'
    """ 個別又は非連結株主資本 """


class ProvisionOfReserveForDividends3(Enum):
    """"配当準備積立金の積立"""
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_RetainedEarningsMember'
    """ 当年度会計期間個別又は非連結利益剰余金 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__SHAREHOLDERS_EQUITY_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_ShareholdersEquityMember'
    """ 当年度会計期間個別又は非連結株主資本 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RESERVE_FOR_DIVIDENDS3_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_ReserveForDividends3Member'
    """ 個別又は非連結配当準備積立金 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_BROUGHT_FORWARD_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_RetainedEarningsBroughtForwardMember'
    """ 個別又は非連結繰越利益剰余金 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_RetainedEarningsMember'
    """ 個別又は非連結利益剰余金 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_ShareholdersEquityMember'
    """ 個別又は非連結株主資本 """


class ProvisionOfReserveForPriceFluctuationELINS(Enum):
    """"価格変動準備金繰入額、特別損失、保険業"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProvisionOfReservesUnderTheSpecialLawsEL(Enum):
    """"特別法上の準備金繰入額、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PurchaseDiscountsNOI(Enum):
    """"仕入割引、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class PurchaseOfAssetsForRentOpeCF(Enum):
    """"賃貸資産の取得による支出、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class PurchaseOfInsuranceFundsInvCF(Enum):
    """"保険積立金の積立による支出、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class PurchaseOfIntangibleAssetsInvCF(Enum):
    """"無形固定資産の取得による支出、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class PurchaseOfInvestmentSecuritiesInvCF(Enum):
    """"投資有価証券の取得による支出、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class PurchaseOfInvestmentsInCapitalOfSubsidiariesInvCF(Enum):
    """"子会社出資金の取得による支出、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PurchaseOfInvestmentsInSubsidiariesInvCF(Enum):
    """"子会社株式の取得による支出、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class PurchaseOfInvestmentsInSubsidiariesResultingInChangeInScopeOfConsolidationInvCF(Enum):
    """"連結の範囲の変更を伴う子会社株式の取得による支出、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class PurchaseOfLongTermPrepaidExpensesInvCF(Enum):
    """"長期前払費用の取得による支出、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class PurchaseOfNoncurrentAssetsInvCF(Enum):
    """"固定資産の取得による支出、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class PurchaseOfPropertyPlantAndEquipmentAndIntangibleAssetsInvCF(Enum):
    """"有形及び無形固定資産の取得による支出、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class PurchaseOfPropertyPlantAndEquipmentInvCF(Enum):
    """"有形固定資産の取得による支出、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class PurchaseOfSecuritiesInvCFBNK(Enum):
    """"有価証券の取得による支出、投資活動によるキャッシュ・フロー、銀行業"""
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'


class PurchaseOfSharesOfConsolidatedSubsidiaries(Enum):
    """"連結子会社株式の取得による持分の増減"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__CAPITAL_SURPLUS_MEMBER = 'CurrentYearDuration_CapitalSurplusMember'
    """ 当年度会計期間資本剰余金 """
    CURRENT_YEAR_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'CurrentYearDuration_ShareholdersEquityMember'
    """ 当年度会計期間株主資本 """
    INTERIM_DURATION = 'InterimDuration'
    INTERIM_DURATION__CAPITAL_SURPLUS_MEMBER = 'InterimDuration_CapitalSurplusMember'
    """ 資本剰余金 """
    INTERIM_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'InterimDuration_ShareholdersEquityMember'
    """ 株主資本 """
    INTERIM_DURATION__TREASURY_STOCK_MEMBER = 'InterimDuration_TreasuryStockMember'
    """ 自己株式 """
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_INTERIM_DURATION__CAPITAL_SURPLUS_MEMBER = 'Prior1InterimDuration_CapitalSurplusMember'
    """ 資本剰余金 """
    PRIOR1_INTERIM_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1InterimDuration_ShareholdersEquityMember'
    """ 株主資本 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__CAPITAL_SURPLUS_MEMBER = 'Prior1YearDuration_CapitalSurplusMember'
    """ 資本剰余金 """
    PRIOR1_YEAR_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1YearDuration_ShareholdersEquityMember'
    """ 株主資本 """


class PurchaseOfShortTermAndLongTermInvestmentSecuritiesInvCF(Enum):
    """"有価証券及び投資有価証券の取得による支出、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class PurchaseOfShortTermInvestmentSecuritiesInvCF(Enum):
    """"有価証券の取得による支出、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class PurchaseOfSoftwareInvCF(Enum):
    """"ソフトウエアの取得による支出、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PurchaseOfStocksOfSubsidiariesAndAffiliatesInvCF(Enum):
    """"関係会社株式の取得による支出、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class PurchaseOfTreasuryStock(Enum):
    """"自己株式の取得"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__CAPITAL_STOCK_MEMBER = 'CurrentYearDuration_CapitalStockMember'
    """ 当年度会計期間資本金 """
    CURRENT_YEAR_DURATION__CAPITAL_SURPLUS_MEMBER = 'CurrentYearDuration_CapitalSurplusMember'
    """ 当年度会計期間資本剰余金 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CAPITAL_STOCK_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_CapitalStockMember'
    """ 当年度会計期間個別又は非連結資本金 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CAPITAL_SURPLUS_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_CapitalSurplusMember'
    """ 当年度会計期間個別又は非連結資本剰余金 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__LEGAL_CAPITAL_SURPLUS_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_LegalCapitalSurplusMember'
    """ 当年度会計期間個別又は非連結資本準備金 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_BROUGHT_FORWARD_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_RetainedEarningsBroughtForwardMember'
    """ 当年度会計期間個別又は非連結繰越利益剰余金 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_RetainedEarningsMember'
    """ 当年度会計期間個別又は非連結利益剰余金 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__SHAREHOLDERS_EQUITY_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_ShareholdersEquityMember'
    """ 当年度会計期間個別又は非連結株主資本 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__SUBSCRIPTION_RIGHTS_TO_SHARES_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_SubscriptionRightsToSharesMember'
    """ 当年度会計期間個別又は非連結新株予約権 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__TREASURY_STOCK_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_TreasuryStockMember'
    """ 当年度会計期間個別又は非連結自己株式 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__VALUATION_AND_TRANSLATION_ADJUSTMENTS_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_ValuationAndTranslationAdjustmentsMember'
    """ 当年度会計期間個別又は非連結評価・換算差額等 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__VALUATION_DIFFERENCE_ON_AVAILABLE_FOR_SALE_SECURITIES_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_ValuationDifferenceOnAvailableForSaleSecuritiesMember'
    """ 当年度会計期間個別又は非連結その他有価証券評価差額金 """
    CURRENT_YEAR_DURATION__NON_CONTROLLING_INTERESTS_MEMBER = 'CurrentYearDuration_NonControllingInterestsMember'
    """ 当年度会計期間非支配株主持分 """
    CURRENT_YEAR_DURATION__RETAINED_EARNINGS_MEMBER = 'CurrentYearDuration_RetainedEarningsMember'
    """ 当年度会計期間利益剰余金 """
    CURRENT_YEAR_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'CurrentYearDuration_ShareholdersEquityMember'
    """ 当年度会計期間株主資本 """
    CURRENT_YEAR_DURATION__SUBSCRIPTION_RIGHTS_TO_SHARES_MEMBER = 'CurrentYearDuration_SubscriptionRightsToSharesMember'
    """ 当年度会計期間新株予約権 """
    CURRENT_YEAR_DURATION__TREASURY_STOCK_MEMBER = 'CurrentYearDuration_TreasuryStockMember'
    """ 当年度会計期間自己株式 """
    CURRENT_YEAR_DURATION__VALUATION_AND_TRANSLATION_ADJUSTMENTS_MEMBER = 'CurrentYearDuration_ValuationAndTranslationAdjustmentsMember'
    """ 当年度会計期間評価・換算差額等 """
    INTERIM_DURATION = 'InterimDuration'
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__SHAREHOLDERS_EQUITY_MEMBER = 'InterimDuration_NonConsolidatedMember_ShareholdersEquityMember'
    """ 個別又は非連結株主資本 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__TREASURY_STOCK_MEMBER = 'InterimDuration_NonConsolidatedMember_TreasuryStockMember'
    """ 個別又は非連結自己株式 """
    INTERIM_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'InterimDuration_ShareholdersEquityMember'
    """ 株主資本 """
    INTERIM_DURATION__TREASURY_STOCK_MEMBER = 'InterimDuration_TreasuryStockMember'
    """ 自己株式 """
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_ShareholdersEquityMember'
    """ 個別又は非連結株主資本 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__TREASURY_STOCK_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_TreasuryStockMember'
    """ 個別又は非連結自己株式 """
    PRIOR1_INTERIM_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1InterimDuration_ShareholdersEquityMember'
    """ 株主資本 """
    PRIOR1_INTERIM_DURATION__TREASURY_STOCK_MEMBER = 'Prior1InterimDuration_TreasuryStockMember'
    """ 自己株式 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__CAPITAL_STOCK_MEMBER = 'Prior1YearDuration_CapitalStockMember'
    """ 資本金 """
    PRIOR1_YEAR_DURATION__CAPITAL_SURPLUS_MEMBER = 'Prior1YearDuration_CapitalSurplusMember'
    """ 資本剰余金 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CAPITAL_STOCK_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_CapitalStockMember'
    """ 個別又は非連結資本金 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CAPITAL_SURPLUS_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_CapitalSurplusMember'
    """ 個別又は非連結資本剰余金 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__LEGAL_CAPITAL_SURPLUS_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_LegalCapitalSurplusMember'
    """ 個別又は非連結資本準備金 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_BROUGHT_FORWARD_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_RetainedEarningsBroughtForwardMember'
    """ 個別又は非連結繰越利益剰余金 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_RetainedEarningsMember'
    """ 個別又は非連結利益剰余金 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_ShareholdersEquityMember'
    """ 個別又は非連結株主資本 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__SUBSCRIPTION_RIGHTS_TO_SHARES_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_SubscriptionRightsToSharesMember'
    """ 個別又は非連結新株予約権 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__TREASURY_STOCK_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_TreasuryStockMember'
    """ 個別又は非連結自己株式 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__VALUATION_AND_TRANSLATION_ADJUSTMENTS_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_ValuationAndTranslationAdjustmentsMember'
    """ 個別又は非連結評価・換算差額等 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__VALUATION_DIFFERENCE_ON_AVAILABLE_FOR_SALE_SECURITIES_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_ValuationDifferenceOnAvailableForSaleSecuritiesMember'
    """ 個別又は非連結その他有価証券評価差額金 """
    PRIOR1_YEAR_DURATION__NON_CONTROLLING_INTERESTS_MEMBER = 'Prior1YearDuration_NonControllingInterestsMember'
    """ 非支配株主持分 """
    PRIOR1_YEAR_DURATION__RETAINED_EARNINGS_MEMBER = 'Prior1YearDuration_RetainedEarningsMember'
    """ 利益剰余金 """
    PRIOR1_YEAR_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1YearDuration_ShareholdersEquityMember'
    """ 株主資本 """
    PRIOR1_YEAR_DURATION__SUBSCRIPTION_RIGHTS_TO_SHARES_MEMBER = 'Prior1YearDuration_SubscriptionRightsToSharesMember'
    """ 新株予約権 """
    PRIOR1_YEAR_DURATION__TREASURY_STOCK_MEMBER = 'Prior1YearDuration_TreasuryStockMember'
    """ 自己株式 """
    PRIOR1_YEAR_DURATION__VALUATION_AND_TRANSLATION_ADJUSTMENTS_MEMBER = 'Prior1YearDuration_ValuationAndTranslationAdjustmentsMember'
    """ 評価・換算差額等 """


class PurchaseOfTreasuryStockFinCF(Enum):
    """"自己株式の取得による支出、財務活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class PurchaseOfTreasuryStockOfSubsidiariesInConsolidationFinCF(Enum):
    """"子会社の自己株式の取得による支出、財務活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class PurchaseOfTrustBeneficiaryRightInvCF(Enum):
    """"信託受益権の取得による支出、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PurchasedReceivablesCA(Enum):
    """"買取債権、流動資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class RawMaterials(Enum):
    """"原材料"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class RawMaterialsAndSupplies(Enum):
    """"原材料及び貯蔵品"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class RawMaterialsAndSuppliesCNS(Enum):
    """"材料貯蔵品、建設業"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class RealEstateForInvestment(Enum):
    """"投資不動産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class RealEstateForInvestmentNet(Enum):
    """"投資不動産（純額）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class RealEstateForRentNet(Enum):
    """"賃貸不動産（純額）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class RealEstateForSale(Enum):
    """"販売用不動産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class RealEstateForSaleCNS(Enum):
    """"販売用不動産、建設業"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class RealEstateForSaleInProcess(Enum):
    """"仕掛販売用不動産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class RealEstateIncomeRevOA(Enum):
    """"不動産収入、営業活動による収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class RealEstateRentNOI(Enum):
    """"不動産賃貸料、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class RedemptionOfBondsFinCF(Enum):
    """"社債の償還による支出、財務活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class RedemptionOfCommercialPapersFinCF(Enum):
    """"コマーシャル・ペーパーの償還による支出、財務活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ReductionEntryOfLandContributionForConstructionEL(Enum):
    """"工事負担金等圧縮額、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class RefundOfIncomeTaxesIncomeTaxes(Enum):
    """"法人税等還付税額、法人税等"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class RefundedConsumptionTaxesNOI(Enum):
    """"還付消費税等、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ReinsuranceAccountsReceivableAssetsINS(Enum):
    """"再保険貸、資産の部、保険業"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class RelocationExpensesOpeCF(Enum):
    """"移転費用、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class RemeasurementsOfDefinedBenefitPlans(Enum):
    """"退職給付に係る調整累計額"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    INTERIM_INSTANT = 'InterimInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class RemeasurementsOfDefinedBenefitPlansBeforeTaxOCI(Enum):
    """"退職給付に係る調整額（税引前）、その他の包括利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class RemeasurementsOfDefinedBenefitPlansNetOfTaxOCI(Enum):
    """"退職給付に係る調整額（税引後）、その他の包括利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class RentCostCOSExpOA(Enum):
    """"賃貸原価、営業活動による費用・売上原価"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class RentCostOfRealEstateNOE(Enum):
    """"不動産賃貸原価、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class RentExpensesNOE(Enum):
    """"賃貸費用、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class RentExpensesOnFacilitiesNOE(Enum):
    """"設備賃貸費用、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class RentExpensesOnNoncurrentAssetsNOE(Enum):
    """"固定資産賃貸費用、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class RentExpensesOnRealEstatesNOE(Enum):
    """"不動産賃貸費用、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class RentExpensesOnRealEstatesSGA(Enum):
    """"不動産賃借料、販売費及び一般管理費"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class RentExpensesSGA(Enum):
    """"賃借料、販売費及び一般管理費"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class RentIncomeNOI(Enum):
    """"受取賃貸料、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class RentIncomeOnFacilitiesNOI(Enum):
    """"設備賃貸料、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class RentIncomeOnNoncurrentAssetsNOI(Enum):
    """"固定資産賃貸料、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class RentIncomeOpeCF(Enum):
    """"受取賃貸料、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class RentIncomeRevOA(Enum):
    """"賃貸収入、営業活動による収益"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class RentOfRealEstateForInvestmentNOI(Enum):
    """"投資不動産賃貸料、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class RentsSGA(Enum):
    """"地代家賃、販売費及び一般管理費"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class RepairAndMaintenanceSGA(Enum):
    """"修繕維持費、販売費及び一般管理費"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class RepairExpensesSGA(Enum):
    """"修繕費、販売費及び一般管理費"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class RepaymentOfLongTermLoansPayableFinCF(Enum):
    """"長期借入金の返済による支出、財務活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class RepaymentsOfFinanceLeaseObligationsFinCF(Enum):
    """"ファイナンス・リース債務の返済による支出、財務活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class RepaymentsOfGuaranteeDepositsReceivedInvCF(Enum):
    """"預り保証金の返還による支出、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class RepaymentsOfInstallmentPayablesFinCF(Enum):
    """"割賦債務の返済による支出、財務活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class RepaymentsOfLeaseObligationsFinCF(Enum):
    """"リース債務の返済による支出、財務活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class RepaymentsToNonControllingShareholdersFinCF(Enum):
    """"非支配株主への払戻による支出、財務活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ResearchAndDevelopmentExpensesSGA(Enum):
    """"研究開発費、販売費及び一般管理費"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class ResearchStudyExpensesSGA(Enum):
    """"調査研究費、販売費及び一般管理費"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class ReserveForAdvancedDepreciationOfNoncurrentAssets(Enum):
    """"固定資産圧縮積立金"""
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class ReserveForCommoditiesTransactionLiabilitiesReservesUnderTheSpecialLawsCMD(Enum):
    """"商品取引責任準備金、特別法上の準備金、商品先物取引業"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ReserveForContractOfInsurance(Enum):
    """"保険契約準備金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ReserveForDividends3(Enum):
    """"配当準備積立金"""
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class ReserveForFinancialProductsTransactionLiabilitiesReservesUnderTheSpecialLawsSEC(Enum):
    """"金融商品取引責任準備金、特別法上の準備金、第一種金融商品取引業"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ReserveForInsurancePolicyLiabilitiesLiabilitiesINS(Enum):
    """"保険契約準備金、負債の部、保険業"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ReserveForPriceFluctuationLiabilitiesINS(Enum):
    """"価格変動準備金、負債の部、保険業"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ReserveForReductionEntry2(Enum):
    """"圧縮積立金"""
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class ReserveForReductionEntryOfRealEstate(Enum):
    """"不動産圧縮積立金"""
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class ReserveForSpecialAccountForAdvancedDepreciationOfNoncurrentAssets(Enum):
    """"固定資産圧縮特別勘定積立金"""
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class ReservesUnderTheSpecialLaws1(Enum):
    """"特別法上の準備金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ReservesUnderTheSpecialLaws2(Enum):
    """"特別法上の引当金"""
    INTERIM_INSTANT = 'InterimInstant'
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class RestOfTheOtherAssetsAssetsINS(Enum):
    """"その他の資産、資産の部、保険業"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class RestatedBalance(Enum):
    """"会計方針の変更を反映した当期首残高"""
    PRIOR2_YEAR_INSTANT = 'Prior2YearInstant'
    PRIOR2_YEAR_INSTANT__CAPITAL_STOCK_MEMBER = 'Prior2YearInstant_CapitalStockMember'
    """ 資本金 """
    PRIOR2_YEAR_INSTANT__CAPITAL_SURPLUS_MEMBER = 'Prior2YearInstant_CapitalSurplusMember'
    """ 資本剰余金 """
    PRIOR2_YEAR_INSTANT__DEFERRED_GAINS_OR_LOSSES_ON_HEDGES_MEMBER = 'Prior2YearInstant_DeferredGainsOrLossesOnHedgesMember'
    """ 繰延ヘッジ損益 """
    PRIOR2_YEAR_INSTANT__REMEASUREMENTS_OF_DEFINED_BENEFIT_PLANS_MEMBER = 'Prior2YearInstant_RemeasurementsOfDefinedBenefitPlansMember'
    """ 退職給付に係る調整累計額 """
    PRIOR2_YEAR_INSTANT__RETAINED_EARNINGS_MEMBER = 'Prior2YearInstant_RetainedEarningsMember'
    """ 利益剰余金 """
    PRIOR2_YEAR_INSTANT__SHAREHOLDERS_EQUITY_MEMBER = 'Prior2YearInstant_ShareholdersEquityMember'
    """ 株主資本 """
    PRIOR2_YEAR_INSTANT__SUBSCRIPTION_RIGHTS_TO_SHARES_MEMBER = 'Prior2YearInstant_SubscriptionRightsToSharesMember'
    """ 新株予約権 """
    PRIOR2_YEAR_INSTANT__TREASURY_STOCK_MEMBER = 'Prior2YearInstant_TreasuryStockMember'
    """ 自己株式 """
    PRIOR2_YEAR_INSTANT__VALUATION_AND_TRANSLATION_ADJUSTMENTS_MEMBER = 'Prior2YearInstant_ValuationAndTranslationAdjustmentsMember'
    """ 評価・換算差額等 """
    PRIOR2_YEAR_INSTANT__VALUATION_DIFFERENCE_ON_AVAILABLE_FOR_SALE_SECURITIES_MEMBER = 'Prior2YearInstant_ValuationDifferenceOnAvailableForSaleSecuritiesMember'
    """ その他有価証券評価差額金 """


class RestructuringLossEL(Enum):
    """"事業再編損、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class RetainedEarnings(Enum):
    """"利益剰余金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    INTERIM_INSTANT = 'InterimInstant'
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class RetainedEarningsBroughtForward(Enum):
    """"繰越利益剰余金"""
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class RetirementBenefitExpensesEL(Enum):
    """"退職給付費用、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class RetirementBenefitExpensesSGA(Enum):
    """"退職給付費用、販売費及び一般管理費"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class RetirementOfTreasuryStock(Enum):
    """"自己株式の消却"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_RetainedEarningsMember'
    """ 当年度会計期間個別又は非連結利益剰余金 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__SHAREHOLDERS_EQUITY_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_ShareholdersEquityMember'
    """ 当年度会計期間個別又は非連結株主資本 """
    CURRENT_YEAR_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'CurrentYearDuration_ShareholdersEquityMember'
    """ 当年度会計期間株主資本 """
    INTERIM_DURATION = 'InterimDuration'
    INTERIM_DURATION__CAPITAL_SURPLUS_MEMBER = 'InterimDuration_CapitalSurplusMember'
    """ 資本剰余金 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__CAPITAL_SURPLUS_MEMBER = 'InterimDuration_NonConsolidatedMember_CapitalSurplusMember'
    """ 個別又は非連結資本剰余金 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__OTHER_CAPITAL_SURPLUS_MEMBER = 'InterimDuration_NonConsolidatedMember_OtherCapitalSurplusMember'
    """ 個別又は非連結その他資本剰余金 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__SHAREHOLDERS_EQUITY_MEMBER = 'InterimDuration_NonConsolidatedMember_ShareholdersEquityMember'
    """ 個別又は非連結株主資本 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__TREASURY_STOCK_MEMBER = 'InterimDuration_NonConsolidatedMember_TreasuryStockMember'
    """ 個別又は非連結自己株式 """
    INTERIM_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'InterimDuration_ShareholdersEquityMember'
    """ 株主資本 """
    INTERIM_DURATION__TREASURY_STOCK_MEMBER = 'InterimDuration_TreasuryStockMember'
    """ 自己株式 """
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_INTERIM_DURATION__CAPITAL_SURPLUS_MEMBER = 'Prior1InterimDuration_CapitalSurplusMember'
    """ 資本剰余金 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__CAPITAL_SURPLUS_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_CapitalSurplusMember'
    """ 個別又は非連結資本剰余金 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__OTHER_CAPITAL_SURPLUS_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_OtherCapitalSurplusMember'
    """ 個別又は非連結その他資本剰余金 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_BROUGHT_FORWARD_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_RetainedEarningsBroughtForwardMember'
    """ 個別又は非連結繰越利益剰余金 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_RetainedEarningsMember'
    """ 個別又は非連結利益剰余金 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_ShareholdersEquityMember'
    """ 個別又は非連結株主資本 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__TREASURY_STOCK_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_TreasuryStockMember'
    """ 個別又は非連結自己株式 """
    PRIOR1_INTERIM_DURATION__RETAINED_EARNINGS_MEMBER = 'Prior1InterimDuration_RetainedEarningsMember'
    """ 利益剰余金 """
    PRIOR1_INTERIM_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1InterimDuration_ShareholdersEquityMember'
    """ 株主資本 """
    PRIOR1_INTERIM_DURATION__TREASURY_STOCK_MEMBER = 'Prior1InterimDuration_TreasuryStockMember'
    """ 自己株式 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__CAPITAL_SURPLUS_MEMBER = 'Prior1YearDuration_CapitalSurplusMember'
    """ 資本剰余金 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_BROUGHT_FORWARD_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_RetainedEarningsBroughtForwardMember'
    """ 個別又は非連結繰越利益剰余金 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_RetainedEarningsMember'
    """ 個別又は非連結利益剰余金 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_ShareholdersEquityMember'
    """ 個別又は非連結株主資本 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__TREASURY_STOCK_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_TreasuryStockMember'
    """ 個別又は非連結自己株式 """
    PRIOR1_YEAR_DURATION__RETAINED_EARNINGS_MEMBER = 'Prior1YearDuration_RetainedEarningsMember'
    """ 利益剰余金 """
    PRIOR1_YEAR_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1YearDuration_ShareholdersEquityMember'
    """ 株主資本 """
    PRIOR1_YEAR_DURATION__TREASURY_STOCK_MEMBER = 'Prior1YearDuration_TreasuryStockMember'
    """ 自己株式 """


class RetirementPaymentsSGA(Enum):
    """"退職金、販売費及び一般管理費"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class RevaluationReserveForLand(Enum):
    """"土地再評価差額金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    INTERIM_INSTANT = 'InterimInstant'
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class RevaluationReserveForLandNetOfTaxOCI(Enum):
    """"土地再評価差額金（税引後）、その他の包括利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class Revenue(Enum):
    """"売上収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'CurrentYTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    CURRENT_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'CurrentYTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1YTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1YTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """


class RevenueFromContractsWithCustomers(Enum):
    """"顧客との契約から生じる収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER__OTHER_REPORTABLE_SEGMENTS_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember_OtherReportableSegmentsMember'
    """ 個別又は非連結その他 """
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER__RECONCILING_ITEMS_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember_ReconcilingItemsMember'
    """ 個別又は非連結調整項目 """
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER__REPORTABLE_SEGMENTS_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember_ReportableSegmentsMember'
    """ 個別又は非連結報告セグメント """
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember_TotalOfReportableSegmentsAndOthersMember'
    """ 個別又は非連結事業セグメント合計 """
    CURRENT_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'CurrentYTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    CURRENT_YTD_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'CurrentYTDDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    CURRENT_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'CurrentYTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER__RECONCILING_ITEMS_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember_ReconcilingItemsMember'
    """ 個別又は非連結調整項目 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER__REPORTABLE_SEGMENTS_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember_ReportableSegmentsMember'
    """ 個別又は非連結報告セグメント """
    PRIOR1_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1YTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_YTD_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'Prior1YTDDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    PRIOR1_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1YTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """


class RevenueFromCreditGuaranteeRevOA(Enum):
    """"信用保証収益、営業活動による収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class RevenueOtherThanThatFromContractsWithCustomers(Enum):
    """"顧客との契約から生じる収益以外の収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER__OTHER_REPORTABLE_SEGMENTS_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember_OtherReportableSegmentsMember'
    """ 個別又は非連結その他 """
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER__RECONCILING_ITEMS_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember_ReconcilingItemsMember'
    """ 個別又は非連結調整項目 """
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER__REPORTABLE_SEGMENTS_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember_ReportableSegmentsMember'
    """ 個別又は非連結報告セグメント """
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember_TotalOfReportableSegmentsAndOthersMember'
    """ 個別又は非連結事業セグメント合計 """
    CURRENT_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'CurrentYTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    CURRENT_YTD_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'CurrentYTDDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    CURRENT_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'CurrentYTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER__RECONCILING_ITEMS_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember_ReconcilingItemsMember'
    """ 個別又は非連結調整項目 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER__REPORTABLE_SEGMENTS_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember_ReportableSegmentsMember'
    """ 個別又は非連結報告セグメント """
    PRIOR1_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1YTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_YTD_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'Prior1YTDDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    PRIOR1_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1YTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """


class ReversalOfAllowanceForDoubtfulAccountsEI(Enum):
    """"貸倒引当金戻入額、特別利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class ReversalOfAllowanceForDoubtfulAccountsNOI(Enum):
    """"貸倒引当金戻入額、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class ReversalOfPolicyReserveINS(Enum):
    """"責任準備金戻入額、保険業"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ReversalOfProvisionForBusinessStructureImprovementEI(Enum):
    """"事業構造改善引当金戻入額、特別利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ReversalOfProvisionForDirectorsRetirementBenefitsEI(Enum):
    """"役員退職慰労引当金戻入額、特別利益"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class ReversalOfProvisionForLossOnLiquidationOfSubsidiariesAndAffiliatesEI(Enum):
    """"関係会社整理損失引当金戻入額、特別利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ReversalOfProvisionForLossOnStoreClosingEI(Enum):
    """"店舗閉鎖損失引当金戻入額、特別利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ReversalOfReserveForAdvancedDepreciationOfNoncurrentAssets(Enum):
    """"固定資産圧縮積立金の取崩"""
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RESERVE_FOR_ADVANCED_DEPRECIATION_OF_NONCURRENT_ASSETS_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_ReserveForAdvancedDepreciationOfNoncurrentAssetsMember'
    """ 当年度会計期間個別又は非連結固定資産圧縮積立金 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_BROUGHT_FORWARD_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_RetainedEarningsBroughtForwardMember'
    """ 当年度会計期間個別又は非連結繰越利益剰余金 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_RetainedEarningsMember'
    """ 当年度会計期間個別又は非連結利益剰余金 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__SHAREHOLDERS_EQUITY_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_ShareholdersEquityMember'
    """ 当年度会計期間個別又は非連結株主資本 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RESERVE_FOR_ADVANCED_DEPRECIATION_OF_NONCURRENT_ASSETS_MEMBER = 'InterimDuration_NonConsolidatedMember_ReserveForAdvancedDepreciationOfNoncurrentAssetsMember'
    """ 個別又は非連結固定資産圧縮積立金 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_BROUGHT_FORWARD_MEMBER = 'InterimDuration_NonConsolidatedMember_RetainedEarningsBroughtForwardMember'
    """ 個別又は非連結繰越利益剰余金 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_MEMBER = 'InterimDuration_NonConsolidatedMember_RetainedEarningsMember'
    """ 個別又は非連結利益剰余金 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__SHAREHOLDERS_EQUITY_MEMBER = 'InterimDuration_NonConsolidatedMember_ShareholdersEquityMember'
    """ 個別又は非連結株主資本 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RESERVE_FOR_ADVANCED_DEPRECIATION_OF_NONCURRENT_ASSETS_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_ReserveForAdvancedDepreciationOfNoncurrentAssetsMember'
    """ 個別又は非連結固定資産圧縮積立金 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_BROUGHT_FORWARD_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_RetainedEarningsBroughtForwardMember'
    """ 個別又は非連結繰越利益剰余金 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_RetainedEarningsMember'
    """ 個別又は非連結利益剰余金 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_ShareholdersEquityMember'
    """ 個別又は非連結株主資本 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RESERVE_FOR_ADVANCED_DEPRECIATION_OF_NONCURRENT_ASSETS_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_ReserveForAdvancedDepreciationOfNoncurrentAssetsMember'
    """ 個別又は非連結固定資産圧縮積立金 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_BROUGHT_FORWARD_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_RetainedEarningsBroughtForwardMember'
    """ 個別又は非連結繰越利益剰余金 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_RetainedEarningsMember'
    """ 個別又は非連結利益剰余金 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_ShareholdersEquityMember'
    """ 個別又は非連結株主資本 """


class ReversalOfReserveForReductionEntry2(Enum):
    """"圧縮積立金の取崩"""
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RESERVE_FOR_REDUCTION_ENTRY2_MEMBER = 'InterimDuration_NonConsolidatedMember_ReserveForReductionEntry2Member'
    """ 個別又は非連結圧縮積立金 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_BROUGHT_FORWARD_MEMBER = 'InterimDuration_NonConsolidatedMember_RetainedEarningsBroughtForwardMember'
    """ 個別又は非連結繰越利益剰余金 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_MEMBER = 'InterimDuration_NonConsolidatedMember_RetainedEarningsMember'
    """ 個別又は非連結利益剰余金 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__SHAREHOLDERS_EQUITY_MEMBER = 'InterimDuration_NonConsolidatedMember_ShareholdersEquityMember'
    """ 個別又は非連結株主資本 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RESERVE_FOR_REDUCTION_ENTRY2_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_ReserveForReductionEntry2Member'
    """ 個別又は非連結圧縮積立金 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_BROUGHT_FORWARD_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_RetainedEarningsBroughtForwardMember'
    """ 個別又は非連結繰越利益剰余金 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_RetainedEarningsMember'
    """ 個別又は非連結利益剰余金 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_ShareholdersEquityMember'
    """ 個別又は非連結株主資本 """


class ReversalOfReserveForReductionEntryOfRealEstate(Enum):
    """"不動産圧縮積立金の取崩"""
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RESERVE_FOR_REDUCTION_ENTRY_OF_REAL_ESTATE_MEMBER = 'InterimDuration_NonConsolidatedMember_ReserveForReductionEntryOfRealEstateMember'
    """ 個別又は非連結不動産圧縮積立金 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_BROUGHT_FORWARD_MEMBER = 'InterimDuration_NonConsolidatedMember_RetainedEarningsBroughtForwardMember'
    """ 個別又は非連結繰越利益剰余金 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_MEMBER = 'InterimDuration_NonConsolidatedMember_RetainedEarningsMember'
    """ 個別又は非連結利益剰余金 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__SHAREHOLDERS_EQUITY_MEMBER = 'InterimDuration_NonConsolidatedMember_ShareholdersEquityMember'
    """ 個別又は非連結株主資本 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RESERVE_FOR_REDUCTION_ENTRY_OF_REAL_ESTATE_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_ReserveForReductionEntryOfRealEstateMember'
    """ 個別又は非連結不動産圧縮積立金 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_BROUGHT_FORWARD_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_RetainedEarningsBroughtForwardMember'
    """ 個別又は非連結繰越利益剰余金 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_RetainedEarningsMember'
    """ 個別又は非連結利益剰余金 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_ShareholdersEquityMember'
    """ 個別又は非連結株主資本 """


class ReversalOfReserveForSpecialDepreciation(Enum):
    """"特別償却準備金の取崩"""
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RESERVE_FOR_SPECIAL_DEPRECIATION_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_ReserveForSpecialDepreciationMember'
    """ 当年度会計期間個別又は非連結特別償却準備金 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_BROUGHT_FORWARD_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_RetainedEarningsBroughtForwardMember'
    """ 当年度会計期間個別又は非連結繰越利益剰余金 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_RetainedEarningsMember'
    """ 当年度会計期間個別又は非連結利益剰余金 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__SHAREHOLDERS_EQUITY_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_ShareholdersEquityMember'
    """ 当年度会計期間個別又は非連結株主資本 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RESERVE_FOR_SPECIAL_DEPRECIATION_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_ReserveForSpecialDepreciationMember'
    """ 個別又は非連結特別償却準備金 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_BROUGHT_FORWARD_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_RetainedEarningsBroughtForwardMember'
    """ 個別又は非連結繰越利益剰余金 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_RetainedEarningsMember'
    """ 個別又は非連結利益剰余金 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_ShareholdersEquityMember'
    """ 個別又は非連結株主資本 """


class ReversalOfRevaluationReserveForLand(Enum):
    """"土地再評価差額金の取崩"""
    INTERIM_DURATION = 'InterimDuration'
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_BROUGHT_FORWARD_MEMBER = 'InterimDuration_NonConsolidatedMember_RetainedEarningsBroughtForwardMember'
    """ 個別又は非連結繰越利益剰余金 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_MEMBER = 'InterimDuration_NonConsolidatedMember_RetainedEarningsMember'
    """ 個別又は非連結利益剰余金 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__SHAREHOLDERS_EQUITY_MEMBER = 'InterimDuration_NonConsolidatedMember_ShareholdersEquityMember'
    """ 個別又は非連結株主資本 """
    INTERIM_DURATION__RETAINED_EARNINGS_MEMBER = 'InterimDuration_RetainedEarningsMember'
    """ 利益剰余金 """
    INTERIM_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'InterimDuration_ShareholdersEquityMember'
    """ 株主資本 """
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_BROUGHT_FORWARD_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_RetainedEarningsBroughtForwardMember'
    """ 個別又は非連結繰越利益剰余金 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_RetainedEarningsMember'
    """ 個別又は非連結利益剰余金 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_ShareholdersEquityMember'
    """ 個別又は非連結株主資本 """
    PRIOR1_INTERIM_DURATION__RETAINED_EARNINGS_MEMBER = 'Prior1InterimDuration_RetainedEarningsMember'
    """ 利益剰余金 """
    PRIOR1_INTERIM_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1InterimDuration_ShareholdersEquityMember'
    """ 株主資本 """


class ReversalOfSpecialReserveForExpansionOfRailwayTransportCapacityEIRWY(Enum):
    """"特定都市鉄道整備準備金取崩額、特別利益、鉄道事業"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class RightOfTrademark(Enum):
    """"商標権"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class RightOfUseAssets(Enum):
    """"使用権資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class RightOfUseAssetsNet(Enum):
    """"使用権資産（純額）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class RightOfUsingFacilitiesIA(Enum):
    """"施設利用権"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class RoyaltyIncomeNOI(Enum):
    """"受取ロイヤリティー、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class SalariesAllowancesAndBonusesSGA(Enum):
    """"給料手当及び賞与、販売費及び一般管理費"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class SalariesAndAllowancesSGA(Enum):
    """"給料及び手当、販売費及び一般管理費"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class SalariesAndBonusesSGA(Enum):
    """"給料及び賞与、販売費及び一般管理費"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class SalariesAndWagesSGA(Enum):
    """"給料及び賃金、販売費及び一般管理費"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class SalariesSGA(Enum):
    """"給料、販売費及び一般管理費"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class SalesAndAdministrativeExpensesOEINS(Enum):
    """"営業費及び一般管理費、経常費用、保険業"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class SalesCommissionSGA(Enum):
    """"販売手数料、販売費及び一般管理費"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class SalesDiscountsNOE(Enum):
    """"売上割引、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class SalesOnOtherBusinessRevOA(Enum):
    """"その他の事業売上高、営業活動による収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class SalesOnRealEstateBusinessRevOA(Enum):
    """"不動産事業売上高、営業活動による収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class SecuritiesAssetsBNK(Enum):
    """"有価証券、資産の部、銀行業"""
    INTERIM_INSTANT = 'InterimInstant'
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class SecuritiesAssetsINS(Enum):
    """"有価証券、資産の部、保険業"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class SellingExpensesSGA(Enum):
    """"販売費、販売費及び一般管理費"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class SellingGeneralAndAdministrativeExpenses(Enum):
    """"販売費及び一般管理費"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class SellingGeneralAndAdministrativeExpensesGAS(Enum):
    """"供給販売費及び一般管理費、ガス事業"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class SemiFinishedGoods(Enum):
    """"半製品"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ServiceAndMaintenanceFacilitiesPPEGAS(Enum):
    """"業務設備、有形固定資産、ガス事業"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class SettlementPackageEL(Enum):
    """"和解金、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class SettlementPackageNOE(Enum):
    """"和解金、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class SettlementPackageOpeCF(Enum):
    """"和解金、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class SettlementPackagePaidOpeCF(Enum):
    """"和解金の支払額、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class SettlementPackageReceivedOpeCF(Enum):
    """"和解金の受取額、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class SettlementReceivedEI(Enum):
    """"受取和解金、特別利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class SettlementReceivedOpeCF(Enum):
    """"受取和解金、営業活動によるキャッシュ・フロー"""
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class ShareAcquisitionRightsIssuanceCostsNOE(Enum):
    """"新株予約権発行費、営業外費用"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class ShareBasedCompensationExpensesOpeCF(Enum):
    """"株式報酬費用、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class ShareBasedCompensationExpensesSGA(Enum):
    """"株式報酬費用、販売費及び一般管理費"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class ShareOfOtherComprehensiveIncomeOfAssociatesAccountedForUsingEquityMethodOCI(Enum):
    """"持分法適用会社に対する持分相当額、その他の包括利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class ShareholdersEquity(Enum):
    """"株主資本"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    INTERIM_INSTANT = 'InterimInstant'
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class ShortTermBondsPayable(Enum):
    """"短期社債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ShortTermInvestmentSecurities(Enum):
    """"有価証券"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class ShortTermLoansPayable(Enum):
    """"短期借入金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class ShortTermLoansPayableToSubsidiariesAndAffiliates(Enum):
    """"関係会社短期借入金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ShortTermLoansReceivable(Enum):
    """"短期貸付金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class ShortTermLoansReceivableToSubsidiariesAndAffiliates(Enum):
    """"関係会社短期貸付金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class Software(Enum):
    """"ソフトウエア"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class SoftwareInProgress(Enum):
    """"ソフトウエア仮勘定"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class SpecialReserveForExpansionOfRailwayTransportCapacityRWY(Enum):
    """"特定都市鉄道整備準備金、鉄道事業"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class SpecialRetirementExpensesEL(Enum):
    """"特別退職金、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class StateSubsidyEI(Enum):
    """"国庫補助金、特別利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class StationeryExpensesSGA(Enum):
    """"事務用品費、販売費及び一般管理費"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class StevedoringIncomeRevOA(Enum):
    """"倉庫荷役料、営業活動による収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class StockIssuanceCostDA(Enum):
    """"株式交付費、繰延資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class StockIssuanceCostNOE(Enum):
    """"株式交付費、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class StockIssuanceCostOpeCF(Enum):
    """"株式交付費、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class StockIssuanceCostPriorNOE(Enum):
    """"新株発行費、営業外費用"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class StocksOfSubsidiariesAndAffiliates(Enum):
    """"関係会社株式"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class Structures(Enum):
    """"構築物"""
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class StructuresNet(Enum):
    """"構築物（純額）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class SubscriptionRightsToShares(Enum):
    """"新株予約権"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    INTERIM_INSTANT = 'InterimInstant'
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class SubsidiesForEmploymentAdjustmentNOI(Enum):
    """"雇用調整助成金、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class SubsidiesForEmploymentAdjustmentOpeCF(Enum):
    """"雇用調整助成金、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class SubsidiesReceivedInvCF(Enum):
    """"補助金の受取額、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class SubsidyEI(Enum):
    """"補助金収入、特別利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class SubsidyEIRWY(Enum):
    """"補助金、特別利益、鉄道事業"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class SubsidyIncome2EI(Enum):
    """"助成金収入、特別利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class SubsidyIncome2OpeCF(Enum):
    """"助成金収入、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class SubsidyIncomeNOI(Enum):
    """"補助金収入、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class SubsidyIncomeNOIBounty(Enum):
    """"助成金収入、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class SubsidyIncomeOpeCF(Enum):
    """"補助金収入、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class SubtotalOpeCF(Enum):
    """"小計、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class Supplies(Enum):
    """"貯蔵品"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class SuppliesExpensesSGA(Enum):
    """"消耗品費、販売費及び一般管理費"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class SurrenderValueOfInsuranceEI(Enum):
    """"保険解約返戻金、特別利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class SurrenderValueOfInsuranceOpeCF(Enum):
    """"保険解約返戻金、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class SuspensePaymentsAssetsINS(Enum):
    """"仮払金、資産の部、保険業"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class TaxesAndDuesNOE(Enum):
    """"租税公課、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class TaxesAndDuesSGA(Enum):
    """"租税公課、販売費及び一般管理費"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class TechnicalSupportFeeNOI(Enum):
    """"受取技術料、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class TelephoneSubscriptionRight(Enum):
    """"電話加入権"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class ToolsFurnitureAndFixtures(Enum):
    """"工具、器具及び備品"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class ToolsFurnitureAndFixturesNet(Enum):
    """"工具、器具及び備品（純額）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class TotalBeginningAndPurchaseOfGoods(Enum):
    """"合計、商品期首棚卸高及び当期商品仕入高"""
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class TotalBeginningFinishedGoodsAndCostOfProductsManufacturedForThePeriod(Enum):
    """"合計、製品期首棚卸高及び当期製品製造原価"""
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class TotalChangesOfItemsDuringThePeriod(Enum):
    """"当期変動額合計"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__CAPITAL_STOCK_MEMBER = 'CurrentYearDuration_CapitalStockMember'
    """ 当年度会計期間資本金 """
    CURRENT_YEAR_DURATION__CAPITAL_SURPLUS_MEMBER = 'CurrentYearDuration_CapitalSurplusMember'
    """ 当年度会計期間資本剰余金 """
    CURRENT_YEAR_DURATION__DEFERRED_GAINS_OR_LOSSES_ON_HEDGES_MEMBER = 'CurrentYearDuration_DeferredGainsOrLossesOnHedgesMember'
    """ 当年度会計期間繰延ヘッジ損益 """
    CURRENT_YEAR_DURATION__FOREIGN_CURRENCY_TRANSLATION_ADJUSTMENT_MEMBER = 'CurrentYearDuration_ForeignCurrencyTranslationAdjustmentMember'
    """ 当年度会計期間為替換算調整勘定 """
    CURRENT_YEAR_DURATION__LEGAL_CAPITAL_SURPLUS_MEMBER = 'CurrentYearDuration_LegalCapitalSurplusMember'
    """ 当年度会計期間資本準備金 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CAPITAL_STOCK_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_CapitalStockMember'
    """ 当年度会計期間個別又は非連結資本金 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CAPITAL_SURPLUS_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_CapitalSurplusMember'
    """ 当年度会計期間個別又は非連結資本剰余金 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__DEFERRED_GAINS_OR_LOSSES_ON_HEDGES_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_DeferredGainsOrLossesOnHedgesMember'
    """ 当年度会計期間個別又は非連結繰延ヘッジ損益 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__GENERAL_RESERVE_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_GeneralReserveMember'
    """ 当年度会計期間個別又は非連結別途積立金 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__LEGAL_CAPITAL_SURPLUS_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_LegalCapitalSurplusMember'
    """ 当年度会計期間個別又は非連結資本準備金 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__LEGAL_RETAINED_EARNINGS_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_LegalRetainedEarningsMember'
    """ 当年度会計期間個別又は非連結利益準備金 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__OTHER_CAPITAL_SURPLUS_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_OtherCapitalSurplusMember'
    """ 当年度会計期間個別又は非連結その他資本剰余金 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RESERVE_FOR_ADVANCED_DEPRECIATION_OF_NONCURRENT_ASSETS_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_ReserveForAdvancedDepreciationOfNoncurrentAssetsMember'
    """ 当年度会計期間個別又は非連結固定資産圧縮積立金 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RESERVE_FOR_DIVIDENDS3_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_ReserveForDividends3Member'
    """ 当年度会計期間個別又は非連結配当準備積立金 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RESERVE_FOR_SPECIAL_DEPRECIATION_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_ReserveForSpecialDepreciationMember'
    """ 当年度会計期間個別又は非連結特別償却準備金 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_BROUGHT_FORWARD_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_RetainedEarningsBroughtForwardMember'
    """ 当年度会計期間個別又は非連結繰越利益剰余金 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_RetainedEarningsMember'
    """ 当年度会計期間個別又は非連結利益剰余金 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__SHAREHOLDERS_EQUITY_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_ShareholdersEquityMember'
    """ 当年度会計期間個別又は非連結株主資本 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__SUBSCRIPTION_RIGHTS_TO_SHARES_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_SubscriptionRightsToSharesMember'
    """ 当年度会計期間個別又は非連結新株予約権 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__TREASURY_STOCK_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_TreasuryStockMember'
    """ 当年度会計期間個別又は非連結自己株式 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__VALUATION_AND_TRANSLATION_ADJUSTMENTS_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_ValuationAndTranslationAdjustmentsMember'
    """ 当年度会計期間個別又は非連結評価・換算差額等 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__VALUATION_DIFFERENCE_ON_AVAILABLE_FOR_SALE_SECURITIES_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_ValuationDifferenceOnAvailableForSaleSecuritiesMember'
    """ 当年度会計期間個別又は非連結その他有価証券評価差額金 """
    CURRENT_YEAR_DURATION__NON_CONTROLLING_INTERESTS_MEMBER = 'CurrentYearDuration_NonControllingInterestsMember'
    """ 当年度会計期間非支配株主持分 """
    CURRENT_YEAR_DURATION__OTHER_CAPITAL_SURPLUS_MEMBER = 'CurrentYearDuration_OtherCapitalSurplusMember'
    """ 当年度会計期間その他資本剰余金 """
    CURRENT_YEAR_DURATION__REMEASUREMENTS_OF_DEFINED_BENEFIT_PLANS_MEMBER = 'CurrentYearDuration_RemeasurementsOfDefinedBenefitPlansMember'
    """ 当年度会計期間退職給付に係る調整累計額 """
    CURRENT_YEAR_DURATION__RETAINED_EARNINGS_BROUGHT_FORWARD_MEMBER = 'CurrentYearDuration_RetainedEarningsBroughtForwardMember'
    """ 当年度会計期間繰越利益剰余金 """
    CURRENT_YEAR_DURATION__RETAINED_EARNINGS_MEMBER = 'CurrentYearDuration_RetainedEarningsMember'
    """ 当年度会計期間利益剰余金 """
    CURRENT_YEAR_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'CurrentYearDuration_ShareholdersEquityMember'
    """ 当年度会計期間株主資本 """
    CURRENT_YEAR_DURATION__SUBSCRIPTION_RIGHTS_TO_SHARES_MEMBER = 'CurrentYearDuration_SubscriptionRightsToSharesMember'
    """ 当年度会計期間新株予約権 """
    CURRENT_YEAR_DURATION__TREASURY_STOCK_MEMBER = 'CurrentYearDuration_TreasuryStockMember'
    """ 当年度会計期間自己株式 """
    CURRENT_YEAR_DURATION__VALUATION_AND_TRANSLATION_ADJUSTMENTS_MEMBER = 'CurrentYearDuration_ValuationAndTranslationAdjustmentsMember'
    """ 当年度会計期間評価・換算差額等 """
    CURRENT_YEAR_DURATION__VALUATION_DIFFERENCE_ON_AVAILABLE_FOR_SALE_SECURITIES_MEMBER = 'CurrentYearDuration_ValuationDifferenceOnAvailableForSaleSecuritiesMember'
    """ 当年度会計期間その他有価証券評価差額金 """
    INTERIM_DURATION = 'InterimDuration'
    INTERIM_DURATION__CAPITAL_STOCK_MEMBER = 'InterimDuration_CapitalStockMember'
    """ 資本金 """
    INTERIM_DURATION__CAPITAL_SURPLUS_MEMBER = 'InterimDuration_CapitalSurplusMember'
    """ 資本剰余金 """
    INTERIM_DURATION__DEFERRED_GAINS_OR_LOSSES_ON_HEDGES_MEMBER = 'InterimDuration_DeferredGainsOrLossesOnHedgesMember'
    """ 繰延ヘッジ損益 """
    INTERIM_DURATION__FOREIGN_CURRENCY_TRANSLATION_ADJUSTMENT_MEMBER = 'InterimDuration_ForeignCurrencyTranslationAdjustmentMember'
    """ 為替換算調整勘定 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__CAPITAL_STOCK_MEMBER = 'InterimDuration_NonConsolidatedMember_CapitalStockMember'
    """ 個別又は非連結資本金 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__CAPITAL_SURPLUS_MEMBER = 'InterimDuration_NonConsolidatedMember_CapitalSurplusMember'
    """ 個別又は非連結資本剰余金 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__DEFERRED_GAINS_OR_LOSSES_ON_HEDGES_MEMBER = 'InterimDuration_NonConsolidatedMember_DeferredGainsOrLossesOnHedgesMember'
    """ 個別又は非連結繰延ヘッジ損益 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__GENERAL_RESERVE_MEMBER = 'InterimDuration_NonConsolidatedMember_GeneralReserveMember'
    """ 個別又は非連結別途積立金 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__LEGAL_CAPITAL_SURPLUS_MEMBER = 'InterimDuration_NonConsolidatedMember_LegalCapitalSurplusMember'
    """ 個別又は非連結資本準備金 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__LEGAL_RETAINED_EARNINGS_MEMBER = 'InterimDuration_NonConsolidatedMember_LegalRetainedEarningsMember'
    """ 個別又は非連結利益準備金 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__OTHER_CAPITAL_SURPLUS_MEMBER = 'InterimDuration_NonConsolidatedMember_OtherCapitalSurplusMember'
    """ 個別又は非連結その他資本剰余金 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RESERVE_FOR_ADVANCED_DEPRECIATION_OF_NONCURRENT_ASSETS_MEMBER = 'InterimDuration_NonConsolidatedMember_ReserveForAdvancedDepreciationOfNoncurrentAssetsMember'
    """ 個別又は非連結固定資産圧縮積立金 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RESERVE_FOR_REDUCTION_ENTRY2_MEMBER = 'InterimDuration_NonConsolidatedMember_ReserveForReductionEntry2Member'
    """ 個別又は非連結圧縮積立金 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RESERVE_FOR_REDUCTION_ENTRY_OF_REAL_ESTATE_MEMBER = 'InterimDuration_NonConsolidatedMember_ReserveForReductionEntryOfRealEstateMember'
    """ 個別又は非連結不動産圧縮積立金 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RESERVE_FOR_SPECIAL_ACCOUNT_FOR_ADVANCED_DEPRECIATION_OF_NONCURRENT_ASSETS_MEMBER = 'InterimDuration_NonConsolidatedMember_ReserveForSpecialAccountForAdvancedDepreciationOfNoncurrentAssetsMember'
    """ 個別又は非連結固定資産圧縮特別勘定積立金 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_BROUGHT_FORWARD_MEMBER = 'InterimDuration_NonConsolidatedMember_RetainedEarningsBroughtForwardMember'
    """ 個別又は非連結繰越利益剰余金 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_MEMBER = 'InterimDuration_NonConsolidatedMember_RetainedEarningsMember'
    """ 個別又は非連結利益剰余金 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__REVALUATION_RESERVE_FOR_LAND_MEMBER = 'InterimDuration_NonConsolidatedMember_RevaluationReserveForLandMember'
    """ 個別又は非連結土地再評価差額金 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__SHAREHOLDERS_EQUITY_MEMBER = 'InterimDuration_NonConsolidatedMember_ShareholdersEquityMember'
    """ 個別又は非連結株主資本 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__SUBSCRIPTION_RIGHTS_TO_SHARES_MEMBER = 'InterimDuration_NonConsolidatedMember_SubscriptionRightsToSharesMember'
    """ 個別又は非連結新株予約権 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__TREASURY_STOCK_MEMBER = 'InterimDuration_NonConsolidatedMember_TreasuryStockMember'
    """ 個別又は非連結自己株式 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__VALUATION_AND_TRANSLATION_ADJUSTMENTS_MEMBER = 'InterimDuration_NonConsolidatedMember_ValuationAndTranslationAdjustmentsMember'
    """ 個別又は非連結評価・換算差額等 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__VALUATION_DIFFERENCE_ON_AVAILABLE_FOR_SALE_SECURITIES_MEMBER = 'InterimDuration_NonConsolidatedMember_ValuationDifferenceOnAvailableForSaleSecuritiesMember'
    """ 個別又は非連結その他有価証券評価差額金 """
    INTERIM_DURATION__NON_CONTROLLING_INTERESTS_MEMBER = 'InterimDuration_NonControllingInterestsMember'
    """ 非支配株主持分 """
    INTERIM_DURATION__REMEASUREMENTS_OF_DEFINED_BENEFIT_PLANS_MEMBER = 'InterimDuration_RemeasurementsOfDefinedBenefitPlansMember'
    """ 退職給付に係る調整累計額 """
    INTERIM_DURATION__RETAINED_EARNINGS_MEMBER = 'InterimDuration_RetainedEarningsMember'
    """ 利益剰余金 """
    INTERIM_DURATION__REVALUATION_RESERVE_FOR_LAND_MEMBER = 'InterimDuration_RevaluationReserveForLandMember'
    """ 土地再評価差額金 """
    INTERIM_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'InterimDuration_ShareholdersEquityMember'
    """ 株主資本 """
    INTERIM_DURATION__SUBSCRIPTION_RIGHTS_TO_SHARES_MEMBER = 'InterimDuration_SubscriptionRightsToSharesMember'
    """ 新株予約権 """
    INTERIM_DURATION__TREASURY_STOCK_MEMBER = 'InterimDuration_TreasuryStockMember'
    """ 自己株式 """
    INTERIM_DURATION__VALUATION_AND_TRANSLATION_ADJUSTMENTS_MEMBER = 'InterimDuration_ValuationAndTranslationAdjustmentsMember'
    """ 評価・換算差額等 """
    INTERIM_DURATION__VALUATION_DIFFERENCE_ON_AVAILABLE_FOR_SALE_SECURITIES_MEMBER = 'InterimDuration_ValuationDifferenceOnAvailableForSaleSecuritiesMember'
    """ その他有価証券評価差額金 """
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_INTERIM_DURATION__CAPITAL_STOCK_MEMBER = 'Prior1InterimDuration_CapitalStockMember'
    """ 資本金 """
    PRIOR1_INTERIM_DURATION__CAPITAL_SURPLUS_MEMBER = 'Prior1InterimDuration_CapitalSurplusMember'
    """ 資本剰余金 """
    PRIOR1_INTERIM_DURATION__DEFERRED_GAINS_OR_LOSSES_ON_HEDGES_MEMBER = 'Prior1InterimDuration_DeferredGainsOrLossesOnHedgesMember'
    """ 繰延ヘッジ損益 """
    PRIOR1_INTERIM_DURATION__FOREIGN_CURRENCY_TRANSLATION_ADJUSTMENT_MEMBER = 'Prior1InterimDuration_ForeignCurrencyTranslationAdjustmentMember'
    """ 為替換算調整勘定 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__CAPITAL_STOCK_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_CapitalStockMember'
    """ 個別又は非連結資本金 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__CAPITAL_SURPLUS_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_CapitalSurplusMember'
    """ 個別又は非連結資本剰余金 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__DEFERRED_GAINS_OR_LOSSES_ON_HEDGES_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_DeferredGainsOrLossesOnHedgesMember'
    """ 個別又は非連結繰延ヘッジ損益 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__GENERAL_RESERVE_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_GeneralReserveMember'
    """ 個別又は非連結別途積立金 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__LEGAL_CAPITAL_SURPLUS_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_LegalCapitalSurplusMember'
    """ 個別又は非連結資本準備金 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__LEGAL_RETAINED_EARNINGS_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_LegalRetainedEarningsMember'
    """ 個別又は非連結利益準備金 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__OTHER_CAPITAL_SURPLUS_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_OtherCapitalSurplusMember'
    """ 個別又は非連結その他資本剰余金 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RESERVE_FOR_ADVANCED_DEPRECIATION_OF_NONCURRENT_ASSETS_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_ReserveForAdvancedDepreciationOfNoncurrentAssetsMember'
    """ 個別又は非連結固定資産圧縮積立金 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RESERVE_FOR_REDUCTION_ENTRY2_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_ReserveForReductionEntry2Member'
    """ 個別又は非連結圧縮積立金 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RESERVE_FOR_REDUCTION_ENTRY_OF_REAL_ESTATE_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_ReserveForReductionEntryOfRealEstateMember'
    """ 個別又は非連結不動産圧縮積立金 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RESERVE_FOR_SPECIAL_ACCOUNT_FOR_ADVANCED_DEPRECIATION_OF_NONCURRENT_ASSETS_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_ReserveForSpecialAccountForAdvancedDepreciationOfNoncurrentAssetsMember'
    """ 個別又は非連結固定資産圧縮特別勘定積立金 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_BROUGHT_FORWARD_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_RetainedEarningsBroughtForwardMember'
    """ 個別又は非連結繰越利益剰余金 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_RetainedEarningsMember'
    """ 個別又は非連結利益剰余金 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__REVALUATION_RESERVE_FOR_LAND_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_RevaluationReserveForLandMember'
    """ 個別又は非連結土地再評価差額金 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_ShareholdersEquityMember'
    """ 個別又は非連結株主資本 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__SUBSCRIPTION_RIGHTS_TO_SHARES_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_SubscriptionRightsToSharesMember'
    """ 個別又は非連結新株予約権 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__TREASURY_STOCK_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_TreasuryStockMember'
    """ 個別又は非連結自己株式 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__VALUATION_AND_TRANSLATION_ADJUSTMENTS_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_ValuationAndTranslationAdjustmentsMember'
    """ 個別又は非連結評価・換算差額等 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__VALUATION_DIFFERENCE_ON_AVAILABLE_FOR_SALE_SECURITIES_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_ValuationDifferenceOnAvailableForSaleSecuritiesMember'
    """ 個別又は非連結その他有価証券評価差額金 """
    PRIOR1_INTERIM_DURATION__NON_CONTROLLING_INTERESTS_MEMBER = 'Prior1InterimDuration_NonControllingInterestsMember'
    """ 非支配株主持分 """
    PRIOR1_INTERIM_DURATION__REMEASUREMENTS_OF_DEFINED_BENEFIT_PLANS_MEMBER = 'Prior1InterimDuration_RemeasurementsOfDefinedBenefitPlansMember'
    """ 退職給付に係る調整累計額 """
    PRIOR1_INTERIM_DURATION__RETAINED_EARNINGS_MEMBER = 'Prior1InterimDuration_RetainedEarningsMember'
    """ 利益剰余金 """
    PRIOR1_INTERIM_DURATION__REVALUATION_RESERVE_FOR_LAND_MEMBER = 'Prior1InterimDuration_RevaluationReserveForLandMember'
    """ 土地再評価差額金 """
    PRIOR1_INTERIM_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1InterimDuration_ShareholdersEquityMember'
    """ 株主資本 """
    PRIOR1_INTERIM_DURATION__SUBSCRIPTION_RIGHTS_TO_SHARES_MEMBER = 'Prior1InterimDuration_SubscriptionRightsToSharesMember'
    """ 新株予約権 """
    PRIOR1_INTERIM_DURATION__TREASURY_STOCK_MEMBER = 'Prior1InterimDuration_TreasuryStockMember'
    """ 自己株式 """
    PRIOR1_INTERIM_DURATION__VALUATION_AND_TRANSLATION_ADJUSTMENTS_MEMBER = 'Prior1InterimDuration_ValuationAndTranslationAdjustmentsMember'
    """ 評価・換算差額等 """
    PRIOR1_INTERIM_DURATION__VALUATION_DIFFERENCE_ON_AVAILABLE_FOR_SALE_SECURITIES_MEMBER = 'Prior1InterimDuration_ValuationDifferenceOnAvailableForSaleSecuritiesMember'
    """ その他有価証券評価差額金 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__CAPITAL_STOCK_MEMBER = 'Prior1YearDuration_CapitalStockMember'
    """ 資本金 """
    PRIOR1_YEAR_DURATION__CAPITAL_SURPLUS_MEMBER = 'Prior1YearDuration_CapitalSurplusMember'
    """ 資本剰余金 """
    PRIOR1_YEAR_DURATION__DEFERRED_GAINS_OR_LOSSES_ON_HEDGES_MEMBER = 'Prior1YearDuration_DeferredGainsOrLossesOnHedgesMember'
    """ 繰延ヘッジ損益 """
    PRIOR1_YEAR_DURATION__FOREIGN_CURRENCY_TRANSLATION_ADJUSTMENT_MEMBER = 'Prior1YearDuration_ForeignCurrencyTranslationAdjustmentMember'
    """ 為替換算調整勘定 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CAPITAL_STOCK_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_CapitalStockMember'
    """ 個別又は非連結資本金 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CAPITAL_SURPLUS_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_CapitalSurplusMember'
    """ 個別又は非連結資本剰余金 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__DEFERRED_GAINS_OR_LOSSES_ON_HEDGES_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_DeferredGainsOrLossesOnHedgesMember'
    """ 個別又は非連結繰延ヘッジ損益 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__GENERAL_RESERVE_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_GeneralReserveMember'
    """ 個別又は非連結別途積立金 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__LEGAL_CAPITAL_SURPLUS_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_LegalCapitalSurplusMember'
    """ 個別又は非連結資本準備金 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__LEGAL_RETAINED_EARNINGS_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_LegalRetainedEarningsMember'
    """ 個別又は非連結利益準備金 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__OTHER_CAPITAL_SURPLUS_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_OtherCapitalSurplusMember'
    """ 個別又は非連結その他資本剰余金 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RESERVE_FOR_ADVANCED_DEPRECIATION_OF_NONCURRENT_ASSETS_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_ReserveForAdvancedDepreciationOfNoncurrentAssetsMember'
    """ 個別又は非連結固定資産圧縮積立金 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RESERVE_FOR_DIVIDENDS3_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_ReserveForDividends3Member'
    """ 個別又は非連結配当準備積立金 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RESERVE_FOR_SPECIAL_DEPRECIATION_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_ReserveForSpecialDepreciationMember'
    """ 個別又は非連結特別償却準備金 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_BROUGHT_FORWARD_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_RetainedEarningsBroughtForwardMember'
    """ 個別又は非連結繰越利益剰余金 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_RetainedEarningsMember'
    """ 個別又は非連結利益剰余金 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_ShareholdersEquityMember'
    """ 個別又は非連結株主資本 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__SUBSCRIPTION_RIGHTS_TO_SHARES_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_SubscriptionRightsToSharesMember'
    """ 個別又は非連結新株予約権 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__TREASURY_STOCK_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_TreasuryStockMember'
    """ 個別又は非連結自己株式 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__VALUATION_AND_TRANSLATION_ADJUSTMENTS_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_ValuationAndTranslationAdjustmentsMember'
    """ 個別又は非連結評価・換算差額等 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__VALUATION_DIFFERENCE_ON_AVAILABLE_FOR_SALE_SECURITIES_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_ValuationDifferenceOnAvailableForSaleSecuritiesMember'
    """ 個別又は非連結その他有価証券評価差額金 """
    PRIOR1_YEAR_DURATION__NON_CONTROLLING_INTERESTS_MEMBER = 'Prior1YearDuration_NonControllingInterestsMember'
    """ 非支配株主持分 """
    PRIOR1_YEAR_DURATION__REMEASUREMENTS_OF_DEFINED_BENEFIT_PLANS_MEMBER = 'Prior1YearDuration_RemeasurementsOfDefinedBenefitPlansMember'
    """ 退職給付に係る調整累計額 """
    PRIOR1_YEAR_DURATION__RETAINED_EARNINGS_MEMBER = 'Prior1YearDuration_RetainedEarningsMember'
    """ 利益剰余金 """
    PRIOR1_YEAR_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1YearDuration_ShareholdersEquityMember'
    """ 株主資本 """
    PRIOR1_YEAR_DURATION__SUBSCRIPTION_RIGHTS_TO_SHARES_MEMBER = 'Prior1YearDuration_SubscriptionRightsToSharesMember'
    """ 新株予約権 """
    PRIOR1_YEAR_DURATION__TREASURY_STOCK_MEMBER = 'Prior1YearDuration_TreasuryStockMember'
    """ 自己株式 """
    PRIOR1_YEAR_DURATION__VALUATION_AND_TRANSLATION_ADJUSTMENTS_MEMBER = 'Prior1YearDuration_ValuationAndTranslationAdjustmentsMember'
    """ 評価・換算差額等 """
    PRIOR1_YEAR_DURATION__VALUATION_DIFFERENCE_ON_AVAILABLE_FOR_SALE_SECURITIES_MEMBER = 'Prior1YearDuration_ValuationDifferenceOnAvailableForSaleSecuritiesMember'
    """ その他有価証券評価差額金 """


class TotalOfNetCashProvidedByUsedInInvestmentTransactionsInvCFINS(Enum):
    """"資産運用活動計、投資活動によるキャッシュ・フロー、保険業"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class TotalOfNetCashProvidedByUsedInOperatingActivitiesAndInvestmentTransactionsInvCFINS(Enum):
    """"営業活動及び資産運用活動計、投資活動によるキャッシュ・フロー、保険業"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class TradingAccountSecuritiesAssetsBNK(Enum):
    """"商品有価証券、資産の部、銀行業"""
    INTERIM_INSTANT = 'InterimInstant'
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class TradingAssetsAssetsBNK(Enum):
    """"特定取引資産、資産の部、銀行業"""
    INTERIM_INSTANT = 'InterimInstant'
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class TradingExpensesOEBNK(Enum):
    """"特定取引費用、経常費用、銀行業"""
    INTERIM_DURATION = 'InterimDuration'
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class TradingIncomeOIBNK(Enum):
    """"特定取引収益、経常収益、銀行業"""
    INTERIM_DURATION = 'InterimDuration'
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class TradingLiabilitiesLiabilitiesBNK(Enum):
    """"特定取引負債、負債の部、銀行業"""
    INTERIM_INSTANT = 'InterimInstant'
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class TransferFromReserveForFinancialProductsTransactionLiabilitiesEIBNK(Enum):
    """"金融商品取引責任準備金取崩額、特別利益、銀行業"""
    INTERIM_DURATION = 'InterimDuration'
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class TransferOfLossOnDisposalOfTreasuryStock(Enum):
    """"自己株式処分差損の振替"""
    INTERIM_DURATION = 'InterimDuration'
    INTERIM_DURATION__CAPITAL_SURPLUS_MEMBER = 'InterimDuration_CapitalSurplusMember'
    """ 資本剰余金 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__CAPITAL_SURPLUS_MEMBER = 'InterimDuration_NonConsolidatedMember_CapitalSurplusMember'
    """ 個別又は非連結資本剰余金 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__OTHER_CAPITAL_SURPLUS_MEMBER = 'InterimDuration_NonConsolidatedMember_OtherCapitalSurplusMember'
    """ 個別又は非連結その他資本剰余金 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_BROUGHT_FORWARD_MEMBER = 'InterimDuration_NonConsolidatedMember_RetainedEarningsBroughtForwardMember'
    """ 個別又は非連結繰越利益剰余金 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_MEMBER = 'InterimDuration_NonConsolidatedMember_RetainedEarningsMember'
    """ 個別又は非連結利益剰余金 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__SHAREHOLDERS_EQUITY_MEMBER = 'InterimDuration_NonConsolidatedMember_ShareholdersEquityMember'
    """ 個別又は非連結株主資本 """
    INTERIM_DURATION__RETAINED_EARNINGS_MEMBER = 'InterimDuration_RetainedEarningsMember'
    """ 利益剰余金 """
    INTERIM_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'InterimDuration_ShareholdersEquityMember'
    """ 株主資本 """
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_INTERIM_DURATION__CAPITAL_SURPLUS_MEMBER = 'Prior1InterimDuration_CapitalSurplusMember'
    """ 資本剰余金 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__CAPITAL_SURPLUS_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_CapitalSurplusMember'
    """ 個別又は非連結資本剰余金 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__OTHER_CAPITAL_SURPLUS_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_OtherCapitalSurplusMember'
    """ 個別又は非連結その他資本剰余金 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_BROUGHT_FORWARD_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_RetainedEarningsBroughtForwardMember'
    """ 個別又は非連結繰越利益剰余金 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_RetainedEarningsMember'
    """ 個別又は非連結利益剰余金 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_ShareholdersEquityMember'
    """ 個別又は非連結株主資本 """
    PRIOR1_INTERIM_DURATION__RETAINED_EARNINGS_MEMBER = 'Prior1InterimDuration_RetainedEarningsMember'
    """ 利益剰余金 """
    PRIOR1_INTERIM_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1InterimDuration_ShareholdersEquityMember'
    """ 株主資本 """


class TransferToCapitalSurplusFromRetainedEarnings(Enum):
    """"利益剰余金から資本剰余金への振替"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__CAPITAL_SURPLUS_MEMBER = 'CurrentYearDuration_CapitalSurplusMember'
    """ 当年度会計期間資本剰余金 """
    CURRENT_YEAR_DURATION__RETAINED_EARNINGS_MEMBER = 'CurrentYearDuration_RetainedEarningsMember'
    """ 当年度会計期間利益剰余金 """
    CURRENT_YEAR_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'CurrentYearDuration_ShareholdersEquityMember'
    """ 当年度会計期間株主資本 """
    INTERIM_DURATION = 'InterimDuration'
    INTERIM_DURATION__CAPITAL_SURPLUS_MEMBER = 'InterimDuration_CapitalSurplusMember'
    """ 資本剰余金 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__CAPITAL_SURPLUS_MEMBER = 'InterimDuration_NonConsolidatedMember_CapitalSurplusMember'
    """ 個別又は非連結資本剰余金 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__OTHER_CAPITAL_SURPLUS_MEMBER = 'InterimDuration_NonConsolidatedMember_OtherCapitalSurplusMember'
    """ 個別又は非連結その他資本剰余金 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_BROUGHT_FORWARD_MEMBER = 'InterimDuration_NonConsolidatedMember_RetainedEarningsBroughtForwardMember'
    """ 個別又は非連結繰越利益剰余金 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_MEMBER = 'InterimDuration_NonConsolidatedMember_RetainedEarningsMember'
    """ 個別又は非連結利益剰余金 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__SHAREHOLDERS_EQUITY_MEMBER = 'InterimDuration_NonConsolidatedMember_ShareholdersEquityMember'
    """ 個別又は非連結株主資本 """
    INTERIM_DURATION__RETAINED_EARNINGS_MEMBER = 'InterimDuration_RetainedEarningsMember'
    """ 利益剰余金 """
    INTERIM_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'InterimDuration_ShareholdersEquityMember'
    """ 株主資本 """
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_INTERIM_DURATION__CAPITAL_SURPLUS_MEMBER = 'Prior1InterimDuration_CapitalSurplusMember'
    """ 資本剰余金 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__CAPITAL_SURPLUS_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_CapitalSurplusMember'
    """ 個別又は非連結資本剰余金 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__OTHER_CAPITAL_SURPLUS_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_OtherCapitalSurplusMember'
    """ 個別又は非連結その他資本剰余金 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_BROUGHT_FORWARD_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_RetainedEarningsBroughtForwardMember'
    """ 個別又は非連結繰越利益剰余金 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_RetainedEarningsMember'
    """ 個別又は非連結利益剰余金 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_ShareholdersEquityMember'
    """ 個別又は非連結株主資本 """
    PRIOR1_INTERIM_DURATION__RETAINED_EARNINGS_MEMBER = 'Prior1InterimDuration_RetainedEarningsMember'
    """ 利益剰余金 """
    PRIOR1_INTERIM_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1InterimDuration_ShareholdersEquityMember'
    """ 株主資本 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__CAPITAL_SURPLUS_MEMBER = 'Prior1YearDuration_CapitalSurplusMember'
    """ 資本剰余金 """
    PRIOR1_YEAR_DURATION__RETAINED_EARNINGS_MEMBER = 'Prior1YearDuration_RetainedEarningsMember'
    """ 利益剰余金 """
    PRIOR1_YEAR_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1YearDuration_ShareholdersEquityMember'
    """ 株主資本 """


class TransferToOtherAccountCOS(Enum):
    """"他勘定振替高、売上原価"""
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class TransferToReserveForFinancialProductsTransactionLiabilitiesELBNK(Enum):
    """"金融商品取引責任準備金繰入額、特別損失、銀行業"""
    INTERIM_DURATION = 'InterimDuration'
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class TransportationAndCommunicationExpensesSGA(Enum):
    """"旅費交通費及び通信費、販売費及び一般管理費"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class TransportationAndWarehousingExpensesSGA(Enum):
    """"運送費及び保管費、販売費及び一般管理費"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class TransportationIncomeRevOA(Enum):
    """"運送収入、営業活動による収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class TravelingAndTransportationExpensesSGA(Enum):
    """"旅費及び交通費、販売費及び一般管理費"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class TreasuryStock(Enum):
    """"自己株式"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    INTERIM_INSTANT = 'InterimInstant'
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class TreesPPE(Enum):
    """"立木、有形固定資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class TrustFeesBNK(Enum):
    """"信託報酬、銀行業"""
    INTERIM_DURATION = 'InterimDuration'
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class UnderwritingExpensesOEINS(Enum):
    """"保険引受費用、経常費用、保険業"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class UnderwritingIncomeOIINS(Enum):
    """"保険引受収益、経常収益、保険業"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class UnearnedRevenue(Enum):
    """"前受収益"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class UtilitiesExpensesSGA(Enum):
    """"水道光熱費、販売費及び一般管理費"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class ValuationAndTranslationAdjustments(Enum):
    """"評価・換算差額等"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    INTERIM_INSTANT = 'InterimInstant'
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class ValuationDifferenceOnAvailableForSaleSecurities(Enum):
    """"その他有価証券評価差額金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    INTERIM_INSTANT = 'InterimInstant'
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class ValuationDifferenceOnAvailableForSaleSecuritiesBeforeTaxOCI(Enum):
    """"その他有価証券評価差額金（税引前）、その他の包括利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ValuationDifferenceOnAvailableForSaleSecuritiesNetOfTaxOCI(Enum):
    """"その他有価証券評価差額金（税引後）、その他の包括利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class VehicleExpensesSGA(Enum):
    """"車両費、販売費及び一般管理費"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class Vehicles(Enum):
    """"車両運搬具"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class VehiclesNet(Enum):
    """"車両運搬具（純額）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class Vessels(Enum):
    """"船舶"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class VesselsNet(Enum):
    """"船舶（純額）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class WarehousingExpensesSGA(Enum):
    """"保管費、販売費及び一般管理費"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class WarehousingFeeIncomeRevOA(Enum):
    """"倉庫保管料、営業活動による収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class WelfareExpensesSGA(Enum):
    """"福利厚生費、販売費及び一般管理費"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class WorkInProcess(Enum):
    """"仕掛品"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class BusinessStructureImprovementPaymentsOpeCF(Enum):
    """"事業構造改善支出、営業活動によるキャッシュ・フロー"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class ChangesInEquityDueToCapitalTransfer(Enum):
    """"資本移動に伴う持分の変動"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__CAPITAL_SURPLUS_MEMBER = 'CurrentYearDuration_CapitalSurplusMember'
    """ 当年度会計期間資本剰余金 """
    CURRENT_YEAR_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'CurrentYearDuration_ShareholdersEquityMember'
    """ 当年度会計期間株主資本 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1YearDuration_ShareholdersEquityMember'
    """ 株主資本 """


class LoansMadeToCustomersInvCF(Enum):
    """"貸付金による支出、投資活動によるキャッシュ・フロー"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class LossesOnFireDisasterEL(Enum):
    """"火災損害等損失、特別損失"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class PurchaseOfShareOfConsolidatedSubsidiariesTreasuryStockChangesOfItemsDuringPeriod(Enum):
    """"連結子会社の自己株式取得による持分の増減"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__CAPITAL_SURPLUS_MEMBER = 'CurrentYearDuration_CapitalSurplusMember'
    """ 当年度会計期間資本剰余金 """
    CURRENT_YEAR_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'CurrentYearDuration_ShareholdersEquityMember'
    """ 当年度会計期間株主資本 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__CAPITAL_SURPLUS_MEMBER = 'Prior1YearDuration_CapitalSurplusMember'
    """ 資本剰余金 """
    PRIOR1_YEAR_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1YearDuration_ShareholdersEquityMember'
    """ 株主資本 """


class NonDeductibleConsumptionTaxNOE(Enum):
    """"控除対象外消費税等、営業外費用"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class AmortizationOfGoodwillEL(Enum):
    """"のれん償却額、特別損失"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class AmortizationOfGoodwillSegmentInformation(Enum):
    """"のれん償却額、セグメント情報"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class DepreciationOfFixedAssetsOpeCF(Enum):
    """"有形固定資産減価償却費、営業活動によるキャッシュ・フロー"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class DepreciationOfIntangibleAssets(Enum):
    """"無形固定資産減価償却費、営業活動によるキャッシュ・フロー"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class IssuanceOfNewSharesRestrictedStock(Enum):
    """"新株の発行（譲渡制限付株式報酬）"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__CAPITAL_STOCK_MEMBER = 'CurrentYearDuration_CapitalStockMember'
    """ 当年度会計期間資本金 """
    CURRENT_YEAR_DURATION__CAPITAL_SURPLUS_MEMBER = 'CurrentYearDuration_CapitalSurplusMember'
    """ 当年度会計期間資本剰余金 """
    CURRENT_YEAR_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'CurrentYearDuration_ShareholdersEquityMember'
    """ 当年度会計期間株主資本 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__CAPITAL_STOCK_MEMBER = 'Prior1YearDuration_CapitalStockMember'
    """ 資本金 """
    PRIOR1_YEAR_DURATION__CAPITAL_SURPLUS_MEMBER = 'Prior1YearDuration_CapitalSurplusMember'
    """ 資本剰余金 """
    PRIOR1_YEAR_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1YearDuration_ShareholdersEquityMember'
    """ 株主資本 """


class LeaseAndGuaranteeDepositsIOA(Enum):
    """"差入敷金保証金、投資その他の資産、固定資産、資産の部"""
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ProceedsFromShareOfProfitsOnInvestmentsInPartnership(Enum):
    """"投資事業組合分配金収入、投資活動によるキャッシュ・フロー"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class GainOnDisposalOfTreasuryStock(Enum):
    """"自己株式処分差益"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__CAPITAL_SURPLUS_MEMBER = 'CurrentYearDuration_CapitalSurplusMember'
    """ 当年度会計期間資本剰余金 """
    CURRENT_YEAR_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'CurrentYearDuration_ShareholdersEquityMember'
    """ 当年度会計期間株主資本 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__CAPITAL_SURPLUS_MEMBER = 'Prior1YearDuration_CapitalSurplusMember'
    """ 資本剰余金 """
    PRIOR1_YEAR_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1YearDuration_ShareholdersEquityMember'
    """ 株主資本 """


class HeadOfficeRelocationExpensesNOE(Enum):
    """"本社移転費用、営業外費用"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class NonDeductibleConsumptionTaxNOE(Enum):
    """"控除対象外消費税等、営業外費用"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class ProceedsFromSurrenderValueOfInsurancePoliciesOpeCF(Enum):
    """"保険解約返戻金の受取額、営業活動によるキャッシュ・フロー"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class ProceedsFromWithdrawalOfInvestmentsInSecuritiesInvCF(Enum):
    """"投資有価証券の払戻による収入、投資活動によるキャッシュ・フロー"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class RetirementBenefitLiabilityCL(Enum):
    """"退職給付に係る負債、流動負債"""
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class CompensationForDamageIncomeNOI(Enum):
    """"受取損害賠償金、営業外収益"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class IncreaseDecreaseInAccountPayableTransitionOfRetirementBenefitPlanOpeCF(Enum):
    """"退職給付制度移行に伴う未払金の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class IncreaseDecreaseInNetDefinedBenefitAssetAndLiabilityOpeCF(Enum):
    """"退職給付に係る資産負債の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class ProceedsFromSurrenderValueOfInsuranceOpeCF(Enum):
    """"保険解約返戻金の受取額、営業活動によるキャッシュ・フロー"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class CustomerRelationshipIA(Enum):
    """"顧客関連資産、無形固定資産"""
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class LossOnRelatedToRebuildingEL(Enum):
    """"建替関連損失、特別損失"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class LossOnRelatedToRebuildingOpeCF(Enum):
    """"建替関連損失、営業活動によるキャッシュ・フロー"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class ProvisionForRemovalCostCL(Enum):
    """"撤去費用引当金、流動負債"""
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class SurrenderValueOfInsurancePoliciesOpeCF(Enum):
    """"保険解約返戻金の受取額、営業活動によるキャッシュ・フロー"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class CollectionOfLoansReceivableFromSubsidiariesAndAffiliatesInvCF(Enum):
    """"関係会社貸付金の回収による収入、投資活動によるキャッシュ・フロー"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """


class CompensationForDamageNOE(Enum):
    """"損害賠償金、営業外費用"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """


class RestrictedStock(Enum):
    """"譲渡制限付株式報酬"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__CAPITAL_SURPLUS_MEMBER = 'CurrentYearDuration_CapitalSurplusMember'
    """ 当年度会計期間資本剰余金 """
    CURRENT_YEAR_DURATION__OTHER_CAPITAL_SURPLUS_MEMBER = 'CurrentYearDuration_OtherCapitalSurplusMember'
    """ 当年度会計期間その他資本剰余金 """
    CURRENT_YEAR_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'CurrentYearDuration_ShareholdersEquityMember'
    """ 当年度会計期間株主資本 """
    CURRENT_YEAR_DURATION__TREASURY_STOCK_MEMBER = 'CurrentYearDuration_TreasuryStockMember'
    """ 当年度会計期間自己株式 """


class LossOnDevelopmentOfSystemEL(Enum):
    """"システム開発に伴う損失、特別損失"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class LossOnDevelopmentOfSystemOpeCF(Enum):
    """"システム開発に伴う損失、営業活動によるキャッシュ・フロー"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class NondeductibleConsumptionTaxNOE(Enum):
    """"控除対象外消費税等、営業外費用"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class ProceedsFromPenaltyIncomeOpeCF(Enum):
    """"違約金の受取額、営業活動によるキャッシュ・フロー"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class AccumulatedDepreciationRightOfUseAssetsPPE(Enum):
    """"減価償却累計額、使用権資産、有形固定資産"""
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class CompensationForDamageNOE(Enum):
    """"損害賠償金、営業外費用"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class DividendsFromSurplusInterimDividends(Enum):
    """"剰余金の配当（中間配当）"""
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_BROUGHT_FORWARD_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_RetainedEarningsBroughtForwardMember'
    """ 当年度会計期間個別又は非連結繰越利益剰余金 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_RetainedEarningsMember'
    """ 当年度会計期間個別又は非連結利益剰余金 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__SHAREHOLDERS_EQUITY_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_ShareholdersEquityMember'
    """ 当年度会計期間個別又は非連結株主資本 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_BROUGHT_FORWARD_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_RetainedEarningsBroughtForwardMember'
    """ 個別又は非連結繰越利益剰余金 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_RetainedEarningsMember'
    """ 個別又は非連結利益剰余金 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_ShareholdersEquityMember'
    """ 個別又は非連結株主資本 """


class IncomeOfCompensationEI(Enum):
    """"受取賠償金、特別利益"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class RightOfUseAssetsPPE(Enum):
    """"使用権資産、有形固定資産"""
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class DisposalOfTreasurySharesByStockPaymentTrust(Enum):
    """"株式給付信託による自己株式の処分"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'CurrentYearDuration_ShareholdersEquityMember'
    """ 当年度会計期間株主資本 """
    CURRENT_YEAR_DURATION__TREASURY_STOCK_MEMBER = 'CurrentYearDuration_TreasuryStockMember'
    """ 当年度会計期間自己株式 """


class IncreaseDecreaseProvisionForLossOnStoreClosingOpeCF(Enum):
    """"閉店損失引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class ProvisionForLossOnStoreClosureCL(Enum):
    """"閉店損失引当金、流動負債"""
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class StockRelatedCostNOE(Enum):
    """"株式関連費、営業外費用"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class CompensationForDamageOpeCF(Enum):
    """"損害賠償金、営業活動によるキャッシュ・フロー"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class CompensationReceivedNOI(Enum):
    """"補償金収入、営業外収益"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class IncreaseDueToShareIssuance(Enum):
    """"株式交付による増加"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__CAPITAL_SURPLUS_MEMBER = 'CurrentYearDuration_CapitalSurplusMember'
    """ 当年度会計期間資本剰余金 """
    CURRENT_YEAR_DURATION__NON_CONTROLLING_INTERESTS_MEMBER = 'CurrentYearDuration_NonControllingInterestsMember'
    """ 当年度会計期間非支配株主持分 """
    CURRENT_YEAR_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'CurrentYearDuration_ShareholdersEquityMember'
    """ 当年度会計期間株主資本 """


class IncreaseInCashAndCashEquivalentsDueToShareIssuance(Enum):
    """"株式交付に伴う現金及び現金同等物の増加額"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class InsuranceReceivedNOI(Enum):
    """"保険金収入、営業外収益"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class LossOnAccidentEL(Enum):
    """"事故関連損失、特別損失"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class LossOnAccidentOpeCF(Enum):
    """"事故関連損失、営業活動によるキャッシュ・フロー"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class LossOnAccidentPaymentsOpeCF(Enum):
    """"事故関連損失の支払額、営業活動によるキャッシュ・フロー"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class PlantOfficeRebuildingExpensesEL(Enum):
    """"事業所建替関連費用、特別損失"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class PlantOfficeRebuildingExpensesOpeCF(Enum):
    """"事業所建替関連費用、営業活動によるキャッシュ・フロー"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class AmortizationOfCustomerRelationshipOpeCF(Enum):
    """"顧客関連資産償却額、営業活動によるキャッシュ・フロー"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """


class AmortizationOfLeaseDepositsOpeCF(Enum):
    """"敷金償却、営業活動によるキャッシュ・フロー"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """


class CustomerRelatedAssetAmortizationExpense(Enum):
    """"顧客関連資産償却額"""
    CURRENT_YEAR_DURATION__RECONCILING_ITEMS_MEMBER = 'CurrentYearDuration_ReconcilingItemsMember'
    """ 当年度会計期間調整項目 """
    CURRENT_YEAR_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'CurrentYearDuration_ReportableSegmentsMember'
    """ 当年度会計期間報告セグメント """
    CURRENT_YEAR_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'CurrentYearDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 当年度会計期間事業セグメント合計 """


class IncreaseDecreaseInOtherCurrentAssetsOpeCF(Enum):
    """"その他流動資産の増減額（△は増加）、営業活動によるキャッシュ・フロー"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """


class LossDueToInsuranceContractChangeNOE(Enum):
    """"保険契約変更による損失、営業外費用"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """


class LossDueToInsuranceContractChangeOpeCF(Enum):
    """"保険契約変更による損失、営業活動によるキャッシュ・フロー"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """


class RefundsDueToChangesInInsuranceContractInvCF(Enum):
    """"保険契約変更による返戻額、投資活動によるキャッシュ・フロー"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """


class RefundsDueToChangesInInsuranceContractNOI(Enum):
    """"保険契約変更による返戻金、営業外収益"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """


class RefundsDueToChangesInInsuranceContractOpeCF(Enum):
    """"保険契約変更による返戻金、営業活動によるキャッシュ・フロー"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """


class TransferCostFromSalesOfAssetsForRentOpeCF(Enum):
    """"賃貸資産の売却による原価振替高、営業活動によるキャッシュ・フロー"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class AllowanceForInvestmentEvaluationIOA(Enum):
    """"投資評価引当金、投資その他の資産"""
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class AllowanceForInvestmentLossNCL(Enum):
    """"投資損失引当金、固定負債"""
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class AmortizationOfGoodwillSegmentInformation(Enum):
    """"のれんの償却額、セグメント情報"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'CurrentYearDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ 当年度会計期間その他 """
    CURRENT_YEAR_DURATION__RECONCILING_ITEMS_MEMBER = 'CurrentYearDuration_ReconcilingItemsMember'
    """ 当年度会計期間調整項目 """
    CURRENT_YEAR_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'CurrentYearDuration_ReportableSegmentsMember'
    """ 当年度会計期間報告セグメント """
    CURRENT_YEAR_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'CurrentYearDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 当年度会計期間事業セグメント合計 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'Prior1YearDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    PRIOR1_YEAR_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1YearDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_YEAR_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'Prior1YearDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    PRIOR1_YEAR_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1YearDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """


class ImpairmentLossesSegmentInformation(Enum):
    """"減損損失、セグメント情報"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'CurrentYearDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ 当年度会計期間その他 """
    CURRENT_YEAR_DURATION__RECONCILING_ITEMS_MEMBER = 'CurrentYearDuration_ReconcilingItemsMember'
    """ 当年度会計期間調整項目 """
    CURRENT_YEAR_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'CurrentYearDuration_ReportableSegmentsMember'
    """ 当年度会計期間報告セグメント """
    CURRENT_YEAR_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'CurrentYearDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 当年度会計期間事業セグメント合計 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'Prior1YearDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    PRIOR1_YEAR_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1YearDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_YEAR_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'Prior1YearDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    PRIOR1_YEAR_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1YearDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """


class InformationSystemCostSGA(Enum):
    """"情報システム費、販売費及び一般管理費"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class ProvisionOfAllowanceForInvestmentEvaluationEL(Enum):
    """"投資評価引当金繰入額、特別損失"""
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class CollectionOfLeaseReceivablesInvCF(Enum):
    """"リース債権の回収による収入、投資活動によるキャッシュ・フロー"""
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class ProceedsFromCollectionOfLongTermAccountsReceivableOtherInvCFInvCF(Enum):
    """"長期未収入金の回収による収入、投資活動によるキャッシュ・フロー"""
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class CostOfNewBanknoteSupportEL(Enum):
    """"新紙幣対応費用、特別損失"""
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class TreasuryStockPaymentOfStockOwnershipPlanTrustChangesOfItemsDuringPeriod(Enum):
    """"株式給付信託による自己株式の交付、当期変動額"""
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__SHAREHOLDERS_EQUITY_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_ShareholdersEquityMember'
    """ 当年度会計期間個別又は非連結株主資本 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__TREASURY_STOCK_MEMBER = 'CurrentYearDuration_NonConsolidatedMember_TreasuryStockMember'
    """ 当年度会計期間個別又は非連結自己株式 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_ShareholdersEquityMember'
    """ 個別又は非連結株主資本 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__TREASURY_STOCK_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_TreasuryStockMember'
    """ 個別又は非連結自己株式 """


class IncreaseDecreaseInLongTermUnearnedRevenueOpeCF(Enum):
    """"長期前受収益の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class RentExpensesOfRealEstateForInvestmentNOE(Enum):
    """"投資不動産賃貸費用、営業外費用"""
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class IncreaseDecreaseInProvisionForCouponOpeCF(Enum):
    """"クーポン引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class IssuanceOfNewSharesRestrictedStock(Enum):
    """"新株の発行（譲渡制限付株式報酬）"""
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CAPITAL_STOCK_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_CapitalStockMember'
    """ 個別又は非連結資本金 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__CAPITAL_SURPLUS_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_CapitalSurplusMember'
    """ 個別又は非連結資本剰余金 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__LEGAL_CAPITAL_SURPLUS_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_LegalCapitalSurplusMember'
    """ 個別又は非連結資本準備金 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1YearDuration_NonConsolidatedMember_ShareholdersEquityMember'
    """ 個別又は非連結株主資本 """


class ProvisionForCouponCertificatesCL(Enum):
    """"クーポン引当金、流動負債"""
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class SettlementIncomeNOI(Enum):
    """"受取和解金、営業外収益"""
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class CustomerRelatedAssetsIA(Enum):
    """"顧客関連資産、無形固定資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class AdvancesReceivedOnUncompletedConstructionContractsAndOthersCNS(Enum):
    """"未成工事受入金等、建設業"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class PrepaymentGuaranteeFeeNOE(Enum):
    """"前払金保証料、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class GainOnForgivenessOfDebtsNOI(Enum):
    """"債務免除益、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class CancellationPenaltyOfRentAgreement(Enum):
    """"賃貸借契約解約違約金、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class CurrentPortionOfAccountReceivableLongterm(Enum):
    """"1年内回収予定の長期繰延営業債権"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class IncomeTaxesIncomeTaxes(Enum):
    """"法人税等、法人税等"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LongTermDeferredAccountsReceivable(Enum):
    """"長期繰延営業債権"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class LossOnRetirementOfNoncurrentAssetsAtCompanyOperatedRestaurantsNOE(Enum):
    """"店舗用固定資産除却損、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProvisionForBonusesNonCurrentNCL(Enum):
    """"賞与引当金、固定負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ProvisionForDirectorsBonusesNCL(Enum):
    """"役員賞与引当金、固定負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ReserveForLossOnDisposalOfInventoriesCL(Enum):
    """"棚卸資産処分損失引当金、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class LongTermAccountReceivableIOA(Enum):
    """"長期営業債権、投資その他の資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class StayCreditIOA(Enum):
    """"長期滞留債権、投資その他の資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class TheftLossEL(Enum):
    """"盗難損失、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class CryptocurrencyValuationLossNOE(Enum):
    """"暗号資産評価損、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProvisionForLossOnGuaranteesNOE(Enum):
    """"債務保証損失引当金繰入額、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class AccountsReceivableFromCompletedConstructionContractsAndContractAssetsCNS(Enum):
    """"完成工事未収入金及び契約資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ConsumptionTaxesForPriorPeriodsEI(Enum):
    """"過年度消費税等、特別利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProvisionForLossOnLeaseContractsCL(Enum):
    """"賃借契約損失引当金、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ProvisionForLossOnLeaseContractsNCL(Enum):
    """"賃借契約損失引当金、固定負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class AdjustmentOfHyperinflationCCE(Enum):
    """"超インフレの調整額、現金及び現金同等物"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnTheNetMonetaryPositionNOE(Enum):
    """"正味貨幣持高に関する損失、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnTheNetMonetaryPositionOpeCF(Enum):
    """"正味貨幣持高に関する損失、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LongTermAdvancePaymentsIOA(Enum):
    """"長期前渡金、投資その他の資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class DepositsReceivedFromSilentPartnershipNCL(Enum):
    """"匿名組合出資預り金、固定負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class CurrentPortionOfConvertibleBondTypeBondsWithShareAcquisitionRightsCL(Enum):
    """"1年内償還予定の転換社債型新株予約権付社債、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class IdleAssetExpensesNOE(Enum):
    """"遊休資産諸費用、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class AmortizationOfPatentRightNOE(Enum):
    """"特許権償却、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnTransferOfStocksOfSubsidiariesAndAffiliatesEL(Enum):
    """"関係会社株式譲渡損、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnValuationOfSoftwareEL(Enum):
    """"ソフトウエア評価損、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProvisionOfTheReserveForCapitalLossOfRelatedCompaniesEL(Enum):
    """"関係会社株式譲渡損失引当金繰入額、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProvisionForHeadOfficeRelocationExpensesCL(Enum):
    """"本社移転費用引当金、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class CompensationExpensesEL(Enum):
    """"支払経済補償金、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class AccountsReceivableTradeAndContractAssetsCA(Enum):
    """"売掛金及び契約資産、流動資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class AdjustmentOfPaymentNOE(Enum):
    """"支払精算金、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class TransferRestrictionsStocksBelongingToExpenditureRelatedNOE(Enum):
    """"譲渡制限付株式関連費用、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ConsumptionTaxDifferenceNOI(Enum):
    """"消費税差額、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class CostOfRealEstateRentalIncomeNOE(Enum):
    """"家賃原価、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class GuaranteeDeposited(Enum):
    """"預り保証金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class LossFromInvestmentPartnershipsNOE(Enum):
    """"投資事業組合損失、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class RealEstateRentalIncomeNOI(Enum):
    """"家賃収入、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class SecurityAndLeaseDepositsPaidIOA(Enum):
    """"差入保証金・敷金、投資その他の資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class IncomeFromPointCordNOI(Enum):
    """"ポイント収入額、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class BusinessExpenses(Enum):
    """"事業費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class BusinessRevenues(Enum):
    """"事業収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class BusinessStructuralReformExpensesEL(Enum):
    """"事業構造改革費用、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProvisionForBusinessRestructuringCL(Enum):
    """"事業構造改革引当金、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ResearchAndDevelopmentRevenuesRevOA(Enum):
    """"研究開発事業収益、営業活動による収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class RightOfUseAssetPPE(Enum):
    """"使用権資産、有形固定資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class PlantShutsdownRelatedCostsNOE(Enum):
    """"操業停止関連費用、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProvisionForLossOnSubleasesCL(Enum):
    """"転貸損失引当金、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ProvisionForLossOnSubleasesNCL(Enum):
    """"転貸損失引当金、固定負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class RefundLiabilitiesCL(Enum):
    """"返金負債、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class RestorationContributionIncomeNOI(Enum):
    """"原状回復負担金等収入、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class NonOperatingCommissionFeeNOE(Enum):
    """"営業外支払手数料、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class RevenueFromResearchAndDevelopmentRevOA(Enum):
    """"研究開発等収入、売上高"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class GainOnNetMonetaryPositionNOI(Enum):
    """"正味貨幣持高に係る利得、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnNetMonetaryPositionNOE(Enum):
    """"正味貨幣持高に係る損失、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class RevenueAdvertisingNOI(Enum):
    """"広告収入、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class RefundLiabilitiesCL(Enum):
    """"返金負債、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ARecallRelatedLossEL(Enum):
    """"製品回収関連損失、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ReserveForLossesRelatedToProductRecallCL(Enum):
    """"製品回収関連損失引当金、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class CustomerRelationAssets(Enum):
    """"顧客関係資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ProvisionForSalesReturn(Enum):
    """"損害賠償引当金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class RefundLiability(Enum):
    """"返金負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class AProductRepairReserveFundCL(Enum):
    """"製品改修引当金、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class LegalExpensesNOE(Enum):
    """"支払報酬、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnExtinguishmentShareBasedCompensationExpensesNOE(Enum):
    """"株式報酬費用消滅損、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class RefundsOnPriorPeriodsDividendsIncomeNOI(Enum):
    """"受取返還金、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class CompensationExpensesEL(Enum):
    """"支払補償費、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class CompensationForAbsenceFromWorkToEmployee(Enum):
    """"従業員休業補償損失、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class OtherRevenueSegment(Enum):
    """"その他の収益、セグメント"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'CurrentYTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    CURRENT_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'CurrentYTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1YTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1YTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """


class RevenueFromContractsWithCustomersSegment(Enum):
    """"顧客との契約から生じる収益、セグメント"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'CurrentYTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    CURRENT_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'CurrentYTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1YTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1YTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """


class SalesCompensationNOI(Enum):
    """"営業補償金、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ServicesAtTransferredAtAPointInTime(Enum):
    """"一時点で移転されるサービス"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'CurrentYTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    CURRENT_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'CurrentYTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1YTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1YTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """


class ServicesTransferredOverTime(Enum):
    """"一定の期間にわたり移転されるサービス"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'CurrentYTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    CURRENT_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'CurrentYTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1YTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1YTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """


class SpecialSurveyCostsEtcEL(Enum):
    """"特別調査費用等、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class CostOfElectricitySalesNOE(Enum):
    """"売電原価、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class RentalIncomeFromEmployeesBuildingsNOI(Enum):
    """"従業員受取家賃、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class BurdenChargeForDevelopmentNOI(Enum):
    """"開発負担金収入、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LandUseRightsIA(Enum):
    """"土地使用権、無形固定資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class LossOnCancellationOfMembershipEL(Enum):
    """"会員権解約損、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PostRetirementBenefitsPayableForDirectorsNCL(Enum):
    """"役員退職慰労未払金、固定負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class DecreaseIncreaseInMoneyHeldInTrustForPurchaseOfTreasuryStockFinCF(Enum):
    """"自己株式取得のための金銭の信託の増減額（△は増加）、財務活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DecreaseIncreaseInTradeReceivablesAndContractAssetsOpeCF(Enum):
    """"売上債権及び契約資産の増減額（△は増加）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class InsuranceIncomeNOIB(Enum):
    """"保険収入、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnRetirementOfIntangibleAssetsEL(Enum):
    """"無形固定資産除却損、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnSalesAndRetirementOfPropertyPlantAndEquipmentEL(Enum):
    """"有形固定資産除売却損、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class FactoryTransferExpensesNOE(Enum):
    """"工場移転費用、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class CompensationPaymentEL(Enum):
    """"支払補償金、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DecreaseIncreaseInDepositPaidForRepurchaseOfTreasuryStockFinCF(Enum):
    """"自己株式取得のための預け金の増減額（△は増加）、財務活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LeaseholdRightNCL(Enum):
    """"土地使用権、無形固定資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class GainOnSalesOfTrialPiecesNOI(Enum):
    """"試作品等売却代、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class BorrowingFeeNOE(Enum):
    """"借入手数料、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class CurrentPortionOfConvertibleBondTypeBondsWithShareAcquisitionRightsCL(Enum):
    """"１年内償還予定の転換社債型新株予約権付社債、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class CustomerRelatedAssetsIA(Enum):
    """"顧客関連資産、無形固定資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class StockRelatedCostNOE(Enum):
    """"株式関連費、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ExpensesForPurchasesOfGoodsNOE(Enum):
    """"物品購入費用、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromSalesOfGoodsNOI(Enum):
    """"物品売却収入、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class RentExpensesOnRealEstateForInvestmentsNOE(Enum):
    """"投資不動産賃貸費用、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnOverseasBusinessNOI(Enum):
    """"海外事業関連損失、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnProfitStructureImprovementInJapanEL(Enum):
    """"国内収益構造改善損、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnProfitStructureImprovementInOverseasEL(Enum):
    """"海外収益構造改善損、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class RelocationRelatedLossesEL(Enum):
    """"移転関連損失、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class RightOfUseAssetsIA(Enum):
    """"使用権資産、無形固定資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ProvisionForManagementBoardIncentivePlanTrust(Enum):
    """"役員株式給付引当金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ProvisionForStocksPayment(Enum):
    """"株式給付引当金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ContractLossAllowanceNCL(Enum):
    """"契約損失引当金、固定負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ContractLossEL(Enum):
    """"契約損失、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class GainOnReversalOfAllowanceForContractLossEI(Enum):
    """"契約損失引当金戻入額、特別利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProvisionForLossOnContractCL(Enum):
    """"契約損失引当金、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ProvisionOfAllowanceForContractLossEL(Enum):
    """"契約損失引当金繰入額、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class RentsNOE(Enum):
    """"地代家賃、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class GainOnAmortizationOfDepositsReceivedNOI(Enum):
    """"預り金償却益、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProvisionForLossOnGuaranteesForRentCL(Enum):
    """"保証履行引当金、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ProvisionForLossOnRelatedToRepairWorkCL(Enum):
    """"補修工事関連損失引当金、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ProvisionForLossOnRelatedToRepairWorkNCL(Enum):
    """"補修工事関連損失引当金、固定負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ProvisionForLossOnVacanciesNCL(Enum):
    """"空室損失引当金、固定負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ReversalOfProvisionForLossOnRelatedToRepairWorkEI(Enum):
    """"補修工事関連損失引当金戻入額、特別利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class InsuranceIncomeAroseFromDisasterEI(Enum):
    """"災害に伴う受取保険金、特別利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class TradeAndContractAssetsCA(Enum):
    """"売掛金及び契約資産、流動資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class BuildingsAndAccompanyingFacilitiesInTrustNetPPE(Enum):
    """"信託建物附属設備（純額）、有形固定資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class BuildingsInTrustNetPPE(Enum):
    """"信託建物（純額）、有形固定資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class EarthquakeResistantConstructionExpenseEL(Enum):
    """"耐震工事関連費用、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LandInTrustPPE(Enum):
    """"信託土地、有形固定資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class LongTermAdvancePaidIOA(Enum):
    """"長期立替金、投資その他の資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ProfitRelatedToEmploymentAdjustmentSubsidesEtcNOI(Enum):
    """"雇用調整助成金等、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class TradeNotesAndAccountsReceivableTradeAndContractAssetsCA(Enum):
    """"受取手形、営業未収入金及び契約資産、流動資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class GainOnReversalOfProvisionForLossOnBusinessWithdrawalEI(Enum):
    """"事業撤退損失引当金戻入額、特別利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProvisionForLossOnBusinessWithdrawalCL(Enum):
    """"事業撤退損失引当金、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ProvisionForLossOnBusinessWithdrawalEL(Enum):
    """"事業撤退損失引当金繰入額、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProvisionForNoncurrentAssetsRemovalCostCL(Enum):
    """"固定資産撤去費用引当金、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ProvisionForRemovalExpensesOfNoncurrentAssetsEL(Enum):
    """"固定資産撤去費用引当金繰入額、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class InvestmentPartnershipManagementFeeNOE(Enum):
    """"投資事業組合管理費、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ClaimsProvableInBankruptcyClaimsProvableInRehabilitationAndOtherIOA(Enum):
    """"破産債権等に準ずる債権、投資その他の資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class CommissionIncomeNOI(Enum):
    """"手数料収入、営業外収益"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class CompensationForDamagesReceivedNOI(Enum):
    """"受取損害賠償金、営業外収益"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class IdleAssetsExpenseNOE(Enum):
    """"遊休資産費用、営業外費用"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class MaterialProfitOnSaleNOI(Enum):
    """"資材売却益、営業外収益"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class ProvisionForBuildingDemolitionExpenseNCL(Enum):
    """"建物解体費用引当金、固定負債"""
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class ProvisionOfAllowanceForBuildingDemolitionExpense(Enum):
    """"建物解体費用引当金繰入額、特別損失"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class SupportingExpensesForSubsidiariesAndAffiliatesNOE(Enum):
    """"関係会社支援費用、営業外費用"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class VariousFacilitiesUseRightsIA(Enum):
    """"諸施設利用権、無形固定資産"""
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class AccountsReceivableTradeAndContractAssetsCA(Enum):
    """"売掛金及び契約資産、流動資産"""
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class CashBackIncomeNOI(Enum):
    """"キャッシュバック収入、営業外収益"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class GainOnForgivenessOfDebtsNOI(Enum):
    """"債務免除益、営業外収益"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class PastFiscalYearsConsumptionTaxEtcNOI(Enum):
    """"過年度消費税等、営業外収益"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class HandicappedEmploymentLevyNOE(Enum):
    """"障害者雇用納付金、営業外費用"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class LossOnAntiMonopolyActEL(Enum):
    """"独占禁止法関連損失、特別損失"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class OperatingProfitLossOperatingProfitLoss(Enum):
    """"営業損失（△）、営業利益又は営業損失（△）"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember_TotalOfReportableSegmentsAndOthersMember'
    """ 個別又は非連結事業セグメント合計 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember_TotalOfReportableSegmentsAndOthersMember'
    """ 個別又は非連結事業セグメント合計 """


class SalesCommissionNOI(Enum):
    """"販売手数料、営業外収益"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class AmortizationOfRestrictedStockRemunerationNOE(Enum):
    """"譲渡制限付株式報酬償却損、営業外費用"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class BusinessRevenue(Enum):
    """"事業収益"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER__RECONCILING_ITEMS_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember_ReconcilingItemsMember'
    """ 個別又は非連結調整項目 """
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER__REPORTABLE_SEGMENTS_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember_ReportableSegmentsMember'
    """ 個別又は非連結報告セグメント """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER__RECONCILING_ITEMS_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember_ReconcilingItemsMember'
    """ 個別又は非連結調整項目 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER__REPORTABLE_SEGMENTS_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember_ReportableSegmentsMember'
    """ 個別又は非連結報告セグメント """


class CostOfBusinessRevenue(Enum):
    """"事業原価"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class LectureSFeeIncomeNOI(Enum):
    """"講演料等収入、営業外収益"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class SubsidyIncomeEtcNOI(Enum):
    """"助成金等収入、営業外収益"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class TotalBusinessExpenses(Enum):
    """"事業費用合計"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class TradeReceivablesAndContractAssetCA(Enum):
    """"売掛金及び契約資産、流動資産"""
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class AmortizationOfRestrictedStockRemunerationNOE(Enum):
    """"譲渡制限付株式報酬償却、営業外費用"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class TransportationIncomeNOI(Enum):
    """"受取運送料、営業外収益"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class GainOnSalesOfRawMaterialsNOI(Enum):
    """"原材料売却益、営業外収益"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class LossOnExtinguishmentOfShareBasedRemunerationExpensesNOE(Enum):
    """"株式報酬費用消滅損、営業外費用"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class SalesEngineeringExpensesSGA(Enum):
    """"受注前活動費、販売費及び一般管理費"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class AccountsReceivableTradeAndContractAssetsCA(Enum):
    """"売掛金及び契約資産、流動資産"""
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class ReceivedIncentiveNOI(Enum):
    """"受取報奨金、営業外収益"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class GoodsTransferAtAPointInTime(Enum):
    """"一時点で移転される財"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER__OTHER_REPORTABLE_SEGMENTS_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember_OtherReportableSegmentsMember'
    """ 個別又は非連結その他 """
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER__RECONCILING_ITEMS_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember_ReconcilingItemsMember'
    """ 個別又は非連結調整項目 """
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER__REPORTABLE_SEGMENTS_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember_ReportableSegmentsMember'
    """ 個別又は非連結報告セグメント """
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember_TotalOfReportableSegmentsAndOthersMember'
    """ 個別又は非連結事業セグメント合計 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER__RECONCILING_ITEMS_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember_ReconcilingItemsMember'
    """ 個別又は非連結調整項目 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER__REPORTABLE_SEGMENTS_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember_ReportableSegmentsMember'
    """ 個別又は非連結報告セグメント """


class GoodsTransferOverTime(Enum):
    """"一定の期間にわたり移転される財"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER__OTHER_REPORTABLE_SEGMENTS_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember_OtherReportableSegmentsMember'
    """ 個別又は非連結その他 """
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER__RECONCILING_ITEMS_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember_ReconcilingItemsMember'
    """ 個別又は非連結調整項目 """
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER__REPORTABLE_SEGMENTS_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember_ReportableSegmentsMember'
    """ 個別又は非連結報告セグメント """
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember_TotalOfReportableSegmentsAndOthersMember'
    """ 個別又は非連結事業セグメント合計 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER__RECONCILING_ITEMS_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember_ReconcilingItemsMember'
    """ 個別又は非連結調整項目 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER__REPORTABLE_SEGMENTS_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember_ReportableSegmentsMember'
    """ 個別又は非連結報告セグメント """


class TenderOfferRelatedExpensesEL(Enum):
    """"公開買付関連費用、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DecreaseIncreaseInDepositPaidForRepurchaseOfTreasuryStockFinCF(Enum):
    """"自己株式取得のための預け金の増減額（△は増加）、財務活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DecreaseIncreaseInDepositsPaidInvCF(Enum):
    """"預け金の増減額（△は増加）、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInProvisionForMineClosureExpensesOpeCF(Enum):
    """"閉山損失引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProductCompensationLossEL(Enum):
    """"製品補償損失、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProductCompensationLossOpeCF(Enum):
    """"製品補償損失、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProvisionForMineClosureExpensesNCL(Enum):
    """"閉山損失引当金、固定負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class BusinessRestructuringExpensesEL(Enum):
    """"事業構造改革費用、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class CompensationForDamageIncomeEI(Enum):
    """"受取損害賠償金、特別利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class E00322000InsuranceReturnEI(Enum):
    """"保険返戻金、特別利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class UnemployedCapitalCostNOE(Enum):
    """"遊休資産費用、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ConstructionGuaranteeFeeNOE(Enum):
    """"工事保証料、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class AccountsPayableForConstructionContractsAndOtherCLCNS(Enum):
    """"工事未払金等、流動負債、建設業"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class AccountsReceivableFromCompletedConstructionContractsAndOtherCNS(Enum):
    """"完成工事未収入金等、建設業"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class CostOfTransportationBusinessCOS(Enum):
    """"運輸事業売上原価、売上原価"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class GrossProfitOnTransportationBusinessGP(Enum):
    """"運輸事業総利益、売上総利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProvisionForLossOnLitigationNOE(Enum):
    """"訴訟損失引当金繰入額、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class SalesOfTransportationBusinessNetSales(Enum):
    """"運輸事業売上高、売上高"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ContractAssetsCA(Enum):
    """"契約資産、流動資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class PatentEnforcementIncomNOI(Enum):
    """"特許実施収入、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class RepaymentsOfInstallmentPayablesAndLeaseObligationsFinCF(Enum):
    """"割賦債務及びリース債務の返済による支出、財務活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class CostsOnRealEstateBusinessAndOtherCA(Enum):
    """"不動産事業等支出金、流動資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class IncreaseDecreaseInProvisionForLossOnRealEstateBusinessAndOtherOpeCF(Enum):
    """"不動産事業等損失引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnSupportToSubsidiariesEL(Enum):
    """"子会社支援損、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProvisionForLossOnRealEstateBusinessAndOtherCL(Enum):
    """"不動産事業等損失引当金、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class IncreaseDecreaseInNetDefinedBenefitAssetOrLiabilityOpeCF(Enum):
    """"退職給付に係る資産又は負債の増減額、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class NotesAndAccountsReceivableFromCompletedConstructionContractsAndContractAssetsCNS(Enum):
    """"受取手形、完成工事未収入金等及び契約資産、建設業"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class FinancialCommissionNOE(Enum):
    """"金融手数料、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class NonDeductedConsumptionTaxNOE(Enum):
    """"控除対象外消費税等、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class NotesReceivableAccountsReceivableFromCompletedConstructionContractsContractAssetsAndOther(Enum):
    """"受取手形・完成工事未収入金及び契約資産等"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ProvisionForLossOnCompensationForDamageEL(Enum):
    """"損害補償損失引当金繰入、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LicenseIncomeNOI(Enum):
    """"特許関連収入、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class CompensationForDamageNOE(Enum):
    """"損害賠償金、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class Animals(Enum):
    """"動物"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class CommissionExpensesPaidFinCF(Enum):
    """"支払手数料の支払額、財務活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class HeadOfficeRelocationExpensesOpeCF(Enum):
    """"本社移転費用、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnClosingOfFactoryEL(Enum):
    """"工場閉鎖損失、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PaymentsForHeadOfficeRelocationExpensesOpeCF(Enum):
    """"本社移転費用の支払額、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class StockpileStorageRevenueNOI(Enum):
    """"備蓄保管収入、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromStateSubsidyInvCF(Enum):
    """"国庫補助金等の受入による収入、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class RepaymentsOfDepositsReceivedInvCF(Enum):
    """"預り敷金の返還による支出、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class BountyOnEstablishmentOfNewBusinessFacilitiesNOI(Enum):
    """"企業立地奨励金、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class BountyOnEstablishmentOfNewBusinessFacilitiesOpeCF(Enum):
    """"企業立地奨励金、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class BountyOnEstablishmentOfNewBusinessFacilitiesReceivedOpeCF(Enum):
    """"企業立地奨励金の受取額、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProvisionForNoncurrentAssetsRemovalCostNCL(Enum):
    """"固定資産撤去費用引当金、固定負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class RemovalLossOfPropertyPlantAndEquipmentInvCF(Enum):
    """"固定資産撤去に伴う支出、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class CompensationIncomeReceivedOpeCF(Enum):
    """"受取補償金の受取額、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInProvisionForOfficersRetirementBenefitsOpeCF(Enum):
    """"執行役員退職慰労引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProvisionForOfficerRetirementBenefits(Enum):
    """"執行役員退職慰労引当金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class DisbursementToTheHIKARIFoundationEL(Enum):
    """"公益財団法人ひかり協会負担金、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossRelatedToRebuildingEL(Enum):
    """"建替関連損失、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class CostsRelatedToVoluntaryRecoveryOfProductEL(Enum):
    """"製品自主回収関連費用、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProvisionForRestructualReformsCL(Enum):
    """"構造改革引当金、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class RestructuringExpensesEL(Enum):
    """"構造改革費用、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class RestructuringExpensesOpeCF(Enum):
    """"構造改革費用、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DecreaeIncreaseInDefferedConsumerTaxOpeCF(Enum):
    """"繰延消費税等の増減額（△は増加）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ExpensesRelatedToTheProposedTenderOfferEL(Enum):
    """"公開買付提案対応費用、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class TVExhibitionRightsAndVideogramRights(Enum):
    """"映像使用権"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class AccumulatedDepreciationAssetsForRentPPE(Enum):
    """"減価償却累計額、賃貸資産、有形固定資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class AssetsForRentNetPPE(Enum):
    """"賃貸資産（純額）、有形固定資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class AssetsForRentPPE(Enum):
    """"賃貸資産、有形固定資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class GainOnSalesOfScrapNOI(Enum):
    """"スクラップ売却収入、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnRetirementOfAssetsForRentOpeCF(Enum):
    """"賃貸資産除却に伴う原価振替額、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnSalesOfAssetsForRentOpeCF(Enum):
    """"賃貸資産売却に伴う原価振替額、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class AccountsReceivableTradeAndContractAssetsCA(Enum):
    """"売掛金及び契約資産、流動資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class GainOnExemptionOfConsumptionTaxesNOI(Enum):
    """"消費税等免税益、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class CustomerRelatedAssetsOfGoodwillOpeCF(Enum):
    """"顧客関連資産償却額、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnValuationOfInvestmentSecuritiesOpeCF(Enum):
    """"投資有価証券評価損、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class RefundLiabilitiesCL(Enum):
    """"返金負債、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class IncreaseDecreaseInLiquorTaxesPayableOpeCF(Enum):
    """"未払酒税の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProvisionForLossOnLitigationNOE(Enum):
    """"訴訟損失引当金繰入額、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossGainOnSaleOfInvestmentsInCapitalOfSubsidiariesAndAssociatesOpeCF(Enum):
    """"関係会社出資金売却損益（△は益）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnSaleOfInvestmentsInCapitalOfSubsidiariesAndAssociatesEL(Enum):
    """"関係会社出資金売却損、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PaymentsForSalesOfInvestmentsInCapitalOfSubsidiariesAndAffiliatesResultingInChangeInScopeOfConsolidationInvCF(Enum):
    """"連結の範囲の変更を伴う関係会社出資金の売却による支出、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class AProductRepairReserveFundCL(Enum):
    """"製品改修引当金、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class IncreaseDecreaseInAProductRepairReserveFundOpeCF(Enum):
    """"製品改修引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class RefundedTaxesNOI(Enum):
    """"還付税金、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class RefundedTaxesOpeCF(Enum):
    """"還付税金、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class CashOverAndShortNOE(Enum):
    """"現金過不足、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PaymentsForRepairOpeCF(Enum):
    """"補修費用に伴う支払額、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class BorrowingRelatedExpensesLossesNOE(Enum):
    """"借入関係費用、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class NondeductibleConsumptionTaxNOE(Enum):
    """"控除対象外消費税等、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class AdvancesReceivedDepositsNOE(Enum):
    """"前受金保証料、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class AutomotiveSafetySystemsBusinessDivisionRevOA(Enum):
    """"自動車安全部品、営業活動による収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'CurrentYTDDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    CURRENT_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'CurrentYTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    CURRENT_YTD_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'CurrentYTDDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    CURRENT_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'CurrentYTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'Prior1YTDDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    PRIOR1_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1YTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_YTD_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'Prior1YTDDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    PRIOR1_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1YTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """


class DisasterPreventionDivisionRevOA(Enum):
    """"防災、営業活動による収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'CurrentYTDDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    CURRENT_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'CurrentYTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    CURRENT_YTD_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'CurrentYTDDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    CURRENT_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'CurrentYTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'Prior1YTDDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    PRIOR1_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1YTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_YTD_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'Prior1YTDDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    PRIOR1_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1YTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """


class IncreaseDecreaseInNetDefinedBenefitAssetOrLiabilityOpeCF(Enum):
    """"退職給付に係る資産負債の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IndustrialMaterialsDivisionRevOA(Enum):
    """"産業資材、営業活動による収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'CurrentYTDDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    CURRENT_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'CurrentYTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    CURRENT_YTD_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'CurrentYTDDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    CURRENT_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'CurrentYTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'Prior1YTDDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    PRIOR1_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1YTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_YTD_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'Prior1YTDDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    PRIOR1_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1YTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """


class LossOnProductCompensationEL(Enum):
    """"製品補償対策費、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class OtherBusinessesDivisionRevOA(Enum):
    """"その他"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'CurrentYTDDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    CURRENT_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'CurrentYTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    CURRENT_YTD_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'CurrentYTDDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    CURRENT_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'CurrentYTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'Prior1YTDDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    PRIOR1_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1YTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_YTD_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'Prior1YTDDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    PRIOR1_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1YTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """


class OtherRevenue(Enum):
    """"その他の収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'CurrentYTDDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    CURRENT_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'CurrentYTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    CURRENT_YTD_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'CurrentYTDDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    CURRENT_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'CurrentYTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'Prior1YTDDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    PRIOR1_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1YTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_YTD_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'Prior1YTDDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    PRIOR1_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1YTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """


class PALTEMDivisionRevOA(Enum):
    """"パルテム、営業活動による収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'CurrentYTDDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    CURRENT_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'CurrentYTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    CURRENT_YTD_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'CurrentYTDDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    CURRENT_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'CurrentYTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'Prior1YTDDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    PRIOR1_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1YTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_YTD_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'Prior1YTDDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    PRIOR1_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1YTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """


class ProductWarrantyLossEL(Enum):
    """"製品保証損失、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class RevenueFromContractsWithCustomersRevOA(Enum):
    """"顧客との契約から生じる収益、営業活動による収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'CurrentYTDDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    CURRENT_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'CurrentYTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    CURRENT_YTD_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'CurrentYTDDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    CURRENT_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'CurrentYTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'Prior1YTDDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    PRIOR1_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1YTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_YTD_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'Prior1YTDDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    PRIOR1_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1YTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """


class DismantlementRelatedExpensesEL(Enum):
    """"解体撤去関連費用、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class GoodOutputCA(Enum):
    """"完成品、流動資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class NondeductibleConsumptionTaxNOE(Enum):
    """"控除対象外消費税等、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PaymentOfDemolitionAndRemovalCostsOpeCF(Enum):
    """"解体撤去関連費用の支払額、営業活動によるキャッシュフロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PaymentsForFactoryTransferExpensesOpeCF(Enum):
    """"工場移転費用の支払額、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ContentsAssetsCA(Enum):
    """"コンテンツ資産、流動資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ProvisionForShareBasedCompensation(Enum):
    """"株式報酬引当金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class RevenueFromUnusedPointByWithdrawalFromMembershipNOI(Enum):
    """"退会者未使用課金収益、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class WorkInProcessContentsAssetsCA(Enum):
    """"仕掛コンテンツ資産、流動資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class DirectorsShareBasedAllowancesNCL(Enum):
    """"役員株式報酬引当金、固定負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class DirectorsShareBasedAllowancesSGA(Enum):
    """"役員株式報酬引当金繰入額、販売費及び一般管理費"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInDirectorsShareBasedAllowancesOpeCF(Enum):
    """"役員株式報酬引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProvisionForHeadOfficeRelocationExpensesCL(Enum):
    """"本社移転費用引当金、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ContentsAssetsIA(Enum):
    """"コンテンツ資産、無形固定資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class MoneyHeldInTrustIOA(Enum):
    """"金銭の信託、投資その他の資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ProceedsFromDisposalOfTreasurySharesFromExerciseOfShareAcquisitionRightsFinCF(Enum):
    """"新株予約権の行使による自己株式の処分による収入、財務活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromLongTermDepositsReceivedFinCF(Enum):
    """"長期預り金の受入による収入、財務活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class AccountsReceivableAndContractAssetsCA(Enum):
    """"売掛金及び契約資産、流動資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class OfficeRelocationExpensesOpeCF(Enum):
    """"事務所移転費用、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInRefundLiabilityOpeCF(Enum):
    """"返金負債の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class RefundLiability(Enum):
    """"返金負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class TrialProductsIncomeNOI(Enum):
    """"試作品売却収入、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class CashBackIncomeNOI(Enum):
    """"キャッシュバック収入、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class AccountsReceivableTradeAndContractAssetsCA(Enum):
    """"売掛金及び契約資産、流動資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class GainOnReversalOfAssetRetirementObligationsOpeCF(Enum):
    """"資産除去債務戻入益、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class GainOnSaleOfCryptoAssetsNOI(Enum):
    """"暗号資産売却益、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossGainOnSaleOfCryptoAssetsOpeCF(Enum):
    """"暗号資産売却益、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossGainOnValuationOfCryptocurrencyOpeCF(Enum):
    """"暗号資産評価損益（△は益）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnLiquidationOfInvestmentSecuritiesEL(Enum):
    """"投資有価証券清算損、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnLiquidationOfInvestmentSecuritiesOpeCF(Enum):
    """"投資有価証券清算損、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnValuationOfCryptoAssetsNOE(Enum):
    """"暗号資産評価損、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromSalesOfCryptoAssetsInvCF(Enum):
    """"暗号資産の売却による収入、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class GainOnReversalOfAssetRetirementObligationsNOI(Enum):
    """"資産除去債務戻入益、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class FinancialCommissionNOE(Enum):
    """"金融手数料、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class GainOnSalesOfRawMaterialsNOI(Enum):
    """"原材料売却益、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ReserveForImplementationOfEnvironmentalAndSafetyArrangementNCL(Enum):
    """"環境安全整備引当金、固定負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ReserveForImplementationOfEnvironmentalAndSafetyArrangementsOpeCF(Enum):
    """"環境安全整備引当金の増減額(△は減少)、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class CostDuringTheSuspensionOfPlantOperationNOE(Enum):
    """"操業休止等経費、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class CompensationExpensesEL(Enum):
    """"支払補償費、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PaymentsForIssuanceOfBondsFinCF(Enum):
    """"社債の発行による支出、財務活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class TenderOfferRelatedExpensesNOE(Enum):
    """"公開買付関連費用、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromCancellationOfLifeInsuranceFundsInvCF(Enum):
    """"生命保険積立金の解約による収入、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PurchaseOfInsuranceFunds(Enum):
    """"生命保険積立金の積立による支出"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnClosingOfPlantEL(Enum):
    """"工場閉鎖損失、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnCompensationOfClaimsNOE(Enum):
    """"クレーム弁償損、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInProvisionForLossCompensationOpeCF(Enum):
    """"損害補償損失引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProvisionForLossCompensationCL(Enum):
    """"損害補償損失引当金、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ProvisionForLossCompensationNOE(Enum):
    """"損害補償損失引当金繰入額、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PersonnelExpensesForSecondedEmployeesNOE(Enum):
    """"出向者労務費差額負担、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class FixedAssetRemovalCostsOpeCF(Enum):
    """"固定資産撤去費用、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInRefundLiabilitiesOpeCF(Enum):
    """"返金負債の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnRemovalOfNoncurrentAssetsNOE(Enum):
    """"固定資産撤去費用、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProvisionForAssetsRemovalNCLLiabilities(Enum):
    """"固定資産撤去引当金、固定負債、負債の部"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class RepaymentsOfLongTermDepositsReceivedFinCF(Enum):
    """"長期預り金の返還による支出、財務活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class AccountReceivableMedicalIncomeCA(Enum):
    """"調剤報酬等購入債権、流動資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class AccountReceivableMonetizationOfReceivableCA(Enum):
    """"債権売却未収入金、流動資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class DecreaseIncreaseInAccountReceivableMedicalIncomeOpeCF(Enum):
    """"調剤報酬等購入債権の増減額（△は増加）、営業活動によるキャッシュフロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DecreaseIncreaseInAccountReceivableOpeCF(Enum):
    """"債権売却未収入金の増減額（△は増加）、営業活動によるキャッシュフロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class CommunicationLineIA(Enum):
    """"通信回線使用権、無形固定資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class IncreaseDecreaseInUnrealizedGainOnDeferredRevenueOpeCF(Enum):
    """"繰延延払利益の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class InterestAndIncomeOpeCF(Enum):
    """"受取利息及び配当金、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PaymentForGuaranteeDepositsInvCF(Enum):
    """"保証金の差入による支出、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromCollectionOfGuaranteeDepositsFinCF(Enum):
    """"保証金の返戻による収入、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class UnrealizedGainOnDeferredRevenueCL(Enum):
    """"繰延延払利益、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class BonusesAndProvisionForBonusesSGA(Enum):
    """"賞与及び賞与引当金繰入額、販売費及び一般管理費"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class InProcessResearchAndDevelopmentIA(Enum):
    """"仕掛研究開発、無形固定資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class IncreaseDecreaseInRetirementBenefitAssetAndLiabilityOpeCF(Enum):
    """"退職給付に係る資産負債の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class NetSalesOfFinishedGoodsAndMerchandise(Enum):
    """"商品及び製品の販売"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'CurrentYTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    CURRENT_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'CurrentYTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1YTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1YTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """


class OtherIncome(Enum):
    """"その他の収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'CurrentYTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    CURRENT_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'CurrentYTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1YTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1YTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """


class Royalty(Enum):
    """"製品の販売等に関するライセンス契約"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'CurrentYTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    CURRENT_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'CurrentYTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1YTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1YTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """


class CustomerRelatedIntangibleAssetsIA(Enum):
    """"顧客関連無形資産、無形固定資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class PaymentsOfContingentConsiderationForSharesOfSubsidiariesInvCF(Enum):
    """"子会社株式の条件付取得対価の支払額、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProvisionForCompensationLossNCL(Enum):
    """"補償損失引当金、固定負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ReversalOfProvisionForCompensationLossEL(Enum):
    """"補償損失引当金戻入額、特別利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ReversalOfProvisionForCompensationLossOpeCF(Enum):
    """"補償損失引当金戻入額、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class BusinessStructureImprovementExpensesNOE(Enum):
    """"事業構造改善費用、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class CompensationIncomeForDamageNOI(Enum):
    """"受取賠償金、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class BusinessExpenses(Enum):
    """"事業費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class BusinessRevenue(Enum):
    """"事業収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class RepaymentsToShareAcquisitionRightsFinCF(Enum):
    """"自己新株予約権の取得による支出、財務活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class AmendsForProductWarrantiesCL(Enum):
    """"製品補償引当金、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class IncreaseDecreaseInAmendsForProduct(Enum):
    """"製品補償引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInNetDefinedBenefitAssetLiabilityOpeCF(Enum):
    """"退職給付に係る資産負債の増減額、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PaymentsOfLossRelatedToQualityOpeCF(Enum):
    """"品質関連損失の支払額、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProductAmendsDrawingNOE(Enum):
    """"製品補償引当金繰入額、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnNetMonetaryPositionNOE(Enum):
    """"正味貨幣持高に係る損失、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromPaymentsForDerivativeSettlementNetInvCF(Enum):
    """"デリバティブ決済による収支（純額）、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ReversalOfImpairmentLossEI(Enum):
    """"減損損失戻入益、特別利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ReversalOfImpairmentLossOpeCF(Enum):
    """"減損損失戻入益、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class SegmentProfitSegmentInformation(Enum):
    """"セグメント利益、セグメント情報"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'CurrentYTDDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    CURRENT_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'CurrentYTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    CURRENT_YTD_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'CurrentYTDDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    CURRENT_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'CurrentYTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'Prior1YTDDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    PRIOR1_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1YTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_YTD_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'Prior1YTDDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    PRIOR1_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1YTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """


class DecreaseIncreaseInLongtermAccountsReceivableOtherOpeCF(Enum):
    """"長期未収入金の増減額（△は増加）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ShareholderBenefitProgramExpenseNOE(Enum):
    """"株主優待費用、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnOperationOfInvestmentNOE(Enum):
    """"投資運用損、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class GainOnForfeitureOfUnclaimedDividends(Enum):
    """"除斥配当金受入益、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LongTermAccountReceivableFixedAssets(Enum):
    """"滞留債権、投資その他の資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class FiduciaryObligationIncomeNOI(Enum):
    """"業務受託収入、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class OfficeRenovationExpensesEL(Enum):
    """"事務所改装費用、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProvisionForBadDebtsBonusesAndRetirementExpensesSGA(Enum):
    """"引当金繰入額、販売費及び一般管理費"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PurchaseOfOtherPropertyInvCF(Enum):
    """"その他償却資産の取得による支出、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseOrDecreaseInRefundLiabilitiesOpeCF(Enum):
    """"返金負債の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseOrDecreaseInReturnedAssetsOpeCF(Enum):
    """"返品資産の増減額（△は増加）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class RefundLiabilityCL(Enum):
    """"返金負債、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ReturnedAssetsCA(Enum):
    """"返品資産、流動資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class RightOfUseAssetPPE(Enum):
    """"使用権資産（純額）、有形固定資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class CustomerRelationshipIA(Enum):
    """"顧客関連資産、無形固定資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class TechnicalAssetsIA(Enum):
    """"技術資産、無形固定資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class AccruedGasolineTax(Enum):
    """"未払揮発油税"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class IncreaseDecreaseInAccruedGasolineTaxOpeCF(Enum):
    """"未払揮発油税の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PaymentsForSalesOfSharesOfSubsidiariesResultingInChangeInScopeOfConsolidationInvCF(Enum):
    """"連結範囲の変更を伴う子会社株式の売却による支出、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class RentOfOilTanks(Enum):
    """"タンク賃借料"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class RentalIncomeOfOilTanks(Enum):
    """"タンク賃貸料"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class RepaymentOfTheExaminationByTheRegionalTaxationBureauEL(Enum):
    """"国税局調査に基づく返納金、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class StorageTanksNet(Enum):
    """"油槽（純額）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class GainOnReversalOfProvisionForLossOnBusinessWithdrawalEI(Enum):
    """"事業撤退損失引当金戻入額、特別利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProvisionForLossOnBusinessWithdrawalCL(Enum):
    """"事業撤退損失引当金、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class LongTermDepositIOA(Enum):
    """"長期性預金、投資その他の資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class TenderOfferRelatedExpensesNOE(Enum):
    """"公開買付関連費用、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class RemeasurementsOfDefinedBenefitPlansOCI(Enum):
    """"退職給付に係る調整額、その他の包括利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class CashDividendsPaidByParentCompanyFinCF(Enum):
    """"親会社による配当金の支払額、財務活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ExpensesOfVoluntaryRecallOfProductsEL(Enum):
    """"製品自主回収関連費用、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class FeeOnSalesOfNotesPayableNOE(Enum):
    """"手形売却費、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class GainOnReversalOfForeignCurrencyTranslationAdjustmentEI(Enum):
    """"為替換算調整勘定取崩益、特別利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class GainOnReversalOfForeignCurrencyTranslationAdjustmentOpeCF(Enum):
    """"為替換算調整勘定取崩益、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInProvisionForLiquidationOfSubsidiariesLosses2OpeCF(Enum):
    """"関係会社清算損失引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInProvisionForProductCompensationOpeCF(Enum):
    """"製品補償引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LitigationLossEI(Enum):
    """"訴訟損失、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProvisionForLossOnClosingSubsidiariesAndAffiliatesCL(Enum):
    """"関係会社清算損失引当金、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ProvisionForProductCompensationCL(Enum):
    """"製品補償引当金、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class IncreaseDecreaseInGuaranteeDepositedFinCF(Enum):
    """"預り保証金の純増減額（△は減少）、財務活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInProvisionForSpecialCompensationOpeCF(Enum):
    """"従業員特別補償引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class OperatingAccountsReceivableNetAmountCA(Enum):
    """"営業未収入金（純額）、流動資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ProvisionForEmployeeSpecialAmendsNCL(Enum):
    """"従業員特別補償引当金、固定負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ProvisionForSpecialCompensationsEL(Enum):
    """"従業員特別補償引当金繰入額、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class RefundIncomeNOI(Enum):
    """"還付金収入、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DisasterRepairExpensesNOE(Enum):
    """"災害修繕費、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInProvisionForEmployeeStockOwnershipPlanTrustOpeCF(Enum):
    """"従業員株式給付引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProvisionForEmployeeStockOwnershipPlanTrustNCL(Enum):
    """"従業員株式給付引当金、固定負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ListingFeesNOE(Enum):
    """"上場賦課金、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PaymentsOfLossOnWorkplaceClosingOpeCF(Enum):
    """"事業所閉鎖損失の支払額、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProvisionForLossOnWorkplaceClosingCL(Enum):
    """"事業所閉鎖損失引当金、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class CustomerRelationshipIA(Enum):
    """"顧客関連資産、無形固定資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class DividendsIncomeReceivedInProportionToTransactionsWithPartnershipNOI(Enum):
    """"利用分量配当金、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnCancellationOfMembershipEL(Enum):
    """"会員権解約損、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnCancellationOfMembershipOpeCF(Enum):
    """"会員権解約損、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedFromDisposalOfIronScrapsNOI(Enum):
    """"鉄屑処分収入、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class AccruedLiabilityForFactoring(Enum):
    """"ファクタリング未払金、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class DecreaseIncreaseInDepositsForPurchaseOfTreausurySharesFinCF(Enum):
    """"自己株式取得のための預託金の増減額(△は増加)、財務活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LongTermSuspenseReceiptNCL(Enum):
    """"長期仮受金、固定負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ShareBasedPaymentExpensesEL(Enum):
    """"株式報酬費用、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ForeignWithholdingTaxNOE(Enum):
    """"外国源泉税、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProvisionForLossContractNCL(Enum):
    """"契約損失引当金、固定負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ProvisionOfRestorationCostCL(Enum):
    """"復旧費用引当金、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ProvisionOfRestorationCostNCL(Enum):
    """"復旧費用引当金、固定負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class GainOnNonCurrentAssetsRentNOI(Enum):
    """"固定資産賃貸益、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnInappropriateConductInQualityInspectionsEL(Enum):
    """"品質不適切行為関連損失、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProvisionForBusinessRestructureCL(Enum):
    """"事業再構築引当金、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ProvisionForLossOnWindPowerGeneratorBusinessCL(Enum):
    """"風力事業損失引当金、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class CompensationExpensesEL(Enum):
    """"支払補償金、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PaymentAmountOfCompensationOpeCF(Enum):
    """"支払補償金の支払額、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PaymentCompensationOpeCF(Enum):
    """"支払補償金、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class AccumulatedDepreciationLandUsedForMiningOperations(Enum):
    """"減価償却累計額、鉱業用地"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class GainOnSaleOfSharesOfSubsidiariesAndAssociatesOpeCF(Enum):
    """"関係会社株式売却益、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LandUsedForMiningOperationsNet(Enum):
    """"鉱業用地（純額）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class LandUsedForMiningOperationsPPE(Enum):
    """"鉱業用地、有形固定資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class CompensationForPaymentEL(Enum):
    """"支払補償金、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DepositedGoldBullionCL(Enum):
    """"預り金地金、流動負債、負債の部"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ExpenseForTheMaintenanceAndManagementOfAbandonedMines(Enum):
    """"鉱山残務整理費用、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseInCashAndCashEquivalentsFromNewlyConsolidated(Enum):
    """"非連結子会社の連結に伴う現金及び現金同等物の増加額"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LandNetPPE(Enum):
    """"土地（純額）、有形固定資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class LeasedGoldBullionReceivableCA(Enum):
    """"貸付け金地金、流動資産、資産の部"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class LossesOnWithdrawalFromBusinessEL(Enum):
    """"事業撤退損失、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PaymentForPurchasesOfGoldBullionFromMarketForCustomersUnderMyGoldPlanOpeCF(Enum):
    """"金地金購入による支出、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromSalesOfGoldBullionDepositedFromCustomersUnderConsumingBailmentMyGoldPlanOpeCF(Enum):
    """"金地金売却による収入、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnDisasterNOE(Enum):
    """"災害損失、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class AllowanceForDemolitionOfNonCurrentAssetsLiabilities(Enum):
    """"固定資産解体費用引当金、負債の部"""
    INTERIM_INSTANT = 'InterimInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class IncreaseDecreaseInAllowanceForDemolitionOfNonCurrentAssetsOpeCF(Enum):
    """"固定資産解体費用引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'


class IncreaseDecreaseInProvisionForShareBasedCompensationOpeCFBNK(Enum):
    """"株式報酬引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー、銀行業"""
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'


class LeaseReceivablesAndInvestmentAssetsAssetsBNK(Enum):
    """"リース債権及びリース投資資産、資産の部、銀行業"""
    INTERIM_INSTANT = 'InterimInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ProvisionForShareBasedCompensationLiabilitiesBNK(Enum):
    """"株式報酬引当金、負債の部、銀行業"""
    INTERIM_INSTANT = 'InterimInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ProvisionOfReserveForFinancialInstrumentsTransactionLiabilities(Enum):
    """"金融商品取引責任準備金繰入額"""
    INTERIM_DURATION = 'InterimDuration'
    INTERIM_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'InterimDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    INTERIM_DURATION__RECONCILING_ITEMS_MEMBER = 'InterimDuration_ReconcilingItemsMember'
    """ 調整項目 """
    INTERIM_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'InterimDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    INTERIM_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'InterimDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """


class ProvisionForPollutionLoadLevyCL(Enum):
    """"汚染負荷量賦課金引当金、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ProvisionForPollutionLoadLevyNCL(Enum):
    """"汚染負荷量賦課金引当金、固定負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class AllowanceForStockBenefitForEmployeeNCL(Enum):
    """"従業員株式給付引当金、固定負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class CondolenceMoneyNOE(Enum):
    """"弔慰金、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInProvisionForDecommissioningOfInventoriesGoodsOpeCF(Enum):
    """"棚卸資産廃棄費用引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInProvisionForEmployeeStockOwnershipPlanTrustOpeCF(Enum):
    """"従業員株式給付引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInProvisionForSpecialInvestigationFeesOpeCF(Enum):
    """"特別調査費用引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PaymentForBusinesRestrucuringExpensesOpeCF(Enum):
    """"事業構造改革費用の支払額、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProvisionForBusinessRestructuringNCL(Enum):
    """"事業構造改革引当金、固定負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ProvisionForDecommissioningOfInventoriesGoodsCL(Enum):
    """"棚卸資産廃棄費用引当金、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ProvisionForSpecialInvestigationExpensesCL(Enum):
    """"特別調査費用引当金、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class LossOnValuationOfInvestmentSecuritiesOpeCF(Enum):
    """"投資有価証券評価損、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class GainOnReversalOfLiabilitiesNOI(Enum):
    """"債務取崩益、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class CompensationExpensesEL(Enum):
    """"支払補償費、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProfitOnCansellationOfLeasesEI(Enum):
    """"リース解約益、特別利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class NewFactoryConstructionExpensesEL(Enum):
    """"新工場建設関連費用、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LitigationExpensesEL(Enum):
    """"訴訟関連費用、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LitigationExpensesOpeCF(Enum):
    """"訴訟関連費用、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LitigationExpensesPaidOpeCF(Enum):
    """"訴訟関連費用の支払額、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class RentalInventoryAssetsCA(Enum):
    """"レンタル商品、流動資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class InsuranceExpensesNOE(Enum):
    """"保険料、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class MaintenanceCostForIdleAssetsNOE(Enum):
    """"遊休資産維持管理費用、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class WithholdingTaxBurdenLossNOE(Enum):
    """"源泉税負担損失、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class UseQuantityDividendNOI(Enum):
    """"利用分量配当金、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class GainOnScrapMetalNOI(Enum):
    """"原材料等売却益、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class SystemFailureResponseCostsEL(Enum):
    """"システム障害対応費用、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProvisionForCompensationCL(Enum):
    """"損害補償損失引当金、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class DirectorsCompensationsSalariesAllowancesBonusesAndWelfareExpensesSGA(Enum):
    """"役員報酬及び従業員給与・諸手当・賞与・福利費、販売費及び一般管理費"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class EstimateDesignCostSGA(Enum):
    """"見積設計費、販売費及び一般管理費"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseNetDefinedBenefitAssetLiabilityOpeCF(Enum):
    """"退職給付に係る資産負債の増減額(△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class NotesReceivableAccountsReceivableFromCompletedConstructionContractsAndContractAssetsCA(Enum):
    """"受取手形、完成工事未収入金及び契約資産、流動資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class PaymentsIntoLongTermTimeDepositsInvCF(Enum):
    """"長期性預金の預け入れによる支出、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromWithdrawalOfLongTermTimeDepositsInvCF(Enum):
    """"長期性預金の払戻による収入、投資活動によるキャッシュフロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class NotesReceivableAccountsReceivableFromCompletedConstructionContractsAndOtherAndContractAssetsCA(Enum):
    """"受取手形・完成工事未収入金等及び契約資産、流動資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ProceedsFromIssuanceOfConvertibleBondsWithStockAcquisitionRightsFinCF(Enum):
    """"転換社債型新株予約権付社債の発行による収入、財務活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnInvestmentsInPartenershipFundNOE(Enum):
    """"組合投資損失、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInUnearnedInterestOnInstallmentSaleOpeCF(Enum):
    """"割賦販売前受利息の増減額(△は減少)、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class InterestIncomeOnInstallmentSaleNOI(Enum):
    """"割賦販売受取利息、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PaymentsFromRentalOfRealEstateForInvestmentInvCF(Enum):
    """"投資不動産の賃貸による支出、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class RentExpensesOpeCF(Enum):
    """"賃貸費用、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ReversalOfProvisionForProductWarrantiesNOI(Enum):
    """"製品保証引当金戻入額、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DirectorsCompensationsAndEmployeesSalariesSGA(Enum):
    """"役員・従業員給与手当、販売費及び一般管理費"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class RefundLiabilities(Enum):
    """"返金負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class RestructuringExpensesEL(Enum):
    """"構造改革費用、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProvisionForLossOnDisasterNOE(Enum):
    """"災害損失引当金繰入額、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class RestructuringExpensesNOE(Enum):
    """"事業再編費用、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnLiquidationOfNonCurrentAssetsEL(Enum):
    """"固定資産整理損失、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProvisionForLossOnLiquidationOfNonCurrentAssets(Enum):
    """"固定資産整理損失引当金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ProvisionForProductWarrantiesCL(Enum):
    """"製品保証引当金、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class MinimumPensionLiabilityAdjustmentOCI(Enum):
    """"最小年金負債調整額、その他の包括利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class MinimumPensionLiabilityAdjustments(Enum):
    """"最小年金負債調整額"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class PaymentForExtraRetirementPaymentsOpeCF(Enum):
    """"割増退職金等の支払額、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PaymentsForLitigationExpensesOpeCF(Enum):
    """"訴訟損失費用の支払額、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class RestructuringCostEL(Enum):
    """"事業構造改革費用、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class RestructuringCostOpeCF(Enum):
    """"事業構造改革費用、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class TheRightOfUsingLandIA(Enum):
    """"土地使用権、無形固定資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class BorrowingFeeNOE(Enum):
    """"借入手数料、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class BorrowingFeeOpeCF(Enum):
    """"借入手数料、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DecreaseIncreaseInRealEstateForSaleInProcessOpeCF(Enum):
    """"仕掛販売用不動産の増減額（△は増加）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DepositsFormSilentPartnershipCL(Enum):
    """"匿名組合預り金、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class DistributionsOfLossOnSilentPartnershipsOpeCF(Enum):
    """"匿名組合損益分配額、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DividendToASleepingPartnerFinCF(Enum):
    """"匿名組合員への分配金、財務活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class GainOnReversalOfProvisionForDemolitionCostEI(Enum):
    """"解体費用引当金戻入額、特別利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class GainOnReversalOfProvisionForDemolitionCostOpeCF(Enum):
    """"解体費用引当金戻入額、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInAccruedBusinessTaxesOpeCF(Enum):
    """"未払事業税等の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseOrDecreaseInTheTrustDepositsOpeCF(Enum):
    """"信託預金の増減額（△は増加）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PaymentsOfBorrowingFeeFinCF(Enum):
    """"借入手数料の支払額、財務活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromWithdrawalOfInvestmentsInSilentPartnershipFinCF(Enum):
    """"匿名組合員からの出資払込による収入、財務活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class RentalRealEstateExpensesNOE(Enum):
    """"賃貸不動産経費、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ReversalOfAllowanceForDoubtfulAccountsOpeCF(Enum):
    """"貸倒引当金戻入額、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class SalesAccruedIncomeCA(Enum):
    """"営業未収収益、流動資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class SpendingFundedByReimbursementsToTheAnonymousMembersFinCF(Enum):
    """"匿名組合員への出資払戻による支出、財務活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class TrustDeposit(Enum):
    """"信託預金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class TrustGuaranteeDepositsReceived(Enum):
    """"信託預り保証金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class TrustUnearnedRevenue(Enum):
    """"信託前受金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class CommissionForPurchaseOfTreasurySharesOpeCF(Enum):
    """"自己株式取得費用、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ReserveForRepairExpensesOfProductsCL(Enum):
    """"製品補修引当金、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ReseveForRepairExpensesOfProductsNCL(Enum):
    """"製品補修引当金、固定負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class AssetsForLeaseNet(Enum):
    """"賃貸資産（純額）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ExpensesOfRealEstateForRentNOE(Enum):
    """"賃貸不動産関係費用、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnSaleOfRawMaterialsNOE(Enum):
    """"原材料売却損、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInNetDefinedBenefitAssetAndLiabilityOpeCF(Enum):
    """"退職給付に係る資産及び負債の増減額、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DecreaseIncreaseInOperatingAccountsReceivableOpeCF(Enum):
    """"営業未収入金の増減額（△は増加）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class RedumptionOfBondsWithShareAcquisitionRightsFinCF(Enum):
    """"新株予約権付社債の償還による支出、財務活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class CompensationIncomeForDamagesEI(Enum):
    """"受取損害賠償金、特別利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ExpensesOfRealEstateNOE(Enum):
    """"不動産費用、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class GainOnSaleOfInvestmentsInCapitalOfSubsidiariesAndAssociatesEI(Enum):
    """"関係会社出資金売却益、特別利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInCashAndCashEquivalentsResultingFromChangeInAccountingPeriodOfSubsidiariesCCE(Enum):
    """"連結子会社の決算期変更に伴う現金及び現金同等物の増減額（△は減少）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossGainOnSaleOfInvestmentsInCapitalOfSubsidiariesAndAssociatesOpeCF(Enum):
    """"関係会社出資金売却損益（△は益）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromSaleOfInvestmentsInCapitalOfSubsidiariesResultingInChangeInScopeOf(Enum):
    """"連結の範囲の変更を伴う子会社出資金の売却による収入、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ElectronicallyRecordedObligationsOperatingFacilitiesCL(Enum):
    """"設備電子記録債務、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class GainOnSalesOfScrapsNOI(Enum):
    """"材料屑売却益、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromAcceptanceOfInvestmentToNonControllingInterestsFinCF(Enum):
    """"投資事業組合等における非支配持分からの出資受入による収入、財務活動によるキャッシュフロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class AccumulatedDepreciationRentalAssets(Enum):
    """"減価償却累計額、レンタル資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class IncomeOfRentNOI(Enum):
    """"賃貸収入、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class RentalAssetsNet(Enum):
    """"レンタル資産（純額）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class RentalAssetsPPE(Enum):
    """"レンタル資産、有形固定資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class LossOnSalesOfNotesAndAccountsReceivableTradeOpeCF(Enum):
    """"売上債権売却損、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProvisionForManagementBoardIncentivePlanTrust(Enum):
    """"役員株式給付引当金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class RevenueFromAcceptanceOfDevelopmentServicesNOI(Enum):
    """"受託研究収入、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class SalesOfTradeReceivablesPaid(Enum):
    """"売上債権売却による支払額、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ExpensesForPersonsOfTemporaryTransferOpeCF(Enum):
    """"出向者経費、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class GainOnReversalOfLossOnBusinessRelatedToBusinessPartnersEL(Enum):
    """"取引先関連事業損失戻入益、特別利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class GainOnReversalOfLossOnBusinessRelatedToBusinessPartnersOpeCF(Enum):
    """"取引先関連事業損失戻入益、、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromSurrenderValueOfInsuranceOpeCF(Enum):
    """"保険解約返戻金の受取額、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class CurrentPotionOfLongTermLoansPayableCL(Enum):
    """"一年以内返済長期借入金、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class GainOnReversalOfAssetRetirementObligationsNOI(Enum):
    """"資産除去債務戻入益、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInConsumptionTaxesPayableConsumptionTaxesRefundReceivableOpeCF(Enum):
    """"未払又は未収消費税等の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class NoteNotesAndAccountsReceivableTradeAndContractAssetsNetCA(Enum):
    """"売掛金及び契約資産、流動資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class OperationsCosignmentFeeNOI(Enum):
    """"業務受託収入、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class CommissionForSyndicateLoanOpeCF(Enum):
    """"シンジケートローン手数料、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class AmortizationOfCustomerRelatedAssetsOpeCF(Enum):
    """"顧客関連資産償却額、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ExpensesEtcSegmentInformation(Enum):
    """"経費等、セグメント情報"""
    INTERIM_DURATION = 'InterimDuration'
    INTERIM_DURATION__RECONCILING_ITEMS_MEMBER = 'InterimDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_INTERIM_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1InterimDuration_ReconcilingItemsMember'
    """ 調整項目 """


class GrossOperatingProfitSegmentInformation(Enum):
    """"連結業務粗利益、セグメント情報"""
    INTERIM_DURATION = 'InterimDuration'
    INTERIM_DURATION__RECONCILING_ITEMS_MEMBER = 'InterimDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_INTERIM_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1InterimDuration_ReconcilingItemsMember'
    """ 調整項目 """


class ReserveForPointProgramLiabilitiesBNK(Enum):
    """"ポイント引当金、負債の部、銀行業"""
    INTERIM_INSTANT = 'InterimInstant'
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class BalanceOfPurchaseAndSalesOfTreasuryStockFinCF(Enum):
    """"自己株式の取得・売却による収支、財務活動によるキャッシュ・フロー"""
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'


class IncreaseDueToShareDelivery(Enum):
    """"株式交付による増加"""
    INTERIM_DURATION = 'InterimDuration'
    INTERIM_DURATION__CAPITAL_SURPLUS_MEMBER = 'InterimDuration_CapitalSurplusMember'
    """ 資本剰余金 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__CAPITAL_SURPLUS_MEMBER = 'InterimDuration_NonConsolidatedMember_CapitalSurplusMember'
    """ 個別又は非連結資本剰余金 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__OTHER_CAPITAL_SURPLUS_MEMBER = 'InterimDuration_NonConsolidatedMember_OtherCapitalSurplusMember'
    """ 個別又は非連結その他資本剰余金 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__SHAREHOLDERS_EQUITY_MEMBER = 'InterimDuration_NonConsolidatedMember_ShareholdersEquityMember'
    """ 個別又は非連結株主資本 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__TREASURY_STOCK_MEMBER = 'InterimDuration_NonConsolidatedMember_TreasuryStockMember'
    """ 個別又は非連結自己株式 """
    INTERIM_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'InterimDuration_ShareholdersEquityMember'
    """ 株主資本 """
    INTERIM_DURATION__TREASURY_STOCK_MEMBER = 'InterimDuration_TreasuryStockMember'
    """ 自己株式 """


class LncreaseDecreaseInLeaseReceivablesAndInvestmentAssetsOpeCFBNK(Enum):
    """"リース債権及びリース投資資産の純増(△)減、営業活動によるキャッシュ・フロー、銀行業"""
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'


class ProvisionForLossOnSpecialClaims(Enum):
    """"特別クレーム損失引当金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class DevelopmentFiduciaryObligationFeeNOI(Enum):
    """"開発業務受託料、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LandUseRightsIA(Enum):
    """"土地使用権、無形固定資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class LeaseReceivablesAndInvestmentsInLeasesAssetsBNK(Enum):
    """"リース債権及びリース投資資産、資産の部、銀行業"""
    INTERIM_INSTANT = 'InterimInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ProvisionForShareAwards(Enum):
    """"株式給付引当金"""
    INTERIM_INSTANT = 'InterimInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class AllowanceForDemolitionOfNonCurrentAssetsLiabilities(Enum):
    """"固定資産解体費用引当金、負債の部"""
    INTERIM_INSTANT = 'InterimInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ReversalOfProvisionForLossOnGuaranteesNOI(Enum):
    """"債務保証損失引当金戻入額、営業外収益"""
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class IncreaseOfTreasurySharesByIncreasingOfEntitiesAccountedForUsingEquityMethodSS(Enum):
    """"持分法適用の関連会社の増加に伴う自己株式の増加 、株主資本等変動計算書"""
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_INTERIM_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1InterimDuration_ShareholdersEquityMember'
    """ 株主資本 """
    PRIOR1_INTERIM_DURATION__TREASURY_STOCK_MEMBER = 'Prior1InterimDuration_TreasuryStockMember'
    """ 自己株式 """


class LeaseReceivablesAndInvestmentsInLeasesAssets(Enum):
    """"リース債権及びリース投資資産、資産の部"""
    INTERIM_INSTANT = 'InterimInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ProvisionForStocksharesLiabilities(Enum):
    """"株式給付引当金、負債の部"""
    INTERIM_INSTANT = 'InterimInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class RetainedEarningsIncreasedSalesAssociatedWithAIncreaseInEquityMethodAffiliatesSS(Enum):
    """"持分法適用の関連会社の増加に伴う利益剰余金の増加、株主資本等変動計算書"""
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_INTERIM_DURATION__RETAINED_EARNINGS_MEMBER = 'Prior1InterimDuration_RetainedEarningsMember'
    """ 利益剰余金 """
    PRIOR1_INTERIM_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1InterimDuration_ShareholdersEquityMember'
    """ 株主資本 """


class RevaluationReserveForLandChangesOfItemsDuringPeriod(Enum):
    """"土地再評価差額金取崩額、当期変動額"""
    INTERIM_DURATION = 'InterimDuration'
    INTERIM_DURATION__RETAINED_EARNINGS_MEMBER = 'InterimDuration_RetainedEarningsMember'
    """ 利益剰余金 """
    INTERIM_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'InterimDuration_ShareholdersEquityMember'
    """ 株主資本 """


class NetDecreaseIncreaseInMarginForCentralCounterpartyOpeCF(Enum):
    """"中央清算機関差入証拠金の純増（△）減、営業活動によるキャッシュ・フロー"""
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'


class ProvisionForShareBasedCompensationLiabilities(Enum):
    """"株式報酬引当金、負債の部"""
    INTERIM_INSTANT = 'InterimInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ProvisionForShereBasedCompensationOpeCF(Enum):
    """"株式報酬引当金の増減（△）、営業活動によるキャッシュ・フロー"""
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'


class RetirementOfTreasuryStockChangesDuringPeriod(Enum):
    """"自己株式の消却、当期変動額"""
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_INTERIM_DURATION__CAPITAL_SURPLUS_MEMBER = 'Prior1InterimDuration_CapitalSurplusMember'
    """ 資本剰余金 """
    PRIOR1_INTERIM_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1InterimDuration_ShareholdersEquityMember'
    """ 株主資本 """
    PRIOR1_INTERIM_DURATION__TREASURY_STOCK_MEMBER = 'Prior1InterimDuration_TreasuryStockMember'
    """ 自己株式 """


class RefundLiabilityCL(Enum):
    """"返金負債、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class GainOnSalesOfPropertyPlantAndEquipmentOpeCF(Enum):
    """"有形固定資産売却益、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnSalesAndRetirementOfPropertyPlantAndEquipmentOpeCF(Enum):
    """"有形固定資産除売却損、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnCessionOfAnObligationNOE(Enum):
    """"売掛債権譲渡損、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProvisionForCompensationNCL(Enum):
    """"損害補償損失引当金、固定負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class VendingMachinesIncomeNOI(Enum):
    """"自動販売機収入、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DecreaseIncreaseInBadLoansOpeCF(Enum):
    """"固定化債権の増減額（△は増加）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class CustomerRelationshipIA(Enum):
    """"顧客関連資産、無形固定資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class GainOnSaleOfSecuritiesOfOtherSubsidiariesAndAssociatesEI(Enum):
    """"その他の関係会社有価証券売却益、特別利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossGainOnSaleOfSecuritiesOfOtherSubsidiariesAndAssociatesOpeCF(Enum):
    """"その他の関係会社有価証券売却損益（△は益）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromSaleOfSecuritiesOfOtherSubsidiariesAndAssociatesInvCF(Enum):
    """"その他の関係会社有価証券の売却による収入、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class AccruedRetirementBenefitsForDirectorsNCL(Enum):
    """"未払役員退職慰労金、固定負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class InvestmentAdvisoryFeeNOE(Enum):
    """"投資顧問料、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DemolitionAndRemovalCostsEL(Enum):
    """"解体撤去費用、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DemolitionAndRemovalCostsOpeCF(Enum):
    """"解体撤去費用、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ExpensesForDemolitionAndRemovalCostsInvCF(Enum):
    """"解体撤去費用の支出、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class GainOnSaleOfInvestmentInAffiliatedInvCF(Enum):
    """"関係会社出資金売却による収入、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class GainOnSaleOfInvestmentsInCapitalOfSubsidiariesAndAssociatesEI(Enum):
    """"関係会社出資金売却益、特別利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class GainOnSaleOfInvestmentsInCapitalOfSubsidiariesAndAssociatesOpeCF(Enum):
    """"関係会社出資金売却益、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class SpecialSurveyCostsEtcEL(Enum):
    """"特別調査費用等、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class SpecialSurveyCostsEtcOpeCF(Enum):
    """"特別調査費用等、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LandUseRightIA(Enum):
    """"土地使用権、無形固定資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class NationalSubsidiesOpeCF(Enum):
    """"国庫補助金、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInNetDefinedBenefitAssetAndLabilityOpeCF(Enum):
    """"退職給付に係る資産及び負債の増減額、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInProvisionForLossOnAntiMonopolyActOpeCF(Enum):
    """"独占禁止法関連損失引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInProvisionForProductDefectCompensationOpeCF(Enum):
    """"製品補償引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProvisionForProductCompensationEL(Enum):
    """"製品補償引当金繰入額、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProvisionForProductDefectCompensationNCL(Enum):
    """"製品補償引当金、固定負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class CompensationForDamageIncomeEI(Enum):
    """"受取損害賠償金、特別利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class CompensationForDamageIncomeOpeCF(Enum):
    """"受取損害賠償金、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class CompensationForDamageIncomeReceivedOpeCFFinCF(Enum):
    """"受取損害賠償金の受領額、営業活動によるキャッシュ・フロー又は投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProvisionForShareAwardsForEmployeesNCL(Enum):
    """"従業員株式給付引当金、固定負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ProvisionForTaxesRelatedExpensesCL(Enum):
    """"租税関連費用引当金、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class MiscellaneousExpensesOfAssetsForRentNOE(Enum):
    """"貸与資産諸費用、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PaidAmountOfBonusForDirectorsOpeCF(Enum):
    """"役員賞与の支払額、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class RightOfUseAssetsNetPPE(Enum):
    """"使用権資産（純額）、有形固定資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class InceaseDecreaseInNetDefinedBenefitAssetAndLiabilityOpeCF(Enum):
    """"退職給付に係る資産及び負債の増減額、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IntersegmentRevenueAndTransfers(Enum):
    """"セグメント間の内部売上収益又は振替高"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'CurrentYTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    CURRENT_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'CurrentYTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1YTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1YTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """


class RevenueFromExternalCustomers(Enum):
    """"外部顧客への売上収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'CurrentYTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    CURRENT_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'CurrentYTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1YTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1YTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """


class GainOnSaleOfInvestmentsInCapitalOfSubsidiariesAndAssociatesEI(Enum):
    """"関係会社出資金売却益、特別利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class GainOnSalesOfInvestmentSecuritiesOpeCF(Enum):
    """"投資有価証券売却益、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class GainOnSalesOfInvestmentsInCapitalOfSubsidiariesAndAssociatesOpeCF(Enum):
    """"関係会社出資金売却益、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInRetirementBenefitAssetOrLiabilityOpeCF(Enum):
    """"退職給付に係る資産又は負債の増減額、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnValuationOfInvestmentSecuritiesOpeCF(Enum):
    """"投資有価証券評価損、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossGainOnSalesOfInvestmentInCapitalOfSubsidiariesAndAssociatesOpeCF(Enum):
    """"関係会社出資金売却損益（△は益）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnProductRecallEL(Enum):
    """"製品回収関連損失、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnSaleOfInvestmentInAffiliatedCompaniesEL(Enum):
    """"関係会社出資金売却損、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PaymentsForSalesOfInvestmentsInCapitalOfSubsidiariesResultingInChangeInScopeOfConsolidationInvCF(Enum):
    """"連結の範囲の変更を伴う子会社出資金の売却による支出、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromGovernmentalSubsideiesForInvestmentInPropertyAndEquipmentInvCF(Enum):
    """"設備投資助成金の受入による収入、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PuschaseOfStocksOfAffiliatesInvCF(Enum):
    """"関連会社株式の取得による支出、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class StateSubsidyOpeCF(Enum):
    """"国庫補助金、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class GainOnCancellationOfLeaseObligationsEI(Enum):
    """"リース債務解約益、特別利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class GainOnForgivenessOfLeaseObligationsOpeCF(Enum):
    """"リース債務解約益、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class AccumulatedDepreciationRightOfUseAssetsPPE(Enum):
    """"減価償却累計額、使用権資産、有形固定資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class DecreaseIncreaseInGuaranteeDepositsInvCF(Enum):
    """"差入保証金の増減額（△は増加）、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class RestorationCostOpeCF(Enum):
    """"原状回復費用、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class RestorationCostsEL(Enum):
    """"原状回復費用、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class RightOfUseAssetsNetPPE(Enum):
    """"使用権資産（純額）、有形固定資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class RightOfUseAssetsPPE(Enum):
    """"使用権資産、有形固定資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class BorrowingFeeNOE(Enum):
    """"借入手数料、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class BorrowingFeeOpeCF(Enum):
    """"借入手数料、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class GainOnLiquidationOfSubsidiariesAndAssociatesOpeCF(Enum):
    """"関係会社清算益、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class NonDeductibleConsumptionTaxNOE(Enum):
    """"控除対象外消費税等、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PaymentsOfBorrowingFeeFinCF(Enum):
    """"借入手数料の支払額、財務活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class TenderOfferRelatedExpensesEL(Enum):
    """"公開買付関連費用、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DecreaseIncreaseInDepositsForPurchaseOfTreasurySharesFinCF(Enum):
    """"自己株式取得のための預託金の増減額(△は増加)、財務活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ExepencesBeforeDeductionOfTemporaryConsumptionTaxPaymentSGA(Enum):
    """"仮払消費税の未控除費用、販売費及び一般管理費"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProvisionForLossOnAntiMonopolyActNCL(Enum):
    """"独占禁止法関連損失引当金、固定負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class LossOnDerivativesTradingNOE(Enum):
    """"デリバティブ損失、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class AdvesoryCost(Enum):
    """"アドバイザリー費用、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class GainOnSaleOfInvestmentsInCapitalOfSubsidiariesAndAssociatesEI(Enum):
    """"関係会社出資金売却益、特別利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnCancellationOfLeaseAgreementsNOE(Enum):
    """"差入保証金・敷金解約損、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class NetDecreaseIncreaseInTrustBeneficiaryRightInvCF(Enum):
    """"信託受益権の純増減額（△は増加）、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ReceivedSettlementFeeEI(Enum):
    """"受取解決金、特別利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ReceivedSettlementFeeOpeCF(Enum):
    """"受取解決金、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class TheReceiptOfSettlementFeeOpeCF(Enum):
    """"解決金の受取額、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class CommissionExpensesNOE(Enum):
    """"業務受託費用、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnSaleOfNonCurrentAssetsOpenCF(Enum):
    """"固定資産売却損、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProvisionForShareBasedCompensationLiabilities(Enum):
    """"株式報酬引当金、負債の部"""
    INTERIM_INSTANT = 'InterimInstant'
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class ProvisionForExecutiveOfficersRetirementBenefits(Enum):
    """"執行役員退職慰労引当金"""
    INTERIM_INSTANT = 'InterimInstant'
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class ProvisionForStocksPaymentLiabilities(Enum):
    """"株式給付引当金、負債の部"""
    INTERIM_INSTANT = 'InterimInstant'
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class ProvisionForShareBasedRemuneration(Enum):
    """"株式給付引当金"""
    INTERIM_INSTANT = 'InterimInstant'
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class IncreaseByShareExchangesChangesOfItemsDuringPeriod(Enum):
    """"株式交換による増加、当期変動額"""
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_INTERIM_DURATION__CAPITAL_SURPLUS_MEMBER = 'Prior1InterimDuration_CapitalSurplusMember'
    """ 資本剰余金 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__CAPITAL_SURPLUS_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_CapitalSurplusMember'
    """ 個別又は非連結資本剰余金 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__OTHER_CAPITAL_SURPLUS_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_OtherCapitalSurplusMember'
    """ 個別又は非連結その他資本剰余金 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_ShareholdersEquityMember'
    """ 個別又は非連結株主資本 """
    PRIOR1_INTERIM_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1InterimDuration_ShareholdersEquityMember'
    """ 株主資本 """
    PRIOR1_INTERIM_DURATION__TREASURY_STOCK_MEMBER = 'Prior1InterimDuration_TreasuryStockMember'
    """ 自己株式 """


class ProvisionForLossOnCancellationOfSystemContractsLiabilitiesBNK(Enum):
    """"システム解約損失引当金、負債の部、銀行業"""
    INTERIM_INSTANT = 'InterimInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class AllowanceForDemolitionOfNonCurrentAssetsLiabilities(Enum):
    """"固定資産解体費用引当金、負債の部"""
    INTERIM_INSTANT = 'InterimInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ProvisionForLossOnCancellationOfSystemContractsLiabilities(Enum):
    """"システム解約損失引当金、負債の部"""
    INTERIM_INSTANT = 'InterimInstant'
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class ReversalOfProvisionForLossOnCancellationOfSystemContractsEI(Enum):
    """"システム解約損失引当金戻入益、特別利益"""
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'


class TransferToOtherCapitalSurplusFromRetainedEarningsBroughtForward(Enum):
    """"繰越利益剰余金からその他資本剰余金への振替"""
    INTERIM_DURATION = 'InterimDuration'
    INTERIM_DURATION__CAPITAL_SURPLUS_MEMBER = 'InterimDuration_CapitalSurplusMember'
    """ 資本剰余金 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__CAPITAL_SURPLUS_MEMBER = 'InterimDuration_NonConsolidatedMember_CapitalSurplusMember'
    """ 個別又は非連結資本剰余金 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__OTHER_CAPITAL_SURPLUS_MEMBER = 'InterimDuration_NonConsolidatedMember_OtherCapitalSurplusMember'
    """ 個別又は非連結その他資本剰余金 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_BROUGHT_FORWARD_MEMBER = 'InterimDuration_NonConsolidatedMember_RetainedEarningsBroughtForwardMember'
    """ 個別又は非連結繰越利益剰余金 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_MEMBER = 'InterimDuration_NonConsolidatedMember_RetainedEarningsMember'
    """ 個別又は非連結利益剰余金 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__SHAREHOLDERS_EQUITY_MEMBER = 'InterimDuration_NonConsolidatedMember_ShareholdersEquityMember'
    """ 個別又は非連結株主資本 """
    INTERIM_DURATION__RETAINED_EARNINGS_MEMBER = 'InterimDuration_RetainedEarningsMember'
    """ 利益剰余金 """
    INTERIM_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'InterimDuration_ShareholdersEquityMember'
    """ 株主資本 """
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_INTERIM_DURATION__CAPITAL_SURPLUS_MEMBER = 'Prior1InterimDuration_CapitalSurplusMember'
    """ 資本剰余金 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__CAPITAL_SURPLUS_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_CapitalSurplusMember'
    """ 個別又は非連結資本剰余金 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__OTHER_CAPITAL_SURPLUS_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_OtherCapitalSurplusMember'
    """ 個別又は非連結その他資本剰余金 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_BROUGHT_FORWARD_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_RetainedEarningsBroughtForwardMember'
    """ 個別又は非連結繰越利益剰余金 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_RetainedEarningsMember'
    """ 個別又は非連結利益剰余金 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_ShareholdersEquityMember'
    """ 個別又は非連結株主資本 """
    PRIOR1_INTERIM_DURATION__RETAINED_EARNINGS_MEMBER = 'Prior1InterimDuration_RetainedEarningsMember'
    """ 利益剰余金 """
    PRIOR1_INTERIM_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1InterimDuration_ShareholdersEquityMember'
    """ 株主資本 """


class RevaluationReserveForLandChangesOfItemsDuringPeriod(Enum):
    """"土地再評価差額金の取崩、当期変動額"""
    INTERIM_DURATION = 'InterimDuration'
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_BROUGHT_FORWARD_MEMBER = 'InterimDuration_NonConsolidatedMember_RetainedEarningsBroughtForwardMember'
    """ 個別又は非連結繰越利益剰余金 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_MEMBER = 'InterimDuration_NonConsolidatedMember_RetainedEarningsMember'
    """ 個別又は非連結利益剰余金 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__SHAREHOLDERS_EQUITY_MEMBER = 'InterimDuration_NonConsolidatedMember_ShareholdersEquityMember'
    """ 個別又は非連結株主資本 """
    INTERIM_DURATION__RETAINED_EARNINGS_MEMBER = 'InterimDuration_RetainedEarningsMember'
    """ 利益剰余金 """
    INTERIM_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'InterimDuration_ShareholdersEquityMember'
    """ 株主資本 """


class RevaluationReserveForLandChangesOfItemsDuringPeriod(Enum):
    """"土地再評価差額金の取崩、当期変動額"""
    INTERIM_DURATION = 'InterimDuration'
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_BROUGHT_FORWARD_MEMBER = 'InterimDuration_NonConsolidatedMember_RetainedEarningsBroughtForwardMember'
    """ 個別又は非連結繰越利益剰余金 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_MEMBER = 'InterimDuration_NonConsolidatedMember_RetainedEarningsMember'
    """ 個別又は非連結利益剰余金 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__SHAREHOLDERS_EQUITY_MEMBER = 'InterimDuration_NonConsolidatedMember_ShareholdersEquityMember'
    """ 個別又は非連結株主資本 """
    INTERIM_DURATION__RETAINED_EARNINGS_MEMBER = 'InterimDuration_RetainedEarningsMember'
    """ 利益剰余金 """
    INTERIM_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'InterimDuration_ShareholdersEquityMember'
    """ 株主資本 """
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_BROUGHT_FORWARD_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_RetainedEarningsBroughtForwardMember'
    """ 個別又は非連結繰越利益剰余金 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_RetainedEarningsMember'
    """ 個別又は非連結利益剰余金 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_ShareholdersEquityMember'
    """ 個別又は非連結株主資本 """
    PRIOR1_INTERIM_DURATION__RETAINED_EARNINGS_MEMBER = 'Prior1InterimDuration_RetainedEarningsMember'
    """ 利益剰余金 """
    PRIOR1_INTERIM_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1InterimDuration_ShareholdersEquityMember'
    """ 株主資本 """


class ProvisionForShareBasedCompensationLiabilities(Enum):
    """"株式報酬引当金、負債の部"""
    INTERIM_INSTANT = 'InterimInstant'
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class RetirementOfTreasuryStockChangesDuringPeriod(Enum):
    """"自己株式の消却、当期変動額"""
    INTERIM_DURATION = 'InterimDuration'
    INTERIM_DURATION__CAPITAL_SURPLUS_MEMBER = 'InterimDuration_CapitalSurplusMember'
    """ 資本剰余金 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__CAPITAL_SURPLUS_MEMBER = 'InterimDuration_NonConsolidatedMember_CapitalSurplusMember'
    """ 個別又は非連結資本剰余金 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__OTHER_CAPITAL_SURPLUS_MEMBER = 'InterimDuration_NonConsolidatedMember_OtherCapitalSurplusMember'
    """ 個別又は非連結その他資本剰余金 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_MEMBER = 'InterimDuration_NonConsolidatedMember_RetainedEarningsMember'
    """ 個別又は非連結利益剰余金 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__SHAREHOLDERS_EQUITY_MEMBER = 'InterimDuration_NonConsolidatedMember_ShareholdersEquityMember'
    """ 個別又は非連結株主資本 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__TREASURY_STOCK_MEMBER = 'InterimDuration_NonConsolidatedMember_TreasuryStockMember'
    """ 個別又は非連結自己株式 """
    INTERIM_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'InterimDuration_ShareholdersEquityMember'
    """ 株主資本 """
    INTERIM_DURATION__TREASURY_STOCK_MEMBER = 'InterimDuration_TreasuryStockMember'
    """ 自己株式 """
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_BROUGHT_FORWARD_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_RetainedEarningsBroughtForwardMember'
    """ 個別又は非連結繰越利益剰余金 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_RetainedEarningsMember'
    """ 個別又は非連結利益剰余金 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_ShareholdersEquityMember'
    """ 個別又は非連結株主資本 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__TREASURY_STOCK_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_TreasuryStockMember'
    """ 個別又は非連結自己株式 """
    PRIOR1_INTERIM_DURATION__RETAINED_EARNINGS_MEMBER = 'Prior1InterimDuration_RetainedEarningsMember'
    """ 利益剰余金 """
    PRIOR1_INTERIM_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1InterimDuration_ShareholdersEquityMember'
    """ 株主資本 """
    PRIOR1_INTERIM_DURATION__TREASURY_STOCK_MEMBER = 'Prior1InterimDuration_TreasuryStockMember'
    """ 自己株式 """


class ProvisionForShareBasedCompensationLiabilities(Enum):
    """"株式報酬引当金、負債の部"""
    INTERIM_INSTANT = 'InterimInstant'
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class ProvisionOfReserveForCancellationOfShares(Enum):
    """"株式消却積立金の積立"""
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_BROUGHT_FORWARD_MEMBER = 'InterimDuration_NonConsolidatedMember_RetainedEarningsBroughtForwardMember'
    """ 個別又は非連結繰越利益剰余金 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_MEMBER = 'InterimDuration_NonConsolidatedMember_RetainedEarningsMember'
    """ 個別又は非連結利益剰余金 """
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__SHAREHOLDERS_EQUITY_MEMBER = 'InterimDuration_NonConsolidatedMember_ShareholdersEquityMember'
    """ 個別又は非連結株主資本 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_BROUGHT_FORWARD_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_RetainedEarningsBroughtForwardMember'
    """ 個別又は非連結繰越利益剰余金 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__RETAINED_EARNINGS_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_RetainedEarningsMember'
    """ 個別又は非連結利益剰余金 """
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember_ShareholdersEquityMember'
    """ 個別又は非連結株主資本 """


class ReserveForCancellationOfShares(Enum):
    """"株式消却積立金"""
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class BalanceAtTheBeginningOfThePeriodAfterRetroactiveProcessing(Enum):
    """"遡及処理後当期首残高"""
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__CAPITAL_STOCK_MEMBER = 'Prior1YearInstant_CapitalStockMember'
    """ 資本金 """
    PRIOR1_YEAR_INSTANT__CAPITAL_SURPLUS_MEMBER = 'Prior1YearInstant_CapitalSurplusMember'
    """ 資本剰余金 """
    PRIOR1_YEAR_INSTANT__DEFERRED_GAINS_OR_LOSSES_ON_HEDGES_MEMBER = 'Prior1YearInstant_DeferredGainsOrLossesOnHedgesMember'
    """ 繰延ヘッジ損益 """
    PRIOR1_YEAR_INSTANT__REMEASUREMENTS_OF_DEFINED_BENEFIT_PLANS_MEMBER = 'Prior1YearInstant_RemeasurementsOfDefinedBenefitPlansMember'
    """ 退職給付に係る調整累計額 """
    PRIOR1_YEAR_INSTANT__RETAINED_EARNINGS_MEMBER = 'Prior1YearInstant_RetainedEarningsMember'
    """ 利益剰余金 """
    PRIOR1_YEAR_INSTANT__REVALUATION_RESERVE_FOR_LAND_MEMBER = 'Prior1YearInstant_RevaluationReserveForLandMember'
    """ 土地再評価差額金 """
    PRIOR1_YEAR_INSTANT__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1YearInstant_ShareholdersEquityMember'
    """ 株主資本 """
    PRIOR1_YEAR_INSTANT__SUBSCRIPTION_RIGHTS_TO_SHARES_MEMBER = 'Prior1YearInstant_SubscriptionRightsToSharesMember'
    """ 新株予約権 """
    PRIOR1_YEAR_INSTANT__TREASURY_STOCK_MEMBER = 'Prior1YearInstant_TreasuryStockMember'
    """ 自己株式 """
    PRIOR1_YEAR_INSTANT__VALUATION_AND_TRANSLATION_ADJUSTMENTS_MEMBER = 'Prior1YearInstant_ValuationAndTranslationAdjustmentsMember'
    """ 評価・換算差額等 """
    PRIOR1_YEAR_INSTANT__VALUATION_DIFFERENCE_ON_AVAILABLE_FOR_SALE_SECURITIES_MEMBER = 'Prior1YearInstant_ValuationDifferenceOnAvailableForSaleSecuritiesMember'
    """ その他有価証券評価差額金 """
    PRIOR2_YEAR_INSTANT = 'Prior2YearInstant'
    PRIOR2_YEAR_INSTANT__CAPITAL_STOCK_MEMBER = 'Prior2YearInstant_CapitalStockMember'
    """ 資本金 """
    PRIOR2_YEAR_INSTANT__CAPITAL_SURPLUS_MEMBER = 'Prior2YearInstant_CapitalSurplusMember'
    """ 資本剰余金 """
    PRIOR2_YEAR_INSTANT__DEFERRED_GAINS_OR_LOSSES_ON_HEDGES_MEMBER = 'Prior2YearInstant_DeferredGainsOrLossesOnHedgesMember'
    """ 繰延ヘッジ損益 """
    PRIOR2_YEAR_INSTANT__REMEASUREMENTS_OF_DEFINED_BENEFIT_PLANS_MEMBER = 'Prior2YearInstant_RemeasurementsOfDefinedBenefitPlansMember'
    """ 退職給付に係る調整累計額 """
    PRIOR2_YEAR_INSTANT__RETAINED_EARNINGS_MEMBER = 'Prior2YearInstant_RetainedEarningsMember'
    """ 利益剰余金 """
    PRIOR2_YEAR_INSTANT__REVALUATION_RESERVE_FOR_LAND_MEMBER = 'Prior2YearInstant_RevaluationReserveForLandMember'
    """ 土地再評価差額金 """
    PRIOR2_YEAR_INSTANT__SHAREHOLDERS_EQUITY_MEMBER = 'Prior2YearInstant_ShareholdersEquityMember'
    """ 株主資本 """
    PRIOR2_YEAR_INSTANT__SUBSCRIPTION_RIGHTS_TO_SHARES_MEMBER = 'Prior2YearInstant_SubscriptionRightsToSharesMember'
    """ 新株予約権 """
    PRIOR2_YEAR_INSTANT__TREASURY_STOCK_MEMBER = 'Prior2YearInstant_TreasuryStockMember'
    """ 自己株式 """
    PRIOR2_YEAR_INSTANT__VALUATION_AND_TRANSLATION_ADJUSTMENTS_MEMBER = 'Prior2YearInstant_ValuationAndTranslationAdjustmentsMember'
    """ 評価・換算差額等 """
    PRIOR2_YEAR_INSTANT__VALUATION_DIFFERENCE_ON_AVAILABLE_FOR_SALE_SECURITIES_MEMBER = 'Prior2YearInstant_ValuationDifferenceOnAvailableForSaleSecuritiesMember'
    """ その他有価証券評価差額金 """


class ATMPlacementFeeExpensesOEBNK(Enum):
    """"ＡＴＭ設置支払手数料、経常費用、銀行業"""
    INTERIM_DURATION = 'InterimDuration'
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class ATMRelatedFeeExpensesOEBNK(Enum):
    """"ＡＴＭ支払手数料、経常費用、銀行業"""
    INTERIM_DURATION = 'InterimDuration'
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class ATMRelatedFeeIncomeOIBNK(Enum):
    """"ＡＴＭ受入手数料、経常収益、銀行業"""
    INTERIM_DURATION = 'InterimDuration'
    INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_INTERIM_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1InterimDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class ATMRelatedTemporaryAdvancesLiabilitiesBNK(Enum):
    """"ＡＴＭ仮受金、負債の部、銀行業"""
    INTERIM_INSTANT = 'InterimInstant'
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class ATMRelatedTemporaryPaymentsAssetsBNK(Enum):
    """"ＡＴＭ仮払金、資産の部、銀行業"""
    INTERIM_INSTANT = 'InterimInstant'
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class AccountsPayableForCreditCardBusinessLiabilities(Enum):
    """"クレジットカード事業未払金、負債の部"""
    INTERIM_INSTANT = 'InterimInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class AccountsReceivableMembersAssets(Enum):
    """"会員未収金、資産の部"""
    INTERIM_INSTANT = 'InterimInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class CreditCardOperatingExpenseOEBNK(Enum):
    """"クレジットカード業務経費、経常費用、銀行業"""
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'


class CreditCardOperatingIncomeOIBNK(Enum):
    """"クレジットカード営業収入、経常収益、銀行業"""
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'


class DecreaseIncreaseOfCapitalSurplusByChangeOfShareToConsolidatedSubsidiary(Enum):
    """"連結子会社に対する持分変動に伴う資本剰余金の増減"""
    INTERIM_DURATION = 'InterimDuration'
    INTERIM_DURATION__CAPITAL_SURPLUS_MEMBER = 'InterimDuration_CapitalSurplusMember'
    """ 資本剰余金 """
    INTERIM_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'InterimDuration_ShareholdersEquityMember'
    """ 株主資本 """
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_INTERIM_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1InterimDuration_ShareholdersEquityMember'
    """ 株主資本 """


class DepositsForElectronicMoneyLiabilities(Enum):
    """"電子マネー預り金、負債の部"""
    INTERIM_INSTANT = 'InterimInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ElectronicMoneyOperatingExpenseOEBNK(Enum):
    """"電子マネー業務経費、経常費用、銀行業"""
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'


class ElectronicMoneyOperatingIncomeOIBNK(Enum):
    """"電子マネー営業収入、経常収益、銀行業"""
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'


class FluctuationResultingFromExclusionOfEquityMethodAffiliates(Enum):
    """"持分法適用会社の減少に伴う変動"""
    INTERIM_DURATION = 'InterimDuration'
    INTERIM_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'InterimDuration_ShareholdersEquityMember'
    """ 株主資本 """
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_INTERIM_DURATION__RETAINED_EARNINGS_MEMBER = 'Prior1InterimDuration_RetainedEarningsMember'
    """ 利益剰余金 """
    PRIOR1_INTERIM_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'Prior1InterimDuration_ShareholdersEquityMember'
    """ 株主資本 """


class InterestExpensesSegmentInformation(Enum):
    """"資金調達費用、セグメント情報"""
    INTERIM_DURATION = 'InterimDuration'
    INTERIM_DURATION__RECONCILING_ITEMS_MEMBER = 'InterimDuration_ReconcilingItemsMember'
    """ 調整項目 """
    INTERIM_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'InterimDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_INTERIM_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1InterimDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_INTERIM_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1InterimDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """


class InterestIncomeSegmentInformation(Enum):
    """"資金運用収益、セグメント情報"""
    INTERIM_DURATION = 'InterimDuration'
    INTERIM_DURATION__RECONCILING_ITEMS_MEMBER = 'InterimDuration_ReconcilingItemsMember'
    """ 調整項目 """
    INTERIM_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'InterimDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_INTERIM_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1InterimDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_INTERIM_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1InterimDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """


class ReserveForStocksPaymentLiabilities(Enum):
    """"株式給付引当金、負債の部"""
    INTERIM_INSTANT = 'InterimInstant'
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class ProvisionForEmployeeStockOwnershipPlanTrustLiabilities(Enum):
    """"従業員株式給付引当金、負債の部"""
    INTERIM_INSTANT = 'InterimInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ProvisionForManagementBoardBenefitTrustLiabilities(Enum):
    """"役員株式給付引当金、負債の部"""
    INTERIM_INSTANT = 'InterimInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class DistributionsOfLossOnSilentPartnershipsNOE(Enum):
    """"匿名組合損益分配額、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class OtherOperatingAssetsPPE(Enum):
    """"その他の営業資産、有形固定資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ProvisionForAutomobileInspectionCostsNCL(Enum):
    """"メンテナンス引当金、固定負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ReversalOfProvisionForLossOnGuaranteesNOI(Enum):
    """"債務保証損失引当金戻入額、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class OperatingLoanReceivablesCA(Enum):
    """"営業貸付債権、流動資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class OtherOperatingAssetsPPELEA(Enum):
    """"その他の営業資産、有形固定資産、リース事業"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ReserveForCarMaintenanceNCL(Enum):
    """"メンテナンス引当金、固定負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class CommissionFeeRevOA(Enum):
    """"受取手数料、営業活動による収益の内訳"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DecreaseIncreaseInOperationalGuaranteeDepositsOpeCF(Enum):
    """"営業保証金等の増減額（△は増加）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DecreaseIncreaseInOtherOperatingDebenturesOpeCF(Enum):
    """"その他営業債権の増減額（△は増加）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DecreaseIncreaseInPurchasedReceivablesOpeCF(Enum):
    """"買取債権の増減額（△は増加）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInReserveForInsurancePolicyLiabilitiesOpeCF(Enum):
    """"保険契約準備金の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class InsuranceExpensesCOSExpOA(Enum):
    """"保険費用、営業活動による費用・売上原価の内訳"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class InsuranceRevenueRevOA(Enum):
    """"保険収益、営業活動による収益の内訳"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class OtherOperatingDebenturesCA(Enum):
    """"その他営業債権、流動資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ProvisionForManagementBoardBenefitTrustLiabilitiesBNK(Enum):
    """"役員株式給付引当金、負債の部、銀行業"""
    INTERIM_INSTANT = 'InterimInstant'
    INTERIM_INSTANT__NON_CONSOLIDATED_MEMBER = 'InterimInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class RevaluationReserveForLandChangesOfItemsDuringPeriod(Enum):
    """"土地再評価差額金の取崩、当期変動額"""
    INTERIM_DURATION = 'InterimDuration'
    INTERIM_DURATION__RETAINED_EARNINGS_MEMBER = 'InterimDuration_RetainedEarningsMember'
    """ 利益剰余金 """
    INTERIM_DURATION__SHAREHOLDERS_EQUITY_MEMBER = 'InterimDuration_ShareholdersEquityMember'
    """ 株主資本 """


class DecreaseIncreaseInFuturesTransactionMarginCustomerOpeCF(Enum):
    """"委託者先物取引差金の増減額（△は増加）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class EquityInvestmentsInPropertiesForSaleCA(Enum):
    """"営業出資金、流動資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class LandHeldForDevelopmentCA(Enum):
    """"開発用土地、流動資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class LongTermNonRecourseLoansNCL(Enum):
    """"ノンリコース長期借入金、固定負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class NonRecourseBondsDueWithinOneYearCL(Enum):
    """"ノンリコース１年内償還予定の社債、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class NonRecourseBondsNCL(Enum):
    """"ノンリコース社債、固定負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class PaymentsForEquityTransactionsWithNonControllingShareholderFinCF(Enum):
    """"非支配株主との資本取引による支出、財務活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromLeaseAndGuaranteeDepositsReceivedInvCF(Enum):
    """"預り敷金保証金の受入による収入、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class RepaymentsOfLeaseAndGuaranteeDepositsReceivedInvCF(Enum):
    """"預り敷金保証金の返還による支出、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ShortTermNonRecourseLoansCL(Enum):
    """"ノンリコース短期借入金、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class CurrentPortionOfLongTermNonRecourseLoansPayableCL(Enum):
    """"ノンリコース1年内返済予定長期借入金、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class CurrentPortionOfNonRecourseBondsCL(Enum):
    """"ノンリコース1年内償還予定社債、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class LeaseAndGuaranteeDepositedNCL(Enum):
    """"預り敷金及び保証金、固定負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class LongTermNonRecourseLoansPayableNCL(Enum):
    """"ノンリコース長期借入金、固定負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class NonRecoureseBondsPayableNCL(Enum):
    """"ノンリコース社債、固定負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ProceedsFromLeaseAndGuaranteeDepositsReceivedInvCF(Enum):
    """"預り敷金及び保証金の受入による収入、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class RepaymentOfLongTermNonRecourseLoansPayableFinCF(Enum):
    """"ノンリコース長期借入金の返済による支出、財務活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class RepaymentsOfLeaseAndGuaranteeDepositsReceivedInvCF(Enum):
    """"預り敷金及び保証金の返還による支出、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DepositsReceivedFromRealEstateSpecifiedJointEnterpriseInvestment(Enum):
    """"不動産特定共同事業出資受入金、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class DepositsReceivedFromRealEstateSpecifiedJointEnterpriseInvestmentNCL(Enum):
    """"不動産特定共同事業出資受入金、固定負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class PayablesUnderFluidityReceivablesCL(Enum):
    """"債権流動化債務、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ProceedsFromDepositsReceivedFromRealEstateSpecifiedJointEnterpriseInvestmentFinCF(Enum):
    """"不動産特定共同事業出資受入による収入、財務活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class RepaymentsOfDistributionReceivedFromRealEstateSpecifiedJointEnterpriseInvestmentFinCF(Enum):
    """"不動産特定共同事業出資返還による支出、財務活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnRelatedToRepairWorkEL(Enum):
    """"補修工事関連損失、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnRelatedToRepairWorkOpeCF(Enum):
    """"補修工事関連損失、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PaymentForRelatedToRepairWorkOpeCF(Enum):
    """"補修工事関連支払額、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProvisionForLossOnGuaranteesForRentCL(Enum):
    """"保証履行引当金、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ProvisionForLossOnRelatedToRepairWorkCL(Enum):
    """"補修工事関連損失引当金、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ProvisionForLossOnRelatedToRepairWorkNCL(Enum):
    """"補修工事関連損失引当金、固定負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ProvisionForLossOnVacanciesNCL(Enum):
    """"空室損失引当金、固定負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ReversalOfProvisionForLossOnRelatedToRepairWorkEI(Enum):
    """"補修工事関連損失引当金戻入額、特別利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ReversalOfProvisionForLossOnRelatedToRepairWorkOpeCF(Enum):
    """"補修工事関連損失引当金戻入額、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class AccountsPayableTradeAndAccountsPayableForConstructionContractsCL(Enum):
    """"買掛金及び工事未払金、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class IncreaseDecreaseInNetDefinedBenefitAssetAndLiabilityOpeCF(Enum):
    """"退職給付に係る資産負債の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProvisionForLossOnLeaseBusinessNCL(Enum):
    """"賃貸事業損失引当金、固定負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class BenefitsIncomeNOI(Enum):
    """"受取給付金、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class CommissionForAFinancialLoanNOE(Enum):
    """"財務手数料、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DecreaseIncreaseInRealEstateForSaleInProcessOpeCF(Enum):
    """"仕掛販売用不動産の増減額 （△は増加）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DecreaseIncreaseOnInvestmentsInSilentPartnershipOpeCF(Enum):
    """"匿名組合出資金の増減額、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class GainOnCapitalReductionWithCompensationOfSubsidiariesAndAffiliatesEI(Enum):
    """"関係会社有償減資払戻差益、特別利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class GainOnCapitalReductionWithCompensationOfSubsidiariesAndAffiliatesOpeCF(Enum):
    """"関係会社有償減資払戻差益、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInLeaseDepositsReceivedOpeCF(Enum):
    """"預り敷金の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnLiquidationOfSubsidiariesAndAffiliatesInvestmentsEL(Enum):
    """"関係会社出資金清算損、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnLiquidationOfSubsidiariesAndAffiliatesInvestmentsOpeCF(Enum):
    """"関係会社出資金清算損、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromCapitalReductionOfAffiliatedCompanyStockInvCF(Enum):
    """"関係会社株式の有償減資による収入、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromTheLiquidationOfSubsidiariesAndAssociatesInvCF(Enum):
    """"関係会社の清算による収入、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class GainOnCancellationOfInsurancePoliciesNOI(Enum):
    """"保険解約益、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class GainOnSalesOfInvestmentSecuritiesOpeCF(Enum):
    """"投資有価証券売却益、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsDueToMaturityOfInsuranceFundsInvCF(Enum):
    """"保険積立金の返戻による収入、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProfitLossBeforeIncomeTaxesOpeCF(Enum):
    """"税金等調整前中間純利益又は税金等調整前中間純損失（△）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class AllowanceForConstructionLossCL(Enum):
    """"工事損失引当金、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class IncreaseDecreaseInUneamedFaresOpeCF(Enum):
    """"前受運賃の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProvisionForDismantlingOfFixedAssetsCL(Enum):
    """"解体費用引当金、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ReserveForDismantlingCostsNCL(Enum):
    """"解体費用引当金、固定負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class COVID19SubsidiesNOI(Enum):
    """"新型コロナウイルス感染症対策補助金、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromCapitalReductionOfAffiliatesInvCF(Enum):
    """"関係会社株式の有償減資による収入、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInProvisionForLossOnLiquidationOpeCF(Enum):
    """"整理損失引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProvisionForLossOnLiquidationCL(Enum):
    """"整理損失引当金、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ProvisionForLossOnLiquidationNCL(Enum):
    """"整理損失引当金、固定負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ProvisionForRedemptionOfGiftCertificatesCL(Enum):
    """"商品券等引換引当金、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ProvisionForReturnOfSubsidyEL(Enum):
    """"助成金返還引当金繰入額、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class TradeAccountsReceivableAndContractAssetsCA(Enum):
    """"営業未収入金及び契約資産、流動資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class IncreaseDecreaseInRetirementBenefitsAssetAndLiabilityOpeCF(Enum):
    """"退職給付に係る資産及び負債の増減額、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class AccumulatedDepreciationMachineryEquipmentAndToolsFurnitureAndFixturesPPE(Enum):
    """"減価償却累計額、機械装置及び工具器具備品、有形固定資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class MachineryEquipmentAndToolsFurnitureAndFixturesNetPPE(Enum):
    """"機械装置及び工具器具備品（純額）、有形固定資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class MachineryEquipmentAndToolsFurnitureAndFixturesPPE(Enum):
    """"機械装置及び工具器具備品、有形固定資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ProvisionForLossOnBusinessOfSubsidiariesAndAssociatesNOE(Enum):
    """"関係会社事業損失引当金繰入額、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProvisionOfAllowanceForDoubtfulAccountsForSubsidiariesAndAssociatesNOE(Enum):
    """"関係会社貸倒引当金繰入額、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class SubsidiesForBusEI(Enum):
    """"車両等購入補助金、特別利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class AccountsReceivableTradeAndContractAssetsCA(Enum):
    """"売掛金及び契約資産、流動資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class NotesAndAccountsReceivableTradeAndContractAssetsCA(Enum):
    """"受取手形、営業未収金及び契約資産、流動資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class DecreaseIncreaseAccrunedConsumptionTaxRefundOpeCF(Enum):
    """"未収還付消費税の増減額（△は増加）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromLongTermAccountsPayableOtherFinCF(Enum):
    """"長期未払金の増加による収入、財務活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DepreciationCOS(Enum):
    """"減価償却費、売上原価"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DirectOperationExpenseCOS(Enum):
    """"作業直接費、売上原価"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class GainOnReversalOfAssetRetirementObligationsOpeCF(Enum):
    """"資産除去債務戻入益、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class NotesAndOperationAccountsReceivableTradeAndContractAssets(Enum):
    """"受取手形、営業未収金及び契約資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class PortTerminalOperationRevOA(Enum):
    """"港湾作業料、営業活動による収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class RentExpensesCOS(Enum):
    """"賃借料、売上原価"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class SalariesAndAllowancesCOS(Enum):
    """"給料及び手当、売上原価"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ExpensesRelatedToThe100thAnniversaryOfFoundationEL(Enum):
    """"創業100周年記念関連費用、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class AccountsReceivableTradeAndContractAssetsCA(Enum):
    """"営業未収金及び契約資産、流動資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class BuildingsAndStructuresInTrustNet(Enum):
    """"信託建物及び信託構築物（純額）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class DecreaseIncreaseInDeferredAndPrepaidExpensesOpeCF(Enum):
    """"繰延及び前払費用の増減額（△は増加）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DecreaseIncreaseInNotesAndAccountsReceivableContractAssetsOpeCF(Enum):
    """"契約資産の増減額（△は増加）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class CostOfSaleOfGoodsNOE(Enum):
    """"物品売却費用、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DecreaseIncreaseInDepositsPledgedAsCollateralInvCF(Enum):
    """"担保に供している預金の増減額（△は増加）、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LandfillsNetPPE(Enum):
    """"最終処分場（純額）、有形固定資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class LossGainOnValuationOfCurrencySwapsOpeCF(Enum):
    """"通貨スワップ評価損益（△は益）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsOnSalesOfGoodsNOI(Enum):
    """"物品売却収入、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProvisionOfAllowanceForDoubtfulAccountsOfGolfClubMembershipNOE(Enum):
    """"ゴルフ会員権貸倒引当金繰入額、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class TradeNotesAndAccountsReceivableTradeAndContractAssets(Enum):
    """"受取手形、営業未収入金及び契約資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class IncreaseDecreaseInProvisionForRemovalExpensesOfNonCurrentAssetsOpeCF(Enum):
    """"固定資産撤去費用引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class NonDeductibleConsumptionTaxNOE(Enum):
    """"控除対象外消費税等、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProgramRightsAndWorkInProcess(Enum):
    """"番組及び仕掛品"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class RemovalExpensesOfNonCurrentAssetsEL(Enum):
    """"固定資産撤去費、 特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class RestructuringCostEL(Enum):
    """"組織再編関連費用、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProvisionForGasApplianceWarrantiesNCL(Enum):
    """"器具保証引当金、固定負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class AllowanceForWithdrawalOfBusinessNCL(Enum):
    """"事業撤退損失引当金、固定負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class LossOnWithdrawalOfBusinessEL(Enum):
    """"事業撤退損失、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnWithdrawalOfBusinessOpeCF(Enum):
    """"事業撤退損失、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class BusinessRestructuringExpensesNOE(Enum):
    """"事業構造改善費用、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ContentProductionAccountCA(Enum):
    """"コンテンツ制作勘定、流動資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class GainOnSaleOfCryptoAssetsNOI(Enum):
    """"暗号資産売却益、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnValuationOfCryptoAssetsNOE(Enum):
    """"暗号資産評価損、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProvisionForOfficeRelocationNCL(Enum):
    """"事務所退去費用引当金、固定負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class RefundLiabilitiesCL(Enum):
    """"返金負債、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class RelocationRelatedCostsNOE(Enum):
    """"移転関連費用、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class CostOfFoodAndBeverageCOS(Enum):
    """"飲食売上原価、売上原価"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class FacilityRentIncomeRevOA(Enum):
    """"施設利用料収入、営業活動による収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class OfficeShopRentIncomeRevOA(Enum):
    """"家賃収入、営業活動による収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class SalesOfFoodAndBeverageRevOA(Enum):
    """"飲食売上高、営業活動による収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class CompensationForDamageNOE(Enum):
    """"損害賠償金、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class RentIncomeOfRealEstateNOI(Enum):
    """"不動産賃貸収入、営業外収益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class AcquisitionsOfSubsidiariesAccompaniedWithChangeInScopeOfConsolidationInvCF(Enum):
    """"連結の範囲の変更を伴う子会社株式の取得、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class CallLoanCA(Enum):
    """"コールローン、流動資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class CashDepositsForCashCollectionAndDepositServicesCA(Enum):
    """"現金護送業務用現金及び預金、流動資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class DamageInsuranceClaimGainEI(Enum):
    """"受取損害保険金、特別利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DamageInsuranceClaimGainOpeCF(Enum):
    """"受取損害保険金、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DecreaseIncreaseInInvestmentDepositsByPolicyholdersUnearnedPremiumsAndOtherInsuranceLiabilitiesOpeCF(Enum):
    """"保険契約準備金の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DecreaseIncreaseInNetDefinedBenefitAssetAndLiabilityOpeCF(Enum):
    """"退職給付に係る負債及び資産の増減額、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DeferredRevenueCL(Enum):
    """"前受契約料、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class DepositsReceivedForCashCollectionAndDepositServicesCL(Enum):
    """"現金護送業務用預り金、流動負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class DismantlementExpensesEL(Enum):
    """"解体撤去費用、特別損失"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DueFromSubscribersCA(Enum):
    """"未収契約料、流動資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class GainOnReversalOfAllowanceForDoubtfulAccountsEI(Enum):
    """"貸倒引当金戻入益、特別利益"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInCashDepositsForCashCollectionAndDepositServicesAndDepositsReceivedOpeCF(Enum):
    """"現金護送業務用現金預金及び預り金の増減額、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInDeferredRevenueOpeCF(Enum):
    """"前受契約料の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LongTermDeferredRevenueNCL(Enum):
    """"長期前受契約料、固定負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class LossOnDisposalOfFixedAssetsNOE(Enum):
    """"固定資産売却廃棄損、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class NetLossGainOnSalesAndDisposalOfAssetsOpeCF(Enum):
    """"固定資産売却損益及び廃棄損益（△は益）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PaymentsForSalesOfSharesOfSubsidiariesResultingInChangeInScopeOfConsolidation(Enum):
    """"連結の範囲の変更を伴う子会社株式の売却"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromDamageInsuranceIncomeOpeCF(Enum):
    """"損害保険金の受取額、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PurchaseOfStocksOfAffiliatesInvCF(Enum):
    """"関連会社株式の取得による支出、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class SecurityEquipmentAndControlStationsNetPPE(Enum):
    """"警報機器及び設備（純額）、有形固定資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class LongTermLeaseAndGuaranteeDepositsNCL(Enum):
    """"預り敷金保証金、固定負債"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class LossOnCancellationOfRentalContractsNOE(Enum):
    """"賃貸借解約損、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class SettlementMoneyNOE(Enum):
    """"解決金、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ConstructionMaterialCA(Enum):
    """"建設機材、流動資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class SubsidyRefundAmountNOE(Enum):
    """"助成金返還額、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProvisionForLossOnDisasterNOE(Enum):
    """"災害損失引当金繰入額、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProvisionForLossOnDisasterOpeCF(Enum):
    """"災害損失引当金繰入額、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class AccountsPayableForConstructionContracts(Enum):
    """"工事未払金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class AccountsReceivableFromCompletedConstructionContracts(Enum):
    """"完成工事未収入金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class AdvancesReceivedOnConstructionContractsInProgress(Enum):
    """"未成工事受入金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class CostsOnConstructionContractsInProgress(Enum):
    """"未成工事支出金"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class DecreaseIncreaseInInventoriesAndAdvancePaymentsOpeCF(Enum):
    """"棚卸資産及び前渡金の増減額（△は増加）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ClaimsProvableInBankruptcyClaimsProvableInRehabilitationAndOtherIOA(Enum):
    """"長期滞留債権、投資その他の資産"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class RentExpensesOnRealEstatesForInvestmentNOE(Enum):
    """"投資不動産賃貸費用、営業外費用"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProvisionForLossOnProjectContractsCL(Enum):
    """"プロジェクト損失引当金、流動負債"""
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class RoyaltyNOE(Enum):
    """"支払技術料、営業外費用"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class IncreaseDecreaseInLongTermUnearnedRevenueOpeCF(Enum):
    """"長期前受収益の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class NonDeductionableConsumptionTaxNOE(Enum):
    """"控除対象外消費税等、営業外費用"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class RitairemenntOpeCF(Enum):
    """"役員退職慰労未払金の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class DecreaseIncreaseInBusinessGuarantyMoneyOpeCF(Enum):
    """"営業保証金の増減額（△は増加）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class GainOnSalesOfScrapsNOI(Enum):
    """"廃棄物リサイクル収入、営業外収益"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class LossOnRemovalOfFixedAssetsEL(Enum):
    """"固定資産撤去費用、特別損失"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class LossOnRemovalOfFixedAssetsOpeCF(Enum):
    """"有形固定資産撤去費用、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class CompensationForDamageIncomeEI(Enum):
    """"受取損害賠償金、特別利益"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class CompensationForDamageIncomeOpeCF(Enum):
    """"受取損害賠償金、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class CompensationForDamageIncomeReceivedOpeCF(Enum):
    """"損害賠償金の受取額、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class CompensationForDamageOpeCF(Enum):
    """"損害賠償金、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class IncreaseDecreaseInProvisionForShareBasedRemunerationForEmployeeOpeCF(Enum):
    """"従業員株式給付引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class ProvisionForShareBasedRemunerationForEmployeeNCL(Enum):
    """"従業員株式給付引当金、固定負債"""
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class IncreaseDecreaseInProvisionForProvisionForPerformanceLinkedIncentiveCompensationOpeCF(Enum):
    """"業績連動報酬引当金の増減額(△は減少)、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class LossOnExtinguishmentShareBasedCompensationExpensesNOE(Enum):
    """"株式報酬費用消滅損、営業外費用"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class ProceedsFromDisposalOfTreasurySharesResultingFromExerciseOfShareAcquisitionRightsFinCF(Enum):
    """"新株予約権の行使による自己株式の処分による収入、財務活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class ProvisionForPerformanceLinkedIncentiveCompensationNCL(Enum):
    """"業績連動報酬引当金、固定負債"""
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class RepaymentIncomeNOI(Enum):
    """"受取弁済金、営業外収益"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class AllowanceForEmployeeStockBenefitsNCL(Enum):
    """"従業員株式給付引当金、固定負債"""
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class EmploymentLevySystemForPersonsWithDisabilitiesNOE(Enum):
    """"障害者雇用納付金、営業外費用"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class PaymentsForPurchaseOfTreasurySubscriptionRightToSharesFinCF(Enum):
    """"自己新株予約権の取得による支出、財務活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class SettlementReceivedNOI(Enum):
    """"受取和解金、営業外収益"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class PurchaseOfSharesOfAssociatesInvCF(Enum):
    """"関連会社株式の取得による支出、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class ConsignmentIncomeFromResearchAndDevelopmentNOI(Enum):
    """"受託研究収入、営業外収益"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class NetIncreaseDecreaseInRestrictionsOnBankDepositWithdrawalsFinCF(Enum):
    """"引出制限付預金の純増減額（△は増加）、財務活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class ExpenseOfInactiveNoncurrentAssetsNOE(Enum):
    """"生産休止費用、営業外費用"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class ProvisionForEmployeeStockOwnershipPlanTrustNCL(Enum):
    """"従業員株式給付引当金、固定負債"""
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class InterestExpensesAndGuaranteeCommissionOpeCF(Enum):
    """"支払利息及び支払保証料、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class InterestExpensesAndGuaranteeCommissionPaidOpeCF(Enum):
    """"利息及び保証料の支払額、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class VariousCostAccordingToFactoryStopNOE(Enum):
    """"工場休止に伴う諸費用、営業外費用"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class ProvisionForRemovalLossCL(Enum):
    """"撤去損失引当金、流動負債"""
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class ShareholderBenefitProgramNOE(Enum):
    """"株主優待費用、営業外費用"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class DecreaseIncreaseInAdvancePaymentOpeCF(Enum):
    """"前払金の増減額（△は増加）、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class NonOperatingCommissionFeeOpeCF(Enum):
    """"営業外支払手数料、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class PaymentOfNonOperatingCommissionFeeOpeCF(Enum):
    """"営業外支払手数料の支払額、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class TaxRefundNOI(Enum):
    """"租税公課還付金、営業外収益"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class ExpensesOnInterestSubsidyNOI(Enum):
    """"利子補給金、営業外収益"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class PaymentsIntoPeriodicalDepositsInvCF(Enum):
    """"定期積金の預入による支出、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class LossOnAntiMonopolyActEL(Enum):
    """"独占禁止法関連損失、特別損失"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class NotesAndAccountsPayableTradeAndContractLiabilitiesCL(Enum):
    """"支払手形、買掛金及び契約負債、流動負債"""
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class ProvisionForLossOnAntiMonopolyActOpeCF(Enum):
    """"独占禁止法関連損失、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class ProvisionForLossOnAntiMonopolyActPaidOpeCF(Enum):
    """"独占禁止法関連支払額、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class ConsultingIncomeNOI(Enum):
    """"コンサルティング収入、営業外収益"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class PaymentsFromCollectionOfLoansReceivableFromDirectorsInvCF(Enum):
    """"役員に対する貸付による支出、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class ProceedsFromCollectionOfLoansReceivableFromDirectorsInvCF(Enum):
    """"役員に対する貸付金の回収による収入、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class ProceedsFromSaleOfInvestmentSecuritiesAndOthersInvCF(Enum):
    """"投資有価証券等の売却による収入、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class PurchaseOfInvestmentSecuritiesAndOthersInvCF(Enum):
    """"投資有価証券等の取得による支出、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class AccountsReceivableTradeAndContractAssetsCA(Enum):
    """"売掛金及び契約資産、流動資産"""
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class ReceivedIncentiveNOI(Enum):
    """"受取報奨金、営業外収益"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class AccountsReceivableTradeAndContractAssetsCA(Enum):
    """"売掛金及び契約資産、流動資産"""
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class BountyForEarlyPaymentsSGA(Enum):
    """"完納奨励金、販売費及び一般管理費"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class BountyForSuppliersSGA(Enum):
    """"出荷奨励金、販売費及び一般管理費"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class RentOfTheMarketsBaseOnSalesSGA(Enum):
    """"売上高割市場使用料、販売費及び一般管理費"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class CollectionOfCooperationMoneyOfCemeteryDevelopmentInvCF(Enum):
    """"霊園開発協力金の回収、投資活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class CooperationMoneyOFcemeteryDevelopmentIOA(Enum):
    """"霊園開発協力金、投資その他の資産"""
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class PermanentUsingRightCA(Enum):
    """"永代使用権、流動資産"""
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class SalesIncentiveIncomeNOI(Enum):
    """"受取販売奨励金、営業外収益"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class AntiquePPE(Enum):
    """"美術骨董品、有形固定資産"""
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class NetIncreaseDecreaseInGuaranteeDepositsReceivedFinCF(Enum):
    """"預り保証金の純増減額(△は減少)、財務活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class LossOnCancellationOfMembershipEL(Enum):
    """"会員権解約損、特別損失"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class ProceedsFromSurrenderValueOfInsuranceOpeCF(Enum):
    """"保険解約返戻金の受取額、営業活動によるキャッシュ・フロー"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class CurrentPortionOfLongTermLoansPayableCL(Enum):
    """"一年内返済予定長期借入金、流動負債"""
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'Prior1YearInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class RentIncomeOfRealEstateNOI(Enum):
    """"不動産賃貸収入、営業外収益"""
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


