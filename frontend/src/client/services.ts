import type { CancelablePromise } from './core/CancelablePromise';
import { OpenAPI } from './core/OpenAPI';
import { request as __request } from './core/request';

import type { GroupingNonFractionList,edjp_FinancialReportSummary,edjp_FinancialReportSummary_FY,edjp_FinancialReportSummary_HY_specific_business,edjp_FinancialReportSummary_Q1,edjp_FinancialReportSummary_Q2,edjp_FinancialReportSummary_Q3,IxHeadTitleCreate,IxHeadTitleCreateList,IxHeadTitlePublic,IxHeadTitlesPublic,IxReportTypeCountList,IxNonFractionCreate_Input,IxNonFractionCreate_Output,IxNonFractionCreateList,IxNonNumericCreate,IxNonNumericCreateList,IxLabelArcCreate,IxLabelArcCreateList,IxLabelLocCreate,IxLabelLocCreateList,IxLabelValueCreate,IxLabelValueCreateList,IxCalculationArcCreate_Input,IxCalculationArcCreate_Output,IxCalculationArcCreateList,IxCalculationLocCreate,IxCalculationLocCreateList,IxDefinitionArcCreate_Input,IxDefinitionArcCreate_Output,IxDefinitionArcCreateList,IxDefinitionLocCreate,IxDefinitionLocCreateList,IxPresentationArcCreate_Input,IxPresentationArcCreate_Output,IxPresentationArcCreateList,IxPresentationLocCreate,IxPresentationLocCreateList,IxSourceFileCreate,IxSourceFileCreateList,IxSchemaLinkBaseCreate,IxSchemaLinkBaseCreateList,IxFilePathCreate,IxFilePathPublic,IxQualitativeCreate,IxQualitativeCreates,IxQualitativePublic,IxQualitativePublics,QualitativeInfoHeader,Body_login_login_access_token,Message,NewPassword,Token,UserPublic,UpdatePassword,UserCreate,UserRegister,UsersPublic,UserUpdate,UserUpdateMe,ItemCreate,ItemPublic,ItemsPublic,ItemUpdate } from './models';

export type TDataGetSummaryContextLabels = {
                contexts: Array<string>
                
            }

export class XbrlService {

	/**
	 * Get Summary Context Labels
	 * Get context labels
	 * @returns unknown Successful Response
	 * @throws ApiError
	 */
	public static getSummaryContextLabels(data: TDataGetSummaryContextLabels): CancelablePromise<unknown> {
		const {
contexts,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/generate/context_labels/',
			query: {
				contexts
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Get Grouping Non Fraction
	 * 分数でないグルーピングされた項目名とコンテキストを取得する
	 * @returns GroupingNonFractionList Successful Response
	 * @throws ApiError
	 */
	public static getGroupingNonFraction(): CancelablePromise<GroupingNonFractionList> {
				return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/generate/grouping/non_fraction/',
		});
	}

}

export type TDataGetSummaryHead = {
                code: string
period: number
year: number
                
            }
export type TDataGetSummaryKey = {
                code: string
period: number
year: number
                
            }
export type TDataGetSummaryItems = {
                code: string
period: number
year: number
                
            }

export class SummaryService {

	/**
	 * Get Summary Head
	 * Get summary of all items.
	 * @returns unknown Successful Response
	 * @throws ApiError
	 */
	public static getSummaryHead(data: TDataGetSummaryHead): CancelablePromise<unknown> {
		const {
code,
period,
year,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/ix/summary/head/',
			query: {
				code, year, period
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Get Summary Key
	 * Get summary of all items.
	 * @returns string Successful Response
	 * @throws ApiError
	 */
	public static getSummaryKey(data: TDataGetSummaryKey): CancelablePromise<Record<string, string>> {
		const {
code,
period,
year,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/ix/summary/key/',
			query: {
				code, year, period
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Get Summary Items
	 * Get summary of all items.
	 * @returns unknown Successful Response
	 * @throws ApiError
	 */
	public static getSummaryItems(data: TDataGetSummaryItems): CancelablePromise<edjp_FinancialReportSummary_HY_specific_business | edjp_FinancialReportSummary_Q1 | edjp_FinancialReportSummary_Q2 | edjp_FinancialReportSummary_Q3 | edjp_FinancialReportSummary_FY | edjp_FinancialReportSummary> {
		const {
code,
period,
year,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/ix/summary/items/',
			query: {
				code, year, period
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

}

export type TDataIsModelChecking = {
                headItemKey: string
                
            }

export class XbrlCheckService {

	/**
	 * Is Model Checking
	 * head_item_keyがすべてのテーブルに存在するか確認します
 * 
 * Properties:
 * - session: SessionDep
 * - head_item_key: str
 * 
 * Returns:
 * - bool
 * 
 * Raises:
 * - HTTPException: テーブルにhead_item_keyが存在しない場合
	 * @returns boolean Successful Response
	 * @throws ApiError
	 */
	public static isModelChecking(data: TDataIsModelChecking): CancelablePromise<boolean> {
		const {
headItemKey,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/xbrl/check/model/',
			query: {
				head_item_key: headItemKey
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

}

export type TDataCreateIxHeadTitleItem = {
                requestBody: IxHeadTitleCreate
                
            }
export type TDataCreateIxHeadTitleItemExists = {
                requestBody: IxHeadTitleCreate
                
            }
export type TDataCreateIxHeadTitleItemsExists = {
                requestBody: IxHeadTitleCreateList
                
            }
export type TDataIsIxHeadTitleItemExists = {
                headItemKey: string
                
            }
export type TDataGetCountReportType = {
                dateStr: string
                
            }
export type TDataSelectIxHeadTitleItems = {
                dateStr: string
                
            }
export type TDataDeleteIxHeadTitleItem = {
                headItemKey: string
                
            }
export type TDataActiveIxHeadTitleItem = {
                headItemKey: string
                
            }
export type TDataIsIxHeadTitleItemActive = {
                headItemKey: string
                
            }

export class XbrlIxHeadService {

	/**
	 * Create Ix Head Title Item
	 * Create new item.
	 * @returns IxHeadTitlePublic Successful Response
	 * @throws ApiError
	 */
	public static createIxHeadTitleItem(data: TDataCreateIxHeadTitleItem): CancelablePromise<IxHeadTitlePublic> {
		const {
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'POST',
			url: '/api/v1/xbrl/ix/head/',
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Create Ix Head Title Item Exists
	 * Create new item.
	 * @returns string Successful Response
	 * @throws ApiError
	 */
	public static createIxHeadTitleItemExists(data: TDataCreateIxHeadTitleItemExists): CancelablePromise<string> {
		const {
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'POST',
			url: '/api/v1/xbrl/ix/head/exist/',
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Create Ix Head Title Items Exists
	 * Create new items.(Insert Select ... Not Exists)
	 * @returns string Successful Response
	 * @throws ApiError
	 */
	public static createIxHeadTitleItemsExists(data: TDataCreateIxHeadTitleItemsExists): CancelablePromise<string> {
		const {
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'POST',
			url: '/api/v1/xbrl/ix/head/list/',
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Is Ix Head Title Item Exists
	 * Check if item exists.
	 * @returns boolean Successful Response
	 * @throws ApiError
	 */
	public static isIxHeadTitleItemExists(data: TDataIsIxHeadTitleItemExists): CancelablePromise<boolean> {
		const {
headItemKey,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/xbrl/ix/head/is/{head_item_key}/',
			path: {
				head_item_key: headItemKey
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Get Count Report Type
	 * 指定した日付の報告書タイプごとの件数を取得する。
	 * @returns IxReportTypeCountList Successful Response
	 * @throws ApiError
	 */
	public static getCountReportType(data: TDataGetCountReportType): CancelablePromise<IxReportTypeCountList> {
		const {
dateStr,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/xbrl/head/count-report-type/',
			query: {
				date_str: dateStr
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Select Ix Head Title Items
	 * 指定した日付の報告書タイプごとの件数を取得する。
	 * @returns IxHeadTitlesPublic Successful Response
	 * @throws ApiError
	 */
	public static selectIxHeadTitleItems(data: TDataSelectIxHeadTitleItems): CancelablePromise<IxHeadTitlesPublic> {
		const {
dateStr,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/xbrl/head/select/',
			query: {
				date_str: dateStr
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Delete Ix Head Title Item
	 * Delete item.
	 * @returns boolean Successful Response
	 * @throws ApiError
	 */
	public static deleteIxHeadTitleItem(data: TDataDeleteIxHeadTitleItem): CancelablePromise<boolean> {
		const {
headItemKey,
} = data;
		return __request(OpenAPI, {
			method: 'DELETE',
			url: '/api/v1/xbrl/ix/head/delete/',
			query: {
				head_item_key: headItemKey
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Active Ix Head Title Item
	 * Active item.
	 * @returns boolean Successful Response
	 * @throws ApiError
	 */
	public static activeIxHeadTitleItem(data: TDataActiveIxHeadTitleItem): CancelablePromise<boolean> {
		const {
headItemKey,
} = data;
		return __request(OpenAPI, {
			method: 'PUT',
			url: '/api/v1/xbrl/ix/head/active/',
			query: {
				head_item_key: headItemKey
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Is Ix Head Title Item Active
	 * Check if item is active.
	 * @returns boolean Successful Response
	 * @throws ApiError
	 */
	public static isIxHeadTitleItemActive(data: TDataIsIxHeadTitleItemActive): CancelablePromise<boolean> {
		const {
headItemKey,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/xbrl/ix/head/is_active/',
			query: {
				head_item_key: headItemKey
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

}

export type TDataCreateIxNonNumericItem = {
                requestBody: IxNonNumericCreate
                
            }
export type TDataCreateIxNonNumericItemsExists = {
                requestBody: IxNonNumericCreateList
                
            }
export type TDataIsIxNonNumericItemExists = {
                sourceFileId: string
                
            }
export type TDataDeleteIxNonNumericItem = {
                headItemKey: string
                
            }
export type TDataCreateIxNonFractionItem = {
                requestBody: IxNonFractionCreate_Input
                
            }
export type TDataCreateIxNonFractionItemsExists = {
                requestBody: IxNonFractionCreateList
                
            }
export type TDataIsIxNonFractionItemExists = {
                sourceFileId: string
                
            }
export type TDataIsConsolidated = {
                headItemKey: string
                
            }
export type TDataDeleteIxNonFractionItem = {
                headItemKey: string
                
            }
export type TDataGetIxNonFractionItemCount = {
                headIdKey: string
                
            }

export class XbrlIxService {

	/**
	 * Create Ix Non Numeric Item
	 * Create new item.
	 * @returns IxNonNumericCreate Successful Response
	 * @throws ApiError
	 */
	public static createIxNonNumericItem(data: TDataCreateIxNonNumericItem): CancelablePromise<IxNonNumericCreate> {
		const {
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'POST',
			url: '/api/v1/xbrl/ix/non_numeric/',
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Create Ix Non Numeric Items Exists
	 * Create new items.(Insert Select ... Not Exists)
	 * @returns string Successful Response
	 * @throws ApiError
	 */
	public static createIxNonNumericItemsExists(data: TDataCreateIxNonNumericItemsExists): CancelablePromise<string> {
		const {
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'POST',
			url: '/api/v1/xbrl/ix/non_numeric/list/',
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Is Ix Non Numeric Item Exists
	 * Check if item exists.
	 * @returns boolean Successful Response
	 * @throws ApiError
	 */
	public static isIxNonNumericItemExists(data: TDataIsIxNonNumericItemExists): CancelablePromise<boolean> {
		const {
sourceFileId,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/xbrl/ix/non_numeric/is/{source_file_id}/',
			path: {
				source_file_id: sourceFileId
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Delete Ix Non Numeric Item
	 * Delete item.
	 * @returns boolean Successful Response
	 * @throws ApiError
	 */
	public static deleteIxNonNumericItem(data: TDataDeleteIxNonNumericItem): CancelablePromise<boolean> {
		const {
headItemKey,
} = data;
		return __request(OpenAPI, {
			method: 'DELETE',
			url: '/api/v1/xbrl/ix/non_numeric/delete/',
			query: {
				head_item_key: headItemKey
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Create Ix Non Fraction Item
	 * Create new item.
	 * @returns IxNonFractionCreate_Output Successful Response
	 * @throws ApiError
	 */
	public static createIxNonFractionItem(data: TDataCreateIxNonFractionItem): CancelablePromise<IxNonFractionCreate_Output> {
		const {
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'POST',
			url: '/api/v1/xbrl/ix/non_fraction/',
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Create Ix Non Fraction Items Exists
	 * Create new items.(Insert Select ... Not Exists)
	 * @returns string Successful Response
	 * @throws ApiError
	 */
	public static createIxNonFractionItemsExists(data: TDataCreateIxNonFractionItemsExists): CancelablePromise<string> {
		const {
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'POST',
			url: '/api/v1/xbrl/ix/non_fraction/list/',
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Is Ix Non Fraction Item Exists
	 * Check if item exists.
	 * @returns boolean Successful Response
	 * @throws ApiError
	 */
	public static isIxNonFractionItemExists(data: TDataIsIxNonFractionItemExists): CancelablePromise<boolean> {
		const {
sourceFileId,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/xbrl/ix/non_fraction/is/{source_file_id}/',
			path: {
				source_file_id: sourceFileId
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Is Consolidated
	 * Check if item exists.
	 * @returns boolean Successful Response
	 * @throws ApiError
	 */
	public static isConsolidated(data: TDataIsConsolidated): CancelablePromise<boolean> {
		const {
headItemKey,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/xbrl/isConsolidated/{head_item_key}/',
			path: {
				head_item_key: headItemKey
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Delete Ix Non Fraction Item
	 * Delete item.
	 * @returns boolean Successful Response
	 * @throws ApiError
	 */
	public static deleteIxNonFractionItem(data: TDataDeleteIxNonFractionItem): CancelablePromise<boolean> {
		const {
headItemKey,
} = data;
		return __request(OpenAPI, {
			method: 'DELETE',
			url: '/api/v1/xbrl/ix/non_fraction/delete/',
			query: {
				head_item_key: headItemKey
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Get Ix Non Fraction Item Count
	 * Get item count.
	 * @returns number Successful Response
	 * @throws ApiError
	 */
	public static getIxNonFractionItemCount(data: TDataGetIxNonFractionItemCount): CancelablePromise<number> {
		const {
headIdKey,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/xbrl/item/net_sales/',
			query: {
				head_id_key: headIdKey
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

}

export type TDataCreateIxLabelLocItem = {
                requestBody: IxLabelLocCreate
                
            }
export type TDataCreateIxLabelArcItem = {
                requestBody: IxLabelArcCreate
                
            }
export type TDataCreateIxLabelValueItem = {
                requestBody: IxLabelValueCreate
                
            }
export type TDataCreateIxLabelLocItemsExists = {
                requestBody: IxLabelLocCreateList
                
            }
export type TDataCreateIxLabelArcItemsExists = {
                requestBody: IxLabelArcCreateList
                
            }
export type TDataCreateIxLabelValueItemsExists = {
                requestBody: IxLabelValueCreateList
                
            }
export type TDataGetIxLabelLocItem = {
                sourceFileId: string
                
            }
export type TDataGetIxLabelArcItem = {
                sourceFileId: string
                
            }
export type TDataGetIxLabelValueItem = {
                sourceFileId: string
                
            }
export type TDataDeleteIxLabelLocItem = {
                requestBody: Array<string>
                
            }
export type TDataDeleteIxLabelArcItem = {
                requestBody: Array<string>
                
            }
export type TDataDeleteIxLabelValueItem = {
                requestBody: Array<string>
                
            }

export class XbrlLabService {

	/**
	 * Create Ix Label Loc Item
	 * Create new item.
	 * @returns IxLabelLocCreate Successful Response
	 * @throws ApiError
	 */
	public static createIxLabelLocItem(data: TDataCreateIxLabelLocItem): CancelablePromise<IxLabelLocCreate> {
		const {
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'POST',
			url: '/api/v1/xbrl/link/lab/loc/',
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Create Ix Label Arc Item
	 * Create new item.
	 * @returns IxLabelArcCreate Successful Response
	 * @throws ApiError
	 */
	public static createIxLabelArcItem(data: TDataCreateIxLabelArcItem): CancelablePromise<IxLabelArcCreate> {
		const {
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'POST',
			url: '/api/v1/xbrl/link/lab/arc/',
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Create Ix Label Value Item
	 * Create new item.
	 * @returns IxLabelValueCreate Successful Response
	 * @throws ApiError
	 */
	public static createIxLabelValueItem(data: TDataCreateIxLabelValueItem): CancelablePromise<IxLabelValueCreate> {
		const {
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'POST',
			url: '/api/v1/xbrl/link/lab/value/',
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Create Ix Label Loc Items Exists
	 * Create new items.(Insert Select ... Not Exists)
	 * @returns string Successful Response
	 * @throws ApiError
	 */
	public static createIxLabelLocItemsExists(data: TDataCreateIxLabelLocItemsExists): CancelablePromise<string> {
		const {
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'POST',
			url: '/api/v1/xbrl/link/lab/loc/list/',
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Create Ix Label Arc Items Exists
	 * Create new items.(Insert Select ... Not Exists)
	 * @returns string Successful Response
	 * @throws ApiError
	 */
	public static createIxLabelArcItemsExists(data: TDataCreateIxLabelArcItemsExists): CancelablePromise<string> {
		const {
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'POST',
			url: '/api/v1/xbrl/link/lab/arc/list/',
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Create Ix Label Value Items Exists
	 * Create new items.(Insert Select ... Not Exists)
	 * @returns string Successful Response
	 * @throws ApiError
	 */
	public static createIxLabelValueItemsExists(data: TDataCreateIxLabelValueItemsExists): CancelablePromise<string> {
		const {
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'POST',
			url: '/api/v1/xbrl/link/lab/value/list/',
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Get Ix Label Loc Item
	 * Get item.
	 * @returns boolean Successful Response
	 * @throws ApiError
	 */
	public static getIxLabelLocItem(data: TDataGetIxLabelLocItem): CancelablePromise<boolean> {
		const {
sourceFileId,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/xbrl/link/lab/loc/is/{source_file_id}/',
			path: {
				source_file_id: sourceFileId
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Get Ix Label Arc Item
	 * Get item.
	 * @returns boolean Successful Response
	 * @throws ApiError
	 */
	public static getIxLabelArcItem(data: TDataGetIxLabelArcItem): CancelablePromise<boolean> {
		const {
sourceFileId,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/xbrl/link/lab/arc/is/{source_file_id}/',
			path: {
				source_file_id: sourceFileId
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Get Ix Label Value Item
	 * Get item.
	 * @returns boolean Successful Response
	 * @throws ApiError
	 */
	public static getIxLabelValueItem(data: TDataGetIxLabelValueItem): CancelablePromise<boolean> {
		const {
sourceFileId,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/xbrl/link/lab/value/is/{source_file_id}/',
			path: {
				source_file_id: sourceFileId
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Delete Ix Label Loc Item
	 * Delete item.
	 * @returns boolean Successful Response
	 * @throws ApiError
	 */
	public static deleteIxLabelLocItem(data: TDataDeleteIxLabelLocItem): CancelablePromise<boolean> {
		const {
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'DELETE',
			url: '/api/v1/xbrl/link/lab/loc/delete/',
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Delete Ix Label Arc Item
	 * Delete item.
	 * @returns boolean Successful Response
	 * @throws ApiError
	 */
	public static deleteIxLabelArcItem(data: TDataDeleteIxLabelArcItem): CancelablePromise<boolean> {
		const {
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'DELETE',
			url: '/api/v1/xbrl/link/lab/arc/delete/',
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Delete Ix Label Value Item
	 * Delete item.
	 * @returns boolean Successful Response
	 * @throws ApiError
	 */
	public static deleteIxLabelValueItem(data: TDataDeleteIxLabelValueItem): CancelablePromise<boolean> {
		const {
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'DELETE',
			url: '/api/v1/xbrl/link/lab/value/delete/',
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				422: `Validation Error`,
			},
		});
	}

}

export type TDataCreateIxCalLocItem = {
                requestBody: IxCalculationLocCreate
                
            }
export type TDataCreateIxCalArcItem = {
                requestBody: IxCalculationArcCreate_Input
                
            }
export type TDataCreateIxCalLocItemsExists = {
                requestBody: IxCalculationLocCreateList
                
            }
export type TDataCreateIxCalArcItemsExists = {
                requestBody: IxCalculationArcCreateList
                
            }
export type TDataGetIxCalLocItem = {
                sourceFileId: string
                
            }
export type TDataGetIxCalArcItem = {
                sourceFileId: string
                
            }
export type TDataDeleteIxCalLocItem = {
                headItemKey: string | null
                
            }
export type TDataDeleteIxCalArcItem = {
                headItemKey: string | null
                
            }

export class XbrlCalService {

	/**
	 * Create Ix Cal Loc Item
	 * Create new item.
	 * @returns IxCalculationLocCreate Successful Response
	 * @throws ApiError
	 */
	public static createIxCalLocItem(data: TDataCreateIxCalLocItem): CancelablePromise<IxCalculationLocCreate> {
		const {
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'POST',
			url: '/api/v1/xbrl/link/cal/loc/',
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Create Ix Cal Arc Item
	 * Create new item.
	 * @returns IxCalculationArcCreate_Output Successful Response
	 * @throws ApiError
	 */
	public static createIxCalArcItem(data: TDataCreateIxCalArcItem): CancelablePromise<IxCalculationArcCreate_Output> {
		const {
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'POST',
			url: '/api/v1/xbrl/link/cal/arc/',
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Create Ix Cal Loc Items Exists
	 * Create new items.(Insert Select ... Not Exists)
	 * @returns string Successful Response
	 * @throws ApiError
	 */
	public static createIxCalLocItemsExists(data: TDataCreateIxCalLocItemsExists): CancelablePromise<string> {
		const {
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'POST',
			url: '/api/v1/xbrl/link/cal/loc/list/',
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Create Ix Cal Arc Items Exists
	 * Create new items.(Insert Select ... Not Exists)
	 * @returns string Successful Response
	 * @throws ApiError
	 */
	public static createIxCalArcItemsExists(data: TDataCreateIxCalArcItemsExists): CancelablePromise<string> {
		const {
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'POST',
			url: '/api/v1/xbrl/link/cal/arc/list/',
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Get Ix Cal Loc Item
	 * Get item.
	 * @returns boolean Successful Response
	 * @throws ApiError
	 */
	public static getIxCalLocItem(data: TDataGetIxCalLocItem): CancelablePromise<boolean> {
		const {
sourceFileId,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/xbrl/link/cal/loc/is/{source_file_id}/',
			path: {
				source_file_id: sourceFileId
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Get Ix Cal Arc Item
	 * Get item.
	 * @returns boolean Successful Response
	 * @throws ApiError
	 */
	public static getIxCalArcItem(data: TDataGetIxCalArcItem): CancelablePromise<boolean> {
		const {
sourceFileId,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/xbrl/link/cal/arc/is/{source_file_id}/',
			path: {
				source_file_id: sourceFileId
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Delete Ix Cal Loc Item
	 * Delete item.
	 * @returns boolean Successful Response
	 * @throws ApiError
	 */
	public static deleteIxCalLocItem(data: TDataDeleteIxCalLocItem): CancelablePromise<boolean> {
		const {
headItemKey,
} = data;
		return __request(OpenAPI, {
			method: 'DELETE',
			url: '/api/v1/xbrl/link/cal/loc/delete/',
			query: {
				head_item_key: headItemKey
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Delete Ix Cal Arc Item
	 * Delete item.
	 * @returns boolean Successful Response
	 * @throws ApiError
	 */
	public static deleteIxCalArcItem(data: TDataDeleteIxCalArcItem): CancelablePromise<boolean> {
		const {
headItemKey,
} = data;
		return __request(OpenAPI, {
			method: 'DELETE',
			url: '/api/v1/xbrl/link/cal/arc/delete/',
			query: {
				head_item_key: headItemKey
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

}

export type TDataCreateIxDefLocItem = {
                requestBody: IxDefinitionLocCreate
                
            }
export type TDataCreateIxDefArcItem = {
                requestBody: IxDefinitionArcCreate_Input
                
            }
export type TDataCreateIxDefLocItemsExists = {
                requestBody: IxDefinitionLocCreateList
                
            }
export type TDataCreateIxDefArcItemsExists = {
                requestBody: IxDefinitionArcCreateList
                
            }
export type TDataGetIxDefLocItem = {
                sourceFileId: string
                
            }
export type TDataGetIxDefArcItem = {
                sourceFileId: string
                
            }
export type TDataDeleteIxDefLocItem = {
                headItemKey: string
                
            }
export type TDataDeleteIxDefArcItem = {
                headItemKey: string
                
            }

export class XbrlDefService {

	/**
	 * Create Ix Def Loc Item
	 * Create new item.
	 * @returns IxDefinitionLocCreate Successful Response
	 * @throws ApiError
	 */
	public static createIxDefLocItem(data: TDataCreateIxDefLocItem): CancelablePromise<IxDefinitionLocCreate> {
		const {
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'POST',
			url: '/api/v1/xbrl/link/def/loc/',
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Create Ix Def Arc Item
	 * Create new item.
	 * @returns IxDefinitionArcCreate_Output Successful Response
	 * @throws ApiError
	 */
	public static createIxDefArcItem(data: TDataCreateIxDefArcItem): CancelablePromise<IxDefinitionArcCreate_Output> {
		const {
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'POST',
			url: '/api/v1/xbrl/link/def/arc/',
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Create Ix Def Loc Items Exists
	 * Create new items.(Insert Select ... Not Exists)
	 * @returns string Successful Response
	 * @throws ApiError
	 */
	public static createIxDefLocItemsExists(data: TDataCreateIxDefLocItemsExists): CancelablePromise<string> {
		const {
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'POST',
			url: '/api/v1/xbrl/link/def/loc/list/',
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Create Ix Def Arc Items Exists
	 * Create new items.(Insert Select ... Not Exists)
	 * @returns string Successful Response
	 * @throws ApiError
	 */
	public static createIxDefArcItemsExists(data: TDataCreateIxDefArcItemsExists): CancelablePromise<string> {
		const {
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'POST',
			url: '/api/v1/xbrl/link/def/arc/list/',
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Get Ix Def Loc Item
	 * Get item.
	 * @returns boolean Successful Response
	 * @throws ApiError
	 */
	public static getIxDefLocItem(data: TDataGetIxDefLocItem): CancelablePromise<boolean> {
		const {
sourceFileId,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/xbrl/link/def/loc/is/{source_file_id}/',
			path: {
				source_file_id: sourceFileId
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Get Ix Def Arc Item
	 * Get item.
	 * @returns boolean Successful Response
	 * @throws ApiError
	 */
	public static getIxDefArcItem(data: TDataGetIxDefArcItem): CancelablePromise<boolean> {
		const {
sourceFileId,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/xbrl/link/def/arc/is/{source_file_id}/',
			path: {
				source_file_id: sourceFileId
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Delete Ix Def Loc Item
	 * Delete item.
	 * @returns boolean Successful Response
	 * @throws ApiError
	 */
	public static deleteIxDefLocItem(data: TDataDeleteIxDefLocItem): CancelablePromise<boolean> {
		const {
headItemKey,
} = data;
		return __request(OpenAPI, {
			method: 'DELETE',
			url: '/api/v1/xbrl/link/def/loc/delete/',
			query: {
				head_item_key: headItemKey
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Delete Ix Def Arc Item
	 * Delete item.
	 * @returns boolean Successful Response
	 * @throws ApiError
	 */
	public static deleteIxDefArcItem(data: TDataDeleteIxDefArcItem): CancelablePromise<boolean> {
		const {
headItemKey,
} = data;
		return __request(OpenAPI, {
			method: 'DELETE',
			url: '/api/v1/xbrl/link/def/arc/delete/',
			query: {
				head_item_key: headItemKey
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

}

export type TDataCreateIxPreLocItem = {
                requestBody: IxPresentationLocCreate
                
            }
export type TDataCreateIxPreArcItem = {
                requestBody: IxPresentationArcCreate_Input
                
            }
export type TDataCreateIxPreLocItemsExists = {
                requestBody: IxPresentationLocCreateList
                
            }
export type TDataCreateIxPreArcItemsExists = {
                requestBody: IxPresentationArcCreateList
                
            }
export type TDataGetIxPreLocItem = {
                sourceFileId: string
                
            }
export type TDataGetIxPreArcItem = {
                sourceFileId: string
                
            }
export type TDataDeleteIxPreLocItem = {
                headItemKey: string
                
            }
export type TDataDeleteIxPreArcItem = {
                headItemKey: string
                
            }

export class XbrlPreService {

	/**
	 * Create Ix Pre Loc Item
	 * Create new item.
	 * @returns IxPresentationLocCreate Successful Response
	 * @throws ApiError
	 */
	public static createIxPreLocItem(data: TDataCreateIxPreLocItem): CancelablePromise<IxPresentationLocCreate> {
		const {
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'POST',
			url: '/api/v1/xbrl/link/pre/loc/',
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Create Ix Pre Arc Item
	 * Create new item.
	 * @returns IxPresentationArcCreate_Output Successful Response
	 * @throws ApiError
	 */
	public static createIxPreArcItem(data: TDataCreateIxPreArcItem): CancelablePromise<IxPresentationArcCreate_Output> {
		const {
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'POST',
			url: '/api/v1/xbrl/link/pre/arc/',
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Create Ix Pre Loc Items Exists
	 * Create new items.(Insert Select ... Not Exists)
	 * @returns string Successful Response
	 * @throws ApiError
	 */
	public static createIxPreLocItemsExists(data: TDataCreateIxPreLocItemsExists): CancelablePromise<string> {
		const {
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'POST',
			url: '/api/v1/xbrl/link/pre/loc/list/',
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Create Ix Pre Arc Items Exists
	 * Create new items.(Insert Select ... Not Exists)
	 * @returns string Successful Response
	 * @throws ApiError
	 */
	public static createIxPreArcItemsExists(data: TDataCreateIxPreArcItemsExists): CancelablePromise<string> {
		const {
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'POST',
			url: '/api/v1/xbrl/link/pre/arc/list/',
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Get Ix Pre Loc Item
	 * Check if item exists.
	 * @returns boolean Successful Response
	 * @throws ApiError
	 */
	public static getIxPreLocItem(data: TDataGetIxPreLocItem): CancelablePromise<boolean> {
		const {
sourceFileId,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/xbrl/link/pre/loc/is/{source_file_id}/',
			path: {
				source_file_id: sourceFileId
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Get Ix Pre Arc Item
	 * Check if item exists.
	 * @returns boolean Successful Response
	 * @throws ApiError
	 */
	public static getIxPreArcItem(data: TDataGetIxPreArcItem): CancelablePromise<boolean> {
		const {
sourceFileId,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/xbrl/link/pre/arc/is/{source_file_id}/',
			path: {
				source_file_id: sourceFileId
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Delete Ix Pre Loc Item
	 * Delete item.
	 * @returns boolean Successful Response
	 * @throws ApiError
	 */
	public static deleteIxPreLocItem(data: TDataDeleteIxPreLocItem): CancelablePromise<boolean> {
		const {
headItemKey,
} = data;
		return __request(OpenAPI, {
			method: 'DELETE',
			url: '/api/v1/xbrl/link/pre/loc/delete/',
			query: {
				head_item_key: headItemKey
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Delete Ix Pre Arc Item
	 * Delete item.
	 * @returns boolean Successful Response
	 * @throws ApiError
	 */
	public static deleteIxPreArcItem(data: TDataDeleteIxPreArcItem): CancelablePromise<boolean> {
		const {
headItemKey,
} = data;
		return __request(OpenAPI, {
			method: 'DELETE',
			url: '/api/v1/xbrl/link/pre/arc/delete/',
			query: {
				head_item_key: headItemKey
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

}

export type TDataCreateIxSourceFileItem = {
                requestBody: IxSourceFileCreate
                
            }
export type TDataCreateIxSourceFileItemExists = {
                requestBody: IxSourceFileCreate
                
            }
export type TDataCreateIxSourceFileItemsExists = {
                requestBody: IxSourceFileCreateList
                
            }
export type TDataGetIxSourceFileItem = {
                sourceFileId: string
                
            }
export type TDataDeleteIxSourceFileItem = {
                headItemKey: string
                
            }
export type TDataGetIxSourceFileIdList = {
                headItemKey: string
                
            }

export class XbrlSourceService {

	/**
	 * Create Ix Source File Item
	 * Create new item.
	 * @returns string Successful Response
	 * @throws ApiError
	 */
	public static createIxSourceFileItem(data: TDataCreateIxSourceFileItem): CancelablePromise<string> {
		const {
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'POST',
			url: '/api/v1/xbrl/source/',
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Create Ix Source File Item Exists
	 * Create new item.
	 * @returns boolean Successful Response
	 * @throws ApiError
	 */
	public static createIxSourceFileItemExists(data: TDataCreateIxSourceFileItemExists): CancelablePromise<boolean> {
		const {
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'POST',
			url: '/api/v1/xbrl/source/exist/',
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Create Ix Source File Items Exists
	 * Create new items.(Insert Select ... Not Exists)
	 * @returns string Successful Response
	 * @throws ApiError
	 */
	public static createIxSourceFileItemsExists(data: TDataCreateIxSourceFileItemsExists): CancelablePromise<string> {
		const {
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'POST',
			url: '/api/v1/xbrl/source/list/',
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Get Ix Source File Item
	 * Get item.
	 * @returns boolean Successful Response
	 * @throws ApiError
	 */
	public static getIxSourceFileItem(data: TDataGetIxSourceFileItem): CancelablePromise<boolean> {
		const {
sourceFileId,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/xbrl/is/exits/source_file_id/',
			query: {
				source_file_id: sourceFileId
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Delete Ix Source File Item
	 * Delete item.
	 * @returns boolean Successful Response
	 * @throws ApiError
	 */
	public static deleteIxSourceFileItem(data: TDataDeleteIxSourceFileItem): CancelablePromise<boolean> {
		const {
headItemKey,
} = data;
		return __request(OpenAPI, {
			method: 'DELETE',
			url: '/api/v1/xbrl/source/delete/',
			query: {
				head_item_key: headItemKey
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Get Ix Source File Id List
	 * Get item.
	 * @returns string Successful Response
	 * @throws ApiError
	 */
	public static getIxSourceFileIdList(data: TDataGetIxSourceFileIdList): CancelablePromise<Array<string>> {
		const {
headItemKey,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/xbrl/source/id_list/',
			query: {
				head_item_key: headItemKey
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

}

export type TDataCreateIxSchemaLinkbaseItem = {
                requestBody: IxSchemaLinkBaseCreate
                
            }
export type TDataCreateIxSchemaLinkbaseItemsExists = {
                requestBody: IxSchemaLinkBaseCreateList
                
            }
export type TDataIsIxSchemaItemExists = {
                headItemKey: string
                
            }
export type TDataDeleteIxSchemaItem = {
                headItemKey: string
                
            }

export class XbrlSchemaService {

	/**
	 * Create Ix Schema Linkbase Item
	 * Create new item.
	 * @returns IxSchemaLinkBaseCreate Successful Response
	 * @throws ApiError
	 */
	public static createIxSchemaLinkbaseItem(data: TDataCreateIxSchemaLinkbaseItem): CancelablePromise<IxSchemaLinkBaseCreate> {
		const {
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'POST',
			url: '/api/v1/xbrl/schema/linkbase/',
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Create Ix Schema Linkbase Items Exists
	 * Create new items.(Insert Select ... Not Exists)
	 * @returns string Successful Response
	 * @throws ApiError
	 */
	public static createIxSchemaLinkbaseItemsExists(data: TDataCreateIxSchemaLinkbaseItemsExists): CancelablePromise<string> {
		const {
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'POST',
			url: '/api/v1/xbrl/schema/linkbase/list/',
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Is Ix Schema Item Exists
	 * Check if item exists.
	 * @returns boolean Successful Response
	 * @throws ApiError
	 */
	public static isIxSchemaItemExists(data: TDataIsIxSchemaItemExists): CancelablePromise<boolean> {
		const {
headItemKey,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/xbrl/schema/linkbase/is/{head_item_key}/',
			path: {
				head_item_key: headItemKey
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Delete Ix Schema Item
	 * Delete item.
	 * @returns boolean Successful Response
	 * @throws ApiError
	 */
	public static deleteIxSchemaItem(data: TDataDeleteIxSchemaItem): CancelablePromise<boolean> {
		const {
headItemKey,
} = data;
		return __request(OpenAPI, {
			method: 'DELETE',
			url: '/api/v1/xbrl/schema/linkbase/delete/',
			query: {
				head_item_key: headItemKey
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

}

export type TDataCreateIxFilePathItem = {
                requestBody: IxFilePathCreate
                
            }
export type TDataIsIxFilePathItemExists = {
                filePath?: string | null
headItemKey?: string | null
                
            }
export type TDataDeleteIxFilePathItem = {
                filePath: string
                
            }

export class XbrlFilePathService {

	/**
	 * Create Ix File Path Item
	 * Create new item.
	 * @returns IxFilePathPublic Successful Response
	 * @throws ApiError
	 */
	public static createIxFilePathItem(data: TDataCreateIxFilePathItem): CancelablePromise<IxFilePathPublic> {
		const {
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'POST',
			url: '/api/v1/xbrl/ix/file_path/',
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Is Ix File Path Item Exists
	 * head_item_keyまたは、ファイルパスを指定して、レコードが存在するか確認する
	 * @returns boolean Successful Response
	 * @throws ApiError
	 */
	public static isIxFilePathItemExists(data: TDataIsIxFilePathItemExists = {}): CancelablePromise<boolean> {
		const {
filePath,
headItemKey,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/xbrl/is/file_path/',
			query: {
				head_item_key: headItemKey, file_path: filePath
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Delete Ix File Path Item
	 * Delete item.
	 * @returns boolean Successful Response
	 * @throws ApiError
	 */
	public static deleteIxFilePathItem(data: TDataDeleteIxFilePathItem): CancelablePromise<boolean> {
		const {
filePath,
} = data;
		return __request(OpenAPI, {
			method: 'DELETE',
			url: '/api/v1/xbrl/ix/file_path/delete/',
			query: {
				file_path: filePath
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

}

export type TDataCreateIxQualitativeItem = {
                requestBody: IxQualitativeCreate
                
            }
export type TDataReadIxQualitativeItem = {
                headItemKey: string
                
            }
export type TDataCreateIxQualitativeItemsExists = {
                requestBody: IxQualitativeCreates
                
            }
export type TDataUpdateIxQualitativeItems = {
                requestBody: IxQualitativeCreates
                
            }
export type TDataIsIxQualitativeItemExists = {
                headItemKey: string
                
            }
export type TDataDeleteIxQualitativeItem = {
                headItemKey: string
                
            }
export type TDataSearchContent = {
                keyword: string
                
            }

export class XbrlQualitativeService {

	/**
	 * Create Ix Qualitative Item
	 * 提携情報をIxQualitativeテーブルに登録する
 * 
 * Raises:
 * HTTPException: アイテムが既に存在する場合
 * 
 * Returns:
 * sc.ix_qualitative.IxQualitativePublic: 登録したアイテム
	 * @returns IxQualitativePublic Successful Response
	 * @throws ApiError
	 */
	public static createIxQualitativeItem(data: TDataCreateIxQualitativeItem): CancelablePromise<IxQualitativePublic> {
		const {
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'POST',
			url: '/api/v1/xbrl/qualitative/',
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Read Ix Qualitative Item
	 * 提携情報をIxQualitativeテーブルから取得する
 * 
 * Raises:
 * HTTPException: アイテムが存在しない場合
 * 
 * Returns:
 * sc.ix_qualitative.IxQualitativePublic: 取得したアイテム
	 * @returns QualitativeInfoHeader Successful Response
	 * @throws ApiError
	 */
	public static readIxQualitativeItem(data: TDataReadIxQualitativeItem): CancelablePromise<QualitativeInfoHeader> {
		const {
headItemKey,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/xbrl/qualitative/',
			query: {
				head_item_key: headItemKey
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Create Ix Qualitative Items Exists
	 * 提携情報をIxQualitativeテーブルに登録する
 * 
 * Raises:
 * HTTPException: アイテムが既に存在する場合
 * 
 * Returns:
 * sc.ix_qualitative.IxQualitativePublics: 登録したアイテム
	 * @returns IxQualitativePublics Successful Response
	 * @throws ApiError
	 */
	public static createIxQualitativeItemsExists(data: TDataCreateIxQualitativeItemsExists): CancelablePromise<IxQualitativePublics> {
		const {
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'POST',
			url: '/api/v1/xbrl/qualitative/list/',
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Update Ix Qualitative Items
	 * 提携情報をIxQualitativeテーブルに登録する
 * 
 * Raises:
 * HTTPException: アイテムが存在しない場合
 * 
 * Returns:
 * sc.ix_qualitative.IxQualitativePublics: 登録したアイテム
	 * @returns IxQualitativePublics Successful Response
	 * @throws ApiError
	 */
	public static updateIxQualitativeItems(data: TDataUpdateIxQualitativeItems): CancelablePromise<IxQualitativePublics> {
		const {
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'POST',
			url: '/api/v1/xbrl/qualitative/list/update/',
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Is Ix Qualitative Item Exists
	 * 提携情報がIxQualitativeテーブルに存在するか確認する
 * 
 * Returns:
 * bool: アイテムが存在する場合はTrue
	 * @returns boolean Successful Response
	 * @throws ApiError
	 */
	public static isIxQualitativeItemExists(data: TDataIsIxQualitativeItemExists): CancelablePromise<boolean> {
		const {
headItemKey,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/xbrl/qualitative/is/{head_item_key}/',
			path: {
				head_item_key: headItemKey
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Delete Ix Qualitative Item
	 * 提携情報をIxQualitativeテーブルから削除する
 * 
 * Raises:
 * HTTPException: アイテムが存在しない場合
 * 
 * Returns:
 * bool: 削除した場合はTrue
	 * @returns boolean Successful Response
	 * @throws ApiError
	 */
	public static deleteIxQualitativeItem(data: TDataDeleteIxQualitativeItem): CancelablePromise<boolean> {
		const {
headItemKey,
} = data;
		return __request(OpenAPI, {
			method: 'DELETE',
			url: '/api/v1/xbrl/qualitative/delete/',
			query: {
				head_item_key: headItemKey
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Search Content
	 * 定性情報から指定したキーワードを検索し、該当する証券コードを取得します
 * 
 * Properties:
 * - session: SessionDep - セッション
 * - keyword: str      - 検索キーワード
 * 
 * Returns:
 * List[str]: 証券コードのリスト
	 * @returns string Successful Response
	 * @throws ApiError
	 */
	public static searchContent(data: TDataSearchContent): CancelablePromise<Array<string>> {
		const {
keyword,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/xbrl/content/search/',
			query: {
				keyword
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

}

export type TDataLoginAccessToken = {
                formData: Body_login_login_access_token
                
            }
export type TDataRecoverPassword = {
                email: string
                
            }
export type TDataResetPassword = {
                requestBody: NewPassword
                
            }
export type TDataRecoverPasswordHtmlContent = {
                email: string
                
            }

export class LoginService {

	/**
	 * Login Access Token
	 * OAuth2 compatible token login, get an access token for future requests
	 * @returns Token Successful Response
	 * @throws ApiError
	 */
	public static loginAccessToken(data: TDataLoginAccessToken): CancelablePromise<Token> {
		const {
formData,
} = data;
		return __request(OpenAPI, {
			method: 'POST',
			url: '/api/v1/login/access-token',
			formData: formData,
			mediaType: 'application/x-www-form-urlencoded',
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Test Token
	 * Test access token
	 * @returns UserPublic Successful Response
	 * @throws ApiError
	 */
	public static testToken(): CancelablePromise<UserPublic> {
				return __request(OpenAPI, {
			method: 'POST',
			url: '/api/v1/login/test-token',
		});
	}

	/**
	 * Recover Password
	 * Password Recovery
	 * @returns Message Successful Response
	 * @throws ApiError
	 */
	public static recoverPassword(data: TDataRecoverPassword): CancelablePromise<Message> {
		const {
email,
} = data;
		return __request(OpenAPI, {
			method: 'POST',
			url: '/api/v1/password-recovery/{email}',
			path: {
				email
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Reset Password
	 * Reset password
	 * @returns Message Successful Response
	 * @throws ApiError
	 */
	public static resetPassword(data: TDataResetPassword): CancelablePromise<Message> {
		const {
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'POST',
			url: '/api/v1/reset-password/',
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Recover Password Html Content
	 * HTML Content for Password Recovery
	 * @returns string Successful Response
	 * @throws ApiError
	 */
	public static recoverPasswordHtmlContent(data: TDataRecoverPasswordHtmlContent): CancelablePromise<string> {
		const {
email,
} = data;
		return __request(OpenAPI, {
			method: 'POST',
			url: '/api/v1/password-recovery-html-content/{email}',
			path: {
				email
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

}

export type TDataReadUsers = {
                limit?: number
skip?: number
                
            }
export type TDataCreateUser = {
                requestBody: UserCreate
                
            }
export type TDataUpdateUserMe = {
                requestBody: UserUpdateMe
                
            }
export type TDataUpdatePasswordMe = {
                requestBody: UpdatePassword
                
            }
export type TDataRegisterUser = {
                requestBody: UserRegister
                
            }
export type TDataReadUserById = {
                userId: string
                
            }
export type TDataUpdateUser = {
                requestBody: UserUpdate
userId: string
                
            }
export type TDataDeleteUser = {
                userId: string
                
            }

export class UsersService {

	/**
	 * Read Users
	 * Retrieve users.
	 * @returns UsersPublic Successful Response
	 * @throws ApiError
	 */
	public static readUsers(data: TDataReadUsers = {}): CancelablePromise<UsersPublic> {
		const {
limit = 100,
skip = 0,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/users/',
			query: {
				skip, limit
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Create User
	 * Create new user.
	 * @returns UserPublic Successful Response
	 * @throws ApiError
	 */
	public static createUser(data: TDataCreateUser): CancelablePromise<UserPublic> {
		const {
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'POST',
			url: '/api/v1/users/',
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Read User Me
	 * Get current user.
	 * @returns UserPublic Successful Response
	 * @throws ApiError
	 */
	public static readUserMe(): CancelablePromise<UserPublic> {
				return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/users/me',
		});
	}

	/**
	 * Delete User Me
	 * Delete own user.
	 * @returns Message Successful Response
	 * @throws ApiError
	 */
	public static deleteUserMe(): CancelablePromise<Message> {
				return __request(OpenAPI, {
			method: 'DELETE',
			url: '/api/v1/users/me',
		});
	}

	/**
	 * Update User Me
	 * Update own user.
	 * @returns UserPublic Successful Response
	 * @throws ApiError
	 */
	public static updateUserMe(data: TDataUpdateUserMe): CancelablePromise<UserPublic> {
		const {
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'PATCH',
			url: '/api/v1/users/me',
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Update Password Me
	 * Update own password.
	 * @returns Message Successful Response
	 * @throws ApiError
	 */
	public static updatePasswordMe(data: TDataUpdatePasswordMe): CancelablePromise<Message> {
		const {
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'PATCH',
			url: '/api/v1/users/me/password',
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Register User
	 * Create new user without the need to be logged in.
	 * @returns UserPublic Successful Response
	 * @throws ApiError
	 */
	public static registerUser(data: TDataRegisterUser): CancelablePromise<UserPublic> {
		const {
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'POST',
			url: '/api/v1/users/signup',
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Read User By Id
	 * Get a specific user by id.
	 * @returns UserPublic Successful Response
	 * @throws ApiError
	 */
	public static readUserById(data: TDataReadUserById): CancelablePromise<UserPublic> {
		const {
userId,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/users/{user_id}',
			path: {
				user_id: userId
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Update User
	 * Update a user.
	 * @returns UserPublic Successful Response
	 * @throws ApiError
	 */
	public static updateUser(data: TDataUpdateUser): CancelablePromise<UserPublic> {
		const {
requestBody,
userId,
} = data;
		return __request(OpenAPI, {
			method: 'PATCH',
			url: '/api/v1/users/{user_id}',
			path: {
				user_id: userId
			},
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Delete User
	 * Delete a user.
	 * @returns Message Successful Response
	 * @throws ApiError
	 */
	public static deleteUser(data: TDataDeleteUser): CancelablePromise<Message> {
		const {
userId,
} = data;
		return __request(OpenAPI, {
			method: 'DELETE',
			url: '/api/v1/users/{user_id}',
			path: {
				user_id: userId
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

}

export type TDataTestEmail = {
                emailTo: string
                
            }

export class UtilsService {

	/**
	 * Test Email
	 * Test emails.
	 * @returns Message Successful Response
	 * @throws ApiError
	 */
	public static testEmail(data: TDataTestEmail): CancelablePromise<Message> {
		const {
emailTo,
} = data;
		return __request(OpenAPI, {
			method: 'POST',
			url: '/api/v1/utils/test-email/',
			query: {
				email_to: emailTo
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Health Check
	 * @returns boolean Successful Response
	 * @throws ApiError
	 */
	public static healthCheck(): CancelablePromise<boolean> {
				return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/utils/health-check/',
		});
	}

}

export type TDataReadItems = {
                limit?: number
skip?: number
                
            }
export type TDataCreateItem = {
                requestBody: ItemCreate
                
            }
export type TDataReadItem = {
                id: string
                
            }
export type TDataUpdateItem = {
                id: string
requestBody: ItemUpdate
                
            }
export type TDataDeleteItem = {
                id: string
                
            }

export class ItemsService {

	/**
	 * Read Items
	 * Retrieve items.
	 * @returns ItemsPublic Successful Response
	 * @throws ApiError
	 */
	public static readItems(data: TDataReadItems = {}): CancelablePromise<ItemsPublic> {
		const {
limit = 100,
skip = 0,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/items/',
			query: {
				skip, limit
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Create Item
	 * Create new item.
	 * @returns ItemPublic Successful Response
	 * @throws ApiError
	 */
	public static createItem(data: TDataCreateItem): CancelablePromise<ItemPublic> {
		const {
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'POST',
			url: '/api/v1/items/',
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Read Item
	 * Get item by ID.
	 * @returns ItemPublic Successful Response
	 * @throws ApiError
	 */
	public static readItem(data: TDataReadItem): CancelablePromise<ItemPublic> {
		const {
id,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/items/{id}',
			path: {
				id
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Update Item
	 * Update an item.
	 * @returns ItemPublic Successful Response
	 * @throws ApiError
	 */
	public static updateItem(data: TDataUpdateItem): CancelablePromise<ItemPublic> {
		const {
id,
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'PUT',
			url: '/api/v1/items/{id}',
			path: {
				id
			},
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Delete Item
	 * Delete an item.
	 * @returns Message Successful Response
	 * @throws ApiError
	 */
	public static deleteItem(data: TDataDeleteItem): CancelablePromise<Message> {
		const {
id,
} = data;
		return __request(OpenAPI, {
			method: 'DELETE',
			url: '/api/v1/items/{id}',
			path: {
				id
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

}