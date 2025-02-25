from collections import defaultdict
from typing import Any, Dict, List

from sqlmodel import Session

from app.models import IxNonFraction

from . import crud
from . import schema as sc
from .exceptions import HeadItemNotFound, NotDictKeyError


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


def create_metric_parent_schema(item) -> sc.MetricParentSchema:
    return sc.MetricParentSchema(
        name=item.xlink_to,
        order=item.xlink_order,
        label=item.to_label,
    )


def get_metric_schema_value_and_change(
    items: List[IxNonFraction],
    schema_items: list[sc.MetricParentSchema],
    child_items: Dict[str, str],
    metric_contexts: List[str],
):
    for item in items:
        for schema_item in schema_items:
            if schema_item.name == child_items[item.name]:
                if bool(set(item.context) & set(metric_contexts)):
                    if item.name.startswith("tse-ed-t_ChangeIn"):
                        schema_item.change = sc.MetricSchema(
                            key=item.item_key,
                            name=item.name,
                            value=item.numeric,
                            unit=item.unit_ref,
                        )
                    else:
                        schema_item.value = sc.MetricSchema(
                            key=item.item_key,
                            name=item.name,
                            value=item.numeric,
                            unit=item.unit_ref,
                        )


def get_summary_items(
    session: Session,
    head_item_key: str,
    attr_value_dict: Dict[str, str],
    from_name_dict: Dict[str, str],
    is_change: bool = True,
) -> sc.FinancialResponseSchema:
    """
    #### この関数は、指定された条件に一致するiXBRLの非分数情報を取得する関数です。
    - **機能**:指定された条件に一致するiXBRLの非分数情報を取得します。
    - **引数**:session: Session, head_item_key: str, attr_value_dict: Dict[str, str], from_name_dict: Dict[str, str]
    - **戻り値**:sc.FinancialResponseSchema
    - **例外**:NotDictKeyError, HeadItem
    """

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

    # region tree_itemsの取得
    tree_items = crud.read_tree_items(
        head_item_key=head_item_key,
        attr_value=attr_value,
        session=session,
        xbrl_type="sm",
    )

    # region is_consolidatedの設定
    is_consolidated = any(  # is_consolidatedを取得
        item.xlink_to == "tse-ed-t_ConsolidatedMember" for item in tree_items.data
    )

    if is_consolidated:  # is_consolidatedがTrueの場合、from_nameを"consolidated"に設定
        from_name = from_name_dict["consolidated"]
    else:  # is_consolidatedがFalseの場合、from_nameを"non_consolidated"に設定
        from_name = from_name_dict["non_consolidated"]
    # endregion

    # region parent_itemsの取得
    parent_items = [
        item.xlink_to for item in tree_items.data if item.xlink_from == from_name
    ]

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

    # contextの取得
    context_list = get_context_list(tree_items, attr_value)

    # ix_non_fractionsの取得
    ix_non_fractions = crud.get_ix_non_fraction_records(
        session=session,
        head_item_key=head_item_key,
        names=child_items.keys(),
        contexts=context_list,
    )

    schema_items = {
        "result": sc.MetricItems(),
        "forecast": sc.MetricItems(),
        "upper": sc.MetricItems(),
        "lower": sc.MetricItems(),
    }

    for item in tree_items.data:
        if item.xlink_from == from_name:
            schema_items["result"].data.append(create_metric_parent_schema(item))
            schema_items["forecast"].data.append(create_metric_parent_schema(item))
            schema_items["upper"].data.append(create_metric_parent_schema(item))
            schema_items["lower"].data.append(create_metric_parent_schema(item))

    context_mapping = {
        "result": ["ResultMember"],
        "forecast": ["ForecastMember"],
        "upper": ["UpperMember"],
        "lower": ["LowerMember"],
    }

    for item in ix_non_fractions:
        for key, contexts in context_mapping.items():
            if bool(set(item.context) & set(contexts)):
                print(item.context, item.numeric)
                for schema_item in schema_items[key].data:
                    if schema_item.name == child_items[item.name]:
                        if item.numeric is not None:
                            schema_items[key].is_active = True
                        metric_schema = sc.MetricSchema(
                            key=item.item_key,
                            name=item.name,
                            value=item.numeric,
                            unit=item.unit_ref,
                        )
                        if item.name.startswith("tse-ed-t_ChangeIn"):
                            schema_item.change = metric_schema
                        else:
                            schema_item.value = metric_schema

    period = sc.PeriodSchema(  # periodを設定
        accountingStandard=head_item.report_type,
        fiscalYear=head_item.fy_year_end,
        period=head_item.current_period,
    )

    res = sc.FinancialResponseSchema(  # FinancialResponseSchemaを返す
        period=period,
        result=schema_items["result"],
        forecast=schema_items["forecast"],
        upper=schema_items["upper"],
        lower=schema_items["lower"],
    )

    return res


def get_header_labels(
    items: List[sc.FinancialResponseSchema],
) -> List[sc.LabelItemSchema]:
    """
    #### この関数は、ヘッダーラベルを取得する関数です。
    - **機能**:ヘッダーラベルを取得します。
    - **引数**:items: List[sc.FinancialResponseSchema]
    - **戻り値**:List[sc.LabelItemSchema
    """

    labels = []
    for item in items:
        for result in item.result.data:
            labels.append(sc.LabelItemSchema(label=result.label))

    return labels


def get_financial_response_list_schema(
    head_item_keys: List[str],
    session: Session,
    attr_value_dict: Dict[str, str],
    from_name_dict: Dict[str, str],
    is_change: bool = True,
) -> sc.FinancialResponseListSchema:
    """
    #### この関数は、FinancialResponseListSchemaを取得する関数です。
    - **機能**:FinancialResponseListSchemaを取得します。
    - **引数**:items: List[sc.FinancialResponseSchema]
    - **戻り値**:sc.FinancialResponseListSchema
    - **例外**:NotDictKeyError
    """

    items_list: List[sc.FinancialResponseSchema] = []
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

    labels = get_header_labels(items_list)

    return sc.FinancialResponseListSchema(
        data=items_list, count=len(items_list), labels=labels
    )


def get_head_item_key(
    session: Session,
    code: str,
) -> List[str]:
    """
    #### この関数は、指定された証券コードに一致するhead_item_keyを取得する関数です。
    - **機能**:指定された証券コードに一致するhead_item_keyを取得します。
    - **引数**:session: Session, code: str
    - **戻り値**:List[str]
    - **例外**:HeadItemNotFound
    """

    headItems = crud.get_ix_head_title_by_code(session=session, code=code)

    if len(headItems) == 0:
        raise HeadItemNotFound("Item not found")

    head_item_keys = [item.item_key for item in headItems]

    return head_item_keys
