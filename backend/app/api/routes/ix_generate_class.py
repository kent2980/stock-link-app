import json
import os
from typing import List

import app.schema as sc
from app.api.deps import SessionDep
from app.models import (
    IxHeadTitle,
    IxLabelArc,
    IxLabelLoc,
    IxLabelValue,
    IxNonFraction,
    IxNonNumeric,
    ScLinkBaseRef,
)
from fastapi import APIRouter, Query
from sqlmodel import and_, select

router = APIRouter()


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


@router.get(
    "/grouping/non_fraction/",
    response_model=sc.ix_generate_class.GroupingNonFractionList,
)
def get_grouping_non_fraction(
    *,
    session: SessionDep,
) -> sc.ix_generate_class.GroupingNonFractionList:
    """分数でないグルーピングされた項目名とコンテキストを取得する"""
    statement = (
        select(
            IxHeadTitle.report_type,
            IxHeadTitle.specific_business,
            IxNonFraction.ixbrl_role,
            IxHeadTitle.current_period,
            IxNonFraction.name,
            IxNonFraction.context,
            IxLabelValue.label,
            IxHeadTitle.is_consolidated,
        )
        .join(IxHeadTitle, IxNonFraction.head_item_key == IxHeadTitle.item_key)
        .join(ScLinkBaseRef, ScLinkBaseRef.head_item_key == IxNonFraction.head_item_key)
        .join(
            IxLabelLoc,
            and_(
                ScLinkBaseRef.href_source_file_id == IxLabelLoc.source_file_id,
                IxNonFraction.name == IxLabelLoc.xlink_href,
            ),
        )
        .join(
            IxLabelArc,
            and_(
                ScLinkBaseRef.href_source_file_id == IxLabelArc.source_file_id,
                IxLabelLoc.xlink_label == IxLabelArc.xlink_from,
            ),
        )
        .join(
            IxLabelValue,
            and_(
                ScLinkBaseRef.href_source_file_id == IxLabelValue.source_file_id,
                IxLabelArc.xlink_to == IxLabelValue.xlink_label,
            ),
        )
        .where(
            IxNonFraction.name.op("!~")("^tse-[a-z]{8}-[0-9]{5}.*"),
            IxNonFraction.context.op("!~")(".*tse-[a-z]{8}-[0-9]{5}.*"),
            IxLabelValue.xlink_role == "http://www.xbrl.org/2003/role/verboseLabel",
        )
        .group_by(
            IxHeadTitle.report_type,
            IxHeadTitle.specific_business,
            IxNonFraction.ixbrl_role,
            IxHeadTitle.current_period,
            IxNonFraction.name,
            IxNonFraction.context,
            IxLabelValue.label,
            IxHeadTitle.is_consolidated,
        )
        .order_by(
            IxHeadTitle.report_type.asc(),
            IxHeadTitle.specific_business.asc(),
            IxNonFraction.ixbrl_role.asc(),
            IxHeadTitle.current_period.asc(),
            IxNonFraction.name.asc(),
            IxNonFraction.context.asc(),
        )
    )
    result = session.exec(statement)
    name_list = result.all()

    # contextを収集
    contexts = [item.context for item in name_list]
    # contextをフラットなリストに変換
    context_list = [
        sub_context for context in contexts for sub_context in context.split("_")
    ]
    # 重複を削除
    context_list = list(set(context_list))
    # context_label_dictを取得
    context_label_dict = get_summary_context_labels(
        session=session, contexts=context_list
    )

    # name_listを辞書に変換
    name_list = [
        {
            "report_type": item.report_type,
            "specific_business": item.specific_business,
            "ixbrl_role": item.ixbrl_role,
            "current_period": item.current_period,
            "name": item.name,
            "context": item.context,
            "label": item.label,
            "is_consolidated": item.is_consolidated,
        }
        for item in name_list
    ]

    # name_listにcontext_labelを追加
    for item in name_list:
        context = item["context"]
        context_list = context.split("_")
        context_label = ""
        count = 0
        for context_item in context_list:
            if count == 0:
                context_label += context_label_dict[context_item]
            elif count > 0:
                context_label += f"_{context_label_dict[context_item]}"
            count += 1
        item["context_label"] = context_label

    return sc.ix_generate_class.GroupingNonFractionList(
        item=name_list, count=len(name_list)
    )


@router.get("/grouping/non_numeric/")
def get_grouping_non_numeric(
    *,
    session: SessionDep,
) -> sc.ix_generate_class.GroupingNonFractionList:
    """非数値グルーピングされた項目名とコンテキストを取得する"""
    statement = (
        select(
            IxHeadTitle.report_type,
            IxHeadTitle.specific_business,
            IxNonNumeric.ixbrl_role,
            IxHeadTitle.current_period,
            IxNonNumeric.name,
            IxNonNumeric.context,
            IxLabelValue.label,
            IxHeadTitle.is_consolidated,
        )
        .join(IxHeadTitle, IxNonNumeric.head_item_key == IxHeadTitle.item_key)
        .join(ScLinkBaseRef, ScLinkBaseRef.head_item_key == IxNonNumeric.head_item_key)
        .join(
            IxLabelLoc,
            and_(
                ScLinkBaseRef.href_source_file_id == IxLabelLoc.source_file_id,
                IxNonNumeric.name == IxLabelLoc.xlink_href,
            ),
        )
        .join(
            IxLabelArc,
            and_(
                ScLinkBaseRef.href_source_file_id == IxLabelArc.source_file_id,
                IxLabelLoc.xlink_label == IxLabelArc.xlink_from,
            ),
        )
        .join(
            IxLabelValue,
            and_(
                ScLinkBaseRef.href_source_file_id == IxLabelValue.source_file_id,
                IxLabelArc.xlink_to == IxLabelValue.xlink_label,
            ),
        )
        .where(
            IxNonNumeric.name.op("!~")("^tse-[a-z]{8}-[0-9]{5}.*"),
            IxNonNumeric.context.op("!~")(".*tse-[a-z]{8}-[0-9]{5}.*"),
            IxLabelValue.xlink_role == "http://www.xbrl.org/2003/role/verboseLabel",
        )
        .group_by(
            IxHeadTitle.report_type,
            IxHeadTitle.specific_business,
            IxNonNumeric.ixbrl_role,
            IxHeadTitle.current_period,
            IxNonNumeric.name,
            IxNonNumeric.context,
            IxLabelValue.label,
            IxHeadTitle.is_consolidated,
        )
        .order_by(
            IxHeadTitle.report_type.asc(),
            IxHeadTitle.specific_business.asc(),
            IxNonNumeric.ixbrl_role.asc(),
            IxHeadTitle.current_period.asc(),
            IxNonNumeric.name.asc(),
            IxNonNumeric.context.asc(),
        )
    )
    result = session.exec(statement)
    name_list = result.all()

    # contextを収集
    contexts = [item.context for item in name_list]

    # contextをフラットなリストに変換
    context_list = [
        sub_context for context in contexts for sub_context in context.split("_")
    ]

    # 重複を削除
    context_list = list(set(context_list))

    # context_label_dictを取得
    context_label_dict = get_summary_context_labels(
        session=session, contexts=context_list
    )

    # name_listを辞書に変換
    name_list = [
        {
            "report_type": item.report_type,
            "specific_business": item.specific_business,
            "ixbrl_role": item.ixbrl_role,
            "current_period": item.current_period,
            "name": item.name,
            "context": item.context,
            "label": item.label,
            "is_consolidated": item.is_consolidated,
        }
        for item in name_list
    ]

    # name_listにcontext_labelを追加
    for item in name_list:
        context = item["context"]
        context_list = context.split("_")
        context_label = ""
        count = 0
        for context_item in context_list:
            if count == 0:
                context_label += context_label_dict[context_item]
            elif count > 0:
                context_label += f"_{context_label_dict[context_item]}"
            count += 1
        item["context_label"] = context_label

    return sc.ix_generate_class.GroupingNonFractionList(
        item=name_list, count=len(name_list)
    )
