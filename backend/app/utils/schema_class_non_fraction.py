import app.schema.ix_summary_non_fraction as sc


def get_schema_class(key: str):
    if key == "edif_CondensedQuarterlyConsolidatedStatementOfCashFlowsIFRS_Con_Q2":
        return sc.edif_CondensedQuarterlyConsolidatedStatementOfCashFlowsIFRS_Con_Q2
    if key == "edif_CondensedQuarterlyConsolidatedStatementOfCashFlowsIFRS_Con_Q3":
        return sc.edif_CondensedQuarterlyConsolidatedStatementOfCashFlowsIFRS_Con_Q3
    if key == "edif_CondensedQuarterlyConsolidatedStatementOfChangesInEquityIFRS_Con_Q2":
        return sc.edif_CondensedQuarterlyConsolidatedStatementOfChangesInEquityIFRS_Con_Q2
    if key == "edif_CondensedQuarterlyConsolidatedStatementOfChangesInEquityIFRS_Con_Q3":
        return sc.edif_CondensedQuarterlyConsolidatedStatementOfChangesInEquityIFRS_Con_Q3
    if key == "edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_Con_Q2":
        return sc.edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_Con_Q2
    if key == "edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_Con_Q3":
        return sc.edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_Con_Q3
    if key == "edif_CondensedQuarterPeriodConsolidatedStatementOfComprehensiveIncomeIFRS_Con_Q3":
        return sc.edif_CondensedQuarterPeriodConsolidatedStatementOfComprehensiveIncomeIFRS_Con_Q3
    if key == "edif_CondensedQuarterPeriodConsolidatedStatementOfProfitOrLossIFRS_Con_Q3":
        return sc.edif_CondensedQuarterPeriodConsolidatedStatementOfProfitOrLossIFRS_Con_Q3
    if key == "edif_CondensedYearToQuarterEndConsolidatedStatementOfComprehensiveIncomeIFRS_Con_Q2":
        return sc.edif_CondensedYearToQuarterEndConsolidatedStatementOfComprehensiveIncomeIFRS_Con_Q2
    if key == "edif_CondensedYearToQuarterEndConsolidatedStatementOfComprehensiveIncomeIFRS_Con_Q3":
        return sc.edif_CondensedYearToQuarterEndConsolidatedStatementOfComprehensiveIncomeIFRS_Con_Q3
    if key == "edif_CondensedYearToQuarterEndConsolidatedStatementOfComprehensiveIncomeSingleStatementIFRS_Con_Q2":
        return sc.edif_CondensedYearToQuarterEndConsolidatedStatementOfComprehensiveIncomeSingleStatementIFRS_Con_Q2
    if key == "edif_CondensedYearToQuarterEndConsolidatedStatementOfProfitOrLossIFRS_Con_Q2":
        return sc.edif_CondensedYearToQuarterEndConsolidatedStatementOfProfitOrLossIFRS_Con_Q2
    if key == "edif_CondensedYearToQuarterEndConsolidatedStatementOfProfitOrLossIFRS_Con_Q3":
        return sc.edif_CondensedYearToQuarterEndConsolidatedStatementOfProfitOrLossIFRS_Con_Q3
    if key == "edif_FinancialReportSummary_Con_Q2":
        return sc.edif_FinancialReportSummary_Con_Q2
    if key == "edif_FinancialReportSummary_Con_Q3":
        return sc.edif_FinancialReportSummary_Con_Q3
    if key == "edif_NotesSegmentInformationCondensedQuarterlyConsolidatedFinancialStatementsIFRS_Con_Q2":
        return sc.edif_NotesSegmentInformationCondensedQuarterlyConsolidatedFinancialStatementsIFRS_Con_Q2
    if key == "edif_NotesSegmentInformationCondensedQuarterlyConsolidatedFinancialStatementsIFRS_Con_Q3":
        return sc.edif_NotesSegmentInformationCondensedQuarterlyConsolidatedFinancialStatementsIFRS_Con_Q3
    if key == "edjp_BalanceSheet_NonCon_FY":
        return sc.edjp_BalanceSheet_NonCon_FY
    if key == "edjp_BalanceSheet_Con_FY":
        return sc.edjp_BalanceSheet_Con_FY
    if key == "edjp_ConsolidatedBalanceSheet_Con_FY":
        return sc.edjp_ConsolidatedBalanceSheet_Con_FY
    if key == "edjp_ConsolidatedStatementOfCashFlows_Con_FY":
        return sc.edjp_ConsolidatedStatementOfCashFlows_Con_FY
    if key == "edjp_ConsolidatedStatementOfChangesInEquity_Con_FY":
        return sc.edjp_ConsolidatedStatementOfChangesInEquity_Con_FY
    if key == "edjp_ConsolidatedStatementOfComprehensiveIncome_Con_FY":
        return sc.edjp_ConsolidatedStatementOfComprehensiveIncome_Con_FY
    if key == "edjp_ConsolidatedStatementOfIncome_Con_FY":
        return sc.edjp_ConsolidatedStatementOfIncome_Con_FY
    if key == "edjp_FinancialReportSummary_NonCon_FY":
        return sc.edjp_FinancialReportSummary_NonCon_FY
    if key == "edjp_FinancialReportSummary_Con_FY":
        return sc.edjp_FinancialReportSummary_Con_FY
    if key == "edjp_FinancialReportSummary_NonCon_Q1":
        return sc.edjp_FinancialReportSummary_NonCon_Q1
    if key == "edjp_FinancialReportSummary_Con_Q1":
        return sc.edjp_FinancialReportSummary_Con_Q1
    if key == "edjp_FinancialReportSummary_NonCon_Q2":
        return sc.edjp_FinancialReportSummary_NonCon_Q2
    if key == "edjp_FinancialReportSummary_Con_Q2":
        return sc.edjp_FinancialReportSummary_Con_Q2
    if key == "edjp_FinancialReportSummary_Con_Q3":
        return sc.edjp_FinancialReportSummary_Con_Q3
    if key == "edjp_FinancialReportSummary":
        return sc.edjp_FinancialReportSummary
    if key == "edjp_NotesSegmentInformationEtcConsolidatedFinancialStatements_Con_FY":
        return sc.edjp_NotesSegmentInformationEtcConsolidatedFinancialStatements_Con_FY
    if key == "edjp_NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatements_Con_Q1":
        return sc.edjp_NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatements_Con_Q1
    if key == "edjp_NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatements_Con_Q2":
        return sc.edjp_NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatements_Con_Q2
    if key == "edjp_NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatements_Con_Q3":
        return sc.edjp_NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatements_Con_Q3
    if key == "edjp_NotesSegmentInformationEtcQuarterlyFinancialStatements_NonCon_Q2":
        return sc.edjp_NotesSegmentInformationEtcQuarterlyFinancialStatements_NonCon_Q2
    if key == "edjp_QuarterlyBalanceSheet_NonCon_Q1":
        return sc.edjp_QuarterlyBalanceSheet_NonCon_Q1
    if key == "edjp_QuarterlyBalanceSheet_NonCon_Q2":
        return sc.edjp_QuarterlyBalanceSheet_NonCon_Q2
    if key == "edjp_QuarterlyConsolidatedBalanceSheet_Con_Q1":
        return sc.edjp_QuarterlyConsolidatedBalanceSheet_Con_Q1
    if key == "edjp_QuarterlyConsolidatedBalanceSheet_Con_Q2":
        return sc.edjp_QuarterlyConsolidatedBalanceSheet_Con_Q2
    if key == "edjp_QuarterlyConsolidatedBalanceSheet_Con_Q3":
        return sc.edjp_QuarterlyConsolidatedBalanceSheet_Con_Q3
    if key == "edjp_QuarterlyConsolidatedStatementOfCashFlows_Con_Q2":
        return sc.edjp_QuarterlyConsolidatedStatementOfCashFlows_Con_Q2
    if key == "edjp_QuarterlyConsolidatedStatementOfCashFlows_Con_Q3":
        return sc.edjp_QuarterlyConsolidatedStatementOfCashFlows_Con_Q3
    if key == "edjp_QuarterlyStatementOfCashFlows_NonCon_Q2":
        return sc.edjp_QuarterlyStatementOfCashFlows_NonCon_Q2
    if key == "edjp_StatementOfCashFlows_NonCon_FY":
        return sc.edjp_StatementOfCashFlows_NonCon_FY
    if key == "edjp_StatementOfChangesInEquity_NonCon_FY":
        return sc.edjp_StatementOfChangesInEquity_NonCon_FY
    if key == "edjp_StatementOfChangesInEquity_Con_FY":
        return sc.edjp_StatementOfChangesInEquity_Con_FY
    if key == "edjp_StatementOfIncome_Con_FY":
        return sc.edjp_StatementOfIncome_Con_FY
    if key == "edjp_StatementOfIncome_NonCon_FY":
        return sc.edjp_StatementOfIncome_NonCon_FY
    if key == "edjp_YearToQuarterEndConsolidatedStatementOfComprehensiveIncome_Con_Q1":
        return sc.edjp_YearToQuarterEndConsolidatedStatementOfComprehensiveIncome_Con_Q1
    if key == "edjp_YearToQuarterEndConsolidatedStatementOfComprehensiveIncome_Con_Q2":
        return sc.edjp_YearToQuarterEndConsolidatedStatementOfComprehensiveIncome_Con_Q2
    if key == "edjp_YearToQuarterEndConsolidatedStatementOfComprehensiveIncome_Con_Q3":
        return sc.edjp_YearToQuarterEndConsolidatedStatementOfComprehensiveIncome_Con_Q3
    if key == "edjp_YearToQuarterEndConsolidatedStatementOfComprehensiveIncomeSingleStatement_Con_Q2":
        return sc.edjp_YearToQuarterEndConsolidatedStatementOfComprehensiveIncomeSingleStatement_Con_Q2
    if key == "edjp_YearToQuarterEndConsolidatedStatementOfIncome_Con_Q1":
        return sc.edjp_YearToQuarterEndConsolidatedStatementOfIncome_Con_Q1
    if key == "edjp_YearToQuarterEndConsolidatedStatementOfIncome_Con_Q2":
        return sc.edjp_YearToQuarterEndConsolidatedStatementOfIncome_Con_Q2
    if key == "edjp_YearToQuarterEndConsolidatedStatementOfIncome_Con_Q3":
        return sc.edjp_YearToQuarterEndConsolidatedStatementOfIncome_Con_Q3
    if key == "edjp_YearToQuarterEndStatementOfIncome_NonCon_Q1":
        return sc.edjp_YearToQuarterEndStatementOfIncome_NonCon_Q1
    if key == "edjp_YearToQuarterEndStatementOfIncome_NonCon_Q2":
        return sc.edjp_YearToQuarterEndStatementOfIncome_NonCon_Q2
    if key == "edjp_FinancialReportSummary_Con_HY_spec":
        return sc.edjp_FinancialReportSummary_Con_HY_spec
    if key == "edjp_NotesSegmentInformationEtcSemiAnnualConsolidatedFinancialStatements_Con_HY_spec":
        return sc.edjp_NotesSegmentInformationEtcSemiAnnualConsolidatedFinancialStatements_Con_HY_spec
    if key == "edjp_SemiAnnualBalanceSheet_Con_HY_spec":
        return sc.edjp_SemiAnnualBalanceSheet_Con_HY_spec
    if key == "edjp_SemiAnnualConsolidatedBalanceSheet_Con_HY_spec":
        return sc.edjp_SemiAnnualConsolidatedBalanceSheet_Con_HY_spec
    if key == "edjp_SemiAnnualConsolidatedStatementOfChangesInEquity_Con_HY_spec":
        return sc.edjp_SemiAnnualConsolidatedStatementOfChangesInEquity_Con_HY_spec
    if key == "edjp_SemiAnnualConsolidatedStatementOfComprehensiveIncome_Con_HY_spec":
        return sc.edjp_SemiAnnualConsolidatedStatementOfComprehensiveIncome_Con_HY_spec
    if key == "edjp_SemiAnnualConsolidatedStatementOfIncome_Con_HY_spec":
        return sc.edjp_SemiAnnualConsolidatedStatementOfIncome_Con_HY_spec
    if key == "edjp_SemiAnnualStatementOfChangesInEquity_Con_HY_spec":
        return sc.edjp_SemiAnnualStatementOfChangesInEquity_Con_HY_spec
    if key == "edjp_SemiAnnualStatementOfIncome_Con_HY_spec":
        return sc.edjp_SemiAnnualStatementOfIncome_Con_HY_spec
    if key == "rvfc_FinancialReportSummary":
        return sc.rvfc_FinancialReportSummary
    if key == "rvfc_FinancialReportSummary_spec":
        return sc.rvfc_FinancialReportSummary_spec


def get_response_schema_FinancialReportSummary_class():
    items = (
    sc.edif_FinancialReportSummary_Con_Q2
    | sc.edif_FinancialReportSummary_Con_Q3
    | sc.edjp_FinancialReportSummary_NonCon_FY
    | sc.edjp_FinancialReportSummary_Con_FY
    | sc.edjp_FinancialReportSummary_NonCon_Q1
    | sc.edjp_FinancialReportSummary_Con_Q1
    | sc.edjp_FinancialReportSummary_NonCon_Q2
    | sc.edjp_FinancialReportSummary_Con_Q2
    | sc.edjp_FinancialReportSummary_Con_Q3
    | sc.edjp_FinancialReportSummary
    | sc.edjp_FinancialReportSummary_Con_HY_spec
    | sc.rvfc_FinancialReportSummary
    | sc.rvfc_FinancialReportSummary_spec
    )
    return items
