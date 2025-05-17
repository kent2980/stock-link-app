from fastapi import APIRouter, HTTPException, Query

from app.api.deps import SessionDep

from . import crud, utils
from . import schema as sc
from .exceptions import HeadItemNotFound, NotDictKeyError

router = APIRouter()


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
    if code and head_item_key:
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

    print(f"head_item_key: {head_item_key}")

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
