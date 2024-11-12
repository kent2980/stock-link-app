from app.models import IxNonFraction
from sqlmodel import Session, select, func

def average_number_of_shares(*, session: Session, head_item_key:str, context:str):
    """
    期中平均株式数
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_AverageNumberOfShares',
            IxNonFraction.head_item_key == head_item_key,
            func.regexp_match(IxNonFraction.context, context),
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def basic_earnings_per_share_ifrs(*, session: Session, head_item_key:str, context:str):
    """
    基本的1株当たり当期利益、IFRS
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_BasicEarningsPerShareIFRS',
            IxNonFraction.head_item_key == head_item_key,
            func.regexp_match(IxNonFraction.context, context),
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def cash_and_cash_equivalents_at_end_of_period_ifrs(*, session: Session, head_item_key:str, context:str):
    """
    現金及び現金同等物期末残高、IFRS
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_CashAndCashEquivalentsAtEndOfPeriodIFRS',
            IxNonFraction.head_item_key == head_item_key,
            func.regexp_match(IxNonFraction.context, context),
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def cash_flows_from_financing_activities_ifrs(*, session: Session, head_item_key:str, context:str):
    """
    財務活動によるキャッシュ・フロー、IFRS
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_CashFlowsFromFinancingActivitiesIFRS',
            IxNonFraction.head_item_key == head_item_key,
            func.regexp_match(IxNonFraction.context, context),
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def cash_flows_from_investing_activities_ifrs(*, session: Session, head_item_key:str, context:str):
    """
    投資活動によるキャッシュ・フロー、IFRS
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_CashFlowsFromInvestingActivitiesIFRS',
            IxNonFraction.head_item_key == head_item_key,
            func.regexp_match(IxNonFraction.context, context),
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def cash_flows_from_operating_activities_ifrs(*, session: Session, head_item_key:str, context:str):
    """
    営業活動によるキャッシュ・フロー、IFRS
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_CashFlowsFromOperatingActivitiesIFRS',
            IxNonFraction.head_item_key == head_item_key,
            func.regexp_match(IxNonFraction.context, context),
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def change_in_net_sales_ifrs(*, session: Session, head_item_key:str, context:str):
    """
    増減率、売上高、IFRS
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_ChangeInNetSalesIFRS',
            IxNonFraction.head_item_key == head_item_key,
            func.regexp_match(IxNonFraction.context, context),
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def change_in_operating_income_ifrs(*, session: Session, head_item_key:str, context:str):
    """
    増減率、営業利益、IFRS
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_ChangeInOperatingIncomeIFRS',
            IxNonFraction.head_item_key == head_item_key,
            func.regexp_match(IxNonFraction.context, context),
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def change_in_profit_attributable_to_owners_of_parent_ifrs(*, session: Session, head_item_key:str, context:str):
    """
    増減率、親会社の所有者に帰属する当期利益、IFRS
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_ChangeInProfitAttributableToOwnersOfParentIFRS',
            IxNonFraction.head_item_key == head_item_key,
            func.regexp_match(IxNonFraction.context, context),
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def change_in_profit_before_tax_ifrs(*, session: Session, head_item_key:str, context:str):
    """
    増減率、税引前利益、IFRS
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_ChangeInProfitBeforeTaxIFRS',
            IxNonFraction.head_item_key == head_item_key,
            func.regexp_match(IxNonFraction.context, context),
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def change_in_profit_ifrs(*, session: Session, head_item_key:str, context:str):
    """
    増減率、当期利益、IFRS
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_ChangeInProfitIFRS',
            IxNonFraction.head_item_key == head_item_key,
            func.regexp_match(IxNonFraction.context, context),
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def change_in_revenue_ifrs(*, session: Session, head_item_key:str, context:str):
    """
    増減率、収益、IFRS
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_ChangeInRevenueIFRS',
            IxNonFraction.head_item_key == head_item_key,
            func.regexp_match(IxNonFraction.context, context),
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def change_in_sales_ifrs(*, session: Session, head_item_key:str, context:str):
    """
    増減率、売上収益、IFRS
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_ChangeInSalesIFRS',
            IxNonFraction.head_item_key == head_item_key,
            func.regexp_match(IxNonFraction.context, context),
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def changes_in_total_comprehensive_income_ifrs(*, session: Session, head_item_key:str, context:str):
    """
    当期包括利益合計額増減率、IFRS
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_ChangesInTotalComprehensiveIncomeIFRS',
            IxNonFraction.head_item_key == head_item_key,
            func.regexp_match(IxNonFraction.context, context),
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def diluted_earnings_per_share_ifrs(*, session: Session, head_item_key:str, context:str):
    """
    希薄化後1株当たり当期利益、IFRS
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_DilutedEarningsPerShareIFRS',
            IxNonFraction.head_item_key == head_item_key,
            func.regexp_match(IxNonFraction.context, context),
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def dividend_per_share(*, session: Session, head_item_key:str, context:str):
    """
    1株当たり配当金
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_DividendPerShare',
            IxNonFraction.head_item_key == head_item_key,
            func.regexp_match(IxNonFraction.context, context),
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def equity_attributable_to_owners_of_parent_ifrs(*, session: Session, head_item_key:str, context:str):
    """
    親会社の所有者に帰属する持分（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_EquityAttributableToOwnersOfParentIFRS',
            IxNonFraction.head_item_key == head_item_key,
            func.regexp_match(IxNonFraction.context, context),
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def equity_attributable_to_owners_of_parent_per_share_ifrs(*, session: Session, head_item_key:str, context:str):
    """
    1株当たり親会社所有者帰属持分、IFRS
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_EquityAttributableToOwnersOfParentPerShareIFRS',
            IxNonFraction.head_item_key == head_item_key,
            func.regexp_match(IxNonFraction.context, context),
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def equity_attributable_to_owners_of_parent_to_total_assets_ratio_ifrs(*, session: Session, head_item_key:str, context:str):
    """
    親会社所有者帰属持分比率、IFRS
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_EquityAttributableToOwnersOfParentToTotalAssetsRatioIFRS',
            IxNonFraction.head_item_key == head_item_key,
            func.regexp_match(IxNonFraction.context, context),
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def investments_accounted_for_using_equity_method_ifrs(*, session: Session, head_item_key:str, context:str):
    """
    持分法で会計処理されている投資（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_InvestmentsAccountedForUsingEquityMethodIFRS',
            IxNonFraction.head_item_key == head_item_key,
            func.regexp_match(IxNonFraction.context, context),
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def net_sales_ifrs(*, session: Session, head_item_key:str, context:str):
    """
    売上高、IFRS
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_NetSalesIFRS',
            IxNonFraction.head_item_key == head_item_key,
            func.regexp_match(IxNonFraction.context, context),
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def number_of_issued_and_outstanding_shares_at_the_end_of_fiscal_year_including_treasury_stock(*, session: Session, head_item_key:str, context:str):
    """
    期末発行済株式数（自己株式を含む）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_NumberOfIssuedAndOutstandingSharesAtTheEndOfFiscalYearIncludingTreasuryStock',
            IxNonFraction.head_item_key == head_item_key,
            func.regexp_match(IxNonFraction.context, context),
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def number_of_subsidiaries_excluded_from_consolidation_ifrs(*, session: Session, head_item_key:str, context:str):
    """
    除外、IFRS
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_NumberOfSubsidiariesExcludedFromConsolidationIFRS',
            IxNonFraction.head_item_key == head_item_key,
            func.regexp_match(IxNonFraction.context, context),
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def number_of_subsidiaries_newly_consolidated_ifrs(*, session: Session, head_item_key:str, context:str):
    """
    新規、IFRS
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_NumberOfSubsidiariesNewlyConsolidatedIFRS',
            IxNonFraction.head_item_key == head_item_key,
            func.regexp_match(IxNonFraction.context, context),
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def number_of_treasury_stock_at_the_end_of_fiscal_year(*, session: Session, head_item_key:str, context:str):
    """
    期末自己株式数
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_NumberOfTreasuryStockAtTheEndOfFiscalYear',
            IxNonFraction.head_item_key == head_item_key,
            func.regexp_match(IxNonFraction.context, context),
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def operating_income_ifrs(*, session: Session, head_item_key:str, context:str):
    """
    営業利益、IFRS
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_OperatingIncomeIFRS',
            IxNonFraction.head_item_key == head_item_key,
            func.regexp_match(IxNonFraction.context, context),
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def operating_income_to_sales_ratio_ifrs(*, session: Session, head_item_key:str, context:str):
    """
    売上収益営業利益率、IFRS
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_OperatingIncomeToSalesRatioIFRS',
            IxNonFraction.head_item_key == head_item_key,
            func.regexp_match(IxNonFraction.context, context),
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def payout_ratio_ifrs(*, session: Session, head_item_key:str, context:str):
    """
    配当性向、IFRS
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_PayoutRatioIFRS',
            IxNonFraction.head_item_key == head_item_key,
            func.regexp_match(IxNonFraction.context, context),
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def profit_attributable_to_owners_of_parent_ifrs(*, session: Session, head_item_key:str, context:str):
    """
    親会社の所有者に帰属する当期利益、IFRS
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_ProfitAttributableToOwnersOfParentIFRS',
            IxNonFraction.head_item_key == head_item_key,
            func.regexp_match(IxNonFraction.context, context),
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def profit_before_tax_ifrs(*, session: Session, head_item_key:str, context:str):
    """
    税引前利益、IFRS
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_ProfitBeforeTaxIFRS',
            IxNonFraction.head_item_key == head_item_key,
            func.regexp_match(IxNonFraction.context, context),
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def profit_before_tax_to_total_assets_ratio_ifrs(*, session: Session, head_item_key:str, context:str):
    """
    資産合計税引前利益率、IFRS
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_ProfitBeforeTaxToTotalAssetsRatioIFRS',
            IxNonFraction.head_item_key == head_item_key,
            func.regexp_match(IxNonFraction.context, context),
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def profit_ifrs(*, session: Session, head_item_key:str, context:str):
    """
    当期利益、IFRS
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_ProfitIFRS',
            IxNonFraction.head_item_key == head_item_key,
            func.regexp_match(IxNonFraction.context, context),
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def profit_to_equity_attributable_to_owners_of_parent_ratio_ifrs(*, session: Session, head_item_key:str, context:str):
    """
    親会社所有者帰属持分当期利益率、IFRS
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_ProfitToEquityAttributableToOwnersOfParentRatioIFRS',
            IxNonFraction.head_item_key == head_item_key,
            func.regexp_match(IxNonFraction.context, context),
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def quarterly_period(*, session: Session, head_item_key:str, context:str):
    """
    四半期
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_QuarterlyPeriod',
            IxNonFraction.head_item_key == head_item_key,
            func.regexp_match(IxNonFraction.context, context),
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def ratio_of_total_amount_of_dividends_to_equity_attributable_to_owner_of_parent_consolidated_ifrs(*, session: Session, head_item_key:str, context:str):
    """
    親会社所有者帰属持分配当率（連結）、IFRS
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_RatioOfTotalAmountOfDividendsToEquityAttributableToOwnerOfParentConsolidatedIFRS',
            IxNonFraction.head_item_key == head_item_key,
            func.regexp_match(IxNonFraction.context, context),
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def revenue_ifrs(*, session: Session, head_item_key:str, context:str):
    """
    収益、IFRS
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_RevenueIFRS',
            IxNonFraction.head_item_key == head_item_key,
            func.regexp_match(IxNonFraction.context, context),
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def sales_ifrs(*, session: Session, head_item_key:str, context:str):
    """
    売上収益、IFRS
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_SalesIFRS',
            IxNonFraction.head_item_key == head_item_key,
            func.regexp_match(IxNonFraction.context, context),
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def total_assets_ifrs(*, session: Session, head_item_key:str, context:str):
    """
    資産合計、IFRS
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_TotalAssetsIFRS',
            IxNonFraction.head_item_key == head_item_key,
            func.regexp_match(IxNonFraction.context, context),
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def total_comprehensive_income_ifrs(*, session: Session, head_item_key:str, context:str):
    """
    当期包括利益合計額、IFRS
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_TotalComprehensiveIncomeIFRS',
            IxNonFraction.head_item_key == head_item_key,
            func.regexp_match(IxNonFraction.context, context),
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def total_dividend_paid_annual(*, session: Session, head_item_key:str, context:str):
    """
    配当金総額（合計）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_TotalDividendPaidAnnual',
            IxNonFraction.head_item_key == head_item_key,
            func.regexp_match(IxNonFraction.context, context),
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

def total_equity_ifrs(*, session: Session, head_item_key:str, context:str):
    """
    資本合計、IFRS
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_TotalEquityIFRS',
            IxNonFraction.head_item_key == head_item_key,
            func.regexp_match(IxNonFraction.context, context),
        )
    )
    result = session.exec(statement)
    item = result.first()
    if item:
        return item
    return None

