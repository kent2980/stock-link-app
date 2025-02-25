from typing import List

from fastapi import APIRouter, HTTPException, Query

from app.api.deps import SessionDep

from . import crud
from . import schema as sc
from . import utils
from .exceptions import HeadItemNotFound, NotDictKeyError

router = APIRouter()


@router.get(
    "/operating_results/income/{code}",
    summary="経営成績情報を取得",
    response_model=sc.FinancialResponseListSchema,
)
def get_operating_results(
    *,
    session: SessionDep,
    code: str,
) -> sc.FinancialResponseListSchema:

    attr_value_dict = {  # この辞書は、attr_valueとfrom_nameの対応を表しています。
        "FY": "BusinessResultsOperatingResults",
        "QU": "BusinessResultsQuarterlyOperatingResults",
    }

    from_name_dict = {
        "consolidated": "tse-ed-t_ConsolidatedIncomeStatementsInformationAbstract",
        "non_consolidated": "tse-ed-t_IncomeStatementsInformationAbstract",
    }

    try:
        head_item_keys = utils.get_head_item_key(session=session, code=code)
    except HeadItemNotFound as e:
        raise HTTPException(status_code=404, detail=str(e))

    try:
        return utils.get_financial_response_list_schema(
            session=session,
            head_item_keys=head_item_keys,
            attr_value_dict=attr_value_dict,
            from_name_dict=from_name_dict,
            is_change=True,
        )
    except NotDictKeyError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/operating_results/other/{code}", summary="その他の経営成績情報を取得")
def get_other_operating_results(
    *,
    session: SessionDep,
    code: str,
) -> sc.FinancialResponseListSchema:

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
        return utils.get_financial_response_list_schema(
            session=session,
            head_item_keys=head_item_keys,
            attr_value_dict=attr_value_dict,
            from_name_dict=from_name_dict,
            is_change=False,
        )
    except NotDictKeyError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/forecasts/{code}", summary="予測情報を取得")
def get_forecasts(
    *,
    session: SessionDep,
    code: str,
) -> sc.FinancialResponseListSchema:

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
        return utils.get_financial_response_list_schema(
            session=session,
            head_item_keys=head_item_keys,
            attr_value_dict=attr_value_dict,
            from_name_dict=from_name_dict,
            is_change=True,
        )
    except NotDictKeyError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get(
    "/financial_position/{code}",
    summary="財政状態情報を取得",
    response_model=sc.FinancialResponseListSchema,
)
def get_financial_position(
    *,
    session: SessionDep,
    code: str,
) -> sc.FinancialResponseListSchema:

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
        return utils.get_financial_response_list_schema(
            session=session,
            head_item_keys=head_item_keys,
            attr_value_dict=attr_value_dict,
            from_name_dict=from_name_dict,
            is_change=False,
        )
    except NotDictKeyError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get(
    "/cash_flows/{code}",
    summary="キャッシュフロー情報を取得",
    response_model=sc.FinancialResponseListSchema,
)
def get_cash_flows(
    *,
    session: SessionDep,
    code: str,
) -> sc.FinancialResponseListSchema:

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
        return utils.get_financial_response_list_schema(
            session=session,
            head_item_keys=head_item_keys,
            attr_value_dict=attr_value_dict,
            from_name_dict=from_name_dict,
            is_change=False,
        )
    except NotDictKeyError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get(
    "/dividends/{code}",
    summary="配当情報を取得",
    response_model=sc.FinancialResponseListSchema,
)
def get_dividends(
    *,
    session: SessionDep,
    code: str,
) -> sc.FinancialResponseListSchema:

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
        return utils.get_financial_response_list_schema(
            session=session,
            head_item_keys=head_item_keys,
            attr_value_dict=attr_value_dict,
            from_name_dict=from_name_dict,
            is_change=True,
        )
    except NotDictKeyError as e:
        raise HTTPException(status_code=404, detail=str(e))
