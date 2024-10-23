import datetime
import pprint
import re
from typing import Optional, Union

import app.crud as crud
import app.schema as ssc
import app.utils as utils
from app.api.deps import SessionDep
from app.models import IxHeadTitle, IxNonFraction, IxNonNumeric
from app.schema import ix_view as sc
from fastapi import APIRouter, HTTPException, Query
from sqlmodel import select, text

router = APIRouter()


@router.get("/stock/all/", response_model=sc.StockRecordInfos)
def read_stock_record(
    *,
    session: SessionDep,
    code: Optional[str] = Query(None),
    type: Optional[str] = Query(None),
    dateStr: Optional[str] = Query(None),
    period: Optional[int] = Query(None),
    skip: int = Query(0, ge=0),  # ページネーションのためのスキップ数
    limit: int = Query(10, ge=1),  # ページネーションのための取得数
) -> sc.StockRecordInfos:
    """すべての銘柄コードを取得する

    Args:
        type (str): レポートの種類

    Returns:
        sc.ix_head.IxHeadShortsPublic: 銘柄コードのリスト
    """

    # region 引数のチェック処理
    if dateStr is not None and not re.match(r"^\d{8}$", dateStr):
        detail = "dateStrはYYYYMMDDの形式で指定してください"
        raise HTTPException(status_code=400, detail=detail)
    if period is not None and period not in [1, 2, 3, 4]:
        detail = "periodは1,2,3,4のいずれかを指定してください"
        raise HTTPException(status_code=400, detail=detail)
    # endregion

    # region クエリの作成
    statement = select(
        IxHeadTitle.xbrl_id,
        IxHeadTitle.company_name,
        IxHeadTitle.securities_code,
        IxHeadTitle.current_period,
        IxHeadTitle.report_type,
        IxHeadTitle.reporting_date,
        IxHeadTitle.document_name,
        IxHeadTitle.fiscal_year_end,
        IxHeadTitle.url,
    ).order_by(IxHeadTitle.securities_code.asc())
    if code:
        statement = statement.where(IxHeadTitle.securities_code == code)
    if type:
        statement = statement.where(IxHeadTitle.report_type.like(f"%{type}%"))
    if dateStr:
        statement = statement.where(
            IxHeadTitle.reporting_date == datetime.datetime.strptime(dateStr, "%Y%m%d")
        )
    if period:
        period_mapping = {1: "Q1", 2: "Q2", 3: "Q3", 4: "FY"}
        statement = statement.where(
            IxHeadTitle.current_period == period_mapping[period]
        )
    # endregion

    # region クエリの実行
    result = session.exec(statement.offset(skip).limit(limit))
    data = result.all()
    # endregion

    # 次のレコードが存在しない場合はnextOffsetをNoneにする
    if len(data) < limit:
        nextOffset = None
    else:
        nextOffset = skip + limit

    pprint.pprint(data)

    return sc.StockRecordInfos(data=data, count=len(data), nextOffset=nextOffset)


@router.get("/stock/all/new/", response_model=sc.StockRecordInfos)
def read_new_stock_record(
    *,
    session: SessionDep,
    skip: int = Query(0, ge=0),  # ページネーションのためのスキップ数
    limit: int = Query(10, ge=1),  # ページネーションのための取得数
) -> sc.StockRecordInfos:

    # SQL文を定義
    statement = text(
        """
        SELECT DISTINCT ON (iht.securities_code) *
        FROM ix_head_title iht
        ORDER BY iht.securities_code, iht.reporting_date DESC
    """
    )

    # SQL文を実行
    result = session.exec(statement)
    data = result.all()

    # 次のレコードが存在しない場合はnextOffsetをNoneにする
    if len(data) < limit:
        nextOffset = None
    else:
        nextOffset = skip + limit

    return sc.StockRecordInfos(data=data, count=len(data), nextOffset=nextOffset)


@router.get("/head_items/", response_model=sc.HeadItems)
def read_head_items(
    *,
    session: SessionDep,
    code: str = Query(None),  # 銘柄コード
    limit: int = Query(10, ge=1),  # ページネーションのための取得数
    skip: int = Query(0, ge=0),  # ページネーションのためのスキップ数
) -> sc.HeadItems:
    """銘柄コードからXBRLファイルのIDを取得する
    Args:
        code (str): 銘柄コード
        limit (int): 取得数
        skip (int): スキップ数
    """

    # 銘柄コードからXBRLファイルのIDを抽出
    statement = select(IxHeadTitle)
    statement = statement.order_by(IxHeadTitle.reporting_date.desc())
    if code:
        statement = statement.where(IxHeadTitle.securities_code == code)
    statement = statement.offset(skip).limit(limit)

    # アイテムの取得
    items = session.exec(statement).all()

    # endregion

    return sc.HeadItems(data=items, count=len(items))


@router.get("/head_item/${xbrl_id}", response_model=sc.HeadItem)
def read_head_item(
    *,
    session: SessionDep,
    xbrl_id: str,
) -> sc.HeadItem:
    """XBRLファイルのIDからXBRLファイルの情報を取得する
    Args:
        xbrl_id (str): XBRLファイルのID
    """

    statement = select(IxHeadTitle).where(IxHeadTitle.xbrl_id == xbrl_id)
    items = session.exec(statement).first()

    return items


@router.get("/menu/", response_model=sc.MenuTitles)
def read_menu_title(
    *, session: SessionDep, type: str = Query(...), id: str = Query(...)
) -> sc.MenuTitles:
    """XBRLファイルのIDからメニューラベルを取得する
    Args:
        xbrl_id (str): XBRLファイルのID
    """

    # region 引数のチェック処理
    if type not in ["sm", "fr"]:
        detail = "typeは [sm:サマリー], [fr:財務諸表] のいずれかを指定してください"
        raise HTTPException(status_code=400, detail=detail)

    # endregion

    # region データベースからの取得
    items = crud.read_menu_label(session=session, xbrl_id=id, type=type)

    menu_list = []
    for item in items:
        menu_item = {
            "label": item.xlink_href,
            "jp": re.sub(r" \[.*\]", "", item.label).split("、")[-1],
        }
        menu_list.append(menu_item)

    # endregion

    return sc.MenuTitles(data=menu_list, count=len(menu_list))


@router.get("/items/", response_model=dict)
def read_menu_items(
    *,
    session: SessionDep,
    type: str = Query(...),
    id: str = Query(...),
    header: Optional[str] = Query(None),
) -> dict:
    """XBRLファイルのIDとメニューラベルから項目を取得する
    Args:
        xbrl_id (str): XBRLファイルのID
        menu_label (str): メニューラベル
    """

    # region 引数のチェック処理
    # typeのチェック
    if type not in ["sm", "fr"]:
        detail = "typeは [sm:サマリー], [fr:財務諸表] のいずれかを指定してください"
        raise HTTPException(status_code=400, detail=detail)

    # menu_labelのチェック
    header_list = read_menu_title(session=session, type=type, id=id).data
    headers = [item.label for item in header_list]
    if header is not None and header != "" and header not in headers:
        detail = f"menu_labelは {header_list} のいずれかを指定してください"
        raise HTTPException(status_code=400, detail=detail)
    # endregion

    # region ツリーの取得
    tree = utils.create_menu_items_tree(
        session=session, id=id, type=type, header=header
    )
    # endregion

    return tree.to_dict(with_data=True, key=lambda x: x.data.order)


@router.get("/info/", response_model=Union[sc.FiscalYearStockInfo, sc.StockInfo])
def read_stock_info(
    *,
    session: SessionDep,
    code: str = Query(...),
) -> Union[sc.FiscalYearStockInfo, sc.StockInfo]:
    """銘柄コードから企業情報を取得する

    Args:
        code (str): 銘柄コード

    Returns:
        sc.StockInfoPublic: 企業情報
    """

    statement = (
        select(IxHeadTitle)
        .where(IxHeadTitle.securities_code == code, IxHeadTitle.report_type.like("ed%"))
        .order_by(IxHeadTitle.reporting_date.desc())
    )
    items = session.exec(statement).all()
    if len(items) == 0:
        raise HTTPException(status_code=404, detail="Item not found")

    # itemsをlistに変換
    items = [item for item in items]

    id = items[0].xbrl_id

    period = items[0].current_period

    if period is None:
        raise HTTPException(status_code=404, detail="Item not found")

    # region データベースからの取得
    header = "tse-ed-t_DocumentEntityInformationHeading"

    tree = utils.create_menu_items_tree(
        session=session, id=id, type="sm", header=header
    )
    # endregion

    # region ツリーから情報を取得
    info = sc.StockInfo()

    for header in tree.all_nodes():
        if header.tag == "tse-ed-t_DocumentEntityInformationHeading":
            subtree = tree.subtree(header.identifier)
            for node in subtree.all_nodes():
                try:
                    tag = node.tag
                    value = node.data.items.data[0].value
                    label = node.data.label
                except AttributeError:
                    continue
                if tag == "tse-ed-t_GeneralBusiness":  # 一般事業会社
                    info.BusinessCategory.GeneralBusiness.set_value(value)
                    info.BusinessCategory.GeneralBusiness.label = label
                elif tag == "tse-ed-t_SpecificBusiness":  # 特定事業会社
                    info.BusinessCategory.SpecificBusiness.set_value(value)
                    info.BusinessCategory.SpecificBusiness.label = label
                elif tag == "tse-ed-t_CompanyName":  # 上場会社名
                    info.CompanyName.set_value(value)
                    info.CompanyName.label = label
                elif tag == "tse-ed-t_DocumentName":  # 文書名
                    info.DocumentName.set_value(value)
                    info.DocumentName.label = label
                elif tag == "tse-ed-t_FilingDate":  # 提出日
                    info.FilingDate.set_value(value)
                    info.FilingDate.label = label
                elif tag == "tse-ed-t_FiscalYearEnd":  # 決算期
                    info.FiscalYearEnd.set_value(value)
                    info.FiscalYearEnd.label = label
                elif tag == "tse-ed-t_NameInquiries":  # 問合せ先
                    info.NameInquiries.set_value(value)
                    info.NameInquiries.label = label
                elif tag == "tse-ed-t_TitleInquiries":  # 問合せ先役職
                    info.TitleInquiries.set_value(value)
                    info.TitleInquiries.label = label
                elif (
                    tag == "tse-ed-t_NoteToFractionProcessingMethod"
                ):  # 端数処理方法に関する注記
                    info.NoteToFractionProcessingMethod.set_value(value)
                    info.NoteToFractionProcessingMethod.label = label
                elif tag == "tse-ed-t_NameRepresentative":  # 代表者氏名
                    info.NameRepresentative.set_value(value)
                    info.NameRepresentative.label = label
                elif tag == "tse-ed-t_TitleRepresentative":  # 代表者役職名
                    info.TitleRepresentative.set_value(value)
                    info.TitleRepresentative.label = label
                elif tag == "tse-ed-t_SecuritiesCode":  # 証券コード
                    info.SecuritiesCode.set_value(value)
                    info.SecuritiesCode.label = label
                elif tag == "tse-ed-t_Tel":  # 電話番号
                    info.Tel.set_value(value)
                    info.Tel.label = label
                elif tag == "tse-ed-t_URL":  # URL
                    info.URL.set_value(value)
                    info.URL.label = label
                elif "tse-ed-t_TokyoStockExchange" in tag:  # 東京証券取引所の上場市場
                    info.TokyoStockExchange.set_value(value)
                    info.TokyoStockExchange.label = label
    # endregion

    if period == "FY":
        result = sc.FiscalYearStockInfo.from_parent(info)
        for node in tree.all_nodes():
            tag = node.tag
            try:
                data = node.data.items.data[0]
                value = data.value
                label = node.data.label
            except AttributeError:
                continue
            if (
                tag == "tse-ed-t_ConveningBriefingOfAnnualResults"
            ):  # 決算説明会の開催の有無
                result.ConveningBriefingOfAnnualResults.set_value(value)
                result.ConveningBriefingOfAnnualResults.label = label
            elif (
                tag == "tse-ed-t_AnnualSecuritiesReportFilingDateAsPlanned"
            ):  # 有価証券報告書提出予定日
                result.AnnualSecuritiesReportFilingDateAsPlanned.set_value(value)
                result.AnnualSecuritiesReportFilingDateAsPlanned.label = label
            elif (
                tag == "tse-ed-t_DateOfGeneralShareholdersMeetingAsPlanned"
            ):  # 定時株主総会の開催予定日
                result.DateOfGeneralShareholdersMeetingAsPlanned.set_value(value)
                result.DateOfGeneralShareholdersMeetingAsPlanned.label = label
            elif tag == "tse-ed-t_DividendPayableDateAsPlanned":  # 配当支払予定日
                result.DividendPayableDateAsPlanned.set_value(value)
                result.DividendPayableDateAsPlanned.label = label
            result.QuarterlyPeriod.set_value("FY")  # 四半期
            result.QuarterlyPeriod.label = "四半期"

        return result

    elif period in ["Q1", "Q2", "Q3"]:
        for node in tree.all_nodes():
            tag = node.tag
            try:
                data = node.data.items.data[0]
                value = data.value
                label = node.data.label
            except AttributeError:
                continue
            if tag == "tse-ed-t_QuarterlyPeriod":  # 四半期
                info.QuarterlyPeriod.set_value(value)
                info.QuarterlyPeriod.label = label
        return info


@router.get("/summary/items/", response_model=sc.SummaryItemsAbstractJpList)
def read_summary_items(
    *,
    session: SessionDep,
    code: str = Query(...),  # 銘柄コード
    length: Optional[int] = Query(None),  # 期間
) -> sc.SummaryItemsAbstractJpList:
    """銘柄コードから決算情報を取得する"""

    summaryLst = []

    # region idの取得
    try:
        items = read_head_items(session=session, code=code, type=0, period=None).data
        if length is None:
            head_items = [item for item in items]
        else:
            head_items = [item for item in items][:length]
    except IndexError:
        raise HTTPException(status_code=404, detail="Item not found")
    # endregion

    for head_item in head_items:

        try:
            xbrl_id = head_item.xbrl_id
        except IndexError:
            raise HTTPException(status_code=404, detail="Item not found")

        # region ツリーの生成
        tree = utils.create_menu_items_tree(session=session, id=xbrl_id, type="sm")
        # endregion

        summary = utils.summary_result(tree)

        summaryLst.append(summary)

    return sc.SummaryItemsAbstractJpList(data=summaryLst, count=len(summaryLst))
    # endregion


@router.get("/summary/item/", response_model=sc.SummaryItemsAbstractJp)
def read_summary_item(
    *,
    session: SessionDep,
    code: str = Query(...),  # 銘柄コード
    count: Optional[int] = Query(None),  # 期間
) -> sc.SummaryItemsAbstractJp:
    """銘柄コードから決算情報を取得する"""

    # region idの取得
    try:
        items = read_head_items(session=session, code=code, type=0, period=None).data
        head_items = [item for item in items]
    except IndexError:
        raise HTTPException(status_code=404, detail="Item not found")
    # endregion
    try:
        if count:
            count = count
            head_item = head_items[count]
        else:
            head_item = head_items[0]
    except IndexError:
        raise HTTPException(status_code=404, detail="Item not found")

    try:
        xbrl_id = head_item.xbrl_id
    except IndexError:
        raise HTTPException(status_code=404, detail="Item not found")

    # region ツリーの生成
    tree = utils.create_menu_items_tree(session=session, id=xbrl_id, type="sm")
    # endregion

    summary = utils.summary_result(tree)

    summary.XbrlId = xbrl_id

    return summary
    # endregion


@router.get("/summary/item/{xbrl_id}", response_model=sc.SummaryItemsAbstractJp)
def read_summary_item_by_xbrl_id(
    *,
    session: SessionDep,
    xbrl_id: str,  # XBRLファイルのID
) -> sc.SummaryItemsAbstractJp:
    """XBRLファイルのIDから決算情報を取得する"""

    # region ツリーの生成
    tree = utils.create_menu_items_tree(session=session, id=xbrl_id, type="sm")
    # endregion

    summary = utils.summary_result(tree)

    return summary
    # endregion
