import re
from collections import defaultdict
from typing import Dict, List, Optional

from sqlmodel import Session

from app.api.endpoints.ix_summary.crud import get_base_head_item_key_offset_item
from app.models import IxHeadTitle, IxNonFraction

from . import crud
from . import schema as sc
from .exceptions import HeadItemNotFound, NotDictKeyError
from .summaryItems import SummaryItems


def get_context_list(items: sc.TreeItemsList, attr_value: str) -> List[List[str]]:
    """
    #### この関数は、TreeItemsListからcontextのリストを取得する関数です。
    - **機能**:TreeItemsListからcontextのリストを取得します。
    - **引数**:items: TreeItemsList
    - **戻り値**:List[List[str]]
    """
    from_dict = defaultdict(list)
    for item in items.data:
        if item.attr_value == attr_value:
            if item.xlink_arcrole == "dimension-domain":
                from_dict[item.xlink_from].append(item.xlink_to.split("_")[-1])
    return list(from_dict.values())


def create_metric_parent_schema(item) -> sc.FinValueAbstractBase:
    return sc.FinValueAbstractBase(
        name=item.xlink_to,
        order=item.xlink_order,
        label=item.to_label,
    )


def get_metric_schema_value_and_change(
    items: List[IxNonFraction],
    schema_items: list[sc.FinValueAbstractBase],
    child_items: Dict[str, str],
    metric_contexts: List[str],
):
    for item in items:
        for schema_item in schema_items:
            if schema_item.name == child_items[item.name]:
                if bool(set(item.context) & set(metric_contexts)):
                    is_prior = any(
                        re.match(r"Prior.*", context) for context in item.context
                    )
                    valueBase = sc.FinValueBase(
                        name=item.name,
                        value=item.numeric,
                        unit=item.unit_ref,
                        display_scale=item.display_scale,
                        scale=item.scale,
                    )
                    if is_prior:
                        if item.name.startswith("tse-ed-t_ChangeIn"):
                            schema_item.preChange = valueBase
                        else:
                            schema_item.preValue = valueBase
                    else:
                        if item.name.startswith("tse-ed-t_ChangeIn"):
                            schema_item.curChange = valueBase
                        else:
                            schema_item.curValue = valueBase


def get_attr_value(head_item: IxHeadTitle, attr_value_dict: Dict[str, str]) -> str:

    # region attr_valueの設定
    if head_item.current_period is None:  # head_itemが存在しない場合、例外を発生させる
        raise HeadItemNotFound("head item not found.")
    elif (
        head_item.current_period == "FY"
    ):  # head_itemのcurrent_periodがFYの場合、attr_valueをFYに設定
        attr_value = attr_value_dict["FY"]
    else:  # head_itemのcurrent_periodがQUの場合、attr_valueをQUに設定
        attr_value = attr_value_dict["QU"]
    # endregion

    return attr_value


def get_from_name(from_name_dict: Dict[str, str], tree_items: sc.TreeItemsList) -> str:

    # region is_consolidatedの設定
    is_consolidated = any(  # is_consolidatedを取得
        item.xlink_to == "tse-ed-t_ConsolidatedMember" for item in tree_items.data
    )

    if is_consolidated:  # is_consolidatedがTrueの場合、from_nameを"consolidated"に設定
        from_name = from_name_dict["consolidated"]
    else:  # is_consolidatedがFalseの場合、from_nameを"non_consolidated"に設定
        from_name = from_name_dict["non_consolidated"]
    # endregion

    return from_name


def get_parent_items(tree_items: sc.TreeItemsList, from_name: str) -> List[str]:
    parent_items = [
        item.xlink_to for item in tree_items.data if item.xlink_from == from_name
    ]

    return parent_items


def get_child_items(
    tree_items: sc.TreeItemsList,
    from_name: str,
    is_change: bool,
    parent_items: List[str],
) -> Dict[str, str]:
    # region child_itemsの取得
    if is_change:  # is_changeがTrueの場合、child_itemsを取得
        child_items = {
            item.xlink_to: item.xlink_from
            for item in tree_items.data
            if item.xlink_from in parent_items
        }
    else:  # is_changeがFalseの場合、child_itemsを取得
        child_items = {
            item.xlink_to: item.xlink_to
            for item in tree_items.data
            if item.xlink_from == from_name
        }
    # endregion

    return child_items


def var_init(
    session: Session,
    head_item_key: str,
    attr_value_dict: Dict[str, str],
    from_name_dict: Dict[str, str],
    is_change: bool = True,
):

    # region 引数のバリデーション
    # キーのバリデーションを行い、エラーがあれば例外を発生させる
    if not list(attr_value_dict.keys()).__eq__(
        ["FY", "QU"]
    ):  # attr_value_dictのキーがFY, QUでない場合、例外を発生させる
        raise NotDictKeyError("not dict keys error. keys must be 'FY' or 'QU'.")
    if not list(from_name_dict.keys()).__eq__(
        ["consolidated", "non_consolidated"]
    ):  # from_name_dictのキーがconsolidated, non_consolidatedでない場合、例外を発生させる
        raise NotDictKeyError(
            "not dict keys error. keys must be 'consolidated' or 'non_consolidated'."
        )
    # endregion

    # region head_itemの取得
    head_item = crud.get_ix_head_title_by_item_key(  # head_itemを取得
        session=session, item_key=head_item_key
    )

    attr_value = get_attr_value(head_item, attr_value_dict)
    # region tree_itemsの取得
    tree_items = crud.read_tree_items(
        head_item_key=head_item_key,
        attr_value=attr_value,
        session=session,
        xbrl_type="sm",
    )

    # print(tree_items)

    from_name = get_from_name(from_name_dict, tree_items)

    # region parent_itemsの取得
    parent_items = get_parent_items(tree_items, from_name)

    child_items = get_child_items(
        tree_items=tree_items,
        from_name=from_name,
        is_change=is_change,
        parent_items=parent_items,
    )

    # contextの取得
    context_list = get_context_list(tree_items, attr_value)

    return (
        head_item,
        attr_value,
        tree_items,
        from_name,
        parent_items,
        child_items,
        context_list,
    )


def get_summary_items(
    session: Session,
    head_item_key: str,
    attr_value_dict: Dict[str, str],
    from_name_dict: Dict[str, str],
    is_change: bool = True,
) -> SummaryItems:
    """
    #### この関数は、指定された条件に一致するiXBRLの非分数情報を取得する関数です。
    - **機能**:指定された条件に一致するiXBRLの非分数情報を取得します。
    - **引数**:session: Session, head_item_key: str, attr_value_dict: Dict[str, str], from_name_dict: Dict[str, str]
    - **戻り値**:sc.FinStructBase
    - **例外**:NotDictKeyError, HeadItem
    """

    (
        head_item,
        attr_value,
        tree_items,
        from_name,
        parent_items,
        child_items,
        context_list,
    ) = var_init(
        session=session,
        head_item_key=head_item_key,
        attr_value_dict=attr_value_dict,
        from_name_dict=from_name_dict,
        is_change=is_change,
    )

    if tree_items.count == 0:
        raise HeadItemNotFound("Item not found")

    # ix_non_fractionsの取得
    ix_non_fractions = crud.get_ix_non_fraction_records(
        session=session,
        head_item_key=head_item_key,
        names=child_items.keys(),
        contexts=context_list,
    )

    items = SummaryItems(
        head_item=head_item,
        attr_value=attr_value,
        tree_items=tree_items,
        from_name=from_name,
        parent_items=parent_items,
        child_items=child_items,
        context_list=context_list,
        ix_non_fractions=ix_non_fractions,
    )

    return items


def get_struct(
    items: SummaryItems,
    struct: sc.FinStructBase,
) -> sc.FinStructBase:
    """
    #### この関数は、FinStructBaseを取得する関数です。
    - **機能**:FinStructBaseを取得します。
    - **引数**:head_item: Any, tree_items: sc.TreeItemsList, ix_non_fractions: List[IxNonFraction], from_name: str, child_items: Dict[str, str]
    - **戻り値**:sc.FinStructBase
    """

    # structがsc.FinStructBaseまたはその継承クラスでない場合、例外を発生させる
    if not isinstance(struct, sc.FinStructBase):
        raise TypeError("struct must be sc.FinStructBase or its subclass.")

    head_item = items.get_head_item()
    tree_items = items.get_tree_items()
    from_name = items.get_from_name()
    child_items = items.get_child_items()
    ix_non_fractions = items.get_ix_non_fractions()

    for item in tree_items.data:
        if item.xlink_from == from_name:
            for key in struct.__fields__.keys():
                field = getattr(struct, key)
                if isinstance(field, sc.FinItemsBase):
                    if item.xlink_from == from_name:
                        field.data.append(create_metric_parent_schema(item))

    if isinstance(struct, sc.FinStructBase):
        for item in ix_non_fractions:
            for key in struct.__fields__.keys():
                struct_default = getattr(struct, key)
                if isinstance(struct_default, sc.FinItemsBase):
                    context = struct_default.context
                    if context in item.context:
                        for struct_item in struct_default.data:
                            if struct_item.name == child_items[item.name]:
                                if item.numeric is not None:
                                    struct_default.is_active = True
                                metric_schema = sc.FinValueBase(
                                    name=item.name,
                                    value=item.numeric,
                                    unit=item.unit_ref,
                                    display_scale=item.display_scale,
                                    scale=item.scale,
                                )
                                is_prior = any(
                                    re.match(r"Prior.*", context)
                                    for context in item.context
                                )
                                if is_prior:
                                    if item.name.startswith("tse-ed-t_ChangeIn"):
                                        struct_item.preChange = metric_schema
                                    else:
                                        struct_item.preValue = metric_schema
                                else:
                                    if item.name.startswith("tse-ed-t_ChangeIn"):
                                        struct_item.curChange = metric_schema
                                    else:
                                        struct_item.curValue = metric_schema

    period = sc.PeriodSchemaBase(  # periodを設定
        accountingStandard=head_item.report_type,
        fiscalYear=head_item.fy_year_end,
        period=head_item.current_period,
    )

    struct.period = period
    struct.head_item_key = head_item.item_key

    return struct


def get_header_labels(items: List[sc.FinStructBase]) -> List[sc.LabelBase]:
    """
    #### この関数は、ヘッダーラベルを取得する関数です。
    - **機能**:ヘッダーラベルを取得します。
    - **引数**:items: List[sc.FinStructBase]
    - **戻り値**:List[sc.LabelBase]
    """

    labels = []
    for item in items:
        for key in item.__fields__.keys():
            field = getattr(item, key)
            if isinstance(field, sc.FinItemsBase):
                for result in field.data:
                    labels.append(sc.LabelBase(label=result.label))

    # labelsから重複を削除
    labels = list({label.label: label for label in labels}.values())

    return labels


def get_summary_items_list(
    head_item_keys: List[str],
    session: Session,
    attr_value_dict: Dict[str, str],
    from_name_dict: Dict[str, str],
    is_change: bool = True,
) -> List[SummaryItems]:
    """
    #### この関数は、FinResponseBaseを取得する関数です。
    - **機能**:FinResponseBaseを取得します。
    - **引数**:items: List[sc.FinStructBase]
    - **戻り値**:sc.FinResponseBase
    - **例外**:NotDictKeyError
    """

    items_list = []
    for head_item_key in head_item_keys:
        try:
            items = get_summary_items(
                session=session,
                head_item_key=head_item_key,
                attr_value_dict=attr_value_dict,
                from_name_dict=from_name_dict,
                is_change=is_change,
            )
            items_list.append(items)
        except HeadItemNotFound as e:
            continue
        except NotDictKeyError as e:
            raise NotDictKeyError(str(e))

    return items_list


def get_head_item_key(
    session: Session,
    code: str,
    report_types: Optional[List[str]],
    current_period: Optional[str] = None,
    year: Optional[str] = None,
    offset: int = 0,
) -> str:
    """
    #### この関数は、指定された証券コードに一致するhead_item_keyを取得する関数です。
    - **機能**:指定された証券コードに一致するhead_item_keyを取得します。
    - **引数**:session: Session
    - **引数**:code: str - 証券コード
    - **引数**:report_types: List[str]  - レポートタイプ
    - **引数**:offset: int - オフセット
    - **戻り値**:str - head_item_key
    - **例外**:HeadItemNotFound
    """

    headItems = crud.get_ix_head_title(
        session,
        code=code,
        report_types=report_types,
        offset=offset,
        current_period=current_period,
        year=year,
    )

    if not headItems:
        raise HeadItemNotFound("head item not found.")

    return headItems.item_key


def get_base_head_item_key_offset(
    session: Session,
    headItemKey: str,
    report_types: Optional[List[str]] = None,
    offset: int = 0,
) -> str:

    try:
        item = crud.get_base_head_item_key_offset_item(
            session=session,
            headItemKey=headItemKey,
            report_types=report_types,
            offset=offset,
        )
    except ValueError as e:
        raise HeadItemNotFound(f"head item not found.{str(e)}")

    return item
