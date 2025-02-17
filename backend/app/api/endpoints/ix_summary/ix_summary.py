from collections import defaultdict
from itertools import product
from typing import Any, Dict, List

from fastapi import APIRouter, HTTPException, Query
from sqlalchemy import func
from sqlalchemy.orm import aliased
from sqlmodel import and_, case, exists, literal, or_, select

import app.schema as sc
from app.api.deps import SessionDep
from app.models import (
    IxDefinitionArc,
    IxDefinitionLoc,
    IxHeadTitle,
    IxLabelArc,
    IxLabelLoc,
    IxLabelValue,
    IxNonFraction,
    IxNonNumeric,
    ScLinkBaseRef,
)

router = APIRouter()


@router.get(
    "/doc/info/{code}",
    response_model=sc.ix_summary.IxDocumentInfoList,
    summary="XBRL文書情報を取得",
)
def get_document_info(
    *, session: SessionDep, code: str
) -> sc.ix_summary.IxDocumentInfoList:
    """
    ## XBRL文書情報を取得するエンドポイント
    - **機能**: 証券コードからXBRL文書情報を取得します。
    - **認証不要**
    - **レスポンス形式**: JSON
    - **param1**: code: str 必須項目
    """

    statement = select(IxHeadTitle).where(IxHeadTitle.securities_code == code)
    result = session.exec(statement)
    items = result.all()

    return sc.ix_summary.IxDocumentInfoList(data=items, count=len(items))


@router.get(
    "/tree/menus/{head_item_key}",
    response_model=sc.ix_summary.MenuLabelList,
    summary="attr_valueと日本語ラベルを取得",
)
def read_menu_labels(
    *, head_item_key: str, xbrl_type: str, session: SessionDep
) -> sc.ix_summary.MenuLabelList:
    """
    ## attr_valueと日本語ラベルを取得するエンドポイント
    - **機能**: HeadItemKeyからattr_valueと日本語ラベルを取得します。
    - **認証不要**
    - **レスポンス形式**: JSON
    - **param1**: head_item_key: str 必須項目
    - **param2**: xbrl_type: str 必須項目
    """

    statement = (
        select(IxDefinitionArc.attr_value, IxLabelValue.label)
        .join(
            ScLinkBaseRef,
            IxDefinitionArc.head_item_key == ScLinkBaseRef.head_item_key,
        )
        .join(
            IxDefinitionLoc,
            and_(
                IxDefinitionArc.source_file_id == IxDefinitionLoc.source_file_id,
                IxDefinitionArc.xlink_from == IxDefinitionLoc.xlink_label,
            ),
        )
        .join(
            IxLabelLoc,
            and_(
                IxLabelLoc.source_file_id == ScLinkBaseRef.href_source_file_id,
                IxLabelLoc.xlink_href == IxDefinitionLoc.xlink_href,
            ),
        )
        .join(
            IxLabelArc,
            and_(
                IxLabelArc.source_file_id == IxLabelLoc.source_file_id,
                IxLabelArc.xlink_from == IxLabelLoc.xlink_label,
            ),
        )
        .join(
            IxLabelValue,
            and_(
                IxLabelValue.source_file_id == IxLabelArc.source_file_id,
                IxLabelValue.xlink_label == IxLabelArc.xlink_to,
            ),
        )
        .where(
            IxDefinitionArc.head_item_key == head_item_key,
            IxLabelValue.xlink_role == "http://www.xbrl.org/2003/role/label",
            IxDefinitionArc.xlink_arcrole == "http://xbrl.org/int/dim/arcrole/all",
            ScLinkBaseRef.xbrl_type == xbrl_type,
        )
        .order_by(IxDefinitionArc.id)
    )

    results = session.exec(statement)
    items = results.all()

    if items is None:
        raise HTTPException(status_code=404, detail="Items not found")

    return sc.ix_summary.MenuLabelList(data=items, count=len(items))


@router.get(
    "/tree/items/{head_item_key}",
    response_model=sc.ix_summary.TreeItemsList,
    summary="表示リンクアイテムを取得",
)
def read_tree_items(
    *,
    head_item_key: str,
    attr_value: str = Query(None),
    has_children: bool = Query(None),
    xlink_arcrole: str = Query(None),
    xbrl_type: str = Query("sm"),
    session: SessionDep,
) -> sc.ix_summary.TreeItemsList:
    """
    ## 表示リンクアイテムを取得するエンドポイント
    - **機能**: HeadItemKeyから表示リンクのツリーアイテム一覧を取得します。
    - **認証不要**
    - **レスポンス形式**: JSON
    - **param1**: head_item_key: str 必須項目
    - **param2**: attr_value: str 任意項目
    - **param3**: has_children: bool 任意項目
    - **param4**: xlink_arcrole: str 任意項目
    - **param5**: xbrl_type: str 任意項目
    """

    scl1 = aliased(ScLinkBaseRef)
    scl2 = aliased(ScLinkBaseRef)
    ida1 = aliased(IxDefinitionArc)
    ida2 = aliased(IxDefinitionArc)
    ida3 = aliased(IxDefinitionArc)
    idl1 = aliased(IxDefinitionLoc)
    idl2 = aliased(IxDefinitionLoc)
    idl3 = aliased(IxDefinitionLoc)
    idl4 = aliased(IxDefinitionLoc)

    # 再帰的CTEの定義
    tree_h = (
        select(
            ida1.id,
            ida1.xlink_from,
            ida1.xlink_to,
            ida1.head_item_key,
            ida1.attr_value,
            ida1.xlink_arcrole,
            ida1.source_file_id,
            ida1.xlink_order,
            idl1.xlink_href.label("from_href"),
            idl2.xlink_href.label("to_href"),
            literal(1).label("level"),  # ツリー深さの初期値
        )
        .join(
            idl1,
            and_(
                ida1.head_item_key == idl1.head_item_key,
                ida1.source_file_id == idl1.source_file_id,
                ida1.xlink_from == idl1.xlink_label,
                ida1.attr_value == idl1.attr_value,
            ),
        )
        .join(
            idl2,
            and_(
                ida1.head_item_key == idl2.head_item_key,
                ida1.source_file_id == idl2.source_file_id,
                ida1.xlink_to == idl2.xlink_label,
                ida1.attr_value == idl2.attr_value,
            ),
        )
        .join(
            scl1,
            and_(
                ida1.head_item_key == scl1.head_item_key,
                ida1.source_file_id == scl1.href_source_file_id,
            ),
        )
        .where(
            ida1.head_item_key == head_item_key,
            ida1.xlink_from
            == (
                select(ida2.xlink_from)
                .where(
                    and_(
                        ida2.head_item_key == head_item_key,
                        ida2.xlink_arcrole == "http://xbrl.org/int/dim/arcrole/all",
                        ida1.source_file_id == ida2.source_file_id,
                        ida1.attr_value == ida2.attr_value,
                    )
                )
                .scalar_subquery()
            ),
        )
    )

    if attr_value:
        tree_h = tree_h.where(ida1.attr_value == attr_value)
    if xbrl_type:
        tree_h = tree_h.where(scl1.xbrl_type == xbrl_type)

    tree_h = tree_h.cte(name="tree_h", recursive=True)  # 再帰CTEの定義

    tree_h_alias = aliased(tree_h)

    recursive = (
        select(
            ida3.id,
            ida3.xlink_from,
            ida3.xlink_to,
            ida3.head_item_key,
            ida3.attr_value,
            ida3.xlink_arcrole,
            ida3.source_file_id,
            ida3.xlink_order,
            idl3.xlink_href.label("from_href"),  # リンク先の更新
            idl4.xlink_href.label("to_href"),  # リンク元の更新
            (tree_h_alias.c.level + 1).label("level"),  # ツリー深さの更新
        )
        .join(
            idl3,
            and_(
                ida3.head_item_key == idl3.head_item_key,
                ida3.source_file_id == idl3.source_file_id,
                ida3.xlink_from == idl3.xlink_label,
                ida3.attr_value == idl3.attr_value,
            ),
        )
        .join(
            idl4,
            and_(
                ida3.head_item_key == idl4.head_item_key,
                ida3.source_file_id == idl4.source_file_id,
                ida3.xlink_to == idl4.xlink_label,
                ida3.attr_value == idl4.attr_value,
            ),
        )
        .join(
            tree_h_alias,
            and_(
                idl3.head_item_key == tree_h_alias.c.head_item_key,
                idl3.xlink_href == tree_h_alias.c.to_href,
                idl3.attr_value == tree_h_alias.c.attr_value,
            ),
        )
        .join(
            scl2,
            and_(
                ida3.head_item_key == scl2.head_item_key,
                ida3.source_file_id == scl2.href_source_file_id,
            ),
        )
        .where(
            ida3.head_item_key == head_item_key,
        )
    )

    if attr_value:
        recursive = recursive.where(ida3.attr_value == attr_value)
    if xbrl_type:
        recursive = recursive.where(scl2.xbrl_type == xbrl_type)

    tree_h = tree_h.union_all(recursive)  # 再帰CTEの結合

    # 最終的なクエリの構築
    final_query = (
        select(
            tree_h.c.id,
            tree_h.c.from_href.label("xlink_from"),  # リンク元の更新
            tree_h.c.to_href.label("xlink_to"),  # リンク先の更新
            tree_h.c.attr_value,
            func.split_part(tree_h.c.xlink_arcrole, "/", 7).label(
                "xlink_arcrole"
            ),  # リンクアークロールの取得
            tree_h.c.xlink_order,
            tree_h.c.level,
            case(  # 子要素の有無を判定
                (
                    exists().where(tree_h_alias.c.from_href == tree_h.c.to_href),
                    True,
                ),
                else_=False,
            ).label("has_children"),
        )
        .select_from(tree_h)
        .order_by(tree_h.c.id)
    )

    if has_children is not None:  # 子要素の有無でフィルタリング
        final_query = final_query.where(
            case(
                (
                    exists().where(tree_h_alias.c.from_href == tree_h.c.to_href),
                    True,  # 子要素がある場合
                ),
                else_=False,  # 子要素がない場合
            ).label("has_children")
            == has_children
        )
    if xlink_arcrole:
        xlink_arcrole_str = f"http://xbrl.org/int/dim/arcrole/{xlink_arcrole}"
        final_query = final_query.where(tree_h.c.xlink_arcrole == xlink_arcrole_str)

    # クエリの実行
    results = session.exec(final_query)
    items = results.all()

    if items is None:
        raise HTTPException(status_code=404, detail="Items not found")

    return sc.ix_summary.TreeItemsList(data=items, count=len(items))


@router.get(
    "/tree/contexts/{head_item_key}",
    response_model=Dict,
    summary="コンテキストリストを取得",
)
def read_context_list(
    *, head_item_key: str, attr_value: str = Query(None), session: SessionDep
) -> Dict:
    """
    ## コンテキストリストを取得するエンドポイント
    - **機能**: HeadItemKeyからコンテキストリストを取得します。
    - **認証不要**
    - **レスポンス形式**: JSON
    - **param1**: head_item_key: str 必須項目
    """

    arcrole = "dimension-domain"

    data = read_tree_items(
        head_item_key=head_item_key,
        xlink_arcrole=arcrole,
        session=session,
        attr_value=attr_value,
        has_children=False,
        xbrl_type="sm",
    ).data

    dict_data = defaultdict(lambda: defaultdict(list))

    for item in data:
        dict_data[item.attr_value][item.xlink_from].append(item.xlink_to.split("_")[-1])

    return dict_data


@router.get(
    "/tree/names/{head_item_key}", response_model=Dict, summary="名前リストを取得"
)
def read_names(
    *, head_item_key: str, attr_value: str = Query(None), session: SessionDep
) -> Dict:
    """
    ## 名前リストを取得するエンドポイント
    - **機能**: HeadItemKeyから名前リストを取得します。
    - **認証不要**
    - **レスポンス形式**: JSON
    - **param1**: head_item_key: str 必須項目
    """

    arcrole = "domain-member"

    data = read_tree_items(
        head_item_key=head_item_key,
        xlink_arcrole=arcrole,
        session=session,
        has_children=None,
        xbrl_type="sm",
        attr_value=attr_value,
    ).data

    dict_data = defaultdict(list)

    for item in data:
        dict_data[item.attr_value].append(
            {
                "to": item.xlink_to,
                "from": item.xlink_from,
                "order": item.xlink_order,
                "level": item.level,
                "has_children": item.has_children,
            }
        )

    return dict_data


@router.get(
    "/Company/{HeadItemKey}",
    response_model=sc.ix_summary.CompanySchema,
    summary="企業情報を取得",
)
def get_company(
    *, HeadItemKey: str, session: SessionDep
) -> sc.ix_summary.CompanySchema:
    """
    ## 企業情報を取得するエンドポイント
    - **機能**: HeadItemKeyから企業情報を取得します。
    - **認証不要**
    - **レスポンス形式**: JSON
    - **param1**: HeadItemKey: str 必須項目
    """

    statement = select(IxHeadTitle).where(IxHeadTitle.item_key == HeadItemKey)
    result = session.exec(statement)
    item = result.first()

    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    item_dict = {
        "code": item.securities_code,
        "name": item.company_name,
        "accountingStandard": item.report_type,
        "fiscalYear": item.fy_year_end,
        "fiscalQuarter": item.current_period,
    }

    return sc.ix_summary.CompanySchema(**item_dict)


def get_label(
    *,
    head_item_key: str,
    names: List[str],
    session: SessionDep,
) -> Dict[str, str]:

    statement = (
        select(ScLinkBaseRef, IxLabelValue.label, IxLabelLoc.xlink_href)
        .join(
            IxLabelArc,
            and_(
                IxLabelValue.source_file_id == IxLabelArc.source_file_id,
                IxLabelValue.xlink_label == IxLabelArc.xlink_to,
            ),
        )
        .join(
            IxLabelLoc,
            and_(
                IxLabelValue.source_file_id == IxLabelLoc.source_file_id,
                IxLabelArc.xlink_from == IxLabelLoc.xlink_label,
            ),
        )
        .where(
            ScLinkBaseRef.head_item_key == head_item_key,
            ScLinkBaseRef.xbrl_type == "sm",
            IxLabelValue.source_file_id == ScLinkBaseRef.href_source_file_id,
            IxLabelLoc.xlink_href.in_(names),
            IxLabelValue.xlink_role == "http://www.xbrl.org/2003/role/label",
        )
    )
    result = session.exec(statement)
    items = result.all()

    if items is None:
        raise HTTPException(status_code=404, detail="Items not found")

    return {item.xlink_href: item.label for item in items}


@router.get(
    "/summary/operatingResults/{HeadItemKey}/{attr_type}",
    response_model=sc.ix_summary.FinancialResponseSchema,
    summary="経営成績を取得",
)
def get_operating_results(
    *,
    HeadItemKey: str,
    attr_type: str,
    session: SessionDep,
) -> sc.ix_summary.FinancialResponseSchema:
    """
    ## 経営成績を取得するエンドポイント
    - **機能**: HeadItemKeyから経営成績を取得します。
    - **認証不要**
    - **レスポンス形式**: JSON
    - **param1**: HeadItemKey: str 必須項目
    """

    attr_type_dict = {
        "operatingResults": {
            "attr_value": [  # ここで取得する属性値を指定
                "BusinessResultsOperatingResults",
                "BusinessResultsQuarterlyOperatingResults",
            ],
            "from_name": "StatementsInformationAbstract",
        },
        "Forecast": {
            "attr_value": [  # ここで取得する属性値を指定
                "BusinessResultsForecast",
                "BusinessResultsQuarterlyForecast",
            ],
            "from_name": "StatementsInformationAbstract",
        },
    }

    statement = select(IxDefinitionArc.attr_value).where(
        IxDefinitionArc.head_item_key == HeadItemKey,
        IxDefinitionArc.xlink_arcrole == "http://xbrl.org/int/dim/arcrole/all",
        IxDefinitionArc.attr_value.in_(attr_type_dict[attr_type]["attr_value"]),
    )
    result = session.exec(statement)
    attr_value = result.first()

    contexts = read_context_list(
        head_item_key=HeadItemKey, attr_value=attr_value, session=session
    )[attr_value]

    names = read_names(
        head_item_key=HeadItemKey, attr_value=attr_value, session=session
    )[attr_value]

    context_list = product(*contexts.values())

    context_list = [list(context) for context in context_list]

    names_to_list = [name["to"] for name in names]

    to_from_dict = {name["to"]: name["from"] for name in names}

    to_order_dict = {name["to"]: name["order"] for name in names}

    from_list = list(set(to_from_dict.values()))

    statement = select(IxNonFraction).where(
        IxNonFraction.head_item_key == HeadItemKey,
        IxNonFraction.name.in_(names_to_list),
        func.array_to_string(IxNonFraction.context, ",").not_ilike("%Prior%"),
    )

    if context_list:
        if type(context_list[0]) == str:
            print("str")
            statement = statement.where(
                IxNonFraction.context.op("@>")(context_list),
            )
        elif type(context_list[0]) == list:
            print("list")
            or_conditions = [
                IxNonFraction.context.op("@>")(context) for context in context_list
            ]
            statement = statement.where(or_(*or_conditions))

    result = session.exec(statement)
    items = result.all()

    print(items)

    if items is None:
        raise HTTPException(status_code=404, detail="Items not found")

    parentLabels = get_label(
        head_item_key=HeadItemKey, names=from_list, session=session
    )

    parentList = []
    for from_item in from_list:
        try:
            if to_from_dict[from_item].startswith(
                "tse-ed-t_Note"
            ):  # ここで取得する属性値を指定
                continue
            # elif to_from_dict[from_item].endswith(
            #     attr_type_dict[attr_type]["from_name"]
            # ):  # ここで取得する属性値を指定
            parentList.append(
                {
                    "name": from_item,
                    "order": to_order_dict[from_item],
                    "label": parentLabels[from_item],
                }
            )
        except KeyError:
            continue
            print(HeadItemKey)
    parentList = sorted(parentList, key=lambda x: x["order"])

    for item in items:
        for parent in parentList:
            try:
                if to_from_dict[item.name] == parent["name"]:
                    item_dict = {
                        "key": item.item_key,
                        "name": item.name,
                        "value": item.numeric,
                        "unit": item.unit_ref,
                    }
                    if item.name.startswith("tse-ed-t_ChangeIn"):
                        parent["change"] = item_dict
                    else:
                        parent["value"] = item_dict
            except KeyError:
                continue

    company = get_company(HeadItemKey=HeadItemKey, session=session)

    print(parentList)

    return sc.ix_summary.FinancialResponseSchema(company=company, metrics=parentList)


@router.get(
    "/operatingResults/{code}",
    response_model=sc.ix_summary.FinancialResponseSchema,
    summary="証券コードから経営成績を取得",
)
def get_operating_results_by_code(
    *,
    code: str,
    year: str = Query(None),
    period: str = Query(None),
    attr_type: str = Query("operatingResults"),
    session: SessionDep,
) -> sc.ix_summary.FinancialResponseSchema:
    """
    ## 証券コードから経営成績を取得するエンドポイント
    - **機能**: 証券コードから経営成績を取得します。
    - **認証不要**
    - **レスポンス形式**: JSON
    - **param1**: code: str 必須項目
    - **param2**: year: str 任意項目
    - **param3**: period: str 任意項目
    """

    if year and period:
        statement = (
            select(IxHeadTitle)
            .where(
                IxHeadTitle.securities_code == code,
                IxHeadTitle.fy_year_end.startswith(year),
                IxHeadTitle.current_period == period,
            )
            .order_by(IxHeadTitle.report_type.desc(), IxHeadTitle.current_period.desc())
        )
    elif year:
        statement = (
            select(IxHeadTitle)
            .where(
                IxHeadTitle.securities_code == code,
                IxHeadTitle.fy_year_end.startswith(year),
                IxHeadTitle.current_period is not None,
            )
            .order_by(IxHeadTitle.report_type.desc(), IxHeadTitle.current_period.desc())
        )
    elif period:
        statement = (
            select(IxHeadTitle)
            .where(
                IxHeadTitle.securities_code == code,
                IxHeadTitle.current_period == period,
                IxHeadTitle.fy_year_end is not None,
            )
            .order_by(IxHeadTitle.report_type.desc(), IxHeadTitle.current_period.desc())
        )
    else:
        statement = (
            select(IxHeadTitle)
            .where(
                IxHeadTitle.securities_code == code,
                IxHeadTitle.current_period is not None,
            )
            .order_by(IxHeadTitle.report_type.desc(), IxHeadTitle.current_period.desc())
        )
    result = session.exec(statement)
    item = result.first()

    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    HeadItemKey = item.item_key

    return get_operating_results(
        HeadItemKey=HeadItemKey, attr_type=attr_type, session=session
    )
