import json
import os
from typing import Any, Dict, List

import app.schema as sc
import app.utils.schema_class_non_fraction as scnf
import app.utils.schema_class_non_numeric as scnn
import app.utils.summary as summary
import humps
from app.api.deps import SessionDep
from app.models import IxHeadTitle, IxNonFraction, IxNonNumeric
from fastapi import APIRouter, HTTPException, Query
from sqlalchemy.exc import NoResultFound
from sqlmodel import col, select, tuple_

router = APIRouter()


@router.get("/head/")
def get_summary_head(
    *,
    session: SessionDep,
    code: str = Query(...),
    year: int = Query(...),
    period: int = Query(...),
):
    """
    指定されたコード、年度、期間のサマリーのヘッダーを取得する

    Args:
        session (SessionDep): 接続セッション
        code (str): 銘柄コード
        year (int): 年度
        period (int): 期間
    """

    period_dict = {1: ["Q1"], 2: ["Q2", "FY"], 3: ["Q3"], 4: ["FY"]}
    if period not in period_dict:
        raise HTTPException(status_code=400, detail="Invalid period value.")
    select_period = period_dict[period]

    statement = select(IxHeadTitle).where(
        IxHeadTitle.securities_code == code,
        IxHeadTitle.fy_year_end.like(f"{year}%"),
        col(IxHeadTitle.current_period).in_(select_period),
    )

    result = session.exec(statement)
    try:
        item = result.one()
    except NoResultFound:
        raise HTTPException(
            status_code=404, detail="指定したデータが見つかりませんでした。"
        )

    return item


@router.get("/key/", response_model=Dict[str, str])
def get_summary_key(
    *,
    session: SessionDep,
    code: str = Query(...),
    year: int = Query(...),
    period: int = Query(...),
) -> Dict[str, str]:
    """
    指定されたコード、年度、期間のサマリーのキーを取得する

    Args:
        session (SessionDep): 接続セッション
        code (str): 銘柄コード
        year (int): 年度
        period (int): 期間
    """

    head_item = get_summary_head(session=session, code=code, year=year, period=period)

    if head_item.is_consolidated:
        is_consolidated = "_consolidated"
    elif not head_item.is_consolidated:
        is_consolidated = "_Nonconsolidated"
    else:
        is_consolidated = ""
    specific_business = head_item.specific_business
    if head_item.current_period:
        if specific_business:
            key = f"{head_item.report_type}_FinancialReportSummary{is_consolidated}_{head_item.current_period}_specific_business"
        else:
            key = f"{head_item.report_type}_FinancialReportSummary{is_consolidated}_{head_item.current_period}"
    else:
        if specific_business:
            key = f"{head_item.report_type}_FinancialReportSummary{is_consolidated}_specific_business"
        else:
            key = f"{head_item.report_type}_FinancialReportSummary{is_consolidated}"

    return {"head_item_key": head_item.item_key, "key": key}


@router.get(
    "/non_fraction/items/head_item_key",
    response_model=scnf.get_response_schema_FinancialReportSummary_class(),
)
def get_summary_non_fraction_items_head_item_key(
    *,
    session: SessionDep,
    head_item_key: str,
):
    """
    指定されたヘッダーアイテムキーのサマリーを取得する

    Args:
        session (SessionDep): 接続セッション
        head_item_key (int): ヘッダーアイテムキー
    """

    statement = select(IxHeadTitle).where(IxHeadTitle.item_key == head_item_key)
    result = session.exec(statement)
    try:
        head_item = result.one()
    except NoResultFound:
        raise HTTPException(
            status_code=404, detail="指定したデータが見つかりませんでした。"
        )

    key = summary.generate_non_fraction_key(
        head_item.model_dump(), "FinancialReportSummary"
    )

    # 絶対パスを使用
    base_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(base_dir, "../../json/non_fraction/grouped_data.json")

    with open(json_path, "r") as f:
        data = json.load(f)

    items: List[Dict[str, str]] = data[key]

    non_fraction_list = []

    # すべての必要なキーを収集
    item_keys = [(item.get("name"), item.get("context")) for item in items]

    # バッチクエリを実行
    statement = select(IxNonFraction).where(
        IxNonFraction.head_item_key == head_item_key,
        tuple_(IxNonFraction.name, IxNonFraction.context).in_(item_keys),
    )
    result = session.exec(statement)
    non_fractions = result.all()

    # クエリ結果を辞書に変換
    non_fraction_dict = {(nf.name, nf.context): nf for nf in non_fractions}

    summary_data = {}
    for item in items:
        non_fraction = non_fraction_dict.get((item.get("name"), item.get("context")))
        if non_fraction:
            non_fraction_list.append(
                {
                    "name": item.get("name"),
                    "context": item.get("context"),
                    "label": item.get("label"),
                    "item": non_fraction,
                }
            )
            name = humps.decamelize(item.get("name").split("_")[-1]).replace("__", "_")
            context = humps.decamelize(item.get("context")).replace("__", "_")
            if name not in summary_data:
                summary_data[name] = {}
            summary_data[name][context] = non_fraction.model_dump()

    schema = scnf.get_schema_class(key)(**summary_data)
    if schema is None:
        raise HTTPException(
            status_code=404, detail="指定したデータが見つかりませんでした。"
        )

    return schema


@router.get(
    "/non_fraction/items/",
    response_model=scnf.get_response_schema_FinancialReportSummary_class(),
)
def get_summary_non_fraction_items(
    *,
    session: SessionDep,
    code: str = Query(...),
    year: int = Query(...),
    period: int = Query(...),
):
    """
    指定されたコード、年度、期間のサマリーを取得する

    Args:
        session (SessionDep): 接続セッション
        code (str): 銘柄コード
        year (int): 年度
        period (int): 期間
    """

    head_item = get_summary_head(session=session, code=code, year=year, period=period)
    head_item_key = head_item.item_key

    return get_summary_non_fraction_items_head_item_key(
        session=session, head_item_key=head_item_key
    )


@router.get(
    "/non_numeric/items/head_item_key",
    response_model=scnn.get_response_schema_FinancialReportSummary_class(),
)
def get_summary_non_numeric_items_head_item_key(
    *,
    session: SessionDep,
    head_item_key: str,
):
    """
    指定されたヘッダーアイテムキーのサマリーを取得する

    Args:
        session (SessionDep): 接続セッション
        head_item_key (int): ヘッダーアイテムキー
    """

    statement = select(IxHeadTitle).where(IxHeadTitle.item_key == head_item_key)
    result = session.exec(statement)
    try:
        head_item = result.one()
    except NoResultFound:
        raise HTTPException(
            status_code=404, detail="指定したデータが見つかりませんでした。"
        )

    key = summary.generate_non_numeric_key(head_item.model_dump())

    # 絶対パスを使用
    base_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(base_dir, "../../json/non_numeric/grouped_data.json")

    with open(json_path, "r") as f:
        data = json.load(f)

    items: List[Dict[str, str]] = data[key]

    non_numeric_list = []

    # すべての必要なキーを収集
    item_keys = [(item.get("name")) for item in items]

    # バッチクエリを実行
    statement = select(IxNonNumeric).where(
        IxNonNumeric.head_item_key == head_item_key,
        col(IxNonNumeric.name).in_(item_keys),
    )
    result = session.exec(statement)
    non_numerics = result.all()

    # クエリ結果を辞書に変換
    non_numeric_dict = {(nn.name): nn for nn in non_numerics}

    summary_data = {}
    for item in items:
        non_numeric = non_numeric_dict.get((item.get("name")))
        if non_numeric:
            non_numeric_list.append(
                {
                    "name": item.get("name"),
                    "label": item.get("label"),
                    "item": non_numeric,
                }
            )
            name = humps.decamelize(item.get("name").split("_")[-1]).replace("__", "_")
            if name not in summary_data:
                summary_data[name] = {}
            summary_data[name] = non_numeric.model_dump()

    schema = scnn.get_schema_class(key)(**summary_data)
    if schema is None:
        raise HTTPException(
            status_code=404, detail="指定したデータが見つかりませんでした。"
        )

    return schema


@router.get(
    "/non_numeric/items/",
    response_model=scnn.get_response_schema_FinancialReportSummary_class(),
)
def get_summary_non_numeric_items(
    *,
    session: SessionDep,
    code: str = Query(...),
    year: int = Query(...),
    period: int = Query(...),
):
    """
    指定されたコード、年度、期間のサマリーを取得する

    Args:
        session (SessionDep): 接続セッション
        code (str): 銘柄コード
        year (int): 年度
        period (int): 期間
    """

    head_item = get_summary_head(session=session, code=code, year=year, period=period)
    head_item_key = head_item.item_key

    return get_summary_non_numeric_items_head_item_key(
        session=session, head_item_key=head_item_key
    )
