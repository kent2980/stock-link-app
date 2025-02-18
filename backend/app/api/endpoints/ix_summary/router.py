from collections import defaultdict
from itertools import product
from typing import Dict, List

from fastapi import APIRouter, HTTPException, Query

from app.api.deps import SessionDep

from . import crud
from . import schema as sc

router = APIRouter()


@router.get(
    "/doc/info/{code}",
    response_model=sc.IxDocumentInfoList,
    summary="XBRL文書情報を取得",
)
def get_document_info(*, session: SessionDep, code: str) -> sc.IxDocumentInfoList:
    """
    #### XBRL文書情報を取得するエンドポイント
    - **機能**: 証券コードからXBRL文書情報を取得します。
    - **認証不要**
    - **レスポンス形式**: JSON
    - **param1**: code: str 必須項目
    """

    items = crud.get_ix_head_title_by_code(session=session, code=code)

    return sc.IxDocumentInfoList(data=items, count=len(items))


@router.get(
    "/tree/items/{head_item_key}",
    response_model=sc.TreeItemsList,
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

    items = crud.read_tree_items(
        head_item_key=head_item_key,
        attr_value=attr_value,
        has_children=has_children,
        xlink_arcrole=xlink_arcrole,
        xbrl_type=xbrl_type,
        session=session,
    )

    if items is None:
        raise HTTPException(status_code=404, detail="Items not found")

    return sc.TreeItemsList(data=items, count=len(items))


@router.get(
    "/tree/contexts/{head_item_key}",
    response_model=Dict,
    summary="コンテキストリストを取得",
)
def read_context_list(
    *, head_item_key: str, attr_value: str = Query(None), session: SessionDep
) -> Dict:
    """
    #### コンテキストリストを取得するエンドポイント
    - **機能**: HeadItemKeyからコンテキストリストを取得します。
    - **認証不要**
    - **レスポンス形式**: JSON
    - **param1**: head_item_key: str 必須項目
    """

    arcrole = "dimension-domain"

    data = crud.read_tree_items(
        head_item_key=head_item_key,
        xlink_arcrole=arcrole,
        session=session,
        attr_value=attr_value,
        has_children=False,
        xbrl_type="sm",
    )

    dict_data = defaultdict(lambda: defaultdict(list))

    for item in data.data:
        dict_data[item.attr_value][item.xlink_from].append(item.xlink_to.split("_")[-1])

    return dict_data


@router.get(
    "/tree/names/{head_item_key}", response_model=Dict, summary="名前リストを取得"
)
def read_names(
    *, head_item_key: str, attr_value: str = Query(None), session: SessionDep
) -> Dict:
    """
    #### 名前リストを取得するエンドポイント
    - **機能**: HeadItemKeyから名前リストを取得します。
    - **認証不要**
    - **レスポンス形式**: JSON
    - **param1**: head_item_key: str 必須項目
    """

    arcrole = "domain-member"

    data = crud.read_tree_items(
        head_item_key=head_item_key,
        xlink_arcrole=arcrole,
        session=session,
        has_children=None,
        xbrl_type="sm",
        attr_value=attr_value,
    )

    dict_data = defaultdict(list)

    for item in data.data:
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
    response_model=sc.CompanySchema,
    summary="企業情報を取得",
)
def get_company(*, HeadItemKey: str, session: SessionDep) -> sc.CompanySchema:
    """
    #### 企業情報を取得するエンドポイント
    - **機能**: HeadItemKeyから企業情報を取得します。
    - **認証不要**
    - **レスポンス形式**: JSON
    - **param1**: HeadItemKey: str 必須項目
    """

    item = crud.get_ix_head_title_by_item_key(session=session, item_key=HeadItemKey)

    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    item_dict = {
        "code": item.securities_code,
        "name": item.company_name,
        "accountingStandard": item.report_type,
        "fiscalYear": item.fy_year_end,
        "fiscalQuarter": item.current_period,
    }

    return sc.CompanySchema(**item_dict)


def get_label(
    *,
    head_item_key: str,
    names: List[str],
    session: SessionDep,
) -> Dict[str, str]:

    items = crud.get_label_by_names(
        session=session, head_item_key=head_item_key, names=names
    )

    if items is None:
        raise HTTPException(status_code=404, detail="Items not found")

    return {item.xlink_href: item.label for item in items}


@router.get(
    "/summary/operatingResults/{HeadItemKey}/{attr_type}",
    response_model=sc.FinancialResponseSchema,
    summary="経営成績を取得",
)
def get_operating_results(
    *,
    HeadItemKey: str,
    attr_type: str,
    session: SessionDep,
) -> sc.FinancialResponseSchema:
    """
    #### 経営成績を取得するエンドポイント
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

    attr_values = attr_type_dict[attr_type]["attr_value"]  # ここで取得する属性値を指定

    attr_value = crud.get_attr_value(  # attr_valueを取得
        session=session, head_item_key=HeadItemKey, attr_values=attr_values
    )

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

    items = crud.get_ix_non_fraction_records(
        session=session,
        head_item_key=HeadItemKey,
        names=names_to_list,
        contexts=context_list,
    )

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
            elif to_from_dict[from_item].endswith(
                attr_type_dict[attr_type]["from_name"]
            ):  # ここで取得する属性値を指定
                parentList.append(
                    {
                        "name": from_item,
                        "order": to_order_dict[from_item],
                        "label": parentLabels[from_item],
                    }
                )
        except KeyError:
            continue
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

    return sc.FinancialResponseSchema(company=company, metrics=parentList)


@router.get(
    "/operatingResults/{code}",
    response_model=sc.FinancialResponseSchema,
    summary="証券コードから経営成績を取得",
)
def get_operating_results_by_code(
    *,
    code: str,
    year: str = Query(None),
    period: str = Query(None),
    attr_type: str = Query("operatingResults"),
    session: SessionDep,
) -> sc.FinancialResponseSchema:
    """
    #### 証券コードから経営成績を取得するエンドポイント
    - **機能**: 証券コードから経営成績を取得します。
    - **認証不要**
    - **レスポンス形式**: JSON
    - **param1**: code: str 必須項目
    - **param2**: year: str 任意項目
    - **param3**: period: str 任意項目
    """

    item = crud.get_ix_head_title(session=session, code=code, year=year, period=period)

    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    HeadItemKey = item.item_key

    return get_operating_results(
        HeadItemKey=HeadItemKey, attr_type=attr_type, session=session
    )
