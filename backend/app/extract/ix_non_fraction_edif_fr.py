from app.models import IxNonFraction
from sqlmodel import Session, select, func

def number_of_submission_dei(session: Session, head_item_key:str, context:str):
    """
    提出回数、DEI
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpdei_cor_NumberOfSubmissionDEI',
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

def accrued_expenses_clifrs(session: Session, head_item_key:str, context:str):
    """
    未払費用、流動負債（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_AccruedExpensesCLIFRS',
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

def accumulated_other_comprehensive_income_ifrs(session: Session, head_item_key:str, context:str):
    """
    その他の包括利益累計額（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_AccumulatedOtherComprehensiveIncomeIFRS',
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

def assets_held_for_sale_ifrs(session: Session, head_item_key:str, context:str):
    """
    売却目的で保有する資産（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_AssetsHeldForSaleIFRS',
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

def assets_ifrs(session: Session, head_item_key:str, context:str):
    """
    資産（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_AssetsIFRS',
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

def basic_earnings_loss_per_share_ifrs(session: Session, head_item_key:str, context:str):
    """
    基本的１株当たり当期利益（△損失）（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_BasicEarningsLossPerShareIFRS',
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

def bonds_and_borrowings_clifrs(session: Session, head_item_key:str, context:str):
    """
    社債及び借入金、流動負債（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_BondsAndBorrowingsCLIFRS',
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

def bonds_and_borrowings_liabilities_ifrs(session: Session, head_item_key:str, context:str):
    """
    社債及び借入金、負債（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_BondsAndBorrowingsLiabilitiesIFRS',
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

def bonds_and_borrowings_nclifrs(session: Session, head_item_key:str, context:str):
    """
    社債及び借入金、非流動負債（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_BondsAndBorrowingsNCLIFRS',
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

def borrowings_clifrs(session: Session, head_item_key:str, context:str):
    """
    借入金、流動負債（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_BorrowingsCLIFRS',
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

def borrowings_nclifrs(session: Session, head_item_key:str, context:str):
    """
    借入金、非流動負債（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_BorrowingsNCLIFRS',
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

def cancellation_of_treasury_shares_ssifrs(session: Session, head_item_key:str, context:str):
    """
    自己株式の消却、持分変動計算書（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_CancellationOfTreasurySharesSSIFRS',
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

def capital_contribution_from_non_controlling_interests_fin_cfifrs(session: Session, head_item_key:str, context:str):
    """
    非支配持分からの払込による収入、財務活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_CapitalContributionFromNonControllingInterestsFinCFIFRS',
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

def capital_surplus_ifrs(session: Session, head_item_key:str, context:str):
    """
    資本剰余金（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_CapitalSurplusIFRS',
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

def cash_and_cash_equivalents_ifrs(session: Session, head_item_key:str, context:str):
    """
    現金及び現金同等物（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_CashAndCashEquivalentsIFRS',
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

def cash_and_cash_equivalents_if_different_from_bs_balance_ifrs(session: Session, head_item_key:str, context:str):
    """
    現金及び現金同等物（財政状態計算書と異なる場合にCFで用いる）（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_CashAndCashEquivalentsIfDifferentFromBSBalanceIFRS',
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

def change_in_scope_of_consolidation_ssifrs(session: Session, head_item_key:str, context:str):
    """
    連結範囲の変動、持分変動計算書（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_ChangeInScopeOfConsolidationSSIFRS',
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

def changes_in_ownership_interest_in_subsidiaries_ssifrs(session: Session, head_item_key:str, context:str):
    """
    支配継続子会社に対する持分変動、持分変動計算書（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_ChangesInOwnershipInterestInSubsidiariesSSIFRS',
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

def collection_of_loans_receivable_inv_cfifrs(session: Session, head_item_key:str, context:str):
    """
    貸付金の回収による収入、投資活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_CollectionOfLoansReceivableInvCFIFRS',
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

def comprehensive_income_attributable_to_non_controlling_interests_ifrs(session: Session, head_item_key:str, context:str):
    """
    非支配持分、当期包括利益（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_ComprehensiveIncomeAttributableToNonControllingInterestsIFRS',
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

def comprehensive_income_attributable_to_owners_of_parent_ifrs(session: Session, head_item_key:str, context:str):
    """
    親会社の所有者、当期包括利益（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_ComprehensiveIncomeAttributableToOwnersOfParentIFRS',
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

def comprehensive_income_ifrs(session: Session, head_item_key:str, context:str):
    """
    当期包括利益（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_ComprehensiveIncomeIFRS',
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

def continuing_operations_basic_earnings_loss_per_share_ifrs(session: Session, head_item_key:str, context:str):
    """
    継続事業、基本的１株当たり当期利益（△損失）（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_ContinuingOperationsBasicEarningsLossPerShareIFRS',
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

def continuing_operations_diluted_earnings_loss_per_share_ifrs(session: Session, head_item_key:str, context:str):
    """
    継続事業、希薄化後１株当たり当期利益（△損失）（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_ContinuingOperationsDilutedEarningsLossPerShareIFRS',
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

def contract_assets_caifrs(session: Session, head_item_key:str, context:str):
    """
    契約資産、流動資産（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_ContractAssetsCAIFRS',
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

def contract_assets_ncaifrs(session: Session, head_item_key:str, context:str):
    """
    契約資産、非流動資産（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_ContractAssetsNCAIFRS',
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

def contract_liabilities_clifrs(session: Session, head_item_key:str, context:str):
    """
    契約負債、流動負債（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_ContractLiabilitiesCLIFRS',
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

def contract_liabilities_nclifrs(session: Session, head_item_key:str, context:str):
    """
    契約負債、非流動負債（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_ContractLiabilitiesNCLIFRS',
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

def cost_of_sales_ifrs(session: Session, head_item_key:str, context:str):
    """
    売上原価（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_CostOfSalesIFRS',
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

def cumulative_effect_of_accounting_change_ifrs(session: Session, head_item_key:str, context:str):
    """
    会計方針の変更による累積的影響額（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_CumulativeEffectOfAccountingChangeIFRS',
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

def current_assets_ifrs(session: Session, head_item_key:str, context:str):
    """
    流動資産（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_CurrentAssetsIFRS',
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

def current_assets_other_than_assets_held_for_sale_caifrs(session: Session, head_item_key:str, context:str):
    """
    売却目的で保有する資産を除く流動資産（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_CurrentAssetsOtherThanAssetsHeldForSaleCAIFRS',
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

def decrease_increase_in_contract_assets_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    契約資産の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_DecreaseIncreaseInContractAssetsOpeCFIFRS',
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

def decrease_increase_in_inventories_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    棚卸資産の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_DecreaseIncreaseInInventoriesOpeCFIFRS',
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

def decrease_increase_in_retirement_benefit_asset_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    退職給付に係る資産の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_DecreaseIncreaseInRetirementBenefitAssetOpeCFIFRS',
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

def decrease_increase_in_trade_and_other_receivables2_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    売上債権及びその他の債権の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_DecreaseIncreaseInTradeAndOtherReceivables2OpeCFIFRS',
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

def decrease_increase_in_trade_and_other_receivables_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    営業債権及びその他の債権の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_DecreaseIncreaseInTradeAndOtherReceivablesOpeCFIFRS',
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

def decrease_increase_in_trade_receivables2_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    売上債権の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_DecreaseIncreaseInTradeReceivables2OpeCFIFRS',
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

def decrease_increase_in_trade_receivables_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    営業債権の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_DecreaseIncreaseInTradeReceivablesOpeCFIFRS',
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

def deferred_income_clifrs(session: Session, head_item_key:str, context:str):
    """
    繰延収益、流動負債（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_DeferredIncomeCLIFRS',
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

def deferred_income_nclifrs(session: Session, head_item_key:str, context:str):
    """
    繰延収益、非流動負債（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_DeferredIncomeNCLIFRS',
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

def deferred_tax_assets_ifrs(session: Session, head_item_key:str, context:str):
    """
    繰延税金資産（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_DeferredTaxAssetsIFRS',
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

def deferred_tax_liabilities_ifrs(session: Session, head_item_key:str, context:str):
    """
    繰延税金負債（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_DeferredTaxLiabilitiesIFRS',
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

def depreciation_and_amortization_of_intangible_assets_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    減価償却費及び無形資産償却費、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_DepreciationAndAmortizationOfIntangibleAssetsOpeCFIFRS',
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

def depreciation_and_amortization_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    減価償却費及び償却費、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_DepreciationAndAmortizationOpeCFIFRS',
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

def depreciation_and_amortization_operating_expenses_ifrs(session: Session, head_item_key:str, context:str):
    """
    減価償却費及び償却費、営業費用（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_DepreciationAndAmortizationOperatingExpensesIFRS',
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

def derivative_assets_caifrs(session: Session, head_item_key:str, context:str):
    """
    デリバティブ資産、流動資産（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_DerivativeAssetsCAIFRS',
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

def derivative_assets_ncaifrs(session: Session, head_item_key:str, context:str):
    """
    デリバティブ資産、非流動資産（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_DerivativeAssetsNCAIFRS',
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

def derivative_liabilities_clifrs(session: Session, head_item_key:str, context:str):
    """
    デリバティブ負債、流動負債（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_DerivativeLiabilitiesCLIFRS',
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

def derivative_liabilities_nclifrs(session: Session, head_item_key:str, context:str):
    """
    デリバティブ負債、非流動負債（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_DerivativeLiabilitiesNCLIFRS',
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

def diluted_earnings_loss_per_share_ifrs(session: Session, head_item_key:str, context:str):
    """
    希薄化後１株当たり当期利益（△損失）（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_DilutedEarningsLossPerShareIFRS',
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

def discontinued_operations_basic_earnings_loss_per_share_ifrs(session: Session, head_item_key:str, context:str):
    """
    非継続事業、基本的１株当たり当期利益（△損失）（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_DiscontinuedOperationsBasicEarningsLossPerShareIFRS',
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

def discontinued_operations_diluted_earnings_loss_per_share_ifrs(session: Session, head_item_key:str, context:str):
    """
    非継続事業、希薄化後１株当たり当期利益（△損失）（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_DiscontinuedOperationsDilutedEarningsLossPerShareIFRS',
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

def disposal_of_subsidiaries_ssifrs(session: Session, head_item_key:str, context:str):
    """
    子会社の支配喪失に伴う変動、持分変動計算書（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_DisposalOfSubsidiariesSSIFRS',
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

def disposal_of_treasury_shares_ssifrs(session: Session, head_item_key:str, context:str):
    """
    自己株式の処分、持分変動計算書（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_DisposalOfTreasurySharesSSIFRS',
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

def dividend_income_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    受取配当金、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_DividendIncomeOpeCFIFRS',
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

def dividends_paid_fin_cfifrs(session: Session, head_item_key:str, context:str):
    """
    配当金の支払額、財務活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_DividendsPaidFinCFIFRS',
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

def dividends_paid_to_non_controlling_interests_fin_cfifrs(session: Session, head_item_key:str, context:str):
    """
    非支配持分への配当金の支払額、財務活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_DividendsPaidToNonControllingInterestsFinCFIFRS',
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

def dividends_paid_to_owners_of_parent_fin_cfifrs(session: Session, head_item_key:str, context:str):
    """
    親会社の所有者への配当金の支払額、財務活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_DividendsPaidToOwnersOfParentFinCFIFRS',
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

def dividends_received_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    配当金の受取額、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_DividendsReceivedOpeCFIFRS',
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

def dividends_ssifrs(session: Session, head_item_key:str, context:str):
    """
    配当金、持分変動計算書（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_DividendsSSIFRS',
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

def effect_of_exchange_rate_changes_on_cash_and_cash_equivalents_ifrs(session: Session, head_item_key:str, context:str):
    """
    現金及び現金同等物の為替変動による影響（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_EffectOfExchangeRateChangesOnCashAndCashEquivalentsIFRS',
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

def effective_portion_of_cash_flow_hedges_net_of_tax_items_that_may_be_reclassified_to_profit_or_loss_ociifrs(session: Session, head_item_key:str, context:str):
    """
    キャッシュ・フロー・ヘッジの有効部分（税引後）、純損益に振り替えられる可能性のあるその他の包括利益（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_EffectivePortionOfCashFlowHedgesNetOfTaxItemsThatMayBeReclassifiedToProfitOrLossOCIIFRS',
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

def employee_benefits_nclifrs(session: Session, head_item_key:str, context:str):
    """
    従業員給付、非流動負債（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_EmployeeBenefitsNCLIFRS',
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

def equity_attributable_to_owners_of_parent_ifrs(session: Session, head_item_key:str, context:str):
    """
    親会社の所有者に帰属する持分（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_EquityAttributableToOwnersOfParentIFRS',
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

def equity_ifrs(session: Session, head_item_key:str, context:str):
    """
    資本（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_EquityIFRS',
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

def exchange_differences_on_translation_of_foreign_operations_before_tax_items_that_may_be_reclassified_to_profit_or_loss_ociifrs(session: Session, head_item_key:str, context:str):
    """
    在外営業活動体の外貨換算差額（税引前）、純損益に振り替えられる可能性のあるその他の包括利益（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_ExchangeDifferencesOnTranslationOfForeignOperationsBeforeTaxItemsThatMayBeReclassifiedToProfitOrLossOCIIFRS',
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

def exchange_differences_on_translation_of_foreign_operations_net_of_tax_items_that_may_be_reclassified_to_profit_or_loss_ociifrs(session: Session, head_item_key:str, context:str):
    """
    在外営業活動体の外貨換算差額（税引後）、純損益に振り替えられる可能性のあるその他の包括利益（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_ExchangeDifferencesOnTranslationOfForeignOperationsNetOfTaxItemsThatMayBeReclassifiedToProfitOrLossOCIIFRS',
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

def exercise_of_share_acquisition_rights_ssifrs(session: Session, head_item_key:str, context:str):
    """
    新株予約権の行使、持分変動計算書（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_ExerciseOfShareAcquisitionRightsSSIFRS',
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

def finance_costs_ifrs(session: Session, head_item_key:str, context:str):
    """
    金融費用（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_FinanceCostsIFRS',
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

def finance_costs_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    金融費用、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_FinanceCostsOpeCFIFRS',
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

def finance_income_and_expenses_net_ifrs(session: Session, head_item_key:str, context:str):
    """
    金融収益・費用（純額）（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_FinanceIncomeAndExpensesNetIFRS',
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

def finance_income_and_finance_costs_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    金融収益及び金融費用、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_FinanceIncomeAndFinanceCostsOpeCFIFRS',
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

def finance_income_ifrs(session: Session, head_item_key:str, context:str):
    """
    金融収益（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_FinanceIncomeIFRS',
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

def finance_income_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    金融収益、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_FinanceIncomeOpeCFIFRS',
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

def financial_assets_measured_at_fair_value_through_other_comprehensive_income_net_of_tax_items_that_may_be_reclassified_to_profit_or_loss_ociifrs(session: Session, head_item_key:str, context:str):
    """
    その他の包括利益を通じて公正価値で測定する金融資産（税引後）、純損益に振り替えられる可能性のあるその他の包括利益（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_FinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncomeNetOfTaxItemsThatMayBeReclassifiedToProfitOrLossOCIIFRS',
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

def foreign_exchange_loss_gain_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    為替差損益（△は益）、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_ForeignExchangeLossGainOpeCFIFRS',
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

def forfeiture_of_share_acquisition_rights_ssifrs(session: Session, head_item_key:str, context:str):
    """
    新株予約権の失効、持分変動計算書（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_ForfeitureOfShareAcquisitionRightsSSIFRS',
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

def gain_on_bargain_purchase_ifrs(session: Session, head_item_key:str, context:str):
    """
    負ののれん発生益（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_GainOnBargainPurchaseIFRS',
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

def general_and_administrative_expenses_ifrs(session: Session, head_item_key:str, context:str):
    """
    一般管理費（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_GeneralAndAdministrativeExpensesIFRS',
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

def goodwill_and_intangible_assets_ifrs(session: Session, head_item_key:str, context:str):
    """
    のれん及び無形資産（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_GoodwillAndIntangibleAssetsIFRS',
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

def goodwill_ifrs(session: Session, head_item_key:str, context:str):
    """
    のれん（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_GoodwillIFRS',
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

def gross_profit_ifrs(session: Session, head_item_key:str, context:str):
    """
    売上総利益（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_GrossProfitIFRS',
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

def impairment_losses_plifrs(session: Session, head_item_key:str, context:str):
    """
    減損損失、損益（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_ImpairmentLossesPLIFRS',
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

def impairment_losses_reversal_of_impairment_losses_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    減損損失（又は戻入れ）、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_ImpairmentLossesReversalOfImpairmentLossesOpeCFIFRS',
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

def income_tax_expense_ifrs(session: Session, head_item_key:str, context:str):
    """
    法人所得税費用（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_IncomeTaxExpenseIFRS',
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

def income_tax_expense_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    法人所得税費用、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_IncomeTaxExpenseOpeCFIFRS',
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

def income_taxes_items_that_will_not_be_reclassified_to_profit_or_loss_ociifrs(session: Session, head_item_key:str, context:str):
    """
    法人所得税、純損益に振り替えられることのないその他の包括利益（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_IncomeTaxesItemsThatWillNotBeReclassifiedToProfitOrLossOCIIFRS',
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

def income_taxes_paid_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    法人所得税の支払額、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_IncomeTaxesPaidOpeCFIFRS',
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

def income_taxes_payable_clifrs(session: Session, head_item_key:str, context:str):
    """
    未払法人所得税、流動負債（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_IncomeTaxesPayableCLIFRS',
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

def income_taxes_payable_liabilities_ifrs(session: Session, head_item_key:str, context:str):
    """
    未払法人所得税、負債（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_IncomeTaxesPayableLiabilitiesIFRS',
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

def income_taxes_receivable_caifrs(session: Session, head_item_key:str, context:str):
    """
    未収法人所得税、流動資産（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_IncomeTaxesReceivableCAIFRS',
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

def income_taxes_refund_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    法人所得税の還付額、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_IncomeTaxesRefundOpeCFIFRS',
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

def income_taxes_refund_paid_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    法人所得税の支払額又は還付額（△は支払）、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_IncomeTaxesRefundPaidOpeCFIFRS',
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

def increase_decrease_by_business_combination_ssifrs(session: Session, head_item_key:str, context:str):
    """
    企業結合による変動、持分変動計算書（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_IncreaseDecreaseByBusinessCombinationSSIFRS',
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

def increase_decrease_in_contract_liabilities_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    契約負債の増減額（△は減少）、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_IncreaseDecreaseInContractLiabilitiesOpeCFIFRS',
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

def increase_decrease_in_provisions_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_IncreaseDecreaseInProvisionsOpeCFIFRS',
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

def increase_decrease_in_retirement_benefit_liability_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    退職給付に係る負債の増減額（△は減少）、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_IncreaseDecreaseInRetirementBenefitLiabilityOpeCFIFRS',
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

def increase_decrease_in_trade_and_other_payables2_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    仕入債務及びその他の債務の増減額（△は減少）、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_IncreaseDecreaseInTradeAndOtherPayables2OpeCFIFRS',
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

def increase_decrease_in_trade_and_other_payables_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    営業債務及びその他の債務の増減額（△は減少）、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_IncreaseDecreaseInTradeAndOtherPayablesOpeCFIFRS',
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

def increase_decrease_in_trade_payables3_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    買入債務の増減額（△は減少）、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_IncreaseDecreaseInTradePayables3OpeCFIFRS',
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

def increase_decrease_in_trade_payables_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    営業債務の増減額（△は減少）、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_IncreaseDecreaseInTradePayablesOpeCFIFRS',
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

def increase_or_decrease_in_retirement_benefit_asset_or_liability_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    退職給付に係る資産及び負債の増減額、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_IncreaseOrDecreaseInRetirementBenefitAssetOrLiabilityOpeCFIFRS',
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

def intangible_assets_ifrs(session: Session, head_item_key:str, context:str):
    """
    無形資産（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_IntangibleAssetsIFRS',
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

def interest_and_dividend_income_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    受取利息及び受取配当金、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_InterestAndDividendIncomeOpeCFIFRS',
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

def interest_and_dividends_received_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    利息及び配当金の受取額、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_InterestAndDividendsReceivedOpeCFIFRS',
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

def interest_bearing_liabilities_clifrs(session: Session, head_item_key:str, context:str):
    """
    有利子負債、流動負債（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_InterestBearingLiabilitiesCLIFRS',
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

def interest_bearing_liabilities_nclifrs(session: Session, head_item_key:str, context:str):
    """
    有利子負債、非流動負債（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_InterestBearingLiabilitiesNCLIFRS',
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

def interest_expenses_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    支払利息、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_InterestExpensesOpeCFIFRS',
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

def interest_income_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    受取利息、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_InterestIncomeOpeCFIFRS',
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

def interest_paid_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    利息の支払額、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_InterestPaidOpeCFIFRS',
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

def interest_received_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    利息の受取額、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_InterestReceivedOpeCFIFRS',
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

def intersegment_revenue_ifrs(session: Session, head_item_key:str, context:str):
    """
    セグメント間の売上収益（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_IntersegmentRevenueIFRS',
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

def intersegment_sales_ifrs(session: Session, head_item_key:str, context:str):
    """
    セグメント間の売上高（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_IntersegmentSalesIFRS',
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

def inventories_caifrs(session: Session, head_item_key:str, context:str):
    """
    棚卸資産、流動資産（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_InventoriesCAIFRS',
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

def investment_property_ifrs(session: Session, head_item_key:str, context:str):
    """
    投資不動産（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_InvestmentPropertyIFRS',
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

def investment_securities_ncaifrs(session: Session, head_item_key:str, context:str):
    """
    投資有価証券、非流動資産（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_InvestmentSecuritiesNCAIFRS',
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

def investments_accounted_for_using_equity_method_ifrs(session: Session, head_item_key:str, context:str):
    """
    持分法による投資損益、IFRS
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_InvestmentsAccountedForUsingEquityMethodIFRS',
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

def issuance_of_new_shares_ssifrs(session: Session, head_item_key:str, context:str):
    """
    新株の発行、持分変動計算書（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_IssuanceOfNewSharesSSIFRS',
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

def lease_liabilities_clifrs(session: Session, head_item_key:str, context:str):
    """
    リース負債、流動負債（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_LeaseLiabilitiesCLIFRS',
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

def lease_liabilities_nclifrs(session: Session, head_item_key:str, context:str):
    """
    リース負債、非流動負債（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_LeaseLiabilitiesNCLIFRS',
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

def liabilities_and_equity_ifrs(session: Session, head_item_key:str, context:str):
    """
    負債及び資本（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_LiabilitiesAndEquityIFRS',
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

def liabilities_directly_associated_with_assets_held_for_sale_ifrs(session: Session, head_item_key:str, context:str):
    """
    売却目的で保有する資産に直接関連する負債（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_LiabilitiesDirectlyAssociatedWithAssetsHeldForSaleIFRS',
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

def liabilities_ifrs(session: Session, head_item_key:str, context:str):
    """
    負債（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_LiabilitiesIFRS',
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

def liabilities_other_than_liabilities_directly_associated_with_assets_held_for_sale_ifrs(session: Session, head_item_key:str, context:str):
    """
    売却目的で保有する資産に直接関連する負債を除く負債（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_LiabilitiesOtherThanLiabilitiesDirectlyAssociatedWithAssetsHeldForSaleIFRS',
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

def long_term_debt_nclifrs(session: Session, head_item_key:str, context:str):
    """
    長期債務、非流動負債（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_LongTermDebtNCLIFRS',
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

def loss_gain_on_sale_and_retirement_of_fixed_assets_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    固定資産除売却損益（△は益）、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_LossGainOnSaleAndRetirementOfFixedAssetsOpeCFIFRS',
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

def loss_gain_on_sale_and_retirement_of_property_plant_and_equipment_and_intangible_assets_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    有形固定資産及び無形資産除売却損益（△は益）、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_LossGainOnSaleAndRetirementOfPropertyPlantAndEquipmentAndIntangibleAssetsOpeCFIFRS',
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

def loss_gain_on_sale_of_fixed_assets_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    固定資産売却損益（△は益）、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_LossGainOnSaleOfFixedAssetsOpeCFIFRS',
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

def loss_gain_on_step_acquisition_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    段階取得に係る差損益（△は益）、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_LossGainOnStepAcquisitionOpeCFIFRS',
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

def loss_gain_related_to_fixed_assets_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    固定資産に係る損益（△は益）、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_LossGainRelatedToFixedAssetsOpeCFIFRS',
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

def loss_on_retirement_of_fixed_assets_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    固定資産除却損、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_LossOnRetirementOfFixedAssetsOpeCFIFRS',
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

def net_cash_provided_by_used_in_financing_activities_ifrs(session: Session, head_item_key:str, context:str):
    """
    財務活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_NetCashProvidedByUsedInFinancingActivitiesIFRS',
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

def net_cash_provided_by_used_in_investing_activities_ifrs(session: Session, head_item_key:str, context:str):
    """
    投資活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_NetCashProvidedByUsedInInvestingActivitiesIFRS',
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

def net_cash_provided_by_used_in_operating_activities_ifrs(session: Session, head_item_key:str, context:str):
    """
    営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_NetCashProvidedByUsedInOperatingActivitiesIFRS',
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

def net_change_in_fair_value_of_equity_instruments_designated_as_measured_at_fair_value_through_other_comprehensive_income_before_tax_items_that_will_not_be_reclassified_to_profit_or_loss_ociifrs(session: Session, head_item_key:str, context:str):
    """
    その他の包括利益を通じて公正価値で測定するものとして指定した資本性金融商品の公正価値の純変動額（税引前）、純損益に振り替えられることのないその他の包括利益（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_NetChangeInFairValueOfEquityInstrumentsDesignatedAsMeasuredAtFairValueThroughOtherComprehensiveIncomeBeforeTaxItemsThatWillNotBeReclassifiedToProfitOrLossOCIIFRS',
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

def net_change_in_fair_value_of_equity_instruments_designated_as_measured_at_fair_value_through_other_comprehensive_income_net_of_tax_items_that_will_not_be_reclassified_to_profit_or_loss_ociifrs(session: Session, head_item_key:str, context:str):
    """
    その他の包括利益を通じて公正価値で測定するものとして指定した資本性金融商品の公正価値の純変動額（税引後）、純損益に振り替えられることのないその他の包括利益（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_NetChangeInFairValueOfEquityInstrumentsDesignatedAsMeasuredAtFairValueThroughOtherComprehensiveIncomeNetOfTaxItemsThatWillNotBeReclassifiedToProfitOrLossOCIIFRS',
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

def net_decrease_increase_in_time_deposits_inv_cfifrs(session: Session, head_item_key:str, context:str):
    """
    定期預金の純増減額（△は増加）、投資活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_NetDecreaseIncreaseInTimeDepositsInvCFIFRS',
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

def net_decrease_increase_in_treasury_shares_fin_cfifrs(session: Session, head_item_key:str, context:str):
    """
    自己株式の純増減額（△は増加）、財務活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_NetDecreaseIncreaseInTreasurySharesFinCFIFRS',
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

def net_increase_decrease_in_cash_and_cash_equivalents_before_effect_of_exchange_rate_changes_ifrs(session: Session, head_item_key:str, context:str):
    """
    現金及び現金同等物の増減額（△は減少）（換算差額加算前）（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_NetIncreaseDecreaseInCashAndCashEquivalentsBeforeEffectOfExchangeRateChangesIFRS',
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

def net_increase_decrease_in_cash_and_cash_equivalents_ifrs(session: Session, head_item_key:str, context:str):
    """
    現金及び現金同等物の増減額（△は減少）（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_NetIncreaseDecreaseInCashAndCashEquivalentsIFRS',
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

def net_increase_decrease_in_short_term_borrowings_fin_cfifrs(session: Session, head_item_key:str, context:str):
    """
    短期借入金の純増減額（△は減少）、財務活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_NetIncreaseDecreaseInShortTermBorrowingsFinCFIFRS',
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

def net_sales_ifrs(session: Session, head_item_key:str, context:str):
    """
    売上高、IFRS
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_NetSalesIFRS',
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

def non_controlling_interests_ifrs(session: Session, head_item_key:str, context:str):
    """
    非支配持分（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_NonControllingInterestsIFRS',
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

def non_current_assets_ifrs(session: Session, head_item_key:str, context:str):
    """
    非流動資産（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_NonCurrentAssetsIFRS',
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

def non_current_labilities_ifrs(session: Session, head_item_key:str, context:str):
    """
    非流動負債（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_NonCurrentLabilitiesIFRS',
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

def operating_expenses_ifrs(session: Session, head_item_key:str, context:str):
    """
    営業費用（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_OperatingExpensesIFRS',
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

def operating_profit_loss_ifrs(session: Session, head_item_key:str, context:str):
    """
    営業利益（△損失）（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_OperatingProfitLossIFRS',
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

def other_assets_assets_ifrs(session: Session, head_item_key:str, context:str):
    """
    その他の資産、資産（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_OtherAssetsAssetsIFRS',
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

def other_changes_in_working_capital_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    その他、運転資本の増減、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_OtherChangesInWorkingCapitalOpeCFIFRS',
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

def other_components_of_equity_ifrs(session: Session, head_item_key:str, context:str):
    """
    その他の資本の構成要素（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_OtherComponentsOfEquityIFRS',
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

def other_comprehensive_income_ifrs(session: Session, head_item_key:str, context:str):
    """
    その他の包括利益（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_OtherComprehensiveIncomeIFRS',
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

def other_current_assets_caifrs(session: Session, head_item_key:str, context:str):
    """
    その他の流動資産（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_OtherCurrentAssetsCAIFRS',
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

def other_current_liabilities_clifrs(session: Session, head_item_key:str, context:str):
    """
    その他の流動負債（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_OtherCurrentLiabilitiesCLIFRS',
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

def other_expenses_ifrs(session: Session, head_item_key:str, context:str):
    """
    その他の費用（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_OtherExpensesIFRS',
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

def other_fin_cfifrs(session: Session, head_item_key:str, context:str):
    """
    その他、財務活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_OtherFinCFIFRS',
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

def other_financial_assets_assets_ifrs(session: Session, head_item_key:str, context:str):
    """
    その他の金融資産、資産（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_OtherFinancialAssetsAssetsIFRS',
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

def other_financial_assets_caifrs(session: Session, head_item_key:str, context:str):
    """
    その他の金融資産、流動資産（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_OtherFinancialAssetsCAIFRS',
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

def other_financial_assets_ncaifrs(session: Session, head_item_key:str, context:str):
    """
    その他の金融資産、非流動資産（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_OtherFinancialAssetsNCAIFRS',
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

def other_financial_liabilities_clifrs(session: Session, head_item_key:str, context:str):
    """
    その他の金融負債、流動負債（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_OtherFinancialLiabilitiesCLIFRS',
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

def other_financial_liabilities_liabilities_ifrs(session: Session, head_item_key:str, context:str):
    """
    その他の金融負債、負債（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_OtherFinancialLiabilitiesLiabilitiesIFRS',
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

def other_financial_liabilities_nclifrs(session: Session, head_item_key:str, context:str):
    """
    その他の金融負債、非流動負債（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_OtherFinancialLiabilitiesNCLIFRS',
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

def other_income_and_expenses_net_ifrs(session: Session, head_item_key:str, context:str):
    """
    その他の収益・費用（純額）（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_OtherIncomeAndExpensesNetIFRS',
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

def other_income_ifrs(session: Session, head_item_key:str, context:str):
    """
    その他の収益（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_OtherIncomeIFRS',
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

def other_intangible_assets_ifrs(session: Session, head_item_key:str, context:str):
    """
    その他の無形資産（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_OtherIntangibleAssetsIFRS',
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

def other_inv_cfifrs(session: Session, head_item_key:str, context:str):
    """
    その他、投資活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_OtherInvCFIFRS',
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

def other_investments_ifrs(session: Session, head_item_key:str, context:str):
    """
    その他の投資（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_OtherInvestmentsIFRS',
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

def other_liabilities_liabilities_ifrs(session: Session, head_item_key:str, context:str):
    """
    その他の負債、負債（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_OtherLiabilitiesLiabilitiesIFRS',
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

def other_non_current_assets_ncaifrs(session: Session, head_item_key:str, context:str):
    """
    その他の非流動資産（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_OtherNonCurrentAssetsNCAIFRS',
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

def other_non_current_liabilities_nclifrs(session: Session, head_item_key:str, context:str):
    """
    その他の非流動負債（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_OtherNonCurrentLiabilitiesNCLIFRS',
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

def other_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    その他、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_OtherOpeCFIFRS',
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

def other_operating_expenses_ifrs(session: Session, head_item_key:str, context:str):
    """
    その他の営業費用（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_OtherOperatingExpensesIFRS',
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

def other_operating_income_ifrs(session: Session, head_item_key:str, context:str):
    """
    その他の営業収益（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_OtherOperatingIncomeIFRS',
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

def other_ssifrs(session: Session, head_item_key:str, context:str):
    """
    その他、持分変動計算書（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_OtherSSIFRS',
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

def payments_for_acquisition_of_businesses_inv_cfifrs(session: Session, head_item_key:str, context:str):
    """
    事業譲受による支出、投資活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_PaymentsForAcquisitionOfBusinessesInvCFIFRS',
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

def payments_for_acquisition_of_interests_in_subsidiaries_from_non_controlling_interests_fin_cfifrs(session: Session, head_item_key:str, context:str):
    """
    非支配持分からの子会社持分取得による支出、財務活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_PaymentsForAcquisitionOfInterestsInSubsidiariesFromNonControllingInterestsFinCFIFRS',
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

def payments_for_acquisition_of_subsidiaries_inv_cfifrs(session: Session, head_item_key:str, context:str):
    """
    子会社の取得による支出、投資活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_PaymentsForAcquisitionOfSubsidiariesInvCFIFRS',
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

def payments_for_leasehold_deposits_and_guarantee_deposits_inv_cfifrs(session: Session, head_item_key:str, context:str):
    """
    敷金及び保証金の差入による支出、投資活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_PaymentsForLeaseholdDepositsAndGuaranteeDepositsInvCFIFRS',
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

def payments_for_loans_receivable_inv_cfifrs(session: Session, head_item_key:str, context:str):
    """
    貸付けによる支出、投資活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_PaymentsForLoansReceivableInvCFIFRS',
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

def payments_for_purchase_of_treasury_shares_fin_cfifrs(session: Session, head_item_key:str, context:str):
    """
    自己株式の取得による支出、財務活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_PaymentsForPurchaseOfTreasurySharesFinCFIFRS',
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

def payments_into_time_deposits_inv_cfifrs(session: Session, head_item_key:str, context:str):
    """
    定期預金の預入による支出、投資活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_PaymentsIntoTimeDepositsInvCFIFRS',
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

def proceeds_from_changes_in_ownership_interests_in_subsidiaries_that_do_not_result_in_loss_of_control_fin_cfifrs(session: Session, head_item_key:str, context:str):
    """
    非支配持分への子会社持分売却による収入、財務活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_ProceedsFromChangesInOwnershipInterestsInSubsidiariesThatDoNotResultInLossOfControlFinCFIFRS',
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

def proceeds_from_collection_of_leasehold_deposits_and_guarantee_deposits_inv_cfifrs(session: Session, head_item_key:str, context:str):
    """
    敷金及び保証金の回収による収入、投資活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_ProceedsFromCollectionOfLeaseholdDepositsAndGuaranteeDepositsInvCFIFRS',
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

def proceeds_from_exercise_of_share_acquisition_rights_fin_cfifrs(session: Session, head_item_key:str, context:str):
    """
    新株予約権の行使による収入、財務活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_ProceedsFromExerciseOfShareAcquisitionRightsFinCFIFRS',
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

def proceeds_from_issuance_of_bonds_and_long_term_borrowings_fin_cfifrs(session: Session, head_item_key:str, context:str):
    """
    社債の発行及び長期借入れによる収入、財務活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_ProceedsFromIssuanceOfBondsAndLongTermBorrowingsFinCFIFRS',
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

def proceeds_from_issuance_of_bonds_fin_cfifrs(session: Session, head_item_key:str, context:str):
    """
    社債の発行による収入、財務活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_ProceedsFromIssuanceOfBondsFinCFIFRS',
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

def proceeds_from_issuance_of_shares_fin_cfifrs(session: Session, head_item_key:str, context:str):
    """
    株式の発行による収入、財務活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_ProceedsFromIssuanceOfSharesFinCFIFRS',
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

def proceeds_from_long_term_borrowings_fin_cfifrs(session: Session, head_item_key:str, context:str):
    """
    長期借入れによる収入、財務活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_ProceedsFromLongTermBorrowingsFinCFIFRS',
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

def proceeds_from_sale_of_businesses_inv_cfifrs(session: Session, head_item_key:str, context:str):
    """
    事業譲渡による収入、投資活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_ProceedsFromSaleOfBusinessesInvCFIFRS',
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

def proceeds_from_sale_of_equity_instruments_inv_cfifrs(session: Session, head_item_key:str, context:str):
    """
    資本性金融商品の売却による収入、投資活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_ProceedsFromSaleOfEquityInstrumentsInvCFIFRS',
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

def proceeds_from_sale_of_intangible_assets_inv_cfifrs(session: Session, head_item_key:str, context:str):
    """
    無形資産の売却による収入、投資活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_ProceedsFromSaleOfIntangibleAssetsInvCFIFRS',
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

def proceeds_from_sale_of_investment_securities_inv_cfifrs(session: Session, head_item_key:str, context:str):
    """
    投資有価証券の売却による収入、投資活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_ProceedsFromSaleOfInvestmentSecuritiesInvCFIFRS',
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

def proceeds_from_sale_of_investments_inv_cfifrs(session: Session, head_item_key:str, context:str):
    """
    投資の売却及び償還による収入、投資活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_ProceedsFromSaleOfInvestmentsInvCFIFRS',
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

def proceeds_from_sale_of_marketable_securities_inv_cfifrs(session: Session, head_item_key:str, context:str):
    """
    有価証券の売却による収入、投資活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_ProceedsFromSaleOfMarketableSecuritiesInvCFIFRS',
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

def proceeds_from_sale_of_other_financial_assets_inv_cfifrs(session: Session, head_item_key:str, context:str):
    """
    その他の金融資産の売却による収入、投資活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_ProceedsFromSaleOfOtherFinancialAssetsInvCFIFRS',
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

def proceeds_from_sale_of_property_plant_and_equipment_and_intangible_assets_inv_cfifrs(session: Session, head_item_key:str, context:str):
    """
    有形固定資産及び無形資産の売却による収入、投資活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_ProceedsFromSaleOfPropertyPlantAndEquipmentAndIntangibleAssetsInvCFIFRS',
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

def proceeds_from_sale_of_property_plant_and_equipment_inv_cfifrs(session: Session, head_item_key:str, context:str):
    """
    有形固定資産の売却による収入、投資活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_ProceedsFromSaleOfPropertyPlantAndEquipmentInvCFIFRS',
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

def proceeds_from_sale_of_subsidiaries_inv_cfifrs(session: Session, head_item_key:str, context:str):
    """
    子会社の売却による収入、投資活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_ProceedsFromSaleOfSubsidiariesInvCFIFRS',
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

def proceeds_from_sale_of_treasury_shares_fin_cfifrs(session: Session, head_item_key:str, context:str):
    """
    自己株式の売却による収入、財務活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_ProceedsFromSaleOfTreasurySharesFinCFIFRS',
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

def proceeds_from_short_term_borrowings_fin_cfifrs(session: Session, head_item_key:str, context:str):
    """
    短期借入れによる収入、財務活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_ProceedsFromShortTermBorrowingsFinCFIFRS',
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

def proceeds_from_withdrawal_of_time_deposits_inv_cfifrs(session: Session, head_item_key:str, context:str):
    """
    定期預金の払戻による収入、投資活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_ProceedsFromWithdrawalOfTimeDepositsInvCFIFRS',
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

def profit_loss_attributable_to_non_controlling_interests_ifrs(session: Session, head_item_key:str, context:str):
    """
    非支配持分、当期利益（△損失）（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_ProfitLossAttributableToNonControllingInterestsIFRS',
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

def profit_loss_attributable_to_owners_of_parent_ifrs(session: Session, head_item_key:str, context:str):
    """
    親会社の所有者、当期利益（△損失）（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_ProfitLossAttributableToOwnersOfParentIFRS',
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

def profit_loss_before_tax_from_discontinued_operations_ifrs(session: Session, head_item_key:str, context:str):
    """
    非継続事業からの税引前利益（△損失）（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_ProfitLossBeforeTaxFromDiscontinuedOperationsIFRS',
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

def profit_loss_before_tax_ifrs(session: Session, head_item_key:str, context:str):
    """
    継続事業からの税引前利益（△損失）（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_ProfitLossBeforeTaxIFRS',
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

def profit_loss_from_continuing_operations_ifrs(session: Session, head_item_key:str, context:str):
    """
    継続事業からの当期利益（△損失）（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_ProfitLossFromContinuingOperationsIFRS',
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

def profit_loss_from_discontinued_operations_ifrs(session: Session, head_item_key:str, context:str):
    """
    非継続事業からの当期利益（△損失）（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_ProfitLossFromDiscontinuedOperationsIFRS',
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

def profit_loss_ifrs(session: Session, head_item_key:str, context:str):
    """
    当期利益（△損失）（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_ProfitLossIFRS',
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

def property_plant_and_equipment_ifrs(session: Session, head_item_key:str, context:str):
    """
    有形固定資産（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_PropertyPlantAndEquipmentIFRS',
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

def provisions_clifrs(session: Session, head_item_key:str, context:str):
    """
    引当金、流動負債（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_ProvisionsCLIFRS',
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

def provisions_liabilities_ifrs(session: Session, head_item_key:str, context:str):
    """
    引当金、負債（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_ProvisionsLiabilitiesIFRS',
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

def provisions_nclifrs(session: Session, head_item_key:str, context:str):
    """
    引当金、非流動負債（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_ProvisionsNCLIFRS',
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

def purchase_and_disposal_of_treasury_shares_ssifrs(session: Session, head_item_key:str, context:str):
    """
    自己株式の取得及び処分、持分変動計算書（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_PurchaseAndDisposalOfTreasurySharesSSIFRS',
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

def purchase_of_equity_instruments_inv_cfifrs(session: Session, head_item_key:str, context:str):
    """
    資本性金融商品の取得による支出、投資活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_PurchaseOfEquityInstrumentsInvCFIFRS',
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

def purchase_of_intangible_assets_inv_cfifrs(session: Session, head_item_key:str, context:str):
    """
    無形資産の取得による支出、投資活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_PurchaseOfIntangibleAssetsInvCFIFRS',
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

def purchase_of_investment_property_inv_cfifrs(session: Session, head_item_key:str, context:str):
    """
    投資不動産の取得による支出、投資活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_PurchaseOfInvestmentPropertyInvCFIFRS',
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

def purchase_of_investment_securities_inv_cfifrs(session: Session, head_item_key:str, context:str):
    """
    投資有価証券の取得による支出、投資活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_PurchaseOfInvestmentSecuritiesInvCFIFRS',
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

def purchase_of_investments_accounted_for_using_equity_method_inv_cfifrs(session: Session, head_item_key:str, context:str):
    """
    持分法で会計処理されている投資の取得による支出、投資活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_PurchaseOfInvestmentsAccountedForUsingEquityMethodInvCFIFRS',
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

def purchase_of_investments_inv_cfifrs(session: Session, head_item_key:str, context:str):
    """
    投資の取得による支出、投資活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_PurchaseOfInvestmentsInvCFIFRS',
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

def purchase_of_marketable_securities_inv_cfifrs(session: Session, head_item_key:str, context:str):
    """
    有価証券の取得による支出、投資活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_PurchaseOfMarketableSecuritiesInvCFIFRS',
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

def purchase_of_other_financial_assets_inv_cfifrs(session: Session, head_item_key:str, context:str):
    """
    その他の金融資産の取得による支出、投資活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_PurchaseOfOtherFinancialAssetsInvCFIFRS',
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

def purchase_of_other_investments_inv_cfifrs(session: Session, head_item_key:str, context:str):
    """
    その他の投資の取得による支出、投資活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_PurchaseOfOtherInvestmentsInvCFIFRS',
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

def purchase_of_property_plant_and_equipment_and_intangible_assets_inv_cfifrs(session: Session, head_item_key:str, context:str):
    """
    有形固定資産及び無形資産の取得による支出、投資活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_PurchaseOfPropertyPlantAndEquipmentAndIntangibleAssetsInvCFIFRS',
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

def purchase_of_property_plant_and_equipment_inv_cfifrs(session: Session, head_item_key:str, context:str):
    """
    有形固定資産の取得による支出、投資活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_PurchaseOfPropertyPlantAndEquipmentInvCFIFRS',
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

def purchase_of_treasury_shares_ssifrs(session: Session, head_item_key:str, context:str):
    """
    自己株式の取得、持分変動計算書（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_PurchaseOfTreasurySharesSSIFRS',
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

def redemption_of_bonds_and_repayments_of_long_term_borrowings_fin_cfifrs(session: Session, head_item_key:str, context:str):
    """
    社債の償還及び長期借入金の返済、財務活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_RedemptionOfBondsAndRepaymentsOfLongTermBorrowingsFinCFIFRS',
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

def redemption_of_bonds_fin_cfifrs(session: Session, head_item_key:str, context:str):
    """
    社債の償還による支出、財務活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_RedemptionOfBondsFinCFIFRS',
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

def remeasurements_of_defined_benefit_plans_before_tax_items_that_will_not_be_reclassified_to_profit_or_loss_ociifrs(session: Session, head_item_key:str, context:str):
    """
    確定給付制度の再測定（税引前）、純損益に振り替えられることのないその他の包括利益（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_RemeasurementsOfDefinedBenefitPlansBeforeTaxItemsThatWillNotBeReclassifiedToProfitOrLossOCIIFRS',
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

def remeasurements_of_defined_benefit_plans_net_of_tax_items_that_will_not_be_reclassified_to_profit_or_loss_ociifrs(session: Session, head_item_key:str, context:str):
    """
    確定給付制度の再測定（税引後）、純損益に振り替えられることのないその他の包括利益（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_RemeasurementsOfDefinedBenefitPlansNetOfTaxItemsThatWillNotBeReclassifiedToProfitOrLossOCIIFRS',
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

def repayments_of_lease_obligations_fin_cfifrs(session: Session, head_item_key:str, context:str):
    """
    リース負債の返済による支出、財務活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_RepaymentsOfLeaseObligationsFinCFIFRS',
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

def repayments_of_long_term_borrowings_fin_cfifrs(session: Session, head_item_key:str, context:str):
    """
    長期借入金の返済による支出、財務活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_RepaymentsOfLongTermBorrowingsFinCFIFRS',
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

def repayments_of_short_term_borrowings_fin_cfifrs(session: Session, head_item_key:str, context:str):
    """
    短期借入金の返済による支出、財務活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_RepaymentsOfShortTermBorrowingsFinCFIFRS',
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

def research_and_development_expenditure_recognized_as_expense_during_period_ifrs(session: Session, head_item_key:str, context:str):
    """
    当期に費用認識した研究開発費（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_ResearchAndDevelopmentExpenditureRecognizedAsExpenseDuringPeriodIFRS',
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

def restated_balance_ifrs(session: Session, head_item_key:str, context:str):
    """
    会計方針の変更を反映した当期首残高（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_RestatedBalanceIFRS',
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

def retained_earnings_ifrs(session: Session, head_item_key:str, context:str):
    """
    利益剰余金（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_RetainedEarningsIFRS',
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

def retirement_benefit_asset_ncaifrs(session: Session, head_item_key:str, context:str):
    """
    退職給付に係る資産、非流動資産（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_RetirementBenefitAssetNCAIFRS',
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

def retirement_benefit_liability_nclifrs(session: Session, head_item_key:str, context:str):
    """
    退職給付に係る負債、非流動負債（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_RetirementBenefitLiabilityNCLIFRS',
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

def revenue2_ifrs(session: Session, head_item_key:str, context:str):
    """
    収益（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_Revenue2IFRS',
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

def revenue_from_external_customers_ifrs(session: Session, head_item_key:str, context:str):
    """
    外部顧客への売上収益（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_RevenueFromExternalCustomersIFRS',
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

def revenue_ifrs(session: Session, head_item_key:str, context:str):
    """
    売上収益（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_RevenueIFRS',
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

def right_of_use_assets_ifrs(session: Session, head_item_key:str, context:str):
    """
    使用権資産（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_RightOfUseAssetsIFRS',
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

def sales_to_external_customers_ifrs(session: Session, head_item_key:str, context:str):
    """
    外部顧客への売上高（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_SalesToExternalCustomersIFRS',
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

def segment_profit_loss_ifrs(session: Session, head_item_key:str, context:str):
    """
    セグメント利益（△損失）（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_SegmentProfitLossIFRS',
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

def selling_expenses_ifrs(session: Session, head_item_key:str, context:str):
    """
    販売費（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_SellingExpensesIFRS',
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

def selling_general_and_administrative_expenses_ifrs(session: Session, head_item_key:str, context:str):
    """
    販売費及び一般管理費（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_SellingGeneralAndAdministrativeExpensesIFRS',
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

def share_based_payment_expenses_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    株式報酬費用、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_ShareBasedPaymentExpensesOpeCFIFRS',
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

def share_based_payment_transactions_ssifrs(session: Session, head_item_key:str, context:str):
    """
    株式報酬取引、持分変動計算書（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_ShareBasedPaymentTransactionsSSIFRS',
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

def share_capital_ifrs(session: Session, head_item_key:str, context:str):
    """
    資本金（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_ShareCapitalIFRS',
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

def share_of_loss_profit_of_investments_accounted_for_using_equity_method_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    持分法による投資損益（△は益）、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_ShareOfLossProfitOfInvestmentsAccountedForUsingEquityMethodOpeCFIFRS',
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

def share_of_other_comprehensive_income_of_investments_accounted_for_using_equity_method_net_of_tax_items_that_may_be_reclassified_to_profit_or_loss_ociifrs(session: Session, head_item_key:str, context:str):
    """
    持分法によるその他の包括利益（税引後）、純損益に振り替えられる可能性のあるその他の包括利益（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_ShareOfOtherComprehensiveIncomeOfInvestmentsAccountedForUsingEquityMethodNetOfTaxItemsThatMayBeReclassifiedToProfitOrLossOCIIFRS',
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

def share_of_other_comprehensive_income_of_investments_accounted_for_using_equity_method_net_of_tax_items_that_will_not_be_reclassified_to_profit_or_loss_ociifrs(session: Session, head_item_key:str, context:str):
    """
    持分法によるその他の包括利益（税引後）、純損益に振り替えられることのないその他の包括利益（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_ShareOfOtherComprehensiveIncomeOfInvestmentsAccountedForUsingEquityMethodNetOfTaxItemsThatWillNotBeReclassifiedToProfitOrLossOCIIFRS',
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

def share_of_profit_loss_of_investments_accounted_for_using_equity_method_ifrs(session: Session, head_item_key:str, context:str):
    """
    持分法による投資損益（△は損失）（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_ShareOfProfitLossOfInvestmentsAccountedForUsingEquityMethodIFRS',
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

def subtotal_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    小計、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_SubtotalOpeCFIFRS',
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

def time_deposits_caifrs(session: Session, head_item_key:str, context:str):
    """
    定期預金、流動資産（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_TimeDepositsCAIFRS',
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

def total_changes_in_equity_ifrs(session: Session, head_item_key:str, context:str):
    """
    変動額合計（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_TotalChangesInEquityIFRS',
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

def total_current_liabilities_ifrs(session: Session, head_item_key:str, context:str):
    """
    流動負債（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_TotalCurrentLiabilitiesIFRS',
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

def total_of_items_that_may_be_reclassified_to_profit_or_loss_ociifrs(session: Session, head_item_key:str, context:str):
    """
    純損益に振り替えられる可能性のある項目合計（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_TotalOfItemsThatMayBeReclassifiedToProfitOrLossOCIIFRS',
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

def total_of_items_that_will_not_be_reclassified_to_profit_or_loss_ociifrs(session: Session, head_item_key:str, context:str):
    """
    純損益に振り替えられることのない項目合計（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_TotalOfItemsThatWillNotBeReclassifiedToProfitOrLossOCIIFRS',
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

def total_transactions_with_owners_ifrs(session: Session, head_item_key:str, context:str):
    """
    所有者との取引額（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_TotalTransactionsWithOwnersIFRS',
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

def trade_and_other_payables2_clifrs(session: Session, head_item_key:str, context:str):
    """
    仕入債務及びその他の債務、流動負債（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_TradeAndOtherPayables2CLIFRS',
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

def trade_and_other_payables2_nclifrs(session: Session, head_item_key:str, context:str):
    """
    仕入債務及びその他の債務、非流動負債（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_TradeAndOtherPayables2NCLIFRS',
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

def trade_and_other_payables_clifrs(session: Session, head_item_key:str, context:str):
    """
    営業債務及びその他の債務、流動負債（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_TradeAndOtherPayablesCLIFRS',
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

def trade_and_other_payables_liabilities_ifrs(session: Session, head_item_key:str, context:str):
    """
    営業債務及びその他の債務、負債（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_TradeAndOtherPayablesLiabilitiesIFRS',
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

def trade_and_other_payables_nclifrs(session: Session, head_item_key:str, context:str):
    """
    営業債務及びその他の債務、非流動負債（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_TradeAndOtherPayablesNCLIFRS',
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

def trade_and_other_receivables2_caifrs(session: Session, head_item_key:str, context:str):
    """
    売上債権及びその他の債権、流動資産（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_TradeAndOtherReceivables2CAIFRS',
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

def trade_and_other_receivables_assets_ifrs(session: Session, head_item_key:str, context:str):
    """
    営業債権及びその他の債権、資産（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_TradeAndOtherReceivablesAssetsIFRS',
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

def trade_and_other_receivables_caifrs(session: Session, head_item_key:str, context:str):
    """
    営業債権及びその他の債権、流動資産（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_TradeAndOtherReceivablesCAIFRS',
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

def trade_and_other_receivables_ncaifrs(session: Session, head_item_key:str, context:str):
    """
    営業債権及びその他の債権、非流動資産（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_TradeAndOtherReceivablesNCAIFRS',
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

def trade_payables3_clifrs(session: Session, head_item_key:str, context:str):
    """
    買入債務、流動負債（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_TradePayables3CLIFRS',
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

def trade_payables_clifrs(session: Session, head_item_key:str, context:str):
    """
    営業債務、流動負債（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_TradePayablesCLIFRS',
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

def trade_receivables2_caifrs(session: Session, head_item_key:str, context:str):
    """
    売上債権、流動資産（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_TradeReceivables2CAIFRS',
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

def trade_receivables_caifrs(session: Session, head_item_key:str, context:str):
    """
    営業債権、流動資産（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_TradeReceivablesCAIFRS',
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

def transfer_from_accumulated_other_comprehensive_income_to_retained_earnings_ssifrs(session: Session, head_item_key:str, context:str):
    """
    その他の包括利益累計額から利益剰余金への振替、持分変動計算書（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_TransferFromAccumulatedOtherComprehensiveIncomeToRetainedEarningsSSIFRS',
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

def transfer_from_other_components_of_equity_to_retained_earnings_ssifrs(session: Session, head_item_key:str, context:str):
    """
    その他の資本の構成要素から利益剰余金への振替、持分変動計算書（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_TransferFromOtherComponentsOfEquityToRetainedEarningsSSIFRS',
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

def transfer_ssifrs(session: Session, head_item_key:str, context:str):
    """
    振替、持分変動計算書（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_TransferSSIFRS',
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

def transfer_to_retained_earnings_ssifrs(session: Session, head_item_key:str, context:str):
    """
    利益剰余金への振替、持分変動計算書（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_TransferToRetainedEarningsSSIFRS',
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

def treasury_shares_ifrs(session: Session, head_item_key:str, context:str):
    """
    自己株式（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpigp_cor_TreasurySharesIFRS',
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

def amount_of_rent_offset_by_lease_and_guarantee_deposits_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    敷金及び保証金の家賃相殺額、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-acediffr-35630_AmountOfRentOffsetByLeaseAndGuaranteeDepositsOpeCFIFRS',
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

def increase_decrease_in_provision_for_bonuses_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    賞与引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-acediffr-35630_IncreaseDecreaseInProvisionForBonusesOpeCFIFRS',
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

def lease_and_guarantee_deposits_ncaifrs(session: Session, head_item_key:str, context:str):
    """
    敷金及び保証金、非流動資産（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-acediffr-35630_LeaseAndGuaranteeDepositsNCAIFRS',
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

def net_change_in_fair_value_of_instruments_measured_at_fair_value_through_other_comprehensive_income_items_that_will_not_be_reclassified_to_profit_or_loss_ociifrs(session: Session, head_item_key:str, context:str):
    """
    その他の包括利益を通じて測定する金融資産の公正価値の純変動、純損益に振り替えられることのないその他の包括利益（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-acediffr-35630_NetChangeInFairValueOfInstrumentsMeasuredAtFairValueThroughOtherComprehensiveIncomeItemsThatWillNotBeReclassifiedToProfitOrLossOCIIFRS',
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

def payments_for_commission_fees_fin_cfifrs(session: Session, head_item_key:str, context:str):
    """
    支払手数料の支払による支出、財務活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-acediffr-35630_PaymentsForCommissionFeesFinCFIFRS',
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

def accrued_labor_expenses_clifrs(session: Session, head_item_key:str, context:str):
    """
    未払人件費、流動負債（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-qcediffr-21540_AccruedLaborExpensesCLIFRS',
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

def changes_in_put_option_liabilities_related_to_non_controlling_interests_ssifrs(session: Session, head_item_key:str, context:str):
    """
    非支配株主に係る売建プット・オプション負債の変動等、持分変動計算書（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-qcediffr-21540_ChangesInPutOptionLiabilitiesRelatedToNonControllingInterestsSSIFRS',
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

def increase_decrease_in_accrued_consumption_taxes_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    未払消費税等の増減額（△は減少）、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-qcediffr-21540_IncreaseDecreaseInAccruedConsumptionTaxesOpeCFIFRS',
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

def increase_decrease_in_accrued_labor_expenses_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    未払人件費の増減額（△は減少）、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-qcediffr-21540_IncreaseDecreaseInAccruedLaborExpensesOpeCFIFRS',
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

def increase_decrease_in_lease_receivables_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    リース債権の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-qcediffr-21540_IncreaseDecreaseInLeaseReceivablesOpeCFIFRS',
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

def increase_decrease_in_prepaid_expenses_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    前払費用の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-qcediffr-21540_IncreaseDecreaseInPrepaidExpensesOpeCFIFRS',
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

def core_operating_profit_loss_ifrs(session: Session, head_item_key:str, context:str):
    """
    事業利益（△損失）（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-qcediffr-28110_CoreOperatingProfitLossIFRS',
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

def current_portion_of_bonds_clifrs(session: Session, head_item_key:str, context:str):
    """
    1年内償還社債、流動負債（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-qcediffr-28110_CurrentPortionOfBondsCLIFRS',
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

def hedging_cost_net_of_tax_items_that_may_be_reclassified_to_profit_or_loss_ociifrs(session: Session, head_item_key:str, context:str):
    """
    ヘッジコスト（税引後）、純損益に振替えられる可能性のあるその他の包括利益（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-qcediffr-28110_HedgingCostNetOfTaxItemsThatMayBeReclassifiedToProfitOrLossOCIIFRS',
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

def income_by_settlement_in_derivatives_fin_cfifrs(session: Session, head_item_key:str, context:str):
    """
    デリバティブの決済による収入、財務活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-qcediffr-28110_IncomeBySettlementInDerivativesFinCFIFRS',
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

def operating_income_loss_ifrs(session: Session, head_item_key:str, context:str):
    """
    事業利益（△は損失）（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-qcediffr-28110_OperatingIncomeLossIFRS',
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

def proceeds_from_sale_and_redemption_of_other_financial_assets_inv_cfifrs(session: Session, head_item_key:str, context:str):
    """
    その他の金融資産の売却及び償還による収入、投資活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-qcediffr-28110_ProceedsFromSaleAndRedemptionOfOtherFinancialAssetsInvCFIFRS',
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

def purchase_of_shares_of_subsidiaries_resulting_in_no_change_in_scope_of_consolidation_fin_cfifrs(session: Session, head_item_key:str, context:str):
    """
    連結範囲の変更を伴わない子会社株式の取得による支出、財務活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-qcediffr-28110_PurchaseOfSharesOfSubsidiariesResultingInNoChangeInScopeOfConsolidationFinCFIFRS',
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

def transfer_to_non_financial_assets_ssifrs(session: Session, head_item_key:str, context:str):
    """
    非金融資産等への振替、持分変動計算書（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-qcediffr-28110_TransferToNonFinancialAssetsSSIFRS',
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

def decrease_increase_in_advance_payments_to_suppliers_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    前渡金の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-qcediffr-42860_DecreaseIncreaseInAdvancePaymentsToSuppliersOpeCFIFRS',
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

def increase_decrease_in_bonus_payable_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    未払賞与の増減額(△は減少)、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-qcediffr-42860_IncreaseDecreaseInBonusPayableOpeCFIFRS',
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

def increase_decrease_in_consumption_tax_payable_etc_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    未払消費税等の増減額(△は減少)、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-qcediffr-42860_IncreaseDecreaseInConsumptionTaxPayableEtcOpeCFIFRS',
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

def purchase_of_treasury_shares_of_subsidiaries_fin_cfifrs(session: Session, head_item_key:str, context:str):
    """
    子会社の自己株式の取得による支出、財務活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-qcediffr-42860_PurchaseOfTreasurySharesOfSubsidiariesFinCFIFRS',
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

def tra_changes_in_ownership_interest_in_subsidiaries_ifrs(session: Session, head_item_key:str, context:str):
    """
    非支配株主との取引に係る親会社の持分変動（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-qcediffr-42860_TraChangesInOwnershipInterestInSubsidiariesIFRS',
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

def businessprofit_ifrs(session: Session, head_item_key:str, context:str):
    """
    事業利益（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-qcediffr-51100_BusinessprofitIFRS',
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

def cash_and_cash_equivalents_included_in_assets_of_disposal_groups_classified_as_for_sale_cfifrs(session: Session, head_item_key:str, context:str):
    """
    売却目的保有に分類される処分グループに係る資産に含まれる現金及び現金同等物、キャッシュ・フロー計算書（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-qcediffr-51100_CashAndCashEquivalentsIncludedInAssetsOfDisposalGroupsClassifiedAsForSaleCFIFRS',
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

def transfer_to_capital_surplus_ssifrs(session: Session, head_item_key:str, context:str):
    """
    資本剰余金への振替、持分変動計算書（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-qcediffr-51100_TransferToCapitalSurplusSSIFRS',
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

def collection_of_loans_receivable_from_associates_inv_cfifrs(session: Session, head_item_key:str, context:str):
    """
    関連会社に対する貸付金の回収、投資活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-qcediffr-63260_CollectionOfLoansReceivableFromAssociatesInvCFIFRS',
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

def decrease_increase_in_finance_receivables_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    金融債権の減少(△増加)、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-qcediffr-63260_DecreaseIncreaseInFinanceReceivablesOpeCFIFRS',
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

def decrease_increase_in_other_assets_ifrs_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    その他資産の減少(△増加)（IFRS）、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-qcediffr-63260_DecreaseIncreaseInOtherAssetsIFRSOpeCFIFRS',
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

def financial_receivables_caifrs(session: Session, head_item_key:str, context:str):
    """
    金融債権、流動資産（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-qcediffr-63260_FinancialReceivablesCAIFRS',
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

def financial_receivables_ncaifrs(session: Session, head_item_key:str, context:str):
    """
    金融債権、非流動資産（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-qcediffr-63260_FinancialReceivablesNCAIFRS',
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

def increase_decrease_in_other_liabilities_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    その他負債の増加(△減少)、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-qcediffr-63260_IncreaseDecreaseInOtherLiabilitiesOpeCFIFRS',
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

def insurance_contracts_liabilities_clifrs(session: Session, head_item_key:str, context:str):
    """
    保険契約負債、流動負債（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-qcediffr-63260_InsuranceContractsLiabilitiesCLIFRS',
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

def loss_gain_on_disposal_of_fixed_assets_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    固定資産処分損益、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-qcediffr-63260_LossGainOnDisposalOfFixedAssetsOpeCFIFRS',
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

def net_decrease_increase_in_deposits_from_group_financing_within_three_months_fin_cfifrs(session: Session, head_item_key:str, context:str):
    """
    グループファイナンス預り金(３ヶ月以内)の純増減(△減少)、財務活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-qcediffr-63260_NetDecreaseIncreaseInDepositsFromGroupFinancingWithinThreeMonthsFinCFIFRS',
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

def net_decrease_increase_in_restricted_cash_inv_cfifrs(session: Session, head_item_key:str, context:str):
    """
    引出制限条項付預金の純増減(△増加)、投資活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-qcediffr-63260_NetDecreaseIncreaseInRestrictedCashInvCFIFRS',
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

def payments_for_acquisition_of_short_term_investments_inv_cfifrs(session: Session, head_item_key:str, context:str):
    """
    短期投資の取得、投資活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-qcediffr-63260_PaymentsForAcquisitionOfShortTermInvestmentsInvCFIFRS',
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

def payments_for_loans_receivable_from_associates_inv_cfifrs(session: Session, head_item_key:str, context:str):
    """
    関連会社に対する貸付、投資活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-qcediffr-63260_PaymentsForLoansReceivableFromAssociatesInvCFIFRS',
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

def proceeds_from_deposits_from_group_financing_over_three_months_fin_cfifrs(session: Session, head_item_key:str, context:str):
    """
    グループファイナンス預り金(３ヶ月超)の受入、財務活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-qcediffr-63260_ProceedsFromDepositsFromGroupFinancingOverThreeMonthsFinCFIFRS',
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

def proceeds_from_sales_and_redemptions_of_short_term_investments_inv_cfifrs(session: Session, head_item_key:str, context:str):
    """
    短期投資の売却及び償還、投資活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-qcediffr-63260_ProceedsFromSalesAndRedemptionsOfShortTermInvestmentsInvCFIFRS',
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

def repayments_of_deposits_from_group_financing_over_three_months_fin_cfifrs(session: Session, head_item_key:str, context:str):
    """
    グループファイナンス預り金(３ヶ月超)の返還、財務活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-qcediffr-63260_RepaymentsOfDepositsFromGroupFinancingOverThreeMonthsFinCFIFRS',
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

def depreciation_and_amortization_ifrs(session: Session, head_item_key:str, context:str):
    """
    減価償却費及び償却費（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-qcediffr-77440_DepreciationAndAmortizationIFRS',
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

def increase_decrease_in_assets_and_liabilities_of_operating_activities_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    営業活動に係る資産・負債の増減合計、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-qcediffr-77440_IncreaseDecreaseInAssetsAndLiabilitiesOfOperatingActivitiesOpeCFIFRS',
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

def loss_gain_on_sale_of_shares_of_subsidiaries_ifrs(session: Session, head_item_key:str, context:str):
    """
    子会社株式売却損益（△は益）、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-qcediffr-77440_LossGainOnSaleOfSharesOfSubsidiariesIFRS',
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

def operating_ebitdaifrs(session: Session, head_item_key:str, context:str):
    """
    事業EBITDA（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-qcediffr-77440_OperatingEBITDAIFRS',
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

def payments_for_acquisition_of_share_acquisition_rights_in_subsidiaries_from_non_controlling_interests_fin_cfifrs(session: Session, head_item_key:str, context:str):
    """
    非支配持分からの子会社新株予約権の取得による支出、財務活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-qcediffr-77440_PaymentsForAcquisitionOfShareAcquisitionRightsInSubsidiariesFromNonControllingInterestsFinCFIFRS',
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

def proceeds_from_exercise_of_share_acquisition_rights_in_subsidiaries_fin_cfifrs(session: Session, head_item_key:str, context:str):
    """
    子会社新株予約権の行使による収入、財務活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-qcediffr-77440_ProceedsFromExerciseOfShareAcquisitionRightsInSubsidiariesFinCFIFRS',
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

def proceeds_from_government_grants_inv_cfifrs(session: Session, head_item_key:str, context:str):
    """
    政府補助金による収入、投資活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-qcediffr-77440_ProceedsFromGovernmentGrantsInvCFIFRS',
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

def subtotal2_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    小計-2、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-qcediffr-77440_Subtotal2OpeCFIFRS',
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

def total_adjustments_to_reconcile_profit_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    利益に対する調整項目合計、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-qcediffr-77440_TotalAdjustmentsToReconcileProfitOpeCFIFRS',
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

def transactions_with_non_controlling_interests_ssifrs(session: Session, head_item_key:str, context:str):
    """
    非支配持分との取引等、持分変動計算書（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-qcediffr-77440_TransactionsWithNonControllingInterestsSSIFRS',
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

def changes_in_ownership_interest_ifrs(session: Session, head_item_key:str, context:str):
    """
    所有者持分の変動（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-qcediffr-79150_ChangesInOwnershipInterestIFRS',
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

def decrease_increase_in_deposit_paid_for_repurchase_of_treasury_stock_fin_cfifrs(session: Session, head_item_key:str, context:str):
    """
    自己株式取得のための預託金の増減額（△は増加）、財務活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-qcediffr-79150_DecreaseIncreaseInDepositPaidForRepurchaseOfTreasuryStockFinCFIFRS',
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

def dividends_paid_to_non_controlling_shareholders_fin_cfifrs(session: Session, head_item_key:str, context:str):
    """
    非支配株主への配当金の支払額、財務活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-qcediffr-79150_DividendsPaidToNonControllingShareholdersFinCFIFRS',
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

def payments_for_retirement_of_property_plant_and_equipment_inv_cfifrs(session: Session, head_item_key:str, context:str):
    """
    有形固定資産の除却による支出、投資活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-qcediffr-79150_PaymentsForRetirementOfPropertyPlantAndEquipmentInvCFIFRS',
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

def purchase_of_shares_of_subsidiaries_and_affiliates_inv_cfifrs(session: Session, head_item_key:str, context:str):
    """
    関係会社株式の取得による支出、投資活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-qcediffr-79150_PurchaseOfSharesOfSubsidiariesAndAffiliatesInvCFIFRS',
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

def put_options_written_on_non_controlling_interests_ifrs(session: Session, head_item_key:str, context:str):
    """
    非支配持分に付与されたプット・オプション（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-qcediffr-79150_PutOptionsWrittenOnNonControllingInterestsIFRS',
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

def decrease_increase_in_other_non_current_assets_ifrsifrs(session: Session, head_item_key:str, context:str):
    """
    その他の非流動資産の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS）（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-qcediffr-81130_DecreaseIncreaseInOtherNonCurrentAssetsIFRSIFRS',
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

def equity_transactions_with_non_controlling_interests_ssifrs(session: Session, head_item_key:str, context:str):
    """
    非支配持分との資本取引、持分変動計算書（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-qcediffr-81130_EquityTransactionsWithNonControllingInterestsSSIFRS',
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

def increase_decrease_in_other_current_liabilities_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    その他の流動負債の増減額（△は減少）、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-qcediffr-81130_IncreaseDecreaseInOtherCurrentLiabilitiesOpeCFIFRS',
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

def payments_of_long_term_loans_receivable_inv_cfifrs(session: Session, head_item_key:str, context:str):
    """
    長期貸付けによる支出、投資活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-qcediffr-81130_PaymentsOfLongTermLoansReceivableInvCFIFRS',
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

def proceeds_from_sale_redemption_of_financial_assets_inv_cfifrs(session: Session, head_item_key:str, context:str):
    """
    金融資産の売却及び償還による収入、投資活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-qcediffr-81130_ProceedsFromSaleRedemptionOfFinancialAssetsInvCFIFRS',
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

def purchase_of_financial_assets_inv_cfifrs(session: Session, head_item_key:str, context:str):
    """
    金融資産の取得による支出、投資活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-qcediffr-81130_PurchaseOfFinancialAssetsInvCFIFRS',
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

def purchase_of_shares_of_subsidiaries_and_associates_inv_cfifrs(session: Session, head_item_key:str, context:str):
    """
    関係会社株式の取得による支出、投資活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-qcediffr-81130_PurchaseOfSharesOfSubsidiariesAndAssociatesInvCFIFRS',
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

def purchase_of_shares_of_subsidiaries_not_resulting_in_change_in_scope_of_consolidation_fin_cfifrsifrs(session: Session, head_item_key:str, context:str):
    """
    連結の範囲の変更を伴わない子会社株式の取得による支出、財務活動によるキャッシュ・フロー（IFRS）（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-qcediffr-81130_PurchaseOfSharesOfSubsidiariesNotResultingInChangeInScopeOfConsolidationFinCFIFRSIFRS',
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

def atm_operation_business_revenues_ifrs(session: Session, head_item_key:str, context:str):
    """
    ATM運営事業売上高（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-37740_ATMOperationBusinessRevenuesIFRS',
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

def cost_of_atm_operation_business_revenues_ifrs(session: Session, head_item_key:str, context:str):
    """
    ATM運営事業売上原価（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-37740_CostOfATMOperationBusinessRevenuesIFRS',
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

def cost_of_network_services_revenues_ifrs(session: Session, head_item_key:str, context:str):
    """
    ネットワークサービス売上原価（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-37740_CostOfNetworkServicesRevenuesIFRS',
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

def cost_of_si_revenues_ifrs(session: Session, head_item_key:str, context:str):
    """
    システムインテグレーション売上原価（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-37740_CostOfSIRevenuesIFRS',
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

def decrease_increase_in_other_assets_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    その他の資産の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-37740_DecreaseIncreaseInOtherAssetsOpeCFIFRS',
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

def decrease_increase_in_other_financial_assets_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    その他の金融資産の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-37740_DecreaseIncreaseInOtherFinancialAssetsOpeCFIFRS',
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

def decrease_increase_in_prepaid_expenses_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    前払費用の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-37740_DecreaseIncreaseInPrepaidExpensesOpeCFIFRS',
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

def increase_decrease_in_deferred_income_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    繰延収益の増減額（△は減少）、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-37740_IncreaseDecreaseInDeferredIncomeOpeCFIFRS',
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

def increase_decrease_in_other_financial_liabilities_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    その他の金融負債の増減額（△は減少）、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-37740_IncreaseDecreaseInOtherFinancialLiabilitiesOpeCFIFRS',
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

def investment_securities_equity_ncaifrs(session: Session, head_item_key:str, context:str):
    """
    投資有価証券（株式）、非流動資産（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-37740_InvestmentSecuritiesEquityNCAIFRS',
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

def network_services_revenues_ifrs(session: Session, head_item_key:str, context:str):
    """
    ネットワークサービス売上高（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-37740_NetworkServicesRevenuesIFRS',
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

def payments_for_refundable_insurance_policies_inv_cfifrs(session: Session, head_item_key:str, context:str):
    """
    積立保険料の支払、投資活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-37740_PaymentsForRefundableInsurancePoliciesInvCFIFRS',
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

def payments_of_other_financial_liabilities_fin_cfifrs(session: Session, head_item_key:str, context:str):
    """
    その他の金融負債の支払、財務活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-37740_PaymentsOfOtherFinancialLiabilitiesFinCFIFRS',
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

def prepaid_expenses_caifrs(session: Session, head_item_key:str, context:str):
    """
    前払費用、流動資産（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-37740_PrepaidExpensesCAIFRS',
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

def prepaid_expenses_ncaifrs(session: Session, head_item_key:str, context:str):
    """
    前払費用、非流動資産（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-37740_PrepaidExpensesNCAIFRS',
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

def proceeds_from_other_financial_liabilities_fin_cfifrs(session: Session, head_item_key:str, context:str):
    """
    その他の金融負債による収入、財務活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-37740_ProceedsFromOtherFinancialLiabilitiesFinCFIFRS',
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

def proceeds_from_sales_of_investment_securities_equity_inv_cfifrs(session: Session, head_item_key:str, context:str):
    """
    投資有価証券（株式）の売却による収入、投資活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-37740_ProceedsFromSalesOfInvestmentSecuritiesEquityInvCFIFRS',
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

def purchases_of_investment_securities_equity_inv_cfifrs(session: Session, head_item_key:str, context:str):
    """
    投資有価証券（株式）の取得による支出、投資活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-37740_PurchasesOfInvestmentSecuritiesEquityInvCFIFRS',
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

def si_revenues_ifrs(session: Session, head_item_key:str, context:str):
    """
    システムインテグレーション売上高（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-37740_SIRevenuesIFRS',
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

def group_headquarters_management_costs_and_other_expenses_ifrs(session: Session, head_item_key:str, context:str):
    """
    親会社の本社管理費等（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-45230_GroupHeadquartersManagementCostsAndOtherExpensesIFRS',
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

def increase_decrease_in_working_capital_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    運転資本の増減額(△は増加)、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-45230_IncreaseDecreaseInWorkingCapitalOpeCFIFRS',
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

def payments_of_time_deposits_exceeding_three_month_inv_cfifrs(session: Session, head_item_key:str, context:str):
    """
    3カ月超預金の預入による支出、投資活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-45230_PaymentsOfTimeDepositsExceedingThreeMonthInvCFIFRS',
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

def payments_on_investments_in_joint_ventures_inv_cfifrs(session: Session, head_item_key:str, context:str):
    """
    共同支配企業に対する投資による支出、投資活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-45230_PaymentsOnInvestmentsInJointVenturesInvCFIFRS',
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

def proceeds_from_redemption_of_time_deposits_exceeding_three_months_inv_cfifrs(session: Session, head_item_key:str, context:str):
    """
    3カ月超預金の払戻による収入、投資活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-45230_ProceedsFromRedemptionOfTimeDepositsExceedingThreeMonthsInvCFIFRS',
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

def proceeds_from_sale_and_redemption_of_financial_assets_inv_cfifrs(session: Session, head_item_key:str, context:str):
    """
    金融資産の売却・償還による収入、投資活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-45230_ProceedsFromSaleAndRedemptionOfFinancialAssetsInvCFIFRS',
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

def purchases_of_financial_assets_inv_cfifrs(session: Session, head_item_key:str, context:str):
    """
    金融資産の取得による支出、投資活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-45230_PurchasesOfFinancialAssetsInvCFIFRS',
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

def research_and_development_expenditure_recognized_as_expense_during_period_segment_information_ifrs(session: Session, head_item_key:str, context:str):
    """
    当期に費用認識した研究開発費、セグメント情報（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-45230_ResearchAndDevelopmentExpenditureRecognizedAsExpenseDuringPeriodSegmentInformationIFRS',
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

def increase_decrease_in_other_non_current_liabilities_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    その他の非流動負債の増減額（△は減少）、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-51950_IncreaseDecreaseInOtherNonCurrentLiabilitiesOpeCFIFRS',
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

def net_increase_decrease_in_short_term_loans_borrowings_within_three_months_fin_cfifrs(session: Session, head_item_key:str, context:str):
    """
    短期借入金（３ヶ月以内）の純増減額（△は減少）、財務活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-51950_NetIncreaseDecreaseInShortTermLoansBorrowingsWithinThreeMonthsFinCFIFRS',
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

def americas_ifrs(session: Session, head_item_key:str, context:str):
    """
    米州、外部顧客への売上高 地域別区分への分解（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-52020_AmericasIFRS',
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

def asia_ifrs(session: Session, head_item_key:str, context:str):
    """
    アジア、外部顧客への売上高 地域別区分への分解（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-52020_AsiaIFRS',
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

def assets_held_at_fair_value_through_other_comprehensive2_caifrs(session: Session, head_item_key:str, context:str):
    """
    その他の包括利益を通じて公正価値を測定する金融資産、流動資産（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-52020_AssetsHeldAtFairValueThroughOtherComprehensive2CAIFRS',
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

def assets_held_at_fair_value_through_other_comprehensive_income_ifrs(session: Session, head_item_key:str, context:str):
    """
    その他の包括利益を通じて公正価値を測定する金融資産（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-52020_AssetsHeldAtFairValueThroughOtherComprehensiveIncomeIFRS',
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

def capital_contribution_for_non_controlling_interests_ifrsifrs(session: Session, head_item_key:str, context:str):
    """
    非支配持分株主との資本取引による支出、財務活動によるキャッシュ・フロー（IFRS）（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-52020_CapitalContributionForNonControllingInterestsIFRSIFRS',
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

def changes_in_ownership_interests_in_subsidiaries_and_others_ssifrs(session: Session, head_item_key:str, context:str):
    """
    子会社等に対する所有持分の変動額、持分変動計算書（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-52020_ChangesInOwnershipInterestsInSubsidiariesAndOthersSSIFRS',
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

def dividends_received_from_joint_ventures_and_associates_inv_cfifrs(session: Session, head_item_key:str, context:str):
    """
    持分法適用会社からの配当金受領額、投資活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-52020_DividendsReceivedFromJointVenturesAndAssociatesInvCFIFRS',
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

def europe_ifrs(session: Session, head_item_key:str, context:str):
    """
    欧州、外部顧客への売上高 地域別区分への分解（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-52020_EuropeIFRS',
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

def exceptional_items_gains_ifrs(session: Session, head_item_key:str, context:str):
    """
    個別開示項目収益（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-52020_ExceptionalItemsGainsIFRS',
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

def exceptional_items_losses_ifrs(session: Session, head_item_key:str, context:str):
    """
    個別開示項目費用（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-52020_ExceptionalItemsLossesIFRS',
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

def hyperinflation_adjustment_cfifrs(session: Session, head_item_key:str, context:str):
    """
    超インフレの調整、キャッシュ・フロー計算書（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-52020_HyperinflationAdjustmentCFIFRS',
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

def hyperinflation_adjustment_ssifrs(session: Session, head_item_key:str, context:str):
    """
    超インフレの調整、持分変動計算書（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-52020_HyperinflationAdjustmentSSIFRS',
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

def operating_profit_after_exceptional_items_ifrs(session: Session, head_item_key:str, context:str):
    """
    個別開示項目後営業利益（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-52020_OperatingProfitAfterExceptionalItemsIFRS',
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

def other_gains_losses_on_equity_method_investments_ifrs(session: Session, head_item_key:str, context:str):
    """
    持分法投資に関するその他の利益（△は損失）（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-52020_OtherGainsLossesOnEquityMethodInvestmentsIFRS',
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

def proceeds_from_borrowings_fin_cfifrs(session: Session, head_item_key:str, context:str):
    """
    社債発行及び借入れによる収入、財務活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-52020_ProceedsFromBorrowingsFinCFIFRS',
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

def proceeds_on_disposal_of_assets_held_at_fair_value_through_other_comprehensive_income_inv_cfifrs(session: Session, head_item_key:str, context:str):
    """
    その他の包括利益を通じて公正価値を測定する金融資産の売却による収入、投資活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-52020_ProceedsOnDisposalOfAssetsHeldAtFairValueThroughOtherComprehensiveIncomeInvCFIFRS',
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

def proceeds_on_disposal_of_joint_ventures_and_associates_ifrs(session: Session, head_item_key:str, context:str):
    """
    ジョイント・ベンチャー及び関連会社の売却による収入、投資活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-52020_ProceedsOnDisposalOfJointVenturesAndAssociatesIFRS',
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

def purchase_of_assets_held_at_fair_value_through_other_comprehensive_income_inv_cfifrs(session: Session, head_item_key:str, context:str):
    """
    その他の包括利益を通じて公正価値を測定する金融資産の取得による支出、投資活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-52020_PurchaseOfAssetsHeldAtFairValueThroughOtherComprehensiveIncomeInvCFIFRS',
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

def repayment_of_borrowings_fin_cfifrs(session: Session, head_item_key:str, context:str):
    """
    社債償還及び借入金返済による支出、財務活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-52020_RepaymentOfBorrowingsFinCFIFRS',
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

def retained_earnings_translation_adjustment_at_the_ifrs_transition_date_equity_ifrs(session: Session, head_item_key:str, context:str):
    """
    利益剰余金（IFRS移行時の累積換算差額）、資本（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-52020_RetainedEarningsTranslationAdjustmentAtTheIFRSTransitionDateEquityIFRS',
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

def reversal_of_previous_impairment_of_financial_receivables_owed_by_joint_ventures_and_associates_ifrs(session: Session, head_item_key:str, context:str):
    """
    持分法適用会社に対する金融債権の減損損失の戻入益（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-52020_ReversalOfPreviousImpairmentOfFinancialReceivablesOwedByJointVenturesAndAssociatesIFRS',
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

def stock_options_ssifrs(session: Session, head_item_key:str, context:str):
    """
    新株予約権の増減、持分変動計算書（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-52020_StockOptionsSSIFRS',
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

def trade_and_other_receivables_ifrs(session: Session, head_item_key:str, context:str):
    """
    売上債権及びその他の債権、非流動資産（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-52020_TradeAndOtherReceivablesIFRS',
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

def proceeds_from_government_grants_fin_cfifrs(session: Session, head_item_key:str, context:str):
    """
    政府補助金による収入、財務活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-60890_ProceedsFromGovernmentGrantsFinCFIFRS',
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

def proceeds_from_sales_or_redemption_of_investments_in_debt_instruments_ifrs(session: Session, head_item_key:str, context:str):
    """
    負債性金融商品の売却又は償還による収入、投資活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-64480_ProceedsFromSalesOrRedemptionOfInvestmentsInDebtInstrumentsIFRS',
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

def purchase_of_investments_in_debt_instruments_ifrs(session: Session, head_item_key:str, context:str):
    """
    負債性金融商品の取得による支出、投資活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-64480_PurchaseOfInvestmentsInDebtInstrumentsIFRS',
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

def bonds_borrowings_and_lease_liabilities_clifrs(session: Session, head_item_key:str, context:str):
    """
    社債、借入金及びリース負債、流動負債（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-65030_BondsBorrowingsAndLeaseLiabilitiesCLIFRS',
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

def bonds_borrowings_and_lease_liabilities_nclifrs(session: Session, head_item_key:str, context:str):
    """
    社債、借入金及びリース負債、非流動負債（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-65030_BondsBorrowingsAndLeaseLiabilitiesNCLIFRS',
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

def free_cash_flow_cfifrs(session: Session, head_item_key:str, context:str):
    """
    フリー・キャッシュ・フロー、キャッシュ・フロー計算書（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-65030_FreeCashFlowCFIFRS',
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

def loss_gain_from_sales_and_disposal_of_property_plant_and_equipment_net_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    固定資産の売廃却損益、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-65030_LossGainFromSalesAndDisposalOfPropertyPlantAndEquipmentNetOpeCFIFRS',
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

def transactions_with_non_controlling_interests_and_others_ssifrs(session: Session, head_item_key:str, context:str):
    """
    非支配持分との取引等、持分変動計算書（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-65030_TransactionsWithNonControllingInterestsAndOthersSSIFRS',
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

def transactions_with_non_controlling_interests_fin_cfifrs(session: Session, head_item_key:str, context:str):
    """
    非支配持分との取引、財務活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-65030_TransactionsWithNonControllingInterestsFinCFIFRS',
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

def accounts_payable_and_accrued_expenses_clifrs(session: Session, head_item_key:str, context:str):
    """
    未払金及び未払費用、流動負債（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-67520_AccountsPayableAndAccruedExpensesCLIFRS',
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

def decrease_increase_in_trade_receivables_and_contract_assets_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    営業債権及び契約資産の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-67520_DecreaseIncreaseInTradeReceivablesAndContractAssetsOpeCFIFRS',
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

def exchange_differences_on_translation_of_foreign_operations_ssifrs(session: Session, head_item_key:str, context:str):
    """
    在外営業活動体の換算差額、持分変動計算書（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-67520_ExchangeDifferencesOnTranslationOfForeignOperationsSSIFRS',
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

def financial_assets_measured_at_fair_value_through_other_comprehensive_income_ssifrs(session: Session, head_item_key:str, context:str):
    """
    その他の包括利益を通じて公正価値で測定する金融資産、持分変動計算書（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-67520_FinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncomeSSIFRS',
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

def increase_decrease_in_long_term_debt_fin_cfifrs(session: Session, head_item_key:str, context:str):
    """
    長期債務の増減額（△は減少）、財務活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-67520_IncreaseDecreaseInLongTermDebtFinCFIFRS',
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

def increase_decrease_in_short_term_debt_fin_cfifrs(session: Session, head_item_key:str, context:str):
    """
    短期債務の増減額（△は減少）、財務活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-67520_IncreaseDecreaseInShortTermDebtFinCFIFRS',
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

def net_changes_in_cash_flow_hedges_ssifrs(session: Session, head_item_key:str, context:str):
    """
    キャッシュ・フロー・ヘッジの公正価値の純変動、持分変動計算書（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-67520_NetChangesInCashFlowHedgesSSIFRS',
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

def proceeds_from_sale_and_redemption_of_investments_accounted_for_using_the_equity_method_and_other_financial_assets_inv_cfifrs(session: Session, head_item_key:str, context:str):
    """
    持分法投資及びその他の金融資産の売却及び償還、投資活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-67520_ProceedsFromSaleAndRedemptionOfInvestmentsAccountedForUsingTheEquityMethodAndOtherFinancialAssetsInvCFIFRS',
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

def purchase_of_investments_accounted_for_using_the_equity_method_and_other_financial_assets_inv_cfifrs(session: Session, head_item_key:str, context:str):
    """
    持分法投資及びその他の金融資産の取得、投資活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-67520_PurchaseOfInvestmentsAccountedForUsingTheEquityMethodAndOtherFinancialAssetsInvCFIFRS',
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

def remeasurements_of_defined_benefit_plans_ssifrs(session: Session, head_item_key:str, context:str):
    """
    確定給付制度の再測定、持分変動計算書（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-67520_RemeasurementsOfDefinedBenefitPlansSSIFRS',
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

def short_term_debt_including_current_portion_of_long_term_debt_clifrs(session: Session, head_item_key:str, context:str):
    """
    短期負債及び一年以内返済長期負債、流動負債（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-67520_ShortTermDebtIncludingCurrentPortionOfLongTermDebtCLIFRS',
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

def trade_receivables_and_contract_assets_caifrs(session: Session, head_item_key:str, context:str):
    """
    営業債権及び契約資産、流動資産（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-67520_TradeReceivablesAndContractAssetsCAIFRS',
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

def transactions_with_non_controlling_interests_and_other_ssifrs(session: Session, head_item_key:str, context:str):
    """
    非支配持分との取引等、持分変動計算書（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-67520_TransactionsWithNonControllingInterestsAndOtherSSIFRS',
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

def content_assets_ncaifrs(session: Session, head_item_key:str, context:str):
    """
    コンテンツ資産、非流動資産（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-67580_ContentAssetsNCAIFRS',
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

def costs_and_expenses_costs_and_expenses_ifrs(session: Session, head_item_key:str, context:str):
    """
    売上原価、販売費・一般管理費及びその他の一般費用、売上原価、販売費・一般管理費及びその他の一般費用（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-67580_CostsAndExpensesCostsAndExpensesIFRS',
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

def current_portion_of_long_term_debt_clifrs(session: Session, head_item_key:str, context:str):
    """
    １年以内に返済期限の到来する長期借入債務、流動負債（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-67580_CurrentPortionOfLongTermDebtCLIFRS',
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

def deposits_from_customers_in_the_banking_business_clifrs(session: Session, head_item_key:str, context:str):
    """
    銀行ビジネスにおける顧客預金、流動負債（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-67580_DepositsFromCustomersInTheBankingBusinessCLIFRS',
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

def exercise_of_share_acquisition_rights_and_other_ssifrs(session: Session, head_item_key:str, context:str):
    """
    新株予約権の行使等、持分変動計算書（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-67580_ExerciseOfShareAcquisitionRightsAndOtherSSIFRS',
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

def financial_services_expenses_costs_and_expenses_ifrs(session: Session, head_item_key:str, context:str):
    """
    金融ビジネス費用、売上原価、販売費・一般管理費及びその他の一般費用（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-67580_FinancialServicesExpensesCostsAndExpensesIFRS',
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

def financial_services_revenue_sales_and_operating_revenue_ifrs(session: Session, head_item_key:str, context:str):
    """
    金融ビジネス収入、売上高及び金融ビジネス収入（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-67580_FinancialServicesRevenueSalesAndOperatingRevenueIFRS',
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

def gain_loss_on_securities_net_other_than_financial_services_segment_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    有価証券に関する損（益）（純額）（金融分野以外）、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-67580_GainLossOnSecuritiesNetOtherThanFinancialServicesSegmentOpeCFIFRS',
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

def increase_decrease_in_borrowings_in_the_life_insurance_business_and_the_banking_business_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    生命保険ビジネス及び銀行ビジネスにおける借入債務の増加・減少（△）、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-67580_IncreaseDecreaseInBorrowingsInTheLifeInsuranceBusinessAndTheBankingBusinessOpeCFIFRS',
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

def increase_decrease_in_content_assets_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    コンテンツ資産の増加（△）・減少、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-67580_IncreaseDecreaseInContentAssetsOpeCFIFRS',
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

def increase_decrease_in_deposits_from_customers_in_the_banking_business_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    銀行ビジネスにおける顧客預金の増加・減少（△）、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-67580_IncreaseDecreaseInDepositsFromCustomersInTheBankingBusinessOpeCFIFRS',
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

def increase_decrease_in_insurance_contract_liabilities_net_of_insurance_contract_assets_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    保険契約負債（保険契約資産との純額）の増加・減少（△）、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-67580_IncreaseDecreaseInInsuranceContractLiabilitiesNetOfInsuranceContractAssetsOpeCFIFRS',
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

def increase_decrease_in_investments_and_advances_in_the_financial_services_business_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    金融分野における投資及び貸付の増加（△）・減少、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-67580_IncreaseDecreaseInInvestmentsAndAdvancesInTheFinancialServicesBusinessOpeCFIFRS',
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

def increase_decrease_in_other_financial_assets_and_other_current_assets_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    その他の金融資産及びその他の資産（流動）の増加（△）・減少、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-67580_IncreaseDecreaseInOtherFinancialAssetsAndOtherCurrentAssetsOpeCFIFRS',
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

def increase_decrease_in_other_financial_liabilities_and_other_current_liabilities_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    その他の金融負債及びその他の負債（流動）の増加・減少（△）、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-67580_IncreaseDecreaseInOtherFinancialLiabilitiesAndOtherCurrentLiabilitiesOpeCFIFRS',
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

def increase_decrease_in_taxes_payable_other_than_income_taxes_net_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    法人所得税以外の未払税金（純額）の増加・減少（△）、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-67580_IncreaseDecreaseInTaxesPayableOtherThanIncomeTaxesNetOpeCFIFRS',
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

def increase_decrease_in_trade_receivables_and_contract_assets_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    営業債権及び契約資産の増加（△）・減少、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-67580_IncreaseDecreaseInTradeReceivablesAndContractAssetsOpeCFIFRS',
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

def insurance_contract_liabilities_nclifrs(session: Session, head_item_key:str, context:str):
    """
    保険契約負債（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-67580_InsuranceContractLiabilitiesNCLIFRS',
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

def insurance_finance_expenses_income_financial_services_expenses_ifrs(session: Session, head_item_key:str, context:str):
    """
    保険金融費用（収益）、金融ビジネス費用（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-67580_InsuranceFinanceExpensesIncomeFinancialServicesExpensesIFRS',
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

def insurance_finance_income_expenses_net_of_tax_items_that_may_be_reclassified_to_profit_or_loss_ociifrs(session: Session, head_item_key:str, context:str):
    """
    保険金融収益（費用）（税引後）、純損益に振り替えられる可能性のあるその他の包括利益（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-67580_InsuranceFinanceIncomeExpensesNetOfTaxItemsThatMayBeReclassifiedToProfitOrLossOCIIFRS',
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

def insurance_income_financial_services_revenue_ifrs(session: Session, head_item_key:str, context:str):
    """
    保険収益、金融ビジネス収入（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-67580_InsuranceIncomeFinancialServicesRevenueIFRS',
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

def insurance_service_costs_financial_services_expenses_ifrs(session: Session, head_item_key:str, context:str):
    """
    保険サービス費用、金融ビジネス費用（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-67580_InsuranceServiceCostsFinancialServicesExpensesIFRS',
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

def intersegment_sales_and_financial_services_revenue_ifrs(session: Session, head_item_key:str, context:str):
    """
    セグメント間の売上高及び金融ビジネス収入（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-67580_IntersegmentSalesAndFinancialServicesRevenueIFRS',
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

def investments_and_advances_in_the_financial_services_segment_caifrs(session: Session, head_item_key:str, context:str):
    """
    金融分野における投資及び貸付、流動資産（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-67580_InvestmentsAndAdvancesInTheFinancialServicesSegmentCAIFRS',
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

def investments_and_advances_in_the_financial_services_segment_ncaifrs(session: Session, head_item_key:str, context:str):
    """
    金融分野における投資及び貸付、非流動資産（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-67580_InvestmentsAndAdvancesInTheFinancialServicesSegmentNCAIFRS',
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

def long_term_debt2_nclifrs(session: Session, head_item_key:str, context:str):
    """
    長期借入債務、非流動負債（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-67580_LongTermDebt2NCLIFRS',
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

def other_financial_services_expense_financial_services_expenses_ifrs(session: Session, head_item_key:str, context:str):
    """
    その他の保険ビジネス費用、金融ビジネス費用（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-67580_OtherFinancialServicesExpenseFinancialServicesExpensesIFRS',
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

def other_financial_services_revenue_financial_services_revenue_ifrs(session: Session, head_item_key:str, context:str):
    """
    その他の金融ビジネス収入、金融ビジネス収入（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-67580_OtherFinancialServicesRevenueFinancialServicesRevenueIFRS',
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

def other_net_of_tax_items_that_may_be_reclassified_to_profit_or_loss_ociifrs(session: Session, head_item_key:str, context:str):
    """
    その他（税引後）、純損益に振り替えられる可能性のあるその他の包括利益（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-67580_OtherNetOfTaxItemsThatMayBeReclassifiedToProfitOrLossOCIIFRS',
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

def other_operating_income_expense_net_costs_and_expenses_ifrs(session: Session, head_item_key:str, context:str):
    """
    その他の営業損（益）（純額）、売上原価、販売費・一般管理費及びその他の一般費用（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-67580_OtherOperatingIncomeExpenseNetCostsAndExpensesIFRS',
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

def other_operating_income_expense_net_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    その他の営業損（益）（純額）、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-67580_OtherOperatingIncomeExpenseNetOpeCFIFRS',
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

def participation_liabilities_in_the_pictures_segment_clifrs(session: Session, head_item_key:str, context:str):
    """
    映画分野における未払分配金債務、流動負債（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-67580_ParticipationLiabilitiesInThePicturesSegmentCLIFRS',
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

def participation_liabilities_in_the_pictures_segment_nclifrs(session: Session, head_item_key:str, context:str):
    """
    映画分野における未払分配金債務、非流動負債（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-67580_ParticipationLiabilitiesInThePicturesSegmentNCLIFRS',
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

def payments_for_investments_and_advances_other_than_financial_services_business_inv_cfifrs(session: Session, head_item_key:str, context:str):
    """
    投資及び貸付（金融分野以外）、投資活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-67580_PaymentsForInvestmentsAndAdvancesOtherThanFinancialServicesBusinessInvCFIFRS',
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

def payments_of_long_term_debt_fin_cfifrs(session: Session, head_item_key:str, context:str):
    """
    長期借入債務の返済、財務活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-67580_PaymentsOfLongTermDebtFinCFIFRS',
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

def proceeds_from_issuance_of_long_term_debt_fin_cfifrs(session: Session, head_item_key:str, context:str):
    """
    長期借入債務による調達、財務活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-67580_ProceedsFromIssuanceOfLongTermDebtFinCFIFRS',
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

def proceeds_from_sales_or_return_of_investments_and_collections_of_advances_other_than_financial_services_business_inv_cfifrs(session: Session, head_item_key:str, context:str):
    """
    投資の売却又は償還及び貸付の回収（金融分野以外）、投資活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-67580_ProceedsFromSalesOrReturnOfInvestmentsAndCollectionsOfAdvancesOtherThanFinancialServicesBusinessInvCFIFRS',
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

def sales_and_financial_services_revenue_ifrs(session: Session, head_item_key:str, context:str):
    """
    売上高及び金融ビジネス収入（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-67580_SalesAndFinancialServicesRevenueIFRS',
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

def sales_and_financial_services_revenue_to_customers_ifrs(session: Session, head_item_key:str, context:str):
    """
    外部顧客への売上高及び金融ビジネス収入（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-67580_SalesAndFinancialServicesRevenueToCustomersIFRS',
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

def share_of_profit_loss_of_investments_accounted_for_using_the_equity_method_net_of_dividends_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    持分法による投資（利益）損失（純額）（受取配当金相殺後）、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-67580_ShareOfProfitLossOfInvestmentsAccountedForUsingTheEquityMethodNetOfDividendsOpeCFIFRS',
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

def trade_receivables_other_receivables_and_contract_assets_caifrs(session: Session, head_item_key:str, context:str):
    """
    営業債権、その他の債権及び契約資産、流動資産（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-67580_TradeReceivablesOtherReceivablesAndContractAssetsCAIFRS',
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

def transactions_with_noncontrolling_interests_shareholders_and_other_ssifrs(session: Session, head_item_key:str, context:str):
    """
    非支配持分株主との取引及びその他、持分変動計算書（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-67580_TransactionsWithNoncontrollingInterestsShareholdersAndOtherSSIFRS',
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

def decrease_increase_in_derivative_liabilities_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    デリバティブ負債の増減額（△は減少）、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-67790_DecreaseIncreaseInDerivativeLiabilitiesOpeCFIFRS',
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

def deferred_government_grants_nclifrs(session: Session, head_item_key:str, context:str):
    """
    政府補助金繰延収益、非流動負債（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-67790_DeferredGovernmentGrantsNCLIFRS',
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

def exchange_differences_on_translation_of_foreign_operations_ifrs(session: Session, head_item_key:str, context:str):
    """
    在外営業活動体の換算差額（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-67790_ExchangeDifferencesOnTranslationOfForeignOperationsIFRS',
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

def government_grants_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    政府補助金、営業活動によるキャッシュフロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-67790_GovernmentGrantsOpeCFIFRS',
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

def increase_decrease_in_accrued_expenses_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    未払費用の増減額（△は減少）、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-67790_IncreaseDecreaseInAccruedExpensesOpeCFIFRS',
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

def increase_decrease_in_consumption_tax_value_added_tax_receivables_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    未収消費税等の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-67790_IncreaseDecreaseInConsumptionTaxValueAddedTaxReceivablesOpeCFIFRS',
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

def increase_decrease_in_derivative_assets_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    デリバティブ資産の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-67790_IncreaseDecreaseInDerivativeAssetsOpeCFIFRS',
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

def net_change_in_financial_assets_measured_at_fair_value_through_other_comprehensive_income_ifrs(session: Session, head_item_key:str, context:str):
    """
    その他の包括利益を通じて公正価値で測定する金融資産の純変動（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-67790_NetChangeInFinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncomeIFRS',
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

def share_of_other_comprehensive_income_of_entities_accounted_for_using_equity_method_ifrs(session: Session, head_item_key:str, context:str):
    """
    持分法によるその他の包括利益に対する持分相当額（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-67790_ShareOfOtherComprehensiveIncomeOfEntitiesAccountedForUsingEquityMethodIFRS',
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

def share_of_other_comprehensive_income_of_entities_accounted_for_using_equity_method_items_that_may_be_reclassified_to_profit_or_loss_ifrs(session: Session, head_item_key:str, context:str):
    """
    持分法によるその他の包括利益に対する持分相当額、純損益に振り替えられる可能性のある項目（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-67790_ShareOfOtherComprehensiveIncomeOfEntitiesAccountedForUsingEquityMethodItemsThatMayBeReclassifiedToProfitOrLossIFRS',
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

def increase_decrease_in_long_term_accounts_payable_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    長期未払金の増減額（△は減少）、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-68030_IncreaseDecreaseInLongTermAccountsPayableOpeCFIFRS',
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

def long_term_accounts_payable_nclifrs(session: Session, head_item_key:str, context:str):
    """
    長期未払金、非流動負債（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-68030_LongTermAccountsPayableNCLIFRS',
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

def retained_earnings_cumulative_translation_difference_at_transition_to_ifrsifrs(session: Session, head_item_key:str, context:str):
    """
    利益剰余金（IFRS移行時の累積換算差額）、資本（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-68030_RetainedEarningsCumulativeTranslationDifferenceAtTransitionToIFRSIFRS',
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

def bonds_borrowings_and_other_financial_liabilities_clifrs(session: Session, head_item_key:str, context:str):
    """
    社債、借入金及びその他の金融負債、流動負債（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-70120_BondsBorrowingsAndOtherFinancialLiabilitiesCLIFRS',
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

def bonds_borrowings_and_other_financial_liabilities_nclifrs(session: Session, head_item_key:str, context:str):
    """
    社債、借入金及びその他の金融負債、非流動負債（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-70120_BondsBorrowingsAndOtherFinancialLiabilitiesNCLIFRS',
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

def business_profit_loss_ifrs(session: Session, head_item_key:str, context:str):
    """
    事業利益（△は損失）（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-70120_BusinessProfitLossIFRS',
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

def capital_increase_of_consolidated_subsidiaries_ssifrs(session: Session, head_item_key:str, context:str):
    """
    連結子会社の増資による持分の増減、持分変動計算書（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-70120_CapitalIncreaseOfConsolidatedSubsidiariesSSIFRS',
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

def change_in_ownership_interest_of_parent_due_to_transactions_with_non_controlling_interests_ssifrs(session: Session, head_item_key:str, context:str):
    """
    非支配株主との取引に係る親会社の持分変動、持分変動計算書（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-70120_ChangeInOwnershipInterestOfParentDueToTransactionsWithNonControllingInterestsSSIFRS',
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

def decrease_increase_in_avdance_payment_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    前渡金の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-70120_DecreaseIncreaseInAvdancePaymentOpeCFIFRS',
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

def increase_decrease_in_other_current_assets_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    その他流動資産の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-70120_IncreaseDecreaseInOtherCurrentAssetsOpeCFIFRS',
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

def increase_decrease_in_refund_liability_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    返金負債の増減額（△は減少）、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-70120_IncreaseDecreaseInRefundLiabilityOpeCFIFRS',
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

def payments_for_acquisition_of_subsidiaries_not_resulting_in_change_in_scope_of_consolidation_fin_cfifrs(session: Session, head_item_key:str, context:str):
    """
    連結範囲の変更を伴わない子会社株式の取得による支出、財務活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-70120_PaymentsForAcquisitionOfSubsidiariesNotResultingInChangeInScopeOfConsolidationFinCFIFRS',
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

def payments_for_equity_method_investment_and_purchase_of_other_financial_assets_inv_cfifrs(session: Session, head_item_key:str, context:str):
    """
    持分法投資及びその他の金融資産の取得による支出、投資活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-70120_PaymentsForEquityMethodInvestmentAndPurchaseOfOtherFinancialAssetsInvCFIFRS',
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

def proceeds_from_equity_method_investment_and_sale_of_other_financial_assets_inv_cfifrs(session: Session, head_item_key:str, context:str):
    """
    持分法投資及びその他の金融資産の売却による収入、投資活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-70120_ProceedsFromEquityMethodInvestmentAndSaleOfOtherFinancialAssetsInvCFIFRS',
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

def proceeds_from_factoring_agreements_fin_cfifrs(session: Session, head_item_key:str, context:str):
    """
    債権流動化による収入、財務活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-70120_ProceedsFromFactoringAgreementsFinCFIFRS',
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

def refund_liabilities_clifrs(session: Session, head_item_key:str, context:str):
    """
    返金負債、流動負債（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-70120_RefundLiabilitiesCLIFRS',
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

def repayment_of_liabilities_under_factoring_agreements_fin_cfifrs(session: Session, head_item_key:str, context:str):
    """
    債権流動化の返済による支出、財務活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-70120_RepaymentOfLiabilitiesUnderFactoringAgreementsFinCFIFRS',
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

def increase_decrease_in_equity_due_to_acquisition_of_shares_in_consolidated_subsidiaries_ifrs(session: Session, head_item_key:str, context:str):
    """
    連結子会社株式の取得による持分の増減（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-72690_IncreaseDecreaseInEquityDueToAcquisitionOfSharesInConsolidatedSubsidiariesIFRS',
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

def increase_decrease_in_liabilities_related_to_provisions_and_employee_benefits_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    引当金及び従業員給付に係る負債の増減額（△は減少）、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-72690_IncreaseDecreaseInLiabilitiesRelatedToProvisionsAndEmployeeBenefitsOpeCFIFRS',
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

def payments_from_changes_in_ownership_interests_in_subsidiaries_that_do_not_result_in_change_in_scope_of_consolidation_fin_cfifrs(session: Session, head_item_key:str, context:str):
    """
    連結範囲の変更を伴わない子会社株式の取得による支出、財務活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-72690_PaymentsFromChangesInOwnershipInterestsInSubsidiariesThatDoNotResultInChangeInScopeOfConsolidationFinCFIFRS',
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

def proceeds_from_sale_or_recovery_of_other_financial_assets_inv_cfifrs(session: Session, head_item_key:str, context:str):
    """
    その他の金融資産の売却または回収による収入、投資活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-72690_ProceedsFromSaleOrRecoveryOfOtherFinancialAssetsInvCFIFRS',
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

def purchase_of_intangible_assets_and_expenditure_on_internally_generated_intangible_assets_inv_cfifrs(session: Session, head_item_key:str, context:str):
    """
    無形資産の取得及び内部開発にかかわる支出、投資活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-72690_PurchaseOfIntangibleAssetsAndExpenditureOnInternallyGeneratedIntangibleAssetsInvCFIFRS',
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

def decrease_increase_in_deposits_for_purchase_of_treasury_shares_fin_cfifrs(session: Session, head_item_key:str, context:str):
    """
    自己株式取得のための預託金の増減額（△は増加）、財務活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-73130_DecreaseIncreaseInDepositsForPurchaseOfTreasurySharesFinCFIFRS',
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

def loss_gain_on_disposal_of_non_current_assets_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    固定資産処分損益（△は益）、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-73130_LossGainOnDisposalOfNonCurrentAssetsOpeCFIFRS',
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

def net_decrease_increase_in_leased_receivables_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    リース債権の増減額(△は増加)、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-73130_NetDecreaseIncreaseInLeasedReceivablesOpeCFIFRS',
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

def expense_by_acquisition_of_repurchased_stock_of_consolidated_subsidiary_fin_cfifrs(session: Session, head_item_key:str, context:str):
    """
    連結子会社の自己株式の取得による支出、財務活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-76160_ExpenseByAcquisitionOfRepurchasedStockOfConsolidatedSubsidiaryFinCFIFRS',
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

def tra_changes_in_ownership_interest_in_subsidiaries_ssifrs(session: Session, head_item_key:str, context:str):
    """
    非支配株主との取引に係る親会社の持分変動、持分変動計算書（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-76160_TraChangesInOwnershipInterestInSubsidiariesSSIFRS',
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

def claw_back_from_cancellation_of_stock_acquisition_agreements_inv_cfifrs(session: Session, head_item_key:str, context:str):
    """
    株式取得契約の解除に伴う回収額、投資活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-77330_ClawBackFromCancellationOfStockAcquisitionAgreementsInvCFIFRS',
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

def decrease_increase_in_deposit_for_purchase_of_treasury_shares_fin_cfifrs(session: Session, head_item_key:str, context:str):
    """
    自己株式取得のための預託金の増減額、財務活動によるキャッシュ・フロー（△は増加）（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-77330_DecreaseIncreaseInDepositForPurchaseOfTreasurySharesFinCFIFRS',
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

def gain_on_transfer_of_ssd_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    科学事業の譲渡益、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-77330_GainOnTransferOfSSDOpeCFIFRS',
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

def payments_for_contingent_consideration_inv_cfifrs(session: Session, head_item_key:str, context:str):
    """
    条件付対価の決済による支出、投資活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-77330_PaymentsForContingentConsiderationInvCFIFRS',
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

def proceeds_from_sale_of_ssd_businessse_inv_cfifrs(session: Session, head_item_key:str, context:str):
    """
    科学事業の譲渡による収入、投資活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-77330_ProceedsFromSaleOfSSDBusinessseInvCFIFRS',
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

def proceeds_from_transfer_of_collagen_business_and_dental_product_sales_businesses_inv_cfifrs(session: Session, head_item_key:str, context:str):
    """
    コラーゲン事業及び歯科用商品販売事業の譲渡による収入、投資活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-77330_ProceedsFromTransferOfCollagenBusinessAndDentalProductSalesBusinessesInvCFIFRS',
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

def transfer_from_retained_earnings_to_capital_surplus_ssifrs(session: Session, head_item_key:str, context:str):
    """
    利益剰余金から資本剰余金への振替額、持分変動計算書（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-77330_TransferFromRetainedEarningsToCapitalSurplusSSIFRS',
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

def capital_transaction_with_non_controlling_interests_ifrs(session: Session, head_item_key:str, context:str):
    """
    非支配株主との資本取引（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-77520_CapitalTransactionWithNonControllingInterestsIFRS',
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

def increase_in_lease_receivables_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    リース債権の増加、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-77520_IncreaseInLeaseReceivablesOpeCFIFRS',
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

def intersegment_operating_expenses_ifrs(session: Session, head_item_key:str, context:str):
    """
    セグメント間の営業費用（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-77520_IntersegmentOperatingExpensesIFRS',
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

def net_change_in_treasury_stock_ssifrs(session: Session, head_item_key:str, context:str):
    """
    自己株式の取得及び売却、持分変動計算書（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-77520_NetChangeInTreasuryStockSSIFRS',
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

def other_income_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    その他の収益、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-77520_OtherIncomeOpeCFIFRS',
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

def proceeds_from_sales_of_business_inv_cfifrs(session: Session, head_item_key:str, context:str):
    """
    事業の売却 （売却時の現金及び現金同等物保有額控除後）、投資活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-77520_ProceedsFromSalesOfBusinessInvCFIFRS',
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

def purchases_of_business_net_of_cash_acquired_inv_cfifrs(session: Session, head_item_key:str, context:str):
    """
    事業の買収（取得時の現金及び現金同等物受入額控除後）、投資活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-77520_PurchasesOfBusinessNetOfCashAcquiredInvCFIFRS',
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

def transfer_to_capital_surplus_from_retained_earnings_ifrs(session: Session, head_item_key:str, context:str):
    """
    利益剰余金から資本剰余金への振替（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-77520_TransferToCapitalSurplusFromRetainedEarningsIFRS',
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

def unallocatable_expenses_ifrs(session: Session, head_item_key:str, context:str):
    """
    配賦不能費用（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-77520_UnallocatableExpensesIFRS',
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

def assets_related_to_securities_business_ifrs(session: Session, head_item_key:str, context:str):
    """
    証券業関連資産、資産（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-84730_AssetsRelatedToSecuritiesBusinessIFRS',
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

def customer_deposits_for_banking_business_ifrs(session: Session, head_item_key:str, context:str):
    """
    顧客預金、負債（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-84730_CustomerDepositsForBankingBusinessIFRS',
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

def decrease_in_bond_and_borrowing_banking_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    社債及び借入金（銀行業）の増減、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-84730_DecreaseInBondAndBorrowingBankingOpeCFIFRS',
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

def decrease_in_payables_under_securities_lending_transactions_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    債券貸借取引受入担保金の増減、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-84730_DecreaseInPayablesUnderSecuritiesLendingTransactionsOpeCFIFRS',
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

def decrease_increase_in_assets_liabilities_related_to_securities_business_ifrs(session: Session, head_item_key:str, context:str):
    """
    証券業関連資産及び負債の増減、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-84730_DecreaseIncreaseInAssetsLiabilitiesRelatedToSecuritiesBusinessIFRS',
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

def decrease_increase_in_customer_deposits_for_banking_business_ifrs(session: Session, head_item_key:str, context:str):
    """
    顧客預金の増減、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-84730_DecreaseIncreaseInCustomerDepositsForBankingBusinessIFRS',
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

def decrease_increase_in_operational_investment_securities_ifrs(session: Session, head_item_key:str, context:str):
    """
    営業投資有価証券の増減、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-84730_DecreaseIncreaseInOperationalInvestmentSecuritiesIFRS',
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

def distributions_to_non_controlling_interests_in_consolidated_investment_funds_fin_cfifrs(session: Session, head_item_key:str, context:str):
    """
    投資事業組合等における非支配持分への分配金支払額、財務活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-84730_DistributionsToNonControllingInterestsInConsolidatedInvestmentFundsFinCFIFRS',
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

def expense_ifrs(session: Session, head_item_key:str, context:str):
    """
    費用（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-84730_ExpenseIFRS',
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

def financial_cost_associated_with_financial_income_ifrs(session: Session, head_item_key:str, context:str):
    """
    金融収益に係る金融費用、費用（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-84730_FinancialCostAssociatedWithFinancialIncomeIFRS',
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

def financial_instruments_pledged_as_collateral_assets_ifrs(session: Session, head_item_key:str, context:str):
    """
    担保差入金融商品、資産（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-84730_FinancialInstrumentsPledgedAsCollateralAssetsIFRS',
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

def fluctuations_in_discount_rates_of_insurance_contracts_items_that_may_be_reclassified_to_profit_or_loss_ociifrs(session: Session, head_item_key:str, context:str):
    """
    保険契約の割引率変動差額（税引後）、純損益に振り替えられる可能性のあるその他の包括利益（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-84730_FluctuationsInDiscountRatesOfInsuranceContractsItemsThatMayBeReclassifiedToProfitOrLossOCIIFRS',
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

def gain_on_bargain_purchase_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    負ののれん発生益、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-84730_GainOnBargainPurchaseOpeCFIFRS',
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

def insurance_contract_liabilities_ifrs(session: Session, head_item_key:str, context:str):
    """
    保険契約負債、負債（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-84730_InsuranceContractLiabilitiesIFRS',
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

def insurance_service_expenses_ifrs(session: Session, head_item_key:str, context:str):
    """
    保険サービス費用（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-84730_InsuranceServiceExpensesIFRS',
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

def inventories_assets_ifrs(session: Session, head_item_key:str, context:str):
    """
    棚卸資産、資産（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-84730_InventoriesAssetsIFRS',
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

def issuance_of_convertible_bonds_ssifrs(session: Session, head_item_key:str, context:str):
    """
    転換社債型新株予約権付社債の発行、持分変動計算書（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-84730_IssuanceOfConvertibleBondsSSIFRS',
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

def liabilities_related_to_securities_business_ifrs(session: Session, head_item_key:str, context:str):
    """
    証券業関連負債、負債（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-84730_LiabilitiesRelatedToSecuritiesBusinessIFRS',
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

def net_fair_value_gains_losses_net_of_tax_attributable_to_credit_risk_related_to_financial_liabilities_designated_as_at_fair_value_through_profit_or_loss_ociifrs(session: Session, head_item_key:str, context:str):
    """
    負債の信用リスクの変動額（税引後）、純損益に振り替えられることのないその他の包括利益（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-84730_NetFairValueGainsLossesNetOfTaxAttributableToCreditRiskRelatedToFinancialLiabilitiesDesignatedAsAtFairValueThroughProfitOrLossOCIIFRS',
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

def of_insurance_revenue_ifrs(session: Session, head_item_key:str, context:str):
    """
    （内、保険収益）（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-84730_OfInsuranceRevenueIFRS',
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

def of_interest_income_revenue_ifrs(session: Session, head_item_key:str, context:str):
    """
    （内、受取利息）（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-84730_OfInterestIncomeRevenueIFRS',
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

def operational_investment_securities_ifrs(session: Session, head_item_key:str, context:str):
    """
    営業投資有価証券、資産（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-84730_OperationalInvestmentSecuritiesIFRS',
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

def other_financial_cost_ifrs(session: Session, head_item_key:str, context:str):
    """
    その他の金融費用、費用（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-84730_OtherFinancialCostIFRS',
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

def other_investment_securities_ifrs(session: Session, head_item_key:str, context:str):
    """
    その他の投資有価証券、資産（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-84730_OtherInvestmentSecuritiesIFRS',
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

def proceeds_from_stock_issuance_to_non_controlling_interests_ifrs(session: Session, head_item_key:str, context:str):
    """
    投資事業組合等における非支配持分からの出資受入による収入、財務活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-84730_ProceedsFromStockIssuanceToNonControllingInterestsIFRS',
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

def provision_for_credit_losses_ifrs(session: Session, head_item_key:str, context:str):
    """
    信用損失引当金繰入（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-84730_ProvisionForCreditLossesIFRS',
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

def reinsurance_contracts_assets_ifrs(session: Session, head_item_key:str, context:str):
    """
    再保険契約資産、資産（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-84730_ReinsuranceContractsAssetsIFRS',
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

def changes_from_loss_of_control_ssifrs(session: Session, head_item_key:str, context:str):
    """
    支配喪失による変動、持分変動計算書（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-94340_ChangesFromLossOfControlSSIFRS',
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

def changes_in_the_fair_value_of_debt_investments_at_fvtoci_items_that_may_be_reclassified_to_profit_or_loss_ifrs(session: Session, head_item_key:str, context:str):
    """
    FVTOCIの負債性金融資産の公正価値の変動、純損益に振り替えられる可能性のある項目（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-94340_ChangesInTheFairValueOfDebtInvestmentsAtFVTOCIItemsThatMayBeReclassifiedToProfitOrLossIFRS',
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

def changes_in_the_fair_value_of_equity_investments_at_fvtoci_net_of_tax_items_that_will_not_be_reclassified_to_profit_or_loss_ociifrs(session: Session, head_item_key:str, context:str):
    """
    FVTOCIの資本性金融資産の公正価値の変動（税引後）、純損益に振り替えられることのないその他の包括利益（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-94340_ChangesInTheFairValueOfEquityInvestmentsAtFVTOCINetOfTaxItemsThatWillNotBeReclassifiedToProfitOrLossOCIIFRS',
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

def contract_costs_ncaifrs(session: Session, head_item_key:str, context:str):
    """
    契約コスト、非流動資産（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-94340_ContractCostsNCAIFRS',
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

def decrease_in_consumption_taxes_payable_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    未払消費税等の増減額（△は減少額）、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-94340_DecreaseInConsumptionTaxesPayableOpeCFIFRS',
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

def deposits_for_banking_business_clifrs(session: Session, head_item_key:str, context:str):
    """
    銀行事業の預金、流動負債（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-94340_DepositsForBankingBusinessCLIFRS',
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

def gain_or_loss_on_change_in_equity_ifrs(session: Session, head_item_key:str, context:str):
    """
    持分変動損益（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-94340_GainOrLossOnChangeInEquityIFRS',
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

def gain_or_loss_on_sale_of_equity_method_investment_ifrs(session: Session, head_item_key:str, context:str):
    """
    持分法による投資の売却損益（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-94340_GainOrLossOnSaleOfEquityMethodInvestmentIFRS',
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

def gain_or_loss_on_sales_of_equity_method_investments_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    持分法による投資の売却損益（△は益）、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-94340_GainOrLossOnSalesOfEquityMethodInvestmentsOpeCFIFRS',
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

def gain_relating_to_loss_of_control_over_subsidiaries_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    子会社の支配喪失に伴う利益、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-94340_GainRelatingToLossOfControlOverSubsidiariesOpeCFIFRS',
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

def increase_decrease_in_customer_deposits_in_banking_business_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    銀行事業の預金の増減額（△は減少額）、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-94340_IncreaseDecreaseInCustomerDepositsInBankingBusinessOpeCFIFRS',
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

def increase_decrease_in_loans_in_banking_business_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    銀行事業の貸付金の増減額(△は増加額)、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-94340_IncreaseDecreaseInLoansInBankingBusinessOpeCFIFRS',
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

def investment_securities_for_banking_business_ncaifrs(session: Session, head_item_key:str, context:str):
    """
    銀行事業の有価証券、非流動資産（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-94340_InvestmentSecuritiesForBankingBusinessNCAIFRS',
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

def loss_gain_on_change_in_equity_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    持分変動損益（△は益）、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-94340_LossGainOnChangeInEquityOpeCFIFRS',
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

def net_increase_decrease_in_cash_and_cash_equivalents_resulting_from_transfer_to_assets_as_held_for_sale_ifrs(session: Session, head_item_key:str, context:str):
    """
    売却目的保有に分類された資産への振替に伴う現金及び現金同等物の増減額(△は減少額)（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-94340_NetIncreaseDecreaseInCashAndCashEquivalentsResultingFromTransferToAssetsAsHeldForSaleIFRS',
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

def net_increase_decrease_in_short_term_interest_bearing_liabilities_fin_cfifrs(session: Session, head_item_key:str, context:str):
    """
    短期有利子負債の純増減額（△は減少額）、財務活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-94340_NetIncreaseDecreaseInShortTermInterestBearingLiabilitiesFinCFIFRS',
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

def proceeds_from_interst_bearing_debt_fin_cfifrs(session: Session, head_item_key:str, context:str):
    """
    有利子負債の収入、財務活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-94340_ProceedsFromInterstBearingDebtFinCFIFRS',
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

def proceeds_from_loss_of_control_of_subsidiaries_inv_cfifrs(session: Session, head_item_key:str, context:str):
    """
    子会社の支配喪失による収支（△は支出）、投資活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-94340_ProceedsFromLossOfControlOfSubsidiariesInvCFIFRS',
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

def proceeds_from_obtaining_control_of_subsidiaries_inv_cfifrs(session: Session, head_item_key:str, context:str):
    """
    子会社の支配獲得による収支（△は支出）、投資活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-94340_ProceedsFromObtainingControlOfSubsidiariesInvCFIFRS',
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

def proceeds_from_sales_of_investment_securities_in_banking_business_inv_cfifrs(session: Session, head_item_key:str, context:str):
    """
    銀行事業の有価証券の売却または償還による収入、投資活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-94340_ProceedsFromSalesOfInvestmentSecuritiesInBankingBusinessInvCFIFRS',
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

def purchase_of_investment_securities_in_banking_business_inv_cfifrs(session: Session, head_item_key:str, context:str):
    """
    銀行事業の有価証券の取得による支出、投資活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-94340_PurchaseOfInvestmentSecuritiesInBankingBusinessInvCFIFRS',
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

def purchases_of_mobile_devices_leased_to_enterprise_customers_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    法人向けレンタル用携帯端末の取得による支出、営業活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-94340_PurchasesOfMobileDevicesLeasedToEnterpriseCustomersOpeCFIFRS',
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

def repayment_of_interest_bearing_debt_fin_cfifrs(session: Session, head_item_key:str, context:str):
    """
    有利子負債の支出、財務活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-94340_RepaymentOfInterestBearingDebtFinCFIFRS',
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

def transfer_from_retained_earnings_to_capital_surplus_ifrs(session: Session, head_item_key:str, context:str):
    """
    利益剰余金から資本剰余金への振替（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-94340_TransferFromRetainedEarningsToCapitalSurplusIFRS',
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

def decrease_increase_in_consumption_taxes_refund_receivable_ope_cfifrs(session: Session, head_item_key:str, context:str):
    """
    未収消費税等の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS）（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-95170_DecreaseIncreaseInConsumptionTaxesRefundReceivableOpeCFIFRS',
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

def net_increase_decrease_in_short_term_borrowings_within3_months_fin_cfifrs(session: Session, head_item_key:str, context:str):
    """
    短期借入金（３ヶ月以内）の純増減額、財務活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-95170_NetIncreaseDecreaseInShortTermBorrowingsWithin3MonthsFinCFIFRS',
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

def proceeds_from_short_term_borrowings_over_three_months_fin_cfifrs(session: Session, head_item_key:str, context:str):
    """
    短期借入れ（３ヶ月超）による収入、財務活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-95170_ProceedsFromShortTermBorrowingsOverThreeMonthsFinCFIFRS',
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

def reduction_in_subsidiaries_without_sale_of_equity_interest_inv_cfifrs(session: Session, head_item_key:str, context:str):
    """
    持分の売却を伴わない子会社の減少、投資活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-95170_ReductionInSubsidiariesWithoutSaleOfEquityInterestInvCFIFRS',
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

def repayments_of_short_term_borrowings_over_three_months_fin_cfifrs(session: Session, head_item_key:str, context:str):
    """
    短期借入金（３ヶ月超）の返済による支出、財務活動によるキャッシュ・フロー（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-95170_RepaymentsOfShortTermBorrowingsOverThreeMonthsFinCFIFRS',
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

def transfer_to_non_financial_assets_etc_ifrsssifrs(session: Session, head_item_key:str, context:str):
    """
    非金融資産等への振替、持分変動計算書（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-95170_TransferToNonFinancialAssetsEtcIFRSSSIFRS',
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

def gain_on_loss_of_control_of_subsidiaries_ifrs(session: Session, head_item_key:str, context:str):
    """
    子会社の支配喪失に伴う利益（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-96580_GainOnLossOfControlOfSubsidiariesIFRS',
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

def loss_on_change_in_equity_ifrs(session: Session, head_item_key:str, context:str):
    """
    持分変動損失（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-96580_LossOnChangeInEquityIFRS',
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

def non_current_liability_for_stock_benefit_ifrs(session: Session, head_item_key:str, context:str):
    """
    株式報酬に係る負債、非流動負債（IFRS）
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'tse-scediffr-96580_NonCurrentLiabilityForStockBenefitIFRS',
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

