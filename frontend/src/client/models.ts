/**
 * 期中平均株式数 
 */
export type AverageNumberOfShares_edjp_FinancialReportSummary = {
	/**
	 * 当年度期初から第２四半期間_非連結又は個別_実績
	 */
	current_accumulated_q2_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第２四半期間_非連結又は個別_実績
	 */
	prior_accumulated_q2_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 期中平均株式数 
 */
export type AverageNumberOfShares_edjp_FinancialReportSummary_FY = {
	/**
	 * 当年度会計期間_非連結又は個別_実績
	 */
	current_year_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度会計期間_非連結又は個別_実績
	 */
	prior_year_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 期中平均株式数 
 */
export type AverageNumberOfShares_edjp_FinancialReportSummary_HY_specific_business = {
	/**
	 * 当年度期初から第２四半期間_非連結又は個別_実績
	 */
	current_accumulated_q2_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第２四半期間_非連結又は個別_実績
	 */
	prior_accumulated_q2_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 期中平均株式数 
 */
export type AverageNumberOfShares_edjp_FinancialReportSummary_Q1 = {
	/**
	 * 当年度期初から第１四半期間_非連結又は個別_実績
	 */
	current_accumulated_q1_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第１四半期間_非連結又は個別_実績
	 */
	prior_accumulated_q1_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 期中平均株式数 
 */
export type AverageNumberOfShares_edjp_FinancialReportSummary_Q2 = {
	/**
	 * 当年度期初から第２四半期間_非連結又は個別_実績
	 */
	current_accumulated_q2_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第２四半期間_非連結又は個別_実績
	 */
	prior_accumulated_q2_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 期中平均株式数 
 */
export type AverageNumberOfShares_edjp_FinancialReportSummary_Q3 = {
	/**
	 * 当年度期初から第３四半期間_非連結又は個別_実績
	 */
	current_accumulated_q3_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第３四半期間_非連結又は個別_実績
	 */
	prior_accumulated_q3_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
};



export type Body_login_login_access_token = {
	grant_type?: string | null;
	username: string;
	password: string;
	scope?: string;
	client_id?: string | null;
	client_secret?: string | null;
};



/**
 * 自己資本比率 
 */
export type CapitalAdequacyRatio_edjp_FinancialReportSummary = {
	/**
	 * 当年度期初から第２四半期間時点_連結_実績
	 */
	current_accumulated_q2_instant_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度時点_連結_実績
	 */
	prior_year_instant_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 自己資本比率 
 */
export type CapitalAdequacyRatio_edjp_FinancialReportSummary_FY = {
	/**
	 * 当年度時点_連結_実績
	 */
	current_year_instant_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度時点_非連結又は個別_実績
	 */
	current_year_instant_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度時点_連結_実績
	 */
	prior_year_instant_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度時点_非連結又は個別_実績
	 */
	prior_year_instant_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 自己資本比率 
 */
export type CapitalAdequacyRatio_edjp_FinancialReportSummary_HY_specific_business = {
	/**
	 * 当年度期初から第２四半期間時点_連結_実績
	 */
	current_accumulated_q2_instant_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度期初から第２四半期間時点_非連結又は個別_実績
	 */
	current_accumulated_q2_instant_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度時点_連結_実績
	 */
	prior_year_instant_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度時点_非連結又は個別_実績
	 */
	prior_year_instant_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 自己資本比率 
 */
export type CapitalAdequacyRatio_edjp_FinancialReportSummary_Q1 = {
	/**
	 * 当年度期初から第１四半期間時点_連結_実績
	 */
	current_accumulated_q1_instant_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度期初から第１四半期間時点_非連結又は個別_実績
	 */
	current_accumulated_q1_instant_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度時点_連結_実績
	 */
	prior_year_instant_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度時点_非連結又は個別_実績
	 */
	prior_year_instant_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 自己資本比率 
 */
export type CapitalAdequacyRatio_edjp_FinancialReportSummary_Q2 = {
	/**
	 * 当年度期初から第２四半期間時点_連結_実績
	 */
	current_accumulated_q2_instant_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度期初から第２四半期間時点_非連結又は個別_実績
	 */
	current_accumulated_q2_instant_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度時点_連結_実績
	 */
	prior_year_instant_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度時点_非連結又は個別_実績
	 */
	prior_year_instant_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 自己資本比率 
 */
export type CapitalAdequacyRatio_edjp_FinancialReportSummary_Q3 = {
	/**
	 * 当年度期初から第３四半期間時点_連結_実績
	 */
	current_accumulated_q3_instant_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度時点_連結_実績
	 */
	prior_year_instant_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 現金及び現金同等物期末残高 
 */
export type CashAndEquivalentsEndOfPeriod_edjp_FinancialReportSummary_FY = {
	/**
	 * 当年度時点_連結_実績
	 */
	current_year_instant_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度時点_非連結又は個別_実績
	 */
	current_year_instant_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度時点_連結_実績
	 */
	prior_year_instant_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度時点_非連結又は個別_実績
	 */
	prior_year_instant_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 財務活動によるキャッシュ・フロー 
 */
export type CashFlowsFromFinancingActivities_edjp_FinancialReportSummary_FY = {
	/**
	 * 当年度会計期間_連結_実績
	 */
	current_year_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_実績
	 */
	current_year_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度会計期間_連結_実績
	 */
	prior_year_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度会計期間_非連結又は個別_実績
	 */
	prior_year_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 投資活動によるキャッシュ・フロー 
 */
export type CashFlowsFromInvestingActivities_edjp_FinancialReportSummary_FY = {
	/**
	 * 当年度会計期間_連結_実績
	 */
	current_year_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_実績
	 */
	current_year_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度会計期間_連結_実績
	 */
	prior_year_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度会計期間_非連結又は個別_実績
	 */
	prior_year_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 営業活動によるキャッシュ・フロー 
 */
export type CashFlowsFromOperatingActivities_edjp_FinancialReportSummary_FY = {
	/**
	 * 当年度会計期間_連結_実績
	 */
	current_year_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_実績
	 */
	current_year_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度会計期間_連結_実績
	 */
	prior_year_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度会計期間_非連結又は個別_実績
	 */
	prior_year_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 包括利益増減率 
 */
export type ChangeInComprehensiveIncome_edjp_FinancialReportSummary = {
	/**
	 * 当年度期初から第２四半期間_連結_実績
	 */
	current_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第２四半期間_連結_実績
	 */
	prior_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 包括利益増減率 
 */
export type ChangeInComprehensiveIncome_edjp_FinancialReportSummary_FY = {
	/**
	 * 当年度会計期間_連結_実績
	 */
	current_year_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度会計期間_連結_実績
	 */
	prior_year_duration_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 包括利益増減率 
 */
export type ChangeInComprehensiveIncome_edjp_FinancialReportSummary_HY_specific_business = {
	/**
	 * 当年度期初から第２四半期間_連結_実績
	 */
	current_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第２四半期間_連結_実績
	 */
	prior_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 包括利益増減率 
 */
export type ChangeInComprehensiveIncome_edjp_FinancialReportSummary_Q1 = {
	/**
	 * 当年度期初から第１四半期間_連結_実績
	 */
	current_accumulated_q1_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第１四半期間_連結_実績
	 */
	prior_accumulated_q1_duration_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 包括利益増減率 
 */
export type ChangeInComprehensiveIncome_edjp_FinancialReportSummary_Q2 = {
	/**
	 * 当年度期初から第２四半期間_連結_実績
	 */
	current_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第２四半期間_連結_実績
	 */
	prior_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 包括利益増減率 
 */
export type ChangeInComprehensiveIncome_edjp_FinancialReportSummary_Q3 = {
	/**
	 * 当年度期初から第３四半期間_連結_実績
	 */
	current_accumulated_q3_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第３四半期間_連結_実績
	 */
	prior_accumulated_q3_duration_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 増減率、当期純利益 
 */
export type ChangeInNetIncome_edjp_FinancialReportSummary_FY = {
	/**
	 * 当年度会計期間_非連結又は個別_実績
	 */
	current_year_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 次年度期初から第２四半期間_非連結又は個別_予想
	 */
	next_accumulated_q2_duration_non_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 次年度期初から第２四半期間_非連結又は個別_下限
	 */
	next_accumulated_q2_duration_non_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 次年度期初から第２四半期間_非連結又は個別_上限
	 */
	next_accumulated_q2_duration_non_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 次年度会計期間_非連結又は個別_予想
	 */
	next_year_duration_non_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 次年度会計期間_非連結又は個別_下限
	 */
	next_year_duration_non_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 次年度会計期間_非連結又は個別_上限
	 */
	next_year_duration_non_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 前年度会計期間_非連結又は個別_実績
	 */
	prior_year_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 増減率、当期純利益 
 */
export type ChangeInNetIncome_edjp_FinancialReportSummary_HY_specific_business = {
	/**
	 * 当年度期初から第２四半期間_非連結又は個別_実績
	 */
	current_accumulated_q2_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_予想
	 */
	current_year_duration_non_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_下限
	 */
	current_year_duration_non_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_上限
	 */
	current_year_duration_non_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第２四半期間_非連結又は個別_実績
	 */
	prior_accumulated_q2_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 増減率、当期純利益 
 */
export type ChangeInNetIncome_edjp_FinancialReportSummary_Q1 = {
	/**
	 * 当年度期初から第１四半期間_非連結又は個別_実績
	 */
	current_accumulated_q1_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度期初から第２四半期間_非連結又は個別_予想
	 */
	current_accumulated_q2_duration_non_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度期初から第２四半期間_非連結又は個別_下限
	 */
	current_accumulated_q2_duration_non_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度期初から第２四半期間_非連結又は個別_上限
	 */
	current_accumulated_q2_duration_non_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_予想
	 */
	current_year_duration_non_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_下限
	 */
	current_year_duration_non_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_上限
	 */
	current_year_duration_non_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第１四半期間_非連結又は個別_実績
	 */
	prior_accumulated_q1_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 増減率、当期純利益 
 */
export type ChangeInNetIncome_edjp_FinancialReportSummary_Q2 = {
	/**
	 * 当年度期初から第２四半期間_非連結又は個別_実績
	 */
	current_accumulated_q2_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_予想
	 */
	current_year_duration_non_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_下限
	 */
	current_year_duration_non_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_上限
	 */
	current_year_duration_non_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第２四半期間_非連結又は個別_実績
	 */
	prior_accumulated_q2_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 増減率、純営業収益、証券 
 */
export type ChangeInNetOperatingRevenuesSE_edjp_FinancialReportSummary_Q2 = {
	/**
	 * 当年度期初から第２四半期間_連結_実績
	 */
	current_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度期初から第２四半期間_非連結又は個別_実績
	 */
	current_accumulated_q2_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第２四半期間_連結_実績
	 */
	prior_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第２四半期間_非連結又は個別_実績
	 */
	prior_accumulated_q2_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 増減率、売上高 
 */
export type ChangeInNetSales_edjp_FinancialReportSummary = {
	/**
	 * 当年度期初から第２四半期間_連結_実績
	 */
	current_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_予想
	 */
	current_year_duration_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_下限
	 */
	current_year_duration_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_上限
	 */
	current_year_duration_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第２四半期間_連結_実績
	 */
	prior_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 増減率、売上高 
 */
export type ChangeInNetSales_edjp_FinancialReportSummary_FY = {
	/**
	 * 当年度会計期間_連結_実績
	 */
	current_year_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_実績
	 */
	current_year_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 次年度期初から第２四半期間_非連結又は個別_予想
	 */
	next_accumulated_q2_duration_non_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 次年度期初から第２四半期間_非連結又は個別_下限
	 */
	next_accumulated_q2_duration_non_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 次年度期初から第２四半期間_非連結又は個別_上限
	 */
	next_accumulated_q2_duration_non_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 次年度会計期間_連結_予想
	 */
	next_year_duration_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 次年度会計期間_連結_下限
	 */
	next_year_duration_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 次年度会計期間_連結_上限
	 */
	next_year_duration_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 次年度会計期間_非連結又は個別_予想
	 */
	next_year_duration_non_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 次年度会計期間_非連結又は個別_下限
	 */
	next_year_duration_non_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 次年度会計期間_非連結又は個別_上限
	 */
	next_year_duration_non_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 前年度会計期間_連結_実績
	 */
	prior_year_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度会計期間_非連結又は個別_実績
	 */
	prior_year_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 増減率、売上高 
 */
export type ChangeInNetSales_edjp_FinancialReportSummary_Q1 = {
	/**
	 * 当年度期初から第１四半期間_連結_実績
	 */
	current_accumulated_q1_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度期初から第１四半期間_非連結又は個別_実績
	 */
	current_accumulated_q1_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度期初から第２四半期間_非連結又は個別_予想
	 */
	current_accumulated_q2_duration_non_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度期初から第２四半期間_非連結又は個別_下限
	 */
	current_accumulated_q2_duration_non_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度期初から第２四半期間_非連結又は個別_上限
	 */
	current_accumulated_q2_duration_non_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_予想
	 */
	current_year_duration_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_下限
	 */
	current_year_duration_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_上限
	 */
	current_year_duration_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_予想
	 */
	current_year_duration_non_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_下限
	 */
	current_year_duration_non_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_上限
	 */
	current_year_duration_non_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第１四半期間_連結_実績
	 */
	prior_accumulated_q1_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第１四半期間_非連結又は個別_実績
	 */
	prior_accumulated_q1_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 増減率、売上高 
 */
export type ChangeInNetSales_edjp_FinancialReportSummary_Q2 = {
	/**
	 * 当年度期初から第２四半期間_連結_実績
	 */
	current_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度期初から第２四半期間_非連結又は個別_実績
	 */
	current_accumulated_q2_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_予想
	 */
	current_year_duration_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_下限
	 */
	current_year_duration_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_上限
	 */
	current_year_duration_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_予想
	 */
	current_year_duration_non_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_下限
	 */
	current_year_duration_non_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_上限
	 */
	current_year_duration_non_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第２四半期間_連結_実績
	 */
	prior_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第２四半期間_非連結又は個別_実績
	 */
	prior_accumulated_q2_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 増減率、売上高 
 */
export type ChangeInNetSales_edjp_FinancialReportSummary_Q3 = {
	/**
	 * 当年度期初から第３四半期間_連結_実績
	 */
	current_accumulated_q3_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_予想
	 */
	current_year_duration_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_下限
	 */
	current_year_duration_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_上限
	 */
	current_year_duration_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第３四半期間_連結_実績
	 */
	prior_accumulated_q3_duration_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 増減率、営業利益 
 */
export type ChangeInOperatingIncome_edjp_FinancialReportSummary = {
	/**
	 * 当年度期初から第２四半期間_連結_実績
	 */
	current_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_予想
	 */
	current_year_duration_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_下限
	 */
	current_year_duration_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_上限
	 */
	current_year_duration_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第２四半期間_連結_実績
	 */
	prior_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 増減率、営業利益 
 */
export type ChangeInOperatingIncome_edjp_FinancialReportSummary_FY = {
	/**
	 * 当年度会計期間_連結_実績
	 */
	current_year_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_実績
	 */
	current_year_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 次年度期初から第２四半期間_非連結又は個別_予想
	 */
	next_accumulated_q2_duration_non_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 次年度期初から第２四半期間_非連結又は個別_下限
	 */
	next_accumulated_q2_duration_non_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 次年度期初から第２四半期間_非連結又は個別_上限
	 */
	next_accumulated_q2_duration_non_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 次年度会計期間_連結_予想
	 */
	next_year_duration_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 次年度会計期間_連結_下限
	 */
	next_year_duration_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 次年度会計期間_連結_上限
	 */
	next_year_duration_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 次年度会計期間_非連結又は個別_予想
	 */
	next_year_duration_non_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 次年度会計期間_非連結又は個別_下限
	 */
	next_year_duration_non_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 次年度会計期間_非連結又は個別_上限
	 */
	next_year_duration_non_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 前年度会計期間_連結_実績
	 */
	prior_year_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度会計期間_非連結又は個別_実績
	 */
	prior_year_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 増減率、営業利益 
 */
export type ChangeInOperatingIncome_edjp_FinancialReportSummary_Q1 = {
	/**
	 * 当年度期初から第１四半期間_連結_実績
	 */
	current_accumulated_q1_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度期初から第１四半期間_非連結又は個別_実績
	 */
	current_accumulated_q1_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度期初から第２四半期間_非連結又は個別_予想
	 */
	current_accumulated_q2_duration_non_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度期初から第２四半期間_非連結又は個別_下限
	 */
	current_accumulated_q2_duration_non_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度期初から第２四半期間_非連結又は個別_上限
	 */
	current_accumulated_q2_duration_non_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_予想
	 */
	current_year_duration_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_下限
	 */
	current_year_duration_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_上限
	 */
	current_year_duration_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_予想
	 */
	current_year_duration_non_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_下限
	 */
	current_year_duration_non_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_上限
	 */
	current_year_duration_non_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第１四半期間_連結_実績
	 */
	prior_accumulated_q1_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第１四半期間_非連結又は個別_実績
	 */
	prior_accumulated_q1_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 増減率、営業利益 
 */
export type ChangeInOperatingIncome_edjp_FinancialReportSummary_Q2 = {
	/**
	 * 当年度期初から第２四半期間_連結_実績
	 */
	current_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度期初から第２四半期間_非連結又は個別_実績
	 */
	current_accumulated_q2_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_予想
	 */
	current_year_duration_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_下限
	 */
	current_year_duration_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_上限
	 */
	current_year_duration_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_予想
	 */
	current_year_duration_non_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_下限
	 */
	current_year_duration_non_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_上限
	 */
	current_year_duration_non_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第２四半期間_連結_実績
	 */
	prior_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第２四半期間_非連結又は個別_実績
	 */
	prior_accumulated_q2_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 増減率、営業利益 
 */
export type ChangeInOperatingIncome_edjp_FinancialReportSummary_Q3 = {
	/**
	 * 当年度期初から第３四半期間_連結_実績
	 */
	current_accumulated_q3_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_予想
	 */
	current_year_duration_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_下限
	 */
	current_year_duration_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_上限
	 */
	current_year_duration_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第３四半期間_連結_実績
	 */
	prior_accumulated_q3_duration_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 増減率、営業収益、証券 
 */
export type ChangeInOperatingRevenuesSE_edjp_FinancialReportSummary_Q2 = {
	/**
	 * 当年度期初から第２四半期間_連結_実績
	 */
	current_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第２四半期間_連結_実績
	 */
	prior_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 増減率、営業収益 
 */
export type ChangeInOperatingRevenues_edjp_FinancialReportSummary_Q2 = {
	/**
	 * 当年度期初から第２四半期間_連結_実績
	 */
	current_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度期初から第２四半期間_非連結又は個別_実績
	 */
	current_accumulated_q2_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_予想
	 */
	current_year_duration_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_下限
	 */
	current_year_duration_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_上限
	 */
	current_year_duration_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第２四半期間_連結_実績
	 */
	prior_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第２四半期間_非連結又は個別_実績
	 */
	prior_accumulated_q2_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 増減率、経常利益 
 */
export type ChangeInOrdinaryIncome_edjp_FinancialReportSummary = {
	/**
	 * 当年度期初から第２四半期間_連結_実績
	 */
	current_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_予想
	 */
	current_year_duration_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_下限
	 */
	current_year_duration_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_上限
	 */
	current_year_duration_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第２四半期間_連結_実績
	 */
	prior_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 増減率、経常利益 
 */
export type ChangeInOrdinaryIncome_edjp_FinancialReportSummary_FY = {
	/**
	 * 当年度会計期間_連結_実績
	 */
	current_year_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_実績
	 */
	current_year_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 次年度期初から第２四半期間_非連結又は個別_予想
	 */
	next_accumulated_q2_duration_non_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 次年度期初から第２四半期間_非連結又は個別_下限
	 */
	next_accumulated_q2_duration_non_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 次年度期初から第２四半期間_非連結又は個別_上限
	 */
	next_accumulated_q2_duration_non_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 次年度会計期間_連結_予想
	 */
	next_year_duration_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 次年度会計期間_連結_下限
	 */
	next_year_duration_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 次年度会計期間_連結_上限
	 */
	next_year_duration_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 次年度会計期間_非連結又は個別_予想
	 */
	next_year_duration_non_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 次年度会計期間_非連結又は個別_下限
	 */
	next_year_duration_non_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 次年度会計期間_非連結又は個別_上限
	 */
	next_year_duration_non_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 前年度会計期間_連結_実績
	 */
	prior_year_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度会計期間_非連結又は個別_実績
	 */
	prior_year_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 増減率、経常利益 
 */
export type ChangeInOrdinaryIncome_edjp_FinancialReportSummary_HY_specific_business = {
	/**
	 * 当年度期初から第２四半期間_連結_実績
	 */
	current_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度期初から第２四半期間_非連結又は個別_実績
	 */
	current_accumulated_q2_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_予想
	 */
	current_year_duration_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_下限
	 */
	current_year_duration_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_上限
	 */
	current_year_duration_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_予想
	 */
	current_year_duration_non_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_下限
	 */
	current_year_duration_non_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_上限
	 */
	current_year_duration_non_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第２四半期間_連結_実績
	 */
	prior_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第２四半期間_非連結又は個別_実績
	 */
	prior_accumulated_q2_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 増減率、経常利益 
 */
export type ChangeInOrdinaryIncome_edjp_FinancialReportSummary_Q1 = {
	/**
	 * 当年度期初から第１四半期間_連結_実績
	 */
	current_accumulated_q1_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度期初から第１四半期間_非連結又は個別_実績
	 */
	current_accumulated_q1_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度期初から第２四半期間_非連結又は個別_予想
	 */
	current_accumulated_q2_duration_non_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度期初から第２四半期間_非連結又は個別_下限
	 */
	current_accumulated_q2_duration_non_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度期初から第２四半期間_非連結又は個別_上限
	 */
	current_accumulated_q2_duration_non_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_予想
	 */
	current_year_duration_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_下限
	 */
	current_year_duration_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_上限
	 */
	current_year_duration_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_予想
	 */
	current_year_duration_non_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_下限
	 */
	current_year_duration_non_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_上限
	 */
	current_year_duration_non_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第１四半期間_連結_実績
	 */
	prior_accumulated_q1_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第１四半期間_非連結又は個別_実績
	 */
	prior_accumulated_q1_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 増減率、経常利益 
 */
export type ChangeInOrdinaryIncome_edjp_FinancialReportSummary_Q2 = {
	/**
	 * 当年度期初から第２四半期間_連結_実績
	 */
	current_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度期初から第２四半期間_非連結又は個別_実績
	 */
	current_accumulated_q2_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_予想
	 */
	current_year_duration_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_下限
	 */
	current_year_duration_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_上限
	 */
	current_year_duration_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_予想
	 */
	current_year_duration_non_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_下限
	 */
	current_year_duration_non_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_上限
	 */
	current_year_duration_non_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第２四半期間_連結_実績
	 */
	prior_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第２四半期間_非連結又は個別_実績
	 */
	prior_accumulated_q2_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 増減率、経常利益 
 */
export type ChangeInOrdinaryIncome_edjp_FinancialReportSummary_Q3 = {
	/**
	 * 当年度期初から第３四半期間_連結_実績
	 */
	current_accumulated_q3_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_予想
	 */
	current_year_duration_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_下限
	 */
	current_year_duration_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_上限
	 */
	current_year_duration_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第３四半期間_連結_実績
	 */
	prior_accumulated_q3_duration_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 増減率、経常収益、銀行 
 */
export type ChangeInOrdinaryRevenuesBK_edjp_FinancialReportSummary_HY_specific_business = {
	/**
	 * 当年度期初から第２四半期間_連結_実績
	 */
	current_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度期初から第２四半期間_非連結又は個別_実績
	 */
	current_accumulated_q2_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第２四半期間_連結_実績
	 */
	prior_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第２四半期間_非連結又は個別_実績
	 */
	prior_accumulated_q2_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 増減率、親会社株主に帰属する当期純利益 
 */
export type ChangeInProfitAttributableToOwnersOfParent_edjp_FinancialReportSummary = {
	/**
	 * 当年度期初から第２四半期間_連結_実績
	 */
	current_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_予想
	 */
	current_year_duration_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_下限
	 */
	current_year_duration_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_上限
	 */
	current_year_duration_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第２四半期間_連結_実績
	 */
	prior_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 増減率、親会社株主に帰属する当期純利益 
 */
export type ChangeInProfitAttributableToOwnersOfParent_edjp_FinancialReportSummary_FY = {
	/**
	 * 当年度会計期間_連結_実績
	 */
	current_year_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 次年度会計期間_連結_予想
	 */
	next_year_duration_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 次年度会計期間_連結_下限
	 */
	next_year_duration_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 次年度会計期間_連結_上限
	 */
	next_year_duration_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 前年度会計期間_連結_実績
	 */
	prior_year_duration_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 増減率、親会社株主に帰属する当期純利益 
 */
export type ChangeInProfitAttributableToOwnersOfParent_edjp_FinancialReportSummary_HY_specific_business = {
	/**
	 * 当年度期初から第２四半期間_連結_実績
	 */
	current_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_予想
	 */
	current_year_duration_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_下限
	 */
	current_year_duration_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_上限
	 */
	current_year_duration_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第２四半期間_連結_実績
	 */
	prior_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 増減率、親会社株主に帰属する当期純利益 
 */
export type ChangeInProfitAttributableToOwnersOfParent_edjp_FinancialReportSummary_Q1 = {
	/**
	 * 当年度期初から第１四半期間_連結_実績
	 */
	current_accumulated_q1_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_予想
	 */
	current_year_duration_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_下限
	 */
	current_year_duration_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_上限
	 */
	current_year_duration_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第１四半期間_連結_実績
	 */
	prior_accumulated_q1_duration_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 増減率、親会社株主に帰属する当期純利益 
 */
export type ChangeInProfitAttributableToOwnersOfParent_edjp_FinancialReportSummary_Q2 = {
	/**
	 * 当年度期初から第２四半期間_連結_実績
	 */
	current_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_予想
	 */
	current_year_duration_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_下限
	 */
	current_year_duration_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_上限
	 */
	current_year_duration_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第２四半期間_連結_実績
	 */
	prior_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 増減率、親会社株主に帰属する当期純利益 
 */
export type ChangeInProfitAttributableToOwnersOfParent_edjp_FinancialReportSummary_Q3 = {
	/**
	 * 当年度期初から第３四半期間_連結_実績
	 */
	current_accumulated_q3_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_予想
	 */
	current_year_duration_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_下限
	 */
	current_year_duration_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_上限
	 */
	current_year_duration_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第３四半期間_連結_実績
	 */
	prior_accumulated_q3_duration_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 記念配当 
 */
export type CommemorativeDividend_edjp_FinancialReportSummary_Q2 = {
	/**
	 * 当年度期初から第２四半期間_年間_非連結又は個別_実績
	 */
	current_accumulated_q2_duration_annual_member_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 包括利益 
 */
export type ComprehensiveIncome_edjp_FinancialReportSummary = {
	/**
	 * 当年度期初から第２四半期間_連結_実績
	 */
	current_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第２四半期間_連結_実績
	 */
	prior_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 包括利益 
 */
export type ComprehensiveIncome_edjp_FinancialReportSummary_FY = {
	/**
	 * 当年度会計期間_連結_実績
	 */
	current_year_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度会計期間_連結_実績
	 */
	prior_year_duration_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 包括利益 
 */
export type ComprehensiveIncome_edjp_FinancialReportSummary_HY_specific_business = {
	/**
	 * 当年度期初から第２四半期間_連結_実績
	 */
	current_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第２四半期間_連結_実績
	 */
	prior_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 包括利益 
 */
export type ComprehensiveIncome_edjp_FinancialReportSummary_Q1 = {
	/**
	 * 当年度期初から第１四半期間_連結_実績
	 */
	current_accumulated_q1_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第１四半期間_連結_実績
	 */
	prior_accumulated_q1_duration_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 包括利益 
 */
export type ComprehensiveIncome_edjp_FinancialReportSummary_Q2 = {
	/**
	 * 当年度期初から第２四半期間_連結_実績
	 */
	current_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第２四半期間_連結_実績
	 */
	prior_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 包括利益 
 */
export type ComprehensiveIncome_edjp_FinancialReportSummary_Q3 = {
	/**
	 * 当年度期初から第３四半期間_連結_実績
	 */
	current_accumulated_q3_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第３四半期間_連結_実績
	 */
	prior_accumulated_q3_duration_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 潜在株式調整後1株当たり当期純利益 
 */
export type DilutedNetIncomePerShare_edjp_FinancialReportSummary = {
	/**
	 * 当年度期初から第２四半期間_連結_実績
	 */
	current_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第２四半期間_連結_実績
	 */
	prior_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 潜在株式調整後1株当たり当期純利益 
 */
export type DilutedNetIncomePerShare_edjp_FinancialReportSummary_FY = {
	/**
	 * 当年度会計期間_連結_実績
	 */
	current_year_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_実績
	 */
	current_year_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度会計期間_連結_実績
	 */
	prior_year_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度会計期間_非連結又は個別_実績
	 */
	prior_year_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 潜在株式調整後1株当たり当期純利益 
 */
export type DilutedNetIncomePerShare_edjp_FinancialReportSummary_HY_specific_business = {
	/**
	 * 当年度期初から第２四半期間_連結_実績
	 */
	current_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第２四半期間_連結_実績
	 */
	prior_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 潜在株式調整後1株当たり当期純利益 
 */
export type DilutedNetIncomePerShare_edjp_FinancialReportSummary_Q1 = {
	/**
	 * 当年度期初から第１四半期間_連結_実績
	 */
	current_accumulated_q1_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度期初から第１四半期間_非連結又は個別_実績
	 */
	current_accumulated_q1_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第１四半期間_連結_実績
	 */
	prior_accumulated_q1_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第１四半期間_非連結又は個別_実績
	 */
	prior_accumulated_q1_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 潜在株式調整後1株当たり当期純利益 
 */
export type DilutedNetIncomePerShare_edjp_FinancialReportSummary_Q2 = {
	/**
	 * 当年度期初から第２四半期間_連結_実績
	 */
	current_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度期初から第２四半期間_非連結又は個別_実績
	 */
	current_accumulated_q2_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第２四半期間_連結_実績
	 */
	prior_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第２四半期間_非連結又は個別_実績
	 */
	prior_accumulated_q2_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 潜在株式調整後1株当たり当期純利益 
 */
export type DilutedNetIncomePerShare_edjp_FinancialReportSummary_Q3 = {
	/**
	 * 当年度期初から第３四半期間_連結_実績
	 */
	current_accumulated_q3_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第３四半期間_連結_実績
	 */
	prior_accumulated_q3_duration_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 1株当たり配当金 
 */
export type DividendPerShare_edjp_FinancialReportSummary = {
	/**
	 * 当年度会計期間_年間_非連結又は個別_予想
	 */
	current_year_duration_annual_member_non_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_年間_非連結又は個別_下限
	 */
	current_year_duration_annual_member_non_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_年間_非連結又は個別_上限
	 */
	current_year_duration_annual_member_non_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_1Q_非連結又は個別_実績
	 */
	current_year_duration_first_quarter_member_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_2Q_非連結又は個別_実績
	 */
	current_year_duration_second_quarter_member_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_3Q_非連結又は個別_予想
	 */
	current_year_duration_third_quarter_member_non_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_3Q_非連結又は個別_下限
	 */
	current_year_duration_third_quarter_member_non_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_3Q_非連結又は個別_上限
	 */
	current_year_duration_third_quarter_member_non_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_期末_非連結又は個別_予想
	 */
	current_year_duration_year_end_member_non_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_期末_非連結又は個別_下限
	 */
	current_year_duration_year_end_member_non_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_期末_非連結又は個別_上限
	 */
	current_year_duration_year_end_member_non_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 前年度会計期間_年間_非連結又は個別_実績
	 */
	prior_year_duration_annual_member_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度会計期間_1Q_非連結又は個別_実績
	 */
	prior_year_duration_first_quarter_member_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度会計期間_2Q_非連結又は個別_実績
	 */
	prior_year_duration_second_quarter_member_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度会計期間_3Q_非連結又は個別_実績
	 */
	prior_year_duration_third_quarter_member_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度会計期間_期末_非連結又は個別_実績
	 */
	prior_year_duration_year_end_member_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 1株当たり配当金 
 */
export type DividendPerShare_edjp_FinancialReportSummary_FY = {
	/**
	 * 当年度会計期間_年間_非連結又は個別_実績
	 */
	current_year_duration_annual_member_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_1Q_非連結又は個別_実績
	 */
	current_year_duration_first_quarter_member_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_2Q_非連結又は個別_実績
	 */
	current_year_duration_second_quarter_member_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_3Q_非連結又は個別_実績
	 */
	current_year_duration_third_quarter_member_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_期末_非連結又は個別_実績
	 */
	current_year_duration_year_end_member_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 次年度会計期間_年間_非連結又は個別_予想
	 */
	next_year_duration_annual_member_non_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 次年度会計期間_年間_非連結又は個別_下限
	 */
	next_year_duration_annual_member_non_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 次年度会計期間_年間_非連結又は個別_上限
	 */
	next_year_duration_annual_member_non_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 次年度会計期間_1Q_非連結又は個別_予想
	 */
	next_year_duration_first_quarter_member_non_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 次年度会計期間_1Q_非連結又は個別_下限
	 */
	next_year_duration_first_quarter_member_non_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 次年度会計期間_1Q_非連結又は個別_上限
	 */
	next_year_duration_first_quarter_member_non_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 次年度会計期間_2Q_非連結又は個別_予想
	 */
	next_year_duration_second_quarter_member_non_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 次年度会計期間_2Q_非連結又は個別_下限
	 */
	next_year_duration_second_quarter_member_non_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 次年度会計期間_2Q_非連結又は個別_上限
	 */
	next_year_duration_second_quarter_member_non_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 次年度会計期間_3Q_非連結又は個別_予想
	 */
	next_year_duration_third_quarter_member_non_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 次年度会計期間_3Q_非連結又は個別_下限
	 */
	next_year_duration_third_quarter_member_non_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 次年度会計期間_3Q_非連結又は個別_上限
	 */
	next_year_duration_third_quarter_member_non_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 次年度会計期間_期末_非連結又は個別_予想
	 */
	next_year_duration_year_end_member_non_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 次年度会計期間_期末_非連結又は個別_下限
	 */
	next_year_duration_year_end_member_non_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 次年度会計期間_期末_非連結又は個別_上限
	 */
	next_year_duration_year_end_member_non_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 前年度会計期間_年間_非連結又は個別_実績
	 */
	prior_year_duration_annual_member_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度会計期間_1Q_非連結又は個別_実績
	 */
	prior_year_duration_first_quarter_member_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度会計期間_2Q_非連結又は個別_実績
	 */
	prior_year_duration_second_quarter_member_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度会計期間_3Q_非連結又は個別_実績
	 */
	prior_year_duration_third_quarter_member_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度会計期間_期末_非連結又は個別_実績
	 */
	prior_year_duration_year_end_member_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 1株当たり配当金 
 */
export type DividendPerShare_edjp_FinancialReportSummary_HY_specific_business = {
	/**
	 * 当年度会計期間_年間_非連結又は個別_予想
	 */
	current_year_duration_annual_member_non_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_年間_非連結又は個別_下限
	 */
	current_year_duration_annual_member_non_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_年間_非連結又は個別_上限
	 */
	current_year_duration_annual_member_non_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_1Q_非連結又は個別_実績
	 */
	current_year_duration_first_quarter_member_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_2Q_非連結又は個別_実績
	 */
	current_year_duration_second_quarter_member_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_3Q_非連結又は個別_予想
	 */
	current_year_duration_third_quarter_member_non_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_3Q_非連結又は個別_下限
	 */
	current_year_duration_third_quarter_member_non_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_3Q_非連結又は個別_上限
	 */
	current_year_duration_third_quarter_member_non_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_期末_非連結又は個別_予想
	 */
	current_year_duration_year_end_member_non_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_期末_非連結又は個別_下限
	 */
	current_year_duration_year_end_member_non_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_期末_非連結又は個別_上限
	 */
	current_year_duration_year_end_member_non_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 前年度会計期間_年間_非連結又は個別_実績
	 */
	prior_year_duration_annual_member_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度会計期間_1Q_非連結又は個別_実績
	 */
	prior_year_duration_first_quarter_member_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度会計期間_2Q_非連結又は個別_実績
	 */
	prior_year_duration_second_quarter_member_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度会計期間_3Q_非連結又は個別_実績
	 */
	prior_year_duration_third_quarter_member_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度会計期間_期末_非連結又は個別_実績
	 */
	prior_year_duration_year_end_member_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 1株当たり配当金 
 */
export type DividendPerShare_edjp_FinancialReportSummary_Q1 = {
	/**
	 * 当年度会計期間_年間_非連結又は個別_予想
	 */
	current_year_duration_annual_member_non_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_年間_非連結又は個別_下限
	 */
	current_year_duration_annual_member_non_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_年間_非連結又は個別_上限
	 */
	current_year_duration_annual_member_non_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_1Q_非連結又は個別_実績
	 */
	current_year_duration_first_quarter_member_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_2Q_非連結又は個別_予想
	 */
	current_year_duration_second_quarter_member_non_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_2Q_非連結又は個別_下限
	 */
	current_year_duration_second_quarter_member_non_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_2Q_非連結又は個別_上限
	 */
	current_year_duration_second_quarter_member_non_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_3Q_非連結又は個別_予想
	 */
	current_year_duration_third_quarter_member_non_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_3Q_非連結又は個別_下限
	 */
	current_year_duration_third_quarter_member_non_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_3Q_非連結又は個別_上限
	 */
	current_year_duration_third_quarter_member_non_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_期末_非連結又は個別_予想
	 */
	current_year_duration_year_end_member_non_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_期末_非連結又は個別_下限
	 */
	current_year_duration_year_end_member_non_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_期末_非連結又は個別_上限
	 */
	current_year_duration_year_end_member_non_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 前年度会計期間_年間_非連結又は個別_実績
	 */
	prior_year_duration_annual_member_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度会計期間_1Q_非連結又は個別_実績
	 */
	prior_year_duration_first_quarter_member_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度会計期間_2Q_非連結又は個別_実績
	 */
	prior_year_duration_second_quarter_member_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度会計期間_3Q_非連結又は個別_実績
	 */
	prior_year_duration_third_quarter_member_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度会計期間_期末_非連結又は個別_実績
	 */
	prior_year_duration_year_end_member_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 1株当たり配当金 
 */
export type DividendPerShare_edjp_FinancialReportSummary_Q2 = {
	/**
	 * 当年度会計期間_年間_非連結又は個別_予想
	 */
	current_year_duration_annual_member_non_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_年間_非連結又は個別_下限
	 */
	current_year_duration_annual_member_non_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_年間_非連結又は個別_上限
	 */
	current_year_duration_annual_member_non_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_1Q_非連結又は個別_実績
	 */
	current_year_duration_first_quarter_member_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_2Q_非連結又は個別_実績
	 */
	current_year_duration_second_quarter_member_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_3Q_非連結又は個別_予想
	 */
	current_year_duration_third_quarter_member_non_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_3Q_非連結又は個別_下限
	 */
	current_year_duration_third_quarter_member_non_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_3Q_非連結又は個別_上限
	 */
	current_year_duration_third_quarter_member_non_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_期末_非連結又は個別_予想
	 */
	current_year_duration_year_end_member_non_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_期末_非連結又は個別_下限
	 */
	current_year_duration_year_end_member_non_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_期末_非連結又は個別_上限
	 */
	current_year_duration_year_end_member_non_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 前年度会計期間_年間_非連結又は個別_実績
	 */
	prior_year_duration_annual_member_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度会計期間_1Q_非連結又は個別_実績
	 */
	prior_year_duration_first_quarter_member_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度会計期間_2Q_非連結又は個別_実績
	 */
	prior_year_duration_second_quarter_member_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度会計期間_3Q_非連結又は個別_実績
	 */
	prior_year_duration_third_quarter_member_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度会計期間_期末_非連結又は個別_実績
	 */
	prior_year_duration_year_end_member_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 1株当たり配当金 
 */
export type DividendPerShare_edjp_FinancialReportSummary_Q3 = {
	/**
	 * 当年度会計期間_年間_非連結又は個別_予想
	 */
	current_year_duration_annual_member_non_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_年間_非連結又は個別_下限
	 */
	current_year_duration_annual_member_non_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_年間_非連結又は個別_上限
	 */
	current_year_duration_annual_member_non_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_1Q_非連結又は個別_実績
	 */
	current_year_duration_first_quarter_member_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_2Q_非連結又は個別_実績
	 */
	current_year_duration_second_quarter_member_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_3Q_非連結又は個別_実績
	 */
	current_year_duration_third_quarter_member_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_期末_非連結又は個別_予想
	 */
	current_year_duration_year_end_member_non_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_期末_非連結又は個別_下限
	 */
	current_year_duration_year_end_member_non_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_期末_非連結又は個別_上限
	 */
	current_year_duration_year_end_member_non_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 前年度会計期間_年間_非連結又は個別_実績
	 */
	prior_year_duration_annual_member_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度会計期間_1Q_非連結又は個別_実績
	 */
	prior_year_duration_first_quarter_member_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度会計期間_2Q_非連結又は個別_実績
	 */
	prior_year_duration_second_quarter_member_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度会計期間_3Q_非連結又は個別_実績
	 */
	prior_year_duration_third_quarter_member_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度会計期間_期末_非連結又は個別_実績
	 */
	prior_year_duration_year_end_member_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 特別配当 
 */
export type ExtraDividend_edjp_FinancialReportSummary_Q2 = {
	/**
	 * 当年度期初から第２四半期間_年間_非連結又は個別_実績
	 */
	current_accumulated_q2_duration_annual_member_non_consolidated_member_result_member?: IxNonFractionPublic;
};



export type GroupingNonFraction = {
	report_type: string | null;
	specific_business: boolean | null;
	ixbrl_role: string | null;
	current_period: string | null;
	name: string;
	context: string;
	label: string | null;
	context_label: string | null;
};



export type GroupingNonFractionList = {
	count: number;
	item: Array<GroupingNonFraction>;
};



export type HTTPValidationError = {
	detail?: Array<ValidationError>;
};



/**
 * 持分法投資損益 
 */
export type InvestmentProfitLossOnEquityMethod_edjp_FinancialReportSummary_FY = {
	/**
	 * 当年度会計期間_連結_実績
	 */
	current_year_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_実績
	 */
	current_year_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度会計期間_連結_実績
	 */
	prior_year_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度会計期間_非連結又は個別_実績
	 */
	prior_year_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
};



export type ItemCreate = {
	title: string;
	description?: string | null;
};



export type ItemPublic = {
	title: string;
	description?: string | null;
	id: string;
	owner_id: string;
};



export type ItemUpdate = {
	title?: string | null;
	description?: string | null;
};



export type ItemsPublic = {
	data: Array<ItemPublic>;
	count: number;
};



/**
 * iXBRLの計算アーク情報を表すクラス
 */
export type IxCalculationArcCreate_Input = {
	item_key: string | null;
	head_item_key: string;
	attr_value: string | null;
	xlink_order?: number | string | null;
	xlink_weight?: number | string | null;
	xlink_type: string | null;
	xlink_arcrole: string | null;
	xlink_to?: string | null;
	xlink_from?: string | null;
	source_file_id: string | null;
};



/**
 * iXBRLの計算アーク情報を表すクラス
 */
export type IxCalculationArcCreate_Output = {
	item_key: string | null;
	head_item_key: string;
	attr_value: string | null;
	xlink_order?: string | null;
	xlink_weight?: string | null;
	xlink_type: string | null;
	xlink_arcrole: string | null;
	xlink_to?: string | null;
	xlink_from?: string | null;
	source_file_id: string | null;
};



/**
 * iXBRLの計算アーク情報を作成するためのクラス
 */
export type IxCalculationArcCreateList = {
	data: Array<IxCalculationArcCreate_Input>;
};



/**
 * iXBRLの計算ロケーション情報を表すクラス
 */
export type IxCalculationLocCreate = {
	item_key: string | null;
	head_item_key: string;
	attr_value: string | null;
	xlink_href: string | null;
	xlink_type: string | null;
	xlink_schema: string | null;
	xlink_label?: string | null;
	source_file_id: string | null;
};



/**
 * iXBRLの計算ロケーション情報を作成するためのクラス
 */
export type IxCalculationLocCreateList = {
	data: Array<IxCalculationLocCreate>;
};



/**
 * XBRLの表示リンクアークを表すクラス
 */
export type IxDefinitionArcCreate_Input = {
	item_key: string | null;
	head_item_key: string;
	attr_value: string | null;
	xlink_order: number | string;
	xlink_weight?: number | string | null;
	xlink_type: string | null;
	xlink_arcrole: string | null;
	xlink_to: string;
	xlink_from: string;
	source_file_id: string | null;
};



/**
 * XBRLの表示リンクアークを表すクラス
 */
export type IxDefinitionArcCreate_Output = {
	item_key: string | null;
	head_item_key: string;
	attr_value: string | null;
	xlink_order: string;
	xlink_weight?: string | null;
	xlink_type: string | null;
	xlink_arcrole: string | null;
	xlink_to: string;
	xlink_from: string;
	source_file_id: string | null;
};



/**
 * XBRLの表示リンクアークを作成するためのクラス
 */
export type IxDefinitionArcCreateList = {
	data: Array<IxDefinitionArcCreate_Input>;
};



/**
 * XBRLの表示リンクロケーションを表すクラス
 */
export type IxDefinitionLocCreate = {
	item_key: string | null;
	head_item_key: string;
	attr_value: string | null;
	xlink_href: string | null;
	xlink_type: string | null;
	xlink_schema: string | null;
	xlink_label?: string | null;
	source_file_id: string | null;
};



/**
 * XBRLの表示リンクロケーションを作成するためのクラス
 */
export type IxDefinitionLocCreateList = {
	data: Array<IxDefinitionLocCreate>;
};



/**
 * iXBRLのファイルパス情報を作成するためのクラス
 */
export type IxFilePathCreate = {
	item_key: string | null;
	path?: string;
	head_item_key: string | null;
};



/**
 * iXBRLのファイルパス情報を公開するためのクラス
 */
export type IxFilePathPublic = {
	path: string;
	head_item_key: string;
};



/**
 * iXBRLのヘッダー情報を表すクラス
 */
export type IxHeadTitleCreate = {
	item_key: string;
	company_name?: string | null;
	securities_code?: string | null;
	document_name?: string | null;
	reporting_date?: string | null;
	current_period?: string | null;
	report_type?: string | null;
	listed_market?: string | null;
	market_section?: string | null;
	url?: string | null;
	is_bs?: boolean | null;
	is_pl?: boolean | null;
	is_cf?: boolean | null;
	is_ci?: boolean | null;
	is_sce?: boolean | null;
	is_sfp?: boolean | null;
	fy_year_end?: string | null;
	tel?: string | null;
	specific_business?: boolean | null;
};



/**
 * iXBRLのヘッダー情報のリストを表すクラス
 */
export type IxHeadTitleCreateList = {
	data: Array<IxHeadTitleCreate>;
};



/**
 * iXBRLのヘッダー情報を表すクラス
 */
export type IxHeadTitlePublic = {
	item_key: string;
	company_name: string | null;
	securities_code: string | null;
	document_name: string | null;
	reporting_date: string | null;
	current_period: string | null;
	report_type: string | null;
	listed_market: string | null;
	market_section: string | null;
	url: string | null;
	is_bs: boolean | null;
	is_pl: boolean | null;
	is_cf: boolean | null;
	is_ci: boolean | null;
	is_sce: boolean | null;
	is_sfp: boolean | null;
	fy_year_end: string | null;
	tel: string | null;
	is_div_rev: boolean | null;
	div_inc_rt: string | null;
	is_fcst_rev: boolean | null;
	fcst_oi_gr_rt: string | null;
	oi_prog_rt: number | null;
	specific_business: boolean | null;
};



/**
 * iXBRLのヘッダー情報のリストを表すクラス
 */
export type IxHeadTitlesPublic = {
	data: Array<IxHeadTitlePublic>;
	count: number;
};



/**
 * iXBRLのラベルアーク情報を作成するためのクラス
 */
export type IxLabelArcCreate = {
	item_key: string | null;
	xlink_type: string;
	xlink_arcrole: string;
	xlink_from?: string;
	xlink_to?: string;
	source_file_id: string;
};



/**
 * iXBRLの計算アーク情報を作成するためのクラス
 */
export type IxLabelArcCreateList = {
	data: Array<IxLabelArcCreate>;
};



/**
 * iXBRLのラベルロケーション情報を作成するためのクラス
 */
export type IxLabelLocCreate = {
	item_key: string | null;
	xlink_href?: string;
	xlink_label?: string;
	xlink_type: string;
	xlink_schema: string;
	source_file_id: string;
};



/**
 * iXBRLのラベルロケーション情報を作成するためのクラス
 */
export type IxLabelLocCreateList = {
	data: Array<IxLabelLocCreate>;
};



/**
 * iXBRLのラベルリンク情報を作成するためのクラス
 */
export type IxLabelValueCreate = {
	item_key: string | null;
	xlink_type: string;
	xlink_label?: string;
	xlink_role: string;
	xml_lang: string;
	label?: string;
	source_file_id: string;
};



/**
 * iXBRLのラベルリンク情報を作成するためのクラス
 */
export type IxLabelValueCreateList = {
	data: Array<IxLabelValueCreate>;
};



/**
 * iXBRLの非分数情報を表すクラス
 */
export type IxNonFractionCreate_Input = {
	item_key: string | null;
	head_item_key: string;
	context: string;
	decimals?: number | string | null;
	format: string | null;
	name?: string;
	scale?: number | string | null;
	sign?: string | null;
	unit_ref: string;
	xsi_nil?: boolean | null;
	numeric?: number | string | null;
	report_type: string | null;
	ixbrl_role: string | null;
	source_file_id: string | null;
	xbrl_type: string;
	display_numeric: string | null;
	display_scale: string | null;
};



/**
 * iXBRLの非分数情報を表すクラス
 */
export type IxNonFractionCreate_Output = {
	item_key: string | null;
	head_item_key: string;
	context: string;
	decimals?: string | null;
	format: string | null;
	name?: string;
	scale?: string | null;
	sign?: string | null;
	unit_ref: string;
	xsi_nil?: boolean | null;
	numeric?: string | null;
	report_type: string | null;
	ixbrl_role: string | null;
	source_file_id: string | null;
	xbrl_type: string;
	display_numeric: string | null;
	display_scale: string | null;
};



/**
 * iXBRLの非分数情報を作成するためのクラス
 */
export type IxNonFractionCreateList = {
	data: Array<IxNonFractionCreate_Input>;
};



/**
 * iXBRLの非分数情報を表すクラス
 */
export type IxNonFractionPublic = {
	id: number | null;
	insert_date: string;
	update_date: string;
	head_item_key: string | null;
	context: string;
	decimals: string | null;
	format: string | null;
	name: string;
	scale: string | null;
	sign: string | null;
	unit_ref: string | null;
	xsi_nil: boolean | null;
	numeric: string | null;
	report_type: string | null;
	ixbrl_role: string | null;
	source_file_id: string | null;
	xbrl_type: string | null;
	display_numeric: string | null;
	display_scale: string | null;
};



/**
 * iXBRLの非数値情報を表すクラス
 */
export type IxNonNumericCreate = {
	item_key: string | null;
	head_item_key: string;
	context: string | null;
	name?: string;
	xsi_nil?: boolean | null;
	escape?: boolean;
	format?: string | null;
	value?: string | null;
	report_type: string | null;
	ixbrl_role: string | null;
	source_file_id: string | null;
	xbrl_type: string;
};



/**
 * iXBRLの非数値情報を作成するためのクラス
 */
export type IxNonNumericCreateList = {
	data: Array<IxNonNumericCreate>;
};



/**
 * XBRLの表示リンクアークを表すクラス
 */
export type IxPresentationArcCreate_Input = {
	item_key: string | null;
	head_item_key: string;
	attr_value: string | null;
	xlink_order?: number | string | null;
	xlink_weight?: number | string | null;
	xlink_type: string | null;
	xlink_arcrole: string | null;
	xlink_to?: string | null;
	xlink_from?: string | null;
	source_file_id: string | null;
};



/**
 * XBRLの表示リンクアークを表すクラス
 */
export type IxPresentationArcCreate_Output = {
	item_key: string | null;
	head_item_key: string;
	attr_value: string | null;
	xlink_order?: string | null;
	xlink_weight?: string | null;
	xlink_type: string | null;
	xlink_arcrole: string | null;
	xlink_to?: string | null;
	xlink_from?: string | null;
	source_file_id: string | null;
};



/**
 * XBRLの表示リンクアークを作成するためのクラス
 */
export type IxPresentationArcCreateList = {
	data: Array<IxPresentationArcCreate_Input>;
};



/**
 * XBRLの表示リンクロケーションを表すクラス
 */
export type IxPresentationLocCreate = {
	item_key: string | null;
	head_item_key: string;
	attr_value: string | null;
	xlink_href: string | null;
	xlink_type: string | null;
	xlink_schema: string | null;
	xlink_label?: string | null;
	source_file_id: string | null;
};



/**
 * XBRLの表示リンクロケーションを作成するためのクラス
 */
export type IxPresentationLocCreateList = {
	data: Array<IxPresentationLocCreate>;
};



/**
 * 定性的情報を登録するためのモデル
 */
export type IxQualitativeCreate = {
	/**
	 * ID
	 */
	item_key?: string | null;
	/**
	 * 現在のID
	 */
	currentId?: string;
	/**
	 * 親ID
	 */
	parentId?: string | null;
	/**
	 * タイプ
	 */
	type?: string | null;
	/**
	 * 内容
	 */
	content?: string | null;
	/**
	 * 順序
	 */
	order?: number | null;
	/**
	 * XBRL-ID
	 */
	head_item_key?: string | null;
	/**
	 * ソースファイルID
	 */
	source_file_id?: string | null;
	/**
	 * 写真URL
	 */
	photo_url?: string | null;
};



/**
 * 複数の定性的情報を登録するためのモデル
 */
export type IxQualitativeCreates = {
	data: Array<IxQualitativeCreate>;
};



/**
 * 定性的情報を取得するためのモデル
 */
export type IxQualitativePublic = {
	currentId: string;
	parentId: string | null;
	type: string | null;
	content: string | null;
	order: number | null;
	head_item_key: string | null;
	photo_url: string | null;
};



/**
 * 複数の定性的情報を取得するためのモデル
 */
export type IxQualitativePublics = {
	count: number;
	data: Array<IxQualitativePublic>;
};



/**
 * 報告書タイプのカウントを表すクラス
 */
export type IxReportTypeCount = {
	report_type: string;
	report_type_jp: string;
	count: number;
};



/**
 * 報告書タイプのカウントのリストを表すクラス
 */
export type IxReportTypeCountList = {
	data: Array<IxReportTypeCount>;
	count: number;
};



/**
 * iXBRLのスキーマリンクベース情報を作成するためのクラス
 */
export type IxSchemaLinkBaseCreate = {
	item_key: string | null;
	head_item_key: string;
	xlink_arcrole: string | null;
	xlink_href: string | null;
	xlink_role: string | null;
	xlink_type: string | null;
	source_file_id: string | null;
	xbrl_type: string | null;
	href_source_file_id: string | null;
};



/**
 * iXBRLのスキーマリンクベース情報を作成するためのクラス
 */
export type IxSchemaLinkBaseCreateList = {
	data: Array<IxSchemaLinkBaseCreate>;
};



/**
 * iXBRLのソースファイル情報を作成するためのクラス
 */
export type IxSourceFileCreate = {
	id: string | null;
	item_key: string | null;
	name: string;
	type: string;
	head_item_key: string | null;
	url: string | null;
};



/**
 * iXBRLのソースファイル情報を作成するためのクラス
 */
export type IxSourceFileCreateList = {
	data: Array<IxSourceFileCreate>;
};



export type Message = {
	message: string;
};



/**
 * 1株当たり純資産 
 */
export type NetAssetsPerShare_edjp_FinancialReportSummary = {
	/**
	 * 当年度期初から第２四半期間時点_連結_実績
	 */
	current_accumulated_q2_instant_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度時点_連結_実績
	 */
	prior_year_instant_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 1株当たり純資産 
 */
export type NetAssetsPerShare_edjp_FinancialReportSummary_FY = {
	/**
	 * 当年度時点_連結_実績
	 */
	current_year_instant_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度時点_非連結又は個別_実績
	 */
	current_year_instant_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度時点_連結_実績
	 */
	prior_year_instant_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度時点_非連結又は個別_実績
	 */
	prior_year_instant_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 1株当たり純資産 
 */
export type NetAssetsPerShare_edjp_FinancialReportSummary_HY_specific_business = {
	/**
	 * 当年度期初から第２四半期間時点_連結_実績
	 */
	current_accumulated_q2_instant_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度期初から第２四半期間時点_非連結又は個別_実績
	 */
	current_accumulated_q2_instant_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度時点_連結_実績
	 */
	prior_year_instant_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度時点_非連結又は個別_実績
	 */
	prior_year_instant_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 1株当たり純資産 
 */
export type NetAssetsPerShare_edjp_FinancialReportSummary_Q1 = {
	/**
	 * 当年度期初から第１四半期間時点_連結_実績
	 */
	current_accumulated_q1_instant_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度期初から第１四半期間時点_非連結又は個別_実績
	 */
	current_accumulated_q1_instant_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度時点_連結_実績
	 */
	prior_year_instant_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度時点_非連結又は個別_実績
	 */
	prior_year_instant_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 1株当たり純資産 
 */
export type NetAssetsPerShare_edjp_FinancialReportSummary_Q2 = {
	/**
	 * 当年度期初から第２四半期間時点_連結_実績
	 */
	current_accumulated_q2_instant_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度期初から第２四半期間時点_非連結又は個別_実績
	 */
	current_accumulated_q2_instant_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度時点_連結_実績
	 */
	prior_year_instant_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度時点_非連結又は個別_実績
	 */
	prior_year_instant_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 1株当たり純資産 
 */
export type NetAssetsPerShare_edjp_FinancialReportSummary_Q3 = {
	/**
	 * 当年度期初から第３四半期間時点_連結_実績
	 */
	current_accumulated_q3_instant_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度時点_連結_実績
	 */
	prior_year_instant_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 純資産 
 */
export type NetAssets_edjp_FinancialReportSummary = {
	/**
	 * 当年度期初から第２四半期間時点_連結_実績
	 */
	current_accumulated_q2_instant_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度時点_連結_実績
	 */
	prior_year_instant_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 純資産 
 */
export type NetAssets_edjp_FinancialReportSummary_FY = {
	/**
	 * 当年度時点_連結_実績
	 */
	current_year_instant_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度時点_非連結又は個別_実績
	 */
	current_year_instant_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度時点_連結_実績
	 */
	prior_year_instant_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度時点_非連結又は個別_実績
	 */
	prior_year_instant_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 純資産 
 */
export type NetAssets_edjp_FinancialReportSummary_HY_specific_business = {
	/**
	 * 当年度期初から第２四半期間時点_連結_実績
	 */
	current_accumulated_q2_instant_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度期初から第２四半期間時点_非連結又は個別_実績
	 */
	current_accumulated_q2_instant_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度時点_連結_実績
	 */
	prior_year_instant_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度時点_非連結又は個別_実績
	 */
	prior_year_instant_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 純資産 
 */
export type NetAssets_edjp_FinancialReportSummary_Q1 = {
	/**
	 * 当年度期初から第１四半期間時点_連結_実績
	 */
	current_accumulated_q1_instant_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度期初から第１四半期間時点_非連結又は個別_実績
	 */
	current_accumulated_q1_instant_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度時点_連結_実績
	 */
	prior_year_instant_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度時点_非連結又は個別_実績
	 */
	prior_year_instant_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 純資産 
 */
export type NetAssets_edjp_FinancialReportSummary_Q2 = {
	/**
	 * 当年度期初から第２四半期間時点_連結_実績
	 */
	current_accumulated_q2_instant_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度期初から第２四半期間時点_非連結又は個別_実績
	 */
	current_accumulated_q2_instant_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度時点_連結_実績
	 */
	prior_year_instant_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度時点_非連結又は個別_実績
	 */
	prior_year_instant_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 純資産 
 */
export type NetAssets_edjp_FinancialReportSummary_Q3 = {
	/**
	 * 当年度期初から第３四半期間時点_連結_実績
	 */
	current_accumulated_q3_instant_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度時点_連結_実績
	 */
	prior_year_instant_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 1株当たり当期純利益 
 */
export type NetIncomePerShare_edjp_FinancialReportSummary = {
	/**
	 * 当年度期初から第２四半期間_連結_実績
	 */
	current_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_予想
	 */
	current_year_duration_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_下限
	 */
	current_year_duration_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_上限
	 */
	current_year_duration_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第２四半期間_連結_実績
	 */
	prior_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 1株当たり当期純利益 
 */
export type NetIncomePerShare_edjp_FinancialReportSummary_FY = {
	/**
	 * 当年度会計期間_連結_実績
	 */
	current_year_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_実績
	 */
	current_year_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 次年度期初から第２四半期間_非連結又は個別_予想
	 */
	next_accumulated_q2_duration_non_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 次年度期初から第２四半期間_非連結又は個別_下限
	 */
	next_accumulated_q2_duration_non_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 次年度期初から第２四半期間_非連結又は個別_上限
	 */
	next_accumulated_q2_duration_non_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 次年度会計期間_連結_予想
	 */
	next_year_duration_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 次年度会計期間_連結_下限
	 */
	next_year_duration_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 次年度会計期間_連結_上限
	 */
	next_year_duration_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 次年度会計期間_非連結又は個別_予想
	 */
	next_year_duration_non_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 次年度会計期間_非連結又は個別_下限
	 */
	next_year_duration_non_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 次年度会計期間_非連結又は個別_上限
	 */
	next_year_duration_non_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 前年度会計期間_連結_実績
	 */
	prior_year_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度会計期間_非連結又は個別_実績
	 */
	prior_year_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 1株当たり当期純利益 
 */
export type NetIncomePerShare_edjp_FinancialReportSummary_HY_specific_business = {
	/**
	 * 当年度期初から第２四半期間_連結_実績
	 */
	current_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度期初から第２四半期間_非連結又は個別_実績
	 */
	current_accumulated_q2_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_予想
	 */
	current_year_duration_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_下限
	 */
	current_year_duration_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_上限
	 */
	current_year_duration_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_予想
	 */
	current_year_duration_non_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_下限
	 */
	current_year_duration_non_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_上限
	 */
	current_year_duration_non_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第２四半期間_連結_実績
	 */
	prior_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第２四半期間_非連結又は個別_実績
	 */
	prior_accumulated_q2_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 1株当たり当期純利益 
 */
export type NetIncomePerShare_edjp_FinancialReportSummary_Q1 = {
	/**
	 * 当年度期初から第１四半期間_連結_実績
	 */
	current_accumulated_q1_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度期初から第１四半期間_非連結又は個別_実績
	 */
	current_accumulated_q1_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度期初から第２四半期間_非連結又は個別_予想
	 */
	current_accumulated_q2_duration_non_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度期初から第２四半期間_非連結又は個別_下限
	 */
	current_accumulated_q2_duration_non_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度期初から第２四半期間_非連結又は個別_上限
	 */
	current_accumulated_q2_duration_non_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_予想
	 */
	current_year_duration_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_下限
	 */
	current_year_duration_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_上限
	 */
	current_year_duration_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_予想
	 */
	current_year_duration_non_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_下限
	 */
	current_year_duration_non_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_上限
	 */
	current_year_duration_non_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第１四半期間_連結_実績
	 */
	prior_accumulated_q1_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第１四半期間_非連結又は個別_実績
	 */
	prior_accumulated_q1_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 1株当たり当期純利益 
 */
export type NetIncomePerShare_edjp_FinancialReportSummary_Q2 = {
	/**
	 * 当年度期初から第２四半期間_連結_実績
	 */
	current_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度期初から第２四半期間_非連結又は個別_実績
	 */
	current_accumulated_q2_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_予想
	 */
	current_year_duration_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_下限
	 */
	current_year_duration_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_上限
	 */
	current_year_duration_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_予想
	 */
	current_year_duration_non_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_下限
	 */
	current_year_duration_non_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_上限
	 */
	current_year_duration_non_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第２四半期間_連結_実績
	 */
	prior_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第２四半期間_非連結又は個別_実績
	 */
	prior_accumulated_q2_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 1株当たり当期純利益 
 */
export type NetIncomePerShare_edjp_FinancialReportSummary_Q3 = {
	/**
	 * 当年度期初から第３四半期間_連結_実績
	 */
	current_accumulated_q3_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_予想
	 */
	current_year_duration_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_下限
	 */
	current_year_duration_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_上限
	 */
	current_year_duration_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第３四半期間_連結_実績
	 */
	prior_accumulated_q3_duration_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 自己資本当期純利益率 
 */
export type NetIncomeToShareholdersEquityRatio_edjp_FinancialReportSummary_FY = {
	/**
	 * 当年度会計期間_連結_実績
	 */
	current_year_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_実績
	 */
	current_year_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度会計期間_連結_実績
	 */
	prior_year_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度会計期間_非連結又は個別_実績
	 */
	prior_year_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 当期純利益 
 */
export type NetIncome_edjp_FinancialReportSummary_FY = {
	/**
	 * 当年度会計期間_非連結又は個別_実績
	 */
	current_year_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 次年度期初から第２四半期間_非連結又は個別_予想
	 */
	next_accumulated_q2_duration_non_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 次年度期初から第２四半期間_非連結又は個別_下限
	 */
	next_accumulated_q2_duration_non_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 次年度期初から第２四半期間_非連結又は個別_上限
	 */
	next_accumulated_q2_duration_non_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 次年度会計期間_非連結又は個別_予想
	 */
	next_year_duration_non_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 次年度会計期間_非連結又は個別_下限
	 */
	next_year_duration_non_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 次年度会計期間_非連結又は個別_上限
	 */
	next_year_duration_non_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 前年度会計期間_非連結又は個別_実績
	 */
	prior_year_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 当期純利益 
 */
export type NetIncome_edjp_FinancialReportSummary_HY_specific_business = {
	/**
	 * 当年度期初から第２四半期間_非連結又は個別_実績
	 */
	current_accumulated_q2_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_予想
	 */
	current_year_duration_non_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_下限
	 */
	current_year_duration_non_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_上限
	 */
	current_year_duration_non_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第２四半期間_非連結又は個別_実績
	 */
	prior_accumulated_q2_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 当期純利益 
 */
export type NetIncome_edjp_FinancialReportSummary_Q1 = {
	/**
	 * 当年度期初から第１四半期間_非連結又は個別_実績
	 */
	current_accumulated_q1_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度期初から第２四半期間_非連結又は個別_予想
	 */
	current_accumulated_q2_duration_non_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度期初から第２四半期間_非連結又は個別_下限
	 */
	current_accumulated_q2_duration_non_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度期初から第２四半期間_非連結又は個別_上限
	 */
	current_accumulated_q2_duration_non_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_予想
	 */
	current_year_duration_non_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_下限
	 */
	current_year_duration_non_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_上限
	 */
	current_year_duration_non_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第１四半期間_非連結又は個別_実績
	 */
	prior_accumulated_q1_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 当期純利益 
 */
export type NetIncome_edjp_FinancialReportSummary_Q2 = {
	/**
	 * 当年度期初から第２四半期間_非連結又は個別_実績
	 */
	current_accumulated_q2_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_予想
	 */
	current_year_duration_non_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_下限
	 */
	current_year_duration_non_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_上限
	 */
	current_year_duration_non_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第２四半期間_非連結又は個別_実績
	 */
	prior_accumulated_q2_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 純営業収益、証券 
 */
export type NetOperatingRevenuesSE_edjp_FinancialReportSummary_Q2 = {
	/**
	 * 当年度期初から第２四半期間_連結_実績
	 */
	current_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度期初から第２四半期間_非連結又は個別_実績
	 */
	current_accumulated_q2_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第２四半期間_連結_実績
	 */
	prior_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第２四半期間_非連結又は個別_実績
	 */
	prior_accumulated_q2_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 売上高 
 */
export type NetSales_edjp_FinancialReportSummary = {
	/**
	 * 当年度期初から第２四半期間_連結_実績
	 */
	current_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_予想
	 */
	current_year_duration_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_下限
	 */
	current_year_duration_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_上限
	 */
	current_year_duration_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第２四半期間_連結_実績
	 */
	prior_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 売上高 
 */
export type NetSales_edjp_FinancialReportSummary_FY = {
	/**
	 * 当年度会計期間_連結_実績
	 */
	current_year_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_実績
	 */
	current_year_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 次年度期初から第２四半期間_非連結又は個別_予想
	 */
	next_accumulated_q2_duration_non_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 次年度期初から第２四半期間_非連結又は個別_下限
	 */
	next_accumulated_q2_duration_non_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 次年度期初から第２四半期間_非連結又は個別_上限
	 */
	next_accumulated_q2_duration_non_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 次年度会計期間_連結_予想
	 */
	next_year_duration_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 次年度会計期間_連結_下限
	 */
	next_year_duration_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 次年度会計期間_連結_上限
	 */
	next_year_duration_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 次年度会計期間_非連結又は個別_予想
	 */
	next_year_duration_non_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 次年度会計期間_非連結又は個別_下限
	 */
	next_year_duration_non_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 次年度会計期間_非連結又は個別_上限
	 */
	next_year_duration_non_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 前年度会計期間_連結_実績
	 */
	prior_year_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度会計期間_非連結又は個別_実績
	 */
	prior_year_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 売上高 
 */
export type NetSales_edjp_FinancialReportSummary_Q1 = {
	/**
	 * 当年度期初から第１四半期間_連結_実績
	 */
	current_accumulated_q1_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度期初から第１四半期間_非連結又は個別_実績
	 */
	current_accumulated_q1_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度期初から第２四半期間_非連結又は個別_予想
	 */
	current_accumulated_q2_duration_non_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度期初から第２四半期間_非連結又は個別_下限
	 */
	current_accumulated_q2_duration_non_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度期初から第２四半期間_非連結又は個別_上限
	 */
	current_accumulated_q2_duration_non_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_予想
	 */
	current_year_duration_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_下限
	 */
	current_year_duration_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_上限
	 */
	current_year_duration_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_予想
	 */
	current_year_duration_non_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_下限
	 */
	current_year_duration_non_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_上限
	 */
	current_year_duration_non_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第１四半期間_連結_実績
	 */
	prior_accumulated_q1_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第１四半期間_非連結又は個別_実績
	 */
	prior_accumulated_q1_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 売上高 
 */
export type NetSales_edjp_FinancialReportSummary_Q2 = {
	/**
	 * 当年度期初から第２四半期間_連結_実績
	 */
	current_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度期初から第２四半期間_非連結又は個別_実績
	 */
	current_accumulated_q2_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_予想
	 */
	current_year_duration_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_下限
	 */
	current_year_duration_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_上限
	 */
	current_year_duration_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_予想
	 */
	current_year_duration_non_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_下限
	 */
	current_year_duration_non_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_上限
	 */
	current_year_duration_non_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第２四半期間_連結_実績
	 */
	prior_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第２四半期間_非連結又は個別_実績
	 */
	prior_accumulated_q2_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 売上高 
 */
export type NetSales_edjp_FinancialReportSummary_Q3 = {
	/**
	 * 当年度期初から第３四半期間_連結_実績
	 */
	current_accumulated_q3_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_予想
	 */
	current_year_duration_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_下限
	 */
	current_year_duration_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_上限
	 */
	current_year_duration_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第３四半期間_連結_実績
	 */
	prior_accumulated_q3_duration_consolidated_member_result_member?: IxNonFractionPublic;
};



export type NewPassword = {
	token: string;
	new_password: string;
};



/**
 * 期末発行済株式数（自己株式を含む） 
 */
export type NumberOfIssuedAndOutstandingSharesAtTheEndOfFiscalYearIncludingTreasuryStock_edjp_FinancialReportSummary = {
	/**
	 * 当年度期初から第２四半期間時点_非連結又は個別_実績
	 */
	current_accumulated_q2_instant_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度時点_非連結又は個別_実績
	 */
	prior_year_instant_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 期末発行済株式数（自己株式を含む） 
 */
export type NumberOfIssuedAndOutstandingSharesAtTheEndOfFiscalYearIncludingTreasuryStock_edjp_FinancialReportSummary_FY = {
	/**
	 * 当年度時点_非連結又は個別_実績
	 */
	current_year_instant_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度時点_非連結又は個別_実績
	 */
	prior_year_instant_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 期末発行済株式数（自己株式を含む） 
 */
export type NumberOfIssuedAndOutstandingSharesAtTheEndOfFiscalYearIncludingTreasuryStock_edjp_FinancialReportSummary_HY_specific_business = {
	/**
	 * 当年度期初から第２四半期間時点_非連結又は個別_実績
	 */
	current_accumulated_q2_instant_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度時点_非連結又は個別_実績
	 */
	prior_year_instant_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 期末発行済株式数（自己株式を含む） 
 */
export type NumberOfIssuedAndOutstandingSharesAtTheEndOfFiscalYearIncludingTreasuryStock_edjp_FinancialReportSummary_Q1 = {
	/**
	 * 当年度期初から第１四半期間時点_非連結又は個別_実績
	 */
	current_accumulated_q1_instant_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度時点_非連結又は個別_実績
	 */
	prior_year_instant_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 期末発行済株式数（自己株式を含む） 
 */
export type NumberOfIssuedAndOutstandingSharesAtTheEndOfFiscalYearIncludingTreasuryStock_edjp_FinancialReportSummary_Q2 = {
	/**
	 * 当年度期初から第２四半期間時点_非連結又は個別_実績
	 */
	current_accumulated_q2_instant_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度時点_非連結又は個別_実績
	 */
	prior_year_instant_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 期末発行済株式数（自己株式を含む） 
 */
export type NumberOfIssuedAndOutstandingSharesAtTheEndOfFiscalYearIncludingTreasuryStock_edjp_FinancialReportSummary_Q3 = {
	/**
	 * 当年度期初から第３四半期間時点_非連結又は個別_実績
	 */
	current_accumulated_q3_instant_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度時点_非連結又は個別_実績
	 */
	prior_year_instant_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 除外 
 */
export type NumberOfSubsidiariesExcludedFromConsolidation_edjp_FinancialReportSummary_FY = {
	/**
	 * 当年度会計期間_連結_実績
	 */
	current_year_duration_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 除外 
 */
export type NumberOfSubsidiariesExcludedFromConsolidation_edjp_FinancialReportSummary_Q1 = {
	/**
	 * 当年度期初から第１四半期間_連結_実績
	 */
	current_accumulated_q1_duration_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 除外 
 */
export type NumberOfSubsidiariesExcludedFromConsolidation_edjp_FinancialReportSummary_Q2 = {
	/**
	 * 当年度期初から第２四半期間_連結_実績
	 */
	current_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 除外 
 */
export type NumberOfSubsidiariesExcludedFromConsolidation_edjp_FinancialReportSummary_Q3 = {
	/**
	 * 当年度期初から第３四半期間_連結_実績
	 */
	current_accumulated_q3_duration_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 新規 
 */
export type NumberOfSubsidiariesNewlyConsolidated_edjp_FinancialReportSummary_FY = {
	/**
	 * 当年度会計期間_連結_実績
	 */
	current_year_duration_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 新規 
 */
export type NumberOfSubsidiariesNewlyConsolidated_edjp_FinancialReportSummary_Q1 = {
	/**
	 * 当年度期初から第１四半期間_連結_実績
	 */
	current_accumulated_q1_duration_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 新規 
 */
export type NumberOfSubsidiariesNewlyConsolidated_edjp_FinancialReportSummary_Q2 = {
	/**
	 * 当年度期初から第２四半期間_連結_実績
	 */
	current_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 新規 
 */
export type NumberOfSubsidiariesNewlyConsolidated_edjp_FinancialReportSummary_Q3 = {
	/**
	 * 当年度期初から第３四半期間_連結_実績
	 */
	current_accumulated_q3_duration_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 期末自己株式数 
 */
export type NumberOfTreasuryStockAtTheEndOfFiscalYear_edjp_FinancialReportSummary = {
	/**
	 * 当年度期初から第２四半期間時点_非連結又は個別_実績
	 */
	current_accumulated_q2_instant_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度時点_非連結又は個別_実績
	 */
	prior_year_instant_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 期末自己株式数 
 */
export type NumberOfTreasuryStockAtTheEndOfFiscalYear_edjp_FinancialReportSummary_FY = {
	/**
	 * 当年度時点_非連結又は個別_実績
	 */
	current_year_instant_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度時点_非連結又は個別_実績
	 */
	prior_year_instant_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 期末自己株式数 
 */
export type NumberOfTreasuryStockAtTheEndOfFiscalYear_edjp_FinancialReportSummary_HY_specific_business = {
	/**
	 * 当年度期初から第２四半期間時点_非連結又は個別_実績
	 */
	current_accumulated_q2_instant_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度時点_非連結又は個別_実績
	 */
	prior_year_instant_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 期末自己株式数 
 */
export type NumberOfTreasuryStockAtTheEndOfFiscalYear_edjp_FinancialReportSummary_Q1 = {
	/**
	 * 当年度期初から第１四半期間時点_非連結又は個別_実績
	 */
	current_accumulated_q1_instant_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度時点_非連結又は個別_実績
	 */
	prior_year_instant_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 期末自己株式数 
 */
export type NumberOfTreasuryStockAtTheEndOfFiscalYear_edjp_FinancialReportSummary_Q2 = {
	/**
	 * 当年度期初から第２四半期間時点_非連結又は個別_実績
	 */
	current_accumulated_q2_instant_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度時点_非連結又は個別_実績
	 */
	prior_year_instant_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 期末自己株式数 
 */
export type NumberOfTreasuryStockAtTheEndOfFiscalYear_edjp_FinancialReportSummary_Q3 = {
	/**
	 * 当年度期初から第３四半期間時点_非連結又は個別_実績
	 */
	current_accumulated_q3_instant_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度時点_非連結又は個別_実績
	 */
	prior_year_instant_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 売上高営業利益率 
 */
export type OperatingIncomeToNetSalesRatio_edjp_FinancialReportSummary_FY = {
	/**
	 * 当年度会計期間_連結_実績
	 */
	current_year_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_実績
	 */
	current_year_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度会計期間_連結_実績
	 */
	prior_year_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度会計期間_非連結又は個別_実績
	 */
	prior_year_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 営業利益 
 */
export type OperatingIncome_edjp_FinancialReportSummary = {
	/**
	 * 当年度期初から第２四半期間_連結_実績
	 */
	current_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_予想
	 */
	current_year_duration_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_下限
	 */
	current_year_duration_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_上限
	 */
	current_year_duration_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第２四半期間_連結_実績
	 */
	prior_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 営業利益 
 */
export type OperatingIncome_edjp_FinancialReportSummary_FY = {
	/**
	 * 当年度会計期間_連結_実績
	 */
	current_year_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_実績
	 */
	current_year_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 次年度期初から第２四半期間_非連結又は個別_予想
	 */
	next_accumulated_q2_duration_non_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 次年度期初から第２四半期間_非連結又は個別_下限
	 */
	next_accumulated_q2_duration_non_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 次年度期初から第２四半期間_非連結又は個別_上限
	 */
	next_accumulated_q2_duration_non_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 次年度会計期間_連結_予想
	 */
	next_year_duration_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 次年度会計期間_連結_下限
	 */
	next_year_duration_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 次年度会計期間_連結_上限
	 */
	next_year_duration_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 次年度会計期間_非連結又は個別_予想
	 */
	next_year_duration_non_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 次年度会計期間_非連結又は個別_下限
	 */
	next_year_duration_non_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 次年度会計期間_非連結又は個別_上限
	 */
	next_year_duration_non_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 前年度会計期間_連結_実績
	 */
	prior_year_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度会計期間_非連結又は個別_実績
	 */
	prior_year_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 営業利益 
 */
export type OperatingIncome_edjp_FinancialReportSummary_Q1 = {
	/**
	 * 当年度期初から第１四半期間_連結_実績
	 */
	current_accumulated_q1_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度期初から第１四半期間_非連結又は個別_実績
	 */
	current_accumulated_q1_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度期初から第２四半期間_非連結又は個別_予想
	 */
	current_accumulated_q2_duration_non_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度期初から第２四半期間_非連結又は個別_下限
	 */
	current_accumulated_q2_duration_non_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度期初から第２四半期間_非連結又は個別_上限
	 */
	current_accumulated_q2_duration_non_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_予想
	 */
	current_year_duration_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_下限
	 */
	current_year_duration_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_上限
	 */
	current_year_duration_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_予想
	 */
	current_year_duration_non_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_下限
	 */
	current_year_duration_non_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_上限
	 */
	current_year_duration_non_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第１四半期間_連結_実績
	 */
	prior_accumulated_q1_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第１四半期間_非連結又は個別_実績
	 */
	prior_accumulated_q1_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 営業利益 
 */
export type OperatingIncome_edjp_FinancialReportSummary_Q2 = {
	/**
	 * 当年度期初から第２四半期間_連結_実績
	 */
	current_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度期初から第２四半期間_非連結又は個別_実績
	 */
	current_accumulated_q2_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_予想
	 */
	current_year_duration_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_下限
	 */
	current_year_duration_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_上限
	 */
	current_year_duration_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_予想
	 */
	current_year_duration_non_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_下限
	 */
	current_year_duration_non_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_上限
	 */
	current_year_duration_non_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第２四半期間_連結_実績
	 */
	prior_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第２四半期間_非連結又は個別_実績
	 */
	prior_accumulated_q2_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 営業利益 
 */
export type OperatingIncome_edjp_FinancialReportSummary_Q3 = {
	/**
	 * 当年度期初から第３四半期間_連結_実績
	 */
	current_accumulated_q3_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_予想
	 */
	current_year_duration_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_下限
	 */
	current_year_duration_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_上限
	 */
	current_year_duration_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第３四半期間_連結_実績
	 */
	prior_accumulated_q3_duration_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 営業収益、証券 
 */
export type OperatingRevenuesSE_edjp_FinancialReportSummary_Q2 = {
	/**
	 * 当年度期初から第２四半期間_連結_実績
	 */
	current_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第２四半期間_連結_実績
	 */
	prior_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 営業収益 
 */
export type OperatingRevenues_edjp_FinancialReportSummary_Q2 = {
	/**
	 * 当年度期初から第２四半期間_連結_実績
	 */
	current_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度期初から第２四半期間_非連結又は個別_実績
	 */
	current_accumulated_q2_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_予想
	 */
	current_year_duration_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_下限
	 */
	current_year_duration_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_上限
	 */
	current_year_duration_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第２四半期間_連結_実績
	 */
	prior_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第２四半期間_非連結又は個別_実績
	 */
	prior_accumulated_q2_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 総資産経常利益率 
 */
export type OrdinaryIncomeToTotalAssetsRatio_edjp_FinancialReportSummary_FY = {
	/**
	 * 当年度会計期間_連結_実績
	 */
	current_year_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_実績
	 */
	current_year_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度会計期間_連結_実績
	 */
	prior_year_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度会計期間_非連結又は個別_実績
	 */
	prior_year_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 経常利益 
 */
export type OrdinaryIncome_edjp_FinancialReportSummary = {
	/**
	 * 当年度期初から第２四半期間_連結_実績
	 */
	current_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_予想
	 */
	current_year_duration_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_下限
	 */
	current_year_duration_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_上限
	 */
	current_year_duration_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第２四半期間_連結_実績
	 */
	prior_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 経常利益 
 */
export type OrdinaryIncome_edjp_FinancialReportSummary_FY = {
	/**
	 * 当年度会計期間_連結_実績
	 */
	current_year_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_実績
	 */
	current_year_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 次年度期初から第２四半期間_非連結又は個別_予想
	 */
	next_accumulated_q2_duration_non_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 次年度期初から第２四半期間_非連結又は個別_下限
	 */
	next_accumulated_q2_duration_non_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 次年度期初から第２四半期間_非連結又は個別_上限
	 */
	next_accumulated_q2_duration_non_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 次年度会計期間_連結_予想
	 */
	next_year_duration_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 次年度会計期間_連結_下限
	 */
	next_year_duration_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 次年度会計期間_連結_上限
	 */
	next_year_duration_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 次年度会計期間_非連結又は個別_予想
	 */
	next_year_duration_non_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 次年度会計期間_非連結又は個別_下限
	 */
	next_year_duration_non_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 次年度会計期間_非連結又は個別_上限
	 */
	next_year_duration_non_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 前年度会計期間_連結_実績
	 */
	prior_year_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度会計期間_非連結又は個別_実績
	 */
	prior_year_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 経常利益 
 */
export type OrdinaryIncome_edjp_FinancialReportSummary_HY_specific_business = {
	/**
	 * 当年度期初から第２四半期間_連結_実績
	 */
	current_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度期初から第２四半期間_非連結又は個別_実績
	 */
	current_accumulated_q2_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_予想
	 */
	current_year_duration_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_下限
	 */
	current_year_duration_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_上限
	 */
	current_year_duration_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_予想
	 */
	current_year_duration_non_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_下限
	 */
	current_year_duration_non_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_上限
	 */
	current_year_duration_non_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第２四半期間_連結_実績
	 */
	prior_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第２四半期間_非連結又は個別_実績
	 */
	prior_accumulated_q2_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 経常利益 
 */
export type OrdinaryIncome_edjp_FinancialReportSummary_Q1 = {
	/**
	 * 当年度期初から第１四半期間_連結_実績
	 */
	current_accumulated_q1_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度期初から第１四半期間_非連結又は個別_実績
	 */
	current_accumulated_q1_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度期初から第２四半期間_非連結又は個別_予想
	 */
	current_accumulated_q2_duration_non_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度期初から第２四半期間_非連結又は個別_下限
	 */
	current_accumulated_q2_duration_non_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度期初から第２四半期間_非連結又は個別_上限
	 */
	current_accumulated_q2_duration_non_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_予想
	 */
	current_year_duration_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_下限
	 */
	current_year_duration_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_上限
	 */
	current_year_duration_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_予想
	 */
	current_year_duration_non_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_下限
	 */
	current_year_duration_non_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_上限
	 */
	current_year_duration_non_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第１四半期間_連結_実績
	 */
	prior_accumulated_q1_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第１四半期間_非連結又は個別_実績
	 */
	prior_accumulated_q1_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 経常利益 
 */
export type OrdinaryIncome_edjp_FinancialReportSummary_Q2 = {
	/**
	 * 当年度期初から第２四半期間_連結_実績
	 */
	current_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度期初から第２四半期間_非連結又は個別_実績
	 */
	current_accumulated_q2_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_予想
	 */
	current_year_duration_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_下限
	 */
	current_year_duration_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_上限
	 */
	current_year_duration_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_予想
	 */
	current_year_duration_non_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_下限
	 */
	current_year_duration_non_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_非連結又は個別_上限
	 */
	current_year_duration_non_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第２四半期間_連結_実績
	 */
	prior_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第２四半期間_非連結又は個別_実績
	 */
	prior_accumulated_q2_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 経常利益 
 */
export type OrdinaryIncome_edjp_FinancialReportSummary_Q3 = {
	/**
	 * 当年度期初から第３四半期間_連結_実績
	 */
	current_accumulated_q3_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_予想
	 */
	current_year_duration_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_下限
	 */
	current_year_duration_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_上限
	 */
	current_year_duration_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第３四半期間_連結_実績
	 */
	prior_accumulated_q3_duration_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 経常収益、銀行 
 */
export type OrdinaryRevenuesBK_edjp_FinancialReportSummary_HY_specific_business = {
	/**
	 * 当年度期初から第２四半期間_連結_実績
	 */
	current_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度期初から第２四半期間_非連結又は個別_実績
	 */
	current_accumulated_q2_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第２四半期間_連結_実績
	 */
	prior_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第２四半期間_非連結又は個別_実績
	 */
	prior_accumulated_q2_duration_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 自己資本 
 */
export type OwnersEquity_edjp_FinancialReportSummary = {
	/**
	 * 当年度期初から第２四半期間時点_連結_実績
	 */
	current_accumulated_q2_instant_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度時点_連結_実績
	 */
	prior_year_instant_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 自己資本 
 */
export type OwnersEquity_edjp_FinancialReportSummary_FY = {
	/**
	 * 当年度時点_連結_実績
	 */
	current_year_instant_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度時点_非連結又は個別_実績
	 */
	current_year_instant_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度時点_連結_実績
	 */
	prior_year_instant_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度時点_非連結又は個別_実績
	 */
	prior_year_instant_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 自己資本 
 */
export type OwnersEquity_edjp_FinancialReportSummary_HY_specific_business = {
	/**
	 * 当年度期初から第２四半期間時点_連結_実績
	 */
	current_accumulated_q2_instant_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度期初から第２四半期間時点_非連結又は個別_実績
	 */
	current_accumulated_q2_instant_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度時点_連結_実績
	 */
	prior_year_instant_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度時点_非連結又は個別_実績
	 */
	prior_year_instant_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 自己資本 
 */
export type OwnersEquity_edjp_FinancialReportSummary_Q1 = {
	/**
	 * 当年度期初から第１四半期間時点_連結_実績
	 */
	current_accumulated_q1_instant_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度期初から第１四半期間時点_非連結又は個別_実績
	 */
	current_accumulated_q1_instant_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度時点_連結_実績
	 */
	prior_year_instant_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度時点_非連結又は個別_実績
	 */
	prior_year_instant_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 自己資本 
 */
export type OwnersEquity_edjp_FinancialReportSummary_Q2 = {
	/**
	 * 当年度期初から第２四半期間時点_連結_実績
	 */
	current_accumulated_q2_instant_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度期初から第２四半期間時点_非連結又は個別_実績
	 */
	current_accumulated_q2_instant_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度時点_連結_実績
	 */
	prior_year_instant_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度時点_非連結又は個別_実績
	 */
	prior_year_instant_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 自己資本 
 */
export type OwnersEquity_edjp_FinancialReportSummary_Q3 = {
	/**
	 * 当年度期初から第３四半期間時点_連結_実績
	 */
	current_accumulated_q3_instant_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度時点_連結_実績
	 */
	prior_year_instant_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 配当性向 
 */
export type PayoutRatio_edjp_FinancialReportSummary_FY = {
	/**
	 * 当年度会計期間_年間_連結_実績
	 */
	current_year_duration_annual_member_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_年間_非連結又は個別_実績
	 */
	current_year_duration_annual_member_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 次年度会計期間_年間_連結_予想
	 */
	next_year_duration_annual_member_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 次年度会計期間_年間_非連結又は個別_予想
	 */
	next_year_duration_annual_member_non_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 前年度会計期間_年間_連結_実績
	 */
	prior_year_duration_annual_member_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度会計期間_年間_非連結又は個別_実績
	 */
	prior_year_duration_annual_member_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 親会社株主に帰属する当期純利益 
 */
export type ProfitAttributableToOwnersOfParent_edjp_FinancialReportSummary = {
	/**
	 * 当年度期初から第２四半期間_連結_実績
	 */
	current_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_予想
	 */
	current_year_duration_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_下限
	 */
	current_year_duration_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_上限
	 */
	current_year_duration_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第２四半期間_連結_実績
	 */
	prior_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 親会社株主に帰属する当期純利益 
 */
export type ProfitAttributableToOwnersOfParent_edjp_FinancialReportSummary_FY = {
	/**
	 * 当年度会計期間_連結_実績
	 */
	current_year_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 次年度会計期間_連結_予想
	 */
	next_year_duration_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 次年度会計期間_連結_下限
	 */
	next_year_duration_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 次年度会計期間_連結_上限
	 */
	next_year_duration_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 前年度会計期間_連結_実績
	 */
	prior_year_duration_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 親会社株主に帰属する当期純利益 
 */
export type ProfitAttributableToOwnersOfParent_edjp_FinancialReportSummary_HY_specific_business = {
	/**
	 * 当年度期初から第２四半期間_連結_実績
	 */
	current_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_予想
	 */
	current_year_duration_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_下限
	 */
	current_year_duration_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_上限
	 */
	current_year_duration_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第２四半期間_連結_実績
	 */
	prior_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 親会社株主に帰属する当期純利益 
 */
export type ProfitAttributableToOwnersOfParent_edjp_FinancialReportSummary_Q1 = {
	/**
	 * 当年度期初から第１四半期間_連結_実績
	 */
	current_accumulated_q1_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_予想
	 */
	current_year_duration_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_下限
	 */
	current_year_duration_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_上限
	 */
	current_year_duration_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第１四半期間_連結_実績
	 */
	prior_accumulated_q1_duration_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 親会社株主に帰属する当期純利益 
 */
export type ProfitAttributableToOwnersOfParent_edjp_FinancialReportSummary_Q2 = {
	/**
	 * 当年度期初から第２四半期間_連結_実績
	 */
	current_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_予想
	 */
	current_year_duration_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_下限
	 */
	current_year_duration_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_上限
	 */
	current_year_duration_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第２四半期間_連結_実績
	 */
	prior_accumulated_q2_duration_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 親会社株主に帰属する当期純利益 
 */
export type ProfitAttributableToOwnersOfParent_edjp_FinancialReportSummary_Q3 = {
	/**
	 * 当年度期初から第３四半期間_連結_実績
	 */
	current_accumulated_q3_duration_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_予想
	 */
	current_year_duration_consolidated_member_forecast_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_下限
	 */
	current_year_duration_consolidated_member_lower_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_連結_上限
	 */
	current_year_duration_consolidated_member_upper_member?: IxNonFractionPublic;
	/**
	 * 前年度期初から第３四半期間_連結_実績
	 */
	prior_accumulated_q3_duration_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 定性的情報のヘッダー情報を取得するためのモデル
 */
export type QualitativeInfoHeader = {
	/**
	 * 当四半期決算に関する定性的情報
	 */
	qualitative_info?: QualitativeInfoSubTitle | null;
};



/**
 * 定性的情報を取得するためのモデル
 */
export type QualitativeInfoSubTitle = {
	/**
	 * 経営成績に関する説明
	 */
	operating_result_info?: string | null;
	/**
	 * セグメント情報
	 */
	segment_info_key?: Array<string> | null;
	/**
	 * セグメント情報
	 */
	segment_info?: Record<string, unknown>;
	/**
	 * セグメント画像URL
	 */
	segment_photo_url?: Record<string, unknown>;
	/**
	 * 財政状態の説明
	 */
	explanation_of_financial_position?: string | null;
	/**
	 * 将来予測に関する説明
	 */
	forecast_info?: string | null;
};



/**
 * 四半期 
 */
export type QuarterlyPeriod_edjp_FinancialReportSummary = {
	/**
	 * 当年度期初から第２四半期間時点
	 */
	current_accumulated_q2_instant?: IxNonFractionPublic;
};



/**
 * 四半期 
 */
export type QuarterlyPeriod_edjp_FinancialReportSummary_HY_specific_business = {
	/**
	 * 当年度期初から第２四半期間時点
	 */
	current_accumulated_q2_instant?: IxNonFractionPublic;
};



/**
 * 四半期 
 */
export type QuarterlyPeriod_edjp_FinancialReportSummary_Q1 = {
	/**
	 * 当年度期初から第１四半期間時点
	 */
	current_accumulated_q1_instant?: IxNonFractionPublic;
};



/**
 * 四半期 
 */
export type QuarterlyPeriod_edjp_FinancialReportSummary_Q2 = {
	/**
	 * 当年度期初から第２四半期間時点
	 */
	current_accumulated_q2_instant?: IxNonFractionPublic;
};



/**
 * 四半期 
 */
export type QuarterlyPeriod_edjp_FinancialReportSummary_Q3 = {
	/**
	 * 当年度期初から第３四半期間時点
	 */
	current_accumulated_q3_instant?: IxNonFractionPublic;
};



/**
 * 純資産配当率 
 */
export type RatioOfTotalAmountOfDividendsToNetAssets_edjp_FinancialReportSummary_FY = {
	/**
	 * 当年度会計期間_年間_連結_実績
	 */
	current_year_duration_annual_member_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度会計期間_年間_非連結又は個別_実績
	 */
	current_year_duration_annual_member_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度会計期間_年間_連結_実績
	 */
	prior_year_duration_annual_member_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度会計期間_年間_非連結又は個別_実績
	 */
	prior_year_duration_annual_member_non_consolidated_member_result_member?: IxNonFractionPublic;
};



export type Token = {
	access_token: string;
	token_type?: string;
};



/**
 * 総資産 
 */
export type TotalAssets_edjp_FinancialReportSummary = {
	/**
	 * 当年度期初から第２四半期間時点_連結_実績
	 */
	current_accumulated_q2_instant_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度時点_連結_実績
	 */
	prior_year_instant_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 総資産 
 */
export type TotalAssets_edjp_FinancialReportSummary_FY = {
	/**
	 * 当年度時点_連結_実績
	 */
	current_year_instant_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度時点_非連結又は個別_実績
	 */
	current_year_instant_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度時点_連結_実績
	 */
	prior_year_instant_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度時点_非連結又は個別_実績
	 */
	prior_year_instant_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 総資産 
 */
export type TotalAssets_edjp_FinancialReportSummary_HY_specific_business = {
	/**
	 * 当年度期初から第２四半期間時点_連結_実績
	 */
	current_accumulated_q2_instant_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度期初から第２四半期間時点_非連結又は個別_実績
	 */
	current_accumulated_q2_instant_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度時点_連結_実績
	 */
	prior_year_instant_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度時点_非連結又は個別_実績
	 */
	prior_year_instant_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 総資産 
 */
export type TotalAssets_edjp_FinancialReportSummary_Q1 = {
	/**
	 * 当年度期初から第１四半期間時点_連結_実績
	 */
	current_accumulated_q1_instant_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度期初から第１四半期間時点_非連結又は個別_実績
	 */
	current_accumulated_q1_instant_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度時点_連結_実績
	 */
	prior_year_instant_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度時点_非連結又は個別_実績
	 */
	prior_year_instant_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 総資産 
 */
export type TotalAssets_edjp_FinancialReportSummary_Q2 = {
	/**
	 * 当年度期初から第２四半期間時点_連結_実績
	 */
	current_accumulated_q2_instant_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 当年度期初から第２四半期間時点_非連結又は個別_実績
	 */
	current_accumulated_q2_instant_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度時点_連結_実績
	 */
	prior_year_instant_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度時点_非連結又は個別_実績
	 */
	prior_year_instant_non_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 総資産 
 */
export type TotalAssets_edjp_FinancialReportSummary_Q3 = {
	/**
	 * 当年度期初から第３四半期間時点_連結_実績
	 */
	current_accumulated_q3_instant_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度時点_連結_実績
	 */
	prior_year_instant_consolidated_member_result_member?: IxNonFractionPublic;
};



/**
 * 配当金総額（合計） 
 */
export type TotalDividendPaidAnnual_edjp_FinancialReportSummary_FY = {
	/**
	 * 当年度会計期間_年間_非連結又は個別_実績
	 */
	current_year_duration_annual_member_non_consolidated_member_result_member?: IxNonFractionPublic;
	/**
	 * 前年度会計期間_年間_非連結又は個別_実績
	 */
	prior_year_duration_annual_member_non_consolidated_member_result_member?: IxNonFractionPublic;
};



export type UpdatePassword = {
	current_password: string;
	new_password: string;
};



export type UserCreate = {
	email: string;
	is_active?: boolean;
	is_superuser?: boolean;
	full_name?: string | null;
	password: string;
};



export type UserPublic = {
	email: string;
	is_active?: boolean;
	is_superuser?: boolean;
	full_name?: string | null;
	id: string;
};



export type UserRegister = {
	email: string;
	password: string;
	full_name?: string | null;
};



export type UserUpdate = {
	email?: string | null;
	is_active?: boolean;
	is_superuser?: boolean;
	full_name?: string | null;
	password?: string | null;
};



export type UserUpdateMe = {
	full_name?: string | null;
	email?: string | null;
};



export type UsersPublic = {
	data: Array<UserPublic>;
	count: number;
};



export type ValidationError = {
	loc: Array<string | number>;
	msg: string;
	type: string;
};



export type edjp_FinancialReportSummary = {
	/**
	 * 期中平均株式数
	 */
	average_number_of_shares?: AverageNumberOfShares_edjp_FinancialReportSummary;
	/**
	 * 自己資本比率
	 */
	capital_adequacy_ratio?: CapitalAdequacyRatio_edjp_FinancialReportSummary;
	/**
	 * 包括利益増減率
	 */
	change_in_comprehensive_income?: ChangeInComprehensiveIncome_edjp_FinancialReportSummary;
	/**
	 * 増減率、売上高
	 */
	change_in_net_sales?: ChangeInNetSales_edjp_FinancialReportSummary;
	/**
	 * 増減率、営業利益
	 */
	change_in_operating_income?: ChangeInOperatingIncome_edjp_FinancialReportSummary;
	/**
	 * 増減率、経常利益
	 */
	change_in_ordinary_income?: ChangeInOrdinaryIncome_edjp_FinancialReportSummary;
	/**
	 * 増減率、親会社株主に帰属する当期純利益
	 */
	change_in_profit_attributable_to_owners_of_parent?: ChangeInProfitAttributableToOwnersOfParent_edjp_FinancialReportSummary;
	/**
	 * 包括利益
	 */
	comprehensive_income?: ComprehensiveIncome_edjp_FinancialReportSummary;
	/**
	 * 潜在株式調整後1株当たり当期純利益
	 */
	diluted_net_income_per_share?: DilutedNetIncomePerShare_edjp_FinancialReportSummary;
	/**
	 * 1株当たり配当金
	 */
	dividend_per_share?: DividendPerShare_edjp_FinancialReportSummary;
	/**
	 * 純資産
	 */
	net_assets?: NetAssets_edjp_FinancialReportSummary;
	/**
	 * 1株当たり純資産
	 */
	net_assets_per_share?: NetAssetsPerShare_edjp_FinancialReportSummary;
	/**
	 * 1株当たり当期純利益
	 */
	net_income_per_share?: NetIncomePerShare_edjp_FinancialReportSummary;
	/**
	 * 売上高
	 */
	net_sales?: NetSales_edjp_FinancialReportSummary;
	/**
	 * 期末発行済株式数（自己株式を含む）
	 */
	number_of_issued_and_outstanding_shares_at_the_end_of_fiscal_year_including_treasury_stock?: NumberOfIssuedAndOutstandingSharesAtTheEndOfFiscalYearIncludingTreasuryStock_edjp_FinancialReportSummary;
	/**
	 * 期末自己株式数
	 */
	number_of_treasury_stock_at_the_end_of_fiscal_year?: NumberOfTreasuryStockAtTheEndOfFiscalYear_edjp_FinancialReportSummary;
	/**
	 * 営業利益
	 */
	operating_income?: OperatingIncome_edjp_FinancialReportSummary;
	/**
	 * 経常利益
	 */
	ordinary_income?: OrdinaryIncome_edjp_FinancialReportSummary;
	/**
	 * 自己資本
	 */
	owners_equity?: OwnersEquity_edjp_FinancialReportSummary;
	/**
	 * 親会社株主に帰属する当期純利益
	 */
	profit_attributable_to_owners_of_parent?: ProfitAttributableToOwnersOfParent_edjp_FinancialReportSummary;
	/**
	 * 四半期
	 */
	quarterly_period?: QuarterlyPeriod_edjp_FinancialReportSummary;
	/**
	 * 総資産
	 */
	total_assets?: TotalAssets_edjp_FinancialReportSummary;
};



export type edjp_FinancialReportSummary_FY = {
	/**
	 * 期中平均株式数
	 */
	average_number_of_shares?: AverageNumberOfShares_edjp_FinancialReportSummary_FY;
	/**
	 * 自己資本比率
	 */
	capital_adequacy_ratio?: CapitalAdequacyRatio_edjp_FinancialReportSummary_FY;
	/**
	 * 現金及び現金同等物期末残高
	 */
	cash_and_equivalents_end_of_period?: CashAndEquivalentsEndOfPeriod_edjp_FinancialReportSummary_FY;
	/**
	 * 財務活動によるキャッシュ・フロー
	 */
	cash_flows_from_financing_activities?: CashFlowsFromFinancingActivities_edjp_FinancialReportSummary_FY;
	/**
	 * 投資活動によるキャッシュ・フロー
	 */
	cash_flows_from_investing_activities?: CashFlowsFromInvestingActivities_edjp_FinancialReportSummary_FY;
	/**
	 * 営業活動によるキャッシュ・フロー
	 */
	cash_flows_from_operating_activities?: CashFlowsFromOperatingActivities_edjp_FinancialReportSummary_FY;
	/**
	 * 包括利益増減率
	 */
	change_in_comprehensive_income?: ChangeInComprehensiveIncome_edjp_FinancialReportSummary_FY;
	/**
	 * 増減率、当期純利益
	 */
	change_in_net_income?: ChangeInNetIncome_edjp_FinancialReportSummary_FY;
	/**
	 * 増減率、売上高
	 */
	change_in_net_sales?: ChangeInNetSales_edjp_FinancialReportSummary_FY;
	/**
	 * 増減率、営業利益
	 */
	change_in_operating_income?: ChangeInOperatingIncome_edjp_FinancialReportSummary_FY;
	/**
	 * 増減率、経常利益
	 */
	change_in_ordinary_income?: ChangeInOrdinaryIncome_edjp_FinancialReportSummary_FY;
	/**
	 * 増減率、親会社株主に帰属する当期純利益
	 */
	change_in_profit_attributable_to_owners_of_parent?: ChangeInProfitAttributableToOwnersOfParent_edjp_FinancialReportSummary_FY;
	/**
	 * 包括利益
	 */
	comprehensive_income?: ComprehensiveIncome_edjp_FinancialReportSummary_FY;
	/**
	 * 潜在株式調整後1株当たり当期純利益
	 */
	diluted_net_income_per_share?: DilutedNetIncomePerShare_edjp_FinancialReportSummary_FY;
	/**
	 * 1株当たり配当金
	 */
	dividend_per_share?: DividendPerShare_edjp_FinancialReportSummary_FY;
	/**
	 * 持分法投資損益
	 */
	investment_profit_loss_on_equity_method?: InvestmentProfitLossOnEquityMethod_edjp_FinancialReportSummary_FY;
	/**
	 * 純資産
	 */
	net_assets?: NetAssets_edjp_FinancialReportSummary_FY;
	/**
	 * 1株当たり純資産
	 */
	net_assets_per_share?: NetAssetsPerShare_edjp_FinancialReportSummary_FY;
	/**
	 * 当期純利益
	 */
	net_income?: NetIncome_edjp_FinancialReportSummary_FY;
	/**
	 * 1株当たり当期純利益
	 */
	net_income_per_share?: NetIncomePerShare_edjp_FinancialReportSummary_FY;
	/**
	 * 自己資本当期純利益率
	 */
	net_income_to_shareholders_equity_ratio?: NetIncomeToShareholdersEquityRatio_edjp_FinancialReportSummary_FY;
	/**
	 * 売上高
	 */
	net_sales?: NetSales_edjp_FinancialReportSummary_FY;
	/**
	 * 期末発行済株式数（自己株式を含む）
	 */
	number_of_issued_and_outstanding_shares_at_the_end_of_fiscal_year_including_treasury_stock?: NumberOfIssuedAndOutstandingSharesAtTheEndOfFiscalYearIncludingTreasuryStock_edjp_FinancialReportSummary_FY;
	/**
	 * 除外
	 */
	number_of_subsidiaries_excluded_from_consolidation?: NumberOfSubsidiariesExcludedFromConsolidation_edjp_FinancialReportSummary_FY;
	/**
	 * 新規
	 */
	number_of_subsidiaries_newly_consolidated?: NumberOfSubsidiariesNewlyConsolidated_edjp_FinancialReportSummary_FY;
	/**
	 * 期末自己株式数
	 */
	number_of_treasury_stock_at_the_end_of_fiscal_year?: NumberOfTreasuryStockAtTheEndOfFiscalYear_edjp_FinancialReportSummary_FY;
	/**
	 * 営業利益
	 */
	operating_income?: OperatingIncome_edjp_FinancialReportSummary_FY;
	/**
	 * 売上高営業利益率
	 */
	operating_income_to_net_sales_ratio?: OperatingIncomeToNetSalesRatio_edjp_FinancialReportSummary_FY;
	/**
	 * 経常利益
	 */
	ordinary_income?: OrdinaryIncome_edjp_FinancialReportSummary_FY;
	/**
	 * 総資産経常利益率
	 */
	ordinary_income_to_total_assets_ratio?: OrdinaryIncomeToTotalAssetsRatio_edjp_FinancialReportSummary_FY;
	/**
	 * 自己資本
	 */
	owners_equity?: OwnersEquity_edjp_FinancialReportSummary_FY;
	/**
	 * 配当性向
	 */
	payout_ratio?: PayoutRatio_edjp_FinancialReportSummary_FY;
	/**
	 * 親会社株主に帰属する当期純利益
	 */
	profit_attributable_to_owners_of_parent?: ProfitAttributableToOwnersOfParent_edjp_FinancialReportSummary_FY;
	/**
	 * 純資産配当率
	 */
	ratio_of_total_amount_of_dividends_to_net_assets?: RatioOfTotalAmountOfDividendsToNetAssets_edjp_FinancialReportSummary_FY;
	/**
	 * 総資産
	 */
	total_assets?: TotalAssets_edjp_FinancialReportSummary_FY;
	/**
	 * 配当金総額（合計）
	 */
	total_dividend_paid_annual?: TotalDividendPaidAnnual_edjp_FinancialReportSummary_FY;
};



export type edjp_FinancialReportSummary_HY_specific_business = {
	/**
	 * 期中平均株式数
	 */
	average_number_of_shares?: AverageNumberOfShares_edjp_FinancialReportSummary_HY_specific_business;
	/**
	 * 自己資本比率
	 */
	capital_adequacy_ratio?: CapitalAdequacyRatio_edjp_FinancialReportSummary_HY_specific_business;
	/**
	 * 包括利益増減率
	 */
	change_in_comprehensive_income?: ChangeInComprehensiveIncome_edjp_FinancialReportSummary_HY_specific_business;
	/**
	 * 増減率、当期純利益
	 */
	change_in_net_income?: ChangeInNetIncome_edjp_FinancialReportSummary_HY_specific_business;
	/**
	 * 増減率、経常利益
	 */
	change_in_ordinary_income?: ChangeInOrdinaryIncome_edjp_FinancialReportSummary_HY_specific_business;
	/**
	 * 増減率、経常収益、銀行
	 */
	change_in_ordinary_revenues_bk?: ChangeInOrdinaryRevenuesBK_edjp_FinancialReportSummary_HY_specific_business;
	/**
	 * 増減率、親会社株主に帰属する当期純利益
	 */
	change_in_profit_attributable_to_owners_of_parent?: ChangeInProfitAttributableToOwnersOfParent_edjp_FinancialReportSummary_HY_specific_business;
	/**
	 * 包括利益
	 */
	comprehensive_income?: ComprehensiveIncome_edjp_FinancialReportSummary_HY_specific_business;
	/**
	 * 潜在株式調整後1株当たり当期純利益
	 */
	diluted_net_income_per_share?: DilutedNetIncomePerShare_edjp_FinancialReportSummary_HY_specific_business;
	/**
	 * 1株当たり配当金
	 */
	dividend_per_share?: DividendPerShare_edjp_FinancialReportSummary_HY_specific_business;
	/**
	 * 純資産
	 */
	net_assets?: NetAssets_edjp_FinancialReportSummary_HY_specific_business;
	/**
	 * 1株当たり純資産
	 */
	net_assets_per_share?: NetAssetsPerShare_edjp_FinancialReportSummary_HY_specific_business;
	/**
	 * 当期純利益
	 */
	net_income?: NetIncome_edjp_FinancialReportSummary_HY_specific_business;
	/**
	 * 1株当たり当期純利益
	 */
	net_income_per_share?: NetIncomePerShare_edjp_FinancialReportSummary_HY_specific_business;
	/**
	 * 期末発行済株式数（自己株式を含む）
	 */
	number_of_issued_and_outstanding_shares_at_the_end_of_fiscal_year_including_treasury_stock?: NumberOfIssuedAndOutstandingSharesAtTheEndOfFiscalYearIncludingTreasuryStock_edjp_FinancialReportSummary_HY_specific_business;
	/**
	 * 期末自己株式数
	 */
	number_of_treasury_stock_at_the_end_of_fiscal_year?: NumberOfTreasuryStockAtTheEndOfFiscalYear_edjp_FinancialReportSummary_HY_specific_business;
	/**
	 * 経常利益
	 */
	ordinary_income?: OrdinaryIncome_edjp_FinancialReportSummary_HY_specific_business;
	/**
	 * 経常収益、銀行
	 */
	ordinary_revenues_bk?: OrdinaryRevenuesBK_edjp_FinancialReportSummary_HY_specific_business;
	/**
	 * 自己資本
	 */
	owners_equity?: OwnersEquity_edjp_FinancialReportSummary_HY_specific_business;
	/**
	 * 親会社株主に帰属する当期純利益
	 */
	profit_attributable_to_owners_of_parent?: ProfitAttributableToOwnersOfParent_edjp_FinancialReportSummary_HY_specific_business;
	/**
	 * 四半期
	 */
	quarterly_period?: QuarterlyPeriod_edjp_FinancialReportSummary_HY_specific_business;
	/**
	 * 総資産
	 */
	total_assets?: TotalAssets_edjp_FinancialReportSummary_HY_specific_business;
};



export type edjp_FinancialReportSummary_Q1 = {
	/**
	 * 期中平均株式数
	 */
	average_number_of_shares?: AverageNumberOfShares_edjp_FinancialReportSummary_Q1;
	/**
	 * 自己資本比率
	 */
	capital_adequacy_ratio?: CapitalAdequacyRatio_edjp_FinancialReportSummary_Q1;
	/**
	 * 包括利益増減率
	 */
	change_in_comprehensive_income?: ChangeInComprehensiveIncome_edjp_FinancialReportSummary_Q1;
	/**
	 * 増減率、当期純利益
	 */
	change_in_net_income?: ChangeInNetIncome_edjp_FinancialReportSummary_Q1;
	/**
	 * 増減率、売上高
	 */
	change_in_net_sales?: ChangeInNetSales_edjp_FinancialReportSummary_Q1;
	/**
	 * 増減率、営業利益
	 */
	change_in_operating_income?: ChangeInOperatingIncome_edjp_FinancialReportSummary_Q1;
	/**
	 * 増減率、経常利益
	 */
	change_in_ordinary_income?: ChangeInOrdinaryIncome_edjp_FinancialReportSummary_Q1;
	/**
	 * 増減率、親会社株主に帰属する当期純利益
	 */
	change_in_profit_attributable_to_owners_of_parent?: ChangeInProfitAttributableToOwnersOfParent_edjp_FinancialReportSummary_Q1;
	/**
	 * 包括利益
	 */
	comprehensive_income?: ComprehensiveIncome_edjp_FinancialReportSummary_Q1;
	/**
	 * 潜在株式調整後1株当たり当期純利益
	 */
	diluted_net_income_per_share?: DilutedNetIncomePerShare_edjp_FinancialReportSummary_Q1;
	/**
	 * 1株当たり配当金
	 */
	dividend_per_share?: DividendPerShare_edjp_FinancialReportSummary_Q1;
	/**
	 * 純資産
	 */
	net_assets?: NetAssets_edjp_FinancialReportSummary_Q1;
	/**
	 * 1株当たり純資産
	 */
	net_assets_per_share?: NetAssetsPerShare_edjp_FinancialReportSummary_Q1;
	/**
	 * 当期純利益
	 */
	net_income?: NetIncome_edjp_FinancialReportSummary_Q1;
	/**
	 * 1株当たり当期純利益
	 */
	net_income_per_share?: NetIncomePerShare_edjp_FinancialReportSummary_Q1;
	/**
	 * 売上高
	 */
	net_sales?: NetSales_edjp_FinancialReportSummary_Q1;
	/**
	 * 期末発行済株式数（自己株式を含む）
	 */
	number_of_issued_and_outstanding_shares_at_the_end_of_fiscal_year_including_treasury_stock?: NumberOfIssuedAndOutstandingSharesAtTheEndOfFiscalYearIncludingTreasuryStock_edjp_FinancialReportSummary_Q1;
	/**
	 * 除外
	 */
	number_of_subsidiaries_excluded_from_consolidation?: NumberOfSubsidiariesExcludedFromConsolidation_edjp_FinancialReportSummary_Q1;
	/**
	 * 新規
	 */
	number_of_subsidiaries_newly_consolidated?: NumberOfSubsidiariesNewlyConsolidated_edjp_FinancialReportSummary_Q1;
	/**
	 * 期末自己株式数
	 */
	number_of_treasury_stock_at_the_end_of_fiscal_year?: NumberOfTreasuryStockAtTheEndOfFiscalYear_edjp_FinancialReportSummary_Q1;
	/**
	 * 営業利益
	 */
	operating_income?: OperatingIncome_edjp_FinancialReportSummary_Q1;
	/**
	 * 経常利益
	 */
	ordinary_income?: OrdinaryIncome_edjp_FinancialReportSummary_Q1;
	/**
	 * 自己資本
	 */
	owners_equity?: OwnersEquity_edjp_FinancialReportSummary_Q1;
	/**
	 * 親会社株主に帰属する当期純利益
	 */
	profit_attributable_to_owners_of_parent?: ProfitAttributableToOwnersOfParent_edjp_FinancialReportSummary_Q1;
	/**
	 * 四半期
	 */
	quarterly_period?: QuarterlyPeriod_edjp_FinancialReportSummary_Q1;
	/**
	 * 総資産
	 */
	total_assets?: TotalAssets_edjp_FinancialReportSummary_Q1;
};



export type edjp_FinancialReportSummary_Q2 = {
	/**
	 * 期中平均株式数
	 */
	average_number_of_shares?: AverageNumberOfShares_edjp_FinancialReportSummary_Q2;
	/**
	 * 自己資本比率
	 */
	capital_adequacy_ratio?: CapitalAdequacyRatio_edjp_FinancialReportSummary_Q2;
	/**
	 * 包括利益増減率
	 */
	change_in_comprehensive_income?: ChangeInComprehensiveIncome_edjp_FinancialReportSummary_Q2;
	/**
	 * 増減率、当期純利益
	 */
	change_in_net_income?: ChangeInNetIncome_edjp_FinancialReportSummary_Q2;
	/**
	 * 増減率、純営業収益、証券
	 */
	change_in_net_operating_revenues_se?: ChangeInNetOperatingRevenuesSE_edjp_FinancialReportSummary_Q2;
	/**
	 * 増減率、売上高
	 */
	change_in_net_sales?: ChangeInNetSales_edjp_FinancialReportSummary_Q2;
	/**
	 * 増減率、営業利益
	 */
	change_in_operating_income?: ChangeInOperatingIncome_edjp_FinancialReportSummary_Q2;
	/**
	 * 増減率、営業収益
	 */
	change_in_operating_revenues?: ChangeInOperatingRevenues_edjp_FinancialReportSummary_Q2;
	/**
	 * 増減率、営業収益、証券
	 */
	change_in_operating_revenues_se?: ChangeInOperatingRevenuesSE_edjp_FinancialReportSummary_Q2;
	/**
	 * 増減率、経常利益
	 */
	change_in_ordinary_income?: ChangeInOrdinaryIncome_edjp_FinancialReportSummary_Q2;
	/**
	 * 増減率、親会社株主に帰属する当期純利益
	 */
	change_in_profit_attributable_to_owners_of_parent?: ChangeInProfitAttributableToOwnersOfParent_edjp_FinancialReportSummary_Q2;
	/**
	 * 記念配当
	 */
	commemorative_dividend?: CommemorativeDividend_edjp_FinancialReportSummary_Q2;
	/**
	 * 包括利益
	 */
	comprehensive_income?: ComprehensiveIncome_edjp_FinancialReportSummary_Q2;
	/**
	 * 潜在株式調整後1株当たり当期純利益
	 */
	diluted_net_income_per_share?: DilutedNetIncomePerShare_edjp_FinancialReportSummary_Q2;
	/**
	 * 1株当たり配当金
	 */
	dividend_per_share?: DividendPerShare_edjp_FinancialReportSummary_Q2;
	/**
	 * 特別配当
	 */
	extra_dividend?: ExtraDividend_edjp_FinancialReportSummary_Q2;
	/**
	 * 純資産
	 */
	net_assets?: NetAssets_edjp_FinancialReportSummary_Q2;
	/**
	 * 1株当たり純資産
	 */
	net_assets_per_share?: NetAssetsPerShare_edjp_FinancialReportSummary_Q2;
	/**
	 * 当期純利益
	 */
	net_income?: NetIncome_edjp_FinancialReportSummary_Q2;
	/**
	 * 1株当たり当期純利益
	 */
	net_income_per_share?: NetIncomePerShare_edjp_FinancialReportSummary_Q2;
	/**
	 * 純営業収益、証券
	 */
	net_operating_revenues_se?: NetOperatingRevenuesSE_edjp_FinancialReportSummary_Q2;
	/**
	 * 売上高
	 */
	net_sales?: NetSales_edjp_FinancialReportSummary_Q2;
	/**
	 * 期末発行済株式数（自己株式を含む）
	 */
	number_of_issued_and_outstanding_shares_at_the_end_of_fiscal_year_including_treasury_stock?: NumberOfIssuedAndOutstandingSharesAtTheEndOfFiscalYearIncludingTreasuryStock_edjp_FinancialReportSummary_Q2;
	/**
	 * 除外
	 */
	number_of_subsidiaries_excluded_from_consolidation?: NumberOfSubsidiariesExcludedFromConsolidation_edjp_FinancialReportSummary_Q2;
	/**
	 * 新規
	 */
	number_of_subsidiaries_newly_consolidated?: NumberOfSubsidiariesNewlyConsolidated_edjp_FinancialReportSummary_Q2;
	/**
	 * 期末自己株式数
	 */
	number_of_treasury_stock_at_the_end_of_fiscal_year?: NumberOfTreasuryStockAtTheEndOfFiscalYear_edjp_FinancialReportSummary_Q2;
	/**
	 * 営業利益
	 */
	operating_income?: OperatingIncome_edjp_FinancialReportSummary_Q2;
	/**
	 * 営業収益
	 */
	operating_revenues?: OperatingRevenues_edjp_FinancialReportSummary_Q2;
	/**
	 * 営業収益、証券
	 */
	operating_revenues_se?: OperatingRevenuesSE_edjp_FinancialReportSummary_Q2;
	/**
	 * 経常利益
	 */
	ordinary_income?: OrdinaryIncome_edjp_FinancialReportSummary_Q2;
	/**
	 * 自己資本
	 */
	owners_equity?: OwnersEquity_edjp_FinancialReportSummary_Q2;
	/**
	 * 親会社株主に帰属する当期純利益
	 */
	profit_attributable_to_owners_of_parent?: ProfitAttributableToOwnersOfParent_edjp_FinancialReportSummary_Q2;
	/**
	 * 四半期
	 */
	quarterly_period?: QuarterlyPeriod_edjp_FinancialReportSummary_Q2;
	/**
	 * 総資産
	 */
	total_assets?: TotalAssets_edjp_FinancialReportSummary_Q2;
};



export type edjp_FinancialReportSummary_Q3 = {
	/**
	 * 期中平均株式数
	 */
	average_number_of_shares?: AverageNumberOfShares_edjp_FinancialReportSummary_Q3;
	/**
	 * 自己資本比率
	 */
	capital_adequacy_ratio?: CapitalAdequacyRatio_edjp_FinancialReportSummary_Q3;
	/**
	 * 包括利益増減率
	 */
	change_in_comprehensive_income?: ChangeInComprehensiveIncome_edjp_FinancialReportSummary_Q3;
	/**
	 * 増減率、売上高
	 */
	change_in_net_sales?: ChangeInNetSales_edjp_FinancialReportSummary_Q3;
	/**
	 * 増減率、営業利益
	 */
	change_in_operating_income?: ChangeInOperatingIncome_edjp_FinancialReportSummary_Q3;
	/**
	 * 増減率、経常利益
	 */
	change_in_ordinary_income?: ChangeInOrdinaryIncome_edjp_FinancialReportSummary_Q3;
	/**
	 * 増減率、親会社株主に帰属する当期純利益
	 */
	change_in_profit_attributable_to_owners_of_parent?: ChangeInProfitAttributableToOwnersOfParent_edjp_FinancialReportSummary_Q3;
	/**
	 * 包括利益
	 */
	comprehensive_income?: ComprehensiveIncome_edjp_FinancialReportSummary_Q3;
	/**
	 * 潜在株式調整後1株当たり当期純利益
	 */
	diluted_net_income_per_share?: DilutedNetIncomePerShare_edjp_FinancialReportSummary_Q3;
	/**
	 * 1株当たり配当金
	 */
	dividend_per_share?: DividendPerShare_edjp_FinancialReportSummary_Q3;
	/**
	 * 純資産
	 */
	net_assets?: NetAssets_edjp_FinancialReportSummary_Q3;
	/**
	 * 1株当たり純資産
	 */
	net_assets_per_share?: NetAssetsPerShare_edjp_FinancialReportSummary_Q3;
	/**
	 * 1株当たり当期純利益
	 */
	net_income_per_share?: NetIncomePerShare_edjp_FinancialReportSummary_Q3;
	/**
	 * 売上高
	 */
	net_sales?: NetSales_edjp_FinancialReportSummary_Q3;
	/**
	 * 期末発行済株式数（自己株式を含む）
	 */
	number_of_issued_and_outstanding_shares_at_the_end_of_fiscal_year_including_treasury_stock?: NumberOfIssuedAndOutstandingSharesAtTheEndOfFiscalYearIncludingTreasuryStock_edjp_FinancialReportSummary_Q3;
	/**
	 * 除外
	 */
	number_of_subsidiaries_excluded_from_consolidation?: NumberOfSubsidiariesExcludedFromConsolidation_edjp_FinancialReportSummary_Q3;
	/**
	 * 新規
	 */
	number_of_subsidiaries_newly_consolidated?: NumberOfSubsidiariesNewlyConsolidated_edjp_FinancialReportSummary_Q3;
	/**
	 * 期末自己株式数
	 */
	number_of_treasury_stock_at_the_end_of_fiscal_year?: NumberOfTreasuryStockAtTheEndOfFiscalYear_edjp_FinancialReportSummary_Q3;
	/**
	 * 営業利益
	 */
	operating_income?: OperatingIncome_edjp_FinancialReportSummary_Q3;
	/**
	 * 経常利益
	 */
	ordinary_income?: OrdinaryIncome_edjp_FinancialReportSummary_Q3;
	/**
	 * 自己資本
	 */
	owners_equity?: OwnersEquity_edjp_FinancialReportSummary_Q3;
	/**
	 * 親会社株主に帰属する当期純利益
	 */
	profit_attributable_to_owners_of_parent?: ProfitAttributableToOwnersOfParent_edjp_FinancialReportSummary_Q3;
	/**
	 * 四半期
	 */
	quarterly_period?: QuarterlyPeriod_edjp_FinancialReportSummary_Q3;
	/**
	 * 総資産
	 */
	total_assets?: TotalAssets_edjp_FinancialReportSummary_Q3;
};

