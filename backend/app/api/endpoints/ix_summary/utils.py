import datetime
import re
from collections import defaultdict

from sqlmodel import Session

from app.models import IxHeadTitle, IxNonFraction

from . import crud
from . import schema as sc
from .exceptions import HeadItemNotFound, NotDictKeyError
from .summaryItems import SummaryItems


def get_head_item_key(
    session: Session,
    code: str,
    head_item_key: str | None = None,
    report_types: list[str] | None = None,
    current_period: str | None = None,
    year: str | None = None,
    offset: int = 0,
) -> str:
    """
    #### この関数は、head_item_keyを取得する関数です。
    - **機能**:head_item_keyを取得します。
    - **引数**:session: Session
    - **引数**:head_item_key: str | None - head_item_key
    - **引数**:code: str - 証券コード
    - **引数**:report_types: list[str] | None - レポートタイプ
    - **引数**:current_period: str | None - 現在の期間
    - **引数**:year: str | None - 年
    - **引数**:offset: int - オフセット
    - **戻り値**:str - head_item_key
    - **例外**:HeadItemNotFound - head item not found.
    """
    if head_item_key is None:
        head_item = crud.get_ix_head_title(
            session=session,
            code=code,
            report_types=report_types,
            offset=offset,
            current_period=current_period,
            year=year,
        )
        head_item_key = head_item.item_key if head_item else None
        if not head_item_key:
            raise HeadItemNotFound("head item not found.2")
    else:
        if offset > 0:
            try:
                head_item_key = get_base_head_item_key_offset(
                    session=session,
                    headItemKey=head_item_key,
                    report_types=report_types,
                    offset=offset,
                )
            except HeadItemNotFound:
                raise

    return head_item_key


def get_context_list(items: sc.TreeItemsList, attr_value: str) -> list[list[str]]:
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


def get_metric_schema_value_and_change(
    items: list[IxNonFraction],
    schema_items: list[sc.FinValueFinance],
    child_items: dict[str, str],
    metric_contexts: list[str],
) -> None:
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


def get_attr_value(head_item: IxHeadTitle, attr_value_dict: dict[str, str]) -> str:
    # region attr_valueの設定
    if head_item.current_period is None:  # head_itemが存在しない場合、例外を発生させる
        raise HeadItemNotFound("head item not found.1")
    elif (
        head_item.current_period == "FY"
    ):  # head_itemのcurrent_periodがFYの場合、attr_valueをFYに設定
        attr_value = attr_value_dict["FY"]
    else:  # head_itemのcurrent_periodがQUの場合、attr_valueをQUに設定
        attr_value = attr_value_dict["QU"]
    # endregion

    return attr_value


def get_from_name(from_names: dict[str, str], tree_items: sc.TreeItemsList) -> str:
    # region is_consolidatedの設定
    is_consolidated = any(  # is_consolidatedを取得
        item.xlink_to == "tse-ed-t_ConsolidatedMember" for item in tree_items.data
    )

    if is_consolidated:  # is_consolidatedがTrueの場合、from_nameを"consolidated"に設定
        from_name = from_names["consolidated"]
    else:  # is_consolidatedがFalseの場合、from_nameを"non_consolidated"に設定
        from_name = from_names["non_consolidated"]
    # endregion

    return from_name


def get_parent_items(tree_items: sc.TreeItemsList, from_name: list[str]) -> list[str]:
    parent_items = [
        item.xlink_to for item in tree_items.data if item.xlink_from in from_name
    ]

    return parent_items


def get_child_items(
    tree_items: sc.TreeItemsList,
    from_names: list[str],
    is_change: bool,
    parent_items: list[str],
) -> dict[str, str]:
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
            if item.xlink_from in from_names
        }
    # endregion

    return child_items


def var_init(
    session: Session,
    head_item_key: str,
    attr_value_dict: dict[str, str],
    from_names: list[str],
    is_change: bool = True,
):
    # region 引数のバリデーション
    # キーのバリデーションを行い、エラーがあれば例外を発生させる
    if not list(attr_value_dict.keys()).__eq__(
        ["FY", "QU"]
    ):  # attr_value_dictのキーがFY, QUでない場合、例外を発生させる
        raise NotDictKeyError("not dict keys error. keys must be 'FY' or 'QU'.")
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

    # region parent_itemsの取得
    parent_items = get_parent_items(tree_items, from_names)

    child_items = get_child_items(
        tree_items=tree_items,
        from_names=from_names,
        is_change=is_change,
        parent_items=parent_items,
    )

    # contextの取得
    context_list = get_context_list(tree_items, attr_value)

    return (
        head_item,
        attr_value,
        tree_items,
        parent_items,
        child_items,
        context_list,
    )


def get_summary_items(
    session: Session,
    head_item_key: str,
    attr_value_dict: dict[str, str],
    from_names: list[str],
    is_change: bool = True,
) -> SummaryItems:
    """
    #### この関数は、指定された条件に一致するiXBRLの非分数情報を取得する関数です。
    - **機能**:指定された条件に一致するiXBRLの非分数情報を取得します。
    - **引数**:session: Session, head_item_key: str, attr_value_dict: Dict[str, str], from_names: List[str]
    - **戻り値**:sc.FinStructBase
    - **例外**:NotDictKeyError, HeadItem
    """

    (
        head_item,
        attr_value,
        tree_items,
        parent_items,
        child_items,
        context_list,
    ) = var_init(
        session=session,
        head_item_key=head_item_key,
        attr_value_dict=attr_value_dict,
        from_names=from_names,
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
        from_names=from_names,
        parent_items=parent_items,
        child_items=child_items,
        context_list=context_list,
        ix_non_fractions=ix_non_fractions,
    )

    return items


def create_fin_value_base(item):
    """itemからsc.FinValueBaseを生成する共通関数"""
    return sc.FinValueBase(
        name=item.name,
        value=item.numeric,
        unit=item.unit_ref,
        display_scale=item.display_scale,
        scale=item.scale,
    )


def set_result_value(struct_item_result, item, value_type):
    """
    struct_item_resultのcurValue/curChange/preValue/preChangeに値をセットする共通関数
    value_type: 'curValue', 'curChange', 'preValue', 'preChange'
    """
    value = create_fin_value_base(item)
    setattr(struct_item_result, value_type, value)
    if value.value is not None:
        struct_item_result.isActive = True


def set_struct_item_value(struct_item_part, item):
    """
    struct_item_part（result/forecast/upper/lower）にitemの値をセットしisActiveをTrueにする共通関数
    """
    if any(ctx.startswith("Next") for ctx in item.context):
        if item.name.startswith("tse-ed-t_ChangeIn"):
            set_result_value(struct_item_part, item, "curChange")
        else:
            set_result_value(struct_item_part, item, "curValue")
    elif any(ctx.startswith("Current") for ctx in item.context):
        if item.name.startswith("tse-ed-t_ChangeIn"):
            set_result_value(struct_item_part, item, "curChange")
        else:
            set_result_value(struct_item_part, item, "curValue")
    elif any(ctx.startswith("Prior") for ctx in item.context):
        if item.name.startswith("tse-ed-t_ChangeIn"):
            set_result_value(struct_item_part, item, "preChange")
        else:
            set_result_value(struct_item_part, item, "preValue")


def get_struct(
    items: SummaryItems,
    struct: sc.FinItemsResponse,
) -> sc.FinItemsResponse:
    """
    #### この関数は、FinItemsResponseを取得する関数です。
    - **機能**:FinItemsResponseを取得します。
    - **引数**:head_item: Any, tree_items: sc.TreeItemsList, ix_non_fractions: List[IxNonFraction], from_name: str, child_items: Dict[str, str]
    - **戻り値**:sc.FinItemsResponse
    """

    # structがsc.FinItemsResponseまたはその継承クラスでない場合、例外を発生させる
    if not isinstance(struct, sc.FinItemsResponse):
        raise TypeError("struct must be sc.FinItemsResponse or its subclass.")

    head_item = items.get_head_item()
    tree_items = items.get_tree_items()
    from_names = items.get_from_names()
    child_items = items.get_child_items()
    ix_non_fractions = items.get_ix_non_fractions()

    for item in tree_items.data:
        # from_nameと一致するxlink_fromを持つitemのみ処理
        if item.xlink_from in from_names:
            # structの全フィールドに対してループ
            for key in struct.__fields__.keys():
                # フィールドの値を取得
                field = getattr(struct, key)
                # フィールドがFinItemsBase型の場合のみ処理
                if isinstance(field, list):
                    # item情報をもとにFinValueFinanceを生成しdataリストに追加
                    field.append(
                        sc.FinValueFinance(
                            name=item.xlink_to,
                            order=item.xlink_order,
                            label=item.to_label,
                        )
                    )

    if isinstance(struct, sc.FinItemsResponse):
        # ix_non_fractionsの各itemについて処理
        for item in ix_non_fractions:
            # structの各フィールドごとに処理
            for structItem in struct.data:
                if structItem.name == child_items[item.name]:
                    if structItem.result.context in item.context:
                        set_struct_item_value(structItem.result, item)
                    elif structItem.forecast.context in item.context:
                        set_struct_item_value(structItem.forecast, item)
                    elif structItem.upper.context in item.context:
                        set_struct_item_value(structItem.upper, item)
                    elif structItem.lower.context in item.context:
                        set_struct_item_value(structItem.lower, item)

    period = sc.PeriodSchemaBase(  # periodを設定
        accountingStandard=head_item.report_type,
        fiscalYear=head_item.fy_year_end,
        period=head_item.current_period,
    )

    struct.period = period
    struct.head_item_key = head_item.item_key

    return struct


def get_metric_schema(
    structItem: sc.FinValueWithDividends,
    item: IxNonFraction,
) -> sc.FinValueWithDividends:
    """
    #### この関数は、FinValueWithDividendsを取得する関数です。
    - **機能**:FinValueWithDividendsを取得します。
    - **引数**:head_item: Any, tree_items: sc.TreeItemsList, ix_non_fractions: List[IxNonFraction], from_name: str, child_items: Dict[str, str]
    - **戻り値**:sc.FinValueWithDividends
    """
    # structがsc.FinItemsResponseまたはその継承クラスでない場合、例外を発生させる
    if not isinstance(structItem, sc.FinValueWithDividends):
        raise TypeError("struct must be sc.FinStructBase or its subclass.")

    if structItem.result.context in item.context:
        set_struct_item_value(structItem.result, item)
    if structItem.forecast.context in item.context:
        set_struct_item_value(structItem.forecast, item)
    if structItem.upper.context in item.context:
        set_struct_item_value(structItem.upper, item)
    if structItem.lower.context in item.context:
        set_struct_item_value(structItem.lower, item)

    return structItem


def set_dividends_other(
    structItem: sc.FinItemsDividendsResponse,
    items: list[IxNonFraction],
) -> sc.FinItemsDividendsResponse:
    """
    #### この関数は、FinItemsDividendsResponseを取得する関数です。
    - **機能**:FinItemsDividendsResponseを取得します。
    - **引数**:head_item: Any, tree_items: sc.TreeItemsList, ix_non_fractions: List[IxNonFraction], from_name: str, child_items: Dict[str, str]
    - **戻り値**:sc.FinItemsDividendsResponse
    """
    # structがsc.FinItemsResponseまたはその継承クラスでない場合、例外を発生させる
    if not isinstance(structItem, sc.FinItemsDividendsResponse):
        raise TypeError("struct must be sc.FinItemsDividendsResponse or its subclass.")

    names = [
        "tse-ed-t_TotalDividendPaidAnnual",
        "tse-ed-t_PayoutRatio",
        "tse-ed-t_RatioTotalAmountOfDividendTotalNetAssets",
        "tse-ed-t_RatioOfTotalAmountOfDividendsToNetAssets",
    ]

    for item in items:
        # structの各フィールドごとに処理
        if names[0] == item.name:
            if structItem.data.TotalDividendPaidAnnual.context in item.context:
                get_metric_schema(structItem.data.TotalDividendPaidAnnual, item)
        elif names[1] == item.name:
            if structItem.data.PayoutRatio.context in item.context:
                get_metric_schema(structItem.data.PayoutRatio, item)
        elif names[2] == item.name:
            if (
                structItem.data.RatioTotalAmountOfDividendTotalNetAssets.context
                in item.context
            ):
                get_metric_schema(
                    structItem.data.RatioTotalAmountOfDividendTotalNetAssets, item
                )
        elif names[3] == item.name:
            if (
                structItem.data.RatioTotalAmountOfDividendTotalNetAssets.context
                in item.context
            ):
                get_metric_schema(
                    structItem.data.RatioTotalAmountOfDividendTotalNetAssets, item
                )


def get_dividends_struct(
    items: SummaryItems,
    struct: sc.FinItemsDividendsResponse,
) -> sc.FinItemsDividendsResponse:
    """
    #### この関数は、FinValueDividendsを取得する関数です。
    - **機能**:FinValueDividendsを取得します。
    - **引数**:head_item: Any, tree_items: sc.TreeItemsList, ix_non_fractions: List[IxNonFraction], from_name: str, child_items: Dict[str, str]
    - **戻り値**:sc.FinValueDividends
    """

    # structがsc.FinItemsResponseまたはその継承クラスでない場合、例外を発生させる
    if not isinstance(struct, sc.FinItemsDividendsResponse):
        raise TypeError("struct must be sc.FinStructBase or its subclass.")

    head_item = items.get_head_item()
    tree_items = items.get_tree_items()
    from_names = items.get_from_names()
    ix_non_fractions = items.get_ix_non_fractions()

    for item in tree_items.data:
        # from_nameと一致するxlink_fromを持つitemのみ処理
        if item.xlink_from in from_names:
            # structの全フィールドに対してループ
            # item情報をもとにFinValueDividendsを生成しdataリストに追加
            struct.data = sc.FinValueDividends(
                name=item.xlink_to,
                order=item.xlink_order,
            )

    if isinstance(struct, sc.FinItemsDividendsResponse):
        # ix_non_fractionsの各itemについて処理
        for item in ix_non_fractions:
            # structの各フィールドごとに処理
            if item.name == "tse-ed-t_DividendPerShare":
                # if struct.data.name == child_items[item.name]:
                if struct.data.FirstQuarterMember.context in item.context:
                    get_metric_schema(struct.data.FirstQuarterMember, item)
                elif struct.data.SecondQuarterMember.context in item.context:
                    get_metric_schema(struct.data.SecondQuarterMember, item)
                elif struct.data.ThirdQuarterMember.context in item.context:
                    get_metric_schema(struct.data.ThirdQuarterMember, item)
                elif struct.data.YearEndMember.context in item.context:
                    get_metric_schema(struct.data.YearEndMember, item)
                elif struct.data.AnnualMember.context in item.context:
                    get_metric_schema(struct.data.AnnualMember, item)

    set_dividends_other(struct, ix_non_fractions)

    period = sc.PeriodSchemaBase(  # periodを設定
        accountingStandard=head_item.report_type,
        fiscalYear=head_item.fy_year_end,
        period=head_item.current_period,
    )

    struct.period = period
    struct.head_item_key = head_item.item_key

    return struct


def get_summary_items_list(
    head_item_keys: list[str],
    session: Session,
    attr_value_dict: dict[str, str],
    from_names: dict[str, str],
    is_change: bool = True,
) -> list[SummaryItems]:
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
                from_names=from_names,
                is_change=is_change,
            )
            items_list.append(items)
        except HeadItemNotFound:
            continue
        except NotDictKeyError as e:
            raise NotDictKeyError(str(e))

    return items_list


def get_base_head_item_key_offset(
    session: Session,
    headItemKey: str,
    report_types: list[str] | None = None,
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


def generate_summary_sentence(data: sc.FinItemsResponse) -> str:
    """
    指定されたデータから財務情報の要約文を生成する関数
    - **引数**: data: dict - 財務情報のデータ
    - **戻り値**: str - 財務情報の要約文
    - **例外**: 対象期間の財務情報が取得できない場合、適切なメッセージを返す
    """

    # 期間タイトルの取得
    yearDate = datetime.date.fromisoformat(data.period.fiscalYear).year
    period = data.period.period
    if period == "FY":
        period_title = f"{yearDate}年度通期"
    elif period == "HY":
        period_title = f"{yearDate}年度上期"
    elif period == "Q1":
        period_title = f"{yearDate}年度第1四半期"
    elif period == "Q2":
        period_title = f"{yearDate}年度第2四半期"
    elif period == "Q3":
        period_title = f"{yearDate}年度第3四半期"
    else:
        period_title = f"{yearDate}年度{period}期"

    # 要約文の生成
    phrases = []
    increase_count = 0
    decrease_count = 0

    revenue_change = None
    profit_change = None

    for item in data.data:
        label = item.label
        result = item.result
        cur_change = result.curChange

        if cur_change:
            if result.isActive is not True or cur_change.value is None:
                continue

            change_value = cur_change.value
            percentage = f"{abs(change_value):.1f}%"

            if change_value > 0:
                phrase = f"{label}は{percentage}増加"
                increase_count += 1
            elif change_value < 0:
                phrase = f"{label}は{percentage}減少"
                decrease_count += 1
            else:
                phrase = f"{label}は前年と同水準"

            phrases.append(phrase)

            # 増収増益などの判定に使う
            if "売上" in label or "収益" in label:
                revenue_change = change_value
            if "利益" in label:
                profit_change = change_value

    if not phrases:
        return "対象期間の財務情報は取得できませんでした。"

    # 要約の構築
    if len(phrases) > 1:
        summary = "、".join(phrases[:-1]) + "および" + phrases[-1]
    else:
        summary = phrases[0]

    # 全体コメントの決定
    if increase_count > decrease_count:
        comment = "前年同期比で好調な結果。"
    elif decrease_count > increase_count:
        comment = "前年同期比でやや不調な結果。"
    else:
        comment = "前年並みの結果。"

    # 増収増益などの判定
    trend = ""
    if revenue_change is not None and profit_change is not None:
        if revenue_change > 0 and profit_change > 0:
            trend = "増収増益、"
        elif revenue_change > 0 and profit_change < 0:
            trend = "増収減益、"
        elif revenue_change < 0 and profit_change > 0:
            trend = "減収増益、"
        elif revenue_change < 0 and profit_change < 0:
            trend = "減収減益、"
        else:
            trend = ""

    return f"{period_title}において、{summary}しました。{trend}{comment}"


def get_financial_summary(
    *,
    session: Session,
    code: str | None = None,
    head_item_key: str | None = None,
    report_types: list[str] | None = None,
    offset: int = 0,
) -> str:
    """
    財務サマリー情報を取得するエンドポイント。

    Args:
        session (Session): データベースセッション依存性。
        code (str | None, optional): 銘柄コード。指定しない場合はhead_item_keyを利用。
        head_item_key (str | None, optional): ヘッドアイテムキー。指定しない場合はcodeを利用。
        report_types (list[str] | None, optional): レポートタイプのリスト。
        offset (int, optional): オフセット値。デフォルトは0。

    Raises:
        HeadItemNotFound: パラメータ不正やデータが見つからない場合に発生。

    Returns:
        str: 財務サマリー情報の文字列。
    """
    ope = get_operating_results(
        session=session,
        code=code,
        head_item_key=head_item_key,
        report_types=report_types,
        offset=offset,
    )

    titles = generate_summary_sentence(ope)

    if not titles:
        raise HeadItemNotFound(
            "指定された銘柄コードまたはhead_item_keyに対応するタイトル情報が見つかりません。"
        )

    return titles


def get_operating_results(
    *,
    session: Session,
    code: str | None = None,
    head_item_key: str | None = None,
    report_types: list[str] | None = None,
    offset: int = 0,
) -> sc.FinItemsResponse:
    """
    経営成績情報を取得するエンドポイント。

    Args:
        session (Session): データベースセッション依存性。
        code (str | None, optional): 銘柄コード。指定しない場合はhead_item_keyを利用。
        head_item_key (str | None, optional): ヘッドアイテムキー。指定しない場合はcodeを利用。
        report_types (list[str] | None, optional): レポートタイプのリスト。
        offset (int, optional): オフセット値。デフォルトは0。

    Raises:
        HeadItemNotFound: パラメータ不正やデータが見つからない場合に発生。

    Returns:
        sc.FinItemsResponse: 経営成績情報のレスポンスモデル。
    """
    if code is None and head_item_key is None:
        raise HeadItemNotFound(
            "銘柄コードかhead_item_keyどちらかを指定してください",
        )

    attr_value_dict = {  # この辞書は、attr_valueとfrom_nameの対応を表しています。
        "FY": "BusinessResultsOperatingResults",
        "QU": "BusinessResultsQuarterlyOperatingResults",
    }

    from_names = [
        "tse-ed-t_ConsolidatedIncomeStatementsInformationAbstract",
        "tse-ed-t_IncomeStatementsInformationAbstract",
    ]

    # head_item_keyを取得
    try:
        head_item_key = get_head_item_key(
            session=session,
            head_item_key=head_item_key,
            code=code,
            report_types=report_types,
            offset=offset,
        )
    except HeadItemNotFound as e:
        raise HeadItemNotFound(str(e))

    try:
        item = get_summary_items(
            session=session,
            head_item_key=head_item_key,
            attr_value_dict=attr_value_dict,
            from_names=from_names,
            is_change=True,
        )
    except NotDictKeyError as e:
        raise HeadItemNotFound(str(e))
    except HeadItemNotFound as e:
        raise HeadItemNotFound(str(e))

    result = get_struct(
        items=item,
        struct=sc.FinItemsResponse(),
    )

    return result


def get_other_operating_results(
    *,
    session: Session,
    code: str | None = None,
    head_item_key: str | None = None,
    report_types: list[str] | None = None,
    offset: int = 0,
) -> sc.FinItemsResponse:
    """
    その他の経営成績情報を取得するエンドポイント。
    Args:
        session (Session): データベースセッション依存性。
        code (str | None, optional): 銘柄コード。指定しない場合はhead_item_keyを利用。
        head_item_key (str | None, optional): ヘッドアイテムキー。指定しない場合はcodeを利用。
        report_types (list[str] | None, optional): レポートタイプのリスト。
        offset (int, optional): オフセット値。デフォルトは0。
    Raises:
        HeadItemNotFound: パラメータ不正やデータが見つからない場合に発生。
    Returns:
        sc.FinItemsResponse: その他の経営成績情報のレスポンスモデル。
    """
    if code and head_item_key:
        raise HeadItemNotFound(
            "銘柄コードかhead_item_keyどちらかを指定してください",
        )

    attr_value_dict = {
        "FY": "BusinessResultsOperatingResults",
        "QU": "BusinessResultsQuarterlyOperatingResults",
    }

    from_names = [
        "tse-ed-t_OtherConsolidatedOperatingResultsAbstract",
        "tse-ed-t_OtherOperatingResultsAbstract",
    ]

    # head_item_keyを取得
    try:
        head_item_key = get_head_item_key(
            session=session,
            head_item_key=head_item_key,
            code=code,
            report_types=report_types,
            offset=offset,
        )
    except HeadItemNotFound as e:
        raise HeadItemNotFound(str(e))

    try:
        item = get_summary_items(
            session=session,
            head_item_key=head_item_key,
            attr_value_dict=attr_value_dict,
            from_names=from_names,
            is_change=False,
        )
    except NotDictKeyError as e:
        raise HeadItemNotFound(str(e))
    except HeadItemNotFound as e:
        raise HeadItemNotFound(str(e))

    result = get_struct(
        items=item,
        struct=sc.FinItemsResponse(),
    )

    return result


def get_forecasts(
    *,
    session: Session,
    code: str | None = None,
    head_item_key: str | None = None,
    report_types: list[str] | None = None,
    offset: int = 0,
) -> sc.FinItemsResponse:
    """
    予測情報を取得するエンドポイント。
    Args:
        session (Session): データベースセッション依存性。
        code (str | None, optional): 銘柄コード。指定しない場合はhead_item_keyを利用。
        head_item_key (str | None, optional): ヘッドアイテムキー。指定しない場合はcodeを利用。
        report_types (list[str] | None, optional): レポートタイプのリスト。
        offset (int, optional): オフセット値。デフォルトは0。
    Raises:
        HeadItemNotFound: パラメータ不正やデータが見つからない場合に発生。
    Returns:
        sc.FinItemsResponse: 予測情報のレスポンスモデル。
    """
    if code and head_item_key:
        raise HeadItemNotFound(
            "銘柄コードかhead_item_keyどちらかを指定してください",
        )

    attr_value_dict = {
        "FY": "Forecasts",
        "QU": "QuarterlyForecasts",
    }

    from_names = [
        "tse-ed-t_MainTableOfConsolidatedForecastsAbstract",
        "tse-ed-t_MainTableOfForecastsAbstract",
    ]

    # head_item_keyを取得
    try:
        head_item_key = get_head_item_key(
            session=session,
            head_item_key=head_item_key,
            code=code,
            report_types=report_types,
            offset=offset,
        )
    except HeadItemNotFound as e:
        raise HeadItemNotFound(str(e))

    try:
        item = get_summary_items(
            session=session,
            head_item_key=head_item_key,
            attr_value_dict=attr_value_dict,
            from_names=from_names,
            is_change=True,
        )
    except NotDictKeyError as e:
        raise HeadItemNotFound(str(e))
    except HeadItemNotFound as e:
        raise HeadItemNotFound(str(e))

    result = get_struct(
        items=item,
        struct=sc.FinItemsResponse(),
    )

    return result


def get_financial_position(
    *,
    session: Session,
    code: str | None = None,
    head_item_key: str | None = None,
    report_types: list[str] | None = None,
    offset: int = 0,
) -> sc.FinItemsResponse:
    """
    財政状態情報を取得するエンドポイント。
    Args:
        session (Session): データベースセッション依存性。
        code (str | None, optional): 銘柄コード。指定しない場合はhead_item_keyを利用。
        head_item_key (str | None, optional): ヘッドアイテムキー。指定しない場合はcodeを利用。
        report_types (list[str] | None, optional): レポートタイプのリスト。
        offset (int, optional): オフセット値。デフォルトは0。
    Raises:
        HeadItemNotFound: パラメータ不正やデータが見つからない場合に発生。
    Returns:
        sc.FinItemsResponse: 財政状態情報のレスポンスモデル。
    """
    if code and head_item_key:
        raise HeadItemNotFound(
            "銘柄コードかhead_item_keyどちらかを指定してください",
        )

    attr_value_dict = {
        "FY": "BusinessResultsFinancialPositions",
        "QU": "BusinessResultsQuarterlyFinancialPositions",
    }

    from_names = [
        "tse-ed-t_ConsolidatedFinancialPositionsAbstract",
        "tse-ed-t_FinancialPositionsAbstract",
    ]

    # head_item_keyを取得
    try:
        head_item_key = get_head_item_key(
            session=session,
            head_item_key=head_item_key,
            code=code,
            report_types=report_types,
            offset=offset,
        )
    except HeadItemNotFound as e:
        raise HeadItemNotFound(str(e))

    try:
        item = get_summary_items(
            session=session,
            head_item_key=head_item_key,
            attr_value_dict=attr_value_dict,
            from_names=from_names,
            is_change=False,
        )
    except NotDictKeyError as e:
        raise HeadItemNotFound(str(e))
    except HeadItemNotFound as e:
        raise HeadItemNotFound(str(e))

    result = get_struct(
        items=item,
        struct=sc.FinItemsResponse(),
    )

    return result


def get_cash_flows(
    *,
    session: Session,
    code: str,
    year: str | None = None,
    offset: int = 0,
) -> sc.FinItemsResponse:
    """
    キャッシュフロー情報を取得するエンドポイント。
    Args:
        session (Session): データベースセッション依存性。
        code (str): 銘柄コード。
        year (str | None, optional): 年度。指定しない場合は最新の年度を利用。
        offset (int, optional): オフセット値。デフォルトは0。
    Raises:
        HeadItemNotFound: パラメータ不正やデータが見つからない場合に発生。
    Returns:
        sc.FinItemsResponse: キャッシュフロー情報のレスポンスモデル。
    """
    attr_value_dict = {
        "FY": "BusinessResultsCashFlows",
        "QU": "BusinessResultsQuarterlyCashFlows",
    }

    from_names = [
        "tse-ed-t_ConsolidatedCashFlowsAbstract",
        "tse-ed-t_CashFlowsAbstract",
    ]

    try:
        head_item_key = get_head_item_key(
            session=session,
            code=code,
            report_types=["edjp", "edif", "edus"],
            offset=offset,
            year=year,
            current_period="FY",
        )
    except HeadItemNotFound as e:
        raise HeadItemNotFound(str(e))

    try:
        item = get_summary_items(
            session=session,
            head_item_key=head_item_key,
            attr_value_dict=attr_value_dict,
            from_names=from_names,
            is_change=False,
        )
    except NotDictKeyError as e:
        raise HeadItemNotFound(str(e))
    except HeadItemNotFound as e:
        raise HeadItemNotFound(str(e))

    result = get_struct(
        items=item,
        struct=sc.FinItemsResponse(),
    )

    return result


def get_forecast_change(
    *,
    session: Session,
    head_item_key: str | None = None,
    code: str | None = None,
    report_types: list[str] | None = None,
    offset: int = 0,
) -> bool | None:
    """
    業績予想の変更情報を取得するエンドポイント。
    Args:
        session (Session): データベースセッション依存性。
        head_item_key (str | None, optional): ヘッドアイテムキー。指定しない場合はcodeを利用。
        code (str | None, optional): 銘柄コード。指定しない場合はhead_item_keyを利用。
        report_types (list[str] | None, optional): レポートタイプのリスト。
        offset (int, optional): オフセット値。デフォルトは0。
    Raises:
        HeadItemNotFound: パラメータ不正やデータが見つからない場合に発生。
    Returns:
        bool | None: 業績予想の変更情報。変更がない場合はNone。
    """
    if head_item_key is None:
        try:
            head_item_key = get_head_item_key(
                session=session, code=code, report_types=report_types, offset=offset
            )
        except HeadItemNotFound as e:
            raise HeadItemNotFound(str(e))
    else:
        if offset > 0:
            try:
                head_item_key = get_base_head_item_key_offset(
                    session=session,
                    headItemKey=head_item_key,
                    report_types=report_types,
                    offset=offset,
                )
            except HeadItemNotFound as e:
                raise HeadItemNotFound(str(e))

    names = [
        "tse-ed-t_CorrectionOfConsolidatedFinancialForecastInThisQuarter",
        "tse-ed-t_CorrectionOfNonConsolidatedFinancialForecastInThisQuarter",
        "tse-ed-t_CorrectionOfFinancialForecastInThisQuarter",
    ]

    item = crud.is_change_value(
        session=session, head_item_key=head_item_key, names=names
    )

    return item


def get_dividends_change(
    *,
    session: Session,
    head_item_key: str | None = None,
    code: str | None = None,
    report_types: list[str] | None = None,
    offset: int = 0,
) -> bool | None:
    """
    配当予想の変更情報を取得するエンドポイント。
    Args:
        session (Session): データベースセッション依存性。
        head_item_key (str | None, optional): ヘッドアイテムキー。指定しない場合はcodeを利用。
        code (str | None, optional): 銘柄コード。指定しない場合はhead_item_keyを利用。
        report_types (list[str] | None, optional): レポートタイプのリスト。
        offset (int, optional): オフセット値。デフォルトは0。
    Raises:
        HeadItemNotFound: パラメータ不正やデータが見つからない場合に発生。
    Returns:
        bool | None: 配当予想の変更情報。変更がない場合はNone。
    """
    if head_item_key is None:
        try:
            head_item_key = get_head_item_key(
                session=session, code=code, report_types=report_types, offset=offset
            )
        except HeadItemNotFound as e:
            raise HeadItemNotFound(str(e))
    else:
        if offset > 0:
            try:
                head_item_key = get_base_head_item_key_offset(
                    session=session,
                    headItemKey=head_item_key,
                    report_types=report_types,
                    offset=offset,
                )
            except HeadItemNotFound as e:
                raise HeadItemNotFound(str(e))

    names = ["tse-ed-t_CorrectionOfDividendForecastInThisQuarter"]

    item = crud.is_change_value(
        session=session, head_item_key=head_item_key, names=names
    )

    return item


def get_dividends(
    *,
    session: Session,
    code: str | None = None,
    head_item_key: str | None = None,
    report_types: list[str] | None = None,
    offset: int = 0,
) -> sc.FinItemsDividendsResponse:
    """
    配当情報を取得するエンドポイント。
    Args:
        session (Session): データベースセッション依存性。
        code (str | None, optional): 銘柄コード。指定しない場合はhead_item_keyを利用。
        head_item_key (str | None, optional): ヘッドアイテムキー。指定しない場合はcodeを利用。
        report_types (list[str] | None, optional): レポートタイプのリスト。
        offset (int, optional): オフセット値。デフォルトは0。
    Raises:
        HeadItemNotFound: パラメータ不正やデータが見つからない場合に発生。
    Returns:
        sc.FinItemsDividendsResponse: 配当情報のレスポンスモデル。
    """
    if code and head_item_key:
        raise HeadItemNotFound(
            "銘柄コードかhead_item_keyどちらかを指定してください",
        )

    attr_value_dict = {
        "FY": "Dividends",
        "QU": "QuarterlyDividends",
    }

    from_names = [
        "tse-ed-t_DividendPerShareAbstract",
        "tse-ed-t_TotalDividendPaidAnnualAbstract",
        "tse-ed-t_PayoutRatioConsolidatedAbstract",
        "tse-ed-t_RatioOfTotalAmountOfDividendsToNetAssetsAbstract",
        "tse-ed-t_RatioOfTotalAmountOfDividendsToNetAssetsConsolidatedAbstract",
    ]

    if head_item_key is None:
        try:
            head_item_key = get_head_item_key(
                session=session, code=code, report_types=report_types, offset=offset
            )
        except HeadItemNotFound as e:
            raise HeadItemNotFound(str(e))
    else:
        if offset > 0:
            try:
                head_item_key = get_base_head_item_key_offset(
                    session=session,
                    headItemKey=head_item_key,
                    report_types=report_types,
                    offset=offset,
                )
            except HeadItemNotFound as e:
                raise HeadItemNotFound(str(e))

    try:
        item = get_summary_items(
            session=session,
            head_item_key=head_item_key,
            attr_value_dict=attr_value_dict,
            from_names=from_names,
            is_change=False,
        )
    except NotDictKeyError as e:
        raise HeadItemNotFound(str(e))
    except HeadItemNotFound as e:
        raise HeadItemNotFound(str(e))

    result = get_dividends_struct(
        items=item,
        struct=sc.FinItemsDividendsResponse(),
    )

    return result
