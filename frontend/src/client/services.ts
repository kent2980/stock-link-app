import type { CancelablePromise } from './core/CancelablePromise';
import { OpenAPI } from './core/OpenAPI';
import { request as __request } from './core/request';

import type { FiscalYearStockInfo,HeadItem,HeadItems,MenuTitles,StockInfo,StockRecordInfos,SummaryItemsAbstractJp,SummaryItemsAbstractJpList,IxHeadTitleCreate,IxHeadTitleCreateList,IxHeadTitlePublic,IxHeadTitlesPublic,IxReportTypeCountList,IxNonFractionCreate_Input,IxNonFractionCreate_Output,IxNonFractionCreateList,IxNonNumericCreate,IxNonNumericCreateList,IxLabelArcCreate,IxLabelArcCreateList,IxLabelLocCreate,IxLabelLocCreateList,IxLabelValueCreate,IxLabelValueCreateList,IxCalculationArcCreate_Input,IxCalculationArcCreate_Output,IxCalculationArcCreateList,IxCalculationLocCreate,IxCalculationLocCreateList,IxDefinitionArcCreate_Input,IxDefinitionArcCreate_Output,IxDefinitionArcCreateList,IxDefinitionLocCreate,IxDefinitionLocCreateList,IxPresentationArcCreate_Input,IxPresentationArcCreate_Output,IxPresentationArcCreateList,IxPresentationLocCreate,IxPresentationLocCreateList,IxSourceFileCreate,IxSourceFileCreateList,IxSchemaLinkBaseCreate,IxSchemaLinkBaseCreateList,IxFilePathCreate,IxFilePathPublic,IxQualitativeCreate,IxQualitativeCreates,IxQualitativePublic,IxQualitativePublics,QualitativeInfoHeader,Body_login_login_access_token,Message,NewPassword,Token,UserPublic,UpdatePassword,UserCreate,UserRegister,UsersPublic,UserUpdate,UserUpdateMe,ItemCreate,ItemPublic,ItemsPublic,ItemUpdate } from './models';

export type TDataReadStockRecord = {
                code?: string | null
dateStr?: string | null
limit?: number
period?: number | null
skip?: number
type?: string | null
                
            }
export type TDataReadNewStockRecord = {
                limit?: number
skip?: number
                
            }
export type TDataReadHeadItems = {
                code?: string
limit?: number
skip?: number
                
            }
export type TDataReadHeadItem = {
                xbrlId: string
                
            }
export type TDataReadMenuTitle = {
                id: string
type: string
                
            }
export type TDataReadMenuItems = {
                header?: string | null
id: string
type: string
                
            }
export type TDataReadStockInfo = {
                code: string
                
            }
export type TDataReadSummaryItems = {
                code: string
length?: number | null
                
            }
export type TDataReadSummaryItem = {
                code: string
count?: number | null
                
            }
export type TDataReadSummaryItemByXbrlId = {
                xbrlId: string
                
            }

export class XbrlViewService {

	/**
	 * Read Stock Record
	 * すべての銘柄コードを取得する
 * 
 * Args:
 * type (str): レポートの種類
 * 
 * Returns:
 * sc.ix_head.IxHeadShortsPublic: 銘柄コードのリスト
	 * @returns StockRecordInfos Successful Response
	 * @throws ApiError
	 */
	public static readStockRecord(data: TDataReadStockRecord = {}): CancelablePromise<StockRecordInfos> {
		const {
code,
dateStr,
limit = 10,
period,
skip = 0,
type,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/xbrl/view/stock/all/',
			query: {
				code, type, dateStr, period, skip, limit
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Read New Stock Record
	 * @returns StockRecordInfos Successful Response
	 * @throws ApiError
	 */
	public static readNewStockRecord(data: TDataReadNewStockRecord = {}): CancelablePromise<StockRecordInfos> {
		const {
limit = 10,
skip = 0,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/xbrl/view/stock/all/new/',
			query: {
				skip, limit
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Read Head Items
	 * 銘柄コードからXBRLファイルのIDを取得する
 * Args:
 * code (str): 銘柄コード
 * limit (int): 取得数
 * skip (int): スキップ数
	 * @returns HeadItems Successful Response
	 * @throws ApiError
	 */
	public static readHeadItems(data: TDataReadHeadItems = {}): CancelablePromise<HeadItems> {
		const {
code,
limit = 10,
skip = 0,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/xbrl/view/head_items/',
			query: {
				code, limit, skip
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Read Head Item
	 * XBRLファイルのIDからXBRLファイルの情報を取得する
 * Args:
 * xbrl_id (str): XBRLファイルのID
	 * @returns HeadItem Successful Response
	 * @throws ApiError
	 */
	public static readHeadItem(data: TDataReadHeadItem): CancelablePromise<HeadItem> {
		const {
xbrlId,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/xbrl/view/head_item/${xbrl_id}',
			path: {
				xbrl_id: xbrlId
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Read Menu Title
	 * XBRLファイルのIDからメニューラベルを取得する
 * Args:
 * xbrl_id (str): XBRLファイルのID
	 * @returns MenuTitles Successful Response
	 * @throws ApiError
	 */
	public static readMenuTitle(data: TDataReadMenuTitle): CancelablePromise<MenuTitles> {
		const {
id,
type,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/xbrl/view/menu/',
			query: {
				type, id
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Read Menu Items
	 * XBRLファイルのIDとメニューラベルから項目を取得する
 * Args:
 * xbrl_id (str): XBRLファイルのID
 * menu_label (str): メニューラベル
	 * @returns unknown Successful Response
	 * @throws ApiError
	 */
	public static readMenuItems(data: TDataReadMenuItems): CancelablePromise<Record<string, unknown>> {
		const {
header,
id,
type,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/xbrl/view/items/',
			query: {
				type, id, header
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Read Stock Info
	 * 銘柄コードから企業情報を取得する
 * 
 * Args:
 * code (str): 銘柄コード
 * 
 * Returns:
 * sc.StockInfoPublic: 企業情報
	 * @returns unknown Successful Response
	 * @throws ApiError
	 */
	public static readStockInfo(data: TDataReadStockInfo): CancelablePromise<FiscalYearStockInfo | StockInfo> {
		const {
code,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/xbrl/view/info/',
			query: {
				code
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Read Summary Items
	 * 銘柄コードから決算情報を取得する
	 * @returns SummaryItemsAbstractJpList Successful Response
	 * @throws ApiError
	 */
	public static readSummaryItems(data: TDataReadSummaryItems): CancelablePromise<SummaryItemsAbstractJpList> {
		const {
code,
length,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/xbrl/view/summary/items/',
			query: {
				code, length
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Read Summary Item
	 * 銘柄コードから決算情報を取得する
	 * @returns SummaryItemsAbstractJp Successful Response
	 * @throws ApiError
	 */
	public static readSummaryItem(data: TDataReadSummaryItem): CancelablePromise<SummaryItemsAbstractJp> {
		const {
code,
count,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/xbrl/view/summary/item/',
			query: {
				code, count
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Read Summary Item By Xbrl Id
	 * XBRLファイルのIDから決算情報を取得する
	 * @returns SummaryItemsAbstractJp Successful Response
	 * @throws ApiError
	 */
	public static readSummaryItemByXbrlId(data: TDataReadSummaryItemByXbrlId): CancelablePromise<SummaryItemsAbstractJp> {
		const {
xbrlId,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/xbrl/view/summary/item/select/',
			query: {
				xbrl_id: xbrlId
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
                xbrlId: string
                
            }
export type TDataGetCountReportType = {
                dateStr: string
                
            }
export type TDataSelectIxHeadTitleItems = {
                dateStr: string
                
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
xbrlId,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/xbrl/ix/head/is/{xbrl_id}/',
			path: {
				xbrl_id: xbrlId
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
                xbrlId: string
                
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
xbrlId,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/xbrl/isConsolidated/{xbrl_id}/',
			path: {
				xbrl_id: xbrlId
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
			url: '/api/v1/xbrl/source/is/{source_file_id}/',
			path: {
				source_file_id: sourceFileId
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
                xbrlId: string
                
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
xbrlId,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/xbrl/schema/linkbase/is/{xbrl_id}/',
			path: {
				xbrl_id: xbrlId
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
                xbrlId: string
                
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
	 * Check if item exists.
	 * @returns boolean Successful Response
	 * @throws ApiError
	 */
	public static isIxFilePathItemExists(data: TDataIsIxFilePathItemExists): CancelablePromise<boolean> {
		const {
xbrlId,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/xbrl/ix/file_path/is/{xbrl_id}',
			path: {
				xbrl_id: xbrlId
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
                xbrlId: string
                
            }
export type TDataCreateIxQualitativeItemsExists = {
                requestBody: IxQualitativeCreates
                
            }
export type TDataUpdateIxQualitativeItems = {
                requestBody: IxQualitativeCreates
                
            }
export type TDataIsIxQualitativeItemExists = {
                xbrlId: string
                
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
xbrlId,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/xbrl/qualitative/',
			query: {
				xbrl_id: xbrlId
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
xbrlId,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/xbrl/qualitative/is/{xbrl_id}/',
			path: {
				xbrl_id: xbrlId
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