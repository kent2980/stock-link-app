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

export const $BusinessResultsFinancialPositionsJp = {
	description: `業績及び財政状態に関する注記を公開するためのクラス`,
	properties: {
		order: {
	type: 'any-of',
	description: `順序`,
	contains: [{
	type: 'number',
}, {
	type: 'null',
}],
},
		Label: {
	type: 'any-of',
	description: `ラベル`,
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
		FinancialPositions: {
	type: 'FinancialPositionsAbstractJp',
	description: `財政状態の概要`,
},
		NoteToFinancialPositions: {
	type: 'NoteToFinancialPositionsAbstractJp',
	description: `連結財務諸表に関する注記`,
},
	},
} as const;

export const $DividendPerShareJp = {
	description: `1株当たり配当に関する情報を公開するためのクラス`,
	properties: {
		order: {
	type: 'any-of',
	description: `順序`,
	contains: [{
	type: 'number',
}, {
	type: 'null',
}],
},
		Label: {
	type: 'any-of',
	description: `ラベル`,
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
		FirstQuarterPriorYearResults: {
	type: 'any-of',
	description: `昨季Q1期末1株当たり配当実績`,
	contains: [{
	type: 'stockNumeric',
}, {
	type: 'null',
}],
},
		SecondQuarterPriorYearResults: {
	type: 'any-of',
	description: `昨季中間期末1株当たり配当実績`,
	contains: [{
	type: 'stockNumeric',
}, {
	type: 'null',
}],
},
		ThirdQuarterPriorYearResults: {
	type: 'any-of',
	description: `昨季Q3期末1株当たり配当実績`,
	contains: [{
	type: 'stockNumeric',
}, {
	type: 'null',
}],
},
		YearEndPriorYearResults: {
	type: 'any-of',
	description: `昨季期末1株当たり配当実績`,
	contains: [{
	type: 'stockNumeric',
}, {
	type: 'null',
}],
},
		AnnualPriorYearResults: {
	type: 'any-of',
	description: `昨季年間1株当たり配当実績`,
	contains: [{
	type: 'stockNumeric',
}, {
	type: 'null',
}],
},
		FirstQuarterCurrentYearResults: {
	type: 'any-of',
	description: `今期Q1期末1株当たり配当実績`,
	contains: [{
	type: 'stockNumeric',
}, {
	type: 'null',
}],
},
		SecondQuarterCurrentYearResults: {
	type: 'any-of',
	description: `今期中間期末1株当たり配当実績`,
	contains: [{
	type: 'stockNumeric',
}, {
	type: 'null',
}],
},
		ThirdQuarterCurrentYearResults: {
	type: 'any-of',
	description: `今期Q3期末1株当たり配当実績`,
	contains: [{
	type: 'stockNumeric',
}, {
	type: 'null',
}],
},
		YearEndCurrentYearResults: {
	type: 'any-of',
	description: `今期期末1株当たり配当実績`,
	contains: [{
	type: 'stockNumeric',
}, {
	type: 'null',
}],
},
		AnnualCurrentYearResults: {
	type: 'any-of',
	description: `今期年間1株当たり配当実績`,
	contains: [{
	type: 'stockNumeric',
}, {
	type: 'null',
}],
},
		FirstQuarterCurrentYearForecasts: {
	type: 'any-of',
	description: `今期Q1期末1株当たり配当予想`,
	contains: [{
	type: 'stockNumeric',
}, {
	type: 'null',
}],
},
		SecondQuarterCurrentYearForecasts: {
	type: 'any-of',
	description: `今期中間期末1株当たり配当予想`,
	contains: [{
	type: 'stockNumeric',
}, {
	type: 'null',
}],
},
		ThirdQuarterCurrentYearForecasts: {
	type: 'any-of',
	description: `今期Q3期末1株当たり配当予想`,
	contains: [{
	type: 'stockNumeric',
}, {
	type: 'null',
}],
},
		YearEndCurrentYearForecasts: {
	type: 'any-of',
	description: `今期期末1株当たり配当予想`,
	contains: [{
	type: 'stockNumeric',
}, {
	type: 'null',
}],
},
		AnnualCurrentYearForecasts: {
	type: 'any-of',
	description: `今期年間1株当たり配当予想`,
	contains: [{
	type: 'stockNumeric',
}, {
	type: 'null',
}],
},
		FirstQuarterNextYearForecasts: {
	type: 'any-of',
	description: `来期Q1期末1株当たり配当予想`,
	contains: [{
	type: 'stockNumeric',
}, {
	type: 'null',
}],
},
		SecondQuarterNextYearForecasts: {
	type: 'any-of',
	description: `来期中間期末1株当たり配当予想`,
	contains: [{
	type: 'stockNumeric',
}, {
	type: 'null',
}],
},
		ThirdQuarterNextYearForecasts: {
	type: 'any-of',
	description: `来期Q3期末1株当たり配当予想`,
	contains: [{
	type: 'stockNumeric',
}, {
	type: 'null',
}],
},
		YearEndNextYearForecasts: {
	type: 'any-of',
	description: `来期期末1株当たり配当予想`,
	contains: [{
	type: 'stockNumeric',
}, {
	type: 'null',
}],
},
		AnnualNextYearForecasts: {
	type: 'any-of',
	description: `来期年間1株当たり配当予想`,
	contains: [{
	type: 'stockNumeric',
}, {
	type: 'null',
}],
},
	},
} as const;

export const $DividendsJp = {
	description: `四半期配当に関する注記を公開するためのクラス`,
	properties: {
		order: {
	type: 'any-of',
	description: `順序`,
	contains: [{
	type: 'number',
}, {
	type: 'null',
}],
},
		Label: {
	type: 'any-of',
	description: `ラベル`,
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
		DividendPerShare: {
	type: 'any-of',
	description: `1株当たり配当`,
	contains: [{
	type: 'DividendPerShareJp',
}, {
	type: 'null',
}],
},
		CorrectionOfDividendForecast: {
	type: 'any-of',
	description: `当四半期における配当予想の修正`,
	contains: [{
	type: 'stockNumeric',
}, {
	type: 'null',
}],
},
		DetailOfDividendPerShareFiscalYearEndAbstract: {
	type: 'any-of',
	description: `期末1株当たり配当の内訳`,
	contains: [{
	type: 'stockNumeric',
}, {
	type: 'null',
}],
},
		NoteToDividends: {
	type: 'any-of',
	description: `配当に関する注記`,
	contains: [{
	type: 'stockNumeric',
}, {
	type: 'null',
}],
},
		DividendPayoutRatioPriorYear: {
	type: 'any-of',
	description: `配当性向`,
	contains: [{
	type: 'stockNumeric',
}, {
	type: 'null',
}],
},
		DividendPayoutRatioCurrentYear: {
	type: 'any-of',
	description: `配当性向`,
	contains: [{
	type: 'stockNumeric',
}, {
	type: 'null',
}],
},
		DividendPayoutRatioNextYear: {
	type: 'any-of',
	description: `配当性向`,
	contains: [{
	type: 'stockNumeric',
}, {
	type: 'null',
}],
},
		RatioOfTotalAmountOfDividendsToNetAssets: {
	type: 'any-of',
	description: `配当総額純資産比率`,
	contains: [{
	type: 'stockNumeric',
}, {
	type: 'null',
}],
},
	},
} as const;

export const $FinancialPositionsAbstractJp = {
	description: `財政状態の概要を公開するためのクラス`,
	properties: {
		order: {
	type: 'any-of',
	description: `順序`,
	contains: [{
	type: 'number',
}, {
	type: 'null',
}],
},
		Label: {
	type: 'any-of',
	description: `ラベル`,
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
		CapitalAdequacyRatio: {
	type: 'any-of',
	description: `総資産`,
	contains: [{
	type: 'stockNumeric',
}, {
	type: 'null',
}],
},
		NetAssets: {
	type: 'any-of',
	description: `純資産`,
	contains: [{
	type: 'stockNumeric',
}, {
	type: 'null',
}],
},
		TotalAssets: {
	type: 'any-of',
	description: `自己資本`,
	contains: [{
	type: 'stockNumeric',
}, {
	type: 'null',
}],
},
		PeriodCapitalAdequacyRatio: {
	type: 'any-of',
	description: `昨年度総資産`,
	contains: [{
	type: 'stockNumeric',
}, {
	type: 'null',
}],
},
		PeriodNetAssets: {
	type: 'any-of',
	description: `昨年度純資産`,
	contains: [{
	type: 'stockNumeric',
}, {
	type: 'null',
}],
},
		PeriodTotalAssets: {
	type: 'any-of',
	description: `昨年度自己資本`,
	contains: [{
	type: 'stockNumeric',
}, {
	type: 'null',
}],
},
	},
} as const;

export const $ForecastsJp = {
	description: `四半期予想に関する注記を公開するためのクラス`,
	properties: {
		order: {
	type: 'any-of',
	description: `順序`,
	contains: [{
	type: 'number',
}, {
	type: 'null',
}],
},
		Label: {
	type: 'any-of',
	description: `ラベル`,
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
		TitleForForecasts: {
	type: 'any-of',
	description: `予想のタイトル`,
	contains: [{
	type: 'stockNumeric',
}, {
	type: 'null',
}],
},
		CorrectionOfFinancialForecastInThisQuarter: {
	type: 'any-of',
	description: `当四半期における連結業績予想の修正`,
	contains: [{
	type: 'stockNumeric',
}, {
	type: 'null',
}],
},
		NetSales: {
	type: 'any-of',
	description: `売上高`,
	contains: [{
	type: 'abstract',
}, {
	type: 'null',
}],
},
		OperatingIncome: {
	type: 'any-of',
	description: `営業利益`,
	contains: [{
	type: 'abstract',
}, {
	type: 'null',
}],
},
		OrdinaryIncome: {
	type: 'any-of',
	description: `経常利益`,
	contains: [{
	type: 'abstract',
}, {
	type: 'null',
}],
},
		ProfitAttributableToOwnersOfParent: {
	type: 'any-of',
	description: `親会社株主に帰属する当期純利益`,
	contains: [{
	type: 'abstract',
}, {
	type: 'null',
}],
},
		NetIncomePerShare: {
	type: 'any-of',
	description: `1株当たり当期純利益`,
	contains: [{
	type: 'stockNumeric',
}, {
	type: 'null',
}],
},
		NoteToForecasts: {
	type: 'any-of',
	description: `予想に関する注記`,
	contains: [{
	type: 'stockNumeric',
}, {
	type: 'null',
}],
},
		PreambleToForecasts: {
	type: 'any-of',
	description: `予想の前文`,
	contains: [{
	type: 'stockNumeric',
}, {
	type: 'null',
}],
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

export const $HeadItem = {
	description: `iXBRLのソースID情報を表すクラス`,
	properties: {
		item_key: {
	type: 'string',
	isRequired: true,
},
		company_name: {
	type: 'string',
	isRequired: true,
},
		securities_code: {
	type: 'string',
	isRequired: true,
},
		document_name: {
	type: 'string',
	isRequired: true,
},
		reporting_date: {
	type: 'string',
	isRequired: true,
	format: 'date',
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
	},
} as const;

export const $HeadItems = {
	description: `iXBRLのソースID情報のリストを表すクラス`,
	properties: {
		data: {
	type: 'array',
	contains: {
		type: 'HeadItem',
	},
	isRequired: true,
},
		count: {
	type: 'number',
	isRequired: true,
},
	},
} as const;

export const $IncomeStatementsInformationAbstractJp = {
	description: `損益計算書情報を公開するためのクラス`,
	properties: {
		order: {
	type: 'any-of',
	description: `順序`,
	contains: [{
	type: 'number',
}, {
	type: 'null',
}],
},
		Label: {
	type: 'any-of',
	description: `ラベル`,
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
		NetSales: {
	type: 'abstract',
	description: `売上高`,
},
		PeriodNetSales: {
	type: 'abstract',
	description: `昨年度売上高`,
},
		OperatingIncome: {
	type: 'abstract',
	description: `営業利益`,
},
		PeriodOperatingIncome: {
	type: 'abstract',
	description: `昨年度営業利益`,
},
		OrdinaryIncome: {
	type: 'abstract',
	description: `経常利益`,
},
		PeriodOrdinaryIncome: {
	type: 'abstract',
	description: `昨年度経常利益`,
},
		Profit: {
	type: 'abstract',
	description: `親会社株主に帰属する当期純利益`,
},
		PeriodProfit: {
	type: 'abstract',
	description: `昨年度親会社株主に帰属する当期純利益`,
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

export const $NoteToFinancialPositionsAbstractJp = {
	description: `連結財務諸表に関する注記を公開するためのクラス`,
	properties: {
		order: {
	type: 'any-of',
	description: `順序`,
	contains: [{
	type: 'number',
}, {
	type: 'null',
}],
},
		Label: {
	type: 'any-of',
	description: `ラベル`,
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
		NoteToFinancialPositions: {
	type: 'any-of',
	description: `連結財務諸表に関する注記`,
	contains: [{
	type: 'stockNumeric',
}, {
	type: 'null',
}],
},
		OwnersEquity: {
	type: 'any-of',
	description: `自己資本`,
	contains: [{
	type: 'stockNumeric',
}, {
	type: 'null',
}],
},
	},
} as const;

export const $NoteToFinancialResultsJp = {
	description: `連結財務諸表に関する注記を公開するためのクラス`,
	properties: {
		order: {
	type: 'any-of',
	description: `順序`,
	contains: [{
	type: 'number',
}, {
	type: 'null',
}],
},
		Label: {
	type: 'any-of',
	description: `ラベル`,
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
		NoteToFinancialResults: {
	type: 'any-of',
	description: `連結財務諸表に関する注記`,
	contains: [{
	type: 'stockNumeric',
}, {
	type: 'null',
}],
},
	},
} as const;

export const $NoteToIncomeStatementsInformationAbstractJp = {
	description: `損益計算書情報に関する注記を公開するためのクラス`,
	properties: {
		order: {
	type: 'any-of',
	description: `順序`,
	contains: [{
	type: 'number',
}, {
	type: 'null',
}],
},
		Label: {
	type: 'any-of',
	description: `ラベル`,
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
		ComprehensiveIncomeAbstract: {
	type: 'abstract',
	description: `包括利益`,
},
		PeriodComprehensiveIncomeAbstract: {
	type: 'abstract',
	description: `昨年度包括利益`,
},
	},
} as const;

export const $NoteToOperatingResultsAbstractJp = {
	description: `業績情報に関する注記を公開するためのクラス`,
	properties: {
		order: {
	type: 'any-of',
	description: `順序`,
	contains: [{
	type: 'number',
}, {
	type: 'null',
}],
},
		Label: {
	type: 'any-of',
	description: `ラベル`,
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
		NoteToOperatingResults: {
	type: 'any-of',
	description: `業績情報に関する注記`,
	contains: [{
	type: 'stockNumeric',
}, {
	type: 'null',
}],
},
	},
} as const;

export const $NotesApplyingSpecificAccountingQuarterlyFinancialStatementsJp = {
	description: `四半期連結財務諸表に適用する特定会計基準に関する注記を公開するためのクラス`,
	properties: {
		order: {
	type: 'any-of',
	description: `順序`,
	contains: [{
	type: 'number',
}, {
	type: 'null',
}],
},
		Label: {
	type: 'any-of',
	description: `ラベル`,
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
		ApplyingOfSpecificAccountingOfTheConsolidatedQuarterlyFinancialStatements: {
	type: 'any-of',
	description: `四半期連結財務諸表に適用する特定会計基準の適用状況`,
	contains: [{
	type: 'stockNumeric',
}, {
	type: 'null',
}],
},
		NoteToApplyingOfSpecificAccountingOfTheConsolidatedQuarterlyFinancialStatements: {
	type: 'any-of',
	description: `四半期連結財務諸表に適用する特定会計基準に関する注記`,
	contains: [{
	type: 'stockNumeric',
}, {
	type: 'null',
}],
},
	},
} as const;

export const $NotesChangesAccountingPoliciesAccountingEstimatesRetrospectiveRestatementJp = {
	properties: {
		order: {
	type: 'any-of',
	description: `順序`,
	contains: [{
	type: 'number',
}, {
	type: 'null',
}],
},
		Label: {
	type: 'any-of',
	description: `ラベル`,
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
		ChangesBasedOnRevisionsOfAccountingStandard: {
	type: 'any-of',
	description: `会計基準の改正に基づく変更`,
	contains: [{
	type: 'stockNumeric',
}, {
	type: 'null',
}],
},
		ChangesInAccountingEstimates: {
	type: 'any-of',
	description: `会計上の見積りの変更`,
	contains: [{
	type: 'stockNumeric',
}, {
	type: 'null',
}],
},
		ChangesOtherThanOnesBasedOnRevisionsOfAccountingStandard: {
	type: 'any-of',
	description: `会計基準の改正以外の変更`,
	contains: [{
	type: 'stockNumeric',
}, {
	type: 'null',
}],
},
		RetrospectiveRestatement: {
	type: 'any-of',
	description: `遡及的な再表示`,
	contains: [{
	type: 'stockNumeric',
}, {
	type: 'null',
}],
},
		NoteToChangesInAccountingPoliciesAccountingEstimatesAndRetrospectiveRestatementQuarterly: {
	type: 'any-of',
	description: `四半期連結財務諸表における会計方針の変更、会計上の見積りの変更及び遡及的な再表示に関する注記`,
	contains: [{
	type: 'stockNumeric',
}, {
	type: 'null',
}],
},
	},
} as const;

export const $NotesNumberIssuedOutstandingSharesCommonStockJp = {
	description: `四半期連結財務諸表における発行済株式数（普通株式）に関する注記を公開するためのクラス`,
	properties: {
		order: {
	type: 'any-of',
	description: `順序`,
	contains: [{
	type: 'number',
}, {
	type: 'null',
}],
},
		Label: {
	type: 'any-of',
	description: `ラベル`,
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
		NoteToNumberOfIssuedAndOutstandingSharesCommonStock: {
	type: 'any-of',
	description: `四半期連結財務諸表における発行済株式数（普通株式）に関する注記`,
	contains: [{
	type: 'stock',
}, {
	type: 'null',
}],
},
		AverageNumberOfShares: {
	type: 'any-of',
	description: `平均発行株数`,
	contains: [{
	type: 'stockNumeric',
}, {
	type: 'null',
}],
},
		NumberOfIssuedAndOutstandingSharesAtTheEndOfFiscalYearIncludingTreasuryStock: {
	type: 'any-of',
	description: `期末発行済株式数（自己株式を含む）`,
	contains: [{
	type: 'stockNumeric',
}, {
	type: 'null',
}],
},
		NumberOfTreasuryStockAtTheEndOfFiscalYear: {
	type: 'any-of',
	description: `期末自己株式数`,
	contains: [{
	type: 'stockNumeric',
}, {
	type: 'null',
}],
},
	},
} as const;

export const $OperatingResultJp = {
	description: `業績情報を公開するためのクラス`,
	properties: {
		order: {
	type: 'any-of',
	description: `順序`,
	contains: [{
	type: 'number',
}, {
	type: 'null',
}],
},
		Label: {
	type: 'any-of',
	description: `ラベル`,
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
		OperatingResultsAbstract: {
	type: 'OperatingResultsAbstractJp',
	description: `業績情報`,
},
		NoteToOperatingResultsAbstract: {
	type: 'NoteToOperatingResultsAbstractJp',
	description: `業績情報に関する注記`,
},
	},
} as const;

export const $OperatingResultsAbstractJp = {
	description: `業績情報を公開するためのクラス`,
	properties: {
		order: {
	type: 'any-of',
	description: `順序`,
	contains: [{
	type: 'number',
}, {
	type: 'null',
}],
},
		Label: {
	type: 'any-of',
	description: `ラベル`,
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
		IncomeStatementsInformationAbstract: {
	type: 'IncomeStatementsInformationAbstractJp',
	description: `連結損益計算書情報`,
},
		NoteToIncomeStatementsInformationAbstract: {
	type: 'NoteToIncomeStatementsInformationAbstractJp',
	description: `連結損益計算書情報に関する注記`,
},
		OtherOperatingResultsAbstract: {
	type: 'OtherOperatingResultsAbstractJp',
	description: `その他の連結経営成績の概要`,
},
	},
} as const;

export const $OtherOperatingResultsAbstractJp = {
	description: `その他の連結経営成績の概要を公開するためのクラス`,
	properties: {
		order: {
	type: 'any-of',
	description: `順序`,
	contains: [{
	type: 'number',
}, {
	type: 'null',
}],
},
		Label: {
	type: 'any-of',
	description: `ラベル`,
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
		NetIncomePerShare: {
	type: 'any-of',
	description: `1株当たり当期純利益（基本）`,
	contains: [{
	type: 'stockNumeric',
}, {
	type: 'null',
}],
},
		DilutedNetIncomePerShare: {
	type: 'any-of',
	description: `1株当たり当期純利益`,
	contains: [{
	type: 'stockNumeric',
}, {
	type: 'null',
}],
},
		NetIncomeToShareholdersEquityRatio: {
	type: 'any-of',
	description: `自己資本当期純利益率`,
	contains: [{
	type: 'stockNumeric',
}, {
	type: 'null',
}],
},
		OrdinaryIncomeToTotalAssetsRatio: {
	type: 'any-of',
	description: `総資産経常利益率`,
	contains: [{
	type: 'stockNumeric',
}, {
	type: 'null',
}],
},
		OperatingIncomeToNetSalesRatio: {
	type: 'any-of',
	description: `売上高営業利益率`,
	contains: [{
	type: 'stockNumeric',
}, {
	type: 'null',
}],
},
		PeriodNetIncomePerShare: {
	type: 'any-of',
	description: `昨年度1株当たり当期純利益（基本）`,
	contains: [{
	type: 'stockNumeric',
}, {
	type: 'null',
}],
},
		PeriodDilutedNetIncomePerShare: {
	type: 'any-of',
	description: `昨年度1株当たり当期純利益`,
	contains: [{
	type: 'stockNumeric',
}, {
	type: 'null',
}],
},
		PeriodNetIncomeToShareholdersEquityRatio: {
	type: 'any-of',
	description: `昨年度自己資本当期純利益率`,
	contains: [{
	type: 'stockNumeric',
}, {
	type: 'null',
}],
},
		PeriodOrdinaryIncomeToTotalAssetsRatio: {
	type: 'any-of',
	description: `昨年度総資産経常利益率`,
	contains: [{
	type: 'stockNumeric',
}, {
	type: 'null',
}],
},
		PeriodOperatingIncomeToNetSalesRatio: {
	type: 'any-of',
	description: `昨年度売上高営業利益率`,
	contains: [{
	type: 'stockNumeric',
}, {
	type: 'null',
}],
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

export const $SignificantChangesInTheScopeOfConsolidationDuringThePeriodJp = {
	description: `期間中の連結の範囲における重要な変更を公開するためのクラス`,
	properties: {
		order: {
	type: 'any-of',
	description: `順序`,
	contains: [{
	type: 'number',
}, {
	type: 'null',
}],
},
		Label: {
	type: 'any-of',
	description: `ラベル`,
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
		NoteToSignificantChangesInTheScopeOfConsolidationDuringThePeriod: {
	type: 'any-of',
	description: `期間中の連結の範囲における重要な変更に関する注記`,
	contains: [{
	type: 'stockNumeric',
}, {
	type: 'null',
}],
},
		NameOfSubsidiariesExcludedFromConsolidation: {
	type: 'any-of',
	description: `連結から除外された子会社の名称`,
	contains: [{
	type: 'stockNumeric',
}, {
	type: 'null',
}],
},
		NameOfSubsidiariesNewlyConsolidated: {
	type: 'any-of',
	description: `新たに連結された子会社の名称`,
	contains: [{
	type: 'stockNumeric',
}, {
	type: 'null',
}],
},
		NumberOfSubsidiariesExcludedFromConsolidation: {
	type: 'any-of',
	description: `連結から除外された子会社の数`,
	contains: [{
	type: 'stockNumeric',
}, {
	type: 'null',
}],
},
		NumberOfSubsidiariesNewlyConsolidated: {
	type: 'any-of',
	description: `新たに連結された子会社の数`,
	contains: [{
	type: 'stockNumeric',
}, {
	type: 'null',
}],
},
	},
} as const;

export const $SpecialNotesJp = {
	description: `四半期決算概要に関する特記事項を公開するためのクラス`,
	properties: {
		order: {
	type: 'any-of',
	description: `順序`,
	contains: [{
	type: 'number',
}, {
	type: 'null',
}],
},
		Label: {
	type: 'any-of',
	description: `ラベル`,
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
		NotesForUsingForecastedInformationAndOthers: {
	type: 'any-of',
	description: `予想情報の利用等に関する注記`,
	contains: [{
	type: 'stock',
}, {
	type: 'null',
}],
},
		ReviewOfAttachedConsolidatedQuarterlyFinancialStatementsByACertifiedPublicAccountantOrAnAuditFirm: {
	type: 'any-of',
	description: `公認会計士若しくは監査法人による四半期連結財務諸表の監査の実施の有無`,
	contains: [{
	type: 'stockNumeric',
}, {
	type: 'null',
}],
},
	},
} as const;

export const $StockInfo = {
	description: `株式情報を公開するためのクラス`,
	properties: {
		order: {
	type: 'any-of',
	description: `順序`,
	contains: [{
	type: 'number',
}, {
	type: 'null',
}],
},
		Label: {
	type: 'any-of',
	description: `ラベル`,
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
		DocumentName: {
	type: 'any-of',
	description: `文書名`,
	contains: [{
	type: 'stock',
}, {
	type: 'null',
}],
},
		FilingDate: {
	type: 'any-of',
	description: `提出日`,
	contains: [{
	type: 'stock',
}, {
	type: 'null',
}],
},
		CompanyName: {
	type: 'any-of',
	description: `上場会社名`,
	contains: [{
	type: 'stock',
}, {
	type: 'null',
}],
},
		SecuritiesCode: {
	type: 'any-of',
	description: `証券コード`,
	contains: [{
	type: 'stock',
}, {
	type: 'null',
}],
},
		URL: {
	type: 'any-of',
	description: `URL`,
	contains: [{
	type: 'stock',
}, {
	type: 'null',
}],
},
		RepresentativeAbstract: {
	type: 'any-of',
	description: `代表者情報`,
	contains: [{
	type: 'representative_abstract',
}, {
	type: 'null',
}],
},
		InquiriesAbstract: {
	type: 'any-of',
	description: `問合せ先情報`,
	contains: [{
	type: 'inquiries_abstract',
}, {
	type: 'null',
}],
},
		Tel: {
	type: 'any-of',
	description: `電話番号`,
	contains: [{
	type: 'stock',
}, {
	type: 'null',
}],
},
		OtherCompanyInformationAbstract: {
	type: 'any-of',
	description: `その他の上場会社情報`,
	contains: [{
	type: 'other_company_information_abstract',
}, {
	type: 'null',
}],
},
		SupplementalMaterialOfAnnualResults: {
	type: 'any-of',
	description: `決算補足資料`,
	contains: [{
	type: 'stock',
}, {
	type: 'null',
}],
},
		WayOfGettingSupplementalMaterialOfAnnualResults: {
	type: 'any-of',
	description: `決算補足資料の入手方法`,
	contains: [{
	type: 'stock',
}, {
	type: 'null',
}],
},
		ConveningBriefingOfAnnualResults: {
	type: 'any-of',
	description: `決算説明会の開催の有無`,
	contains: [{
	type: 'stock',
}, {
	type: 'null',
}],
},
		TargetAudienceBriefingOfAnnualResults: {
	type: 'any-of',
	description: `決算説明会の対象者`,
	contains: [{
	type: 'stock',
}, {
	type: 'null',
}],
},
		NoteToFractionProcessingMethod: {
	type: 'any-of',
	description: `端数処理方法に関する注記`,
	contains: [{
	type: 'stock',
}, {
	type: 'null',
}],
},
		TokyoStockExchange: {
	type: 'any-of',
	description: `東京証券取引所の上場市場`,
	contains: [{
	type: 'stock',
}, {
	type: 'null',
}],
},
		BusinessCategory: {
	type: 'any-of',
	description: `事業会社種別`,
	contains: [{
	type: 'business_category',
}, {
	type: 'null',
}],
},
		FiscalYearEnd: {
	type: 'any-of',
	description: `決算期`,
	contains: [{
	type: 'stock',
}, {
	type: 'null',
}],
},
		QuarterlyPeriod: {
	type: 'any-of',
	description: `四半期`,
	contains: [{
	type: 'stock',
}, {
	type: 'null',
}],
},
	},
} as const;

export const $SummaryItemsAbstractJp = {
	description: `概要情報を公開するためのクラス`,
	properties: {
		type: {
	type: 'any-of',
	description: `タイプ`,
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
		XbrlId: {
	type: 'any-of',
	description: `XBRL識別子`,
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
		DocumentEntityInformation: {
	type: 'any-of',
	description: `上場会社情報`,
	contains: [{
	type: 'StockInfo',
}, {
	type: 'null',
}],
},
		OperatingResult: {
	type: 'any-of',
	description: `業績情報`,
	contains: [{
	type: 'OperatingResultJp',
}, {
	type: 'null',
}],
},
		NoteToFinancialResults: {
	type: 'any-of',
	description: `連結財務諸表に関する注記`,
	contains: [{
	type: 'NoteToFinancialResultsJp',
}, {
	type: 'null',
}],
},
		BusinessResultsFinancialPositions: {
	type: 'any-of',
	description: `業績及び財政状態に関する注記`,
	contains: [{
	type: 'BusinessResultsFinancialPositionsJp',
}, {
	type: 'null',
}],
},
		NotesApplyingSpecificAccountingQuarterlyFinancialStatements: {
	type: 'any-of',
	description: `四半期連結財務諸表に適用する特定会計基準に関する注記`,
	contains: [{
	type: 'NotesApplyingSpecificAccountingQuarterlyFinancialStatementsJp',
}, {
	type: 'null',
}],
},
		NotesChangesAccountingPoliciesAccountingEstimatesRetrospectiveRestatement: {
	type: 'any-of',
	description: `四半期連結財務諸表における会計方針の変更、会計上の見積りの変更及び遡及的な再表示に関する注記`,
	contains: [{
	type: 'NotesChangesAccountingPoliciesAccountingEstimatesRetrospectiveRestatementJp',
}, {
	type: 'null',
}],
},
		NotesNumberIssuedOutstandingSharesCommonStock: {
	type: 'any-of',
	description: `四半期連結財務諸表における発行済株式数（普通株式）に関する注記`,
	contains: [{
	type: 'NotesNumberIssuedOutstandingSharesCommonStockJp',
}, {
	type: 'null',
}],
},
		Dividends: {
	type: 'any-of',
	description: `配当に関する注記`,
	contains: [{
	type: 'DividendsJp',
}, {
	type: 'null',
}],
},
		Forecasts: {
	type: 'any-of',
	description: `四半期予想に関する注記`,
	contains: [{
	type: 'ForecastsJp',
}, {
	type: 'null',
}],
},
		SignificantChangesInTheScopeOfConsolidationDuringThePeriod: {
	type: 'any-of',
	description: `期間中の連結の範囲における重要な変更`,
	contains: [{
	type: 'SignificantChangesInTheScopeOfConsolidationDuringThePeriodJp',
}, {
	type: 'null',
}],
},
		SpecialNotes: {
	type: 'any-of',
	description: `四半期決算概要に関する特記事項`,
	contains: [{
	type: 'SpecialNotesJp',
}, {
	type: 'null',
}],
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

export const $abstract = {
	description: `概要を公開するためのクラス`,
	properties: {
		order: {
	type: 'any-of',
	description: `順序`,
	contains: [{
	type: 'number',
}, {
	type: 'null',
}],
},
		Label: {
	type: 'any-of',
	description: `ラベル`,
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
		Values: {
	type: 'any-of',
	description: `値`,
	contains: [{
	type: 'stockNumeric',
}, {
	type: 'null',
}],
},
		ChangeIn: {
	type: 'any-of',
	description: `増減`,
	contains: [{
	type: 'stockNumeric',
}, {
	type: 'null',
}],
},
	},
} as const;

export const $business_category = {
	description: `事業会社種別を公開するためのクラス`,
	properties: {
		order: {
	type: 'any-of',
	description: `順序`,
	contains: [{
	type: 'number',
}, {
	type: 'null',
}],
},
		Label: {
	type: 'any-of',
	description: `ラベル`,
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
		GeneralBusiness: {
	type: 'any-of',
	description: `一般事業会社の可否`,
	contains: [{
	type: 'stock',
}, {
	type: 'null',
}],
},
		SpecificBusiness: {
	type: 'any-of',
	description: `特定事業会社の可否`,
	contains: [{
	type: 'stock',
}, {
	type: 'null',
}],
},
	},
} as const;

export const $inquiries_abstract = {
	properties: {
		order: {
	type: 'any-of',
	description: `順序`,
	contains: [{
	type: 'number',
}, {
	type: 'null',
}],
},
		Label: {
	type: 'any-of',
	description: `ラベル`,
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
		NameInquiries: {
	type: 'any-of',
	description: `問合せ先責任者氏名`,
	contains: [{
	type: 'stock',
}, {
	type: 'null',
}],
},
		TitleInquiries: {
	type: 'any-of',
	description: `問合せ先責任者役職名`,
	contains: [{
	type: 'stock',
}, {
	type: 'null',
}],
},
	},
} as const;

export const $other_company_information_abstract = {
	properties: {
		order: {
	type: 'any-of',
	description: `順序`,
	contains: [{
	type: 'number',
}, {
	type: 'null',
}],
},
		Label: {
	type: 'any-of',
	description: `ラベル`,
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
		AnnualSecuritiesReportFilingDateAsPlanned: {
	type: 'any-of',
	description: `有価証券報告書提出予定日`,
	contains: [{
	type: 'stock',
}, {
	type: 'null',
}],
},
		DateOfGeneralShareholdersMeetingAsPlanned: {
	type: 'any-of',
	description: `定時株主総会の開催予定日`,
	contains: [{
	type: 'stock',
}, {
	type: 'null',
}],
},
		DividendPayableDateAsPlanned: {
	type: 'any-of',
	description: `配当支払予定日`,
	contains: [{
	type: 'stock',
}, {
	type: 'null',
}],
},
	},
} as const;

export const $representative_abstract = {
	properties: {
		order: {
	type: 'any-of',
	description: `順序`,
	contains: [{
	type: 'number',
}, {
	type: 'null',
}],
},
		Label: {
	type: 'any-of',
	description: `ラベル`,
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
		NameRepresentative: {
	type: 'any-of',
	description: `代表者氏名`,
	contains: [{
	type: 'stock',
}, {
	type: 'null',
}],
},
		TitleRepresentative: {
	type: 'any-of',
	description: `代表者役職名`,
	contains: [{
	type: 'stock',
}, {
	type: 'null',
}],
},
	},
} as const;

export const $stock = {
	properties: {
		is_valid: {
	type: 'any-of',
	description: `有効なデータかどうか`,
	contains: [{
	type: 'boolean',
}, {
	type: 'null',
}],
},
		label: {
	type: 'any-of',
	description: `ラベル`,
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
		value: {
	type: 'any-of',
	description: `値`,
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
	},
} as const;

export const $stockNumeric = {
	properties: {
		order: {
	type: 'any-of',
	description: `順序`,
	contains: [{
	type: 'number',
}, {
	type: 'null',
}],
},
		is_valid: {
	type: 'any-of',
	description: `有効なデータかどうか`,
	contains: [{
	type: 'boolean',
}, {
	type: 'null',
}],
},
		label: {
	type: 'any-of',
	description: `ラベル`,
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
		numeric: {
	type: 'any-of',
	description: `数値データ`,
	contains: [{
	type: 'number',
}, {
	type: 'null',
}],
},
		value: {
	type: 'any-of',
	description: `値`,
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
		scale: {
	type: 'any-of',
	description: `スケール`,
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
	},
} as const;