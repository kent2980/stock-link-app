import json
from collections.abc import Sequence

from fastapi import Query
from sqlalchemy.orm import aliased
from sqlmodel import Session, and_, case, desc, exists, func, literal, select

from app.models import (
    IxDefinitionArc,
    IxDefinitionLoc,
    IxHeadTitle,
    IxHeadTitleSummary,
    IxLabelArc,
    IxLabelLoc,
    IxLabelValue,
    IxNonFraction,
    IxNonNumeric,
    ScLinkBaseRef,
)

from . import schema as sc


def get_ix_head_title_by_item_key(
    session: Session, item_key: str
) -> IxHeadTitle | None:
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


def get_ix_head_title_by_code(session: Session, code: str) -> list[IxHeadTitle]:
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


def get_ix_head_title(
    session: Session,
    code: str,
    report_types: list[str] | None = Query(None),
    current_period: str | None = None,
    year: str | None = None,
    offset: int = 0,
) -> IxHeadTitle | None:
    """
    #### IxHeadTitleテーブルから証券コードに紐づくレコードを取得する
    - **機能**: 証券コードに紐づくIxHeadTitleテーブルのレコードを取得する
    - **param1**: session: Session  DBセッション
    - **param2**: code: str 証券コード
    - **param3**: report_types: List[str] レポートタイプ
    - **param4**: offset: int オフセット
    - **return**: IxHeadTitle | None
    """
    statement = select(IxHeadTitle).where(
        IxHeadTitle.securities_code == code,
    )
    if report_types:
        statement = statement.where(
            IxHeadTitle.report_type.in_(report_types),
        )
    if current_period:
        statement = statement.where(
            IxHeadTitle.current_period == current_period,
        )
    if year:
        statement = statement.where(
            IxHeadTitle.fy_year_end.startswith(year),
        )
    statement = statement.order_by(
        desc(IxHeadTitle.id),
    )
    if offset < 0:
        print("Offset must be greater than or equal to 0")
        statement = statement.offset(offset)
    result = session.exec(statement)
    item = result.first()
    return item


def get_attr_value(
    session: Session, head_item_key: str, attr_values: list[str]
) -> str | None:
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


def read_tree_items(
    *,
    head_item_key: str,
    attr_value: str | None = None,
    level: int | None = None,
    has_children: bool | None = None,
    xlink_arcrole: str | None = None,
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
            IxLabelValue.label.label("to_label"),
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
        .join(
            ScLinkBaseRef,
            tree_h.c.head_item_key == ScLinkBaseRef.head_item_key,
        )
        .join(
            IxLabelLoc,
            and_(
                ScLinkBaseRef.href_source_file_id == IxLabelLoc.source_file_id,
                tree_h.c.to_href == IxLabelLoc.xlink_href,
            ),
        )
        .join(
            IxLabelArc,
            and_(
                IxLabelLoc.source_file_id == IxLabelArc.source_file_id,
                IxLabelLoc.xlink_label == IxLabelArc.xlink_from,
            ),
        )
        .join(
            IxLabelValue,
            and_(
                IxLabelArc.source_file_id == IxLabelValue.source_file_id,
                IxLabelArc.xlink_to == IxLabelValue.xlink_label,
            ),
        )
        .where(IxLabelValue.xlink_role == "http://www.xbrl.org/2003/role/label")
        .order_by(tree_h.c.xlink_order)
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


def get_ix_non_fraction_records(
    session: Session,
    head_item_key: str,
    names: list[str],
    contexts: list[str] | list[list[str]],
) -> Sequence[IxNonFraction]:
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
        # func.array_to_string(IxNonFraction.context, ",").not_ilike("%Prior%"),
    )

    if contexts:
        if isinstance(contexts[0], str):
            statement = statement.where(
                IxNonFraction.context.op("@>")(contexts),
            )
        elif isinstance(contexts[0], list):
            or_conditions = [
                IxNonFraction.context.op("&&")(context) for context in contexts
            ]
            statement = statement.where(and_(*or_conditions))

    result = session.exec(statement)
    items = result.all()

    return items


def is_change_value(
    session: Session, head_item_key: str, names: list[str]
) -> bool | None:
    """
    #### 予想変更の有無を取得する
    - **機能**: 予想変更の有無を取得する
    - **param1**: session: Session  DBセッション
    - **param2**: head_item_key: str ID
    - **param3**: names: List[str] ラベル名
    """

    statement = select(IxNonNumeric).where(
        IxNonNumeric.head_item_key == head_item_key,
        IxNonNumeric.name.in_(names),
    )
    result = session.exec(statement)
    item = result.first()

    if not item:
        return None
    return item.value == "true"


def get_base_head_item_key_offset_item(
    session: Session,
    headItemKey: str,
    report_types: list[str] | None = None,
    offset: int = 0,
) -> str:
    statement = select(IxHeadTitle).where(
        IxHeadTitle.item_key == headItemKey,
    )
    result = session.exec(statement)
    item = result.first()

    # itemがNoneの場合は、エラーを返す
    if item is None:
        raise ValueError("Item not found")

    reporting_date = item.reporting_date
    code = item.securities_code
    current_period = item.current_period
    fy_year_end = item.fy_year_end

    if current_period is None:
        raise ValueError("Current period not found")
    if fy_year_end is None:
        raise ValueError("FY year end not found")

    if reporting_date is None and code is None:
        raise ValueError("Base reporting_date and Code not found")
    elif reporting_date is None:
        raise ValueError("Base reporting_date not found")
    elif code is None:
        raise ValueError("Code not found")

    statement = select(IxHeadTitle).where(
        IxHeadTitle.reporting_date.isnot(None),
        (IxHeadTitle.current_period, IxHeadTitle.fy_year_end)
        != (current_period, fy_year_end),
    )

    statement = (
        select(statement)
        .where(
            and_(
                statement.c.reporting_date < reporting_date,
                statement.c.securities_code == code,
            )
        )
        .order_by(
            desc(statement.c.reporting_date),
        )
    )

    if report_types:
        statement = statement.where(
            IxHeadTitle.report_type.in_(report_types),
        )

    statement = statement.offset(offset - 1)
    result = session.exec(statement)
    item = result.first()
    if item is None:
        raise ValueError("No previous item found")
    return item.item_key


def get_disclosure_items(
    session: Session, report_types: list[str], limit: int = 10, offset: int = 0
) -> Sequence[tuple[IxHeadTitle, IxHeadTitleSummary]]:
    """
    #### 開示項目情報を取得する
    - **機能**: 開示項目情報を取得する
    - **param1**: session: Session  DBセッション
    - **param2**: limit: int  取得する最大数
    - **param3**: offset: int  オフセット
    """

    statement = (
        select(IxHeadTitle, IxHeadTitleSummary)
        .outerjoin(
            IxHeadTitleSummary, IxHeadTitleSummary.head_item_key == IxHeadTitle.item_key
        )
        .where(
            IxHeadTitle.current_period.isnot(None),
            IxHeadTitle.company_name.isnot(None),
            IxHeadTitle.report_type.in_(report_types),
        )
        .order_by(
            desc(IxHeadTitle.reporting_date),
            desc(IxHeadTitle.insert_date),
        )
        .limit(limit)
        .offset(offset)  # オフセットを適用
    )
    result = session.exec(statement)
    items = result.all()
    return items


def get_disclosure_cursor(
    session: Session,
    report_types: list[str],
    limit: int = 10,
    cursor: int | None = None,
    direction: str = "order",
) -> sc.DisclosureCursor:
    """
    #### 開示項目情報を取得する
    - **機能**: 開示項目情報を取得する
    """

    if direction not in ["order", "newer"]:
        raise ValueError("Direction must be 'order' or 'newer'")

    statement = (
        select(IxHeadTitle, IxHeadTitleSummary)
        .outerjoin(
            IxHeadTitleSummary, IxHeadTitleSummary.head_item_key == IxHeadTitle.item_key
        )
        .where(
            IxHeadTitle.current_period.isnot(None),
            IxHeadTitle.company_name.isnot(None),
            IxHeadTitle.report_type.in_(report_types),
        )
        .order_by(
            desc(IxHeadTitle.reporting_date),
            desc(IxHeadTitle.insert_date),
        )
    )

    if cursor is not None:
        if direction == "order":
            statement = statement.where(IxHeadTitle.id > cursor)
        else:
            statement = statement.where(IxHeadTitle.id < cursor)

    statement = statement.limit(limit)

    result = session.exec(statement)
    items = result.all()

    next_cursor = items[0][0].id if items else None
    try:
        previous_cursor = items[limit - 1][0].id if items else None
    except IndexError:
        previous_cursor = None
    item_list = []

    for item in items:
        try:
            item_list.append(
                sc.DisclosureItem(
                    headItemKey=item[0].item_key,
                    item_id=item[0].id,
                    company=item[0].company_name,
                    code=item[0].securities_code,
                    reporting_date=item[0].reporting_date.strftime("%Y-%m-%d"),
                    insert_date=item[0].insert_date.strftime("%Y-%m-%d %H:%M:%S"),
                    title=item[0].document_name,
                    category=item[0].report_type,
                    summary=item[1].summary if item[1] else "",
                    important=True,
                    operating_result=(
                        json.loads(item[1].operating_result_json)
                        if item[1] and item[1].operating_result_json
                        else None
                    ),
                    forecast=(
                        json.loads(item[1].forecast_json)
                        if item[1] and item[1].forecast_json
                        else None
                    ),
                    cashflow=(
                        json.loads(item[1].cashflow_json)
                        if item[1] and item[1].cashflow_json
                        else None
                    ),
                )
            )
        except Exception as e:
            print(
                f"Error processing item ID {item[0].id}: {item[0].company_name} - {str(e)}"
            )
            continue

    return sc.DisclosureCursor(
        data=item_list,
        count=len(item_list),
        next_cursor=next_cursor,
        previous_cursor=previous_cursor,
    )


def get_disclosure_item_by_id(
    session: Session, report_types: list[str], item_id: int, limit: int = 5
) -> Sequence[tuple[IxHeadTitle, IxHeadTitleSummary]]:
    """
    #### 開示項目情報をIDで取得する
    - **機能**: 開示項目情報をIDで取得する
    - **param1**: session: Session  DBセッション
    - **param2**: report_types: List[str] レポートタイプ
    - **param3**: item_id: int  取得するID
    - **return**: Sequence[IxHeadTitle] 開示項目情報のリスト
    - **raises**: ValueError if no item found with the given ID
    """

    statement = (
        select(IxHeadTitle, IxHeadTitleSummary)
        .outerjoin(
            IxHeadTitleSummary, IxHeadTitleSummary.head_item_key == IxHeadTitle.item_key
        )
        .where(
            IxHeadTitle.id < item_id,
            IxHeadTitle.current_period.isnot(None),
            IxHeadTitle.company_name.isnot(None),
            IxHeadTitle.report_type.in_(report_types) if report_types else True,
        )
        .order_by(
            desc(IxHeadTitle.id),
        )
        .limit(limit)
    )

    result = session.exec(statement)
    items = result.all()
    if not items:
        raise ValueError("No item found with the given ID")
    return items
