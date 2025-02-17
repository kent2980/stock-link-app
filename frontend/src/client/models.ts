export type Body_login_login_access_token = {
	grant_type?: string | null;
	username: string;
	password: string;
	scope?: string;
	client_id?: string | null;
	client_secret?: string | null;
};



export type CompanySchema = {
	code: string;
	name: string;
	accountingStandard: string;
	fiscalYear: string;
	fiscalQuarter: string;
};



export type FinancialResponseSchema = {
	company: CompanySchema;
	metrics: Array<MetricParentSchema>;
};



export type HTTPValidationError = {
	detail?: Array<ValidationError>;
};



export type IndustriesList = {
	data: Array<Industry>;
};



export type Industry = {
	code: number;
	name: string;
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



export type IxDocumentInfo = {
	item_key: string;
	document_name: string;
	reporting_date: string;
	current_period: string | null;
	report_type: string;
};



export type IxDocumentInfoList = {
	data: Array<IxDocumentInfo>;
	count: number;
};



export type JpxStockInfoPublic = {
	input_date: string;
	code: string;
	name: string;
	market_or_type: string;
	industry_33_code: number | null;
	industry_33_name: string | null;
	industry_17_code: number | null;
	industry_17_name: string | null;
	scale_code: number | null;
	scale_name: string | null;
};



export type JpxStockInfosPublicList = {
	count: number;
	data: Array<JpxStockInfoPublic>;
};



/**
 * メニューラベルを表すクラス
 */
export type MenuLabel = {
	attr_value: string;
	label: string;
};



/**
 * メニューラベルのリストを表すクラス
 */
export type MenuLabelList = {
	data: Array<MenuLabel>;
	count: number;
};



export type Message = {
	message: string;
};



export type MetricParentSchema = {
	name: string;
	order: number;
	label: string;
	value: MetricSchema | null;
	change: MetricSchema | null;
};



export type MetricSchema = {
	key: string;
	name: string;
	value: number | null;
	unit: string | null;
};



export type NewPassword = {
	token: string;
	new_password: string;
};



/**
 * StockWikiCreate
 */
export type StockWikiCreate = {
	code: string;
	name: string;
	description: string | null;
	url: string | null;
};



/**
 * StockWikiPublic
 */
export type StockWikiPublic = {
	code: string;
	name: string;
	description: string | null;
	url: string | null;
};



/**
 * StockWikisPublicList
 */
export type StockWikisPublicList = {
	count: number;
	data: Array<StockWikiPublic>;
};



export type Token = {
	access_token: string;
	token_type?: string;
};



/**
 * ツリーアイテムを表すクラス
 */
export type TreeItem = {
	id: number;
	xlink_from: string;
	xlink_to: string;
	attr_value: string;
	xlink_arcrole: string;
	xlink_order: number;
	level: number;
	has_children: boolean;
};



/**
 * ツリーアイテムのリストを表すクラス
 */
export type TreeItemsList = {
	count: number;
	data: Array<TreeItem>;
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

