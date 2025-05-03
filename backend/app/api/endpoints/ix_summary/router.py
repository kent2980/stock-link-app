from typing import List, Optional

from fastapi import APIRouter, HTTPException, Query

from app.api.deps import SessionDep

from . import crud
from . import schema as sc
from . import utils
from .exceptions import HeadItemNotFound, NotDictKeyError

router = APIRouter()


@router.get(
    "/operating_results/income/",
    summary="経営成績情報を取得",
    response_model=sc.FinResultStruct,
)
def get_operating_results(
    *,
    session: SessionDep,
    code: Optional[str] = Query(None, description="銘柄コード"),
    head_item_key: Optional[str] = Query(None, description="head_item_key"),
    report_types: Optional[List[str]] = Query(None, description="レポートタイプ"),
    offset: int = Query(0, description="オフセット"),
) -> sc.FinResultStruct:

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
            from_name_dict=from_name_dict,
            is_change=True,
        )
    except NotDictKeyError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except HeadItemNotFound as e:
        raise HTTPException(status_code=404, detail=str(e))

    result = utils.get_struct(
        items=item,
        struct=sc.FinResultStruct(),
    )

    return result


@router.get("/operating_results/other/{}", summary="その他の経営成績情報を取得")
def get_other_operating_results(
    *,
    session: SessionDep,
    code: Optional[str] = Query(None, description="銘柄コード"),
    head_item_key: Optional[str] = Query(None, description="head_item_key"),
    report_types: Optional[List[str]] = Query(None, description="レポートタイプ"),
    offset: int = Query(0, description="オフセット"),
) -> sc.FinResultStruct:

    if code and head_item_key:
        raise HTTPException(
            status_code=404,
            detail="銘柄コードかhead_item_keyどちらかを指定してください",
        )

    attr_value_dict = {
        "FY": "BusinessResultsOperatingResults",
        "QU": "BusinessResultsQuarterlyOperatingResults",
    }

    from_name_dict = {
        "consolidated": "tse-ed-t_OtherConsolidatedOperatingResultsAbstract",
        "non_consolidated": "tse-ed-t_OtherOperatingResultsAbstract",
    }

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
            from_name_dict=from_name_dict,
            is_change=False,
        )
    except NotDictKeyError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except HeadItemNotFound as e:
        raise HTTPException(status_code=404, detail=str(e))

    result = utils.get_struct(
        items=item,
        struct=sc.FinResultStruct(),
    )

    return result


@router.get("/forecasts/", summary="予測情報を取得")
def get_forecasts(
    *,
    session: SessionDep,
    code: Optional[str] = Query(None, description="銘柄コード"),
    head_item_key: Optional[str] = Query(None, description="head_item_key"),
    report_types: Optional[List[str]] = Query(None, description="レポートタイプ"),
    offset: int = Query(0, description="オフセット"),
) -> sc.FinForecastStruct:

    if code and head_item_key:
        raise HTTPException(
            status_code=404,
            detail="銘柄コードかhead_item_keyどちらかを指定してください",
        )

    attr_value_dict = {
        "FY": "Forecasts",
        "QU": "QuarterlyForecasts",
    }

    from_name_dict = {
        "consolidated": "tse-ed-t_MainTableOfConsolidatedForecastsAbstract",
        "non_consolidated": "tse-ed-t_MainTableOfForecastsAbstract",
    }

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
            from_name_dict=from_name_dict,
            is_change=True,
        )
    except NotDictKeyError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except HeadItemNotFound as e:
        raise HTTPException(status_code=404, detail=str(e))

    result = utils.get_struct(
        items=item,
        struct=sc.FinForecastStruct(),
    )

    return result


@router.get(
    "/financial_position",
    summary="財政状態情報を取得",
    response_model=sc.FinResultOnlyStruct,
)
def get_financial_position(
    *,
    session: SessionDep,
    code: Optional[str] = Query(None, description="銘柄コード"),
    head_item_key: Optional[str] = Query(None, description="head_item_key"),
    report_types: Optional[List[str]] = Query(None, description="レポートタイプ"),
    offset: int = Query(0, description="オフセット"),
) -> sc.FinResultOnlyStruct:

    if code and head_item_key:
        raise HTTPException(
            status_code=404,
            detail="銘柄コードかhead_item_keyどちらかを指定してください",
        )

    attr_value_dict = {
        "FY": "BusinessResultsFinancialPositions",
        "QU": "BusinessResultsQuarterlyFinancialPositions",
    }

    from_name_dict = {
        "consolidated": "tse-ed-t_ConsolidatedFinancialPositionsAbstract",
        "non_consolidated": "tse-ed-t_FinancialPositionsAbstract",
    }

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
            from_name_dict=from_name_dict,
            is_change=False,
        )
    except NotDictKeyError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except HeadItemNotFound as e:
        raise HTTPException(status_code=404, detail=str(e))

    result = utils.get_struct(
        items=item,
        struct=sc.FinResultOnlyStruct(),
    )

    return result


@router.get(
    "/cash_flows/{code}",
    summary="キャッシュフロー情報を取得",
    response_model=sc.FinResultOnlyStruct,
)
def get_cash_flows(
    *,
    session: SessionDep,
    code: str,
    year: Optional[str] = Query(None, description="年度"),
    offset: int = Query(0, description="オフセット"),
) -> sc.FinResultOnlyStruct:

    attr_value_dict = {
        "FY": "BusinessResultsCashFlows",
        "QU": "BusinessResultsQuarterlyCashFlows",
    }

    from_name_dict = {
        "consolidated": "tse-ed-t_ConsolidatedCashFlowsAbstract",
        "non_consolidated": "tse-ed-t_CashFlowsAbstract",
    }

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
            from_name_dict=from_name_dict,
            is_change=False,
        )
    except NotDictKeyError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except HeadItemNotFound as e:
        raise HTTPException(status_code=404, detail=str(e))

    result = utils.get_struct(
        items=item,
        struct=sc.FinResultOnlyStruct(),
    )

    return result


@router.get(
    "/forecasts/change/",
    summary="業績予想の変更情報を取得",
    response_model=Optional[bool],
)
def get_forecast_change(
    *,
    session: SessionDep,
    head_item_key: Optional[str] = Query(None, description="head_item_key"),
    code: Optional[str] = Query(None, description="銘柄コード"),
    report_types: Optional[List[str]] = Query(None, description="レポートタイプ"),
    offset: int = Query(0, description="オフセット"),
) -> Optional[bool]:

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
    ]

    item = crud.is_change_value(
        session=session, head_item_key=head_item_key, names=names
    )

    return item


@router.get(
    "/dividends/change/",
    summary="配当予想の変更情報を取得",
    response_model=Optional[bool],
)
def get_dividends_change(
    *,
    session: SessionDep,
    head_item_key: Optional[str] = Query(None, description="head_item_key"),
    code: Optional[str] = Query(None, description="銘柄コード"),
    report_types: Optional[List[str]] = Query(None, description="レポートタイプ"),
    offset: int = Query(0, description="オフセット"),
) -> Optional[bool]:

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

    pass
