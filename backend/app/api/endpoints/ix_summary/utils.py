from collections import defaultdict
from typing import Any, Dict, List

from sqlmodel import Session

from app.models import IxHeadTitle, IxNonFraction

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


def get_company_schema(item: IxHeadTitle) -> sc.CompanySchema:
    """
    #### この関数は、IxHeadTitleからCompanySchemaを取得する関数です。
    - **機能**:IxHeadTitleからCompanySchemaを取得します。
    - **引数**:item: IxHeadTitle
    - **戻り値**:sc.CompanySchema
    """

    item_dict = {
        "code": item.securities_code,
        "name": item.company_name,
        "accountingStandard": item.report_type,
        "fiscalYear": item.fy_year_end,
        "fiscalQuarter": item.current_period,
    }

    return sc.CompanySchema(**item_dict)


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
    - **戻り値**:List[sc.MetricParentSchema]
    """

    # キーのバリデーションを行い、エラーがあれば例外を発生させる
    if not list(attr_value_dict.keys()).__eq__(["FY", "QU"]):
        raise NotDictKeyError("not dict keys error. keys must be 'FY' or 'QU'.")
    if not list(from_name_dict.keys()).__eq__(["consolidated", "non_consolidated"]):
        raise NotDictKeyError(
            "not dict keys error. keys must be 'consolidated' or 'non_consolidated'."
        )

    head_item = crud.get_ix_head_title_by_item_key(
        session=session, item_key=head_item_key
    )

    if head_item.current_period is None:
        raise HeadItemNotFound("head item not found.")
    elif head_item.current_period == "FY":
        attr_value = attr_value_dict["FY"]
    else:
        attr_value = attr_value_dict["QU"]

    tree_items = crud.read_tree_items(
        head_item_key=head_item_key,
        attr_value=attr_value,
        session=session,
        xbrl_type="sm",
    )

    is_consolidated = any(
        item.xlink_to == "tse-ed-t_ConsolidatedMember" for item in tree_items.data
    )

    if is_consolidated:
        from_name = from_name_dict["consolidated"]
    else:
        from_name = from_name_dict["non_consolidated"]

    parent_items = [
        item.xlink_to for item in tree_items.data if item.xlink_from == from_name
    ]
    if is_change:
        child_items = {
            item.xlink_to: item.xlink_from
            for item in tree_items.data
            if item.xlink_from in parent_items
        }
    else:
        child_items = {
            item.xlink_to: item.xlink_to
            for item in tree_items.data
            if item.xlink_from == from_name
        }
    contexts = get_context_list(tree_items, attr_value)

    ix_non_fractions = crud.get_ix_non_fraction_records(
        session=session,
        head_item_key=head_item_key,
        names=child_items.keys(),
        contexts=contexts,
    )

    schema_items: sc.MetricItems = sc.MetricItems(data=[])
    upper_schema_items: sc.MetricItems = sc.MetricItems(data=[])
    lower_schema_items: sc.MetricItems = sc.MetricItems(data=[])
    for item in tree_items.data:
        if item.xlink_from == from_name:
            schema_items.data.append(create_metric_parent_schema(item))
            upper_schema_items.data.append(create_metric_parent_schema(item))
            lower_schema_items.data.append(create_metric_parent_schema(item))

    metric_contexts = ["ResultMember", "ForecastMember"]
    upper_contexts = ["UpperMember"]
    lower_contexts = ["LowerMember"]
    contexts_list = [metric_contexts, upper_contexts, lower_contexts]
    schema_items_dict = {
        metric_contexts.__str__(): schema_items,
        upper_contexts.__str__(): upper_schema_items,
        lower_contexts.__str__(): lower_schema_items,
    }

    for item in ix_non_fractions:
        for contexts in contexts_list:
            if bool(set(item.context) & set(contexts)):
                for schema_item in schema_items_dict[contexts.__str__()].data:
                    if schema_item.name == child_items[item.name]:
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
                        if item.numeric is not None:
                            schema_items_dict[contexts.__str__()].is_active = True

    period = sc.PeriodSchema(
        accountingStandard=head_item.report_type,
        fiscalYear=head_item.fy_year_end,
        period=head_item.current_period,
    )

    return sc.FinancialResponseSchema(
        period=period,
        metrics=schema_items,
        upperMetrics=upper_schema_items,
        lowerMetrics=lower_schema_items,
    )


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
        for metric in item.metrics.data:
            labels.append(sc.LabelItemSchema(label=metric.label))

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
