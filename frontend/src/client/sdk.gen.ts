// This file is auto-generated by @hey-api/openapi-ts

import type { CancelablePromise } from './core/CancelablePromise';
import { OpenAPI } from './core/OpenAPI';
import { request as __request } from './core/request';
import type { ItemsReadItemsData, ItemsReadItemsResponse, ItemsCreateItemData, ItemsCreateItemResponse, ItemsReadItemData, ItemsReadItemResponse, ItemsUpdateItemData, ItemsUpdateItemResponse, ItemsDeleteItemData, ItemsDeleteItemResponse, IxGetDocumentCountData, IxGetDocumentCountResponse, IxGetLatestDocumentTitleResponse, IxGetDocumentListData, IxGetDocumentListResponse, JpxReadJpxStockInfoItemData, JpxReadJpxStockInfoItemResponse, JpxReadJpxStockInfoItemsResponse, JpxReadJpxStockInfoItemsTcsData, JpxReadJpxStockInfoItemsTcsResponse, JpxReadJpxStockInfoItemTcsData, JpxReadJpxStockInfoItemTcsResponse, JpxReadJpxStockInfoIndustryNamesData, JpxReadJpxStockInfoIndustryNamesResponse, JpxReadSelectIndustriesData, JpxReadSelectIndustriesResponse, LoginLoginAccessTokenData, LoginLoginAccessTokenResponse, LoginTestTokenResponse, LoginRecoverPasswordData, LoginRecoverPasswordResponse, LoginResetPasswordData, LoginResetPasswordResponse, LoginRecoverPasswordHtmlContentData, LoginRecoverPasswordHtmlContentResponse, SummaryGetOperatingResultsData, SummaryGetOperatingResultsResponse, SummaryGetOtherOperatingResultsData, SummaryGetOtherOperatingResultsResponse, SummaryGetForecastsData, SummaryGetForecastsResponse, SummaryGetFinancialPositionData, SummaryGetFinancialPositionResponse, SummaryGetCashFlowsData, SummaryGetCashFlowsResponse, SummaryGetDividendsData, SummaryGetDividendsResponse, SummaryGetForecastProgressRateData, SummaryGetForecastProgressRateResponse, UsersReadUsersData, UsersReadUsersResponse, UsersCreateUserData, UsersCreateUserResponse, UsersReadUserMeResponse, UsersDeleteUserMeResponse, UsersUpdateUserMeData, UsersUpdateUserMeResponse, UsersUpdatePasswordMeData, UsersUpdatePasswordMeResponse, UsersRegisterUserData, UsersRegisterUserResponse, UsersReadUserByIdData, UsersReadUserByIdResponse, UsersUpdateUserData, UsersUpdateUserResponse, UsersDeleteUserData, UsersDeleteUserResponse, UtilsTestEmailData, UtilsTestEmailResponse, UtilsHealthCheckResponse, WikiGetStockWikiItemsResponse, WikiCreateStockWikiItemData, WikiCreateStockWikiItemResponse, WikiGetStockWikiItemData, WikiGetStockWikiItemResponse, XbrlIxHeadIsIxHeadTitleItemActiveData, XbrlIxHeadIsIxHeadTitleItemActiveResponse, XbrlIxHeadReadIxHeadTitleItemData, XbrlIxHeadReadIxHeadTitleItemResponse, XbrlIxHeadReadIxHeadTitleItemsResponse, XbrlIxHeadReadIxHeadTitleItemsUrlListResponse } from './types.gen';

export class ItemsService {
    /**
     * Read Items
     * Retrieve items.
     * @param data The data for the request.
     * @param data.skip
     * @param data.limit
     * @returns ItemsPublic Successful Response
     * @throws ApiError
     */
    public static readItems(data: ItemsReadItemsData = {}): CancelablePromise<ItemsReadItemsResponse> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/items/',
            query: {
                skip: data.skip,
                limit: data.limit
            },
            errors: {
                422: 'Validation Error'
            }
        });
    }
    
    /**
     * Create Item
     * Create new item.
     * @param data The data for the request.
     * @param data.requestBody
     * @returns ItemPublic Successful Response
     * @throws ApiError
     */
    public static createItem(data: ItemsCreateItemData): CancelablePromise<ItemsCreateItemResponse> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/v1/items/',
            body: data.requestBody,
            mediaType: 'application/json',
            errors: {
                422: 'Validation Error'
            }
        });
    }
    
    /**
     * Read Item
     * Get item by ID.
     * @param data The data for the request.
     * @param data.id
     * @returns ItemPublic Successful Response
     * @throws ApiError
     */
    public static readItem(data: ItemsReadItemData): CancelablePromise<ItemsReadItemResponse> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/items/{id}',
            path: {
                id: data.id
            },
            errors: {
                422: 'Validation Error'
            }
        });
    }
    
    /**
     * Update Item
     * Update an item.
     * @param data The data for the request.
     * @param data.id
     * @param data.requestBody
     * @returns ItemPublic Successful Response
     * @throws ApiError
     */
    public static updateItem(data: ItemsUpdateItemData): CancelablePromise<ItemsUpdateItemResponse> {
        return __request(OpenAPI, {
            method: 'PUT',
            url: '/api/v1/items/{id}',
            path: {
                id: data.id
            },
            body: data.requestBody,
            mediaType: 'application/json',
            errors: {
                422: 'Validation Error'
            }
        });
    }
    
    /**
     * Delete Item
     * Delete an item.
     * @param data The data for the request.
     * @param data.id
     * @returns Message Successful Response
     * @throws ApiError
     */
    public static deleteItem(data: ItemsDeleteItemData): CancelablePromise<ItemsDeleteItemResponse> {
        return __request(OpenAPI, {
            method: 'DELETE',
            url: '/api/v1/items/{id}',
            path: {
                id: data.id
            },
            errors: {
                422: 'Validation Error'
            }
        });
    }
    
}

export class IxService {
    /**
     * XBRL文書数を取得
     * @param data The data for the request.
     * @param data.dateStr
     * @returns number Successful Response
     * @throws ApiError
     */
    public static getDocumentCount(data: IxGetDocumentCountData = {}): CancelablePromise<IxGetDocumentCountResponse> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/ix/stock_info/document/count',
            query: {
                date_str: data.dateStr
            },
            errors: {
                422: 'Validation Error'
            }
        });
    }
    
    /**
     * 最新XBRL文書のタイトルを取得
     * @returns string Successful Response
     * @throws ApiError
     */
    public static getLatestDocumentTitle(): CancelablePromise<IxGetLatestDocumentTitleResponse> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/ix/stock_info/document/latest/title'
        });
    }
    
    /**
     * XBRL文書のリストを取得
     * @param data The data for the request.
     * @param data.reportTypes
     * @param data.dateStr
     * @param data.limit
     * @param data.page
     * @returns DocumentListPublics Successful Response
     * @throws ApiError
     */
    public static getDocumentList(data: IxGetDocumentListData = {}): CancelablePromise<IxGetDocumentListResponse> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/ix/stock_info/document/list',
            query: {
                report_types: data.reportTypes,
                date_str: data.dateStr,
                limit: data.limit,
                page: data.page
            },
            errors: {
                422: 'Validation Error'
            }
        });
    }
    
}

export class JpxService {
    /**
     * Read Jpx Stock Info Item
     * Get item by code.
     * @param data The data for the request.
     * @param data.code
     * @returns JpxStockInfoPublic Successful Response
     * @throws ApiError
     */
    public static readJpxStockInfoItem(data: JpxReadJpxStockInfoItemData): CancelablePromise<JpxReadJpxStockInfoItemResponse> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/jpx/stock_info/code/{code}',
            path: {
                code: data.code
            },
            errors: {
                422: 'Validation Error'
            }
        });
    }
    
    /**
     * Read Jpx Stock Info Items
     * Get all items.
     * @returns JpxStockInfosPublicList Successful Response
     * @throws ApiError
     */
    public static readJpxStockInfoItems(): CancelablePromise<JpxReadJpxStockInfoItemsResponse> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/jpx/stock_info/'
        });
    }
    
    /**
     * Read Jpx Stock Info Items Tcs
     * Get all items.
     * @param data The data for the request.
     * @param data.industry17Code
     * @param data.industry33Code
     * @param data.isItems
     * @param data.limit
     * @returns JpxStockInfosPublicList Successful Response
     * @throws ApiError
     */
    public static readJpxStockInfoItemsTcs(data: JpxReadJpxStockInfoItemsTcsData = {}): CancelablePromise<JpxReadJpxStockInfoItemsTcsResponse> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/jpx/stock_info/tcs',
            query: {
                industry_17_code: data.industry17Code,
                industry_33_code: data.industry33Code,
                isItems: data.isItems,
                limit: data.limit
            },
            errors: {
                422: 'Validation Error'
            }
        });
    }
    
    /**
     * Read Jpx Stock Info Item Tcs
     * Get item by market.
     * @param data The data for the request.
     * @param data.market
     * @returns JpxStockInfosPublicList Successful Response
     * @throws ApiError
     */
    public static readJpxStockInfoItemTcs(data: JpxReadJpxStockInfoItemTcsData): CancelablePromise<JpxReadJpxStockInfoItemTcsResponse> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/jpx/stock_info/tcs/{market}',
            path: {
                market: data.market
            },
            errors: {
                422: 'Validation Error'
            }
        });
    }
    
    /**
     * Read Jpx Stock Info Industry Names
     * Get all industries.
     * @param data The data for the request.
     * @param data.type
     * @returns IndustriesList Successful Response
     * @throws ApiError
     */
    public static readJpxStockInfoIndustryNames(data: JpxReadJpxStockInfoIndustryNamesData): CancelablePromise<JpxReadJpxStockInfoIndustryNamesResponse> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/jpx/stock_info/industries/{type}',
            path: {
                type: data.type
            },
            errors: {
                422: 'Validation Error'
            }
        });
    }
    
    /**
     * Read Select Industries
     * Get all industries.
     * @param data The data for the request.
     * @param data.industry17Code
     * @returns IndustriesList Successful Response
     * @throws ApiError
     */
    public static readSelectIndustries(data: JpxReadSelectIndustriesData = {}): CancelablePromise<JpxReadSelectIndustriesResponse> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/jpx/stock_info/industries',
            query: {
                industry_17_code: data.industry17Code
            },
            errors: {
                422: 'Validation Error'
            }
        });
    }
    
}

export class LoginService {
    /**
     * Login Access Token
     * OAuth2 compatible token login, get an access token for future requests
     * @param data The data for the request.
     * @param data.formData
     * @returns Token Successful Response
     * @throws ApiError
     */
    public static loginAccessToken(data: LoginLoginAccessTokenData): CancelablePromise<LoginLoginAccessTokenResponse> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/v1/login/access-token',
            formData: data.formData,
            mediaType: 'application/x-www-form-urlencoded',
            errors: {
                422: 'Validation Error'
            }
        });
    }
    
    /**
     * Test Token
     * Test access token
     * @returns UserPublic Successful Response
     * @throws ApiError
     */
    public static testToken(): CancelablePromise<LoginTestTokenResponse> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/v1/login/test-token'
        });
    }
    
    /**
     * Recover Password
     * Password Recovery
     * @param data The data for the request.
     * @param data.email
     * @returns Message Successful Response
     * @throws ApiError
     */
    public static recoverPassword(data: LoginRecoverPasswordData): CancelablePromise<LoginRecoverPasswordResponse> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/v1/password-recovery/{email}',
            path: {
                email: data.email
            },
            errors: {
                422: 'Validation Error'
            }
        });
    }
    
    /**
     * Reset Password
     * Reset password
     * @param data The data for the request.
     * @param data.requestBody
     * @returns Message Successful Response
     * @throws ApiError
     */
    public static resetPassword(data: LoginResetPasswordData): CancelablePromise<LoginResetPasswordResponse> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/v1/reset-password/',
            body: data.requestBody,
            mediaType: 'application/json',
            errors: {
                422: 'Validation Error'
            }
        });
    }
    
    /**
     * Recover Password Html Content
     * HTML Content for Password Recovery
     * @param data The data for the request.
     * @param data.email
     * @returns string Successful Response
     * @throws ApiError
     */
    public static recoverPasswordHtmlContent(data: LoginRecoverPasswordHtmlContentData): CancelablePromise<LoginRecoverPasswordHtmlContentResponse> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/v1/password-recovery-html-content/{email}',
            path: {
                email: data.email
            },
            errors: {
                422: 'Validation Error'
            }
        });
    }
    
}

export class SummaryService {
    /**
     * 経営成績情報を取得
     * @param data The data for the request.
     * @param data.code 銘柄コード
     * @param data.headItemKey head_item_key
     * @returns FinResultResponse Successful Response
     * @throws ApiError
     */
    public static getOperatingResults(data: SummaryGetOperatingResultsData = {}): CancelablePromise<SummaryGetOperatingResultsResponse> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/ix/summary/operating_results/income/',
            query: {
                code: data.code,
                head_item_key: data.headItemKey
            },
            errors: {
                422: 'Validation Error'
            }
        });
    }
    
    /**
     * その他の経営成績情報を取得
     * @param data The data for the request.
     * @param data.code
     * @returns FinResultResponse Successful Response
     * @throws ApiError
     */
    public static getOtherOperatingResults(data: SummaryGetOtherOperatingResultsData): CancelablePromise<SummaryGetOtherOperatingResultsResponse> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/ix/summary/operating_results/other/{}',
            query: {
                code: data.code
            },
            errors: {
                422: 'Validation Error'
            }
        });
    }
    
    /**
     * 予測情報を取得
     * @param data The data for the request.
     * @param data.code 銘柄コード
     * @param data.headItemKey head_item_key
     * @returns FinForecastResponse Successful Response
     * @throws ApiError
     */
    public static getForecasts(data: SummaryGetForecastsData = {}): CancelablePromise<SummaryGetForecastsResponse> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/ix/summary/forecasts/',
            query: {
                code: data.code,
                head_item_key: data.headItemKey
            },
            errors: {
                422: 'Validation Error'
            }
        });
    }
    
    /**
     * 財政状態情報を取得
     * @param data The data for the request.
     * @param data.code
     * @returns FinResultOnlyResponse Successful Response
     * @throws ApiError
     */
    public static getFinancialPosition(data: SummaryGetFinancialPositionData): CancelablePromise<SummaryGetFinancialPositionResponse> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/ix/summary/financial_position/{code}',
            path: {
                code: data.code
            },
            errors: {
                422: 'Validation Error'
            }
        });
    }
    
    /**
     * キャッシュフロー情報を取得
     * @param data The data for the request.
     * @param data.code
     * @returns FinResultOnlyResponse Successful Response
     * @throws ApiError
     */
    public static getCashFlows(data: SummaryGetCashFlowsData): CancelablePromise<SummaryGetCashFlowsResponse> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/ix/summary/cash_flows/{code}',
            path: {
                code: data.code
            },
            errors: {
                422: 'Validation Error'
            }
        });
    }
    
    /**
     * 配当情報を取得
     * @param data The data for the request.
     * @param data.code
     * @returns FinResponseBase Successful Response
     * @throws ApiError
     */
    public static getDividends(data: SummaryGetDividendsData): CancelablePromise<SummaryGetDividendsResponse> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/ix/summary/dividends/{code}',
            path: {
                code: data.code
            },
            errors: {
                422: 'Validation Error'
            }
        });
    }
    
    /**
     * 予測進捗率情報を取得
     * @param data The data for the request.
     * @param data.headItemKey
     * @param data.operatingResultLate
     * @returns unknown Successful Response
     * @throws ApiError
     */
    public static getForecastProgressRate(data: SummaryGetForecastProgressRateData): CancelablePromise<SummaryGetForecastProgressRateResponse> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/ix/summary/forecast_progress_rate/{head_item_key}',
            path: {
                head_item_key: data.headItemKey
            },
            query: {
                operating_result_late: data.operatingResultLate
            },
            errors: {
                422: 'Validation Error'
            }
        });
    }
    
}

export class UsersService {
    /**
     * Read Users
     * Retrieve users.
     * @param data The data for the request.
     * @param data.skip
     * @param data.limit
     * @returns UsersPublic Successful Response
     * @throws ApiError
     */
    public static readUsers(data: UsersReadUsersData = {}): CancelablePromise<UsersReadUsersResponse> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/users/',
            query: {
                skip: data.skip,
                limit: data.limit
            },
            errors: {
                422: 'Validation Error'
            }
        });
    }
    
    /**
     * Create User
     * Create new user.
     * @param data The data for the request.
     * @param data.requestBody
     * @returns UserPublic Successful Response
     * @throws ApiError
     */
    public static createUser(data: UsersCreateUserData): CancelablePromise<UsersCreateUserResponse> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/v1/users/',
            body: data.requestBody,
            mediaType: 'application/json',
            errors: {
                422: 'Validation Error'
            }
        });
    }
    
    /**
     * Read User Me
     * Get current user.
     * @returns UserPublic Successful Response
     * @throws ApiError
     */
    public static readUserMe(): CancelablePromise<UsersReadUserMeResponse> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/users/me'
        });
    }
    
    /**
     * Delete User Me
     * Delete own user.
     * @returns Message Successful Response
     * @throws ApiError
     */
    public static deleteUserMe(): CancelablePromise<UsersDeleteUserMeResponse> {
        return __request(OpenAPI, {
            method: 'DELETE',
            url: '/api/v1/users/me'
        });
    }
    
    /**
     * Update User Me
     * Update own user.
     * @param data The data for the request.
     * @param data.requestBody
     * @returns UserPublic Successful Response
     * @throws ApiError
     */
    public static updateUserMe(data: UsersUpdateUserMeData): CancelablePromise<UsersUpdateUserMeResponse> {
        return __request(OpenAPI, {
            method: 'PATCH',
            url: '/api/v1/users/me',
            body: data.requestBody,
            mediaType: 'application/json',
            errors: {
                422: 'Validation Error'
            }
        });
    }
    
    /**
     * Update Password Me
     * Update own password.
     * @param data The data for the request.
     * @param data.requestBody
     * @returns Message Successful Response
     * @throws ApiError
     */
    public static updatePasswordMe(data: UsersUpdatePasswordMeData): CancelablePromise<UsersUpdatePasswordMeResponse> {
        return __request(OpenAPI, {
            method: 'PATCH',
            url: '/api/v1/users/me/password',
            body: data.requestBody,
            mediaType: 'application/json',
            errors: {
                422: 'Validation Error'
            }
        });
    }
    
    /**
     * Register User
     * Create new user without the need to be logged in.
     * @param data The data for the request.
     * @param data.requestBody
     * @returns UserPublic Successful Response
     * @throws ApiError
     */
    public static registerUser(data: UsersRegisterUserData): CancelablePromise<UsersRegisterUserResponse> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/v1/users/signup',
            body: data.requestBody,
            mediaType: 'application/json',
            errors: {
                422: 'Validation Error'
            }
        });
    }
    
    /**
     * Read User By Id
     * Get a specific user by id.
     * @param data The data for the request.
     * @param data.userId
     * @returns UserPublic Successful Response
     * @throws ApiError
     */
    public static readUserById(data: UsersReadUserByIdData): CancelablePromise<UsersReadUserByIdResponse> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/users/{user_id}',
            path: {
                user_id: data.userId
            },
            errors: {
                422: 'Validation Error'
            }
        });
    }
    
    /**
     * Update User
     * Update a user.
     * @param data The data for the request.
     * @param data.userId
     * @param data.requestBody
     * @returns UserPublic Successful Response
     * @throws ApiError
     */
    public static updateUser(data: UsersUpdateUserData): CancelablePromise<UsersUpdateUserResponse> {
        return __request(OpenAPI, {
            method: 'PATCH',
            url: '/api/v1/users/{user_id}',
            path: {
                user_id: data.userId
            },
            body: data.requestBody,
            mediaType: 'application/json',
            errors: {
                422: 'Validation Error'
            }
        });
    }
    
    /**
     * Delete User
     * Delete a user.
     * @param data The data for the request.
     * @param data.userId
     * @returns Message Successful Response
     * @throws ApiError
     */
    public static deleteUser(data: UsersDeleteUserData): CancelablePromise<UsersDeleteUserResponse> {
        return __request(OpenAPI, {
            method: 'DELETE',
            url: '/api/v1/users/{user_id}',
            path: {
                user_id: data.userId
            },
            errors: {
                422: 'Validation Error'
            }
        });
    }
    
}

export class UtilsService {
    /**
     * Test Email
     * Test emails.
     * @param data The data for the request.
     * @param data.emailTo
     * @returns Message Successful Response
     * @throws ApiError
     */
    public static testEmail(data: UtilsTestEmailData): CancelablePromise<UtilsTestEmailResponse> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/v1/utils/test-email/',
            query: {
                email_to: data.emailTo
            },
            errors: {
                422: 'Validation Error'
            }
        });
    }
    
    /**
     * Health Check
     * @returns boolean Successful Response
     * @throws ApiError
     */
    public static healthCheck(): CancelablePromise<UtilsHealthCheckResponse> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/utils/health-check/'
        });
    }
    
}

export class WikiService {
    /**
     * Get Stock Wiki Items
     * Get all items.
     * @returns StockWikisPublicList Successful Response
     * @throws ApiError
     */
    public static getStockWikiItems(): CancelablePromise<WikiGetStockWikiItemsResponse> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/wiki/'
        });
    }
    
    /**
     * Create Stock Wiki Item
     * Create new item.
     * @param data The data for the request.
     * @param data.requestBody
     * @returns StockWikiCreate Successful Response
     * @throws ApiError
     */
    public static createStockWikiItem(data: WikiCreateStockWikiItemData): CancelablePromise<WikiCreateStockWikiItemResponse> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/v1/wiki/',
            body: data.requestBody,
            mediaType: 'application/json',
            errors: {
                422: 'Validation Error'
            }
        });
    }
    
    /**
     * Get Stock Wiki Item
     * Get item.
     * @param data The data for the request.
     * @param data.code
     * @returns StockWikiPublic Successful Response
     * @throws ApiError
     */
    public static getStockWikiItem(data: WikiGetStockWikiItemData): CancelablePromise<WikiGetStockWikiItemResponse> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/wiki/{code}',
            path: {
                code: data.code
            },
            errors: {
                422: 'Validation Error'
            }
        });
    }
    
}

export class XbrlIxHeadService {
    /**
     * Is Ix Head Title Item Active
     * Check if item is active.
     * @param data The data for the request.
     * @param data.headItemKey
     * @returns boolean Successful Response
     * @throws ApiError
     */
    public static isIxHeadTitleItemActive(data: XbrlIxHeadIsIxHeadTitleItemActiveData): CancelablePromise<XbrlIxHeadIsIxHeadTitleItemActiveResponse> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/xbrl/ix/head/is_active/',
            query: {
                head_item_key: data.headItemKey
            },
            errors: {
                422: 'Validation Error'
            }
        });
    }
    
    /**
     * Read Ix Head Title Item
     * Get item by head_item_key.
     * @param data The data for the request.
     * @param data.headItemKey
     * @returns IxHeadTitlePublic Successful Response
     * @throws ApiError
     */
    public static readIxHeadTitleItem(data: XbrlIxHeadReadIxHeadTitleItemData): CancelablePromise<XbrlIxHeadReadIxHeadTitleItemResponse> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/xbrl/ix/head/',
            query: {
                head_item_key: data.headItemKey
            },
            errors: {
                422: 'Validation Error'
            }
        });
    }
    
    /**
     * XBRL文書のリストを取得
     * Get items.
     * @returns IxHeadTitlesPublic Successful Response
     * @throws ApiError
     */
    public static readIxHeadTitleItems(): CancelablePromise<XbrlIxHeadReadIxHeadTitleItemsResponse> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/xbrl/ix/head/list/'
        });
    }
    
    /**
     * Read Ix Head Title Items Url List
     * Get items.
     * @returns UrlSchemaList Successful Response
     * @throws ApiError
     */
    public static readIxHeadTitleItemsUrlList(): CancelablePromise<XbrlIxHeadReadIxHeadTitleItemsUrlListResponse> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/xbrl/url_list/'
        });
    }
    
}