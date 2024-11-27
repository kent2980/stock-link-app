import json
import os
from typing import Dict, List

from app.api.deps import SessionDep
from app.models import IxHeadTitle, IxLabelValue, IxNonFraction
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

    if specific_business:
        key = f"{head_item.report_type}_sm_{head_item.current_period}_specific_business"
    else:
        key = f"{head_item.report_type}_sm_{head_item.current_period}"

    return {"head_item_key": head_item.item_key, "key": key}


@router.get("/context_label/", response_model=str)
def get_summary_context_label(
    *,
    session: SessionDep,
    context: str = Query(...),
) -> str:

    context_list = context.split("_")

    base_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(base_dir, "../../json/context_label.json")

    with open(json_path, "r") as f:
        data = json.load(f)

    count = 0
    context_label = ""
    label_role = "http://www.xbrl.org/2003/role/label"
    for context_item in context_list:
        if count == 0:
            context_label += data[context_item]
        elif count > 0:
            statement = select(IxLabelValue.label).where(
                IxLabelValue.xlink_label == f"label_{context_item}",
                IxLabelValue.xlink_role == label_role,
            )
            result = session.exec(statement)
            label = result.first()
            if label:
                context_label += f"_{label}"
        count += 1

    return context_label


@router.get("/context_labels/")
def get_summary_context_labels(
    *,
    session: SessionDep,
    contexts: List[str] = Query(...),
):
    """Get context labels"""

    # 空のcontext_listを作成
    context_list = []

    # contextを分割してリストに追加
    for context in contexts:
        if context:
            context_list = context_list + context.split("_")
    # 重複を削除
    context_list = list(set(context_list))
    # label_{context}の形式に変換
    context_list = [f"label_{context}" for context in context_list]

    # バッチクエリを実行
    statement = select(IxLabelValue).where(IxLabelValue.xlink_label.in_(context_list))
    result = session.exec(statement)
    labels = result.all()

    # 辞書に変換
    label_dict = {
        label.xlink_label.replace("label_", ""): label.label for label in labels
    }

    base_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(base_dir, "../../json/context_label.json")

    with open(json_path, "r") as f:
        data = json.load(f)

    # dataを辞書に変換
    data_dict = {f"{key}": value for key, value in data.items()}

    # data_dictとlabel_dictを結合
    label_dict = {**data_dict, **label_dict}

    return label_dict


@router.get("/items/")
def get_summary_items(
    *,
    session: SessionDep,
    code: str = Query(...),
    year: int = Query(...),
    period: int = Query(...),
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

    # コンテキストをコンテキストを収集
    contexts = [
        item.get("context") for item in items if item.get("context") is not None
    ]

    # コンテキストラベルを取得
    context_labels = get_summary_context_labels(session=session, contexts=contexts)

    for item in items:
        # region コンテキストラベルを取得
        context = item.get("context")
        context_label = ""
        if context:
            contexts = context.split("_")
            for context in contexts:
                if context_label:
                    context_label += f"_{context_labels.get(context)}"
                else:
                    context_label += context_labels.get(context)
        # endregion
        non_fraction = non_fraction_dict.get((item.get("name"), item.get("context")))
        if non_fraction:
            non_fraction_list.append(
                {
                    "name": item.get("name"),
                    "context": item.get("context"),
                    "label": item.get("label"),
                    "context_label": context_label,
                    "item": non_fraction,
                }
            )

    return non_fraction_list
