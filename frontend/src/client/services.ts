import type { CancelablePromise } from './core/CancelablePromise';
import { OpenAPI } from './core/OpenAPI';
import { request as __request } from './core/request';

import type { IndustriesList,JpxStockInfoPublic,JpxStockInfosPublicList,CompanySchema,FinancialResponseSchema,IxDocumentInfoList,MenuLabelList,TreeItemsList,StockWikiCreate,StockWikiPublic,StockWikisPublicList,Body_login_login_access_token,Message,NewPassword,Token,UserPublic,UpdatePassword,UserCreate,UserRegister,UsersPublic,UserUpdate,UserUpdateMe,ItemPublic,ItemUpdate } from './models';

export type TDataReadJpxStockInfoItem = {
                code: string
                
            }
export type TDataReadJpxStockInfoItemsTcs = {
                industry17Code?: number | null
industry33Code?: Array<number> | null
isItems?: boolean
limit?: number
                
            }
export type TDataReadJpxStockInfoItemTcs = {
                market: string
                
            }
export type TDataReadJpxStockInfoIndustryNames = {
                type: number
                
            }
export type TDataReadSelectIndustries = {
                industry17Code?: number | null
                
            }

export class JpxService {

	/**
	 * Read Jpx Stock Info Item
	 * Get item by code.
	 * @returns JpxStockInfoPublic Successful Response
	 * @throws ApiError
	 */
	public static readJpxStockInfoItem(data: TDataReadJpxStockInfoItem): CancelablePromise<JpxStockInfoPublic> {
		const {
code,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/jpx/stock_info/code/{code}',
			path: {
				code
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Read Jpx Stock Info Items
	 * Get all items.
	 * @returns JpxStockInfosPublicList Successful Response
	 * @throws ApiError
	 */
	public static readJpxStockInfoItems(): CancelablePromise<JpxStockInfosPublicList> {
				return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/jpx/stock_info/',
		});
	}

	/**
	 * Read Jpx Stock Info Items Tcs
	 * Get all items.
	 * @returns JpxStockInfosPublicList Successful Response
	 * @throws ApiError
	 */
	public static readJpxStockInfoItemsTcs(data: TDataReadJpxStockInfoItemsTcs = {}): CancelablePromise<JpxStockInfosPublicList> {
		const {
industry17Code,
industry33Code,
isItems = true,
limit = 100,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/jpx/stock_info/tcs',
			query: {
				industry_17_code: industry17Code, industry_33_code: industry33Code, isItems, limit
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Read Jpx Stock Info Item Tcs
	 * Get item by market.
	 * @returns JpxStockInfosPublicList Successful Response
	 * @throws ApiError
	 */
	public static readJpxStockInfoItemTcs(data: TDataReadJpxStockInfoItemTcs): CancelablePromise<JpxStockInfosPublicList> {
		const {
market,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/jpx/stock_info/tcs/{market}',
			path: {
				market
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Read Jpx Stock Info Industry Names
	 * Get all industries.
	 * @returns IndustriesList Successful Response
	 * @throws ApiError
	 */
	public static readJpxStockInfoIndustryNames(data: TDataReadJpxStockInfoIndustryNames): CancelablePromise<IndustriesList> {
		const {
type,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/jpx/stock_info/industries/{type}',
			path: {
				type
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Read Select Industries
	 * Get all industries.
	 * @returns IndustriesList Successful Response
	 * @throws ApiError
	 */
	public static readSelectIndustries(data: TDataReadSelectIndustries = {}): CancelablePromise<IndustriesList> {
		const {
industry17Code,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/jpx/stock_info/industries',
			query: {
				industry_17_code: industry17Code
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

}

export type TDataGetDocumentInfo = {
                code: string
                
            }
export type TDataReadMenuLabels = {
                headItemKey: string
xbrlType: string
                
            }
export type TDataReadTreeItems = {
                attrValue?: string
hasChildren?: boolean
headItemKey: string
xbrlType?: string
xlinkArcrole?: string
                
            }
export type TDataReadContextList = {
                attrValue?: string
headItemKey: string
                
            }
export type TDataReadNames = {
                attrValue?: string
headItemKey: string
                
            }
export type TDataGetCompany = {
                headItemKey: string
                
            }
export type TDataGetOperatingResults = {
                headItemKey: string
                
            }
export type TDataGetOperatingResultsByCode = {
                code: string
period?: string
year?: string
                
            }

export class SummaryService {

	/**
	 * XBRL文書情報を取得
	 * ## XBRL文書情報を取得するエンドポイント
 * - **機能**: 証券コードからXBRL文書情報を取得します。
 * - **認証不要**
 * - **レスポンス形式**: JSON
 * - **param1**: code: str 必須項目
	 * @returns IxDocumentInfoList Successful Response
	 * @throws ApiError
	 */
	public static getDocumentInfo(data: TDataGetDocumentInfo): CancelablePromise<IxDocumentInfoList> {
		const {
code,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/ix/summary/doc/info/{code}',
			path: {
				code
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * attr_valueと日本語ラベルを取得
	 * ## attr_valueと日本語ラベルを取得するエンドポイント
 * - **機能**: HeadItemKeyからattr_valueと日本語ラベルを取得します。
 * - **認証不要**
 * - **レスポンス形式**: JSON
 * - **param1**: head_item_key: str 必須項目
 * - **param2**: xbrl_type: str 必須項目
	 * @returns MenuLabelList Successful Response
	 * @throws ApiError
	 */
	public static readMenuLabels(data: TDataReadMenuLabels): CancelablePromise<MenuLabelList> {
		const {
headItemKey,
xbrlType,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/ix/summary/tree/menus/{head_item_key}',
			path: {
				head_item_key: headItemKey
			},
			query: {
				xbrl_type: xbrlType
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * 表示リンクアイテムを取得
	 * ## 表示リンクアイテムを取得するエンドポイント
 * - **機能**: HeadItemKeyから表示リンクのツリーアイテム一覧を取得します。
 * - **認証不要**
 * - **レスポンス形式**: JSON
 * - **param1**: head_item_key: str 必須項目
 * - **param2**: attr_value: str 任意項目
 * - **param3**: has_children: bool 任意項目
 * - **param4**: xlink_arcrole: str 任意項目
 * - **param5**: xbrl_type: str 任意項目
	 * @returns TreeItemsList Successful Response
	 * @throws ApiError
	 */
	public static readTreeItems(data: TDataReadTreeItems): CancelablePromise<TreeItemsList> {
		const {
attrValue,
hasChildren,
headItemKey,
xbrlType = 'sm',
xlinkArcrole,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/ix/summary/tree/items/{head_item_key}',
			path: {
				head_item_key: headItemKey
			},
			query: {
				attr_value: attrValue, has_children: hasChildren, xlink_arcrole: xlinkArcrole, xbrl_type: xbrlType
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * コンテキストリストを取得
	 * ## コンテキストリストを取得するエンドポイント
 * - **機能**: HeadItemKeyからコンテキストリストを取得します。
 * - **認証不要**
 * - **レスポンス形式**: JSON
 * - **param1**: head_item_key: str 必須項目
	 * @returns unknown Successful Response
	 * @throws ApiError
	 */
	public static readContextList(data: TDataReadContextList): CancelablePromise<Record<string, unknown>> {
		const {
attrValue,
headItemKey,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/ix/summary/tree/contexts/{head_item_key}',
			path: {
				head_item_key: headItemKey
			},
			query: {
				attr_value: attrValue
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * 名前リストを取得
	 * ## 名前リストを取得するエンドポイント
 * - **機能**: HeadItemKeyから名前リストを取得します。
 * - **認証不要**
 * - **レスポンス形式**: JSON
 * - **param1**: head_item_key: str 必須項目
	 * @returns unknown Successful Response
	 * @throws ApiError
	 */
	public static readNames(data: TDataReadNames): CancelablePromise<Record<string, unknown>> {
		const {
attrValue,
headItemKey,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/ix/summary/tree/names/{head_item_key}',
			path: {
				head_item_key: headItemKey
			},
			query: {
				attr_value: attrValue
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * 企業情報を取得
	 * ## 企業情報を取得するエンドポイント
 * - **機能**: HeadItemKeyから企業情報を取得します。
 * - **認証不要**
 * - **レスポンス形式**: JSON
 * - **param1**: HeadItemKey: str 必須項目
	 * @returns CompanySchema Successful Response
	 * @throws ApiError
	 */
	public static getCompany(data: TDataGetCompany): CancelablePromise<CompanySchema> {
		const {
headItemKey,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/ix/summary/Company/{HeadItemKey}',
			path: {
				HeadItemKey: headItemKey
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * 経営成績を取得
	 * ## 経営成績を取得するエンドポイント
 * - **機能**: HeadItemKeyから経営成績を取得します。
 * - **認証不要**
 * - **レスポンス形式**: JSON
 * - **param1**: HeadItemKey: str 必須項目
	 * @returns FinancialResponseSchema Successful Response
	 * @throws ApiError
	 */
	public static getOperatingResults(data: TDataGetOperatingResults): CancelablePromise<FinancialResponseSchema> {
		const {
headItemKey,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/ix/summary/summary/operatingResults/{HeadItemKey}',
			path: {
				HeadItemKey: headItemKey
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * 証券コードから経営成績を取得
	 * ## 証券コードから経営成績を取得するエンドポイント
 * - **機能**: 証券コードから経営成績を取得します。
 * - **認証不要**
 * - **レスポンス形式**: JSON
 * - **param1**: code: str 必須項目
 * - **param2**: year: str 任意項目
 * - **param3**: period: str 任意項目
	 * @returns FinancialResponseSchema Successful Response
	 * @throws ApiError
	 */
	public static getOperatingResultsByCode(data: TDataGetOperatingResultsByCode): CancelablePromise<FinancialResponseSchema> {
		const {
code,
period,
year,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/ix/summary/operatingResults/{code}',
			path: {
				code
			},
			query: {
				year, period
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

}

export type TDataCreateStockWikiItem = {
                requestBody: StockWikiCreate
                
            }
export type TDataGetStockWikiItem = {
                code: string
                
            }

export class WikiService {

	/**
	 * Get Stock Wiki Items
	 * Get all items.
	 * @returns StockWikisPublicList Successful Response
	 * @throws ApiError
	 */
	public static getStockWikiItems(): CancelablePromise<StockWikisPublicList> {
				return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/wiki/',
		});
	}

	/**
	 * Create Stock Wiki Item
	 * Create new item.
	 * @returns StockWikiCreate Successful Response
	 * @throws ApiError
	 */
	public static createStockWikiItem(data: TDataCreateStockWikiItem): CancelablePromise<StockWikiCreate> {
		const {
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'POST',
			url: '/api/v1/wiki/',
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Get Stock Wiki Item
	 * Get item.
	 * @returns StockWikiPublic Successful Response
	 * @throws ApiError
	 */
	public static getStockWikiItem(data: TDataGetStockWikiItem): CancelablePromise<StockWikiPublic> {
		const {
code,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/wiki/{code}',
			path: {
				code
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

export type TDataUpdateItem = {
                id: string
requestBody: ItemUpdate
                
            }
export type TDataDeleteItem = {
                id: string
                
            }

export class ItemsService {

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