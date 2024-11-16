from typing import Any, Dict, List, Tuple

from app.api.deps import SessionDep
from app.models import (
    IxLabelArc,
    IxLabelLoc,
    IxLabelValue,
    IxNonFraction,
    IxNonNumeric,
    IxSourceFile,
    ScLinkBaseRef,
)
from fastapi import APIRouter, Query
from sqlalchemy.orm import aliased as alias
from sqlmodel import and_, select

router = APIRouter()


@router.get("/grouping/names/", response_model=List[Tuple[str, str]])
def get_grouping_names(
    *,
    session: SessionDep,
    report_type: str = Query(...),
    xbrl_type: str = Query(...),
    non_fraction: bool = True,
) -> str:
    """指定したレポートタイプに対応するクラスファイルを生成する

    Args:<br/>
        session (SessionDep): DBセッション<br/>
        report_type (str): レポートタイプ (edjp, edif, edus, edit, rvdf, rvfc, rejp, rrdf, rrfc, efjp)<br/>
        non_fraction (bool): 分数でないかどうか
    """
    if non_fraction:
        alias_ = alias(IxNonFraction)
    else:
        alias_ = alias(IxNonNumeric)

    # _aliasからnameとlabelを取得
    statement = (
        select(alias_.name, IxLabelValue.label)
        .join(IxLabelLoc, alias_.name == IxLabelLoc.xlink_href)
        .join(IxLabelArc, IxLabelLoc.xlink_label == IxLabelArc.xlink_from)
        .join(IxLabelValue, IxLabelArc.xlink_to == IxLabelValue.xlink_label)
        .where(
            alias_.xbrl_type == xbrl_type,
            alias_.report_type == report_type,
            IxLabelValue.xlink_role == "http://www.xbrl.org/2003/role/verboseLabel",
        )
        .group_by(
            alias_.name,
            alias_.xbrl_type,
            alias_.report_type,
            IxLabelValue.label,
        )
        .order_by(alias_.name.asc())
    )
    # statementを実行
    result = session.exec(statement)
    # name_listに結果を格納
    name_list = result.all()

    # name_listの重複を削除
    name_list = list(set(name_list))

    # name_listをalias_.name昇順に並び替え
    name_list.sort(key=lambda x: x[0])

    return name_list


@router.get(
    "/grouping/contexts/",
    response_model=Dict[Any, Any],
)
def get_grouping_contexts(
    *,
    session: SessionDep,
    report_type: str = Query(...),
    xbrl_type: str = Query(...),
    non_fraction: bool = True,
) -> str:
    """指定したレポートタイプに対応するクラスファイルを生成する (context用)"""

    if non_fraction:
        alias_ = alias(IxNonFraction)
    else:
        alias_ = alias(IxNonNumeric)

    statement = (
        select(alias_.name, alias_.context, IxLabelValue.label)
        .join(ScLinkBaseRef, ScLinkBaseRef.head_item_key == alias_.head_item_key)
        .join(
            IxLabelLoc,
            and_(
                ScLinkBaseRef.href_source_file_id == IxLabelLoc.source_file_id,
                alias_.name == IxLabelLoc.xlink_href,
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
            alias_.xbrl_type == xbrl_type,
            alias_.report_type == report_type,
            IxLabelValue.xlink_role == "http://www.xbrl.org/2003/role/verboseLabel",
        )
        .group_by(
            alias_.name,
            alias_.context,
            IxLabelValue.label,
        )
    )
    # statementを実行
    result = session.exec(statement)
    # name_listに結果を格納
    name_list = result.all()

    print(f"statementを実行しました。")

    # name_listの重複を削除
    name_list = list(set(name_list))

    # name,contextで昇順ソート
    name_list.sort(key=lambda x: (x[0], x[1]))

    # 期間ラベル情報を取得
    context_label = {
        "CurrentYearDuration": "当年度会計期間",
        "CurrentAccumulatedQ1Duration": "当年度期初から第１四半期間",
        "CurrentAccumulatedQ2Duration": "当年度期初から第２四半期間",
        "CurrentAccumulatedQ3Duration": "当年度期初から第３四半期間",
        "NextYearDuration": "次年度会計期間",
        "Next2YearDuration": "次々年度会計期間",
        "NextAccumulatedQ1Duration": "次年度期初から第１四半期間",
        "NextAccumulatedQ2Duration": "次年度期初から第２四半期間",
        "NextAccumulatedQ3Duration": "次年度期初から第３四半期間",
        "PriorYearDuration": "前年度会計期間",
        "PriorAccumulatedQ1Duration": "前年度期初から第１四半期間",
        "PriorAccumulatedQ2Duration": "前年度期初から第２四半期間",
        "PriorAccumulatedQ3Duration": "前年度期初から第３四半期間",
        "CurrentYearInstant": "当年度時点",
        "CurrentAccumulatedQ1Instant": "当年度期初から第１四半期間時点",
        "CurrentAccumulatedQ2Instant": "当年度期初から第２四半期間時点",
        "CurrentAccumulatedQ3Instant": "当年度期初から第３四半期間時点",
        "NextYearInstant": "次年度時点",
        "Next2YearInstant": "次々年度時点",
        "NextAccumulatedQ1Instant": "次年度期初から第１四半期間時点",
        "NextAccumulatedQ2Instant": "次年度期初から第２四半期間時点",
        "NextAccumulatedQ3Instant": "次年度期初から第３四半期間時点",
        "PriorYearInstant": "前年度時点",
        "PriorAccumulatedQ1Instant": "前年度期初から第１四半期間時点",
        "PriorAccumulatedQ2Instant": "前年度期初から第２四半期間時点",
        "PriorAccumulatedQ3Instant": "前年度期初から第３四半期間時点",
    }

    # Memberラベル情報を取得する関数
    def get_label_value(context: str) -> str:
        statement = select(IxLabelValue.label).where(
            IxLabelValue.xlink_label.like(f"%\_{context}%"),
            IxLabelValue.xlink_role == "http://www.xbrl.org/2003/role/label",
        )
        result = session.exec(statement)
        label = result.first()

        if label is None:
            raise ValueError(
                f"Memberラベル情報が取得できませんでした。context: {context}"
            )

        return label

    # name_listをnameをキーとした辞書に変換
    print("name_listをnameをキーとした辞書に変換します。")
    name_dict = {}
    for name, context, name_label in name_list:
        print(f"name: {name}, context: {context}, name_label: {name_label}")
        count = 0
        context_list = context.split("_")
        label = ""
        is_label = True
        for cont in context_list:
            if count == 0:
                try:
                    label = label + context_label[context.split("_")[0]]
                except KeyError:
                    label = ""
            elif count > 0:
                try:
                    label = label + get_label_value(cont)
                except ValueError:
                    is_label = False
            count += 1
        if is_label:
            if name in name_dict:
                name_dict[name]["item"].append({"context": context, "label": label})
            else:
                name_dict[name] = {
                    "label": name_label,
                    "item": [{"context": context, "label": label}],
                }

    return name_dict
