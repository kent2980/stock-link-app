import copy
import itertools
import logging
import re
from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Dict, List, Optional

import app.crud as crud
import app.schema as sc
import emails  # type: ignore
import jwt
from app.core.config import settings
from app.schema.ix_view import (
    abstractBase,
    stock,
    stockNumeric,
)
from jinja2 import Template
from jwt.exceptions import InvalidTokenError
from treelib import Node, Tree


@dataclass
class EmailData:
    html_content: str
    subject: str


def render_email_template(*, template_name: str, context: dict[str, Any]) -> str:
    template_str = (
        Path(__file__).parent / "email-templates" / "build" / template_name
    ).read_text()
    html_content = Template(template_str).render(context)
    return html_content


def send_email(
    *,
    email_to: str,
    subject: str = "",
    html_content: str = "",
) -> None:
    assert settings.emails_enabled, "no provided configuration for email variables"
    message = emails.Message(
        subject=subject,
        html=html_content,
        mail_from=(settings.EMAILS_FROM_NAME, settings.EMAILS_FROM_EMAIL),
    )
    smtp_options = {"host": settings.SMTP_HOST, "port": settings.SMTP_PORT}
    if settings.SMTP_TLS:
        smtp_options["tls"] = True
    elif settings.SMTP_SSL:
        smtp_options["ssl"] = True
    if settings.SMTP_USER:
        smtp_options["user"] = settings.SMTP_USER
    if settings.SMTP_PASSWORD:
        smtp_options["password"] = settings.SMTP_PASSWORD
    response = message.send(to=email_to, smtp=smtp_options)
    logging.info(f"send email result: {response}")


def generate_test_email(email_to: str) -> EmailData:
    project_name = settings.PROJECT_NAME
    subject = f"{project_name} - Test email"
    html_content = render_email_template(
        template_name="test_email.html",
        context={"project_name": settings.PROJECT_NAME, "email": email_to},
    )
    return EmailData(html_content=html_content, subject=subject)


def generate_reset_password_email(email_to: str, email: str, token: str) -> EmailData:
    project_name = settings.PROJECT_NAME
    subject = f"{project_name} - Password recovery for user {email}"
    link = f"{settings.server_host}/reset-password?token={token}"
    html_content = render_email_template(
        template_name="reset_password.html",
        context={
            "project_name": settings.PROJECT_NAME,
            "username": email,
            "email": email_to,
            "valid_hours": settings.EMAIL_RESET_TOKEN_EXPIRE_HOURS,
            "link": link,
        },
    )
    return EmailData(html_content=html_content, subject=subject)


def generate_new_account_email(
    email_to: str, username: str, password: str
) -> EmailData:
    project_name = settings.PROJECT_NAME
    subject = f"{project_name} - New account for user {username}"
    html_content = render_email_template(
        template_name="new_account.html",
        context={
            "project_name": settings.PROJECT_NAME,
            "username": username,
            "password": password,
            "email": email_to,
            "link": settings.server_host,
        },
    )
    return EmailData(html_content=html_content, subject=subject)


def generate_password_reset_token(email: str) -> str:
    delta = timedelta(hours=settings.EMAIL_RESET_TOKEN_EXPIRE_HOURS)
    now = datetime.utcnow()
    expires = now + delta
    exp = expires.timestamp()
    encoded_jwt = jwt.encode(
        {"exp": exp, "nbf": now, "sub": email},
        settings.SECRET_KEY,
        algorithm="HS256",
    )
    return encoded_jwt


def verify_password_reset_token(token: str) -> str | None:
    try:
        decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        return str(decoded_token["sub"])
    except InvalidTokenError:
        return None


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


def create_menu_items_tree(*, session, id: str, type: str, header: str = None) -> Tree:

    # 処理時間の計測
    start = datetime.now()

    # region データベースからアイテムを取得
    items = crud.read_menu_items(session=session, xbrl_id=id, xbrl_type=type).data
    # endregion

    endTime = datetime.now()
    print("処理時間: ", endTime - start)

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
    for nodes in tree.children("root"):
        nodes: Node
        for node in tree.leaves(nodes.identifier):
            node: Node
            if not node.tag.endswith("Member"):
                finance_item = crud.read_finance_item(
                    session=session,
                    xbrl_id=id,
                    xbrl_type=type,
                    name=node.tag,
                    context=context_id[nodes.tag]["id"],
                )
                node.data.items = finance_item
    # endregion

    # region 不要なノードの削除
    for nodes in tree.children("root"):
        nodes: Node
        for node in tree.children(nodes.identifier):
            node: Node
            if node.tag.endswith("Table"):
                tree.remove_node(node.identifier)
    # endregion

    endTime = datetime.now()
    print("処理時間: ", endTime - start)

    return tree


def set_view_item(item, value, label, scale, numeric):
    """ix_view項目を設定する"""
    item.set_value(value)
    item.label = label
    item.scale = scale
    item.numeric = numeric


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


def set_view_abstract(item, order, label):
    """ix_view概要を設定する"""
    item.Order = order
    item.Label = label


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


def remove_context(tree: Tree, context: str):
    for node in tree.leaves():
        items = node.data.items
        if type(items) == sc.ix_global.IxViewFinances:
            for item in items.data:
                if context in item.context:
                    items.data.remove(item)

    return tree


def set_regex(item: any, regex: str, abstract=False) -> dict[str, any]:
    return {"item": item, "regex": regex, "abstract": abstract}


def document_entity_info(tree: Tree) -> sc.ix_view.StockInfo:

    items = sc.ix_view.StockInfo()

    abstract_regex = [
        set_regex(items.BusinessCategory, r"^tse-ed-t_BusinessCategoryAbstract$"),
        set_regex(items.InquiriesAbstract, r"tse-ed-t_InquiriesAbstract$"),
        set_regex(
            items.OtherCompanyInformationAbstract,
            r"tse-ed-t_OtherCompanyInformationAbstract$",
        ),
        set_regex(items.RepresentativeAbstract, r"tse-ed-t_RepresentativeAbstract$"),
    ]

    item_regex = [
        set_regex(items.BusinessCategory.GeneralBusiness, r"tse-ed-t_GeneralBusiness$"),
        set_regex(
            items.BusinessCategory.SpecificBusiness, r"tse-ed-t_SpecificBusiness$"
        ),
        set_regex(items.CompanyName, r"tse-ed-t_CompanyName$"),
        set_regex(items.DocumentName, r"tse-ed-t_DocumentName$"),
        set_regex(items.FilingDate, r"tse-ed-t_FilingDate$"),
        set_regex(items.FiscalYearEnd, r"tse-ed-t_FiscalYearEnd$"),
        set_regex(items.QuarterlyPeriod, r"tse-ed-t_QuarterlyPeriod$"),
        set_regex(items.InquiriesAbstract.NameInquiries, r"tse-ed-t_NameInquiries$"),
        set_regex(items.InquiriesAbstract.TitleInquiries, r"tse-ed-t_TitleInquiries$"),
        set_regex(
            items.NoteToFractionProcessingMethod,
            r"tse-ed-t_NoteToFractionProcessingMethod$",
        ),
        set_regex(
            items.RepresentativeAbstract.NameRepresentative,
            r"tse-ed-t_NameRepresentative$",
        ),
        set_regex(
            items.RepresentativeAbstract.TitleRepresentative,
            r"tse-ed-t_TitleRepresentative$",
        ),
        set_regex(items.SecuritiesCode, r"tse-ed-t_SecuritiesCode$"),
        set_regex(items.Tel, r"tse-ed-t_Tel$"),
        set_regex(items.URL, r"tse-ed-t_URL$"),
        set_regex(
            items.ConveningBriefingOfAnnualResults,
            r"tse-ed-t_ConveningBriefingOfAnnualResults$",
        ),
        set_regex(
            items.OtherCompanyInformationAbstract.AnnualSecuritiesReportFilingDateAsPlanned,
            r"tse-ed-t_AnnualSecuritiesReportFilingDateAsPlanned$",
        ),
        set_regex(
            items.OtherCompanyInformationAbstract.DateOfGeneralShareholdersMeetingAsPlanned,
            r"tse-ed-t_DateOfGeneralShareholdersMeetingAsPlanned$",
        ),
        set_regex(
            items.OtherCompanyInformationAbstract.DividendPayableDateAsPlanned,
            r"tse-ed-t_DividendPayableDateAsPlanned$",
        ),
        set_regex(
            items.SupplementalMaterialOfAnnualResults,
            r"tse-ed-t_SupplementalMaterialOfAnnualResults$",
        ),
        set_regex(
            items.WayOfGettingSupplementalMaterialOfAnnualResults,
            r"tse-ed-t_WayOfGettingSupplementalMaterialOfAnnualResults$",
        ),
        set_regex(
            items.TargetAudienceBriefingOfAnnualResults,
            r"tse-ed-t_TargetAudienceBriefingOfAnnualResults$",
        ),
    ]

    for header in tree.all_nodes():
        if re.match(r"^tse-ed-t_DocumentEntityInformationHeading$", header.tag):
            subtree = tree.subtree(header.identifier)
            for node in subtree.all_nodes():
                if re.match(
                    r"^tse-ed-t_TokyoStockExchange.*$", node.tag
                ):  # 東京証券取引所の上場区分
                    try:
                        value = node.data.items.data[0].value
                        if value == "true":
                            items.TokyoStockExchange.label = node.data.label
                            items.TokyoStockExchange.set_value(value)
                    except (IndexError, AttributeError):
                        continue
                elif re.match(
                    r"tse-ed-t_StockExchangeListingsAbstract$", node.tag
                ):  # 上場区分
                    try:
                        items.TokyoStockExchange.order = node.data.order
                    except (IndexError, AttributeError):
                        continue
                for item in abstract_regex:
                    set_view_abstract_regex(item["item"], node, item["regex"])
                for item in item_regex:
                    set_view_stock_regex(item["item"], node, item["regex"])

    return items


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


def operating_result_ifrs(
    tree: Tree,
) -> sc.ix_view.OperatingResultIfrs:

    tree = remove_context(tree, "Prior")

    items = sc.ix_view.OperatingResultIfrs()
    ope = items.OperatingResultsAbstract  # 経営成績の概要
    cisi = ope.IncomeStatementsInformationAbstract  # 連結損益計算書情報
    ncisi = items.NoteToOperatingResultAbstract  # 連結損益計算書情報に関する注記
    ocor = ope.OtherOperatingResultsAbstract  # その他包括利益の概要

    regex_item = [
        # region 損益計算書情報
        set_regex(cisi, r"tse-ed-t_.*IncomeStatementsInformationAbstract$", True),
        set_regex(
            cisi.NetSalesAbstract,
            r"tse-ed-t_.*SalesIFRSAbstract$|tse-ed-t_.*RevenueIFRSAbstract$",
            True,
        ),
        set_regex(
            cisi.OperatingIncomeAbstract, r"tse-ed-t_OperatingIncomeIFRSAbstract", True
        ),
        set_regex(
            cisi.ProfitBeforeTaxAbstract, r"tse-ed-t_ProfitBeforeTaxIFRSAbstract", True
        ),
        set_regex(
            cisi.ProfitAttributableToOwnersOfParentAbstract,
            r"tse-ed-t_ProfitAttributableToOwnersOfParentIFRSAbstract",
            True,
        ),
        set_regex(cisi.ProfitAbstract, r"tse-ed-t_ProfitIFRSAbstract", True),
        set_regex(
            cisi.TotalComprehensiveIncomeAbstract,
            r"tse-ed-t_TotalComprehensiveIncomeIFRSAbstract",
            True,
        ),
        set_regex(
            cisi.NetSalesAbstract.ChangeIn,
            r"tse-ed-t_ChangeIn.*SalesIFRS|tse-ed-t_ChangeInRevenueIFRS$",
        ),
        set_regex(
            cisi.NetSalesAbstract.Values, r"tse-ed-t_.*SalesIFRS|tse-ed-t_RevenueIFRS$"
        ),
        set_regex(
            cisi.OperatingIncomeAbstract.ChangeIn,
            r"tse-ed-t_ChangeInOperatingIncomeIFRS",
        ),
        set_regex(cisi.OperatingIncomeAbstract.Values, r"tse-ed-t_OperatingIncomeIFRS"),
        set_regex(
            cisi.ProfitBeforeTaxAbstract.ChangeIn,
            r"tse-ed-t_ChangeInProfitBeforeTaxIFRS",
        ),
        set_regex(cisi.ProfitBeforeTaxAbstract.Values, r"tse-ed-t_ProfitBeforeTaxIFRS"),
        set_regex(
            cisi.ProfitAttributableToOwnersOfParentAbstract.ChangeIn,
            r"tse-ed-t_ChangeInProfitAttributableToOwnersOfParentIFRS",
        ),
        set_regex(
            cisi.ProfitAttributableToOwnersOfParentAbstract.Values,
            r"tse-ed-t_ProfitAttributableToOwnersOfParentIFRS",
        ),
        set_regex(cisi.ProfitAbstract.ChangeIn, r"tse-ed-t_ChangeInProfitIFRS"),
        set_regex(cisi.ProfitAbstract.Values, r"tse-ed-t_ProfitIFRS"),
        set_regex(
            cisi.TotalComprehensiveIncomeAbstract.ChangeIn,
            r"tse-ed-t_ChangesInTotalComprehensiveIncomeIFRS",
        ),
        set_regex(
            cisi.TotalComprehensiveIncomeAbstract.Values,
            r"tse-ed-t_TotalComprehensiveIncomeIFRS",
        ),
        # endregion
        # region 連結損益計算書情報に関する注記
        set_regex(ncisi, r"tse-ed-t_NoteTo.*OperatingResultsAbstract", True),
        set_regex(
            ncisi.InvestmentsAccountedForUsingEquityMethod,
            r"tse-ed-t_InvestmentsAccountedForUsingEquityMethodIFRS",
        ),
        set_regex(ncisi.NoteToOperatingResult, r"tse-ed-t_NoteToOperatingResults"),
        # endregion
        # region その他包括利益の概要
        set_regex(ocor, r"tse-ed-t_Other.*OperatingResultsAbstract", True),
        set_regex(
            ocor.DilutedEarningsPerShare, r"tse-ed-t_DilutedEarningsPerShareIFRS"
        ),
        set_regex(
            ocor.OperatingIncomeToSalesRatio,
            r"tse-ed-t_OperatingIncomeToSalesRatioIFRS",
        ),
        set_regex(
            ocor.ProfitBeforeTaxToTotalAssetsRatio,
            r"tse-ed-t_ProfitBeforeTaxToTotalAssetsRatioIFRS",
        ),
        set_regex(
            ocor.ProfitToEquityAttributableToOwnersOfParentRatio,
            r"tse-ed-t_ProfitToEquityAttributableToOwnersOfParentRatioIFRS",
        ),
        set_regex(ocor.BasicEarningsPerShare, r"tse-ed-t_BasicEarningsPerShareIFRS"),
        # endregion
        # region 経営成績の概要
        set_regex(ope, r"tse-ed-t_(?!NoteTo)(?!Other).*OperatingResultsAbstract", True),
        # endregion
    ]

    # region ツリーから情報を取得
    for header in tree.all_nodes():
        if re.match(r"^tse-ed-t_BusinessResults.*OperatingResultsHeading$", header.tag):
            subtree = tree.subtree(header.identifier)
            for node in subtree.all_nodes():
                for item in regex_item:
                    if item["abstract"]:
                        set_view_abstract_regex(item["item"], node, item["regex"])
                    else:
                        set_view_item_regex(item["item"], node, item["regex"])
    # endregion

    return items


def operating_result_us(
    tree: Tree,
) -> sc.ix_view.OperatingResultUs:

    tree = remove_context(tree, "Prior")

    items = sc.ix_view.OperatingResultUs()
    ncisi = items.NoteToOperatingResultsAbstract  # 経営成績に関する注記
    ope = items.OperatingResultsAbstract  # 経営成績の概要
    ntis = ope.NoteToIncomeStatementsInformationAbstract  # 損益計算書情報に関する注記
    cisi = ope.IncomeStatementsInformationAbstract  # 連結損益計算書情報
    ocor = ope.OtherOperatingResultsAbstract  # その他包括利益の概要

    regex_item = [
        # region 損益計算書情報
        set_regex(
            cisi, r"tse-ed-t_(?!NoteTo).*IncomeStatementsInformationAbstract$", True
        ),
        set_regex(
            cisi.IncomeBeforeIncomeTaxesUSAbstract.ChangeIn,
            r"tse-ed-t_ChangeInIncomeBeforeIncomeTaxesUS$",
        ),
        set_regex(
            cisi.IncomeBeforeIncomeTaxesUSAbstract.Values,
            r"tse-ed-t_IncomeBeforeIncomeTaxesUS$",
        ),
        set_regex(cisi.NetIncomeUSAbstract.ChangeIn, r"tse-ed-t_ChangeInNetIncomeUS$"),
        set_regex(cisi.NetIncomeUSAbstract.Values, r"tse-ed-t_NetIncomeUS$"),
        set_regex(
            cisi.OperatingIncomeUSAbstract.ChangeIn,
            r"tse-ed-t_ChangeInOperatingIncomeUS$",
        ),
        set_regex(
            cisi.OperatingIncomeUSAbstract.Values, r"tse-ed-t_OperatingIncomeUS$"
        ),
        set_regex(
            cisi.OperatingRevenuesUSAbstract.ChangeIn,
            r"tse-ed-t_ChangeInOperatingRevenuesUS$",
        ),
        set_regex(
            cisi.OperatingRevenuesUSAbstract.Values, r"tse-ed-t_OperatingRevenuesUS$"
        ),
        set_regex(
            cisi.IncomeBeforeIncomeTaxesUSAbstract,
            r"tse-ed-t_IncomeBeforeIncomeTaxesUSAbstract$",
            True,
        ),
        set_regex(cisi.NetIncomeUSAbstract, r"tse-ed-t_NetIncomeUSAbstract$", True),
        set_regex(
            cisi.OperatingIncomeUSAbstract, r"tse-ed-t_OperatingIncomeUSAbstract$", True
        ),
        set_regex(
            cisi.OperatingRevenuesUSAbstract,
            r"tse-ed-t_OperatingRevenuesUSAbstract$",
            True,
        ),
        # endregion
        # region 経営成績に関する注記
        set_regex(ncisi, r"tse-ed-t_NoteTo.*OperatingResultsAbstract$", True),
        set_regex(ncisi.NoteToOperatingResults, r"tse-ed-t_NoteToOperatingResults$"),
        # endregion
        # region その他包括利益の概要
        set_regex(ocor, r"tse-ed-t_Other.*OperatingResults.*Abstract$", True),
        set_regex(
            ocor.DilutedNetIncomePerShare2US, r"tse-ed-t_DilutedNetIncomePerShare2US$"
        ),
        set_regex(ocor.NetIncomePerShareUS, r"tse-ed-t_NetIncomePerShareUS$"),
        # endregion
        # region 損益計算書情報に関する注記
        set_regex(ntis, r"tse-ed-t_NoteTo.*IncomeStatementsInformationAbstract$", True),
        set_regex(
            ntis.ComprehensiveIncomeUSAbstract,
            r"tse-ed-t_ComprehensiveIncomeUSAbstract$",
            True,
        ),
        set_regex(
            ntis.ComprehensiveIncomeUSAbstract.ChangeIn,
            r"tse-ed-t_ChangeInComprehensiveIncomeNetOfTaxIncludingPortionAttributableToNoncontrollingInterest5US$",
        ),
        set_regex(
            ntis.ComprehensiveIncomeUSAbstract.Values,
            r"tse-ed-t_ComprehensiveIncomeNetOfTaxIncludingPortionAttributableToNoncontrollingInterest5US$",
        ),
        # endregion
        # region 経営成績の概要
        set_regex(
            ope, r"tse-ed-t_(?!NoteTo)(?!Other).*OperatingResultsAbstract$", True
        ),
        # endregion
    ]

    # region ツリーから情報を取得
    for header in tree.all_nodes():
        if re.match(r"^tse-ed-t_BusinessResults.*OperatingResultsHeading$", header.tag):
            subtree = tree.subtree(header.identifier)
            for node in subtree.all_nodes():
                for item in regex_item:
                    if item["abstract"]:
                        set_view_abstract_regex(item["item"], node, item["regex"])
                    else:
                        set_view_item_regex(item["item"], node, item["regex"])
    # endregion

    return items
