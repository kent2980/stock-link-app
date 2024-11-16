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

def basic_net_income_per_share_us(session: Session, head_item_key:str, context:str):
    """
    基本的1株当たり当社株主に帰属する当期純利益、米国基準
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_BasicNetIncomePerShareUS',
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

def change_in_comprehensive_income_net_of_tax_including_portion_attributable_to_noncontrolling_interest5_us(session: Session, head_item_key:str, context:str):
    """
    当社株主に帰属する包括利益増減率、米国基準
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_ChangeInComprehensiveIncomeNetOfTaxIncludingPortionAttributableToNoncontrollingInterest5US',
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

def change_in_comprehensive_income_net_of_tax_including_portion_attributable_to_noncontrolling_interest_us(session: Session, head_item_key:str, context:str):
    """
    当期包括利益増減率、米国基準
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_ChangeInComprehensiveIncomeNetOfTaxIncludingPortionAttributableToNoncontrollingInterestUS',
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

def change_in_income_before_income_taxes_us(session: Session, head_item_key:str, context:str):
    """
    増減率、税引前当期純利益、米国基準
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_ChangeInIncomeBeforeIncomeTaxesUS',
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

def change_in_net_income_us(session: Session, head_item_key:str, context:str):
    """
    増減率、当社株主に帰属する当期純利益、米国基準
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_ChangeInNetIncomeUS',
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

def change_in_net_sales_us(session: Session, head_item_key:str, context:str):
    """
    増減率、売上高、米国基準
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_ChangeInNetSalesUS',
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

def change_in_operating_income_us(session: Session, head_item_key:str, context:str):
    """
    増減率、営業利益、米国基準
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_ChangeInOperatingIncomeUS',
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

def change_in_operating_revenues_us(session: Session, head_item_key:str, context:str):
    """
    増減率、営業収益、米国基準
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_ChangeInOperatingRevenuesUS',
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

def comprehensive_income_net_of_tax_including_portion_attributable_to_noncontrolling_interest5_us(session: Session, head_item_key:str, context:str):
    """
    当社株主に帰属する包括利益、米国基準
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_ComprehensiveIncomeNetOfTaxIncludingPortionAttributableToNoncontrollingInterest5US',
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

def comprehensive_income_net_of_tax_including_portion_attributable_to_noncontrolling_interest_us(session: Session, head_item_key:str, context:str):
    """
    当期包括利益、米国基準
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_ComprehensiveIncomeNetOfTaxIncludingPortionAttributableToNoncontrollingInterestUS',
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

def diluted_net_income_per_share2_us(session: Session, head_item_key:str, context:str):
    """
    潜在株式調整後1株当たり当社株主に帰属する当期純利益、米国基準
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_DilutedNetIncomePerShare2US',
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

def diluted_net_income_per_share_us(session: Session, head_item_key:str, context:str):
    """
    希薄化後1株当たり当社株主に帰属する当期純利益、米国基準
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_DilutedNetIncomePerShareUS',
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

def income_before_income_taxes_us(session: Session, head_item_key:str, context:str):
    """
    税引前当期純利益、米国基準
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_IncomeBeforeIncomeTaxesUS',
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

def net_assets_us(session: Session, head_item_key:str, context:str):
    """
    資本合計（純資産）、米国基準
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_NetAssetsUS',
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

def net_income_per_share_us(session: Session, head_item_key:str, context:str):
    """
    1株当たり当社株主に帰属する当期純利益、米国基準
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_NetIncomePerShareUS',
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

def net_income_us(session: Session, head_item_key:str, context:str):
    """
    当社株主に帰属する当期純利益、米国基準
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_NetIncomeUS',
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

def net_sales_us(session: Session, head_item_key:str, context:str):
    """
    売上高、米国基準
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_NetSalesUS',
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

def number_of_subsidiaries_excluded_from_consolidation_us(session: Session, head_item_key:str, context:str):
    """
    除外、米国基準
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_NumberOfSubsidiariesExcludedFromConsolidationUS',
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

def number_of_subsidiaries_newly_consolidated_us(session: Session, head_item_key:str, context:str):
    """
    新規、米国基準
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_NumberOfSubsidiariesNewlyConsolidatedUS',
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

def operating_income_us(session: Session, head_item_key:str, context:str):
    """
    営業利益、米国基準
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_OperatingIncomeUS',
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

def operating_revenues_us(session: Session, head_item_key:str, context:str):
    """
    営業収益、米国基準
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_OperatingRevenuesUS',
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

def shareholders_equity_ratio_us(session: Session, head_item_key:str, context:str):
    """
    株主資本比率、米国基準
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_ShareholdersEquityRatioUS',
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

def shareholders_equity_us(session: Session, head_item_key:str, context:str):
    """
    株主資本、米国基準
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_ShareholdersEquityUS',
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

def total_assets_us(session: Session, head_item_key:str, context:str):
    """
    総資産、米国基準
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_TotalAssetsUS',
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

