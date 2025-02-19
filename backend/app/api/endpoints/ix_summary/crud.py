from typing import Any, List, Optional

from app.models import (
    IxDefinitionArc,
    IxDefinitionLoc,
    IxHeadTitle,
    IxLabelArc,
    IxLabelLoc,
    IxLabelValue,
    IxNonFraction,
    ScLinkBaseRef,
)
from sqlalchemy.orm import aliased
from sqlmodel import Session, and_, case, exists, func, literal, or_, select

from . import schema as sc


def get_ix_head_title(
    session: Session,
    code: str,
    year: Optional[str] = None,
    period: Optional[str] = None,
) -> Optional[IxHeadTitle]:
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

    return item


def get_ix_head_title_by_item_key(
    session: Session, item_key: str
) -> Optional[IxHeadTitle]:
    """
    #### IxHeadTitleテーブルからIDに紐づくレコードを取得する
    - **機能**: IDに紐づくIxHeadTitleテーブルのレコードを取得する
    - **param1**: session: Session  DBセッション
    - **param2**: item_key: str ID
    """
    statement = select(IxHeadTitle).where(IxHeadTitle.item_key == item_key)
    result = session.exec(statement)
    item = result.first()
    return item


def get_ix_head_title_by_code(session: Session, code: str) -> List[IxHeadTitle]:
    """
    #### IxHeadTitleテーブルから証券コードに紐づくレコードを取得する
    - **機能**: 証券コードに紐づくIxHeadTitleテーブルのレコードを取得する
    - **param1**: session: Session  DBセッション
    - **param2**: code: str 証券コード
    """
    statement = select(IxHeadTitle).where(IxHeadTitle.securities_code == code)
    result = session.exec(statement)
    items = result.all()
    return items


def get_attr_value(
    session: Session, head_item_key: str, attr_values: List[str]
) -> Optional[str]:
    """
    #### HeadItemKeyに紐づくattr_valueを取得する
    - **機能**: HeadItemKeyに紐づくattr_valueを取得する
    - **param1**: session: Session  DBセッション
    - **param2**: head_item_key: str ID
    - **param3**: attr_values: List[str] 属性値
    """

    statement = select(IxDefinitionArc.attr_value).where(
        IxDefinitionArc.head_item_key == head_item_key,
        IxDefinitionArc.xlink_arcrole == "http://xbrl.org/int/dim/arcrole/all",
        IxDefinitionArc.attr_value.in_(attr_values),
    )
    result = session.exec(statement)
    item = result.first()

    return item


def read_menu_labels(
    *, head_item_key: str, xbrl_type: str, session: Session
) -> sc.MenuLabelList:
    """
    #### attr_valueと日本語ラベルを取得するエンドポイント
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

    return items


def read_tree_items(
    *,
    head_item_key: str,
    attr_value: Optional[str],
    level: Optional[int] = None,
    has_children: Optional[bool],
    xlink_arcrole: Optional[str],
    xbrl_type: str = "sm",
    session: Session,
) -> sc.TreeItemsList:
    """
    #### 表示リンクアイテムを取得するエンドポイント
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

    if level:
        final_query = final_query.where(tree_h.c.level == level)
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

    return sc.TreeItemsList(count=len(items), data=items)


def get_label_by_names(session: Session, head_item_key: str, names: List[str]) -> Any:
    """
    #### IxLabelValueテーブルからIDに紐づくレコードを取得する
    - **機能**: IDに紐づくIxLabelValueテーブルのレコードを取得する
    - **param1**: session: Session  DBセッション
    - **param2**: head_item_key: str ID
    - **param3**: names: List[str] ラベル名
    """

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

    return items


def get_ix_non_fraction_records(
    session: Session,
    head_item_key: str,
    names: List[str],
    contexts: List[str] | List[List[str]],
) -> List[IxNonFraction]:
    """
    #### IxNonFractionテーブルから条件に紐づくレコードを取得する
    - **機能**: 条件に紐づくIxNonFractionテーブルのレコードを取得する
    - **param1**: session: Session  DBセッション
    - **param2**: head_item_key: str ID
    - **param3**: names: List[str] ラベル名
    - **param4**: contexts: List[str] コンテキスト
    """

    statement = select(IxNonFraction).where(
        IxNonFraction.head_item_key == head_item_key,
        IxNonFraction.name.in_(names),
        func.array_to_string(IxNonFraction.context, ",").not_ilike("%Prior%"),
    )

    if contexts:
        if type(contexts[0]) == str:
            statement = statement.where(
                IxNonFraction.context.op("@>")(contexts),
            )
        elif type(contexts[0]) == list:
            or_conditions = [
                IxNonFraction.context.op("@>")(context) for context in contexts
            ]
            statement = statement.where(or_(*or_conditions))

    result = session.exec(statement)
    items = result.all()

    return items
