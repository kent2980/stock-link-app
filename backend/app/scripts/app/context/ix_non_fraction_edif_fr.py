from enum import Enum

class NumberOfSubmissionDEI(Enum):
    """"提出回数、DEI"""
    FILING_DATE_INSTANT = 'FilingDateInstant'


class AccruedExpensesCLIFRS(Enum):
    """"未払費用、流動負債（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class AccumulatedOtherComprehensiveIncomeIFRS(Enum):
    """"その他の包括利益累計額（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class AssetsHeldForSaleIFRS(Enum):
    """"売却目的で保有する資産（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class AssetsIFRS(Enum):
    """"資産（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR2_YEAR_INSTANT = 'Prior2YearInstant'


class BasicEarningsLossPerShareIFRS(Enum):
    """"基本的１株当たり当期利益（△損失）（IFRS）"""
    CURRENT_QUARTER_DURATION = 'CurrentQuarterDuration'
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_QUARTER_DURATION = 'Prior1QuarterDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class BondsAndBorrowingsCLIFRS(Enum):
    """"社債及び借入金、流動負債（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR2_YEAR_INSTANT = 'Prior2YearInstant'


class BondsAndBorrowingsLiabilitiesIFRS(Enum):
    """"社債及び借入金、負債（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class BondsAndBorrowingsNCLIFRS(Enum):
    """"社債及び借入金、非流動負債（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR2_YEAR_INSTANT = 'Prior2YearInstant'


class BorrowingsCLIFRS(Enum):
    """"借入金、流動負債（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR2_YEAR_INSTANT = 'Prior2YearInstant'


class BorrowingsNCLIFRS(Enum):
    """"借入金、非流動負債（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class CancellationOfTreasurySharesSSIFRS(Enum):
    """"自己株式の消却、持分変動計算書（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'CurrentYTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    CURRENT_YTD_DURATION__EFFECTIVE_PORTION_OF_CASH_FLOW_HEDGES_IFRS_MEMBER = 'CurrentYTDDuration_EffectivePortionOfCashFlowHedgesIFRSMember'
    """ キャッシュ・フロー・ヘッジの有効部分 """
    CURRENT_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'CurrentYTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    CURRENT_YTD_DURATION__EXCHANGE_DIFFERENCES_ON_TRANSLATION_OF_FOREIGN_OPERATIONS_IFRS_MEMBER = 'CurrentYTDDuration_ExchangeDifferencesOnTranslationOfForeignOperationsIFRSMember'
    """ 在外営業活動体の外貨換算差額 """
    CURRENT_YTD_DURATION__FINANCIAL_ASSETS_MEASURED_AT_FAIR_VALUE_THROUGH_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'CurrentYTDDuration_FinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益を通じて公正価値で測定する金融資産 """
    CURRENT_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'CurrentYTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    CURRENT_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'CurrentYTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    CURRENT_YTD_DURATION__REMEASUREMENTS_OF_DEFINED_BENEFIT_PLANS_IFRS_MEMBER = 'CurrentYTDDuration_RemeasurementsOfDefinedBenefitPlansIFRSMember'
    """ 確定給付制度の再測定 """
    CURRENT_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'CurrentYTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    CURRENT_YTD_DURATION__SHARE_CAPITAL_IFRS_MEMBER = 'CurrentYTDDuration_ShareCapitalIFRSMember'
    """ 資本金 """
    CURRENT_YTD_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'CurrentYTDDuration_TreasurySharesIFRSMember'
    """ 自己株式 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'Prior1YTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    PRIOR1_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'Prior1YTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    PRIOR1_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'Prior1YTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    PRIOR1_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'Prior1YTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    PRIOR1_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'Prior1YTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    PRIOR1_YTD_DURATION__SHARE_CAPITAL_IFRS_MEMBER = 'Prior1YTDDuration_ShareCapitalIFRSMember'
    """ 資本金 """
    PRIOR1_YTD_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'Prior1YTDDuration_TreasurySharesIFRSMember'
    """ 自己株式 """


class CapitalContributionFromNonControllingInterestsFinCFIFRS(Enum):
    """"非支配持分からの払込による収入、財務活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class CapitalSurplusIFRS(Enum):
    """"資本剰余金（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR2_YEAR_INSTANT = 'Prior2YearInstant'


class CashAndCashEquivalentsIFRS(Enum):
    """"現金及び現金同等物（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_QUARTER_INSTANT = 'Prior1QuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR2_YEAR_INSTANT = 'Prior2YearInstant'


class CashAndCashEquivalentsIfDifferentFromBSBalanceIFRS(Enum):
    """"現金及び現金同等物（財政状態計算書と異なる場合にCFで用いる）（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_QUARTER_INSTANT = 'Prior1QuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR2_YEAR_INSTANT = 'Prior2YearInstant'


class ChangeInScopeOfConsolidationSSIFRS(Enum):
    """"連結範囲の変動、持分変動計算書（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'CurrentYTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    CURRENT_YTD_DURATION__EFFECTIVE_PORTION_OF_CASH_FLOW_HEDGES_IFRS_MEMBER = 'CurrentYTDDuration_EffectivePortionOfCashFlowHedgesIFRSMember'
    """ キャッシュ・フロー・ヘッジの有効部分 """
    CURRENT_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'CurrentYTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    CURRENT_YTD_DURATION__EXCHANGE_DIFFERENCES_ON_TRANSLATION_OF_FOREIGN_OPERATIONS_IFRS_MEMBER = 'CurrentYTDDuration_ExchangeDifferencesOnTranslationOfForeignOperationsIFRSMember'
    """ 在外営業活動体の外貨換算差額 """
    CURRENT_YTD_DURATION__FINANCIAL_ASSETS_MEASURED_AT_FAIR_VALUE_THROUGH_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'CurrentYTDDuration_FinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益を通じて公正価値で測定する金融資産 """
    CURRENT_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'CurrentYTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    CURRENT_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'CurrentYTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    CURRENT_YTD_DURATION__REMEASUREMENTS_OF_DEFINED_BENEFIT_PLANS_IFRS_MEMBER = 'CurrentYTDDuration_RemeasurementsOfDefinedBenefitPlansIFRSMember'
    """ 確定給付制度の再測定 """
    CURRENT_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'CurrentYTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    CURRENT_YTD_DURATION__SHARE_CAPITAL_IFRS_MEMBER = 'CurrentYTDDuration_ShareCapitalIFRSMember'
    """ 資本金 """
    CURRENT_YTD_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'CurrentYTDDuration_TreasurySharesIFRSMember'
    """ 自己株式 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'Prior1YTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    PRIOR1_YTD_DURATION__EFFECTIVE_PORTION_OF_CASH_FLOW_HEDGES_IFRS_MEMBER = 'Prior1YTDDuration_EffectivePortionOfCashFlowHedgesIFRSMember'
    """ キャッシュ・フロー・ヘッジの有効部分 """
    PRIOR1_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'Prior1YTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    PRIOR1_YTD_DURATION__EXCHANGE_DIFFERENCES_ON_TRANSLATION_OF_FOREIGN_OPERATIONS_IFRS_MEMBER = 'Prior1YTDDuration_ExchangeDifferencesOnTranslationOfForeignOperationsIFRSMember'
    """ 在外営業活動体の外貨換算差額 """
    PRIOR1_YTD_DURATION__FINANCIAL_ASSETS_MEASURED_AT_FAIR_VALUE_THROUGH_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'Prior1YTDDuration_FinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益を通じて公正価値で測定する金融資産 """
    PRIOR1_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'Prior1YTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    PRIOR1_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'Prior1YTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    PRIOR1_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'Prior1YTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    PRIOR1_YTD_DURATION__SHARE_CAPITAL_IFRS_MEMBER = 'Prior1YTDDuration_ShareCapitalIFRSMember'
    """ 資本金 """
    PRIOR1_YTD_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'Prior1YTDDuration_TreasurySharesIFRSMember'
    """ 自己株式 """


class ChangesInOwnershipInterestInSubsidiariesSSIFRS(Enum):
    """"支配継続子会社に対する持分変動、持分変動計算書（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__ACCUMULATED_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'CurrentYTDDuration_AccumulatedOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益累計額 """
    CURRENT_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'CurrentYTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    CURRENT_YTD_DURATION__EFFECTIVE_PORTION_OF_CASH_FLOW_HEDGES_IFRS_MEMBER = 'CurrentYTDDuration_EffectivePortionOfCashFlowHedgesIFRSMember'
    """ キャッシュ・フロー・ヘッジの有効部分 """
    CURRENT_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'CurrentYTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    CURRENT_YTD_DURATION__EXCHANGE_DIFFERENCES_ON_TRANSLATION_OF_FOREIGN_OPERATIONS_IFRS_MEMBER = 'CurrentYTDDuration_ExchangeDifferencesOnTranslationOfForeignOperationsIFRSMember'
    """ 在外営業活動体の外貨換算差額 """
    CURRENT_YTD_DURATION__FINANCIAL_ASSETS_MEASURED_AT_FAIR_VALUE_THROUGH_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'CurrentYTDDuration_FinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益を通じて公正価値で測定する金融資産 """
    CURRENT_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'CurrentYTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    CURRENT_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'CurrentYTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    CURRENT_YTD_DURATION__REMEASUREMENTS_OF_DEFINED_BENEFIT_PLANS_IFRS_MEMBER = 'CurrentYTDDuration_RemeasurementsOfDefinedBenefitPlansIFRSMember'
    """ 確定給付制度の再測定 """
    CURRENT_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'CurrentYTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    CURRENT_YTD_DURATION__SHARE_CAPITAL_IFRS_MEMBER = 'CurrentYTDDuration_ShareCapitalIFRSMember'
    """ 資本金 """
    CURRENT_YTD_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'CurrentYTDDuration_TreasurySharesIFRSMember'
    """ 自己株式 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__ACCUMULATED_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'Prior1YTDDuration_AccumulatedOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益累計額 """
    PRIOR1_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'Prior1YTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    PRIOR1_YTD_DURATION__EFFECTIVE_PORTION_OF_CASH_FLOW_HEDGES_IFRS_MEMBER = 'Prior1YTDDuration_EffectivePortionOfCashFlowHedgesIFRSMember'
    """ キャッシュ・フロー・ヘッジの有効部分 """
    PRIOR1_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'Prior1YTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    PRIOR1_YTD_DURATION__EXCHANGE_DIFFERENCES_ON_TRANSLATION_OF_FOREIGN_OPERATIONS_IFRS_MEMBER = 'Prior1YTDDuration_ExchangeDifferencesOnTranslationOfForeignOperationsIFRSMember'
    """ 在外営業活動体の外貨換算差額 """
    PRIOR1_YTD_DURATION__FINANCIAL_ASSETS_MEASURED_AT_FAIR_VALUE_THROUGH_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'Prior1YTDDuration_FinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益を通じて公正価値で測定する金融資産 """
    PRIOR1_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'Prior1YTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    PRIOR1_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'Prior1YTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    PRIOR1_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'Prior1YTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    PRIOR1_YTD_DURATION__SHARE_CAPITAL_IFRS_MEMBER = 'Prior1YTDDuration_ShareCapitalIFRSMember'
    """ 資本金 """
    PRIOR1_YTD_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'Prior1YTDDuration_TreasurySharesIFRSMember'
    """ 自己株式 """


class CollectionOfLoansReceivableInvCFIFRS(Enum):
    """"貸付金の回収による収入、投資活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ComprehensiveIncomeAttributableToNonControllingInterestsIFRS(Enum):
    """"非支配持分、当期包括利益（IFRS）"""
    CURRENT_QUARTER_DURATION = 'CurrentQuarterDuration'
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_QUARTER_DURATION = 'Prior1QuarterDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class ComprehensiveIncomeAttributableToOwnersOfParentIFRS(Enum):
    """"親会社の所有者、当期包括利益（IFRS）"""
    CURRENT_QUARTER_DURATION = 'CurrentQuarterDuration'
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_QUARTER_DURATION = 'Prior1QuarterDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class ComprehensiveIncomeIFRS(Enum):
    """"当期包括利益（IFRS）"""
    CURRENT_QUARTER_DURATION = 'CurrentQuarterDuration'
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__ACCUMULATED_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'CurrentYTDDuration_AccumulatedOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益累計額 """
    CURRENT_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'CurrentYTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    CURRENT_YTD_DURATION__EFFECTIVE_PORTION_OF_CASH_FLOW_HEDGES_IFRS_MEMBER = 'CurrentYTDDuration_EffectivePortionOfCashFlowHedgesIFRSMember'
    """ キャッシュ・フロー・ヘッジの有効部分 """
    CURRENT_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'CurrentYTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    CURRENT_YTD_DURATION__EXCHANGE_DIFFERENCES_ON_TRANSLATION_OF_FOREIGN_OPERATIONS_IFRS_MEMBER = 'CurrentYTDDuration_ExchangeDifferencesOnTranslationOfForeignOperationsIFRSMember'
    """ 在外営業活動体の外貨換算差額 """
    CURRENT_YTD_DURATION__FINANCIAL_ASSETS_MEASURED_AT_FAIR_VALUE_THROUGH_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'CurrentYTDDuration_FinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益を通じて公正価値で測定する金融資産 """
    CURRENT_YTD_DURATION__NET_CHANGE_IN_FAIR_VALUE_OF_EQUITY_INSTRUMENTS_DESIGNATED_AS_MEASURED_AT_FAIR_VALUE_THROUGH_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'CurrentYTDDuration_NetChangeInFairValueOfEquityInstrumentsDesignatedAsMeasuredAtFairValueThroughOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益を通じて公正価値で測定するものとして指定した資本性金融商品の公正価値の純変動額 """
    CURRENT_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'CurrentYTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    CURRENT_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'CurrentYTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    CURRENT_YTD_DURATION__REMEASUREMENTS_OF_DEFINED_BENEFIT_PLANS_IFRS_MEMBER = 'CurrentYTDDuration_RemeasurementsOfDefinedBenefitPlansIFRSMember'
    """ 確定給付制度の再測定 """
    CURRENT_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'CurrentYTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    CURRENT_YTD_DURATION__SHARE_ACQUISITION_RIGHTS_IFRS_MEMBER = 'CurrentYTDDuration_ShareAcquisitionRightsIFRSMember'
    """ 新株予約権 """
    CURRENT_YTD_DURATION__SHARE_CAPITAL_IFRS_MEMBER = 'CurrentYTDDuration_ShareCapitalIFRSMember'
    """ 資本金 """
    CURRENT_YTD_DURATION__SHARE_OF_OTHER_COMPREHENSIVE_INCOME_OF_INVESTMENTS_ACCOUNTED_FOR_USING_EQUITY_METHOD_IFRS_MEMBER = 'CurrentYTDDuration_ShareOfOtherComprehensiveIncomeOfInvestmentsAccountedForUsingEquityMethodIFRSMember'
    """ 持分法によるその他の包括利益 """
    CURRENT_YTD_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'CurrentYTDDuration_TreasurySharesIFRSMember'
    """ 自己株式 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'CurrentYearDuration_CapitalSurplusIFRSMember'
    """ 当年度会計期間資本剰余金 """
    CURRENT_YEAR_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'CurrentYearDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 当年度会計期間親会社の所有者に帰属する持分 """
    CURRENT_YEAR_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'CurrentYearDuration_NonControllingInterestsIFRSMember'
    """ 当年度会計期間非支配持分 """
    CURRENT_YEAR_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'CurrentYearDuration_OtherComponentsOfEquityIFRSMember'
    """ 当年度会計期間その他の資本の構成要素 """
    CURRENT_YEAR_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'CurrentYearDuration_RetainedEarningsIFRSMember'
    """ 当年度会計期間利益剰余金 """
    CURRENT_YEAR_DURATION__SHARE_CAPITAL_IFRS_MEMBER = 'CurrentYearDuration_ShareCapitalIFRSMember'
    """ 当年度会計期間資本金 """
    CURRENT_YEAR_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'CurrentYearDuration_TreasurySharesIFRSMember'
    """ 当年度会計期間自己株式 """
    PRIOR1_QUARTER_DURATION = 'Prior1QuarterDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__ACCUMULATED_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'Prior1YTDDuration_AccumulatedOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益累計額 """
    PRIOR1_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'Prior1YTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    PRIOR1_YTD_DURATION__EFFECTIVE_PORTION_OF_CASH_FLOW_HEDGES_IFRS_MEMBER = 'Prior1YTDDuration_EffectivePortionOfCashFlowHedgesIFRSMember'
    """ キャッシュ・フロー・ヘッジの有効部分 """
    PRIOR1_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'Prior1YTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    PRIOR1_YTD_DURATION__EXCHANGE_DIFFERENCES_ON_TRANSLATION_OF_FOREIGN_OPERATIONS_IFRS_MEMBER = 'Prior1YTDDuration_ExchangeDifferencesOnTranslationOfForeignOperationsIFRSMember'
    """ 在外営業活動体の外貨換算差額 """
    PRIOR1_YTD_DURATION__FINANCIAL_ASSETS_MEASURED_AT_FAIR_VALUE_THROUGH_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'Prior1YTDDuration_FinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益を通じて公正価値で測定する金融資産 """
    PRIOR1_YTD_DURATION__NET_CHANGE_IN_FAIR_VALUE_OF_EQUITY_INSTRUMENTS_DESIGNATED_AS_MEASURED_AT_FAIR_VALUE_THROUGH_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'Prior1YTDDuration_NetChangeInFairValueOfEquityInstrumentsDesignatedAsMeasuredAtFairValueThroughOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益を通じて公正価値で測定するものとして指定した資本性金融商品の公正価値の純変動額 """
    PRIOR1_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'Prior1YTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    PRIOR1_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'Prior1YTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    PRIOR1_YTD_DURATION__REMEASUREMENTS_OF_DEFINED_BENEFIT_PLANS_IFRS_MEMBER = 'Prior1YTDDuration_RemeasurementsOfDefinedBenefitPlansIFRSMember'
    """ 確定給付制度の再測定 """
    PRIOR1_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'Prior1YTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    PRIOR1_YTD_DURATION__SHARE_ACQUISITION_RIGHTS_IFRS_MEMBER = 'Prior1YTDDuration_ShareAcquisitionRightsIFRSMember'
    """ 新株予約権 """
    PRIOR1_YTD_DURATION__SHARE_CAPITAL_IFRS_MEMBER = 'Prior1YTDDuration_ShareCapitalIFRSMember'
    """ 資本金 """
    PRIOR1_YTD_DURATION__SHARE_OF_OTHER_COMPREHENSIVE_INCOME_OF_INVESTMENTS_ACCOUNTED_FOR_USING_EQUITY_METHOD_IFRS_MEMBER = 'Prior1YTDDuration_ShareOfOtherComprehensiveIncomeOfInvestmentsAccountedForUsingEquityMethodIFRSMember'
    """ 持分法によるその他の包括利益 """
    PRIOR1_YTD_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'Prior1YTDDuration_TreasurySharesIFRSMember'
    """ 自己株式 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'Prior1YearDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    PRIOR1_YEAR_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'Prior1YearDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    PRIOR1_YEAR_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'Prior1YearDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    PRIOR1_YEAR_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'Prior1YearDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    PRIOR1_YEAR_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'Prior1YearDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    PRIOR1_YEAR_DURATION__SHARE_CAPITAL_IFRS_MEMBER = 'Prior1YearDuration_ShareCapitalIFRSMember'
    """ 資本金 """
    PRIOR1_YEAR_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'Prior1YearDuration_TreasurySharesIFRSMember'
    """ 自己株式 """


class ContinuingOperationsBasicEarningsLossPerShareIFRS(Enum):
    """"継続事業、基本的１株当たり当期利益（△損失）（IFRS）"""
    CURRENT_QUARTER_DURATION = 'CurrentQuarterDuration'
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_QUARTER_DURATION = 'Prior1QuarterDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ContinuingOperationsDilutedEarningsLossPerShareIFRS(Enum):
    """"継続事業、希薄化後１株当たり当期利益（△損失）（IFRS）"""
    CURRENT_QUARTER_DURATION = 'CurrentQuarterDuration'
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_QUARTER_DURATION = 'Prior1QuarterDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ContractAssetsCAIFRS(Enum):
    """"契約資産、流動資産（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ContractAssetsNCAIFRS(Enum):
    """"契約資産、非流動資産（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ContractLiabilitiesCLIFRS(Enum):
    """"契約負債、流動負債（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ContractLiabilitiesNCLIFRS(Enum):
    """"契約負債、非流動負債（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class CostOfSalesIFRS(Enum):
    """"売上原価（IFRS）"""
    CURRENT_QUARTER_DURATION = 'CurrentQuarterDuration'
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_QUARTER_DURATION = 'Prior1QuarterDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class CumulativeEffectOfAccountingChangeIFRS(Enum):
    """"会計方針の変更による累積的影響額（IFRS）"""
    PRIOR2_YEAR_INSTANT = 'Prior2YearInstant'
    PRIOR2_YEAR_INSTANT__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'Prior2YearInstant_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    PRIOR2_YEAR_INSTANT__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'Prior2YearInstant_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    PRIOR2_YEAR_INSTANT__RETAINED_EARNINGS_IFRS_MEMBER = 'Prior2YearInstant_RetainedEarningsIFRSMember'
    """ 利益剰余金 """


class CurrentAssetsIFRS(Enum):
    """"流動資産（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR2_YEAR_INSTANT = 'Prior2YearInstant'


class CurrentAssetsOtherThanAssetsHeldForSaleCAIFRS(Enum):
    """"売却目的で保有する資産を除く流動資産（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class DecreaseIncreaseInContractAssetsOpeCFIFRS(Enum):
    """"契約資産の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DecreaseIncreaseInInventoriesOpeCFIFRS(Enum):
    """"棚卸資産の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class DecreaseIncreaseInRetirementBenefitAssetOpeCFIFRS(Enum):
    """"退職給付に係る資産の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DecreaseIncreaseInTradeAndOtherReceivables2OpeCFIFRS(Enum):
    """"売上債権及びその他の債権の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DecreaseIncreaseInTradeAndOtherReceivablesOpeCFIFRS(Enum):
    """"営業債権及びその他の債権の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class DecreaseIncreaseInTradeReceivables2OpeCFIFRS(Enum):
    """"売上債権の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DecreaseIncreaseInTradeReceivablesOpeCFIFRS(Enum):
    """"営業債権の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DeferredIncomeCLIFRS(Enum):
    """"繰延収益、流動負債（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class DeferredIncomeNCLIFRS(Enum):
    """"繰延収益、非流動負債（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class DeferredTaxAssetsIFRS(Enum):
    """"繰延税金資産（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR2_YEAR_INSTANT = 'Prior2YearInstant'


class DeferredTaxLiabilitiesIFRS(Enum):
    """"繰延税金負債（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR2_YEAR_INSTANT = 'Prior2YearInstant'


class DepreciationAndAmortizationOfIntangibleAssetsOpeCFIFRS(Enum):
    """"減価償却費及び無形資産償却費、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DepreciationAndAmortizationOpeCFIFRS(Enum):
    """"減価償却費及び償却費、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class DepreciationAndAmortizationOperatingExpensesIFRS(Enum):
    """"減価償却費及び償却費、営業費用（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'CurrentYTDDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    CURRENT_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'CurrentYTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    CURRENT_YTD_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'CurrentYTDDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__OTHER_REPORTABLE_SEGMENTS_MEMBER = 'CurrentYearDuration_OtherReportableSegmentsMember'
    """ 当年度会計期間その他 """
    CURRENT_YEAR_DURATION__RECONCILING_ITEMS_MEMBER = 'CurrentYearDuration_ReconcilingItemsMember'
    """ 当年度会計期間調整項目 """
    CURRENT_YEAR_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'CurrentYearDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 当年度会計期間事業セグメント合計 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'Prior1YTDDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    PRIOR1_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1YTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_YTD_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'Prior1YTDDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__OTHER_REPORTABLE_SEGMENTS_MEMBER = 'Prior1YearDuration_OtherReportableSegmentsMember'
    """ その他 """
    PRIOR1_YEAR_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1YearDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_YEAR_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1YearDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """


class DerivativeAssetsCAIFRS(Enum):
    """"デリバティブ資産、流動資産（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class DerivativeAssetsNCAIFRS(Enum):
    """"デリバティブ資産、非流動資産（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class DerivativeLiabilitiesCLIFRS(Enum):
    """"デリバティブ負債、流動負債（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class DerivativeLiabilitiesNCLIFRS(Enum):
    """"デリバティブ負債、非流動負債（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class DilutedEarningsLossPerShareIFRS(Enum):
    """"希薄化後１株当たり当期利益（△損失）（IFRS）"""
    CURRENT_QUARTER_DURATION = 'CurrentQuarterDuration'
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_QUARTER_DURATION = 'Prior1QuarterDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class DiscontinuedOperationsBasicEarningsLossPerShareIFRS(Enum):
    """"非継続事業、基本的１株当たり当期利益（△損失）（IFRS）"""
    CURRENT_QUARTER_DURATION = 'CurrentQuarterDuration'
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_QUARTER_DURATION = 'Prior1QuarterDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DiscontinuedOperationsDilutedEarningsLossPerShareIFRS(Enum):
    """"非継続事業、希薄化後１株当たり当期利益（△損失）（IFRS）"""
    CURRENT_QUARTER_DURATION = 'CurrentQuarterDuration'
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_QUARTER_DURATION = 'Prior1QuarterDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DisposalOfSubsidiariesSSIFRS(Enum):
    """"子会社の支配喪失に伴う変動、持分変動計算書（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'CurrentYTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    CURRENT_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'CurrentYTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    CURRENT_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'CurrentYTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'Prior1YTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    PRIOR1_YTD_DURATION__FINANCIAL_ASSETS_MEASURED_AT_FAIR_VALUE_THROUGH_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'Prior1YTDDuration_FinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益を通じて公正価値で測定する金融資産 """
    PRIOR1_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'Prior1YTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    PRIOR1_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'Prior1YTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    PRIOR1_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'Prior1YTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """


class DisposalOfTreasurySharesSSIFRS(Enum):
    """"自己株式の処分、持分変動計算書（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__ACCUMULATED_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'CurrentYTDDuration_AccumulatedOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益累計額 """
    CURRENT_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'CurrentYTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    CURRENT_YTD_DURATION__EFFECTIVE_PORTION_OF_CASH_FLOW_HEDGES_IFRS_MEMBER = 'CurrentYTDDuration_EffectivePortionOfCashFlowHedgesIFRSMember'
    """ キャッシュ・フロー・ヘッジの有効部分 """
    CURRENT_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'CurrentYTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    CURRENT_YTD_DURATION__EXCHANGE_DIFFERENCES_ON_TRANSLATION_OF_FOREIGN_OPERATIONS_IFRS_MEMBER = 'CurrentYTDDuration_ExchangeDifferencesOnTranslationOfForeignOperationsIFRSMember'
    """ 在外営業活動体の外貨換算差額 """
    CURRENT_YTD_DURATION__FINANCIAL_ASSETS_MEASURED_AT_FAIR_VALUE_THROUGH_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'CurrentYTDDuration_FinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益を通じて公正価値で測定する金融資産 """
    CURRENT_YTD_DURATION__NET_CHANGE_IN_FAIR_VALUE_OF_EQUITY_INSTRUMENTS_DESIGNATED_AS_MEASURED_AT_FAIR_VALUE_THROUGH_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'CurrentYTDDuration_NetChangeInFairValueOfEquityInstrumentsDesignatedAsMeasuredAtFairValueThroughOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益を通じて公正価値で測定するものとして指定した資本性金融商品の公正価値の純変動額 """
    CURRENT_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'CurrentYTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    CURRENT_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'CurrentYTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    CURRENT_YTD_DURATION__REMEASUREMENTS_OF_DEFINED_BENEFIT_PLANS_IFRS_MEMBER = 'CurrentYTDDuration_RemeasurementsOfDefinedBenefitPlansIFRSMember'
    """ 確定給付制度の再測定 """
    CURRENT_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'CurrentYTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    CURRENT_YTD_DURATION__SHARE_CAPITAL_IFRS_MEMBER = 'CurrentYTDDuration_ShareCapitalIFRSMember'
    """ 資本金 """
    CURRENT_YTD_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'CurrentYTDDuration_TreasurySharesIFRSMember'
    """ 自己株式 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'CurrentYearDuration_CapitalSurplusIFRSMember'
    """ 当年度会計期間資本剰余金 """
    CURRENT_YEAR_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'CurrentYearDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 当年度会計期間親会社の所有者に帰属する持分 """
    CURRENT_YEAR_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'CurrentYearDuration_OtherComponentsOfEquityIFRSMember'
    """ 当年度会計期間その他の資本の構成要素 """
    CURRENT_YEAR_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'CurrentYearDuration_TreasurySharesIFRSMember'
    """ 当年度会計期間自己株式 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__ACCUMULATED_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'Prior1YTDDuration_AccumulatedOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益累計額 """
    PRIOR1_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'Prior1YTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    PRIOR1_YTD_DURATION__EFFECTIVE_PORTION_OF_CASH_FLOW_HEDGES_IFRS_MEMBER = 'Prior1YTDDuration_EffectivePortionOfCashFlowHedgesIFRSMember'
    """ キャッシュ・フロー・ヘッジの有効部分 """
    PRIOR1_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'Prior1YTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    PRIOR1_YTD_DURATION__EXCHANGE_DIFFERENCES_ON_TRANSLATION_OF_FOREIGN_OPERATIONS_IFRS_MEMBER = 'Prior1YTDDuration_ExchangeDifferencesOnTranslationOfForeignOperationsIFRSMember'
    """ 在外営業活動体の外貨換算差額 """
    PRIOR1_YTD_DURATION__FINANCIAL_ASSETS_MEASURED_AT_FAIR_VALUE_THROUGH_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'Prior1YTDDuration_FinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益を通じて公正価値で測定する金融資産 """
    PRIOR1_YTD_DURATION__NET_CHANGE_IN_FAIR_VALUE_OF_EQUITY_INSTRUMENTS_DESIGNATED_AS_MEASURED_AT_FAIR_VALUE_THROUGH_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'Prior1YTDDuration_NetChangeInFairValueOfEquityInstrumentsDesignatedAsMeasuredAtFairValueThroughOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益を通じて公正価値で測定するものとして指定した資本性金融商品の公正価値の純変動額 """
    PRIOR1_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'Prior1YTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    PRIOR1_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'Prior1YTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    PRIOR1_YTD_DURATION__REMEASUREMENTS_OF_DEFINED_BENEFIT_PLANS_IFRS_MEMBER = 'Prior1YTDDuration_RemeasurementsOfDefinedBenefitPlansIFRSMember'
    """ 確定給付制度の再測定 """
    PRIOR1_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'Prior1YTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    PRIOR1_YTD_DURATION__SHARE_CAPITAL_IFRS_MEMBER = 'Prior1YTDDuration_ShareCapitalIFRSMember'
    """ 資本金 """
    PRIOR1_YTD_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'Prior1YTDDuration_TreasurySharesIFRSMember'
    """ 自己株式 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'Prior1YearDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    PRIOR1_YEAR_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'Prior1YearDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    PRIOR1_YEAR_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'Prior1YearDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    PRIOR1_YEAR_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'Prior1YearDuration_TreasurySharesIFRSMember'
    """ 自己株式 """


class DividendIncomeOpeCFIFRS(Enum):
    """"受取配当金、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DividendsPaidFinCFIFRS(Enum):
    """"配当金の支払額、財務活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class DividendsPaidToNonControllingInterestsFinCFIFRS(Enum):
    """"非支配持分への配当金の支払額、財務活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DividendsPaidToOwnersOfParentFinCFIFRS(Enum):
    """"親会社の所有者への配当金の支払額、財務活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DividendsReceivedOpeCFIFRS(Enum):
    """"配当金の受取額、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DividendsSSIFRS(Enum):
    """"配当金、持分変動計算書（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__ACCUMULATED_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'CurrentYTDDuration_AccumulatedOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益累計額 """
    CURRENT_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'CurrentYTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    CURRENT_YTD_DURATION__EFFECTIVE_PORTION_OF_CASH_FLOW_HEDGES_IFRS_MEMBER = 'CurrentYTDDuration_EffectivePortionOfCashFlowHedgesIFRSMember'
    """ キャッシュ・フロー・ヘッジの有効部分 """
    CURRENT_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'CurrentYTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    CURRENT_YTD_DURATION__EXCHANGE_DIFFERENCES_ON_TRANSLATION_OF_FOREIGN_OPERATIONS_IFRS_MEMBER = 'CurrentYTDDuration_ExchangeDifferencesOnTranslationOfForeignOperationsIFRSMember'
    """ 在外営業活動体の外貨換算差額 """
    CURRENT_YTD_DURATION__FINANCIAL_ASSETS_MEASURED_AT_FAIR_VALUE_THROUGH_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'CurrentYTDDuration_FinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益を通じて公正価値で測定する金融資産 """
    CURRENT_YTD_DURATION__NET_CHANGE_IN_FAIR_VALUE_OF_EQUITY_INSTRUMENTS_DESIGNATED_AS_MEASURED_AT_FAIR_VALUE_THROUGH_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'CurrentYTDDuration_NetChangeInFairValueOfEquityInstrumentsDesignatedAsMeasuredAtFairValueThroughOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益を通じて公正価値で測定するものとして指定した資本性金融商品の公正価値の純変動額 """
    CURRENT_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'CurrentYTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    CURRENT_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'CurrentYTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    CURRENT_YTD_DURATION__REMEASUREMENTS_OF_DEFINED_BENEFIT_PLANS_IFRS_MEMBER = 'CurrentYTDDuration_RemeasurementsOfDefinedBenefitPlansIFRSMember'
    """ 確定給付制度の再測定 """
    CURRENT_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'CurrentYTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    CURRENT_YTD_DURATION__SHARE_CAPITAL_IFRS_MEMBER = 'CurrentYTDDuration_ShareCapitalIFRSMember'
    """ 資本金 """
    CURRENT_YTD_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'CurrentYTDDuration_TreasurySharesIFRSMember'
    """ 自己株式 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'CurrentYearDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 当年度会計期間親会社の所有者に帰属する持分 """
    CURRENT_YEAR_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'CurrentYearDuration_RetainedEarningsIFRSMember'
    """ 当年度会計期間利益剰余金 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__ACCUMULATED_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'Prior1YTDDuration_AccumulatedOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益累計額 """
    PRIOR1_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'Prior1YTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    PRIOR1_YTD_DURATION__EFFECTIVE_PORTION_OF_CASH_FLOW_HEDGES_IFRS_MEMBER = 'Prior1YTDDuration_EffectivePortionOfCashFlowHedgesIFRSMember'
    """ キャッシュ・フロー・ヘッジの有効部分 """
    PRIOR1_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'Prior1YTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    PRIOR1_YTD_DURATION__EXCHANGE_DIFFERENCES_ON_TRANSLATION_OF_FOREIGN_OPERATIONS_IFRS_MEMBER = 'Prior1YTDDuration_ExchangeDifferencesOnTranslationOfForeignOperationsIFRSMember'
    """ 在外営業活動体の外貨換算差額 """
    PRIOR1_YTD_DURATION__FINANCIAL_ASSETS_MEASURED_AT_FAIR_VALUE_THROUGH_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'Prior1YTDDuration_FinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益を通じて公正価値で測定する金融資産 """
    PRIOR1_YTD_DURATION__NET_CHANGE_IN_FAIR_VALUE_OF_EQUITY_INSTRUMENTS_DESIGNATED_AS_MEASURED_AT_FAIR_VALUE_THROUGH_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'Prior1YTDDuration_NetChangeInFairValueOfEquityInstrumentsDesignatedAsMeasuredAtFairValueThroughOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益を通じて公正価値で測定するものとして指定した資本性金融商品の公正価値の純変動額 """
    PRIOR1_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'Prior1YTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    PRIOR1_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'Prior1YTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    PRIOR1_YTD_DURATION__REMEASUREMENTS_OF_DEFINED_BENEFIT_PLANS_IFRS_MEMBER = 'Prior1YTDDuration_RemeasurementsOfDefinedBenefitPlansIFRSMember'
    """ 確定給付制度の再測定 """
    PRIOR1_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'Prior1YTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    PRIOR1_YTD_DURATION__SHARE_CAPITAL_IFRS_MEMBER = 'Prior1YTDDuration_ShareCapitalIFRSMember'
    """ 資本金 """
    PRIOR1_YTD_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'Prior1YTDDuration_TreasurySharesIFRSMember'
    """ 自己株式 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'Prior1YearDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    PRIOR1_YEAR_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'Prior1YearDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """


class EffectOfExchangeRateChangesOnCashAndCashEquivalentsIFRS(Enum):
    """"現金及び現金同等物の為替変動による影響（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class EffectivePortionOfCashFlowHedgesNetOfTaxItemsThatMayBeReclassifiedToProfitOrLossOCIIFRS(Enum):
    """"キャッシュ・フロー・ヘッジの有効部分（税引後）、純損益に振り替えられる可能性のあるその他の包括利益（IFRS）"""
    CURRENT_QUARTER_DURATION = 'CurrentQuarterDuration'
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_QUARTER_DURATION = 'Prior1QuarterDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class EmployeeBenefitsNCLIFRS(Enum):
    """"従業員給付、非流動負債（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class EquityAttributableToOwnersOfParentIFRS(Enum):
    """"親会社の所有者に帰属する持分（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR2_YEAR_INSTANT = 'Prior2YearInstant'


class EquityIFRS(Enum):
    """"資本（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_QUARTER_INSTANT__ACCUMULATED_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'CurrentQuarterInstant_AccumulatedOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益累計額 """
    CURRENT_QUARTER_INSTANT__CAPITAL_SURPLUS_IFRS_MEMBER = 'CurrentQuarterInstant_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    CURRENT_QUARTER_INSTANT__EFFECTIVE_PORTION_OF_CASH_FLOW_HEDGES_IFRS_MEMBER = 'CurrentQuarterInstant_EffectivePortionOfCashFlowHedgesIFRSMember'
    """ キャッシュ・フロー・ヘッジの有効部分 """
    CURRENT_QUARTER_INSTANT__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'CurrentQuarterInstant_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    CURRENT_QUARTER_INSTANT__EXCHANGE_DIFFERENCES_ON_TRANSLATION_OF_FOREIGN_OPERATIONS_IFRS_MEMBER = 'CurrentQuarterInstant_ExchangeDifferencesOnTranslationOfForeignOperationsIFRSMember'
    """ 在外営業活動体の外貨換算差額 """
    CURRENT_QUARTER_INSTANT__FINANCIAL_ASSETS_MEASURED_AT_FAIR_VALUE_THROUGH_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'CurrentQuarterInstant_FinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益を通じて公正価値で測定する金融資産 """
    CURRENT_QUARTER_INSTANT__NET_CHANGE_IN_FAIR_VALUE_OF_EQUITY_INSTRUMENTS_DESIGNATED_AS_MEASURED_AT_FAIR_VALUE_THROUGH_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'CurrentQuarterInstant_NetChangeInFairValueOfEquityInstrumentsDesignatedAsMeasuredAtFairValueThroughOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益を通じて公正価値で測定するものとして指定した資本性金融商品の公正価値の純変動額 """
    CURRENT_QUARTER_INSTANT__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'CurrentQuarterInstant_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    CURRENT_QUARTER_INSTANT__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'CurrentQuarterInstant_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    CURRENT_QUARTER_INSTANT__REMEASUREMENTS_OF_DEFINED_BENEFIT_PLANS_IFRS_MEMBER = 'CurrentQuarterInstant_RemeasurementsOfDefinedBenefitPlansIFRSMember'
    """ 確定給付制度の再測定 """
    CURRENT_QUARTER_INSTANT__RETAINED_EARNINGS_IFRS_MEMBER = 'CurrentQuarterInstant_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    CURRENT_QUARTER_INSTANT__SHARE_ACQUISITION_RIGHTS_IFRS_MEMBER = 'CurrentQuarterInstant_ShareAcquisitionRightsIFRSMember'
    """ 新株予約権 """
    CURRENT_QUARTER_INSTANT__SHARE_CAPITAL_IFRS_MEMBER = 'CurrentQuarterInstant_ShareCapitalIFRSMember'
    """ 資本金 """
    CURRENT_QUARTER_INSTANT__SHARE_OF_OTHER_COMPREHENSIVE_INCOME_OF_INVESTMENTS_ACCOUNTED_FOR_USING_EQUITY_METHOD_IFRS_MEMBER = 'CurrentQuarterInstant_ShareOfOtherComprehensiveIncomeOfInvestmentsAccountedForUsingEquityMethodIFRSMember'
    """ 持分法によるその他の包括利益 """
    CURRENT_QUARTER_INSTANT__TREASURY_SHARES_IFRS_MEMBER = 'CurrentQuarterInstant_TreasurySharesIFRSMember'
    """ 自己株式 """
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    CURRENT_YEAR_INSTANT__CAPITAL_SURPLUS_IFRS_MEMBER = 'CurrentYearInstant_CapitalSurplusIFRSMember'
    """ 当年度時点資本剰余金 """
    CURRENT_YEAR_INSTANT__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'CurrentYearInstant_EquityAttributableToOwnersOfParentIFRSMember'
    """ 当年度時点親会社の所有者に帰属する持分 """
    CURRENT_YEAR_INSTANT__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'CurrentYearInstant_NonControllingInterestsIFRSMember'
    """ 当年度時点非支配持分 """
    CURRENT_YEAR_INSTANT__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'CurrentYearInstant_OtherComponentsOfEquityIFRSMember'
    """ 当年度時点その他の資本の構成要素 """
    CURRENT_YEAR_INSTANT__RETAINED_EARNINGS_IFRS_MEMBER = 'CurrentYearInstant_RetainedEarningsIFRSMember'
    """ 当年度時点利益剰余金 """
    CURRENT_YEAR_INSTANT__SHARE_CAPITAL_IFRS_MEMBER = 'CurrentYearInstant_ShareCapitalIFRSMember'
    """ 当年度時点資本金 """
    CURRENT_YEAR_INSTANT__TREASURY_SHARES_IFRS_MEMBER = 'CurrentYearInstant_TreasurySharesIFRSMember'
    """ 当年度時点自己株式 """
    PRIOR1_QUARTER_INSTANT = 'Prior1QuarterInstant'
    PRIOR1_QUARTER_INSTANT__ACCUMULATED_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'Prior1QuarterInstant_AccumulatedOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益累計額 """
    PRIOR1_QUARTER_INSTANT__CAPITAL_SURPLUS_IFRS_MEMBER = 'Prior1QuarterInstant_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    PRIOR1_QUARTER_INSTANT__EFFECTIVE_PORTION_OF_CASH_FLOW_HEDGES_IFRS_MEMBER = 'Prior1QuarterInstant_EffectivePortionOfCashFlowHedgesIFRSMember'
    """ キャッシュ・フロー・ヘッジの有効部分 """
    PRIOR1_QUARTER_INSTANT__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'Prior1QuarterInstant_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    PRIOR1_QUARTER_INSTANT__EXCHANGE_DIFFERENCES_ON_TRANSLATION_OF_FOREIGN_OPERATIONS_IFRS_MEMBER = 'Prior1QuarterInstant_ExchangeDifferencesOnTranslationOfForeignOperationsIFRSMember'
    """ 在外営業活動体の外貨換算差額 """
    PRIOR1_QUARTER_INSTANT__FINANCIAL_ASSETS_MEASURED_AT_FAIR_VALUE_THROUGH_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'Prior1QuarterInstant_FinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益を通じて公正価値で測定する金融資産 """
    PRIOR1_QUARTER_INSTANT__NET_CHANGE_IN_FAIR_VALUE_OF_EQUITY_INSTRUMENTS_DESIGNATED_AS_MEASURED_AT_FAIR_VALUE_THROUGH_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'Prior1QuarterInstant_NetChangeInFairValueOfEquityInstrumentsDesignatedAsMeasuredAtFairValueThroughOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益を通じて公正価値で測定するものとして指定した資本性金融商品の公正価値の純変動額 """
    PRIOR1_QUARTER_INSTANT__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'Prior1QuarterInstant_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    PRIOR1_QUARTER_INSTANT__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'Prior1QuarterInstant_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    PRIOR1_QUARTER_INSTANT__REMEASUREMENTS_OF_DEFINED_BENEFIT_PLANS_IFRS_MEMBER = 'Prior1QuarterInstant_RemeasurementsOfDefinedBenefitPlansIFRSMember'
    """ 確定給付制度の再測定 """
    PRIOR1_QUARTER_INSTANT__RETAINED_EARNINGS_IFRS_MEMBER = 'Prior1QuarterInstant_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    PRIOR1_QUARTER_INSTANT__SHARE_ACQUISITION_RIGHTS_IFRS_MEMBER = 'Prior1QuarterInstant_ShareAcquisitionRightsIFRSMember'
    """ 新株予約権 """
    PRIOR1_QUARTER_INSTANT__SHARE_CAPITAL_IFRS_MEMBER = 'Prior1QuarterInstant_ShareCapitalIFRSMember'
    """ 資本金 """
    PRIOR1_QUARTER_INSTANT__SHARE_OF_OTHER_COMPREHENSIVE_INCOME_OF_INVESTMENTS_ACCOUNTED_FOR_USING_EQUITY_METHOD_IFRS_MEMBER = 'Prior1QuarterInstant_ShareOfOtherComprehensiveIncomeOfInvestmentsAccountedForUsingEquityMethodIFRSMember'
    """ 持分法によるその他の包括利益 """
    PRIOR1_QUARTER_INSTANT__TREASURY_SHARES_IFRS_MEMBER = 'Prior1QuarterInstant_TreasurySharesIFRSMember'
    """ 自己株式 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR1_YEAR_INSTANT__ACCUMULATED_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'Prior1YearInstant_AccumulatedOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益累計額 """
    PRIOR1_YEAR_INSTANT__CAPITAL_SURPLUS_IFRS_MEMBER = 'Prior1YearInstant_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    PRIOR1_YEAR_INSTANT__EFFECTIVE_PORTION_OF_CASH_FLOW_HEDGES_IFRS_MEMBER = 'Prior1YearInstant_EffectivePortionOfCashFlowHedgesIFRSMember'
    """ キャッシュ・フロー・ヘッジの有効部分 """
    PRIOR1_YEAR_INSTANT__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'Prior1YearInstant_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    PRIOR1_YEAR_INSTANT__EXCHANGE_DIFFERENCES_ON_TRANSLATION_OF_FOREIGN_OPERATIONS_IFRS_MEMBER = 'Prior1YearInstant_ExchangeDifferencesOnTranslationOfForeignOperationsIFRSMember'
    """ 在外営業活動体の外貨換算差額 """
    PRIOR1_YEAR_INSTANT__FINANCIAL_ASSETS_MEASURED_AT_FAIR_VALUE_THROUGH_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'Prior1YearInstant_FinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益を通じて公正価値で測定する金融資産 """
    PRIOR1_YEAR_INSTANT__NET_CHANGE_IN_FAIR_VALUE_OF_EQUITY_INSTRUMENTS_DESIGNATED_AS_MEASURED_AT_FAIR_VALUE_THROUGH_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'Prior1YearInstant_NetChangeInFairValueOfEquityInstrumentsDesignatedAsMeasuredAtFairValueThroughOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益を通じて公正価値で測定するものとして指定した資本性金融商品の公正価値の純変動額 """
    PRIOR1_YEAR_INSTANT__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'Prior1YearInstant_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    PRIOR1_YEAR_INSTANT__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'Prior1YearInstant_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    PRIOR1_YEAR_INSTANT__REMEASUREMENTS_OF_DEFINED_BENEFIT_PLANS_IFRS_MEMBER = 'Prior1YearInstant_RemeasurementsOfDefinedBenefitPlansIFRSMember'
    """ 確定給付制度の再測定 """
    PRIOR1_YEAR_INSTANT__RETAINED_EARNINGS_IFRS_MEMBER = 'Prior1YearInstant_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    PRIOR1_YEAR_INSTANT__SHARE_ACQUISITION_RIGHTS_IFRS_MEMBER = 'Prior1YearInstant_ShareAcquisitionRightsIFRSMember'
    """ 新株予約権 """
    PRIOR1_YEAR_INSTANT__SHARE_CAPITAL_IFRS_MEMBER = 'Prior1YearInstant_ShareCapitalIFRSMember'
    """ 資本金 """
    PRIOR1_YEAR_INSTANT__SHARE_OF_OTHER_COMPREHENSIVE_INCOME_OF_INVESTMENTS_ACCOUNTED_FOR_USING_EQUITY_METHOD_IFRS_MEMBER = 'Prior1YearInstant_ShareOfOtherComprehensiveIncomeOfInvestmentsAccountedForUsingEquityMethodIFRSMember'
    """ 持分法によるその他の包括利益 """
    PRIOR1_YEAR_INSTANT__TREASURY_SHARES_IFRS_MEMBER = 'Prior1YearInstant_TreasurySharesIFRSMember'
    """ 自己株式 """
    PRIOR2_YEAR_INSTANT = 'Prior2YearInstant'
    PRIOR2_YEAR_INSTANT__ACCUMULATED_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'Prior2YearInstant_AccumulatedOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益累計額 """
    PRIOR2_YEAR_INSTANT__CAPITAL_SURPLUS_IFRS_MEMBER = 'Prior2YearInstant_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    PRIOR2_YEAR_INSTANT__EFFECTIVE_PORTION_OF_CASH_FLOW_HEDGES_IFRS_MEMBER = 'Prior2YearInstant_EffectivePortionOfCashFlowHedgesIFRSMember'
    """ キャッシュ・フロー・ヘッジの有効部分 """
    PRIOR2_YEAR_INSTANT__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'Prior2YearInstant_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    PRIOR2_YEAR_INSTANT__EXCHANGE_DIFFERENCES_ON_TRANSLATION_OF_FOREIGN_OPERATIONS_IFRS_MEMBER = 'Prior2YearInstant_ExchangeDifferencesOnTranslationOfForeignOperationsIFRSMember'
    """ 在外営業活動体の外貨換算差額 """
    PRIOR2_YEAR_INSTANT__FINANCIAL_ASSETS_MEASURED_AT_FAIR_VALUE_THROUGH_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'Prior2YearInstant_FinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益を通じて公正価値で測定する金融資産 """
    PRIOR2_YEAR_INSTANT__NET_CHANGE_IN_FAIR_VALUE_OF_EQUITY_INSTRUMENTS_DESIGNATED_AS_MEASURED_AT_FAIR_VALUE_THROUGH_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'Prior2YearInstant_NetChangeInFairValueOfEquityInstrumentsDesignatedAsMeasuredAtFairValueThroughOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益を通じて公正価値で測定するものとして指定した資本性金融商品の公正価値の純変動額 """
    PRIOR2_YEAR_INSTANT__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'Prior2YearInstant_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    PRIOR2_YEAR_INSTANT__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'Prior2YearInstant_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    PRIOR2_YEAR_INSTANT__REMEASUREMENTS_OF_DEFINED_BENEFIT_PLANS_IFRS_MEMBER = 'Prior2YearInstant_RemeasurementsOfDefinedBenefitPlansIFRSMember'
    """ 確定給付制度の再測定 """
    PRIOR2_YEAR_INSTANT__RETAINED_EARNINGS_IFRS_MEMBER = 'Prior2YearInstant_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    PRIOR2_YEAR_INSTANT__SHARE_ACQUISITION_RIGHTS_IFRS_MEMBER = 'Prior2YearInstant_ShareAcquisitionRightsIFRSMember'
    """ 新株予約権 """
    PRIOR2_YEAR_INSTANT__SHARE_CAPITAL_IFRS_MEMBER = 'Prior2YearInstant_ShareCapitalIFRSMember'
    """ 資本金 """
    PRIOR2_YEAR_INSTANT__SHARE_OF_OTHER_COMPREHENSIVE_INCOME_OF_INVESTMENTS_ACCOUNTED_FOR_USING_EQUITY_METHOD_IFRS_MEMBER = 'Prior2YearInstant_ShareOfOtherComprehensiveIncomeOfInvestmentsAccountedForUsingEquityMethodIFRSMember'
    """ 持分法によるその他の包括利益 """
    PRIOR2_YEAR_INSTANT__TREASURY_SHARES_IFRS_MEMBER = 'Prior2YearInstant_TreasurySharesIFRSMember'
    """ 自己株式 """


class ExchangeDifferencesOnTranslationOfForeignOperationsBeforeTaxItemsThatMayBeReclassifiedToProfitOrLossOCIIFRS(Enum):
    """"在外営業活動体の外貨換算差額（税引前）、純損益に振り替えられる可能性のあるその他の包括利益（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ExchangeDifferencesOnTranslationOfForeignOperationsNetOfTaxItemsThatMayBeReclassifiedToProfitOrLossOCIIFRS(Enum):
    """"在外営業活動体の外貨換算差額（税引後）、純損益に振り替えられる可能性のあるその他の包括利益（IFRS）"""
    CURRENT_QUARTER_DURATION = 'CurrentQuarterDuration'
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_QUARTER_DURATION = 'Prior1QuarterDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class ExerciseOfShareAcquisitionRightsSSIFRS(Enum):
    """"新株予約権の行使、持分変動計算書（IFRS）"""
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'Prior1YTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    PRIOR1_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'Prior1YTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    PRIOR1_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'Prior1YTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    PRIOR1_YTD_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'Prior1YTDDuration_TreasurySharesIFRSMember'
    """ 自己株式 """


class FinanceCostsIFRS(Enum):
    """"金融費用（IFRS）"""
    CURRENT_QUARTER_DURATION = 'CurrentQuarterDuration'
    CURRENT_QUARTER_DURATION__RECONCILING_ITEMS_MEMBER = 'CurrentQuarterDuration_ReconcilingItemsMember'
    """ 調整項目 """
    CURRENT_QUARTER_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'CurrentQuarterDuration_ReportableSegmentsMember'
    """ 報告セグメント """
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
    PRIOR1_QUARTER_DURATION = 'Prior1QuarterDuration'
    PRIOR1_QUARTER_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1QuarterDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_QUARTER_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'Prior1QuarterDuration_ReportableSegmentsMember'
    """ 報告セグメント """
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


class FinanceCostsOpeCFIFRS(Enum):
    """"金融費用、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class FinanceIncomeAndExpensesNetIFRS(Enum):
    """"金融収益・費用（純額）（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'CurrentYTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    CURRENT_YTD_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'CurrentYTDDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    CURRENT_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'CurrentYTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1YTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_YTD_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'Prior1YTDDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    PRIOR1_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1YTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """


class FinanceIncomeAndFinanceCostsOpeCFIFRS(Enum):
    """"金融収益及び金融費用、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class FinanceIncomeIFRS(Enum):
    """"金融収益（IFRS）"""
    CURRENT_QUARTER_DURATION = 'CurrentQuarterDuration'
    CURRENT_QUARTER_DURATION__RECONCILING_ITEMS_MEMBER = 'CurrentQuarterDuration_ReconcilingItemsMember'
    """ 調整項目 """
    CURRENT_QUARTER_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'CurrentQuarterDuration_ReportableSegmentsMember'
    """ 報告セグメント """
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
    PRIOR1_QUARTER_DURATION = 'Prior1QuarterDuration'
    PRIOR1_QUARTER_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1QuarterDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_QUARTER_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'Prior1QuarterDuration_ReportableSegmentsMember'
    """ 報告セグメント """
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


class FinanceIncomeOpeCFIFRS(Enum):
    """"金融収益、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class FinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncomeNetOfTaxItemsThatMayBeReclassifiedToProfitOrLossOCIIFRS(Enum):
    """"その他の包括利益を通じて公正価値で測定する金融資産（税引後）、純損益に振り替えられる可能性のあるその他の包括利益（IFRS）"""
    CURRENT_QUARTER_DURATION = 'CurrentQuarterDuration'
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_QUARTER_DURATION = 'Prior1QuarterDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ForeignExchangeLossGainOpeCFIFRS(Enum):
    """"為替差損益（△は益）、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ForfeitureOfShareAcquisitionRightsSSIFRS(Enum):
    """"新株予約権の失効、持分変動計算書（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'CurrentYTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    CURRENT_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'CurrentYTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    CURRENT_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'CurrentYTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    CURRENT_YTD_DURATION__SHARE_ACQUISITION_RIGHTS_IFRS_MEMBER = 'CurrentYTDDuration_ShareAcquisitionRightsIFRSMember'
    """ 新株予約権 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'CurrentYearDuration_CapitalSurplusIFRSMember'
    """ 当年度会計期間資本剰余金 """
    CURRENT_YEAR_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'CurrentYearDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 当年度会計期間親会社の所有者に帰属する持分 """
    CURRENT_YEAR_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'CurrentYearDuration_OtherComponentsOfEquityIFRSMember'
    """ 当年度会計期間その他の資本の構成要素 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'Prior1YTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    PRIOR1_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'Prior1YTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    PRIOR1_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'Prior1YTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    PRIOR1_YTD_DURATION__SHARE_ACQUISITION_RIGHTS_IFRS_MEMBER = 'Prior1YTDDuration_ShareAcquisitionRightsIFRSMember'
    """ 新株予約権 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'Prior1YearDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    PRIOR1_YEAR_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'Prior1YearDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    PRIOR1_YEAR_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'Prior1YearDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """


class GainOnBargainPurchaseIFRS(Enum):
    """"負ののれん発生益（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class GeneralAndAdministrativeExpensesIFRS(Enum):
    """"一般管理費（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class GoodwillAndIntangibleAssetsIFRS(Enum):
    """"のれん及び無形資産（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class GoodwillIFRS(Enum):
    """"のれん（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR2_YEAR_INSTANT = 'Prior2YearInstant'


class GrossProfitIFRS(Enum):
    """"売上総利益（IFRS）"""
    CURRENT_QUARTER_DURATION = 'CurrentQuarterDuration'
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_QUARTER_DURATION = 'Prior1QuarterDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class ImpairmentLossesPLIFRS(Enum):
    """"減損損失、損益（IFRS）"""
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
    CURRENT_YEAR_DURATION__OTHER_REPORTABLE_SEGMENTS_MEMBER = 'CurrentYearDuration_OtherReportableSegmentsMember'
    """ 当年度会計期間その他 """
    CURRENT_YEAR_DURATION__RECONCILING_ITEMS_MEMBER = 'CurrentYearDuration_ReconcilingItemsMember'
    """ 当年度会計期間調整項目 """
    CURRENT_YEAR_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'CurrentYearDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 当年度会計期間事業セグメント合計 """
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
    PRIOR1_YEAR_DURATION__OTHER_REPORTABLE_SEGMENTS_MEMBER = 'Prior1YearDuration_OtherReportableSegmentsMember'
    """ その他 """
    PRIOR1_YEAR_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1YearDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_YEAR_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1YearDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """


class ImpairmentLossesReversalOfImpairmentLossesOpeCFIFRS(Enum):
    """"減損損失（又は戻入れ）、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class IncomeTaxExpenseIFRS(Enum):
    """"法人所得税費用（IFRS）"""
    CURRENT_QUARTER_DURATION = 'CurrentQuarterDuration'
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
    PRIOR1_QUARTER_DURATION = 'Prior1QuarterDuration'
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


class IncomeTaxExpenseOpeCFIFRS(Enum):
    """"法人所得税費用、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncomeTaxesItemsThatWillNotBeReclassifiedToProfitOrLossOCIIFRS(Enum):
    """"法人所得税、純損益に振り替えられることのないその他の包括利益（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncomeTaxesPaidOpeCFIFRS(Enum):
    """"法人所得税の支払額、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class IncomeTaxesPayableCLIFRS(Enum):
    """"未払法人所得税、流動負債（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR2_YEAR_INSTANT = 'Prior2YearInstant'


class IncomeTaxesPayableLiabilitiesIFRS(Enum):
    """"未払法人所得税、負債（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class IncomeTaxesReceivableCAIFRS(Enum):
    """"未収法人所得税、流動資産（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR2_YEAR_INSTANT = 'Prior2YearInstant'


class IncomeTaxesRefundOpeCFIFRS(Enum):
    """"法人所得税の還付額、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class IncomeTaxesRefundPaidOpeCFIFRS(Enum):
    """"法人所得税の支払額又は還付額（△は支払）、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseByBusinessCombinationSSIFRS(Enum):
    """"企業結合による変動、持分変動計算書（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'CurrentYTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    CURRENT_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'CurrentYTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    CURRENT_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'CurrentYTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    CURRENT_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'CurrentYTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    CURRENT_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'CurrentYTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    CURRENT_YTD_DURATION__SHARE_CAPITAL_IFRS_MEMBER = 'CurrentYTDDuration_ShareCapitalIFRSMember'
    """ 資本金 """
    CURRENT_YTD_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'CurrentYTDDuration_TreasurySharesIFRSMember'
    """ 自己株式 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'Prior1YTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    PRIOR1_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'Prior1YTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    PRIOR1_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'Prior1YTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    PRIOR1_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'Prior1YTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    PRIOR1_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'Prior1YTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    PRIOR1_YTD_DURATION__SHARE_CAPITAL_IFRS_MEMBER = 'Prior1YTDDuration_ShareCapitalIFRSMember'
    """ 資本金 """
    PRIOR1_YTD_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'Prior1YTDDuration_TreasurySharesIFRSMember'
    """ 自己株式 """


class IncreaseDecreaseInContractLiabilitiesOpeCFIFRS(Enum):
    """"契約負債の増減額（△は減少）、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInProvisionsOpeCFIFRS(Enum):
    """"引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInRetirementBenefitLiabilityOpeCFIFRS(Enum):
    """"退職給付に係る負債の増減額（△は減少）、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInTradeAndOtherPayables2OpeCFIFRS(Enum):
    """"仕入債務及びその他の債務の増減額（△は減少）、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInTradeAndOtherPayablesOpeCFIFRS(Enum):
    """"営業債務及びその他の債務の増減額（△は減少）、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class IncreaseDecreaseInTradePayables3OpeCFIFRS(Enum):
    """"買入債務の増減額（△は減少）、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInTradePayablesOpeCFIFRS(Enum):
    """"営業債務の増減額（△は減少）、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseOrDecreaseInRetirementBenefitAssetOrLiabilityOpeCFIFRS(Enum):
    """"退職給付に係る資産及び負債の増減額、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IntangibleAssetsIFRS(Enum):
    """"無形資産（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR2_YEAR_INSTANT = 'Prior2YearInstant'


class InterestAndDividendIncomeOpeCFIFRS(Enum):
    """"受取利息及び受取配当金、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class InterestAndDividendsReceivedOpeCFIFRS(Enum):
    """"利息及び配当金の受取額、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class InterestBearingLiabilitiesCLIFRS(Enum):
    """"有利子負債、流動負債（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class InterestBearingLiabilitiesNCLIFRS(Enum):
    """"有利子負債、非流動負債（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class InterestExpensesOpeCFIFRS(Enum):
    """"支払利息、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class InterestIncomeOpeCFIFRS(Enum):
    """"受取利息、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class InterestPaidOpeCFIFRS(Enum):
    """"利息の支払額、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class InterestReceivedOpeCFIFRS(Enum):
    """"利息の受取額、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IntersegmentRevenueIFRS(Enum):
    """"セグメント間の売上収益（IFRS）"""
    CURRENT_QUARTER_DURATION = 'CurrentQuarterDuration'
    CURRENT_QUARTER_DURATION__RECONCILING_ITEMS_MEMBER = 'CurrentQuarterDuration_ReconcilingItemsMember'
    """ 調整項目 """
    CURRENT_QUARTER_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'CurrentQuarterDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
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
    CURRENT_YEAR_DURATION__OTHER_REPORTABLE_SEGMENTS_MEMBER = 'CurrentYearDuration_OtherReportableSegmentsMember'
    """ 当年度会計期間その他 """
    CURRENT_YEAR_DURATION__RECONCILING_ITEMS_MEMBER = 'CurrentYearDuration_ReconcilingItemsMember'
    """ 当年度会計期間調整項目 """
    CURRENT_YEAR_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'CurrentYearDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 当年度会計期間事業セグメント合計 """
    PRIOR1_QUARTER_DURATION = 'Prior1QuarterDuration'
    PRIOR1_QUARTER_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1QuarterDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_QUARTER_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'Prior1QuarterDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
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
    PRIOR1_YEAR_DURATION__OTHER_REPORTABLE_SEGMENTS_MEMBER = 'Prior1YearDuration_OtherReportableSegmentsMember'
    """ その他 """
    PRIOR1_YEAR_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1YearDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_YEAR_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1YearDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """


class IntersegmentSalesIFRS(Enum):
    """"セグメント間の売上高（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
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
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
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


class InventoriesCAIFRS(Enum):
    """"棚卸資産、流動資産（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR2_YEAR_INSTANT = 'Prior2YearInstant'


class InvestmentPropertyIFRS(Enum):
    """"投資不動産（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class InvestmentSecuritiesNCAIFRS(Enum):
    """"投資有価証券、非流動資産（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class InvestmentsAccountedForUsingEquityMethodIFRS(Enum):
    """"持分法で会計処理されている投資（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR2_YEAR_INSTANT = 'Prior2YearInstant'


class IssuanceOfNewSharesSSIFRS(Enum):
    """"新株の発行、持分変動計算書（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__ACCUMULATED_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'CurrentYTDDuration_AccumulatedOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益累計額 """
    CURRENT_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'CurrentYTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    CURRENT_YTD_DURATION__EFFECTIVE_PORTION_OF_CASH_FLOW_HEDGES_IFRS_MEMBER = 'CurrentYTDDuration_EffectivePortionOfCashFlowHedgesIFRSMember'
    """ キャッシュ・フロー・ヘッジの有効部分 """
    CURRENT_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'CurrentYTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    CURRENT_YTD_DURATION__EXCHANGE_DIFFERENCES_ON_TRANSLATION_OF_FOREIGN_OPERATIONS_IFRS_MEMBER = 'CurrentYTDDuration_ExchangeDifferencesOnTranslationOfForeignOperationsIFRSMember'
    """ 在外営業活動体の外貨換算差額 """
    CURRENT_YTD_DURATION__FINANCIAL_ASSETS_MEASURED_AT_FAIR_VALUE_THROUGH_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'CurrentYTDDuration_FinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益を通じて公正価値で測定する金融資産 """
    CURRENT_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'CurrentYTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    CURRENT_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'CurrentYTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    CURRENT_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'CurrentYTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    CURRENT_YTD_DURATION__SHARE_ACQUISITION_RIGHTS_IFRS_MEMBER = 'CurrentYTDDuration_ShareAcquisitionRightsIFRSMember'
    """ 新株予約権 """
    CURRENT_YTD_DURATION__SHARE_CAPITAL_IFRS_MEMBER = 'CurrentYTDDuration_ShareCapitalIFRSMember'
    """ 資本金 """
    CURRENT_YTD_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'CurrentYTDDuration_TreasurySharesIFRSMember'
    """ 自己株式 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__ACCUMULATED_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'Prior1YTDDuration_AccumulatedOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益累計額 """
    PRIOR1_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'Prior1YTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    PRIOR1_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'Prior1YTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    PRIOR1_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'Prior1YTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    PRIOR1_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'Prior1YTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    PRIOR1_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'Prior1YTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    PRIOR1_YTD_DURATION__SHARE_ACQUISITION_RIGHTS_IFRS_MEMBER = 'Prior1YTDDuration_ShareAcquisitionRightsIFRSMember'
    """ 新株予約権 """
    PRIOR1_YTD_DURATION__SHARE_CAPITAL_IFRS_MEMBER = 'Prior1YTDDuration_ShareCapitalIFRSMember'
    """ 資本金 """
    PRIOR1_YTD_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'Prior1YTDDuration_TreasurySharesIFRSMember'
    """ 自己株式 """


class LeaseLiabilitiesCLIFRS(Enum):
    """"リース負債、流動負債（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR2_YEAR_INSTANT = 'Prior2YearInstant'


class LeaseLiabilitiesNCLIFRS(Enum):
    """"リース負債、非流動負債（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR2_YEAR_INSTANT = 'Prior2YearInstant'


class LiabilitiesAndEquityIFRS(Enum):
    """"負債及び資本（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR2_YEAR_INSTANT = 'Prior2YearInstant'


class LiabilitiesDirectlyAssociatedWithAssetsHeldForSaleIFRS(Enum):
    """"売却目的で保有する資産に直接関連する負債（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class LiabilitiesIFRS(Enum):
    """"負債（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR2_YEAR_INSTANT = 'Prior2YearInstant'


class LiabilitiesOtherThanLiabilitiesDirectlyAssociatedWithAssetsHeldForSaleIFRS(Enum):
    """"売却目的で保有する資産に直接関連する負債を除く負債（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class LongTermDebtNCLIFRS(Enum):
    """"長期債務、非流動負債（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class LossGainOnSaleAndRetirementOfFixedAssetsOpeCFIFRS(Enum):
    """"固定資産除売却損益（△は益）、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossGainOnSaleAndRetirementOfPropertyPlantAndEquipmentAndIntangibleAssetsOpeCFIFRS(Enum):
    """"有形固定資産及び無形資産除売却損益（△は益）、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossGainOnSaleOfFixedAssetsOpeCFIFRS(Enum):
    """"固定資産売却損益（△は益）、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossGainOnStepAcquisitionOpeCFIFRS(Enum):
    """"段階取得に係る差損益（△は益）、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossGainRelatedToFixedAssetsOpeCFIFRS(Enum):
    """"固定資産に係る損益（△は益）、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnRetirementOfFixedAssetsOpeCFIFRS(Enum):
    """"固定資産除却損、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class NetCashProvidedByUsedInFinancingActivitiesIFRS(Enum):
    """"財務活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class NetCashProvidedByUsedInInvestingActivitiesIFRS(Enum):
    """"投資活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class NetCashProvidedByUsedInOperatingActivitiesIFRS(Enum):
    """"営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class NetChangeInFairValueOfEquityInstrumentsDesignatedAsMeasuredAtFairValueThroughOtherComprehensiveIncomeBeforeTaxItemsThatWillNotBeReclassifiedToProfitOrLossOCIIFRS(Enum):
    """"その他の包括利益を通じて公正価値で測定するものとして指定した資本性金融商品の公正価値の純変動額（税引前）、純損益に振り替えられることのないその他の包括利益（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class NetChangeInFairValueOfEquityInstrumentsDesignatedAsMeasuredAtFairValueThroughOtherComprehensiveIncomeNetOfTaxItemsThatWillNotBeReclassifiedToProfitOrLossOCIIFRS(Enum):
    """"その他の包括利益を通じて公正価値で測定するものとして指定した資本性金融商品の公正価値の純変動額（税引後）、純損益に振り替えられることのないその他の包括利益（IFRS）"""
    CURRENT_QUARTER_DURATION = 'CurrentQuarterDuration'
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_QUARTER_DURATION = 'Prior1QuarterDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class NetDecreaseIncreaseInTimeDepositsInvCFIFRS(Enum):
    """"定期預金の純増減額（△は増加）、投資活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class NetDecreaseIncreaseInTreasurySharesFinCFIFRS(Enum):
    """"自己株式の純増減額（△は増加）、財務活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class NetIncreaseDecreaseInCashAndCashEquivalentsBeforeEffectOfExchangeRateChangesIFRS(Enum):
    """"現金及び現金同等物の増減額（△は減少）（換算差額加算前）（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class NetIncreaseDecreaseInCashAndCashEquivalentsIFRS(Enum):
    """"現金及び現金同等物の増減額（△は減少）（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class NetIncreaseDecreaseInShortTermBorrowingsFinCFIFRS(Enum):
    """"短期借入金の純増減額（△は減少）、財務活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class NetSalesIFRS(Enum):
    """"売上高（IFRS）"""
    CURRENT_QUARTER_DURATION = 'CurrentQuarterDuration'
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
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
    PRIOR1_QUARTER_DURATION = 'Prior1QuarterDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
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


class NonControllingInterestsIFRS(Enum):
    """"非支配持分（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR2_YEAR_INSTANT = 'Prior2YearInstant'


class NonCurrentAssetsIFRS(Enum):
    """"非流動資産（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR2_YEAR_INSTANT = 'Prior2YearInstant'


class NonCurrentLabilitiesIFRS(Enum):
    """"非流動負債（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR2_YEAR_INSTANT = 'Prior2YearInstant'


class OperatingExpensesIFRS(Enum):
    """"営業費用（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class OperatingProfitLossIFRS(Enum):
    """"営業利益（△損失）（IFRS）"""
    CURRENT_QUARTER_DURATION = 'CurrentQuarterDuration'
    CURRENT_QUARTER_DURATION__OTHER_REPORTABLE_SEGMENTS_MEMBER = 'CurrentQuarterDuration_OtherReportableSegmentsMember'
    """ その他 """
    CURRENT_QUARTER_DURATION__RECONCILING_ITEMS_MEMBER = 'CurrentQuarterDuration_ReconcilingItemsMember'
    """ 調整項目 """
    CURRENT_QUARTER_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'CurrentQuarterDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
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
    CURRENT_YEAR_DURATION__OTHER_REPORTABLE_SEGMENTS_MEMBER = 'CurrentYearDuration_OtherReportableSegmentsMember'
    """ 当年度会計期間その他 """
    CURRENT_YEAR_DURATION__RECONCILING_ITEMS_MEMBER = 'CurrentYearDuration_ReconcilingItemsMember'
    """ 当年度会計期間調整項目 """
    CURRENT_YEAR_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'CurrentYearDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 当年度会計期間事業セグメント合計 """
    PRIOR1_QUARTER_DURATION = 'Prior1QuarterDuration'
    PRIOR1_QUARTER_DURATION__OTHER_REPORTABLE_SEGMENTS_MEMBER = 'Prior1QuarterDuration_OtherReportableSegmentsMember'
    """ その他 """
    PRIOR1_QUARTER_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1QuarterDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_QUARTER_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'Prior1QuarterDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
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
    PRIOR1_YEAR_DURATION__OTHER_REPORTABLE_SEGMENTS_MEMBER = 'Prior1YearDuration_OtherReportableSegmentsMember'
    """ その他 """
    PRIOR1_YEAR_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1YearDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_YEAR_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1YearDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """


class OtherAssetsAssetsIFRS(Enum):
    """"その他の資産、資産（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class OtherChangesInWorkingCapitalOpeCFIFRS(Enum):
    """"その他、運転資本の増減、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class OtherComponentsOfEquityIFRS(Enum):
    """"その他の資本の構成要素（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR2_YEAR_INSTANT = 'Prior2YearInstant'


class OtherComprehensiveIncomeIFRS(Enum):
    """"その他の包括利益（IFRS）"""
    CURRENT_QUARTER_DURATION = 'CurrentQuarterDuration'
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__ACCUMULATED_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'CurrentYTDDuration_AccumulatedOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益累計額 """
    CURRENT_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'CurrentYTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    CURRENT_YTD_DURATION__EFFECTIVE_PORTION_OF_CASH_FLOW_HEDGES_IFRS_MEMBER = 'CurrentYTDDuration_EffectivePortionOfCashFlowHedgesIFRSMember'
    """ キャッシュ・フロー・ヘッジの有効部分 """
    CURRENT_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'CurrentYTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    CURRENT_YTD_DURATION__EXCHANGE_DIFFERENCES_ON_TRANSLATION_OF_FOREIGN_OPERATIONS_IFRS_MEMBER = 'CurrentYTDDuration_ExchangeDifferencesOnTranslationOfForeignOperationsIFRSMember'
    """ 在外営業活動体の外貨換算差額 """
    CURRENT_YTD_DURATION__FINANCIAL_ASSETS_MEASURED_AT_FAIR_VALUE_THROUGH_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'CurrentYTDDuration_FinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益を通じて公正価値で測定する金融資産 """
    CURRENT_YTD_DURATION__NET_CHANGE_IN_FAIR_VALUE_OF_EQUITY_INSTRUMENTS_DESIGNATED_AS_MEASURED_AT_FAIR_VALUE_THROUGH_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'CurrentYTDDuration_NetChangeInFairValueOfEquityInstrumentsDesignatedAsMeasuredAtFairValueThroughOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益を通じて公正価値で測定するものとして指定した資本性金融商品の公正価値の純変動額 """
    CURRENT_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'CurrentYTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    CURRENT_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'CurrentYTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    CURRENT_YTD_DURATION__REMEASUREMENTS_OF_DEFINED_BENEFIT_PLANS_IFRS_MEMBER = 'CurrentYTDDuration_RemeasurementsOfDefinedBenefitPlansIFRSMember'
    """ 確定給付制度の再測定 """
    CURRENT_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'CurrentYTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    CURRENT_YTD_DURATION__SHARE_CAPITAL_IFRS_MEMBER = 'CurrentYTDDuration_ShareCapitalIFRSMember'
    """ 資本金 """
    CURRENT_YTD_DURATION__SHARE_OF_OTHER_COMPREHENSIVE_INCOME_OF_INVESTMENTS_ACCOUNTED_FOR_USING_EQUITY_METHOD_IFRS_MEMBER = 'CurrentYTDDuration_ShareOfOtherComprehensiveIncomeOfInvestmentsAccountedForUsingEquityMethodIFRSMember'
    """ 持分法によるその他の包括利益 """
    CURRENT_YTD_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'CurrentYTDDuration_TreasurySharesIFRSMember'
    """ 自己株式 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'CurrentYearDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 当年度会計期間親会社の所有者に帰属する持分 """
    CURRENT_YEAR_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'CurrentYearDuration_NonControllingInterestsIFRSMember'
    """ 当年度会計期間非支配持分 """
    CURRENT_YEAR_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'CurrentYearDuration_OtherComponentsOfEquityIFRSMember'
    """ 当年度会計期間その他の資本の構成要素 """
    PRIOR1_QUARTER_DURATION = 'Prior1QuarterDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__ACCUMULATED_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'Prior1YTDDuration_AccumulatedOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益累計額 """
    PRIOR1_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'Prior1YTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    PRIOR1_YTD_DURATION__EFFECTIVE_PORTION_OF_CASH_FLOW_HEDGES_IFRS_MEMBER = 'Prior1YTDDuration_EffectivePortionOfCashFlowHedgesIFRSMember'
    """ キャッシュ・フロー・ヘッジの有効部分 """
    PRIOR1_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'Prior1YTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    PRIOR1_YTD_DURATION__EXCHANGE_DIFFERENCES_ON_TRANSLATION_OF_FOREIGN_OPERATIONS_IFRS_MEMBER = 'Prior1YTDDuration_ExchangeDifferencesOnTranslationOfForeignOperationsIFRSMember'
    """ 在外営業活動体の外貨換算差額 """
    PRIOR1_YTD_DURATION__FINANCIAL_ASSETS_MEASURED_AT_FAIR_VALUE_THROUGH_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'Prior1YTDDuration_FinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益を通じて公正価値で測定する金融資産 """
    PRIOR1_YTD_DURATION__NET_CHANGE_IN_FAIR_VALUE_OF_EQUITY_INSTRUMENTS_DESIGNATED_AS_MEASURED_AT_FAIR_VALUE_THROUGH_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'Prior1YTDDuration_NetChangeInFairValueOfEquityInstrumentsDesignatedAsMeasuredAtFairValueThroughOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益を通じて公正価値で測定するものとして指定した資本性金融商品の公正価値の純変動額 """
    PRIOR1_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'Prior1YTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    PRIOR1_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'Prior1YTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    PRIOR1_YTD_DURATION__REMEASUREMENTS_OF_DEFINED_BENEFIT_PLANS_IFRS_MEMBER = 'Prior1YTDDuration_RemeasurementsOfDefinedBenefitPlansIFRSMember'
    """ 確定給付制度の再測定 """
    PRIOR1_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'Prior1YTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    PRIOR1_YTD_DURATION__SHARE_CAPITAL_IFRS_MEMBER = 'Prior1YTDDuration_ShareCapitalIFRSMember'
    """ 資本金 """
    PRIOR1_YTD_DURATION__SHARE_OF_OTHER_COMPREHENSIVE_INCOME_OF_INVESTMENTS_ACCOUNTED_FOR_USING_EQUITY_METHOD_IFRS_MEMBER = 'Prior1YTDDuration_ShareOfOtherComprehensiveIncomeOfInvestmentsAccountedForUsingEquityMethodIFRSMember'
    """ 持分法によるその他の包括利益 """
    PRIOR1_YTD_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'Prior1YTDDuration_TreasurySharesIFRSMember'
    """ 自己株式 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'Prior1YearDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    PRIOR1_YEAR_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'Prior1YearDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    PRIOR1_YEAR_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'Prior1YearDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """


class OtherCurrentAssetsCAIFRS(Enum):
    """"その他の流動資産（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR2_YEAR_INSTANT = 'Prior2YearInstant'


class OtherCurrentLiabilitiesCLIFRS(Enum):
    """"その他の流動負債（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR2_YEAR_INSTANT = 'Prior2YearInstant'


class OtherExpensesIFRS(Enum):
    """"その他の費用（IFRS）"""
    CURRENT_QUARTER_DURATION = 'CurrentQuarterDuration'
    CURRENT_QUARTER_DURATION__RECONCILING_ITEMS_MEMBER = 'CurrentQuarterDuration_ReconcilingItemsMember'
    """ 調整項目 """
    CURRENT_QUARTER_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'CurrentQuarterDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'CurrentYTDDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    CURRENT_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'CurrentYTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    CURRENT_YTD_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'CurrentYTDDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_QUARTER_DURATION = 'Prior1QuarterDuration'
    PRIOR1_QUARTER_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1QuarterDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_QUARTER_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'Prior1QuarterDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'Prior1YTDDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    PRIOR1_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1YTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_YTD_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'Prior1YTDDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class OtherFinCFIFRS(Enum):
    """"その他、財務活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class OtherFinancialAssetsAssetsIFRS(Enum):
    """"その他の金融資産、資産（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class OtherFinancialAssetsCAIFRS(Enum):
    """"その他の金融資産、流動資産（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR2_YEAR_INSTANT = 'Prior2YearInstant'


class OtherFinancialAssetsNCAIFRS(Enum):
    """"その他の金融資産、非流動資産（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR2_YEAR_INSTANT = 'Prior2YearInstant'


class OtherFinancialLiabilitiesCLIFRS(Enum):
    """"その他の金融負債、流動負債（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR2_YEAR_INSTANT = 'Prior2YearInstant'


class OtherFinancialLiabilitiesLiabilitiesIFRS(Enum):
    """"その他の金融負債、負債（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class OtherFinancialLiabilitiesNCLIFRS(Enum):
    """"その他の金融負債、非流動負債（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR2_YEAR_INSTANT = 'Prior2YearInstant'


class OtherIncomeAndExpensesNetIFRS(Enum):
    """"その他の収益・費用（純額）（IFRS）"""
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


class OtherIncomeIFRS(Enum):
    """"その他の収益（IFRS）"""
    CURRENT_QUARTER_DURATION = 'CurrentQuarterDuration'
    CURRENT_QUARTER_DURATION__RECONCILING_ITEMS_MEMBER = 'CurrentQuarterDuration_ReconcilingItemsMember'
    """ 調整項目 """
    CURRENT_QUARTER_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'CurrentQuarterDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'CurrentYTDDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    CURRENT_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'CurrentYTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    CURRENT_YTD_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'CurrentYTDDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_QUARTER_DURATION = 'Prior1QuarterDuration'
    PRIOR1_QUARTER_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1QuarterDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_QUARTER_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'Prior1QuarterDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'Prior1YTDDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    PRIOR1_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1YTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_YTD_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'Prior1YTDDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class OtherIntangibleAssetsIFRS(Enum):
    """"その他の無形資産（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class OtherInvCFIFRS(Enum):
    """"その他、投資活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class OtherInvestmentsIFRS(Enum):
    """"その他の投資（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class OtherLiabilitiesLiabilitiesIFRS(Enum):
    """"その他の負債、負債（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class OtherNonCurrentAssetsNCAIFRS(Enum):
    """"その他の非流動資産（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR2_YEAR_INSTANT = 'Prior2YearInstant'


class OtherNonCurrentLiabilitiesNCLIFRS(Enum):
    """"その他の非流動負債（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR2_YEAR_INSTANT = 'Prior2YearInstant'


class OtherOpeCFIFRS(Enum):
    """"その他、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class OtherOperatingExpensesIFRS(Enum):
    """"その他の営業費用（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class OtherOperatingIncomeIFRS(Enum):
    """"その他の営業収益（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class OtherSSIFRS(Enum):
    """"その他、持分変動計算書（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__ACCUMULATED_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'CurrentYTDDuration_AccumulatedOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益累計額 """
    CURRENT_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'CurrentYTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    CURRENT_YTD_DURATION__EFFECTIVE_PORTION_OF_CASH_FLOW_HEDGES_IFRS_MEMBER = 'CurrentYTDDuration_EffectivePortionOfCashFlowHedgesIFRSMember'
    """ キャッシュ・フロー・ヘッジの有効部分 """
    CURRENT_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'CurrentYTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    CURRENT_YTD_DURATION__EXCHANGE_DIFFERENCES_ON_TRANSLATION_OF_FOREIGN_OPERATIONS_IFRS_MEMBER = 'CurrentYTDDuration_ExchangeDifferencesOnTranslationOfForeignOperationsIFRSMember'
    """ 在外営業活動体の外貨換算差額 """
    CURRENT_YTD_DURATION__FINANCIAL_ASSETS_MEASURED_AT_FAIR_VALUE_THROUGH_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'CurrentYTDDuration_FinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益を通じて公正価値で測定する金融資産 """
    CURRENT_YTD_DURATION__NET_CHANGE_IN_FAIR_VALUE_OF_EQUITY_INSTRUMENTS_DESIGNATED_AS_MEASURED_AT_FAIR_VALUE_THROUGH_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'CurrentYTDDuration_NetChangeInFairValueOfEquityInstrumentsDesignatedAsMeasuredAtFairValueThroughOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益を通じて公正価値で測定するものとして指定した資本性金融商品の公正価値の純変動額 """
    CURRENT_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'CurrentYTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    CURRENT_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'CurrentYTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    CURRENT_YTD_DURATION__REMEASUREMENTS_OF_DEFINED_BENEFIT_PLANS_IFRS_MEMBER = 'CurrentYTDDuration_RemeasurementsOfDefinedBenefitPlansIFRSMember'
    """ 確定給付制度の再測定 """
    CURRENT_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'CurrentYTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    CURRENT_YTD_DURATION__SHARE_CAPITAL_IFRS_MEMBER = 'CurrentYTDDuration_ShareCapitalIFRSMember'
    """ 資本金 """
    CURRENT_YTD_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'CurrentYTDDuration_TreasurySharesIFRSMember'
    """ 自己株式 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__ACCUMULATED_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'Prior1YTDDuration_AccumulatedOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益累計額 """
    PRIOR1_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'Prior1YTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    PRIOR1_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'Prior1YTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    PRIOR1_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'Prior1YTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    PRIOR1_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'Prior1YTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    PRIOR1_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'Prior1YTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    PRIOR1_YTD_DURATION__SHARE_CAPITAL_IFRS_MEMBER = 'Prior1YTDDuration_ShareCapitalIFRSMember'
    """ 資本金 """
    PRIOR1_YTD_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'Prior1YTDDuration_TreasurySharesIFRSMember'
    """ 自己株式 """


class PaymentsForAcquisitionOfBusinessesInvCFIFRS(Enum):
    """"事業譲受による支出、投資活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PaymentsForAcquisitionOfInterestsInSubsidiariesFromNonControllingInterestsFinCFIFRS(Enum):
    """"非支配持分からの子会社持分取得による支出、財務活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PaymentsForAcquisitionOfSubsidiariesInvCFIFRS(Enum):
    """"子会社の取得による支出、投資活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PaymentsForLeaseholdDepositsAndGuaranteeDepositsInvCFIFRS(Enum):
    """"敷金及び保証金の差入による支出、投資活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class PaymentsForLoansReceivableInvCFIFRS(Enum):
    """"貸付けによる支出、投資活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PaymentsForPurchaseOfTreasurySharesFinCFIFRS(Enum):
    """"自己株式の取得による支出、財務活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class PaymentsIntoTimeDepositsInvCFIFRS(Enum):
    """"定期預金の預入による支出、投資活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class ProceedsFromChangesInOwnershipInterestsInSubsidiariesThatDoNotResultInLossOfControlFinCFIFRS(Enum):
    """"非支配持分への子会社持分売却による収入、財務活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromCollectionOfLeaseholdDepositsAndGuaranteeDepositsInvCFIFRS(Enum):
    """"敷金及び保証金の回収による収入、投資活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromExerciseOfShareAcquisitionRightsFinCFIFRS(Enum):
    """"新株予約権の行使による収入、財務活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class ProceedsFromIssuanceOfBondsAndLongTermBorrowingsFinCFIFRS(Enum):
    """"社債の発行及び長期借入れによる収入、財務活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromIssuanceOfBondsFinCFIFRS(Enum):
    """"社債の発行による収入、財務活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class ProceedsFromIssuanceOfSharesFinCFIFRS(Enum):
    """"株式の発行による収入、財務活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromLongTermBorrowingsFinCFIFRS(Enum):
    """"長期借入れによる収入、財務活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromSaleOfBusinessesInvCFIFRS(Enum):
    """"事業譲渡による収入、投資活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromSaleOfEquityInstrumentsInvCFIFRS(Enum):
    """"資本性金融商品の売却による収入、投資活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromSaleOfIntangibleAssetsInvCFIFRS(Enum):
    """"無形資産の売却による収入、投資活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromSaleOfInvestmentSecuritiesInvCFIFRS(Enum):
    """"投資有価証券の売却による収入、投資活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromSaleOfInvestmentsInvCFIFRS(Enum):
    """"投資の売却及び償還による収入、投資活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromSaleOfMarketableSecuritiesInvCFIFRS(Enum):
    """"有価証券の売却による収入、投資活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromSaleOfOtherFinancialAssetsInvCFIFRS(Enum):
    """"その他の金融資産の売却による収入、投資活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromSaleOfPropertyPlantAndEquipmentAndIntangibleAssetsInvCFIFRS(Enum):
    """"有形固定資産及び無形資産の売却による収入、投資活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromSaleOfPropertyPlantAndEquipmentInvCFIFRS(Enum):
    """"有形固定資産の売却による収入、投資活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class ProceedsFromSaleOfSubsidiariesInvCFIFRS(Enum):
    """"子会社の売却による収入、投資活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromSaleOfTreasurySharesFinCFIFRS(Enum):
    """"自己株式の売却による収入、財務活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromShortTermBorrowingsFinCFIFRS(Enum):
    """"短期借入れによる収入、財務活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromWithdrawalOfTimeDepositsInvCFIFRS(Enum):
    """"定期預金の払戻による収入、投資活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class ProfitLossAttributableToNonControllingInterestsIFRS(Enum):
    """"非支配持分、当期利益（△損失）（IFRS）"""
    CURRENT_QUARTER_DURATION = 'CurrentQuarterDuration'
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_QUARTER_DURATION = 'Prior1QuarterDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class ProfitLossAttributableToOwnersOfParentIFRS(Enum):
    """"親会社の所有者、当期利益（△損失）（IFRS）"""
    CURRENT_QUARTER_DURATION = 'CurrentQuarterDuration'
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_QUARTER_DURATION = 'Prior1QuarterDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class ProfitLossBeforeTaxFromDiscontinuedOperationsIFRS(Enum):
    """"非継続事業からの税引前利益（△損失）（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProfitLossBeforeTaxIFRS(Enum):
    """"継続事業からの税引前利益（△損失）（IFRS）"""
    CURRENT_QUARTER_DURATION = 'CurrentQuarterDuration'
    CURRENT_QUARTER_DURATION__RECONCILING_ITEMS_MEMBER = 'CurrentQuarterDuration_ReconcilingItemsMember'
    """ 調整項目 """
    CURRENT_QUARTER_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'CurrentQuarterDuration_ReportableSegmentsMember'
    """ 報告セグメント """
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
    PRIOR1_QUARTER_DURATION = 'Prior1QuarterDuration'
    PRIOR1_QUARTER_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1QuarterDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_QUARTER_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'Prior1QuarterDuration_ReportableSegmentsMember'
    """ 報告セグメント """
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


class ProfitLossFromContinuingOperationsIFRS(Enum):
    """"継続事業からの当期利益（△損失）（IFRS）"""
    CURRENT_QUARTER_DURATION = 'CurrentQuarterDuration'
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_QUARTER_DURATION = 'Prior1QuarterDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProfitLossFromDiscontinuedOperationsIFRS(Enum):
    """"非継続事業からの当期利益（△損失）（IFRS）"""
    CURRENT_QUARTER_DURATION = 'CurrentQuarterDuration'
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_QUARTER_DURATION = 'Prior1QuarterDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProfitLossIFRS(Enum):
    """"当期利益（△損失）（IFRS）"""
    CURRENT_QUARTER_DURATION = 'CurrentQuarterDuration'
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__ACCUMULATED_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'CurrentYTDDuration_AccumulatedOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益累計額 """
    CURRENT_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'CurrentYTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    CURRENT_YTD_DURATION__EFFECTIVE_PORTION_OF_CASH_FLOW_HEDGES_IFRS_MEMBER = 'CurrentYTDDuration_EffectivePortionOfCashFlowHedgesIFRSMember'
    """ キャッシュ・フロー・ヘッジの有効部分 """
    CURRENT_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'CurrentYTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    CURRENT_YTD_DURATION__EXCHANGE_DIFFERENCES_ON_TRANSLATION_OF_FOREIGN_OPERATIONS_IFRS_MEMBER = 'CurrentYTDDuration_ExchangeDifferencesOnTranslationOfForeignOperationsIFRSMember'
    """ 在外営業活動体の外貨換算差額 """
    CURRENT_YTD_DURATION__FINANCIAL_ASSETS_MEASURED_AT_FAIR_VALUE_THROUGH_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'CurrentYTDDuration_FinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益を通じて公正価値で測定する金融資産 """
    CURRENT_YTD_DURATION__NET_CHANGE_IN_FAIR_VALUE_OF_EQUITY_INSTRUMENTS_DESIGNATED_AS_MEASURED_AT_FAIR_VALUE_THROUGH_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'CurrentYTDDuration_NetChangeInFairValueOfEquityInstrumentsDesignatedAsMeasuredAtFairValueThroughOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益を通じて公正価値で測定するものとして指定した資本性金融商品の公正価値の純変動額 """
    CURRENT_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'CurrentYTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    CURRENT_YTD_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'CurrentYTDDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    CURRENT_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'CurrentYTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    CURRENT_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'CurrentYTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    CURRENT_YTD_DURATION__REMEASUREMENTS_OF_DEFINED_BENEFIT_PLANS_IFRS_MEMBER = 'CurrentYTDDuration_RemeasurementsOfDefinedBenefitPlansIFRSMember'
    """ 確定給付制度の再測定 """
    CURRENT_YTD_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'CurrentYTDDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    CURRENT_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'CurrentYTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    CURRENT_YTD_DURATION__SHARE_CAPITAL_IFRS_MEMBER = 'CurrentYTDDuration_ShareCapitalIFRSMember'
    """ 資本金 """
    CURRENT_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'CurrentYTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    CURRENT_YTD_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'CurrentYTDDuration_TreasurySharesIFRSMember'
    """ 自己株式 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'CurrentYearDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 当年度会計期間親会社の所有者に帰属する持分 """
    CURRENT_YEAR_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'CurrentYearDuration_NonControllingInterestsIFRSMember'
    """ 当年度会計期間非支配持分 """
    CURRENT_YEAR_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'CurrentYearDuration_RetainedEarningsIFRSMember'
    """ 当年度会計期間利益剰余金 """
    PRIOR1_QUARTER_DURATION = 'Prior1QuarterDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__ACCUMULATED_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'Prior1YTDDuration_AccumulatedOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益累計額 """
    PRIOR1_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'Prior1YTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    PRIOR1_YTD_DURATION__EFFECTIVE_PORTION_OF_CASH_FLOW_HEDGES_IFRS_MEMBER = 'Prior1YTDDuration_EffectivePortionOfCashFlowHedgesIFRSMember'
    """ キャッシュ・フロー・ヘッジの有効部分 """
    PRIOR1_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'Prior1YTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    PRIOR1_YTD_DURATION__EXCHANGE_DIFFERENCES_ON_TRANSLATION_OF_FOREIGN_OPERATIONS_IFRS_MEMBER = 'Prior1YTDDuration_ExchangeDifferencesOnTranslationOfForeignOperationsIFRSMember'
    """ 在外営業活動体の外貨換算差額 """
    PRIOR1_YTD_DURATION__FINANCIAL_ASSETS_MEASURED_AT_FAIR_VALUE_THROUGH_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'Prior1YTDDuration_FinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益を通じて公正価値で測定する金融資産 """
    PRIOR1_YTD_DURATION__NET_CHANGE_IN_FAIR_VALUE_OF_EQUITY_INSTRUMENTS_DESIGNATED_AS_MEASURED_AT_FAIR_VALUE_THROUGH_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'Prior1YTDDuration_NetChangeInFairValueOfEquityInstrumentsDesignatedAsMeasuredAtFairValueThroughOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益を通じて公正価値で測定するものとして指定した資本性金融商品の公正価値の純変動額 """
    PRIOR1_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'Prior1YTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    PRIOR1_YTD_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'Prior1YTDDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    PRIOR1_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'Prior1YTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    PRIOR1_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1YTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_YTD_DURATION__REMEASUREMENTS_OF_DEFINED_BENEFIT_PLANS_IFRS_MEMBER = 'Prior1YTDDuration_RemeasurementsOfDefinedBenefitPlansIFRSMember'
    """ 確定給付制度の再測定 """
    PRIOR1_YTD_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'Prior1YTDDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    PRIOR1_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'Prior1YTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    PRIOR1_YTD_DURATION__SHARE_CAPITAL_IFRS_MEMBER = 'Prior1YTDDuration_ShareCapitalIFRSMember'
    """ 資本金 """
    PRIOR1_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1YTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    PRIOR1_YTD_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'Prior1YTDDuration_TreasurySharesIFRSMember'
    """ 自己株式 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'Prior1YearDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    PRIOR1_YEAR_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'Prior1YearDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    PRIOR1_YEAR_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'Prior1YearDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """


class PropertyPlantAndEquipmentIFRS(Enum):
    """"有形固定資産（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR2_YEAR_INSTANT = 'Prior2YearInstant'


class ProvisionsCLIFRS(Enum):
    """"引当金、流動負債（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR2_YEAR_INSTANT = 'Prior2YearInstant'


class ProvisionsLiabilitiesIFRS(Enum):
    """"引当金、負債（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ProvisionsNCLIFRS(Enum):
    """"引当金、非流動負債（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR2_YEAR_INSTANT = 'Prior2YearInstant'


class PurchaseAndDisposalOfTreasurySharesSSIFRS(Enum):
    """"自己株式の取得及び処分、持分変動計算書（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'CurrentYTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    CURRENT_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'CurrentYTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    CURRENT_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'CurrentYTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    CURRENT_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'CurrentYTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    CURRENT_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'CurrentYTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    CURRENT_YTD_DURATION__SHARE_CAPITAL_IFRS_MEMBER = 'CurrentYTDDuration_ShareCapitalIFRSMember'
    """ 資本金 """
    CURRENT_YTD_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'CurrentYTDDuration_TreasurySharesIFRSMember'
    """ 自己株式 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'Prior1YTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    PRIOR1_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'Prior1YTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    PRIOR1_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'Prior1YTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    PRIOR1_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'Prior1YTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    PRIOR1_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'Prior1YTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    PRIOR1_YTD_DURATION__SHARE_CAPITAL_IFRS_MEMBER = 'Prior1YTDDuration_ShareCapitalIFRSMember'
    """ 資本金 """
    PRIOR1_YTD_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'Prior1YTDDuration_TreasurySharesIFRSMember'
    """ 自己株式 """


class PurchaseOfEquityInstrumentsInvCFIFRS(Enum):
    """"資本性金融商品の取得による支出、投資活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PurchaseOfIntangibleAssetsInvCFIFRS(Enum):
    """"無形資産の取得による支出、投資活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class PurchaseOfInvestmentPropertyInvCFIFRS(Enum):
    """"投資不動産の取得による支出、投資活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PurchaseOfInvestmentSecuritiesInvCFIFRS(Enum):
    """"投資有価証券の取得による支出、投資活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class PurchaseOfInvestmentsAccountedForUsingEquityMethodInvCFIFRS(Enum):
    """"持分法で会計処理されている投資の取得による支出、投資活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PurchaseOfInvestmentsInvCFIFRS(Enum):
    """"投資の取得による支出、投資活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PurchaseOfMarketableSecuritiesInvCFIFRS(Enum):
    """"有価証券の取得による支出、投資活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PurchaseOfOtherFinancialAssetsInvCFIFRS(Enum):
    """"その他の金融資産の取得による支出、投資活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PurchaseOfOtherInvestmentsInvCFIFRS(Enum):
    """"その他の投資の取得による支出、投資活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PurchaseOfPropertyPlantAndEquipmentAndIntangibleAssetsInvCFIFRS(Enum):
    """"有形固定資産及び無形資産の取得による支出、投資活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PurchaseOfPropertyPlantAndEquipmentInvCFIFRS(Enum):
    """"有形固定資産の取得による支出、投資活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class PurchaseOfTreasurySharesSSIFRS(Enum):
    """"自己株式の取得、持分変動計算書（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__ACCUMULATED_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'CurrentYTDDuration_AccumulatedOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益累計額 """
    CURRENT_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'CurrentYTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    CURRENT_YTD_DURATION__EFFECTIVE_PORTION_OF_CASH_FLOW_HEDGES_IFRS_MEMBER = 'CurrentYTDDuration_EffectivePortionOfCashFlowHedgesIFRSMember'
    """ キャッシュ・フロー・ヘッジの有効部分 """
    CURRENT_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'CurrentYTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    CURRENT_YTD_DURATION__EXCHANGE_DIFFERENCES_ON_TRANSLATION_OF_FOREIGN_OPERATIONS_IFRS_MEMBER = 'CurrentYTDDuration_ExchangeDifferencesOnTranslationOfForeignOperationsIFRSMember'
    """ 在外営業活動体の外貨換算差額 """
    CURRENT_YTD_DURATION__FINANCIAL_ASSETS_MEASURED_AT_FAIR_VALUE_THROUGH_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'CurrentYTDDuration_FinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益を通じて公正価値で測定する金融資産 """
    CURRENT_YTD_DURATION__NET_CHANGE_IN_FAIR_VALUE_OF_EQUITY_INSTRUMENTS_DESIGNATED_AS_MEASURED_AT_FAIR_VALUE_THROUGH_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'CurrentYTDDuration_NetChangeInFairValueOfEquityInstrumentsDesignatedAsMeasuredAtFairValueThroughOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益を通じて公正価値で測定するものとして指定した資本性金融商品の公正価値の純変動額 """
    CURRENT_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'CurrentYTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    CURRENT_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'CurrentYTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    CURRENT_YTD_DURATION__REMEASUREMENTS_OF_DEFINED_BENEFIT_PLANS_IFRS_MEMBER = 'CurrentYTDDuration_RemeasurementsOfDefinedBenefitPlansIFRSMember'
    """ 確定給付制度の再測定 """
    CURRENT_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'CurrentYTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    CURRENT_YTD_DURATION__SHARE_CAPITAL_IFRS_MEMBER = 'CurrentYTDDuration_ShareCapitalIFRSMember'
    """ 資本金 """
    CURRENT_YTD_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'CurrentYTDDuration_TreasurySharesIFRSMember'
    """ 自己株式 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'CurrentYearDuration_CapitalSurplusIFRSMember'
    """ 当年度会計期間資本剰余金 """
    CURRENT_YEAR_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'CurrentYearDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 当年度会計期間親会社の所有者に帰属する持分 """
    CURRENT_YEAR_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'CurrentYearDuration_TreasurySharesIFRSMember'
    """ 当年度会計期間自己株式 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__ACCUMULATED_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'Prior1YTDDuration_AccumulatedOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益累計額 """
    PRIOR1_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'Prior1YTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    PRIOR1_YTD_DURATION__EFFECTIVE_PORTION_OF_CASH_FLOW_HEDGES_IFRS_MEMBER = 'Prior1YTDDuration_EffectivePortionOfCashFlowHedgesIFRSMember'
    """ キャッシュ・フロー・ヘッジの有効部分 """
    PRIOR1_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'Prior1YTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    PRIOR1_YTD_DURATION__EXCHANGE_DIFFERENCES_ON_TRANSLATION_OF_FOREIGN_OPERATIONS_IFRS_MEMBER = 'Prior1YTDDuration_ExchangeDifferencesOnTranslationOfForeignOperationsIFRSMember'
    """ 在外営業活動体の外貨換算差額 """
    PRIOR1_YTD_DURATION__FINANCIAL_ASSETS_MEASURED_AT_FAIR_VALUE_THROUGH_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'Prior1YTDDuration_FinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益を通じて公正価値で測定する金融資産 """
    PRIOR1_YTD_DURATION__NET_CHANGE_IN_FAIR_VALUE_OF_EQUITY_INSTRUMENTS_DESIGNATED_AS_MEASURED_AT_FAIR_VALUE_THROUGH_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'Prior1YTDDuration_NetChangeInFairValueOfEquityInstrumentsDesignatedAsMeasuredAtFairValueThroughOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益を通じて公正価値で測定するものとして指定した資本性金融商品の公正価値の純変動額 """
    PRIOR1_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'Prior1YTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    PRIOR1_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'Prior1YTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    PRIOR1_YTD_DURATION__REMEASUREMENTS_OF_DEFINED_BENEFIT_PLANS_IFRS_MEMBER = 'Prior1YTDDuration_RemeasurementsOfDefinedBenefitPlansIFRSMember'
    """ 確定給付制度の再測定 """
    PRIOR1_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'Prior1YTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    PRIOR1_YTD_DURATION__SHARE_CAPITAL_IFRS_MEMBER = 'Prior1YTDDuration_ShareCapitalIFRSMember'
    """ 資本金 """
    PRIOR1_YTD_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'Prior1YTDDuration_TreasurySharesIFRSMember'
    """ 自己株式 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'Prior1YearDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    PRIOR1_YEAR_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'Prior1YearDuration_TreasurySharesIFRSMember'
    """ 自己株式 """


class RedemptionOfBondsAndRepaymentsOfLongTermBorrowingsFinCFIFRS(Enum):
    """"社債の償還及び長期借入金の返済、財務活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class RedemptionOfBondsFinCFIFRS(Enum):
    """"社債の償還による支出、財務活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class RemeasurementsOfDefinedBenefitPlansBeforeTaxItemsThatWillNotBeReclassifiedToProfitOrLossOCIIFRS(Enum):
    """"確定給付制度の再測定（税引前）、純損益に振り替えられることのないその他の包括利益（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class RemeasurementsOfDefinedBenefitPlansNetOfTaxItemsThatWillNotBeReclassifiedToProfitOrLossOCIIFRS(Enum):
    """"確定給付制度の再測定（税引後）、純損益に振り替えられることのないその他の包括利益（IFRS）"""
    CURRENT_QUARTER_DURATION = 'CurrentQuarterDuration'
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_QUARTER_DURATION = 'Prior1QuarterDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class RepaymentsOfLeaseObligationsFinCFIFRS(Enum):
    """"リース負債の返済による支出、財務活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class RepaymentsOfLongTermBorrowingsFinCFIFRS(Enum):
    """"長期借入金の返済による支出、財務活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class RepaymentsOfShortTermBorrowingsFinCFIFRS(Enum):
    """"短期借入金の返済による支出、財務活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ResearchAndDevelopmentExpenditureRecognizedAsExpenseDuringPeriodIFRS(Enum):
    """"当期に費用認識した研究開発費（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class RestatedBalanceIFRS(Enum):
    """"会計方針の変更を反映した当期首残高（IFRS）"""
    PRIOR2_YEAR_INSTANT = 'Prior2YearInstant'
    PRIOR2_YEAR_INSTANT__CAPITAL_SURPLUS_IFRS_MEMBER = 'Prior2YearInstant_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    PRIOR2_YEAR_INSTANT__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'Prior2YearInstant_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    PRIOR2_YEAR_INSTANT__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'Prior2YearInstant_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    PRIOR2_YEAR_INSTANT__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'Prior2YearInstant_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    PRIOR2_YEAR_INSTANT__RETAINED_EARNINGS_IFRS_MEMBER = 'Prior2YearInstant_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    PRIOR2_YEAR_INSTANT__SHARE_CAPITAL_IFRS_MEMBER = 'Prior2YearInstant_ShareCapitalIFRSMember'
    """ 資本金 """
    PRIOR2_YEAR_INSTANT__TREASURY_SHARES_IFRS_MEMBER = 'Prior2YearInstant_TreasurySharesIFRSMember'
    """ 自己株式 """


class RetainedEarningsIFRS(Enum):
    """"利益剰余金（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR2_YEAR_INSTANT = 'Prior2YearInstant'


class RetirementBenefitAssetNCAIFRS(Enum):
    """"退職給付に係る資産、非流動資産（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class RetirementBenefitLiabilityNCLIFRS(Enum):
    """"退職給付に係る負債、非流動負債（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR2_YEAR_INSTANT = 'Prior2YearInstant'


class Revenue2IFRS(Enum):
    """"収益（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'CurrentYTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    CURRENT_YTD_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'CurrentYTDDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1YTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_YTD_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'Prior1YTDDuration_ReportableSegmentsMember'
    """ 報告セグメント """


class RevenueFromExternalCustomersIFRS(Enum):
    """"外部顧客への売上収益（IFRS）"""
    CURRENT_QUARTER_DURATION = 'CurrentQuarterDuration'
    CURRENT_QUARTER_DURATION__RECONCILING_ITEMS_MEMBER = 'CurrentQuarterDuration_ReconcilingItemsMember'
    """ 調整項目 """
    CURRENT_QUARTER_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'CurrentQuarterDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
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
    CURRENT_YEAR_DURATION__OTHER_REPORTABLE_SEGMENTS_MEMBER = 'CurrentYearDuration_OtherReportableSegmentsMember'
    """ 当年度会計期間その他 """
    CURRENT_YEAR_DURATION__RECONCILING_ITEMS_MEMBER = 'CurrentYearDuration_ReconcilingItemsMember'
    """ 当年度会計期間調整項目 """
    CURRENT_YEAR_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'CurrentYearDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 当年度会計期間事業セグメント合計 """
    PRIOR1_QUARTER_DURATION = 'Prior1QuarterDuration'
    PRIOR1_QUARTER_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1QuarterDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_QUARTER_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'Prior1QuarterDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
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
    PRIOR1_YEAR_DURATION__OTHER_REPORTABLE_SEGMENTS_MEMBER = 'Prior1YearDuration_OtherReportableSegmentsMember'
    """ その他 """
    PRIOR1_YEAR_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1YearDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_YEAR_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1YearDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """


class RevenueIFRS(Enum):
    """"売上収益（IFRS）"""
    CURRENT_QUARTER_DURATION = 'CurrentQuarterDuration'
    CURRENT_QUARTER_DURATION__RECONCILING_ITEMS_MEMBER = 'CurrentQuarterDuration_ReconcilingItemsMember'
    """ 調整項目 """
    CURRENT_QUARTER_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'CurrentQuarterDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
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
    CURRENT_YEAR_DURATION__OTHER_REPORTABLE_SEGMENTS_MEMBER = 'CurrentYearDuration_OtherReportableSegmentsMember'
    """ 当年度会計期間その他 """
    CURRENT_YEAR_DURATION__RECONCILING_ITEMS_MEMBER = 'CurrentYearDuration_ReconcilingItemsMember'
    """ 当年度会計期間調整項目 """
    CURRENT_YEAR_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'CurrentYearDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 当年度会計期間事業セグメント合計 """
    PRIOR1_QUARTER_DURATION = 'Prior1QuarterDuration'
    PRIOR1_QUARTER_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1QuarterDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_QUARTER_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'Prior1QuarterDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
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
    PRIOR1_YEAR_DURATION__OTHER_REPORTABLE_SEGMENTS_MEMBER = 'Prior1YearDuration_OtherReportableSegmentsMember'
    """ その他 """
    PRIOR1_YEAR_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1YearDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_YEAR_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1YearDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """


class RightOfUseAssetsIFRS(Enum):
    """"使用権資産（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR2_YEAR_INSTANT = 'Prior2YearInstant'


class SalesToExternalCustomersIFRS(Enum):
    """"外部顧客への売上高（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
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
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
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


class SegmentProfitLossIFRS(Enum):
    """"セグメント利益（△損失）（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
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
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
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


class SellingExpensesIFRS(Enum):
    """"販売費（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class SellingGeneralAndAdministrativeExpensesIFRS(Enum):
    """"販売費及び一般管理費（IFRS）"""
    CURRENT_QUARTER_DURATION = 'CurrentQuarterDuration'
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_QUARTER_DURATION = 'Prior1QuarterDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class ShareBasedPaymentExpensesOpeCFIFRS(Enum):
    """"株式報酬費用、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ShareBasedPaymentTransactionsSSIFRS(Enum):
    """"株式報酬取引、持分変動計算書（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__ACCUMULATED_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'CurrentYTDDuration_AccumulatedOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益累計額 """
    CURRENT_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'CurrentYTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    CURRENT_YTD_DURATION__EFFECTIVE_PORTION_OF_CASH_FLOW_HEDGES_IFRS_MEMBER = 'CurrentYTDDuration_EffectivePortionOfCashFlowHedgesIFRSMember'
    """ キャッシュ・フロー・ヘッジの有効部分 """
    CURRENT_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'CurrentYTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    CURRENT_YTD_DURATION__EXCHANGE_DIFFERENCES_ON_TRANSLATION_OF_FOREIGN_OPERATIONS_IFRS_MEMBER = 'CurrentYTDDuration_ExchangeDifferencesOnTranslationOfForeignOperationsIFRSMember'
    """ 在外営業活動体の外貨換算差額 """
    CURRENT_YTD_DURATION__FINANCIAL_ASSETS_MEASURED_AT_FAIR_VALUE_THROUGH_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'CurrentYTDDuration_FinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益を通じて公正価値で測定する金融資産 """
    CURRENT_YTD_DURATION__NET_CHANGE_IN_FAIR_VALUE_OF_EQUITY_INSTRUMENTS_DESIGNATED_AS_MEASURED_AT_FAIR_VALUE_THROUGH_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'CurrentYTDDuration_NetChangeInFairValueOfEquityInstrumentsDesignatedAsMeasuredAtFairValueThroughOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益を通じて公正価値で測定するものとして指定した資本性金融商品の公正価値の純変動額 """
    CURRENT_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'CurrentYTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    CURRENT_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'CurrentYTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    CURRENT_YTD_DURATION__REMEASUREMENTS_OF_DEFINED_BENEFIT_PLANS_IFRS_MEMBER = 'CurrentYTDDuration_RemeasurementsOfDefinedBenefitPlansIFRSMember'
    """ 確定給付制度の再測定 """
    CURRENT_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'CurrentYTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    CURRENT_YTD_DURATION__SHARE_ACQUISITION_RIGHTS_IFRS_MEMBER = 'CurrentYTDDuration_ShareAcquisitionRightsIFRSMember'
    """ 新株予約権 """
    CURRENT_YTD_DURATION__SHARE_CAPITAL_IFRS_MEMBER = 'CurrentYTDDuration_ShareCapitalIFRSMember'
    """ 資本金 """
    CURRENT_YTD_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'CurrentYTDDuration_TreasurySharesIFRSMember'
    """ 自己株式 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'CurrentYearDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 当年度会計期間親会社の所有者に帰属する持分 """
    CURRENT_YEAR_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'CurrentYearDuration_OtherComponentsOfEquityIFRSMember'
    """ 当年度会計期間その他の資本の構成要素 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__ACCUMULATED_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'Prior1YTDDuration_AccumulatedOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益累計額 """
    PRIOR1_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'Prior1YTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    PRIOR1_YTD_DURATION__EFFECTIVE_PORTION_OF_CASH_FLOW_HEDGES_IFRS_MEMBER = 'Prior1YTDDuration_EffectivePortionOfCashFlowHedgesIFRSMember'
    """ キャッシュ・フロー・ヘッジの有効部分 """
    PRIOR1_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'Prior1YTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    PRIOR1_YTD_DURATION__EXCHANGE_DIFFERENCES_ON_TRANSLATION_OF_FOREIGN_OPERATIONS_IFRS_MEMBER = 'Prior1YTDDuration_ExchangeDifferencesOnTranslationOfForeignOperationsIFRSMember'
    """ 在外営業活動体の外貨換算差額 """
    PRIOR1_YTD_DURATION__FINANCIAL_ASSETS_MEASURED_AT_FAIR_VALUE_THROUGH_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'Prior1YTDDuration_FinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益を通じて公正価値で測定する金融資産 """
    PRIOR1_YTD_DURATION__NET_CHANGE_IN_FAIR_VALUE_OF_EQUITY_INSTRUMENTS_DESIGNATED_AS_MEASURED_AT_FAIR_VALUE_THROUGH_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'Prior1YTDDuration_NetChangeInFairValueOfEquityInstrumentsDesignatedAsMeasuredAtFairValueThroughOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益を通じて公正価値で測定するものとして指定した資本性金融商品の公正価値の純変動額 """
    PRIOR1_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'Prior1YTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    PRIOR1_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'Prior1YTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    PRIOR1_YTD_DURATION__REMEASUREMENTS_OF_DEFINED_BENEFIT_PLANS_IFRS_MEMBER = 'Prior1YTDDuration_RemeasurementsOfDefinedBenefitPlansIFRSMember'
    """ 確定給付制度の再測定 """
    PRIOR1_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'Prior1YTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    PRIOR1_YTD_DURATION__SHARE_ACQUISITION_RIGHTS_IFRS_MEMBER = 'Prior1YTDDuration_ShareAcquisitionRightsIFRSMember'
    """ 新株予約権 """
    PRIOR1_YTD_DURATION__SHARE_CAPITAL_IFRS_MEMBER = 'Prior1YTDDuration_ShareCapitalIFRSMember'
    """ 資本金 """
    PRIOR1_YTD_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'Prior1YTDDuration_TreasurySharesIFRSMember'
    """ 自己株式 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'Prior1YearDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    PRIOR1_YEAR_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'Prior1YearDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """


class ShareCapitalIFRS(Enum):
    """"資本金（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR2_YEAR_INSTANT = 'Prior2YearInstant'


class ShareOfLossProfitOfInvestmentsAccountedForUsingEquityMethodOpeCFIFRS(Enum):
    """"持分法による投資損益（△は益）、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class ShareOfOtherComprehensiveIncomeOfInvestmentsAccountedForUsingEquityMethodNetOfTaxItemsThatMayBeReclassifiedToProfitOrLossOCIIFRS(Enum):
    """"持分法によるその他の包括利益（税引後）、純損益に振り替えられる可能性のあるその他の包括利益（IFRS）"""
    CURRENT_QUARTER_DURATION = 'CurrentQuarterDuration'
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_QUARTER_DURATION = 'Prior1QuarterDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ShareOfOtherComprehensiveIncomeOfInvestmentsAccountedForUsingEquityMethodNetOfTaxItemsThatWillNotBeReclassifiedToProfitOrLossOCIIFRS(Enum):
    """"持分法によるその他の包括利益（税引後）、純損益に振り替えられることのないその他の包括利益（IFRS）"""
    CURRENT_QUARTER_DURATION = 'CurrentQuarterDuration'
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_QUARTER_DURATION = 'Prior1QuarterDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ShareOfProfitLossOfInvestmentsAccountedForUsingEquityMethodIFRS(Enum):
    """"持分法による投資損益（△は損失）（IFRS）"""
    CURRENT_QUARTER_DURATION = 'CurrentQuarterDuration'
    CURRENT_QUARTER_DURATION__RECONCILING_ITEMS_MEMBER = 'CurrentQuarterDuration_ReconcilingItemsMember'
    """ 調整項目 """
    CURRENT_QUARTER_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'CurrentQuarterDuration_ReportableSegmentsMember'
    """ 報告セグメント """
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
    PRIOR1_QUARTER_DURATION = 'Prior1QuarterDuration'
    PRIOR1_QUARTER_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1QuarterDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_QUARTER_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'Prior1QuarterDuration_ReportableSegmentsMember'
    """ 報告セグメント """
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


class SubtotalOpeCFIFRS(Enum):
    """"小計、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class TimeDepositsCAIFRS(Enum):
    """"定期預金、流動資産（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class TotalChangesInEquityIFRS(Enum):
    """"変動額合計（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'CurrentYTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    CURRENT_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'CurrentYTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    CURRENT_YTD_DURATION__EXCHANGE_DIFFERENCES_ON_TRANSLATION_OF_FOREIGN_OPERATIONS_IFRS_MEMBER = 'CurrentYTDDuration_ExchangeDifferencesOnTranslationOfForeignOperationsIFRSMember'
    """ 在外営業活動体の外貨換算差額 """
    CURRENT_YTD_DURATION__FINANCIAL_ASSETS_MEASURED_AT_FAIR_VALUE_THROUGH_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'CurrentYTDDuration_FinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益を通じて公正価値で測定する金融資産 """
    CURRENT_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'CurrentYTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    CURRENT_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'CurrentYTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    CURRENT_YTD_DURATION__REMEASUREMENTS_OF_DEFINED_BENEFIT_PLANS_IFRS_MEMBER = 'CurrentYTDDuration_RemeasurementsOfDefinedBenefitPlansIFRSMember'
    """ 確定給付制度の再測定 """
    CURRENT_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'CurrentYTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    CURRENT_YTD_DURATION__SHARE_ACQUISITION_RIGHTS_IFRS_MEMBER = 'CurrentYTDDuration_ShareAcquisitionRightsIFRSMember'
    """ 新株予約権 """
    CURRENT_YTD_DURATION__SHARE_CAPITAL_IFRS_MEMBER = 'CurrentYTDDuration_ShareCapitalIFRSMember'
    """ 資本金 """
    CURRENT_YTD_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'CurrentYTDDuration_TreasurySharesIFRSMember'
    """ 自己株式 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'Prior1YTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    PRIOR1_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'Prior1YTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    PRIOR1_YTD_DURATION__EXCHANGE_DIFFERENCES_ON_TRANSLATION_OF_FOREIGN_OPERATIONS_IFRS_MEMBER = 'Prior1YTDDuration_ExchangeDifferencesOnTranslationOfForeignOperationsIFRSMember'
    """ 在外営業活動体の外貨換算差額 """
    PRIOR1_YTD_DURATION__FINANCIAL_ASSETS_MEASURED_AT_FAIR_VALUE_THROUGH_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'Prior1YTDDuration_FinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益を通じて公正価値で測定する金融資産 """
    PRIOR1_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'Prior1YTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    PRIOR1_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'Prior1YTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    PRIOR1_YTD_DURATION__REMEASUREMENTS_OF_DEFINED_BENEFIT_PLANS_IFRS_MEMBER = 'Prior1YTDDuration_RemeasurementsOfDefinedBenefitPlansIFRSMember'
    """ 確定給付制度の再測定 """
    PRIOR1_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'Prior1YTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    PRIOR1_YTD_DURATION__SHARE_ACQUISITION_RIGHTS_IFRS_MEMBER = 'Prior1YTDDuration_ShareAcquisitionRightsIFRSMember'
    """ 新株予約権 """
    PRIOR1_YTD_DURATION__SHARE_CAPITAL_IFRS_MEMBER = 'Prior1YTDDuration_ShareCapitalIFRSMember'
    """ 資本金 """
    PRIOR1_YTD_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'Prior1YTDDuration_TreasurySharesIFRSMember'
    """ 自己株式 """


class TotalCurrentLiabilitiesIFRS(Enum):
    """"流動負債（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR2_YEAR_INSTANT = 'Prior2YearInstant'


class TotalOfItemsThatMayBeReclassifiedToProfitOrLossOCIIFRS(Enum):
    """"純損益に振り替えられる可能性のある項目合計（IFRS）"""
    CURRENT_QUARTER_DURATION = 'CurrentQuarterDuration'
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_QUARTER_DURATION = 'Prior1QuarterDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class TotalOfItemsThatWillNotBeReclassifiedToProfitOrLossOCIIFRS(Enum):
    """"純損益に振り替えられることのない項目合計（IFRS）"""
    CURRENT_QUARTER_DURATION = 'CurrentQuarterDuration'
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_QUARTER_DURATION = 'Prior1QuarterDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class TotalTransactionsWithOwnersIFRS(Enum):
    """"所有者との取引額（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__ACCUMULATED_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'CurrentYTDDuration_AccumulatedOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益累計額 """
    CURRENT_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'CurrentYTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    CURRENT_YTD_DURATION__EFFECTIVE_PORTION_OF_CASH_FLOW_HEDGES_IFRS_MEMBER = 'CurrentYTDDuration_EffectivePortionOfCashFlowHedgesIFRSMember'
    """ キャッシュ・フロー・ヘッジの有効部分 """
    CURRENT_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'CurrentYTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    CURRENT_YTD_DURATION__EXCHANGE_DIFFERENCES_ON_TRANSLATION_OF_FOREIGN_OPERATIONS_IFRS_MEMBER = 'CurrentYTDDuration_ExchangeDifferencesOnTranslationOfForeignOperationsIFRSMember'
    """ 在外営業活動体の外貨換算差額 """
    CURRENT_YTD_DURATION__FINANCIAL_ASSETS_MEASURED_AT_FAIR_VALUE_THROUGH_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'CurrentYTDDuration_FinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益を通じて公正価値で測定する金融資産 """
    CURRENT_YTD_DURATION__NET_CHANGE_IN_FAIR_VALUE_OF_EQUITY_INSTRUMENTS_DESIGNATED_AS_MEASURED_AT_FAIR_VALUE_THROUGH_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'CurrentYTDDuration_NetChangeInFairValueOfEquityInstrumentsDesignatedAsMeasuredAtFairValueThroughOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益を通じて公正価値で測定するものとして指定した資本性金融商品の公正価値の純変動額 """
    CURRENT_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'CurrentYTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    CURRENT_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'CurrentYTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    CURRENT_YTD_DURATION__REMEASUREMENTS_OF_DEFINED_BENEFIT_PLANS_IFRS_MEMBER = 'CurrentYTDDuration_RemeasurementsOfDefinedBenefitPlansIFRSMember'
    """ 確定給付制度の再測定 """
    CURRENT_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'CurrentYTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    CURRENT_YTD_DURATION__SHARE_ACQUISITION_RIGHTS_IFRS_MEMBER = 'CurrentYTDDuration_ShareAcquisitionRightsIFRSMember'
    """ 新株予約権 """
    CURRENT_YTD_DURATION__SHARE_CAPITAL_IFRS_MEMBER = 'CurrentYTDDuration_ShareCapitalIFRSMember'
    """ 資本金 """
    CURRENT_YTD_DURATION__SHARE_OF_OTHER_COMPREHENSIVE_INCOME_OF_INVESTMENTS_ACCOUNTED_FOR_USING_EQUITY_METHOD_IFRS_MEMBER = 'CurrentYTDDuration_ShareOfOtherComprehensiveIncomeOfInvestmentsAccountedForUsingEquityMethodIFRSMember'
    """ 持分法によるその他の包括利益 """
    CURRENT_YTD_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'CurrentYTDDuration_TreasurySharesIFRSMember'
    """ 自己株式 """
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    CURRENT_YEAR_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'CurrentYearDuration_CapitalSurplusIFRSMember'
    """ 当年度会計期間資本剰余金 """
    CURRENT_YEAR_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'CurrentYearDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 当年度会計期間親会社の所有者に帰属する持分 """
    CURRENT_YEAR_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'CurrentYearDuration_NonControllingInterestsIFRSMember'
    """ 当年度会計期間非支配持分 """
    CURRENT_YEAR_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'CurrentYearDuration_OtherComponentsOfEquityIFRSMember'
    """ 当年度会計期間その他の資本の構成要素 """
    CURRENT_YEAR_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'CurrentYearDuration_RetainedEarningsIFRSMember'
    """ 当年度会計期間利益剰余金 """
    CURRENT_YEAR_DURATION__SHARE_CAPITAL_IFRS_MEMBER = 'CurrentYearDuration_ShareCapitalIFRSMember'
    """ 当年度会計期間資本金 """
    CURRENT_YEAR_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'CurrentYearDuration_TreasurySharesIFRSMember'
    """ 当年度会計期間自己株式 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__ACCUMULATED_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'Prior1YTDDuration_AccumulatedOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益累計額 """
    PRIOR1_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'Prior1YTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    PRIOR1_YTD_DURATION__EFFECTIVE_PORTION_OF_CASH_FLOW_HEDGES_IFRS_MEMBER = 'Prior1YTDDuration_EffectivePortionOfCashFlowHedgesIFRSMember'
    """ キャッシュ・フロー・ヘッジの有効部分 """
    PRIOR1_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'Prior1YTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    PRIOR1_YTD_DURATION__EXCHANGE_DIFFERENCES_ON_TRANSLATION_OF_FOREIGN_OPERATIONS_IFRS_MEMBER = 'Prior1YTDDuration_ExchangeDifferencesOnTranslationOfForeignOperationsIFRSMember'
    """ 在外営業活動体の外貨換算差額 """
    PRIOR1_YTD_DURATION__FINANCIAL_ASSETS_MEASURED_AT_FAIR_VALUE_THROUGH_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'Prior1YTDDuration_FinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益を通じて公正価値で測定する金融資産 """
    PRIOR1_YTD_DURATION__NET_CHANGE_IN_FAIR_VALUE_OF_EQUITY_INSTRUMENTS_DESIGNATED_AS_MEASURED_AT_FAIR_VALUE_THROUGH_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'Prior1YTDDuration_NetChangeInFairValueOfEquityInstrumentsDesignatedAsMeasuredAtFairValueThroughOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益を通じて公正価値で測定するものとして指定した資本性金融商品の公正価値の純変動額 """
    PRIOR1_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'Prior1YTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    PRIOR1_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'Prior1YTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    PRIOR1_YTD_DURATION__REMEASUREMENTS_OF_DEFINED_BENEFIT_PLANS_IFRS_MEMBER = 'Prior1YTDDuration_RemeasurementsOfDefinedBenefitPlansIFRSMember'
    """ 確定給付制度の再測定 """
    PRIOR1_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'Prior1YTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    PRIOR1_YTD_DURATION__SHARE_ACQUISITION_RIGHTS_IFRS_MEMBER = 'Prior1YTDDuration_ShareAcquisitionRightsIFRSMember'
    """ 新株予約権 """
    PRIOR1_YTD_DURATION__SHARE_CAPITAL_IFRS_MEMBER = 'Prior1YTDDuration_ShareCapitalIFRSMember'
    """ 資本金 """
    PRIOR1_YTD_DURATION__SHARE_OF_OTHER_COMPREHENSIVE_INCOME_OF_INVESTMENTS_ACCOUNTED_FOR_USING_EQUITY_METHOD_IFRS_MEMBER = 'Prior1YTDDuration_ShareOfOtherComprehensiveIncomeOfInvestmentsAccountedForUsingEquityMethodIFRSMember'
    """ 持分法によるその他の包括利益 """
    PRIOR1_YTD_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'Prior1YTDDuration_TreasurySharesIFRSMember'
    """ 自己株式 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'
    PRIOR1_YEAR_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'Prior1YearDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    PRIOR1_YEAR_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'Prior1YearDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    PRIOR1_YEAR_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'Prior1YearDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    PRIOR1_YEAR_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'Prior1YearDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    PRIOR1_YEAR_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'Prior1YearDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    PRIOR1_YEAR_DURATION__SHARE_CAPITAL_IFRS_MEMBER = 'Prior1YearDuration_ShareCapitalIFRSMember'
    """ 資本金 """
    PRIOR1_YEAR_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'Prior1YearDuration_TreasurySharesIFRSMember'
    """ 自己株式 """


class TradeAndOtherPayables2CLIFRS(Enum):
    """"仕入債務及びその他の債務、流動負債（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class TradeAndOtherPayables2NCLIFRS(Enum):
    """"仕入債務及びその他の債務、非流動負債（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class TradeAndOtherPayablesCLIFRS(Enum):
    """"営業債務及びその他の債務、流動負債（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR2_YEAR_INSTANT = 'Prior2YearInstant'


class TradeAndOtherPayablesLiabilitiesIFRS(Enum):
    """"営業債務及びその他の債務、負債（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class TradeAndOtherPayablesNCLIFRS(Enum):
    """"営業債務及びその他の債務、非流動負債（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class TradeAndOtherReceivables2CAIFRS(Enum):
    """"売上債権及びその他の債権、流動資産（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class TradeAndOtherReceivablesAssetsIFRS(Enum):
    """"営業債権及びその他の債権、資産（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class TradeAndOtherReceivablesCAIFRS(Enum):
    """"営業債権及びその他の債権、流動資産（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR2_YEAR_INSTANT = 'Prior2YearInstant'


class TradeAndOtherReceivablesNCAIFRS(Enum):
    """"営業債権及びその他の債権、非流動資産（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class TradePayables3CLIFRS(Enum):
    """"買入債務、流動負債（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class TradePayablesCLIFRS(Enum):
    """"営業債務、流動負債（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class TradeReceivables2CAIFRS(Enum):
    """"売上債権、流動資産（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class TradeReceivablesCAIFRS(Enum):
    """"営業債権、流動資産（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class TransferFromAccumulatedOtherComprehensiveIncomeToRetainedEarningsSSIFRS(Enum):
    """"その他の包括利益累計額から利益剰余金への振替、持分変動計算書（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__ACCUMULATED_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'CurrentYTDDuration_AccumulatedOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益累計額 """
    CURRENT_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'CurrentYTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    CURRENT_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'CurrentYTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    CURRENT_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'CurrentYTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    CURRENT_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'CurrentYTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    CURRENT_YTD_DURATION__SHARE_CAPITAL_IFRS_MEMBER = 'CurrentYTDDuration_ShareCapitalIFRSMember'
    """ 資本金 """
    CURRENT_YTD_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'CurrentYTDDuration_TreasurySharesIFRSMember'
    """ 自己株式 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__ACCUMULATED_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'Prior1YTDDuration_AccumulatedOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益累計額 """
    PRIOR1_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'Prior1YTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    PRIOR1_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'Prior1YTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    PRIOR1_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'Prior1YTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    PRIOR1_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'Prior1YTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    PRIOR1_YTD_DURATION__SHARE_CAPITAL_IFRS_MEMBER = 'Prior1YTDDuration_ShareCapitalIFRSMember'
    """ 資本金 """
    PRIOR1_YTD_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'Prior1YTDDuration_TreasurySharesIFRSMember'
    """ 自己株式 """


class TransferFromOtherComponentsOfEquityToRetainedEarningsSSIFRS(Enum):
    """"その他の資本の構成要素から利益剰余金への振替、持分変動計算書（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'CurrentYTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    CURRENT_YTD_DURATION__EFFECTIVE_PORTION_OF_CASH_FLOW_HEDGES_IFRS_MEMBER = 'CurrentYTDDuration_EffectivePortionOfCashFlowHedgesIFRSMember'
    """ キャッシュ・フロー・ヘッジの有効部分 """
    CURRENT_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'CurrentYTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    CURRENT_YTD_DURATION__EXCHANGE_DIFFERENCES_ON_TRANSLATION_OF_FOREIGN_OPERATIONS_IFRS_MEMBER = 'CurrentYTDDuration_ExchangeDifferencesOnTranslationOfForeignOperationsIFRSMember'
    """ 在外営業活動体の外貨換算差額 """
    CURRENT_YTD_DURATION__FINANCIAL_ASSETS_MEASURED_AT_FAIR_VALUE_THROUGH_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'CurrentYTDDuration_FinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益を通じて公正価値で測定する金融資産 """
    CURRENT_YTD_DURATION__NET_CHANGE_IN_FAIR_VALUE_OF_EQUITY_INSTRUMENTS_DESIGNATED_AS_MEASURED_AT_FAIR_VALUE_THROUGH_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'CurrentYTDDuration_NetChangeInFairValueOfEquityInstrumentsDesignatedAsMeasuredAtFairValueThroughOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益を通じて公正価値で測定するものとして指定した資本性金融商品の公正価値の純変動額 """
    CURRENT_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'CurrentYTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    CURRENT_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'CurrentYTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    CURRENT_YTD_DURATION__REMEASUREMENTS_OF_DEFINED_BENEFIT_PLANS_IFRS_MEMBER = 'CurrentYTDDuration_RemeasurementsOfDefinedBenefitPlansIFRSMember'
    """ 確定給付制度の再測定 """
    CURRENT_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'CurrentYTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    CURRENT_YTD_DURATION__SHARE_CAPITAL_IFRS_MEMBER = 'CurrentYTDDuration_ShareCapitalIFRSMember'
    """ 資本金 """
    CURRENT_YTD_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'CurrentYTDDuration_TreasurySharesIFRSMember'
    """ 自己株式 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'Prior1YTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    PRIOR1_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'Prior1YTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    PRIOR1_YTD_DURATION__EXCHANGE_DIFFERENCES_ON_TRANSLATION_OF_FOREIGN_OPERATIONS_IFRS_MEMBER = 'Prior1YTDDuration_ExchangeDifferencesOnTranslationOfForeignOperationsIFRSMember'
    """ 在外営業活動体の外貨換算差額 """
    PRIOR1_YTD_DURATION__FINANCIAL_ASSETS_MEASURED_AT_FAIR_VALUE_THROUGH_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'Prior1YTDDuration_FinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益を通じて公正価値で測定する金融資産 """
    PRIOR1_YTD_DURATION__NET_CHANGE_IN_FAIR_VALUE_OF_EQUITY_INSTRUMENTS_DESIGNATED_AS_MEASURED_AT_FAIR_VALUE_THROUGH_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'Prior1YTDDuration_NetChangeInFairValueOfEquityInstrumentsDesignatedAsMeasuredAtFairValueThroughOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益を通じて公正価値で測定するものとして指定した資本性金融商品の公正価値の純変動額 """
    PRIOR1_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'Prior1YTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    PRIOR1_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'Prior1YTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    PRIOR1_YTD_DURATION__REMEASUREMENTS_OF_DEFINED_BENEFIT_PLANS_IFRS_MEMBER = 'Prior1YTDDuration_RemeasurementsOfDefinedBenefitPlansIFRSMember'
    """ 確定給付制度の再測定 """
    PRIOR1_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'Prior1YTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    PRIOR1_YTD_DURATION__SHARE_CAPITAL_IFRS_MEMBER = 'Prior1YTDDuration_ShareCapitalIFRSMember'
    """ 資本金 """
    PRIOR1_YTD_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'Prior1YTDDuration_TreasurySharesIFRSMember'
    """ 自己株式 """


class TransferSSIFRS(Enum):
    """"振替、持分変動計算書（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'CurrentYTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    CURRENT_YTD_DURATION__EFFECTIVE_PORTION_OF_CASH_FLOW_HEDGES_IFRS_MEMBER = 'CurrentYTDDuration_EffectivePortionOfCashFlowHedgesIFRSMember'
    """ キャッシュ・フロー・ヘッジの有効部分 """
    CURRENT_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'CurrentYTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    CURRENT_YTD_DURATION__EXCHANGE_DIFFERENCES_ON_TRANSLATION_OF_FOREIGN_OPERATIONS_IFRS_MEMBER = 'CurrentYTDDuration_ExchangeDifferencesOnTranslationOfForeignOperationsIFRSMember'
    """ 在外営業活動体の外貨換算差額 """
    CURRENT_YTD_DURATION__FINANCIAL_ASSETS_MEASURED_AT_FAIR_VALUE_THROUGH_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'CurrentYTDDuration_FinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益を通じて公正価値で測定する金融資産 """
    CURRENT_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'CurrentYTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    CURRENT_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'CurrentYTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    CURRENT_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'CurrentYTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    CURRENT_YTD_DURATION__SHARE_CAPITAL_IFRS_MEMBER = 'CurrentYTDDuration_ShareCapitalIFRSMember'
    """ 資本金 """
    CURRENT_YTD_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'CurrentYTDDuration_TreasurySharesIFRSMember'
    """ 自己株式 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'Prior1YTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    PRIOR1_YTD_DURATION__EFFECTIVE_PORTION_OF_CASH_FLOW_HEDGES_IFRS_MEMBER = 'Prior1YTDDuration_EffectivePortionOfCashFlowHedgesIFRSMember'
    """ キャッシュ・フロー・ヘッジの有効部分 """
    PRIOR1_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'Prior1YTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    PRIOR1_YTD_DURATION__EXCHANGE_DIFFERENCES_ON_TRANSLATION_OF_FOREIGN_OPERATIONS_IFRS_MEMBER = 'Prior1YTDDuration_ExchangeDifferencesOnTranslationOfForeignOperationsIFRSMember'
    """ 在外営業活動体の外貨換算差額 """
    PRIOR1_YTD_DURATION__FINANCIAL_ASSETS_MEASURED_AT_FAIR_VALUE_THROUGH_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'Prior1YTDDuration_FinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益を通じて公正価値で測定する金融資産 """
    PRIOR1_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'Prior1YTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    PRIOR1_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'Prior1YTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    PRIOR1_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'Prior1YTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    PRIOR1_YTD_DURATION__SHARE_CAPITAL_IFRS_MEMBER = 'Prior1YTDDuration_ShareCapitalIFRSMember'
    """ 資本金 """
    PRIOR1_YTD_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'Prior1YTDDuration_TreasurySharesIFRSMember'
    """ 自己株式 """


class TransferToRetainedEarningsSSIFRS(Enum):
    """"利益剰余金への振替、持分変動計算書（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__ACCUMULATED_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'CurrentYTDDuration_AccumulatedOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益累計額 """
    CURRENT_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'CurrentYTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    CURRENT_YTD_DURATION__EFFECTIVE_PORTION_OF_CASH_FLOW_HEDGES_IFRS_MEMBER = 'CurrentYTDDuration_EffectivePortionOfCashFlowHedgesIFRSMember'
    """ キャッシュ・フロー・ヘッジの有効部分 """
    CURRENT_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'CurrentYTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    CURRENT_YTD_DURATION__EXCHANGE_DIFFERENCES_ON_TRANSLATION_OF_FOREIGN_OPERATIONS_IFRS_MEMBER = 'CurrentYTDDuration_ExchangeDifferencesOnTranslationOfForeignOperationsIFRSMember'
    """ 在外営業活動体の外貨換算差額 """
    CURRENT_YTD_DURATION__FINANCIAL_ASSETS_MEASURED_AT_FAIR_VALUE_THROUGH_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'CurrentYTDDuration_FinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益を通じて公正価値で測定する金融資産 """
    CURRENT_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'CurrentYTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    CURRENT_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'CurrentYTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    CURRENT_YTD_DURATION__REMEASUREMENTS_OF_DEFINED_BENEFIT_PLANS_IFRS_MEMBER = 'CurrentYTDDuration_RemeasurementsOfDefinedBenefitPlansIFRSMember'
    """ 確定給付制度の再測定 """
    CURRENT_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'CurrentYTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    CURRENT_YTD_DURATION__SHARE_CAPITAL_IFRS_MEMBER = 'CurrentYTDDuration_ShareCapitalIFRSMember'
    """ 資本金 """
    CURRENT_YTD_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'CurrentYTDDuration_TreasurySharesIFRSMember'
    """ 自己株式 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__ACCUMULATED_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'Prior1YTDDuration_AccumulatedOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益累計額 """
    PRIOR1_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'Prior1YTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    PRIOR1_YTD_DURATION__EFFECTIVE_PORTION_OF_CASH_FLOW_HEDGES_IFRS_MEMBER = 'Prior1YTDDuration_EffectivePortionOfCashFlowHedgesIFRSMember'
    """ キャッシュ・フロー・ヘッジの有効部分 """
    PRIOR1_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'Prior1YTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    PRIOR1_YTD_DURATION__EXCHANGE_DIFFERENCES_ON_TRANSLATION_OF_FOREIGN_OPERATIONS_IFRS_MEMBER = 'Prior1YTDDuration_ExchangeDifferencesOnTranslationOfForeignOperationsIFRSMember'
    """ 在外営業活動体の外貨換算差額 """
    PRIOR1_YTD_DURATION__FINANCIAL_ASSETS_MEASURED_AT_FAIR_VALUE_THROUGH_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'Prior1YTDDuration_FinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益を通じて公正価値で測定する金融資産 """
    PRIOR1_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'Prior1YTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    PRIOR1_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'Prior1YTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    PRIOR1_YTD_DURATION__REMEASUREMENTS_OF_DEFINED_BENEFIT_PLANS_IFRS_MEMBER = 'Prior1YTDDuration_RemeasurementsOfDefinedBenefitPlansIFRSMember'
    """ 確定給付制度の再測定 """
    PRIOR1_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'Prior1YTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    PRIOR1_YTD_DURATION__SHARE_CAPITAL_IFRS_MEMBER = 'Prior1YTDDuration_ShareCapitalIFRSMember'
    """ 資本金 """
    PRIOR1_YTD_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'Prior1YTDDuration_TreasurySharesIFRSMember'
    """ 自己株式 """


class TreasurySharesIFRS(Enum):
    """"自己株式（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'
    PRIOR2_YEAR_INSTANT = 'Prior2YearInstant'


class AmountOfRentOffsetByLeaseAndGuaranteeDepositsOpeCFIFRS(Enum):
    """"敷金及び保証金の家賃相殺額、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class IncreaseDecreaseInProvisionForBonusesOpeCFIFRS(Enum):
    """"賞与引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class LeaseAndGuaranteeDepositsNCAIFRS(Enum):
    """"敷金及び保証金、非流動資産（IFRS）"""
    CURRENT_YEAR_INSTANT = 'CurrentYearInstant'
    """ 当年度時点 """
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class NetChangeInFairValueOfInstrumentsMeasuredAtFairValueThroughOtherComprehensiveIncomeItemsThatWillNotBeReclassifiedToProfitOrLossOCIIFRS(Enum):
    """"その他の包括利益を通じて測定する金融資産の公正価値の純変動、純損益に振り替えられることのないその他の包括利益（IFRS）"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class PaymentsForCommissionFeesFinCFIFRS(Enum):
    """"支払手数料の支払による支出、財務活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YEAR_DURATION = 'CurrentYearDuration'
    """ 当年度会計期間 """
    PRIOR1_YEAR_DURATION = 'Prior1YearDuration'


class AccruedLaborExpensesCLIFRS(Enum):
    """"未払人件費、流動負債（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ChangesInPutOptionLiabilitiesRelatedToNonControllingInterestsSSIFRS(Enum):
    """"非支配株主に係る売建プット・オプション負債の変動等、持分変動計算書（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'CurrentYTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    CURRENT_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'CurrentYTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    CURRENT_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'CurrentYTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """


class IncreaseDecreaseInAccruedConsumptionTaxesOpeCFIFRS(Enum):
    """"未払消費税等の増減額（△は減少）、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInAccruedLaborExpensesOpeCFIFRS(Enum):
    """"未払人件費の増減額（△は減少）、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInLeaseReceivablesOpeCFIFRS(Enum):
    """"リース債権の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInPrepaidExpensesOpeCFIFRS(Enum):
    """"前払費用の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class CoreOperatingProfitLossIFRS(Enum):
    """"事業利益（△損失）（IFRS）"""
    CURRENT_QUARTER_DURATION = 'CurrentQuarterDuration'
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_QUARTER_DURATION = 'Prior1QuarterDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class CurrentPortionOfBondsCLIFRS(Enum):
    """"1年内償還社債、流動負債（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class HedgingCostNetOfTaxItemsThatMayBeReclassifiedToProfitOrLossOCIIFRS(Enum):
    """"ヘッジコスト（税引後）、純損益に振替えられる可能性のあるその他の包括利益（IFRS）"""
    CURRENT_QUARTER_DURATION = 'CurrentQuarterDuration'
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_QUARTER_DURATION = 'Prior1QuarterDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncomeBySettlementInDerivativesFinCFIFRS(Enum):
    """"デリバティブの決済による収入、財務活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class OperatingIncomeLossIFRS(Enum):
    """"事業利益（△は損失）（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'CurrentYTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1YTDDuration_ReconcilingItemsMember'
    """ 調整項目 """


class ProceedsFromSaleAndRedemptionOfOtherFinancialAssetsInvCFIFRS(Enum):
    """"その他の金融資産の売却及び償還による収入、投資活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PurchaseOfSharesOfSubsidiariesResultingInNoChangeInScopeOfConsolidationFinCFIFRS(Enum):
    """"連結範囲の変更を伴わない子会社株式の取得による支出、財務活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class TransferToNonFinancialAssetsSSIFRS(Enum):
    """"非金融資産等への振替、持分変動計算書（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'CurrentYTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    CURRENT_YTD_DURATION__EFFECTIVE_PORTION_OF_CASH_FLOW_HEDGES_IFRS_MEMBER = 'CurrentYTDDuration_EffectivePortionOfCashFlowHedgesIFRSMember'
    """ キャッシュ・フロー・ヘッジの有効部分 """
    CURRENT_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'CurrentYTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    CURRENT_YTD_DURATION__EXCHANGE_DIFFERENCES_ON_TRANSLATION_OF_FOREIGN_OPERATIONS_IFRS_MEMBER = 'CurrentYTDDuration_ExchangeDifferencesOnTranslationOfForeignOperationsIFRSMember'
    """ 在外営業活動体の外貨換算差額 """
    CURRENT_YTD_DURATION__FINANCIAL_ASSETS_MEASURED_AT_FAIR_VALUE_THROUGH_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'CurrentYTDDuration_FinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益を通じて公正価値で測定する金融資産 """
    CURRENT_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'CurrentYTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    CURRENT_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'CurrentYTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    CURRENT_YTD_DURATION__REMEASUREMENTS_OF_DEFINED_BENEFIT_PLANS_IFRS_MEMBER = 'CurrentYTDDuration_RemeasurementsOfDefinedBenefitPlansIFRSMember'
    """ 確定給付制度の再測定 """
    CURRENT_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'CurrentYTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    CURRENT_YTD_DURATION__SHARE_CAPITAL_IFRS_MEMBER = 'CurrentYTDDuration_ShareCapitalIFRSMember'
    """ 資本金 """
    CURRENT_YTD_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'CurrentYTDDuration_TreasurySharesIFRSMember'
    """ 自己株式 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'Prior1YTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    PRIOR1_YTD_DURATION__EFFECTIVE_PORTION_OF_CASH_FLOW_HEDGES_IFRS_MEMBER = 'Prior1YTDDuration_EffectivePortionOfCashFlowHedgesIFRSMember'
    """ キャッシュ・フロー・ヘッジの有効部分 """
    PRIOR1_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'Prior1YTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    PRIOR1_YTD_DURATION__EXCHANGE_DIFFERENCES_ON_TRANSLATION_OF_FOREIGN_OPERATIONS_IFRS_MEMBER = 'Prior1YTDDuration_ExchangeDifferencesOnTranslationOfForeignOperationsIFRSMember'
    """ 在外営業活動体の外貨換算差額 """
    PRIOR1_YTD_DURATION__FINANCIAL_ASSETS_MEASURED_AT_FAIR_VALUE_THROUGH_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'Prior1YTDDuration_FinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益を通じて公正価値で測定する金融資産 """
    PRIOR1_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'Prior1YTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    PRIOR1_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'Prior1YTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    PRIOR1_YTD_DURATION__REMEASUREMENTS_OF_DEFINED_BENEFIT_PLANS_IFRS_MEMBER = 'Prior1YTDDuration_RemeasurementsOfDefinedBenefitPlansIFRSMember'
    """ 確定給付制度の再測定 """
    PRIOR1_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'Prior1YTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    PRIOR1_YTD_DURATION__SHARE_CAPITAL_IFRS_MEMBER = 'Prior1YTDDuration_ShareCapitalIFRSMember'
    """ 資本金 """
    PRIOR1_YTD_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'Prior1YTDDuration_TreasurySharesIFRSMember'
    """ 自己株式 """


class DecreaseIncreaseInAdvancePaymentsToSuppliersOpeCFIFRS(Enum):
    """"前渡金の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInBonusPayableOpeCFIFRS(Enum):
    """"未払賞与の増減額(△は減少)、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInConsumptionTaxPayableEtcOpeCFIFRS(Enum):
    """"未払消費税等の増減額(△は減少)、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromSaleAndRedemptionOfOtherFinancialAssetsInvCFIFRS(Enum):
    """"その他の金融資産の売却及び償還による収入、投資活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PurchaseOfTreasurySharesOfSubsidiariesFinCFIFRS(Enum):
    """"子会社の自己株式の取得による支出、財務活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class TraChangesInOwnershipInterestInSubsidiariesIFRS(Enum):
    """"非支配株主との取引に係る親会社の持分変動（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'CurrentYTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    CURRENT_YTD_DURATION__EFFECTIVE_PORTION_OF_CASH_FLOW_HEDGES_IFRS_MEMBER = 'CurrentYTDDuration_EffectivePortionOfCashFlowHedgesIFRSMember'
    """ キャッシュ・フロー・ヘッジの有効部分 """
    CURRENT_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'CurrentYTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    CURRENT_YTD_DURATION__EXCHANGE_DIFFERENCES_ON_TRANSLATION_OF_FOREIGN_OPERATIONS_IFRS_MEMBER = 'CurrentYTDDuration_ExchangeDifferencesOnTranslationOfForeignOperationsIFRSMember'
    """ 在外営業活動体の外貨換算差額 """
    CURRENT_YTD_DURATION__FINANCIAL_ASSETS_MEASURED_AT_FAIR_VALUE_THROUGH_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'CurrentYTDDuration_FinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益を通じて公正価値で測定する金融資産 """
    CURRENT_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'CurrentYTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    CURRENT_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'CurrentYTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    CURRENT_YTD_DURATION__REMEASUREMENTS_OF_DEFINED_BENEFIT_PLANS_IFRS_MEMBER = 'CurrentYTDDuration_RemeasurementsOfDefinedBenefitPlansIFRSMember'
    """ 確定給付制度の再測定 """
    CURRENT_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'CurrentYTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    CURRENT_YTD_DURATION__SHARE_CAPITAL_IFRS_MEMBER = 'CurrentYTDDuration_ShareCapitalIFRSMember'
    """ 資本金 """
    CURRENT_YTD_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'CurrentYTDDuration_TreasurySharesIFRSMember'
    """ 自己株式 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'Prior1YTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    PRIOR1_YTD_DURATION__EFFECTIVE_PORTION_OF_CASH_FLOW_HEDGES_IFRS_MEMBER = 'Prior1YTDDuration_EffectivePortionOfCashFlowHedgesIFRSMember'
    """ キャッシュ・フロー・ヘッジの有効部分 """
    PRIOR1_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'Prior1YTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    PRIOR1_YTD_DURATION__EXCHANGE_DIFFERENCES_ON_TRANSLATION_OF_FOREIGN_OPERATIONS_IFRS_MEMBER = 'Prior1YTDDuration_ExchangeDifferencesOnTranslationOfForeignOperationsIFRSMember'
    """ 在外営業活動体の外貨換算差額 """
    PRIOR1_YTD_DURATION__FINANCIAL_ASSETS_MEASURED_AT_FAIR_VALUE_THROUGH_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'Prior1YTDDuration_FinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益を通じて公正価値で測定する金融資産 """
    PRIOR1_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'Prior1YTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    PRIOR1_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'Prior1YTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    PRIOR1_YTD_DURATION__REMEASUREMENTS_OF_DEFINED_BENEFIT_PLANS_IFRS_MEMBER = 'Prior1YTDDuration_RemeasurementsOfDefinedBenefitPlansIFRSMember'
    """ 確定給付制度の再測定 """
    PRIOR1_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'Prior1YTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    PRIOR1_YTD_DURATION__SHARE_CAPITAL_IFRS_MEMBER = 'Prior1YTDDuration_ShareCapitalIFRSMember'
    """ 資本金 """
    PRIOR1_YTD_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'Prior1YTDDuration_TreasurySharesIFRSMember'
    """ 自己株式 """


class BusinessprofitIFRS(Enum):
    """"事業利益（IFRS）"""
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


class CashAndCashEquivalentsIncludedInAssetsOfDisposalGroupsClassifiedAsForSaleCFIFRS(Enum):
    """"売却目的保有に分類される処分グループに係る資産に含まれる現金及び現金同等物、キャッシュ・フロー計算書（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class TransferToCapitalSurplusSSIFRS(Enum):
    """"資本剰余金への振替、持分変動計算書（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'CurrentYTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    CURRENT_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'CurrentYTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'Prior1YTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    PRIOR1_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'Prior1YTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    PRIOR1_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'Prior1YTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    PRIOR1_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'Prior1YTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """


class CollectionOfLoansReceivableFromAssociatesInvCFIFRS(Enum):
    """"関連会社に対する貸付金の回収、投資活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DecreaseIncreaseInFinanceReceivablesOpeCFIFRS(Enum):
    """"金融債権の減少(△増加)、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DecreaseIncreaseInOtherAssetsIFRSOpeCFIFRS(Enum):
    """"その他資産の減少(△増加)（IFRS）、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class FinancialReceivablesCAIFRS(Enum):
    """"金融債権、流動資産（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class FinancialReceivablesNCAIFRS(Enum):
    """"金融債権、非流動資産（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class IncreaseDecreaseInOtherLiabilitiesOpeCFIFRS(Enum):
    """"その他負債の増加(△減少)、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class InsuranceContractsLiabilitiesCLIFRS(Enum):
    """"保険契約負債、流動負債（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class LossGainOnDisposalOfFixedAssetsOpeCFIFRS(Enum):
    """"固定資産処分損益、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class NetDecreaseIncreaseInDepositsFromGroupFinancingWithinThreeMonthsFinCFIFRS(Enum):
    """"グループファイナンス預り金(３ヶ月以内)の純増減(△減少)、財務活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class NetDecreaseIncreaseInRestrictedCashInvCFIFRS(Enum):
    """"引出制限条項付預金の純増減(△増加)、投資活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PaymentsForAcquisitionOfShortTermInvestmentsInvCFIFRS(Enum):
    """"短期投資の取得、投資活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PaymentsForLoansReceivableFromAssociatesInvCFIFRS(Enum):
    """"関連会社に対する貸付、投資活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromDepositsFromGroupFinancingOverThreeMonthsFinCFIFRS(Enum):
    """"グループファイナンス預り金(３ヶ月超)の受入、財務活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromSalesAndRedemptionsOfShortTermInvestmentsInvCFIFRS(Enum):
    """"短期投資の売却及び償還、投資活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class RepaymentsOfDepositsFromGroupFinancingOverThreeMonthsFinCFIFRS(Enum):
    """"グループファイナンス預り金(３ヶ月超)の返還、財務活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DepreciationAndAmortizationIFRS(Enum):
    """"減価償却費及び償却費（IFRS）"""
    CURRENT_QUARTER_DURATION = 'CurrentQuarterDuration'
    CURRENT_QUARTER_DURATION__RECONCILING_ITEMS_MEMBER = 'CurrentQuarterDuration_ReconcilingItemsMember'
    """ 調整項目 """
    CURRENT_QUARTER_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'CurrentQuarterDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'CurrentYTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    CURRENT_YTD_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'CurrentYTDDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    PRIOR1_QUARTER_DURATION = 'Prior1QuarterDuration'
    PRIOR1_QUARTER_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1QuarterDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_QUARTER_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'Prior1QuarterDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1YTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_YTD_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'Prior1YTDDuration_ReportableSegmentsMember'
    """ 報告セグメント """


class IncreaseDecreaseInAssetsAndLiabilitiesOfOperatingActivitiesOpeCFIFRS(Enum):
    """"営業活動に係る資産・負債の増減合計、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossGainOnSaleOfSharesOfSubsidiariesIFRS(Enum):
    """"子会社株式売却損益（△は益）、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class OperatingEBITDAIFRS(Enum):
    """"事業EBITDA（IFRS）"""
    CURRENT_QUARTER_DURATION = 'CurrentQuarterDuration'
    CURRENT_QUARTER_DURATION__RECONCILING_ITEMS_MEMBER = 'CurrentQuarterDuration_ReconcilingItemsMember'
    """ 調整項目 """
    CURRENT_QUARTER_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'CurrentQuarterDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'CurrentYTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    CURRENT_YTD_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'CurrentYTDDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    PRIOR1_QUARTER_DURATION = 'Prior1QuarterDuration'
    PRIOR1_QUARTER_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1QuarterDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_QUARTER_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'Prior1QuarterDuration_ReportableSegmentsMember'
    """ 報告セグメント """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1YTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_YTD_DURATION__REPORTABLE_SEGMENTS_MEMBER = 'Prior1YTDDuration_ReportableSegmentsMember'
    """ 報告セグメント """


class PaymentsForAcquisitionOfShareAcquisitionRightsInSubsidiariesFromNonControllingInterestsFinCFIFRS(Enum):
    """"非支配持分からの子会社新株予約権の取得による支出、財務活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromExerciseOfShareAcquisitionRightsInSubsidiariesFinCFIFRS(Enum):
    """"子会社新株予約権の行使による収入、財務活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromGovernmentGrantsInvCFIFRS(Enum):
    """"政府補助金による収入、投資活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class Subtotal2OpeCFIFRS(Enum):
    """"小計-2、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class TotalAdjustmentsToReconcileProfitOpeCFIFRS(Enum):
    """"利益に対する調整項目合計、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class TransactionsWithNonControllingInterestsSSIFRS(Enum):
    """"非支配持分との取引等、持分変動計算書（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'CurrentYTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    CURRENT_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'CurrentYTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    CURRENT_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'CurrentYTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    CURRENT_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'CurrentYTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'Prior1YTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    PRIOR1_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'Prior1YTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    PRIOR1_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'Prior1YTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    PRIOR1_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'Prior1YTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """


class ChangesInOwnershipInterestIFRS(Enum):
    """"所有者持分の変動（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'CurrentYTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    CURRENT_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'CurrentYTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    CURRENT_YTD_DURATION__EXCHANGE_DIFFERENCES_ON_TRANSLATION_OF_FOREIGN_OPERATIONS_IFRS_MEMBER = 'CurrentYTDDuration_ExchangeDifferencesOnTranslationOfForeignOperationsIFRSMember'
    """ 在外営業活動体の外貨換算差額 """
    CURRENT_YTD_DURATION__NET_CHANGE_IN_FAIR_VALUE_OF_EQUITY_INSTRUMENTS_DESIGNATED_AS_MEASURED_AT_FAIR_VALUE_THROUGH_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'CurrentYTDDuration_NetChangeInFairValueOfEquityInstrumentsDesignatedAsMeasuredAtFairValueThroughOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益を通じて公正価値で測定するものとして指定した資本性金融商品の公正価値の純変動額 """
    CURRENT_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'CurrentYTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    CURRENT_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'CurrentYTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    CURRENT_YTD_DURATION__REMEASUREMENTS_OF_DEFINED_BENEFIT_PLANS_IFRS_MEMBER = 'CurrentYTDDuration_RemeasurementsOfDefinedBenefitPlansIFRSMember'
    """ 確定給付制度の再測定 """
    CURRENT_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'CurrentYTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    CURRENT_YTD_DURATION__SHARE_CAPITAL_IFRS_MEMBER = 'CurrentYTDDuration_ShareCapitalIFRSMember'
    """ 資本金 """
    CURRENT_YTD_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'CurrentYTDDuration_TreasurySharesIFRSMember'
    """ 自己株式 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'Prior1YTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    PRIOR1_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'Prior1YTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    PRIOR1_YTD_DURATION__EXCHANGE_DIFFERENCES_ON_TRANSLATION_OF_FOREIGN_OPERATIONS_IFRS_MEMBER = 'Prior1YTDDuration_ExchangeDifferencesOnTranslationOfForeignOperationsIFRSMember'
    """ 在外営業活動体の外貨換算差額 """
    PRIOR1_YTD_DURATION__NET_CHANGE_IN_FAIR_VALUE_OF_EQUITY_INSTRUMENTS_DESIGNATED_AS_MEASURED_AT_FAIR_VALUE_THROUGH_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'Prior1YTDDuration_NetChangeInFairValueOfEquityInstrumentsDesignatedAsMeasuredAtFairValueThroughOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益を通じて公正価値で測定するものとして指定した資本性金融商品の公正価値の純変動額 """
    PRIOR1_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'Prior1YTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    PRIOR1_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'Prior1YTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    PRIOR1_YTD_DURATION__REMEASUREMENTS_OF_DEFINED_BENEFIT_PLANS_IFRS_MEMBER = 'Prior1YTDDuration_RemeasurementsOfDefinedBenefitPlansIFRSMember'
    """ 確定給付制度の再測定 """
    PRIOR1_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'Prior1YTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    PRIOR1_YTD_DURATION__SHARE_CAPITAL_IFRS_MEMBER = 'Prior1YTDDuration_ShareCapitalIFRSMember'
    """ 資本金 """
    PRIOR1_YTD_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'Prior1YTDDuration_TreasurySharesIFRSMember'
    """ 自己株式 """


class DecreaseIncreaseInDepositPaidForRepurchaseOfTreasuryStockFinCFIFRS(Enum):
    """"自己株式取得のための預託金の増減額（△は増加）、財務活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DividendsPaidToNonControllingShareholdersFinCFIFRS(Enum):
    """"非支配株主への配当金の支払額、財務活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PaymentsForRetirementOfPropertyPlantAndEquipmentInvCFIFRS(Enum):
    """"有形固定資産の除却による支出、投資活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PurchaseOfSharesOfSubsidiariesAndAffiliatesInvCFIFRS(Enum):
    """"関係会社株式の取得による支出、投資活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PutOptionsWrittenOnNonControllingInterestsIFRS(Enum):
    """"非支配持分に付与されたプット・オプション（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'CurrentYTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    CURRENT_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'CurrentYTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    CURRENT_YTD_DURATION__EXCHANGE_DIFFERENCES_ON_TRANSLATION_OF_FOREIGN_OPERATIONS_IFRS_MEMBER = 'CurrentYTDDuration_ExchangeDifferencesOnTranslationOfForeignOperationsIFRSMember'
    """ 在外営業活動体の外貨換算差額 """
    CURRENT_YTD_DURATION__NET_CHANGE_IN_FAIR_VALUE_OF_EQUITY_INSTRUMENTS_DESIGNATED_AS_MEASURED_AT_FAIR_VALUE_THROUGH_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'CurrentYTDDuration_NetChangeInFairValueOfEquityInstrumentsDesignatedAsMeasuredAtFairValueThroughOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益を通じて公正価値で測定するものとして指定した資本性金融商品の公正価値の純変動額 """
    CURRENT_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'CurrentYTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    CURRENT_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'CurrentYTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    CURRENT_YTD_DURATION__REMEASUREMENTS_OF_DEFINED_BENEFIT_PLANS_IFRS_MEMBER = 'CurrentYTDDuration_RemeasurementsOfDefinedBenefitPlansIFRSMember'
    """ 確定給付制度の再測定 """
    CURRENT_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'CurrentYTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    CURRENT_YTD_DURATION__SHARE_CAPITAL_IFRS_MEMBER = 'CurrentYTDDuration_ShareCapitalIFRSMember'
    """ 資本金 """
    CURRENT_YTD_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'CurrentYTDDuration_TreasurySharesIFRSMember'
    """ 自己株式 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'Prior1YTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    PRIOR1_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'Prior1YTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    PRIOR1_YTD_DURATION__EXCHANGE_DIFFERENCES_ON_TRANSLATION_OF_FOREIGN_OPERATIONS_IFRS_MEMBER = 'Prior1YTDDuration_ExchangeDifferencesOnTranslationOfForeignOperationsIFRSMember'
    """ 在外営業活動体の外貨換算差額 """
    PRIOR1_YTD_DURATION__NET_CHANGE_IN_FAIR_VALUE_OF_EQUITY_INSTRUMENTS_DESIGNATED_AS_MEASURED_AT_FAIR_VALUE_THROUGH_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'Prior1YTDDuration_NetChangeInFairValueOfEquityInstrumentsDesignatedAsMeasuredAtFairValueThroughOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益を通じて公正価値で測定するものとして指定した資本性金融商品の公正価値の純変動額 """
    PRIOR1_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'Prior1YTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    PRIOR1_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'Prior1YTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    PRIOR1_YTD_DURATION__REMEASUREMENTS_OF_DEFINED_BENEFIT_PLANS_IFRS_MEMBER = 'Prior1YTDDuration_RemeasurementsOfDefinedBenefitPlansIFRSMember'
    """ 確定給付制度の再測定 """
    PRIOR1_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'Prior1YTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    PRIOR1_YTD_DURATION__SHARE_CAPITAL_IFRS_MEMBER = 'Prior1YTDDuration_ShareCapitalIFRSMember'
    """ 資本金 """
    PRIOR1_YTD_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'Prior1YTDDuration_TreasurySharesIFRSMember'
    """ 自己株式 """


class DecreaseIncreaseInOtherNonCurrentAssetsIFRSIFRS(Enum):
    """"その他の非流動資産の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS）（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class EquityTransactionsWithNonControllingInterestsSSIFRS(Enum):
    """"非支配持分との資本取引、持分変動計算書（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'CurrentYTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    CURRENT_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'CurrentYTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    CURRENT_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'CurrentYTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    CURRENT_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'CurrentYTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    CURRENT_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'CurrentYTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    CURRENT_YTD_DURATION__SHARE_CAPITAL_IFRS_MEMBER = 'CurrentYTDDuration_ShareCapitalIFRSMember'
    """ 資本金 """
    CURRENT_YTD_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'CurrentYTDDuration_TreasurySharesIFRSMember'
    """ 自己株式 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'Prior1YTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    PRIOR1_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'Prior1YTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    PRIOR1_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'Prior1YTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    PRIOR1_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'Prior1YTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    PRIOR1_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'Prior1YTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    PRIOR1_YTD_DURATION__SHARE_CAPITAL_IFRS_MEMBER = 'Prior1YTDDuration_ShareCapitalIFRSMember'
    """ 資本金 """
    PRIOR1_YTD_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'Prior1YTDDuration_TreasurySharesIFRSMember'
    """ 自己株式 """


class IncreaseDecreaseInOtherCurrentLiabilitiesOpeCFIFRS(Enum):
    """"その他の流動負債の増減額（△は減少）、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PaymentsOfLongTermLoansReceivableInvCFIFRS(Enum):
    """"長期貸付けによる支出、投資活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromSaleRedemptionOfFinancialAssetsInvCFIFRS(Enum):
    """"金融資産の売却及び償還による収入、投資活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PurchaseOfFinancialAssetsInvCFIFRS(Enum):
    """"金融資産の取得による支出、投資活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PurchaseOfSharesOfSubsidiariesAndAssociatesInvCFIFRS(Enum):
    """"関係会社株式の取得による支出、投資活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PurchaseOfSharesOfSubsidiariesNotResultingInChangeInScopeOfConsolidationFinCFIFRSIFRS(Enum):
    """"連結の範囲の変更を伴わない子会社株式の取得による支出、財務活動によるキャッシュ・フロー（IFRS）（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ATMOperationBusinessRevenuesIFRS(Enum):
    """"ATM運営事業売上高（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class CostOfATMOperationBusinessRevenuesIFRS(Enum):
    """"ATM運営事業売上原価（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class CostOfNetworkServicesRevenuesIFRS(Enum):
    """"ネットワークサービス売上原価（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class CostOfSIRevenuesIFRS(Enum):
    """"システムインテグレーション売上原価（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DecreaseIncreaseInOtherAssetsOpeCFIFRS(Enum):
    """"その他の資産の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DecreaseIncreaseInOtherFinancialAssetsOpeCFIFRS(Enum):
    """"その他の金融資産の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DecreaseIncreaseInPrepaidExpensesOpeCFIFRS(Enum):
    """"前払費用の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInDeferredIncomeOpeCFIFRS(Enum):
    """"繰延収益の増減額（△は減少）、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInOtherFinancialLiabilitiesOpeCFIFRS(Enum):
    """"その他の金融負債の増減額（△は減少）、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInOtherLiabilitiesOpeCFIFRS(Enum):
    """"その他の負債の増減額（△は減少）、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class InvestmentSecuritiesEquityNCAIFRS(Enum):
    """"投資有価証券（株式）、非流動資産（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class NetworkServicesRevenuesIFRS(Enum):
    """"ネットワークサービス売上高（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PaymentsForRefundableInsurancePoliciesInvCFIFRS(Enum):
    """"積立保険料の支払、投資活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PaymentsOfOtherFinancialLiabilitiesFinCFIFRS(Enum):
    """"その他の金融負債の支払、財務活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PrepaidExpensesCAIFRS(Enum):
    """"前払費用、流動資産（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class PrepaidExpensesNCAIFRS(Enum):
    """"前払費用、非流動資産（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ProceedsFromOtherFinancialLiabilitiesFinCFIFRS(Enum):
    """"その他の金融負債による収入、財務活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromSalesOfInvestmentSecuritiesEquityInvCFIFRS(Enum):
    """"投資有価証券（株式）の売却による収入、投資活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PurchasesOfInvestmentSecuritiesEquityInvCFIFRS(Enum):
    """"投資有価証券（株式）の取得による支出、投資活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class SIRevenuesIFRS(Enum):
    """"システムインテグレーション売上高（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class GroupHeadquartersManagementCostsAndOtherExpensesIFRS(Enum):
    """"親会社の本社管理費等（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInWorkingCapitalOpeCFIFRS(Enum):
    """"運転資本の増減額(△は増加)、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PaymentsOfTimeDepositsExceedingThreeMonthInvCFIFRS(Enum):
    """"3カ月超預金の預入による支出、投資活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PaymentsOnInvestmentsInJointVenturesInvCFIFRS(Enum):
    """"共同支配企業に対する投資による支出、投資活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromRedemptionOfTimeDepositsExceedingThreeMonthsInvCFIFRS(Enum):
    """"3カ月超預金の払戻による収入、投資活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromSaleAndRedemptionOfFinancialAssetsInvCFIFRS(Enum):
    """"金融資産の売却・償還による収入、投資活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PurchasesOfFinancialAssetsInvCFIFRS(Enum):
    """"金融資産の取得による支出、投資活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ResearchAndDevelopmentExpenditureRecognizedAsExpenseDuringPeriodSegmentInformationIFRS(Enum):
    """"当期に費用認識した研究開発費、セグメント情報（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInOtherCurrentLiabilitiesOpeCFIFRS(Enum):
    """"その他の流動負債の増減額（△は減少）、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInOtherNonCurrentLiabilitiesOpeCFIFRS(Enum):
    """"その他の非流動負債の増減額（△は減少）、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class NetIncreaseDecreaseInShortTermLoansBorrowingsWithinThreeMonthsFinCFIFRS(Enum):
    """"短期借入金（３ヶ月以内）の純増減額（△は減少）、財務活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class AmericasIFRS(Enum):
    """"米州、外部顧客への売上高 地域別区分への分解（IFRS）"""
    CURRENT_YTD_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'CurrentYTDDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    CURRENT_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'CurrentYTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    PRIOR1_YTD_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'Prior1YTDDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    PRIOR1_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1YTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """


class AsiaIFRS(Enum):
    """"アジア、外部顧客への売上高 地域別区分への分解（IFRS）"""
    CURRENT_YTD_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'CurrentYTDDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    CURRENT_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'CurrentYTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    PRIOR1_YTD_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'Prior1YTDDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    PRIOR1_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1YTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """


class AssetsHeldAtFairValueThroughOtherComprehensive2CAIFRS(Enum):
    """"その他の包括利益を通じて公正価値を測定する金融資産、流動資産（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class AssetsHeldAtFairValueThroughOtherComprehensiveIncomeIFRS(Enum):
    """"その他の包括利益を通じて公正価値を測定する金融資産（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class CapitalContributionForNonControllingInterestsIFRSIFRS(Enum):
    """"非支配持分株主との資本取引による支出、財務活動によるキャッシュ・フロー（IFRS）（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ChangesInOwnershipInterestsInSubsidiariesAndOthersSSIFRS(Enum):
    """"子会社等に対する所有持分の変動額、持分変動計算書（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'CurrentYTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    CURRENT_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'CurrentYTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    CURRENT_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'CurrentYTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """


class DividendsReceivedFromJointVenturesAndAssociatesInvCFIFRS(Enum):
    """"持分法適用会社からの配当金受領額、投資活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class EuropeIFRS(Enum):
    """"欧州、外部顧客への売上高 地域別区分への分解（IFRS）"""
    CURRENT_YTD_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'CurrentYTDDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    CURRENT_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'CurrentYTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    PRIOR1_YTD_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'Prior1YTDDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    PRIOR1_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1YTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """


class ExceptionalItemsGainsIFRS(Enum):
    """"個別開示項目収益（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'CurrentYTDDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    CURRENT_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'CurrentYTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'Prior1YTDDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    PRIOR1_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1YTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """


class ExceptionalItemsLossesIFRS(Enum):
    """"個別開示項目費用（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'CurrentYTDDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    CURRENT_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'CurrentYTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__OPERATING_SEGMENTS_NOT_INCLUDED_IN_REPORTABLE_SEGMENTS_AND_OTHER_REVENUE_GENERATING_BUSINESS_ACTIVITIES_MEMBER = 'Prior1YTDDuration_OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember'
    """ その他 """
    PRIOR1_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1YTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """


class HyperinflationAdjustmentCFIFRS(Enum):
    """"超インフレの調整、キャッシュ・フロー計算書（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class HyperinflationAdjustmentSSIFRS(Enum):
    """"超インフレの調整、持分変動計算書（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'CurrentYTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    CURRENT_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'CurrentYTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    CURRENT_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'CurrentYTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'Prior1YTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    PRIOR1_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'Prior1YTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    PRIOR1_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'Prior1YTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """


class OperatingProfitAfterExceptionalItemsIFRS(Enum):
    """"個別開示項目後営業利益（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'CurrentYTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1YTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """


class OtherGainsLossesOnEquityMethodInvestmentsIFRS(Enum):
    """"持分法投資に関するその他の利益（△は損失）（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'CurrentYTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1YTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """


class ProceedsFromBorrowingsFinCFIFRS(Enum):
    """"社債発行及び借入れによる収入、財務活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsOnDisposalOfAssetsHeldAtFairValueThroughOtherComprehensiveIncomeInvCFIFRS(Enum):
    """"その他の包括利益を通じて公正価値を測定する金融資産の売却による収入、投資活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsOnDisposalOfJointVenturesAndAssociatesIFRS(Enum):
    """"ジョイント・ベンチャー及び関連会社の売却による収入、投資活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PurchaseOfAssetsHeldAtFairValueThroughOtherComprehensiveIncomeInvCFIFRS(Enum):
    """"その他の包括利益を通じて公正価値を測定する金融資産の取得による支出、投資活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class RepaymentOfBorrowingsFinCFIFRS(Enum):
    """"社債償還及び借入金返済による支出、財務活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class RetainedEarningsTranslationAdjustmentAtTheIFRSTransitionDateEquityIFRS(Enum):
    """"利益剰余金（IFRS移行時の累積換算差額）、資本（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ReversalOfPreviousImpairmentOfFinancialReceivablesOwedByJointVenturesAndAssociatesIFRS(Enum):
    """"持分法適用会社に対する金融債権の減損損失の戻入益（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'CurrentYTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1YTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """


class StockOptionsSSIFRS(Enum):
    """"新株予約権の増減、持分変動計算書（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'CurrentYTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    CURRENT_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'CurrentYTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    CURRENT_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'CurrentYTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    CURRENT_YTD_DURATION__SHARE_CAPITAL_IFRS_MEMBER = 'CurrentYTDDuration_ShareCapitalIFRSMember'
    """ 資本金 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'Prior1YTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    PRIOR1_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'Prior1YTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    PRIOR1_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'Prior1YTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    PRIOR1_YTD_DURATION__SHARE_CAPITAL_IFRS_MEMBER = 'Prior1YTDDuration_ShareCapitalIFRSMember'
    """ 資本金 """


class TradeAndOtherReceivablesIFRS(Enum):
    """"売上債権及びその他の債権、非流動資産（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ProceedsFromGovernmentGrantsFinCFIFRS(Enum):
    """"政府補助金による収入、財務活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromSalesOrRedemptionOfInvestmentsInDebtInstrumentsIFRS(Enum):
    """"負債性金融商品の売却又は償還による収入、投資活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PurchaseOfInvestmentsInDebtInstrumentsIFRS(Enum):
    """"負債性金融商品の取得による支出、投資活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class BondsBorrowingsAndLeaseLiabilitiesCLIFRS(Enum):
    """"社債、借入金及びリース負債、流動負債（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class BondsBorrowingsAndLeaseLiabilitiesNCLIFRS(Enum):
    """"社債、借入金及びリース負債、非流動負債（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class DecreaseIncreaseInOtherAssetsOpeCFIFRS(Enum):
    """"その他資産の減少(△増加)、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class FreeCashFlowCFIFRS(Enum):
    """"フリー・キャッシュ・フロー、キャッシュ・フロー計算書（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInOtherLiabilitiesOpeCFIFRS(Enum):
    """"その他負債の増加(△減少)、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossGainFromSalesAndDisposalOfPropertyPlantAndEquipmentNetOpeCFIFRS(Enum):
    """"固定資産の売廃却損益、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class TransactionsWithNonControllingInterestsAndOthersSSIFRS(Enum):
    """"非支配持分との取引等、持分変動計算書（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'CurrentYTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    CURRENT_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'CurrentYTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    CURRENT_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'CurrentYTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'Prior1YTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    PRIOR1_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'Prior1YTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    PRIOR1_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'Prior1YTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """


class TransactionsWithNonControllingInterestsFinCFIFRS(Enum):
    """"非支配持分との取引、財務活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class AccountsPayableAndAccruedExpensesCLIFRS(Enum):
    """"未払金及び未払費用、流動負債（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class DecreaseIncreaseInTradeReceivablesAndContractAssetsOpeCFIFRS(Enum):
    """"営業債権及び契約資産の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ExchangeDifferencesOnTranslationOfForeignOperationsSSIFRS(Enum):
    """"在外営業活動体の換算差額、持分変動計算書（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'CurrentYTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    CURRENT_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'CurrentYTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    CURRENT_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'CurrentYTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    CURRENT_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'CurrentYTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    CURRENT_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'CurrentYTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    CURRENT_YTD_DURATION__SHARE_CAPITAL_IFRS_MEMBER = 'CurrentYTDDuration_ShareCapitalIFRSMember'
    """ 資本金 """
    CURRENT_YTD_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'CurrentYTDDuration_TreasurySharesIFRSMember'
    """ 自己株式 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'Prior1YTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    PRIOR1_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'Prior1YTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    PRIOR1_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'Prior1YTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    PRIOR1_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'Prior1YTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    PRIOR1_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'Prior1YTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    PRIOR1_YTD_DURATION__SHARE_CAPITAL_IFRS_MEMBER = 'Prior1YTDDuration_ShareCapitalIFRSMember'
    """ 資本金 """
    PRIOR1_YTD_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'Prior1YTDDuration_TreasurySharesIFRSMember'
    """ 自己株式 """


class FinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncomeSSIFRS(Enum):
    """"その他の包括利益を通じて公正価値で測定する金融資産、持分変動計算書（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'CurrentYTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    CURRENT_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'CurrentYTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    CURRENT_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'CurrentYTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    CURRENT_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'CurrentYTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    CURRENT_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'CurrentYTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    CURRENT_YTD_DURATION__SHARE_CAPITAL_IFRS_MEMBER = 'CurrentYTDDuration_ShareCapitalIFRSMember'
    """ 資本金 """
    CURRENT_YTD_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'CurrentYTDDuration_TreasurySharesIFRSMember'
    """ 自己株式 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'Prior1YTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    PRIOR1_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'Prior1YTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    PRIOR1_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'Prior1YTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    PRIOR1_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'Prior1YTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    PRIOR1_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'Prior1YTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    PRIOR1_YTD_DURATION__SHARE_CAPITAL_IFRS_MEMBER = 'Prior1YTDDuration_ShareCapitalIFRSMember'
    """ 資本金 """
    PRIOR1_YTD_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'Prior1YTDDuration_TreasurySharesIFRSMember'
    """ 自己株式 """


class IncreaseDecreaseInLongTermDebtFinCFIFRS(Enum):
    """"長期債務の増減額（△は減少）、財務活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInShortTermDebtFinCFIFRS(Enum):
    """"短期債務の増減額（△は減少）、財務活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class NetChangesInCashFlowHedgesSSIFRS(Enum):
    """"キャッシュ・フロー・ヘッジの公正価値の純変動、持分変動計算書（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'CurrentYTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    CURRENT_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'CurrentYTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    CURRENT_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'CurrentYTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    CURRENT_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'CurrentYTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    CURRENT_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'CurrentYTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    CURRENT_YTD_DURATION__SHARE_CAPITAL_IFRS_MEMBER = 'CurrentYTDDuration_ShareCapitalIFRSMember'
    """ 資本金 """
    CURRENT_YTD_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'CurrentYTDDuration_TreasurySharesIFRSMember'
    """ 自己株式 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'Prior1YTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    PRIOR1_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'Prior1YTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    PRIOR1_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'Prior1YTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    PRIOR1_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'Prior1YTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    PRIOR1_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'Prior1YTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    PRIOR1_YTD_DURATION__SHARE_CAPITAL_IFRS_MEMBER = 'Prior1YTDDuration_ShareCapitalIFRSMember'
    """ 資本金 """
    PRIOR1_YTD_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'Prior1YTDDuration_TreasurySharesIFRSMember'
    """ 自己株式 """


class ProceedsFromSaleAndRedemptionOfInvestmentsAccountedForUsingTheEquityMethodAndOtherFinancialAssetsInvCFIFRS(Enum):
    """"持分法投資及びその他の金融資産の売却及び償還、投資活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PurchaseOfInvestmentsAccountedForUsingTheEquityMethodAndOtherFinancialAssetsInvCFIFRS(Enum):
    """"持分法投資及びその他の金融資産の取得、投資活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class RemeasurementsOfDefinedBenefitPlansSSIFRS(Enum):
    """"確定給付制度の再測定、持分変動計算書（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'CurrentYTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    CURRENT_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'CurrentYTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    CURRENT_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'CurrentYTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    CURRENT_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'CurrentYTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    CURRENT_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'CurrentYTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    CURRENT_YTD_DURATION__SHARE_CAPITAL_IFRS_MEMBER = 'CurrentYTDDuration_ShareCapitalIFRSMember'
    """ 資本金 """
    CURRENT_YTD_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'CurrentYTDDuration_TreasurySharesIFRSMember'
    """ 自己株式 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'Prior1YTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    PRIOR1_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'Prior1YTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    PRIOR1_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'Prior1YTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    PRIOR1_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'Prior1YTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    PRIOR1_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'Prior1YTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    PRIOR1_YTD_DURATION__SHARE_CAPITAL_IFRS_MEMBER = 'Prior1YTDDuration_ShareCapitalIFRSMember'
    """ 資本金 """
    PRIOR1_YTD_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'Prior1YTDDuration_TreasurySharesIFRSMember'
    """ 自己株式 """


class ShortTermDebtIncludingCurrentPortionOfLongTermDebtCLIFRS(Enum):
    """"短期負債及び一年以内返済長期負債、流動負債（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class TradeReceivablesAndContractAssetsCAIFRS(Enum):
    """"営業債権及び契約資産、流動資産（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class TransactionsWithNonControllingInterestsAndOtherSSIFRS(Enum):
    """"非支配持分との取引等、持分変動計算書（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'CurrentYTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    CURRENT_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'CurrentYTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    CURRENT_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'CurrentYTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    CURRENT_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'CurrentYTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    CURRENT_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'CurrentYTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    CURRENT_YTD_DURATION__SHARE_CAPITAL_IFRS_MEMBER = 'CurrentYTDDuration_ShareCapitalIFRSMember'
    """ 資本金 """
    CURRENT_YTD_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'CurrentYTDDuration_TreasurySharesIFRSMember'
    """ 自己株式 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'Prior1YTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    PRIOR1_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'Prior1YTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    PRIOR1_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'Prior1YTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    PRIOR1_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'Prior1YTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    PRIOR1_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'Prior1YTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    PRIOR1_YTD_DURATION__SHARE_CAPITAL_IFRS_MEMBER = 'Prior1YTDDuration_ShareCapitalIFRSMember'
    """ 資本金 """
    PRIOR1_YTD_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'Prior1YTDDuration_TreasurySharesIFRSMember'
    """ 自己株式 """


class ContentAssetsNCAIFRS(Enum):
    """"コンテンツ資産、非流動資産（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class CostsAndExpensesCostsAndExpensesIFRS(Enum):
    """"売上原価、販売費・一般管理費及びその他の一般費用、売上原価、販売費・一般管理費及びその他の一般費用（IFRS）"""
    CURRENT_QUARTER_DURATION = 'CurrentQuarterDuration'
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_QUARTER_DURATION = 'Prior1QuarterDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class CurrentPortionOfLongTermDebtCLIFRS(Enum):
    """"１年以内に返済期限の到来する長期借入債務、流動負債（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class DepositsFromCustomersInTheBankingBusinessCLIFRS(Enum):
    """"銀行ビジネスにおける顧客預金、流動負債（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ExerciseOfShareAcquisitionRightsAndOtherSSIFRS(Enum):
    """"新株予約権の行使等、持分変動計算書（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'CurrentYTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    CURRENT_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'CurrentYTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    CURRENT_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'CurrentYTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    CURRENT_YTD_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'CurrentYTDDuration_TreasurySharesIFRSMember'
    """ 自己株式 """


class FinancialServicesExpensesCostsAndExpensesIFRS(Enum):
    """"金融ビジネス費用、売上原価、販売費・一般管理費及びその他の一般費用（IFRS）"""
    CURRENT_QUARTER_DURATION = 'CurrentQuarterDuration'
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_QUARTER_DURATION = 'Prior1QuarterDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class FinancialServicesRevenueSalesAndOperatingRevenueIFRS(Enum):
    """"金融ビジネス収入、売上高及び金融ビジネス収入（IFRS）"""
    CURRENT_QUARTER_DURATION = 'CurrentQuarterDuration'
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_QUARTER_DURATION = 'Prior1QuarterDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class GainLossOnSecuritiesNetOtherThanFinancialServicesSegmentOpeCFIFRS(Enum):
    """"有価証券に関する損（益）（純額）（金融分野以外）、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInBorrowingsInTheLifeInsuranceBusinessAndTheBankingBusinessOpeCFIFRS(Enum):
    """"生命保険ビジネス及び銀行ビジネスにおける借入債務の増加・減少（△）、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInContentAssetsOpeCFIFRS(Enum):
    """"コンテンツ資産の増加（△）・減少、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInDepositsFromCustomersInTheBankingBusinessOpeCFIFRS(Enum):
    """"銀行ビジネスにおける顧客預金の増加・減少（△）、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInInsuranceContractLiabilitiesNetOfInsuranceContractAssetsOpeCFIFRS(Enum):
    """"保険契約負債（保険契約資産との純額）の増加・減少（△）、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInInvestmentsAndAdvancesInTheFinancialServicesBusinessOpeCFIFRS(Enum):
    """"金融分野における投資及び貸付の増加（△）・減少、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInOtherFinancialAssetsAndOtherCurrentAssetsOpeCFIFRS(Enum):
    """"その他の金融資産及びその他の資産（流動）の増加（△）・減少、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInOtherFinancialLiabilitiesAndOtherCurrentLiabilitiesOpeCFIFRS(Enum):
    """"その他の金融負債及びその他の負債（流動）の増加・減少（△）、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInTaxesPayableOtherThanIncomeTaxesNetOpeCFIFRS(Enum):
    """"法人所得税以外の未払税金（純額）の増加・減少（△）、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInTradeReceivablesAndContractAssetsOpeCFIFRS(Enum):
    """"営業債権及び契約資産の増加（△）・減少、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class InsuranceContractLiabilitiesNCLIFRS(Enum):
    """"保険契約負債（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class InsuranceFinanceExpensesIncomeFinancialServicesExpensesIFRS(Enum):
    """"保険金融費用（収益）、金融ビジネス費用（IFRS）"""
    CURRENT_QUARTER_DURATION = 'CurrentQuarterDuration'
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_QUARTER_DURATION = 'Prior1QuarterDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class InsuranceFinanceIncomeExpensesNetOfTaxItemsThatMayBeReclassifiedToProfitOrLossOCIIFRS(Enum):
    """"保険金融収益（費用）（税引後）、純損益に振り替えられる可能性のあるその他の包括利益（IFRS）"""
    CURRENT_QUARTER_DURATION = 'CurrentQuarterDuration'
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_QUARTER_DURATION = 'Prior1QuarterDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class InsuranceIncomeFinancialServicesRevenueIFRS(Enum):
    """"保険収益、金融ビジネス収入（IFRS）"""
    CURRENT_QUARTER_DURATION = 'CurrentQuarterDuration'
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_QUARTER_DURATION = 'Prior1QuarterDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class InsuranceServiceCostsFinancialServicesExpensesIFRS(Enum):
    """"保険サービス費用、金融ビジネス費用（IFRS）"""
    CURRENT_QUARTER_DURATION = 'CurrentQuarterDuration'
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_QUARTER_DURATION = 'Prior1QuarterDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IntersegmentSalesAndFinancialServicesRevenueIFRS(Enum):
    """"セグメント間の売上高及び金融ビジネス収入（IFRS）"""
    CURRENT_QUARTER_DURATION__OTHER_REPORTABLE_SEGMENTS_MEMBER = 'CurrentQuarterDuration_OtherReportableSegmentsMember'
    """ その他 """
    CURRENT_YTD_DURATION__OTHER_REPORTABLE_SEGMENTS_MEMBER = 'CurrentYTDDuration_OtherReportableSegmentsMember'
    """ その他 """
    PRIOR1_QUARTER_DURATION__OTHER_REPORTABLE_SEGMENTS_MEMBER = 'Prior1QuarterDuration_OtherReportableSegmentsMember'
    """ その他 """
    PRIOR1_YTD_DURATION__OTHER_REPORTABLE_SEGMENTS_MEMBER = 'Prior1YTDDuration_OtherReportableSegmentsMember'
    """ その他 """


class InvestmentsAndAdvancesInTheFinancialServicesSegmentCAIFRS(Enum):
    """"金融分野における投資及び貸付、流動資産（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class InvestmentsAndAdvancesInTheFinancialServicesSegmentNCAIFRS(Enum):
    """"金融分野における投資及び貸付、非流動資産（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class LongTermDebt2NCLIFRS(Enum):
    """"長期借入債務、非流動負債（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class OtherFinancialServicesExpenseFinancialServicesExpensesIFRS(Enum):
    """"その他の保険ビジネス費用、金融ビジネス費用（IFRS）"""
    CURRENT_QUARTER_DURATION = 'CurrentQuarterDuration'
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_QUARTER_DURATION = 'Prior1QuarterDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class OtherFinancialServicesRevenueFinancialServicesRevenueIFRS(Enum):
    """"その他の金融ビジネス収入、金融ビジネス収入（IFRS）"""
    CURRENT_QUARTER_DURATION = 'CurrentQuarterDuration'
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_QUARTER_DURATION = 'Prior1QuarterDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class OtherNetOfTaxItemsThatMayBeReclassifiedToProfitOrLossOCIIFRS(Enum):
    """"その他（税引後）、純損益に振り替えられる可能性のあるその他の包括利益（IFRS）"""
    CURRENT_QUARTER_DURATION = 'CurrentQuarterDuration'
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_QUARTER_DURATION = 'Prior1QuarterDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class OtherOperatingIncomeExpenseNetCostsAndExpensesIFRS(Enum):
    """"その他の営業損（益）（純額）、売上原価、販売費・一般管理費及びその他の一般費用（IFRS）"""
    CURRENT_QUARTER_DURATION = 'CurrentQuarterDuration'
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_QUARTER_DURATION = 'Prior1QuarterDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class OtherOperatingIncomeExpenseNetOpeCFIFRS(Enum):
    """"その他の営業損（益）（純額）、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ParticipationLiabilitiesInThePicturesSegmentCLIFRS(Enum):
    """"映画分野における未払分配金債務、流動負債（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ParticipationLiabilitiesInThePicturesSegmentNCLIFRS(Enum):
    """"映画分野における未払分配金債務、非流動負債（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class PaymentsForInvestmentsAndAdvancesOtherThanFinancialServicesBusinessInvCFIFRS(Enum):
    """"投資及び貸付（金融分野以外）、投資活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PaymentsOfLongTermDebtFinCFIFRS(Enum):
    """"長期借入債務の返済、財務活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromIssuanceOfLongTermDebtFinCFIFRS(Enum):
    """"長期借入債務による調達、財務活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromSalesOrReturnOfInvestmentsAndCollectionsOfAdvancesOtherThanFinancialServicesBusinessInvCFIFRS(Enum):
    """"投資の売却又は償還及び貸付の回収（金融分野以外）、投資活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class SalesAndFinancialServicesRevenueIFRS(Enum):
    """"売上高及び金融ビジネス収入（IFRS）"""
    CURRENT_QUARTER_DURATION = 'CurrentQuarterDuration'
    CURRENT_QUARTER_DURATION__OTHER_REPORTABLE_SEGMENTS_MEMBER = 'CurrentQuarterDuration_OtherReportableSegmentsMember'
    """ その他 """
    CURRENT_QUARTER_DURATION__RECONCILING_ITEMS_MEMBER = 'CurrentQuarterDuration_ReconcilingItemsMember'
    """ 調整項目 """
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__OTHER_REPORTABLE_SEGMENTS_MEMBER = 'CurrentYTDDuration_OtherReportableSegmentsMember'
    """ その他 """
    CURRENT_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'CurrentYTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_QUARTER_DURATION = 'Prior1QuarterDuration'
    PRIOR1_QUARTER_DURATION__OTHER_REPORTABLE_SEGMENTS_MEMBER = 'Prior1QuarterDuration_OtherReportableSegmentsMember'
    """ その他 """
    PRIOR1_QUARTER_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1QuarterDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__OTHER_REPORTABLE_SEGMENTS_MEMBER = 'Prior1YTDDuration_OtherReportableSegmentsMember'
    """ その他 """
    PRIOR1_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1YTDDuration_ReconcilingItemsMember'
    """ 調整項目 """


class SalesAndFinancialServicesRevenueToCustomersIFRS(Enum):
    """"外部顧客への売上高及び金融ビジネス収入（IFRS）"""
    CURRENT_QUARTER_DURATION__OTHER_REPORTABLE_SEGMENTS_MEMBER = 'CurrentQuarterDuration_OtherReportableSegmentsMember'
    """ その他 """
    CURRENT_YTD_DURATION__OTHER_REPORTABLE_SEGMENTS_MEMBER = 'CurrentYTDDuration_OtherReportableSegmentsMember'
    """ その他 """
    PRIOR1_QUARTER_DURATION__OTHER_REPORTABLE_SEGMENTS_MEMBER = 'Prior1QuarterDuration_OtherReportableSegmentsMember'
    """ その他 """
    PRIOR1_YTD_DURATION__OTHER_REPORTABLE_SEGMENTS_MEMBER = 'Prior1YTDDuration_OtherReportableSegmentsMember'
    """ その他 """


class ShareOfProfitLossOfInvestmentsAccountedForUsingTheEquityMethodNetOfDividendsOpeCFIFRS(Enum):
    """"持分法による投資（利益）損失（純額）（受取配当金相殺後）、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class TradeReceivablesOtherReceivablesAndContractAssetsCAIFRS(Enum):
    """"営業債権、その他の債権及び契約資産、流動資産（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class TransactionsWithNoncontrollingInterestsShareholdersAndOtherSSIFRS(Enum):
    """"非支配持分株主との取引及びその他、持分変動計算書（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'CurrentYTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    CURRENT_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'CurrentYTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    CURRENT_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'CurrentYTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'Prior1YTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    PRIOR1_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'Prior1YTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    PRIOR1_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'Prior1YTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """


class DecreaseIncreaseInDerivativeLiabilitiesOpeCFIFRS(Enum):
    """"デリバティブ負債の増減額（△は減少）、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DeferredGovernmentGrantsNCLIFRS(Enum):
    """"政府補助金繰延収益、非流動負債（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ExchangeDifferencesOnTranslationOfForeignOperationsIFRS(Enum):
    """"在外営業活動体の換算差額（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'CurrentYTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    CURRENT_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'CurrentYTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    CURRENT_YTD_DURATION__EXCHANGE_DIFFERENCES_ON_TRANSLATION_OF_FOREIGN_OPERATIONS_IFRS_MEMBER = 'CurrentYTDDuration_ExchangeDifferencesOnTranslationOfForeignOperationsIFRSMember'
    """ 在外営業活動体の外貨換算差額 """
    CURRENT_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'CurrentYTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'Prior1YTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    PRIOR1_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'Prior1YTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    PRIOR1_YTD_DURATION__EXCHANGE_DIFFERENCES_ON_TRANSLATION_OF_FOREIGN_OPERATIONS_IFRS_MEMBER = 'Prior1YTDDuration_ExchangeDifferencesOnTranslationOfForeignOperationsIFRSMember'
    """ 在外営業活動体の外貨換算差額 """
    PRIOR1_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'Prior1YTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """


class GovernmentGrantsOpeCFIFRS(Enum):
    """"政府補助金、営業活動によるキャッシュフロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInAccruedExpensesOpeCFIFRS(Enum):
    """"未払費用の増減額（△は減少）、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInConsumptionTaxValueAddedTaxReceivablesOpeCFIFRS(Enum):
    """"未収消費税等の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInDerivativeAssetsOpeCFIFRS(Enum):
    """"デリバティブ資産の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class NetChangeInFinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncomeIFRS(Enum):
    """"その他の包括利益を通じて公正価値で測定する金融資産の純変動（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'CurrentYTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    CURRENT_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'CurrentYTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    CURRENT_YTD_DURATION__FINANCIAL_ASSETS_MEASURED_AT_FAIR_VALUE_THROUGH_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'CurrentYTDDuration_FinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益を通じて公正価値で測定する金融資産 """
    CURRENT_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'CurrentYTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'Prior1YTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    PRIOR1_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'Prior1YTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    PRIOR1_YTD_DURATION__FINANCIAL_ASSETS_MEASURED_AT_FAIR_VALUE_THROUGH_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'Prior1YTDDuration_FinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益を通じて公正価値で測定する金融資産 """
    PRIOR1_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'Prior1YTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """


class RemeasurementsOfDefinedBenefitPlansSSIFRS(Enum):
    """"確定給付制度の再測定、持分変動計算書（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'CurrentYTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    CURRENT_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'CurrentYTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    CURRENT_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'CurrentYTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    CURRENT_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'CurrentYTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """


class ShareOfOtherComprehensiveIncomeOfEntitiesAccountedForUsingEquityMethodIFRS(Enum):
    """"持分法によるその他の包括利益に対する持分相当額（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'CurrentYTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    CURRENT_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'CurrentYTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    CURRENT_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'CurrentYTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'Prior1YTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    PRIOR1_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'Prior1YTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    PRIOR1_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'Prior1YTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """


class ShareOfOtherComprehensiveIncomeOfEntitiesAccountedForUsingEquityMethodItemsThatMayBeReclassifiedToProfitOrLossIFRS(Enum):
    """"持分法によるその他の包括利益に対する持分相当額、純損益に振り替えられる可能性のある項目（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInLongTermAccountsPayableOpeCFIFRS(Enum):
    """"長期未払金の増減額（△は減少）、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LongTermAccountsPayableNCLIFRS(Enum):
    """"長期未払金、非流動負債（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class RetainedEarningsCumulativeTranslationDifferenceAtTransitionToIFRSIFRS(Enum):
    """"利益剰余金（IFRS移行時の累積換算差額）、資本（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class BondsBorrowingsAndOtherFinancialLiabilitiesCLIFRS(Enum):
    """"社債、借入金及びその他の金融負債、流動負債（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class BondsBorrowingsAndOtherFinancialLiabilitiesNCLIFRS(Enum):
    """"社債、借入金及びその他の金融負債、非流動負債（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class BusinessProfitLossIFRS(Enum):
    """"事業利益（△は損失）（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__OTHER_REPORTABLE_SEGMENTS_MEMBER = 'CurrentYTDDuration_OtherReportableSegmentsMember'
    """ その他 """
    CURRENT_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'CurrentYTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    CURRENT_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'CurrentYTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__OTHER_REPORTABLE_SEGMENTS_MEMBER = 'Prior1YTDDuration_OtherReportableSegmentsMember'
    """ その他 """
    PRIOR1_YTD_DURATION__RECONCILING_ITEMS_MEMBER = 'Prior1YTDDuration_ReconcilingItemsMember'
    """ 調整項目 """
    PRIOR1_YTD_DURATION__TOTAL_OF_REPORTABLE_SEGMENTS_AND_OTHERS_MEMBER = 'Prior1YTDDuration_TotalOfReportableSegmentsAndOthersMember'
    """ 事業セグメント合計 """


class CapitalIncreaseOfConsolidatedSubsidiariesSSIFRS(Enum):
    """"連結子会社の増資による持分の増減、持分変動計算書（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'CurrentYTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    CURRENT_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'CurrentYTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'Prior1YTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """


class ChangeInOwnershipInterestOfParentDueToTransactionsWithNonControllingInterestsSSIFRS(Enum):
    """"非支配株主との取引に係る親会社の持分変動、持分変動計算書（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'CurrentYTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'Prior1YTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    PRIOR1_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'Prior1YTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    PRIOR1_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'Prior1YTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """


class DecreaseIncreaseInAvdancePaymentOpeCFIFRS(Enum):
    """"前渡金の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInOtherCurrentAssetsOpeCFIFRS(Enum):
    """"その他流動資産の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInOtherCurrentLiabilitiesOpeCFIFRS(Enum):
    """"その他流動負債の増減額（△は減少）、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInRefundLiabilityOpeCFIFRS(Enum):
    """"返金負債の増減額（△は減少）、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PaymentsForAcquisitionOfSubsidiariesNotResultingInChangeInScopeOfConsolidationFinCFIFRS(Enum):
    """"連結範囲の変更を伴わない子会社株式の取得による支出、財務活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PaymentsForEquityMethodInvestmentAndPurchaseOfOtherFinancialAssetsInvCFIFRS(Enum):
    """"持分法投資及びその他の金融資産の取得による支出、投資活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromEquityMethodInvestmentAndSaleOfOtherFinancialAssetsInvCFIFRS(Enum):
    """"持分法投資及びその他の金融資産の売却による収入、投資活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromFactoringAgreementsFinCFIFRS(Enum):
    """"債権流動化による収入、財務活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class RefundLiabilitiesCLIFRS(Enum):
    """"返金負債、流動負債（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class RepaymentOfLiabilitiesUnderFactoringAgreementsFinCFIFRS(Enum):
    """"債権流動化の返済による支出、財務活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class TransferToNonFinancialAssetsSSIFRS(Enum):
    """"非金融資産への振替、持分変動計算書（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__EFFECTIVE_PORTION_OF_CASH_FLOW_HEDGES_IFRS_MEMBER = 'CurrentYTDDuration_EffectivePortionOfCashFlowHedgesIFRSMember'
    """ キャッシュ・フロー・ヘッジの有効部分 """
    CURRENT_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'CurrentYTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    CURRENT_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'CurrentYTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__EFFECTIVE_PORTION_OF_CASH_FLOW_HEDGES_IFRS_MEMBER = 'Prior1YTDDuration_EffectivePortionOfCashFlowHedgesIFRSMember'
    """ キャッシュ・フロー・ヘッジの有効部分 """
    PRIOR1_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'Prior1YTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    PRIOR1_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'Prior1YTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """


class IncreaseDecreaseInEquityDueToAcquisitionOfSharesInConsolidatedSubsidiariesIFRS(Enum):
    """"連結子会社株式の取得による持分の増減（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'CurrentYTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    CURRENT_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'CurrentYTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    CURRENT_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'CurrentYTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'Prior1YTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """


class IncreaseDecreaseInLiabilitiesRelatedToProvisionsAndEmployeeBenefitsOpeCFIFRS(Enum):
    """"引当金及び従業員給付に係る負債の増減額（△は減少）、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PaymentsFromChangesInOwnershipInterestsInSubsidiariesThatDoNotResultInChangeInScopeOfConsolidationFinCFIFRS(Enum):
    """"連結範囲の変更を伴わない子会社株式の取得による支出、財務活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromSaleOrRecoveryOfOtherFinancialAssetsInvCFIFRS(Enum):
    """"その他の金融資産の売却または回収による収入、投資活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PurchaseOfIntangibleAssetsAndExpenditureOnInternallyGeneratedIntangibleAssetsInvCFIFRS(Enum):
    """"無形資産の取得及び内部開発にかかわる支出、投資活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DecreaseIncreaseInDepositsForPurchaseOfTreasurySharesFinCFIFRS(Enum):
    """"自己株式取得のための預託金の増減額（△は増加）、財務活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossGainOnDisposalOfNonCurrentAssetsOpeCFIFRS(Enum):
    """"固定資産処分損益（△は益）、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class NetDecreaseIncreaseInLeasedReceivablesOpeCFIFRS(Enum):
    """"リース債権の増減額(△は増加)、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class BusinessProfitLossIFRS(Enum):
    """"事業利益又は事業損失（△）（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ExpenseByAcquisitionOfRepurchasedStockOfConsolidatedSubsidiaryFinCFIFRS(Enum):
    """"連結子会社の自己株式の取得による支出、財務活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class TraChangesInOwnershipInterestInSubsidiariesSSIFRS(Enum):
    """"非支配株主との取引に係る親会社の持分変動、持分変動計算書（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'CurrentYTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    CURRENT_YTD_DURATION__EFFECTIVE_PORTION_OF_CASH_FLOW_HEDGES_IFRS_MEMBER = 'CurrentYTDDuration_EffectivePortionOfCashFlowHedgesIFRSMember'
    """ キャッシュ・フロー・ヘッジの有効部分 """
    CURRENT_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'CurrentYTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    CURRENT_YTD_DURATION__EXCHANGE_DIFFERENCES_ON_TRANSLATION_OF_FOREIGN_OPERATIONS_IFRS_MEMBER = 'CurrentYTDDuration_ExchangeDifferencesOnTranslationOfForeignOperationsIFRSMember'
    """ 在外営業活動体の外貨換算差額 """
    CURRENT_YTD_DURATION__FINANCIAL_ASSETS_MEASURED_AT_FAIR_VALUE_THROUGH_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'CurrentYTDDuration_FinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益を通じて公正価値で測定する金融資産 """
    CURRENT_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'CurrentYTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    CURRENT_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'CurrentYTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    CURRENT_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'CurrentYTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    CURRENT_YTD_DURATION__SHARE_CAPITAL_IFRS_MEMBER = 'CurrentYTDDuration_ShareCapitalIFRSMember'
    """ 資本金 """
    CURRENT_YTD_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'CurrentYTDDuration_TreasurySharesIFRSMember'
    """ 自己株式 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'Prior1YTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    PRIOR1_YTD_DURATION__EFFECTIVE_PORTION_OF_CASH_FLOW_HEDGES_IFRS_MEMBER = 'Prior1YTDDuration_EffectivePortionOfCashFlowHedgesIFRSMember'
    """ キャッシュ・フロー・ヘッジの有効部分 """
    PRIOR1_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'Prior1YTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    PRIOR1_YTD_DURATION__EXCHANGE_DIFFERENCES_ON_TRANSLATION_OF_FOREIGN_OPERATIONS_IFRS_MEMBER = 'Prior1YTDDuration_ExchangeDifferencesOnTranslationOfForeignOperationsIFRSMember'
    """ 在外営業活動体の外貨換算差額 """
    PRIOR1_YTD_DURATION__FINANCIAL_ASSETS_MEASURED_AT_FAIR_VALUE_THROUGH_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'Prior1YTDDuration_FinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益を通じて公正価値で測定する金融資産 """
    PRIOR1_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'Prior1YTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    PRIOR1_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'Prior1YTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    PRIOR1_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'Prior1YTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    PRIOR1_YTD_DURATION__SHARE_CAPITAL_IFRS_MEMBER = 'Prior1YTDDuration_ShareCapitalIFRSMember'
    """ 資本金 """
    PRIOR1_YTD_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'Prior1YTDDuration_TreasurySharesIFRSMember'
    """ 自己株式 """


class ClawBackFromCancellationOfStockAcquisitionAgreementsInvCFIFRS(Enum):
    """"株式取得契約の解除に伴う回収額、投資活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DecreaseIncreaseInDepositForPurchaseOfTreasurySharesFinCFIFRS(Enum):
    """"自己株式取得のための預託金の増減額、財務活動によるキャッシュ・フロー（△は増加）（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class GainOnTransferOfSSDOpeCFIFRS(Enum):
    """"科学事業の譲渡益、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PaymentsForContingentConsiderationInvCFIFRS(Enum):
    """"条件付対価の決済による支出、投資活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromSaleOfSSDBusinessseInvCFIFRS(Enum):
    """"科学事業の譲渡による収入、投資活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromTransferOfCollagenBusinessAndDentalProductSalesBusinessesInvCFIFRS(Enum):
    """"コラーゲン事業及び歯科用商品販売事業の譲渡による収入、投資活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class TransferFromRetainedEarningsToCapitalSurplusSSIFRS(Enum):
    """"利益剰余金から資本剰余金への振替額、持分変動計算書（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'CurrentYTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    CURRENT_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'CurrentYTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    CURRENT_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'CurrentYTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'Prior1YTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    PRIOR1_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'Prior1YTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    PRIOR1_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'Prior1YTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """


class CapitalTransactionWithNonControllingInterestsIFRS(Enum):
    """"非支配株主との資本取引（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'CurrentYTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    CURRENT_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'CurrentYTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    CURRENT_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'CurrentYTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'Prior1YTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    PRIOR1_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'Prior1YTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """


class IncreaseInLeaseReceivablesOpeCFIFRS(Enum):
    """"リース債権の増加、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class NetChangeInTreasuryStockSSIFRS(Enum):
    """"自己株式の取得及び売却、持分変動計算書（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'CurrentYTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    CURRENT_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'CurrentYTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    CURRENT_YTD_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'CurrentYTDDuration_TreasurySharesIFRSMember'
    """ 自己株式 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'Prior1YTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    PRIOR1_YTD_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'Prior1YTDDuration_TreasurySharesIFRSMember'
    """ 自己株式 """


class OtherIncomeOpeCFIFRS(Enum):
    """"その他の収益、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromSalesOfBusinessInvCFIFRS(Enum):
    """"事業の売却 （売却時の現金及び現金同等物保有額控除後）、投資活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PurchasesOfBusinessNetOfCashAcquiredInvCFIFRS(Enum):
    """"事業の買収（取得時の現金及び現金同等物受入額控除後）、投資活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class TransferToCapitalSurplusFromRetainedEarningsIFRS(Enum):
    """"利益剰余金から資本剰余金への振替（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'CurrentYTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    CURRENT_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'CurrentYTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    CURRENT_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'CurrentYTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """


class AssetsRelatedToSecuritiesBusinessIFRS(Enum):
    """"証券業関連資産、資産（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class CustomerDepositsForBankingBusinessIFRS(Enum):
    """"顧客預金、負債（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class DecreaseInBondAndBorrowingBankingOpeCFIFRS(Enum):
    """"社債及び借入金（銀行業）の増減、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DecreaseInPayablesUnderSecuritiesLendingTransactionsOpeCFIFRS(Enum):
    """"債券貸借取引受入担保金の増減、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DecreaseIncreaseInAssetsLiabilitiesRelatedToSecuritiesBusinessIFRS(Enum):
    """"証券業関連資産及び負債の増減、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DecreaseIncreaseInCustomerDepositsForBankingBusinessIFRS(Enum):
    """"顧客預金の増減、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DecreaseIncreaseInOperationalInvestmentSecuritiesIFRS(Enum):
    """"営業投資有価証券の増減、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DistributionsToNonControllingInterestsInConsolidatedInvestmentFundsFinCFIFRS(Enum):
    """"投資事業組合等における非支配持分への分配金支払額、財務活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ExpenseIFRS(Enum):
    """"費用（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class FinancialCostAssociatedWithFinancialIncomeIFRS(Enum):
    """"金融収益に係る金融費用、費用（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class FinancialInstrumentsPledgedAsCollateralAssetsIFRS(Enum):
    """"担保差入金融商品、資産（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class FluctuationsInDiscountRatesOfInsuranceContractsItemsThatMayBeReclassifiedToProfitOrLossOCIIFRS(Enum):
    """"保険契約の割引率変動差額（税引後）、純損益に振り替えられる可能性のあるその他の包括利益（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class GainOnBargainPurchaseOpeCFIFRS(Enum):
    """"負ののれん発生益、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class InsuranceContractLiabilitiesIFRS(Enum):
    """"保険契約負債、負債（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class InsuranceServiceExpensesIFRS(Enum):
    """"保険サービス費用（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class InventoriesAssetsIFRS(Enum):
    """"棚卸資産、資産（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class IssuanceOfConvertibleBondsSSIFRS(Enum):
    """"転換社債型新株予約権付社債の発行、持分変動計算書（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'CurrentYTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    CURRENT_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'CurrentYTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    CURRENT_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'CurrentYTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    CURRENT_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'CurrentYTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    CURRENT_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'CurrentYTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    CURRENT_YTD_DURATION__SHARE_CAPITAL_IFRS_MEMBER = 'CurrentYTDDuration_ShareCapitalIFRSMember'
    """ 資本金 """
    CURRENT_YTD_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'CurrentYTDDuration_TreasurySharesIFRSMember'
    """ 自己株式 """


class LiabilitiesRelatedToSecuritiesBusinessIFRS(Enum):
    """"証券業関連負債、負債（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class NetFairValueGainsLossesNetOfTaxAttributableToCreditRiskRelatedToFinancialLiabilitiesDesignatedAsAtFairValueThroughProfitOrLossOCIIFRS(Enum):
    """"負債の信用リスクの変動額（税引後）、純損益に振り替えられることのないその他の包括利益（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class OfInsuranceRevenueIFRS(Enum):
    """"（内、保険収益）（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class OfInterestIncomeRevenueIFRS(Enum):
    """"（内、受取利息）（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class OperationalInvestmentSecuritiesIFRS(Enum):
    """"営業投資有価証券、資産（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class OtherFinancialCostIFRS(Enum):
    """"その他の金融費用、費用（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class OtherInvestmentSecuritiesIFRS(Enum):
    """"その他の投資有価証券、資産（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ProceedsFromStockIssuanceToNonControllingInterestsIFRS(Enum):
    """"投資事業組合等における非支配持分からの出資受入による収入、財務活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProvisionForCreditLossesIFRS(Enum):
    """"信用損失引当金繰入（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ReinsuranceContractsAssetsIFRS(Enum):
    """"再保険契約資産、資産（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class ChangesFromLossOfControlSSIFRS(Enum):
    """"支配喪失による変動、持分変動計算書（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__ACCUMULATED_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'CurrentYTDDuration_AccumulatedOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益累計額 """
    CURRENT_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'CurrentYTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    CURRENT_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'CurrentYTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    CURRENT_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'CurrentYTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    CURRENT_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'CurrentYTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    CURRENT_YTD_DURATION__SHARE_CAPITAL_IFRS_MEMBER = 'CurrentYTDDuration_ShareCapitalIFRSMember'
    """ 資本金 """
    CURRENT_YTD_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'CurrentYTDDuration_TreasurySharesIFRSMember'
    """ 自己株式 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__ACCUMULATED_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'Prior1YTDDuration_AccumulatedOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益累計額 """
    PRIOR1_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'Prior1YTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    PRIOR1_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'Prior1YTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    PRIOR1_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'Prior1YTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    PRIOR1_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'Prior1YTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    PRIOR1_YTD_DURATION__SHARE_CAPITAL_IFRS_MEMBER = 'Prior1YTDDuration_ShareCapitalIFRSMember'
    """ 資本金 """
    PRIOR1_YTD_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'Prior1YTDDuration_TreasurySharesIFRSMember'
    """ 自己株式 """


class ChangesInTheFairValueOfDebtInvestmentsAtFVTOCIItemsThatMayBeReclassifiedToProfitOrLossIFRS(Enum):
    """"FVTOCIの負債性金融資産の公正価値の変動、純損益に振り替えられる可能性のある項目（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ChangesInTheFairValueOfEquityInvestmentsAtFVTOCINetOfTaxItemsThatWillNotBeReclassifiedToProfitOrLossOCIIFRS(Enum):
    """"FVTOCIの資本性金融資産の公正価値の変動（税引後）、純損益に振り替えられることのないその他の包括利益（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ContractCostsNCAIFRS(Enum):
    """"契約コスト、非流動資産（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class DecreaseInConsumptionTaxesPayableOpeCFIFRS(Enum):
    """"未払消費税等の増減額（△は減少額）、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class DepositsForBankingBusinessCLIFRS(Enum):
    """"銀行事業の預金、流動負債（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class GainOrLossOnChangeInEquityIFRS(Enum):
    """"持分変動損益（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class GainOrLossOnSaleOfEquityMethodInvestmentIFRS(Enum):
    """"持分法による投資の売却損益（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class GainOrLossOnSalesOfEquityMethodInvestmentsOpeCFIFRS(Enum):
    """"持分法による投資の売却損益（△は益）、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class GainRelatingToLossOfControlOverSubsidiariesOpeCFIFRS(Enum):
    """"子会社の支配喪失に伴う利益、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInCustomerDepositsInBankingBusinessOpeCFIFRS(Enum):
    """"銀行事業の預金の増減額（△は減少額）、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class IncreaseDecreaseInLoansInBankingBusinessOpeCFIFRS(Enum):
    """"銀行事業の貸付金の増減額(△は増加額)、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class InvestmentSecuritiesForBankingBusinessNCAIFRS(Enum):
    """"銀行事業の有価証券、非流動資産（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


class LossGainOnChangeInEquityOpeCFIFRS(Enum):
    """"持分変動損益（△は益）、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class NetIncreaseDecreaseInCashAndCashEquivalentsResultingFromTransferToAssetsAsHeldForSaleIFRS(Enum):
    """"売却目的保有に分類された資産への振替に伴う現金及び現金同等物の増減額(△は減少額)（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class NetIncreaseDecreaseInShortTermInterestBearingLiabilitiesFinCFIFRS(Enum):
    """"短期有利子負債の純増減額（△は減少額）、財務活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromInterstBearingDebtFinCFIFRS(Enum):
    """"有利子負債の収入、財務活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromLossOfControlOfSubsidiariesInvCFIFRS(Enum):
    """"子会社の支配喪失による収支（△は支出）、投資活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromObtainingControlOfSubsidiariesInvCFIFRS(Enum):
    """"子会社の支配獲得による収支（△は支出）、投資活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromSalesOfInvestmentSecuritiesInBankingBusinessInvCFIFRS(Enum):
    """"銀行事業の有価証券の売却または償還による収入、投資活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PurchaseOfInvestmentSecuritiesInBankingBusinessInvCFIFRS(Enum):
    """"銀行事業の有価証券の取得による支出、投資活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class PurchasesOfMobileDevicesLeasedToEnterpriseCustomersOpeCFIFRS(Enum):
    """"法人向けレンタル用携帯端末の取得による支出、営業活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class RepaymentOfInterestBearingDebtFinCFIFRS(Enum):
    """"有利子負債の支出、財務活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class TransferFromRetainedEarningsToCapitalSurplusIFRS(Enum):
    """"利益剰余金から資本剰余金への振替（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__ACCUMULATED_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'CurrentYTDDuration_AccumulatedOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益累計額 """
    CURRENT_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'CurrentYTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    CURRENT_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'CurrentYTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    CURRENT_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'CurrentYTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    CURRENT_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'CurrentYTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    CURRENT_YTD_DURATION__SHARE_CAPITAL_IFRS_MEMBER = 'CurrentYTDDuration_ShareCapitalIFRSMember'
    """ 資本金 """
    CURRENT_YTD_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'CurrentYTDDuration_TreasurySharesIFRSMember'
    """ 自己株式 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__ACCUMULATED_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'Prior1YTDDuration_AccumulatedOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益累計額 """
    PRIOR1_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'Prior1YTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    PRIOR1_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'Prior1YTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    PRIOR1_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'Prior1YTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    PRIOR1_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'Prior1YTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    PRIOR1_YTD_DURATION__SHARE_CAPITAL_IFRS_MEMBER = 'Prior1YTDDuration_ShareCapitalIFRSMember'
    """ 資本金 """
    PRIOR1_YTD_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'Prior1YTDDuration_TreasurySharesIFRSMember'
    """ 自己株式 """


class DecreaseIncreaseInConsumptionTaxesRefundReceivableOpeCFIFRS(Enum):
    """"未収消費税等の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS）（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class NetIncreaseDecreaseInShortTermBorrowingsWithin3MonthsFinCFIFRS(Enum):
    """"短期借入金（３ヶ月以内）の純増減額、財務活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ProceedsFromShortTermBorrowingsOverThreeMonthsFinCFIFRS(Enum):
    """"短期借入れ（３ヶ月超）による収入、財務活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class ReductionInSubsidiariesWithoutSaleOfEquityInterestInvCFIFRS(Enum):
    """"持分の売却を伴わない子会社の減少、投資活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class RepaymentsOfShortTermBorrowingsOverThreeMonthsFinCFIFRS(Enum):
    """"短期借入金（３ヶ月超）の返済による支出、財務活動によるキャッシュ・フロー（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class TransferToNonFinancialAssetsEtcIFRSSSIFRS(Enum):
    """"非金融資産等への振替、持分変動計算書（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    CURRENT_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'CurrentYTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    CURRENT_YTD_DURATION__EFFECTIVE_PORTION_OF_CASH_FLOW_HEDGES_IFRS_MEMBER = 'CurrentYTDDuration_EffectivePortionOfCashFlowHedgesIFRSMember'
    """ キャッシュ・フロー・ヘッジの有効部分 """
    CURRENT_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'CurrentYTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    CURRENT_YTD_DURATION__EXCHANGE_DIFFERENCES_ON_TRANSLATION_OF_FOREIGN_OPERATIONS_IFRS_MEMBER = 'CurrentYTDDuration_ExchangeDifferencesOnTranslationOfForeignOperationsIFRSMember'
    """ 在外営業活動体の外貨換算差額 """
    CURRENT_YTD_DURATION__FINANCIAL_ASSETS_MEASURED_AT_FAIR_VALUE_THROUGH_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'CurrentYTDDuration_FinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益を通じて公正価値で測定する金融資産 """
    CURRENT_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'CurrentYTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    CURRENT_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'CurrentYTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    CURRENT_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'CurrentYTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    CURRENT_YTD_DURATION__SHARE_CAPITAL_IFRS_MEMBER = 'CurrentYTDDuration_ShareCapitalIFRSMember'
    """ 資本金 """
    CURRENT_YTD_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'CurrentYTDDuration_TreasurySharesIFRSMember'
    """ 自己株式 """
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'
    PRIOR1_YTD_DURATION__CAPITAL_SURPLUS_IFRS_MEMBER = 'Prior1YTDDuration_CapitalSurplusIFRSMember'
    """ 資本剰余金 """
    PRIOR1_YTD_DURATION__EFFECTIVE_PORTION_OF_CASH_FLOW_HEDGES_IFRS_MEMBER = 'Prior1YTDDuration_EffectivePortionOfCashFlowHedgesIFRSMember'
    """ キャッシュ・フロー・ヘッジの有効部分 """
    PRIOR1_YTD_DURATION__EQUITY_ATTRIBUTABLE_TO_OWNERS_OF_PARENT_IFRS_MEMBER = 'Prior1YTDDuration_EquityAttributableToOwnersOfParentIFRSMember'
    """ 親会社の所有者に帰属する持分 """
    PRIOR1_YTD_DURATION__EXCHANGE_DIFFERENCES_ON_TRANSLATION_OF_FOREIGN_OPERATIONS_IFRS_MEMBER = 'Prior1YTDDuration_ExchangeDifferencesOnTranslationOfForeignOperationsIFRSMember'
    """ 在外営業活動体の外貨換算差額 """
    PRIOR1_YTD_DURATION__FINANCIAL_ASSETS_MEASURED_AT_FAIR_VALUE_THROUGH_OTHER_COMPREHENSIVE_INCOME_IFRS_MEMBER = 'Prior1YTDDuration_FinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncomeIFRSMember'
    """ その他の包括利益を通じて公正価値で測定する金融資産 """
    PRIOR1_YTD_DURATION__NON_CONTROLLING_INTERESTS_IFRS_MEMBER = 'Prior1YTDDuration_NonControllingInterestsIFRSMember'
    """ 非支配持分 """
    PRIOR1_YTD_DURATION__OTHER_COMPONENTS_OF_EQUITY_IFRS_MEMBER = 'Prior1YTDDuration_OtherComponentsOfEquityIFRSMember'
    """ その他の資本の構成要素 """
    PRIOR1_YTD_DURATION__RETAINED_EARNINGS_IFRS_MEMBER = 'Prior1YTDDuration_RetainedEarningsIFRSMember'
    """ 利益剰余金 """
    PRIOR1_YTD_DURATION__SHARE_CAPITAL_IFRS_MEMBER = 'Prior1YTDDuration_ShareCapitalIFRSMember'
    """ 資本金 """
    PRIOR1_YTD_DURATION__TREASURY_SHARES_IFRS_MEMBER = 'Prior1YTDDuration_TreasurySharesIFRSMember'
    """ 自己株式 """


class GainOnLossOfControlOfSubsidiariesIFRS(Enum):
    """"子会社の支配喪失に伴う利益（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class LossOnChangeInEquityIFRS(Enum):
    """"持分変動損失（IFRS）"""
    CURRENT_YTD_DURATION = 'CurrentYTDDuration'
    PRIOR1_YTD_DURATION = 'Prior1YTDDuration'


class NonCurrentLiabilityForStockBenefitIFRS(Enum):
    """"株式報酬に係る負債、非流動負債（IFRS）"""
    CURRENT_QUARTER_INSTANT = 'CurrentQuarterInstant'
    PRIOR1_YEAR_INSTANT = 'Prior1YearInstant'


