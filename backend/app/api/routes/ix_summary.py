import json
import os
from typing import Dict, List

import app.schema as sc
import humps
from app.api.deps import SessionDep
from app.models import IxHeadTitle, IxNonFraction
from fastapi import APIRouter, Query
from sqlmodel import or_, select, tuple_

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
    Get summary of all items.
    """

    period_dict = {1: "Q1", 2: "Q2", 3: "Q3", 4: "FY"}
    period_str = period_dict[period]

    statement = select(IxHeadTitle).where(
        IxHeadTitle.securities_code == code,
        IxHeadTitle.fy_year_end.like(f"{year}%"),
    )

    if period_str == "Q2":
        statement = statement.where(
            or_(
                IxHeadTitle.current_period == "HY",
                IxHeadTitle.current_period == "Q2",
            )
        )
    else:
        statement = statement.where(IxHeadTitle.current_period == period_str)

    result = session.exec(statement)
    item = result.one()

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
    Get summary of all items.
    """

    head_item = get_summary_head(session=session, code=code, year=year, period=period)

    specific_business = head_item.specific_business
    if head_item.current_period:
        if specific_business:
            key = f"{head_item.report_type}_FinancialReportSummary_{head_item.current_period}_specific_business"
        else:
            key = f"{head_item.report_type}_FinancialReportSummary_{head_item.current_period}"
    else:
        if specific_business:
            key = f"{head_item.report_type}_FinancialReportSummary_specific_business"
        else:
            key = f"{head_item.report_type}_FinancialReportSummary"

    return {"head_item_key": head_item.item_key, "key": key}


@router.get(
    "/items/",
    response_model=sc.ix_summary.edjp_FinancialReportSummary_HY_specific_business
    | sc.ix_summary.edjp_FinancialReportSummary_Q1
    | sc.ix_summary.edjp_FinancialReportSummary_Q2
    | sc.ix_summary.edjp_FinancialReportSummary_Q3
    | sc.ix_summary.edjp_FinancialReportSummary_FY
    | sc.ix_summary.edjp_FinancialReportSummary,
)
def get_summary_items(
    *,
    session: SessionDep,
    code: str = Query(...),
    year: int = Query(...),
    period: int = Query(...),
) -> (
    sc.ix_summary.edjp_FinancialReportSummary_HY_specific_business
    | sc.ix_summary.edjp_FinancialReportSummary_Q1
    | sc.ix_summary.edjp_FinancialReportSummary_Q2
    | sc.ix_summary.edjp_FinancialReportSummary_Q3
    | sc.ix_summary.edjp_FinancialReportSummary_FY
    | sc.ix_summary.edjp_FinancialReportSummary
):
    """
    Get summary of all items.
    """

    key = get_summary_key(session=session, code=code, year=year, period=period)

    # 絶対パスを使用
    base_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(base_dir, "../../json/grouped_data_non_fraction.json")

    with open(json_path, "r") as f:
        data = json.load(f)

    items: List[Dict[str, str, str]] = data[key.get("key")]

    non_fraction_list = []

    # すべての必要なキーを収集
    item_keys = [(item.get("name"), item.get("context")) for item in items]

    # バッチクエリを実行
    statement = select(IxNonFraction).where(
        IxNonFraction.head_item_key == key.get("head_item_key"),
        tuple_(IxNonFraction.name, IxNonFraction.context).in_(item_keys),
    )
    result = session.exec(statement)
    non_fractions = result.all()

    # クエリ結果を辞書に変換
    non_fraction_dict = {(nf.name, nf.context): nf for nf in non_fractions}

    dict1 = {}
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
            if name not in dict1:
                dict1[name] = {}
            dict1[name][context] = non_fraction.model_dump()

    if key.get("key") == "edjp_FinancialReportSummary_Q1":
        schema = sc.ix_summary.edjp_FinancialReportSummary_Q1(**dict1)
    elif key.get("key") == "edjp_FinancialReportSummary_Q2":
        schema = sc.ix_summary.edjp_FinancialReportSummary_Q2(**dict1)
    elif key.get("key") == "edjp_FinancialReportSummary_Q3":
        schema = sc.ix_summary.edjp_FinancialReportSummary_Q3(**dict1)
    elif key.get("key") == "edjp_FinancialReportSummary_FY":
        schema = sc.ix_summary.edjp_FinancialReportSummary_FY(**dict1)
    elif key.get("key") == "edjp_FinancialReportSummary":
        schema = sc.ix_summary.edjp_FinancialReportSummary(**dict1)
    elif key.get("key") == "edjp_FinancialReportSummary_HY_specific_business":
        schema = sc.ix_summary.edjp_FinancialReportSummary_HY_specific_business(**dict1)

    return schema
