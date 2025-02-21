from collections import defaultdict
from typing import Any, Dict, List

from sqlmodel import Session

from app.models import IxHeadTitle

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


def get_summary_items(
    session: Session,
    head_item_key: str,
    attr_value_dict: Dict[str, str],
    from_name_dict: Dict[str, str],
) -> tuple[sc.FinancialResponseSchema, List[str]]:
    """
    #### この関数は、指定された条件に一致するiXBRLの非分数情報を取得する関数です。
    - **機能**:指定された条件に一致するiXBRLの非分数情報を取得します。
    - **引数**:session: Session, head_item_key: str, attr_value_dict: Dict[str, str], from_name_dict: Dict[str, str]
    - **戻り値**:sc.FinancialResponseSchema, List[str]
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

    child_items = {
        item.xlink_to: item.xlink_from
        for item in tree_items.data
        if item.xlink_from in parent_items
    }

    contexts = get_context_list(tree_items, attr_value)

    ix_non_fractions = crud.get_ix_non_fraction_records(
        session=session,
        head_item_key=head_item_key,
        names=child_items.keys(),
        contexts=contexts,
    )

    schema_items: List[sc.MetricParentSchema] = []
    for item in tree_items.data:
        if item.xlink_from == from_name:
            schema_items.append(
                sc.MetricParentSchema(
                    name=item.xlink_to,
                    order=item.xlink_order,
                    label=item.to_label,
                )
            )
    for item in ix_non_fractions:
        for schema_item in schema_items:
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

    company = get_company_schema(head_item)

    from_labels = [
        item.to_label for item in tree_items.data if item.xlink_from == from_name
    ]

    return (
        sc.FinancialResponseSchema(company=company, metrics=schema_items),
        from_labels,
    )
