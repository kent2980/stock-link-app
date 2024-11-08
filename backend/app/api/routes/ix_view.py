import copy
import datetime
import itertools
import re
from typing import Any, Dict, List, Optional

import app.crud as crud
import app.schema as sc
from app.api.deps import SessionDep
from app.models import IxHeadTitle
from app.schema.ix_view import abstractBase, stock, stockNumeric
from fastapi import APIRouter, Query
from sqlmodel import select
from treelib import Node, Tree

router = APIRouter()


@router.get("/head_item/all/", response_model=sc.ix_view.HeadItems)
def read_head_items(
    *,
    session: SessionDep,
    code: str = Query(None),  # 銘柄コード
    limit: int = Query(10, ge=1),  # ページネーションのための取得数
    skip: int = Query(0, ge=0),  # ページネーションのためのスキップ数
) -> sc.ix_view.HeadItems:
    """銘柄コードからXBRLファイルのIDを取得する
    Args:
        code (str): 銘柄コード
        limit (int): 取得数
        skip (int): スキップ数
    """

    # 銘柄コードからXBRLファイルのIDを抽出
    statement = select(IxHeadTitle).where(IxHeadTitle.is_active == True)
    statement = statement.order_by(IxHeadTitle.reporting_date.desc())
    if code:
        statement = statement.where(IxHeadTitle.securities_code == code)
    statement = statement.offset(skip).limit(limit)

    # アイテムの取得
    items = session.exec(statement).all()

    # endregion

    return sc.ix_view.HeadItems(data=items, count=len(items))


@router.get("/head_item/select/", response_model=sc.ix_view.HeadItem)
def read_head_item(
    *,
    session: SessionDep,
    head_item_key: str = Query(...),  # XBRLファイルのID
) -> sc.ix_view.HeadItem:
    """XBRLファイルのIDからXBRLファイルの情報を取得する
    Args:
        head_item_key (str): XBRLファイルのID
    """

    statement = select(IxHeadTitle).where(
        IxHeadTitle.item_key == head_item_key, IxHeadTitle.is_active == True
    )
    items = session.exec(statement).first()

    return items


@router.get("/summary/item/select/", response_model=sc.ix_view.SummaryItemsAbstractJp)
def read_summary_item_by_head_item_key(
    *,
    session: SessionDep,
    head_item_key: str = Query(...),  # XBRLファイルのID
) -> sc.ix_view.SummaryItemsAbstractJp:
    """XBRLファイルのIDから決算情報を取得する"""

    # region ツリーの生成
    tree = create_menu_items_tree(session=session, id=head_item_key, type="sm")
    # endregion

    summary = summary_result(tree)

    return summary
    # endregion


def create_menu_items_tree(*, session, id: str, type: str, header: str = None) -> Tree:

    # 処理時間の計測
    start = datetime.datetime.now()

    # region データベースからアイテムを取得
    items = crud.read_menu_items(session=session, head_item_key=id, xbrl_type=type).data
    # endregion

    endTime = datetime.datetime.now()
    print("処理時間: ", endTime - start)
    start = datetime.datetime.now()

    # region ツリー構造の作成
    tree = Tree()

    tree.create_node(tag="root", identifier="root", data=sc.ix_global.IxViewItems())

    for item in items:
        arcrole = [
            "http://xbrl.org/int/dim/arcrole/all",
        ]
        if item.xlink_arcrole in arcrole:
            tag = str(item.from_href)
            label = crud.read_finance_item_label(session, id, type, tag)
            tree.create_node(
                tag=tag,
                identifier=item.xlink_from,
                parent="root",
                data=sc.ix_global.IxViewItems(
                    label=label,
                    order=item.xlink_order,
                    arcrole=item.xlink_arcrole,
                ),
            )

    tagList = []
    for item in items:
        tag = str(item.to_href)
        tagList.append(tag)

    labels = crud.read_finance_item_labels(session, id, type, tagList)

    for item in items:
        tag = str(item.to_href)
        if item.from_id is None:
            if tree.contains(item.xlink_from):
                try:
                    label = [label.label for label in labels.data if label.tag == tag][
                        0
                    ]
                except IndexError:
                    label = None
                tree.create_node(
                    tag=tag,
                    identifier=item.id,
                    parent=item.xlink_from,
                    data=sc.ix_global.IxViewItems(
                        label=label,
                        order=item.xlink_order,
                        arcrole=item.xlink_arcrole,
                    ),
                )
        else:
            try:
                label = [label.label for label in labels.data if label.tag == tag][0]
            except IndexError:
                label = None
            tree.create_node(
                tag=tag,
                identifier=item.id,
                parent="root",
                data=sc.ix_global.IxViewItems(
                    label=label,
                    order=item.xlink_order,
                    arcrole=item.xlink_arcrole,
                ),
            )

    for item in items:
        if item.from_id is not None:
            tree.move_node(item.id, item.from_id)
    # endregion

    # region ツリーの抽出
    if header is not None and header != "":
        for node in tree.children("root"):
            if re.match(header, node.tag):
                if tree.contains(node.identifier):
                    new_tree = tree.subtree(node.identifier)
                    tree = Tree()
                    tree.create_node("root", "root")
                    tree.paste("root", new_tree)
    # endregion

    # region itemsの取得
    context_id = create_context_id(tree=tree)
    finance_item = crud.read_finance_item(
        session=session,
        head_item_key=id,
        xbrl_type=type,
    )
    for nodes in tree.children("root"):
        nodes: Node
        for node in tree.leaves(nodes.identifier):
            node: Node
            finance_item_list = []
            if not node.tag.endswith("Member"):
                name = node.tag
                context = context_id[nodes.tag]["id"]
                if finance_item is not None:
                    for item in finance_item.data:
                        if item.name == name and re.match(context, item.context):
                            finance_item_list.append(item)
                node.data.items = sc.ix_global.IxViewFinances(
                    count=len(finance_item_list), data=finance_item_list
                )
    # endregion

    # region 不要なノードの削除
    for nodes in tree.children("root"):
        nodes: Node
        for node in tree.children(nodes.identifier):
            node: Node
            if node.tag.endswith("Table"):
                tree.remove_node(node.identifier)
    # endregion

    endTime = datetime.datetime.now()
    print("処理時間: ", endTime - start)

    return tree


def create_context_id(tree: Tree):
    """contextTableを辞書に変換

    Args:
        tree (Tree): contextTableのTree構造

    Returns:
        Dict[str, Dict[str, Any]]: context_id
    """

    # region contextTableを辞書に変換
    context_id = {}
    for nodes in tree.children("root"):
        parentDict = {}
        for node in tree.children(nodes.identifier):
            if node.tag.endswith("Table"):
                subTree = tree.subtree(node.identifier)
                for axisNode in subTree.all_nodes():
                    if axisNode.tag.endswith("Axis"):
                        member = {}
                        arcrole = ""
                        axisTree = subTree.subtree(axisNode.identifier)
                        for allNode in axisTree.all_nodes():
                            if allNode.tag.endswith("Member"):
                                item = allNode.data
                                if arcrole != item.arcrole.split("/")[-1]:
                                    tags = []
                                arcrole = item.arcrole.split("/")[-1]
                                parent = subTree.parent(allNode.identifier).tag
                                tags.append(allNode.tag)
                                member[arcrole] = tags
                        parentDict[parent] = copy.deepcopy(member)
        context_id[nodes.tag] = parentDict
    # endregion

    # region idを作成
    for _, value in context_id.items():
        id_list = []
        for _, contexts in value.items():
            is_default = True
            default_context = ""
            for arcrole, context in contexts.items():
                if arcrole == "dimension-default":
                    try:
                        id_list.remove(context)
                    except ValueError:
                        is_default = False
                        default_context = context
                elif arcrole == "domain-member":
                    id_list.append(context)
                else:
                    if is_default and default_context != context:
                        id_list.append(context)
        id_mix: List[List[str]] = itertools.product(*id_list)
        # id_mix の内包リスト内の文字列を結合
        idd = []
        for values in id_mix:
            values = [value.split("_")[-1] for value in values]
            values = [r"(?=.*_" + value + ")" for value in values]
            values = "".join(values)
            idd.append(values)
        idd = "|".join(idd)
        value["id"] = idd
    # endregion

    # region context_idからid以外の要素を削除
    for key, value in context_id.items():
        value: Dict[str, Any]
        keys_to_delete = [key2 for key2 in value.keys() if key2 != "id"]
        for key2 in keys_to_delete:
            del value[key2]
    # endregion

    # region 結果を出力
    return context_id
    # endregion


def summary_result(
    tree: Tree, specific: bool = False
) -> sc.ix_view.SummaryItemsAbstractJp:
    """
    operating_result_jp(tree, ncisi, ocor[, specific])<br/><br/>
    この関数は、決算短信サマリー[日本基準]から損益計算書情報を取得するための関数です。<br/>
    特定事業会社の場合は、specificをTrueに設定してください。<br/>
    """

    objLst = []

    if specific is True:  # 特定事業会社の場合
        items = sc.ix_view.OperatingResultSpecificJp()
    else:  # 一般事業会社の場合
        sm = sc.ix_view.SummaryItemsAbstractJp()
        info = sm.DocumentEntityInformation
        operating = sm.OperatingResult
        operating_abstract = operating.OperatingResultsAbstract
        fi_pos = sm.BusinessResultsFinancialPositions
        objLst.extend(
            [
                sm,
                info,
                info.RepresentativeAbstract,
                info.InquiriesAbstract,
                info.OtherCompanyInformationAbstract,
                info.BusinessCategory,
                operating,
                operating_abstract,
                operating_abstract.IncomeStatementsInformationAbstract,
                operating_abstract.NoteToIncomeStatementsInformationAbstract,
                operating_abstract.OtherOperatingResultsAbstract,
                operating.NoteToOperatingResultsAbstract,
                sm.NotesApplyingSpecificAccountingQuarterlyFinancialStatements,
                sm.NotesChangesAccountingPoliciesAccountingEstimatesRetrospectiveRestatement,
                sm.NotesNumberIssuedOutstandingSharesCommonStock,
                sm.NoteToFinancialResults,
                fi_pos,
                fi_pos.FinancialPositions,
                fi_pos.NoteToFinancialPositions,
                sm.Dividends,
                sm.Forecasts,
                sm.Dividends.DividendPerShare,
                sm.SignificantChangesInTheScopeOfConsolidationDuringThePeriod,
                sm.SpecialNotes,
            ]
        )

    # region ツリーから情報を取得
    for header in tree.all_nodes():
        header: Node
        for obj in objLst:
            if isinstance(obj, sc.ix_view.ContextFilter):
                for key, value in obj.__dict__.items():
                    try:
                        if isinstance(value, sc.ix_view.stock):
                            set_view_stock_regex(value, header, value.regex)
                        elif isinstance(value, sc.ix_view.stockNumeric):
                            set_view_item_regex(
                                value, header, value.regex, value.context
                            )
                        elif isinstance(value, sc.ix_view.abstract):
                            set_view_abstract_regex(value, header, value.regex)
                            set_view_item_regex(
                                value.ChangeIn,
                                header,
                                value.ChangeIn.regex,
                                value.context,
                            )
                            set_view_item_regex(
                                value.Values, header, value.Values.regex, value.context
                            )
                        elif isinstance(value, sc.ix_view.abstractBase):
                            set_view_abstract_regex(value, header, value.regex)
                    except TypeError:
                        continue
    # endregion

    return sm


def set_view_stock_regex(item: stock, node: Node, regex: str):
    if node.tag == "root":
        return None

    tag = node.tag
    order = node.data.order
    try:
        data = node.data.items.data[0]
        if re.match(regex, tag):
            item.set_value(data.value)
    except (IndexError, AttributeError):
        return None
    finally:
        if re.match(regex, tag):
            item.label = node.data.label
            item.order = order


def set_view_item_regex(
    item: stockNumeric, node: Node, regex: str, context_regex: Optional[str] = None
):
    """ix_view項目を設定する

    Args:
        item (stockNumeric): 項目
        node (Node): ノード
        regex (str): 正規表現
    """
    if node.tag == "root":
        return None

    try:
        tag = node.tag
        dataLst = node.data.items.data
        if isinstance(dataLst, list):
            for data in dataLst:
                context = data.context
                if re.match(regex, tag) and re.match(context_regex, context):
                    item.set_value(data.value)
                    item.scale = data.display_scale
                    item.numeric = data.numeric
    except (IndexError, AttributeError) as e:
        return None
    finally:
        if re.match(regex, tag):
            item.label = node.data.label
            item.order = node.data.order


def set_view_abstract_regex(item: abstractBase, node: Node, regex: str):
    """ix_view概要を設定する

    Args:
        item (abstractBase): 概要
        node (Node): ノード
        regex (str): 正規表現
    """
    if node.tag == "root" or node.data.items is not None:
        return None
    tag = node.tag
    order = node.data.order
    label = node.data.label

    if re.match(regex, tag):
        item.order = order
        item.Label = label
