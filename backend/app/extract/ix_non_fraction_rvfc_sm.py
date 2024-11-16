from app.models import IxNonFraction
from sqlmodel import Session, select, func

def amount_change_net_income(session: Session, head_item_key:str, context:str):
    """
    増減額、当期純利益
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_AmountChangeNetIncome',
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

def amount_change_net_sales(session: Session, head_item_key:str, context:str):
    """
    増減額、売上高
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_AmountChangeNetSales',
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

def amount_change_operating_income(session: Session, head_item_key:str, context:str):
    """
    増減額、営業利益
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_AmountChangeOperatingIncome',
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

def amount_change_operating_income_ifrs(session: Session, head_item_key:str, context:str):
    """
    増減額、営業利益、IFRS
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_AmountChangeOperatingIncomeIFRS',
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

def amount_change_operating_revenues(session: Session, head_item_key:str, context:str):
    """
    増減額、営業収益
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_AmountChangeOperatingRevenues',
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

def amount_change_ordinary_income(session: Session, head_item_key:str, context:str):
    """
    増減額、経常利益
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_AmountChangeOrdinaryIncome',
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

def amount_change_ordinary_revenues_bk(session: Session, head_item_key:str, context:str):
    """
    増減額、経常収益、銀行
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_AmountChangeOrdinaryRevenuesBK',
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

def amount_change_profit_attributable_to_owners_of_parent(session: Session, head_item_key:str, context:str):
    """
    増減額、親会社株主に帰属する当期純利益
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_AmountChangeProfitAttributableToOwnersOfParent',
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

def amount_change_profit_attributable_to_owners_of_parent_ifrs(session: Session, head_item_key:str, context:str):
    """
    増減額、親会社の所有者に帰属する当期利益、IFRS
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_AmountChangeProfitAttributableToOwnersOfParentIFRS',
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

def amount_change_profit_before_tax_ifrs(session: Session, head_item_key:str, context:str):
    """
    増減額、税引前利益、IFRS
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_AmountChangeProfitBeforeTaxIFRS',
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

def amount_change_profit_ifrs(session: Session, head_item_key:str, context:str):
    """
    増減額、当期利益、IFRS
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_AmountChangeProfitIFRS',
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

def amount_change_revenue(session: Session, head_item_key:str, context:str):
    """
    増減額、売上収益
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_AmountChangeRevenue',
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

def amount_change_sales_ifrs(session: Session, head_item_key:str, context:str):
    """
    増減額、売上収益、IFRS
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_AmountChangeSalesIFRS',
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

def basic_earnings_per_share_ifrs(session: Session, head_item_key:str, context:str):
    """
    基本的1株当たり当期利益、IFRS
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_BasicEarningsPerShareIFRS',
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

def change_in_operating_income_ifrs(session: Session, head_item_key:str, context:str):
    """
    増減率、営業利益、IFRS
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_ChangeInOperatingIncomeIFRS',
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

def change_in_profit_attributable_to_owners_of_parent_ifrs(session: Session, head_item_key:str, context:str):
    """
    増減率、親会社の所有者に帰属する当期利益、IFRS
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_ChangeInProfitAttributableToOwnersOfParentIFRS',
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

def change_in_profit_before_tax_ifrs(session: Session, head_item_key:str, context:str):
    """
    増減率、税引前利益、IFRS
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_ChangeInProfitBeforeTaxIFRS',
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

def change_in_profit_ifrs(session: Session, head_item_key:str, context:str):
    """
    増減率、当期利益、IFRS
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_ChangeInProfitIFRS',
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

def change_in_sales_ifrs(session: Session, head_item_key:str, context:str):
    """
    増減率、売上収益、IFRS
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_ChangeInSalesIFRS',
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

def operating_income(session: Session, head_item_key:str, context:str):
    """
    営業利益又は営業損失（△）
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

def operating_income_ifrs(session: Session, head_item_key:str, context:str):
    """
    営業利益、IFRS
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_OperatingIncomeIFRS',
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
    経常利益又は経常損失（△）
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

def profit_attributable_to_owners_of_parent_ifrs(session: Session, head_item_key:str, context:str):
    """
    親会社の所有者に帰属する当期利益、IFRS
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_ProfitAttributableToOwnersOfParentIFRS',
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

def profit_before_tax_ifrs(session: Session, head_item_key:str, context:str):
    """
    税引前利益、IFRS
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_ProfitBeforeTaxIFRS',
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

def profit_ifrs(session: Session, head_item_key:str, context:str):
    """
    当期利益、IFRS
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_ProfitIFRS',
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

def sales_ifrs(session: Session, head_item_key:str, context:str):
    """
    売上収益、IFRS
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-ed-t_SalesIFRS',
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

