// This file is auto-generated by @hey-api/openapi-ts

export type Body_login_login_access_token = {
    grant_type?: (string | null);
    username: string;
    password: string;
    scope?: string;
    client_id?: (string | null);
    client_secret?: (string | null);
};

export type DocumentListPublic = {
    id: number;
    securities_code: string;
    company_name: string;
    document_name: string;
};

export type DocumentListPublics = {
    count: number;
    data: Array<DocumentListPublic>;
};

export type FinForecastResponse = {
    count: number;
    labels: Array<LabelBase>;
    data: Array<FinForecastStruct>;
};

export type FinForecastStruct = {
    period?: (PeriodSchemaBase | null);
    upper?: (number | null);
    lower?: (number | null);
    forecast?: (FinItemsBase | null);
};

/**
 * メトリック情報のリストを表すクラス
 */
export type FinItemsBase = {
    is_active?: boolean;
    data?: (Array<FinValueAbstractBase> | null);
    context?: (string | null);
};

export type FinResponseBase = {
    count: number;
    labels: Array<LabelBase>;
    data: Array<FinStructBase>;
};

export type FinResultOnlyResponse = {
    count: number;
    labels: Array<LabelBase>;
    data: Array<FinResultOnlyStruct>;
};

export type FinResultOnlyStruct = {
    period?: (PeriodSchemaBase | null);
    result?: (FinItemsBase | null);
};

export type FinResultResponse = {
    count: number;
    labels: Array<LabelBase>;
    data: Array<FinResultStruct>;
};

export type FinResultStruct = {
    period?: (PeriodSchemaBase | null);
    upper?: (number | null);
    lower?: (number | null);
    result?: (FinItemsBase | null);
};

/**
 * ファイナンシャルレスポンス情報を表すクラス
 */
export type FinStructBase = {
    period?: (PeriodSchemaBase | null);
};

/**
 * メトリック親情報を表すクラス
 */
export type FinValueAbstractBase = {
    name: string;
    order: number;
    label: string;
    value?: (FinValueBase | null);
    change?: (FinValueBase | null);
};

/**
 * メトリック情報を表すクラス
 */
export type FinValueBase = {
    name: string;
    value: (number | null);
    unit: (string | null);
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

export type ItemCreate = {
    title: string;
    description?: (string | null);
};

export type ItemPublic = {
    title: string;
    description?: (string | null);
    id: string;
    owner_id: string;
};

export type ItemsPublic = {
    data: Array<ItemPublic>;
    count: number;
};

export type ItemUpdate = {
    title?: (string | null);
    description?: (string | null);
};

export type JpxStockInfoPublic = {
    input_date: string;
    code: string;
    name: string;
    market_or_type: string;
    industry_33_code: (number | null);
    industry_33_name: (string | null);
    industry_17_code: (number | null);
    industry_17_name: (string | null);
    scale_code: (number | null);
    scale_name: (string | null);
};

export type JpxStockInfosPublicList = {
    count: number;
    data: Array<JpxStockInfoPublic>;
};

export type LabelBase = {
    label: string;
};

export type Message = {
    message: string;
};

export type NewPassword = {
    token: string;
    new_password: string;
};

/**
 * 期間情報を表すクラス
 */
export type PeriodSchemaBase = {
    accountingStandard: string;
    fiscalYear: string;
    period: string;
};

/**
 * StockWikiCreate
 */
export type StockWikiCreate = {
    code: string;
    name: string;
    description: (string | null);
    url: (string | null);
};

/**
 * StockWikiPublic
 */
export type StockWikiPublic = {
    code: string;
    name: string;
    description: (string | null);
    url: (string | null);
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

export type UpdatePassword = {
    current_password: string;
    new_password: string;
};

export type UserCreate = {
    email: string;
    is_active?: boolean;
    is_superuser?: boolean;
    full_name?: (string | null);
    password: string;
};

export type UserPublic = {
    email: string;
    is_active?: boolean;
    is_superuser?: boolean;
    full_name?: (string | null);
    id: string;
};

export type UserRegister = {
    email: string;
    password: string;
    full_name?: (string | null);
};

export type UsersPublic = {
    data: Array<UserPublic>;
    count: number;
};

export type UserUpdate = {
    email?: (string | null);
    is_active?: boolean;
    is_superuser?: boolean;
    full_name?: (string | null);
    password?: (string | null);
};

export type UserUpdateMe = {
    full_name?: (string | null);
    email?: (string | null);
};

export type ValidationError = {
    loc: Array<(string | number)>;
    msg: string;
    type: string;
};

export type ItemsReadItemsData = {
    limit?: number;
    skip?: number;
};

export type ItemsReadItemsResponse = (ItemsPublic);

export type ItemsCreateItemData = {
    requestBody: ItemCreate;
};

export type ItemsCreateItemResponse = (ItemPublic);

export type ItemsReadItemData = {
    id: string;
};

export type ItemsReadItemResponse = (ItemPublic);

export type ItemsUpdateItemData = {
    id: string;
    requestBody: ItemUpdate;
};

export type ItemsUpdateItemResponse = (ItemPublic);

export type ItemsDeleteItemData = {
    id: string;
};

export type ItemsDeleteItemResponse = (Message);

export type IxGetDocumentCountData = {
    dateStr?: (string | null);
};

export type IxGetDocumentCountResponse = (number);

export type IxGetLatestDocumentTitleResponse = (string);

export type IxGetDocumentListData = {
    dateStr?: (string | null);
    limit?: (number | null);
    page?: (number | null);
};

export type IxGetDocumentListResponse = (DocumentListPublics);

export type JpxReadJpxStockInfoItemData = {
    code: string;
};

export type JpxReadJpxStockInfoItemResponse = (JpxStockInfoPublic);

export type JpxReadJpxStockInfoItemsResponse = (JpxStockInfosPublicList);

export type JpxReadJpxStockInfoItemsTcsData = {
    industry17Code?: (number | null);
    industry33Code?: (Array<(number)> | null);
    isItems?: boolean;
    limit?: number;
};

export type JpxReadJpxStockInfoItemsTcsResponse = (JpxStockInfosPublicList);

export type JpxReadJpxStockInfoItemTcsData = {
    market: string;
};

export type JpxReadJpxStockInfoItemTcsResponse = (JpxStockInfosPublicList);

export type JpxReadJpxStockInfoIndustryNamesData = {
    type: number;
};

export type JpxReadJpxStockInfoIndustryNamesResponse = (IndustriesList);

export type JpxReadSelectIndustriesData = {
    industry17Code?: (number | null);
};

export type JpxReadSelectIndustriesResponse = (IndustriesList);

export type LoginLoginAccessTokenData = {
    formData: Body_login_login_access_token;
};

export type LoginLoginAccessTokenResponse = (Token);

export type LoginTestTokenResponse = (UserPublic);

export type LoginRecoverPasswordData = {
    email: string;
};

export type LoginRecoverPasswordResponse = (Message);

export type LoginResetPasswordData = {
    requestBody: NewPassword;
};

export type LoginResetPasswordResponse = (Message);

export type LoginRecoverPasswordHtmlContentData = {
    email: string;
};

export type LoginRecoverPasswordHtmlContentResponse = (string);

export type SummaryGetOperatingResultsData = {
    code: string;
};

export type SummaryGetOperatingResultsResponse = (FinResultResponse);

export type SummaryGetOtherOperatingResultsData = {
    code: string;
};

export type SummaryGetOtherOperatingResultsResponse = (FinResultResponse);

export type SummaryGetForecastsData = {
    code: string;
};

export type SummaryGetForecastsResponse = (FinForecastResponse);

export type SummaryGetFinancialPositionData = {
    code: string;
};

export type SummaryGetFinancialPositionResponse = (FinResultOnlyResponse);

export type SummaryGetCashFlowsData = {
    code: string;
};

export type SummaryGetCashFlowsResponse = (FinResultOnlyResponse);

export type SummaryGetDividendsData = {
    code: string;
};

export type SummaryGetDividendsResponse = (FinResponseBase);

export type UsersReadUsersData = {
    limit?: number;
    skip?: number;
};

export type UsersReadUsersResponse = (UsersPublic);

export type UsersCreateUserData = {
    requestBody: UserCreate;
};

export type UsersCreateUserResponse = (UserPublic);

export type UsersReadUserMeResponse = (UserPublic);

export type UsersDeleteUserMeResponse = (Message);

export type UsersUpdateUserMeData = {
    requestBody: UserUpdateMe;
};

export type UsersUpdateUserMeResponse = (UserPublic);

export type UsersUpdatePasswordMeData = {
    requestBody: UpdatePassword;
};

export type UsersUpdatePasswordMeResponse = (Message);

export type UsersRegisterUserData = {
    requestBody: UserRegister;
};

export type UsersRegisterUserResponse = (UserPublic);

export type UsersReadUserByIdData = {
    userId: string;
};

export type UsersReadUserByIdResponse = (UserPublic);

export type UsersUpdateUserData = {
    requestBody: UserUpdate;
    userId: string;
};

export type UsersUpdateUserResponse = (UserPublic);

export type UsersDeleteUserData = {
    userId: string;
};

export type UsersDeleteUserResponse = (Message);

export type UtilsTestEmailData = {
    emailTo: string;
};

export type UtilsTestEmailResponse = (Message);

export type UtilsHealthCheckResponse = (boolean);

export type WikiGetStockWikiItemsResponse = (StockWikisPublicList);

export type WikiCreateStockWikiItemData = {
    requestBody: StockWikiCreate;
};

export type WikiCreateStockWikiItemResponse = (StockWikiCreate);

export type WikiGetStockWikiItemData = {
    code: string;
};

export type WikiGetStockWikiItemResponse = (StockWikiPublic);