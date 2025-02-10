from collections import defaultdict
from typing import Dict, List

from fastapi import APIRouter, HTTPException, Query
from sqlalchemy.orm import aliased
from sqlmodel import and_, case, exists, func, literal, select

import app.schema as sc
from app.api.deps import SessionDep
from app.models import (
    IxDefinitionArc,
    IxDefinitionLoc,
    IxLabelValue,
    IxNonFraction,
    IxNonNumeric,
    ScLinkBaseRef,
)

router = APIRouter()


@router.get(
    "/menu_labels/{head_item_key}",
    response_model=sc.ix_summary.MenuLabelList,
    summary="メニューラベルを取得",
)
def read_menu_labels(
    *, head_item_key: str, session: SessionDep
) -> sc.ix_summary.MenuLabelList:
    """
    ## メニューラベルを取得するエンドポイント
    - **機能**: HeadItemKeyからメニューラベル一覧を取得します。
    - **認証不要**
    - **レスポンス形式**: JSON
    - **param1**: head_item_key: str 必須項目
    """

    statement1 = (
        select(ScLinkBaseRef.href_source_file_id)
        .where(
            ScLinkBaseRef.head_item_key == head_item_key,
            ScLinkBaseRef.xbrl_type == "sm",
            ScLinkBaseRef.xlink_role
            == "http://www.xbrl.org/2003/role/definitionLinkbaseRef",
        )
        .subquery()
    )
    statement = (
        select(IxDefinitionArc.xlink_from, IxLabelValue.label)
        .join(
            statement1,
            IxDefinitionArc.source_file_id == statement1.c.href_source_file_id,
        )
        .join(
            IxLabelValue,
            IxLabelValue.xlink_label.startswith(
                "label_" + func.replace(IxDefinitionArc.xlink_from, "tse-ed-t_", "")
            ),
        )
        .where(
            IxDefinitionArc.xlink_arcrole == "http://xbrl.org/int/dim/arcrole/all",
            IxLabelValue.xlink_role == "http://www.xbrl.org/2003/role/label",
            IxDefinitionArc.xlink_from.not_like("%DocumentEntityInformationHeading%"),
        )
        .order_by(IxDefinitionArc.id)
    )

    result = session.exec(statement)
    items = result.all()

    if items is None:
        return sc.ix_summary.MenuLabelList(data=[])

    return sc.ix_summary.MenuLabelList(data=items, count=len(items))


@router.get(
    "/tree_items/{head_item_key}",
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
                select(ida2.xlink_from).where(
                    and_(
                        ida2.head_item_key == head_item_key,
                        ida2.xlink_arcrole == "http://xbrl.org/int/dim/arcrole/all",
                        ida1.source_file_id == ida2.source_file_id,
                        ida1.attr_value == ida2.attr_value,
                    )
                )
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
    print(has_children)
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
    "/tree_items/context_list/{head_item_key}",
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
    "/tree_items/names/{head_item_key}", response_model=Dict, summary="名前リストを取得"
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
        has_children=False,
        xbrl_type="sm",
        attr_value=attr_value,
    ).data

    dict_data = defaultdict(list)

    for item in data:
        dict_data[item.attr_value].append(item.xlink_to)

    return dict_data


@router.get(
    "/value/non_numeric/",
    response_model=sc.ix_non_numeric.IxNonNumericsPublic,
    summary="非数値リストを取得",
)
def read_non_numeric_values(
    *,
    head_item_key: str,
    attr_value: str,
    session: SessionDep,
) -> sc.ix_non_numeric.IxNonNumericsPublic:
    """
    ## 非数値リストを取得するエンドポイント
    - **機能**: HeadItemKeyから非数値リストを取得します。
    - **認証不要**
    - **レスポンス形式**: JSON
    - **param1**: head_item_key: str 必須項目
    - **param2**: attr_value: str 必須項目
    """

    context_list = read_context_list(
        head_item_key=head_item_key, attr_value=attr_value, session=session
    )
    names = read_names(
        head_item_key=head_item_key, attr_value=attr_value, session=session
    )

    statement = select(IxNonNumeric).where(
        IxNonNumeric.head_item_key == head_item_key,
        IxNonNumeric.name.in_(names[attr_value]),
    )

    results = session.exec(statement)
    items = results.all()

    if items is None:
        return sc.ix_non_numeric.IxNonNumericsPublic(data=[])

    return sc.ix_non_numeric.IxNonNumericsPublic(data=items, count=len(items))


@router.get(
    "/value/non_fraction/",
    response_model=sc.ix_non_fraction.IxNonFractionsPublic,
    summary="非分数値リストを取得",
)
def read_non_fraction_values(
    *,
    head_item_key: str,
    attr_value: str,
    session: SessionDep,
) -> sc.ix_non_fraction.IxNonFractionsPublic:
    """
    ## 非分数値リストを取得するエンドポイント
    - **機能**: HeadItemKeyから非分数値リストを取得します。
    - **認証不要**
    - **レスポンス形式**: JSON
    - **param1**: head_item_key: str 必須項目
    - **param2**: attr_value: str 必須項目
    """

    context_list = read_context_list(
        head_item_key=head_item_key, attr_value=attr_value, session=session
    )
    names = read_names(
        head_item_key=head_item_key, attr_value=attr_value, session=session
    )

    statement = select(IxNonFraction).where(
        IxNonFraction.head_item_key == head_item_key,
        IxNonFraction.name.in_(names[attr_value]),
    )

    results = session.exec(statement)
    items = results.all()

    if items is None:
        return sc.ix_non_fraction.IxNonFractionsPublic(data=[])

    return sc.ix_non_fraction.IxNonFractionsPublic(data=items, count=len(items))
