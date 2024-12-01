import app.schema.ix_summary_non_fraction as sc


def get_schema_class(key: str):
    if key == "edif_CondensedQuarterlyConsolidatedStatementOfCashFlowsIFRS_consolidated_Q2":
        return sc.edif_CondensedQuarterlyConsolidatedStatementOfCashFlowsIFRS_consolidated_Q2
    if key == "edif_CondensedQuarterlyConsolidatedStatementOfCashFlowsIFRS_consolidated_Q3":
        return sc.edif_CondensedQuarterlyConsolidatedStatementOfCashFlowsIFRS_consolidated_Q3
    if key == "edif_CondensedQuarterlyConsolidatedStatementOfChangesInEquityIFRS_consolidated_Q2":
        return sc.edif_CondensedQuarterlyConsolidatedStatementOfChangesInEquityIFRS_consolidated_Q2
    if key == "edif_CondensedQuarterlyConsolidatedStatementOfChangesInEquityIFRS_consolidated_Q3":
        return sc.edif_CondensedQuarterlyConsolidatedStatementOfChangesInEquityIFRS_consolidated_Q3
    if key == "edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q2":
        return sc.edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q2
    if key == "edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q3":
        return sc.edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q3
    if key == "edif_CondensedQuarterPeriodConsolidatedStatementOfComprehensiveIncomeIFRS_consolidated_Q3":
        return sc.edif_CondensedQuarterPeriodConsolidatedStatementOfComprehensiveIncomeIFRS_consolidated_Q3
    if key == "edif_CondensedQuarterPeriodConsolidatedStatementOfProfitOrLossIFRS_consolidated_Q3":
        return sc.edif_CondensedQuarterPeriodConsolidatedStatementOfProfitOrLossIFRS_consolidated_Q3
    if key == "edif_CondensedYearToQuarterEndConsolidatedStatementOfComprehensiveIncomeIFRS_consolidated_Q2":
        return sc.edif_CondensedYearToQuarterEndConsolidatedStatementOfComprehensiveIncomeIFRS_consolidated_Q2
    if key == "edif_CondensedYearToQuarterEndConsolidatedStatementOfComprehensiveIncomeIFRS_consolidated_Q3":
        return sc.edif_CondensedYearToQuarterEndConsolidatedStatementOfComprehensiveIncomeIFRS_consolidated_Q3
    if key == "edif_CondensedYearToQuarterEndConsolidatedStatementOfComprehensiveIncomeSingleStatementIFRS_consolidated_Q2":
        return sc.edif_CondensedYearToQuarterEndConsolidatedStatementOfComprehensiveIncomeSingleStatementIFRS_consolidated_Q2
    if key == "edif_CondensedYearToQuarterEndConsolidatedStatementOfProfitOrLossIFRS_consolidated_Q2":
        return sc.edif_CondensedYearToQuarterEndConsolidatedStatementOfProfitOrLossIFRS_consolidated_Q2
    if key == "edif_CondensedYearToQuarterEndConsolidatedStatementOfProfitOrLossIFRS_consolidated_Q3":
        return sc.edif_CondensedYearToQuarterEndConsolidatedStatementOfProfitOrLossIFRS_consolidated_Q3
    if key == "edif_FinancialReportSummary_consolidated_Q2":
        return sc.edif_FinancialReportSummary_consolidated_Q2
    if key == "edif_FinancialReportSummary_consolidated_Q3":
        return sc.edif_FinancialReportSummary_consolidated_Q3
    if key == "edif_NotesSegmentInformationCondensedQuarterlyConsolidatedFinancialStatementsIFRS_consolidated_Q2":
        return sc.edif_NotesSegmentInformationCondensedQuarterlyConsolidatedFinancialStatementsIFRS_consolidated_Q2
    if key == "edif_NotesSegmentInformationCondensedQuarterlyConsolidatedFinancialStatementsIFRS_consolidated_Q3":
        return sc.edif_NotesSegmentInformationCondensedQuarterlyConsolidatedFinancialStatementsIFRS_consolidated_Q3
    if key == "edjp_BalanceSheet_Nonconsolidated_FY":
        return sc.edjp_BalanceSheet_Nonconsolidated_FY
    if key == "edjp_BalanceSheet_consolidated_FY":
        return sc.edjp_BalanceSheet_consolidated_FY
    if key == "edjp_ConsolidatedBalanceSheet_consolidated_FY":
        return sc.edjp_ConsolidatedBalanceSheet_consolidated_FY
    if key == "edjp_ConsolidatedStatementOfCashFlows_consolidated_FY":
        return sc.edjp_ConsolidatedStatementOfCashFlows_consolidated_FY
    if key == "edjp_ConsolidatedStatementOfChangesInEquity_consolidated_FY":
        return sc.edjp_ConsolidatedStatementOfChangesInEquity_consolidated_FY
    if key == "edjp_ConsolidatedStatementOfComprehensiveIncome_consolidated_FY":
        return sc.edjp_ConsolidatedStatementOfComprehensiveIncome_consolidated_FY
    if key == "edjp_ConsolidatedStatementOfIncome_consolidated_FY":
        return sc.edjp_ConsolidatedStatementOfIncome_consolidated_FY
    if key == "edjp_FinancialReportSummary_Nonconsolidated_FY":
        return sc.edjp_FinancialReportSummary_Nonconsolidated_FY
    if key == "edjp_FinancialReportSummary_consolidated_FY":
        return sc.edjp_FinancialReportSummary_consolidated_FY
    if key == "edjp_FinancialReportSummary_Nonconsolidated_Q1":
        return sc.edjp_FinancialReportSummary_Nonconsolidated_Q1
    if key == "edjp_FinancialReportSummary_consolidated_Q1":
        return sc.edjp_FinancialReportSummary_consolidated_Q1
    if key == "edjp_FinancialReportSummary_Nonconsolidated_Q2":
        return sc.edjp_FinancialReportSummary_Nonconsolidated_Q2
    if key == "edjp_FinancialReportSummary_consolidated_Q2":
        return sc.edjp_FinancialReportSummary_consolidated_Q2
    if key == "edjp_FinancialReportSummary_consolidated_Q3":
        return sc.edjp_FinancialReportSummary_consolidated_Q3
    if key == "edjp_FinancialReportSummary":
        return sc.edjp_FinancialReportSummary
    if key == "edjp_NotesSegmentInformationEtcConsolidatedFinancialStatements_consolidated_FY":
        return sc.edjp_NotesSegmentInformationEtcConsolidatedFinancialStatements_consolidated_FY
    if key == "edjp_NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatements_consolidated_Q1":
        return sc.edjp_NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatements_consolidated_Q1
    if key == "edjp_NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatements_consolidated_Q2":
        return sc.edjp_NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatements_consolidated_Q2
    if key == "edjp_NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatements_consolidated_Q3":
        return sc.edjp_NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatements_consolidated_Q3
    if key == "edjp_NotesSegmentInformationEtcQuarterlyFinancialStatements_Nonconsolidated_Q2":
        return sc.edjp_NotesSegmentInformationEtcQuarterlyFinancialStatements_Nonconsolidated_Q2
    if key == "edjp_QuarterlyBalanceSheet_Nonconsolidated_Q1":
        return sc.edjp_QuarterlyBalanceSheet_Nonconsolidated_Q1
    if key == "edjp_QuarterlyBalanceSheet_Nonconsolidated_Q2":
        return sc.edjp_QuarterlyBalanceSheet_Nonconsolidated_Q2
    if key == "edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q1":
        return sc.edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q1
    if key == "edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q2":
        return sc.edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q2
    if key == "edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q3":
        return sc.edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q3
    if key == "edjp_QuarterlyConsolidatedStatementOfCashFlows_consolidated_Q2":
        return sc.edjp_QuarterlyConsolidatedStatementOfCashFlows_consolidated_Q2
    if key == "edjp_QuarterlyConsolidatedStatementOfCashFlows_consolidated_Q3":
        return sc.edjp_QuarterlyConsolidatedStatementOfCashFlows_consolidated_Q3
    if key == "edjp_QuarterlyStatementOfCashFlows_Nonconsolidated_Q2":
        return sc.edjp_QuarterlyStatementOfCashFlows_Nonconsolidated_Q2
    if key == "edjp_StatementOfCashFlows_Nonconsolidated_FY":
        return sc.edjp_StatementOfCashFlows_Nonconsolidated_FY
    if key == "edjp_StatementOfChangesInEquity_Nonconsolidated_FY":
        return sc.edjp_StatementOfChangesInEquity_Nonconsolidated_FY
    if key == "edjp_StatementOfChangesInEquity_consolidated_FY":
        return sc.edjp_StatementOfChangesInEquity_consolidated_FY
    if key == "edjp_StatementOfIncome_consolidated_FY":
        return sc.edjp_StatementOfIncome_consolidated_FY
    if key == "edjp_StatementOfIncome_Nonconsolidated_FY":
        return sc.edjp_StatementOfIncome_Nonconsolidated_FY
    if key == "edjp_YearToQuarterEndConsolidatedStatementOfComprehensiveIncome_consolidated_Q1":
        return sc.edjp_YearToQuarterEndConsolidatedStatementOfComprehensiveIncome_consolidated_Q1
    if key == "edjp_YearToQuarterEndConsolidatedStatementOfComprehensiveIncome_consolidated_Q2":
        return sc.edjp_YearToQuarterEndConsolidatedStatementOfComprehensiveIncome_consolidated_Q2
    if key == "edjp_YearToQuarterEndConsolidatedStatementOfComprehensiveIncome_consolidated_Q3":
        return sc.edjp_YearToQuarterEndConsolidatedStatementOfComprehensiveIncome_consolidated_Q3
    if key == "edjp_YearToQuarterEndConsolidatedStatementOfComprehensiveIncomeSingleStatement_consolidated_Q2":
        return sc.edjp_YearToQuarterEndConsolidatedStatementOfComprehensiveIncomeSingleStatement_consolidated_Q2
    if key == "edjp_YearToQuarterEndConsolidatedStatementOfIncome_consolidated_Q1":
        return sc.edjp_YearToQuarterEndConsolidatedStatementOfIncome_consolidated_Q1
    if key == "edjp_YearToQuarterEndConsolidatedStatementOfIncome_consolidated_Q2":
        return sc.edjp_YearToQuarterEndConsolidatedStatementOfIncome_consolidated_Q2
    if key == "edjp_YearToQuarterEndConsolidatedStatementOfIncome_consolidated_Q3":
        return sc.edjp_YearToQuarterEndConsolidatedStatementOfIncome_consolidated_Q3
    if key == "edjp_YearToQuarterEndStatementOfIncome_Nonconsolidated_Q1":
        return sc.edjp_YearToQuarterEndStatementOfIncome_Nonconsolidated_Q1
    if key == "edjp_YearToQuarterEndStatementOfIncome_Nonconsolidated_Q2":
        return sc.edjp_YearToQuarterEndStatementOfIncome_Nonconsolidated_Q2
    if key == "edjp_FinancialReportSummary_consolidated_HY_specific_business":
        return sc.edjp_FinancialReportSummary_consolidated_HY_specific_business
    if key == "edjp_NotesSegmentInformationEtcSemiAnnualConsolidatedFinancialStatements_consolidated_HY_specific_business":
        return sc.edjp_NotesSegmentInformationEtcSemiAnnualConsolidatedFinancialStatements_consolidated_HY_specific_business
    if key == "edjp_SemiAnnualBalanceSheet_consolidated_HY_specific_business":
        return sc.edjp_SemiAnnualBalanceSheet_consolidated_HY_specific_business
    if key == "edjp_SemiAnnualConsolidatedBalanceSheet_consolidated_HY_specific_business":
        return sc.edjp_SemiAnnualConsolidatedBalanceSheet_consolidated_HY_specific_business
    if key == "edjp_SemiAnnualConsolidatedStatementOfChangesInEquity_consolidated_HY_specific_business":
        return sc.edjp_SemiAnnualConsolidatedStatementOfChangesInEquity_consolidated_HY_specific_business
    if key == "edjp_SemiAnnualConsolidatedStatementOfComprehensiveIncome_consolidated_HY_specific_business":
        return sc.edjp_SemiAnnualConsolidatedStatementOfComprehensiveIncome_consolidated_HY_specific_business
    if key == "edjp_SemiAnnualConsolidatedStatementOfIncome_consolidated_HY_specific_business":
        return sc.edjp_SemiAnnualConsolidatedStatementOfIncome_consolidated_HY_specific_business
    if key == "edjp_SemiAnnualStatementOfChangesInEquity_consolidated_HY_specific_business":
        return sc.edjp_SemiAnnualStatementOfChangesInEquity_consolidated_HY_specific_business
    if key == "edjp_SemiAnnualStatementOfIncome_consolidated_HY_specific_business":
        return sc.edjp_SemiAnnualStatementOfIncome_consolidated_HY_specific_business
    if key == "rvfc_FinancialReportSummary":
        return sc.rvfc_FinancialReportSummary
    if key == "rvfc_FinancialReportSummary_specific_business":
        return sc.rvfc_FinancialReportSummary_specific_business


