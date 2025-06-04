from fastapi import APIRouter, HTTPException, Query

from app.api.deps import SessionDep

from . import crud, utils
from . import schema as sc
from .exceptions import HeadItemNotFound, NotDictKeyError

router = APIRouter()


@router.get(
    "/disclosure_items/",
    summary="開示項目情報を取得",
    response_model=sc.DisclosureItemsList,
)
def get_disclosure_items(
    *,
    session: SessionDep,
    report_types: list[str] | None = Query(
        ["edif", "edus", "edjp"],
        description="取得する開示項目のレポートタイプ",
        example=["edif", "edus", "edjp"],
    ),
    limit: int = Query(20, description="取得する開示項目の最大数"),
    offset: int = Query(0, description="オフセット"),
) -> sc.DisclosureItemsList:
    """
    開示項目情報を取得するエンドポイント。
    Args:
        session (SessionDep): データベースセッション依存性。
        report_types (list[str] | None, optional): 取得する開示項目のレポートタイプ。デフォルトは["edif", "edus", "edjp"]。
        limit (int, optional): 取得する開示項目の最大数。デフォルトは20。
        offset (int, optional): オフセット値。デフォルトは0。
    Raises:
        HTTPException: パラメータ不正やデータが見つからない場合に発生。
    Returns:
        sc.DisclosureItemsList: 開示項目のリストとメタデータを含むレスポンスモデル。
    """
    items = crud.get_disclosure_items(
        session=session,
        report_types=report_types,
        limit=limit,
        offset=offset,
    )
    if not items:
        raise HTTPException(
            status_code=404,
            detail="開示項目が見つかりません。",
        )

    item_list = []

    for item in items:
        try:
            item_list.append(
                sc.DisclosureItem(
                    id=item.id,
                    company=item.company_name,
                    code=item.securities_code,
                    date=item.insert_date.strftime("%Y-%m-%d %H:%M:%S"),
                    title=item.document_name,
                    category=item.report_type,
                    summary=get_financial_summary(
                        session=session, head_item_key=item.item_key, offset=0
                    ),
                    important=True,
                )
            )
        except Exception:
            print(item.id)
            continue
    return sc.DisclosureItemsList(
        count=len(item_list), data=item_list, offset=offset + limit
    )


@router.get("/financial_summary/", summary="財務サマリー情報を取得")
def get_financial_summary(
    *,
    session: SessionDep,
    code: str | None = Query(None, description="銘柄コード"),
    head_item_key: str | None = Query(None, description="head_item_key"),
    report_types: list[str] | None = Query(None, description="レポートタイプ"),
    offset: int = Query(0, description="オフセット"),
) -> str:
    """
    財務サマリー情報を取得するエンドポイント。

    Args:
        session (SessionDep): データベースセッション依存性。
        code (str | None, optional): 銘柄コード。指定しない場合はhead_item_keyを利用。
        head_item_key (str | None, optional): ヘッドアイテムキー。指定しない場合はcodeを利用。
        report_types (list[str] | None, optional): レポートタイプのリスト。
        offset (int, optional): オフセット値。デフォルトは0。

    Raises:
        HTTPException: パラメータ不正やデータが見つからない場合に発生。

    Returns:
        str: 財務サマリー情報の文字列。
    """
    ope = get_operating_results(
        session=session,
        code=code,
        head_item_key=head_item_key,
        report_types=report_types,
        offset=offset,
    )

    titles = utils.generate_summary_sentence(ope)

    if not titles:
        raise HTTPException(
            status_code=404,
            detail="指定された銘柄コードまたはhead_item_keyに対応するタイトル情報が見つかりません。",
        )

    return titles


@router.get(
    "/operating_results/income/",
    summary="経営成績情報を取得",
    response_model=sc.FinItemsResponse,
)
def get_operating_results(
    *,
    session: SessionDep,
    code: str | None = Query(None, description="銘柄コード"),
    head_item_key: str | None = Query(None, description="head_item_key"),
    report_types: list[str] | None = Query(None, description="レポートタイプ"),
    offset: int = Query(0, description="オフセット"),
) -> sc.FinItemsResponse:
    """
    経営成績情報を取得するエンドポイント。

    Args:
        session (SessionDep): データベースセッション依存性。
        code (str | None, optional): 銘柄コード。指定しない場合はhead_item_keyを利用。
        head_item_key (str | None, optional): ヘッドアイテムキー。指定しない場合はcodeを利用。
        report_types (list[str] | None, optional): レポートタイプのリスト。
        offset (int, optional): オフセット値。デフォルトは0。

    Raises:
        HTTPException: パラメータ不正やデータが見つからない場合に発生。

    Returns:
        sc.FinItemsResponse: 経営成績情報のレスポンスモデル。
    """
    if code is None and head_item_key is None:
        raise HTTPException(
            status_code=404,
            detail="銘柄コードかhead_item_keyどちらかを指定してください",
        )

    attr_value_dict = {  # この辞書は、attr_valueとfrom_nameの対応を表しています。
        "FY": "BusinessResultsOperatingResults",
        "QU": "BusinessResultsQuarterlyOperatingResults",
    }

    from_names = [
        "tse-ed-t_ConsolidatedIncomeStatementsInformationAbstract",
        "tse-ed-t_IncomeStatementsInformationAbstract",
    ]

    # head_item_keyを取得
    try:
        head_item_key = utils.get_head_item_key(
            session=session,
            head_item_key=head_item_key,
            code=code,
            report_types=report_types,
            offset=offset,
        )
    except HeadItemNotFound as e:
        raise HTTPException(status_code=404, detail=str(e))

    try:
        item = utils.get_summary_items(
            session=session,
            head_item_key=head_item_key,
            attr_value_dict=attr_value_dict,
            from_names=from_names,
            is_change=True,
        )
    except NotDictKeyError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except HeadItemNotFound as e:
        raise HTTPException(status_code=404, detail=str(e))

    result = utils.get_struct(
        items=item,
        struct=sc.FinItemsResponse(),
    )

    return result


@router.get("/operating_results/other/{}", summary="その他の経営成績情報を取得")
def get_other_operating_results(
    *,
    session: SessionDep,
    code: str | None = Query(None, description="銘柄コード"),
    head_item_key: str | None = Query(None, description="head_item_key"),
    report_types: list[str] | None = Query(None, description="レポートタイプ"),
    offset: int = Query(0, description="オフセット"),
) -> sc.FinItemsResponse:
    """
    その他の経営成績情報を取得するエンドポイント。
    Args:
        session (SessionDep): データベースセッション依存性。
        code (str | None, optional): 銘柄コード。指定しない場合はhead_item_keyを利用。
        head_item_key (str | None, optional): ヘッドアイテムキー。指定しない場合はcodeを利用。
        report_types (list[str] | None, optional): レポートタイプのリスト。
        offset (int, optional): オフセット値。デフォルトは0。
    Raises:
        HTTPException: パラメータ不正やデータが見つからない場合に発生。
    Returns:
        sc.FinItemsResponse: その他の経営成績情報のレスポンスモデル。
    """
    if code and head_item_key:
        raise HTTPException(
            status_code=404,
            detail="銘柄コードかhead_item_keyどちらかを指定してください",
        )

    attr_value_dict = {
        "FY": "BusinessResultsOperatingResults",
        "QU": "BusinessResultsQuarterlyOperatingResults",
    }

    from_names = [
        "tse-ed-t_OtherConsolidatedOperatingResultsAbstract",
        "tse-ed-t_OtherOperatingResultsAbstract",
    ]

    # head_item_keyを取得
    try:
        head_item_key = utils.get_head_item_key(
            session=session,
            head_item_key=head_item_key,
            code=code,
            report_types=report_types,
            offset=offset,
        )
    except HeadItemNotFound as e:
        raise HTTPException(status_code=404, detail=str(e))

    try:
        item = utils.get_summary_items(
            session=session,
            head_item_key=head_item_key,
            attr_value_dict=attr_value_dict,
            from_names=from_names,
            is_change=False,
        )
    except NotDictKeyError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except HeadItemNotFound as e:
        raise HTTPException(status_code=404, detail=str(e))

    result = utils.get_struct(
        items=item,
        struct=sc.FinItemsResponse(),
    )

    return result


@router.get("/forecasts/", summary="予測情報を取得")
def get_forecasts(
    *,
    session: SessionDep,
    code: str | None = Query(None, description="銘柄コード"),
    head_item_key: str | None = Query(None, description="head_item_key"),
    report_types: list[str] | None = Query(None, description="レポートタイプ"),
    offset: int = Query(0, description="オフセット"),
) -> sc.FinItemsResponse:
    """
    予測情報を取得するエンドポイント。
    Args:
        session (SessionDep): データベースセッション依存性。
        code (str | None, optional): 銘柄コード。指定しない場合はhead_item_keyを利用。
        head_item_key (str | None, optional): ヘッドアイテムキー。指定しない場合はcodeを利用。
        report_types (list[str] | None, optional): レポートタイプのリスト。
        offset (int, optional): オフセット値。デフォルトは0。
    Raises:
        HTTPException: パラメータ不正やデータが見つからない場合に発生。
    Returns:
        sc.FinItemsResponse: 予測情報のレスポンスモデル。
    """
    if code and head_item_key:
        raise HTTPException(
            status_code=404,
            detail="銘柄コードかhead_item_keyどちらかを指定してください",
        )

    attr_value_dict = {
        "FY": "Forecasts",
        "QU": "QuarterlyForecasts",
    }

    from_names = [
        "tse-ed-t_MainTableOfConsolidatedForecastsAbstract",
        "tse-ed-t_MainTableOfForecastsAbstract",
    ]

    # head_item_keyを取得
    try:
        head_item_key = utils.get_head_item_key(
            session=session,
            head_item_key=head_item_key,
            code=code,
            report_types=report_types,
            offset=offset,
        )
    except HeadItemNotFound as e:
        raise HTTPException(status_code=404, detail=str(e))

    try:
        item = utils.get_summary_items(
            session=session,
            head_item_key=head_item_key,
            attr_value_dict=attr_value_dict,
            from_names=from_names,
            is_change=True,
        )
    except NotDictKeyError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except HeadItemNotFound as e:
        raise HTTPException(status_code=404, detail=str(e))

    result = utils.get_struct(
        items=item,
        struct=sc.FinItemsResponse(),
    )

    return result


@router.get(
    "/financial_position",
    summary="財政状態情報を取得",
    response_model=sc.FinItemsResponse,
)
def get_financial_position(
    *,
    session: SessionDep,
    code: str | None = Query(None, description="銘柄コード"),
    head_item_key: str | None = Query(None, description="head_item_key"),
    report_types: list[str] | None = Query(None, description="レポートタイプ"),
    offset: int = Query(0, description="オフセット"),
) -> sc.FinItemsResponse:
    """
    財政状態情報を取得するエンドポイント。
    Args:
        session (SessionDep): データベースセッション依存性。
        code (str | None, optional): 銘柄コード。指定しない場合はhead_item_keyを利用。
        head_item_key (str | None, optional): ヘッドアイテムキー。指定しない場合はcodeを利用。
        report_types (list[str] | None, optional): レポートタイプのリスト。
        offset (int, optional): オフセット値。デフォルトは0。
    Raises:
        HTTPException: パラメータ不正やデータが見つからない場合に発生。
    Returns:
        sc.FinItemsResponse: 財政状態情報のレスポンスモデル。
    """
    if code and head_item_key:
        raise HTTPException(
            status_code=404,
            detail="銘柄コードかhead_item_keyどちらかを指定してください",
        )

    attr_value_dict = {
        "FY": "BusinessResultsFinancialPositions",
        "QU": "BusinessResultsQuarterlyFinancialPositions",
    }

    from_names = [
        "tse-ed-t_ConsolidatedFinancialPositionsAbstract",
        "tse-ed-t_FinancialPositionsAbstract",
    ]

    # head_item_keyを取得
    try:
        head_item_key = utils.get_head_item_key(
            session=session,
            head_item_key=head_item_key,
            code=code,
            report_types=report_types,
            offset=offset,
        )
    except HeadItemNotFound as e:
        raise HTTPException(status_code=404, detail=str(e))

    try:
        item = utils.get_summary_items(
            session=session,
            head_item_key=head_item_key,
            attr_value_dict=attr_value_dict,
            from_names=from_names,
            is_change=False,
        )
    except NotDictKeyError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except HeadItemNotFound as e:
        raise HTTPException(status_code=404, detail=str(e))

    result = utils.get_struct(
        items=item,
        struct=sc.FinItemsResponse(),
    )

    return result


@router.get(
    "/cash_flows/{code}",
    summary="キャッシュフロー情報を取得",
    response_model=sc.FinItemsResponse,
)
def get_cash_flows(
    *,
    session: SessionDep,
    code: str,
    year: str | None = Query(None, description="年度"),
    offset: int = Query(0, description="オフセット"),
) -> sc.FinItemsResponse:
    """
    キャッシュフロー情報を取得するエンドポイント。
    Args:
        session (SessionDep): データベースセッション依存性。
        code (str): 銘柄コード。
        year (str | None, optional): 年度。指定しない場合は最新の年度を利用。
        offset (int, optional): オフセット値。デフォルトは0。
    Raises:
        HTTPException: パラメータ不正やデータが見つからない場合に発生。
    Returns:
        sc.FinItemsResponse: キャッシュフロー情報のレスポンスモデル。
    """
    attr_value_dict = {
        "FY": "BusinessResultsCashFlows",
        "QU": "BusinessResultsQuarterlyCashFlows",
    }

    from_names = [
        "tse-ed-t_ConsolidatedCashFlowsAbstract",
        "tse-ed-t_CashFlowsAbstract",
    ]

    try:
        head_item_key = utils.get_head_item_key(
            session=session,
            code=code,
            report_types=["edjp", "edif", "edus"],
            offset=offset,
            year=year,
            current_period="FY",
        )
    except HeadItemNotFound as e:
        raise HTTPException(status_code=404, detail=str(e))

    try:
        item = utils.get_summary_items(
            session=session,
            head_item_key=head_item_key,
            attr_value_dict=attr_value_dict,
            from_names=from_names,
            is_change=False,
        )
    except NotDictKeyError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except HeadItemNotFound as e:
        raise HTTPException(status_code=404, detail=str(e))

    result = utils.get_struct(
        items=item,
        struct=sc.FinItemsResponse(),
    )

    return result


@router.get(
    "/forecasts/change/",
    summary="業績予想の変更情報を取得",
    response_model=bool | None,
)
def get_forecast_change(
    *,
    session: SessionDep,
    head_item_key: str | None = Query(None, description="head_item_key"),
    code: str | None = Query(None, description="銘柄コード"),
    report_types: list[str] | None = Query(None, description="レポートタイプ"),
    offset: int = Query(0, description="オフセット"),
) -> bool | None:
    """
    業績予想の変更情報を取得するエンドポイント。
    Args:
        session (SessionDep): データベースセッション依存性。
        head_item_key (str | None, optional): ヘッドアイテムキー。指定しない場合はcodeを利用。
        code (str | None, optional): 銘柄コード。指定しない場合はhead_item_keyを利用。
        report_types (list[str] | None, optional): レポートタイプのリスト。
        offset (int, optional): オフセット値。デフォルトは0。
    Raises:
        HTTPException: パラメータ不正やデータが見つからない場合に発生。
    Returns:
        bool | None: 業績予想の変更情報。変更がない場合はNone。
    """
    if head_item_key is None:
        try:
            head_item_key = utils.get_head_item_key(
                session=session, code=code, report_types=report_types, offset=offset
            )
        except HeadItemNotFound as e:
            raise HTTPException(status_code=404, detail=str(e))
    else:
        if offset > 0:
            try:
                head_item_key = utils.get_base_head_item_key_offset(
                    session=session,
                    headItemKey=head_item_key,
                    report_types=report_types,
                    offset=offset,
                )
            except HeadItemNotFound as e:
                raise HTTPException(status_code=404, detail=str(e))

    names = [
        "tse-ed-t_CorrectionOfConsolidatedFinancialForecastInThisQuarter",
        "tse-ed-t_CorrectionOfNonConsolidatedFinancialForecastInThisQuarter",
        "tse-ed-t_CorrectionOfFinancialForecastInThisQuarter",
    ]

    item = crud.is_change_value(
        session=session, head_item_key=head_item_key, names=names
    )

    return item


@router.get(
    "/dividends/change/", summary="配当予想の変更情報を取得", response_model=bool | None
)
def get_dividends_change(
    *,
    session: SessionDep,
    head_item_key: str | None = Query(None, description="head_item_key"),
    code: str | None = Query(None, description="銘柄コード"),
    report_types: list[str] | None = Query(None, description="レポートタイプ"),
    offset: int = Query(0, description="オフセット"),
) -> bool | None:
    """
    配当予想の変更情報を取得するエンドポイント。
    Args:
        session (SessionDep): データベースセッション依存性。
        head_item_key (str | None, optional): ヘッドアイテムキー。指定しない場合はcodeを利用。
        code (str | None, optional): 銘柄コード。指定しない場合はhead_item_keyを利用。
        report_types (list[str] | None, optional): レポートタイプのリスト。
        offset (int, optional): オフセット値。デフォルトは0。
    Raises:
        HTTPException: パラメータ不正やデータが見つからない場合に発生。
    Returns:
        bool | None: 配当予想の変更情報。変更がない場合はNone。
    """
    if head_item_key is None:
        try:
            head_item_key = utils.get_head_item_key(
                session=session, code=code, report_types=report_types, offset=offset
            )
        except HeadItemNotFound as e:
            raise HTTPException(status_code=404, detail=str(e))
    else:
        if offset > 0:
            try:
                head_item_key = utils.get_base_head_item_key_offset(
                    session=session,
                    headItemKey=head_item_key,
                    report_types=report_types,
                    offset=offset,
                )
            except HeadItemNotFound as e:
                raise HTTPException(status_code=404, detail=str(e))

    names = ["tse-ed-t_CorrectionOfDividendForecastInThisQuarter"]

    item = crud.is_change_value(
        session=session, head_item_key=head_item_key, names=names
    )

    return item


@router.get(
    "/dividends/",
    summary="配当情報を取得",
    response_model=sc.FinItemsDividendsResponse,
)
def get_dividends(
    *,
    session: SessionDep,
    code: str | None = Query(None, description="銘柄コード"),
    head_item_key: str | None = Query(None, description="head_item_key"),
    report_types: list[str] | None = Query(None, description="レポートタイプ"),
    offset: int = Query(0, description="オフセット"),
) -> sc.FinItemsDividendsResponse:
    """
    配当情報を取得するエンドポイント。
    Args:
        session (SessionDep): データベースセッション依存性。
        code (str | None, optional): 銘柄コード。指定しない場合はhead_item_keyを利用。
        head_item_key (str | None, optional): ヘッドアイテムキー。指定しない場合はcodeを利用。
        report_types (list[str] | None, optional): レポートタイプのリスト。
        offset (int, optional): オフセット値。デフォルトは0。
    Raises:
        HTTPException: パラメータ不正やデータが見つからない場合に発生。
    Returns:
        sc.FinItemsDividendsResponse: 配当情報のレスポンスモデル。
    """
    if code and head_item_key:
        raise HTTPException(
            status_code=404,
            detail="銘柄コードかhead_item_keyどちらかを指定してください",
        )

    attr_value_dict = {
        "FY": "Dividends",
        "QU": "QuarterlyDividends",
    }

    from_names = [
        "tse-ed-t_DividendPerShareAbstract",
        "tse-ed-t_TotalDividendPaidAnnualAbstract",
        "tse-ed-t_PayoutRatioConsolidatedAbstract",
        "tse-ed-t_RatioOfTotalAmountOfDividendsToNetAssetsAbstract",
        "tse-ed-t_RatioOfTotalAmountOfDividendsToNetAssetsConsolidatedAbstract",
    ]

    if head_item_key is None:
        try:
            head_item_key = utils.get_head_item_key(
                session=session, code=code, report_types=report_types, offset=offset
            )
        except HeadItemNotFound as e:
            raise HTTPException(status_code=404, detail=str(e))
    else:
        if offset > 0:
            try:
                head_item_key = utils.get_base_head_item_key_offset(
                    session=session,
                    headItemKey=head_item_key,
                    report_types=report_types,
                    offset=offset,
                )
            except HeadItemNotFound as e:
                raise HTTPException(status_code=404, detail=str(e))

    try:
        item = utils.get_summary_items(
            session=session,
            head_item_key=head_item_key,
            attr_value_dict=attr_value_dict,
            from_names=from_names,
            is_change=False,
        )
    except NotDictKeyError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except HeadItemNotFound as e:
        raise HTTPException(status_code=404, detail=str(e))

    result = utils.get_dividends_struct(
        items=item,
        struct=sc.FinItemsDividendsResponse(),
    )

    return result
