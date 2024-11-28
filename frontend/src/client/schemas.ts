export const $AverageNumberOfShares_edjp_FinancialReportSummary = {
	description: `期中平均株式数 `,
	properties: {
		current_accumulated_q2_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_非連結又は個別_実績`,
},
		prior_accumulated_q2_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第２四半期間_非連結又は個別_実績`,
},
	},
} as const;

export const $AverageNumberOfShares_edjp_FinancialReportSummary_FY = {
	description: `期中平均株式数 `,
	properties: {
		current_year_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_実績`,
},
		prior_year_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度会計期間_非連結又は個別_実績`,
},
	},
} as const;

export const $AverageNumberOfShares_edjp_FinancialReportSummary_HY_specific_business = {
	description: `期中平均株式数 `,
	properties: {
		current_accumulated_q2_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_非連結又は個別_実績`,
},
		prior_accumulated_q2_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第２四半期間_非連結又は個別_実績`,
},
	},
} as const;

export const $AverageNumberOfShares_edjp_FinancialReportSummary_Q1 = {
	description: `期中平均株式数 `,
	properties: {
		current_accumulated_q1_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第１四半期間_非連結又は個別_実績`,
},
		prior_accumulated_q1_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第１四半期間_非連結又は個別_実績`,
},
	},
} as const;

export const $AverageNumberOfShares_edjp_FinancialReportSummary_Q2 = {
	description: `期中平均株式数 `,
	properties: {
		current_accumulated_q2_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_非連結又は個別_実績`,
},
		prior_accumulated_q2_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第２四半期間_非連結又は個別_実績`,
},
	},
} as const;

export const $AverageNumberOfShares_edjp_FinancialReportSummary_Q3 = {
	description: `期中平均株式数 `,
	properties: {
		current_accumulated_q3_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第３四半期間_非連結又は個別_実績`,
},
		prior_accumulated_q3_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第３四半期間_非連結又は個別_実績`,
},
	},
} as const;

export const $Body_login_login_access_token = {
	properties: {
		grant_type: {
	type: 'any-of',
	contains: [{
	type: 'string',
	pattern: 'password',
}, {
	type: 'null',
}],
},
		username: {
	type: 'string',
	isRequired: true,
},
		password: {
	type: 'string',
	isRequired: true,
},
		scope: {
	type: 'string',
	default: '',
},
		client_id: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
		client_secret: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
	},
} as const;

export const $CapitalAdequacyRatio_edjp_FinancialReportSummary = {
	description: `自己資本比率 `,
	properties: {
		current_accumulated_q2_instant_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間時点_連結_実績`,
},
		prior_year_instant_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度時点_連結_実績`,
},
	},
} as const;

export const $CapitalAdequacyRatio_edjp_FinancialReportSummary_FY = {
	description: `自己資本比率 `,
	properties: {
		current_year_instant_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度時点_連結_実績`,
},
		current_year_instant_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度時点_非連結又は個別_実績`,
},
		prior_year_instant_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度時点_連結_実績`,
},
		prior_year_instant_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度時点_非連結又は個別_実績`,
},
	},
} as const;

export const $CapitalAdequacyRatio_edjp_FinancialReportSummary_HY_specific_business = {
	description: `自己資本比率 `,
	properties: {
		current_accumulated_q2_instant_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間時点_連結_実績`,
},
		current_accumulated_q2_instant_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間時点_非連結又は個別_実績`,
},
		prior_year_instant_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度時点_連結_実績`,
},
		prior_year_instant_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度時点_非連結又は個別_実績`,
},
	},
} as const;

export const $CapitalAdequacyRatio_edjp_FinancialReportSummary_Q1 = {
	description: `自己資本比率 `,
	properties: {
		current_accumulated_q1_instant_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第１四半期間時点_連結_実績`,
},
		current_accumulated_q1_instant_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第１四半期間時点_非連結又は個別_実績`,
},
		prior_year_instant_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度時点_連結_実績`,
},
		prior_year_instant_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度時点_非連結又は個別_実績`,
},
	},
} as const;

export const $CapitalAdequacyRatio_edjp_FinancialReportSummary_Q2 = {
	description: `自己資本比率 `,
	properties: {
		current_accumulated_q2_instant_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間時点_連結_実績`,
},
		current_accumulated_q2_instant_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間時点_非連結又は個別_実績`,
},
		prior_year_instant_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度時点_連結_実績`,
},
		prior_year_instant_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度時点_非連結又は個別_実績`,
},
	},
} as const;

export const $CapitalAdequacyRatio_edjp_FinancialReportSummary_Q3 = {
	description: `自己資本比率 `,
	properties: {
		current_accumulated_q3_instant_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第３四半期間時点_連結_実績`,
},
		prior_year_instant_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度時点_連結_実績`,
},
	},
} as const;

export const $CashAndEquivalentsEndOfPeriod_edjp_FinancialReportSummary_FY = {
	description: `現金及び現金同等物期末残高 `,
	properties: {
		current_year_instant_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度時点_連結_実績`,
},
		current_year_instant_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度時点_非連結又は個別_実績`,
},
		prior_year_instant_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度時点_連結_実績`,
},
		prior_year_instant_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度時点_非連結又は個別_実績`,
},
	},
} as const;

export const $CashFlowsFromFinancingActivities_edjp_FinancialReportSummary_FY = {
	description: `財務活動によるキャッシュ・フロー `,
	properties: {
		current_year_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_実績`,
},
		current_year_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_実績`,
},
		prior_year_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度会計期間_連結_実績`,
},
		prior_year_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度会計期間_非連結又は個別_実績`,
},
	},
} as const;

export const $CashFlowsFromInvestingActivities_edjp_FinancialReportSummary_FY = {
	description: `投資活動によるキャッシュ・フロー `,
	properties: {
		current_year_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_実績`,
},
		current_year_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_実績`,
},
		prior_year_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度会計期間_連結_実績`,
},
		prior_year_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度会計期間_非連結又は個別_実績`,
},
	},
} as const;

export const $CashFlowsFromOperatingActivities_edjp_FinancialReportSummary_FY = {
	description: `営業活動によるキャッシュ・フロー `,
	properties: {
		current_year_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_実績`,
},
		current_year_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_実績`,
},
		prior_year_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度会計期間_連結_実績`,
},
		prior_year_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度会計期間_非連結又は個別_実績`,
},
	},
} as const;

export const $ChangeInComprehensiveIncome_edjp_FinancialReportSummary = {
	description: `包括利益増減率 `,
	properties: {
		current_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_連結_実績`,
},
		prior_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第２四半期間_連結_実績`,
},
	},
} as const;

export const $ChangeInComprehensiveIncome_edjp_FinancialReportSummary_FY = {
	description: `包括利益増減率 `,
	properties: {
		current_year_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_実績`,
},
		prior_year_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度会計期間_連結_実績`,
},
	},
} as const;

export const $ChangeInComprehensiveIncome_edjp_FinancialReportSummary_HY_specific_business = {
	description: `包括利益増減率 `,
	properties: {
		current_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_連結_実績`,
},
		prior_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第２四半期間_連結_実績`,
},
	},
} as const;

export const $ChangeInComprehensiveIncome_edjp_FinancialReportSummary_Q1 = {
	description: `包括利益増減率 `,
	properties: {
		current_accumulated_q1_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第１四半期間_連結_実績`,
},
		prior_accumulated_q1_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第１四半期間_連結_実績`,
},
	},
} as const;

export const $ChangeInComprehensiveIncome_edjp_FinancialReportSummary_Q2 = {
	description: `包括利益増減率 `,
	properties: {
		current_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_連結_実績`,
},
		prior_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第２四半期間_連結_実績`,
},
	},
} as const;

export const $ChangeInComprehensiveIncome_edjp_FinancialReportSummary_Q3 = {
	description: `包括利益増減率 `,
	properties: {
		current_accumulated_q3_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第３四半期間_連結_実績`,
},
		prior_accumulated_q3_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第３四半期間_連結_実績`,
},
	},
} as const;

export const $ChangeInNetIncome_edjp_FinancialReportSummary_FY = {
	description: `増減率、当期純利益 `,
	properties: {
		current_year_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_実績`,
},
		next_accumulated_q2_duration_non_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `次年度期初から第２四半期間_非連結又は個別_予想`,
},
		next_accumulated_q2_duration_non_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `次年度期初から第２四半期間_非連結又は個別_下限`,
},
		next_accumulated_q2_duration_non_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `次年度期初から第２四半期間_非連結又は個別_上限`,
},
		next_year_duration_non_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `次年度会計期間_非連結又は個別_予想`,
},
		next_year_duration_non_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `次年度会計期間_非連結又は個別_下限`,
},
		next_year_duration_non_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `次年度会計期間_非連結又は個別_上限`,
},
		prior_year_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度会計期間_非連結又は個別_実績`,
},
	},
} as const;

export const $ChangeInNetIncome_edjp_FinancialReportSummary_HY_specific_business = {
	description: `増減率、当期純利益 `,
	properties: {
		current_accumulated_q2_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_非連結又は個別_実績`,
},
		current_year_duration_non_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_予想`,
},
		current_year_duration_non_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_下限`,
},
		current_year_duration_non_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_上限`,
},
		prior_accumulated_q2_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第２四半期間_非連結又は個別_実績`,
},
	},
} as const;

export const $ChangeInNetIncome_edjp_FinancialReportSummary_Q1 = {
	description: `増減率、当期純利益 `,
	properties: {
		current_accumulated_q1_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第１四半期間_非連結又は個別_実績`,
},
		current_accumulated_q2_duration_non_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_非連結又は個別_予想`,
},
		current_accumulated_q2_duration_non_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_非連結又は個別_下限`,
},
		current_accumulated_q2_duration_non_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_非連結又は個別_上限`,
},
		current_year_duration_non_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_予想`,
},
		current_year_duration_non_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_下限`,
},
		current_year_duration_non_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_上限`,
},
		prior_accumulated_q1_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第１四半期間_非連結又は個別_実績`,
},
	},
} as const;

export const $ChangeInNetIncome_edjp_FinancialReportSummary_Q2 = {
	description: `増減率、当期純利益 `,
	properties: {
		current_accumulated_q2_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_非連結又は個別_実績`,
},
		current_year_duration_non_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_予想`,
},
		current_year_duration_non_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_下限`,
},
		current_year_duration_non_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_上限`,
},
		prior_accumulated_q2_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第２四半期間_非連結又は個別_実績`,
},
	},
} as const;

export const $ChangeInNetOperatingRevenuesSE_edjp_FinancialReportSummary_Q2 = {
	description: `増減率、純営業収益、証券 `,
	properties: {
		current_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_連結_実績`,
},
		current_accumulated_q2_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_非連結又は個別_実績`,
},
		prior_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第２四半期間_連結_実績`,
},
		prior_accumulated_q2_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第２四半期間_非連結又は個別_実績`,
},
	},
} as const;

export const $ChangeInNetSales_edjp_FinancialReportSummary = {
	description: `増減率、売上高 `,
	properties: {
		current_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_連結_実績`,
},
		current_year_duration_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_予想`,
},
		current_year_duration_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_下限`,
},
		current_year_duration_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_上限`,
},
		prior_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第２四半期間_連結_実績`,
},
	},
} as const;

export const $ChangeInNetSales_edjp_FinancialReportSummary_FY = {
	description: `増減率、売上高 `,
	properties: {
		current_year_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_実績`,
},
		current_year_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_実績`,
},
		next_accumulated_q2_duration_non_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `次年度期初から第２四半期間_非連結又は個別_予想`,
},
		next_accumulated_q2_duration_non_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `次年度期初から第２四半期間_非連結又は個別_下限`,
},
		next_accumulated_q2_duration_non_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `次年度期初から第２四半期間_非連結又は個別_上限`,
},
		next_year_duration_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `次年度会計期間_連結_予想`,
},
		next_year_duration_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `次年度会計期間_連結_下限`,
},
		next_year_duration_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `次年度会計期間_連結_上限`,
},
		next_year_duration_non_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `次年度会計期間_非連結又は個別_予想`,
},
		next_year_duration_non_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `次年度会計期間_非連結又は個別_下限`,
},
		next_year_duration_non_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `次年度会計期間_非連結又は個別_上限`,
},
		prior_year_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度会計期間_連結_実績`,
},
		prior_year_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度会計期間_非連結又は個別_実績`,
},
	},
} as const;

export const $ChangeInNetSales_edjp_FinancialReportSummary_Q1 = {
	description: `増減率、売上高 `,
	properties: {
		current_accumulated_q1_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第１四半期間_連結_実績`,
},
		current_accumulated_q1_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第１四半期間_非連結又は個別_実績`,
},
		current_accumulated_q2_duration_non_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_非連結又は個別_予想`,
},
		current_accumulated_q2_duration_non_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_非連結又は個別_下限`,
},
		current_accumulated_q2_duration_non_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_非連結又は個別_上限`,
},
		current_year_duration_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_予想`,
},
		current_year_duration_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_下限`,
},
		current_year_duration_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_上限`,
},
		current_year_duration_non_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_予想`,
},
		current_year_duration_non_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_下限`,
},
		current_year_duration_non_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_上限`,
},
		prior_accumulated_q1_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第１四半期間_連結_実績`,
},
		prior_accumulated_q1_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第１四半期間_非連結又は個別_実績`,
},
	},
} as const;

export const $ChangeInNetSales_edjp_FinancialReportSummary_Q2 = {
	description: `増減率、売上高 `,
	properties: {
		current_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_連結_実績`,
},
		current_accumulated_q2_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_非連結又は個別_実績`,
},
		current_year_duration_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_予想`,
},
		current_year_duration_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_下限`,
},
		current_year_duration_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_上限`,
},
		current_year_duration_non_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_予想`,
},
		current_year_duration_non_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_下限`,
},
		current_year_duration_non_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_上限`,
},
		prior_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第２四半期間_連結_実績`,
},
		prior_accumulated_q2_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第２四半期間_非連結又は個別_実績`,
},
	},
} as const;

export const $ChangeInNetSales_edjp_FinancialReportSummary_Q3 = {
	description: `増減率、売上高 `,
	properties: {
		current_accumulated_q3_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第３四半期間_連結_実績`,
},
		current_year_duration_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_予想`,
},
		current_year_duration_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_下限`,
},
		current_year_duration_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_上限`,
},
		prior_accumulated_q3_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第３四半期間_連結_実績`,
},
	},
} as const;

export const $ChangeInOperatingIncome_edjp_FinancialReportSummary = {
	description: `増減率、営業利益 `,
	properties: {
		current_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_連結_実績`,
},
		current_year_duration_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_予想`,
},
		current_year_duration_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_下限`,
},
		current_year_duration_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_上限`,
},
		prior_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第２四半期間_連結_実績`,
},
	},
} as const;

export const $ChangeInOperatingIncome_edjp_FinancialReportSummary_FY = {
	description: `増減率、営業利益 `,
	properties: {
		current_year_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_実績`,
},
		current_year_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_実績`,
},
		next_accumulated_q2_duration_non_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `次年度期初から第２四半期間_非連結又は個別_予想`,
},
		next_accumulated_q2_duration_non_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `次年度期初から第２四半期間_非連結又は個別_下限`,
},
		next_accumulated_q2_duration_non_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `次年度期初から第２四半期間_非連結又は個別_上限`,
},
		next_year_duration_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `次年度会計期間_連結_予想`,
},
		next_year_duration_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `次年度会計期間_連結_下限`,
},
		next_year_duration_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `次年度会計期間_連結_上限`,
},
		next_year_duration_non_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `次年度会計期間_非連結又は個別_予想`,
},
		next_year_duration_non_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `次年度会計期間_非連結又は個別_下限`,
},
		next_year_duration_non_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `次年度会計期間_非連結又は個別_上限`,
},
		prior_year_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度会計期間_連結_実績`,
},
		prior_year_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度会計期間_非連結又は個別_実績`,
},
	},
} as const;

export const $ChangeInOperatingIncome_edjp_FinancialReportSummary_Q1 = {
	description: `増減率、営業利益 `,
	properties: {
		current_accumulated_q1_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第１四半期間_連結_実績`,
},
		current_accumulated_q1_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第１四半期間_非連結又は個別_実績`,
},
		current_accumulated_q2_duration_non_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_非連結又は個別_予想`,
},
		current_accumulated_q2_duration_non_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_非連結又は個別_下限`,
},
		current_accumulated_q2_duration_non_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_非連結又は個別_上限`,
},
		current_year_duration_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_予想`,
},
		current_year_duration_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_下限`,
},
		current_year_duration_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_上限`,
},
		current_year_duration_non_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_予想`,
},
		current_year_duration_non_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_下限`,
},
		current_year_duration_non_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_上限`,
},
		prior_accumulated_q1_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第１四半期間_連結_実績`,
},
		prior_accumulated_q1_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第１四半期間_非連結又は個別_実績`,
},
	},
} as const;

export const $ChangeInOperatingIncome_edjp_FinancialReportSummary_Q2 = {
	description: `増減率、営業利益 `,
	properties: {
		current_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_連結_実績`,
},
		current_accumulated_q2_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_非連結又は個別_実績`,
},
		current_year_duration_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_予想`,
},
		current_year_duration_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_下限`,
},
		current_year_duration_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_上限`,
},
		current_year_duration_non_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_予想`,
},
		current_year_duration_non_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_下限`,
},
		current_year_duration_non_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_上限`,
},
		prior_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第２四半期間_連結_実績`,
},
		prior_accumulated_q2_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第２四半期間_非連結又は個別_実績`,
},
	},
} as const;

export const $ChangeInOperatingIncome_edjp_FinancialReportSummary_Q3 = {
	description: `増減率、営業利益 `,
	properties: {
		current_accumulated_q3_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第３四半期間_連結_実績`,
},
		current_year_duration_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_予想`,
},
		current_year_duration_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_下限`,
},
		current_year_duration_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_上限`,
},
		prior_accumulated_q3_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第３四半期間_連結_実績`,
},
	},
} as const;

export const $ChangeInOperatingRevenuesSE_edjp_FinancialReportSummary_Q2 = {
	description: `増減率、営業収益、証券 `,
	properties: {
		current_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_連結_実績`,
},
		prior_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第２四半期間_連結_実績`,
},
	},
} as const;

export const $ChangeInOperatingRevenues_edjp_FinancialReportSummary_Q2 = {
	description: `増減率、営業収益 `,
	properties: {
		current_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_連結_実績`,
},
		current_accumulated_q2_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_非連結又は個別_実績`,
},
		current_year_duration_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_予想`,
},
		current_year_duration_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_下限`,
},
		current_year_duration_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_上限`,
},
		prior_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第２四半期間_連結_実績`,
},
		prior_accumulated_q2_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第２四半期間_非連結又は個別_実績`,
},
	},
} as const;

export const $ChangeInOrdinaryIncome_edjp_FinancialReportSummary = {
	description: `増減率、経常利益 `,
	properties: {
		current_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_連結_実績`,
},
		current_year_duration_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_予想`,
},
		current_year_duration_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_下限`,
},
		current_year_duration_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_上限`,
},
		prior_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第２四半期間_連結_実績`,
},
	},
} as const;

export const $ChangeInOrdinaryIncome_edjp_FinancialReportSummary_FY = {
	description: `増減率、経常利益 `,
	properties: {
		current_year_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_実績`,
},
		current_year_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_実績`,
},
		next_accumulated_q2_duration_non_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `次年度期初から第２四半期間_非連結又は個別_予想`,
},
		next_accumulated_q2_duration_non_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `次年度期初から第２四半期間_非連結又は個別_下限`,
},
		next_accumulated_q2_duration_non_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `次年度期初から第２四半期間_非連結又は個別_上限`,
},
		next_year_duration_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `次年度会計期間_連結_予想`,
},
		next_year_duration_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `次年度会計期間_連結_下限`,
},
		next_year_duration_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `次年度会計期間_連結_上限`,
},
		next_year_duration_non_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `次年度会計期間_非連結又は個別_予想`,
},
		next_year_duration_non_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `次年度会計期間_非連結又は個別_下限`,
},
		next_year_duration_non_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `次年度会計期間_非連結又は個別_上限`,
},
		prior_year_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度会計期間_連結_実績`,
},
		prior_year_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度会計期間_非連結又は個別_実績`,
},
	},
} as const;

export const $ChangeInOrdinaryIncome_edjp_FinancialReportSummary_HY_specific_business = {
	description: `増減率、経常利益 `,
	properties: {
		current_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_連結_実績`,
},
		current_accumulated_q2_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_非連結又は個別_実績`,
},
		current_year_duration_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_予想`,
},
		current_year_duration_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_下限`,
},
		current_year_duration_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_上限`,
},
		current_year_duration_non_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_予想`,
},
		current_year_duration_non_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_下限`,
},
		current_year_duration_non_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_上限`,
},
		prior_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第２四半期間_連結_実績`,
},
		prior_accumulated_q2_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第２四半期間_非連結又は個別_実績`,
},
	},
} as const;

export const $ChangeInOrdinaryIncome_edjp_FinancialReportSummary_Q1 = {
	description: `増減率、経常利益 `,
	properties: {
		current_accumulated_q1_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第１四半期間_連結_実績`,
},
		current_accumulated_q1_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第１四半期間_非連結又は個別_実績`,
},
		current_accumulated_q2_duration_non_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_非連結又は個別_予想`,
},
		current_accumulated_q2_duration_non_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_非連結又は個別_下限`,
},
		current_accumulated_q2_duration_non_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_非連結又は個別_上限`,
},
		current_year_duration_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_予想`,
},
		current_year_duration_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_下限`,
},
		current_year_duration_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_上限`,
},
		current_year_duration_non_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_予想`,
},
		current_year_duration_non_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_下限`,
},
		current_year_duration_non_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_上限`,
},
		prior_accumulated_q1_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第１四半期間_連結_実績`,
},
		prior_accumulated_q1_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第１四半期間_非連結又は個別_実績`,
},
	},
} as const;

export const $ChangeInOrdinaryIncome_edjp_FinancialReportSummary_Q2 = {
	description: `増減率、経常利益 `,
	properties: {
		current_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_連結_実績`,
},
		current_accumulated_q2_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_非連結又は個別_実績`,
},
		current_year_duration_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_予想`,
},
		current_year_duration_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_下限`,
},
		current_year_duration_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_上限`,
},
		current_year_duration_non_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_予想`,
},
		current_year_duration_non_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_下限`,
},
		current_year_duration_non_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_上限`,
},
		prior_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第２四半期間_連結_実績`,
},
		prior_accumulated_q2_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第２四半期間_非連結又は個別_実績`,
},
	},
} as const;

export const $ChangeInOrdinaryIncome_edjp_FinancialReportSummary_Q3 = {
	description: `増減率、経常利益 `,
	properties: {
		current_accumulated_q3_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第３四半期間_連結_実績`,
},
		current_year_duration_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_予想`,
},
		current_year_duration_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_下限`,
},
		current_year_duration_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_上限`,
},
		prior_accumulated_q3_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第３四半期間_連結_実績`,
},
	},
} as const;

export const $ChangeInOrdinaryRevenuesBK_edjp_FinancialReportSummary_HY_specific_business = {
	description: `増減率、経常収益、銀行 `,
	properties: {
		current_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_連結_実績`,
},
		current_accumulated_q2_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_非連結又は個別_実績`,
},
		prior_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第２四半期間_連結_実績`,
},
		prior_accumulated_q2_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第２四半期間_非連結又は個別_実績`,
},
	},
} as const;

export const $ChangeInProfitAttributableToOwnersOfParent_edjp_FinancialReportSummary = {
	description: `増減率、親会社株主に帰属する当期純利益 `,
	properties: {
		current_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_連結_実績`,
},
		current_year_duration_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_予想`,
},
		current_year_duration_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_下限`,
},
		current_year_duration_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_上限`,
},
		prior_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第２四半期間_連結_実績`,
},
	},
} as const;

export const $ChangeInProfitAttributableToOwnersOfParent_edjp_FinancialReportSummary_FY = {
	description: `増減率、親会社株主に帰属する当期純利益 `,
	properties: {
		current_year_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_実績`,
},
		next_year_duration_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `次年度会計期間_連結_予想`,
},
		next_year_duration_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `次年度会計期間_連結_下限`,
},
		next_year_duration_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `次年度会計期間_連結_上限`,
},
		prior_year_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度会計期間_連結_実績`,
},
	},
} as const;

export const $ChangeInProfitAttributableToOwnersOfParent_edjp_FinancialReportSummary_HY_specific_business = {
	description: `増減率、親会社株主に帰属する当期純利益 `,
	properties: {
		current_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_連結_実績`,
},
		current_year_duration_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_予想`,
},
		current_year_duration_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_下限`,
},
		current_year_duration_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_上限`,
},
		prior_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第２四半期間_連結_実績`,
},
	},
} as const;

export const $ChangeInProfitAttributableToOwnersOfParent_edjp_FinancialReportSummary_Q1 = {
	description: `増減率、親会社株主に帰属する当期純利益 `,
	properties: {
		current_accumulated_q1_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第１四半期間_連結_実績`,
},
		current_year_duration_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_予想`,
},
		current_year_duration_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_下限`,
},
		current_year_duration_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_上限`,
},
		prior_accumulated_q1_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第１四半期間_連結_実績`,
},
	},
} as const;

export const $ChangeInProfitAttributableToOwnersOfParent_edjp_FinancialReportSummary_Q2 = {
	description: `増減率、親会社株主に帰属する当期純利益 `,
	properties: {
		current_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_連結_実績`,
},
		current_year_duration_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_予想`,
},
		current_year_duration_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_下限`,
},
		current_year_duration_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_上限`,
},
		prior_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第２四半期間_連結_実績`,
},
	},
} as const;

export const $ChangeInProfitAttributableToOwnersOfParent_edjp_FinancialReportSummary_Q3 = {
	description: `増減率、親会社株主に帰属する当期純利益 `,
	properties: {
		current_accumulated_q3_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第３四半期間_連結_実績`,
},
		current_year_duration_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_予想`,
},
		current_year_duration_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_下限`,
},
		current_year_duration_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_上限`,
},
		prior_accumulated_q3_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第３四半期間_連結_実績`,
},
	},
} as const;

export const $CommemorativeDividend_edjp_FinancialReportSummary_Q2 = {
	description: `記念配当 `,
	properties: {
		current_accumulated_q2_duration_annual_member_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_年間_非連結又は個別_実績`,
},
	},
} as const;

export const $ComprehensiveIncome_edjp_FinancialReportSummary = {
	description: `包括利益 `,
	properties: {
		current_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_連結_実績`,
},
		prior_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第２四半期間_連結_実績`,
},
	},
} as const;

export const $ComprehensiveIncome_edjp_FinancialReportSummary_FY = {
	description: `包括利益 `,
	properties: {
		current_year_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_実績`,
},
		prior_year_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度会計期間_連結_実績`,
},
	},
} as const;

export const $ComprehensiveIncome_edjp_FinancialReportSummary_HY_specific_business = {
	description: `包括利益 `,
	properties: {
		current_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_連結_実績`,
},
		prior_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第２四半期間_連結_実績`,
},
	},
} as const;

export const $ComprehensiveIncome_edjp_FinancialReportSummary_Q1 = {
	description: `包括利益 `,
	properties: {
		current_accumulated_q1_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第１四半期間_連結_実績`,
},
		prior_accumulated_q1_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第１四半期間_連結_実績`,
},
	},
} as const;

export const $ComprehensiveIncome_edjp_FinancialReportSummary_Q2 = {
	description: `包括利益 `,
	properties: {
		current_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_連結_実績`,
},
		prior_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第２四半期間_連結_実績`,
},
	},
} as const;

export const $ComprehensiveIncome_edjp_FinancialReportSummary_Q3 = {
	description: `包括利益 `,
	properties: {
		current_accumulated_q3_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第３四半期間_連結_実績`,
},
		prior_accumulated_q3_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第３四半期間_連結_実績`,
},
	},
} as const;

export const $DilutedNetIncomePerShare_edjp_FinancialReportSummary = {
	description: `潜在株式調整後1株当たり当期純利益 `,
	properties: {
		current_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_連結_実績`,
},
		prior_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第２四半期間_連結_実績`,
},
	},
} as const;

export const $DilutedNetIncomePerShare_edjp_FinancialReportSummary_FY = {
	description: `潜在株式調整後1株当たり当期純利益 `,
	properties: {
		current_year_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_実績`,
},
		current_year_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_実績`,
},
		prior_year_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度会計期間_連結_実績`,
},
		prior_year_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度会計期間_非連結又は個別_実績`,
},
	},
} as const;

export const $DilutedNetIncomePerShare_edjp_FinancialReportSummary_HY_specific_business = {
	description: `潜在株式調整後1株当たり当期純利益 `,
	properties: {
		current_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_連結_実績`,
},
		prior_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第２四半期間_連結_実績`,
},
	},
} as const;

export const $DilutedNetIncomePerShare_edjp_FinancialReportSummary_Q1 = {
	description: `潜在株式調整後1株当たり当期純利益 `,
	properties: {
		current_accumulated_q1_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第１四半期間_連結_実績`,
},
		current_accumulated_q1_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第１四半期間_非連結又は個別_実績`,
},
		prior_accumulated_q1_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第１四半期間_連結_実績`,
},
		prior_accumulated_q1_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第１四半期間_非連結又は個別_実績`,
},
	},
} as const;

export const $DilutedNetIncomePerShare_edjp_FinancialReportSummary_Q2 = {
	description: `潜在株式調整後1株当たり当期純利益 `,
	properties: {
		current_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_連結_実績`,
},
		current_accumulated_q2_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_非連結又は個別_実績`,
},
		prior_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第２四半期間_連結_実績`,
},
		prior_accumulated_q2_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第２四半期間_非連結又は個別_実績`,
},
	},
} as const;

export const $DilutedNetIncomePerShare_edjp_FinancialReportSummary_Q3 = {
	description: `潜在株式調整後1株当たり当期純利益 `,
	properties: {
		current_accumulated_q3_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第３四半期間_連結_実績`,
},
		prior_accumulated_q3_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第３四半期間_連結_実績`,
},
	},
} as const;

export const $DividendPerShare_edjp_FinancialReportSummary = {
	description: `1株当たり配当金 `,
	properties: {
		current_year_duration_annual_member_non_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_年間_非連結又は個別_予想`,
},
		current_year_duration_annual_member_non_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_年間_非連結又は個別_下限`,
},
		current_year_duration_annual_member_non_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_年間_非連結又は個別_上限`,
},
		current_year_duration_first_quarter_member_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_1Q_非連結又は個別_実績`,
},
		current_year_duration_second_quarter_member_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_2Q_非連結又は個別_実績`,
},
		current_year_duration_third_quarter_member_non_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_3Q_非連結又は個別_予想`,
},
		current_year_duration_third_quarter_member_non_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_3Q_非連結又は個別_下限`,
},
		current_year_duration_third_quarter_member_non_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_3Q_非連結又は個別_上限`,
},
		current_year_duration_year_end_member_non_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_期末_非連結又は個別_予想`,
},
		current_year_duration_year_end_member_non_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_期末_非連結又は個別_下限`,
},
		current_year_duration_year_end_member_non_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_期末_非連結又は個別_上限`,
},
		prior_year_duration_annual_member_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度会計期間_年間_非連結又は個別_実績`,
},
		prior_year_duration_first_quarter_member_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度会計期間_1Q_非連結又は個別_実績`,
},
		prior_year_duration_second_quarter_member_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度会計期間_2Q_非連結又は個別_実績`,
},
		prior_year_duration_third_quarter_member_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度会計期間_3Q_非連結又は個別_実績`,
},
		prior_year_duration_year_end_member_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度会計期間_期末_非連結又は個別_実績`,
},
	},
} as const;

export const $DividendPerShare_edjp_FinancialReportSummary_FY = {
	description: `1株当たり配当金 `,
	properties: {
		current_year_duration_annual_member_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_年間_非連結又は個別_実績`,
},
		current_year_duration_first_quarter_member_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_1Q_非連結又は個別_実績`,
},
		current_year_duration_second_quarter_member_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_2Q_非連結又は個別_実績`,
},
		current_year_duration_third_quarter_member_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_3Q_非連結又は個別_実績`,
},
		current_year_duration_year_end_member_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_期末_非連結又は個別_実績`,
},
		next_year_duration_annual_member_non_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `次年度会計期間_年間_非連結又は個別_予想`,
},
		next_year_duration_annual_member_non_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `次年度会計期間_年間_非連結又は個別_下限`,
},
		next_year_duration_annual_member_non_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `次年度会計期間_年間_非連結又は個別_上限`,
},
		next_year_duration_first_quarter_member_non_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `次年度会計期間_1Q_非連結又は個別_予想`,
},
		next_year_duration_first_quarter_member_non_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `次年度会計期間_1Q_非連結又は個別_下限`,
},
		next_year_duration_first_quarter_member_non_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `次年度会計期間_1Q_非連結又は個別_上限`,
},
		next_year_duration_second_quarter_member_non_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `次年度会計期間_2Q_非連結又は個別_予想`,
},
		next_year_duration_second_quarter_member_non_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `次年度会計期間_2Q_非連結又は個別_下限`,
},
		next_year_duration_second_quarter_member_non_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `次年度会計期間_2Q_非連結又は個別_上限`,
},
		next_year_duration_third_quarter_member_non_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `次年度会計期間_3Q_非連結又は個別_予想`,
},
		next_year_duration_third_quarter_member_non_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `次年度会計期間_3Q_非連結又は個別_下限`,
},
		next_year_duration_third_quarter_member_non_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `次年度会計期間_3Q_非連結又は個別_上限`,
},
		next_year_duration_year_end_member_non_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `次年度会計期間_期末_非連結又は個別_予想`,
},
		next_year_duration_year_end_member_non_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `次年度会計期間_期末_非連結又は個別_下限`,
},
		next_year_duration_year_end_member_non_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `次年度会計期間_期末_非連結又は個別_上限`,
},
		prior_year_duration_annual_member_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度会計期間_年間_非連結又は個別_実績`,
},
		prior_year_duration_first_quarter_member_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度会計期間_1Q_非連結又は個別_実績`,
},
		prior_year_duration_second_quarter_member_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度会計期間_2Q_非連結又は個別_実績`,
},
		prior_year_duration_third_quarter_member_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度会計期間_3Q_非連結又は個別_実績`,
},
		prior_year_duration_year_end_member_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度会計期間_期末_非連結又は個別_実績`,
},
	},
} as const;

export const $DividendPerShare_edjp_FinancialReportSummary_HY_specific_business = {
	description: `1株当たり配当金 `,
	properties: {
		current_year_duration_annual_member_non_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_年間_非連結又は個別_予想`,
},
		current_year_duration_annual_member_non_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_年間_非連結又は個別_下限`,
},
		current_year_duration_annual_member_non_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_年間_非連結又は個別_上限`,
},
		current_year_duration_first_quarter_member_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_1Q_非連結又は個別_実績`,
},
		current_year_duration_second_quarter_member_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_2Q_非連結又は個別_実績`,
},
		current_year_duration_third_quarter_member_non_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_3Q_非連結又は個別_予想`,
},
		current_year_duration_third_quarter_member_non_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_3Q_非連結又は個別_下限`,
},
		current_year_duration_third_quarter_member_non_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_3Q_非連結又は個別_上限`,
},
		current_year_duration_year_end_member_non_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_期末_非連結又は個別_予想`,
},
		current_year_duration_year_end_member_non_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_期末_非連結又は個別_下限`,
},
		current_year_duration_year_end_member_non_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_期末_非連結又は個別_上限`,
},
		prior_year_duration_annual_member_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度会計期間_年間_非連結又は個別_実績`,
},
		prior_year_duration_first_quarter_member_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度会計期間_1Q_非連結又は個別_実績`,
},
		prior_year_duration_second_quarter_member_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度会計期間_2Q_非連結又は個別_実績`,
},
		prior_year_duration_third_quarter_member_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度会計期間_3Q_非連結又は個別_実績`,
},
		prior_year_duration_year_end_member_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度会計期間_期末_非連結又は個別_実績`,
},
	},
} as const;

export const $DividendPerShare_edjp_FinancialReportSummary_Q1 = {
	description: `1株当たり配当金 `,
	properties: {
		current_year_duration_annual_member_non_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_年間_非連結又は個別_予想`,
},
		current_year_duration_annual_member_non_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_年間_非連結又は個別_下限`,
},
		current_year_duration_annual_member_non_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_年間_非連結又は個別_上限`,
},
		current_year_duration_first_quarter_member_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_1Q_非連結又は個別_実績`,
},
		current_year_duration_second_quarter_member_non_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_2Q_非連結又は個別_予想`,
},
		current_year_duration_second_quarter_member_non_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_2Q_非連結又は個別_下限`,
},
		current_year_duration_second_quarter_member_non_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_2Q_非連結又は個別_上限`,
},
		current_year_duration_third_quarter_member_non_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_3Q_非連結又は個別_予想`,
},
		current_year_duration_third_quarter_member_non_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_3Q_非連結又は個別_下限`,
},
		current_year_duration_third_quarter_member_non_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_3Q_非連結又は個別_上限`,
},
		current_year_duration_year_end_member_non_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_期末_非連結又は個別_予想`,
},
		current_year_duration_year_end_member_non_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_期末_非連結又は個別_下限`,
},
		current_year_duration_year_end_member_non_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_期末_非連結又は個別_上限`,
},
		prior_year_duration_annual_member_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度会計期間_年間_非連結又は個別_実績`,
},
		prior_year_duration_first_quarter_member_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度会計期間_1Q_非連結又は個別_実績`,
},
		prior_year_duration_second_quarter_member_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度会計期間_2Q_非連結又は個別_実績`,
},
		prior_year_duration_third_quarter_member_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度会計期間_3Q_非連結又は個別_実績`,
},
		prior_year_duration_year_end_member_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度会計期間_期末_非連結又は個別_実績`,
},
	},
} as const;

export const $DividendPerShare_edjp_FinancialReportSummary_Q2 = {
	description: `1株当たり配当金 `,
	properties: {
		current_year_duration_annual_member_non_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_年間_非連結又は個別_予想`,
},
		current_year_duration_annual_member_non_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_年間_非連結又は個別_下限`,
},
		current_year_duration_annual_member_non_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_年間_非連結又は個別_上限`,
},
		current_year_duration_first_quarter_member_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_1Q_非連結又は個別_実績`,
},
		current_year_duration_second_quarter_member_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_2Q_非連結又は個別_実績`,
},
		current_year_duration_third_quarter_member_non_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_3Q_非連結又は個別_予想`,
},
		current_year_duration_third_quarter_member_non_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_3Q_非連結又は個別_下限`,
},
		current_year_duration_third_quarter_member_non_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_3Q_非連結又は個別_上限`,
},
		current_year_duration_year_end_member_non_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_期末_非連結又は個別_予想`,
},
		current_year_duration_year_end_member_non_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_期末_非連結又は個別_下限`,
},
		current_year_duration_year_end_member_non_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_期末_非連結又は個別_上限`,
},
		prior_year_duration_annual_member_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度会計期間_年間_非連結又は個別_実績`,
},
		prior_year_duration_first_quarter_member_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度会計期間_1Q_非連結又は個別_実績`,
},
		prior_year_duration_second_quarter_member_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度会計期間_2Q_非連結又は個別_実績`,
},
		prior_year_duration_third_quarter_member_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度会計期間_3Q_非連結又は個別_実績`,
},
		prior_year_duration_year_end_member_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度会計期間_期末_非連結又は個別_実績`,
},
	},
} as const;

export const $DividendPerShare_edjp_FinancialReportSummary_Q3 = {
	description: `1株当たり配当金 `,
	properties: {
		current_year_duration_annual_member_non_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_年間_非連結又は個別_予想`,
},
		current_year_duration_annual_member_non_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_年間_非連結又は個別_下限`,
},
		current_year_duration_annual_member_non_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_年間_非連結又は個別_上限`,
},
		current_year_duration_first_quarter_member_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_1Q_非連結又は個別_実績`,
},
		current_year_duration_second_quarter_member_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_2Q_非連結又は個別_実績`,
},
		current_year_duration_third_quarter_member_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_3Q_非連結又は個別_実績`,
},
		current_year_duration_year_end_member_non_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_期末_非連結又は個別_予想`,
},
		current_year_duration_year_end_member_non_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_期末_非連結又は個別_下限`,
},
		current_year_duration_year_end_member_non_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_期末_非連結又は個別_上限`,
},
		prior_year_duration_annual_member_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度会計期間_年間_非連結又は個別_実績`,
},
		prior_year_duration_first_quarter_member_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度会計期間_1Q_非連結又は個別_実績`,
},
		prior_year_duration_second_quarter_member_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度会計期間_2Q_非連結又は個別_実績`,
},
		prior_year_duration_third_quarter_member_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度会計期間_3Q_非連結又は個別_実績`,
},
		prior_year_duration_year_end_member_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度会計期間_期末_非連結又は個別_実績`,
},
	},
} as const;

export const $ExtraDividend_edjp_FinancialReportSummary_Q2 = {
	description: `特別配当 `,
	properties: {
		current_accumulated_q2_duration_annual_member_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_年間_非連結又は個別_実績`,
},
	},
} as const;

export const $GroupingNonFraction = {
	properties: {
		report_type: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
	isRequired: true,
},
		specific_business: {
	type: 'any-of',
	contains: [{
	type: 'boolean',
}, {
	type: 'null',
}],
	isRequired: true,
},
		ixbrl_role: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
	isRequired: true,
},
		current_period: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
	isRequired: true,
},
		name: {
	type: 'string',
	isRequired: true,
},
		context: {
	type: 'string',
	isRequired: true,
},
		label: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
	isRequired: true,
},
		context_label: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
	isRequired: true,
},
	},
} as const;

export const $GroupingNonFractionList = {
	properties: {
		count: {
	type: 'number',
	isRequired: true,
},
		item: {
	type: 'array',
	contains: {
		type: 'GroupingNonFraction',
	},
	isRequired: true,
},
	},
} as const;

export const $HTTPValidationError = {
	properties: {
		detail: {
	type: 'array',
	contains: {
		type: 'ValidationError',
	},
},
	},
} as const;

export const $InvestmentProfitLossOnEquityMethod_edjp_FinancialReportSummary_FY = {
	description: `持分法投資損益 `,
	properties: {
		current_year_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_実績`,
},
		current_year_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_実績`,
},
		prior_year_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度会計期間_連結_実績`,
},
		prior_year_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度会計期間_非連結又は個別_実績`,
},
	},
} as const;

export const $ItemCreate = {
	properties: {
		title: {
	type: 'string',
	isRequired: true,
	maxLength: 255,
	minLength: 1,
},
		description: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 255,
}, {
	type: 'null',
}],
},
	},
} as const;

export const $ItemPublic = {
	properties: {
		title: {
	type: 'string',
	isRequired: true,
	maxLength: 255,
	minLength: 1,
},
		description: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 255,
}, {
	type: 'null',
}],
},
		id: {
	type: 'string',
	isRequired: true,
	format: 'uuid',
},
		owner_id: {
	type: 'string',
	isRequired: true,
	format: 'uuid',
},
	},
} as const;

export const $ItemUpdate = {
	properties: {
		title: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 255,
	minLength: 1,
}, {
	type: 'null',
}],
},
		description: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 255,
}, {
	type: 'null',
}],
},
	},
} as const;

export const $ItemsPublic = {
	properties: {
		data: {
	type: 'array',
	contains: {
		type: 'ItemPublic',
	},
	isRequired: true,
},
		count: {
	type: 'number',
	isRequired: true,
},
	},
} as const;

export const $IxCalculationArcCreate_Input = {
	description: `iXBRLの計算アーク情報を表すクラス`,
	properties: {
		item_key: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 36,
	minLength: 36,
}, {
	type: 'null',
}],
	isRequired: true,
},
		head_item_key: {
	type: 'string',
	isRequired: true,
},
		attr_value: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 255,
}, {
	type: 'null',
}],
	isRequired: true,
},
		xlink_order: {
	type: 'any-of',
	contains: [{
	type: 'number',
}, {
	type: 'string',
}, {
	type: 'null',
}],
},
		xlink_weight: {
	type: 'any-of',
	contains: [{
	type: 'number',
}, {
	type: 'string',
}, {
	type: 'null',
}],
},
		xlink_type: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 255,
}, {
	type: 'null',
}],
	isRequired: true,
},
		xlink_arcrole: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 255,
}, {
	type: 'null',
}],
	isRequired: true,
},
		xlink_to: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
		xlink_from: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
		source_file_id: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 36,
}, {
	type: 'null',
}],
	isRequired: true,
},
	},
} as const;

export const $IxCalculationArcCreate_Output = {
	description: `iXBRLの計算アーク情報を表すクラス`,
	properties: {
		item_key: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 36,
	minLength: 36,
}, {
	type: 'null',
}],
	isRequired: true,
},
		head_item_key: {
	type: 'string',
	isRequired: true,
},
		attr_value: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 255,
}, {
	type: 'null',
}],
	isRequired: true,
},
		xlink_order: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
		xlink_weight: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
		xlink_type: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 255,
}, {
	type: 'null',
}],
	isRequired: true,
},
		xlink_arcrole: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 255,
}, {
	type: 'null',
}],
	isRequired: true,
},
		xlink_to: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
		xlink_from: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
		source_file_id: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 36,
}, {
	type: 'null',
}],
	isRequired: true,
},
	},
} as const;

export const $IxCalculationArcCreateList = {
	description: `iXBRLの計算アーク情報を作成するためのクラス`,
	properties: {
		data: {
	type: 'array',
	contains: {
		type: 'IxCalculationArcCreate_Input',
	},
	isRequired: true,
},
	},
} as const;

export const $IxCalculationLocCreate = {
	description: `iXBRLの計算ロケーション情報を表すクラス`,
	properties: {
		item_key: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 36,
	minLength: 36,
}, {
	type: 'null',
}],
	isRequired: true,
},
		head_item_key: {
	type: 'string',
	isRequired: true,
},
		attr_value: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 255,
}, {
	type: 'null',
}],
	isRequired: true,
},
		xlink_href: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
	isRequired: true,
},
		xlink_type: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 255,
}, {
	type: 'null',
}],
	isRequired: true,
},
		xlink_schema: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 255,
}, {
	type: 'null',
}],
	isRequired: true,
},
		xlink_label: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
		source_file_id: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 36,
}, {
	type: 'null',
}],
	isRequired: true,
},
	},
} as const;

export const $IxCalculationLocCreateList = {
	description: `iXBRLの計算ロケーション情報を作成するためのクラス`,
	properties: {
		data: {
	type: 'array',
	contains: {
		type: 'IxCalculationLocCreate',
	},
	isRequired: true,
},
	},
} as const;

export const $IxDefinitionArcCreate_Input = {
	description: `XBRLの表示リンクアークを表すクラス`,
	properties: {
		item_key: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 36,
	minLength: 36,
}, {
	type: 'null',
}],
	isRequired: true,
},
		head_item_key: {
	type: 'string',
	isRequired: true,
},
		attr_value: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 255,
}, {
	type: 'null',
}],
	isRequired: true,
},
		xlink_order: {
	type: 'any-of',
	contains: [{
	type: 'number',
}, {
	type: 'string',
}],
	isRequired: true,
},
		xlink_weight: {
	type: 'any-of',
	contains: [{
	type: 'number',
}, {
	type: 'string',
}, {
	type: 'null',
}],
},
		xlink_type: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 255,
}, {
	type: 'null',
}],
	isRequired: true,
},
		xlink_arcrole: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 255,
}, {
	type: 'null',
}],
	isRequired: true,
},
		xlink_to: {
	type: 'string',
	isRequired: true,
},
		xlink_from: {
	type: 'string',
	isRequired: true,
},
		source_file_id: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 36,
}, {
	type: 'null',
}],
	isRequired: true,
},
	},
} as const;

export const $IxDefinitionArcCreate_Output = {
	description: `XBRLの表示リンクアークを表すクラス`,
	properties: {
		item_key: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 36,
	minLength: 36,
}, {
	type: 'null',
}],
	isRequired: true,
},
		head_item_key: {
	type: 'string',
	isRequired: true,
},
		attr_value: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 255,
}, {
	type: 'null',
}],
	isRequired: true,
},
		xlink_order: {
	type: 'string',
	isRequired: true,
},
		xlink_weight: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
		xlink_type: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 255,
}, {
	type: 'null',
}],
	isRequired: true,
},
		xlink_arcrole: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 255,
}, {
	type: 'null',
}],
	isRequired: true,
},
		xlink_to: {
	type: 'string',
	isRequired: true,
},
		xlink_from: {
	type: 'string',
	isRequired: true,
},
		source_file_id: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 36,
}, {
	type: 'null',
}],
	isRequired: true,
},
	},
} as const;

export const $IxDefinitionArcCreateList = {
	description: `XBRLの表示リンクアークを作成するためのクラス`,
	properties: {
		data: {
	type: 'array',
	contains: {
		type: 'IxDefinitionArcCreate_Input',
	},
	isRequired: true,
},
	},
} as const;

export const $IxDefinitionLocCreate = {
	description: `XBRLの表示リンクロケーションを表すクラス`,
	properties: {
		item_key: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 36,
	minLength: 36,
}, {
	type: 'null',
}],
	isRequired: true,
},
		head_item_key: {
	type: 'string',
	isRequired: true,
},
		attr_value: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 255,
}, {
	type: 'null',
}],
	isRequired: true,
},
		xlink_href: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
	isRequired: true,
},
		xlink_type: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 255,
}, {
	type: 'null',
}],
	isRequired: true,
},
		xlink_schema: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 255,
}, {
	type: 'null',
}],
	isRequired: true,
},
		xlink_label: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
		source_file_id: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 36,
}, {
	type: 'null',
}],
	isRequired: true,
},
	},
} as const;

export const $IxDefinitionLocCreateList = {
	description: `XBRLの表示リンクロケーションを作成するためのクラス`,
	properties: {
		data: {
	type: 'array',
	contains: {
		type: 'IxDefinitionLocCreate',
	},
	isRequired: true,
},
	},
} as const;

export const $IxFilePathCreate = {
	description: `iXBRLのファイルパス情報を作成するためのクラス`,
	properties: {
		item_key: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 36,
	minLength: 36,
}, {
	type: 'null',
}],
	isRequired: true,
},
		path: {
	type: 'string',
},
		head_item_key: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 36,
}, {
	type: 'null',
}],
	isRequired: true,
},
	},
} as const;

export const $IxFilePathPublic = {
	description: `iXBRLのファイルパス情報を公開するためのクラス`,
	properties: {
		path: {
	type: 'string',
	isRequired: true,
},
		head_item_key: {
	type: 'string',
	isRequired: true,
},
	},
} as const;

export const $IxHeadTitleCreate = {
	description: `iXBRLのヘッダー情報を表すクラス`,
	properties: {
		item_key: {
	type: 'string',
	isRequired: true,
	maxLength: 36,
	minLength: 36,
},
		company_name: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
		securities_code: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
		document_name: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
		reporting_date: {
	type: 'any-of',
	contains: [{
	type: 'string',
	format: 'date',
}, {
	type: 'null',
}],
},
		current_period: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
		report_type: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
		listed_market: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
		market_section: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
		url: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
		is_bs: {
	type: 'any-of',
	contains: [{
	type: 'boolean',
}, {
	type: 'null',
}],
},
		is_pl: {
	type: 'any-of',
	contains: [{
	type: 'boolean',
}, {
	type: 'null',
}],
},
		is_cf: {
	type: 'any-of',
	contains: [{
	type: 'boolean',
}, {
	type: 'null',
}],
},
		is_ci: {
	type: 'any-of',
	contains: [{
	type: 'boolean',
}, {
	type: 'null',
}],
},
		is_sce: {
	type: 'any-of',
	contains: [{
	type: 'boolean',
}, {
	type: 'null',
}],
},
		is_sfp: {
	type: 'any-of',
	contains: [{
	type: 'boolean',
}, {
	type: 'null',
}],
},
		fy_year_end: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
		tel: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
		specific_business: {
	type: 'any-of',
	contains: [{
	type: 'boolean',
}, {
	type: 'null',
}],
},
	},
} as const;

export const $IxHeadTitleCreateList = {
	description: `iXBRLのヘッダー情報のリストを表すクラス`,
	properties: {
		data: {
	type: 'array',
	contains: {
		type: 'IxHeadTitleCreate',
	},
	isRequired: true,
},
	},
} as const;

export const $IxHeadTitlePublic = {
	description: `iXBRLのヘッダー情報を表すクラス`,
	properties: {
		item_key: {
	type: 'string',
	isRequired: true,
},
		company_name: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
	isRequired: true,
},
		securities_code: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
	isRequired: true,
},
		document_name: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
	isRequired: true,
},
		reporting_date: {
	type: 'any-of',
	contains: [{
	type: 'string',
	format: 'date',
}, {
	type: 'null',
}],
	isRequired: true,
},
		current_period: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
	isRequired: true,
},
		report_type: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
	isRequired: true,
},
		listed_market: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
	isRequired: true,
},
		market_section: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
	isRequired: true,
},
		url: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
	isRequired: true,
},
		is_bs: {
	type: 'any-of',
	contains: [{
	type: 'boolean',
}, {
	type: 'null',
}],
	isRequired: true,
},
		is_pl: {
	type: 'any-of',
	contains: [{
	type: 'boolean',
}, {
	type: 'null',
}],
	isRequired: true,
},
		is_cf: {
	type: 'any-of',
	contains: [{
	type: 'boolean',
}, {
	type: 'null',
}],
	isRequired: true,
},
		is_ci: {
	type: 'any-of',
	contains: [{
	type: 'boolean',
}, {
	type: 'null',
}],
	isRequired: true,
},
		is_sce: {
	type: 'any-of',
	contains: [{
	type: 'boolean',
}, {
	type: 'null',
}],
	isRequired: true,
},
		is_sfp: {
	type: 'any-of',
	contains: [{
	type: 'boolean',
}, {
	type: 'null',
}],
	isRequired: true,
},
		fy_year_end: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
	isRequired: true,
},
		tel: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
	isRequired: true,
},
		is_div_rev: {
	type: 'any-of',
	contains: [{
	type: 'boolean',
}, {
	type: 'null',
}],
	isRequired: true,
},
		div_inc_rt: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
	isRequired: true,
},
		is_fcst_rev: {
	type: 'any-of',
	contains: [{
	type: 'boolean',
}, {
	type: 'null',
}],
	isRequired: true,
},
		fcst_oi_gr_rt: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
	isRequired: true,
},
		oi_prog_rt: {
	type: 'any-of',
	contains: [{
	type: 'number',
}, {
	type: 'null',
}],
	isRequired: true,
},
		specific_business: {
	type: 'any-of',
	contains: [{
	type: 'boolean',
}, {
	type: 'null',
}],
	isRequired: true,
},
	},
} as const;

export const $IxHeadTitlesPublic = {
	description: `iXBRLのヘッダー情報のリストを表すクラス`,
	properties: {
		data: {
	type: 'array',
	contains: {
		type: 'IxHeadTitlePublic',
	},
	isRequired: true,
},
		count: {
	type: 'number',
	isRequired: true,
},
	},
} as const;

export const $IxLabelArcCreate = {
	description: `iXBRLのラベルアーク情報を作成するためのクラス`,
	properties: {
		item_key: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 36,
	minLength: 36,
}, {
	type: 'null',
}],
	isRequired: true,
},
		xlink_type: {
	type: 'string',
	isRequired: true,
	maxLength: 255,
},
		xlink_arcrole: {
	type: 'string',
	isRequired: true,
	maxLength: 255,
},
		xlink_from: {
	type: 'string',
},
		xlink_to: {
	type: 'string',
},
		source_file_id: {
	type: 'string',
	isRequired: true,
	maxLength: 36,
},
	},
} as const;

export const $IxLabelArcCreateList = {
	description: `iXBRLの計算アーク情報を作成するためのクラス`,
	properties: {
		data: {
	type: 'array',
	contains: {
		type: 'IxLabelArcCreate',
	},
	isRequired: true,
},
	},
} as const;

export const $IxLabelLocCreate = {
	description: `iXBRLのラベルロケーション情報を作成するためのクラス`,
	properties: {
		item_key: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 36,
	minLength: 36,
}, {
	type: 'null',
}],
	isRequired: true,
},
		xlink_href: {
	type: 'string',
},
		xlink_label: {
	type: 'string',
},
		xlink_type: {
	type: 'string',
	isRequired: true,
	maxLength: 255,
},
		xlink_schema: {
	type: 'string',
	isRequired: true,
	maxLength: 255,
},
		source_file_id: {
	type: 'string',
	isRequired: true,
	maxLength: 36,
},
	},
} as const;

export const $IxLabelLocCreateList = {
	description: `iXBRLのラベルロケーション情報を作成するためのクラス`,
	properties: {
		data: {
	type: 'array',
	contains: {
		type: 'IxLabelLocCreate',
	},
	isRequired: true,
},
	},
} as const;

export const $IxLabelValueCreate = {
	description: `iXBRLのラベルリンク情報を作成するためのクラス`,
	properties: {
		item_key: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 36,
	minLength: 36,
}, {
	type: 'null',
}],
	isRequired: true,
},
		xlink_type: {
	type: 'string',
	isRequired: true,
	maxLength: 255,
},
		xlink_label: {
	type: 'string',
},
		xlink_role: {
	type: 'string',
	isRequired: true,
	maxLength: 255,
},
		xml_lang: {
	type: 'string',
	isRequired: true,
	maxLength: 255,
},
		label: {
	type: 'string',
},
		source_file_id: {
	type: 'string',
	isRequired: true,
	maxLength: 36,
},
	},
} as const;

export const $IxLabelValueCreateList = {
	description: `iXBRLのラベルリンク情報を作成するためのクラス`,
	properties: {
		data: {
	type: 'array',
	contains: {
		type: 'IxLabelValueCreate',
	},
	isRequired: true,
},
	},
} as const;

export const $IxNonFractionCreate_Input = {
	description: `iXBRLの非分数情報を表すクラス`,
	properties: {
		item_key: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 36,
	minLength: 36,
}, {
	type: 'null',
}],
	isRequired: true,
},
		head_item_key: {
	type: 'string',
	isRequired: true,
	maxLength: 255,
},
		context: {
	type: 'string',
	isRequired: true,
	maxLength: 255,
},
		decimals: {
	type: 'any-of',
	contains: [{
	type: 'number',
}, {
	type: 'string',
}, {
	type: 'null',
}],
},
		format: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 255,
}, {
	type: 'null',
}],
	isRequired: true,
},
		name: {
	type: 'string',
},
		scale: {
	type: 'any-of',
	contains: [{
	type: 'number',
}, {
	type: 'string',
}, {
	type: 'null',
}],
},
		sign: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 255,
}, {
	type: 'null',
}],
},
		unit_ref: {
	type: 'string',
	isRequired: true,
	maxLength: 255,
},
		xsi_nil: {
	type: 'any-of',
	contains: [{
	type: 'boolean',
}, {
	type: 'null',
}],
},
		numeric: {
	type: 'any-of',
	contains: [{
	type: 'number',
}, {
	type: 'string',
}, {
	type: 'null',
}],
},
		report_type: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 4,
}, {
	type: 'null',
}],
	isRequired: true,
},
		ixbrl_role: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 255,
}, {
	type: 'null',
}],
	isRequired: true,
},
		source_file_id: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 36,
}, {
	type: 'null',
}],
	isRequired: true,
},
		xbrl_type: {
	type: 'string',
	isRequired: true,
	maxLength: 255,
},
		display_numeric: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 255,
}, {
	type: 'null',
}],
	isRequired: true,
},
		display_scale: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 255,
}, {
	type: 'null',
}],
	isRequired: true,
},
	},
} as const;

export const $IxNonFractionCreate_Output = {
	description: `iXBRLの非分数情報を表すクラス`,
	properties: {
		item_key: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 36,
	minLength: 36,
}, {
	type: 'null',
}],
	isRequired: true,
},
		head_item_key: {
	type: 'string',
	isRequired: true,
	maxLength: 255,
},
		context: {
	type: 'string',
	isRequired: true,
	maxLength: 255,
},
		decimals: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
		format: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 255,
}, {
	type: 'null',
}],
	isRequired: true,
},
		name: {
	type: 'string',
},
		scale: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
		sign: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 255,
}, {
	type: 'null',
}],
},
		unit_ref: {
	type: 'string',
	isRequired: true,
	maxLength: 255,
},
		xsi_nil: {
	type: 'any-of',
	contains: [{
	type: 'boolean',
}, {
	type: 'null',
}],
},
		numeric: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
		report_type: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 4,
}, {
	type: 'null',
}],
	isRequired: true,
},
		ixbrl_role: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 255,
}, {
	type: 'null',
}],
	isRequired: true,
},
		source_file_id: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 36,
}, {
	type: 'null',
}],
	isRequired: true,
},
		xbrl_type: {
	type: 'string',
	isRequired: true,
	maxLength: 255,
},
		display_numeric: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 255,
}, {
	type: 'null',
}],
	isRequired: true,
},
		display_scale: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 255,
}, {
	type: 'null',
}],
	isRequired: true,
},
	},
} as const;

export const $IxNonFractionCreateList = {
	description: `iXBRLの非分数情報を作成するためのクラス`,
	properties: {
		data: {
	type: 'array',
	contains: {
		type: 'IxNonFractionCreate_Input',
	},
	isRequired: true,
},
	},
} as const;

export const $IxNonFractionPublic = {
	description: `iXBRLの非分数情報を表すクラス`,
	properties: {
		id: {
	type: 'any-of',
	contains: [{
	type: 'number',
}, {
	type: 'null',
}],
	isRequired: true,
},
		insert_date: {
	type: 'string',
	isRequired: true,
	format: 'date-time',
},
		update_date: {
	type: 'string',
	isRequired: true,
	format: 'date-time',
},
		head_item_key: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
	isRequired: true,
},
		context: {
	type: 'string',
	isRequired: true,
},
		decimals: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
	isRequired: true,
},
		format: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
	isRequired: true,
},
		name: {
	type: 'string',
	isRequired: true,
},
		scale: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
	isRequired: true,
},
		sign: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
	isRequired: true,
},
		unit_ref: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
	isRequired: true,
},
		xsi_nil: {
	type: 'any-of',
	contains: [{
	type: 'boolean',
}, {
	type: 'null',
}],
	isRequired: true,
},
		numeric: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
	isRequired: true,
},
		report_type: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
	isRequired: true,
},
		ixbrl_role: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
	isRequired: true,
},
		source_file_id: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
	isRequired: true,
},
		xbrl_type: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
	isRequired: true,
},
		display_numeric: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
	isRequired: true,
},
		display_scale: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
	isRequired: true,
},
	},
} as const;

export const $IxNonNumericCreate = {
	description: `iXBRLの非数値情報を表すクラス`,
	properties: {
		item_key: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 36,
	minLength: 36,
}, {
	type: 'null',
}],
	isRequired: true,
},
		head_item_key: {
	type: 'string',
	isRequired: true,
	maxLength: 255,
},
		context: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 255,
}, {
	type: 'null',
}],
	isRequired: true,
},
		name: {
	type: 'string',
},
		xsi_nil: {
	type: 'any-of',
	contains: [{
	type: 'boolean',
}, {
	type: 'null',
}],
},
		escape: {
	type: 'boolean',
	default: false,
},
		format: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 255,
}, {
	type: 'null',
}],
},
		value: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
		report_type: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 4,
}, {
	type: 'null',
}],
	isRequired: true,
},
		ixbrl_role: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 255,
}, {
	type: 'null',
}],
	isRequired: true,
},
		source_file_id: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 36,
}, {
	type: 'null',
}],
	isRequired: true,
},
		xbrl_type: {
	type: 'string',
	isRequired: true,
	maxLength: 255,
},
	},
} as const;

export const $IxNonNumericCreateList = {
	description: `iXBRLの非数値情報を作成するためのクラス`,
	properties: {
		data: {
	type: 'array',
	contains: {
		type: 'IxNonNumericCreate',
	},
	isRequired: true,
},
	},
} as const;

export const $IxPresentationArcCreate_Input = {
	description: `XBRLの表示リンクアークを表すクラス`,
	properties: {
		item_key: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 36,
	minLength: 36,
}, {
	type: 'null',
}],
	isRequired: true,
},
		head_item_key: {
	type: 'string',
	isRequired: true,
},
		attr_value: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 255,
}, {
	type: 'null',
}],
	isRequired: true,
},
		xlink_order: {
	type: 'any-of',
	contains: [{
	type: 'number',
}, {
	type: 'string',
}, {
	type: 'null',
}],
},
		xlink_weight: {
	type: 'any-of',
	contains: [{
	type: 'number',
}, {
	type: 'string',
}, {
	type: 'null',
}],
},
		xlink_type: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 255,
}, {
	type: 'null',
}],
	isRequired: true,
},
		xlink_arcrole: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 255,
}, {
	type: 'null',
}],
	isRequired: true,
},
		xlink_to: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
		xlink_from: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
		source_file_id: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 36,
}, {
	type: 'null',
}],
	isRequired: true,
},
	},
} as const;

export const $IxPresentationArcCreate_Output = {
	description: `XBRLの表示リンクアークを表すクラス`,
	properties: {
		item_key: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 36,
	minLength: 36,
}, {
	type: 'null',
}],
	isRequired: true,
},
		head_item_key: {
	type: 'string',
	isRequired: true,
},
		attr_value: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 255,
}, {
	type: 'null',
}],
	isRequired: true,
},
		xlink_order: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
		xlink_weight: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
		xlink_type: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 255,
}, {
	type: 'null',
}],
	isRequired: true,
},
		xlink_arcrole: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 255,
}, {
	type: 'null',
}],
	isRequired: true,
},
		xlink_to: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
		xlink_from: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
		source_file_id: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 36,
}, {
	type: 'null',
}],
	isRequired: true,
},
	},
} as const;

export const $IxPresentationArcCreateList = {
	description: `XBRLの表示リンクアークを作成するためのクラス`,
	properties: {
		data: {
	type: 'array',
	contains: {
		type: 'IxPresentationArcCreate_Input',
	},
	isRequired: true,
},
	},
} as const;

export const $IxPresentationLocCreate = {
	description: `XBRLの表示リンクロケーションを表すクラス`,
	properties: {
		item_key: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 36,
	minLength: 36,
}, {
	type: 'null',
}],
	isRequired: true,
},
		head_item_key: {
	type: 'string',
	isRequired: true,
},
		attr_value: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 255,
}, {
	type: 'null',
}],
	isRequired: true,
},
		xlink_href: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
	isRequired: true,
},
		xlink_type: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 255,
}, {
	type: 'null',
}],
	isRequired: true,
},
		xlink_schema: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 255,
}, {
	type: 'null',
}],
	isRequired: true,
},
		xlink_label: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
		source_file_id: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 36,
}, {
	type: 'null',
}],
	isRequired: true,
},
	},
} as const;

export const $IxPresentationLocCreateList = {
	description: `XBRLの表示リンクロケーションを作成するためのクラス`,
	properties: {
		data: {
	type: 'array',
	contains: {
		type: 'IxPresentationLocCreate',
	},
	isRequired: true,
},
	},
} as const;

export const $IxQualitativeCreate = {
	description: `定性的情報を登録するためのモデル`,
	properties: {
		item_key: {
	type: 'any-of',
	description: `ID`,
	contains: [{
	type: 'string',
	maxLength: 36,
}, {
	type: 'null',
}],
},
		currentId: {
	type: 'string',
	description: `現在のID`,
	maxLength: 36,
},
		parentId: {
	type: 'any-of',
	description: `親ID`,
	contains: [{
	type: 'string',
	maxLength: 36,
}, {
	type: 'null',
}],
},
		type: {
	type: 'any-of',
	description: `タイプ`,
	contains: [{
	type: 'string',
	maxLength: 255,
}, {
	type: 'null',
}],
},
		content: {
	type: 'any-of',
	description: `内容`,
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
		order: {
	type: 'any-of',
	description: `順序`,
	contains: [{
	type: 'number',
}, {
	type: 'null',
}],
},
		head_item_key: {
	type: 'any-of',
	description: `XBRL-ID`,
	contains: [{
	type: 'string',
	maxLength: 36,
}, {
	type: 'null',
}],
},
		source_file_id: {
	type: 'any-of',
	description: `ソースファイルID`,
	contains: [{
	type: 'string',
	maxLength: 36,
}, {
	type: 'null',
}],
},
		photo_url: {
	type: 'any-of',
	description: `写真URL`,
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
	},
} as const;

export const $IxQualitativeCreates = {
	description: `複数の定性的情報を登録するためのモデル`,
	properties: {
		data: {
	type: 'array',
	contains: {
		type: 'IxQualitativeCreate',
	},
	isRequired: true,
},
	},
} as const;

export const $IxQualitativePublic = {
	description: `定性的情報を取得するためのモデル`,
	properties: {
		currentId: {
	type: 'string',
	isRequired: true,
},
		parentId: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
	isRequired: true,
},
		type: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
	isRequired: true,
},
		content: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
	isRequired: true,
},
		order: {
	type: 'any-of',
	contains: [{
	type: 'number',
}, {
	type: 'null',
}],
	isRequired: true,
},
		head_item_key: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
	isRequired: true,
},
		photo_url: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
	isRequired: true,
},
	},
} as const;

export const $IxQualitativePublics = {
	description: `複数の定性的情報を取得するためのモデル`,
	properties: {
		count: {
	type: 'number',
	isRequired: true,
},
		data: {
	type: 'array',
	contains: {
		type: 'IxQualitativePublic',
	},
	isRequired: true,
},
	},
} as const;

export const $IxReportTypeCount = {
	description: `報告書タイプのカウントを表すクラス`,
	properties: {
		report_type: {
	type: 'string',
	isRequired: true,
},
		report_type_jp: {
	type: 'string',
	isRequired: true,
},
		count: {
	type: 'number',
	isRequired: true,
},
	},
} as const;

export const $IxReportTypeCountList = {
	description: `報告書タイプのカウントのリストを表すクラス`,
	properties: {
		data: {
	type: 'array',
	contains: {
		type: 'IxReportTypeCount',
	},
	isRequired: true,
},
		count: {
	type: 'number',
	isRequired: true,
},
	},
} as const;

export const $IxSchemaLinkBaseCreate = {
	description: `iXBRLのスキーマリンクベース情報を作成するためのクラス`,
	properties: {
		item_key: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 36,
	minLength: 36,
}, {
	type: 'null',
}],
	isRequired: true,
},
		head_item_key: {
	type: 'string',
	isRequired: true,
},
		xlink_arcrole: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 255,
}, {
	type: 'null',
}],
	isRequired: true,
},
		xlink_href: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 255,
}, {
	type: 'null',
}],
	isRequired: true,
},
		xlink_role: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 255,
}, {
	type: 'null',
}],
	isRequired: true,
},
		xlink_type: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 255,
}, {
	type: 'null',
}],
	isRequired: true,
},
		source_file_id: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 36,
}, {
	type: 'null',
}],
	isRequired: true,
},
		xbrl_type: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 255,
}, {
	type: 'null',
}],
	isRequired: true,
},
		href_source_file_id: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 36,
}, {
	type: 'null',
}],
	isRequired: true,
},
	},
} as const;

export const $IxSchemaLinkBaseCreateList = {
	description: `iXBRLのスキーマリンクベース情報を作成するためのクラス`,
	properties: {
		data: {
	type: 'array',
	contains: {
		type: 'IxSchemaLinkBaseCreate',
	},
	isRequired: true,
},
	},
} as const;

export const $IxSourceFileCreate = {
	description: `iXBRLのソースファイル情報を作成するためのクラス`,
	properties: {
		id: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 36,
}, {
	type: 'null',
}],
	isRequired: true,
},
		item_key: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 36,
	minLength: 36,
}, {
	type: 'null',
}],
	isRequired: true,
},
		name: {
	type: 'string',
	isRequired: true,
	maxLength: 255,
},
		type: {
	type: 'string',
	isRequired: true,
	maxLength: 255,
},
		head_item_key: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 36,
}, {
	type: 'null',
}],
	isRequired: true,
},
		url: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 255,
}, {
	type: 'null',
}],
	isRequired: true,
},
	},
} as const;

export const $IxSourceFileCreateList = {
	description: `iXBRLのソースファイル情報を作成するためのクラス`,
	properties: {
		data: {
	type: 'array',
	contains: {
		type: 'IxSourceFileCreate',
	},
	isRequired: true,
},
	},
} as const;

export const $Message = {
	properties: {
		message: {
	type: 'string',
	isRequired: true,
},
	},
} as const;

export const $NetAssetsPerShare_edjp_FinancialReportSummary = {
	description: `1株当たり純資産 `,
	properties: {
		current_accumulated_q2_instant_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間時点_連結_実績`,
},
		prior_year_instant_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度時点_連結_実績`,
},
	},
} as const;

export const $NetAssetsPerShare_edjp_FinancialReportSummary_FY = {
	description: `1株当たり純資産 `,
	properties: {
		current_year_instant_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度時点_連結_実績`,
},
		current_year_instant_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度時点_非連結又は個別_実績`,
},
		prior_year_instant_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度時点_連結_実績`,
},
		prior_year_instant_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度時点_非連結又は個別_実績`,
},
	},
} as const;

export const $NetAssetsPerShare_edjp_FinancialReportSummary_HY_specific_business = {
	description: `1株当たり純資産 `,
	properties: {
		current_accumulated_q2_instant_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間時点_連結_実績`,
},
		current_accumulated_q2_instant_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間時点_非連結又は個別_実績`,
},
		prior_year_instant_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度時点_連結_実績`,
},
		prior_year_instant_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度時点_非連結又は個別_実績`,
},
	},
} as const;

export const $NetAssetsPerShare_edjp_FinancialReportSummary_Q1 = {
	description: `1株当たり純資産 `,
	properties: {
		current_accumulated_q1_instant_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第１四半期間時点_連結_実績`,
},
		current_accumulated_q1_instant_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第１四半期間時点_非連結又は個別_実績`,
},
		prior_year_instant_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度時点_連結_実績`,
},
		prior_year_instant_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度時点_非連結又は個別_実績`,
},
	},
} as const;

export const $NetAssetsPerShare_edjp_FinancialReportSummary_Q2 = {
	description: `1株当たり純資産 `,
	properties: {
		current_accumulated_q2_instant_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間時点_連結_実績`,
},
		current_accumulated_q2_instant_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間時点_非連結又は個別_実績`,
},
		prior_year_instant_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度時点_連結_実績`,
},
		prior_year_instant_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度時点_非連結又は個別_実績`,
},
	},
} as const;

export const $NetAssetsPerShare_edjp_FinancialReportSummary_Q3 = {
	description: `1株当たり純資産 `,
	properties: {
		current_accumulated_q3_instant_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第３四半期間時点_連結_実績`,
},
		prior_year_instant_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度時点_連結_実績`,
},
	},
} as const;

export const $NetAssets_edjp_FinancialReportSummary = {
	description: `純資産 `,
	properties: {
		current_accumulated_q2_instant_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間時点_連結_実績`,
},
		prior_year_instant_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度時点_連結_実績`,
},
	},
} as const;

export const $NetAssets_edjp_FinancialReportSummary_FY = {
	description: `純資産 `,
	properties: {
		current_year_instant_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度時点_連結_実績`,
},
		current_year_instant_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度時点_非連結又は個別_実績`,
},
		prior_year_instant_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度時点_連結_実績`,
},
		prior_year_instant_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度時点_非連結又は個別_実績`,
},
	},
} as const;

export const $NetAssets_edjp_FinancialReportSummary_HY_specific_business = {
	description: `純資産 `,
	properties: {
		current_accumulated_q2_instant_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間時点_連結_実績`,
},
		current_accumulated_q2_instant_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間時点_非連結又は個別_実績`,
},
		prior_year_instant_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度時点_連結_実績`,
},
		prior_year_instant_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度時点_非連結又は個別_実績`,
},
	},
} as const;

export const $NetAssets_edjp_FinancialReportSummary_Q1 = {
	description: `純資産 `,
	properties: {
		current_accumulated_q1_instant_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第１四半期間時点_連結_実績`,
},
		current_accumulated_q1_instant_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第１四半期間時点_非連結又は個別_実績`,
},
		prior_year_instant_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度時点_連結_実績`,
},
		prior_year_instant_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度時点_非連結又は個別_実績`,
},
	},
} as const;

export const $NetAssets_edjp_FinancialReportSummary_Q2 = {
	description: `純資産 `,
	properties: {
		current_accumulated_q2_instant_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間時点_連結_実績`,
},
		current_accumulated_q2_instant_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間時点_非連結又は個別_実績`,
},
		prior_year_instant_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度時点_連結_実績`,
},
		prior_year_instant_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度時点_非連結又は個別_実績`,
},
	},
} as const;

export const $NetAssets_edjp_FinancialReportSummary_Q3 = {
	description: `純資産 `,
	properties: {
		current_accumulated_q3_instant_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第３四半期間時点_連結_実績`,
},
		prior_year_instant_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度時点_連結_実績`,
},
	},
} as const;

export const $NetIncomePerShare_edjp_FinancialReportSummary = {
	description: `1株当たり当期純利益 `,
	properties: {
		current_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_連結_実績`,
},
		current_year_duration_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_予想`,
},
		current_year_duration_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_下限`,
},
		current_year_duration_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_上限`,
},
		prior_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第２四半期間_連結_実績`,
},
	},
} as const;

export const $NetIncomePerShare_edjp_FinancialReportSummary_FY = {
	description: `1株当たり当期純利益 `,
	properties: {
		current_year_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_実績`,
},
		current_year_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_実績`,
},
		next_accumulated_q2_duration_non_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `次年度期初から第２四半期間_非連結又は個別_予想`,
},
		next_accumulated_q2_duration_non_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `次年度期初から第２四半期間_非連結又は個別_下限`,
},
		next_accumulated_q2_duration_non_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `次年度期初から第２四半期間_非連結又は個別_上限`,
},
		next_year_duration_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `次年度会計期間_連結_予想`,
},
		next_year_duration_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `次年度会計期間_連結_下限`,
},
		next_year_duration_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `次年度会計期間_連結_上限`,
},
		next_year_duration_non_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `次年度会計期間_非連結又は個別_予想`,
},
		next_year_duration_non_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `次年度会計期間_非連結又は個別_下限`,
},
		next_year_duration_non_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `次年度会計期間_非連結又は個別_上限`,
},
		prior_year_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度会計期間_連結_実績`,
},
		prior_year_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度会計期間_非連結又は個別_実績`,
},
	},
} as const;

export const $NetIncomePerShare_edjp_FinancialReportSummary_HY_specific_business = {
	description: `1株当たり当期純利益 `,
	properties: {
		current_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_連結_実績`,
},
		current_accumulated_q2_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_非連結又は個別_実績`,
},
		current_year_duration_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_予想`,
},
		current_year_duration_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_下限`,
},
		current_year_duration_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_上限`,
},
		current_year_duration_non_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_予想`,
},
		current_year_duration_non_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_下限`,
},
		current_year_duration_non_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_上限`,
},
		prior_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第２四半期間_連結_実績`,
},
		prior_accumulated_q2_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第２四半期間_非連結又は個別_実績`,
},
	},
} as const;

export const $NetIncomePerShare_edjp_FinancialReportSummary_Q1 = {
	description: `1株当たり当期純利益 `,
	properties: {
		current_accumulated_q1_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第１四半期間_連結_実績`,
},
		current_accumulated_q1_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第１四半期間_非連結又は個別_実績`,
},
		current_accumulated_q2_duration_non_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_非連結又は個別_予想`,
},
		current_accumulated_q2_duration_non_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_非連結又は個別_下限`,
},
		current_accumulated_q2_duration_non_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_非連結又は個別_上限`,
},
		current_year_duration_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_予想`,
},
		current_year_duration_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_下限`,
},
		current_year_duration_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_上限`,
},
		current_year_duration_non_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_予想`,
},
		current_year_duration_non_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_下限`,
},
		current_year_duration_non_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_上限`,
},
		prior_accumulated_q1_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第１四半期間_連結_実績`,
},
		prior_accumulated_q1_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第１四半期間_非連結又は個別_実績`,
},
	},
} as const;

export const $NetIncomePerShare_edjp_FinancialReportSummary_Q2 = {
	description: `1株当たり当期純利益 `,
	properties: {
		current_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_連結_実績`,
},
		current_accumulated_q2_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_非連結又は個別_実績`,
},
		current_year_duration_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_予想`,
},
		current_year_duration_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_下限`,
},
		current_year_duration_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_上限`,
},
		current_year_duration_non_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_予想`,
},
		current_year_duration_non_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_下限`,
},
		current_year_duration_non_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_上限`,
},
		prior_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第２四半期間_連結_実績`,
},
		prior_accumulated_q2_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第２四半期間_非連結又は個別_実績`,
},
	},
} as const;

export const $NetIncomePerShare_edjp_FinancialReportSummary_Q3 = {
	description: `1株当たり当期純利益 `,
	properties: {
		current_accumulated_q3_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第３四半期間_連結_実績`,
},
		current_year_duration_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_予想`,
},
		current_year_duration_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_下限`,
},
		current_year_duration_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_上限`,
},
		prior_accumulated_q3_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第３四半期間_連結_実績`,
},
	},
} as const;

export const $NetIncomeToShareholdersEquityRatio_edjp_FinancialReportSummary_FY = {
	description: `自己資本当期純利益率 `,
	properties: {
		current_year_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_実績`,
},
		current_year_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_実績`,
},
		prior_year_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度会計期間_連結_実績`,
},
		prior_year_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度会計期間_非連結又は個別_実績`,
},
	},
} as const;

export const $NetIncome_edjp_FinancialReportSummary_FY = {
	description: `当期純利益 `,
	properties: {
		current_year_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_実績`,
},
		next_accumulated_q2_duration_non_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `次年度期初から第２四半期間_非連結又は個別_予想`,
},
		next_accumulated_q2_duration_non_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `次年度期初から第２四半期間_非連結又は個別_下限`,
},
		next_accumulated_q2_duration_non_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `次年度期初から第２四半期間_非連結又は個別_上限`,
},
		next_year_duration_non_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `次年度会計期間_非連結又は個別_予想`,
},
		next_year_duration_non_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `次年度会計期間_非連結又は個別_下限`,
},
		next_year_duration_non_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `次年度会計期間_非連結又は個別_上限`,
},
		prior_year_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度会計期間_非連結又は個別_実績`,
},
	},
} as const;

export const $NetIncome_edjp_FinancialReportSummary_HY_specific_business = {
	description: `当期純利益 `,
	properties: {
		current_accumulated_q2_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_非連結又は個別_実績`,
},
		current_year_duration_non_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_予想`,
},
		current_year_duration_non_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_下限`,
},
		current_year_duration_non_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_上限`,
},
		prior_accumulated_q2_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第２四半期間_非連結又は個別_実績`,
},
	},
} as const;

export const $NetIncome_edjp_FinancialReportSummary_Q1 = {
	description: `当期純利益 `,
	properties: {
		current_accumulated_q1_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第１四半期間_非連結又は個別_実績`,
},
		current_accumulated_q2_duration_non_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_非連結又は個別_予想`,
},
		current_accumulated_q2_duration_non_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_非連結又は個別_下限`,
},
		current_accumulated_q2_duration_non_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_非連結又は個別_上限`,
},
		current_year_duration_non_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_予想`,
},
		current_year_duration_non_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_下限`,
},
		current_year_duration_non_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_上限`,
},
		prior_accumulated_q1_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第１四半期間_非連結又は個別_実績`,
},
	},
} as const;

export const $NetIncome_edjp_FinancialReportSummary_Q2 = {
	description: `当期純利益 `,
	properties: {
		current_accumulated_q2_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_非連結又は個別_実績`,
},
		current_year_duration_non_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_予想`,
},
		current_year_duration_non_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_下限`,
},
		current_year_duration_non_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_上限`,
},
		prior_accumulated_q2_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第２四半期間_非連結又は個別_実績`,
},
	},
} as const;

export const $NetOperatingRevenuesSE_edjp_FinancialReportSummary_Q2 = {
	description: `純営業収益、証券 `,
	properties: {
		current_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_連結_実績`,
},
		current_accumulated_q2_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_非連結又は個別_実績`,
},
		prior_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第２四半期間_連結_実績`,
},
		prior_accumulated_q2_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第２四半期間_非連結又は個別_実績`,
},
	},
} as const;

export const $NetSales_edjp_FinancialReportSummary = {
	description: `売上高 `,
	properties: {
		current_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_連結_実績`,
},
		current_year_duration_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_予想`,
},
		current_year_duration_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_下限`,
},
		current_year_duration_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_上限`,
},
		prior_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第２四半期間_連結_実績`,
},
	},
} as const;

export const $NetSales_edjp_FinancialReportSummary_FY = {
	description: `売上高 `,
	properties: {
		current_year_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_実績`,
},
		current_year_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_実績`,
},
		next_accumulated_q2_duration_non_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `次年度期初から第２四半期間_非連結又は個別_予想`,
},
		next_accumulated_q2_duration_non_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `次年度期初から第２四半期間_非連結又は個別_下限`,
},
		next_accumulated_q2_duration_non_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `次年度期初から第２四半期間_非連結又は個別_上限`,
},
		next_year_duration_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `次年度会計期間_連結_予想`,
},
		next_year_duration_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `次年度会計期間_連結_下限`,
},
		next_year_duration_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `次年度会計期間_連結_上限`,
},
		next_year_duration_non_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `次年度会計期間_非連結又は個別_予想`,
},
		next_year_duration_non_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `次年度会計期間_非連結又は個別_下限`,
},
		next_year_duration_non_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `次年度会計期間_非連結又は個別_上限`,
},
		prior_year_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度会計期間_連結_実績`,
},
		prior_year_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度会計期間_非連結又は個別_実績`,
},
	},
} as const;

export const $NetSales_edjp_FinancialReportSummary_Q1 = {
	description: `売上高 `,
	properties: {
		current_accumulated_q1_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第１四半期間_連結_実績`,
},
		current_accumulated_q1_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第１四半期間_非連結又は個別_実績`,
},
		current_accumulated_q2_duration_non_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_非連結又は個別_予想`,
},
		current_accumulated_q2_duration_non_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_非連結又は個別_下限`,
},
		current_accumulated_q2_duration_non_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_非連結又は個別_上限`,
},
		current_year_duration_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_予想`,
},
		current_year_duration_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_下限`,
},
		current_year_duration_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_上限`,
},
		current_year_duration_non_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_予想`,
},
		current_year_duration_non_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_下限`,
},
		current_year_duration_non_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_上限`,
},
		prior_accumulated_q1_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第１四半期間_連結_実績`,
},
		prior_accumulated_q1_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第１四半期間_非連結又は個別_実績`,
},
	},
} as const;

export const $NetSales_edjp_FinancialReportSummary_Q2 = {
	description: `売上高 `,
	properties: {
		current_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_連結_実績`,
},
		current_accumulated_q2_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_非連結又は個別_実績`,
},
		current_year_duration_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_予想`,
},
		current_year_duration_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_下限`,
},
		current_year_duration_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_上限`,
},
		current_year_duration_non_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_予想`,
},
		current_year_duration_non_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_下限`,
},
		current_year_duration_non_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_上限`,
},
		prior_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第２四半期間_連結_実績`,
},
		prior_accumulated_q2_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第２四半期間_非連結又は個別_実績`,
},
	},
} as const;

export const $NetSales_edjp_FinancialReportSummary_Q3 = {
	description: `売上高 `,
	properties: {
		current_accumulated_q3_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第３四半期間_連結_実績`,
},
		current_year_duration_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_予想`,
},
		current_year_duration_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_下限`,
},
		current_year_duration_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_上限`,
},
		prior_accumulated_q3_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第３四半期間_連結_実績`,
},
	},
} as const;

export const $NewPassword = {
	properties: {
		token: {
	type: 'string',
	isRequired: true,
},
		new_password: {
	type: 'string',
	isRequired: true,
	maxLength: 40,
	minLength: 8,
},
	},
} as const;

export const $NumberOfIssuedAndOutstandingSharesAtTheEndOfFiscalYearIncludingTreasuryStock_edjp_FinancialReportSummary = {
	description: `期末発行済株式数（自己株式を含む） `,
	properties: {
		current_accumulated_q2_instant_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間時点_非連結又は個別_実績`,
},
		prior_year_instant_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度時点_非連結又は個別_実績`,
},
	},
} as const;

export const $NumberOfIssuedAndOutstandingSharesAtTheEndOfFiscalYearIncludingTreasuryStock_edjp_FinancialReportSummary_FY = {
	description: `期末発行済株式数（自己株式を含む） `,
	properties: {
		current_year_instant_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度時点_非連結又は個別_実績`,
},
		prior_year_instant_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度時点_非連結又は個別_実績`,
},
	},
} as const;

export const $NumberOfIssuedAndOutstandingSharesAtTheEndOfFiscalYearIncludingTreasuryStock_edjp_FinancialReportSummary_HY_specific_business = {
	description: `期末発行済株式数（自己株式を含む） `,
	properties: {
		current_accumulated_q2_instant_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間時点_非連結又は個別_実績`,
},
		prior_year_instant_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度時点_非連結又は個別_実績`,
},
	},
} as const;

export const $NumberOfIssuedAndOutstandingSharesAtTheEndOfFiscalYearIncludingTreasuryStock_edjp_FinancialReportSummary_Q1 = {
	description: `期末発行済株式数（自己株式を含む） `,
	properties: {
		current_accumulated_q1_instant_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第１四半期間時点_非連結又は個別_実績`,
},
		prior_year_instant_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度時点_非連結又は個別_実績`,
},
	},
} as const;

export const $NumberOfIssuedAndOutstandingSharesAtTheEndOfFiscalYearIncludingTreasuryStock_edjp_FinancialReportSummary_Q2 = {
	description: `期末発行済株式数（自己株式を含む） `,
	properties: {
		current_accumulated_q2_instant_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間時点_非連結又は個別_実績`,
},
		prior_year_instant_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度時点_非連結又は個別_実績`,
},
	},
} as const;

export const $NumberOfIssuedAndOutstandingSharesAtTheEndOfFiscalYearIncludingTreasuryStock_edjp_FinancialReportSummary_Q3 = {
	description: `期末発行済株式数（自己株式を含む） `,
	properties: {
		current_accumulated_q3_instant_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第３四半期間時点_非連結又は個別_実績`,
},
		prior_year_instant_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度時点_非連結又は個別_実績`,
},
	},
} as const;

export const $NumberOfSubsidiariesExcludedFromConsolidation_edjp_FinancialReportSummary_FY = {
	description: `除外 `,
	properties: {
		current_year_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_実績`,
},
	},
} as const;

export const $NumberOfSubsidiariesExcludedFromConsolidation_edjp_FinancialReportSummary_Q1 = {
	description: `除外 `,
	properties: {
		current_accumulated_q1_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第１四半期間_連結_実績`,
},
	},
} as const;

export const $NumberOfSubsidiariesExcludedFromConsolidation_edjp_FinancialReportSummary_Q2 = {
	description: `除外 `,
	properties: {
		current_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_連結_実績`,
},
	},
} as const;

export const $NumberOfSubsidiariesExcludedFromConsolidation_edjp_FinancialReportSummary_Q3 = {
	description: `除外 `,
	properties: {
		current_accumulated_q3_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第３四半期間_連結_実績`,
},
	},
} as const;

export const $NumberOfSubsidiariesNewlyConsolidated_edjp_FinancialReportSummary_FY = {
	description: `新規 `,
	properties: {
		current_year_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_実績`,
},
	},
} as const;

export const $NumberOfSubsidiariesNewlyConsolidated_edjp_FinancialReportSummary_Q1 = {
	description: `新規 `,
	properties: {
		current_accumulated_q1_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第１四半期間_連結_実績`,
},
	},
} as const;

export const $NumberOfSubsidiariesNewlyConsolidated_edjp_FinancialReportSummary_Q2 = {
	description: `新規 `,
	properties: {
		current_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_連結_実績`,
},
	},
} as const;

export const $NumberOfSubsidiariesNewlyConsolidated_edjp_FinancialReportSummary_Q3 = {
	description: `新規 `,
	properties: {
		current_accumulated_q3_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第３四半期間_連結_実績`,
},
	},
} as const;

export const $NumberOfTreasuryStockAtTheEndOfFiscalYear_edjp_FinancialReportSummary = {
	description: `期末自己株式数 `,
	properties: {
		current_accumulated_q2_instant_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間時点_非連結又は個別_実績`,
},
		prior_year_instant_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度時点_非連結又は個別_実績`,
},
	},
} as const;

export const $NumberOfTreasuryStockAtTheEndOfFiscalYear_edjp_FinancialReportSummary_FY = {
	description: `期末自己株式数 `,
	properties: {
		current_year_instant_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度時点_非連結又は個別_実績`,
},
		prior_year_instant_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度時点_非連結又は個別_実績`,
},
	},
} as const;

export const $NumberOfTreasuryStockAtTheEndOfFiscalYear_edjp_FinancialReportSummary_HY_specific_business = {
	description: `期末自己株式数 `,
	properties: {
		current_accumulated_q2_instant_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間時点_非連結又は個別_実績`,
},
		prior_year_instant_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度時点_非連結又は個別_実績`,
},
	},
} as const;

export const $NumberOfTreasuryStockAtTheEndOfFiscalYear_edjp_FinancialReportSummary_Q1 = {
	description: `期末自己株式数 `,
	properties: {
		current_accumulated_q1_instant_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第１四半期間時点_非連結又は個別_実績`,
},
		prior_year_instant_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度時点_非連結又は個別_実績`,
},
	},
} as const;

export const $NumberOfTreasuryStockAtTheEndOfFiscalYear_edjp_FinancialReportSummary_Q2 = {
	description: `期末自己株式数 `,
	properties: {
		current_accumulated_q2_instant_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間時点_非連結又は個別_実績`,
},
		prior_year_instant_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度時点_非連結又は個別_実績`,
},
	},
} as const;

export const $NumberOfTreasuryStockAtTheEndOfFiscalYear_edjp_FinancialReportSummary_Q3 = {
	description: `期末自己株式数 `,
	properties: {
		current_accumulated_q3_instant_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第３四半期間時点_非連結又は個別_実績`,
},
		prior_year_instant_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度時点_非連結又は個別_実績`,
},
	},
} as const;

export const $OperatingIncomeToNetSalesRatio_edjp_FinancialReportSummary_FY = {
	description: `売上高営業利益率 `,
	properties: {
		current_year_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_実績`,
},
		current_year_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_実績`,
},
		prior_year_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度会計期間_連結_実績`,
},
		prior_year_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度会計期間_非連結又は個別_実績`,
},
	},
} as const;

export const $OperatingIncome_edjp_FinancialReportSummary = {
	description: `営業利益 `,
	properties: {
		current_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_連結_実績`,
},
		current_year_duration_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_予想`,
},
		current_year_duration_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_下限`,
},
		current_year_duration_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_上限`,
},
		prior_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第２四半期間_連結_実績`,
},
	},
} as const;

export const $OperatingIncome_edjp_FinancialReportSummary_FY = {
	description: `営業利益 `,
	properties: {
		current_year_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_実績`,
},
		current_year_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_実績`,
},
		next_accumulated_q2_duration_non_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `次年度期初から第２四半期間_非連結又は個別_予想`,
},
		next_accumulated_q2_duration_non_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `次年度期初から第２四半期間_非連結又は個別_下限`,
},
		next_accumulated_q2_duration_non_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `次年度期初から第２四半期間_非連結又は個別_上限`,
},
		next_year_duration_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `次年度会計期間_連結_予想`,
},
		next_year_duration_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `次年度会計期間_連結_下限`,
},
		next_year_duration_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `次年度会計期間_連結_上限`,
},
		next_year_duration_non_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `次年度会計期間_非連結又は個別_予想`,
},
		next_year_duration_non_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `次年度会計期間_非連結又は個別_下限`,
},
		next_year_duration_non_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `次年度会計期間_非連結又は個別_上限`,
},
		prior_year_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度会計期間_連結_実績`,
},
		prior_year_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度会計期間_非連結又は個別_実績`,
},
	},
} as const;

export const $OperatingIncome_edjp_FinancialReportSummary_Q1 = {
	description: `営業利益 `,
	properties: {
		current_accumulated_q1_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第１四半期間_連結_実績`,
},
		current_accumulated_q1_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第１四半期間_非連結又は個別_実績`,
},
		current_accumulated_q2_duration_non_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_非連結又は個別_予想`,
},
		current_accumulated_q2_duration_non_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_非連結又は個別_下限`,
},
		current_accumulated_q2_duration_non_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_非連結又は個別_上限`,
},
		current_year_duration_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_予想`,
},
		current_year_duration_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_下限`,
},
		current_year_duration_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_上限`,
},
		current_year_duration_non_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_予想`,
},
		current_year_duration_non_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_下限`,
},
		current_year_duration_non_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_上限`,
},
		prior_accumulated_q1_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第１四半期間_連結_実績`,
},
		prior_accumulated_q1_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第１四半期間_非連結又は個別_実績`,
},
	},
} as const;

export const $OperatingIncome_edjp_FinancialReportSummary_Q2 = {
	description: `営業利益 `,
	properties: {
		current_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_連結_実績`,
},
		current_accumulated_q2_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_非連結又は個別_実績`,
},
		current_year_duration_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_予想`,
},
		current_year_duration_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_下限`,
},
		current_year_duration_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_上限`,
},
		current_year_duration_non_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_予想`,
},
		current_year_duration_non_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_下限`,
},
		current_year_duration_non_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_上限`,
},
		prior_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第２四半期間_連結_実績`,
},
		prior_accumulated_q2_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第２四半期間_非連結又は個別_実績`,
},
	},
} as const;

export const $OperatingIncome_edjp_FinancialReportSummary_Q3 = {
	description: `営業利益 `,
	properties: {
		current_accumulated_q3_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第３四半期間_連結_実績`,
},
		current_year_duration_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_予想`,
},
		current_year_duration_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_下限`,
},
		current_year_duration_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_上限`,
},
		prior_accumulated_q3_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第３四半期間_連結_実績`,
},
	},
} as const;

export const $OperatingRevenuesSE_edjp_FinancialReportSummary_Q2 = {
	description: `営業収益、証券 `,
	properties: {
		current_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_連結_実績`,
},
		prior_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第２四半期間_連結_実績`,
},
	},
} as const;

export const $OperatingRevenues_edjp_FinancialReportSummary_Q2 = {
	description: `営業収益 `,
	properties: {
		current_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_連結_実績`,
},
		current_accumulated_q2_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_非連結又は個別_実績`,
},
		current_year_duration_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_予想`,
},
		current_year_duration_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_下限`,
},
		current_year_duration_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_上限`,
},
		prior_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第２四半期間_連結_実績`,
},
		prior_accumulated_q2_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第２四半期間_非連結又は個別_実績`,
},
	},
} as const;

export const $OrdinaryIncomeToTotalAssetsRatio_edjp_FinancialReportSummary_FY = {
	description: `総資産経常利益率 `,
	properties: {
		current_year_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_実績`,
},
		current_year_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_実績`,
},
		prior_year_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度会計期間_連結_実績`,
},
		prior_year_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度会計期間_非連結又は個別_実績`,
},
	},
} as const;

export const $OrdinaryIncome_edjp_FinancialReportSummary = {
	description: `経常利益 `,
	properties: {
		current_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_連結_実績`,
},
		current_year_duration_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_予想`,
},
		current_year_duration_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_下限`,
},
		current_year_duration_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_上限`,
},
		prior_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第２四半期間_連結_実績`,
},
	},
} as const;

export const $OrdinaryIncome_edjp_FinancialReportSummary_FY = {
	description: `経常利益 `,
	properties: {
		current_year_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_実績`,
},
		current_year_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_実績`,
},
		next_accumulated_q2_duration_non_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `次年度期初から第２四半期間_非連結又は個別_予想`,
},
		next_accumulated_q2_duration_non_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `次年度期初から第２四半期間_非連結又は個別_下限`,
},
		next_accumulated_q2_duration_non_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `次年度期初から第２四半期間_非連結又は個別_上限`,
},
		next_year_duration_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `次年度会計期間_連結_予想`,
},
		next_year_duration_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `次年度会計期間_連結_下限`,
},
		next_year_duration_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `次年度会計期間_連結_上限`,
},
		next_year_duration_non_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `次年度会計期間_非連結又は個別_予想`,
},
		next_year_duration_non_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `次年度会計期間_非連結又は個別_下限`,
},
		next_year_duration_non_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `次年度会計期間_非連結又は個別_上限`,
},
		prior_year_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度会計期間_連結_実績`,
},
		prior_year_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度会計期間_非連結又は個別_実績`,
},
	},
} as const;

export const $OrdinaryIncome_edjp_FinancialReportSummary_HY_specific_business = {
	description: `経常利益 `,
	properties: {
		current_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_連結_実績`,
},
		current_accumulated_q2_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_非連結又は個別_実績`,
},
		current_year_duration_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_予想`,
},
		current_year_duration_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_下限`,
},
		current_year_duration_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_上限`,
},
		current_year_duration_non_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_予想`,
},
		current_year_duration_non_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_下限`,
},
		current_year_duration_non_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_上限`,
},
		prior_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第２四半期間_連結_実績`,
},
		prior_accumulated_q2_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第２四半期間_非連結又は個別_実績`,
},
	},
} as const;

export const $OrdinaryIncome_edjp_FinancialReportSummary_Q1 = {
	description: `経常利益 `,
	properties: {
		current_accumulated_q1_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第１四半期間_連結_実績`,
},
		current_accumulated_q1_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第１四半期間_非連結又は個別_実績`,
},
		current_accumulated_q2_duration_non_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_非連結又は個別_予想`,
},
		current_accumulated_q2_duration_non_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_非連結又は個別_下限`,
},
		current_accumulated_q2_duration_non_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_非連結又は個別_上限`,
},
		current_year_duration_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_予想`,
},
		current_year_duration_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_下限`,
},
		current_year_duration_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_上限`,
},
		current_year_duration_non_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_予想`,
},
		current_year_duration_non_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_下限`,
},
		current_year_duration_non_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_上限`,
},
		prior_accumulated_q1_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第１四半期間_連結_実績`,
},
		prior_accumulated_q1_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第１四半期間_非連結又は個別_実績`,
},
	},
} as const;

export const $OrdinaryIncome_edjp_FinancialReportSummary_Q2 = {
	description: `経常利益 `,
	properties: {
		current_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_連結_実績`,
},
		current_accumulated_q2_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_非連結又は個別_実績`,
},
		current_year_duration_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_予想`,
},
		current_year_duration_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_下限`,
},
		current_year_duration_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_上限`,
},
		current_year_duration_non_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_予想`,
},
		current_year_duration_non_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_下限`,
},
		current_year_duration_non_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_非連結又は個別_上限`,
},
		prior_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第２四半期間_連結_実績`,
},
		prior_accumulated_q2_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第２四半期間_非連結又は個別_実績`,
},
	},
} as const;

export const $OrdinaryIncome_edjp_FinancialReportSummary_Q3 = {
	description: `経常利益 `,
	properties: {
		current_accumulated_q3_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第３四半期間_連結_実績`,
},
		current_year_duration_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_予想`,
},
		current_year_duration_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_下限`,
},
		current_year_duration_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_上限`,
},
		prior_accumulated_q3_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第３四半期間_連結_実績`,
},
	},
} as const;

export const $OrdinaryRevenuesBK_edjp_FinancialReportSummary_HY_specific_business = {
	description: `経常収益、銀行 `,
	properties: {
		current_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_連結_実績`,
},
		current_accumulated_q2_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_非連結又は個別_実績`,
},
		prior_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第２四半期間_連結_実績`,
},
		prior_accumulated_q2_duration_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第２四半期間_非連結又は個別_実績`,
},
	},
} as const;

export const $OwnersEquity_edjp_FinancialReportSummary = {
	description: `自己資本 `,
	properties: {
		current_accumulated_q2_instant_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間時点_連結_実績`,
},
		prior_year_instant_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度時点_連結_実績`,
},
	},
} as const;

export const $OwnersEquity_edjp_FinancialReportSummary_FY = {
	description: `自己資本 `,
	properties: {
		current_year_instant_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度時点_連結_実績`,
},
		current_year_instant_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度時点_非連結又は個別_実績`,
},
		prior_year_instant_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度時点_連結_実績`,
},
		prior_year_instant_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度時点_非連結又は個別_実績`,
},
	},
} as const;

export const $OwnersEquity_edjp_FinancialReportSummary_HY_specific_business = {
	description: `自己資本 `,
	properties: {
		current_accumulated_q2_instant_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間時点_連結_実績`,
},
		current_accumulated_q2_instant_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間時点_非連結又は個別_実績`,
},
		prior_year_instant_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度時点_連結_実績`,
},
		prior_year_instant_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度時点_非連結又は個別_実績`,
},
	},
} as const;

export const $OwnersEquity_edjp_FinancialReportSummary_Q1 = {
	description: `自己資本 `,
	properties: {
		current_accumulated_q1_instant_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第１四半期間時点_連結_実績`,
},
		current_accumulated_q1_instant_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第１四半期間時点_非連結又は個別_実績`,
},
		prior_year_instant_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度時点_連結_実績`,
},
		prior_year_instant_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度時点_非連結又は個別_実績`,
},
	},
} as const;

export const $OwnersEquity_edjp_FinancialReportSummary_Q2 = {
	description: `自己資本 `,
	properties: {
		current_accumulated_q2_instant_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間時点_連結_実績`,
},
		current_accumulated_q2_instant_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間時点_非連結又は個別_実績`,
},
		prior_year_instant_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度時点_連結_実績`,
},
		prior_year_instant_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度時点_非連結又は個別_実績`,
},
	},
} as const;

export const $OwnersEquity_edjp_FinancialReportSummary_Q3 = {
	description: `自己資本 `,
	properties: {
		current_accumulated_q3_instant_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第３四半期間時点_連結_実績`,
},
		prior_year_instant_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度時点_連結_実績`,
},
	},
} as const;

export const $PayoutRatio_edjp_FinancialReportSummary_FY = {
	description: `配当性向 `,
	properties: {
		current_year_duration_annual_member_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_年間_連結_実績`,
},
		current_year_duration_annual_member_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_年間_非連結又は個別_実績`,
},
		next_year_duration_annual_member_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `次年度会計期間_年間_連結_予想`,
},
		next_year_duration_annual_member_non_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `次年度会計期間_年間_非連結又は個別_予想`,
},
		prior_year_duration_annual_member_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度会計期間_年間_連結_実績`,
},
		prior_year_duration_annual_member_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度会計期間_年間_非連結又は個別_実績`,
},
	},
} as const;

export const $ProfitAttributableToOwnersOfParent_edjp_FinancialReportSummary = {
	description: `親会社株主に帰属する当期純利益 `,
	properties: {
		current_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_連結_実績`,
},
		current_year_duration_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_予想`,
},
		current_year_duration_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_下限`,
},
		current_year_duration_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_上限`,
},
		prior_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第２四半期間_連結_実績`,
},
	},
} as const;

export const $ProfitAttributableToOwnersOfParent_edjp_FinancialReportSummary_FY = {
	description: `親会社株主に帰属する当期純利益 `,
	properties: {
		current_year_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_実績`,
},
		next_year_duration_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `次年度会計期間_連結_予想`,
},
		next_year_duration_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `次年度会計期間_連結_下限`,
},
		next_year_duration_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `次年度会計期間_連結_上限`,
},
		prior_year_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度会計期間_連結_実績`,
},
	},
} as const;

export const $ProfitAttributableToOwnersOfParent_edjp_FinancialReportSummary_HY_specific_business = {
	description: `親会社株主に帰属する当期純利益 `,
	properties: {
		current_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_連結_実績`,
},
		current_year_duration_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_予想`,
},
		current_year_duration_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_下限`,
},
		current_year_duration_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_上限`,
},
		prior_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第２四半期間_連結_実績`,
},
	},
} as const;

export const $ProfitAttributableToOwnersOfParent_edjp_FinancialReportSummary_Q1 = {
	description: `親会社株主に帰属する当期純利益 `,
	properties: {
		current_accumulated_q1_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第１四半期間_連結_実績`,
},
		current_year_duration_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_予想`,
},
		current_year_duration_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_下限`,
},
		current_year_duration_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_上限`,
},
		prior_accumulated_q1_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第１四半期間_連結_実績`,
},
	},
} as const;

export const $ProfitAttributableToOwnersOfParent_edjp_FinancialReportSummary_Q2 = {
	description: `親会社株主に帰属する当期純利益 `,
	properties: {
		current_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間_連結_実績`,
},
		current_year_duration_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_予想`,
},
		current_year_duration_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_下限`,
},
		current_year_duration_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_上限`,
},
		prior_accumulated_q2_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第２四半期間_連結_実績`,
},
	},
} as const;

export const $ProfitAttributableToOwnersOfParent_edjp_FinancialReportSummary_Q3 = {
	description: `親会社株主に帰属する当期純利益 `,
	properties: {
		current_accumulated_q3_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第３四半期間_連結_実績`,
},
		current_year_duration_consolidated_member_forecast_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_予想`,
},
		current_year_duration_consolidated_member_lower_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_下限`,
},
		current_year_duration_consolidated_member_upper_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_連結_上限`,
},
		prior_accumulated_q3_duration_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度期初から第３四半期間_連結_実績`,
},
	},
} as const;

export const $QualitativeInfoHeader = {
	description: `定性的情報のヘッダー情報を取得するためのモデル`,
	properties: {
		qualitative_info: {
	type: 'any-of',
	description: `当四半期決算に関する定性的情報`,
	contains: [{
	type: 'QualitativeInfoSubTitle',
}, {
	type: 'null',
}],
},
	},
} as const;

export const $QualitativeInfoSubTitle = {
	description: `定性的情報を取得するためのモデル`,
	properties: {
		operating_result_info: {
	type: 'any-of',
	description: `経営成績に関する説明`,
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
		segment_info_key: {
	type: 'any-of',
	description: `セグメント情報`,
	contains: [{
	type: 'array',
	contains: {
	type: 'string',
},
}, {
	type: 'null',
}],
},
		segment_info: {
	type: 'dictionary',
	contains: {
	properties: {
	},
},
},
		segment_photo_url: {
	type: 'dictionary',
	contains: {
	properties: {
	},
},
},
		explanation_of_financial_position: {
	type: 'any-of',
	description: `財政状態の説明`,
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
		forecast_info: {
	type: 'any-of',
	description: `将来予測に関する説明`,
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
	},
} as const;

export const $QuarterlyPeriod_edjp_FinancialReportSummary = {
	description: `四半期 `,
	properties: {
		current_accumulated_q2_instant: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間時点`,
},
	},
} as const;

export const $QuarterlyPeriod_edjp_FinancialReportSummary_HY_specific_business = {
	description: `四半期 `,
	properties: {
		current_accumulated_q2_instant: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間時点`,
},
	},
} as const;

export const $QuarterlyPeriod_edjp_FinancialReportSummary_Q1 = {
	description: `四半期 `,
	properties: {
		current_accumulated_q1_instant: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第１四半期間時点`,
},
	},
} as const;

export const $QuarterlyPeriod_edjp_FinancialReportSummary_Q2 = {
	description: `四半期 `,
	properties: {
		current_accumulated_q2_instant: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間時点`,
},
	},
} as const;

export const $QuarterlyPeriod_edjp_FinancialReportSummary_Q3 = {
	description: `四半期 `,
	properties: {
		current_accumulated_q3_instant: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第３四半期間時点`,
},
	},
} as const;

export const $RatioOfTotalAmountOfDividendsToNetAssets_edjp_FinancialReportSummary_FY = {
	description: `純資産配当率 `,
	properties: {
		current_year_duration_annual_member_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_年間_連結_実績`,
},
		current_year_duration_annual_member_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_年間_非連結又は個別_実績`,
},
		prior_year_duration_annual_member_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度会計期間_年間_連結_実績`,
},
		prior_year_duration_annual_member_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度会計期間_年間_非連結又は個別_実績`,
},
	},
} as const;

export const $Token = {
	properties: {
		access_token: {
	type: 'string',
	isRequired: true,
},
		token_type: {
	type: 'string',
	default: 'bearer',
},
	},
} as const;

export const $TotalAssets_edjp_FinancialReportSummary = {
	description: `総資産 `,
	properties: {
		current_accumulated_q2_instant_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間時点_連結_実績`,
},
		prior_year_instant_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度時点_連結_実績`,
},
	},
} as const;

export const $TotalAssets_edjp_FinancialReportSummary_FY = {
	description: `総資産 `,
	properties: {
		current_year_instant_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度時点_連結_実績`,
},
		current_year_instant_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度時点_非連結又は個別_実績`,
},
		prior_year_instant_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度時点_連結_実績`,
},
		prior_year_instant_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度時点_非連結又は個別_実績`,
},
	},
} as const;

export const $TotalAssets_edjp_FinancialReportSummary_HY_specific_business = {
	description: `総資産 `,
	properties: {
		current_accumulated_q2_instant_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間時点_連結_実績`,
},
		current_accumulated_q2_instant_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間時点_非連結又は個別_実績`,
},
		prior_year_instant_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度時点_連結_実績`,
},
		prior_year_instant_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度時点_非連結又は個別_実績`,
},
	},
} as const;

export const $TotalAssets_edjp_FinancialReportSummary_Q1 = {
	description: `総資産 `,
	properties: {
		current_accumulated_q1_instant_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第１四半期間時点_連結_実績`,
},
		current_accumulated_q1_instant_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第１四半期間時点_非連結又は個別_実績`,
},
		prior_year_instant_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度時点_連結_実績`,
},
		prior_year_instant_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度時点_非連結又は個別_実績`,
},
	},
} as const;

export const $TotalAssets_edjp_FinancialReportSummary_Q2 = {
	description: `総資産 `,
	properties: {
		current_accumulated_q2_instant_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間時点_連結_実績`,
},
		current_accumulated_q2_instant_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第２四半期間時点_非連結又は個別_実績`,
},
		prior_year_instant_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度時点_連結_実績`,
},
		prior_year_instant_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度時点_非連結又は個別_実績`,
},
	},
} as const;

export const $TotalAssets_edjp_FinancialReportSummary_Q3 = {
	description: `総資産 `,
	properties: {
		current_accumulated_q3_instant_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度期初から第３四半期間時点_連結_実績`,
},
		prior_year_instant_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度時点_連結_実績`,
},
	},
} as const;

export const $TotalDividendPaidAnnual_edjp_FinancialReportSummary_FY = {
	description: `配当金総額（合計） `,
	properties: {
		current_year_duration_annual_member_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `当年度会計期間_年間_非連結又は個別_実績`,
},
		prior_year_duration_annual_member_non_consolidated_member_result_member: {
	type: 'IxNonFractionPublic',
	description: `前年度会計期間_年間_非連結又は個別_実績`,
},
	},
} as const;

export const $UpdatePassword = {
	properties: {
		current_password: {
	type: 'string',
	isRequired: true,
	maxLength: 40,
	minLength: 8,
},
		new_password: {
	type: 'string',
	isRequired: true,
	maxLength: 40,
	minLength: 8,
},
	},
} as const;

export const $UserCreate = {
	properties: {
		email: {
	type: 'string',
	isRequired: true,
	format: 'email',
	maxLength: 255,
},
		is_active: {
	type: 'boolean',
	default: true,
},
		is_superuser: {
	type: 'boolean',
	default: false,
},
		full_name: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 255,
}, {
	type: 'null',
}],
},
		password: {
	type: 'string',
	isRequired: true,
	maxLength: 40,
	minLength: 8,
},
	},
} as const;

export const $UserPublic = {
	properties: {
		email: {
	type: 'string',
	isRequired: true,
	format: 'email',
	maxLength: 255,
},
		is_active: {
	type: 'boolean',
	default: true,
},
		is_superuser: {
	type: 'boolean',
	default: false,
},
		full_name: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 255,
}, {
	type: 'null',
}],
},
		id: {
	type: 'string',
	isRequired: true,
	format: 'uuid',
},
	},
} as const;

export const $UserRegister = {
	properties: {
		email: {
	type: 'string',
	isRequired: true,
	format: 'email',
	maxLength: 255,
},
		password: {
	type: 'string',
	isRequired: true,
	maxLength: 40,
	minLength: 8,
},
		full_name: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 255,
}, {
	type: 'null',
}],
},
	},
} as const;

export const $UserUpdate = {
	properties: {
		email: {
	type: 'any-of',
	contains: [{
	type: 'string',
	format: 'email',
	maxLength: 255,
}, {
	type: 'null',
}],
},
		is_active: {
	type: 'boolean',
	default: true,
},
		is_superuser: {
	type: 'boolean',
	default: false,
},
		full_name: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 255,
}, {
	type: 'null',
}],
},
		password: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 40,
	minLength: 8,
}, {
	type: 'null',
}],
},
	},
} as const;

export const $UserUpdateMe = {
	properties: {
		full_name: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 255,
}, {
	type: 'null',
}],
},
		email: {
	type: 'any-of',
	contains: [{
	type: 'string',
	format: 'email',
	maxLength: 255,
}, {
	type: 'null',
}],
},
	},
} as const;

export const $UsersPublic = {
	properties: {
		data: {
	type: 'array',
	contains: {
		type: 'UserPublic',
	},
	isRequired: true,
},
		count: {
	type: 'number',
	isRequired: true,
},
	},
} as const;

export const $ValidationError = {
	properties: {
		loc: {
	type: 'array',
	contains: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'number',
}],
},
	isRequired: true,
},
		msg: {
	type: 'string',
	isRequired: true,
},
		type: {
	type: 'string',
	isRequired: true,
},
	},
} as const;

export const $edjp_FinancialReportSummary = {
	properties: {
		average_number_of_shares: {
	type: 'AverageNumberOfShares_edjp_FinancialReportSummary',
	description: `期中平均株式数`,
},
		capital_adequacy_ratio: {
	type: 'CapitalAdequacyRatio_edjp_FinancialReportSummary',
	description: `自己資本比率`,
},
		change_in_comprehensive_income: {
	type: 'ChangeInComprehensiveIncome_edjp_FinancialReportSummary',
	description: `包括利益増減率`,
},
		change_in_net_sales: {
	type: 'ChangeInNetSales_edjp_FinancialReportSummary',
	description: `増減率、売上高`,
},
		change_in_operating_income: {
	type: 'ChangeInOperatingIncome_edjp_FinancialReportSummary',
	description: `増減率、営業利益`,
},
		change_in_ordinary_income: {
	type: 'ChangeInOrdinaryIncome_edjp_FinancialReportSummary',
	description: `増減率、経常利益`,
},
		change_in_profit_attributable_to_owners_of_parent: {
	type: 'ChangeInProfitAttributableToOwnersOfParent_edjp_FinancialReportSummary',
	description: `増減率、親会社株主に帰属する当期純利益`,
},
		comprehensive_income: {
	type: 'ComprehensiveIncome_edjp_FinancialReportSummary',
	description: `包括利益`,
},
		diluted_net_income_per_share: {
	type: 'DilutedNetIncomePerShare_edjp_FinancialReportSummary',
	description: `潜在株式調整後1株当たり当期純利益`,
},
		dividend_per_share: {
	type: 'DividendPerShare_edjp_FinancialReportSummary',
	description: `1株当たり配当金`,
},
		net_assets: {
	type: 'NetAssets_edjp_FinancialReportSummary',
	description: `純資産`,
},
		net_assets_per_share: {
	type: 'NetAssetsPerShare_edjp_FinancialReportSummary',
	description: `1株当たり純資産`,
},
		net_income_per_share: {
	type: 'NetIncomePerShare_edjp_FinancialReportSummary',
	description: `1株当たり当期純利益`,
},
		net_sales: {
	type: 'NetSales_edjp_FinancialReportSummary',
	description: `売上高`,
},
		number_of_issued_and_outstanding_shares_at_the_end_of_fiscal_year_including_treasury_stock: {
	type: 'NumberOfIssuedAndOutstandingSharesAtTheEndOfFiscalYearIncludingTreasuryStock_edjp_FinancialReportSummary',
	description: `期末発行済株式数（自己株式を含む）`,
},
		number_of_treasury_stock_at_the_end_of_fiscal_year: {
	type: 'NumberOfTreasuryStockAtTheEndOfFiscalYear_edjp_FinancialReportSummary',
	description: `期末自己株式数`,
},
		operating_income: {
	type: 'OperatingIncome_edjp_FinancialReportSummary',
	description: `営業利益`,
},
		ordinary_income: {
	type: 'OrdinaryIncome_edjp_FinancialReportSummary',
	description: `経常利益`,
},
		owners_equity: {
	type: 'OwnersEquity_edjp_FinancialReportSummary',
	description: `自己資本`,
},
		profit_attributable_to_owners_of_parent: {
	type: 'ProfitAttributableToOwnersOfParent_edjp_FinancialReportSummary',
	description: `親会社株主に帰属する当期純利益`,
},
		quarterly_period: {
	type: 'QuarterlyPeriod_edjp_FinancialReportSummary',
	description: `四半期`,
},
		total_assets: {
	type: 'TotalAssets_edjp_FinancialReportSummary',
	description: `総資産`,
},
	},
} as const;

export const $edjp_FinancialReportSummary_FY = {
	properties: {
		average_number_of_shares: {
	type: 'AverageNumberOfShares_edjp_FinancialReportSummary_FY',
	description: `期中平均株式数`,
},
		capital_adequacy_ratio: {
	type: 'CapitalAdequacyRatio_edjp_FinancialReportSummary_FY',
	description: `自己資本比率`,
},
		cash_and_equivalents_end_of_period: {
	type: 'CashAndEquivalentsEndOfPeriod_edjp_FinancialReportSummary_FY',
	description: `現金及び現金同等物期末残高`,
},
		cash_flows_from_financing_activities: {
	type: 'CashFlowsFromFinancingActivities_edjp_FinancialReportSummary_FY',
	description: `財務活動によるキャッシュ・フロー`,
},
		cash_flows_from_investing_activities: {
	type: 'CashFlowsFromInvestingActivities_edjp_FinancialReportSummary_FY',
	description: `投資活動によるキャッシュ・フロー`,
},
		cash_flows_from_operating_activities: {
	type: 'CashFlowsFromOperatingActivities_edjp_FinancialReportSummary_FY',
	description: `営業活動によるキャッシュ・フロー`,
},
		change_in_comprehensive_income: {
	type: 'ChangeInComprehensiveIncome_edjp_FinancialReportSummary_FY',
	description: `包括利益増減率`,
},
		change_in_net_income: {
	type: 'ChangeInNetIncome_edjp_FinancialReportSummary_FY',
	description: `増減率、当期純利益`,
},
		change_in_net_sales: {
	type: 'ChangeInNetSales_edjp_FinancialReportSummary_FY',
	description: `増減率、売上高`,
},
		change_in_operating_income: {
	type: 'ChangeInOperatingIncome_edjp_FinancialReportSummary_FY',
	description: `増減率、営業利益`,
},
		change_in_ordinary_income: {
	type: 'ChangeInOrdinaryIncome_edjp_FinancialReportSummary_FY',
	description: `増減率、経常利益`,
},
		change_in_profit_attributable_to_owners_of_parent: {
	type: 'ChangeInProfitAttributableToOwnersOfParent_edjp_FinancialReportSummary_FY',
	description: `増減率、親会社株主に帰属する当期純利益`,
},
		comprehensive_income: {
	type: 'ComprehensiveIncome_edjp_FinancialReportSummary_FY',
	description: `包括利益`,
},
		diluted_net_income_per_share: {
	type: 'DilutedNetIncomePerShare_edjp_FinancialReportSummary_FY',
	description: `潜在株式調整後1株当たり当期純利益`,
},
		dividend_per_share: {
	type: 'DividendPerShare_edjp_FinancialReportSummary_FY',
	description: `1株当たり配当金`,
},
		investment_profit_loss_on_equity_method: {
	type: 'InvestmentProfitLossOnEquityMethod_edjp_FinancialReportSummary_FY',
	description: `持分法投資損益`,
},
		net_assets: {
	type: 'NetAssets_edjp_FinancialReportSummary_FY',
	description: `純資産`,
},
		net_assets_per_share: {
	type: 'NetAssetsPerShare_edjp_FinancialReportSummary_FY',
	description: `1株当たり純資産`,
},
		net_income: {
	type: 'NetIncome_edjp_FinancialReportSummary_FY',
	description: `当期純利益`,
},
		net_income_per_share: {
	type: 'NetIncomePerShare_edjp_FinancialReportSummary_FY',
	description: `1株当たり当期純利益`,
},
		net_income_to_shareholders_equity_ratio: {
	type: 'NetIncomeToShareholdersEquityRatio_edjp_FinancialReportSummary_FY',
	description: `自己資本当期純利益率`,
},
		net_sales: {
	type: 'NetSales_edjp_FinancialReportSummary_FY',
	description: `売上高`,
},
		number_of_issued_and_outstanding_shares_at_the_end_of_fiscal_year_including_treasury_stock: {
	type: 'NumberOfIssuedAndOutstandingSharesAtTheEndOfFiscalYearIncludingTreasuryStock_edjp_FinancialReportSummary_FY',
	description: `期末発行済株式数（自己株式を含む）`,
},
		number_of_subsidiaries_excluded_from_consolidation: {
	type: 'NumberOfSubsidiariesExcludedFromConsolidation_edjp_FinancialReportSummary_FY',
	description: `除外`,
},
		number_of_subsidiaries_newly_consolidated: {
	type: 'NumberOfSubsidiariesNewlyConsolidated_edjp_FinancialReportSummary_FY',
	description: `新規`,
},
		number_of_treasury_stock_at_the_end_of_fiscal_year: {
	type: 'NumberOfTreasuryStockAtTheEndOfFiscalYear_edjp_FinancialReportSummary_FY',
	description: `期末自己株式数`,
},
		operating_income: {
	type: 'OperatingIncome_edjp_FinancialReportSummary_FY',
	description: `営業利益`,
},
		operating_income_to_net_sales_ratio: {
	type: 'OperatingIncomeToNetSalesRatio_edjp_FinancialReportSummary_FY',
	description: `売上高営業利益率`,
},
		ordinary_income: {
	type: 'OrdinaryIncome_edjp_FinancialReportSummary_FY',
	description: `経常利益`,
},
		ordinary_income_to_total_assets_ratio: {
	type: 'OrdinaryIncomeToTotalAssetsRatio_edjp_FinancialReportSummary_FY',
	description: `総資産経常利益率`,
},
		owners_equity: {
	type: 'OwnersEquity_edjp_FinancialReportSummary_FY',
	description: `自己資本`,
},
		payout_ratio: {
	type: 'PayoutRatio_edjp_FinancialReportSummary_FY',
	description: `配当性向`,
},
		profit_attributable_to_owners_of_parent: {
	type: 'ProfitAttributableToOwnersOfParent_edjp_FinancialReportSummary_FY',
	description: `親会社株主に帰属する当期純利益`,
},
		ratio_of_total_amount_of_dividends_to_net_assets: {
	type: 'RatioOfTotalAmountOfDividendsToNetAssets_edjp_FinancialReportSummary_FY',
	description: `純資産配当率`,
},
		total_assets: {
	type: 'TotalAssets_edjp_FinancialReportSummary_FY',
	description: `総資産`,
},
		total_dividend_paid_annual: {
	type: 'TotalDividendPaidAnnual_edjp_FinancialReportSummary_FY',
	description: `配当金総額（合計）`,
},
	},
} as const;

export const $edjp_FinancialReportSummary_HY_specific_business = {
	properties: {
		average_number_of_shares: {
	type: 'AverageNumberOfShares_edjp_FinancialReportSummary_HY_specific_business',
	description: `期中平均株式数`,
},
		capital_adequacy_ratio: {
	type: 'CapitalAdequacyRatio_edjp_FinancialReportSummary_HY_specific_business',
	description: `自己資本比率`,
},
		change_in_comprehensive_income: {
	type: 'ChangeInComprehensiveIncome_edjp_FinancialReportSummary_HY_specific_business',
	description: `包括利益増減率`,
},
		change_in_net_income: {
	type: 'ChangeInNetIncome_edjp_FinancialReportSummary_HY_specific_business',
	description: `増減率、当期純利益`,
},
		change_in_ordinary_income: {
	type: 'ChangeInOrdinaryIncome_edjp_FinancialReportSummary_HY_specific_business',
	description: `増減率、経常利益`,
},
		change_in_ordinary_revenues_bk: {
	type: 'ChangeInOrdinaryRevenuesBK_edjp_FinancialReportSummary_HY_specific_business',
	description: `増減率、経常収益、銀行`,
},
		change_in_profit_attributable_to_owners_of_parent: {
	type: 'ChangeInProfitAttributableToOwnersOfParent_edjp_FinancialReportSummary_HY_specific_business',
	description: `増減率、親会社株主に帰属する当期純利益`,
},
		comprehensive_income: {
	type: 'ComprehensiveIncome_edjp_FinancialReportSummary_HY_specific_business',
	description: `包括利益`,
},
		diluted_net_income_per_share: {
	type: 'DilutedNetIncomePerShare_edjp_FinancialReportSummary_HY_specific_business',
	description: `潜在株式調整後1株当たり当期純利益`,
},
		dividend_per_share: {
	type: 'DividendPerShare_edjp_FinancialReportSummary_HY_specific_business',
	description: `1株当たり配当金`,
},
		net_assets: {
	type: 'NetAssets_edjp_FinancialReportSummary_HY_specific_business',
	description: `純資産`,
},
		net_assets_per_share: {
	type: 'NetAssetsPerShare_edjp_FinancialReportSummary_HY_specific_business',
	description: `1株当たり純資産`,
},
		net_income: {
	type: 'NetIncome_edjp_FinancialReportSummary_HY_specific_business',
	description: `当期純利益`,
},
		net_income_per_share: {
	type: 'NetIncomePerShare_edjp_FinancialReportSummary_HY_specific_business',
	description: `1株当たり当期純利益`,
},
		number_of_issued_and_outstanding_shares_at_the_end_of_fiscal_year_including_treasury_stock: {
	type: 'NumberOfIssuedAndOutstandingSharesAtTheEndOfFiscalYearIncludingTreasuryStock_edjp_FinancialReportSummary_HY_specific_business',
	description: `期末発行済株式数（自己株式を含む）`,
},
		number_of_treasury_stock_at_the_end_of_fiscal_year: {
	type: 'NumberOfTreasuryStockAtTheEndOfFiscalYear_edjp_FinancialReportSummary_HY_specific_business',
	description: `期末自己株式数`,
},
		ordinary_income: {
	type: 'OrdinaryIncome_edjp_FinancialReportSummary_HY_specific_business',
	description: `経常利益`,
},
		ordinary_revenues_bk: {
	type: 'OrdinaryRevenuesBK_edjp_FinancialReportSummary_HY_specific_business',
	description: `経常収益、銀行`,
},
		owners_equity: {
	type: 'OwnersEquity_edjp_FinancialReportSummary_HY_specific_business',
	description: `自己資本`,
},
		profit_attributable_to_owners_of_parent: {
	type: 'ProfitAttributableToOwnersOfParent_edjp_FinancialReportSummary_HY_specific_business',
	description: `親会社株主に帰属する当期純利益`,
},
		quarterly_period: {
	type: 'QuarterlyPeriod_edjp_FinancialReportSummary_HY_specific_business',
	description: `四半期`,
},
		total_assets: {
	type: 'TotalAssets_edjp_FinancialReportSummary_HY_specific_business',
	description: `総資産`,
},
	},
} as const;

export const $edjp_FinancialReportSummary_Q1 = {
	properties: {
		average_number_of_shares: {
	type: 'AverageNumberOfShares_edjp_FinancialReportSummary_Q1',
	description: `期中平均株式数`,
},
		capital_adequacy_ratio: {
	type: 'CapitalAdequacyRatio_edjp_FinancialReportSummary_Q1',
	description: `自己資本比率`,
},
		change_in_comprehensive_income: {
	type: 'ChangeInComprehensiveIncome_edjp_FinancialReportSummary_Q1',
	description: `包括利益増減率`,
},
		change_in_net_income: {
	type: 'ChangeInNetIncome_edjp_FinancialReportSummary_Q1',
	description: `増減率、当期純利益`,
},
		change_in_net_sales: {
	type: 'ChangeInNetSales_edjp_FinancialReportSummary_Q1',
	description: `増減率、売上高`,
},
		change_in_operating_income: {
	type: 'ChangeInOperatingIncome_edjp_FinancialReportSummary_Q1',
	description: `増減率、営業利益`,
},
		change_in_ordinary_income: {
	type: 'ChangeInOrdinaryIncome_edjp_FinancialReportSummary_Q1',
	description: `増減率、経常利益`,
},
		change_in_profit_attributable_to_owners_of_parent: {
	type: 'ChangeInProfitAttributableToOwnersOfParent_edjp_FinancialReportSummary_Q1',
	description: `増減率、親会社株主に帰属する当期純利益`,
},
		comprehensive_income: {
	type: 'ComprehensiveIncome_edjp_FinancialReportSummary_Q1',
	description: `包括利益`,
},
		diluted_net_income_per_share: {
	type: 'DilutedNetIncomePerShare_edjp_FinancialReportSummary_Q1',
	description: `潜在株式調整後1株当たり当期純利益`,
},
		dividend_per_share: {
	type: 'DividendPerShare_edjp_FinancialReportSummary_Q1',
	description: `1株当たり配当金`,
},
		net_assets: {
	type: 'NetAssets_edjp_FinancialReportSummary_Q1',
	description: `純資産`,
},
		net_assets_per_share: {
	type: 'NetAssetsPerShare_edjp_FinancialReportSummary_Q1',
	description: `1株当たり純資産`,
},
		net_income: {
	type: 'NetIncome_edjp_FinancialReportSummary_Q1',
	description: `当期純利益`,
},
		net_income_per_share: {
	type: 'NetIncomePerShare_edjp_FinancialReportSummary_Q1',
	description: `1株当たり当期純利益`,
},
		net_sales: {
	type: 'NetSales_edjp_FinancialReportSummary_Q1',
	description: `売上高`,
},
		number_of_issued_and_outstanding_shares_at_the_end_of_fiscal_year_including_treasury_stock: {
	type: 'NumberOfIssuedAndOutstandingSharesAtTheEndOfFiscalYearIncludingTreasuryStock_edjp_FinancialReportSummary_Q1',
	description: `期末発行済株式数（自己株式を含む）`,
},
		number_of_subsidiaries_excluded_from_consolidation: {
	type: 'NumberOfSubsidiariesExcludedFromConsolidation_edjp_FinancialReportSummary_Q1',
	description: `除外`,
},
		number_of_subsidiaries_newly_consolidated: {
	type: 'NumberOfSubsidiariesNewlyConsolidated_edjp_FinancialReportSummary_Q1',
	description: `新規`,
},
		number_of_treasury_stock_at_the_end_of_fiscal_year: {
	type: 'NumberOfTreasuryStockAtTheEndOfFiscalYear_edjp_FinancialReportSummary_Q1',
	description: `期末自己株式数`,
},
		operating_income: {
	type: 'OperatingIncome_edjp_FinancialReportSummary_Q1',
	description: `営業利益`,
},
		ordinary_income: {
	type: 'OrdinaryIncome_edjp_FinancialReportSummary_Q1',
	description: `経常利益`,
},
		owners_equity: {
	type: 'OwnersEquity_edjp_FinancialReportSummary_Q1',
	description: `自己資本`,
},
		profit_attributable_to_owners_of_parent: {
	type: 'ProfitAttributableToOwnersOfParent_edjp_FinancialReportSummary_Q1',
	description: `親会社株主に帰属する当期純利益`,
},
		quarterly_period: {
	type: 'QuarterlyPeriod_edjp_FinancialReportSummary_Q1',
	description: `四半期`,
},
		total_assets: {
	type: 'TotalAssets_edjp_FinancialReportSummary_Q1',
	description: `総資産`,
},
	},
} as const;

export const $edjp_FinancialReportSummary_Q2 = {
	properties: {
		average_number_of_shares: {
	type: 'AverageNumberOfShares_edjp_FinancialReportSummary_Q2',
	description: `期中平均株式数`,
},
		capital_adequacy_ratio: {
	type: 'CapitalAdequacyRatio_edjp_FinancialReportSummary_Q2',
	description: `自己資本比率`,
},
		change_in_comprehensive_income: {
	type: 'ChangeInComprehensiveIncome_edjp_FinancialReportSummary_Q2',
	description: `包括利益増減率`,
},
		change_in_net_income: {
	type: 'ChangeInNetIncome_edjp_FinancialReportSummary_Q2',
	description: `増減率、当期純利益`,
},
		change_in_net_operating_revenues_se: {
	type: 'ChangeInNetOperatingRevenuesSE_edjp_FinancialReportSummary_Q2',
	description: `増減率、純営業収益、証券`,
},
		change_in_net_sales: {
	type: 'ChangeInNetSales_edjp_FinancialReportSummary_Q2',
	description: `増減率、売上高`,
},
		change_in_operating_income: {
	type: 'ChangeInOperatingIncome_edjp_FinancialReportSummary_Q2',
	description: `増減率、営業利益`,
},
		change_in_operating_revenues: {
	type: 'ChangeInOperatingRevenues_edjp_FinancialReportSummary_Q2',
	description: `増減率、営業収益`,
},
		change_in_operating_revenues_se: {
	type: 'ChangeInOperatingRevenuesSE_edjp_FinancialReportSummary_Q2',
	description: `増減率、営業収益、証券`,
},
		change_in_ordinary_income: {
	type: 'ChangeInOrdinaryIncome_edjp_FinancialReportSummary_Q2',
	description: `増減率、経常利益`,
},
		change_in_profit_attributable_to_owners_of_parent: {
	type: 'ChangeInProfitAttributableToOwnersOfParent_edjp_FinancialReportSummary_Q2',
	description: `増減率、親会社株主に帰属する当期純利益`,
},
		commemorative_dividend: {
	type: 'CommemorativeDividend_edjp_FinancialReportSummary_Q2',
	description: `記念配当`,
},
		comprehensive_income: {
	type: 'ComprehensiveIncome_edjp_FinancialReportSummary_Q2',
	description: `包括利益`,
},
		diluted_net_income_per_share: {
	type: 'DilutedNetIncomePerShare_edjp_FinancialReportSummary_Q2',
	description: `潜在株式調整後1株当たり当期純利益`,
},
		dividend_per_share: {
	type: 'DividendPerShare_edjp_FinancialReportSummary_Q2',
	description: `1株当たり配当金`,
},
		extra_dividend: {
	type: 'ExtraDividend_edjp_FinancialReportSummary_Q2',
	description: `特別配当`,
},
		net_assets: {
	type: 'NetAssets_edjp_FinancialReportSummary_Q2',
	description: `純資産`,
},
		net_assets_per_share: {
	type: 'NetAssetsPerShare_edjp_FinancialReportSummary_Q2',
	description: `1株当たり純資産`,
},
		net_income: {
	type: 'NetIncome_edjp_FinancialReportSummary_Q2',
	description: `当期純利益`,
},
		net_income_per_share: {
	type: 'NetIncomePerShare_edjp_FinancialReportSummary_Q2',
	description: `1株当たり当期純利益`,
},
		net_operating_revenues_se: {
	type: 'NetOperatingRevenuesSE_edjp_FinancialReportSummary_Q2',
	description: `純営業収益、証券`,
},
		net_sales: {
	type: 'NetSales_edjp_FinancialReportSummary_Q2',
	description: `売上高`,
},
		number_of_issued_and_outstanding_shares_at_the_end_of_fiscal_year_including_treasury_stock: {
	type: 'NumberOfIssuedAndOutstandingSharesAtTheEndOfFiscalYearIncludingTreasuryStock_edjp_FinancialReportSummary_Q2',
	description: `期末発行済株式数（自己株式を含む）`,
},
		number_of_subsidiaries_excluded_from_consolidation: {
	type: 'NumberOfSubsidiariesExcludedFromConsolidation_edjp_FinancialReportSummary_Q2',
	description: `除外`,
},
		number_of_subsidiaries_newly_consolidated: {
	type: 'NumberOfSubsidiariesNewlyConsolidated_edjp_FinancialReportSummary_Q2',
	description: `新規`,
},
		number_of_treasury_stock_at_the_end_of_fiscal_year: {
	type: 'NumberOfTreasuryStockAtTheEndOfFiscalYear_edjp_FinancialReportSummary_Q2',
	description: `期末自己株式数`,
},
		operating_income: {
	type: 'OperatingIncome_edjp_FinancialReportSummary_Q2',
	description: `営業利益`,
},
		operating_revenues: {
	type: 'OperatingRevenues_edjp_FinancialReportSummary_Q2',
	description: `営業収益`,
},
		operating_revenues_se: {
	type: 'OperatingRevenuesSE_edjp_FinancialReportSummary_Q2',
	description: `営業収益、証券`,
},
		ordinary_income: {
	type: 'OrdinaryIncome_edjp_FinancialReportSummary_Q2',
	description: `経常利益`,
},
		owners_equity: {
	type: 'OwnersEquity_edjp_FinancialReportSummary_Q2',
	description: `自己資本`,
},
		profit_attributable_to_owners_of_parent: {
	type: 'ProfitAttributableToOwnersOfParent_edjp_FinancialReportSummary_Q2',
	description: `親会社株主に帰属する当期純利益`,
},
		quarterly_period: {
	type: 'QuarterlyPeriod_edjp_FinancialReportSummary_Q2',
	description: `四半期`,
},
		total_assets: {
	type: 'TotalAssets_edjp_FinancialReportSummary_Q2',
	description: `総資産`,
},
	},
} as const;

export const $edjp_FinancialReportSummary_Q3 = {
	properties: {
		average_number_of_shares: {
	type: 'AverageNumberOfShares_edjp_FinancialReportSummary_Q3',
	description: `期中平均株式数`,
},
		capital_adequacy_ratio: {
	type: 'CapitalAdequacyRatio_edjp_FinancialReportSummary_Q3',
	description: `自己資本比率`,
},
		change_in_comprehensive_income: {
	type: 'ChangeInComprehensiveIncome_edjp_FinancialReportSummary_Q3',
	description: `包括利益増減率`,
},
		change_in_net_sales: {
	type: 'ChangeInNetSales_edjp_FinancialReportSummary_Q3',
	description: `増減率、売上高`,
},
		change_in_operating_income: {
	type: 'ChangeInOperatingIncome_edjp_FinancialReportSummary_Q3',
	description: `増減率、営業利益`,
},
		change_in_ordinary_income: {
	type: 'ChangeInOrdinaryIncome_edjp_FinancialReportSummary_Q3',
	description: `増減率、経常利益`,
},
		change_in_profit_attributable_to_owners_of_parent: {
	type: 'ChangeInProfitAttributableToOwnersOfParent_edjp_FinancialReportSummary_Q3',
	description: `増減率、親会社株主に帰属する当期純利益`,
},
		comprehensive_income: {
	type: 'ComprehensiveIncome_edjp_FinancialReportSummary_Q3',
	description: `包括利益`,
},
		diluted_net_income_per_share: {
	type: 'DilutedNetIncomePerShare_edjp_FinancialReportSummary_Q3',
	description: `潜在株式調整後1株当たり当期純利益`,
},
		dividend_per_share: {
	type: 'DividendPerShare_edjp_FinancialReportSummary_Q3',
	description: `1株当たり配当金`,
},
		net_assets: {
	type: 'NetAssets_edjp_FinancialReportSummary_Q3',
	description: `純資産`,
},
		net_assets_per_share: {
	type: 'NetAssetsPerShare_edjp_FinancialReportSummary_Q3',
	description: `1株当たり純資産`,
},
		net_income_per_share: {
	type: 'NetIncomePerShare_edjp_FinancialReportSummary_Q3',
	description: `1株当たり当期純利益`,
},
		net_sales: {
	type: 'NetSales_edjp_FinancialReportSummary_Q3',
	description: `売上高`,
},
		number_of_issued_and_outstanding_shares_at_the_end_of_fiscal_year_including_treasury_stock: {
	type: 'NumberOfIssuedAndOutstandingSharesAtTheEndOfFiscalYearIncludingTreasuryStock_edjp_FinancialReportSummary_Q3',
	description: `期末発行済株式数（自己株式を含む）`,
},
		number_of_subsidiaries_excluded_from_consolidation: {
	type: 'NumberOfSubsidiariesExcludedFromConsolidation_edjp_FinancialReportSummary_Q3',
	description: `除外`,
},
		number_of_subsidiaries_newly_consolidated: {
	type: 'NumberOfSubsidiariesNewlyConsolidated_edjp_FinancialReportSummary_Q3',
	description: `新規`,
},
		number_of_treasury_stock_at_the_end_of_fiscal_year: {
	type: 'NumberOfTreasuryStockAtTheEndOfFiscalYear_edjp_FinancialReportSummary_Q3',
	description: `期末自己株式数`,
},
		operating_income: {
	type: 'OperatingIncome_edjp_FinancialReportSummary_Q3',
	description: `営業利益`,
},
		ordinary_income: {
	type: 'OrdinaryIncome_edjp_FinancialReportSummary_Q3',
	description: `経常利益`,
},
		owners_equity: {
	type: 'OwnersEquity_edjp_FinancialReportSummary_Q3',
	description: `自己資本`,
},
		profit_attributable_to_owners_of_parent: {
	type: 'ProfitAttributableToOwnersOfParent_edjp_FinancialReportSummary_Q3',
	description: `親会社株主に帰属する当期純利益`,
},
		quarterly_period: {
	type: 'QuarterlyPeriod_edjp_FinancialReportSummary_Q3',
	description: `四半期`,
},
		total_assets: {
	type: 'TotalAssets_edjp_FinancialReportSummary_Q3',
	description: `総資産`,
},
	},
} as const;