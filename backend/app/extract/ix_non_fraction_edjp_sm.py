from app.models import IxNonFraction
from sqlmodel import Session, select, func

def average_number_of_shares(session: Session, head_item_key:str, context:str):
    """
    期中平均株式数
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_AverageNumberOfShares',
            IxNonFraction.head_item_key == head_item_key,
            IxNonFraction.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def capital_adequacy_ratio(session: Session, head_item_key:str, context:str):
    """
    自己資本比率
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_CapitalAdequacyRatio',
            IxNonFraction.head_item_key == head_item_key,
            IxNonFraction.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def cash_and_equivalents_end_of_period(session: Session, head_item_key:str, context:str):
    """
    現金及び現金同等物期末残高
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_CashAndEquivalentsEndOfPeriod',
            IxNonFraction.head_item_key == head_item_key,
            IxNonFraction.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def cash_flows_from_financing_activities(session: Session, head_item_key:str, context:str):
    """
    財務活動によるキャッシュ・フロー
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_CashFlowsFromFinancingActivities',
            IxNonFraction.head_item_key == head_item_key,
            IxNonFraction.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def cash_flows_from_investing_activities(session: Session, head_item_key:str, context:str):
    """
    投資活動によるキャッシュ・フロー
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_CashFlowsFromInvestingActivities',
            IxNonFraction.head_item_key == head_item_key,
            IxNonFraction.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def cash_flows_from_operating_activities(session: Session, head_item_key:str, context:str):
    """
    営業活動によるキャッシュ・フロー
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_CashFlowsFromOperatingActivities',
            IxNonFraction.head_item_key == head_item_key,
            IxNonFraction.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def change_in_comprehensive_income(session: Session, head_item_key:str, context:str):
    """
    包括利益増減率
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_ChangeInComprehensiveIncome',
            IxNonFraction.head_item_key == head_item_key,
            IxNonFraction.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def change_in_net_income(session: Session, head_item_key:str, context:str):
    """
    増減率、当期純利益
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_ChangeInNetIncome',
            IxNonFraction.head_item_key == head_item_key,
            IxNonFraction.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def change_in_net_sales(session: Session, head_item_key:str, context:str):
    """
    増減率、売上高
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_ChangeInNetSales',
            IxNonFraction.head_item_key == head_item_key,
            IxNonFraction.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def change_in_operating_income(session: Session, head_item_key:str, context:str):
    """
    増減率、営業利益
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_ChangeInOperatingIncome',
            IxNonFraction.head_item_key == head_item_key,
            IxNonFraction.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def change_in_operating_revenues(session: Session, head_item_key:str, context:str):
    """
    増減率、営業収益
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_ChangeInOperatingRevenues',
            IxNonFraction.head_item_key == head_item_key,
            IxNonFraction.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def change_in_ordinary_income(session: Session, head_item_key:str, context:str):
    """
    増減率、経常利益
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_ChangeInOrdinaryIncome',
            IxNonFraction.head_item_key == head_item_key,
            IxNonFraction.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def change_in_ordinary_revenues_bk(session: Session, head_item_key:str, context:str):
    """
    増減率、経常収益、銀行
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_ChangeInOrdinaryRevenuesBK',
            IxNonFraction.head_item_key == head_item_key,
            IxNonFraction.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def change_in_ordinary_revenues_in(session: Session, head_item_key:str, context:str):
    """
    増減率、経常収益、保険
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_ChangeInOrdinaryRevenuesIN',
            IxNonFraction.head_item_key == head_item_key,
            IxNonFraction.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def change_in_profit_attributable_to_owners_of_parent(session: Session, head_item_key:str, context:str):
    """
    増減率、親会社株主に帰属する当期純利益
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_ChangeInProfitAttributableToOwnersOfParent',
            IxNonFraction.head_item_key == head_item_key,
            IxNonFraction.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def change_in_revenue(session: Session, head_item_key:str, context:str):
    """
    増減率、売上収益
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_ChangeInRevenue',
            IxNonFraction.head_item_key == head_item_key,
            IxNonFraction.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def commemorative_dividend(session: Session, head_item_key:str, context:str):
    """
    記念配当
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_CommemorativeDividend',
            IxNonFraction.head_item_key == head_item_key,
            IxNonFraction.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def comprehensive_income(session: Session, head_item_key:str, context:str):
    """
    包括利益
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_ComprehensiveIncome',
            IxNonFraction.head_item_key == head_item_key,
            IxNonFraction.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def diluted_net_income_per_share(session: Session, head_item_key:str, context:str):
    """
    潜在株式調整後1株当たり当期純利益
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_DilutedNetIncomePerShare',
            IxNonFraction.head_item_key == head_item_key,
            IxNonFraction.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def dividend_per_share(session: Session, head_item_key:str, context:str):
    """
    1株当たり配当金
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_DividendPerShare',
            IxNonFraction.head_item_key == head_item_key,
            IxNonFraction.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def extra_dividend(session: Session, head_item_key:str, context:str):
    """
    特別配当
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_ExtraDividend',
            IxNonFraction.head_item_key == head_item_key,
            IxNonFraction.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def investment_profit_loss_on_equity_method(session: Session, head_item_key:str, context:str):
    """
    持分法投資損益
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_InvestmentProfitLossOnEquityMethod',
            IxNonFraction.head_item_key == head_item_key,
            IxNonFraction.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def net_assets(session: Session, head_item_key:str, context:str):
    """
    純資産
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_NetAssets',
            IxNonFraction.head_item_key == head_item_key,
            IxNonFraction.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def net_assets_per_share(session: Session, head_item_key:str, context:str):
    """
    1株当たり純資産
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_NetAssetsPerShare',
            IxNonFraction.head_item_key == head_item_key,
            IxNonFraction.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def net_income(session: Session, head_item_key:str, context:str):
    """
    当期純利益
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_NetIncome',
            IxNonFraction.head_item_key == head_item_key,
            IxNonFraction.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def net_income_per_share(session: Session, head_item_key:str, context:str):
    """
    1株当たり当期純利益
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_NetIncomePerShare',
            IxNonFraction.head_item_key == head_item_key,
            IxNonFraction.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def net_income_to_shareholders_equity_ratio(session: Session, head_item_key:str, context:str):
    """
    自己資本当期純利益率
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_NetIncomeToShareholdersEquityRatio',
            IxNonFraction.head_item_key == head_item_key,
            IxNonFraction.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def net_sales(session: Session, head_item_key:str, context:str):
    """
    売上高
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_NetSales',
            IxNonFraction.head_item_key == head_item_key,
            IxNonFraction.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def number_of_issued_and_outstanding_shares_at_the_end_of_fiscal_year_including_treasury_stock(session: Session, head_item_key:str, context:str):
    """
    期末発行済株式数（自己株式を含む）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_NumberOfIssuedAndOutstandingSharesAtTheEndOfFiscalYearIncludingTreasuryStock',
            IxNonFraction.head_item_key == head_item_key,
            IxNonFraction.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def number_of_subsidiaries_excluded_from_consolidation(session: Session, head_item_key:str, context:str):
    """
    除外
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_NumberOfSubsidiariesExcludedFromConsolidation',
            IxNonFraction.head_item_key == head_item_key,
            IxNonFraction.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def number_of_subsidiaries_newly_consolidated(session: Session, head_item_key:str, context:str):
    """
    新規
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_NumberOfSubsidiariesNewlyConsolidated',
            IxNonFraction.head_item_key == head_item_key,
            IxNonFraction.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def number_of_treasury_stock_at_the_end_of_fiscal_year(session: Session, head_item_key:str, context:str):
    """
    期末自己株式数
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_NumberOfTreasuryStockAtTheEndOfFiscalYear',
            IxNonFraction.head_item_key == head_item_key,
            IxNonFraction.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def operating_income(session: Session, head_item_key:str, context:str):
    """
    営業利益
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_OperatingIncome',
            IxNonFraction.head_item_key == head_item_key,
            IxNonFraction.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def operating_income_to_net_sales_ratio(session: Session, head_item_key:str, context:str):
    """
    売上高営業利益率
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_OperatingIncomeToNetSalesRatio',
            IxNonFraction.head_item_key == head_item_key,
            IxNonFraction.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def operating_income_to_operating_revenues_ratio(session: Session, head_item_key:str, context:str):
    """
    営業収益営業利益率
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_OperatingIncomeToOperatingRevenuesRatio',
            IxNonFraction.head_item_key == head_item_key,
            IxNonFraction.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def operating_revenues(session: Session, head_item_key:str, context:str):
    """
    営業収益
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_OperatingRevenues',
            IxNonFraction.head_item_key == head_item_key,
            IxNonFraction.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def ordinary_income(session: Session, head_item_key:str, context:str):
    """
    経常利益
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_OrdinaryIncome',
            IxNonFraction.head_item_key == head_item_key,
            IxNonFraction.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def ordinary_income_to_total_assets_ratio(session: Session, head_item_key:str, context:str):
    """
    総資産経常利益率
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_OrdinaryIncomeToTotalAssetsRatio',
            IxNonFraction.head_item_key == head_item_key,
            IxNonFraction.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def ordinary_revenues_bk(session: Session, head_item_key:str, context:str):
    """
    経常収益、銀行
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_OrdinaryRevenuesBK',
            IxNonFraction.head_item_key == head_item_key,
            IxNonFraction.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def ordinary_revenues_in(session: Session, head_item_key:str, context:str):
    """
    経常収益、保険
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_OrdinaryRevenuesIN',
            IxNonFraction.head_item_key == head_item_key,
            IxNonFraction.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def owners_equity(session: Session, head_item_key:str, context:str):
    """
    自己資本
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_OwnersEquity',
            IxNonFraction.head_item_key == head_item_key,
            IxNonFraction.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def payout_ratio(session: Session, head_item_key:str, context:str):
    """
    配当性向
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_PayoutRatio',
            IxNonFraction.head_item_key == head_item_key,
            IxNonFraction.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def profit_attributable_to_owners_of_parent(session: Session, head_item_key:str, context:str):
    """
    親会社株主に帰属する当期純利益
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_ProfitAttributableToOwnersOfParent',
            IxNonFraction.head_item_key == head_item_key,
            IxNonFraction.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def quarterly_period(session: Session, head_item_key:str, context:str):
    """
    四半期
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_QuarterlyPeriod',
            IxNonFraction.head_item_key == head_item_key,
            IxNonFraction.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def ratio_of_total_amount_of_dividends_to_net_assets(session: Session, head_item_key:str, context:str):
    """
    純資産配当率
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_RatioOfTotalAmountOfDividendsToNetAssets',
            IxNonFraction.head_item_key == head_item_key,
            IxNonFraction.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def revenue(session: Session, head_item_key:str, context:str):
    """
    売上収益
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_Revenue',
            IxNonFraction.head_item_key == head_item_key,
            IxNonFraction.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def total_assets(session: Session, head_item_key:str, context:str):
    """
    総資産
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_TotalAssets',
            IxNonFraction.head_item_key == head_item_key,
            IxNonFraction.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def total_dividend_paid_annual(session: Session, head_item_key:str, context:str):
    """
    配当金総額（合計）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_TotalDividendPaidAnnual',
            IxNonFraction.head_item_key == head_item_key,
            IxNonFraction.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

