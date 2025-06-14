from fastapi import APIRouter, HTTPException, Query
from sqlmodel import select

from app.api.deps import SessionDep
from app.models import IxHeadTitle, IxHeadTitleSummary

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
    page: int = Query(1, description="ページ番号", ge=1, le=1000),
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
        limit=5,  # デフォルトの取得数を20に設定
        offset=(page - 1) * 5,  # ページ番号に基づいてオフセットを計算
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
                    headItemKey=item[0].item_key,
                    item_id=item[0].id,
                    company=item[0].company_name,
                    code=item[0].securities_code,
                    reporting_date=item[0].reporting_date.strftime("%Y-%m-%d"),
                    insert_date=item[0].insert_date.strftime("%Y-%m-%d %H:%M:%S"),
                    title=item[0].document_name,
                    category=item[0].report_type,
                    summary=item[1].summary if item[1] else "",
                    important=True,
                    operating_result_json=item[1].operating_result_json,
                    forecast_json=item[1].forecast_json,
                    cashflow_json=item[1].cashflow_json,
                )
            )
        except Exception:
            print(item.id)
            continue
    return sc.DisclosureItemsList(
        count=len(item_list),
        data=item_list,
        page=page,
        next_page=page + 1 if len(item_list) == 5 else None,
        previous_page=page - 1 if page > 1 else None,
    )


@router.get(
    "/disclosure_items/id/{id}",
    summary="開示項目情報をIDで取得",
    response_model=sc.DisclosureItemsIdList,
)
def get_disclosure_items_by_id(
    *,
    session: SessionDep,
    report_types: list[str] | None = Query(
        ["edif", "edus", "edjp"],
        description="取得する開示項目のレポートタイプ",
        example=["edif", "edus", "edjp"],
    ),
    item_id: int = Query(..., description="開示項目のID"),
) -> sc.DisclosureItemsIdList:
    """
    開示項目情報をIDで取得するエンドポイント。

    Args:
        session (SessionDep): データベースセッション依存性。
        id (int): 開示項目のID。

    Raises:
        HTTPException: データが見つからない場合に発生。

    Returns:
        sc.DisclosureItem: 開示項目の詳細情報。
    """
    items = crud.get_disclosure_item_by_id(
        session=session, report_types=report_types, item_id=item_id
    )

    if not items:
        raise HTTPException(
            status_code=404,
            detail=f"ID {item_id} の開示項目が見つかりません。",
        )

    items_list = []

    for item in items:
        try:
            items_list.append(
                sc.DisclosureItem(
                    item_id=item[0].id,
                    company=item[0].company_name,
                    code=item[0].securities_code,
                    reporting_date=item[0].reporting_date.strftime("%Y-%m-%d"),
                    insert_date=item[0].insert_date.strftime("%Y-%m-%d %H:%M:%S"),
                    title=item[0].document_name,
                    category=item[0].report_type,
                    summary=item[1].summary if item[1] else "",
                    important=True,
                    operating_result_json=item[1].operating_result_json,
                    forecast_json=item[1].forecast_json,
                    cashflow_json=item[1].cashflow_json,
                )
            )
        except Exception:
            print(item.id)
            continue

    return sc.DisclosureItemsIdList(
        count=len(items_list),
        data=items_list,
        item_id=item_id,
        next_id=items_list[0].item_id if items_list else None,
        previous_id=items_list[-1].item_id if items_list else None,
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


@router.post(
    "/ix_title_summary/all/",
    summary="iXBRLのヘッダー情報の要約レコードを書き込む",
    response_model=int,
)
def post_ix_title_summaries(
    *,
    session: SessionDep,
) -> int:
    """
    Get IX title summaries.
    """

    # 要約が取得されていない全てのKeyを取得
    statement = (
        select(IxHeadTitle)
        .outerjoin(
            IxHeadTitleSummary,
            IxHeadTitle.item_key == IxHeadTitleSummary.head_item_key,
        )
        .where(IxHeadTitleSummary.summary.is_(None))
    )

    items = session.exec(statement)
    if not items:
        raise HTTPException(
            status_code=404,
            detail="要約はすでに取得されています。",
        )

    # 要約を取得
    BATCH_SIZE = 1000  # 一度に処理するバッチサイズ
    buffer = []
    count = 0

    for item in items:
        try:
            summary = get_financial_summary(
                session=session, head_item_key=item.item_key, offset=0
            )
            ope = get_operating_results(
                session=session, head_item_key=item.item_key, offset=0
            )
            forecast = get_forecasts(
                session=session, code=None, head_item_key=item.item_key, offset=0
            )
            cashflow = get_cash_flows(
                session=session,
                code=item.securities_code,
                year=item.fy_year_end[0:4] if item.fy_year_end else None,
                offset=0 if item.current_period == "FY" else 1,
            )
            data = sc.IxSummaryResponseCreate(
                head_item_key=item.item_key,
                summary=summary,
                operating_result_json=ope.model_dump_json() if ope else None,
                forecast_json=forecast.model_dump_json() if forecast else None,
                cashflow_json=cashflow.model_dump_json() if cashflow else None,
            )
            buffer.append(IxHeadTitleSummary.model_validate(data))
        except Exception as e:
            print(f"Error processing key {item.item_key}: {str(e)}")
            # ヘッドアイテムが見つからない場合はスキップ
            continue

        if len(buffer) >= BATCH_SIZE:
            session.bulk_save_objects(buffer)
            session.commit()
            count += len(buffer)
            buffer.clear()

    # 残りのデータを保存
    if buffer:
        session.bulk_save_objects(buffer)
        session.commit()
        count += len(buffer)

    return count


@router.post(
    "/ix_title_summary/item/",
    summary="iXBRLのヘッダー情報の要約レコードを作成",
    response_model=sc.IxSummaryResponseCreate,
)
def post_ix_title_summary_item(
    *,
    session: SessionDep,
    head_item_key: str,
) -> int:
    statement = select(IxHeadTitle).where(IxHeadTitle.item_key == head_item_key)
    result = session.exec(statement).first()
    code = result.securities_code if result else None
    fy_year_end = result.fy_year_end if result else None
    item = sc.IxSummaryResponseCreate(head_item_key=head_item_key)

    try:
        summary = get_financial_summary(
            session=session, head_item_key=head_item_key, offset=0
        )
        ope = get_operating_results(
            session=session, code=None, head_item_key=head_item_key, offset=0
        )
        forecast = get_forecasts(
            session=session, code=None, head_item_key=head_item_key, offset=0
        )
        cashflow = get_cash_flows(
            session=session,
            code=code,
            year=fy_year_end[0:4] if fy_year_end else None,
            offset=0 if item.current_period == "FY" else 1,
        )
        item.summary = summary
        item.operating_result_json = ope.model_dump_json() if ope else None
        item.forecast_json = forecast.model_dump_json() if forecast else None
        item.cashflow_json = cashflow.model_dump_json() if cashflow else None
    except Exception as e:
        raise HTTPException(
            status_code=404,
            detail=f"ヘッドアイテムキー {head_item_key} の要約が見つかりません: {str(e)}",
        )

    new_item = IxHeadTitleSummary.model_validate(item)

    try:
        session.add(new_item)
        session.commit()
        session.refresh(new_item)
    except Exception as e:
        session.rollback()
        raise HTTPException(
            status_code=500,
            detail=f"要約の保存に失敗しました: {str(e)}",
        )

    return new_item


@router.patch(
    "/ix_title_summary/all/",
    summary="iXBRLのヘッダー情報の要約レコードを更新",
    response_model=int,
)
def patch_ix_title_summary_all(
    *,
    session: SessionDep,
) -> int:
    statement = (
        select(IxHeadTitleSummary, IxHeadTitle)
        .join(IxHeadTitle, IxHeadTitle.item_key == IxHeadTitleSummary.head_item_key)
        .where(IxHeadTitleSummary.summary.is_not(None))
    )

    count = 0
    BATCH_SIZE = 100
    batch = []

    for summary in session.exec(statement):
        head_item_key = summary[0].head_item_key
        code = summary[1].securities_code
        updated = False
        print(f"Processing head_item_key: {head_item_key}, code: {code}")
        if not summary[0].operating_result_json:
            try:
                summary[0].operating_result_json = get_operating_results(
                    session=session, code=None, head_item_key=head_item_key, offset=0
                ).model_dump_json()
                updated = True
            except Exception:
                summary[0].operating_result_json = None
        if not summary[0].forecast_json:
            try:
                summary[0].forecast_json = get_forecasts(
                    session=session, code=None, head_item_key=head_item_key, offset=0
                ).model_dump_json()
                updated = True
            except Exception:
                summary[0].forecast_json = None
        if not summary[0].cashflow_json:
            try:
                summary[0].cashflow_json = get_cash_flows(
                    session=session,
                    code=code,
                    year=summary[1].fy_year_end[0:4],
                    offset=0 if summary[1].current_period == "FY" else 1,
                ).model_dump_json()
                updated = True
            except Exception:
                summary[0].cashflow_json = None
        if updated:
            batch.append(summary[0])
            count += 1
        if len(batch) >= BATCH_SIZE:
            session.commit()
            batch.clear()
            print(f"Updated {count} summaries so far...")

    if batch:
        session.commit()
        print(f"Updated {count} summaries so far...")

    return count
