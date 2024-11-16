from enum import Enum

class BalanceSheetTextBlock(Enum):
    """"貸借対照表 [テキストブロック]"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """


class ConsolidatedBalanceSheetTextBlock(Enum):
    """"連結貸借対照表 [テキストブロック]"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """


class ConsolidatedStatementOfCashFlowsTextBlock(Enum):
    """"連結キャッシュ・フロー計算書 [テキストブロック]"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """


class ConsolidatedStatementOfChangesInEquityTextBlock(Enum):
    """"連結株主資本等変動計算書 [テキストブロック]"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """


class ConsolidatedStatementOfComprehensiveIncomeSingleStatementTextBlock(Enum):
    """"連結損益及び包括利益計算書 [テキストブロック]"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """


class ConsolidatedStatementOfComprehensiveIncomeTextBlock(Enum):
    """"連結包括利益計算書 [テキストブロック]"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """


class ConsolidatedStatementOfIncomeTextBlock(Enum):
    """"連結損益計算書 [テキストブロック]"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """


class DebtorsNotesRegardingOverdraftContractsAndOrLoanCommitmentsTextBlock(Enum):
    """"当座貸越契約及び（又は）貸出コミットメントに関する借手の注記 [テキストブロック]"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


class DescriptionOfFactThatCompanysBusinessComprisesSingleSegment(Enum):
    """"単一セグメントである旨"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class DescriptionOfFactorsWhichLedToRecognitionOfGainOnBargainPurchaseTextBlock(Enum):
    """"報告セグメントごとの負ののれん発生益を認識する要因となった事象の概要 [テキストブロック]"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """


class DescriptionOfNatureAndAmountsOfDifferencesBetweenReportableSegmentsTotalAndFinancialStatementsTextBlock(Enum):
    """"報告セグメント合計額と財務諸表計上額との差額及び当該差額の主な内容（差異調整に関する事項） [テキストブロック]"""
    INTERIM_DURATION = 'InterimDuration'


class DescriptionOfNatureOfDifferencesBetweenProfitLossOfReportableSegmentsTotalAndQuarterlyFinancialStatementsTextBlock(Enum):
    """"報告セグメントごとの利益又は損失の金額の合計額と四半期損益計算書計上額との差額及び当該差額の主な内容（差異調整に関する事項） [テキストブロック]"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class DescriptionOfReportableSegmentsTextBlock(Enum):
    """"報告セグメントの概要 [テキストブロック]"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    INTERIM_DURATION = 'InterimDuration'


class DetailedScheduleOfManufacturingCostTextBlock(Enum):
    """"製造原価明細書 [テキストブロック]"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """


class DisclosureOfChangesEtcInReportableSegmentsTextBlock(Enum):
    """"報告セグメントの変更等に関する事項 [テキストブロック]"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DisclosureOfChangesInReportableSegmentsTextBlock(Enum):
    """"報告セグメントの変更に関する事項 [テキストブロック]"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    INTERIM_DURATION = 'InterimDuration'


class ExplanationOfMeasurementsOfSalesProfitLossAssetLiabilityAndOtherItemsForEachReportableSegmentTextBlock(Enum):
    """"報告セグメントごとの売上高、利益又は損失、資産、負債その他の項目の金額の算定方法 [テキストブロック]"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    INTERIM_DURATION = 'InterimDuration'


class FootnotesRegardingSegmentInformationTableTextBlock(Enum):
    """"セグメント表の脚注 [テキストブロック]"""
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


class InformationAboutAssetsForEachReportableSegmentTextBlock(Enum):
    """"報告セグメントごとの資産に関する情報 [テキストブロック]"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class InformationAboutImpairmentLossOfNonCurrentAssetsOrGoodwillEtcForEachReportableSegmentTextBlock(Enum):
    """"報告セグメントごとの固定資産の減損損失又はのれん等に関する情報 [テキストブロック]"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class InformationForEachOfMainCustomersTextBlock(Enum):
    """"主要な顧客ごとの情報 [テキストブロック]"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class InformationForEachProductOrServiceTextBlock(Enum):
    """"製品及びサービスごとの情報 [テキストブロック]"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class MajorComponentsOfSellingGeneralAndAdministrativeExpensesTextBlock(Enum):
    """"主要な販売費及び一般管理費 [テキストブロック]"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class NotesRegardingAccumulatedDepreciationOfPropertyPlantAndEquipmentTextBlock(Enum):
    """"有形固定資産の減価償却累計額の注記 [テキストブロック]"""
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class NotesRegardingAllowancesDirectlyDeductedFromBalancesOfAssetsTextBlock(Enum):
    """"資産の金額から直接控除している引当金の注記 [テキストブロック]"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'


class NotesRegardingAmountsOfReductionEntryOfPropertyPlantAndEquipmentTextBlock(Enum):
    """"有形固定資産の圧縮記帳額の注記 [テキストブロック]"""
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """


class NotesRegardingGainOnSalesOfPropertyPlantAndEquipmentTextBlock(Enum):
    """"固定資産売却益の注記 [テキストブロック]"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """


class NotesRegardingGuaranteeObligationsTextBlock(Enum):
    """"保証債務の注記 [テキストブロック]"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class NotesRegardingImpairmentLossTextBlock(Enum):
    """"減損損失に関する注記 [テキストブロック]"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """


class NotesRegardingInventoriesTextBlock(Enum):
    """"棚卸資産の内訳の注記 [テキストブロック]"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'


class NotesRegardingLossOnDisposalOfPropertyPlantAndEquipmentTextBlock(Enum):
    """"固定資産除却損の注記 [テキストブロック]"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """


class NotesRegardingLossOnSalesOfPropertyPlantAndEquipmentTextBlock(Enum):
    """"固定資産売却損の注記 [テキストブロック]"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """


class NotesRegardingPledgedAssetsTextBlock(Enum):
    """"担保に供している資産の注記 [テキストブロック]"""
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentYearInstant_NonConsolidatedMember'
    """ 当年度時点個別又は非連結 """


class NotesRegardingPromissoryNotesDueOnBalanceSheetDateTextBlock(Enum):
    """"期末日満期手形の会計処理 [テキストブロック]"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class NotesRegardingSharesAndBondsEtcOfUnconsolidatedSubsidiariesAndAssociatesTextBlock(Enum):
    """"非連結子会社及び関連会社の株式及び社債等 [テキストブロック]"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """


class NotesSegmentInformationEtcConsolidatedFinancialStatementsTextBlock(Enum):
    """"セグメント情報等、連結財務諸表 [テキストブロック]"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """


class NotesSegmentInformationEtcFinancialStatementsTextBlock(Enum):
    """"セグメント情報等、財務諸表 [テキストブロック]"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """


class NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatementsTextBlock(Enum):
    """"セグメント情報等、四半期連結財務諸表 [テキストブロック]"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'


class NotesSegmentInformationEtcQuarterlyFinancialStatementsTextBlock(Enum):
    """"セグメント情報等、四半期財務諸表 [テキストブロック]"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'


class NotesSegmentInformationEtcSemiAnnualConsolidatedFinancialStatementsTextBlock(Enum):
    """"セグメント情報等、中間連結財務諸表 [テキストブロック]"""
    INTERIM_DURATION = 'InterimDuration'


class NotesWhenThereIsSignificantSeasonalFluctuationInSalesOrOperatingExpensesTextBlock(Enum):
    """"売上高又は営業費用に著しい季節的変動がある場合の注記 [テキストブロック]"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYTDDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class PropertyPlantAndEquipmentInformationForEachRegionTextBlock(Enum):
    """"有形固定資産、地域ごとの情報 [テキストブロック]"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class QuarterlyBalanceSheetTextBlock(Enum):
    """"四半期貸借対照表 [テキストブロック]"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'


class QuarterlyConsolidatedBalanceSheetTextBlock(Enum):
    """"四半期連結貸借対照表 [テキストブロック]"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'


class QuarterlyConsolidatedStatementOfCashFlowsTextBlock(Enum):
    """"四半期連結キャッシュ・フロー計算書 [テキストブロック]"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'


class QuarterlyStatementOfCashFlowsTextBlock(Enum):
    """"四半期キャッシュ・フロー計算書 [テキストブロック]"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'


class ResearchAndDevelopmentExpensesIncludedInGeneralAndAdministrativeExpensesAndManufacturingCostForCurrentPeriodTextBlock(Enum):
    """"一般管理費及び当期製造費用に含まれる研究開発費 [テキストブロック]"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'


class RevenuesFromExternalCustomersInformationForEachRegionTextBlock(Enum):
    """"売上高、地域ごとの情報 [テキストブロック]"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'CurrentYearDuration_NonConsolidatedMember'
    """ 当年度会計期間個別又は非連結 """
    INTERIM_DURATION = 'InterimDuration'
    PRIOR1_INTERIM_DURATION = 'Prior1InterimDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__NON_CONSOLIDATED_MEMBER = 'Prior1YearDuration_NonConsolidatedMember'
    """ 個別又は非連結 """


class SemiAnnualBalanceSheetTextBlock(Enum):
    """"中間貸借対照表 [テキストブロック]"""
    INTERIM_DURATION = 'InterimDuration'


class SemiAnnualConsolidatedBalanceSheetTextBlock(Enum):
    """"中間連結貸借対照表 [テキストブロック]"""
    INTERIM_DURATION = 'InterimDuration'


class SemiAnnualConsolidatedStatementOfCashFlowsTextBlock(Enum):
    """"中間連結キャッシュ・フロー計算書 [テキストブロック]"""
    INTERIM_DURATION = 'InterimDuration'


class SemiAnnualConsolidatedStatementOfChangesInEquityTextBlock(Enum):
    """"中間連結株主資本等変動計算書 [テキストブロック]"""
    INTERIM_DURATION = 'InterimDuration'


class SemiAnnualConsolidatedStatementOfComprehensiveIncomeTextBlock(Enum):
    """"中間連結包括利益計算書 [テキストブロック]"""
    INTERIM_DURATION = 'InterimDuration'


class SemiAnnualConsolidatedStatementOfIncomeTextBlock(Enum):
    """"中間連結損益計算書 [テキストブロック]"""
    INTERIM_DURATION = 'InterimDuration'


class SemiAnnualStatementOfChangesInEquityTextBlock(Enum):
    """"中間株主資本等変動計算書 [テキストブロック]"""
    INTERIM_DURATION = 'InterimDuration'


class SemiAnnualStatementOfIncomeTextBlock(Enum):
    """"中間損益計算書 [テキストブロック]"""
    INTERIM_DURATION = 'InterimDuration'


class StatementOfCashFlowsTextBlock(Enum):
    """"キャッシュ・フロー計算書 [テキストブロック]"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """


class StatementOfChangesInEquityTextBlock(Enum):
    """"株主資本等変動計算書 [テキストブロック]"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """


class StatementOfIncomeTextBlock(Enum):
    """"損益計算書 [テキストブロック]"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """


class YearToQuarterEndConsolidatedStatementOfComprehensiveIncomeSingleStatementTextBlock(Enum):
    """"四半期連結累計期間、四半期連結損益及び包括利益計算書 [テキストブロック]"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'


class YearToQuarterEndConsolidatedStatementOfComprehensiveIncomeTextBlock(Enum):
    """"四半期連結累計期間、四半期連結包括利益計算書 [テキストブロック]"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'


class YearToQuarterEndConsolidatedStatementOfIncomeTextBlock(Enum):
    """"四半期連結累計期間、四半期連結損益計算書 [テキストブロック]"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'


class YearToQuarterEndStatementOfIncomeTextBlock(Enum):
    """"四半期累計期間、四半期損益計算書 [テキストブロック]"""
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


class NotesRegardingAmortizationOfGoodwillTextBlock(Enum):
    """"のれん償却額の注記 [テキストブロック]"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """


class NotesRegardingLossOnAbandonmentOfInventoriesTextBlock(Enum):
    """"棚卸資産廃棄損の注記 [テキストブロック]"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """


class NotesRegardingLossOnDisasterTextBlock(Enum):
    """"災害による損失の注記 [テキストブロック]"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """


class NotesRegardingRestructuringLossTextBlock(Enum):
    """"事業再編損の注記 [テキストブロック]"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """


class NotesRegardingSubsidyIncomeTextBlock(Enum):
    """"補助金収入の注記 [テキストブロック]"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """


class NotesRegardingFinancialCovenantClausesTextBlock(Enum):
    """"財務制限条項に関する注記 [テキストブロック]"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'


class NotesRegardingDetailsOfExtraordinaryLossesTextBlock(Enum):
    """"特別損失の内容に関する注記 [テキストブロック]"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'


class NotesRegardingRelocationRelatedLossesTextBlock(Enum):
    """"移転関連損失についての注記 [テキストブロック]"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'


class NotesRegardingFinancialCovenantClausesTextBlock(Enum):
    """"財務制限条項に関する注記 [テキストブロック]"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'


class NotesAndAccountsReceivableTredeTextBlock(Enum):
    """"受取手形及び売掛金に関する注記 [テキストブロック]"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'


class NotesRegardingGainOnTransferOfBusinessTextBlock(Enum):
    """"事業譲渡益の注記 [テキストブロック]"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'


class NotesRegardingLossOnLiquidationOfSubsidiariesAndAssociatesTextBlock(Enum):
    """"関係会社清算損の注記 [テキストブロック]"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'


class NotesRegardingReductionEntryTextBlock(Enum):
    """"圧縮記帳額に関する注記 [テキストブロック]"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'


class NotesRegardingReversalOfProvisionForLossOnCompensationTextBlock(Enum):
    """"補償損失引当金戻入額に関する注記 [テキストブロック]"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'


class NotesRegardingLossOnLitigationTextBlock(Enum):
    """"訴訟関連損失の注記 [テキストブロック]"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'


class NotesRegardingProvisionForLossOnLitigationTextBlock(Enum):
    """"訴訟損失引当金に関する注記 [テキストブロック]"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'


class NotesRegardingLossOnInappropriateConductInQualityInspectionsTextBlock(Enum):
    """"品質不適切行為関連損失に関する注記 [テキストブロック]"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'


class NotesSystemFailureResponseCostTextBlock(Enum):
    """"システム障害対応費用の注記 [テキストブロック]"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'


class NotesRegardingLossOnLitigationTextBlock(Enum):
    """"訴訟関連損失の注記 [テキストブロック]"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'


class NotesOnContingentLiabilitiesTextBlock(Enum):
    """"偶発債務に関する注記 [テキストブロック]"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'


class NotesRegardingLossOnLitigationTextBlock(Enum):
    """"訴訟関連損失の注記 [テキストブロック]"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'


class DisclosureOfImpairmentLossOnNonCurrentAssetsForEachReportableSegmentTextBlock(Enum):
    """"報告セグメントごとの固定資産の減損損失に関する情報 [テキストブロック]"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class NotesRegardingProvisionForReturnOfSubsidyTextBlock(Enum):
    """"助成金返還引当金繰入額に関する注記 [テキストブロック]"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'


class NotesRegardingMaterialsSuppliedForValueTextBlock(Enum):
    """"有償支給材料に関する注記 [テキストブロック]"""
    CURRENT_QUARTER_INSTANT__NON_CONSOLIDATED_MEMBER = 'CurrentQuarterInstant_NonConsolidatedMember'
    """ 個別又は非連結 """


