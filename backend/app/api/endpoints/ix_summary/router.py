from typing import Optional

from fastapi import APIRouter, HTTPException, Query

from app.api.deps import SessionDep

from . import schema as sc
from . import utils
from .exceptions import HeadItemNotFound, NotDictKeyError

router = APIRouter()


@router.get(
    "/operating_results/income/",
    summary="経営成績情報を取得",
    response_model=sc.FinResultResponse,
)
def get_operating_results(
    *,
    session: SessionDep,
    code: Optional[str] = Query(None, description="銘柄コード"),
    head_item_key: Optional[str] = Query(None, description="head_item_key"),
) -> sc.FinResultResponse:

    if code and head_item_key:
        raise HTTPException(
            status_code=404,
            detail="銘柄コードかhead_item_keyどちらかを指定してください",
        )

    attr_value_dict = {  # この辞書は、attr_valueとfrom_nameの対応を表しています。
        "FY": "BusinessResultsOperatingResults",
        "QU": "BusinessResultsQuarterlyOperatingResults",
    }

    from_name_dict = {
        "consolidated": "tse-ed-t_ConsolidatedIncomeStatementsInformationAbstract",
        "non_consolidated": "tse-ed-t_IncomeStatementsInformationAbstract",
    }

    if head_item_key is None:
        try:
            head_item_keys = utils.get_head_item_key(session=session, code=code)
        except HeadItemNotFound as e:
            raise HTTPException(status_code=404, detail=str(e))
    else:
        head_item_keys = [head_item_key]

    try:
        items = utils.get_summary_items_list(
            session=session,
            head_item_keys=head_item_keys,
            attr_value_dict=attr_value_dict,
            from_name_dict=from_name_dict,
            is_change=True,
        )
    except NotDictKeyError as e:
        raise HTTPException(status_code=404, detail=str(e))

    results = []
    for item in items:
        result = utils.get_struct(
            items=item,
            struct=sc.FinResultStruct(),
        )
        results.append(result)

    label = utils.get_header_labels(results)

    res = sc.FinResultResponse(
        count=len(results),
        labels=label,
        data=results,
    )

    return res


@router.get("/operating_results/other/{}", summary="その他の経営成績情報を取得")
def get_other_operating_results(
    *,
    session: SessionDep,
    code: str,
) -> sc.FinResultResponse:

    attr_value_dict = {
        "FY": "BusinessResultsOperatingResults",
        "QU": "BusinessResultsQuarterlyOperatingResults",
    }

    from_name_dict = {
        "consolidated": "tse-ed-t_OtherConsolidatedOperatingResultsAbstract",
        "non_consolidated": "tse-ed-t_OtherOperatingResultsAbstract",
    }

    try:
        head_item_keys = utils.get_head_item_key(session=session, code=code)
    except HeadItemNotFound as e:
        raise HTTPException(status_code=404, detail=str(e))

    try:
        items = utils.get_summary_items_list(
            session=session,
            head_item_keys=head_item_keys,
            attr_value_dict=attr_value_dict,
            from_name_dict=from_name_dict,
            is_change=False,
        )
    except NotDictKeyError as e:
        raise HTTPException(status_code=404, detail=str(e))

    results = []
    for item in items:
        result = utils.get_struct(
            items=item,
            struct=sc.FinResultStruct(),
        )
        results.append(result)

    label = utils.get_header_labels(results)

    res = sc.FinResultResponse(
        count=len(results),
        labels=label,
        data=results,
    )

    return res


@router.get("/forecasts/{code}", summary="予測情報を取得")
def get_forecasts(
    *,
    session: SessionDep,
    code: str,
) -> sc.FinForecastResponse:

    attr_value_dict = {
        "FY": "Forecasts",
        "QU": "QuarterlyForecasts",
    }

    from_name_dict = {
        "consolidated": "tse-ed-t_MainTableOfConsolidatedForecastsAbstract",
        "non_consolidated": "tse-ed-t_MainTableOfForecastsAbstract",
    }

    try:
        head_item_keys = utils.get_head_item_key(session=session, code=code)
    except HeadItemNotFound as e:
        raise HTTPException(status_code=404, detail=str(e))

    try:
        items = utils.get_summary_items_list(
            session=session,
            head_item_keys=head_item_keys,
            attr_value_dict=attr_value_dict,
            from_name_dict=from_name_dict,
            is_change=True,
        )
    except NotDictKeyError as e:
        raise HTTPException(status_code=404, detail=str(e))

    results = []
    for item in items:
        result = utils.get_struct(
            items=item,
            struct=sc.FinForecastStruct(),
        )
        results.append(result)

    label = utils.get_header_labels(results)

    res = sc.FinForecastResponse(
        count=len(results),
        labels=label,
        data=results,
    )

    return res


@router.get(
    "/financial_position/{code}",
    summary="財政状態情報を取得",
    response_model=sc.FinResultOnlyResponse,
)
def get_financial_position(
    *,
    session: SessionDep,
    code: str,
) -> sc.FinResultOnlyResponse:

    attr_value_dict = {
        "FY": "BusinessResultsFinancialPositions",
        "QU": "BusinessResultsQuarterlyFinancialPositions",
    }

    from_name_dict = {
        "consolidated": "tse-ed-t_ConsolidatedFinancialPositionsAbstract",
        "non_consolidated": "tse-ed-t_FinancialPositionsAbstract",
    }

    try:
        head_item_keys = utils.get_head_item_key(session=session, code=code)
    except HeadItemNotFound as e:
        raise HTTPException(status_code=404, detail=str(e))

    try:
        items = utils.get_summary_items_list(
            session=session,
            head_item_keys=head_item_keys,
            attr_value_dict=attr_value_dict,
            from_name_dict=from_name_dict,
            is_change=False,
        )
    except NotDictKeyError as e:
        raise HTTPException(status_code=404, detail=str(e))

    results = []
    for item in items:
        result = utils.get_struct(
            items=item,
            struct=sc.FinResultOnlyStruct(),
        )
        results.append(result)

    label = utils.get_header_labels(results)

    res = sc.FinResultOnlyResponse(
        count=len(results),
        labels=label,
        data=results,
    )

    return res


@router.get(
    "/cash_flows/{code}",
    summary="キャッシュフロー情報を取得",
    response_model=sc.FinResultOnlyResponse,
)
def get_cash_flows(
    *,
    session: SessionDep,
    code: str,
) -> sc.FinResultOnlyResponse:

    attr_value_dict = {
        "FY": "BusinessResultsCashFlows",
        "QU": "BusinessResultsQuarterlyCashFlows",
    }

    from_name_dict = {
        "consolidated": "tse-ed-t_ConsolidatedCashFlowsAbstract",
        "non_consolidated": "tse-ed-t_CashFlowsAbstract",
    }

    try:
        head_item_keys = utils.get_head_item_key(session=session, code=code)
    except HeadItemNotFound as e:
        raise HTTPException(status_code=404, detail=str(e))

    try:
        items = utils.get_summary_items_list(
            session=session,
            head_item_keys=head_item_keys,
            attr_value_dict=attr_value_dict,
            from_name_dict=from_name_dict,
            is_change=False,
        )
    except NotDictKeyError as e:
        raise HTTPException(status_code=404, detail=str(e))

    results = []
    for item in items:
        result = utils.get_struct(
            items=item,
            struct=sc.FinResultOnlyStruct(),
        )
        results.append(result)

    label = utils.get_header_labels(results)

    res = sc.FinResultOnlyResponse(
        count=len(results),
        labels=label,
        data=results,
    )

    return res


@router.get(
    "/dividends/{code}",
    summary="配当情報を取得",
    response_model=sc.FinResponseBase,
)
def get_dividends(
    *,
    session: SessionDep,
    code: str,
) -> sc.FinResponseBase:

    attr_value_dict = {
        "FY": "Dividends",
        "QU": "QuarterlyDividends",
    }

    from_name_dict = {
        "consolidated": "tse-ed-t_DividendsAbstract",
        "non_consolidated": "tse-ed-t_DividendsAbstract",
    }

    try:
        head_item_keys = utils.get_head_item_key(session=session, code=code)
    except HeadItemNotFound as e:
        raise HTTPException(status_code=404, detail=str(e))

    try:
        items = utils.get_summary_items_list(
            session=session,
            head_item_keys=head_item_keys,
            attr_value_dict=attr_value_dict,
            from_name_dict=from_name_dict,
            is_change=True,
        )
    except NotDictKeyError as e:
        raise HTTPException(status_code=404, detail=str(e))

    results = []
    for item in items:
        result = utils.get_struct(
            items=item,
        )
        results.append(result)

    label = utils.get_header_labels(results)

    res = sc.FinResponseBase(
        count=len(results),
        labels=label,
        data=results,
    )

    return res
