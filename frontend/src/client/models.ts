export type Body_login_login_access_token = {
	grant_type?: string | null;
	username: string;
	password: string;
	scope?: string;
	client_id?: string | null;
	client_secret?: string | null;
};



/**
 * 業績及び財政状態に関する注記を公開するためのクラス
 */
export type BusinessResultsFinancialPositionsJp = {
	/**
	 * 順序
	 */
	order?: number | null;
	/**
	 * ラベル
	 */
	Label?: string | null;
	/**
	 * 財政状態の概要
	 */
	FinancialPositions?: FinancialPositionsAbstractJp;
	/**
	 * 連結財務諸表に関する注記
	 */
	NoteToFinancialPositions?: NoteToFinancialPositionsAbstractJp;
};



/**
 * 1株当たり配当に関する情報を公開するためのクラス
 */
export type DividendPerShareJp = {
	/**
	 * 順序
	 */
	order?: number | null;
	/**
	 * ラベル
	 */
	Label?: string | null;
	/**
	 * 昨季Q1期末1株当たり配当実績
	 */
	FirstQuarterPriorYearResults?: stockNumeric | null;
	/**
	 * 昨季中間期末1株当たり配当実績
	 */
	SecondQuarterPriorYearResults?: stockNumeric | null;
	/**
	 * 昨季Q3期末1株当たり配当実績
	 */
	ThirdQuarterPriorYearResults?: stockNumeric | null;
	/**
	 * 昨季期末1株当たり配当実績
	 */
	YearEndPriorYearResults?: stockNumeric | null;
	/**
	 * 昨季年間1株当たり配当実績
	 */
	AnnualPriorYearResults?: stockNumeric | null;
	/**
	 * 今期Q1期末1株当たり配当実績
	 */
	FirstQuarterCurrentYearResults?: stockNumeric | null;
	/**
	 * 今期中間期末1株当たり配当実績
	 */
	SecondQuarterCurrentYearResults?: stockNumeric | null;
	/**
	 * 今期Q3期末1株当たり配当実績
	 */
	ThirdQuarterCurrentYearResults?: stockNumeric | null;
	/**
	 * 今期期末1株当たり配当実績
	 */
	YearEndCurrentYearResults?: stockNumeric | null;
	/**
	 * 今期年間1株当たり配当実績
	 */
	AnnualCurrentYearResults?: stockNumeric | null;
	/**
	 * 今期Q1期末1株当たり配当予想
	 */
	FirstQuarterCurrentYearForecasts?: stockNumeric | null;
	/**
	 * 今期中間期末1株当たり配当予想
	 */
	SecondQuarterCurrentYearForecasts?: stockNumeric | null;
	/**
	 * 今期Q3期末1株当たり配当予想
	 */
	ThirdQuarterCurrentYearForecasts?: stockNumeric | null;
	/**
	 * 今期期末1株当たり配当予想
	 */
	YearEndCurrentYearForecasts?: stockNumeric | null;
	/**
	 * 今期年間1株当たり配当予想
	 */
	AnnualCurrentYearForecasts?: stockNumeric | null;
	/**
	 * 来期Q1期末1株当たり配当予想
	 */
	FirstQuarterNextYearForecasts?: stockNumeric | null;
	/**
	 * 来期中間期末1株当たり配当予想
	 */
	SecondQuarterNextYearForecasts?: stockNumeric | null;
	/**
	 * 来期Q3期末1株当たり配当予想
	 */
	ThirdQuarterNextYearForecasts?: stockNumeric | null;
	/**
	 * 来期期末1株当たり配当予想
	 */
	YearEndNextYearForecasts?: stockNumeric | null;
	/**
	 * 来期年間1株当たり配当予想
	 */
	AnnualNextYearForecasts?: stockNumeric | null;
};



/**
 * 四半期配当に関する注記を公開するためのクラス
 */
export type DividendsJp = {
	/**
	 * 順序
	 */
	order?: number | null;
	/**
	 * ラベル
	 */
	Label?: string | null;
	/**
	 * 1株当たり配当
	 */
	DividendPerShare?: DividendPerShareJp | null;
	/**
	 * 当四半期における配当予想の修正
	 */
	CorrectionOfDividendForecast?: stockNumeric | null;
	/**
	 * 期末1株当たり配当の内訳
	 */
	DetailOfDividendPerShareFiscalYearEndAbstract?: stockNumeric | null;
	/**
	 * 配当に関する注記
	 */
	NoteToDividends?: stockNumeric | null;
	/**
	 * 配当性向
	 */
	DividendPayoutRatioPriorYear?: stockNumeric | null;
	/**
	 * 配当性向
	 */
	DividendPayoutRatioCurrentYear?: stockNumeric | null;
	/**
	 * 配当性向
	 */
	DividendPayoutRatioNextYear?: stockNumeric | null;
	/**
	 * 配当総額純資産比率
	 */
	RatioOfTotalAmountOfDividendsToNetAssets?: stockNumeric | null;
};



/**
 * 財政状態の概要を公開するためのクラス
 */
export type FinancialPositionsAbstractJp = {
	/**
	 * 順序
	 */
	order?: number | null;
	/**
	 * ラベル
	 */
	Label?: string | null;
	/**
	 * 総資産
	 */
	CapitalAdequacyRatio?: stockNumeric | null;
	/**
	 * 純資産
	 */
	NetAssets?: stockNumeric | null;
	/**
	 * 自己資本
	 */
	TotalAssets?: stockNumeric | null;
	/**
	 * 昨年度総資産
	 */
	PeriodCapitalAdequacyRatio?: stockNumeric | null;
	/**
	 * 昨年度純資産
	 */
	PeriodNetAssets?: stockNumeric | null;
	/**
	 * 昨年度自己資本
	 */
	PeriodTotalAssets?: stockNumeric | null;
};



/**
 * 決算期情報を公開するためのクラス
 */
export type FiscalYearStockInfo = {
	/**
	 * 順序
	 */
	order?: number | null;
	/**
	 * ラベル
	 */
	Label?: string | null;
	/**
	 * 文書名
	 */
	DocumentName?: stock | null;
	/**
	 * 提出日
	 */
	FilingDate?: stock | null;
	/**
	 * 上場会社名
	 */
	CompanyName?: stock | null;
	/**
	 * 証券コード
	 */
	SecuritiesCode?: stock | null;
	/**
	 * URL
	 */
	URL?: stock | null;
	/**
	 * 代表者情報
	 */
	RepresentativeAbstract?: representative_abstract | null;
	/**
	 * 問合せ先情報
	 */
	InquiriesAbstract?: inquiries_abstract | null;
	/**
	 * 電話番号
	 */
	Tel?: stock | null;
	/**
	 * その他の上場会社情報
	 */
	OtherCompanyInformationAbstract?: other_company_information_abstract | null;
	/**
	 * 決算補足資料
	 */
	SupplementalMaterialOfAnnualResults?: stock | null;
	/**
	 * 決算補足資料の入手方法
	 */
	WayOfGettingSupplementalMaterialOfAnnualResults?: stock | null;
	/**
	 * 決算説明会の開催の有無
	 */
	ConveningBriefingOfAnnualResults?: stock | null;
	/**
	 * 決算説明会の対象者
	 */
	TargetAudienceBriefingOfAnnualResults?: stock | null;
	/**
	 * 端数処理方法に関する注記
	 */
	NoteToFractionProcessingMethod?: stock | null;
	/**
	 * 東京証券取引所の上場市場
	 */
	TokyoStockExchange?: stock | null;
	/**
	 * 事業会社種別
	 */
	BusinessCategory?: business_category | null;
	/**
	 * 決算期
	 */
	FiscalYearEnd?: stock | null;
	/**
	 * 四半期
	 */
	QuarterlyPeriod?: stock | null;
	/**
	 * 有価証券報告書提出予定日
	 */
	AnnualSecuritiesReportFilingDateAsPlanned?: stock | null;
	/**
	 * 定時株主総会の開催予定日
	 */
	DateOfGeneralShareholdersMeetingAsPlanned?: stock | null;
	/**
	 * 配当支払予定日
	 */
	DividendPayableDateAsPlanned?: stock | null;
};



/**
 * 四半期予想に関する注記を公開するためのクラス
 */
export type ForecastsJp = {
	/**
	 * 順序
	 */
	order?: number | null;
	/**
	 * ラベル
	 */
	Label?: string | null;
	/**
	 * 予想のタイトル
	 */
	TitleForForecasts?: stockNumeric | null;
	/**
	 * 当四半期における連結業績予想の修正
	 */
	CorrectionOfFinancialForecastInThisQuarter?: stockNumeric | null;
	/**
	 * 売上高
	 */
	NetSales?: abstract | null;
	/**
	 * 営業利益
	 */
	OperatingIncome?: abstract | null;
	/**
	 * 経常利益
	 */
	OrdinaryIncome?: abstract | null;
	/**
	 * 親会社株主に帰属する当期純利益
	 */
	ProfitAttributableToOwnersOfParent?: abstract | null;
	/**
	 * 1株当たり当期純利益
	 */
	NetIncomePerShare?: stockNumeric | null;
	/**
	 * 予想に関する注記
	 */
	NoteToForecasts?: stockNumeric | null;
	/**
	 * 予想の前文
	 */
	PreambleToForecasts?: stockNumeric | null;
};



export type HTTPValidationError = {
	detail?: Array<ValidationError>;
};



/**
 * iXBRLのソースID情報を表すクラス
 */
export type HeadItem = {
	xbrl_id: string;
	company_name: string;
	securities_code: string;
	document_name: string;
	reporting_date: string;
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
	fiscal_year_end: string | null;
	tel: string | null;
};



/**
 * iXBRLのソースID情報のリストを表すクラス
 */
export type HeadItems = {
	data: Array<HeadItem>;
	count: number;
};



/**
 * 損益計算書情報を公開するためのクラス
 */
export type IncomeStatementsInformationAbstractJp = {
	/**
	 * 順序
	 */
	order?: number | null;
	/**
	 * ラベル
	 */
	Label?: string | null;
	/**
	 * 売上高
	 */
	NetSales?: abstract;
	/**
	 * 昨年度売上高
	 */
	PeriodNetSales?: abstract;
	/**
	 * 営業利益
	 */
	OperatingIncome?: abstract;
	/**
	 * 昨年度営業利益
	 */
	PeriodOperatingIncome?: abstract;
	/**
	 * 経常利益
	 */
	OrdinaryIncome?: abstract;
	/**
	 * 昨年度経常利益
	 */
	PeriodOrdinaryIncome?: abstract;
	/**
	 * 親会社株主に帰属する当期純利益
	 */
	Profit?: abstract;
	/**
	 * 昨年度親会社株主に帰属する当期純利益
	 */
	PeriodProfit?: abstract;
};



/**
 * アイテムの作成時にAPI経由で受け取るプロパティです。
 * 
 * Properties:
 * title (str): アイテムのタイトルです。
 * 
 * examples:
 * ItemCreate(title="title")
 */
export type ItemCreate = {
	title: string;
	description?: string | null;
};



/**
 * アイテムの公開情報を表すクラスです。
 * 
 * Properties:
 * id (int): アイテムのIDです。
 * owner_id (int): アイテムの所有者のIDです。
 * 
 * examples:
 * ItemPublic(id=1, title="title", owner_id=1)
 */
export type ItemPublic = {
	title: string;
	description?: string | null;
	id: number;
	owner_id: number;
};



/**
 * アイテムの更新時にAPI経由で受け取るプロパティです。
 * 
 * Properties:
 * title (str | None): アイテムのタイトルです。デフォルト値はNoneです。
 * 
 * examples:
 * ItemUpdate(title="title")
 */
export type ItemUpdate = {
	title?: string | null;
	description?: string | null;
};



/**
 * アイテムのリストを表すクラスです。
 * 
 * Properties:
 * data (list[ItemPublic]): アイテムのリストです。
 * count (int): アイテムの数です。
 * 
 * Examples:
 * ItemsPublic(data=[ItemPublic(id=1, title="title", owner_id=1)], count=1)
 */
export type ItemsPublic = {
	data: Array<ItemPublic>;
	count: number;
};



/**
 * iXBRLの計算アーク情報を表すクラス
 */
export type IxCalculationArcCreate_Input = {
	xbrl_id: string;
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
	xbrl_id: string;
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
	xbrl_id: string;
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
	xbrl_id: string;
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
	xbrl_id: string;
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
	xbrl_id: string;
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
	path?: string;
	xbrl_id: string | null;
};



/**
 * iXBRLのファイルパス情報を公開するためのクラス
 */
export type IxFilePathPublic = {
	path: string;
	xbrl_id: string;
};



/**
 * iXBRLのヘッダー情報を表すクラス
 */
export type IxHeadTitleCreate = {
	company_name: string | null;
	securities_code: string | null;
	document_name: string | null;
	reporting_date: string;
	current_period: string | null;
	xbrl_id: string | null;
	report_type: string | null;
	listed_market?: string | null;
	market_section?: string | null;
	url?: string | null;
	is_bs?: boolean;
	is_pl?: boolean;
	is_cf?: boolean;
	is_ci?: boolean;
	is_sce?: boolean;
	is_sfp?: boolean;
	fiscal_year_end?: string | null;
	tel?: string | null;
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
	xbrl_id: string;
	company_name: string;
	securities_code: string;
	document_name: string;
	reporting_date: string;
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
	fiscal_year_end: string | null;
	tel: string | null;
};



/**
 * iXBRLのラベルアーク情報を作成するためのクラス
 */
export type IxLabelArcCreate = {
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
	xbrl_id: string;
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
	xbrl_id: string;
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
 * iXBRLの非数値情報を表すクラス
 */
export type IxNonNumericCreate = {
	xbrl_id: string;
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
	xbrl_id: string;
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
	xbrl_id: string;
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
	xbrl_id: string;
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
	xbrl_id?: string | null;
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
	xbrl_id: string | null;
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
 * iXBRLのスキーマリンクベース情報を作成するためのクラス
 */
export type IxSchemaLinkBaseCreate = {
	xbrl_id: string;
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
	id: string;
	name: string;
	type: string;
	xbrl_id: string | null;
	url: string | null;
};



/**
 * iXBRLのソースファイル情報を作成するためのクラス
 */
export type IxSourceFileCreateList = {
	data: Array<IxSourceFileCreate>;
};



export type MenuTitle = {
	/**
	 * タイトルラベル
	 */
	label?: string | null;
	/**
	 * 日本語ラベル
	 */
	jp?: string | null;
};



export type MenuTitles = {
	count: number;
	data: Array<MenuTitle>;
};



/**
 * メッセージを表すクラスです。
 * 
 * Properties:
 * message (str): メッセージです。
 * 
 * Examples:
 * Message(message="message")
 */
export type Message = {
	message: string;
};



/**
 * 新しいパスワードを表すクラスです。
 * 
 * Properties:
 * token (str): トークンです。
 * new_password (str): 新しいパスワードです。
 * 
 * Examples:
 * NewPassword(token="string", new_password="string")
 */
export type NewPassword = {
	token: string;
	new_password: string;
};



/**
 * 連結財務諸表に関する注記を公開するためのクラス
 */
export type NoteToFinancialPositionsAbstractJp = {
	/**
	 * 順序
	 */
	order?: number | null;
	/**
	 * ラベル
	 */
	Label?: string | null;
	/**
	 * 連結財務諸表に関する注記
	 */
	NoteToFinancialPositions?: stockNumeric | null;
	/**
	 * 自己資本
	 */
	OwnersEquity?: stockNumeric | null;
};



/**
 * 連結財務諸表に関する注記を公開するためのクラス
 */
export type NoteToFinancialResultsJp = {
	/**
	 * 順序
	 */
	order?: number | null;
	/**
	 * ラベル
	 */
	Label?: string | null;
	/**
	 * 連結財務諸表に関する注記
	 */
	NoteToFinancialResults?: stockNumeric | null;
};



/**
 * 損益計算書情報に関する注記を公開するためのクラス
 */
export type NoteToIncomeStatementsInformationAbstractJp = {
	/**
	 * 順序
	 */
	order?: number | null;
	/**
	 * ラベル
	 */
	Label?: string | null;
	/**
	 * 包括利益
	 */
	ComprehensiveIncomeAbstract?: abstract;
	/**
	 * 昨年度包括利益
	 */
	PeriodComprehensiveIncomeAbstract?: abstract;
};



/**
 * 業績情報に関する注記を公開するためのクラス
 */
export type NoteToOperatingResultsAbstractJp = {
	/**
	 * 順序
	 */
	order?: number | null;
	/**
	 * ラベル
	 */
	Label?: string | null;
	/**
	 * 業績情報に関する注記
	 */
	NoteToOperatingResults?: stockNumeric | null;
};



/**
 * 四半期連結財務諸表に適用する特定会計基準に関する注記を公開するためのクラス
 */
export type NotesApplyingSpecificAccountingQuarterlyFinancialStatementsJp = {
	/**
	 * 順序
	 */
	order?: number | null;
	/**
	 * ラベル
	 */
	Label?: string | null;
	/**
	 * 四半期連結財務諸表に適用する特定会計基準の適用状況
	 */
	ApplyingOfSpecificAccountingOfTheConsolidatedQuarterlyFinancialStatements?: stockNumeric | null;
	/**
	 * 四半期連結財務諸表に適用する特定会計基準に関する注記
	 */
	NoteToApplyingOfSpecificAccountingOfTheConsolidatedQuarterlyFinancialStatements?: stockNumeric | null;
};



export type NotesChangesAccountingPoliciesAccountingEstimatesRetrospectiveRestatementJp = {
	/**
	 * 順序
	 */
	order?: number | null;
	/**
	 * ラベル
	 */
	Label?: string | null;
	/**
	 * 会計基準の改正に基づく変更
	 */
	ChangesBasedOnRevisionsOfAccountingStandard?: stockNumeric | null;
	/**
	 * 会計上の見積りの変更
	 */
	ChangesInAccountingEstimates?: stockNumeric | null;
	/**
	 * 会計基準の改正以外の変更
	 */
	ChangesOtherThanOnesBasedOnRevisionsOfAccountingStandard?: stockNumeric | null;
	/**
	 * 遡及的な再表示
	 */
	RetrospectiveRestatement?: stockNumeric | null;
	/**
	 * 四半期連結財務諸表における会計方針の変更、会計上の見積りの変更及び遡及的な再表示に関する注記
	 */
	NoteToChangesInAccountingPoliciesAccountingEstimatesAndRetrospectiveRestatementQuarterly?: stockNumeric | null;
};



/**
 * 四半期連結財務諸表における発行済株式数（普通株式）に関する注記を公開するためのクラス
 */
export type NotesNumberIssuedOutstandingSharesCommonStockJp = {
	/**
	 * 順序
	 */
	order?: number | null;
	/**
	 * ラベル
	 */
	Label?: string | null;
	/**
	 * 四半期連結財務諸表における発行済株式数（普通株式）に関する注記
	 */
	NoteToNumberOfIssuedAndOutstandingSharesCommonStock?: stock | null;
	/**
	 * 平均発行株数
	 */
	AverageNumberOfShares?: stockNumeric | null;
	/**
	 * 期末発行済株式数（自己株式を含む）
	 */
	NumberOfIssuedAndOutstandingSharesAtTheEndOfFiscalYearIncludingTreasuryStock?: stockNumeric | null;
	/**
	 * 期末自己株式数
	 */
	NumberOfTreasuryStockAtTheEndOfFiscalYear?: stockNumeric | null;
};



/**
 * 業績情報を公開するためのクラス
 */
export type OperatingResultJp = {
	/**
	 * 順序
	 */
	order?: number | null;
	/**
	 * ラベル
	 */
	Label?: string | null;
	/**
	 * 業績情報
	 */
	OperatingResultsAbstract?: OperatingResultsAbstractJp;
	/**
	 * 業績情報に関する注記
	 */
	NoteToOperatingResultsAbstract?: NoteToOperatingResultsAbstractJp;
};



/**
 * 業績情報を公開するためのクラス
 */
export type OperatingResultsAbstractJp = {
	/**
	 * 順序
	 */
	order?: number | null;
	/**
	 * ラベル
	 */
	Label?: string | null;
	/**
	 * 連結損益計算書情報
	 */
	IncomeStatementsInformationAbstract?: IncomeStatementsInformationAbstractJp;
	/**
	 * 連結損益計算書情報に関する注記
	 */
	NoteToIncomeStatementsInformationAbstract?: NoteToIncomeStatementsInformationAbstractJp;
	/**
	 * その他の連結経営成績の概要
	 */
	OtherOperatingResultsAbstract?: OtherOperatingResultsAbstractJp;
};



/**
 * その他の連結経営成績の概要を公開するためのクラス
 */
export type OtherOperatingResultsAbstractJp = {
	/**
	 * 順序
	 */
	order?: number | null;
	/**
	 * ラベル
	 */
	Label?: string | null;
	/**
	 * 1株当たり当期純利益（基本）
	 */
	NetIncomePerShare?: stockNumeric | null;
	/**
	 * 1株当たり当期純利益
	 */
	DilutedNetIncomePerShare?: stockNumeric | null;
	/**
	 * 自己資本当期純利益率
	 */
	NetIncomeToShareholdersEquityRatio?: stockNumeric | null;
	/**
	 * 総資産経常利益率
	 */
	OrdinaryIncomeToTotalAssetsRatio?: stockNumeric | null;
	/**
	 * 売上高営業利益率
	 */
	OperatingIncomeToNetSalesRatio?: stockNumeric | null;
	/**
	 * 昨年度1株当たり当期純利益（基本）
	 */
	PeriodNetIncomePerShare?: stockNumeric | null;
	/**
	 * 昨年度1株当たり当期純利益
	 */
	PeriodDilutedNetIncomePerShare?: stockNumeric | null;
	/**
	 * 昨年度自己資本当期純利益率
	 */
	PeriodNetIncomeToShareholdersEquityRatio?: stockNumeric | null;
	/**
	 * 昨年度総資産経常利益率
	 */
	PeriodOrdinaryIncomeToTotalAssetsRatio?: stockNumeric | null;
	/**
	 * 昨年度売上高営業利益率
	 */
	PeriodOperatingIncomeToNetSalesRatio?: stockNumeric | null;
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
 * 期間中の連結の範囲における重要な変更を公開するためのクラス
 */
export type SignificantChangesInTheScopeOfConsolidationDuringThePeriodJp = {
	/**
	 * 順序
	 */
	order?: number | null;
	/**
	 * ラベル
	 */
	Label?: string | null;
	/**
	 * 期間中の連結の範囲における重要な変更に関する注記
	 */
	NoteToSignificantChangesInTheScopeOfConsolidationDuringThePeriod?: stockNumeric | null;
	/**
	 * 連結から除外された子会社の名称
	 */
	NameOfSubsidiariesExcludedFromConsolidation?: stockNumeric | null;
	/**
	 * 新たに連結された子会社の名称
	 */
	NameOfSubsidiariesNewlyConsolidated?: stockNumeric | null;
	/**
	 * 連結から除外された子会社の数
	 */
	NumberOfSubsidiariesExcludedFromConsolidation?: stockNumeric | null;
	/**
	 * 新たに連結された子会社の数
	 */
	NumberOfSubsidiariesNewlyConsolidated?: stockNumeric | null;
};



/**
 * 四半期決算概要に関する特記事項を公開するためのクラス
 */
export type SpecialNotesJp = {
	/**
	 * 順序
	 */
	order?: number | null;
	/**
	 * ラベル
	 */
	Label?: string | null;
	/**
	 * 予想情報の利用等に関する注記
	 */
	NotesForUsingForecastedInformationAndOthers?: stock | null;
	/**
	 * 公認会計士若しくは監査法人による四半期連結財務諸表の監査の実施の有無
	 */
	ReviewOfAttachedConsolidatedQuarterlyFinancialStatementsByACertifiedPublicAccountantOrAnAuditFirm?: stockNumeric | null;
};



/**
 * 株式情報を公開するためのクラス
 */
export type StockInfo = {
	/**
	 * 順序
	 */
	order?: number | null;
	/**
	 * ラベル
	 */
	Label?: string | null;
	/**
	 * 文書名
	 */
	DocumentName?: stock | null;
	/**
	 * 提出日
	 */
	FilingDate?: stock | null;
	/**
	 * 上場会社名
	 */
	CompanyName?: stock | null;
	/**
	 * 証券コード
	 */
	SecuritiesCode?: stock | null;
	/**
	 * URL
	 */
	URL?: stock | null;
	/**
	 * 代表者情報
	 */
	RepresentativeAbstract?: representative_abstract | null;
	/**
	 * 問合せ先情報
	 */
	InquiriesAbstract?: inquiries_abstract | null;
	/**
	 * 電話番号
	 */
	Tel?: stock | null;
	/**
	 * その他の上場会社情報
	 */
	OtherCompanyInformationAbstract?: other_company_information_abstract | null;
	/**
	 * 決算補足資料
	 */
	SupplementalMaterialOfAnnualResults?: stock | null;
	/**
	 * 決算補足資料の入手方法
	 */
	WayOfGettingSupplementalMaterialOfAnnualResults?: stock | null;
	/**
	 * 決算説明会の開催の有無
	 */
	ConveningBriefingOfAnnualResults?: stock | null;
	/**
	 * 決算説明会の対象者
	 */
	TargetAudienceBriefingOfAnnualResults?: stock | null;
	/**
	 * 端数処理方法に関する注記
	 */
	NoteToFractionProcessingMethod?: stock | null;
	/**
	 * 東京証券取引所の上場市場
	 */
	TokyoStockExchange?: stock | null;
	/**
	 * 事業会社種別
	 */
	BusinessCategory?: business_category | null;
	/**
	 * 決算期
	 */
	FiscalYearEnd?: stock | null;
	/**
	 * 四半期
	 */
	QuarterlyPeriod?: stock | null;
};



/**
 * iXBRLのヘッダー情報を表すクラス
 */
export type StockRecordInfo = {
	/**
	 * iXBRLのソースID
	 */
	xbrl_id?: string;
	/**
	 * 上場会社名
	 */
	company_name?: string;
	/**
	 * 証券コード
	 */
	securities_code?: string;
	/**
	 * 四半期
	 */
	current_period?: string | null;
	/**
	 * 報告書種別
	 */
	report_type?: string;
	/**
	 * 提出日
	 */
	reporting_date?: string;
	/**
	 * 文書名
	 */
	document_name?: string;
	/**
	 * 決算期
	 */
	fiscal_year_end?: string;
	/**
	 * URL
	 */
	url?: string | null;
};



/**
 * iXBRLのヘッダー情報のリストを表すクラス
 */
export type StockRecordInfos = {
	count: number;
	data: Array<StockRecordInfo>;
	/**
	 * 次のページのオフセット
	 */
	nextOffset?: number | null;
};



/**
 * 概要情報を公開するためのクラス
 */
export type SummaryItemsAbstractJp = {
	/**
	 * タイプ
	 */
	type?: string | null;
	/**
	 * XBRL識別子
	 */
	XbrlId?: string | null;
	/**
	 * 上場会社情報
	 */
	DocumentEntityInformation?: StockInfo | null;
	/**
	 * 業績情報
	 */
	OperatingResult?: OperatingResultJp | null;
	/**
	 * 連結財務諸表に関する注記
	 */
	NoteToFinancialResults?: NoteToFinancialResultsJp | null;
	/**
	 * 業績及び財政状態に関する注記
	 */
	BusinessResultsFinancialPositions?: BusinessResultsFinancialPositionsJp | null;
	/**
	 * 四半期連結財務諸表に適用する特定会計基準に関する注記
	 */
	NotesApplyingSpecificAccountingQuarterlyFinancialStatements?: NotesApplyingSpecificAccountingQuarterlyFinancialStatementsJp | null;
	/**
	 * 四半期連結財務諸表における会計方針の変更、会計上の見積りの変更及び遡及的な再表示に関する注記
	 */
	NotesChangesAccountingPoliciesAccountingEstimatesRetrospectiveRestatement?: NotesChangesAccountingPoliciesAccountingEstimatesRetrospectiveRestatementJp | null;
	/**
	 * 四半期連結財務諸表における発行済株式数（普通株式）に関する注記
	 */
	NotesNumberIssuedOutstandingSharesCommonStock?: NotesNumberIssuedOutstandingSharesCommonStockJp | null;
	/**
	 * 配当に関する注記
	 */
	Dividends?: DividendsJp | null;
	/**
	 * 四半期予想に関する注記
	 */
	Forecasts?: ForecastsJp | null;
	/**
	 * 期間中の連結の範囲における重要な変更
	 */
	SignificantChangesInTheScopeOfConsolidationDuringThePeriod?: SignificantChangesInTheScopeOfConsolidationDuringThePeriodJp | null;
	/**
	 * 四半期決算概要に関する特記事項
	 */
	SpecialNotes?: SpecialNotesJp | null;
};



export type SummaryItemsAbstractJpList = {
	/**
	 * 概要情報のリスト数
	 */
	count?: number;
	/**
	 * 概要情報
	 */
	data?: Array<SummaryItemsAbstractJp>;
};



/**
 * アクセストークンを表すクラスです。
 * 
 * Properties:
 * access_token (str): アクセストークンです。
 * token_type (str): トークンのタイプです。デフォルト値は"bearer"です。
 * 
 * Examples:
 * Token(access_token="string")
 */
export type Token = {
	access_token: string;
	token_type?: string;
};



/**
 * パスワードの更新時にAPI経由で受け取るプロパティです。
 * 
 * Properties:
 * current_password (str): 現在のパスワードです。
 * new_password (str): 新しいパスワードです。
 * 
 * Examples:
 * UpdatePassword(current_password="password", new_password="new_password")
 */
export type UpdatePassword = {
	current_password: string;
	new_password: string;
};



/**
 * ユーザーの作成時にAPI経由で受け取るプロパティです。
 * 
 * Properties:
 * email (EmailStr): ユーザーのメールアドレスです。
 * password (str): ユーザーのパスワードです。
 * full_name (str | None): ユーザーのフルネームです。デフォルト値はNoneです。
 * 
 * Examples:
 * UserCreate(email="example@example.com", password="password", full_name="yamada taro")
 */
export type UserCreate = {
	email: string;
	is_active?: boolean;
	is_superuser?: boolean;
	full_name?: string | null;
	password: string;
};



/**
 * ユーザーの公開情報を表すクラスです。
 * 
 * Properties:
 * id (int): ユーザーのIDです。
 * 
 * Examples:
 * UserPublic(id=1, email="example@example.com", is_active=True, is_superuser=False, full_name="yamada taro")
 */
export type UserPublic = {
	email: string;
	is_active?: boolean;
	is_superuser?: boolean;
	full_name?: string | null;
	id: number;
};



/**
 * ユーザーの登録時にAPI経由で受け取るプロパティです。
 * 
 * Properties:
 * email (EmailStr): ユーザーのメールアドレスです。
 * password (str): ユーザーのパスワードです。
 * full_name (str | None): ユーザーのフルネームです。デフォルト値はNoneです。
 * 
 * Examples:
 * UserRegister(email="example@example.com", password="password", full_name="yamada taro")
 */
export type UserRegister = {
	email: string;
	password: string;
	full_name?: string | null;
};



/**
 * ユーザーの更新時にAPI経由で受け取るプロパティです。
 * 
 * Properties:
 * email (EmailStr | None): ユーザーのメールアドレスです。デフォルト値はNoneです。
 * full_name (str | None): ユーザーのフルネームです。デフォルト値はNoneです。
 * 
 * Examples:
 * UserUpdate(email="example@example.com", full_name="yamada taro")
 */
export type UserUpdate = {
	email?: string | null;
	is_active?: boolean;
	is_superuser?: boolean;
	full_name?: string | null;
	password?: string | null;
};



/**
 * ユーザーの更新時にAPI経由で受け取るプロパティです。
 * 
 * Properties:
 * full_name (str | None): ユーザーのフルネームです。デフォルト値はNoneです。
 * email (EmailStr | None): ユーザーのメールアドレスです。デフォルト値はNoneです。
 * 
 * examples:
 * UserUpdateMe(full_name="yamada taro", email="example@example.com")
 */
export type UserUpdateMe = {
	full_name?: string | null;
	email?: string | null;
};



/**
 * ユーザーのリストを表すクラスです。
 * 
 * Properties:
 * data (list[UserPublic]): ユーザーのリストです。
 * count (int): ユーザーの数です。
 * 
 * Examples:
 * UsersPublic(data=[UserPublic(id=1, email="example@example.com", is_active=True, is_superuser=False, full_name="yamada taro")], count=1)
 */
export type UsersPublic = {
	data: Array<UserPublic>;
	count: number;
};



export type ValidationError = {
	loc: Array<string | number>;
	msg: string;
	type: string;
};



/**
 * 概要を公開するためのクラス
 */
export type abstract = {
	/**
	 * 順序
	 */
	order?: number | null;
	/**
	 * ラベル
	 */
	Label?: string | null;
	/**
	 * 値
	 */
	Values?: stockNumeric | null;
	/**
	 * 増減
	 */
	ChangeIn?: stockNumeric | null;
};



/**
 * 事業会社種別を公開するためのクラス
 */
export type business_category = {
	/**
	 * 順序
	 */
	order?: number | null;
	/**
	 * ラベル
	 */
	Label?: string | null;
	/**
	 * 一般事業会社の可否
	 */
	GeneralBusiness?: stock | null;
	/**
	 * 特定事業会社の可否
	 */
	SpecificBusiness?: stock | null;
};



export type inquiries_abstract = {
	/**
	 * 順序
	 */
	order?: number | null;
	/**
	 * ラベル
	 */
	Label?: string | null;
	/**
	 * 問合せ先責任者氏名
	 */
	NameInquiries?: stock | null;
	/**
	 * 問合せ先責任者役職名
	 */
	TitleInquiries?: stock | null;
};



export type other_company_information_abstract = {
	/**
	 * 順序
	 */
	order?: number | null;
	/**
	 * ラベル
	 */
	Label?: string | null;
	/**
	 * 有価証券報告書提出予定日
	 */
	AnnualSecuritiesReportFilingDateAsPlanned?: stock | null;
	/**
	 * 定時株主総会の開催予定日
	 */
	DateOfGeneralShareholdersMeetingAsPlanned?: stock | null;
	/**
	 * 配当支払予定日
	 */
	DividendPayableDateAsPlanned?: stock | null;
};



export type representative_abstract = {
	/**
	 * 順序
	 */
	order?: number | null;
	/**
	 * ラベル
	 */
	Label?: string | null;
	/**
	 * 代表者氏名
	 */
	NameRepresentative?: stock | null;
	/**
	 * 代表者役職名
	 */
	TitleRepresentative?: stock | null;
};



export type stock = {
	/**
	 * 有効なデータかどうか
	 */
	is_valid?: boolean | null;
	/**
	 * ラベル
	 */
	label?: string | null;
	/**
	 * 値
	 */
	value?: string | null;
	/**
	 * 順序
	 */
	order?: number | null;
};



export type stockNumeric = {
	/**
	 * 順序
	 */
	order?: number | null;
	/**
	 * 有効なデータかどうか
	 */
	is_valid?: boolean | null;
	/**
	 * ラベル
	 */
	label?: string | null;
	/**
	 * 数値データ
	 */
	numeric?: number | null;
	/**
	 * 値
	 */
	value?: string | null;
	/**
	 * スケール
	 */
	scale?: string | null;
};

