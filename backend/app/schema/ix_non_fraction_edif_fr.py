from app.models import Field, SQLModel
from app.schema.ix_non_fraction import IxNonFractionPublic
from typing import Optional

class IxNonFractionEdifFr(SQLModel):
    number_of_submission_dei: Optional[IxNonFractionPublic] = Field(default=None, description='提出回数、DEI')
    """ 提出回数、DEI """
    accrued_expenses_clifrs: Optional[IxNonFractionPublic] = Field(default=None, description='未払費用、流動負債（IFRS）')
    """ 未払費用、流動負債（IFRS） """
    accumulated_other_comprehensive_income_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='その他の包括利益累計額（IFRS）')
    """ その他の包括利益累計額（IFRS） """
    assets_held_for_sale_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='売却目的で保有する資産（IFRS）')
    """ 売却目的で保有する資産（IFRS） """
    assets_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='資産（IFRS）')
    """ 資産（IFRS） """
    basic_earnings_loss_per_share_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='基本的１株当たり当期利益（△損失）（IFRS）')
    """ 基本的１株当たり当期利益（△損失）（IFRS） """
    bonds_and_borrowings_clifrs: Optional[IxNonFractionPublic] = Field(default=None, description='社債及び借入金、流動負債（IFRS）')
    """ 社債及び借入金、流動負債（IFRS） """
    bonds_and_borrowings_liabilities_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='社債及び借入金、負債（IFRS）')
    """ 社債及び借入金、負債（IFRS） """
    bonds_and_borrowings_nclifrs: Optional[IxNonFractionPublic] = Field(default=None, description='社債及び借入金、非流動負債（IFRS）')
    """ 社債及び借入金、非流動負債（IFRS） """
    borrowings_clifrs: Optional[IxNonFractionPublic] = Field(default=None, description='借入金、流動負債（IFRS）')
    """ 借入金、流動負債（IFRS） """
    borrowings_nclifrs: Optional[IxNonFractionPublic] = Field(default=None, description='借入金、非流動負債（IFRS）')
    """ 借入金、非流動負債（IFRS） """
    cancellation_of_treasury_shares_ssifrs: Optional[IxNonFractionPublic] = Field(default=None, description='自己株式の消却、持分変動計算書（IFRS）')
    """ 自己株式の消却、持分変動計算書（IFRS） """
    capital_contribution_from_non_controlling_interests_fin_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='非支配持分からの払込による収入、財務活動によるキャッシュ・フロー（IFRS）')
    """ 非支配持分からの払込による収入、財務活動によるキャッシュ・フロー（IFRS） """
    capital_surplus_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='資本剰余金（IFRS）')
    """ 資本剰余金（IFRS） """
    cash_and_cash_equivalents_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='現金及び現金同等物（IFRS）')
    """ 現金及び現金同等物（IFRS） """
    cash_and_cash_equivalents_if_different_from_bs_balance_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='現金及び現金同等物（財政状態計算書と異なる場合にCFで用いる）（IFRS）')
    """ 現金及び現金同等物（財政状態計算書と異なる場合にCFで用いる）（IFRS） """
    change_in_scope_of_consolidation_ssifrs: Optional[IxNonFractionPublic] = Field(default=None, description='連結範囲の変動、持分変動計算書（IFRS）')
    """ 連結範囲の変動、持分変動計算書（IFRS） """
    changes_in_ownership_interest_in_subsidiaries_ssifrs: Optional[IxNonFractionPublic] = Field(default=None, description='支配継続子会社に対する持分変動、持分変動計算書（IFRS）')
    """ 支配継続子会社に対する持分変動、持分変動計算書（IFRS） """
    collection_of_loans_receivable_inv_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='貸付金の回収による収入、投資活動によるキャッシュ・フロー（IFRS）')
    """ 貸付金の回収による収入、投資活動によるキャッシュ・フロー（IFRS） """
    comprehensive_income_attributable_to_non_controlling_interests_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='非支配持分、当期包括利益（IFRS）')
    """ 非支配持分、当期包括利益（IFRS） """
    comprehensive_income_attributable_to_owners_of_parent_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='親会社の所有者、当期包括利益（IFRS）')
    """ 親会社の所有者、当期包括利益（IFRS） """
    comprehensive_income_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='当期包括利益（IFRS）')
    """ 当期包括利益（IFRS） """
    continuing_operations_basic_earnings_loss_per_share_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='継続事業、基本的１株当たり当期利益（△損失）（IFRS）')
    """ 継続事業、基本的１株当たり当期利益（△損失）（IFRS） """
    continuing_operations_diluted_earnings_loss_per_share_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='継続事業、希薄化後１株当たり当期利益（△損失）（IFRS）')
    """ 継続事業、希薄化後１株当たり当期利益（△損失）（IFRS） """
    contract_assets_caifrs: Optional[IxNonFractionPublic] = Field(default=None, description='契約資産、流動資産（IFRS）')
    """ 契約資産、流動資産（IFRS） """
    contract_assets_ncaifrs: Optional[IxNonFractionPublic] = Field(default=None, description='契約資産、非流動資産（IFRS）')
    """ 契約資産、非流動資産（IFRS） """
    contract_liabilities_clifrs: Optional[IxNonFractionPublic] = Field(default=None, description='契約負債、流動負債（IFRS）')
    """ 契約負債、流動負債（IFRS） """
    contract_liabilities_nclifrs: Optional[IxNonFractionPublic] = Field(default=None, description='契約負債、非流動負債（IFRS）')
    """ 契約負債、非流動負債（IFRS） """
    cost_of_sales_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='売上原価（IFRS）')
    """ 売上原価（IFRS） """
    cumulative_effect_of_accounting_change_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='会計方針の変更による累積的影響額（IFRS）')
    """ 会計方針の変更による累積的影響額（IFRS） """
    current_assets_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='流動資産（IFRS）')
    """ 流動資産（IFRS） """
    current_assets_other_than_assets_held_for_sale_caifrs: Optional[IxNonFractionPublic] = Field(default=None, description='売却目的で保有する資産を除く流動資産（IFRS）')
    """ 売却目的で保有する資産を除く流動資産（IFRS） """
    decrease_increase_in_contract_assets_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='契約資産の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS）')
    """ 契約資産の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS） """
    decrease_increase_in_inventories_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='棚卸資産の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS）')
    """ 棚卸資産の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS） """
    decrease_increase_in_retirement_benefit_asset_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='退職給付に係る資産の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS）')
    """ 退職給付に係る資産の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS） """
    decrease_increase_in_trade_and_other_receivables2_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='売上債権及びその他の債権の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS）')
    """ 売上債権及びその他の債権の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS） """
    decrease_increase_in_trade_and_other_receivables_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='営業債権及びその他の債権の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS）')
    """ 営業債権及びその他の債権の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS） """
    decrease_increase_in_trade_receivables2_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='売上債権の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS）')
    """ 売上債権の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS） """
    decrease_increase_in_trade_receivables_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='営業債権の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS）')
    """ 営業債権の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS） """
    deferred_income_clifrs: Optional[IxNonFractionPublic] = Field(default=None, description='繰延収益、流動負債（IFRS）')
    """ 繰延収益、流動負債（IFRS） """
    deferred_income_nclifrs: Optional[IxNonFractionPublic] = Field(default=None, description='繰延収益、非流動負債（IFRS）')
    """ 繰延収益、非流動負債（IFRS） """
    deferred_tax_assets_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='繰延税金資産（IFRS）')
    """ 繰延税金資産（IFRS） """
    deferred_tax_liabilities_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='繰延税金負債（IFRS）')
    """ 繰延税金負債（IFRS） """
    depreciation_and_amortization_of_intangible_assets_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='減価償却費及び無形資産償却費、営業活動によるキャッシュ・フロー（IFRS）')
    """ 減価償却費及び無形資産償却費、営業活動によるキャッシュ・フロー（IFRS） """
    depreciation_and_amortization_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='減価償却費及び償却費、営業活動によるキャッシュ・フロー（IFRS）')
    """ 減価償却費及び償却費、営業活動によるキャッシュ・フロー（IFRS） """
    depreciation_and_amortization_operating_expenses_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='減価償却費及び償却費、営業費用（IFRS）')
    """ 減価償却費及び償却費、営業費用（IFRS） """
    derivative_assets_caifrs: Optional[IxNonFractionPublic] = Field(default=None, description='デリバティブ資産、流動資産（IFRS）')
    """ デリバティブ資産、流動資産（IFRS） """
    derivative_assets_ncaifrs: Optional[IxNonFractionPublic] = Field(default=None, description='デリバティブ資産、非流動資産（IFRS）')
    """ デリバティブ資産、非流動資産（IFRS） """
    derivative_liabilities_clifrs: Optional[IxNonFractionPublic] = Field(default=None, description='デリバティブ負債、流動負債（IFRS）')
    """ デリバティブ負債、流動負債（IFRS） """
    derivative_liabilities_nclifrs: Optional[IxNonFractionPublic] = Field(default=None, description='デリバティブ負債、非流動負債（IFRS）')
    """ デリバティブ負債、非流動負債（IFRS） """
    diluted_earnings_loss_per_share_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='希薄化後１株当たり当期利益（△損失）（IFRS）')
    """ 希薄化後１株当たり当期利益（△損失）（IFRS） """
    discontinued_operations_basic_earnings_loss_per_share_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='非継続事業、基本的１株当たり当期利益（△損失）（IFRS）')
    """ 非継続事業、基本的１株当たり当期利益（△損失）（IFRS） """
    discontinued_operations_diluted_earnings_loss_per_share_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='非継続事業、希薄化後１株当たり当期利益（△損失）（IFRS）')
    """ 非継続事業、希薄化後１株当たり当期利益（△損失）（IFRS） """
    disposal_of_subsidiaries_ssifrs: Optional[IxNonFractionPublic] = Field(default=None, description='子会社の支配喪失に伴う変動、持分変動計算書（IFRS）')
    """ 子会社の支配喪失に伴う変動、持分変動計算書（IFRS） """
    disposal_of_treasury_shares_ssifrs: Optional[IxNonFractionPublic] = Field(default=None, description='自己株式の処分、持分変動計算書（IFRS）')
    """ 自己株式の処分、持分変動計算書（IFRS） """
    dividend_income_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='受取配当金、営業活動によるキャッシュ・フロー（IFRS）')
    """ 受取配当金、営業活動によるキャッシュ・フロー（IFRS） """
    dividends_paid_fin_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='配当金の支払額、財務活動によるキャッシュ・フロー（IFRS）')
    """ 配当金の支払額、財務活動によるキャッシュ・フロー（IFRS） """
    dividends_paid_to_non_controlling_interests_fin_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='非支配持分への配当金の支払額、財務活動によるキャッシュ・フロー（IFRS）')
    """ 非支配持分への配当金の支払額、財務活動によるキャッシュ・フロー（IFRS） """
    dividends_paid_to_owners_of_parent_fin_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='親会社の所有者への配当金の支払額、財務活動によるキャッシュ・フロー（IFRS）')
    """ 親会社の所有者への配当金の支払額、財務活動によるキャッシュ・フロー（IFRS） """
    dividends_received_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='配当金の受取額、営業活動によるキャッシュ・フロー（IFRS）')
    """ 配当金の受取額、営業活動によるキャッシュ・フロー（IFRS） """
    dividends_ssifrs: Optional[IxNonFractionPublic] = Field(default=None, description='配当金、持分変動計算書（IFRS）')
    """ 配当金、持分変動計算書（IFRS） """
    effect_of_exchange_rate_changes_on_cash_and_cash_equivalents_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='現金及び現金同等物の為替変動による影響（IFRS）')
    """ 現金及び現金同等物の為替変動による影響（IFRS） """
    effective_portion_of_cash_flow_hedges_net_of_tax_items_that_may_be_reclassified_to_profit_or_loss_ociifrs: Optional[IxNonFractionPublic] = Field(default=None, description='キャッシュ・フロー・ヘッジの有効部分（税引後）、純損益に振り替えられる可能性のあるその他の包括利益（IFRS）')
    """ キャッシュ・フロー・ヘッジの有効部分（税引後）、純損益に振り替えられる可能性のあるその他の包括利益（IFRS） """
    employee_benefits_nclifrs: Optional[IxNonFractionPublic] = Field(default=None, description='従業員給付、非流動負債（IFRS）')
    """ 従業員給付、非流動負債（IFRS） """
    equity_attributable_to_owners_of_parent_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='親会社の所有者に帰属する持分（IFRS）')
    """ 親会社の所有者に帰属する持分（IFRS） """
    equity_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='資本（IFRS）')
    """ 資本（IFRS） """
    exchange_differences_on_translation_of_foreign_operations_before_tax_items_that_may_be_reclassified_to_profit_or_loss_ociifrs: Optional[IxNonFractionPublic] = Field(default=None, description='在外営業活動体の外貨換算差額（税引前）、純損益に振り替えられる可能性のあるその他の包括利益（IFRS）')
    """ 在外営業活動体の外貨換算差額（税引前）、純損益に振り替えられる可能性のあるその他の包括利益（IFRS） """
    exchange_differences_on_translation_of_foreign_operations_net_of_tax_items_that_may_be_reclassified_to_profit_or_loss_ociifrs: Optional[IxNonFractionPublic] = Field(default=None, description='在外営業活動体の外貨換算差額（税引後）、純損益に振り替えられる可能性のあるその他の包括利益（IFRS）')
    """ 在外営業活動体の外貨換算差額（税引後）、純損益に振り替えられる可能性のあるその他の包括利益（IFRS） """
    exercise_of_share_acquisition_rights_ssifrs: Optional[IxNonFractionPublic] = Field(default=None, description='新株予約権の行使、持分変動計算書（IFRS）')
    """ 新株予約権の行使、持分変動計算書（IFRS） """
    finance_costs_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='金融費用（IFRS）')
    """ 金融費用（IFRS） """
    finance_costs_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='金融費用、営業活動によるキャッシュ・フロー（IFRS）')
    """ 金融費用、営業活動によるキャッシュ・フロー（IFRS） """
    finance_income_and_expenses_net_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='金融収益・費用（純額）（IFRS）')
    """ 金融収益・費用（純額）（IFRS） """
    finance_income_and_finance_costs_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='金融収益及び金融費用、営業活動によるキャッシュ・フロー（IFRS）')
    """ 金融収益及び金融費用、営業活動によるキャッシュ・フロー（IFRS） """
    finance_income_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='金融収益（IFRS）')
    """ 金融収益（IFRS） """
    finance_income_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='金融収益、営業活動によるキャッシュ・フロー（IFRS）')
    """ 金融収益、営業活動によるキャッシュ・フロー（IFRS） """
    financial_assets_measured_at_fair_value_through_other_comprehensive_income_net_of_tax_items_that_may_be_reclassified_to_profit_or_loss_ociifrs: Optional[IxNonFractionPublic] = Field(default=None, description='その他の包括利益を通じて公正価値で測定する金融資産（税引後）、純損益に振り替えられる可能性のあるその他の包括利益（IFRS）')
    """ その他の包括利益を通じて公正価値で測定する金融資産（税引後）、純損益に振り替えられる可能性のあるその他の包括利益（IFRS） """
    foreign_exchange_loss_gain_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='為替差損益（△は益）、営業活動によるキャッシュ・フロー（IFRS）')
    """ 為替差損益（△は益）、営業活動によるキャッシュ・フロー（IFRS） """
    forfeiture_of_share_acquisition_rights_ssifrs: Optional[IxNonFractionPublic] = Field(default=None, description='新株予約権の失効、持分変動計算書（IFRS）')
    """ 新株予約権の失効、持分変動計算書（IFRS） """
    gain_on_bargain_purchase_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='負ののれん発生益（IFRS）')
    """ 負ののれん発生益（IFRS） """
    general_and_administrative_expenses_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='一般管理費（IFRS）')
    """ 一般管理費（IFRS） """
    goodwill_and_intangible_assets_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='のれん及び無形資産（IFRS）')
    """ のれん及び無形資産（IFRS） """
    goodwill_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='のれん（IFRS）')
    """ のれん（IFRS） """
    gross_profit_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='売上総利益（IFRS）')
    """ 売上総利益（IFRS） """
    impairment_losses_plifrs: Optional[IxNonFractionPublic] = Field(default=None, description='減損損失、損益（IFRS）')
    """ 減損損失、損益（IFRS） """
    impairment_losses_reversal_of_impairment_losses_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='減損損失（又は戻入れ）、営業活動によるキャッシュ・フロー（IFRS）')
    """ 減損損失（又は戻入れ）、営業活動によるキャッシュ・フロー（IFRS） """
    income_tax_expense_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='法人所得税費用（IFRS）')
    """ 法人所得税費用（IFRS） """
    income_tax_expense_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='法人所得税費用、営業活動によるキャッシュ・フロー（IFRS）')
    """ 法人所得税費用、営業活動によるキャッシュ・フロー（IFRS） """
    income_taxes_items_that_will_not_be_reclassified_to_profit_or_loss_ociifrs: Optional[IxNonFractionPublic] = Field(default=None, description='法人所得税、純損益に振り替えられることのないその他の包括利益（IFRS）')
    """ 法人所得税、純損益に振り替えられることのないその他の包括利益（IFRS） """
    income_taxes_paid_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='法人所得税の支払額、営業活動によるキャッシュ・フロー（IFRS）')
    """ 法人所得税の支払額、営業活動によるキャッシュ・フロー（IFRS） """
    income_taxes_payable_clifrs: Optional[IxNonFractionPublic] = Field(default=None, description='未払法人所得税、流動負債（IFRS）')
    """ 未払法人所得税、流動負債（IFRS） """
    income_taxes_payable_liabilities_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='未払法人所得税、負債（IFRS）')
    """ 未払法人所得税、負債（IFRS） """
    income_taxes_receivable_caifrs: Optional[IxNonFractionPublic] = Field(default=None, description='未収法人所得税、流動資産（IFRS）')
    """ 未収法人所得税、流動資産（IFRS） """
    income_taxes_refund_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='法人所得税の還付額、営業活動によるキャッシュ・フロー（IFRS）')
    """ 法人所得税の還付額、営業活動によるキャッシュ・フロー（IFRS） """
    income_taxes_refund_paid_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='法人所得税の支払額又は還付額（△は支払）、営業活動によるキャッシュ・フロー（IFRS）')
    """ 法人所得税の支払額又は還付額（△は支払）、営業活動によるキャッシュ・フロー（IFRS） """
    increase_decrease_by_business_combination_ssifrs: Optional[IxNonFractionPublic] = Field(default=None, description='企業結合による変動、持分変動計算書（IFRS）')
    """ 企業結合による変動、持分変動計算書（IFRS） """
    increase_decrease_in_contract_liabilities_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='契約負債の増減額（△は減少）、営業活動によるキャッシュ・フロー（IFRS）')
    """ 契約負債の増減額（△は減少）、営業活動によるキャッシュ・フロー（IFRS） """
    increase_decrease_in_provisions_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー（IFRS）')
    """ 引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー（IFRS） """
    increase_decrease_in_retirement_benefit_liability_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='退職給付に係る負債の増減額（△は減少）、営業活動によるキャッシュ・フロー（IFRS）')
    """ 退職給付に係る負債の増減額（△は減少）、営業活動によるキャッシュ・フロー（IFRS） """
    increase_decrease_in_trade_and_other_payables2_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='仕入債務及びその他の債務の増減額（△は減少）、営業活動によるキャッシュ・フロー（IFRS）')
    """ 仕入債務及びその他の債務の増減額（△は減少）、営業活動によるキャッシュ・フロー（IFRS） """
    increase_decrease_in_trade_and_other_payables_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='営業債務及びその他の債務の増減額（△は減少）、営業活動によるキャッシュ・フロー（IFRS）')
    """ 営業債務及びその他の債務の増減額（△は減少）、営業活動によるキャッシュ・フロー（IFRS） """
    increase_decrease_in_trade_payables3_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='買入債務の増減額（△は減少）、営業活動によるキャッシュ・フロー（IFRS）')
    """ 買入債務の増減額（△は減少）、営業活動によるキャッシュ・フロー（IFRS） """
    increase_decrease_in_trade_payables_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='営業債務の増減額（△は減少）、営業活動によるキャッシュ・フロー（IFRS）')
    """ 営業債務の増減額（△は減少）、営業活動によるキャッシュ・フロー（IFRS） """
    increase_or_decrease_in_retirement_benefit_asset_or_liability_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='退職給付に係る資産及び負債の増減額、営業活動によるキャッシュ・フロー（IFRS）')
    """ 退職給付に係る資産及び負債の増減額、営業活動によるキャッシュ・フロー（IFRS） """
    intangible_assets_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='無形資産（IFRS）')
    """ 無形資産（IFRS） """
    interest_and_dividend_income_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='受取利息及び受取配当金、営業活動によるキャッシュ・フロー（IFRS）')
    """ 受取利息及び受取配当金、営業活動によるキャッシュ・フロー（IFRS） """
    interest_and_dividends_received_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='利息及び配当金の受取額、営業活動によるキャッシュ・フロー（IFRS）')
    """ 利息及び配当金の受取額、営業活動によるキャッシュ・フロー（IFRS） """
    interest_bearing_liabilities_clifrs: Optional[IxNonFractionPublic] = Field(default=None, description='有利子負債、流動負債（IFRS）')
    """ 有利子負債、流動負債（IFRS） """
    interest_bearing_liabilities_nclifrs: Optional[IxNonFractionPublic] = Field(default=None, description='有利子負債、非流動負債（IFRS）')
    """ 有利子負債、非流動負債（IFRS） """
    interest_expenses_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='支払利息、営業活動によるキャッシュ・フロー（IFRS）')
    """ 支払利息、営業活動によるキャッシュ・フロー（IFRS） """
    interest_income_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='受取利息、営業活動によるキャッシュ・フロー（IFRS）')
    """ 受取利息、営業活動によるキャッシュ・フロー（IFRS） """
    interest_paid_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='利息の支払額、営業活動によるキャッシュ・フロー（IFRS）')
    """ 利息の支払額、営業活動によるキャッシュ・フロー（IFRS） """
    interest_received_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='利息の受取額、営業活動によるキャッシュ・フロー（IFRS）')
    """ 利息の受取額、営業活動によるキャッシュ・フロー（IFRS） """
    intersegment_revenue_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='セグメント間の売上収益（IFRS）')
    """ セグメント間の売上収益（IFRS） """
    intersegment_sales_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='セグメント間の売上高（IFRS）')
    """ セグメント間の売上高（IFRS） """
    inventories_caifrs: Optional[IxNonFractionPublic] = Field(default=None, description='棚卸資産、流動資産（IFRS）')
    """ 棚卸資産、流動資産（IFRS） """
    investment_property_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='投資不動産（IFRS）')
    """ 投資不動産（IFRS） """
    investment_securities_ncaifrs: Optional[IxNonFractionPublic] = Field(default=None, description='投資有価証券、非流動資産（IFRS）')
    """ 投資有価証券、非流動資産（IFRS） """
    investments_accounted_for_using_equity_method_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='持分法による投資損益、IFRS')
    """ 持分法による投資損益、IFRS """
    issuance_of_new_shares_ssifrs: Optional[IxNonFractionPublic] = Field(default=None, description='新株の発行、持分変動計算書（IFRS）')
    """ 新株の発行、持分変動計算書（IFRS） """
    lease_liabilities_clifrs: Optional[IxNonFractionPublic] = Field(default=None, description='リース負債、流動負債（IFRS）')
    """ リース負債、流動負債（IFRS） """
    lease_liabilities_nclifrs: Optional[IxNonFractionPublic] = Field(default=None, description='リース負債、非流動負債（IFRS）')
    """ リース負債、非流動負債（IFRS） """
    liabilities_and_equity_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='負債及び資本（IFRS）')
    """ 負債及び資本（IFRS） """
    liabilities_directly_associated_with_assets_held_for_sale_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='売却目的で保有する資産に直接関連する負債（IFRS）')
    """ 売却目的で保有する資産に直接関連する負債（IFRS） """
    liabilities_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='負債（IFRS）')
    """ 負債（IFRS） """
    liabilities_other_than_liabilities_directly_associated_with_assets_held_for_sale_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='売却目的で保有する資産に直接関連する負債を除く負債（IFRS）')
    """ 売却目的で保有する資産に直接関連する負債を除く負債（IFRS） """
    long_term_debt_nclifrs: Optional[IxNonFractionPublic] = Field(default=None, description='長期債務、非流動負債（IFRS）')
    """ 長期債務、非流動負債（IFRS） """
    loss_gain_on_sale_and_retirement_of_fixed_assets_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='固定資産除売却損益（△は益）、営業活動によるキャッシュ・フロー（IFRS）')
    """ 固定資産除売却損益（△は益）、営業活動によるキャッシュ・フロー（IFRS） """
    loss_gain_on_sale_and_retirement_of_property_plant_and_equipment_and_intangible_assets_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='有形固定資産及び無形資産除売却損益（△は益）、営業活動によるキャッシュ・フロー（IFRS）')
    """ 有形固定資産及び無形資産除売却損益（△は益）、営業活動によるキャッシュ・フロー（IFRS） """
    loss_gain_on_sale_of_fixed_assets_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='固定資産売却損益（△は益）、営業活動によるキャッシュ・フロー（IFRS）')
    """ 固定資産売却損益（△は益）、営業活動によるキャッシュ・フロー（IFRS） """
    loss_gain_on_step_acquisition_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='段階取得に係る差損益（△は益）、営業活動によるキャッシュ・フロー（IFRS）')
    """ 段階取得に係る差損益（△は益）、営業活動によるキャッシュ・フロー（IFRS） """
    loss_gain_related_to_fixed_assets_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='固定資産に係る損益（△は益）、営業活動によるキャッシュ・フロー（IFRS）')
    """ 固定資産に係る損益（△は益）、営業活動によるキャッシュ・フロー（IFRS） """
    loss_on_retirement_of_fixed_assets_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='固定資産除却損、営業活動によるキャッシュ・フロー（IFRS）')
    """ 固定資産除却損、営業活動によるキャッシュ・フロー（IFRS） """
    net_cash_provided_by_used_in_financing_activities_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='財務活動によるキャッシュ・フロー（IFRS）')
    """ 財務活動によるキャッシュ・フロー（IFRS） """
    net_cash_provided_by_used_in_investing_activities_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='投資活動によるキャッシュ・フロー（IFRS）')
    """ 投資活動によるキャッシュ・フロー（IFRS） """
    net_cash_provided_by_used_in_operating_activities_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='営業活動によるキャッシュ・フロー（IFRS）')
    """ 営業活動によるキャッシュ・フロー（IFRS） """
    net_change_in_fair_value_of_equity_instruments_designated_as_measured_at_fair_value_through_other_comprehensive_income_before_tax_items_that_will_not_be_reclassified_to_profit_or_loss_ociifrs: Optional[IxNonFractionPublic] = Field(default=None, description='その他の包括利益を通じて公正価値で測定するものとして指定した資本性金融商品の公正価値の純変動額（税引前）、純損益に振り替えられることのないその他の包括利益（IFRS）')
    """ その他の包括利益を通じて公正価値で測定するものとして指定した資本性金融商品の公正価値の純変動額（税引前）、純損益に振り替えられることのないその他の包括利益（IFRS） """
    net_change_in_fair_value_of_equity_instruments_designated_as_measured_at_fair_value_through_other_comprehensive_income_net_of_tax_items_that_will_not_be_reclassified_to_profit_or_loss_ociifrs: Optional[IxNonFractionPublic] = Field(default=None, description='その他の包括利益を通じて公正価値で測定するものとして指定した資本性金融商品の公正価値の純変動額（税引後）、純損益に振り替えられることのないその他の包括利益（IFRS）')
    """ その他の包括利益を通じて公正価値で測定するものとして指定した資本性金融商品の公正価値の純変動額（税引後）、純損益に振り替えられることのないその他の包括利益（IFRS） """
    net_decrease_increase_in_time_deposits_inv_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='定期預金の純増減額（△は増加）、投資活動によるキャッシュ・フロー（IFRS）')
    """ 定期預金の純増減額（△は増加）、投資活動によるキャッシュ・フロー（IFRS） """
    net_decrease_increase_in_treasury_shares_fin_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='自己株式の純増減額（△は増加）、財務活動によるキャッシュ・フロー（IFRS）')
    """ 自己株式の純増減額（△は増加）、財務活動によるキャッシュ・フロー（IFRS） """
    net_increase_decrease_in_cash_and_cash_equivalents_before_effect_of_exchange_rate_changes_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='現金及び現金同等物の増減額（△は減少）（換算差額加算前）（IFRS）')
    """ 現金及び現金同等物の増減額（△は減少）（換算差額加算前）（IFRS） """
    net_increase_decrease_in_cash_and_cash_equivalents_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='現金及び現金同等物の増減額（△は減少）（IFRS）')
    """ 現金及び現金同等物の増減額（△は減少）（IFRS） """
    net_increase_decrease_in_short_term_borrowings_fin_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='短期借入金の純増減額（△は減少）、財務活動によるキャッシュ・フロー（IFRS）')
    """ 短期借入金の純増減額（△は減少）、財務活動によるキャッシュ・フロー（IFRS） """
    net_sales_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='売上高、IFRS')
    """ 売上高、IFRS """
    non_controlling_interests_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='非支配持分（IFRS）')
    """ 非支配持分（IFRS） """
    non_current_assets_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='非流動資産（IFRS）')
    """ 非流動資産（IFRS） """
    non_current_labilities_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='非流動負債（IFRS）')
    """ 非流動負債（IFRS） """
    operating_expenses_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='営業費用（IFRS）')
    """ 営業費用（IFRS） """
    operating_profit_loss_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='営業利益（△損失）（IFRS）')
    """ 営業利益（△損失）（IFRS） """
    other_assets_assets_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='その他の資産、資産（IFRS）')
    """ その他の資産、資産（IFRS） """
    other_changes_in_working_capital_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='その他、運転資本の増減、営業活動によるキャッシュ・フロー（IFRS）')
    """ その他、運転資本の増減、営業活動によるキャッシュ・フロー（IFRS） """
    other_components_of_equity_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='その他の資本の構成要素（IFRS）')
    """ その他の資本の構成要素（IFRS） """
    other_comprehensive_income_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='その他の包括利益（IFRS）')
    """ その他の包括利益（IFRS） """
    other_current_assets_caifrs: Optional[IxNonFractionPublic] = Field(default=None, description='その他の流動資産（IFRS）')
    """ その他の流動資産（IFRS） """
    other_current_liabilities_clifrs: Optional[IxNonFractionPublic] = Field(default=None, description='その他の流動負債（IFRS）')
    """ その他の流動負債（IFRS） """
    other_expenses_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='その他の費用（IFRS）')
    """ その他の費用（IFRS） """
    other_fin_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='その他、財務活動によるキャッシュ・フロー（IFRS）')
    """ その他、財務活動によるキャッシュ・フロー（IFRS） """
    other_financial_assets_assets_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='その他の金融資産、資産（IFRS）')
    """ その他の金融資産、資産（IFRS） """
    other_financial_assets_caifrs: Optional[IxNonFractionPublic] = Field(default=None, description='その他の金融資産、流動資産（IFRS）')
    """ その他の金融資産、流動資産（IFRS） """
    other_financial_assets_ncaifrs: Optional[IxNonFractionPublic] = Field(default=None, description='その他の金融資産、非流動資産（IFRS）')
    """ その他の金融資産、非流動資産（IFRS） """
    other_financial_liabilities_clifrs: Optional[IxNonFractionPublic] = Field(default=None, description='その他の金融負債、流動負債（IFRS）')
    """ その他の金融負債、流動負債（IFRS） """
    other_financial_liabilities_liabilities_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='その他の金融負債、負債（IFRS）')
    """ その他の金融負債、負債（IFRS） """
    other_financial_liabilities_nclifrs: Optional[IxNonFractionPublic] = Field(default=None, description='その他の金融負債、非流動負債（IFRS）')
    """ その他の金融負債、非流動負債（IFRS） """
    other_income_and_expenses_net_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='その他の収益・費用（純額）（IFRS）')
    """ その他の収益・費用（純額）（IFRS） """
    other_income_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='その他の収益（IFRS）')
    """ その他の収益（IFRS） """
    other_intangible_assets_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='その他の無形資産（IFRS）')
    """ その他の無形資産（IFRS） """
    other_inv_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='その他、投資活動によるキャッシュ・フロー（IFRS）')
    """ その他、投資活動によるキャッシュ・フロー（IFRS） """
    other_investments_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='その他の投資（IFRS）')
    """ その他の投資（IFRS） """
    other_liabilities_liabilities_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='その他の負債、負債（IFRS）')
    """ その他の負債、負債（IFRS） """
    other_non_current_assets_ncaifrs: Optional[IxNonFractionPublic] = Field(default=None, description='その他の非流動資産（IFRS）')
    """ その他の非流動資産（IFRS） """
    other_non_current_liabilities_nclifrs: Optional[IxNonFractionPublic] = Field(default=None, description='その他の非流動負債（IFRS）')
    """ その他の非流動負債（IFRS） """
    other_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='その他、営業活動によるキャッシュ・フロー（IFRS）')
    """ その他、営業活動によるキャッシュ・フロー（IFRS） """
    other_operating_expenses_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='その他の営業費用（IFRS）')
    """ その他の営業費用（IFRS） """
    other_operating_income_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='その他の営業収益（IFRS）')
    """ その他の営業収益（IFRS） """
    other_ssifrs: Optional[IxNonFractionPublic] = Field(default=None, description='その他、持分変動計算書（IFRS）')
    """ その他、持分変動計算書（IFRS） """
    payments_for_acquisition_of_businesses_inv_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='事業譲受による支出、投資活動によるキャッシュ・フロー（IFRS）')
    """ 事業譲受による支出、投資活動によるキャッシュ・フロー（IFRS） """
    payments_for_acquisition_of_interests_in_subsidiaries_from_non_controlling_interests_fin_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='非支配持分からの子会社持分取得による支出、財務活動によるキャッシュ・フロー（IFRS）')
    """ 非支配持分からの子会社持分取得による支出、財務活動によるキャッシュ・フロー（IFRS） """
    payments_for_acquisition_of_subsidiaries_inv_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='子会社の取得による支出、投資活動によるキャッシュ・フロー（IFRS）')
    """ 子会社の取得による支出、投資活動によるキャッシュ・フロー（IFRS） """
    payments_for_leasehold_deposits_and_guarantee_deposits_inv_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='敷金及び保証金の差入による支出、投資活動によるキャッシュ・フロー（IFRS）')
    """ 敷金及び保証金の差入による支出、投資活動によるキャッシュ・フロー（IFRS） """
    payments_for_loans_receivable_inv_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='貸付けによる支出、投資活動によるキャッシュ・フロー（IFRS）')
    """ 貸付けによる支出、投資活動によるキャッシュ・フロー（IFRS） """
    payments_for_purchase_of_treasury_shares_fin_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='自己株式の取得による支出、財務活動によるキャッシュ・フロー（IFRS）')
    """ 自己株式の取得による支出、財務活動によるキャッシュ・フロー（IFRS） """
    payments_into_time_deposits_inv_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='定期預金の預入による支出、投資活動によるキャッシュ・フロー（IFRS）')
    """ 定期預金の預入による支出、投資活動によるキャッシュ・フロー（IFRS） """
    proceeds_from_changes_in_ownership_interests_in_subsidiaries_that_do_not_result_in_loss_of_control_fin_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='非支配持分への子会社持分売却による収入、財務活動によるキャッシュ・フロー（IFRS）')
    """ 非支配持分への子会社持分売却による収入、財務活動によるキャッシュ・フロー（IFRS） """
    proceeds_from_collection_of_leasehold_deposits_and_guarantee_deposits_inv_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='敷金及び保証金の回収による収入、投資活動によるキャッシュ・フロー（IFRS）')
    """ 敷金及び保証金の回収による収入、投資活動によるキャッシュ・フロー（IFRS） """
    proceeds_from_exercise_of_share_acquisition_rights_fin_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='新株予約権の行使による収入、財務活動によるキャッシュ・フロー（IFRS）')
    """ 新株予約権の行使による収入、財務活動によるキャッシュ・フロー（IFRS） """
    proceeds_from_issuance_of_bonds_and_long_term_borrowings_fin_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='社債の発行及び長期借入れによる収入、財務活動によるキャッシュ・フロー（IFRS）')
    """ 社債の発行及び長期借入れによる収入、財務活動によるキャッシュ・フロー（IFRS） """
    proceeds_from_issuance_of_bonds_fin_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='社債の発行による収入、財務活動によるキャッシュ・フロー（IFRS）')
    """ 社債の発行による収入、財務活動によるキャッシュ・フロー（IFRS） """
    proceeds_from_issuance_of_shares_fin_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='株式の発行による収入、財務活動によるキャッシュ・フロー（IFRS）')
    """ 株式の発行による収入、財務活動によるキャッシュ・フロー（IFRS） """
    proceeds_from_long_term_borrowings_fin_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='長期借入れによる収入、財務活動によるキャッシュ・フロー（IFRS）')
    """ 長期借入れによる収入、財務活動によるキャッシュ・フロー（IFRS） """
    proceeds_from_sale_of_businesses_inv_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='事業譲渡による収入、投資活動によるキャッシュ・フロー（IFRS）')
    """ 事業譲渡による収入、投資活動によるキャッシュ・フロー（IFRS） """
    proceeds_from_sale_of_equity_instruments_inv_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='資本性金融商品の売却による収入、投資活動によるキャッシュ・フロー（IFRS）')
    """ 資本性金融商品の売却による収入、投資活動によるキャッシュ・フロー（IFRS） """
    proceeds_from_sale_of_intangible_assets_inv_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='無形資産の売却による収入、投資活動によるキャッシュ・フロー（IFRS）')
    """ 無形資産の売却による収入、投資活動によるキャッシュ・フロー（IFRS） """
    proceeds_from_sale_of_investment_securities_inv_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='投資有価証券の売却による収入、投資活動によるキャッシュ・フロー（IFRS）')
    """ 投資有価証券の売却による収入、投資活動によるキャッシュ・フロー（IFRS） """
    proceeds_from_sale_of_investments_inv_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='投資の売却及び償還による収入、投資活動によるキャッシュ・フロー（IFRS）')
    """ 投資の売却及び償還による収入、投資活動によるキャッシュ・フロー（IFRS） """
    proceeds_from_sale_of_marketable_securities_inv_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='有価証券の売却による収入、投資活動によるキャッシュ・フロー（IFRS）')
    """ 有価証券の売却による収入、投資活動によるキャッシュ・フロー（IFRS） """
    proceeds_from_sale_of_other_financial_assets_inv_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='その他の金融資産の売却による収入、投資活動によるキャッシュ・フロー（IFRS）')
    """ その他の金融資産の売却による収入、投資活動によるキャッシュ・フロー（IFRS） """
    proceeds_from_sale_of_property_plant_and_equipment_and_intangible_assets_inv_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='有形固定資産及び無形資産の売却による収入、投資活動によるキャッシュ・フロー（IFRS）')
    """ 有形固定資産及び無形資産の売却による収入、投資活動によるキャッシュ・フロー（IFRS） """
    proceeds_from_sale_of_property_plant_and_equipment_inv_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='有形固定資産の売却による収入、投資活動によるキャッシュ・フロー（IFRS）')
    """ 有形固定資産の売却による収入、投資活動によるキャッシュ・フロー（IFRS） """
    proceeds_from_sale_of_subsidiaries_inv_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='子会社の売却による収入、投資活動によるキャッシュ・フロー（IFRS）')
    """ 子会社の売却による収入、投資活動によるキャッシュ・フロー（IFRS） """
    proceeds_from_sale_of_treasury_shares_fin_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='自己株式の売却による収入、財務活動によるキャッシュ・フロー（IFRS）')
    """ 自己株式の売却による収入、財務活動によるキャッシュ・フロー（IFRS） """
    proceeds_from_short_term_borrowings_fin_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='短期借入れによる収入、財務活動によるキャッシュ・フロー（IFRS）')
    """ 短期借入れによる収入、財務活動によるキャッシュ・フロー（IFRS） """
    proceeds_from_withdrawal_of_time_deposits_inv_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='定期預金の払戻による収入、投資活動によるキャッシュ・フロー（IFRS）')
    """ 定期預金の払戻による収入、投資活動によるキャッシュ・フロー（IFRS） """
    profit_loss_attributable_to_non_controlling_interests_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='非支配持分、当期利益（△損失）（IFRS）')
    """ 非支配持分、当期利益（△損失）（IFRS） """
    profit_loss_attributable_to_owners_of_parent_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='親会社の所有者、当期利益（△損失）（IFRS）')
    """ 親会社の所有者、当期利益（△損失）（IFRS） """
    profit_loss_before_tax_from_discontinued_operations_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='非継続事業からの税引前利益（△損失）（IFRS）')
    """ 非継続事業からの税引前利益（△損失）（IFRS） """
    profit_loss_before_tax_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='継続事業からの税引前利益（△損失）（IFRS）')
    """ 継続事業からの税引前利益（△損失）（IFRS） """
    profit_loss_from_continuing_operations_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='継続事業からの当期利益（△損失）（IFRS）')
    """ 継続事業からの当期利益（△損失）（IFRS） """
    profit_loss_from_discontinued_operations_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='非継続事業からの当期利益（△損失）（IFRS）')
    """ 非継続事業からの当期利益（△損失）（IFRS） """
    profit_loss_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='当期利益（△損失）（IFRS）')
    """ 当期利益（△損失）（IFRS） """
    property_plant_and_equipment_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='有形固定資産（IFRS）')
    """ 有形固定資産（IFRS） """
    provisions_clifrs: Optional[IxNonFractionPublic] = Field(default=None, description='引当金、流動負債（IFRS）')
    """ 引当金、流動負債（IFRS） """
    provisions_liabilities_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='引当金、負債（IFRS）')
    """ 引当金、負債（IFRS） """
    provisions_nclifrs: Optional[IxNonFractionPublic] = Field(default=None, description='引当金、非流動負債（IFRS）')
    """ 引当金、非流動負債（IFRS） """
    purchase_and_disposal_of_treasury_shares_ssifrs: Optional[IxNonFractionPublic] = Field(default=None, description='自己株式の取得及び処分、持分変動計算書（IFRS）')
    """ 自己株式の取得及び処分、持分変動計算書（IFRS） """
    purchase_of_equity_instruments_inv_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='資本性金融商品の取得による支出、投資活動によるキャッシュ・フロー（IFRS）')
    """ 資本性金融商品の取得による支出、投資活動によるキャッシュ・フロー（IFRS） """
    purchase_of_intangible_assets_inv_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='無形資産の取得による支出、投資活動によるキャッシュ・フロー（IFRS）')
    """ 無形資産の取得による支出、投資活動によるキャッシュ・フロー（IFRS） """
    purchase_of_investment_property_inv_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='投資不動産の取得による支出、投資活動によるキャッシュ・フロー（IFRS）')
    """ 投資不動産の取得による支出、投資活動によるキャッシュ・フロー（IFRS） """
    purchase_of_investment_securities_inv_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='投資有価証券の取得による支出、投資活動によるキャッシュ・フロー（IFRS）')
    """ 投資有価証券の取得による支出、投資活動によるキャッシュ・フロー（IFRS） """
    purchase_of_investments_accounted_for_using_equity_method_inv_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='持分法で会計処理されている投資の取得による支出、投資活動によるキャッシュ・フロー（IFRS）')
    """ 持分法で会計処理されている投資の取得による支出、投資活動によるキャッシュ・フロー（IFRS） """
    purchase_of_investments_inv_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='投資の取得による支出、投資活動によるキャッシュ・フロー（IFRS）')
    """ 投資の取得による支出、投資活動によるキャッシュ・フロー（IFRS） """
    purchase_of_marketable_securities_inv_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='有価証券の取得による支出、投資活動によるキャッシュ・フロー（IFRS）')
    """ 有価証券の取得による支出、投資活動によるキャッシュ・フロー（IFRS） """
    purchase_of_other_financial_assets_inv_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='その他の金融資産の取得による支出、投資活動によるキャッシュ・フロー（IFRS）')
    """ その他の金融資産の取得による支出、投資活動によるキャッシュ・フロー（IFRS） """
    purchase_of_other_investments_inv_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='その他の投資の取得による支出、投資活動によるキャッシュ・フロー（IFRS）')
    """ その他の投資の取得による支出、投資活動によるキャッシュ・フロー（IFRS） """
    purchase_of_property_plant_and_equipment_and_intangible_assets_inv_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='有形固定資産及び無形資産の取得による支出、投資活動によるキャッシュ・フロー（IFRS）')
    """ 有形固定資産及び無形資産の取得による支出、投資活動によるキャッシュ・フロー（IFRS） """
    purchase_of_property_plant_and_equipment_inv_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='有形固定資産の取得による支出、投資活動によるキャッシュ・フロー（IFRS）')
    """ 有形固定資産の取得による支出、投資活動によるキャッシュ・フロー（IFRS） """
    purchase_of_treasury_shares_ssifrs: Optional[IxNonFractionPublic] = Field(default=None, description='自己株式の取得、持分変動計算書（IFRS）')
    """ 自己株式の取得、持分変動計算書（IFRS） """
    redemption_of_bonds_and_repayments_of_long_term_borrowings_fin_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='社債の償還及び長期借入金の返済、財務活動によるキャッシュ・フロー（IFRS）')
    """ 社債の償還及び長期借入金の返済、財務活動によるキャッシュ・フロー（IFRS） """
    redemption_of_bonds_fin_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='社債の償還による支出、財務活動によるキャッシュ・フロー（IFRS）')
    """ 社債の償還による支出、財務活動によるキャッシュ・フロー（IFRS） """
    remeasurements_of_defined_benefit_plans_before_tax_items_that_will_not_be_reclassified_to_profit_or_loss_ociifrs: Optional[IxNonFractionPublic] = Field(default=None, description='確定給付制度の再測定（税引前）、純損益に振り替えられることのないその他の包括利益（IFRS）')
    """ 確定給付制度の再測定（税引前）、純損益に振り替えられることのないその他の包括利益（IFRS） """
    remeasurements_of_defined_benefit_plans_net_of_tax_items_that_will_not_be_reclassified_to_profit_or_loss_ociifrs: Optional[IxNonFractionPublic] = Field(default=None, description='確定給付制度の再測定（税引後）、純損益に振り替えられることのないその他の包括利益（IFRS）')
    """ 確定給付制度の再測定（税引後）、純損益に振り替えられることのないその他の包括利益（IFRS） """
    repayments_of_lease_obligations_fin_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='リース負債の返済による支出、財務活動によるキャッシュ・フロー（IFRS）')
    """ リース負債の返済による支出、財務活動によるキャッシュ・フロー（IFRS） """
    repayments_of_long_term_borrowings_fin_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='長期借入金の返済による支出、財務活動によるキャッシュ・フロー（IFRS）')
    """ 長期借入金の返済による支出、財務活動によるキャッシュ・フロー（IFRS） """
    repayments_of_short_term_borrowings_fin_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='短期借入金の返済による支出、財務活動によるキャッシュ・フロー（IFRS）')
    """ 短期借入金の返済による支出、財務活動によるキャッシュ・フロー（IFRS） """
    research_and_development_expenditure_recognized_as_expense_during_period_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='当期に費用認識した研究開発費（IFRS）')
    """ 当期に費用認識した研究開発費（IFRS） """
    restated_balance_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='会計方針の変更を反映した当期首残高（IFRS）')
    """ 会計方針の変更を反映した当期首残高（IFRS） """
    retained_earnings_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='利益剰余金（IFRS）')
    """ 利益剰余金（IFRS） """
    retirement_benefit_asset_ncaifrs: Optional[IxNonFractionPublic] = Field(default=None, description='退職給付に係る資産、非流動資産（IFRS）')
    """ 退職給付に係る資産、非流動資産（IFRS） """
    retirement_benefit_liability_nclifrs: Optional[IxNonFractionPublic] = Field(default=None, description='退職給付に係る負債、非流動負債（IFRS）')
    """ 退職給付に係る負債、非流動負債（IFRS） """
    revenue2_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='収益（IFRS）')
    """ 収益（IFRS） """
    revenue_from_external_customers_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='外部顧客への売上収益（IFRS）')
    """ 外部顧客への売上収益（IFRS） """
    revenue_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='売上収益（IFRS）')
    """ 売上収益（IFRS） """
    right_of_use_assets_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='使用権資産（IFRS）')
    """ 使用権資産（IFRS） """
    sales_to_external_customers_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='外部顧客への売上高（IFRS）')
    """ 外部顧客への売上高（IFRS） """
    segment_profit_loss_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='セグメント利益（△損失）（IFRS）')
    """ セグメント利益（△損失）（IFRS） """
    selling_expenses_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='販売費（IFRS）')
    """ 販売費（IFRS） """
    selling_general_and_administrative_expenses_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='販売費及び一般管理費（IFRS）')
    """ 販売費及び一般管理費（IFRS） """
    share_based_payment_expenses_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='株式報酬費用、営業活動によるキャッシュ・フロー（IFRS）')
    """ 株式報酬費用、営業活動によるキャッシュ・フロー（IFRS） """
    share_based_payment_transactions_ssifrs: Optional[IxNonFractionPublic] = Field(default=None, description='株式報酬取引、持分変動計算書（IFRS）')
    """ 株式報酬取引、持分変動計算書（IFRS） """
    share_capital_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='資本金（IFRS）')
    """ 資本金（IFRS） """
    share_of_loss_profit_of_investments_accounted_for_using_equity_method_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='持分法による投資損益（△は益）、営業活動によるキャッシュ・フロー（IFRS）')
    """ 持分法による投資損益（△は益）、営業活動によるキャッシュ・フロー（IFRS） """
    share_of_other_comprehensive_income_of_investments_accounted_for_using_equity_method_net_of_tax_items_that_may_be_reclassified_to_profit_or_loss_ociifrs: Optional[IxNonFractionPublic] = Field(default=None, description='持分法によるその他の包括利益（税引後）、純損益に振り替えられる可能性のあるその他の包括利益（IFRS）')
    """ 持分法によるその他の包括利益（税引後）、純損益に振り替えられる可能性のあるその他の包括利益（IFRS） """
    share_of_other_comprehensive_income_of_investments_accounted_for_using_equity_method_net_of_tax_items_that_will_not_be_reclassified_to_profit_or_loss_ociifrs: Optional[IxNonFractionPublic] = Field(default=None, description='持分法によるその他の包括利益（税引後）、純損益に振り替えられることのないその他の包括利益（IFRS）')
    """ 持分法によるその他の包括利益（税引後）、純損益に振り替えられることのないその他の包括利益（IFRS） """
    share_of_profit_loss_of_investments_accounted_for_using_equity_method_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='持分法による投資損益（△は損失）（IFRS）')
    """ 持分法による投資損益（△は損失）（IFRS） """
    subtotal_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='小計、営業活動によるキャッシュ・フロー（IFRS）')
    """ 小計、営業活動によるキャッシュ・フロー（IFRS） """
    time_deposits_caifrs: Optional[IxNonFractionPublic] = Field(default=None, description='定期預金、流動資産（IFRS）')
    """ 定期預金、流動資産（IFRS） """
    total_changes_in_equity_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='変動額合計（IFRS）')
    """ 変動額合計（IFRS） """
    total_current_liabilities_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='流動負債（IFRS）')
    """ 流動負債（IFRS） """
    total_of_items_that_may_be_reclassified_to_profit_or_loss_ociifrs: Optional[IxNonFractionPublic] = Field(default=None, description='純損益に振り替えられる可能性のある項目合計（IFRS）')
    """ 純損益に振り替えられる可能性のある項目合計（IFRS） """
    total_of_items_that_will_not_be_reclassified_to_profit_or_loss_ociifrs: Optional[IxNonFractionPublic] = Field(default=None, description='純損益に振り替えられることのない項目合計（IFRS）')
    """ 純損益に振り替えられることのない項目合計（IFRS） """
    total_transactions_with_owners_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='所有者との取引額（IFRS）')
    """ 所有者との取引額（IFRS） """
    trade_and_other_payables2_clifrs: Optional[IxNonFractionPublic] = Field(default=None, description='仕入債務及びその他の債務、流動負債（IFRS）')
    """ 仕入債務及びその他の債務、流動負債（IFRS） """
    trade_and_other_payables2_nclifrs: Optional[IxNonFractionPublic] = Field(default=None, description='仕入債務及びその他の債務、非流動負債（IFRS）')
    """ 仕入債務及びその他の債務、非流動負債（IFRS） """
    trade_and_other_payables_clifrs: Optional[IxNonFractionPublic] = Field(default=None, description='営業債務及びその他の債務、流動負債（IFRS）')
    """ 営業債務及びその他の債務、流動負債（IFRS） """
    trade_and_other_payables_liabilities_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='営業債務及びその他の債務、負債（IFRS）')
    """ 営業債務及びその他の債務、負債（IFRS） """
    trade_and_other_payables_nclifrs: Optional[IxNonFractionPublic] = Field(default=None, description='営業債務及びその他の債務、非流動負債（IFRS）')
    """ 営業債務及びその他の債務、非流動負債（IFRS） """
    trade_and_other_receivables2_caifrs: Optional[IxNonFractionPublic] = Field(default=None, description='売上債権及びその他の債権、流動資産（IFRS）')
    """ 売上債権及びその他の債権、流動資産（IFRS） """
    trade_and_other_receivables_assets_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='営業債権及びその他の債権、資産（IFRS）')
    """ 営業債権及びその他の債権、資産（IFRS） """
    trade_and_other_receivables_caifrs: Optional[IxNonFractionPublic] = Field(default=None, description='営業債権及びその他の債権、流動資産（IFRS）')
    """ 営業債権及びその他の債権、流動資産（IFRS） """
    trade_and_other_receivables_ncaifrs: Optional[IxNonFractionPublic] = Field(default=None, description='営業債権及びその他の債権、非流動資産（IFRS）')
    """ 営業債権及びその他の債権、非流動資産（IFRS） """
    trade_payables3_clifrs: Optional[IxNonFractionPublic] = Field(default=None, description='買入債務、流動負債（IFRS）')
    """ 買入債務、流動負債（IFRS） """
    trade_payables_clifrs: Optional[IxNonFractionPublic] = Field(default=None, description='営業債務、流動負債（IFRS）')
    """ 営業債務、流動負債（IFRS） """
    trade_receivables2_caifrs: Optional[IxNonFractionPublic] = Field(default=None, description='売上債権、流動資産（IFRS）')
    """ 売上債権、流動資産（IFRS） """
    trade_receivables_caifrs: Optional[IxNonFractionPublic] = Field(default=None, description='営業債権、流動資産（IFRS）')
    """ 営業債権、流動資産（IFRS） """
    transfer_from_accumulated_other_comprehensive_income_to_retained_earnings_ssifrs: Optional[IxNonFractionPublic] = Field(default=None, description='その他の包括利益累計額から利益剰余金への振替、持分変動計算書（IFRS）')
    """ その他の包括利益累計額から利益剰余金への振替、持分変動計算書（IFRS） """
    transfer_from_other_components_of_equity_to_retained_earnings_ssifrs: Optional[IxNonFractionPublic] = Field(default=None, description='その他の資本の構成要素から利益剰余金への振替、持分変動計算書（IFRS）')
    """ その他の資本の構成要素から利益剰余金への振替、持分変動計算書（IFRS） """
    transfer_ssifrs: Optional[IxNonFractionPublic] = Field(default=None, description='振替、持分変動計算書（IFRS）')
    """ 振替、持分変動計算書（IFRS） """
    transfer_to_retained_earnings_ssifrs: Optional[IxNonFractionPublic] = Field(default=None, description='利益剰余金への振替、持分変動計算書（IFRS）')
    """ 利益剰余金への振替、持分変動計算書（IFRS） """
    treasury_shares_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='自己株式（IFRS）')
    """ 自己株式（IFRS） """
    amount_of_rent_offset_by_lease_and_guarantee_deposits_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='敷金及び保証金の家賃相殺額、営業活動によるキャッシュ・フロー（IFRS）')
    """ 敷金及び保証金の家賃相殺額、営業活動によるキャッシュ・フロー（IFRS） """
    increase_decrease_in_provision_for_bonuses_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='賞与引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー（IFRS）')
    """ 賞与引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー（IFRS） """
    lease_and_guarantee_deposits_ncaifrs: Optional[IxNonFractionPublic] = Field(default=None, description='敷金及び保証金、非流動資産（IFRS）')
    """ 敷金及び保証金、非流動資産（IFRS） """
    net_change_in_fair_value_of_instruments_measured_at_fair_value_through_other_comprehensive_income_items_that_will_not_be_reclassified_to_profit_or_loss_ociifrs: Optional[IxNonFractionPublic] = Field(default=None, description='その他の包括利益を通じて測定する金融資産の公正価値の純変動、純損益に振り替えられることのないその他の包括利益（IFRS）')
    """ その他の包括利益を通じて測定する金融資産の公正価値の純変動、純損益に振り替えられることのないその他の包括利益（IFRS） """
    payments_for_commission_fees_fin_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='支払手数料の支払による支出、財務活動によるキャッシュ・フロー（IFRS）')
    """ 支払手数料の支払による支出、財務活動によるキャッシュ・フロー（IFRS） """
    accrued_labor_expenses_clifrs: Optional[IxNonFractionPublic] = Field(default=None, description='未払人件費、流動負債（IFRS）')
    """ 未払人件費、流動負債（IFRS） """
    changes_in_put_option_liabilities_related_to_non_controlling_interests_ssifrs: Optional[IxNonFractionPublic] = Field(default=None, description='非支配株主に係る売建プット・オプション負債の変動等、持分変動計算書（IFRS）')
    """ 非支配株主に係る売建プット・オプション負債の変動等、持分変動計算書（IFRS） """
    increase_decrease_in_accrued_consumption_taxes_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='未払消費税等の増減額（△は減少）、営業活動によるキャッシュ・フロー（IFRS）')
    """ 未払消費税等の増減額（△は減少）、営業活動によるキャッシュ・フロー（IFRS） """
    increase_decrease_in_accrued_labor_expenses_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='未払人件費の増減額（△は減少）、営業活動によるキャッシュ・フロー（IFRS）')
    """ 未払人件費の増減額（△は減少）、営業活動によるキャッシュ・フロー（IFRS） """
    increase_decrease_in_lease_receivables_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='リース債権の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS）')
    """ リース債権の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS） """
    increase_decrease_in_prepaid_expenses_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='前払費用の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS）')
    """ 前払費用の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS） """
    core_operating_profit_loss_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='事業利益（△損失）（IFRS）')
    """ 事業利益（△損失）（IFRS） """
    current_portion_of_bonds_clifrs: Optional[IxNonFractionPublic] = Field(default=None, description='1年内償還社債、流動負債（IFRS）')
    """ 1年内償還社債、流動負債（IFRS） """
    hedging_cost_net_of_tax_items_that_may_be_reclassified_to_profit_or_loss_ociifrs: Optional[IxNonFractionPublic] = Field(default=None, description='ヘッジコスト（税引後）、純損益に振替えられる可能性のあるその他の包括利益（IFRS）')
    """ ヘッジコスト（税引後）、純損益に振替えられる可能性のあるその他の包括利益（IFRS） """
    income_by_settlement_in_derivatives_fin_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='デリバティブの決済による収入、財務活動によるキャッシュ・フロー（IFRS）')
    """ デリバティブの決済による収入、財務活動によるキャッシュ・フロー（IFRS） """
    operating_income_loss_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='事業利益（△は損失）（IFRS）')
    """ 事業利益（△は損失）（IFRS） """
    proceeds_from_sale_and_redemption_of_other_financial_assets_inv_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='その他の金融資産の売却及び償還による収入、投資活動によるキャッシュ・フロー（IFRS）')
    """ その他の金融資産の売却及び償還による収入、投資活動によるキャッシュ・フロー（IFRS） """
    purchase_of_shares_of_subsidiaries_resulting_in_no_change_in_scope_of_consolidation_fin_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='連結範囲の変更を伴わない子会社株式の取得による支出、財務活動によるキャッシュ・フロー（IFRS）')
    """ 連結範囲の変更を伴わない子会社株式の取得による支出、財務活動によるキャッシュ・フロー（IFRS） """
    transfer_to_non_financial_assets_ssifrs: Optional[IxNonFractionPublic] = Field(default=None, description='非金融資産等への振替、持分変動計算書（IFRS）')
    """ 非金融資産等への振替、持分変動計算書（IFRS） """
    decrease_increase_in_advance_payments_to_suppliers_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='前渡金の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS）')
    """ 前渡金の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS） """
    increase_decrease_in_bonus_payable_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='未払賞与の増減額(△は減少)、営業活動によるキャッシュ・フロー（IFRS）')
    """ 未払賞与の増減額(△は減少)、営業活動によるキャッシュ・フロー（IFRS） """
    increase_decrease_in_consumption_tax_payable_etc_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='未払消費税等の増減額(△は減少)、営業活動によるキャッシュ・フロー（IFRS）')
    """ 未払消費税等の増減額(△は減少)、営業活動によるキャッシュ・フロー（IFRS） """
    purchase_of_treasury_shares_of_subsidiaries_fin_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='子会社の自己株式の取得による支出、財務活動によるキャッシュ・フロー（IFRS）')
    """ 子会社の自己株式の取得による支出、財務活動によるキャッシュ・フロー（IFRS） """
    tra_changes_in_ownership_interest_in_subsidiaries_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='非支配株主との取引に係る親会社の持分変動（IFRS）')
    """ 非支配株主との取引に係る親会社の持分変動（IFRS） """
    businessprofit_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='事業利益（IFRS）')
    """ 事業利益（IFRS） """
    cash_and_cash_equivalents_included_in_assets_of_disposal_groups_classified_as_for_sale_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='売却目的保有に分類される処分グループに係る資産に含まれる現金及び現金同等物、キャッシュ・フロー計算書（IFRS）')
    """ 売却目的保有に分類される処分グループに係る資産に含まれる現金及び現金同等物、キャッシュ・フロー計算書（IFRS） """
    transfer_to_capital_surplus_ssifrs: Optional[IxNonFractionPublic] = Field(default=None, description='資本剰余金への振替、持分変動計算書（IFRS）')
    """ 資本剰余金への振替、持分変動計算書（IFRS） """
    collection_of_loans_receivable_from_associates_inv_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='関連会社に対する貸付金の回収、投資活動によるキャッシュ・フロー（IFRS）')
    """ 関連会社に対する貸付金の回収、投資活動によるキャッシュ・フロー（IFRS） """
    decrease_increase_in_finance_receivables_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='金融債権の減少(△増加)、営業活動によるキャッシュ・フロー（IFRS）')
    """ 金融債権の減少(△増加)、営業活動によるキャッシュ・フロー（IFRS） """
    decrease_increase_in_other_assets_ifrs_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='その他資産の減少(△増加)（IFRS）、営業活動によるキャッシュ・フロー（IFRS）')
    """ その他資産の減少(△増加)（IFRS）、営業活動によるキャッシュ・フロー（IFRS） """
    financial_receivables_caifrs: Optional[IxNonFractionPublic] = Field(default=None, description='金融債権、流動資産（IFRS）')
    """ 金融債権、流動資産（IFRS） """
    financial_receivables_ncaifrs: Optional[IxNonFractionPublic] = Field(default=None, description='金融債権、非流動資産（IFRS）')
    """ 金融債権、非流動資産（IFRS） """
    increase_decrease_in_other_liabilities_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='その他負債の増加(△減少)、営業活動によるキャッシュ・フロー（IFRS）')
    """ その他負債の増加(△減少)、営業活動によるキャッシュ・フロー（IFRS） """
    insurance_contracts_liabilities_clifrs: Optional[IxNonFractionPublic] = Field(default=None, description='保険契約負債、流動負債（IFRS）')
    """ 保険契約負債、流動負債（IFRS） """
    loss_gain_on_disposal_of_fixed_assets_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='固定資産処分損益、営業活動によるキャッシュ・フロー（IFRS）')
    """ 固定資産処分損益、営業活動によるキャッシュ・フロー（IFRS） """
    net_decrease_increase_in_deposits_from_group_financing_within_three_months_fin_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='グループファイナンス預り金(３ヶ月以内)の純増減(△減少)、財務活動によるキャッシュ・フロー（IFRS）')
    """ グループファイナンス預り金(３ヶ月以内)の純増減(△減少)、財務活動によるキャッシュ・フロー（IFRS） """
    net_decrease_increase_in_restricted_cash_inv_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='引出制限条項付預金の純増減(△増加)、投資活動によるキャッシュ・フロー（IFRS）')
    """ 引出制限条項付預金の純増減(△増加)、投資活動によるキャッシュ・フロー（IFRS） """
    payments_for_acquisition_of_short_term_investments_inv_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='短期投資の取得、投資活動によるキャッシュ・フロー（IFRS）')
    """ 短期投資の取得、投資活動によるキャッシュ・フロー（IFRS） """
    payments_for_loans_receivable_from_associates_inv_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='関連会社に対する貸付、投資活動によるキャッシュ・フロー（IFRS）')
    """ 関連会社に対する貸付、投資活動によるキャッシュ・フロー（IFRS） """
    proceeds_from_deposits_from_group_financing_over_three_months_fin_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='グループファイナンス預り金(３ヶ月超)の受入、財務活動によるキャッシュ・フロー（IFRS）')
    """ グループファイナンス預り金(３ヶ月超)の受入、財務活動によるキャッシュ・フロー（IFRS） """
    proceeds_from_sales_and_redemptions_of_short_term_investments_inv_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='短期投資の売却及び償還、投資活動によるキャッシュ・フロー（IFRS）')
    """ 短期投資の売却及び償還、投資活動によるキャッシュ・フロー（IFRS） """
    repayments_of_deposits_from_group_financing_over_three_months_fin_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='グループファイナンス預り金(３ヶ月超)の返還、財務活動によるキャッシュ・フロー（IFRS）')
    """ グループファイナンス預り金(３ヶ月超)の返還、財務活動によるキャッシュ・フロー（IFRS） """
    depreciation_and_amortization_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='減価償却費及び償却費（IFRS）')
    """ 減価償却費及び償却費（IFRS） """
    increase_decrease_in_assets_and_liabilities_of_operating_activities_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='営業活動に係る資産・負債の増減合計、営業活動によるキャッシュ・フロー（IFRS）')
    """ 営業活動に係る資産・負債の増減合計、営業活動によるキャッシュ・フロー（IFRS） """
    loss_gain_on_sale_of_shares_of_subsidiaries_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='子会社株式売却損益（△は益）、営業活動によるキャッシュ・フロー（IFRS）')
    """ 子会社株式売却損益（△は益）、営業活動によるキャッシュ・フロー（IFRS） """
    operating_ebitdaifrs: Optional[IxNonFractionPublic] = Field(default=None, description='事業EBITDA（IFRS）')
    """ 事業EBITDA（IFRS） """
    payments_for_acquisition_of_share_acquisition_rights_in_subsidiaries_from_non_controlling_interests_fin_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='非支配持分からの子会社新株予約権の取得による支出、財務活動によるキャッシュ・フロー（IFRS）')
    """ 非支配持分からの子会社新株予約権の取得による支出、財務活動によるキャッシュ・フロー（IFRS） """
    proceeds_from_exercise_of_share_acquisition_rights_in_subsidiaries_fin_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='子会社新株予約権の行使による収入、財務活動によるキャッシュ・フロー（IFRS）')
    """ 子会社新株予約権の行使による収入、財務活動によるキャッシュ・フロー（IFRS） """
    proceeds_from_government_grants_inv_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='政府補助金による収入、投資活動によるキャッシュ・フロー（IFRS）')
    """ 政府補助金による収入、投資活動によるキャッシュ・フロー（IFRS） """
    subtotal2_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='小計-2、営業活動によるキャッシュ・フロー（IFRS）')
    """ 小計-2、営業活動によるキャッシュ・フロー（IFRS） """
    total_adjustments_to_reconcile_profit_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='利益に対する調整項目合計、営業活動によるキャッシュ・フロー（IFRS）')
    """ 利益に対する調整項目合計、営業活動によるキャッシュ・フロー（IFRS） """
    transactions_with_non_controlling_interests_ssifrs: Optional[IxNonFractionPublic] = Field(default=None, description='非支配持分との取引等、持分変動計算書（IFRS）')
    """ 非支配持分との取引等、持分変動計算書（IFRS） """
    changes_in_ownership_interest_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='所有者持分の変動（IFRS）')
    """ 所有者持分の変動（IFRS） """
    decrease_increase_in_deposit_paid_for_repurchase_of_treasury_stock_fin_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='自己株式取得のための預託金の増減額（△は増加）、財務活動によるキャッシュ・フロー（IFRS）')
    """ 自己株式取得のための預託金の増減額（△は増加）、財務活動によるキャッシュ・フロー（IFRS） """
    dividends_paid_to_non_controlling_shareholders_fin_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='非支配株主への配当金の支払額、財務活動によるキャッシュ・フロー（IFRS）')
    """ 非支配株主への配当金の支払額、財務活動によるキャッシュ・フロー（IFRS） """
    payments_for_retirement_of_property_plant_and_equipment_inv_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='有形固定資産の除却による支出、投資活動によるキャッシュ・フロー（IFRS）')
    """ 有形固定資産の除却による支出、投資活動によるキャッシュ・フロー（IFRS） """
    purchase_of_shares_of_subsidiaries_and_affiliates_inv_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='関係会社株式の取得による支出、投資活動によるキャッシュ・フロー（IFRS）')
    """ 関係会社株式の取得による支出、投資活動によるキャッシュ・フロー（IFRS） """
    put_options_written_on_non_controlling_interests_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='非支配持分に付与されたプット・オプション（IFRS）')
    """ 非支配持分に付与されたプット・オプション（IFRS） """
    decrease_increase_in_other_non_current_assets_ifrsifrs: Optional[IxNonFractionPublic] = Field(default=None, description='その他の非流動資産の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS）（IFRS）')
    """ その他の非流動資産の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS）（IFRS） """
    equity_transactions_with_non_controlling_interests_ssifrs: Optional[IxNonFractionPublic] = Field(default=None, description='非支配持分との資本取引、持分変動計算書（IFRS）')
    """ 非支配持分との資本取引、持分変動計算書（IFRS） """
    increase_decrease_in_other_current_liabilities_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='その他の流動負債の増減額（△は減少）、営業活動によるキャッシュ・フロー（IFRS）')
    """ その他の流動負債の増減額（△は減少）、営業活動によるキャッシュ・フロー（IFRS） """
    payments_of_long_term_loans_receivable_inv_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='長期貸付けによる支出、投資活動によるキャッシュ・フロー（IFRS）')
    """ 長期貸付けによる支出、投資活動によるキャッシュ・フロー（IFRS） """
    proceeds_from_sale_redemption_of_financial_assets_inv_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='金融資産の売却及び償還による収入、投資活動によるキャッシュ・フロー（IFRS）')
    """ 金融資産の売却及び償還による収入、投資活動によるキャッシュ・フロー（IFRS） """
    purchase_of_financial_assets_inv_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='金融資産の取得による支出、投資活動によるキャッシュ・フロー（IFRS）')
    """ 金融資産の取得による支出、投資活動によるキャッシュ・フロー（IFRS） """
    purchase_of_shares_of_subsidiaries_and_associates_inv_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='関係会社株式の取得による支出、投資活動によるキャッシュ・フロー（IFRS）')
    """ 関係会社株式の取得による支出、投資活動によるキャッシュ・フロー（IFRS） """
    purchase_of_shares_of_subsidiaries_not_resulting_in_change_in_scope_of_consolidation_fin_cfifrsifrs: Optional[IxNonFractionPublic] = Field(default=None, description='連結の範囲の変更を伴わない子会社株式の取得による支出、財務活動によるキャッシュ・フロー（IFRS）（IFRS）')
    """ 連結の範囲の変更を伴わない子会社株式の取得による支出、財務活動によるキャッシュ・フロー（IFRS）（IFRS） """
    atm_operation_business_revenues_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='ATM運営事業売上高（IFRS）')
    """ ATM運営事業売上高（IFRS） """
    cost_of_atm_operation_business_revenues_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='ATM運営事業売上原価（IFRS）')
    """ ATM運営事業売上原価（IFRS） """
    cost_of_network_services_revenues_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='ネットワークサービス売上原価（IFRS）')
    """ ネットワークサービス売上原価（IFRS） """
    cost_of_si_revenues_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='システムインテグレーション売上原価（IFRS）')
    """ システムインテグレーション売上原価（IFRS） """
    decrease_increase_in_other_assets_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='その他の資産の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS）')
    """ その他の資産の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS） """
    decrease_increase_in_other_financial_assets_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='その他の金融資産の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS）')
    """ その他の金融資産の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS） """
    decrease_increase_in_prepaid_expenses_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='前払費用の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS）')
    """ 前払費用の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS） """
    increase_decrease_in_deferred_income_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='繰延収益の増減額（△は減少）、営業活動によるキャッシュ・フロー（IFRS）')
    """ 繰延収益の増減額（△は減少）、営業活動によるキャッシュ・フロー（IFRS） """
    increase_decrease_in_other_financial_liabilities_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='その他の金融負債の増減額（△は減少）、営業活動によるキャッシュ・フロー（IFRS）')
    """ その他の金融負債の増減額（△は減少）、営業活動によるキャッシュ・フロー（IFRS） """
    investment_securities_equity_ncaifrs: Optional[IxNonFractionPublic] = Field(default=None, description='投資有価証券（株式）、非流動資産（IFRS）')
    """ 投資有価証券（株式）、非流動資産（IFRS） """
    network_services_revenues_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='ネットワークサービス売上高（IFRS）')
    """ ネットワークサービス売上高（IFRS） """
    payments_for_refundable_insurance_policies_inv_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='積立保険料の支払、投資活動によるキャッシュ・フロー（IFRS）')
    """ 積立保険料の支払、投資活動によるキャッシュ・フロー（IFRS） """
    payments_of_other_financial_liabilities_fin_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='その他の金融負債の支払、財務活動によるキャッシュ・フロー（IFRS）')
    """ その他の金融負債の支払、財務活動によるキャッシュ・フロー（IFRS） """
    prepaid_expenses_caifrs: Optional[IxNonFractionPublic] = Field(default=None, description='前払費用、流動資産（IFRS）')
    """ 前払費用、流動資産（IFRS） """
    prepaid_expenses_ncaifrs: Optional[IxNonFractionPublic] = Field(default=None, description='前払費用、非流動資産（IFRS）')
    """ 前払費用、非流動資産（IFRS） """
    proceeds_from_other_financial_liabilities_fin_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='その他の金融負債による収入、財務活動によるキャッシュ・フロー（IFRS）')
    """ その他の金融負債による収入、財務活動によるキャッシュ・フロー（IFRS） """
    proceeds_from_sales_of_investment_securities_equity_inv_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='投資有価証券（株式）の売却による収入、投資活動によるキャッシュ・フロー（IFRS）')
    """ 投資有価証券（株式）の売却による収入、投資活動によるキャッシュ・フロー（IFRS） """
    purchases_of_investment_securities_equity_inv_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='投資有価証券（株式）の取得による支出、投資活動によるキャッシュ・フロー（IFRS）')
    """ 投資有価証券（株式）の取得による支出、投資活動によるキャッシュ・フロー（IFRS） """
    si_revenues_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='システムインテグレーション売上高（IFRS）')
    """ システムインテグレーション売上高（IFRS） """
    group_headquarters_management_costs_and_other_expenses_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='親会社の本社管理費等（IFRS）')
    """ 親会社の本社管理費等（IFRS） """
    increase_decrease_in_working_capital_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='運転資本の増減額(△は増加)、営業活動によるキャッシュ・フロー（IFRS）')
    """ 運転資本の増減額(△は増加)、営業活動によるキャッシュ・フロー（IFRS） """
    payments_of_time_deposits_exceeding_three_month_inv_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='3カ月超預金の預入による支出、投資活動によるキャッシュ・フロー（IFRS）')
    """ 3カ月超預金の預入による支出、投資活動によるキャッシュ・フロー（IFRS） """
    payments_on_investments_in_joint_ventures_inv_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='共同支配企業に対する投資による支出、投資活動によるキャッシュ・フロー（IFRS）')
    """ 共同支配企業に対する投資による支出、投資活動によるキャッシュ・フロー（IFRS） """
    proceeds_from_redemption_of_time_deposits_exceeding_three_months_inv_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='3カ月超預金の払戻による収入、投資活動によるキャッシュ・フロー（IFRS）')
    """ 3カ月超預金の払戻による収入、投資活動によるキャッシュ・フロー（IFRS） """
    proceeds_from_sale_and_redemption_of_financial_assets_inv_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='金融資産の売却・償還による収入、投資活動によるキャッシュ・フロー（IFRS）')
    """ 金融資産の売却・償還による収入、投資活動によるキャッシュ・フロー（IFRS） """
    purchases_of_financial_assets_inv_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='金融資産の取得による支出、投資活動によるキャッシュ・フロー（IFRS）')
    """ 金融資産の取得による支出、投資活動によるキャッシュ・フロー（IFRS） """
    research_and_development_expenditure_recognized_as_expense_during_period_segment_information_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='当期に費用認識した研究開発費、セグメント情報（IFRS）')
    """ 当期に費用認識した研究開発費、セグメント情報（IFRS） """
    increase_decrease_in_other_non_current_liabilities_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='その他の非流動負債の増減額（△は減少）、営業活動によるキャッシュ・フロー（IFRS）')
    """ その他の非流動負債の増減額（△は減少）、営業活動によるキャッシュ・フロー（IFRS） """
    net_increase_decrease_in_short_term_loans_borrowings_within_three_months_fin_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='短期借入金（３ヶ月以内）の純増減額（△は減少）、財務活動によるキャッシュ・フロー（IFRS）')
    """ 短期借入金（３ヶ月以内）の純増減額（△は減少）、財務活動によるキャッシュ・フロー（IFRS） """
    americas_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='米州、外部顧客への売上高 地域別区分への分解（IFRS）')
    """ 米州、外部顧客への売上高 地域別区分への分解（IFRS） """
    asia_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='アジア、外部顧客への売上高 地域別区分への分解（IFRS）')
    """ アジア、外部顧客への売上高 地域別区分への分解（IFRS） """
    assets_held_at_fair_value_through_other_comprehensive2_caifrs: Optional[IxNonFractionPublic] = Field(default=None, description='その他の包括利益を通じて公正価値を測定する金融資産、流動資産（IFRS）')
    """ その他の包括利益を通じて公正価値を測定する金融資産、流動資産（IFRS） """
    assets_held_at_fair_value_through_other_comprehensive_income_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='その他の包括利益を通じて公正価値を測定する金融資産（IFRS）')
    """ その他の包括利益を通じて公正価値を測定する金融資産（IFRS） """
    capital_contribution_for_non_controlling_interests_ifrsifrs: Optional[IxNonFractionPublic] = Field(default=None, description='非支配持分株主との資本取引による支出、財務活動によるキャッシュ・フロー（IFRS）（IFRS）')
    """ 非支配持分株主との資本取引による支出、財務活動によるキャッシュ・フロー（IFRS）（IFRS） """
    changes_in_ownership_interests_in_subsidiaries_and_others_ssifrs: Optional[IxNonFractionPublic] = Field(default=None, description='子会社等に対する所有持分の変動額、持分変動計算書（IFRS）')
    """ 子会社等に対する所有持分の変動額、持分変動計算書（IFRS） """
    dividends_received_from_joint_ventures_and_associates_inv_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='持分法適用会社からの配当金受領額、投資活動によるキャッシュ・フロー（IFRS）')
    """ 持分法適用会社からの配当金受領額、投資活動によるキャッシュ・フロー（IFRS） """
    europe_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='欧州、外部顧客への売上高 地域別区分への分解（IFRS）')
    """ 欧州、外部顧客への売上高 地域別区分への分解（IFRS） """
    exceptional_items_gains_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='個別開示項目収益（IFRS）')
    """ 個別開示項目収益（IFRS） """
    exceptional_items_losses_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='個別開示項目費用（IFRS）')
    """ 個別開示項目費用（IFRS） """
    hyperinflation_adjustment_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='超インフレの調整、キャッシュ・フロー計算書（IFRS）')
    """ 超インフレの調整、キャッシュ・フロー計算書（IFRS） """
    hyperinflation_adjustment_ssifrs: Optional[IxNonFractionPublic] = Field(default=None, description='超インフレの調整、持分変動計算書（IFRS）')
    """ 超インフレの調整、持分変動計算書（IFRS） """
    operating_profit_after_exceptional_items_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='個別開示項目後営業利益（IFRS）')
    """ 個別開示項目後営業利益（IFRS） """
    other_gains_losses_on_equity_method_investments_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='持分法投資に関するその他の利益（△は損失）（IFRS）')
    """ 持分法投資に関するその他の利益（△は損失）（IFRS） """
    proceeds_from_borrowings_fin_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='社債発行及び借入れによる収入、財務活動によるキャッシュ・フロー（IFRS）')
    """ 社債発行及び借入れによる収入、財務活動によるキャッシュ・フロー（IFRS） """
    proceeds_on_disposal_of_assets_held_at_fair_value_through_other_comprehensive_income_inv_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='その他の包括利益を通じて公正価値を測定する金融資産の売却による収入、投資活動によるキャッシュ・フロー（IFRS）')
    """ その他の包括利益を通じて公正価値を測定する金融資産の売却による収入、投資活動によるキャッシュ・フロー（IFRS） """
    proceeds_on_disposal_of_joint_ventures_and_associates_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='ジョイント・ベンチャー及び関連会社の売却による収入、投資活動によるキャッシュ・フロー（IFRS）')
    """ ジョイント・ベンチャー及び関連会社の売却による収入、投資活動によるキャッシュ・フロー（IFRS） """
    purchase_of_assets_held_at_fair_value_through_other_comprehensive_income_inv_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='その他の包括利益を通じて公正価値を測定する金融資産の取得による支出、投資活動によるキャッシュ・フロー（IFRS）')
    """ その他の包括利益を通じて公正価値を測定する金融資産の取得による支出、投資活動によるキャッシュ・フロー（IFRS） """
    repayment_of_borrowings_fin_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='社債償還及び借入金返済による支出、財務活動によるキャッシュ・フロー（IFRS）')
    """ 社債償還及び借入金返済による支出、財務活動によるキャッシュ・フロー（IFRS） """
    retained_earnings_translation_adjustment_at_the_ifrs_transition_date_equity_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='利益剰余金（IFRS移行時の累積換算差額）、資本（IFRS）')
    """ 利益剰余金（IFRS移行時の累積換算差額）、資本（IFRS） """
    reversal_of_previous_impairment_of_financial_receivables_owed_by_joint_ventures_and_associates_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='持分法適用会社に対する金融債権の減損損失の戻入益（IFRS）')
    """ 持分法適用会社に対する金融債権の減損損失の戻入益（IFRS） """
    stock_options_ssifrs: Optional[IxNonFractionPublic] = Field(default=None, description='新株予約権の増減、持分変動計算書（IFRS）')
    """ 新株予約権の増減、持分変動計算書（IFRS） """
    trade_and_other_receivables_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='売上債権及びその他の債権、非流動資産（IFRS）')
    """ 売上債権及びその他の債権、非流動資産（IFRS） """
    proceeds_from_government_grants_fin_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='政府補助金による収入、財務活動によるキャッシュ・フロー（IFRS）')
    """ 政府補助金による収入、財務活動によるキャッシュ・フロー（IFRS） """
    proceeds_from_sales_or_redemption_of_investments_in_debt_instruments_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='負債性金融商品の売却又は償還による収入、投資活動によるキャッシュ・フロー（IFRS）')
    """ 負債性金融商品の売却又は償還による収入、投資活動によるキャッシュ・フロー（IFRS） """
    purchase_of_investments_in_debt_instruments_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='負債性金融商品の取得による支出、投資活動によるキャッシュ・フロー（IFRS）')
    """ 負債性金融商品の取得による支出、投資活動によるキャッシュ・フロー（IFRS） """
    bonds_borrowings_and_lease_liabilities_clifrs: Optional[IxNonFractionPublic] = Field(default=None, description='社債、借入金及びリース負債、流動負債（IFRS）')
    """ 社債、借入金及びリース負債、流動負債（IFRS） """
    bonds_borrowings_and_lease_liabilities_nclifrs: Optional[IxNonFractionPublic] = Field(default=None, description='社債、借入金及びリース負債、非流動負債（IFRS）')
    """ 社債、借入金及びリース負債、非流動負債（IFRS） """
    free_cash_flow_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='フリー・キャッシュ・フロー、キャッシュ・フロー計算書（IFRS）')
    """ フリー・キャッシュ・フロー、キャッシュ・フロー計算書（IFRS） """
    loss_gain_from_sales_and_disposal_of_property_plant_and_equipment_net_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='固定資産の売廃却損益、営業活動によるキャッシュ・フロー（IFRS）')
    """ 固定資産の売廃却損益、営業活動によるキャッシュ・フロー（IFRS） """
    transactions_with_non_controlling_interests_and_others_ssifrs: Optional[IxNonFractionPublic] = Field(default=None, description='非支配持分との取引等、持分変動計算書（IFRS）')
    """ 非支配持分との取引等、持分変動計算書（IFRS） """
    transactions_with_non_controlling_interests_fin_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='非支配持分との取引、財務活動によるキャッシュ・フロー（IFRS）')
    """ 非支配持分との取引、財務活動によるキャッシュ・フロー（IFRS） """
    accounts_payable_and_accrued_expenses_clifrs: Optional[IxNonFractionPublic] = Field(default=None, description='未払金及び未払費用、流動負債（IFRS）')
    """ 未払金及び未払費用、流動負債（IFRS） """
    decrease_increase_in_trade_receivables_and_contract_assets_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='営業債権及び契約資産の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS）')
    """ 営業債権及び契約資産の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS） """
    exchange_differences_on_translation_of_foreign_operations_ssifrs: Optional[IxNonFractionPublic] = Field(default=None, description='在外営業活動体の換算差額、持分変動計算書（IFRS）')
    """ 在外営業活動体の換算差額、持分変動計算書（IFRS） """
    financial_assets_measured_at_fair_value_through_other_comprehensive_income_ssifrs: Optional[IxNonFractionPublic] = Field(default=None, description='その他の包括利益を通じて公正価値で測定する金融資産、持分変動計算書（IFRS）')
    """ その他の包括利益を通じて公正価値で測定する金融資産、持分変動計算書（IFRS） """
    increase_decrease_in_long_term_debt_fin_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='長期債務の増減額（△は減少）、財務活動によるキャッシュ・フロー（IFRS）')
    """ 長期債務の増減額（△は減少）、財務活動によるキャッシュ・フロー（IFRS） """
    increase_decrease_in_short_term_debt_fin_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='短期債務の増減額（△は減少）、財務活動によるキャッシュ・フロー（IFRS）')
    """ 短期債務の増減額（△は減少）、財務活動によるキャッシュ・フロー（IFRS） """
    net_changes_in_cash_flow_hedges_ssifrs: Optional[IxNonFractionPublic] = Field(default=None, description='キャッシュ・フロー・ヘッジの公正価値の純変動、持分変動計算書（IFRS）')
    """ キャッシュ・フロー・ヘッジの公正価値の純変動、持分変動計算書（IFRS） """
    proceeds_from_sale_and_redemption_of_investments_accounted_for_using_the_equity_method_and_other_financial_assets_inv_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='持分法投資及びその他の金融資産の売却及び償還、投資活動によるキャッシュ・フロー（IFRS）')
    """ 持分法投資及びその他の金融資産の売却及び償還、投資活動によるキャッシュ・フロー（IFRS） """
    purchase_of_investments_accounted_for_using_the_equity_method_and_other_financial_assets_inv_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='持分法投資及びその他の金融資産の取得、投資活動によるキャッシュ・フロー（IFRS）')
    """ 持分法投資及びその他の金融資産の取得、投資活動によるキャッシュ・フロー（IFRS） """
    remeasurements_of_defined_benefit_plans_ssifrs: Optional[IxNonFractionPublic] = Field(default=None, description='確定給付制度の再測定、持分変動計算書（IFRS）')
    """ 確定給付制度の再測定、持分変動計算書（IFRS） """
    short_term_debt_including_current_portion_of_long_term_debt_clifrs: Optional[IxNonFractionPublic] = Field(default=None, description='短期負債及び一年以内返済長期負債、流動負債（IFRS）')
    """ 短期負債及び一年以内返済長期負債、流動負債（IFRS） """
    trade_receivables_and_contract_assets_caifrs: Optional[IxNonFractionPublic] = Field(default=None, description='営業債権及び契約資産、流動資産（IFRS）')
    """ 営業債権及び契約資産、流動資産（IFRS） """
    transactions_with_non_controlling_interests_and_other_ssifrs: Optional[IxNonFractionPublic] = Field(default=None, description='非支配持分との取引等、持分変動計算書（IFRS）')
    """ 非支配持分との取引等、持分変動計算書（IFRS） """
    content_assets_ncaifrs: Optional[IxNonFractionPublic] = Field(default=None, description='コンテンツ資産、非流動資産（IFRS）')
    """ コンテンツ資産、非流動資産（IFRS） """
    costs_and_expenses_costs_and_expenses_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='売上原価、販売費・一般管理費及びその他の一般費用、売上原価、販売費・一般管理費及びその他の一般費用（IFRS）')
    """ 売上原価、販売費・一般管理費及びその他の一般費用、売上原価、販売費・一般管理費及びその他の一般費用（IFRS） """
    current_portion_of_long_term_debt_clifrs: Optional[IxNonFractionPublic] = Field(default=None, description='１年以内に返済期限の到来する長期借入債務、流動負債（IFRS）')
    """ １年以内に返済期限の到来する長期借入債務、流動負債（IFRS） """
    deposits_from_customers_in_the_banking_business_clifrs: Optional[IxNonFractionPublic] = Field(default=None, description='銀行ビジネスにおける顧客預金、流動負債（IFRS）')
    """ 銀行ビジネスにおける顧客預金、流動負債（IFRS） """
    exercise_of_share_acquisition_rights_and_other_ssifrs: Optional[IxNonFractionPublic] = Field(default=None, description='新株予約権の行使等、持分変動計算書（IFRS）')
    """ 新株予約権の行使等、持分変動計算書（IFRS） """
    financial_services_expenses_costs_and_expenses_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='金融ビジネス費用、売上原価、販売費・一般管理費及びその他の一般費用（IFRS）')
    """ 金融ビジネス費用、売上原価、販売費・一般管理費及びその他の一般費用（IFRS） """
    financial_services_revenue_sales_and_operating_revenue_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='金融ビジネス収入、売上高及び金融ビジネス収入（IFRS）')
    """ 金融ビジネス収入、売上高及び金融ビジネス収入（IFRS） """
    gain_loss_on_securities_net_other_than_financial_services_segment_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='有価証券に関する損（益）（純額）（金融分野以外）、営業活動によるキャッシュ・フロー（IFRS）')
    """ 有価証券に関する損（益）（純額）（金融分野以外）、営業活動によるキャッシュ・フロー（IFRS） """
    increase_decrease_in_borrowings_in_the_life_insurance_business_and_the_banking_business_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='生命保険ビジネス及び銀行ビジネスにおける借入債務の増加・減少（△）、営業活動によるキャッシュ・フロー（IFRS）')
    """ 生命保険ビジネス及び銀行ビジネスにおける借入債務の増加・減少（△）、営業活動によるキャッシュ・フロー（IFRS） """
    increase_decrease_in_content_assets_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='コンテンツ資産の増加（△）・減少、営業活動によるキャッシュ・フロー（IFRS）')
    """ コンテンツ資産の増加（△）・減少、営業活動によるキャッシュ・フロー（IFRS） """
    increase_decrease_in_deposits_from_customers_in_the_banking_business_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='銀行ビジネスにおける顧客預金の増加・減少（△）、営業活動によるキャッシュ・フロー（IFRS）')
    """ 銀行ビジネスにおける顧客預金の増加・減少（△）、営業活動によるキャッシュ・フロー（IFRS） """
    increase_decrease_in_insurance_contract_liabilities_net_of_insurance_contract_assets_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='保険契約負債（保険契約資産との純額）の増加・減少（△）、営業活動によるキャッシュ・フロー（IFRS）')
    """ 保険契約負債（保険契約資産との純額）の増加・減少（△）、営業活動によるキャッシュ・フロー（IFRS） """
    increase_decrease_in_investments_and_advances_in_the_financial_services_business_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='金融分野における投資及び貸付の増加（△）・減少、営業活動によるキャッシュ・フロー（IFRS）')
    """ 金融分野における投資及び貸付の増加（△）・減少、営業活動によるキャッシュ・フロー（IFRS） """
    increase_decrease_in_other_financial_assets_and_other_current_assets_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='その他の金融資産及びその他の資産（流動）の増加（△）・減少、営業活動によるキャッシュ・フロー（IFRS）')
    """ その他の金融資産及びその他の資産（流動）の増加（△）・減少、営業活動によるキャッシュ・フロー（IFRS） """
    increase_decrease_in_other_financial_liabilities_and_other_current_liabilities_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='その他の金融負債及びその他の負債（流動）の増加・減少（△）、営業活動によるキャッシュ・フロー（IFRS）')
    """ その他の金融負債及びその他の負債（流動）の増加・減少（△）、営業活動によるキャッシュ・フロー（IFRS） """
    increase_decrease_in_taxes_payable_other_than_income_taxes_net_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='法人所得税以外の未払税金（純額）の増加・減少（△）、営業活動によるキャッシュ・フロー（IFRS）')
    """ 法人所得税以外の未払税金（純額）の増加・減少（△）、営業活動によるキャッシュ・フロー（IFRS） """
    increase_decrease_in_trade_receivables_and_contract_assets_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='営業債権及び契約資産の増加（△）・減少、営業活動によるキャッシュ・フロー（IFRS）')
    """ 営業債権及び契約資産の増加（△）・減少、営業活動によるキャッシュ・フロー（IFRS） """
    insurance_contract_liabilities_nclifrs: Optional[IxNonFractionPublic] = Field(default=None, description='保険契約負債（IFRS）')
    """ 保険契約負債（IFRS） """
    insurance_finance_expenses_income_financial_services_expenses_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='保険金融費用（収益）、金融ビジネス費用（IFRS）')
    """ 保険金融費用（収益）、金融ビジネス費用（IFRS） """
    insurance_finance_income_expenses_net_of_tax_items_that_may_be_reclassified_to_profit_or_loss_ociifrs: Optional[IxNonFractionPublic] = Field(default=None, description='保険金融収益（費用）（税引後）、純損益に振り替えられる可能性のあるその他の包括利益（IFRS）')
    """ 保険金融収益（費用）（税引後）、純損益に振り替えられる可能性のあるその他の包括利益（IFRS） """
    insurance_income_financial_services_revenue_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='保険収益、金融ビジネス収入（IFRS）')
    """ 保険収益、金融ビジネス収入（IFRS） """
    insurance_service_costs_financial_services_expenses_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='保険サービス費用、金融ビジネス費用（IFRS）')
    """ 保険サービス費用、金融ビジネス費用（IFRS） """
    intersegment_sales_and_financial_services_revenue_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='セグメント間の売上高及び金融ビジネス収入（IFRS）')
    """ セグメント間の売上高及び金融ビジネス収入（IFRS） """
    investments_and_advances_in_the_financial_services_segment_caifrs: Optional[IxNonFractionPublic] = Field(default=None, description='金融分野における投資及び貸付、流動資産（IFRS）')
    """ 金融分野における投資及び貸付、流動資産（IFRS） """
    investments_and_advances_in_the_financial_services_segment_ncaifrs: Optional[IxNonFractionPublic] = Field(default=None, description='金融分野における投資及び貸付、非流動資産（IFRS）')
    """ 金融分野における投資及び貸付、非流動資産（IFRS） """
    long_term_debt2_nclifrs: Optional[IxNonFractionPublic] = Field(default=None, description='長期借入債務、非流動負債（IFRS）')
    """ 長期借入債務、非流動負債（IFRS） """
    other_financial_services_expense_financial_services_expenses_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='その他の保険ビジネス費用、金融ビジネス費用（IFRS）')
    """ その他の保険ビジネス費用、金融ビジネス費用（IFRS） """
    other_financial_services_revenue_financial_services_revenue_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='その他の金融ビジネス収入、金融ビジネス収入（IFRS）')
    """ その他の金融ビジネス収入、金融ビジネス収入（IFRS） """
    other_net_of_tax_items_that_may_be_reclassified_to_profit_or_loss_ociifrs: Optional[IxNonFractionPublic] = Field(default=None, description='その他（税引後）、純損益に振り替えられる可能性のあるその他の包括利益（IFRS）')
    """ その他（税引後）、純損益に振り替えられる可能性のあるその他の包括利益（IFRS） """
    other_operating_income_expense_net_costs_and_expenses_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='その他の営業損（益）（純額）、売上原価、販売費・一般管理費及びその他の一般費用（IFRS）')
    """ その他の営業損（益）（純額）、売上原価、販売費・一般管理費及びその他の一般費用（IFRS） """
    other_operating_income_expense_net_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='その他の営業損（益）（純額）、営業活動によるキャッシュ・フロー（IFRS）')
    """ その他の営業損（益）（純額）、営業活動によるキャッシュ・フロー（IFRS） """
    participation_liabilities_in_the_pictures_segment_clifrs: Optional[IxNonFractionPublic] = Field(default=None, description='映画分野における未払分配金債務、流動負債（IFRS）')
    """ 映画分野における未払分配金債務、流動負債（IFRS） """
    participation_liabilities_in_the_pictures_segment_nclifrs: Optional[IxNonFractionPublic] = Field(default=None, description='映画分野における未払分配金債務、非流動負債（IFRS）')
    """ 映画分野における未払分配金債務、非流動負債（IFRS） """
    payments_for_investments_and_advances_other_than_financial_services_business_inv_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='投資及び貸付（金融分野以外）、投資活動によるキャッシュ・フロー（IFRS）')
    """ 投資及び貸付（金融分野以外）、投資活動によるキャッシュ・フロー（IFRS） """
    payments_of_long_term_debt_fin_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='長期借入債務の返済、財務活動によるキャッシュ・フロー（IFRS）')
    """ 長期借入債務の返済、財務活動によるキャッシュ・フロー（IFRS） """
    proceeds_from_issuance_of_long_term_debt_fin_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='長期借入債務による調達、財務活動によるキャッシュ・フロー（IFRS）')
    """ 長期借入債務による調達、財務活動によるキャッシュ・フロー（IFRS） """
    proceeds_from_sales_or_return_of_investments_and_collections_of_advances_other_than_financial_services_business_inv_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='投資の売却又は償還及び貸付の回収（金融分野以外）、投資活動によるキャッシュ・フロー（IFRS）')
    """ 投資の売却又は償還及び貸付の回収（金融分野以外）、投資活動によるキャッシュ・フロー（IFRS） """
    sales_and_financial_services_revenue_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='売上高及び金融ビジネス収入（IFRS）')
    """ 売上高及び金融ビジネス収入（IFRS） """
    sales_and_financial_services_revenue_to_customers_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='外部顧客への売上高及び金融ビジネス収入（IFRS）')
    """ 外部顧客への売上高及び金融ビジネス収入（IFRS） """
    share_of_profit_loss_of_investments_accounted_for_using_the_equity_method_net_of_dividends_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='持分法による投資（利益）損失（純額）（受取配当金相殺後）、営業活動によるキャッシュ・フロー（IFRS）')
    """ 持分法による投資（利益）損失（純額）（受取配当金相殺後）、営業活動によるキャッシュ・フロー（IFRS） """
    trade_receivables_other_receivables_and_contract_assets_caifrs: Optional[IxNonFractionPublic] = Field(default=None, description='営業債権、その他の債権及び契約資産、流動資産（IFRS）')
    """ 営業債権、その他の債権及び契約資産、流動資産（IFRS） """
    transactions_with_noncontrolling_interests_shareholders_and_other_ssifrs: Optional[IxNonFractionPublic] = Field(default=None, description='非支配持分株主との取引及びその他、持分変動計算書（IFRS）')
    """ 非支配持分株主との取引及びその他、持分変動計算書（IFRS） """
    decrease_increase_in_derivative_liabilities_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='デリバティブ負債の増減額（△は減少）、営業活動によるキャッシュ・フロー（IFRS）')
    """ デリバティブ負債の増減額（△は減少）、営業活動によるキャッシュ・フロー（IFRS） """
    deferred_government_grants_nclifrs: Optional[IxNonFractionPublic] = Field(default=None, description='政府補助金繰延収益、非流動負債（IFRS）')
    """ 政府補助金繰延収益、非流動負債（IFRS） """
    exchange_differences_on_translation_of_foreign_operations_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='在外営業活動体の換算差額（IFRS）')
    """ 在外営業活動体の換算差額（IFRS） """
    government_grants_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='政府補助金、営業活動によるキャッシュフロー（IFRS）')
    """ 政府補助金、営業活動によるキャッシュフロー（IFRS） """
    increase_decrease_in_accrued_expenses_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='未払費用の増減額（△は減少）、営業活動によるキャッシュ・フロー（IFRS）')
    """ 未払費用の増減額（△は減少）、営業活動によるキャッシュ・フロー（IFRS） """
    increase_decrease_in_consumption_tax_value_added_tax_receivables_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='未収消費税等の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS）')
    """ 未収消費税等の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS） """
    increase_decrease_in_derivative_assets_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='デリバティブ資産の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS）')
    """ デリバティブ資産の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS） """
    net_change_in_financial_assets_measured_at_fair_value_through_other_comprehensive_income_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='その他の包括利益を通じて公正価値で測定する金融資産の純変動（IFRS）')
    """ その他の包括利益を通じて公正価値で測定する金融資産の純変動（IFRS） """
    share_of_other_comprehensive_income_of_entities_accounted_for_using_equity_method_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='持分法によるその他の包括利益に対する持分相当額（IFRS）')
    """ 持分法によるその他の包括利益に対する持分相当額（IFRS） """
    share_of_other_comprehensive_income_of_entities_accounted_for_using_equity_method_items_that_may_be_reclassified_to_profit_or_loss_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='持分法によるその他の包括利益に対する持分相当額、純損益に振り替えられる可能性のある項目（IFRS）')
    """ 持分法によるその他の包括利益に対する持分相当額、純損益に振り替えられる可能性のある項目（IFRS） """
    increase_decrease_in_long_term_accounts_payable_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='長期未払金の増減額（△は減少）、営業活動によるキャッシュ・フロー（IFRS）')
    """ 長期未払金の増減額（△は減少）、営業活動によるキャッシュ・フロー（IFRS） """
    long_term_accounts_payable_nclifrs: Optional[IxNonFractionPublic] = Field(default=None, description='長期未払金、非流動負債（IFRS）')
    """ 長期未払金、非流動負債（IFRS） """
    retained_earnings_cumulative_translation_difference_at_transition_to_ifrsifrs: Optional[IxNonFractionPublic] = Field(default=None, description='利益剰余金（IFRS移行時の累積換算差額）、資本（IFRS）')
    """ 利益剰余金（IFRS移行時の累積換算差額）、資本（IFRS） """
    bonds_borrowings_and_other_financial_liabilities_clifrs: Optional[IxNonFractionPublic] = Field(default=None, description='社債、借入金及びその他の金融負債、流動負債（IFRS）')
    """ 社債、借入金及びその他の金融負債、流動負債（IFRS） """
    bonds_borrowings_and_other_financial_liabilities_nclifrs: Optional[IxNonFractionPublic] = Field(default=None, description='社債、借入金及びその他の金融負債、非流動負債（IFRS）')
    """ 社債、借入金及びその他の金融負債、非流動負債（IFRS） """
    business_profit_loss_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='事業利益（△は損失）（IFRS）')
    """ 事業利益（△は損失）（IFRS） """
    capital_increase_of_consolidated_subsidiaries_ssifrs: Optional[IxNonFractionPublic] = Field(default=None, description='連結子会社の増資による持分の増減、持分変動計算書（IFRS）')
    """ 連結子会社の増資による持分の増減、持分変動計算書（IFRS） """
    change_in_ownership_interest_of_parent_due_to_transactions_with_non_controlling_interests_ssifrs: Optional[IxNonFractionPublic] = Field(default=None, description='非支配株主との取引に係る親会社の持分変動、持分変動計算書（IFRS）')
    """ 非支配株主との取引に係る親会社の持分変動、持分変動計算書（IFRS） """
    decrease_increase_in_avdance_payment_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='前渡金の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS）')
    """ 前渡金の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS） """
    increase_decrease_in_other_current_assets_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='その他流動資産の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS）')
    """ その他流動資産の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS） """
    increase_decrease_in_refund_liability_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='返金負債の増減額（△は減少）、営業活動によるキャッシュ・フロー（IFRS）')
    """ 返金負債の増減額（△は減少）、営業活動によるキャッシュ・フロー（IFRS） """
    payments_for_acquisition_of_subsidiaries_not_resulting_in_change_in_scope_of_consolidation_fin_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='連結範囲の変更を伴わない子会社株式の取得による支出、財務活動によるキャッシュ・フロー（IFRS）')
    """ 連結範囲の変更を伴わない子会社株式の取得による支出、財務活動によるキャッシュ・フロー（IFRS） """
    payments_for_equity_method_investment_and_purchase_of_other_financial_assets_inv_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='持分法投資及びその他の金融資産の取得による支出、投資活動によるキャッシュ・フロー（IFRS）')
    """ 持分法投資及びその他の金融資産の取得による支出、投資活動によるキャッシュ・フロー（IFRS） """
    proceeds_from_equity_method_investment_and_sale_of_other_financial_assets_inv_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='持分法投資及びその他の金融資産の売却による収入、投資活動によるキャッシュ・フロー（IFRS）')
    """ 持分法投資及びその他の金融資産の売却による収入、投資活動によるキャッシュ・フロー（IFRS） """
    proceeds_from_factoring_agreements_fin_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='債権流動化による収入、財務活動によるキャッシュ・フロー（IFRS）')
    """ 債権流動化による収入、財務活動によるキャッシュ・フロー（IFRS） """
    refund_liabilities_clifrs: Optional[IxNonFractionPublic] = Field(default=None, description='返金負債、流動負債（IFRS）')
    """ 返金負債、流動負債（IFRS） """
    repayment_of_liabilities_under_factoring_agreements_fin_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='債権流動化の返済による支出、財務活動によるキャッシュ・フロー（IFRS）')
    """ 債権流動化の返済による支出、財務活動によるキャッシュ・フロー（IFRS） """
    increase_decrease_in_equity_due_to_acquisition_of_shares_in_consolidated_subsidiaries_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='連結子会社株式の取得による持分の増減（IFRS）')
    """ 連結子会社株式の取得による持分の増減（IFRS） """
    increase_decrease_in_liabilities_related_to_provisions_and_employee_benefits_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='引当金及び従業員給付に係る負債の増減額（△は減少）、営業活動によるキャッシュ・フロー（IFRS）')
    """ 引当金及び従業員給付に係る負債の増減額（△は減少）、営業活動によるキャッシュ・フロー（IFRS） """
    payments_from_changes_in_ownership_interests_in_subsidiaries_that_do_not_result_in_change_in_scope_of_consolidation_fin_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='連結範囲の変更を伴わない子会社株式の取得による支出、財務活動によるキャッシュ・フロー（IFRS）')
    """ 連結範囲の変更を伴わない子会社株式の取得による支出、財務活動によるキャッシュ・フロー（IFRS） """
    proceeds_from_sale_or_recovery_of_other_financial_assets_inv_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='その他の金融資産の売却または回収による収入、投資活動によるキャッシュ・フロー（IFRS）')
    """ その他の金融資産の売却または回収による収入、投資活動によるキャッシュ・フロー（IFRS） """
    purchase_of_intangible_assets_and_expenditure_on_internally_generated_intangible_assets_inv_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='無形資産の取得及び内部開発にかかわる支出、投資活動によるキャッシュ・フロー（IFRS）')
    """ 無形資産の取得及び内部開発にかかわる支出、投資活動によるキャッシュ・フロー（IFRS） """
    decrease_increase_in_deposits_for_purchase_of_treasury_shares_fin_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='自己株式取得のための預託金の増減額（△は増加）、財務活動によるキャッシュ・フロー（IFRS）')
    """ 自己株式取得のための預託金の増減額（△は増加）、財務活動によるキャッシュ・フロー（IFRS） """
    loss_gain_on_disposal_of_non_current_assets_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='固定資産処分損益（△は益）、営業活動によるキャッシュ・フロー（IFRS）')
    """ 固定資産処分損益（△は益）、営業活動によるキャッシュ・フロー（IFRS） """
    net_decrease_increase_in_leased_receivables_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='リース債権の増減額(△は増加)、営業活動によるキャッシュ・フロー（IFRS）')
    """ リース債権の増減額(△は増加)、営業活動によるキャッシュ・フロー（IFRS） """
    expense_by_acquisition_of_repurchased_stock_of_consolidated_subsidiary_fin_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='連結子会社の自己株式の取得による支出、財務活動によるキャッシュ・フロー（IFRS）')
    """ 連結子会社の自己株式の取得による支出、財務活動によるキャッシュ・フロー（IFRS） """
    tra_changes_in_ownership_interest_in_subsidiaries_ssifrs: Optional[IxNonFractionPublic] = Field(default=None, description='非支配株主との取引に係る親会社の持分変動、持分変動計算書（IFRS）')
    """ 非支配株主との取引に係る親会社の持分変動、持分変動計算書（IFRS） """
    claw_back_from_cancellation_of_stock_acquisition_agreements_inv_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='株式取得契約の解除に伴う回収額、投資活動によるキャッシュ・フロー（IFRS）')
    """ 株式取得契約の解除に伴う回収額、投資活動によるキャッシュ・フロー（IFRS） """
    decrease_increase_in_deposit_for_purchase_of_treasury_shares_fin_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='自己株式取得のための預託金の増減額、財務活動によるキャッシュ・フロー（△は増加）（IFRS）')
    """ 自己株式取得のための預託金の増減額、財務活動によるキャッシュ・フロー（△は増加）（IFRS） """
    gain_on_transfer_of_ssd_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='科学事業の譲渡益、営業活動によるキャッシュ・フロー（IFRS）')
    """ 科学事業の譲渡益、営業活動によるキャッシュ・フロー（IFRS） """
    payments_for_contingent_consideration_inv_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='条件付対価の決済による支出、投資活動によるキャッシュ・フロー（IFRS）')
    """ 条件付対価の決済による支出、投資活動によるキャッシュ・フロー（IFRS） """
    proceeds_from_sale_of_ssd_businessse_inv_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='科学事業の譲渡による収入、投資活動によるキャッシュ・フロー（IFRS）')
    """ 科学事業の譲渡による収入、投資活動によるキャッシュ・フロー（IFRS） """
    proceeds_from_transfer_of_collagen_business_and_dental_product_sales_businesses_inv_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='コラーゲン事業及び歯科用商品販売事業の譲渡による収入、投資活動によるキャッシュ・フロー（IFRS）')
    """ コラーゲン事業及び歯科用商品販売事業の譲渡による収入、投資活動によるキャッシュ・フロー（IFRS） """
    transfer_from_retained_earnings_to_capital_surplus_ssifrs: Optional[IxNonFractionPublic] = Field(default=None, description='利益剰余金から資本剰余金への振替額、持分変動計算書（IFRS）')
    """ 利益剰余金から資本剰余金への振替額、持分変動計算書（IFRS） """
    capital_transaction_with_non_controlling_interests_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='非支配株主との資本取引（IFRS）')
    """ 非支配株主との資本取引（IFRS） """
    increase_in_lease_receivables_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='リース債権の増加、営業活動によるキャッシュ・フロー（IFRS）')
    """ リース債権の増加、営業活動によるキャッシュ・フロー（IFRS） """
    intersegment_operating_expenses_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='セグメント間の営業費用（IFRS）')
    """ セグメント間の営業費用（IFRS） """
    net_change_in_treasury_stock_ssifrs: Optional[IxNonFractionPublic] = Field(default=None, description='自己株式の取得及び売却、持分変動計算書（IFRS）')
    """ 自己株式の取得及び売却、持分変動計算書（IFRS） """
    other_income_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='その他の収益、営業活動によるキャッシュ・フロー（IFRS）')
    """ その他の収益、営業活動によるキャッシュ・フロー（IFRS） """
    proceeds_from_sales_of_business_inv_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='事業の売却 （売却時の現金及び現金同等物保有額控除後）、投資活動によるキャッシュ・フロー（IFRS）')
    """ 事業の売却 （売却時の現金及び現金同等物保有額控除後）、投資活動によるキャッシュ・フロー（IFRS） """
    purchases_of_business_net_of_cash_acquired_inv_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='事業の買収（取得時の現金及び現金同等物受入額控除後）、投資活動によるキャッシュ・フロー（IFRS）')
    """ 事業の買収（取得時の現金及び現金同等物受入額控除後）、投資活動によるキャッシュ・フロー（IFRS） """
    transfer_to_capital_surplus_from_retained_earnings_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='利益剰余金から資本剰余金への振替（IFRS）')
    """ 利益剰余金から資本剰余金への振替（IFRS） """
    unallocatable_expenses_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='配賦不能費用（IFRS）')
    """ 配賦不能費用（IFRS） """
    assets_related_to_securities_business_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='証券業関連資産、資産（IFRS）')
    """ 証券業関連資産、資産（IFRS） """
    customer_deposits_for_banking_business_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='顧客預金、負債（IFRS）')
    """ 顧客預金、負債（IFRS） """
    decrease_in_bond_and_borrowing_banking_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='社債及び借入金（銀行業）の増減、営業活動によるキャッシュ・フロー（IFRS）')
    """ 社債及び借入金（銀行業）の増減、営業活動によるキャッシュ・フロー（IFRS） """
    decrease_in_payables_under_securities_lending_transactions_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='債券貸借取引受入担保金の増減、営業活動によるキャッシュ・フロー（IFRS）')
    """ 債券貸借取引受入担保金の増減、営業活動によるキャッシュ・フロー（IFRS） """
    decrease_increase_in_assets_liabilities_related_to_securities_business_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='証券業関連資産及び負債の増減、営業活動によるキャッシュ・フロー（IFRS）')
    """ 証券業関連資産及び負債の増減、営業活動によるキャッシュ・フロー（IFRS） """
    decrease_increase_in_customer_deposits_for_banking_business_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='顧客預金の増減、営業活動によるキャッシュ・フロー（IFRS）')
    """ 顧客預金の増減、営業活動によるキャッシュ・フロー（IFRS） """
    decrease_increase_in_operational_investment_securities_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='営業投資有価証券の増減、営業活動によるキャッシュ・フロー（IFRS）')
    """ 営業投資有価証券の増減、営業活動によるキャッシュ・フロー（IFRS） """
    distributions_to_non_controlling_interests_in_consolidated_investment_funds_fin_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='投資事業組合等における非支配持分への分配金支払額、財務活動によるキャッシュ・フロー（IFRS）')
    """ 投資事業組合等における非支配持分への分配金支払額、財務活動によるキャッシュ・フロー（IFRS） """
    expense_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='費用（IFRS）')
    """ 費用（IFRS） """
    financial_cost_associated_with_financial_income_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='金融収益に係る金融費用、費用（IFRS）')
    """ 金融収益に係る金融費用、費用（IFRS） """
    financial_instruments_pledged_as_collateral_assets_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='担保差入金融商品、資産（IFRS）')
    """ 担保差入金融商品、資産（IFRS） """
    fluctuations_in_discount_rates_of_insurance_contracts_items_that_may_be_reclassified_to_profit_or_loss_ociifrs: Optional[IxNonFractionPublic] = Field(default=None, description='保険契約の割引率変動差額（税引後）、純損益に振り替えられる可能性のあるその他の包括利益（IFRS）')
    """ 保険契約の割引率変動差額（税引後）、純損益に振り替えられる可能性のあるその他の包括利益（IFRS） """
    gain_on_bargain_purchase_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='負ののれん発生益、営業活動によるキャッシュ・フロー（IFRS）')
    """ 負ののれん発生益、営業活動によるキャッシュ・フロー（IFRS） """
    insurance_contract_liabilities_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='保険契約負債、負債（IFRS）')
    """ 保険契約負債、負債（IFRS） """
    insurance_service_expenses_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='保険サービス費用（IFRS）')
    """ 保険サービス費用（IFRS） """
    inventories_assets_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='棚卸資産、資産（IFRS）')
    """ 棚卸資産、資産（IFRS） """
    issuance_of_convertible_bonds_ssifrs: Optional[IxNonFractionPublic] = Field(default=None, description='転換社債型新株予約権付社債の発行、持分変動計算書（IFRS）')
    """ 転換社債型新株予約権付社債の発行、持分変動計算書（IFRS） """
    liabilities_related_to_securities_business_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='証券業関連負債、負債（IFRS）')
    """ 証券業関連負債、負債（IFRS） """
    net_fair_value_gains_losses_net_of_tax_attributable_to_credit_risk_related_to_financial_liabilities_designated_as_at_fair_value_through_profit_or_loss_ociifrs: Optional[IxNonFractionPublic] = Field(default=None, description='負債の信用リスクの変動額（税引後）、純損益に振り替えられることのないその他の包括利益（IFRS）')
    """ 負債の信用リスクの変動額（税引後）、純損益に振り替えられることのないその他の包括利益（IFRS） """
    of_insurance_revenue_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='（内、保険収益）（IFRS）')
    """ （内、保険収益）（IFRS） """
    of_interest_income_revenue_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='（内、受取利息）（IFRS）')
    """ （内、受取利息）（IFRS） """
    operational_investment_securities_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='営業投資有価証券、資産（IFRS）')
    """ 営業投資有価証券、資産（IFRS） """
    other_financial_cost_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='その他の金融費用、費用（IFRS）')
    """ その他の金融費用、費用（IFRS） """
    other_investment_securities_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='その他の投資有価証券、資産（IFRS）')
    """ その他の投資有価証券、資産（IFRS） """
    proceeds_from_stock_issuance_to_non_controlling_interests_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='投資事業組合等における非支配持分からの出資受入による収入、財務活動によるキャッシュ・フロー（IFRS）')
    """ 投資事業組合等における非支配持分からの出資受入による収入、財務活動によるキャッシュ・フロー（IFRS） """
    provision_for_credit_losses_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='信用損失引当金繰入（IFRS）')
    """ 信用損失引当金繰入（IFRS） """
    reinsurance_contracts_assets_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='再保険契約資産、資産（IFRS）')
    """ 再保険契約資産、資産（IFRS） """
    changes_from_loss_of_control_ssifrs: Optional[IxNonFractionPublic] = Field(default=None, description='支配喪失による変動、持分変動計算書（IFRS）')
    """ 支配喪失による変動、持分変動計算書（IFRS） """
    changes_in_the_fair_value_of_debt_investments_at_fvtoci_items_that_may_be_reclassified_to_profit_or_loss_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='FVTOCIの負債性金融資産の公正価値の変動、純損益に振り替えられる可能性のある項目（IFRS）')
    """ FVTOCIの負債性金融資産の公正価値の変動、純損益に振り替えられる可能性のある項目（IFRS） """
    changes_in_the_fair_value_of_equity_investments_at_fvtoci_net_of_tax_items_that_will_not_be_reclassified_to_profit_or_loss_ociifrs: Optional[IxNonFractionPublic] = Field(default=None, description='FVTOCIの資本性金融資産の公正価値の変動（税引後）、純損益に振り替えられることのないその他の包括利益（IFRS）')
    """ FVTOCIの資本性金融資産の公正価値の変動（税引後）、純損益に振り替えられることのないその他の包括利益（IFRS） """
    contract_costs_ncaifrs: Optional[IxNonFractionPublic] = Field(default=None, description='契約コスト、非流動資産（IFRS）')
    """ 契約コスト、非流動資産（IFRS） """
    decrease_in_consumption_taxes_payable_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='未払消費税等の増減額（△は減少額）、営業活動によるキャッシュ・フロー（IFRS）')
    """ 未払消費税等の増減額（△は減少額）、営業活動によるキャッシュ・フロー（IFRS） """
    deposits_for_banking_business_clifrs: Optional[IxNonFractionPublic] = Field(default=None, description='銀行事業の預金、流動負債（IFRS）')
    """ 銀行事業の預金、流動負債（IFRS） """
    gain_or_loss_on_change_in_equity_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='持分変動損益（IFRS）')
    """ 持分変動損益（IFRS） """
    gain_or_loss_on_sale_of_equity_method_investment_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='持分法による投資の売却損益（IFRS）')
    """ 持分法による投資の売却損益（IFRS） """
    gain_or_loss_on_sales_of_equity_method_investments_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='持分法による投資の売却損益（△は益）、営業活動によるキャッシュ・フロー（IFRS）')
    """ 持分法による投資の売却損益（△は益）、営業活動によるキャッシュ・フロー（IFRS） """
    gain_relating_to_loss_of_control_over_subsidiaries_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='子会社の支配喪失に伴う利益、営業活動によるキャッシュ・フロー（IFRS）')
    """ 子会社の支配喪失に伴う利益、営業活動によるキャッシュ・フロー（IFRS） """
    increase_decrease_in_customer_deposits_in_banking_business_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='銀行事業の預金の増減額（△は減少額）、営業活動によるキャッシュ・フロー（IFRS）')
    """ 銀行事業の預金の増減額（△は減少額）、営業活動によるキャッシュ・フロー（IFRS） """
    increase_decrease_in_loans_in_banking_business_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='銀行事業の貸付金の増減額(△は増加額)、営業活動によるキャッシュ・フロー（IFRS）')
    """ 銀行事業の貸付金の増減額(△は増加額)、営業活動によるキャッシュ・フロー（IFRS） """
    investment_securities_for_banking_business_ncaifrs: Optional[IxNonFractionPublic] = Field(default=None, description='銀行事業の有価証券、非流動資産（IFRS）')
    """ 銀行事業の有価証券、非流動資産（IFRS） """
    loss_gain_on_change_in_equity_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='持分変動損益（△は益）、営業活動によるキャッシュ・フロー（IFRS）')
    """ 持分変動損益（△は益）、営業活動によるキャッシュ・フロー（IFRS） """
    net_increase_decrease_in_cash_and_cash_equivalents_resulting_from_transfer_to_assets_as_held_for_sale_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='売却目的保有に分類された資産への振替に伴う現金及び現金同等物の増減額(△は減少額)（IFRS）')
    """ 売却目的保有に分類された資産への振替に伴う現金及び現金同等物の増減額(△は減少額)（IFRS） """
    net_increase_decrease_in_short_term_interest_bearing_liabilities_fin_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='短期有利子負債の純増減額（△は減少額）、財務活動によるキャッシュ・フロー（IFRS）')
    """ 短期有利子負債の純増減額（△は減少額）、財務活動によるキャッシュ・フロー（IFRS） """
    proceeds_from_interst_bearing_debt_fin_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='有利子負債の収入、財務活動によるキャッシュ・フロー（IFRS）')
    """ 有利子負債の収入、財務活動によるキャッシュ・フロー（IFRS） """
    proceeds_from_loss_of_control_of_subsidiaries_inv_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='子会社の支配喪失による収支（△は支出）、投資活動によるキャッシュ・フロー（IFRS）')
    """ 子会社の支配喪失による収支（△は支出）、投資活動によるキャッシュ・フロー（IFRS） """
    proceeds_from_obtaining_control_of_subsidiaries_inv_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='子会社の支配獲得による収支（△は支出）、投資活動によるキャッシュ・フロー（IFRS）')
    """ 子会社の支配獲得による収支（△は支出）、投資活動によるキャッシュ・フロー（IFRS） """
    proceeds_from_sales_of_investment_securities_in_banking_business_inv_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='銀行事業の有価証券の売却または償還による収入、投資活動によるキャッシュ・フロー（IFRS）')
    """ 銀行事業の有価証券の売却または償還による収入、投資活動によるキャッシュ・フロー（IFRS） """
    purchase_of_investment_securities_in_banking_business_inv_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='銀行事業の有価証券の取得による支出、投資活動によるキャッシュ・フロー（IFRS）')
    """ 銀行事業の有価証券の取得による支出、投資活動によるキャッシュ・フロー（IFRS） """
    purchases_of_mobile_devices_leased_to_enterprise_customers_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='法人向けレンタル用携帯端末の取得による支出、営業活動によるキャッシュ・フロー（IFRS）')
    """ 法人向けレンタル用携帯端末の取得による支出、営業活動によるキャッシュ・フロー（IFRS） """
    repayment_of_interest_bearing_debt_fin_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='有利子負債の支出、財務活動によるキャッシュ・フロー（IFRS）')
    """ 有利子負債の支出、財務活動によるキャッシュ・フロー（IFRS） """
    transfer_from_retained_earnings_to_capital_surplus_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='利益剰余金から資本剰余金への振替（IFRS）')
    """ 利益剰余金から資本剰余金への振替（IFRS） """
    decrease_increase_in_consumption_taxes_refund_receivable_ope_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='未収消費税等の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS）（IFRS）')
    """ 未収消費税等の増減額（△は増加）、営業活動によるキャッシュ・フロー（IFRS）（IFRS） """
    net_increase_decrease_in_short_term_borrowings_within3_months_fin_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='短期借入金（３ヶ月以内）の純増減額、財務活動によるキャッシュ・フロー（IFRS）')
    """ 短期借入金（３ヶ月以内）の純増減額、財務活動によるキャッシュ・フロー（IFRS） """
    proceeds_from_short_term_borrowings_over_three_months_fin_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='短期借入れ（３ヶ月超）による収入、財務活動によるキャッシュ・フロー（IFRS）')
    """ 短期借入れ（３ヶ月超）による収入、財務活動によるキャッシュ・フロー（IFRS） """
    reduction_in_subsidiaries_without_sale_of_equity_interest_inv_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='持分の売却を伴わない子会社の減少、投資活動によるキャッシュ・フロー（IFRS）')
    """ 持分の売却を伴わない子会社の減少、投資活動によるキャッシュ・フロー（IFRS） """
    repayments_of_short_term_borrowings_over_three_months_fin_cfifrs: Optional[IxNonFractionPublic] = Field(default=None, description='短期借入金（３ヶ月超）の返済による支出、財務活動によるキャッシュ・フロー（IFRS）')
    """ 短期借入金（３ヶ月超）の返済による支出、財務活動によるキャッシュ・フロー（IFRS） """
    transfer_to_non_financial_assets_etc_ifrsssifrs: Optional[IxNonFractionPublic] = Field(default=None, description='非金融資産等への振替、持分変動計算書（IFRS）')
    """ 非金融資産等への振替、持分変動計算書（IFRS） """
    gain_on_loss_of_control_of_subsidiaries_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='子会社の支配喪失に伴う利益（IFRS）')
    """ 子会社の支配喪失に伴う利益（IFRS） """
    loss_on_change_in_equity_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='持分変動損失（IFRS）')
    """ 持分変動損失（IFRS） """
    non_current_liability_for_stock_benefit_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='株式報酬に係る負債、非流動負債（IFRS）')
    """ 株式報酬に係る負債、非流動負債（IFRS） """

