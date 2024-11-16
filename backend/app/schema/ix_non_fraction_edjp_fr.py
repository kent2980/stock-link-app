from app.models import Field, SQLModel
from app.schema.ix_non_fraction import IxNonFractionPublic
from typing import Optional

class IxNonFractionEdjpFr(SQLModel):
    depreciation_segment_information: Optional[IxNonFractionPublic] = Field(default=None, description='減価償却費、セグメント情報')
    """ 減価償却費、セグメント情報 """
    equity_in_earnings_losses_of_affiliates: Optional[IxNonFractionPublic] = Field(default=None, description='持分法投資利益又は損失（△）')
    """ 持分法投資利益又は損失（△） """
    goodwill_before_offsetting: Optional[IxNonFractionPublic] = Field(default=None, description='のれん（相殺前）')
    """ のれん（相殺前） """
    income_tax_expense: Optional[IxNonFractionPublic] = Field(default=None, description='税金費用')
    """ 税金費用 """
    increase_in_property_plant_and_equipment_and_intangible_assets: Optional[IxNonFractionPublic] = Field(default=None, description='有形固定資産及び無形固定資産の増加額')
    """ 有形固定資産及び無形固定資産の増加額 """
    investments_in_entities_accounted_for_using_equity_method: Optional[IxNonFractionPublic] = Field(default=None, description='持分法適用会社への投資額')
    """ 持分法適用会社への投資額 """
    research_and_development_expenses_included_in_general_and_administrative_expenses_and_manufacturing_cost_for_current_period: Optional[IxNonFractionPublic] = Field(default=None, description='一般管理費及び当期製造費用に含まれる研究開発費')
    """ 一般管理費及び当期製造費用に含まれる研究開発費 """
    revenues_from_external_customers: Optional[IxNonFractionPublic] = Field(default=None, description='外部顧客への売上高')
    """ 外部顧客への売上高 """
    transactions_with_other_segments: Optional[IxNonFractionPublic] = Field(default=None, description='セグメント間の内部売上高又は振替高')
    """ セグメント間の内部売上高又は振替高 """
    number_of_submission_dei: Optional[IxNonFractionPublic] = Field(default=None, description='提出回数、DEI')
    """ 提出回数、DEI """
    acceptances_and_guarantees_liabilities_bnk: Optional[IxNonFractionPublic] = Field(default=None, description='支払承諾、負債の部、銀行業')
    """ 支払承諾、負債の部、銀行業 """
    accounts_payable_consignment: Optional[IxNonFractionPublic] = Field(default=None, description='受託販売未払金')
    """ 受託販売未払金 """
    accounts_payable_facilities: Optional[IxNonFractionPublic] = Field(default=None, description='設備関係未払金')
    """ 設備関係未払金 """
    accounts_payable_for_construction_contracts_cns: Optional[IxNonFractionPublic] = Field(default=None, description='工事未払金、建設業')
    """ 工事未払金、建設業 """
    accounts_payable_other: Optional[IxNonFractionPublic] = Field(default=None, description='未払金')
    """ 未払金 """
    accounts_payable_other_and_accrued_expenses: Optional[IxNonFractionPublic] = Field(default=None, description='未払金及び未払費用')
    """ 未払金及び未払費用 """
    accounts_payable_real_estate: Optional[IxNonFractionPublic] = Field(default=None, description='不動産事業未払金')
    """ 不動産事業未払金 """
    accounts_payable_trade: Optional[IxNonFractionPublic] = Field(default=None, description='買掛金')
    """ 買掛金 """
    accounts_receivable_assets_ins: Optional[IxNonFractionPublic] = Field(default=None, description='未収金、資産の部、保険業')
    """ 未収金、資産の部、保険業 """
    accounts_receivable_from_completed_construction_contracts_cns: Optional[IxNonFractionPublic] = Field(default=None, description='完成工事未収入金、建設業')
    """ 完成工事未収入金、建設業 """
    accounts_receivable_installment: Optional[IxNonFractionPublic] = Field(default=None, description='割賦売掛金')
    """ 割賦売掛金 """
    accounts_receivable_installment_sales_calea: Optional[IxNonFractionPublic] = Field(default=None, description='割賦債権、流動資産、リース事業')
    """ 割賦債権、流動資産、リース事業 """
    accounts_receivable_lease_calea: Optional[IxNonFractionPublic] = Field(default=None, description='賃貸料等未収入金、流動資産、リース事業')
    """ 賃貸料等未収入金、流動資産、リース事業 """
    accounts_receivable_operating_loans_calea: Optional[IxNonFractionPublic] = Field(default=None, description='営業貸付金、流動資産、リース事業')
    """ 営業貸付金、流動資産、リース事業 """
    accounts_receivable_other: Optional[IxNonFractionPublic] = Field(default=None, description='未収入金')
    """ 未収入金 """
    accounts_receivable_other_loans_to_customers_calea: Optional[IxNonFractionPublic] = Field(default=None, description='その他の営業貸付債権、流動資産、リース事業')
    """ その他の営業貸付債権、流動資産、リース事業 """
    accounts_receivable_trade: Optional[IxNonFractionPublic] = Field(default=None, description='売掛金')
    """ 売掛金 """
    accounts_receivable_trade_and_contract_assets: Optional[IxNonFractionPublic] = Field(default=None, description='売掛金及び契約資産')
    """ 売掛金及び契約資産 """
    accrued_alcohol_tax: Optional[IxNonFractionPublic] = Field(default=None, description='未払酒税')
    """ 未払酒税 """
    accrued_business_office_taxes: Optional[IxNonFractionPublic] = Field(default=None, description='未払事業所税')
    """ 未払事業所税 """
    accrued_consumption_taxes: Optional[IxNonFractionPublic] = Field(default=None, description='未払消費税等')
    """ 未払消費税等 """
    accrued_expenses: Optional[IxNonFractionPublic] = Field(default=None, description='未払費用')
    """ 未払費用 """
    accrued_income: Optional[IxNonFractionPublic] = Field(default=None, description='未収収益')
    """ 未収収益 """
    accrued_premiums_assets_ins: Optional[IxNonFractionPublic] = Field(default=None, description='未収保険料、資産の部、保険業')
    """ 未収保険料、資産の部、保険業 """
    accumulated_depreciation_and_impairment_loss_buildings_and_structures: Optional[IxNonFractionPublic] = Field(default=None, description='減価償却累計額及び減損損失累計額、建物及び構築物')
    """ 減価償却累計額及び減損損失累計額、建物及び構築物 """
    accumulated_depreciation_and_impairment_loss_lease_assets_ppe: Optional[IxNonFractionPublic] = Field(default=None, description='減価償却累計額及び減損損失累計額、リース資産、有形固定資産')
    """ 減価償却累計額及び減損損失累計額、リース資産、有形固定資産 """
    accumulated_depreciation_and_impairment_loss_machinery_equipment_and_vehicles: Optional[IxNonFractionPublic] = Field(default=None, description='減価償却累計額及び減損損失累計額、機械装置及び運搬具')
    """ 減価償却累計額及び減損損失累計額、機械装置及び運搬具 """
    accumulated_depreciation_and_impairment_loss_other_ppe: Optional[IxNonFractionPublic] = Field(default=None, description='減価償却累計額及び減損損失累計額、その他、有形固定資産')
    """ 減価償却累計額及び減損損失累計額、その他、有形固定資産 """
    accumulated_depreciation_and_impairment_loss_ppe_by_group: Optional[IxNonFractionPublic] = Field(default=None, description='減価償却累計額及び減損損失累計額、有形固定資産、一括控除')
    """ 減価償却累計額及び減損損失累計額、有形固定資産、一括控除 """
    accumulated_depreciation_and_impairment_loss_real_estate_for_investment: Optional[IxNonFractionPublic] = Field(default=None, description='減価償却累計額及び減損損失累計額、投資不動産')
    """ 減価償却累計額及び減損損失累計額、投資不動産 """
    accumulated_depreciation_and_impairment_loss_tools_furniture_and_fixtures: Optional[IxNonFractionPublic] = Field(default=None, description='減価償却累計額及び減損損失累計額、工具、器具及び備品')
    """ 減価償却累計額及び減損損失累計額、工具、器具及び備品 """
    accumulated_depreciation_buildings: Optional[IxNonFractionPublic] = Field(default=None, description='減価償却累計額、建物')
    """ 減価償却累計額、建物 """
    accumulated_depreciation_buildings_and_structures: Optional[IxNonFractionPublic] = Field(default=None, description='減価償却累計額、建物及び構築物')
    """ 減価償却累計額、建物及び構築物 """
    accumulated_depreciation_lease_assets_ppe: Optional[IxNonFractionPublic] = Field(default=None, description='減価償却累計額、リース資産、有形固定資産')
    """ 減価償却累計額、リース資産、有形固定資産 """
    accumulated_depreciation_machinery_and_equipment: Optional[IxNonFractionPublic] = Field(default=None, description='減価償却累計額、機械及び装置')
    """ 減価償却累計額、機械及び装置 """
    accumulated_depreciation_machinery_equipment_and_vehicles: Optional[IxNonFractionPublic] = Field(default=None, description='減価償却累計額、機械装置及び運搬具')
    """ 減価償却累計額、機械装置及び運搬具 """
    accumulated_depreciation_other_ppe: Optional[IxNonFractionPublic] = Field(default=None, description='減価償却累計額、その他、有形固定資産')
    """ 減価償却累計額、その他、有形固定資産 """
    accumulated_depreciation_ppe_by_group: Optional[IxNonFractionPublic] = Field(default=None, description='減価償却累計額、有形固定資産、一括控除')
    """ 減価償却累計額、有形固定資産、一括控除 """
    accumulated_depreciation_real_estate_for_investment: Optional[IxNonFractionPublic] = Field(default=None, description='減価償却累計額、投資不動産')
    """ 減価償却累計額、投資不動産 """
    accumulated_depreciation_right_of_use_assets: Optional[IxNonFractionPublic] = Field(default=None, description='減価償却累計額、使用権資産')
    """ 減価償却累計額、使用権資産 """
    accumulated_depreciation_structures: Optional[IxNonFractionPublic] = Field(default=None, description='減価償却累計額、構築物')
    """ 減価償却累計額、構築物 """
    accumulated_depreciation_tools_furniture_and_fixtures: Optional[IxNonFractionPublic] = Field(default=None, description='減価償却累計額、工具、器具及び備品')
    """ 減価償却累計額、工具、器具及び備品 """
    accumulated_depreciation_vehicles: Optional[IxNonFractionPublic] = Field(default=None, description='減価償却累計額、車両運搬具')
    """ 減価償却累計額、車両運搬具 """
    accumulated_depreciation_vessels: Optional[IxNonFractionPublic] = Field(default=None, description='減価償却累計額、船舶')
    """ 減価償却累計額、船舶 """
    accumulated_impairment_loss_buildings_and_structures: Optional[IxNonFractionPublic] = Field(default=None, description='減損損失累計額、建物及び構築物')
    """ 減損損失累計額、建物及び構築物 """
    accumulated_impairment_loss_machinery_equipment_and_vehicles: Optional[IxNonFractionPublic] = Field(default=None, description='減損損失累計額、機械装置及び運搬具')
    """ 減損損失累計額、機械装置及び運搬具 """
    accumulated_impairment_loss_other_ppe: Optional[IxNonFractionPublic] = Field(default=None, description='減損損失累計額、その他、有形固定資産')
    """ 減損損失累計額、その他、有形固定資産 """
    advance_payments_other: Optional[IxNonFractionPublic] = Field(default=None, description='前払金')
    """ 前払金 """
    advance_payments_trade: Optional[IxNonFractionPublic] = Field(default=None, description='前渡金')
    """ 前渡金 """
    advances_for_purchases_at_leased_assets_ppelea: Optional[IxNonFractionPublic] = Field(default=None, description='賃貸資産前渡金、有形固定資産、リース事業')
    """ 賃貸資産前渡金、有形固定資産、リース事業 """
    advances_paid: Optional[IxNonFractionPublic] = Field(default=None, description='立替金')
    """ 立替金 """
    advances_received: Optional[IxNonFractionPublic] = Field(default=None, description='前受金')
    """ 前受金 """
    advances_received_on_uncompleted_construction_contracts_cns: Optional[IxNonFractionPublic] = Field(default=None, description='未成工事受入金、建設業')
    """ 未成工事受入金、建設業 """
    advertising_and_promotion_expenses_sga: Optional[IxNonFractionPublic] = Field(default=None, description='広告宣伝費及び販売促進費、販売費及び一般管理費')
    """ 広告宣伝費及び販売促進費、販売費及び一般管理費 """
    advertising_expenses_sga: Optional[IxNonFractionPublic] = Field(default=None, description='広告宣伝費、販売費及び一般管理費')
    """ 広告宣伝費、販売費及び一般管理費 """
    agent_fee_sga: Optional[IxNonFractionPublic] = Field(default=None, description='代理店手数料、販売費及び一般管理費')
    """ 代理店手数料、販売費及び一般管理費 """
    allowance_for_doubtful_accounts_assets_ins: Optional[IxNonFractionPublic] = Field(default=None, description='貸倒引当金、資産の部、保険業')
    """ 貸倒引当金、資産の部、保険業 """
    allowance_for_doubtful_accounts_ca: Optional[IxNonFractionPublic] = Field(default=None, description='貸倒引当金、流動資産、一括控除')
    """ 貸倒引当金、流動資産、一括控除 """
    allowance_for_doubtful_accounts_ioa_by_group: Optional[IxNonFractionPublic] = Field(default=None, description='貸倒引当金、投資その他の資産、一括控除')
    """ 貸倒引当金、投資その他の資産、一括控除 """
    allowance_for_investment_loss: Optional[IxNonFractionPublic] = Field(default=None, description='投資損失引当金')
    """ 投資損失引当金 """
    allowance_for_investment_loss_assets_bnk: Optional[IxNonFractionPublic] = Field(default=None, description='投資損失引当金、資産の部、銀行業')
    """ 投資損失引当金、資産の部、銀行業 """
    allowance_for_loan_losses_assets_bnk: Optional[IxNonFractionPublic] = Field(default=None, description='貸倒引当金、資産の部、銀行業')
    """ 貸倒引当金、資産の部、銀行業 """
    amortization_of_bond_issuance_cost_noe: Optional[IxNonFractionPublic] = Field(default=None, description='社債発行費償却、営業外費用')
    """ 社債発行費償却、営業外費用 """
    amortization_of_bond_issuance_cost_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='社債発行費償却、営業活動によるキャッシュ・フロー')
    """ 社債発行費償却、営業活動によるキャッシュ・フロー """
    amortization_of_deferred_assets_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='繰延資産償却額、営業活動によるキャッシュ・フロー')
    """ 繰延資産償却額、営業活動によるキャッシュ・フロー """
    amortization_of_goodwill_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='のれん償却額、営業活動によるキャッシュ・フロー')
    """ のれん償却額、営業活動によるキャッシュ・フロー """
    amortization_of_goodwill_sga: Optional[IxNonFractionPublic] = Field(default=None, description='のれん償却額、販売費及び一般管理費')
    """ のれん償却額、販売費及び一般管理費 """
    amortization_of_guarantee_deposits_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='差入保証金償却額、営業活動によるキャッシュ・フロー')
    """ 差入保証金償却額、営業活動によるキャッシュ・フロー """
    amortization_of_long_term_prepaid_expenses_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='長期前払費用償却額、営業活動によるキャッシュ・フロー')
    """ 長期前払費用償却額、営業活動によるキャッシュ・フロー """
    amortization_of_negative_goodwill_noi: Optional[IxNonFractionPublic] = Field(default=None, description='負ののれん償却額、営業外収益')
    """ 負ののれん償却額、営業外収益 """
    amortization_of_negative_goodwill_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='負ののれん償却額、営業活動によるキャッシュ・フロー')
    """ 負ののれん償却額、営業活動によるキャッシュ・フロー """
    amortization_of_stock_issuance_cost_noe: Optional[IxNonFractionPublic] = Field(default=None, description='株式交付費償却、営業外費用')
    """ 株式交付費償却、営業外費用 """
    asset_retirement_obligations_cl: Optional[IxNonFractionPublic] = Field(default=None, description='資産除去債務、流動負債')
    """ 資産除去債務、流動負債 """
    asset_retirement_obligations_liabilities: Optional[IxNonFractionPublic] = Field(default=None, description='資産除去債務、負債の部')
    """ 資産除去債務、負債の部 """
    asset_retirement_obligations_ncl: Optional[IxNonFractionPublic] = Field(default=None, description='資産除去債務、固定負債')
    """ 資産除去債務、固定負債 """
    assets: Optional[IxNonFractionPublic] = Field(default=None, description='資産')
    """ 資産 """
    assets_for_rent_net: Optional[IxNonFractionPublic] = Field(default=None, description='貸与資産（純額）')
    """ 貸与資産（純額） """
    bad_debts_expenses_noe: Optional[IxNonFractionPublic] = Field(default=None, description='貸倒損失、営業外費用')
    """ 貸倒損失、営業外費用 """
    bad_debts_expenses_sga: Optional[IxNonFractionPublic] = Field(default=None, description='貸倒損失、販売費及び一般管理費')
    """ 貸倒損失、販売費及び一般管理費 """
    bad_debts_written_off_el: Optional[IxNonFractionPublic] = Field(default=None, description='貸倒損失、特別損失')
    """ 貸倒損失、特別損失 """
    beginning_finished_goods_cos: Optional[IxNonFractionPublic] = Field(default=None, description='製品期首棚卸高、売上原価')
    """ 製品期首棚卸高、売上原価 """
    beginning_merchandise_and_finished_goods_cos: Optional[IxNonFractionPublic] = Field(default=None, description='商品及び製品期首棚卸高、売上原価')
    """ 商品及び製品期首棚卸高、売上原価 """
    bond_issuance_cost_da: Optional[IxNonFractionPublic] = Field(default=None, description='社債発行費、繰延資産')
    """ 社債発行費、繰延資産 """
    bond_issuance_cost_noe: Optional[IxNonFractionPublic] = Field(default=None, description='社債発行費、営業外費用')
    """ 社債発行費、営業外費用 """
    bond_issuance_cost_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='社債発行費、営業活動によるキャッシュ・フロー')
    """ 社債発行費、営業活動によるキャッシュ・フロー """
    bonds_payable: Optional[IxNonFractionPublic] = Field(default=None, description='社債')
    """ 社債 """
    bonuses_and_allowance_sga: Optional[IxNonFractionPublic] = Field(default=None, description='賞与及び手当、販売費及び一般管理費')
    """ 賞与及び手当、販売費及び一般管理費 """
    bonuses_sga: Optional[IxNonFractionPublic] = Field(default=None, description='賞与、販売費及び一般管理費')
    """ 賞与、販売費及び一般管理費 """
    borrowed_money_from_trust_account_liabilities_bnk: Optional[IxNonFractionPublic] = Field(default=None, description='信託勘定借、負債の部、銀行業')
    """ 信託勘定借、負債の部、銀行業 """
    borrowed_money_liabilities_bnk: Optional[IxNonFractionPublic] = Field(default=None, description='借用金、負債の部、銀行業')
    """ 借用金、負債の部、銀行業 """
    brokerage_income_orcmd: Optional[IxNonFractionPublic] = Field(default=None, description='受取手数料、営業収益、商品先物取引業')
    """ 受取手数料、営業収益、商品先物取引業 """
    buildings: Optional[IxNonFractionPublic] = Field(default=None, description='建物')
    """ 建物 """
    buildings_and_accompanying_facilities: Optional[IxNonFractionPublic] = Field(default=None, description='建物附属設備')
    """ 建物附属設備 """
    buildings_and_accompanying_facilities_net: Optional[IxNonFractionPublic] = Field(default=None, description='建物附属設備（純額）')
    """ 建物附属設備（純額） """
    buildings_and_structures: Optional[IxNonFractionPublic] = Field(default=None, description='建物及び構築物')
    """ 建物及び構築物 """
    buildings_and_structures_net: Optional[IxNonFractionPublic] = Field(default=None, description='建物及び構築物（純額）')
    """ 建物及び構築物（純額） """
    buildings_net: Optional[IxNonFractionPublic] = Field(default=None, description='建物（純額）')
    """ 建物（純額） """
    business_advisory_fee_noi: Optional[IxNonFractionPublic] = Field(default=None, description='経営指導料、営業外収益')
    """ 経営指導料、営業外収益 """
    business_commencement_expenses_da: Optional[IxNonFractionPublic] = Field(default=None, description='開業費、繰延資産')
    """ 開業費、繰延資産 """
    business_consignment_expenses_sga: Optional[IxNonFractionPublic] = Field(default=None, description='業務委託費、販売費及び一般管理費')
    """ 業務委託費、販売費及び一般管理費 """
    business_structure_improvement_expenses_el: Optional[IxNonFractionPublic] = Field(default=None, description='事業構造改善費用、特別損失')
    """ 事業構造改善費用、特別損失 """
    business_structure_improvement_expenses_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='事業構造改善費用、営業活動によるキャッシュ・フロー')
    """ 事業構造改善費用、営業活動によるキャッシュ・フロー """
    call_loans_and_bills_bought_assets_bnk: Optional[IxNonFractionPublic] = Field(default=None, description='コールローン及び買入手形、資産の部、銀行業')
    """ コールローン及び買入手形、資産の部、銀行業 """
    call_loans_assets_bnk: Optional[IxNonFractionPublic] = Field(default=None, description='コールローン、資産の部、銀行業')
    """ コールローン、資産の部、銀行業 """
    call_money_and_bills_sold_liabilities_bnk: Optional[IxNonFractionPublic] = Field(default=None, description='コールマネー及び売渡手形、負債の部、銀行業')
    """ コールマネー及び売渡手形、負債の部、銀行業 """
    call_money_liabilities_bnk: Optional[IxNonFractionPublic] = Field(default=None, description='コールマネー、負債の部、銀行業')
    """ コールマネー、負債の部、銀行業 """
    capital_stock: Optional[IxNonFractionPublic] = Field(default=None, description='資本金')
    """ 資本金 """
    capital_surplus: Optional[IxNonFractionPublic] = Field(default=None, description='資本剰余金')
    """ 資本剰余金 """
    cash_and_cash_equivalents: Optional[IxNonFractionPublic] = Field(default=None, description='現金及び現金同等物の残高')
    """ 現金及び現金同等物の残高 """
    cash_and_deposits: Optional[IxNonFractionPublic] = Field(default=None, description='現金及び預金')
    """ 現金及び預金 """
    cash_and_deposits_assets_ins: Optional[IxNonFractionPublic] = Field(default=None, description='現金及び預貯金、資産の部、保険業')
    """ 現金及び預貯金、資産の部、保険業 """
    cash_and_due_from_banks_assets_bnk: Optional[IxNonFractionPublic] = Field(default=None, description='現金預け金、資産の部、銀行業')
    """ 現金預け金、資産の部、銀行業 """
    cash_dividends_paid_fin_cf: Optional[IxNonFractionPublic] = Field(default=None, description='配当金の支払額、財務活動によるキャッシュ・フロー')
    """ 配当金の支払額、財務活動によるキャッシュ・フロー """
    change_in_treasury_shares_of_parent_arising_from_transactions_with_non_controlling_shareholders: Optional[IxNonFractionPublic] = Field(default=None, description='非支配株主との取引に係る親会社の持分変動')
    """ 非支配株主との取引に係る親会社の持分変動 """
    change_of_scope_of_consolidation: Optional[IxNonFractionPublic] = Field(default=None, description='連結範囲の変動')
    """ 連結範囲の変動 """
    change_of_scope_of_equity_method: Optional[IxNonFractionPublic] = Field(default=None, description='持分法の適用範囲の変動')
    """ 持分法の適用範囲の変動 """
    claims_provable_in_bankruptcy_claims_provable_in_rehabilitation_and_other: Optional[IxNonFractionPublic] = Field(default=None, description='破産更生債権等')
    """ 破産更生債権等 """
    co_sponsor_fee_noi: Optional[IxNonFractionPublic] = Field(default=None, description='協賛金収入、営業外収益')
    """ 協賛金収入、営業外収益 """
    coinsurance_accounts_receivable_assets_ins: Optional[IxNonFractionPublic] = Field(default=None, description='共同保険貸、資産の部、保険業')
    """ 共同保険貸、資産の部、保険業 """
    collection_of_investment_and_loans_receivable_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='投融資の回収による収入、投資活動によるキャッシュ・フロー')
    """ 投融資の回収による収入、投資活動によるキャッシュ・フロー """
    collection_of_lease_deposits_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='敷金の回収による収入、投資活動によるキャッシュ・フロー')
    """ 敷金の回収による収入、投資活動によるキャッシュ・フロー """
    collection_of_loans_receivable_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='貸付金の回収による収入、投資活動によるキャッシュ・フロー')
    """ 貸付金の回収による収入、投資活動によるキャッシュ・フロー """
    collection_of_loans_receivable_to_employees_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='従業員に対する貸付金の回収による収入、投資活動によるキャッシュ・フロー')
    """ 従業員に対する貸付金の回収による収入、投資活動によるキャッシュ・フロー """
    collection_of_long_term_loans_receivable_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='長期貸付金の回収による収入、投資活動によるキャッシュ・フロー')
    """ 長期貸付金の回収による収入、投資活動によるキャッシュ・フロー """
    collection_of_long_term_loans_receivable_to_employees_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='従業員に対する長期貸付金の回収による収入、投資活動によるキャッシュ・フロー')
    """ 従業員に対する長期貸付金の回収による収入、投資活動によるキャッシュ・フロー """
    collection_of_short_term_loans_receivable_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='短期貸付金の回収による収入、投資活動によるキャッシュ・フロー')
    """ 短期貸付金の回収による収入、投資活動によるキャッシュ・フロー """
    commercial_papers_liabilities: Optional[IxNonFractionPublic] = Field(default=None, description='コマーシャル・ペーパー')
    """ コマーシャル・ペーパー """
    commission_fee_noe: Optional[IxNonFractionPublic] = Field(default=None, description='支払手数料、営業外費用')
    """ 支払手数料、営業外費用 """
    commission_fee_noi: Optional[IxNonFractionPublic] = Field(default=None, description='受取手数料、営業外収益')
    """ 受取手数料、営業外収益 """
    commission_fee_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='支払手数料、営業活動によるキャッシュ・フロー')
    """ 支払手数料、営業活動によるキャッシュ・フロー """
    commission_fee_sga: Optional[IxNonFractionPublic] = Field(default=None, description='支払手数料、販売費及び一般管理費')
    """ 支払手数料、販売費及び一般管理費 """
    commission_for_purchase_of_treasury_stock_noe: Optional[IxNonFractionPublic] = Field(default=None, description='自己株式取得費用、営業外費用')
    """ 自己株式取得費用、営業外費用 """
    commission_for_syndicate_loan_noe: Optional[IxNonFractionPublic] = Field(default=None, description='シンジケートローン手数料、営業外費用')
    """ シンジケートローン手数料、営業外費用 """
    commission_income_rev_oa: Optional[IxNonFractionPublic] = Field(default=None, description='手数料収入、営業活動による収益')
    """ 手数料収入、営業活動による収益 """
    commissions_and_collection_fees_oeins: Optional[IxNonFractionPublic] = Field(default=None, description='諸手数料及び集金費、経常費用、保険業')
    """ 諸手数料及び集金費、経常費用、保険業 """
    commissions_from_subsidiaries_and_affiliates_rev_oa: Optional[IxNonFractionPublic] = Field(default=None, description='関係会社受入手数料、営業活動による収益')
    """ 関係会社受入手数料、営業活動による収益 """
    commitment_fee_noe: Optional[IxNonFractionPublic] = Field(default=None, description='コミットメントフィー、営業外費用')
    """ コミットメントフィー、営業外費用 """
    communication_expenses_sga: Optional[IxNonFractionPublic] = Field(default=None, description='通信費、販売費及び一般管理費')
    """ 通信費、販売費及び一般管理費 """
    compensation_expenses_noe: Optional[IxNonFractionPublic] = Field(default=None, description='支払補償費、営業外費用')
    """ 支払補償費、営業外費用 """
    compensation_for_damage_el: Optional[IxNonFractionPublic] = Field(default=None, description='損害賠償金、特別損失')
    """ 損害賠償金、特別損失 """
    compensation_for_damage_paid_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='損害賠償金の支払額、営業活動によるキャッシュ・フロー')
    """ 損害賠償金の支払額、営業活動によるキャッシュ・フロー """
    compensation_for_removal_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='移転補償金、営業活動によるキャッシュ・フロー')
    """ 移転補償金、営業活動によるキャッシュ・フロー """
    compensation_for_transfer_ei: Optional[IxNonFractionPublic] = Field(default=None, description='移転補償金、特別利益')
    """ 移転補償金、特別利益 """
    compensation_income_ei: Optional[IxNonFractionPublic] = Field(default=None, description='受取補償金、特別利益')
    """ 受取補償金、特別利益 """
    compensation_income_for_expropriation_ei: Optional[IxNonFractionPublic] = Field(default=None, description='収用補償金、特別利益')
    """ 収用補償金、特別利益 """
    compensation_income_for_expropriation_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='収用補償金、営業活動によるキャッシュ・フロー')
    """ 収用補償金、営業活動によるキャッシュ・フロー """
    compensation_income_noi: Optional[IxNonFractionPublic] = Field(default=None, description='受取補償金、営業外収益')
    """ 受取補償金、営業外収益 """
    compensation_income_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='受取補償金、営業活動によるキャッシュ・フロー')
    """ 受取補償金、営業活動によるキャッシュ・フロー """
    compensations_sga: Optional[IxNonFractionPublic] = Field(default=None, description='支払報酬、販売費及び一般管理費')
    """ 支払報酬、販売費及び一般管理費 """
    compensations_salaries_and_allowances_sga: Optional[IxNonFractionPublic] = Field(default=None, description='報酬及び給料手当、販売費及び一般管理費')
    """ 報酬及び給料手当、販売費及び一般管理費 """
    comprehensive_income: Optional[IxNonFractionPublic] = Field(default=None, description='包括利益')
    """ 包括利益 """
    comprehensive_income_attributable_to_non_controlling_interests: Optional[IxNonFractionPublic] = Field(default=None, description='非支配株主に係る包括利益、包括利益')
    """ 非支配株主に係る包括利益、包括利益 """
    comprehensive_income_attributable_to_owners_of_the_parent: Optional[IxNonFractionPublic] = Field(default=None, description='親会社株主に係る包括利益、包括利益')
    """ 親会社株主に係る包括利益、包括利益 """
    construction_assistance_fund_receivables: Optional[IxNonFractionPublic] = Field(default=None, description='建設協力金')
    """ 建設協力金 """
    construction_in_progress: Optional[IxNonFractionPublic] = Field(default=None, description='建設仮勘定')
    """ 建設仮勘定 """
    consumption_taxes_receivable: Optional[IxNonFractionPublic] = Field(default=None, description='未収消費税等')
    """ 未収消費税等 """
    contract_assets: Optional[IxNonFractionPublic] = Field(default=None, description='契約資産')
    """ 契約資産 """
    contract_liabilities: Optional[IxNonFractionPublic] = Field(default=None, description='契約負債')
    """ 契約負債 """
    contribution_for_construction_ei: Optional[IxNonFractionPublic] = Field(default=None, description='工事負担金等受入額、特別利益')
    """ 工事負担金等受入額、特別利益 """
    contribution_noe: Optional[IxNonFractionPublic] = Field(default=None, description='寄付金、営業外費用')
    """ 寄付金、営業外費用 """
    contribution_sga: Optional[IxNonFractionPublic] = Field(default=None, description='寄付金、販売費及び一般管理費')
    """ 寄付金、販売費及び一般管理費 """
    convertible_bond_type_bonds_with_subscription_rights_to_shares: Optional[IxNonFractionPublic] = Field(default=None, description='転換社債型新株予約権付社債')
    """ 転換社債型新株予約権付社債 """
    correspondence_and_transportation_expenses_sga: Optional[IxNonFractionPublic] = Field(default=None, description='通信交通費、販売費及び一般管理費')
    """ 通信交通費、販売費及び一般管理費 """
    cost_of_finished_goods_sold: Optional[IxNonFractionPublic] = Field(default=None, description='製品売上原価')
    """ 製品売上原価 """
    cost_of_goods_sold: Optional[IxNonFractionPublic] = Field(default=None, description='商品売上原価')
    """ 商品売上原価 """
    cost_of_lease_revenue_noe: Optional[IxNonFractionPublic] = Field(default=None, description='賃貸収入原価、営業外費用')
    """ 賃貸収入原価、営業外費用 """
    cost_of_merchandise_and_finished_goods_sold_cos: Optional[IxNonFractionPublic] = Field(default=None, description='商品及び製品売上原価、売上原価')
    """ 商品及び製品売上原価、売上原価 """
    cost_of_products_manufactured: Optional[IxNonFractionPublic] = Field(default=None, description='当期製品製造原価')
    """ 当期製品製造原価 """
    cost_of_purchased_goods: Optional[IxNonFractionPublic] = Field(default=None, description='当期商品仕入高')
    """ 当期商品仕入高 """
    cost_of_sales: Optional[IxNonFractionPublic] = Field(default=None, description='売上原価')
    """ 売上原価 """
    cost_of_sales_of_completed_construction_contracts_cns: Optional[IxNonFractionPublic] = Field(default=None, description='完成工事原価、建設業')
    """ 完成工事原価、建設業 """
    cost_of_sales_on_other_business_cos_exp_oa: Optional[IxNonFractionPublic] = Field(default=None, description='その他の事業売上原価、営業活動による費用・売上原価')
    """ その他の事業売上原価、営業活動による費用・売上原価 """
    cost_of_sales_on_real_estate_business_and_other_cns: Optional[IxNonFractionPublic] = Field(default=None, description='不動産事業等売上原価、建設業')
    """ 不動産事業等売上原価、建設業 """
    cost_of_sales_on_real_estate_business_cos_exp_oa: Optional[IxNonFractionPublic] = Field(default=None, description='不動産事業売上原価、営業活動による費用・売上原価')
    """ 不動産事業売上原価、営業活動による費用・売上原価 """
    cost_of_sales_on_side_line_business_cns: Optional[IxNonFractionPublic] = Field(default=None, description='兼業事業売上原価、建設業')
    """ 兼業事業売上原価、建設業 """
    costs_on_real_estate_business: Optional[IxNonFractionPublic] = Field(default=None, description='不動産事業支出金')
    """ 不動産事業支出金 """
    costs_on_uncompleted_construction_contracts_and_other_cns: Optional[IxNonFractionPublic] = Field(default=None, description='未成工事支出金等、建設業')
    """ 未成工事支出金等、建設業 """
    costs_on_uncompleted_construction_contracts_cns: Optional[IxNonFractionPublic] = Field(default=None, description='未成工事支出金、建設業')
    """ 未成工事支出金、建設業 """
    costs_on_uncompleted_services: Optional[IxNonFractionPublic] = Field(default=None, description='未成業務支出金')
    """ 未成業務支出金 """
    credit_card_revenue_rev_oa: Optional[IxNonFractionPublic] = Field(default=None, description='包括信用購入あっせん収益、営業活動による収益')
    """ 包括信用購入あっせん収益、営業活動による収益 """
    cumulative_effects_of_changes_in_accounting_policies: Optional[IxNonFractionPublic] = Field(default=None, description='会計方針の変更による累積的影響額')
    """ 会計方針の変更による累積的影響額 """
    current_assets: Optional[IxNonFractionPublic] = Field(default=None, description='流動資産')
    """ 流動資産 """
    current_liabilities: Optional[IxNonFractionPublic] = Field(default=None, description='流動負債')
    """ 流動負債 """
    current_portion_of_bonds: Optional[IxNonFractionPublic] = Field(default=None, description='１年内償還予定の社債')
    """ １年内償還予定の社債 """
    current_portion_of_bonds_with_subscription_rights_to_shares: Optional[IxNonFractionPublic] = Field(default=None, description='１年内償還予定の新株予約権付社債')
    """ １年内償還予定の新株予約権付社債 """
    current_portion_of_convertible_bonds: Optional[IxNonFractionPublic] = Field(default=None, description='１年内償還予定の転換社債')
    """ １年内償還予定の転換社債 """
    current_portion_of_long_term_loans_payable: Optional[IxNonFractionPublic] = Field(default=None, description='１年内返済予定の長期借入金')
    """ １年内返済予定の長期借入金 """
    current_portion_of_long_term_loans_payable_to_subsidiaries_and_affiliates: Optional[IxNonFractionPublic] = Field(default=None, description='１年内返済予定の関係会社長期借入金')
    """ １年内返済予定の関係会社長期借入金 """
    current_portion_of_long_term_loans_receivable: Optional[IxNonFractionPublic] = Field(default=None, description='１年内回収予定の長期貸付金')
    """ １年内回収予定の長期貸付金 """
    current_portion_of_long_term_payables_under_fluidity_lease_receivables_cllea: Optional[IxNonFractionPublic] = Field(default=None, description='１年内支払予定の債権流動化に伴う長期支払債務、流動負債、リース事業')
    """ １年内支払予定の債権流動化に伴う長期支払債務、流動負債、リース事業 """
    current_portion_of_noncurrent_liabilities_clgas: Optional[IxNonFractionPublic] = Field(default=None, description='１年以内に期限到来の固定負債、流動負債、ガス事業')
    """ １年以内に期限到来の固定負債、流動負債、ガス事業 """
    current_portion_of_other_noncurrent_liabilities: Optional[IxNonFractionPublic] = Field(default=None, description='１年内期限到来予定のその他の固定負債')
    """ １年内期限到来予定のその他の固定負債 """
    customer_related_intangible_assets: Optional[IxNonFractionPublic] = Field(default=None, description='顧客関連資産')
    """ 顧客関連資産 """
    customers_deposits_received_for_commodity_futures_transaction_clcmd: Optional[IxNonFractionPublic] = Field(default=None, description='預り証拠金、流動負債、商品先物取引業')
    """ 預り証拠金、流動負債、商品先物取引業 """
    customers_liabilities_for_acceptances_and_guarantees_assets_bnk: Optional[IxNonFractionPublic] = Field(default=None, description='支払承諾見返、資産の部、銀行業')
    """ 支払承諾見返、資産の部、銀行業 """
    decrease_by_corporate_divisionsplitoff_type: Optional[IxNonFractionPublic] = Field(default=None, description='分割型の会社分割による減少')
    """ 分割型の会社分割による減少 """
    decrease_in_cash_and_cash_equivalents_resulting_from_exclusion_of_subsidiaries_from_consolidation_cce: Optional[IxNonFractionPublic] = Field(default=None, description='連結除外に伴う現金及び現金同等物の減少額')
    """ 連結除外に伴う現金及び現金同等物の減少額 """
    decrease_in_money_held_in_trust_inv_cfbnk: Optional[IxNonFractionPublic] = Field(default=None, description='金銭の信託の減少による収入、投資活動によるキャッシュ・フロー、銀行業')
    """ 金銭の信託の減少による収入、投資活動によるキャッシュ・フロー、銀行業 """
    decrease_in_short_term_loans_payable_fin_cf: Optional[IxNonFractionPublic] = Field(default=None, description='短期借入金の返済による支出、財務活動によるキャッシュ・フロー')
    """ 短期借入金の返済による支出、財務活動によるキャッシュ・フロー """
    decrease_increase_in_accounts_receivable_installment_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='割賦売掛金の増減額（△は増加）、営業活動によるキャッシュ・フロー')
    """ 割賦売掛金の増減額（△は増加）、営業活動によるキャッシュ・フロー """
    decrease_increase_in_accounts_receivable_other_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='未収入金の増減額（△は増加）、営業活動によるキャッシュ・フロー')
    """ 未収入金の増減額（△は増加）、営業活動によるキャッシュ・フロー """
    decrease_increase_in_accounts_receivable_trade_and_contract_assets_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='売上債権及び契約資産の増減額（△は増加）、営業活動によるキャッシュ・フロー')
    """ 売上債権及び契約資産の増減額（△は増加）、営業活動によるキャッシュ・フロー """
    decrease_increase_in_advance_payments_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='前渡金の増減額（△は増加）、営業活動によるキャッシュ・フロー')
    """ 前渡金の増減額（△は増加）、営業活動によるキャッシュ・フロー """
    decrease_increase_in_advances_paid_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='立替金の増減額（△は増加）、営業活動によるキャッシュ・フロー')
    """ 立替金の増減額（△は増加）、営業活動によるキャッシュ・フロー """
    decrease_increase_in_claims_provable_in_bankruptcy_claims_provable_in_rehabilitation_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='破産更生債権等の増減額（△は増加）、営業活動によるキャッシュ・フロー')
    """ 破産更生債権等の増減額（△は増加）、営業活動によるキャッシュ・フロー """
    decrease_increase_in_consumption_taxes_receivable_payable_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='未払又は未収消費税等の増減額、営業活動によるキャッシュ・フロー')
    """ 未払又は未収消費税等の増減額、営業活動によるキャッシュ・フロー """
    decrease_increase_in_consumption_taxes_refund_receivable_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='未収消費税等の増減額（△は増加）、営業活動によるキャッシュ・フロー')
    """ 未収消費税等の増減額（△は増加）、営業活動によるキャッシュ・フロー """
    decrease_increase_in_costs_on_uncompleted_construction_contracts_and_other_ope_cfcns: Optional[IxNonFractionPublic] = Field(default=None, description='未成工事支出金等の増減額（△は増加）、営業活動によるキャッシュ・フロー、建設業')
    """ 未成工事支出金等の増減額（△は増加）、営業活動によるキャッシュ・フロー、建設業 """
    decrease_increase_in_costs_on_uncompleted_construction_contracts_ope_cfcns: Optional[IxNonFractionPublic] = Field(default=None, description='未成工事支出金の増減額（△は増加）、営業活動によるキャッシュ・フロー、建設業')
    """ 未成工事支出金の増減額（△は増加）、営業活動によるキャッシュ・フロー、建設業 """
    decrease_increase_in_deposits_paid_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='預け金の増減額（△は増加）、営業活動によるキャッシュ・フロー')
    """ 預け金の増減額（△は増加）、営業活動によるキャッシュ・フロー """
    decrease_increase_in_guarantee_deposits_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='差入保証金の増減額（△は増加）、営業活動によるキャッシュ・フロー')
    """ 差入保証金の増減額（△は増加）、営業活動によるキャッシュ・フロー """
    decrease_increase_in_inventories_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='棚卸資産の増減額（△は増加）、営業活動によるキャッシュ・フロー')
    """ 棚卸資産の増減額（△は増加）、営業活動によるキャッシュ・フロー """
    decrease_increase_in_investment_securities_for_sale_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='営業投資有価証券の増減額（△は増加）、営業活動によるキャッシュ・フロー')
    """ 営業投資有価証券の増減額（△は増加）、営業活動によるキャッシュ・フロー """
    decrease_increase_in_lease_investment_assets_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='リース投資資産の増減額（△は増加）、営業活動によるキャッシュ・フロー')
    """ リース投資資産の増減額（△は増加）、営業活動によるキャッシュ・フロー """
    decrease_increase_in_long_term_prepaid_expenses_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='長期前払費用の増減額（△は増加）、営業活動によるキャッシュ・フロー')
    """ 長期前払費用の増減額（△は増加）、営業活動によるキャッシュ・フロー """
    decrease_increase_in_notes_and_accounts_receivable_trade_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='売上債権の増減額（△は増加）、営業活動によるキャッシュ・フロー')
    """ 売上債権の増減額（△は増加）、営業活動によるキャッシュ・フロー """
    decrease_increase_in_operating_loans_receivable_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='営業貸付金の増減額（△は増加）、営業活動によるキャッシュ・フロー')
    """ 営業貸付金の増減額（△は増加）、営業活動によるキャッシュ・フロー """
    decrease_increase_in_other_assets_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='その他の資産の増減額（△は増加）、営業活動によるキャッシュ・フロー')
    """ その他の資産の増減額（△は増加）、営業活動によるキャッシュ・フロー """
    decrease_increase_in_other_current_assets_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='その他の流動資産の増減額（△は増加）、営業活動によるキャッシュ・フロー')
    """ その他の流動資産の増減額（△は増加）、営業活動によるキャッシュ・フロー """
    decrease_increase_in_other_inventories_ope_cfcns: Optional[IxNonFractionPublic] = Field(default=None, description='その他の棚卸資産の増減額（△は増加）、営業活動によるキャッシュ・フロー、建設業')
    """ その他の棚卸資産の増減額（△は増加）、営業活動によるキャッシュ・フロー、建設業 """
    decrease_increase_in_other_investing_and_financing_activities_assets_ope_cfins: Optional[IxNonFractionPublic] = Field(default=None, description='その他資産（除く投資活動関連、財務活動関連）の増減額（△は増加）、営業活動によるキャッシュ・フロー、保険業')
    """ その他資産（除く投資活動関連、財務活動関連）の増減額（△は増加）、営業活動によるキャッシュ・フロー、保険業 """
    decrease_increase_in_other_investments_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='投資その他の資産の増減額（△は増加）、投資活動によるキャッシュ・フロー')
    """ 投資その他の資産の増減額（△は増加）、投資活動によるキャッシュ・フロー """
    decrease_increase_in_other_noncurrent_assets_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='その他の固定資産の増減額（△は増加）、営業活動によるキャッシュ・フロー')
    """ その他の固定資産の増減額（△は増加）、営業活動によるキャッシュ・フロー """
    decrease_increase_in_prepaid_expenses_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='前払費用の増減額（△は増加）、営業活動によるキャッシュ・フロー')
    """ 前払費用の増減額（△は増加）、営業活動によるキャッシュ・フロー """
    decrease_increase_in_prepaid_pension_costs_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='前払年金費用の増減額（△は増加）、営業活動によるキャッシュ・フロー')
    """ 前払年金費用の増減額（△は増加）、営業活動によるキャッシュ・フロー """
    decrease_increase_in_real_estate_for_sale_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='販売用不動産の増減額（△は増加）、営業活動によるキャッシュ・フロー')
    """ 販売用不動産の増減額（△は増加）、営業活動によるキャッシュ・フロー """
    decrease_increase_in_short_term_investment_securities_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='有価証券の増減額（△は増加）、投資活動によるキャッシュ・フロー')
    """ 有価証券の増減額（△は増加）、投資活動によるキャッシュ・フロー """
    decrease_increase_in_short_term_loans_receivable_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='短期貸付金の増減額（△は増加）、投資活動によるキャッシュ・フロー')
    """ 短期貸付金の増減額（△は増加）、投資活動によるキャッシュ・フロー """
    decrease_increase_in_supplies_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='貯蔵品の増減額（△は増加）、営業活動によるキャッシュ・フロー')
    """ 貯蔵品の増減額（△は増加）、営業活動によるキャッシュ・フロー """
    decrease_increase_in_time_deposits_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='定期預金の増減額（△は増加）、投資活動によるキャッシュ・フロー')
    """ 定期預金の増減額（△は増加）、投資活動によるキャッシュ・フロー """
    decrease_increase_in_treasury_stock_fin_cf: Optional[IxNonFractionPublic] = Field(default=None, description='自己株式の増減額（△は増加）、財務活動によるキャッシュ・フロー')
    """ 自己株式の増減額（△は増加）、財務活動によるキャッシュ・フロー """
    deferred_and_prepaid_expenses_cawat: Optional[IxNonFractionPublic] = Field(default=None, description='繰延及び前払費用、流動資産、海運業')
    """ 繰延及び前払費用、流動資産、海運業 """
    deferred_assets: Optional[IxNonFractionPublic] = Field(default=None, description='繰延資産')
    """ 繰延資産 """
    deferred_gains_or_losses_on_hedges: Optional[IxNonFractionPublic] = Field(default=None, description='繰延ヘッジ損益')
    """ 繰延ヘッジ損益 """
    deferred_gains_or_losses_on_hedges_before_tax_oci: Optional[IxNonFractionPublic] = Field(default=None, description='繰延ヘッジ損益（税引前）、その他の包括利益')
    """ 繰延ヘッジ損益（税引前）、その他の包括利益 """
    deferred_gains_or_losses_on_hedges_net_of_tax_oci: Optional[IxNonFractionPublic] = Field(default=None, description='繰延ヘッジ損益（税引後）、その他の包括利益')
    """ 繰延ヘッジ損益（税引後）、その他の包括利益 """
    deferred_organization_expenses_da: Optional[IxNonFractionPublic] = Field(default=None, description='創立費、繰延資産')
    """ 創立費、繰延資産 """
    deferred_profit_on_installment_sales_cllea: Optional[IxNonFractionPublic] = Field(default=None, description='割賦未実現利益、流動負債、リース事業')
    """ 割賦未実現利益、流動負債、リース事業 """
    deferred_tax_assets: Optional[IxNonFractionPublic] = Field(default=None, description='繰延税金資産')
    """ 繰延税金資産 """
    deferred_tax_assets_for_land_revaluation: Optional[IxNonFractionPublic] = Field(default=None, description='再評価に係る繰延税金資産')
    """ 再評価に係る繰延税金資産 """
    deferred_tax_liabilities: Optional[IxNonFractionPublic] = Field(default=None, description='繰延税金負債')
    """ 繰延税金負債 """
    deferred_tax_liabilities_for_land_revaluation: Optional[IxNonFractionPublic] = Field(default=None, description='再評価に係る繰延税金負債')
    """ 再評価に係る繰延税金負債 """
    deposit_received_real_estate: Optional[IxNonFractionPublic] = Field(default=None, description='不動産事業受入金')
    """ 不動産事業受入金 """
    deposits_liabilities_bnk: Optional[IxNonFractionPublic] = Field(default=None, description='預金、負債の部、銀行業')
    """ 預金、負債の部、銀行業 """
    deposits_paid: Optional[IxNonFractionPublic] = Field(default=None, description='預け金')
    """ 預け金 """
    deposits_received: Optional[IxNonFractionPublic] = Field(default=None, description='預り金')
    """ 預り金 """
    deposits_received_from_employees: Optional[IxNonFractionPublic] = Field(default=None, description='従業員預り金')
    """ 従業員預り金 """
    deposits_received_from_members: Optional[IxNonFractionPublic] = Field(default=None, description='会員預り金')
    """ 会員預り金 """
    depreciation_and_amortization_on_other_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='その他の償却額、営業活動によるキャッシュ・フロー')
    """ その他の償却額、営業活動によるキャッシュ・フロー """
    depreciation_and_amortization_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='減価償却費、営業活動によるキャッシュ・フロー')
    """ 減価償却費、営業活動によるキャッシュ・フロー """
    depreciation_and_other_amortization_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='減価償却費及びその他の償却費、営業活動によるキャッシュ・フロー')
    """ 減価償却費及びその他の償却費、営業活動によるキャッシュ・フロー """
    depreciation_noe: Optional[IxNonFractionPublic] = Field(default=None, description='減価償却費、営業外費用')
    """ 減価償却費、営業外費用 """
    depreciation_of_assets_for_rent_noe: Optional[IxNonFractionPublic] = Field(default=None, description='貸与資産減価償却費、営業外費用')
    """ 貸与資産減価償却費、営業外費用 """
    depreciation_of_intangible_assets_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='無形固定資産償却費、営業活動によるキャッシュ・フロー')
    """ 無形固定資産償却費、営業活動によるキャッシュ・フロー """
    depreciation_of_software_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='ソフトウエア償却費、営業活動によるキャッシュ・フロー')
    """ ソフトウエア償却費、営業活動によるキャッシュ・フロー """
    depreciation_sga: Optional[IxNonFractionPublic] = Field(default=None, description='減価償却費、販売費及び一般管理費')
    """ 減価償却費、販売費及び一般管理費 """
    directors_compensations_sga: Optional[IxNonFractionPublic] = Field(default=None, description='役員報酬、販売費及び一般管理費')
    """ 役員報酬、販売費及び一般管理費 """
    directors_compensations_salaries_and_allowances_sga: Optional[IxNonFractionPublic] = Field(default=None, description='役員報酬及び給料手当、販売費及び一般管理費')
    """ 役員報酬及び給料手当、販売費及び一般管理費 """
    directors_retirement_benefits_el: Optional[IxNonFractionPublic] = Field(default=None, description='役員退職慰労金、特別損失')
    """ 役員退職慰労金、特別損失 """
    directors_retirement_benefits_sga: Optional[IxNonFractionPublic] = Field(default=None, description='役員退職慰労金、販売費及び一般管理費')
    """ 役員退職慰労金、販売費及び一般管理費 """
    disposal_of_treasury_stock: Optional[IxNonFractionPublic] = Field(default=None, description='自己株式の処分')
    """ 自己株式の処分 """
    distribution_expenses_sga: Optional[IxNonFractionPublic] = Field(default=None, description='配送費、販売費及び一般管理費')
    """ 配送費、販売費及び一般管理費 """
    distribution_facilities_ppegas: Optional[IxNonFractionPublic] = Field(default=None, description='供給設備、有形固定資産、ガス事業')
    """ 供給設備、有形固定資産、ガス事業 """
    dividends_distribution_from_silent_partnership: Optional[IxNonFractionPublic] = Field(default=None, description='匿名組合損益分配額')
    """ 匿名組合損益分配額 """
    dividends_from_subsidiaries_and_affiliates_rev_oa: Optional[IxNonFractionPublic] = Field(default=None, description='関係会社受取配当金、営業活動による収益')
    """ 関係会社受取配当金、営業活動による収益 """
    dividends_from_surplus: Optional[IxNonFractionPublic] = Field(default=None, description='剰余金の配当')
    """ 剰余金の配当 """
    dividends_income_noi: Optional[IxNonFractionPublic] = Field(default=None, description='受取配当金、営業外収益')
    """ 受取配当金、営業外収益 """
    dividends_income_of_insurance_noi: Optional[IxNonFractionPublic] = Field(default=None, description='保険配当金、営業外収益')
    """ 保険配当金、営業外収益 """
    dividends_income_of_life_insurance_noi: Optional[IxNonFractionPublic] = Field(default=None, description='生命保険配当金、営業外収益')
    """ 生命保険配当金、営業外収益 """
    dividends_paid_to_non_controlling_interests_fin_cf: Optional[IxNonFractionPublic] = Field(default=None, description='非支配株主への配当金の支払額、財務活動によるキャッシュ・フロー')
    """ 非支配株主への配当金の支払額、財務活動によるキャッシュ・フロー """
    dividends_payable: Optional[IxNonFractionPublic] = Field(default=None, description='未払配当金')
    """ 未払配当金 """
    early_extra_retirement_payments_el: Optional[IxNonFractionPublic] = Field(default=None, description='早期割増退職金、特別損失')
    """ 早期割増退職金、特別損失 """
    effect_of_exchange_rate_change_on_cash_and_cash_equivalents: Optional[IxNonFractionPublic] = Field(default=None, description='現金及び現金同等物に係る換算差額')
    """ 現金及び現金同等物に係る換算差額 """
    electricity_sale_expenses_noe: Optional[IxNonFractionPublic] = Field(default=None, description='売電費用、営業外費用')
    """ 売電費用、営業外費用 """
    electricity_sale_income_noi: Optional[IxNonFractionPublic] = Field(default=None, description='売電収入、営業外収益')
    """ 売電収入、営業外収益 """
    electronically_recorded_monetary_claims_operating_ca: Optional[IxNonFractionPublic] = Field(default=None, description='電子記録債権、流動資産')
    """ 電子記録債権、流動資産 """
    electronically_recorded_obligations_facilities_cl: Optional[IxNonFractionPublic] = Field(default=None, description='設備関係電子記録債務、流動負債')
    """ 設備関係電子記録債務、流動負債 """
    electronically_recorded_obligations_non_operating_cl: Optional[IxNonFractionPublic] = Field(default=None, description='営業外電子記録債務、流動負債')
    """ 営業外電子記録債務、流動負債 """
    electronically_recorded_obligations_operating_cl: Optional[IxNonFractionPublic] = Field(default=None, description='電子記録債務、流動負債')
    """ 電子記録債務、流動負債 """
    employees_bonuses_sga: Optional[IxNonFractionPublic] = Field(default=None, description='従業員賞与、販売費及び一般管理費')
    """ 従業員賞与、販売費及び一般管理費 """
    employees_salaries_and_allowances_sga: Optional[IxNonFractionPublic] = Field(default=None, description='従業員給料及び手当、販売費及び一般管理費')
    """ 従業員給料及び手当、販売費及び一般管理費 """
    employees_salaries_and_allowances_sgacns: Optional[IxNonFractionPublic] = Field(default=None, description='従業員給料手当、販売費及び一般管理費、建設業')
    """ 従業員給料手当、販売費及び一般管理費、建設業 """
    employees_salaries_and_bonuses_sga: Optional[IxNonFractionPublic] = Field(default=None, description='従業員給料及び賞与、販売費及び一般管理費')
    """ 従業員給料及び賞与、販売費及び一般管理費 """
    employees_salaries_sga: Optional[IxNonFractionPublic] = Field(default=None, description='従業員給料、販売費及び一般管理費')
    """ 従業員給料、販売費及び一般管理費 """
    ending_finished_goods_cos: Optional[IxNonFractionPublic] = Field(default=None, description='製品期末棚卸高、売上原価')
    """ 製品期末棚卸高、売上原価 """
    ending_merchandise_and_finished_goods_cos: Optional[IxNonFractionPublic] = Field(default=None, description='商品及び製品期末棚卸高、売上原価')
    """ 商品及び製品期末棚卸高、売上原価 """
    enterprise_tax_sga: Optional[IxNonFractionPublic] = Field(default=None, description='事業税、販売費及び一般管理費')
    """ 事業税、販売費及び一般管理費 """
    entertainment_expenses_sga: Optional[IxNonFractionPublic] = Field(default=None, description='交際費、販売費及び一般管理費')
    """ 交際費、販売費及び一般管理費 """
    environmental_expenses_el: Optional[IxNonFractionPublic] = Field(default=None, description='環境対策費、特別損失')
    """ 環境対策費、特別損失 """
    equity_in_earnings_losses_of_affiliates_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='持分法による投資損益（△は益）、営業活動によるキャッシュ・フロー')
    """ 持分法による投資損益（△は益）、営業活動によるキャッシュ・フロー """
    equity_in_earnings_of_affiliates_noi: Optional[IxNonFractionPublic] = Field(default=None, description='持分法による投資利益、営業外収益')
    """ 持分法による投資利益、営業外収益 """
    equity_in_losses_of_affiliates_noe: Optional[IxNonFractionPublic] = Field(default=None, description='持分法による投資損失、営業外費用')
    """ 持分法による投資損失、営業外費用 """
    exercise_of_subscription_rights_to_shares: Optional[IxNonFractionPublic] = Field(default=None, description='新株予約権の行使')
    """ 新株予約権の行使 """
    extra_retirement_payment_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='特別退職金、営業活動によるキャッシュ・フロー')
    """ 特別退職金、営業活動によるキャッシュ・フロー """
    extra_retirement_payments_el: Optional[IxNonFractionPublic] = Field(default=None, description='割増退職金、特別損失')
    """ 割増退職金、特別損失 """
    extra_retirement_payments_noe: Optional[IxNonFractionPublic] = Field(default=None, description='割増退職金、営業外費用')
    """ 割増退職金、営業外費用 """
    extraordinary_income: Optional[IxNonFractionPublic] = Field(default=None, description='特別利益')
    """ 特別利益 """
    extraordinary_loss: Optional[IxNonFractionPublic] = Field(default=None, description='特別損失')
    """ 特別損失 """
    fees_and_commissions_oibnk: Optional[IxNonFractionPublic] = Field(default=None, description='役務取引等収益、経常収益、銀行業')
    """ 役務取引等収益、経常収益、銀行業 """
    fees_and_commissions_payments_oebnk: Optional[IxNonFractionPublic] = Field(default=None, description='役務取引等費用、経常費用、銀行業')
    """ 役務取引等費用、経常費用、銀行業 """
    fiduciary_obligation_fee_noi: Optional[IxNonFractionPublic] = Field(default=None, description='業務受託料、営業外収益')
    """ 業務受託料、営業外収益 """
    financial_expenses: Optional[IxNonFractionPublic] = Field(default=None, description='金融費用')
    """ 金融費用 """
    financing_expenses_noe: Optional[IxNonFractionPublic] = Field(default=None, description='資金調達費用、営業外費用')
    """ 資金調達費用、営業外費用 """
    financing_expenses_ope_cfbnk: Optional[IxNonFractionPublic] = Field(default=None, description='資金調達費用、営業活動によるキャッシュ・フロー、銀行業')
    """ 資金調達費用、営業活動によるキャッシュ・フロー、銀行業 """
    finished_goods: Optional[IxNonFractionPublic] = Field(default=None, description='製品')
    """ 製品 """
    foreign_currency_translation_adjustment: Optional[IxNonFractionPublic] = Field(default=None, description='為替換算調整勘定')
    """ 為替換算調整勘定 """
    foreign_currency_translation_adjustment_net_of_tax_oci: Optional[IxNonFractionPublic] = Field(default=None, description='為替換算調整勘定（税引後）、その他の包括利益')
    """ 為替換算調整勘定（税引後）、その他の包括利益 """
    foreign_exchange_gains_noi: Optional[IxNonFractionPublic] = Field(default=None, description='為替差益、営業外収益')
    """ 為替差益、営業外収益 """
    foreign_exchange_losses_gains_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='為替差損益（△は益）、営業活動によるキャッシュ・フロー')
    """ 為替差損益（△は益）、営業活動によるキャッシュ・フロー """
    foreign_exchange_losses_noe: Optional[IxNonFractionPublic] = Field(default=None, description='為替差損、営業外費用')
    """ 為替差損、営業外費用 """
    foreign_exchanges_assets_bnk: Optional[IxNonFractionPublic] = Field(default=None, description='外国為替、資産の部、銀行業')
    """ 外国為替、資産の部、銀行業 """
    foreign_exchanges_liabilities_bnk: Optional[IxNonFractionPublic] = Field(default=None, description='外国為替、負債の部、銀行業')
    """ 外国為替、負債の部、銀行業 """
    freightage_and_packing_expenses_sga: Optional[IxNonFractionPublic] = Field(default=None, description='運賃及び荷造費、販売費及び一般管理費')
    """ 運賃及び荷造費、販売費及び一般管理費 """
    freightage_expenses_sga: Optional[IxNonFractionPublic] = Field(default=None, description='運賃、販売費及び一般管理費')
    """ 運賃、販売費及び一般管理費 """
    gain_on_adjustment_of_account_payable_noi: Optional[IxNonFractionPublic] = Field(default=None, description='債務勘定整理益、営業外収益')
    """ 債務勘定整理益、営業外収益 """
    gain_on_bad_debts_recovered_noi: Optional[IxNonFractionPublic] = Field(default=None, description='償却債権取立益、営業外収益')
    """ 償却債権取立益、営業外収益 """
    gain_on_change_in_equity_ei: Optional[IxNonFractionPublic] = Field(default=None, description='持分変動利益、特別利益')
    """ 持分変動利益、特別利益 """
    gain_on_disposal_of_noncurrent_assets_ei: Optional[IxNonFractionPublic] = Field(default=None, description='固定資産処分益、特別利益')
    """ 固定資産処分益、特別利益 """
    gain_on_disposal_of_noncurrent_assets_noi: Optional[IxNonFractionPublic] = Field(default=None, description='固定資産処分益、営業外収益')
    """ 固定資産処分益、営業外収益 """
    gain_on_donation_of_noncurrent_assets_ei: Optional[IxNonFractionPublic] = Field(default=None, description='固定資産受贈益、特別利益')
    """ 固定資産受贈益、特別利益 """
    gain_on_donation_of_noncurrent_assets_noi: Optional[IxNonFractionPublic] = Field(default=None, description='固定資産受贈益、営業外収益')
    """ 固定資産受贈益、営業外収益 """
    gain_on_donation_of_noncurrent_assets_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='固定資産受贈益、営業活動によるキャッシュ・フロー')
    """ 固定資産受贈益、営業活動によるキャッシュ・フロー """
    gain_on_extinguishment_of_tie_in_shares_ei: Optional[IxNonFractionPublic] = Field(default=None, description='抱合せ株式消滅差益、特別利益')
    """ 抱合せ株式消滅差益、特別利益 """
    gain_on_forfeiture_of_unclaimed_dividends_noi: Optional[IxNonFractionPublic] = Field(default=None, description='未払配当金除斥益、営業外収益')
    """ 未払配当金除斥益、営業外収益 """
    gain_on_forgiveness_of_debt_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='債務免除益、営業活動によるキャッシュ・フロー')
    """ 債務免除益、営業活動によるキャッシュ・フロー """
    gain_on_forgiveness_of_debts_ei: Optional[IxNonFractionPublic] = Field(default=None, description='債務免除益、特別利益')
    """ 債務免除益、特別利益 """
    gain_on_fund_management_ope_cfbnk: Optional[IxNonFractionPublic] = Field(default=None, description='資金運用収益、営業活動によるキャッシュ・フロー、銀行業')
    """ 資金運用収益、営業活動によるキャッシュ・フロー、銀行業 """
    gain_on_insurance_adjustment_ei: Optional[IxNonFractionPublic] = Field(default=None, description='保険差益、特別利益')
    """ 保険差益、特別利益 """
    gain_on_investment_of_securities_noi: Optional[IxNonFractionPublic] = Field(default=None, description='有価証券運用益、営業外収益')
    """ 有価証券運用益、営業外収益 """
    gain_on_investments_in_capital_noi: Optional[IxNonFractionPublic] = Field(default=None, description='出資金運用益、営業外収益')
    """ 出資金運用益、営業外収益 """
    gain_on_investments_in_partnership_noi: Optional[IxNonFractionPublic] = Field(default=None, description='投資事業組合運用益、営業外収益')
    """ 投資事業組合運用益、営業外収益 """
    gain_on_investments_in_silent_partnership_noi: Optional[IxNonFractionPublic] = Field(default=None, description='匿名組合投資利益、営業外収益')
    """ 匿名組合投資利益、営業外収益 """
    gain_on_liquidation_of_subsidiaries_and_affiliates_ei: Optional[IxNonFractionPublic] = Field(default=None, description='関係会社清算益、特別利益')
    """ 関係会社清算益、特別利益 """
    gain_on_liquidation_of_subsidiaries_ei: Optional[IxNonFractionPublic] = Field(default=None, description='子会社清算益、特別利益')
    """ 子会社清算益、特別利益 """
    gain_on_negative_goodwill_ei: Optional[IxNonFractionPublic] = Field(default=None, description='負ののれん発生益、特別利益')
    """ 負ののれん発生益、特別利益 """
    gain_on_negative_goodwill_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='負ののれん発生益、営業活動によるキャッシュ・フロー')
    """ 負ののれん発生益、営業活動によるキャッシュ・フロー """
    gain_on_redemption_of_investment_securities_ei: Optional[IxNonFractionPublic] = Field(default=None, description='投資有価証券償還益、特別利益')
    """ 投資有価証券償還益、特別利益 """
    gain_on_redemption_of_securities_noi: Optional[IxNonFractionPublic] = Field(default=None, description='有価証券償還益、営業外収益')
    """ 有価証券償還益、営業外収益 """
    gain_on_reversal_of_asset_retirement_obligations_ei: Optional[IxNonFractionPublic] = Field(default=None, description='資産除去債務戻入益、特別利益')
    """ 資産除去債務戻入益、特別利益 """
    gain_on_reversal_of_provision_for_loss_on_disaster_ei: Optional[IxNonFractionPublic] = Field(default=None, description='災害損失引当金戻入額、特別利益')
    """ 災害損失引当金戻入額、特別利益 """
    gain_on_reversal_of_subscription_rights_to_shares_ei: Optional[IxNonFractionPublic] = Field(default=None, description='新株予約権戻入益、特別利益')
    """ 新株予約権戻入益、特別利益 """
    gain_on_reversal_of_subscription_rights_to_shares_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='新株予約権戻入益、営業活動によるキャッシュ・フロー')
    """ 新株予約権戻入益、営業活動によるキャッシュ・フロー """
    gain_on_revision_of_retirement_benefit_plan_ei: Optional[IxNonFractionPublic] = Field(default=None, description='退職給付制度改定益、特別利益')
    """ 退職給付制度改定益、特別利益 """
    gain_on_sales_of_golf_memberships_ei: Optional[IxNonFractionPublic] = Field(default=None, description='ゴルフ会員権売却益、特別利益')
    """ ゴルフ会員権売却益、特別利益 """
    gain_on_sales_of_goods_noi: Optional[IxNonFractionPublic] = Field(default=None, description='物品売却益、営業外収益')
    """ 物品売却益、営業外収益 """
    gain_on_sales_of_investment_securities_ei: Optional[IxNonFractionPublic] = Field(default=None, description='投資有価証券売却益、特別利益')
    """ 投資有価証券売却益、特別利益 """
    gain_on_sales_of_investment_securities_noi: Optional[IxNonFractionPublic] = Field(default=None, description='投資有価証券売却益、営業外収益')
    """ 投資有価証券売却益、営業外収益 """
    gain_on_sales_of_memberships_ei: Optional[IxNonFractionPublic] = Field(default=None, description='会員権売却益、特別利益')
    """ 会員権売却益、特別利益 """
    gain_on_sales_of_non_current_assets_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='固定資産売却益、営業活動によるキャッシュ・フロー')
    """ 固定資産売却益、営業活動によるキャッシュ・フロー """
    gain_on_sales_of_noncurrent_assets_ei: Optional[IxNonFractionPublic] = Field(default=None, description='固定資産売却益、特別利益')
    """ 固定資産売却益、特別利益 """
    gain_on_sales_of_noncurrent_assets_noi: Optional[IxNonFractionPublic] = Field(default=None, description='固定資産売却益、営業外収益')
    """ 固定資産売却益、営業外収益 """
    gain_on_sales_of_property_plant_and_equipment_ei: Optional[IxNonFractionPublic] = Field(default=None, description='有形固定資産売却益、特別利益')
    """ 有形固定資産売却益、特別利益 """
    gain_on_sales_of_scraps1_noi: Optional[IxNonFractionPublic] = Field(default=None, description='作業くず売却益、営業外収益')
    """ 作業くず売却益、営業外収益 """
    gain_on_sales_of_scraps2_noi: Optional[IxNonFractionPublic] = Field(default=None, description='スクラップ売却益、営業外収益')
    """ スクラップ売却益、営業外収益 """
    gain_on_sales_of_securities_oiins: Optional[IxNonFractionPublic] = Field(default=None, description='有価証券売却益、経常収益、保険業')
    """ 有価証券売却益、経常収益、保険業 """
    gain_on_sales_of_subsidiaries_and_affiliates_stocks_ei: Optional[IxNonFractionPublic] = Field(default=None, description='関係会社株式売却益、特別利益')
    """ 関係会社株式売却益、特別利益 """
    gain_on_sales_of_subsidiaries_stocks_ei: Optional[IxNonFractionPublic] = Field(default=None, description='子会社株式売却益、特別利益')
    """ 子会社株式売却益、特別利益 """
    gain_on_step_acquisitions_ei: Optional[IxNonFractionPublic] = Field(default=None, description='段階取得に係る差益、特別利益')
    """ 段階取得に係る差益、特別利益 """
    gain_on_transfer_of_business_ei: Optional[IxNonFractionPublic] = Field(default=None, description='事業譲渡益、特別利益')
    """ 事業譲渡益、特別利益 """
    gain_on_valuation_of_compound_financial_instruments_noi: Optional[IxNonFractionPublic] = Field(default=None, description='複合金融商品評価益、営業外収益')
    """ 複合金融商品評価益、営業外収益 """
    gain_on_valuation_of_derivatives_noi: Optional[IxNonFractionPublic] = Field(default=None, description='デリバティブ評価益、営業外収益')
    """ デリバティブ評価益、営業外収益 """
    gain_on_valuation_of_investment_securities_noi: Optional[IxNonFractionPublic] = Field(default=None, description='投資有価証券評価益、営業外収益')
    """ 投資有価証券評価益、営業外収益 """
    gain_on_valuation_of_securities_noi: Optional[IxNonFractionPublic] = Field(default=None, description='有価証券評価益、営業外収益')
    """ 有価証券評価益、営業外収益 """
    general_and_administrative_expenses_oebnk: Optional[IxNonFractionPublic] = Field(default=None, description='営業経費、経常費用、銀行業')
    """ 営業経費、経常費用、銀行業 """
    general_and_administrative_expenses_sga: Optional[IxNonFractionPublic] = Field(default=None, description='一般管理費、販売費及び一般管理費')
    """ 一般管理費、販売費及び一般管理費 """
    general_reserve: Optional[IxNonFractionPublic] = Field(default=None, description='別途積立金')
    """ 別途積立金 """
    golf_club_membership: Optional[IxNonFractionPublic] = Field(default=None, description='ゴルフ会員権')
    """ ゴルフ会員権 """
    golf_courses: Optional[IxNonFractionPublic] = Field(default=None, description='コース勘定')
    """ コース勘定 """
    goodwill: Optional[IxNonFractionPublic] = Field(default=None, description='のれん')
    """ のれん """
    gross_profit: Optional[IxNonFractionPublic] = Field(default=None, description='売上総利益又は売上総損失（△）')
    """ 売上総利益又は売上総損失（△） """
    gross_profit_merchandise_gp: Optional[IxNonFractionPublic] = Field(default=None, description='商品売上総利益又は商品売上総損失（△）、売上総利益')
    """ 商品売上総利益又は商品売上総損失（△）、売上総利益 """
    gross_profit_on_completed_construction_contracts_cns: Optional[IxNonFractionPublic] = Field(default=None, description='完成工事総利益又は完成工事総損失（△）、建設業')
    """ 完成工事総利益又は完成工事総損失（△）、建設業 """
    gross_profit_on_real_estate_business_and_other_cns: Optional[IxNonFractionPublic] = Field(default=None, description='不動産事業等総利益又は不動産事業等総損失（△）、建設業')
    """ 不動産事業等総利益又は不動産事業等総損失（△）、建設業 """
    gross_profit_on_side_line_business_cns: Optional[IxNonFractionPublic] = Field(default=None, description='兼業事業総利益又は兼業事業総損失（△）、建設業')
    """ 兼業事業総利益又は兼業事業総損失（△）、建設業 """
    gross_profit_other_business_gp: Optional[IxNonFractionPublic] = Field(default=None, description='その他の事業総利益又はその他の事業総損失（△）、売上総利益')
    """ その他の事業総利益又はその他の事業総損失（△）、売上総利益 """
    gross_profit_real_estate_business_gp: Optional[IxNonFractionPublic] = Field(default=None, description='不動産事業総利益又は不動産事業総損失（△）、売上総利益')
    """ 不動産事業総利益又は不動産事業総損失（△）、売上総利益 """
    guarantee_commission_noe: Optional[IxNonFractionPublic] = Field(default=None, description='支払保証料、営業外費用')
    """ 支払保証料、営業外費用 """
    guarantee_commission_received_noi: Optional[IxNonFractionPublic] = Field(default=None, description='受取保証料、営業外収益')
    """ 受取保証料、営業外収益 """
    guarantee_deposits_cacmd: Optional[IxNonFractionPublic] = Field(default=None, description='差入保証金、流動資産、商品先物取引業')
    """ 差入保証金、流動資産、商品先物取引業 """
    guarantee_deposits_ioa: Optional[IxNonFractionPublic] = Field(default=None, description='差入保証金、投資その他の資産')
    """ 差入保証金、投資その他の資産 """
    guarantee_deposits_received2_ncl: Optional[IxNonFractionPublic] = Field(default=None, description='預り保証金、固定負債')
    """ 預り保証金、固定負債 """
    guarantee_deposits_received_clsec: Optional[IxNonFractionPublic] = Field(default=None, description='受入保証金、流動負債、第一種金融商品取引業')
    """ 受入保証金、流動負債、第一種金融商品取引業 """
    guarantee_deposits_received_ncl: Optional[IxNonFractionPublic] = Field(default=None, description='受入保証金、固定負債')
    """ 受入保証金、固定負債 """
    guarantee_received_ncllea: Optional[IxNonFractionPublic] = Field(default=None, description='受取保証金、固定負債、リース事業')
    """ 受取保証金、固定負債、リース事業 """
    haulage_expenses_sga: Optional[IxNonFractionPublic] = Field(default=None, description='運搬費、販売費及び一般管理費')
    """ 運搬費、販売費及び一般管理費 """
    head_office_transfer_cost_el: Optional[IxNonFractionPublic] = Field(default=None, description='本社移転費用、特別損失')
    """ 本社移転費用、特別損失 """
    house_rent_income_noi: Optional[IxNonFractionPublic] = Field(default=None, description='受取家賃、営業外収益')
    """ 受取家賃、営業外収益 """
    impairment_loss_el: Optional[IxNonFractionPublic] = Field(default=None, description='減損損失、特別損失')
    """ 減損損失、特別損失 """
    impairment_loss_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='減損損失、営業活動によるキャッシュ・フロー')
    """ 減損損失、営業活動によるキャッシュ・フロー """
    income_before_dividends_distribution_from_silent_partnership_income_taxes: Optional[IxNonFractionPublic] = Field(default=None, description='匿名組合損益分配前税引前当期純利益又は純損失（△）')
    """ 匿名組合損益分配前税引前当期純利益又は純損失（△） """
    income_before_income_taxes: Optional[IxNonFractionPublic] = Field(default=None, description='税引前当期純利益又は税引前当期純損失（△）')
    """ 税引前当期純利益又は税引前当期純損失（△） """
    income_taxes: Optional[IxNonFractionPublic] = Field(default=None, description='法人税等')
    """ 法人税等 """
    income_taxes_current: Optional[IxNonFractionPublic] = Field(default=None, description='法人税、住民税及び事業税')
    """ 法人税、住民税及び事業税 """
    income_taxes_current_consolidated_ins: Optional[IxNonFractionPublic] = Field(default=None, description='法人税及び住民税等、保険業')
    """ 法人税及び住民税等、保険業 """
    income_taxes_deferred: Optional[IxNonFractionPublic] = Field(default=None, description='法人税等調整額')
    """ 法人税等調整額 """
    income_taxes_paid_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='法人税等の支払額、営業活動によるキャッシュ・フロー')
    """ 法人税等の支払額、営業活動によるキャッシュ・フロー """
    income_taxes_paid_refund_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='法人税等の支払額又は還付額（△は支払）、営業活動によるキャッシュ・フロー')
    """ 法人税等の支払額又は還付額（△は支払）、営業活動によるキャッシュ・フロー """
    income_taxes_payable: Optional[IxNonFractionPublic] = Field(default=None, description='未払法人税等')
    """ 未払法人税等 """
    income_taxes_receivable: Optional[IxNonFractionPublic] = Field(default=None, description='未収還付法人税等')
    """ 未収還付法人税等 """
    income_taxes_refund_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='法人税等の還付額、営業活動によるキャッシュ・フロー')
    """ 法人税等の還付額、営業活動によるキャッシュ・フロー """
    increase_decrease_in_accounts_payable_other_and_accrued_expenses_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='未払金及び未払費用の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 未払金及び未払費用の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    increase_decrease_in_accounts_payable_other_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='未払金の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 未払金の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    increase_decrease_in_accrued_consumption_taxes_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='未払消費税等の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 未払消費税等の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    increase_decrease_in_accrued_expenses_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='未払費用の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 未払費用の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    increase_decrease_in_accrued_liabilities_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='未払債務の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 未払債務の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    increase_decrease_in_advances_received_on_uncompleted_construction_contracts_ope_cfcns: Optional[IxNonFractionPublic] = Field(default=None, description='未成工事受入金の増減額（△は減少）、営業活動によるキャッシュ・フロー、建設業')
    """ 未成工事受入金の増減額（△は減少）、営業活動によるキャッシュ・フロー、建設業 """
    increase_decrease_in_advances_received_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='前受金の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 前受金の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    increase_decrease_in_allowance_for_doubtful_accounts_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='貸倒引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 貸倒引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    increase_decrease_in_allowance_for_investment_loss_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='投資損失引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 投資損失引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    increase_decrease_in_allowance_for_loan_losses_ope_cfbnk: Optional[IxNonFractionPublic] = Field(default=None, description='貸倒引当金の増減（△）、営業活動によるキャッシュ・フロー、銀行業')
    """ 貸倒引当金の増減（△）、営業活動によるキャッシュ・フロー、銀行業 """
    increase_decrease_in_cash_and_cash_equivalents_resulting_from_change_of_scope_of_consolidation_cce: Optional[IxNonFractionPublic] = Field(default=None, description='連結の範囲の変更に伴う現金及び現金同等物の増減額（△は減少）')
    """ 連結の範囲の変更に伴う現金及び現金同等物の増減額（△は減少） """
    increase_decrease_in_commercial_papers_fin_cf: Optional[IxNonFractionPublic] = Field(default=None, description='コマーシャル・ペーパーの増減額（△は減少）、財務活動によるキャッシュ・フロー')
    """ コマーシャル・ペーパーの増減額（△は減少）、財務活動によるキャッシュ・フロー """
    increase_decrease_in_contract_liabilities_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='契約負債の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 契約負債の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    increase_decrease_in_customers_deposits_received_for_commodity_futures_transaction_ope_cfcmd: Optional[IxNonFractionPublic] = Field(default=None, description='預り証拠金の増減額（△は減少）、営業活動によるキャッシュ・フロー、商品先物取引業')
    """ 預り証拠金の増減額（△は減少）、営業活動によるキャッシュ・フロー、商品先物取引業 """
    increase_decrease_in_deposits_received_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='預り金の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 預り金の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    increase_decrease_in_guarantee_deposits_received_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='預り保証金の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 預り保証金の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    increase_decrease_in_guarantee_deposits_received_ope_cfsec: Optional[IxNonFractionPublic] = Field(default=None, description='受入保証金の増減額（△は減少）、営業活動によるキャッシュ・フロー、第一種金融商品取引業')
    """ 受入保証金の増減額（△は減少）、営業活動によるキャッシュ・フロー、第一種金融商品取引業 """
    increase_decrease_in_income_taxes_payable_the_factor_based_tax_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='未払法人税等（外形標準課税）の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 未払法人税等（外形標準課税）の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    increase_decrease_in_lease_and_guarantee_deposits_received_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='預り敷金及び保証金の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 預り敷金及び保証金の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    increase_decrease_in_long_term_accounts_payable_other_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='長期未払金の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 長期未払金の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    increase_decrease_in_net_defined_benefit_asset_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='退職給付に係る資産の増減額（△は増加）、営業活動によるキャッシュ・フロー')
    """ 退職給付に係る資産の増減額（△は増加）、営業活動によるキャッシュ・フロー """
    increase_decrease_in_net_defined_benefit_liability_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='退職給付に係る負債の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 退職給付に係る負債の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    increase_decrease_in_notes_and_accounts_payable_trade_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='仕入債務の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 仕入債務の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    increase_decrease_in_notes_discounted_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='割引手形の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 割引手形の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    increase_decrease_in_operating_debt_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='営業債務の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 営業債務の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    increase_decrease_in_other_assets_liabilities_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='その他の資産・負債の増減額、営業活動によるキャッシュ・フロー')
    """ その他の資産・負債の増減額、営業活動によるキャッシュ・フロー """
    increase_decrease_in_other_current_liabilities_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='その他の流動負債の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ その他の流動負債の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    increase_decrease_in_other_investing_and_financing_activities_liabilities_ope_cfins: Optional[IxNonFractionPublic] = Field(default=None, description='その他負債（除く投資活動関連、財務活動関連）の増減額（△は減少）、営業活動によるキャッシュ・フロー、保険業')
    """ その他負債（除く投資活動関連、財務活動関連）の増減額（△は減少）、営業活動によるキャッシュ・フロー、保険業 """
    increase_decrease_in_other_liabilities_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='その他の負債の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ その他の負債の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    increase_decrease_in_other_noncurrent_liabilities_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='その他の固定負債の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ その他の固定負債の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    increase_decrease_in_other_provision_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='その他の引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ その他の引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    increase_decrease_in_outstanding_claims_ope_cfins: Optional[IxNonFractionPublic] = Field(default=None, description='支払備金の増減額（△は減少）、営業活動によるキャッシュ・フロー、保険業')
    """ 支払備金の増減額（△は減少）、営業活動によるキャッシュ・フロー、保険業 """
    increase_decrease_in_policy_reserve_ope_cfins: Optional[IxNonFractionPublic] = Field(default=None, description='責任準備金の増減額（△は減少）、営業活動によるキャッシュ・フロー、保険業')
    """ 責任準備金の増減額（△は減少）、営業活動によるキャッシュ・フロー、保険業 """
    increase_decrease_in_provision_for_bonuses_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='賞与引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 賞与引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    increase_decrease_in_provision_for_contingent_loss_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='偶発損失引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 偶発損失引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    increase_decrease_in_provision_for_directors_bonuses_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='役員賞与引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 役員賞与引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    increase_decrease_in_provision_for_directors_retirement_benefits_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='役員退職慰労引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 役員退職慰労引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    increase_decrease_in_provision_for_environmental_measures_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='環境対策引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 環境対策引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    increase_decrease_in_provision_for_loss_on_construction_contracts_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='工事損失引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 工事損失引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    increase_decrease_in_provision_for_loss_on_guarantees_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='債務保証損失引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 債務保証損失引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    increase_decrease_in_provision_for_loss_on_interest_repayment_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='利息返還損失引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 利息返還損失引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    increase_decrease_in_provision_for_loss_on_liquidation_of_subsidiaries_and_affiliates_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='関係会社整理損失引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 関係会社整理損失引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    increase_decrease_in_provision_for_loss_on_litigation_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='訴訟損失引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 訴訟損失引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    increase_decrease_in_provision_for_loss_on_order_received_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='受注損失引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 受注損失引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    increase_decrease_in_provision_for_loss_on_store_closing_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='店舗閉鎖損失引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 店舗閉鎖損失引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    increase_decrease_in_provision_for_point_card_certificates_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='ポイント引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ ポイント引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    increase_decrease_in_provision_for_product_warranties_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='製品保証引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 製品保証引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    increase_decrease_in_provision_for_reimbursement_of_deposits_ope_cfbnk: Optional[IxNonFractionPublic] = Field(default=None, description='睡眠預金払戻損失引当金の増減（△）、営業活動によるキャッシュ・フロー、銀行業')
    """ 睡眠預金払戻損失引当金の増減（△）、営業活動によるキャッシュ・フロー、銀行業 """
    increase_decrease_in_provision_for_repairs_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='修繕引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 修繕引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    increase_decrease_in_provision_for_retirement_benefits_and_directors_retirement_benefits_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='退職給付及び役員退職慰労引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 退職給付及び役員退職慰労引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    increase_decrease_in_provision_for_retirement_benefits_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='退職給付引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 退職給付引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    increase_decrease_in_provision_for_sales_promotion_expenses_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='販売促進引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 販売促進引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    increase_decrease_in_provision_for_share_based_payments_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='株式報酬引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 株式報酬引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    increase_decrease_in_provision_for_share_based_remuneration_for_directors_and_other_officers_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='役員株式給付引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 役員株式給付引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    increase_decrease_in_provision_for_share_based_remuneration_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='株式給付引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 株式給付引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    increase_decrease_in_provision_for_shareholder_benefit_program_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='株主優待引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 株主優待引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    increase_decrease_in_provision_for_special_repairs_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='特別修繕引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 特別修繕引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    increase_decrease_in_provision_for_warranties_for_completed_construction_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='完成工事補償引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 完成工事補償引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    increase_decrease_in_provision_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    increase_decrease_in_reserve_for_price_fluctuation_ope_cfins: Optional[IxNonFractionPublic] = Field(default=None, description='価格変動準備金の増減額（△は減少）、営業活動によるキャッシュ・フロー、保険業')
    """ 価格変動準備金の増減額（△は減少）、営業活動によるキャッシュ・フロー、保険業 """
    increase_decrease_in_reserves_under_the_special_laws2_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='特別法上の引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 特別法上の引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    increase_decrease_in_short_term_bank_loans_and_commercial_papers_fin_cf: Optional[IxNonFractionPublic] = Field(default=None, description='短期借入金及びコマーシャル・ペーパーの増減額（△は減少）、財務活動によるキャッシュ・フロー')
    """ 短期借入金及びコマーシャル・ペーパーの増減額（△は減少）、財務活動によるキャッシュ・フロー """
    increase_decrease_in_short_term_loans_payable_fin_cf: Optional[IxNonFractionPublic] = Field(default=None, description='短期借入金の増減額（△は減少）、財務活動によるキャッシュ・フロー')
    """ 短期借入金の増減額（△は減少）、財務活動によるキャッシュ・フロー """
    increase_decrease_in_unearned_revenue_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='前受収益の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 前受収益の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    increase_in_cash_and_cash_equivalents_from_newly_consolidated_subsidiary_cce: Optional[IxNonFractionPublic] = Field(default=None, description='新規連結に伴う現金及び現金同等物の増加額')
    """ 新規連結に伴う現金及び現金同等物の増加額 """
    increase_in_cash_and_cash_equivalents_resulting_from_merger_cce: Optional[IxNonFractionPublic] = Field(default=None, description='合併に伴う現金及び現金同等物の増加額')
    """ 合併に伴う現金及び現金同等物の増加額 """
    increase_in_cash_and_cash_equivalents_resulting_from_merger_with_unconsolidated_subsidiaries_cce: Optional[IxNonFractionPublic] = Field(default=None, description='非連結子会社との合併に伴う現金及び現金同等物の増加額')
    """ 非連結子会社との合併に伴う現金及び現金同等物の増加額 """
    increase_in_money_held_in_trust_inv_cfbnk: Optional[IxNonFractionPublic] = Field(default=None, description='金銭の信託の増加による支出、投資活動によるキャッシュ・フロー、銀行業')
    """ 金銭の信託の増加による支出、投資活動によるキャッシュ・フロー、銀行業 """
    increase_in_short_term_loans_payable_fin_cf: Optional[IxNonFractionPublic] = Field(default=None, description='短期借入れによる収入、財務活動によるキャッシュ・フロー')
    """ 短期借入れによる収入、財務活動によるキャッシュ・フロー """
    insurance_and_dividends_income_noi: Optional[IxNonFractionPublic] = Field(default=None, description='受取保険金及び配当金、営業外収益')
    """ 受取保険金及び配当金、営業外収益 """
    insurance_expenses_sga: Optional[IxNonFractionPublic] = Field(default=None, description='保険料、販売費及び一般管理費')
    """ 保険料、販売費及び一般管理費 """
    insurance_fee_noi: Optional[IxNonFractionPublic] = Field(default=None, description='受取保険料、営業外収益')
    """ 受取保険料、営業外収益 """
    insurance_funds: Optional[IxNonFractionPublic] = Field(default=None, description='保険積立金')
    """ 保険積立金 """
    insurance_funds_for_directors: Optional[IxNonFractionPublic] = Field(default=None, description='役員に対する保険積立金')
    """ 役員に対する保険積立金 """
    insurance_income_ei: Optional[IxNonFractionPublic] = Field(default=None, description='受取保険金、特別利益')
    """ 受取保険金、特別利益 """
    insurance_income_noi: Optional[IxNonFractionPublic] = Field(default=None, description='受取保険金、営業外収益')
    """ 受取保険金、営業外収益 """
    insurance_income_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='受取保険金、営業活動によるキャッシュ・フロー')
    """ 受取保険金、営業活動によるキャッシュ・フロー """
    insurance_premiums_refunded_cancellation_noi: Optional[IxNonFractionPublic] = Field(default=None, description='保険解約返戻金、営業外収益')
    """ 保険解約返戻金、営業外収益 """
    insurance_return_noi: Optional[IxNonFractionPublic] = Field(default=None, description='保険返戻金、営業外収益')
    """ 保険返戻金、営業外収益 """
    intangible_assets: Optional[IxNonFractionPublic] = Field(default=None, description='無形固定資産')
    """ 無形固定資産 """
    interest_and_dividends_income_noi: Optional[IxNonFractionPublic] = Field(default=None, description='受取利息及び配当金、営業外収益')
    """ 受取利息及び配当金、営業外収益 """
    interest_and_dividends_income_oiins: Optional[IxNonFractionPublic] = Field(default=None, description='利息及び配当金収入、経常収益、保険業')
    """ 利息及び配当金収入、経常収益、保険業 """
    interest_and_dividends_income_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='受取利息及び受取配当金、営業活動によるキャッシュ・フロー')
    """ 受取利息及び受取配当金、営業活動によるキャッシュ・フロー """
    interest_and_dividends_income_ope_cfins_nonlife: Optional[IxNonFractionPublic] = Field(default=None, description='利息及び配当金収入、営業活動によるキャッシュ・フロー、保険業、損害保険')
    """ 利息及び配当金収入、営業活動によるキャッシュ・フロー、保険業、損害保険 """
    interest_and_dividends_income_received_ope_cf_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='利息及び配当金の受取額、営業活動によるキャッシュ・フロー又は投資活動によるキャッシュ・フロー')
    """ 利息及び配当金の受取額、営業活動によるキャッシュ・フロー又は投資活動によるキャッシュ・フロー """
    interest_and_dividends_on_securities_oibnk: Optional[IxNonFractionPublic] = Field(default=None, description='有価証券利息配当金、経常収益、銀行業')
    """ 有価証券利息配当金、経常収益、銀行業 """
    interest_expenses_and_loss_on_sales_of_notes_receivable_trade_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='支払利息及び手形売却損、営業活動によるキャッシュ・フロー')
    """ 支払利息及び手形売却損、営業活動によるキャッシュ・フロー """
    interest_expenses_noe: Optional[IxNonFractionPublic] = Field(default=None, description='支払利息、営業外費用')
    """ 支払利息、営業外費用 """
    interest_expenses_oebnk: Optional[IxNonFractionPublic] = Field(default=None, description='資金調達費用、経常費用、銀行業')
    """ 資金調達費用、経常費用、銀行業 """
    interest_expenses_oeins: Optional[IxNonFractionPublic] = Field(default=None, description='支払利息、経常費用、保険業')
    """ 支払利息、経常費用、保険業 """
    interest_expenses_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='支払利息、営業活動によるキャッシュ・フロー')
    """ 支払利息、営業活動によるキャッシュ・フロー """
    interest_expenses_paid_on_loans_and_bonds_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='支払利息及び社債利息、営業活動によるキャッシュ・フロー')
    """ 支払利息及び社債利息、営業活動によるキャッシュ・フロー """
    interest_expenses_paid_ope_cf_fin_cf: Optional[IxNonFractionPublic] = Field(default=None, description='利息の支払額、営業活動によるキャッシュ・フロー又は財務活動によるキャッシュ・フロー')
    """ 利息の支払額、営業活動によるキャッシュ・フロー又は財務活動によるキャッシュ・フロー """
    interest_income_noi: Optional[IxNonFractionPublic] = Field(default=None, description='受取利息、営業外収益')
    """ 受取利息、営業外収益 """
    interest_income_oibnk: Optional[IxNonFractionPublic] = Field(default=None, description='資金運用収益、経常収益、銀行業')
    """ 資金運用収益、経常収益、銀行業 """
    interest_income_on_securities_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='有価証券利息、営業活動によるキャッシュ・フロー')
    """ 有価証券利息、営業活動によるキャッシュ・フロー """
    interest_income_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='受取利息、営業活動によるキャッシュ・フロー')
    """ 受取利息、営業活動によるキャッシュ・フロー """
    interest_income_received_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='利息の受取額、営業活動によるキャッシュ・フロー')
    """ 利息の受取額、営業活動によるキャッシュ・フロー """
    interest_on_bonds_noe: Optional[IxNonFractionPublic] = Field(default=None, description='社債利息、営業外費用')
    """ 社債利息、営業外費用 """
    interest_on_bonds_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='社債利息、営業活動によるキャッシュ・フロー')
    """ 社債利息、営業活動によるキャッシュ・フロー """
    interest_on_deposits_oebnk: Optional[IxNonFractionPublic] = Field(default=None, description='預金利息、経常費用、銀行業')
    """ 預金利息、経常費用、銀行業 """
    interest_on_loans_and_discounts_oibnk: Optional[IxNonFractionPublic] = Field(default=None, description='貸出金利息、経常収益、銀行業')
    """ 貸出金利息、経常収益、銀行業 """
    interest_on_operating_loans_spf: Optional[IxNonFractionPublic] = Field(default=None, description='営業貸付金利息、特定金融業')
    """ 営業貸付金利息、特定金融業 """
    interest_on_payables_under_securities_lending_transactions_oebnk: Optional[IxNonFractionPublic] = Field(default=None, description='債券貸借取引支払利息、経常費用、銀行業')
    """ 債券貸借取引支払利息、経常費用、銀行業 """
    interest_on_refund_noi: Optional[IxNonFractionPublic] = Field(default=None, description='還付加算金、営業外収益')
    """ 還付加算金、営業外収益 """
    interest_on_securities_noi: Optional[IxNonFractionPublic] = Field(default=None, description='有価証券利息、営業外収益')
    """ 有価証券利息、営業外収益 """
    inventories: Optional[IxNonFractionPublic] = Field(default=None, description='棚卸資産')
    """ 棚卸資産 """
    investment_expenses_oeins: Optional[IxNonFractionPublic] = Field(default=None, description='資産運用費用、経常費用、保険業')
    """ 資産運用費用、経常費用、保険業 """
    investment_income_oiins: Optional[IxNonFractionPublic] = Field(default=None, description='資産運用収益、経常収益、保険業')
    """ 資産運用収益、経常収益、保険業 """
    investment_securities: Optional[IxNonFractionPublic] = Field(default=None, description='投資有価証券')
    """ 投資有価証券 """
    investments_and_other_assets: Optional[IxNonFractionPublic] = Field(default=None, description='投資その他の資産')
    """ 投資その他の資産 """
    investments_and_other_assets_gross: Optional[IxNonFractionPublic] = Field(default=None, description='投資その他の資産（総額）')
    """ 投資その他の資産（総額） """
    investments_in_capital: Optional[IxNonFractionPublic] = Field(default=None, description='出資金')
    """ 出資金 """
    investments_in_capital_of_subsidiaries_and_affiliates: Optional[IxNonFractionPublic] = Field(default=None, description='関係会社出資金')
    """ 関係会社出資金 """
    issuance_of_new_shares: Optional[IxNonFractionPublic] = Field(default=None, description='新株の発行')
    """ 新株の発行 """
    issuance_of_new_sharesexercise_of_subscription_rights_to_shares: Optional[IxNonFractionPublic] = Field(default=None, description='新株の発行（新株予約権の行使）')
    """ 新株の発行（新株予約権の行使） """
    issuance_of_subscription_rights_to_shares: Optional[IxNonFractionPublic] = Field(default=None, description='新株予約権の発行')
    """ 新株予約権の発行 """
    land: Optional[IxNonFractionPublic] = Field(default=None, description='土地')
    """ 土地 """
    land_and_buildings_for_sale_carwy: Optional[IxNonFractionPublic] = Field(default=None, description='販売土地及び建物、流動資産、鉄道事業')
    """ 販売土地及び建物、流動資産、鉄道事業 """
    land_and_buildings_for_sale_in_lots: Optional[IxNonFractionPublic] = Field(default=None, description='分譲土地建物')
    """ 分譲土地建物 """
    land_and_house_rent_received_noi: Optional[IxNonFractionPublic] = Field(default=None, description='受取地代家賃、営業外収益')
    """ 受取地代家賃、営業外収益 """
    land_in_trust: Optional[IxNonFractionPublic] = Field(default=None, description='信託土地')
    """ 信託土地 """
    lapse_of_subscription_rights_to_shares: Optional[IxNonFractionPublic] = Field(default=None, description='新株予約権の失効')
    """ 新株予約権の失効 """
    lease_and_guarantee_deposits: Optional[IxNonFractionPublic] = Field(default=None, description='敷金及び保証金')
    """ 敷金及び保証金 """
    lease_and_guarantee_deposits_received: Optional[IxNonFractionPublic] = Field(default=None, description='受入敷金保証金')
    """ 受入敷金保証金 """
    lease_assets_ia: Optional[IxNonFractionPublic] = Field(default=None, description='リース資産、無形固定資産')
    """ リース資産、無形固定資産 """
    lease_assets_net_ppe: Optional[IxNonFractionPublic] = Field(default=None, description='リース資産（純額）、有形固定資産')
    """ リース資産（純額）、有形固定資産 """
    lease_assets_ppe: Optional[IxNonFractionPublic] = Field(default=None, description='リース資産、有形固定資産')
    """ リース資産、有形固定資産 """
    lease_deposits_ioa: Optional[IxNonFractionPublic] = Field(default=None, description='敷金')
    """ 敷金 """
    lease_investment_assets_ca: Optional[IxNonFractionPublic] = Field(default=None, description='リース投資資産、流動資産')
    """ リース投資資産、流動資産 """
    lease_investment_assets_ioa: Optional[IxNonFractionPublic] = Field(default=None, description='リース投資資産、投資その他の資産')
    """ リース投資資産、投資その他の資産 """
    lease_obligations_cl: Optional[IxNonFractionPublic] = Field(default=None, description='リース債務、流動負債')
    """ リース債務、流動負債 """
    lease_obligations_liabilities: Optional[IxNonFractionPublic] = Field(default=None, description='リース債務、負債の部')
    """ リース債務、負債の部 """
    lease_obligations_ncl: Optional[IxNonFractionPublic] = Field(default=None, description='リース債務、固定負債')
    """ リース債務、固定負債 """
    lease_property_ialea: Optional[IxNonFractionPublic] = Field(default=None, description='賃貸資産、無形固定資産、リース事業')
    """ 賃貸資産、無形固定資産、リース事業 """
    lease_receivables_and_investment_assets_ca: Optional[IxNonFractionPublic] = Field(default=None, description='リース債権及びリース投資資産、流動資産')
    """ リース債権及びリース投資資産、流動資産 """
    leased_assets_ppelea: Optional[IxNonFractionPublic] = Field(default=None, description='賃貸資産、合計、有形固定資産、リース事業')
    """ 賃貸資産、合計、有形固定資産、リース事業 """
    leasehold_right: Optional[IxNonFractionPublic] = Field(default=None, description='借地権')
    """ 借地権 """
    legal_and_employee_benefits_expenses_sga: Optional[IxNonFractionPublic] = Field(default=None, description='法定福利及び厚生費、販売費及び一般管理費')
    """ 法定福利及び厚生費、販売費及び一般管理費 """
    legal_capital_surplus: Optional[IxNonFractionPublic] = Field(default=None, description='資本準備金')
    """ 資本準備金 """
    legal_retained_earnings: Optional[IxNonFractionPublic] = Field(default=None, description='利益準備金')
    """ 利益準備金 """
    legal_welfare_expenses_sga: Optional[IxNonFractionPublic] = Field(default=None, description='法定福利費、販売費及び一般管理費')
    """ 法定福利費、販売費及び一般管理費 """
    liabilities: Optional[IxNonFractionPublic] = Field(default=None, description='負債')
    """ 負債 """
    liabilities_and_net_assets: Optional[IxNonFractionPublic] = Field(default=None, description='負債純資産')
    """ 負債純資産 """
    liabilities_from_application_of_equity_method_ncl: Optional[IxNonFractionPublic] = Field(default=None, description='持分法適用に伴う負債、固定負債')
    """ 持分法適用に伴う負債、固定負債 """
    listing_expenses_noe: Optional[IxNonFractionPublic] = Field(default=None, description='上場関連費用、営業外費用')
    """ 上場関連費用、営業外費用 """
    listing_expenses_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='上場関連費用、営業活動によるキャッシュ・フロー')
    """ 上場関連費用、営業活動によるキャッシュ・フロー """
    litigation_expenses_noe: Optional[IxNonFractionPublic] = Field(default=None, description='訴訟関連費用、営業外費用')
    """ 訴訟関連費用、営業外費用 """
    litigation_settlement_el: Optional[IxNonFractionPublic] = Field(default=None, description='訴訟和解金、特別損失')
    """ 訴訟和解金、特別損失 """
    loans_and_bills_discounted_assets_bnk: Optional[IxNonFractionPublic] = Field(default=None, description='貸出金、資産の部、銀行業')
    """ 貸出金、資産の部、銀行業 """
    loans_receivables_assets_ins: Optional[IxNonFractionPublic] = Field(default=None, description='貸付金、資産の部、保険業')
    """ 貸付金、資産の部、保険業 """
    long_term_accounts_payable_other: Optional[IxNonFractionPublic] = Field(default=None, description='長期未払金')
    """ 長期未払金 """
    long_term_accounts_receivable_other: Optional[IxNonFractionPublic] = Field(default=None, description='長期未収入金')
    """ 長期未収入金 """
    long_term_advances_received: Optional[IxNonFractionPublic] = Field(default=None, description='長期前受金')
    """ 長期前受金 """
    long_term_deferred_contribution_for_construction: Optional[IxNonFractionPublic] = Field(default=None, description='長期前受工事負担金')
    """ 長期前受工事負担金 """
    long_term_deposits_received: Optional[IxNonFractionPublic] = Field(default=None, description='長期預り金')
    """ 長期預り金 """
    long_term_guarantee_deposited: Optional[IxNonFractionPublic] = Field(default=None, description='長期預り保証金')
    """ 長期預り保証金 """
    long_term_lease_and_guarantee_deposited: Optional[IxNonFractionPublic] = Field(default=None, description='長期預り敷金保証金')
    """ 長期預り敷金保証金 """
    long_term_lease_deposited: Optional[IxNonFractionPublic] = Field(default=None, description='長期預り敷金')
    """ 長期預り敷金 """
    long_term_loans_payable: Optional[IxNonFractionPublic] = Field(default=None, description='長期借入金')
    """ 長期借入金 """
    long_term_loans_payable_to_subsidiaries_and_affiliates: Optional[IxNonFractionPublic] = Field(default=None, description='関係会社長期借入金')
    """ 関係会社長期借入金 """
    long_term_loans_receivable: Optional[IxNonFractionPublic] = Field(default=None, description='長期貸付金')
    """ 長期貸付金 """
    long_term_loans_receivable_from_directors_and_employees: Optional[IxNonFractionPublic] = Field(default=None, description='役員及び従業員に対する長期貸付金')
    """ 役員及び従業員に対する長期貸付金 """
    long_term_loans_receivable_from_employees: Optional[IxNonFractionPublic] = Field(default=None, description='従業員に対する長期貸付金')
    """ 従業員に対する長期貸付金 """
    long_term_loans_receivable_from_subsidiaries_and_affiliates: Optional[IxNonFractionPublic] = Field(default=None, description='関係会社長期貸付金')
    """ 関係会社長期貸付金 """
    long_term_payables_under_fluidity_lease_receivables_ncllea: Optional[IxNonFractionPublic] = Field(default=None, description='債権流動化に伴う長期支払債務、固定負債、リース事業')
    """ 債権流動化に伴う長期支払債務、固定負債、リース事業 """
    long_term_prepaid_expenses: Optional[IxNonFractionPublic] = Field(default=None, description='長期前払費用')
    """ 長期前払費用 """
    long_term_time_deposits: Optional[IxNonFractionPublic] = Field(default=None, description='長期預金')
    """ 長期預金 """
    long_term_unearned_revenue: Optional[IxNonFractionPublic] = Field(default=None, description='長期前受収益')
    """ 長期前受収益 """
    loss_adjustment_expenses_oeins: Optional[IxNonFractionPublic] = Field(default=None, description='損害調査費、経常費用、保険業')
    """ 損害調査費、経常費用、保険業 """
    loss_gain_on_cancellation_of_insurance_contract_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='保険解約損益（△は益）、営業活動によるキャッシュ・フロー')
    """ 保険解約損益（△は益）、営業活動によるキャッシュ・フロー """
    loss_gain_on_change_in_equity_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='持分変動損益（△は益）、営業活動によるキャッシュ・フロー')
    """ 持分変動損益（△は益）、営業活動によるキャッシュ・フロー """
    loss_gain_on_disposal_of_noncurrent_assets_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='固定資産処分損益（△は益）、営業活動によるキャッシュ・フロー')
    """ 固定資産処分損益（△は益）、営業活動によるキャッシュ・フロー """
    loss_gain_on_disposal_of_property_plant_and_equipment_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='有形固定資産処分損益（△は益）、営業活動によるキャッシュ・フロー')
    """ 有形固定資産処分損益（△は益）、営業活動によるキャッシュ・フロー """
    loss_gain_on_extinguishment_of_tie_in_shares_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='抱合せ株式消滅差損益（△は益）、営業活動によるキャッシュ・フロー')
    """ 抱合せ株式消滅差損益（△は益）、営業活動によるキャッシュ・フロー """
    loss_gain_on_investments_in_partnership_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='投資事業組合運用損益（△は益）、営業活動によるキャッシュ・フロー')
    """ 投資事業組合運用損益（△は益）、営業活動によるキャッシュ・フロー """
    loss_gain_on_liquidation_of_subsidiaries_and_affiliates_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='関係会社清算損益（△は益）、営業活動によるキャッシュ・フロー')
    """ 関係会社清算損益（△は益）、営業活動によるキャッシュ・フロー """
    loss_gain_on_liquidation_of_subsidiaries_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='子会社清算損益（△は益）、営業活動によるキャッシュ・フロー')
    """ 子会社清算損益（△は益）、営業活動によるキャッシュ・フロー """
    loss_gain_on_money_held_in_trust_ope_cfbnk: Optional[IxNonFractionPublic] = Field(default=None, description='金銭の信託の運用損益（△は運用益）、営業活動によるキャッシュ・フロー、銀行業')
    """ 金銭の信託の運用損益（△は運用益）、営業活動によるキャッシュ・フロー、銀行業 """
    loss_gain_on_operation_of_investments_in_capital_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='出資金運用損益（△は益）、営業活動によるキャッシュ・フロー')
    """ 出資金運用損益（△は益）、営業活動によるキャッシュ・フロー """
    loss_gain_on_redemption_of_investment_securities_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='投資有価証券償還損益（△は益）、営業活動によるキャッシュ・フロー')
    """ 投資有価証券償還損益（△は益）、営業活動によるキャッシュ・フロー """
    loss_gain_on_redemption_of_securities_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='有価証券償還損益（△は益）、営業活動によるキャッシュ・フロー')
    """ 有価証券償還損益（△は益）、営業活動によるキャッシュ・フロー """
    loss_gain_on_sales_and_retirement_of_noncurrent_assets_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='固定資産除売却損益（△は益）、営業活動によるキャッシュ・フロー')
    """ 固定資産除売却損益（△は益）、営業活動によるキャッシュ・フロー """
    loss_gain_on_sales_and_retirement_of_property_plant_and_equipment_and_intangible_assets_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='有形及び無形固定資産除売却損益（△は益）、営業活動によるキャッシュ・フロー')
    """ 有形及び無形固定資産除売却損益（△は益）、営業活動によるキャッシュ・フロー """
    loss_gain_on_sales_and_retirement_of_property_plant_and_equipment_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='有形固定資産除売却損益（△は益）、営業活動によるキャッシュ・フロー')
    """ 有形固定資産除売却損益（△は益）、営業活動によるキャッシュ・フロー """
    loss_gain_on_sales_and_valuation_of_investment_securities_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='投資有価証券売却及び評価損益（△は益）、営業活動によるキャッシュ・フロー')
    """ 投資有価証券売却及び評価損益（△は益）、営業活動によるキャッシュ・フロー """
    loss_gain_on_sales_of_golf_club_memberships_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='ゴルフ会員権売却損益（△は益）、営業活動によるキャッシュ・フロー')
    """ ゴルフ会員権売却損益（△は益）、営業活動によるキャッシュ・フロー """
    loss_gain_on_sales_of_investment_securities_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='投資有価証券売却損益（△は益）、営業活動によるキャッシュ・フロー')
    """ 投資有価証券売却損益（△は益）、営業活動によるキャッシュ・フロー """
    loss_gain_on_sales_of_membership_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='会員権売却損益（△は益）、営業活動によるキャッシュ・フロー')
    """ 会員権売却損益（△は益）、営業活動によるキャッシュ・フロー """
    loss_gain_on_sales_of_noncurrent_assets_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='固定資産売却損益（△は益）、営業活動によるキャッシュ・フロー')
    """ 固定資産売却損益（△は益）、営業活動によるキャッシュ・フロー """
    loss_gain_on_sales_of_property_plant_and_equipment_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='有形固定資産売却損益（△は益）、営業活動によるキャッシュ・フロー')
    """ 有形固定資産売却損益（△は益）、営業活動によるキャッシュ・フロー """
    loss_gain_on_sales_of_securities_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='有価証券売却損益（△は益）、営業活動によるキャッシュ・フロー')
    """ 有価証券売却損益（△は益）、営業活動によるキャッシュ・フロー """
    loss_gain_on_sales_of_short_term_and_long_term_investment_securities_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='有価証券及び投資有価証券売却損益（△は益）、営業活動によるキャッシュ・フロー')
    """ 有価証券及び投資有価証券売却損益（△は益）、営業活動によるキャッシュ・フロー """
    loss_gain_on_sales_of_stocks_of_subsidiaries_and_affiliates_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='関係会社株式売却損益（△は益）、営業活動によるキャッシュ・フロー')
    """ 関係会社株式売却損益（△は益）、営業活動によるキャッシュ・フロー """
    loss_gain_on_sales_of_subsidiaries_stocks_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='子会社株式売却損益（△は益）、営業活動によるキャッシュ・フロー')
    """ 子会社株式売却損益（△は益）、営業活動によるキャッシュ・フロー """
    loss_gain_on_step_acquisitions_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='段階取得に係る差損益（△は益）、営業活動によるキャッシュ・フロー')
    """ 段階取得に係る差損益（△は益）、営業活動によるキャッシュ・フロー """
    loss_gain_on_transfer_of_business_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='事業譲渡損益（△は益）、営業活動によるキャッシュ・フロー')
    """ 事業譲渡損益（△は益）、営業活動によるキャッシュ・フロー """
    loss_gain_on_valuation_of_compound_financial_instruments_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='複合金融商品評価損益（△は益）、営業活動によるキャッシュ・フロー')
    """ 複合金融商品評価損益（△は益）、営業活動によるキャッシュ・フロー """
    loss_gain_on_valuation_of_derivatives_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='デリバティブ評価損益（△は益）、営業活動によるキャッシュ・フロー')
    """ デリバティブ評価損益（△は益）、営業活動によるキャッシュ・フロー """
    loss_gain_on_valuation_of_investment_securities_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='投資有価証券評価損益（△は益）、営業活動によるキャッシュ・フロー')
    """ 投資有価証券評価損益（△は益）、営業活動によるキャッシュ・フロー """
    loss_gain_on_valuation_of_securities_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='有価証券評価損益（△は益）、営業活動によるキャッシュ・フロー')
    """ 有価証券評価損益（△は益）、営業活動によるキャッシュ・フロー """
    loss_gain_on_valuation_of_short_term_and_long_term_investment_securities_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='有価証券及び投資有価証券評価損益（△は益）、営業活動によるキャッシュ・フロー')
    """ 有価証券及び投資有価証券評価損益（△は益）、営業活動によるキャッシュ・フロー """
    loss_gain_related_to_property_plant_and_equipment_ope_cfins: Optional[IxNonFractionPublic] = Field(default=None, description='有形固定資産関係損益（△は益）、営業活動によるキャッシュ・フロー、保険業')
    """ 有形固定資産関係損益（△は益）、営業活動によるキャッシュ・フロー、保険業 """
    loss_gain_related_to_securities_ope_cfbnk: Optional[IxNonFractionPublic] = Field(default=None, description='有価証券関係損益（△）、営業活動によるキャッシュ・フロー、銀行業')
    """ 有価証券関係損益（△）、営業活動によるキャッシュ・フロー、銀行業 """
    loss_gain_related_to_securities_ope_cfins: Optional[IxNonFractionPublic] = Field(default=None, description='有価証券関係損益（△は益）、営業活動によるキャッシュ・フロー、保険業')
    """ 有価証券関係損益（△は益）、営業活動によるキャッシュ・フロー、保険業 """
    loss_on_abandonment_of_inventories_el: Optional[IxNonFractionPublic] = Field(default=None, description='棚卸資産廃棄損、特別損失')
    """ 棚卸資産廃棄損、特別損失 """
    loss_on_abandonment_of_inventories_noe: Optional[IxNonFractionPublic] = Field(default=None, description='棚卸資産廃棄損、営業外費用')
    """ 棚卸資産廃棄損、営業外費用 """
    loss_on_abandonment_of_inventories_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='棚卸資産廃棄損、営業活動によるキャッシュ・フロー')
    """ 棚卸資産廃棄損、営業活動によるキャッシュ・フロー """
    loss_on_abandonment_of_noncurrent_assets_el: Optional[IxNonFractionPublic] = Field(default=None, description='固定資産廃棄損、特別損失')
    """ 固定資産廃棄損、特別損失 """
    loss_on_abandonment_of_noncurrent_assets_noe: Optional[IxNonFractionPublic] = Field(default=None, description='固定資産廃棄損、営業外費用')
    """ 固定資産廃棄損、営業外費用 """
    loss_on_abandonment_of_noncurrent_assets_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='固定資産廃棄損、営業活動によるキャッシュ・フロー')
    """ 固定資産廃棄損、営業活動によるキャッシュ・フロー """
    loss_on_business_restructuring_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='事業再編損、営業活動によるキャッシュ・フロー')
    """ 事業再編損、営業活動によるキャッシュ・フロー """
    loss_on_business_withdrawal_el: Optional[IxNonFractionPublic] = Field(default=None, description='事業撤退損、特別損失')
    """ 事業撤退損、特別損失 """
    loss_on_cancel_of_lease_contracts_noe: Optional[IxNonFractionPublic] = Field(default=None, description='リース解約損、営業外費用')
    """ リース解約損、営業外費用 """
    loss_on_cancellation_of_lease_contracts_el: Optional[IxNonFractionPublic] = Field(default=None, description='リース解約損、特別損失')
    """ リース解約損、特別損失 """
    loss_on_cancellation_of_leasehold_contracts_el: Optional[IxNonFractionPublic] = Field(default=None, description='賃貸借契約解約損、特別損失')
    """ 賃貸借契約解約損、特別損失 """
    loss_on_cancellation_of_leases_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='リース解約損、営業活動によるキャッシュ・フロー')
    """ リース解約損、営業活動によるキャッシュ・フロー """
    loss_on_cancellation_of_rental_contract_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='賃貸借契約解約損、営業活動によるキャッシュ・フロー')
    """ 賃貸借契約解約損、営業活動によるキャッシュ・フロー """
    loss_on_change_in_equity_el: Optional[IxNonFractionPublic] = Field(default=None, description='持分変動損失、特別損失')
    """ 持分変動損失、特別損失 """
    loss_on_closing_of_stores_el: Optional[IxNonFractionPublic] = Field(default=None, description='店舗閉鎖損失、特別損失')
    """ 店舗閉鎖損失、特別損失 """
    loss_on_disaster2_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='災害による損失、営業活動によるキャッシュ・フロー')
    """ 災害による損失、営業活動によるキャッシュ・フロー """
    loss_on_disaster_el: Optional[IxNonFractionPublic] = Field(default=None, description='災害による損失、特別損失')
    """ 災害による損失、特別損失 """
    loss_on_disposal_of_inventories_el: Optional[IxNonFractionPublic] = Field(default=None, description='棚卸資産処分損、特別損失')
    """ 棚卸資産処分損、特別損失 """
    loss_on_disposal_of_inventories_noe: Optional[IxNonFractionPublic] = Field(default=None, description='棚卸資産処分損、営業外費用')
    """ 棚卸資産処分損、営業外費用 """
    loss_on_disposal_of_noncurrent_assets_el: Optional[IxNonFractionPublic] = Field(default=None, description='固定資産処分損、特別損失')
    """ 固定資産処分損、特別損失 """
    loss_on_disposal_of_noncurrent_assets_noe: Optional[IxNonFractionPublic] = Field(default=None, description='固定資産処分損、営業外費用')
    """ 固定資産処分損、営業外費用 """
    loss_on_extinguishment_of_tie_in_shares_el: Optional[IxNonFractionPublic] = Field(default=None, description='抱合せ株式消滅差損、特別損失')
    """ 抱合せ株式消滅差損、特別損失 """
    loss_on_insurance_cancellation_el: Optional[IxNonFractionPublic] = Field(default=None, description='保険解約損、特別損失')
    """ 保険解約損、特別損失 """
    loss_on_insurance_cancellation_noe: Optional[IxNonFractionPublic] = Field(default=None, description='保険解約損、営業外費用')
    """ 保険解約損、営業外費用 """
    loss_on_investments_in_capital_noe: Optional[IxNonFractionPublic] = Field(default=None, description='出資金運用損、営業外費用')
    """ 出資金運用損、営業外費用 """
    loss_on_investments_in_partnership_noe: Optional[IxNonFractionPublic] = Field(default=None, description='投資事業組合運用損、営業外費用')
    """ 投資事業組合運用損、営業外費用 """
    loss_on_liquidation_of_business_el: Optional[IxNonFractionPublic] = Field(default=None, description='事業整理損、特別損失')
    """ 事業整理損、特別損失 """
    loss_on_liquidation_of_business_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='事業整理損、営業活動によるキャッシュ・フロー')
    """ 事業整理損、営業活動によるキャッシュ・フロー """
    loss_on_liquidation_of_subsidiaries_and_affiliates_el: Optional[IxNonFractionPublic] = Field(default=None, description='関係会社清算損、特別損失')
    """ 関係会社清算損、特別損失 """
    loss_on_liquidation_of_subsidiaries_and_affiliates_general_el: Optional[IxNonFractionPublic] = Field(default=None, description='関係会社整理損、特別損失')
    """ 関係会社整理損、特別損失 """
    loss_on_liquidation_of_subsidiaries_and_affiliates_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='関係会社整理損、営業活動によるキャッシュ・フロー')
    """ 関係会社整理損、営業活動によるキャッシュ・フロー """
    loss_on_liquidation_of_subsidiaries_el: Optional[IxNonFractionPublic] = Field(default=None, description='子会社清算損、特別損失')
    """ 子会社清算損、特別損失 """
    loss_on_liquidation_of_subsidiaries_general_el: Optional[IxNonFractionPublic] = Field(default=None, description='子会社整理損、特別損失')
    """ 子会社整理損、特別損失 """
    loss_on_liquidation_of_subsidiaries_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='子会社整理損、営業活動によるキャッシュ・フロー')
    """ 子会社整理損、営業活動によるキャッシュ・フロー """
    loss_on_litigation_el: Optional[IxNonFractionPublic] = Field(default=None, description='訴訟関連損失、特別損失')
    """ 訴訟関連損失、特別損失 """
    loss_on_redemption_of_securities_noe: Optional[IxNonFractionPublic] = Field(default=None, description='有価証券償還損、営業外費用')
    """ 有価証券償還損、営業外費用 """
    loss_on_reduction_of_noncurrent_assets_el: Optional[IxNonFractionPublic] = Field(default=None, description='固定資産圧縮損、特別損失')
    """ 固定資産圧縮損、特別損失 """
    loss_on_reduction_of_noncurrent_assets_noe: Optional[IxNonFractionPublic] = Field(default=None, description='固定資産圧縮損、営業外費用')
    """ 固定資産圧縮損、営業外費用 """
    loss_on_reduction_of_noncurrent_assets_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='固定資産圧縮損、営業活動によるキャッシュ・フロー')
    """ 固定資産圧縮損、営業活動によるキャッシュ・フロー """
    loss_on_retirement_of_inventories_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='棚卸資産除却損、営業活動によるキャッシュ・フロー')
    """ 棚卸資産除却損、営業活動によるキャッシュ・フロー """
    loss_on_retirement_of_noncurrent_assets_el: Optional[IxNonFractionPublic] = Field(default=None, description='固定資産除却損、特別損失')
    """ 固定資産除却損、特別損失 """
    loss_on_retirement_of_noncurrent_assets_noe: Optional[IxNonFractionPublic] = Field(default=None, description='固定資産除却損、営業外費用')
    """ 固定資産除却損、営業外費用 """
    loss_on_retirement_of_noncurrent_assets_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='固定資産除却損、営業活動によるキャッシュ・フロー')
    """ 固定資産除却損、営業活動によるキャッシュ・フロー """
    loss_on_retirement_of_property_plant_and_equipment_el: Optional[IxNonFractionPublic] = Field(default=None, description='有形固定資産除却損、特別損失')
    """ 有形固定資産除却損、特別損失 """
    loss_on_retirement_of_property_plant_and_equipment_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='有形固定資産除却損、営業活動によるキャッシュ・フロー')
    """ 有形固定資産除却損、営業活動によるキャッシュ・フロー """
    loss_on_sales_and_retirement_of_noncurrent_assets_el: Optional[IxNonFractionPublic] = Field(default=None, description='固定資産除売却損、特別損失')
    """ 固定資産除売却損、特別損失 """
    loss_on_sales_and_retirement_of_noncurrent_assets_noe: Optional[IxNonFractionPublic] = Field(default=None, description='固定資産除売却損、営業外費用')
    """ 固定資産除売却損、営業外費用 """
    loss_on_sales_of_accounts_receivable_noe: Optional[IxNonFractionPublic] = Field(default=None, description='売上債権売却損、営業外費用')
    """ 売上債権売却損、営業外費用 """
    loss_on_sales_of_electronically_recorded_monetary_claims_noe: Optional[IxNonFractionPublic] = Field(default=None, description='電子記録債権売却損、営業外費用')
    """ 電子記録債権売却損、営業外費用 """
    loss_on_sales_of_investment_securities_el: Optional[IxNonFractionPublic] = Field(default=None, description='投資有価証券売却損、特別損失')
    """ 投資有価証券売却損、特別損失 """
    loss_on_sales_of_investment_securities_noe: Optional[IxNonFractionPublic] = Field(default=None, description='投資有価証券売却損、営業外費用')
    """ 投資有価証券売却損、営業外費用 """
    loss_on_sales_of_membership_el: Optional[IxNonFractionPublic] = Field(default=None, description='会員権売却損、特別損失')
    """ 会員権売却損、特別損失 """
    loss_on_sales_of_noncurrent_assets_el: Optional[IxNonFractionPublic] = Field(default=None, description='固定資産売却損、特別損失')
    """ 固定資産売却損、特別損失 """
    loss_on_sales_of_notes_payable_noe: Optional[IxNonFractionPublic] = Field(default=None, description='手形売却損、営業外費用')
    """ 手形売却損、営業外費用 """
    loss_on_sales_of_securities_noe: Optional[IxNonFractionPublic] = Field(default=None, description='有価証券売却損、営業外費用')
    """ 有価証券売却損、営業外費用 """
    loss_on_sales_of_stocks_of_subsidiaries_and_affiliates_el: Optional[IxNonFractionPublic] = Field(default=None, description='関係会社株式売却損、特別損失')
    """ 関係会社株式売却損、特別損失 """
    loss_on_sales_of_subsidiaries_stocks_el: Optional[IxNonFractionPublic] = Field(default=None, description='子会社株式売却損、特別損失')
    """ 子会社株式売却損、特別損失 """
    loss_on_step_acquisitions_el: Optional[IxNonFractionPublic] = Field(default=None, description='段階取得に係る差損、特別損失')
    """ 段階取得に係る差損、特別損失 """
    loss_on_store_closings_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='店舗閉鎖損失、営業活動によるキャッシュ・フロー')
    """ 店舗閉鎖損失、営業活動によるキャッシュ・フロー """
    loss_on_support_to_subsidiaries_and_subsidiaries_and_affiliates_el: Optional[IxNonFractionPublic] = Field(default=None, description='関係会社支援損、特別損失')
    """ 関係会社支援損、特別損失 """
    loss_on_transfer_of_business_el: Optional[IxNonFractionPublic] = Field(default=None, description='事業譲渡損、特別損失')
    """ 事業譲渡損、特別損失 """
    loss_on_transfer_of_receivables_noe: Optional[IxNonFractionPublic] = Field(default=None, description='債権売却損、営業外費用')
    """ 債権売却損、営業外費用 """
    loss_on_valuation_of_compound_financial_instruments_noe: Optional[IxNonFractionPublic] = Field(default=None, description='複合金融商品評価損、営業外費用')
    """ 複合金融商品評価損、営業外費用 """
    loss_on_valuation_of_derivatives_noe: Optional[IxNonFractionPublic] = Field(default=None, description='デリバティブ評価損、営業外費用')
    """ デリバティブ評価損、営業外費用 """
    loss_on_valuation_of_golf_club_membership_el: Optional[IxNonFractionPublic] = Field(default=None, description='ゴルフ会員権評価損、特別損失')
    """ ゴルフ会員権評価損、特別損失 """
    loss_on_valuation_of_golf_club_memberships_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='ゴルフ会員権評価損、営業活動によるキャッシュ・フロー')
    """ ゴルフ会員権評価損、営業活動によるキャッシュ・フロー """
    loss_on_valuation_of_inventories_el: Optional[IxNonFractionPublic] = Field(default=None, description='棚卸資産評価損、特別損失')
    """ 棚卸資産評価損、特別損失 """
    loss_on_valuation_of_inventories_noe: Optional[IxNonFractionPublic] = Field(default=None, description='棚卸資産評価損、営業外費用')
    """ 棚卸資産評価損、営業外費用 """
    loss_on_valuation_of_investment_securities_el: Optional[IxNonFractionPublic] = Field(default=None, description='投資有価証券評価損、特別損失')
    """ 投資有価証券評価損、特別損失 """
    loss_on_valuation_of_investment_securities_noe: Optional[IxNonFractionPublic] = Field(default=None, description='投資有価証券評価損、営業外費用')
    """ 投資有価証券評価損、営業外費用 """
    loss_on_valuation_of_membership_el: Optional[IxNonFractionPublic] = Field(default=None, description='会員権評価損、特別損失')
    """ 会員権評価損、特別損失 """
    loss_on_valuation_of_membership_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='会員権評価損、営業活動によるキャッシュ・フロー')
    """ 会員権評価損、営業活動によるキャッシュ・フロー """
    loss_on_valuation_of_securities_oeins: Optional[IxNonFractionPublic] = Field(default=None, description='有価証券評価損、経常費用、保険業')
    """ 有価証券評価損、経常費用、保険業 """
    loss_on_valuation_of_stocks_of_subsidiaries_and_affiliates_el: Optional[IxNonFractionPublic] = Field(default=None, description='関係会社株式評価損、特別損失')
    """ 関係会社株式評価損、特別損失 """
    loss_on_valuation_of_stocks_of_subsidiaries_and_affiliates_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='関係会社株式評価損、営業活動によるキャッシュ・フロー')
    """ 関係会社株式評価損、営業活動によるキャッシュ・フロー """
    machinery_and_equipment: Optional[IxNonFractionPublic] = Field(default=None, description='機械及び装置')
    """ 機械及び装置 """
    machinery_and_equipment_net: Optional[IxNonFractionPublic] = Field(default=None, description='機械及び装置（純額）')
    """ 機械及び装置（純額） """
    machinery_equipment_and_vehicles: Optional[IxNonFractionPublic] = Field(default=None, description='機械装置及び運搬具')
    """ 機械装置及び運搬具 """
    machinery_equipment_and_vehicles_net: Optional[IxNonFractionPublic] = Field(default=None, description='機械装置及び運搬具（純額）')
    """ 機械装置及び運搬具（純額） """
    machinery_vehicles_tools_furniture_and_fixtures: Optional[IxNonFractionPublic] = Field(default=None, description='機械、運搬具及び工具器具備品')
    """ 機械、運搬具及び工具器具備品 """
    machinery_vehicles_tools_furniture_and_fixtures_net: Optional[IxNonFractionPublic] = Field(default=None, description='機械、運搬具及び工具器具備品（純額）')
    """ 機械、運搬具及び工具器具備品（純額） """
    medical_expenses_sga: Optional[IxNonFractionPublic] = Field(default=None, description='衛生費、販売費及び一般管理費')
    """ 衛生費、販売費及び一般管理費 """
    membership: Optional[IxNonFractionPublic] = Field(default=None, description='会員権')
    """ 会員権 """
    merchandise: Optional[IxNonFractionPublic] = Field(default=None, description='商品')
    """ 商品 """
    merchandise_and_finished_goods: Optional[IxNonFractionPublic] = Field(default=None, description='商品及び製品')
    """ 商品及び製品 """
    miscellaneous_expenses_gas: Optional[IxNonFractionPublic] = Field(default=None, description='雑支出、ガス事業')
    """ 雑支出、ガス事業 """
    miscellaneous_expenses_noe: Optional[IxNonFractionPublic] = Field(default=None, description='雑支出、営業外費用')
    """ 雑支出、営業外費用 """
    miscellaneous_expenses_noerwy: Optional[IxNonFractionPublic] = Field(default=None, description='雑支出、営業外費用、鉄道事業')
    """ 雑支出、営業外費用、鉄道事業 """
    miscellaneous_expenses_sga: Optional[IxNonFractionPublic] = Field(default=None, description='雑費、販売費及び一般管理費')
    """ 雑費、販売費及び一般管理費 """
    miscellaneous_income_gas: Optional[IxNonFractionPublic] = Field(default=None, description='雑収入、ガス事業')
    """ 雑収入、ガス事業 """
    miscellaneous_income_noi: Optional[IxNonFractionPublic] = Field(default=None, description='雑収入、営業外収益')
    """ 雑収入、営業外収益 """
    miscellaneous_income_noirwy: Optional[IxNonFractionPublic] = Field(default=None, description='雑収入、営業外収益、鉄道事業')
    """ 雑収入、営業外収益、鉄道事業 """
    miscellaneous_loss_noe: Optional[IxNonFractionPublic] = Field(default=None, description='雑損失、営業外費用')
    """ 雑損失、営業外費用 """
    monetary_claims_bought_assets_bnk: Optional[IxNonFractionPublic] = Field(default=None, description='買入金銭債権、資産の部、銀行業')
    """ 買入金銭債権、資産の部、銀行業 """
    money_held_in_trust_assets_bnk: Optional[IxNonFractionPublic] = Field(default=None, description='金銭の信託、資産の部、銀行業')
    """ 金銭の信託、資産の部、銀行業 """
    negative_goodwill: Optional[IxNonFractionPublic] = Field(default=None, description='負ののれん')
    """ 負ののれん """
    negotiable_certificates_of_deposit_liabilities_bnk: Optional[IxNonFractionPublic] = Field(default=None, description='譲渡性預金、負債の部、銀行業')
    """ 譲渡性預金、負債の部、銀行業 """
    net_assets: Optional[IxNonFractionPublic] = Field(default=None, description='純資産')
    """ 純資産 """
    net_cash_provided_by_used_in_financing_activities: Optional[IxNonFractionPublic] = Field(default=None, description='財務活動によるキャッシュ・フロー')
    """ 財務活動によるキャッシュ・フロー """
    net_cash_provided_by_used_in_investment_activities: Optional[IxNonFractionPublic] = Field(default=None, description='投資活動によるキャッシュ・フロー')
    """ 投資活動によるキャッシュ・フロー """
    net_cash_provided_by_used_in_operating_activities: Optional[IxNonFractionPublic] = Field(default=None, description='営業活動によるキャッシュ・フロー')
    """ 営業活動によるキャッシュ・フロー """
    net_changes_of_items_other_than_shareholders_equity: Optional[IxNonFractionPublic] = Field(default=None, description='株主資本以外の項目の当期変動額（純額）')
    """ 株主資本以外の項目の当期変動額（純額） """
    net_decrease_increase_in_call_loans_ope_cfbnk: Optional[IxNonFractionPublic] = Field(default=None, description='コールローン等の純増（△）減、営業活動によるキャッシュ・フロー、銀行業')
    """ コールローン等の純増（△）減、営業活動によるキャッシュ・フロー、銀行業 """
    net_decrease_increase_in_deposit_excluding_deposit_paid_to_bank_of_japan_ope_cfbnk: Optional[IxNonFractionPublic] = Field(default=None, description='預け金（日銀預け金を除く）の純増（△）減、営業活動によるキャッシュ・フロー、銀行業')
    """ 預け金（日銀預け金を除く）の純増（△）減、営業活動によるキャッシュ・フロー、銀行業 """
    net_decrease_increase_in_foreign_exchanges_assets_ope_cfbnk: Optional[IxNonFractionPublic] = Field(default=None, description='外国為替（資産）の純増（△）減、営業活動によるキャッシュ・フロー、銀行業')
    """ 外国為替（資産）の純増（△）減、営業活動によるキャッシュ・フロー、銀行業 """
    net_decrease_increase_in_lease_receivables_and_investment_assets_ope_cfbnk: Optional[IxNonFractionPublic] = Field(default=None, description='リース債権及びリース投資資産の純増（△）減、営業活動によるキャッシュ・フロー、銀行業')
    """ リース債権及びリース投資資産の純増（△）減、営業活動によるキャッシュ・フロー、銀行業 """
    net_decrease_increase_in_loans_and_bills_discounted_ope_cfbnk: Optional[IxNonFractionPublic] = Field(default=None, description='貸出金の純増（△）減、営業活動によるキャッシュ・フロー、銀行業')
    """ 貸出金の純増（△）減、営業活動によるキャッシュ・フロー、銀行業 """
    net_decrease_increase_in_receivables_under_securities_borrowing_transactions_ope_cfbnk: Optional[IxNonFractionPublic] = Field(default=None, description='債券貸借取引支払保証金の純増（△）減、営業活動によるキャッシュ・フロー、銀行業')
    """ 債券貸借取引支払保証金の純増（△）減、営業活動によるキャッシュ・フロー、銀行業 """
    net_decrease_increase_in_short_term_investment_securities_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='有価証券の純増減額（△は増加）、投資活動によるキャッシュ・フロー')
    """ 有価証券の純増減額（△は増加）、投資活動によるキャッシュ・フロー """
    net_decrease_increase_in_short_term_loans_receivable_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='短期貸付金の純増減額（△は増加）、投資活動によるキャッシュ・フロー')
    """ 短期貸付金の純増減額（△は増加）、投資活動によるキャッシュ・フロー """
    net_decrease_increase_in_time_deposits_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='定期預金の純増減額（△は増加）、投資活動によるキャッシュ・フロー')
    """ 定期預金の純増減額（△は増加）、投資活動によるキャッシュ・フロー """
    net_decrease_increase_in_trading_account_securities_ope_cfbnk: Optional[IxNonFractionPublic] = Field(default=None, description='商品有価証券の純増（△）減、営業活動によるキャッシュ・フロー、銀行業')
    """ 商品有価証券の純増（△）減、営業活動によるキャッシュ・フロー、銀行業 """
    net_decrease_increase_in_treasury_stock_fin_cf: Optional[IxNonFractionPublic] = Field(default=None, description='自己株式の純増減額（△は増加）、財務活動によるキャッシュ・フロー')
    """ 自己株式の純増減額（△は増加）、財務活動によるキャッシュ・フロー """
    net_defined_benefit_asset: Optional[IxNonFractionPublic] = Field(default=None, description='退職給付に係る資産')
    """ 退職給付に係る資産 """
    net_defined_benefit_liability: Optional[IxNonFractionPublic] = Field(default=None, description='退職給付に係る負債')
    """ 退職給付に係る負債 """
    net_increase_decrease_in_borrowed_money_excluding_subordinated_borrowings_ope_cfbnk: Optional[IxNonFractionPublic] = Field(default=None, description='借用金（劣後特約付借入金を除く）の純増減（△）、営業活動によるキャッシュ・フロー、銀行業')
    """ 借用金（劣後特約付借入金を除く）の純増減（△）、営業活動によるキャッシュ・フロー、銀行業 """
    net_increase_decrease_in_borrowed_money_from_trust_account_ope_cfbnk: Optional[IxNonFractionPublic] = Field(default=None, description='信託勘定借の純増減（△）、営業活動によるキャッシュ・フロー、銀行業')
    """ 信託勘定借の純増減（△）、営業活動によるキャッシュ・フロー、銀行業 """
    net_increase_decrease_in_call_money_ope_cfbnk: Optional[IxNonFractionPublic] = Field(default=None, description='コールマネー等の純増減（△）、営業活動によるキャッシュ・フロー、銀行業')
    """ コールマネー等の純増減（△）、営業活動によるキャッシュ・フロー、銀行業 """
    net_increase_decrease_in_cash_and_cash_equivalents: Optional[IxNonFractionPublic] = Field(default=None, description='現金及び現金同等物の増減額（△は減少）')
    """ 現金及び現金同等物の増減額（△は減少） """
    net_increase_decrease_in_cash_and_deposits_inv_cfins: Optional[IxNonFractionPublic] = Field(default=None, description='預貯金の純増減額（△は増加）、投資活動によるキャッシュ・フロー、保険業')
    """ 預貯金の純増減額（△は増加）、投資活動によるキャッシュ・フロー、保険業 """
    net_increase_decrease_in_commercial_papers_fin_cf: Optional[IxNonFractionPublic] = Field(default=None, description='コマーシャル・ペーパーの純増減額（△は減少）、財務活動によるキャッシュ・フロー')
    """ コマーシャル・ペーパーの純増減額（△は減少）、財務活動によるキャッシュ・フロー """
    net_increase_decrease_in_deposit_ope_cfbnk: Optional[IxNonFractionPublic] = Field(default=None, description='預金の純増減（△）、営業活動によるキャッシュ・フロー、銀行業')
    """ 預金の純増減（△）、営業活動によるキャッシュ・フロー、銀行業 """
    net_increase_decrease_in_foreign_exchanges_liabilities_ope_cfbnk: Optional[IxNonFractionPublic] = Field(default=None, description='外国為替（負債）の純増減（△）、営業活動によるキャッシュ・フロー、銀行業')
    """ 外国為替（負債）の純増減（△）、営業活動によるキャッシュ・フロー、銀行業 """
    net_increase_decrease_in_negotiable_certificates_of_deposit_ope_cfbnk: Optional[IxNonFractionPublic] = Field(default=None, description='譲渡性預金の純増減（△）、営業活動によるキャッシュ・フロー、銀行業')
    """ 譲渡性預金の純増減（△）、営業活動によるキャッシュ・フロー、銀行業 """
    net_increase_decrease_in_payables_under_securities_lending_transactions_ope_cfbnk: Optional[IxNonFractionPublic] = Field(default=None, description='債券貸借取引受入担保金の純増減（△）、営業活動によるキャッシュ・フロー、銀行業')
    """ 債券貸借取引受入担保金の純増減（△）、営業活動によるキャッシュ・フロー、銀行業 """
    net_increase_decrease_in_short_term_loans_payable_fin_cf: Optional[IxNonFractionPublic] = Field(default=None, description='短期借入金の純増減額（△は減少）、財務活動によるキャッシュ・フロー')
    """ 短期借入金の純増減額（△は減少）、財務活動によるキャッシュ・フロー """
    net_loss_paid_oeins: Optional[IxNonFractionPublic] = Field(default=None, description='正味支払保険金、経常費用、保険業')
    """ 正味支払保険金、経常費用、保険業 """
    net_premiums_written_oiins: Optional[IxNonFractionPublic] = Field(default=None, description='正味収入保険料、経常収益、保険業')
    """ 正味収入保険料、経常収益、保険業 """
    net_sales: Optional[IxNonFractionPublic] = Field(default=None, description='売上高')
    """ 売上高 """
    net_sales_of_completed_construction_contracts_cns: Optional[IxNonFractionPublic] = Field(default=None, description='完成工事高、建設業')
    """ 完成工事高、建設業 """
    net_sales_of_finished_goods_rev_oa: Optional[IxNonFractionPublic] = Field(default=None, description='製品売上高、営業活動による収益')
    """ 製品売上高、営業活動による収益 """
    net_sales_of_goods_rev_oa: Optional[IxNonFractionPublic] = Field(default=None, description='商品売上高、営業活動による収益')
    """ 商品売上高、営業活動による収益 """
    net_sales_of_merchandise_and_finished_goods_rev_oa: Optional[IxNonFractionPublic] = Field(default=None, description='商品及び製品売上高、営業活動による収益')
    """ 商品及び製品売上高、営業活動による収益 """
    net_sales_of_real_estate_business_and_other_cns: Optional[IxNonFractionPublic] = Field(default=None, description='不動産事業等売上高、建設業')
    """ 不動産事業等売上高、建設業 """
    net_sales_of_side_line_business_cns: Optional[IxNonFractionPublic] = Field(default=None, description='兼業事業売上高、建設業')
    """ 兼業事業売上高、建設業 """
    non_controlling_interests: Optional[IxNonFractionPublic] = Field(default=None, description='非支配株主持分')
    """ 非支配株主持分 """
    non_operating_expenses: Optional[IxNonFractionPublic] = Field(default=None, description='営業外費用')
    """ 営業外費用 """
    non_operating_income: Optional[IxNonFractionPublic] = Field(default=None, description='営業外収益')
    """ 営業外収益 """
    noncurrent_assets: Optional[IxNonFractionPublic] = Field(default=None, description='固定資産')
    """ 固定資産 """
    noncurrent_liabilities: Optional[IxNonFractionPublic] = Field(default=None, description='固定負債')
    """ 固定負債 """
    notes_and_accounts_payable_trade: Optional[IxNonFractionPublic] = Field(default=None, description='支払手形及び買掛金')
    """ 支払手形及び買掛金 """
    notes_and_accounts_receivable_trade: Optional[IxNonFractionPublic] = Field(default=None, description='受取手形及び売掛金')
    """ 受取手形及び売掛金 """
    notes_and_accounts_receivable_trade_and_contract_assets: Optional[IxNonFractionPublic] = Field(default=None, description='受取手形、売掛金及び契約資産')
    """ 受取手形、売掛金及び契約資産 """
    notes_and_accounts_receivable_trade_net: Optional[IxNonFractionPublic] = Field(default=None, description='受取手形及び売掛金（純額）')
    """ 受取手形及び売掛金（純額） """
    notes_and_operating_accounts_payable_trade: Optional[IxNonFractionPublic] = Field(default=None, description='支払手形及び営業未払金')
    """ 支払手形及び営業未払金 """
    notes_and_operating_accounts_receivable_ca: Optional[IxNonFractionPublic] = Field(default=None, description='受取手形及び営業未収入金、流動資産')
    """ 受取手形及び営業未収入金、流動資産 """
    notes_payable_accounts_payable_for_construction_contracts_and_other_cns: Optional[IxNonFractionPublic] = Field(default=None, description='支払手形・工事未払金等、建設業')
    """ 支払手形・工事未払金等、建設業 """
    notes_payable_accounts_payable_for_construction_contracts_cns: Optional[IxNonFractionPublic] = Field(default=None, description='支払手形・工事未払金、建設業')
    """ 支払手形・工事未払金、建設業 """
    notes_payable_facilities: Optional[IxNonFractionPublic] = Field(default=None, description='設備関係支払手形')
    """ 設備関係支払手形 """
    notes_payable_trade: Optional[IxNonFractionPublic] = Field(default=None, description='支払手形')
    """ 支払手形 """
    notes_receivable_accounts_receivable_from_completed_construction_contracts_and_other_cns: Optional[IxNonFractionPublic] = Field(default=None, description='受取手形・完成工事未収入金等、建設業')
    """ 受取手形・完成工事未収入金等、建設業 """
    notes_receivable_accounts_receivable_from_completed_construction_contracts_cns: Optional[IxNonFractionPublic] = Field(default=None, description='受取手形・完成工事未収入金、建設業')
    """ 受取手形・完成工事未収入金、建設業 """
    notes_receivable_trade: Optional[IxNonFractionPublic] = Field(default=None, description='受取手形')
    """ 受取手形 """
    office_transfer_expenses_el: Optional[IxNonFractionPublic] = Field(default=None, description='事務所移転費用、特別損失')
    """ 事務所移転費用、特別損失 """
    office_transfer_expenses_noe: Optional[IxNonFractionPublic] = Field(default=None, description='事務所移転費用、営業外費用')
    """ 事務所移転費用、営業外費用 """
    office_work_fee_noi: Optional[IxNonFractionPublic] = Field(default=None, description='受取事務手数料、営業外収益')
    """ 受取事務手数料、営業外収益 """
    operating_accounts_payable: Optional[IxNonFractionPublic] = Field(default=None, description='営業未払金')
    """ 営業未払金 """
    operating_accounts_receivable_ca: Optional[IxNonFractionPublic] = Field(default=None, description='営業未収入金、流動資産')
    """ 営業未収入金、流動資産 """
    operating_cost: Optional[IxNonFractionPublic] = Field(default=None, description='営業原価')
    """ 営業原価 """
    operating_expenses: Optional[IxNonFractionPublic] = Field(default=None, description='営業費用')
    """ 営業費用 """
    operating_expenses_and_cost_of_sales_of_transportation_rwy: Optional[IxNonFractionPublic] = Field(default=None, description='運輸業等営業費及び売上原価、鉄道事業')
    """ 運輸業等営業費及び売上原価、鉄道事業 """
    operating_expenses_ins: Optional[IxNonFractionPublic] = Field(default=None, description='経常費用、保険業')
    """ 経常費用、保険業 """
    operating_expenses_rwy: Optional[IxNonFractionPublic] = Field(default=None, description='営業費、鉄道事業')
    """ 営業費、鉄道事業 """
    operating_gross_profit: Optional[IxNonFractionPublic] = Field(default=None, description='営業総利益又は営業総損失（△）')
    """ 営業総利益又は営業総損失（△） """
    operating_income: Optional[IxNonFractionPublic] = Field(default=None, description='営業利益又は営業損失（△）')
    """ 営業利益又は営業損失（△） """
    operating_income_ins: Optional[IxNonFractionPublic] = Field(default=None, description='経常収益、保険業')
    """ 経常収益、保険業 """
    operating_income_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='営業収入、営業活動によるキャッシュ・フロー')
    """ 営業収入、営業活動によるキャッシュ・フロー """
    operating_loans_ca: Optional[IxNonFractionPublic] = Field(default=None, description='営業貸付金、流動資産')
    """ 営業貸付金、流動資産 """
    operating_revenue1: Optional[IxNonFractionPublic] = Field(default=None, description='営業収益')
    """ 営業収益 """
    operating_revenue_cmd: Optional[IxNonFractionPublic] = Field(default=None, description='営業収益、商品先物取引業')
    """ 営業収益、商品先物取引業 """
    operating_revenue_rwy: Optional[IxNonFractionPublic] = Field(default=None, description='営業収益、鉄道事業')
    """ 営業収益、鉄道事業 """
    operational_investment_securities_ca: Optional[IxNonFractionPublic] = Field(default=None, description='営業投資有価証券、流動資産')
    """ 営業投資有価証券、流動資産 """
    ordinary_expenses_bnk: Optional[IxNonFractionPublic] = Field(default=None, description='経常費用、銀行業')
    """ 経常費用、銀行業 """
    ordinary_income: Optional[IxNonFractionPublic] = Field(default=None, description='経常利益又は経常損失（△）')
    """ 経常利益又は経常損失（△） """
    ordinary_income_bnk: Optional[IxNonFractionPublic] = Field(default=None, description='経常収益、銀行業')
    """ 経常収益、銀行業 """
    other_assets_assets_bnk: Optional[IxNonFractionPublic] = Field(default=None, description='その他資産、資産の部、銀行業')
    """ その他資産、資産の部、銀行業 """
    other_assets_assets_ins: Optional[IxNonFractionPublic] = Field(default=None, description='その他資産、資産の部、保険業')
    """ その他資産、資産の部、保険業 """
    other_ca: Optional[IxNonFractionPublic] = Field(default=None, description='その他、流動資産')
    """ その他、流動資産 """
    other_cl: Optional[IxNonFractionPublic] = Field(default=None, description='その他、流動負債')
    """ その他、流動負債 """
    other_cos_exp_oa: Optional[IxNonFractionPublic] = Field(default=None, description='その他、営業活動による費用・売上原価')
    """ その他、営業活動による費用・売上原価 """
    other_capital_surplus: Optional[IxNonFractionPublic] = Field(default=None, description='その他資本剰余金')
    """ その他資本剰余金 """
    other_comprehensive_income: Optional[IxNonFractionPublic] = Field(default=None, description='その他の包括利益')
    """ その他の包括利益 """
    other_cost_cos_exp_oa: Optional[IxNonFractionPublic] = Field(default=None, description='その他の原価、営業活動による費用・売上原価')
    """ その他の原価、営業活動による費用・売上原価 """
    other_ei: Optional[IxNonFractionPublic] = Field(default=None, description='その他、特別利益')
    """ その他、特別利益 """
    other_el: Optional[IxNonFractionPublic] = Field(default=None, description='その他、特別損失')
    """ その他、特別損失 """
    other_expenses_oebnk: Optional[IxNonFractionPublic] = Field(default=None, description='その他経常費用、経常費用、銀行業')
    """ その他経常費用、経常費用、銀行業 """
    other_expenses_sga: Optional[IxNonFractionPublic] = Field(default=None, description='その他の経費、販売費及び一般管理費')
    """ その他の経費、販売費及び一般管理費 """
    other_facilities_ppegas: Optional[IxNonFractionPublic] = Field(default=None, description='その他の設備、有形固定資産、ガス事業')
    """ その他の設備、有形固定資産、ガス事業 """
    other_financial_revenue_rev_oa: Optional[IxNonFractionPublic] = Field(default=None, description='その他の金融収益、営業活動による収益')
    """ その他の金融収益、営業活動による収益 """
    other_general_and_administrative_expenses_sga: Optional[IxNonFractionPublic] = Field(default=None, description='その他の一般管理費、販売費及び一般管理費')
    """ その他の一般管理費、販売費及び一般管理費 """
    other_ia: Optional[IxNonFractionPublic] = Field(default=None, description='その他、無形固定資産')
    """ その他、無形固定資産 """
    other_ioa: Optional[IxNonFractionPublic] = Field(default=None, description='その他、投資その他の資産')
    """ その他、投資その他の資産 """
    other_income_oibnk: Optional[IxNonFractionPublic] = Field(default=None, description='その他経常収益、経常収益、銀行業')
    """ その他経常収益、経常収益、銀行業 """
    other_intangible_assets_lea: Optional[IxNonFractionPublic] = Field(default=None, description='その他の無形固定資産、リース事業')
    """ その他の無形固定資産、リース事業 """
    other_inventories: Optional[IxNonFractionPublic] = Field(default=None, description='その他の棚卸資産')
    """ その他の棚卸資産 """
    other_liabilities_liabilities_bnk: Optional[IxNonFractionPublic] = Field(default=None, description='その他負債、負債の部、銀行業')
    """ その他負債、負債の部、銀行業 """
    other_liabilities_liabilities_ins: Optional[IxNonFractionPublic] = Field(default=None, description='その他負債、負債の部、保険業')
    """ その他負債、負債の部、保険業 """
    other_loss_gain_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='その他の損益（△は益）、営業活動によるキャッシュ・フロー')
    """ その他の損益（△は益）、営業活動によるキャッシュ・フロー """
    other_ncl: Optional[IxNonFractionPublic] = Field(default=None, description='その他、固定負債')
    """ その他、固定負債 """
    other_noe: Optional[IxNonFractionPublic] = Field(default=None, description='その他、営業外費用')
    """ その他、営業外費用 """
    other_noi: Optional[IxNonFractionPublic] = Field(default=None, description='その他、営業外収益')
    """ その他、営業外収益 """
    other_net_fin_cf: Optional[IxNonFractionPublic] = Field(default=None, description='その他、財務活動によるキャッシュ・フロー')
    """ その他、財務活動によるキャッシュ・フロー """
    other_net_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='その他、投資活動によるキャッシュ・フロー')
    """ その他、投資活動によるキャッシュ・フロー """
    other_net_inv_cf_subtotal_ins: Optional[IxNonFractionPublic] = Field(default=None, description='その他、投資活動によるキャッシュ・フロー、小計の下、保険業')
    """ その他、投資活動によるキャッシュ・フロー、小計の下、保険業 """
    other_net_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='その他、営業活動によるキャッシュ・フロー')
    """ その他、営業活動によるキャッシュ・フロー """
    other_net_ope_cf_subtotal: Optional[IxNonFractionPublic] = Field(default=None, description='その他、営業活動によるキャッシュ・フロー、小計の下')
    """ その他、営業活動によるキャッシュ・フロー、小計の下 """
    other_net_ppe: Optional[IxNonFractionPublic] = Field(default=None, description='その他（純額）、有形固定資産')
    """ その他（純額）、有形固定資産 """
    other_non_operating_expenses_income_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='その他の営業外損益（△は益）、営業活動によるキャッシュ・フロー')
    """ その他の営業外損益（△は益）、営業活動によるキャッシュ・フロー """
    other_operating_assets_calea: Optional[IxNonFractionPublic] = Field(default=None, description='その他の営業資産、流動資産、リース事業')
    """ その他の営業資産、流動資産、リース事業 """
    other_operating_expenses_oeins: Optional[IxNonFractionPublic] = Field(default=None, description='その他経常費用、経常費用、保険業')
    """ その他経常費用、経常費用、保険業 """
    other_operating_expenses_spf: Optional[IxNonFractionPublic] = Field(default=None, description='その他の営業費用、特定金融業')
    """ その他の営業費用、特定金融業 """
    other_operating_income_oiins: Optional[IxNonFractionPublic] = Field(default=None, description='その他経常収益、経常収益、保険業')
    """ その他経常収益、経常収益、保険業 """
    other_operating_revenue1_rev_oa: Optional[IxNonFractionPublic] = Field(default=None, description='その他の営業収益、営業活動による収益')
    """ その他の営業収益、営業活動による収益 """
    other_operating_revenue_cmd: Optional[IxNonFractionPublic] = Field(default=None, description='その他、営業収益、商品先物取引業')
    """ その他、営業収益、商品先物取引業 """
    other_ordinary_expenses_oebnk: Optional[IxNonFractionPublic] = Field(default=None, description='その他業務費用、経常費用、銀行業')
    """ その他業務費用、経常費用、銀行業 """
    other_ordinary_income_oibnk: Optional[IxNonFractionPublic] = Field(default=None, description='その他業務収益、経常収益、銀行業')
    """ その他業務収益、経常収益、銀行業 """
    other_other_assets_assets_bnk: Optional[IxNonFractionPublic] = Field(default=None, description='その他の資産、その他資産、資産の部、銀行業')
    """ その他の資産、その他資産、資産の部、銀行業 """
    other_other_liabilities_liabilities_bnk: Optional[IxNonFractionPublic] = Field(default=None, description='その他の負債、その他負債、負債の部、銀行業')
    """ その他の負債、その他負債、負債の部、銀行業 """
    other_ppe: Optional[IxNonFractionPublic] = Field(default=None, description='その他、有形固定資産')
    """ その他、有形固定資産 """
    other_payments_fin_cf: Optional[IxNonFractionPublic] = Field(default=None, description='その他の支出、財務活動によるキャッシュ・フロー')
    """ その他の支出、財務活動によるキャッシュ・フロー """
    other_payments_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='その他の支出、投資活動によるキャッシュ・フロー')
    """ その他の支出、投資活動によるキャッシュ・フロー """
    other_payments_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='その他の支出、営業活動によるキャッシュ・フロー')
    """ その他の支出、営業活動によるキャッシュ・フロー """
    other_personal_expenses_sga: Optional[IxNonFractionPublic] = Field(default=None, description='その他の人件費、販売費及び一般管理費')
    """ その他の人件費、販売費及び一般管理費 """
    other_proceeds_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='その他の収入、投資活動によるキャッシュ・フロー')
    """ その他の収入、投資活動によるキャッシュ・フロー """
    other_proceeds_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='その他の収入、営業活動によるキャッシュ・フロー')
    """ その他の収入、営業活動によるキャッシュ・フロー """
    other_provision_cl: Optional[IxNonFractionPublic] = Field(default=None, description='その他の引当金、流動負債')
    """ その他の引当金、流動負債 """
    other_provision_ncl: Optional[IxNonFractionPublic] = Field(default=None, description='その他の引当金、固定負債')
    """ その他の引当金、固定負債 """
    other_retained_earnings: Optional[IxNonFractionPublic] = Field(default=None, description='その他利益剰余金')
    """ その他利益剰余金 """
    other_rev_oa: Optional[IxNonFractionPublic] = Field(default=None, description='その他、営業活動による収益')
    """ その他、営業活動による収益 """
    other_revenue1_rev_oa: Optional[IxNonFractionPublic] = Field(default=None, description='その他の収益、営業活動による収益')
    """ その他の収益、営業活動による収益 """
    other_revenue2_rev_oa: Optional[IxNonFractionPublic] = Field(default=None, description='その他の収入、営業活動による収益')
    """ その他の収入、営業活動による収益 """
    other_sga: Optional[IxNonFractionPublic] = Field(default=None, description='その他、販売費及び一般管理費')
    """ その他、販売費及び一般管理費 """
    other_selling_expenses_sga: Optional[IxNonFractionPublic] = Field(default=None, description='その他の販売費、販売費及び一般管理費')
    """ その他の販売費、販売費及び一般管理費 """
    outstanding_claims_liabilities_ins: Optional[IxNonFractionPublic] = Field(default=None, description='支払備金、負債の部、保険業')
    """ 支払備金、負債の部、保険業 """
    own_used_assets_ppelea: Optional[IxNonFractionPublic] = Field(default=None, description='社用資産、有形固定資産、リース事業')
    """ 社用資産、有形固定資産、リース事業 """
    packing_and_transportation_expenses_sga: Optional[IxNonFractionPublic] = Field(default=None, description='荷造運搬費、販売費及び一般管理費')
    """ 荷造運搬費、販売費及び一般管理費 """
    patent_right: Optional[IxNonFractionPublic] = Field(default=None, description='特許権')
    """ 特許権 """
    payables_under_fluidity_lease_receivables_cllea: Optional[IxNonFractionPublic] = Field(default=None, description='債権流動化に伴う支払債務、流動負債、リース事業')
    """ 債権流動化に伴う支払債務、流動負債、リース事業 """
    payables_under_repurchase_agreements_liabilities_bnk: Optional[IxNonFractionPublic] = Field(default=None, description='売現先勘定、負債の部、銀行業')
    """ 売現先勘定、負債の部、銀行業 """
    payables_under_securities_lending_transactions_liabilities_bnk: Optional[IxNonFractionPublic] = Field(default=None, description='債券貸借取引受入担保金、負債の部、銀行業')
    """ 債券貸借取引受入担保金、負債の部、銀行業 """
    payments_associated_with_disaster_loss2_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='災害による損失の支払額、営業活動によるキャッシュ・フロー')
    """ 災害による損失の支払額、営業活動によるキャッシュ・フロー """
    payments_for_asset_retirement_obligations_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='資産除去債務の履行による支出、投資活動によるキャッシュ・フロー')
    """ 資産除去債務の履行による支出、投資活動によるキャッシュ・フロー """
    payments_for_business_restructuring_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='事業再編による支出、営業活動によるキャッシュ・フロー')
    """ 事業再編による支出、営業活動によるキャッシュ・フロー """
    payments_for_directors_retirement_benefits_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='役員退職慰労金の支払額、営業活動によるキャッシュ・フロー')
    """ 役員退職慰労金の支払額、営業活動によるキャッシュ・フロー """
    payments_for_extra_retirement_payments_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='特別退職金の支払額、営業活動によるキャッシュ・フロー')
    """ 特別退職金の支払額、営業活動によるキャッシュ・フロー """
    payments_for_finance_ope_cfbnk: Optional[IxNonFractionPublic] = Field(default=None, description='資金調達による支出、営業活動によるキャッシュ・フロー、銀行業')
    """ 資金調達による支出、営業活動によるキャッシュ・フロー、銀行業 """
    payments_for_guarantee_deposits_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='差入保証金の差入による支出、投資活動によるキャッシュ・フロー')
    """ 差入保証金の差入による支出、投資活動によるキャッシュ・フロー """
    payments_for_investments_in_capital_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='出資金の払込による支出、投資活動によるキャッシュ・フロー')
    """ 出資金の払込による支出、投資活動によるキャッシュ・フロー """
    payments_for_investments_in_real_estates_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='投資不動産の取得による支出、投資活動によるキャッシュ・フロー')
    """ 投資不動産の取得による支出、投資活動によるキャッシュ・フロー """
    payments_for_issuance_of_common_stock_fin_cf: Optional[IxNonFractionPublic] = Field(default=None, description='株式の発行による支出、財務活動によるキャッシュ・フロー')
    """ 株式の発行による支出、財務活動によるキャッシュ・フロー """
    payments_for_lease_and_guarantee_deposits_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='敷金及び保証金の差入による支出、投資活動によるキャッシュ・フロー')
    """ 敷金及び保証金の差入による支出、投資活動によるキャッシュ・フロー """
    payments_for_lease_deposits_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='敷金の差入による支出、投資活動によるキャッシュ・フロー')
    """ 敷金の差入による支出、投資活動によるキャッシュ・フロー """
    payments_for_long_term_accounts_payable_other_fin_cf: Optional[IxNonFractionPublic] = Field(default=None, description='長期未払金の返済による支出、財務活動によるキャッシュ・フロー')
    """ 長期未払金の返済による支出、財務活動によるキャッシュ・フロー """
    payments_for_other_operating_activity_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='その他の営業支出、営業活動によるキャッシュ・フロー')
    """ その他の営業支出、営業活動によるキャッシュ・フロー """
    payments_for_payroll_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='人件費の支出、営業活動によるキャッシュ・フロー')
    """ 人件費の支出、営業活動によるキャッシュ・フロー """
    payments_for_raw_materials_and_goods_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='原材料又は商品の仕入れによる支出、営業活動によるキャッシュ・フロー')
    """ 原材料又は商品の仕入れによる支出、営業活動によるキャッシュ・フロー """
    payments_for_removal_expenses_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='移転費用の支払額、営業活動によるキャッシュ・フロー')
    """ 移転費用の支払額、営業活動によるキャッシュ・フロー """
    payments_for_retirement_of_noncurrent_assets_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='固定資産の除却による支出、投資活動によるキャッシュ・フロー')
    """ 固定資産の除却による支出、投資活動によるキャッシュ・フロー """
    payments_for_retirement_of_property_plant_and_equipment_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='有形固定資産の除却による支出、投資活動によるキャッシュ・フロー')
    """ 有形固定資産の除却による支出、投資活動によるキャッシュ・フロー """
    payments_for_sales_of_investments_in_subsidiaries_resulting_in_change_in_scope_of_consolidation_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='連結の範囲の変更を伴う子会社株式の売却による支出、投資活動によるキャッシュ・フロー')
    """ 連結の範囲の変更を伴う子会社株式の売却による支出、投資活動によるキャッシュ・フロー """
    payments_for_sales_of_notes_receivable_trade_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='手形売却に伴う支払額、営業活動によるキャッシュ・フロー')
    """ 手形売却に伴う支払額、営業活動によるキャッシュ・フロー """
    payments_for_transfer_of_business2_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='事業譲受による支出、投資活動によるキャッシュ・フロー')
    """ 事業譲受による支出、投資活動によるキャッシュ・フロー """
    payments_from_changes_in_ownership_interests_in_subsidiaries_that_do_not_result_in_change_in_scope_of_consolidation_fin_cf: Optional[IxNonFractionPublic] = Field(default=None, description='連結の範囲の変更を伴わない子会社株式の取得による支出、財務活動によるキャッシュ・フロー')
    """ 連結の範囲の変更を伴わない子会社株式の取得による支出、財務活動によるキャッシュ・フロー """
    payments_into_time_deposits_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='定期預金の預入による支出、投資活動によるキャッシュ・フロー')
    """ 定期預金の預入による支出、投資活動によるキャッシュ・フロー """
    payments_of_investment_and_loans_receivable_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='投融資による支出、投資活動によるキャッシュ・フロー')
    """ 投融資による支出、投資活動によるキャッシュ・フロー """
    payments_of_listing_expenses_fin_cf: Optional[IxNonFractionPublic] = Field(default=None, description='上場関連費用の支出、財務活動によるキャッシュ・フロー')
    """ 上場関連費用の支出、財務活動によるキャッシュ・フロー """
    payments_of_loans_receivable_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='貸付けによる支出、投資活動によるキャッシュ・フロー')
    """ 貸付けによる支出、投資活動によるキャッシュ・フロー """
    payments_of_loans_receivable_to_employees_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='従業員に対する貸付けによる支出、投資活動によるキャッシュ・フロー')
    """ 従業員に対する貸付けによる支出、投資活動によるキャッシュ・フロー """
    payments_of_long_term_loans_receivable_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='長期貸付けによる支出、投資活動によるキャッシュ・フロー')
    """ 長期貸付けによる支出、投資活動によるキャッシュ・フロー """
    payments_of_short_term_loans_receivable_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='短期貸付けによる支出、投資活動によるキャッシュ・フロー')
    """ 短期貸付けによる支出、投資活動によるキャッシュ・フロー """
    penalty_income_ei: Optional[IxNonFractionPublic] = Field(default=None, description='違約金収入、特別利益')
    """ 違約金収入、特別利益 """
    penalty_income_noi: Optional[IxNonFractionPublic] = Field(default=None, description='違約金収入、営業外収益')
    """ 違約金収入、営業外収益 """
    per_item_revenue_rev_oa: Optional[IxNonFractionPublic] = Field(default=None, description='個別信用購入あっせん収益、営業活動による収益')
    """ 個別信用購入あっせん収益、営業活動による収益 """
    personal_expenses_sga: Optional[IxNonFractionPublic] = Field(default=None, description='人件費、販売費及び一般管理費')
    """ 人件費、販売費及び一般管理費 """
    policy_reserve_liabilities_ins: Optional[IxNonFractionPublic] = Field(default=None, description='責任準備金、負債の部、保険業')
    """ 責任準備金、負債の部、保険業 """
    power_utilities_expenses_sga: Optional[IxNonFractionPublic] = Field(default=None, description='動力用水光熱費、販売費及び一般管理費')
    """ 動力用水光熱費、販売費及び一般管理費 """
    prepaid_expenses: Optional[IxNonFractionPublic] = Field(default=None, description='前払費用')
    """ 前払費用 """
    prepaid_pension_cost_assets: Optional[IxNonFractionPublic] = Field(default=None, description='前払年金費用、資産の部')
    """ 前払年金費用、資産の部 """
    prepaid_pension_cost_ioa: Optional[IxNonFractionPublic] = Field(default=None, description='前払年金費用、投資その他の資産')
    """ 前払年金費用、投資その他の資産 """
    proceeds_from_cancellation_of_insurance_funds_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='保険積立金の解約による収入、投資活動によるキャッシュ・フロー')
    """ 保険積立金の解約による収入、投資活動によるキャッシュ・フロー """
    proceeds_from_changes_in_ownership_interests_in_subsidiaries_that_do_not_result_in_change_in_scope_of_consolidation_fin_cf: Optional[IxNonFractionPublic] = Field(default=None, description='連結の範囲の変更を伴わない子会社株式の売却による収入、財務活動によるキャッシュ・フロー')
    """ 連結の範囲の変更を伴わない子会社株式の売却による収入、財務活動によるキャッシュ・フロー """
    proceeds_from_collection_of_guarantee_deposits_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='差入保証金の回収による収入、投資活動によるキャッシュ・フロー')
    """ 差入保証金の回収による収入、投資活動によるキャッシュ・フロー """
    proceeds_from_collection_of_lease_and_guarantee_deposits_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='敷金及び保証金の回収による収入、投資活動によるキャッシュ・フロー')
    """ 敷金及び保証金の回収による収入、投資活動によるキャッシュ・フロー """
    proceeds_from_compensation_for_expropriation_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='収用補償金の受取額、営業活動によるキャッシュ・フロー')
    """ 収用補償金の受取額、営業活動によるキャッシュ・フロー """
    proceeds_from_compensation_for_removal_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='移転補償金の受取額、営業活動によるキャッシュ・フロー')
    """ 移転補償金の受取額、営業活動によるキャッシュ・フロー """
    proceeds_from_compensation_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='補償金の受取額、営業活動によるキャッシュ・フロー')
    """ 補償金の受取額、営業活動によるキャッシュ・フロー """
    proceeds_from_contribution_for_construction_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='工事負担金等受入額、営業活動によるキャッシュ・フロー')
    """ 工事負担金等受入額、営業活動によるキャッシュ・フロー """
    proceeds_from_contribution_received_for_construction_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='工事負担金等受入による収入、投資活動によるキャッシュ・フロー')
    """ 工事負担金等受入による収入、投資活動によるキャッシュ・フロー """
    proceeds_from_disposal_of_treasury_stock_fin_cf: Optional[IxNonFractionPublic] = Field(default=None, description='自己株式の処分による収入、財務活動によるキャッシュ・フロー')
    """ 自己株式の処分による収入、財務活動によるキャッシュ・フロー """
    proceeds_from_distribution_of_investment_in_partnerships_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='投資事業組合からの分配による収入、投資活動によるキャッシュ・フロー')
    """ 投資事業組合からの分配による収入、投資活動によるキャッシュ・フロー """
    proceeds_from_dividends_income_from_equity_method_affiliate_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='持分法適用会社からの配当金の受取額、営業活動によるキャッシュ・フロー')
    """ 持分法適用会社からの配当金の受取額、営業活動によるキャッシュ・フロー """
    proceeds_from_exercise_of_stock_option_fin_cf: Optional[IxNonFractionPublic] = Field(default=None, description='ストックオプションの行使による収入、財務活動によるキャッシュ・フロー')
    """ ストックオプションの行使による収入、財務活動によるキャッシュ・フロー """
    proceeds_from_fund_management_ope_cfbnk: Optional[IxNonFractionPublic] = Field(default=None, description='資金運用による収入、営業活動によるキャッシュ・フロー、銀行業')
    """ 資金運用による収入、営業活動によるキャッシュ・フロー、銀行業 """
    proceeds_from_guarantee_deposits_received_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='預り保証金の受入による収入、投資活動によるキャッシュ・フロー')
    """ 預り保証金の受入による収入、投資活動によるキャッシュ・フロー """
    proceeds_from_insurance_income_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='保険金の受取額、営業活動によるキャッシュ・フロー')
    """ 保険金の受取額、営業活動によるキャッシュ・フロー """
    proceeds_from_issuance_of_bonds_fin_cf: Optional[IxNonFractionPublic] = Field(default=None, description='社債の発行による収入、財務活動によるキャッシュ・フロー')
    """ 社債の発行による収入、財務活動によるキャッシュ・フロー """
    proceeds_from_issuance_of_commercial_papers_fin_cf: Optional[IxNonFractionPublic] = Field(default=None, description='コマーシャル・ペーパーの発行による収入、財務活動によるキャッシュ・フロー')
    """ コマーシャル・ペーパーの発行による収入、財務活動によるキャッシュ・フロー """
    proceeds_from_issuance_of_common_stock_fin_cf: Optional[IxNonFractionPublic] = Field(default=None, description='株式の発行による収入、財務活動によるキャッシュ・フロー')
    """ 株式の発行による収入、財務活動によるキャッシュ・フロー """
    proceeds_from_issuance_of_stock_resulting_from_exercise_of_subscription_rights_to_shares_fin_cf: Optional[IxNonFractionPublic] = Field(default=None, description='新株予約権の行使による株式の発行による収入、財務活動によるキャッシュ・フロー')
    """ 新株予約権の行使による株式の発行による収入、財務活動によるキャッシュ・フロー """
    proceeds_from_issuance_of_subscription_rights_to_shares_fin_cf: Optional[IxNonFractionPublic] = Field(default=None, description='新株予約権の発行による収入、財務活動によるキャッシュ・フロー')
    """ 新株予約権の発行による収入、財務活動によるキャッシュ・フロー """
    proceeds_from_liquidation_of_subsidiaries_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='子会社の清算による収入、投資活動によるキャッシュ・フロー')
    """ 子会社の清算による収入、投資活動によるキャッシュ・フロー """
    proceeds_from_long_term_loans_payable_fin_cf: Optional[IxNonFractionPublic] = Field(default=None, description='長期借入れによる収入、財務活動によるキャッシュ・フロー')
    """ 長期借入れによる収入、財務活動によるキャッシュ・フロー """
    proceeds_from_maturity_of_insurance_funds_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='保険積立金の払戻による収入、投資活動によるキャッシュ・フロー')
    """ 保険積立金の払戻による収入、投資活動によるキャッシュ・フロー """
    proceeds_from_purchase_of_investments_in_subsidiaries_resulting_in_change_in_scope_of_consolidation_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='連結の範囲の変更を伴う子会社株式の取得による収入、投資活動によるキャッシュ・フロー')
    """ 連結の範囲の変更を伴う子会社株式の取得による収入、投資活動によるキャッシュ・フロー """
    proceeds_from_redemption_of_investment_securities_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='投資有価証券の償還による収入、投資活動によるキャッシュ・フロー')
    """ 投資有価証券の償還による収入、投資活動によるキャッシュ・フロー """
    proceeds_from_redemption_of_securities_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='有価証券の償還による収入、投資活動によるキャッシュ・フロー')
    """ 有価証券の償還による収入、投資活動によるキャッシュ・フロー """
    proceeds_from_redemption_of_securities_inv_cfbnk: Optional[IxNonFractionPublic] = Field(default=None, description='有価証券の償還による収入、投資活動によるキャッシュ・フロー、銀行業')
    """ 有価証券の償還による収入、投資活動によるキャッシュ・フロー、銀行業 """
    proceeds_from_rent_income_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='賃貸料の受取額、営業活動によるキャッシュ・フロー')
    """ 賃貸料の受取額、営業活動によるキャッシュ・フロー """
    proceeds_from_rental_of_real_estate_for_investment_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='投資不動産の賃貸による収入、投資活動によるキャッシュ・フロー')
    """ 投資不動産の賃貸による収入、投資活動によるキャッシュ・フロー """
    proceeds_from_sale_and_leaseback_fin_cf: Optional[IxNonFractionPublic] = Field(default=None, description='セール・アンド・リースバックによる収入、財務活動によるキャッシュ・フロー')
    """ セール・アンド・リースバックによる収入、財務活動によるキャッシュ・フロー """
    proceeds_from_sales_and_redemption_of_investment_securities_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='投資有価証券の売却及び償還による収入、投資活動によるキャッシュ・フロー')
    """ 投資有価証券の売却及び償還による収入、投資活動によるキャッシュ・フロー """
    proceeds_from_sales_and_redemption_of_securities_inv_cfins: Optional[IxNonFractionPublic] = Field(default=None, description='有価証券の売却・償還による収入、投資活動によるキャッシュ・フロー、保険業')
    """ 有価証券の売却・償還による収入、投資活動によるキャッシュ・フロー、保険業 """
    proceeds_from_sales_and_redemption_of_short_term_and_long_term_investment_securities_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='有価証券及び投資有価証券の売却及び償還による収入、投資活動によるキャッシュ・フロー')
    """ 有価証券及び投資有価証券の売却及び償還による収入、投資活動によるキャッシュ・フロー """
    proceeds_from_sales_of_golf_club_memberships_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='ゴルフ会員権の売却による収入、投資活動によるキャッシュ・フロー')
    """ ゴルフ会員権の売却による収入、投資活動によるキャッシュ・フロー """
    proceeds_from_sales_of_intangible_assets_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='無形固定資産の売却による収入、投資活動によるキャッシュ・フロー')
    """ 無形固定資産の売却による収入、投資活動によるキャッシュ・フロー """
    proceeds_from_sales_of_investment_securities_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='投資有価証券の売却による収入、投資活動によるキャッシュ・フロー')
    """ 投資有価証券の売却による収入、投資活動によるキャッシュ・フロー """
    proceeds_from_sales_of_investments_in_real_estates_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='投資不動産の売却による収入、投資活動によるキャッシュ・フロー')
    """ 投資不動産の売却による収入、投資活動によるキャッシュ・フロー """
    proceeds_from_sales_of_investments_in_subsidiaries_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='子会社株式の売却による収入、投資活動によるキャッシュ・フロー')
    """ 子会社株式の売却による収入、投資活動によるキャッシュ・フロー """
    proceeds_from_sales_of_investments_in_subsidiaries_resulting_in_change_in_scope_of_consolidation_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='連結の範囲の変更を伴う子会社株式の売却による収入、投資活動によるキャッシュ・フロー')
    """ 連結の範囲の変更を伴う子会社株式の売却による収入、投資活動によるキャッシュ・フロー """
    proceeds_from_sales_of_noncurrent_assets_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='固定資産の売却による収入、投資活動によるキャッシュ・フロー')
    """ 固定資産の売却による収入、投資活動によるキャッシュ・フロー """
    proceeds_from_sales_of_property_plant_and_equipment_and_intangible_assets_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='有形及び無形固定資産の売却による収入、投資活動によるキャッシュ・フロー')
    """ 有形及び無形固定資産の売却による収入、投資活動によるキャッシュ・フロー """
    proceeds_from_sales_of_property_plant_and_equipment_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='有形固定資産の売却による収入、投資活動によるキャッシュ・フロー')
    """ 有形固定資産の売却による収入、投資活動によるキャッシュ・フロー """
    proceeds_from_sales_of_securities_inv_cfbnk: Optional[IxNonFractionPublic] = Field(default=None, description='有価証券の売却による収入、投資活動によるキャッシュ・フロー、銀行業')
    """ 有価証券の売却による収入、投資活動によるキャッシュ・フロー、銀行業 """
    proceeds_from_sales_of_short_term_investment_securities_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='有価証券の売却による収入、投資活動によるキャッシュ・フロー')
    """ 有価証券の売却による収入、投資活動によるキャッシュ・フロー """
    proceeds_from_sales_of_stocks_of_subsidiaries_and_affiliates_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='関係会社株式の売却による収入、投資活動によるキャッシュ・フロー')
    """ 関係会社株式の売却による収入、投資活動によるキャッシュ・フロー """
    proceeds_from_sales_of_treasury_stock_fin_cf: Optional[IxNonFractionPublic] = Field(default=None, description='自己株式の売却による収入、財務活動によるキャッシュ・フロー')
    """ 自己株式の売却による収入、財務活動によるキャッシュ・フロー """
    proceeds_from_sales_of_trust_beneficiary_right_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='信託受益権の売却による収入、投資活動によるキャッシュ・フロー')
    """ 信託受益権の売却による収入、投資活動によるキャッシュ・フロー """
    proceeds_from_share_issuance_to_non_controlling_shareholders_fin_cf: Optional[IxNonFractionPublic] = Field(default=None, description='非支配株主からの払込みによる収入、財務活動によるキャッシュ・フロー')
    """ 非支配株主からの払込みによる収入、財務活動によるキャッシュ・フロー """
    proceeds_from_share_of_profits_on_investments_in_capital_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='出資金の分配による収入、投資活動によるキャッシュ・フロー')
    """ 出資金の分配による収入、投資活動によるキャッシュ・フロー """
    proceeds_from_subsidies_for_employment_adjustment_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='雇用調整助成金の受取額、営業活動によるキャッシュ・フロー')
    """ 雇用調整助成金の受取額、営業活動によるキャッシュ・フロー """
    proceeds_from_subsidy_income2_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='助成金の受取額、営業活動によるキャッシュ・フロー')
    """ 助成金の受取額、営業活動によるキャッシュ・フロー """
    proceeds_from_subsidy_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='補助金の受取額、営業活動によるキャッシュ・フロー')
    """ 補助金の受取額、営業活動によるキャッシュ・フロー """
    proceeds_from_transfer_of_business_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='事業譲渡による収入、投資活動によるキャッシュ・フロー')
    """ 事業譲渡による収入、投資活動によるキャッシュ・フロー """
    proceeds_from_withdrawal_of_investments_in_silent_partnership_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='匿名組合出資金の払戻による収入、投資活動によるキャッシュ・フロー')
    """ 匿名組合出資金の払戻による収入、投資活動によるキャッシュ・フロー """
    proceeds_from_withdrawal_of_time_deposits_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='定期預金の払戻による収入、投資活動によるキャッシュ・フロー')
    """ 定期預金の払戻による収入、投資活動によるキャッシュ・フロー """
    production_facilities_ppegas: Optional[IxNonFractionPublic] = Field(default=None, description='製造設備、有形固定資産、ガス事業')
    """ 製造設備、有形固定資産、ガス事業 """
    profit_loss: Optional[IxNonFractionPublic] = Field(default=None, description='当期純利益又は当期純損失（△）（平成26年3月28日財規等改正後）')
    """ 当期純利益又は当期純損失（△）（平成26年3月28日財規等改正後） """
    profit_loss_attributable_to_non_controlling_interests: Optional[IxNonFractionPublic] = Field(default=None, description='非支配株主に帰属する当期純利益又は非支配株主に帰属する当期純損失（△）')
    """ 非支配株主に帰属する当期純利益又は非支配株主に帰属する当期純損失（△） """
    profit_loss_attributable_to_owners_of_parent: Optional[IxNonFractionPublic] = Field(default=None, description='親会社株主に帰属する当期純利益又は親会社株主に帰属する当期純損失（△）')
    """ 親会社株主に帰属する当期純利益又は親会社株主に帰属する当期純損失（△） """
    promotion_expenses_sga: Optional[IxNonFractionPublic] = Field(default=None, description='販売促進費、販売費及び一般管理費')
    """ 販売促進費、販売費及び一般管理費 """
    property_for_lease_ppelea: Optional[IxNonFractionPublic] = Field(default=None, description='賃貸資産、有形固定資産、リース事業')
    """ 賃貸資産、有形固定資産、リース事業 """
    property_plant_and_equipment: Optional[IxNonFractionPublic] = Field(default=None, description='有形固定資産')
    """ 有形固定資産 """
    provision_cl: Optional[IxNonFractionPublic] = Field(default=None, description='引当金、流動負債')
    """ 引当金、流動負債 """
    provision_for_bonuses: Optional[IxNonFractionPublic] = Field(default=None, description='賞与引当金')
    """ 賞与引当金 """
    provision_for_bonuses_sga: Optional[IxNonFractionPublic] = Field(default=None, description='賞与引当金繰入額、販売費及び一般管理費')
    """ 賞与引当金繰入額、販売費及び一般管理費 """
    provision_for_business_structure_improvement_cl: Optional[IxNonFractionPublic] = Field(default=None, description='事業構造改善引当金、流動負債')
    """ 事業構造改善引当金、流動負債 """
    provision_for_business_structure_improvement_el: Optional[IxNonFractionPublic] = Field(default=None, description='事業構造改善引当金繰入額、特別損失')
    """ 事業構造改善引当金繰入額、特別損失 """
    provision_for_business_structure_improvement_ncl: Optional[IxNonFractionPublic] = Field(default=None, description='事業構造改善引当金、固定負債')
    """ 事業構造改善引当金、固定負債 """
    provision_for_contingent_loss_cl: Optional[IxNonFractionPublic] = Field(default=None, description='偶発損失引当金、流動負債')
    """ 偶発損失引当金、流動負債 """
    provision_for_contingent_loss_el: Optional[IxNonFractionPublic] = Field(default=None, description='偶発損失引当金繰入額、特別損失')
    """ 偶発損失引当金繰入額、特別損失 """
    provision_for_contingent_loss_liabilities_bnk: Optional[IxNonFractionPublic] = Field(default=None, description='偶発損失引当金、負債の部、銀行業')
    """ 偶発損失引当金、負債の部、銀行業 """
    provision_for_contingent_loss_ncl: Optional[IxNonFractionPublic] = Field(default=None, description='偶発損失引当金、固定負債')
    """ 偶発損失引当金、固定負債 """
    provision_for_directors_bonuses: Optional[IxNonFractionPublic] = Field(default=None, description='役員賞与引当金')
    """ 役員賞与引当金 """
    provision_for_directors_bonuses_sga: Optional[IxNonFractionPublic] = Field(default=None, description='役員賞与引当金繰入額、販売費及び一般管理費')
    """ 役員賞与引当金繰入額、販売費及び一般管理費 """
    provision_for_directors_retirement_benefits: Optional[IxNonFractionPublic] = Field(default=None, description='役員退職慰労引当金')
    """ 役員退職慰労引当金 """
    provision_for_directors_retirement_benefits_el: Optional[IxNonFractionPublic] = Field(default=None, description='役員退職慰労引当金繰入額、特別損失')
    """ 役員退職慰労引当金繰入額、特別損失 """
    provision_for_directors_retirement_benefits_sga: Optional[IxNonFractionPublic] = Field(default=None, description='役員退職慰労引当金繰入額、販売費及び一般管理費')
    """ 役員退職慰労引当金繰入額、販売費及び一般管理費 """
    provision_for_environmental_measures_cl: Optional[IxNonFractionPublic] = Field(default=None, description='環境対策引当金、流動負債')
    """ 環境対策引当金、流動負債 """
    provision_for_environmental_measures_ncl: Optional[IxNonFractionPublic] = Field(default=None, description='環境対策引当金、固定負債')
    """ 環境対策引当金、固定負債 """
    provision_for_gas_holder_repairs_gas: Optional[IxNonFractionPublic] = Field(default=None, description='ガスホルダー修繕引当金、ガス事業')
    """ ガスホルダー修繕引当金、ガス事業 """
    provision_for_loss_on_business_liquidation_el: Optional[IxNonFractionPublic] = Field(default=None, description='事業整理損失引当金繰入額、特別損失')
    """ 事業整理損失引当金繰入額、特別損失 """
    provision_for_loss_on_business_of_subsidiaries_and_affiliates_el: Optional[IxNonFractionPublic] = Field(default=None, description='関係会社事業損失引当金繰入額、特別損失')
    """ 関係会社事業損失引当金繰入額、特別損失 """
    provision_for_loss_on_business_of_subsidiaries_and_affiliates_ncl: Optional[IxNonFractionPublic] = Field(default=None, description='関係会社事業損失引当金、固定負債')
    """ 関係会社事業損失引当金、固定負債 """
    provision_for_loss_on_construction_contracts: Optional[IxNonFractionPublic] = Field(default=None, description='工事損失引当金')
    """ 工事損失引当金 """
    provision_for_loss_on_disaster_cl: Optional[IxNonFractionPublic] = Field(default=None, description='災害損失引当金、流動負債')
    """ 災害損失引当金、流動負債 """
    provision_for_loss_on_disaster_el: Optional[IxNonFractionPublic] = Field(default=None, description='災害損失引当金繰入額、特別損失')
    """ 災害損失引当金繰入額、特別損失 """
    provision_for_loss_on_guarantees: Optional[IxNonFractionPublic] = Field(default=None, description='債務保証損失引当金')
    """ 債務保証損失引当金 """
    provision_for_loss_on_guarantees_cl: Optional[IxNonFractionPublic] = Field(default=None, description='債務保証損失引当金、流動負債')
    """ 債務保証損失引当金、流動負債 """
    provision_for_loss_on_guarantees_el: Optional[IxNonFractionPublic] = Field(default=None, description='債務保証損失引当金繰入額、特別損失')
    """ 債務保証損失引当金繰入額、特別損失 """
    provision_for_loss_on_interest_repayment_liabilities_bnk: Optional[IxNonFractionPublic] = Field(default=None, description='利息返還損失引当金、負債の部、銀行業')
    """ 利息返還損失引当金、負債の部、銀行業 """
    provision_for_loss_on_interest_repayment_ncl: Optional[IxNonFractionPublic] = Field(default=None, description='利息返還損失引当金、固定負債')
    """ 利息返還損失引当金、固定負債 """
    provision_for_loss_on_liquidation_of_subsidiaries_and_affiliates_cl: Optional[IxNonFractionPublic] = Field(default=None, description='関係会社整理損失引当金、流動負債')
    """ 関係会社整理損失引当金、流動負債 """
    provision_for_loss_on_liquidation_of_subsidiaries_and_affiliates_ncl: Optional[IxNonFractionPublic] = Field(default=None, description='関係会社整理損失引当金、固定負債')
    """ 関係会社整理損失引当金、固定負債 """
    provision_for_loss_on_litigation_cl: Optional[IxNonFractionPublic] = Field(default=None, description='訴訟損失引当金、流動負債')
    """ 訴訟損失引当金、流動負債 """
    provision_for_loss_on_litigation_el: Optional[IxNonFractionPublic] = Field(default=None, description='訴訟損失引当金繰入額、特別損失')
    """ 訴訟損失引当金繰入額、特別損失 """
    provision_for_loss_on_litigation_ncl: Optional[IxNonFractionPublic] = Field(default=None, description='訴訟損失引当金、固定負債')
    """ 訴訟損失引当金、固定負債 """
    provision_for_loss_on_order_received_cl: Optional[IxNonFractionPublic] = Field(default=None, description='受注損失引当金、流動負債')
    """ 受注損失引当金、流動負債 """
    provision_for_loss_on_store_closing: Optional[IxNonFractionPublic] = Field(default=None, description='店舗閉鎖損失引当金')
    """ 店舗閉鎖損失引当金 """
    provision_for_loss_on_store_closing_el: Optional[IxNonFractionPublic] = Field(default=None, description='店舗閉鎖損失引当金繰入額、特別損失')
    """ 店舗閉鎖損失引当金繰入額、特別損失 """
    provision_for_point_card_certificates_cl: Optional[IxNonFractionPublic] = Field(default=None, description='ポイント引当金、流動負債')
    """ ポイント引当金、流動負債 """
    provision_for_point_card_certificates_ncl: Optional[IxNonFractionPublic] = Field(default=None, description='ポイント引当金、固定負債')
    """ ポイント引当金、固定負債 """
    provision_for_product_warranties: Optional[IxNonFractionPublic] = Field(default=None, description='製品保証引当金')
    """ 製品保証引当金 """
    provision_for_product_warranties_ncl: Optional[IxNonFractionPublic] = Field(default=None, description='製品保証引当金、固定負債')
    """ 製品保証引当金、固定負債 """
    provision_for_product_warranties_sga: Optional[IxNonFractionPublic] = Field(default=None, description='製品保証引当金繰入額、販売費及び一般管理費')
    """ 製品保証引当金繰入額、販売費及び一般管理費 """
    provision_for_reimbursement_of_deposits_liabilities_bnk: Optional[IxNonFractionPublic] = Field(default=None, description='睡眠預金払戻損失引当金、負債の部、銀行業')
    """ 睡眠預金払戻損失引当金、負債の部、銀行業 """
    provision_for_repairs_ncl: Optional[IxNonFractionPublic] = Field(default=None, description='修繕引当金、固定負債')
    """ 修繕引当金、固定負債 """
    provision_for_retirement_benefits: Optional[IxNonFractionPublic] = Field(default=None, description='退職給付引当金')
    """ 退職給付引当金 """
    provision_for_retirement_benefits_sga: Optional[IxNonFractionPublic] = Field(default=None, description='退職給付引当金繰入額、販売費及び一般管理費')
    """ 退職給付引当金繰入額、販売費及び一般管理費 """
    provision_for_safety_measures_gas: Optional[IxNonFractionPublic] = Field(default=None, description='保安対策引当金、ガス事業')
    """ 保安対策引当金、ガス事業 """
    provision_for_sales_promotion_expenses: Optional[IxNonFractionPublic] = Field(default=None, description='販売促進引当金')
    """ 販売促進引当金 """
    provision_for_share_based_payments_cl: Optional[IxNonFractionPublic] = Field(default=None, description='株式報酬引当金、流動負債')
    """ 株式報酬引当金、流動負債 """
    provision_for_share_based_payments_ncl: Optional[IxNonFractionPublic] = Field(default=None, description='株式報酬引当金、固定負債')
    """ 株式報酬引当金、固定負債 """
    provision_for_share_based_payments_sga: Optional[IxNonFractionPublic] = Field(default=None, description='株式報酬引当金繰入額、販売費及び一般管理費')
    """ 株式報酬引当金繰入額、販売費及び一般管理費 """
    provision_for_share_based_remuneration_cl: Optional[IxNonFractionPublic] = Field(default=None, description='株式給付引当金、流動負債')
    """ 株式給付引当金、流動負債 """
    provision_for_share_based_remuneration_for_directors_and_other_officers_cl: Optional[IxNonFractionPublic] = Field(default=None, description='役員株式給付引当金、流動負債')
    """ 役員株式給付引当金、流動負債 """
    provision_for_share_based_remuneration_for_directors_and_other_officers_ncl: Optional[IxNonFractionPublic] = Field(default=None, description='役員株式給付引当金、固定負債')
    """ 役員株式給付引当金、固定負債 """
    provision_for_share_based_remuneration_ncl: Optional[IxNonFractionPublic] = Field(default=None, description='株式給付引当金、固定負債')
    """ 株式給付引当金、固定負債 """
    provision_for_share_based_remuneration_sga: Optional[IxNonFractionPublic] = Field(default=None, description='株式給付引当金繰入額、販売費及び一般管理費')
    """ 株式給付引当金繰入額、販売費及び一般管理費 """
    provision_for_shareholder_benefit_program_cl: Optional[IxNonFractionPublic] = Field(default=None, description='株主優待引当金、流動負債')
    """ 株主優待引当金、流動負債 """
    provision_for_special_repairs: Optional[IxNonFractionPublic] = Field(default=None, description='特別修繕引当金')
    """ 特別修繕引当金 """
    provision_for_special_repairs_nclwat: Optional[IxNonFractionPublic] = Field(default=None, description='特別修繕引当金、固定負債、海運業')
    """ 特別修繕引当金、固定負債、海運業 """
    provision_for_warranties_for_completed_construction: Optional[IxNonFractionPublic] = Field(default=None, description='完成工事補償引当金')
    """ 完成工事補償引当金 """
    provision_ncl: Optional[IxNonFractionPublic] = Field(default=None, description='引当金、固定負債')
    """ 引当金、固定負債 """
    provision_of_allowance_for_doubtful_accounts_el: Optional[IxNonFractionPublic] = Field(default=None, description='貸倒引当金繰入額、特別損失')
    """ 貸倒引当金繰入額、特別損失 """
    provision_of_allowance_for_doubtful_accounts_noe: Optional[IxNonFractionPublic] = Field(default=None, description='貸倒引当金繰入額、営業外費用')
    """ 貸倒引当金繰入額、営業外費用 """
    provision_of_allowance_for_doubtful_accounts_sga: Optional[IxNonFractionPublic] = Field(default=None, description='貸倒引当金繰入額、販売費及び一般管理費')
    """ 貸倒引当金繰入額、販売費及び一般管理費 """
    provision_of_allowance_for_investment_loss_el: Optional[IxNonFractionPublic] = Field(default=None, description='投資損失引当金繰入額、特別損失')
    """ 投資損失引当金繰入額、特別損失 """
    provision_of_general_reserve: Optional[IxNonFractionPublic] = Field(default=None, description='別途積立金の積立')
    """ 別途積立金の積立 """
    provision_of_legal_retained_earnings: Optional[IxNonFractionPublic] = Field(default=None, description='利益準備金の積立')
    """ 利益準備金の積立 """
    provision_of_outstanding_claims_oeins: Optional[IxNonFractionPublic] = Field(default=None, description='支払備金繰入額、経常費用、保険業')
    """ 支払備金繰入額、経常費用、保険業 """
    provision_of_policy_reserve_oeins: Optional[IxNonFractionPublic] = Field(default=None, description='責任準備金繰入額、経常費用、保険業')
    """ 責任準備金繰入額、経常費用、保険業 """
    provision_of_reserve_for_advanced_depreciation_of_noncurrent_assets: Optional[IxNonFractionPublic] = Field(default=None, description='固定資産圧縮積立金の積立')
    """ 固定資産圧縮積立金の積立 """
    provision_of_reserve_for_dividends3: Optional[IxNonFractionPublic] = Field(default=None, description='配当準備積立金の積立')
    """ 配当準備積立金の積立 """
    provision_of_reserve_for_price_fluctuation_elins: Optional[IxNonFractionPublic] = Field(default=None, description='価格変動準備金繰入額、特別損失、保険業')
    """ 価格変動準備金繰入額、特別損失、保険業 """
    provision_of_reserves_under_the_special_laws_el: Optional[IxNonFractionPublic] = Field(default=None, description='特別法上の準備金繰入額、特別損失')
    """ 特別法上の準備金繰入額、特別損失 """
    purchase_discounts_noi: Optional[IxNonFractionPublic] = Field(default=None, description='仕入割引、営業外収益')
    """ 仕入割引、営業外収益 """
    purchase_of_assets_for_rent_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='賃貸資産の取得による支出、営業活動によるキャッシュ・フロー')
    """ 賃貸資産の取得による支出、営業活動によるキャッシュ・フロー """
    purchase_of_insurance_funds_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='保険積立金の積立による支出、投資活動によるキャッシュ・フロー')
    """ 保険積立金の積立による支出、投資活動によるキャッシュ・フロー """
    purchase_of_intangible_assets_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='無形固定資産の取得による支出、投資活動によるキャッシュ・フロー')
    """ 無形固定資産の取得による支出、投資活動によるキャッシュ・フロー """
    purchase_of_investment_securities_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='投資有価証券の取得による支出、投資活動によるキャッシュ・フロー')
    """ 投資有価証券の取得による支出、投資活動によるキャッシュ・フロー """
    purchase_of_investments_in_capital_of_subsidiaries_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='子会社出資金の取得による支出、投資活動によるキャッシュ・フロー')
    """ 子会社出資金の取得による支出、投資活動によるキャッシュ・フロー """
    purchase_of_investments_in_subsidiaries_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='子会社株式の取得による支出、投資活動によるキャッシュ・フロー')
    """ 子会社株式の取得による支出、投資活動によるキャッシュ・フロー """
    purchase_of_investments_in_subsidiaries_resulting_in_change_in_scope_of_consolidation_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='連結の範囲の変更を伴う子会社株式の取得による支出、投資活動によるキャッシュ・フロー')
    """ 連結の範囲の変更を伴う子会社株式の取得による支出、投資活動によるキャッシュ・フロー """
    purchase_of_long_term_prepaid_expenses_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='長期前払費用の取得による支出、投資活動によるキャッシュ・フロー')
    """ 長期前払費用の取得による支出、投資活動によるキャッシュ・フロー """
    purchase_of_noncurrent_assets_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='固定資産の取得による支出、投資活動によるキャッシュ・フロー')
    """ 固定資産の取得による支出、投資活動によるキャッシュ・フロー """
    purchase_of_property_plant_and_equipment_and_intangible_assets_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='有形及び無形固定資産の取得による支出、投資活動によるキャッシュ・フロー')
    """ 有形及び無形固定資産の取得による支出、投資活動によるキャッシュ・フロー """
    purchase_of_property_plant_and_equipment_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='有形固定資産の取得による支出、投資活動によるキャッシュ・フロー')
    """ 有形固定資産の取得による支出、投資活動によるキャッシュ・フロー """
    purchase_of_securities_inv_cfbnk: Optional[IxNonFractionPublic] = Field(default=None, description='有価証券の取得による支出、投資活動によるキャッシュ・フロー、銀行業')
    """ 有価証券の取得による支出、投資活動によるキャッシュ・フロー、銀行業 """
    purchase_of_shares_of_consolidated_subsidiaries: Optional[IxNonFractionPublic] = Field(default=None, description='連結子会社株式の取得による持分の増減')
    """ 連結子会社株式の取得による持分の増減 """
    purchase_of_short_term_and_long_term_investment_securities_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='有価証券及び投資有価証券の取得による支出、投資活動によるキャッシュ・フロー')
    """ 有価証券及び投資有価証券の取得による支出、投資活動によるキャッシュ・フロー """
    purchase_of_short_term_investment_securities_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='有価証券の取得による支出、投資活動によるキャッシュ・フロー')
    """ 有価証券の取得による支出、投資活動によるキャッシュ・フロー """
    purchase_of_software_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='ソフトウエアの取得による支出、投資活動によるキャッシュ・フロー')
    """ ソフトウエアの取得による支出、投資活動によるキャッシュ・フロー """
    purchase_of_stocks_of_subsidiaries_and_affiliates_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='関係会社株式の取得による支出、投資活動によるキャッシュ・フロー')
    """ 関係会社株式の取得による支出、投資活動によるキャッシュ・フロー """
    purchase_of_treasury_stock: Optional[IxNonFractionPublic] = Field(default=None, description='自己株式の取得')
    """ 自己株式の取得 """
    purchase_of_treasury_stock_fin_cf: Optional[IxNonFractionPublic] = Field(default=None, description='自己株式の取得による支出、財務活動によるキャッシュ・フロー')
    """ 自己株式の取得による支出、財務活動によるキャッシュ・フロー """
    purchase_of_treasury_stock_of_subsidiaries_in_consolidation_fin_cf: Optional[IxNonFractionPublic] = Field(default=None, description='子会社の自己株式の取得による支出、財務活動によるキャッシュ・フロー')
    """ 子会社の自己株式の取得による支出、財務活動によるキャッシュ・フロー """
    purchase_of_trust_beneficiary_right_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='信託受益権の取得による支出、投資活動によるキャッシュ・フロー')
    """ 信託受益権の取得による支出、投資活動によるキャッシュ・フロー """
    purchased_receivables_ca: Optional[IxNonFractionPublic] = Field(default=None, description='買取債権、流動資産')
    """ 買取債権、流動資産 """
    raw_materials: Optional[IxNonFractionPublic] = Field(default=None, description='原材料')
    """ 原材料 """
    raw_materials_and_supplies: Optional[IxNonFractionPublic] = Field(default=None, description='原材料及び貯蔵品')
    """ 原材料及び貯蔵品 """
    raw_materials_and_supplies_cns: Optional[IxNonFractionPublic] = Field(default=None, description='材料貯蔵品、建設業')
    """ 材料貯蔵品、建設業 """
    real_estate_for_investment: Optional[IxNonFractionPublic] = Field(default=None, description='投資不動産')
    """ 投資不動産 """
    real_estate_for_investment_net: Optional[IxNonFractionPublic] = Field(default=None, description='投資不動産（純額）')
    """ 投資不動産（純額） """
    real_estate_for_rent_net: Optional[IxNonFractionPublic] = Field(default=None, description='賃貸不動産（純額）')
    """ 賃貸不動産（純額） """
    real_estate_for_sale: Optional[IxNonFractionPublic] = Field(default=None, description='販売用不動産')
    """ 販売用不動産 """
    real_estate_for_sale_cns: Optional[IxNonFractionPublic] = Field(default=None, description='販売用不動産、建設業')
    """ 販売用不動産、建設業 """
    real_estate_for_sale_in_process: Optional[IxNonFractionPublic] = Field(default=None, description='仕掛販売用不動産')
    """ 仕掛販売用不動産 """
    real_estate_income_rev_oa: Optional[IxNonFractionPublic] = Field(default=None, description='不動産収入、営業活動による収益')
    """ 不動産収入、営業活動による収益 """
    real_estate_rent_noi: Optional[IxNonFractionPublic] = Field(default=None, description='不動産賃貸料、営業外収益')
    """ 不動産賃貸料、営業外収益 """
    redemption_of_bonds_fin_cf: Optional[IxNonFractionPublic] = Field(default=None, description='社債の償還による支出、財務活動によるキャッシュ・フロー')
    """ 社債の償還による支出、財務活動によるキャッシュ・フロー """
    redemption_of_commercial_papers_fin_cf: Optional[IxNonFractionPublic] = Field(default=None, description='コマーシャル・ペーパーの償還による支出、財務活動によるキャッシュ・フロー')
    """ コマーシャル・ペーパーの償還による支出、財務活動によるキャッシュ・フロー """
    reduction_entry_of_land_contribution_for_construction_el: Optional[IxNonFractionPublic] = Field(default=None, description='工事負担金等圧縮額、特別損失')
    """ 工事負担金等圧縮額、特別損失 """
    refund_of_income_taxes_income_taxes: Optional[IxNonFractionPublic] = Field(default=None, description='法人税等還付税額、法人税等')
    """ 法人税等還付税額、法人税等 """
    refunded_consumption_taxes_noi: Optional[IxNonFractionPublic] = Field(default=None, description='還付消費税等、営業外収益')
    """ 還付消費税等、営業外収益 """
    reinsurance_accounts_receivable_assets_ins: Optional[IxNonFractionPublic] = Field(default=None, description='再保険貸、資産の部、保険業')
    """ 再保険貸、資産の部、保険業 """
    relocation_expenses_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='移転費用、営業活動によるキャッシュ・フロー')
    """ 移転費用、営業活動によるキャッシュ・フロー """
    remeasurements_of_defined_benefit_plans: Optional[IxNonFractionPublic] = Field(default=None, description='退職給付に係る調整累計額')
    """ 退職給付に係る調整累計額 """
    remeasurements_of_defined_benefit_plans_before_tax_oci: Optional[IxNonFractionPublic] = Field(default=None, description='退職給付に係る調整額（税引前）、その他の包括利益')
    """ 退職給付に係る調整額（税引前）、その他の包括利益 """
    remeasurements_of_defined_benefit_plans_net_of_tax_oci: Optional[IxNonFractionPublic] = Field(default=None, description='退職給付に係る調整額（税引後）、その他の包括利益')
    """ 退職給付に係る調整額（税引後）、その他の包括利益 """
    rent_cost_cos_exp_oa: Optional[IxNonFractionPublic] = Field(default=None, description='賃貸原価、営業活動による費用・売上原価')
    """ 賃貸原価、営業活動による費用・売上原価 """
    rent_cost_of_real_estate_noe: Optional[IxNonFractionPublic] = Field(default=None, description='不動産賃貸原価、営業外費用')
    """ 不動産賃貸原価、営業外費用 """
    rent_expenses_noe: Optional[IxNonFractionPublic] = Field(default=None, description='賃貸費用、営業外費用')
    """ 賃貸費用、営業外費用 """
    rent_expenses_on_facilities_noe: Optional[IxNonFractionPublic] = Field(default=None, description='設備賃貸費用、営業外費用')
    """ 設備賃貸費用、営業外費用 """
    rent_expenses_on_noncurrent_assets_noe: Optional[IxNonFractionPublic] = Field(default=None, description='固定資産賃貸費用、営業外費用')
    """ 固定資産賃貸費用、営業外費用 """
    rent_expenses_on_real_estates_noe: Optional[IxNonFractionPublic] = Field(default=None, description='不動産賃貸費用、営業外費用')
    """ 不動産賃貸費用、営業外費用 """
    rent_expenses_on_real_estates_sga: Optional[IxNonFractionPublic] = Field(default=None, description='不動産賃借料、販売費及び一般管理費')
    """ 不動産賃借料、販売費及び一般管理費 """
    rent_expenses_sga: Optional[IxNonFractionPublic] = Field(default=None, description='賃借料、販売費及び一般管理費')
    """ 賃借料、販売費及び一般管理費 """
    rent_income_noi: Optional[IxNonFractionPublic] = Field(default=None, description='受取賃貸料、営業外収益')
    """ 受取賃貸料、営業外収益 """
    rent_income_on_facilities_noi: Optional[IxNonFractionPublic] = Field(default=None, description='設備賃貸料、営業外収益')
    """ 設備賃貸料、営業外収益 """
    rent_income_on_noncurrent_assets_noi: Optional[IxNonFractionPublic] = Field(default=None, description='固定資産賃貸料、営業外収益')
    """ 固定資産賃貸料、営業外収益 """
    rent_income_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='受取賃貸料、営業活動によるキャッシュ・フロー')
    """ 受取賃貸料、営業活動によるキャッシュ・フロー """
    rent_income_rev_oa: Optional[IxNonFractionPublic] = Field(default=None, description='賃貸収入、営業活動による収益')
    """ 賃貸収入、営業活動による収益 """
    rent_of_real_estate_for_investment_noi: Optional[IxNonFractionPublic] = Field(default=None, description='投資不動産賃貸料、営業外収益')
    """ 投資不動産賃貸料、営業外収益 """
    rents_sga: Optional[IxNonFractionPublic] = Field(default=None, description='地代家賃、販売費及び一般管理費')
    """ 地代家賃、販売費及び一般管理費 """
    repair_and_maintenance_sga: Optional[IxNonFractionPublic] = Field(default=None, description='修繕維持費、販売費及び一般管理費')
    """ 修繕維持費、販売費及び一般管理費 """
    repair_expenses_sga: Optional[IxNonFractionPublic] = Field(default=None, description='修繕費、販売費及び一般管理費')
    """ 修繕費、販売費及び一般管理費 """
    repayment_of_long_term_loans_payable_fin_cf: Optional[IxNonFractionPublic] = Field(default=None, description='長期借入金の返済による支出、財務活動によるキャッシュ・フロー')
    """ 長期借入金の返済による支出、財務活動によるキャッシュ・フロー """
    repayments_of_finance_lease_obligations_fin_cf: Optional[IxNonFractionPublic] = Field(default=None, description='ファイナンス・リース債務の返済による支出、財務活動によるキャッシュ・フロー')
    """ ファイナンス・リース債務の返済による支出、財務活動によるキャッシュ・フロー """
    repayments_of_guarantee_deposits_received_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='預り保証金の返還による支出、投資活動によるキャッシュ・フロー')
    """ 預り保証金の返還による支出、投資活動によるキャッシュ・フロー """
    repayments_of_installment_payables_fin_cf: Optional[IxNonFractionPublic] = Field(default=None, description='割賦債務の返済による支出、財務活動によるキャッシュ・フロー')
    """ 割賦債務の返済による支出、財務活動によるキャッシュ・フロー """
    repayments_of_lease_obligations_fin_cf: Optional[IxNonFractionPublic] = Field(default=None, description='リース債務の返済による支出、財務活動によるキャッシュ・フロー')
    """ リース債務の返済による支出、財務活動によるキャッシュ・フロー """
    repayments_to_non_controlling_shareholders_fin_cf: Optional[IxNonFractionPublic] = Field(default=None, description='非支配株主への払戻による支出、財務活動によるキャッシュ・フロー')
    """ 非支配株主への払戻による支出、財務活動によるキャッシュ・フロー """
    research_and_development_expenses_sga: Optional[IxNonFractionPublic] = Field(default=None, description='研究開発費、販売費及び一般管理費')
    """ 研究開発費、販売費及び一般管理費 """
    research_study_expenses_sga: Optional[IxNonFractionPublic] = Field(default=None, description='調査研究費、販売費及び一般管理費')
    """ 調査研究費、販売費及び一般管理費 """
    reserve_for_advanced_depreciation_of_noncurrent_assets: Optional[IxNonFractionPublic] = Field(default=None, description='固定資産圧縮積立金')
    """ 固定資産圧縮積立金 """
    reserve_for_commodities_transaction_liabilities_reserves_under_the_special_laws_cmd: Optional[IxNonFractionPublic] = Field(default=None, description='商品取引責任準備金、特別法上の準備金、商品先物取引業')
    """ 商品取引責任準備金、特別法上の準備金、商品先物取引業 """
    reserve_for_contract_of_insurance: Optional[IxNonFractionPublic] = Field(default=None, description='保険契約準備金')
    """ 保険契約準備金 """
    reserve_for_dividends3: Optional[IxNonFractionPublic] = Field(default=None, description='配当準備積立金')
    """ 配当準備積立金 """
    reserve_for_financial_products_transaction_liabilities_reserves_under_the_special_laws_sec: Optional[IxNonFractionPublic] = Field(default=None, description='金融商品取引責任準備金、特別法上の準備金、第一種金融商品取引業')
    """ 金融商品取引責任準備金、特別法上の準備金、第一種金融商品取引業 """
    reserve_for_insurance_policy_liabilities_liabilities_ins: Optional[IxNonFractionPublic] = Field(default=None, description='保険契約準備金、負債の部、保険業')
    """ 保険契約準備金、負債の部、保険業 """
    reserve_for_price_fluctuation_liabilities_ins: Optional[IxNonFractionPublic] = Field(default=None, description='価格変動準備金、負債の部、保険業')
    """ 価格変動準備金、負債の部、保険業 """
    reserve_for_reduction_entry2: Optional[IxNonFractionPublic] = Field(default=None, description='圧縮積立金')
    """ 圧縮積立金 """
    reserve_for_reduction_entry_of_real_estate: Optional[IxNonFractionPublic] = Field(default=None, description='不動産圧縮積立金')
    """ 不動産圧縮積立金 """
    reserve_for_special_account_for_advanced_depreciation_of_noncurrent_assets: Optional[IxNonFractionPublic] = Field(default=None, description='固定資産圧縮特別勘定積立金')
    """ 固定資産圧縮特別勘定積立金 """
    reserves_under_the_special_laws1: Optional[IxNonFractionPublic] = Field(default=None, description='特別法上の準備金')
    """ 特別法上の準備金 """
    reserves_under_the_special_laws2: Optional[IxNonFractionPublic] = Field(default=None, description='特別法上の引当金')
    """ 特別法上の引当金 """
    rest_of_the_other_assets_assets_ins: Optional[IxNonFractionPublic] = Field(default=None, description='その他の資産、資産の部、保険業')
    """ その他の資産、資産の部、保険業 """
    restated_balance: Optional[IxNonFractionPublic] = Field(default=None, description='会計方針の変更を反映した当期首残高')
    """ 会計方針の変更を反映した当期首残高 """
    restructuring_loss_el: Optional[IxNonFractionPublic] = Field(default=None, description='事業再編損、特別損失')
    """ 事業再編損、特別損失 """
    retained_earnings: Optional[IxNonFractionPublic] = Field(default=None, description='利益剰余金')
    """ 利益剰余金 """
    retained_earnings_brought_forward: Optional[IxNonFractionPublic] = Field(default=None, description='繰越利益剰余金')
    """ 繰越利益剰余金 """
    retirement_benefit_expenses_el: Optional[IxNonFractionPublic] = Field(default=None, description='退職給付費用、特別損失')
    """ 退職給付費用、特別損失 """
    retirement_benefit_expenses_sga: Optional[IxNonFractionPublic] = Field(default=None, description='退職給付費用、販売費及び一般管理費')
    """ 退職給付費用、販売費及び一般管理費 """
    retirement_of_treasury_stock: Optional[IxNonFractionPublic] = Field(default=None, description='自己株式の消却')
    """ 自己株式の消却 """
    retirement_payments_sga: Optional[IxNonFractionPublic] = Field(default=None, description='退職金、販売費及び一般管理費')
    """ 退職金、販売費及び一般管理費 """
    revaluation_reserve_for_land: Optional[IxNonFractionPublic] = Field(default=None, description='土地再評価差額金')
    """ 土地再評価差額金 """
    revaluation_reserve_for_land_net_of_tax_oci: Optional[IxNonFractionPublic] = Field(default=None, description='土地再評価差額金（税引後）、その他の包括利益')
    """ 土地再評価差額金（税引後）、その他の包括利益 """
    revenue: Optional[IxNonFractionPublic] = Field(default=None, description='売上収益')
    """ 売上収益 """
    revenue_from_contracts_with_customers: Optional[IxNonFractionPublic] = Field(default=None, description='顧客との契約から生じる収益')
    """ 顧客との契約から生じる収益 """
    revenue_from_credit_guarantee_rev_oa: Optional[IxNonFractionPublic] = Field(default=None, description='信用保証収益、営業活動による収益')
    """ 信用保証収益、営業活動による収益 """
    revenue_other_than_that_from_contracts_with_customers: Optional[IxNonFractionPublic] = Field(default=None, description='顧客との契約から生じる収益以外の収益')
    """ 顧客との契約から生じる収益以外の収益 """
    reversal_of_allowance_for_doubtful_accounts_ei: Optional[IxNonFractionPublic] = Field(default=None, description='貸倒引当金戻入額、特別利益')
    """ 貸倒引当金戻入額、特別利益 """
    reversal_of_allowance_for_doubtful_accounts_noi: Optional[IxNonFractionPublic] = Field(default=None, description='貸倒引当金戻入額、営業外収益')
    """ 貸倒引当金戻入額、営業外収益 """
    reversal_of_policy_reserve_ins: Optional[IxNonFractionPublic] = Field(default=None, description='責任準備金戻入額、保険業')
    """ 責任準備金戻入額、保険業 """
    reversal_of_provision_for_business_structure_improvement_ei: Optional[IxNonFractionPublic] = Field(default=None, description='事業構造改善引当金戻入額、特別利益')
    """ 事業構造改善引当金戻入額、特別利益 """
    reversal_of_provision_for_directors_retirement_benefits_ei: Optional[IxNonFractionPublic] = Field(default=None, description='役員退職慰労引当金戻入額、特別利益')
    """ 役員退職慰労引当金戻入額、特別利益 """
    reversal_of_provision_for_loss_on_liquidation_of_subsidiaries_and_affiliates_ei: Optional[IxNonFractionPublic] = Field(default=None, description='関係会社整理損失引当金戻入額、特別利益')
    """ 関係会社整理損失引当金戻入額、特別利益 """
    reversal_of_provision_for_loss_on_store_closing_ei: Optional[IxNonFractionPublic] = Field(default=None, description='店舗閉鎖損失引当金戻入額、特別利益')
    """ 店舗閉鎖損失引当金戻入額、特別利益 """
    reversal_of_reserve_for_advanced_depreciation_of_noncurrent_assets: Optional[IxNonFractionPublic] = Field(default=None, description='固定資産圧縮積立金の取崩')
    """ 固定資産圧縮積立金の取崩 """
    reversal_of_reserve_for_reduction_entry2: Optional[IxNonFractionPublic] = Field(default=None, description='圧縮積立金の取崩')
    """ 圧縮積立金の取崩 """
    reversal_of_reserve_for_reduction_entry_of_real_estate: Optional[IxNonFractionPublic] = Field(default=None, description='不動産圧縮積立金の取崩')
    """ 不動産圧縮積立金の取崩 """
    reversal_of_reserve_for_special_depreciation: Optional[IxNonFractionPublic] = Field(default=None, description='特別償却準備金の取崩')
    """ 特別償却準備金の取崩 """
    reversal_of_revaluation_reserve_for_land: Optional[IxNonFractionPublic] = Field(default=None, description='土地再評価差額金の取崩')
    """ 土地再評価差額金の取崩 """
    reversal_of_special_reserve_for_expansion_of_railway_transport_capacity_eirwy: Optional[IxNonFractionPublic] = Field(default=None, description='特定都市鉄道整備準備金取崩額、特別利益、鉄道事業')
    """ 特定都市鉄道整備準備金取崩額、特別利益、鉄道事業 """
    right_of_trademark: Optional[IxNonFractionPublic] = Field(default=None, description='商標権')
    """ 商標権 """
    right_of_use_assets: Optional[IxNonFractionPublic] = Field(default=None, description='使用権資産')
    """ 使用権資産 """
    right_of_use_assets_net: Optional[IxNonFractionPublic] = Field(default=None, description='使用権資産（純額）')
    """ 使用権資産（純額） """
    right_of_using_facilities_ia: Optional[IxNonFractionPublic] = Field(default=None, description='施設利用権')
    """ 施設利用権 """
    royalty_income_noi: Optional[IxNonFractionPublic] = Field(default=None, description='受取ロイヤリティー、営業外収益')
    """ 受取ロイヤリティー、営業外収益 """
    salaries_allowances_and_bonuses_sga: Optional[IxNonFractionPublic] = Field(default=None, description='給料手当及び賞与、販売費及び一般管理費')
    """ 給料手当及び賞与、販売費及び一般管理費 """
    salaries_and_allowances_sga: Optional[IxNonFractionPublic] = Field(default=None, description='給料及び手当、販売費及び一般管理費')
    """ 給料及び手当、販売費及び一般管理費 """
    salaries_and_bonuses_sga: Optional[IxNonFractionPublic] = Field(default=None, description='給料及び賞与、販売費及び一般管理費')
    """ 給料及び賞与、販売費及び一般管理費 """
    salaries_and_wages_sga: Optional[IxNonFractionPublic] = Field(default=None, description='給料及び賃金、販売費及び一般管理費')
    """ 給料及び賃金、販売費及び一般管理費 """
    salaries_sga: Optional[IxNonFractionPublic] = Field(default=None, description='給料、販売費及び一般管理費')
    """ 給料、販売費及び一般管理費 """
    sales_and_administrative_expenses_oeins: Optional[IxNonFractionPublic] = Field(default=None, description='営業費及び一般管理費、経常費用、保険業')
    """ 営業費及び一般管理費、経常費用、保険業 """
    sales_commission_sga: Optional[IxNonFractionPublic] = Field(default=None, description='販売手数料、販売費及び一般管理費')
    """ 販売手数料、販売費及び一般管理費 """
    sales_discounts_noe: Optional[IxNonFractionPublic] = Field(default=None, description='売上割引、営業外費用')
    """ 売上割引、営業外費用 """
    sales_on_other_business_rev_oa: Optional[IxNonFractionPublic] = Field(default=None, description='その他の事業売上高、営業活動による収益')
    """ その他の事業売上高、営業活動による収益 """
    sales_on_real_estate_business_rev_oa: Optional[IxNonFractionPublic] = Field(default=None, description='不動産事業売上高、営業活動による収益')
    """ 不動産事業売上高、営業活動による収益 """
    securities_assets_bnk: Optional[IxNonFractionPublic] = Field(default=None, description='有価証券、資産の部、銀行業')
    """ 有価証券、資産の部、銀行業 """
    securities_assets_ins: Optional[IxNonFractionPublic] = Field(default=None, description='有価証券、資産の部、保険業')
    """ 有価証券、資産の部、保険業 """
    selling_expenses_sga: Optional[IxNonFractionPublic] = Field(default=None, description='販売費、販売費及び一般管理費')
    """ 販売費、販売費及び一般管理費 """
    selling_general_and_administrative_expenses: Optional[IxNonFractionPublic] = Field(default=None, description='販売費及び一般管理費')
    """ 販売費及び一般管理費 """
    selling_general_and_administrative_expenses_gas: Optional[IxNonFractionPublic] = Field(default=None, description='供給販売費及び一般管理費、ガス事業')
    """ 供給販売費及び一般管理費、ガス事業 """
    semi_finished_goods: Optional[IxNonFractionPublic] = Field(default=None, description='半製品')
    """ 半製品 """
    service_and_maintenance_facilities_ppegas: Optional[IxNonFractionPublic] = Field(default=None, description='業務設備、有形固定資産、ガス事業')
    """ 業務設備、有形固定資産、ガス事業 """
    settlement_package_el: Optional[IxNonFractionPublic] = Field(default=None, description='和解金、特別損失')
    """ 和解金、特別損失 """
    settlement_package_noe: Optional[IxNonFractionPublic] = Field(default=None, description='和解金、営業外費用')
    """ 和解金、営業外費用 """
    settlement_package_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='和解金、営業活動によるキャッシュ・フロー')
    """ 和解金、営業活動によるキャッシュ・フロー """
    settlement_package_paid_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='和解金の支払額、営業活動によるキャッシュ・フロー')
    """ 和解金の支払額、営業活動によるキャッシュ・フロー """
    settlement_package_received_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='和解金の受取額、営業活動によるキャッシュ・フロー')
    """ 和解金の受取額、営業活動によるキャッシュ・フロー """
    settlement_received_ei: Optional[IxNonFractionPublic] = Field(default=None, description='受取和解金、特別利益')
    """ 受取和解金、特別利益 """
    settlement_received_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='受取和解金、営業活動によるキャッシュ・フロー')
    """ 受取和解金、営業活動によるキャッシュ・フロー """
    share_acquisition_rights_issuance_costs_noe: Optional[IxNonFractionPublic] = Field(default=None, description='新株予約権発行費、営業外費用')
    """ 新株予約権発行費、営業外費用 """
    share_based_compensation_expenses_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='株式報酬費用、営業活動によるキャッシュ・フロー')
    """ 株式報酬費用、営業活動によるキャッシュ・フロー """
    share_based_compensation_expenses_sga: Optional[IxNonFractionPublic] = Field(default=None, description='株式報酬費用、販売費及び一般管理費')
    """ 株式報酬費用、販売費及び一般管理費 """
    share_of_other_comprehensive_income_of_associates_accounted_for_using_equity_method_oci: Optional[IxNonFractionPublic] = Field(default=None, description='持分法適用会社に対する持分相当額、その他の包括利益')
    """ 持分法適用会社に対する持分相当額、その他の包括利益 """
    shareholders_equity: Optional[IxNonFractionPublic] = Field(default=None, description='株主資本')
    """ 株主資本 """
    short_term_bonds_payable: Optional[IxNonFractionPublic] = Field(default=None, description='短期社債')
    """ 短期社債 """
    short_term_investment_securities: Optional[IxNonFractionPublic] = Field(default=None, description='有価証券')
    """ 有価証券 """
    short_term_loans_payable: Optional[IxNonFractionPublic] = Field(default=None, description='短期借入金')
    """ 短期借入金 """
    short_term_loans_payable_to_subsidiaries_and_affiliates: Optional[IxNonFractionPublic] = Field(default=None, description='関係会社短期借入金')
    """ 関係会社短期借入金 """
    short_term_loans_receivable: Optional[IxNonFractionPublic] = Field(default=None, description='短期貸付金')
    """ 短期貸付金 """
    short_term_loans_receivable_to_subsidiaries_and_affiliates: Optional[IxNonFractionPublic] = Field(default=None, description='関係会社短期貸付金')
    """ 関係会社短期貸付金 """
    software: Optional[IxNonFractionPublic] = Field(default=None, description='ソフトウエア')
    """ ソフトウエア """
    software_in_progress: Optional[IxNonFractionPublic] = Field(default=None, description='ソフトウエア仮勘定')
    """ ソフトウエア仮勘定 """
    special_reserve_for_expansion_of_railway_transport_capacity_rwy: Optional[IxNonFractionPublic] = Field(default=None, description='特定都市鉄道整備準備金、鉄道事業')
    """ 特定都市鉄道整備準備金、鉄道事業 """
    special_retirement_expenses_el: Optional[IxNonFractionPublic] = Field(default=None, description='特別退職金、特別損失')
    """ 特別退職金、特別損失 """
    state_subsidy_ei: Optional[IxNonFractionPublic] = Field(default=None, description='国庫補助金、特別利益')
    """ 国庫補助金、特別利益 """
    stationery_expenses_sga: Optional[IxNonFractionPublic] = Field(default=None, description='事務用品費、販売費及び一般管理費')
    """ 事務用品費、販売費及び一般管理費 """
    stevedoring_income_rev_oa: Optional[IxNonFractionPublic] = Field(default=None, description='倉庫荷役料、営業活動による収益')
    """ 倉庫荷役料、営業活動による収益 """
    stock_issuance_cost_da: Optional[IxNonFractionPublic] = Field(default=None, description='株式交付費、繰延資産')
    """ 株式交付費、繰延資産 """
    stock_issuance_cost_noe: Optional[IxNonFractionPublic] = Field(default=None, description='株式交付費、営業外費用')
    """ 株式交付費、営業外費用 """
    stock_issuance_cost_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='株式交付費、営業活動によるキャッシュ・フロー')
    """ 株式交付費、営業活動によるキャッシュ・フロー """
    stock_issuance_cost_prior_noe: Optional[IxNonFractionPublic] = Field(default=None, description='新株発行費、営業外費用')
    """ 新株発行費、営業外費用 """
    stocks_of_subsidiaries_and_affiliates: Optional[IxNonFractionPublic] = Field(default=None, description='関係会社株式')
    """ 関係会社株式 """
    structures: Optional[IxNonFractionPublic] = Field(default=None, description='構築物')
    """ 構築物 """
    structures_net: Optional[IxNonFractionPublic] = Field(default=None, description='構築物（純額）')
    """ 構築物（純額） """
    subscription_rights_to_shares: Optional[IxNonFractionPublic] = Field(default=None, description='新株予約権')
    """ 新株予約権 """
    subsidies_for_employment_adjustment_noi: Optional[IxNonFractionPublic] = Field(default=None, description='雇用調整助成金、営業外収益')
    """ 雇用調整助成金、営業外収益 """
    subsidies_for_employment_adjustment_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='雇用調整助成金、営業活動によるキャッシュ・フロー')
    """ 雇用調整助成金、営業活動によるキャッシュ・フロー """
    subsidies_received_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='補助金の受取額、投資活動によるキャッシュ・フロー')
    """ 補助金の受取額、投資活動によるキャッシュ・フロー """
    subsidy_ei: Optional[IxNonFractionPublic] = Field(default=None, description='補助金収入、特別利益')
    """ 補助金収入、特別利益 """
    subsidy_eirwy: Optional[IxNonFractionPublic] = Field(default=None, description='補助金、特別利益、鉄道事業')
    """ 補助金、特別利益、鉄道事業 """
    subsidy_income2_ei: Optional[IxNonFractionPublic] = Field(default=None, description='助成金収入、特別利益')
    """ 助成金収入、特別利益 """
    subsidy_income2_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='助成金収入、営業活動によるキャッシュ・フロー')
    """ 助成金収入、営業活動によるキャッシュ・フロー """
    subsidy_income_noi: Optional[IxNonFractionPublic] = Field(default=None, description='補助金収入、営業外収益')
    """ 補助金収入、営業外収益 """
    subsidy_income_noi_bounty: Optional[IxNonFractionPublic] = Field(default=None, description='助成金収入、営業外収益')
    """ 助成金収入、営業外収益 """
    subsidy_income_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='補助金収入、営業活動によるキャッシュ・フロー')
    """ 補助金収入、営業活動によるキャッシュ・フロー """
    subtotal_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='小計、営業活動によるキャッシュ・フロー')
    """ 小計、営業活動によるキャッシュ・フロー """
    supplies: Optional[IxNonFractionPublic] = Field(default=None, description='貯蔵品')
    """ 貯蔵品 """
    supplies_expenses_sga: Optional[IxNonFractionPublic] = Field(default=None, description='消耗品費、販売費及び一般管理費')
    """ 消耗品費、販売費及び一般管理費 """
    surrender_value_of_insurance_ei: Optional[IxNonFractionPublic] = Field(default=None, description='保険解約返戻金、特別利益')
    """ 保険解約返戻金、特別利益 """
    surrender_value_of_insurance_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='保険解約返戻金、営業活動によるキャッシュ・フロー')
    """ 保険解約返戻金、営業活動によるキャッシュ・フロー """
    suspense_payments_assets_ins: Optional[IxNonFractionPublic] = Field(default=None, description='仮払金、資産の部、保険業')
    """ 仮払金、資産の部、保険業 """
    taxes_and_dues_noe: Optional[IxNonFractionPublic] = Field(default=None, description='租税公課、営業外費用')
    """ 租税公課、営業外費用 """
    taxes_and_dues_sga: Optional[IxNonFractionPublic] = Field(default=None, description='租税公課、販売費及び一般管理費')
    """ 租税公課、販売費及び一般管理費 """
    technical_support_fee_noi: Optional[IxNonFractionPublic] = Field(default=None, description='受取技術料、営業外収益')
    """ 受取技術料、営業外収益 """
    telephone_subscription_right: Optional[IxNonFractionPublic] = Field(default=None, description='電話加入権')
    """ 電話加入権 """
    tools_furniture_and_fixtures: Optional[IxNonFractionPublic] = Field(default=None, description='工具、器具及び備品')
    """ 工具、器具及び備品 """
    tools_furniture_and_fixtures_net: Optional[IxNonFractionPublic] = Field(default=None, description='工具、器具及び備品（純額）')
    """ 工具、器具及び備品（純額） """
    total_beginning_and_purchase_of_goods: Optional[IxNonFractionPublic] = Field(default=None, description='合計、商品期首棚卸高及び当期商品仕入高')
    """ 合計、商品期首棚卸高及び当期商品仕入高 """
    total_beginning_finished_goods_and_cost_of_products_manufactured_for_the_period: Optional[IxNonFractionPublic] = Field(default=None, description='合計、製品期首棚卸高及び当期製品製造原価')
    """ 合計、製品期首棚卸高及び当期製品製造原価 """
    total_changes_of_items_during_the_period: Optional[IxNonFractionPublic] = Field(default=None, description='当期変動額合計')
    """ 当期変動額合計 """
    total_of_net_cash_provided_by_used_in_investment_transactions_inv_cfins: Optional[IxNonFractionPublic] = Field(default=None, description='資産運用活動計、投資活動によるキャッシュ・フロー、保険業')
    """ 資産運用活動計、投資活動によるキャッシュ・フロー、保険業 """
    total_of_net_cash_provided_by_used_in_operating_activities_and_investment_transactions_inv_cfins: Optional[IxNonFractionPublic] = Field(default=None, description='営業活動及び資産運用活動計、投資活動によるキャッシュ・フロー、保険業')
    """ 営業活動及び資産運用活動計、投資活動によるキャッシュ・フロー、保険業 """
    trading_account_securities_assets_bnk: Optional[IxNonFractionPublic] = Field(default=None, description='商品有価証券、資産の部、銀行業')
    """ 商品有価証券、資産の部、銀行業 """
    trading_assets_assets_bnk: Optional[IxNonFractionPublic] = Field(default=None, description='特定取引資産、資産の部、銀行業')
    """ 特定取引資産、資産の部、銀行業 """
    trading_expenses_oebnk: Optional[IxNonFractionPublic] = Field(default=None, description='特定取引費用、経常費用、銀行業')
    """ 特定取引費用、経常費用、銀行業 """
    trading_income_oibnk: Optional[IxNonFractionPublic] = Field(default=None, description='特定取引収益、経常収益、銀行業')
    """ 特定取引収益、経常収益、銀行業 """
    trading_liabilities_liabilities_bnk: Optional[IxNonFractionPublic] = Field(default=None, description='特定取引負債、負債の部、銀行業')
    """ 特定取引負債、負債の部、銀行業 """
    transfer_from_reserve_for_financial_products_transaction_liabilities_eibnk: Optional[IxNonFractionPublic] = Field(default=None, description='金融商品取引責任準備金取崩額、特別利益、銀行業')
    """ 金融商品取引責任準備金取崩額、特別利益、銀行業 """
    transfer_of_loss_on_disposal_of_treasury_stock: Optional[IxNonFractionPublic] = Field(default=None, description='自己株式処分差損の振替')
    """ 自己株式処分差損の振替 """
    transfer_to_capital_surplus_from_retained_earnings: Optional[IxNonFractionPublic] = Field(default=None, description='利益剰余金から資本剰余金への振替')
    """ 利益剰余金から資本剰余金への振替 """
    transfer_to_other_account_cos: Optional[IxNonFractionPublic] = Field(default=None, description='他勘定振替高、売上原価')
    """ 他勘定振替高、売上原価 """
    transfer_to_reserve_for_financial_products_transaction_liabilities_elbnk: Optional[IxNonFractionPublic] = Field(default=None, description='金融商品取引責任準備金繰入額、特別損失、銀行業')
    """ 金融商品取引責任準備金繰入額、特別損失、銀行業 """
    transportation_and_communication_expenses_sga: Optional[IxNonFractionPublic] = Field(default=None, description='旅費交通費及び通信費、販売費及び一般管理費')
    """ 旅費交通費及び通信費、販売費及び一般管理費 """
    transportation_and_warehousing_expenses_sga: Optional[IxNonFractionPublic] = Field(default=None, description='運送費及び保管費、販売費及び一般管理費')
    """ 運送費及び保管費、販売費及び一般管理費 """
    transportation_income_rev_oa: Optional[IxNonFractionPublic] = Field(default=None, description='運送収入、営業活動による収益')
    """ 運送収入、営業活動による収益 """
    traveling_and_transportation_expenses_sga: Optional[IxNonFractionPublic] = Field(default=None, description='旅費及び交通費、販売費及び一般管理費')
    """ 旅費及び交通費、販売費及び一般管理費 """
    treasury_stock: Optional[IxNonFractionPublic] = Field(default=None, description='自己株式')
    """ 自己株式 """
    trees_ppe: Optional[IxNonFractionPublic] = Field(default=None, description='立木、有形固定資産')
    """ 立木、有形固定資産 """
    trust_fees_bnk: Optional[IxNonFractionPublic] = Field(default=None, description='信託報酬、銀行業')
    """ 信託報酬、銀行業 """
    underwriting_expenses_oeins: Optional[IxNonFractionPublic] = Field(default=None, description='保険引受費用、経常費用、保険業')
    """ 保険引受費用、経常費用、保険業 """
    underwriting_income_oiins: Optional[IxNonFractionPublic] = Field(default=None, description='保険引受収益、経常収益、保険業')
    """ 保険引受収益、経常収益、保険業 """
    unearned_revenue: Optional[IxNonFractionPublic] = Field(default=None, description='前受収益')
    """ 前受収益 """
    utilities_expenses_sga: Optional[IxNonFractionPublic] = Field(default=None, description='水道光熱費、販売費及び一般管理費')
    """ 水道光熱費、販売費及び一般管理費 """
    valuation_and_translation_adjustments: Optional[IxNonFractionPublic] = Field(default=None, description='評価・換算差額等')
    """ 評価・換算差額等 """
    valuation_difference_on_available_for_sale_securities: Optional[IxNonFractionPublic] = Field(default=None, description='その他有価証券評価差額金')
    """ その他有価証券評価差額金 """
    valuation_difference_on_available_for_sale_securities_before_tax_oci: Optional[IxNonFractionPublic] = Field(default=None, description='その他有価証券評価差額金（税引前）、その他の包括利益')
    """ その他有価証券評価差額金（税引前）、その他の包括利益 """
    valuation_difference_on_available_for_sale_securities_net_of_tax_oci: Optional[IxNonFractionPublic] = Field(default=None, description='その他有価証券評価差額金（税引後）、その他の包括利益')
    """ その他有価証券評価差額金（税引後）、その他の包括利益 """
    vehicle_expenses_sga: Optional[IxNonFractionPublic] = Field(default=None, description='車両費、販売費及び一般管理費')
    """ 車両費、販売費及び一般管理費 """
    vehicles: Optional[IxNonFractionPublic] = Field(default=None, description='車両運搬具')
    """ 車両運搬具 """
    vehicles_net: Optional[IxNonFractionPublic] = Field(default=None, description='車両運搬具（純額）')
    """ 車両運搬具（純額） """
    vessels: Optional[IxNonFractionPublic] = Field(default=None, description='船舶')
    """ 船舶 """
    vessels_net: Optional[IxNonFractionPublic] = Field(default=None, description='船舶（純額）')
    """ 船舶（純額） """
    warehousing_expenses_sga: Optional[IxNonFractionPublic] = Field(default=None, description='保管費、販売費及び一般管理費')
    """ 保管費、販売費及び一般管理費 """
    warehousing_fee_income_rev_oa: Optional[IxNonFractionPublic] = Field(default=None, description='倉庫保管料、営業活動による収益')
    """ 倉庫保管料、営業活動による収益 """
    welfare_expenses_sga: Optional[IxNonFractionPublic] = Field(default=None, description='福利厚生費、販売費及び一般管理費')
    """ 福利厚生費、販売費及び一般管理費 """
    work_in_process: Optional[IxNonFractionPublic] = Field(default=None, description='仕掛品')
    """ 仕掛品 """
    business_structure_improvement_payments_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='事業構造改善支出、営業活動によるキャッシュ・フロー')
    """ 事業構造改善支出、営業活動によるキャッシュ・フロー """
    changes_in_equity_due_to_capital_transfer: Optional[IxNonFractionPublic] = Field(default=None, description='資本移動に伴う持分の変動')
    """ 資本移動に伴う持分の変動 """
    loans_made_to_customers_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='貸付金による支出、投資活動によるキャッシュ・フロー')
    """ 貸付金による支出、投資活動によるキャッシュ・フロー """
    losses_on_fire_disaster_el: Optional[IxNonFractionPublic] = Field(default=None, description='火災損害等損失、特別損失')
    """ 火災損害等損失、特別損失 """
    purchase_of_share_of_consolidated_subsidiaries_treasury_stock_changes_of_items_during_period: Optional[IxNonFractionPublic] = Field(default=None, description='連結子会社の自己株式取得による持分の増減')
    """ 連結子会社の自己株式取得による持分の増減 """
    non_deductible_consumption_tax_noe: Optional[IxNonFractionPublic] = Field(default=None, description='控除対象外消費税等、営業外費用')
    """ 控除対象外消費税等、営業外費用 """
    amortization_of_goodwill_el: Optional[IxNonFractionPublic] = Field(default=None, description='のれん償却額、特別損失')
    """ のれん償却額、特別損失 """
    amortization_of_goodwill_segment_information: Optional[IxNonFractionPublic] = Field(default=None, description='のれんの償却額、セグメント情報')
    """ のれんの償却額、セグメント情報 """
    depreciation_of_fixed_assets_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='有形固定資産減価償却費、営業活動によるキャッシュ・フロー')
    """ 有形固定資産減価償却費、営業活動によるキャッシュ・フロー """
    depreciation_of_intangible_assets: Optional[IxNonFractionPublic] = Field(default=None, description='無形固定資産減価償却費、営業活動によるキャッシュ・フロー')
    """ 無形固定資産減価償却費、営業活動によるキャッシュ・フロー """
    issuance_of_new_shares_restricted_stock: Optional[IxNonFractionPublic] = Field(default=None, description='新株の発行（譲渡制限付株式報酬）')
    """ 新株の発行（譲渡制限付株式報酬） """
    lease_and_guarantee_deposits_ioa: Optional[IxNonFractionPublic] = Field(default=None, description='差入敷金保証金、投資その他の資産、固定資産、資産の部')
    """ 差入敷金保証金、投資その他の資産、固定資産、資産の部 """
    proceeds_from_share_of_profits_on_investments_in_partnership: Optional[IxNonFractionPublic] = Field(default=None, description='投資事業組合分配金収入、投資活動によるキャッシュ・フロー')
    """ 投資事業組合分配金収入、投資活動によるキャッシュ・フロー """
    gain_on_disposal_of_treasury_stock: Optional[IxNonFractionPublic] = Field(default=None, description='自己株式処分差益')
    """ 自己株式処分差益 """
    head_office_relocation_expenses_noe: Optional[IxNonFractionPublic] = Field(default=None, description='本社移転費用、営業外費用')
    """ 本社移転費用、営業外費用 """
    proceeds_from_surrender_value_of_insurance_policies_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='保険解約返戻金の受取額、営業活動によるキャッシュ・フロー')
    """ 保険解約返戻金の受取額、営業活動によるキャッシュ・フロー """
    proceeds_from_withdrawal_of_investments_in_securities_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='投資有価証券の払戻による収入、投資活動によるキャッシュ・フロー')
    """ 投資有価証券の払戻による収入、投資活動によるキャッシュ・フロー """
    retirement_benefit_liability_cl: Optional[IxNonFractionPublic] = Field(default=None, description='退職給付に係る負債、流動負債')
    """ 退職給付に係る負債、流動負債 """
    compensation_for_damage_income_noi: Optional[IxNonFractionPublic] = Field(default=None, description='受取損害賠償金、営業外収益')
    """ 受取損害賠償金、営業外収益 """
    increase_decrease_in_account_payable_transition_of_retirement_benefit_plan_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='退職給付制度移行に伴う未払金の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 退職給付制度移行に伴う未払金の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    increase_decrease_in_net_defined_benefit_asset_and_liability_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='退職給付に係る資産負債の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 退職給付に係る資産負債の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    proceeds_from_surrender_value_of_insurance_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='保険解約返戻金の受取額、営業活動によるキャッシュ・フロー')
    """ 保険解約返戻金の受取額、営業活動によるキャッシュ・フロー """
    customer_relationship_ia: Optional[IxNonFractionPublic] = Field(default=None, description='顧客関連資産、無形固定資産')
    """ 顧客関連資産、無形固定資産 """
    loss_on_related_to_rebuilding_el: Optional[IxNonFractionPublic] = Field(default=None, description='建替関連損失、特別損失')
    """ 建替関連損失、特別損失 """
    loss_on_related_to_rebuilding_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='建替関連損失、営業活動によるキャッシュ・フロー')
    """ 建替関連損失、営業活動によるキャッシュ・フロー """
    provision_for_removal_cost_cl: Optional[IxNonFractionPublic] = Field(default=None, description='撤去費用引当金、流動負債')
    """ 撤去費用引当金、流動負債 """
    surrender_value_of_insurance_policies_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='保険解約返戻金の受取額、営業活動によるキャッシュ・フロー')
    """ 保険解約返戻金の受取額、営業活動によるキャッシュ・フロー """
    collection_of_loans_receivable_from_subsidiaries_and_affiliates_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='関係会社貸付金の回収による収入、投資活動によるキャッシュ・フロー')
    """ 関係会社貸付金の回収による収入、投資活動によるキャッシュ・フロー """
    compensation_for_damage_noe: Optional[IxNonFractionPublic] = Field(default=None, description='損害賠償金、営業外費用')
    """ 損害賠償金、営業外費用 """
    restricted_stock: Optional[IxNonFractionPublic] = Field(default=None, description='譲渡制限付株式報酬')
    """ 譲渡制限付株式報酬 """
    loss_on_development_of_system_el: Optional[IxNonFractionPublic] = Field(default=None, description='システム開発に伴う損失、特別損失')
    """ システム開発に伴う損失、特別損失 """
    loss_on_development_of_system_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='システム開発に伴う損失、営業活動によるキャッシュ・フロー')
    """ システム開発に伴う損失、営業活動によるキャッシュ・フロー """
    nondeductible_consumption_tax_noe: Optional[IxNonFractionPublic] = Field(default=None, description='控除対象外消費税等、営業外費用')
    """ 控除対象外消費税等、営業外費用 """
    proceeds_from_penalty_income_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='違約金の受取額、営業活動によるキャッシュ・フロー')
    """ 違約金の受取額、営業活動によるキャッシュ・フロー """
    accumulated_depreciation_right_of_use_assets_ppe: Optional[IxNonFractionPublic] = Field(default=None, description='減価償却累計額、使用権資産、有形固定資産')
    """ 減価償却累計額、使用権資産、有形固定資産 """
    dividends_from_surplus_interim_dividends: Optional[IxNonFractionPublic] = Field(default=None, description='剰余金の配当（中間配当）')
    """ 剰余金の配当（中間配当） """
    income_of_compensation_ei: Optional[IxNonFractionPublic] = Field(default=None, description='受取賠償金、特別利益')
    """ 受取賠償金、特別利益 """
    right_of_use_assets_ppe: Optional[IxNonFractionPublic] = Field(default=None, description='使用権資産、有形固定資産')
    """ 使用権資産、有形固定資産 """
    disposal_of_treasury_shares_by_stock_payment_trust: Optional[IxNonFractionPublic] = Field(default=None, description='株式給付信託による自己株式の処分')
    """ 株式給付信託による自己株式の処分 """
    increase_decrease_provision_for_loss_on_store_closing_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='閉店損失引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 閉店損失引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    provision_for_loss_on_store_closure_cl: Optional[IxNonFractionPublic] = Field(default=None, description='閉店損失引当金、流動負債')
    """ 閉店損失引当金、流動負債 """
    stock_related_cost_noe: Optional[IxNonFractionPublic] = Field(default=None, description='株式関連費、営業外費用')
    """ 株式関連費、営業外費用 """
    compensation_for_damage_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='損害賠償金、営業活動によるキャッシュ・フロー')
    """ 損害賠償金、営業活動によるキャッシュ・フロー """
    compensation_received_noi: Optional[IxNonFractionPublic] = Field(default=None, description='補償金収入、営業外収益')
    """ 補償金収入、営業外収益 """
    increase_due_to_share_issuance: Optional[IxNonFractionPublic] = Field(default=None, description='株式交付による増加')
    """ 株式交付による増加 """
    increase_in_cash_and_cash_equivalents_due_to_share_issuance: Optional[IxNonFractionPublic] = Field(default=None, description='株式交付に伴う現金及び現金同等物の増加額')
    """ 株式交付に伴う現金及び現金同等物の増加額 """
    insurance_received_noi: Optional[IxNonFractionPublic] = Field(default=None, description='保険金収入、営業外収益')
    """ 保険金収入、営業外収益 """
    loss_on_accident_el: Optional[IxNonFractionPublic] = Field(default=None, description='事故関連損失、特別損失')
    """ 事故関連損失、特別損失 """
    loss_on_accident_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='事故関連損失、営業活動によるキャッシュ・フロー')
    """ 事故関連損失、営業活動によるキャッシュ・フロー """
    loss_on_accident_payments_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='事故関連損失の支払額、営業活動によるキャッシュ・フロー')
    """ 事故関連損失の支払額、営業活動によるキャッシュ・フロー """
    plant_office_rebuilding_expenses_el: Optional[IxNonFractionPublic] = Field(default=None, description='事業所建替関連費用、特別損失')
    """ 事業所建替関連費用、特別損失 """
    plant_office_rebuilding_expenses_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='事業所建替関連費用、営業活動によるキャッシュ・フロー')
    """ 事業所建替関連費用、営業活動によるキャッシュ・フロー """
    amortization_of_customer_relationship_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='顧客関連資産償却額、営業活動によるキャッシュ・フロー')
    """ 顧客関連資産償却額、営業活動によるキャッシュ・フロー """
    amortization_of_lease_deposits_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='敷金償却、営業活動によるキャッシュ・フロー')
    """ 敷金償却、営業活動によるキャッシュ・フロー """
    customer_related_asset_amortization_expense: Optional[IxNonFractionPublic] = Field(default=None, description='顧客関連資産償却額')
    """ 顧客関連資産償却額 """
    increase_decrease_in_other_current_assets_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='その他流動資産の増減額（△は増加）、営業活動によるキャッシュ・フロー')
    """ その他流動資産の増減額（△は増加）、営業活動によるキャッシュ・フロー """
    loss_due_to_insurance_contract_change_noe: Optional[IxNonFractionPublic] = Field(default=None, description='保険契約変更による損失、営業外費用')
    """ 保険契約変更による損失、営業外費用 """
    loss_due_to_insurance_contract_change_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='保険契約変更による損失、営業活動によるキャッシュ・フロー')
    """ 保険契約変更による損失、営業活動によるキャッシュ・フロー """
    refunds_due_to_changes_in_insurance_contract_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='保険契約変更による返戻額、投資活動によるキャッシュ・フロー')
    """ 保険契約変更による返戻額、投資活動によるキャッシュ・フロー """
    refunds_due_to_changes_in_insurance_contract_noi: Optional[IxNonFractionPublic] = Field(default=None, description='保険契約変更による返戻金、営業外収益')
    """ 保険契約変更による返戻金、営業外収益 """
    refunds_due_to_changes_in_insurance_contract_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='保険契約変更による返戻金、営業活動によるキャッシュ・フロー')
    """ 保険契約変更による返戻金、営業活動によるキャッシュ・フロー """
    transfer_cost_from_sales_of_assets_for_rent_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='賃貸資産の売却による原価振替高、営業活動によるキャッシュ・フロー')
    """ 賃貸資産の売却による原価振替高、営業活動によるキャッシュ・フロー """
    allowance_for_investment_evaluation_ioa: Optional[IxNonFractionPublic] = Field(default=None, description='投資評価引当金、投資その他の資産')
    """ 投資評価引当金、投資その他の資産 """
    allowance_for_investment_loss_ncl: Optional[IxNonFractionPublic] = Field(default=None, description='投資損失引当金、固定負債')
    """ 投資損失引当金、固定負債 """
    impairment_losses_segment_information: Optional[IxNonFractionPublic] = Field(default=None, description='減損損失、セグメント情報')
    """ 減損損失、セグメント情報 """
    information_system_cost_sga: Optional[IxNonFractionPublic] = Field(default=None, description='情報システム費、販売費及び一般管理費')
    """ 情報システム費、販売費及び一般管理費 """
    provision_of_allowance_for_investment_evaluation_el: Optional[IxNonFractionPublic] = Field(default=None, description='投資評価引当金繰入額、特別損失')
    """ 投資評価引当金繰入額、特別損失 """
    collection_of_lease_receivables_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='リース債権の回収による収入、投資活動によるキャッシュ・フロー')
    """ リース債権の回収による収入、投資活動によるキャッシュ・フロー """
    proceeds_from_collection_of_long_term_accounts_receivable_other_inv_cf_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='長期未収入金の回収による収入、投資活動によるキャッシュ・フロー')
    """ 長期未収入金の回収による収入、投資活動によるキャッシュ・フロー """
    cost_of_new_banknote_support_el: Optional[IxNonFractionPublic] = Field(default=None, description='新紙幣対応費用、特別損失')
    """ 新紙幣対応費用、特別損失 """
    treasury_stock_payment_of_stock_ownership_plan_trust_changes_of_items_during_period: Optional[IxNonFractionPublic] = Field(default=None, description='株式給付信託による自己株式の交付、当期変動額')
    """ 株式給付信託による自己株式の交付、当期変動額 """
    increase_decrease_in_long_term_unearned_revenue_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='長期前受収益の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 長期前受収益の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    rent_expenses_of_real_estate_for_investment_noe: Optional[IxNonFractionPublic] = Field(default=None, description='投資不動産賃貸費用、営業外費用')
    """ 投資不動産賃貸費用、営業外費用 """
    increase_decrease_in_provision_for_coupon_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='クーポン引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ クーポン引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    provision_for_coupon_certificates_cl: Optional[IxNonFractionPublic] = Field(default=None, description='クーポン引当金、流動負債')
    """ クーポン引当金、流動負債 """
    settlement_income_noi: Optional[IxNonFractionPublic] = Field(default=None, description='受取和解金、営業外収益')
    """ 受取和解金、営業外収益 """
    customer_related_assets_ia: Optional[IxNonFractionPublic] = Field(default=None, description='顧客関連資産、無形固定資産')
    """ 顧客関連資産、無形固定資産 """
    advances_received_on_uncompleted_construction_contracts_and_others_cns: Optional[IxNonFractionPublic] = Field(default=None, description='未成工事受入金等、建設業')
    """ 未成工事受入金等、建設業 """
    prepayment_guarantee_fee_noe: Optional[IxNonFractionPublic] = Field(default=None, description='前払金保証料、営業外費用')
    """ 前払金保証料、営業外費用 """
    gain_on_forgiveness_of_debts_noi: Optional[IxNonFractionPublic] = Field(default=None, description='債務免除益、営業外収益')
    """ 債務免除益、営業外収益 """
    cancellation_penalty_of_rent_agreement: Optional[IxNonFractionPublic] = Field(default=None, description='賃貸借契約解約違約金、営業外費用')
    """ 賃貸借契約解約違約金、営業外費用 """
    current_portion_of_account_receivable_longterm: Optional[IxNonFractionPublic] = Field(default=None, description='1年内回収予定の長期繰延営業債権')
    """ 1年内回収予定の長期繰延営業債権 """
    income_taxes_income_taxes: Optional[IxNonFractionPublic] = Field(default=None, description='法人税等、法人税等')
    """ 法人税等、法人税等 """
    long_term_deferred_accounts_receivable: Optional[IxNonFractionPublic] = Field(default=None, description='長期繰延営業債権')
    """ 長期繰延営業債権 """
    loss_on_retirement_of_noncurrent_assets_at_company_operated_restaurants_noe: Optional[IxNonFractionPublic] = Field(default=None, description='店舗用固定資産除却損、営業外費用')
    """ 店舗用固定資産除却損、営業外費用 """
    provision_for_bonuses_non_current_ncl: Optional[IxNonFractionPublic] = Field(default=None, description='賞与引当金、固定負債')
    """ 賞与引当金、固定負債 """
    provision_for_directors_bonuses_ncl: Optional[IxNonFractionPublic] = Field(default=None, description='役員賞与引当金、固定負債')
    """ 役員賞与引当金、固定負債 """
    reserve_for_loss_on_disposal_of_inventories_cl: Optional[IxNonFractionPublic] = Field(default=None, description='棚卸資産処分損失引当金、流動負債')
    """ 棚卸資産処分損失引当金、流動負債 """
    long_term_account_receivable_ioa: Optional[IxNonFractionPublic] = Field(default=None, description='長期営業債権、投資その他の資産')
    """ 長期営業債権、投資その他の資産 """
    stay_credit_ioa: Optional[IxNonFractionPublic] = Field(default=None, description='長期滞留債権、投資その他の資産')
    """ 長期滞留債権、投資その他の資産 """
    theft_loss_el: Optional[IxNonFractionPublic] = Field(default=None, description='盗難損失、特別損失')
    """ 盗難損失、特別損失 """
    cryptocurrency_valuation_loss_noe: Optional[IxNonFractionPublic] = Field(default=None, description='暗号資産評価損、営業外費用')
    """ 暗号資産評価損、営業外費用 """
    provision_for_loss_on_guarantees_noe: Optional[IxNonFractionPublic] = Field(default=None, description='債務保証損失引当金繰入額、営業外費用')
    """ 債務保証損失引当金繰入額、営業外費用 """
    accounts_receivable_from_completed_construction_contracts_and_contract_assets_cns: Optional[IxNonFractionPublic] = Field(default=None, description='完成工事未収入金及び契約資産')
    """ 完成工事未収入金及び契約資産 """
    consumption_taxes_for_prior_periods_ei: Optional[IxNonFractionPublic] = Field(default=None, description='過年度消費税等、特別利益')
    """ 過年度消費税等、特別利益 """
    provision_for_loss_on_lease_contracts_cl: Optional[IxNonFractionPublic] = Field(default=None, description='賃借契約損失引当金、流動負債')
    """ 賃借契約損失引当金、流動負債 """
    provision_for_loss_on_lease_contracts_ncl: Optional[IxNonFractionPublic] = Field(default=None, description='賃借契約損失引当金、固定負債')
    """ 賃借契約損失引当金、固定負債 """
    adjustment_of_hyperinflation_cce: Optional[IxNonFractionPublic] = Field(default=None, description='超インフレの調整額、現金及び現金同等物')
    """ 超インフレの調整額、現金及び現金同等物 """
    loss_on_the_net_monetary_position_noe: Optional[IxNonFractionPublic] = Field(default=None, description='正味貨幣持高に関する損失、営業外費用')
    """ 正味貨幣持高に関する損失、営業外費用 """
    loss_on_the_net_monetary_position_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='正味貨幣持高に関する損失、営業活動によるキャッシュ・フロー')
    """ 正味貨幣持高に関する損失、営業活動によるキャッシュ・フロー """
    long_term_advance_payments_ioa: Optional[IxNonFractionPublic] = Field(default=None, description='長期前渡金、投資その他の資産')
    """ 長期前渡金、投資その他の資産 """
    deposits_received_from_silent_partnership_ncl: Optional[IxNonFractionPublic] = Field(default=None, description='匿名組合出資預り金、固定負債')
    """ 匿名組合出資預り金、固定負債 """
    current_portion_of_convertible_bond_type_bonds_with_share_acquisition_rights_cl: Optional[IxNonFractionPublic] = Field(default=None, description='1年内償還予定の転換社債型新株予約権付社債、流動負債')
    """ 1年内償還予定の転換社債型新株予約権付社債、流動負債 """
    idle_asset_expenses_noe: Optional[IxNonFractionPublic] = Field(default=None, description='遊休資産諸費用、営業外費用')
    """ 遊休資産諸費用、営業外費用 """
    amortization_of_patent_right_noe: Optional[IxNonFractionPublic] = Field(default=None, description='特許権償却、営業外費用')
    """ 特許権償却、営業外費用 """
    loss_on_transfer_of_stocks_of_subsidiaries_and_affiliates_el: Optional[IxNonFractionPublic] = Field(default=None, description='関係会社株式譲渡損、特別損失')
    """ 関係会社株式譲渡損、特別損失 """
    loss_on_valuation_of_software_el: Optional[IxNonFractionPublic] = Field(default=None, description='ソフトウエア評価損、特別損失')
    """ ソフトウエア評価損、特別損失 """
    provision_of_the_reserve_for_capital_loss_of_related_companies_el: Optional[IxNonFractionPublic] = Field(default=None, description='関係会社株式譲渡損失引当金繰入額、特別損失')
    """ 関係会社株式譲渡損失引当金繰入額、特別損失 """
    provision_for_head_office_relocation_expenses_cl: Optional[IxNonFractionPublic] = Field(default=None, description='本社移転費用引当金、流動負債')
    """ 本社移転費用引当金、流動負債 """
    compensation_expenses_el: Optional[IxNonFractionPublic] = Field(default=None, description='支払経済補償金、特別損失')
    """ 支払経済補償金、特別損失 """
    accounts_receivable_trade_and_contract_assets_ca: Optional[IxNonFractionPublic] = Field(default=None, description='売掛金及び契約資産、流動資産')
    """ 売掛金及び契約資産、流動資産 """
    adjustment_of_payment_noe: Optional[IxNonFractionPublic] = Field(default=None, description='支払精算金、営業外費用')
    """ 支払精算金、営業外費用 """
    transfer_restrictions_stocks_belonging_to_expenditure_related_noe: Optional[IxNonFractionPublic] = Field(default=None, description='譲渡制限付株式関連費用、営業外費用')
    """ 譲渡制限付株式関連費用、営業外費用 """
    consumption_tax_difference_noi: Optional[IxNonFractionPublic] = Field(default=None, description='消費税差額、営業外収益')
    """ 消費税差額、営業外収益 """
    cost_of_real_estate_rental_income_noe: Optional[IxNonFractionPublic] = Field(default=None, description='家賃原価、営業外費用')
    """ 家賃原価、営業外費用 """
    guarantee_deposited: Optional[IxNonFractionPublic] = Field(default=None, description='預り保証金')
    """ 預り保証金 """
    loss_from_investment_partnerships_noe: Optional[IxNonFractionPublic] = Field(default=None, description='投資事業組合損失、営業外費用')
    """ 投資事業組合損失、営業外費用 """
    real_estate_rental_income_noi: Optional[IxNonFractionPublic] = Field(default=None, description='家賃収入、営業外収益')
    """ 家賃収入、営業外収益 """
    security_and_lease_deposits_paid_ioa: Optional[IxNonFractionPublic] = Field(default=None, description='差入保証金・敷金、投資その他の資産')
    """ 差入保証金・敷金、投資その他の資産 """
    income_from_point_cord_noi: Optional[IxNonFractionPublic] = Field(default=None, description='ポイント収入額、営業外収益')
    """ ポイント収入額、営業外収益 """
    business_expenses: Optional[IxNonFractionPublic] = Field(default=None, description='事業費用')
    """ 事業費用 """
    business_revenues: Optional[IxNonFractionPublic] = Field(default=None, description='事業収益')
    """ 事業収益 """
    business_structural_reform_expenses_el: Optional[IxNonFractionPublic] = Field(default=None, description='事業構造改革費用、特別損失')
    """ 事業構造改革費用、特別損失 """
    provision_for_business_restructuring_cl: Optional[IxNonFractionPublic] = Field(default=None, description='事業構造改革引当金、流動負債')
    """ 事業構造改革引当金、流動負債 """
    research_and_development_revenues_rev_oa: Optional[IxNonFractionPublic] = Field(default=None, description='研究開発事業収益、営業活動による収益')
    """ 研究開発事業収益、営業活動による収益 """
    right_of_use_asset_ppe: Optional[IxNonFractionPublic] = Field(default=None, description='使用権資産、有形固定資産')
    """ 使用権資産、有形固定資産 """
    plant_shutsdown_related_costs_noe: Optional[IxNonFractionPublic] = Field(default=None, description='操業停止関連費用、営業外費用')
    """ 操業停止関連費用、営業外費用 """
    provision_for_loss_on_subleases_cl: Optional[IxNonFractionPublic] = Field(default=None, description='転貸損失引当金、流動負債')
    """ 転貸損失引当金、流動負債 """
    provision_for_loss_on_subleases_ncl: Optional[IxNonFractionPublic] = Field(default=None, description='転貸損失引当金、固定負債')
    """ 転貸損失引当金、固定負債 """
    refund_liabilities_cl: Optional[IxNonFractionPublic] = Field(default=None, description='返金負債、流動負債')
    """ 返金負債、流動負債 """
    restoration_contribution_income_noi: Optional[IxNonFractionPublic] = Field(default=None, description='原状回復負担金等収入、営業外収益')
    """ 原状回復負担金等収入、営業外収益 """
    non_operating_commission_fee_noe: Optional[IxNonFractionPublic] = Field(default=None, description='営業外支払手数料、営業外費用')
    """ 営業外支払手数料、営業外費用 """
    revenue_from_research_and_development_rev_oa: Optional[IxNonFractionPublic] = Field(default=None, description='研究開発等収入、売上高')
    """ 研究開発等収入、売上高 """
    gain_on_net_monetary_position_noi: Optional[IxNonFractionPublic] = Field(default=None, description='正味貨幣持高に係る利得、営業外収益')
    """ 正味貨幣持高に係る利得、営業外収益 """
    loss_on_net_monetary_position_noe: Optional[IxNonFractionPublic] = Field(default=None, description='正味貨幣持高に係る損失、営業外費用')
    """ 正味貨幣持高に係る損失、営業外費用 """
    revenue_advertising_noi: Optional[IxNonFractionPublic] = Field(default=None, description='広告収入、営業外収益')
    """ 広告収入、営業外収益 """
    a_recall_related_loss_el: Optional[IxNonFractionPublic] = Field(default=None, description='製品回収関連損失、特別損失')
    """ 製品回収関連損失、特別損失 """
    reserve_for_losses_related_to_product_recall_cl: Optional[IxNonFractionPublic] = Field(default=None, description='製品回収関連損失引当金、流動負債')
    """ 製品回収関連損失引当金、流動負債 """
    customer_relation_assets: Optional[IxNonFractionPublic] = Field(default=None, description='顧客関係資産')
    """ 顧客関係資産 """
    provision_for_sales_return: Optional[IxNonFractionPublic] = Field(default=None, description='損害賠償引当金')
    """ 損害賠償引当金 """
    refund_liability: Optional[IxNonFractionPublic] = Field(default=None, description='返金負債')
    """ 返金負債 """
    a_product_repair_reserve_fund_cl: Optional[IxNonFractionPublic] = Field(default=None, description='製品改修引当金、流動負債')
    """ 製品改修引当金、流動負債 """
    legal_expenses_noe: Optional[IxNonFractionPublic] = Field(default=None, description='支払報酬、営業外費用')
    """ 支払報酬、営業外費用 """
    loss_on_extinguishment_share_based_compensation_expenses_noe: Optional[IxNonFractionPublic] = Field(default=None, description='株式報酬費用消滅損、営業外費用')
    """ 株式報酬費用消滅損、営業外費用 """
    refunds_on_prior_periods_dividends_income_noi: Optional[IxNonFractionPublic] = Field(default=None, description='受取返還金、営業外収益')
    """ 受取返還金、営業外収益 """
    compensation_for_absence_from_work_to_employee: Optional[IxNonFractionPublic] = Field(default=None, description='従業員休業補償損失、特別損失')
    """ 従業員休業補償損失、特別損失 """
    other_revenue_segment: Optional[IxNonFractionPublic] = Field(default=None, description='その他の収益、セグメント')
    """ その他の収益、セグメント """
    revenue_from_contracts_with_customers_segment: Optional[IxNonFractionPublic] = Field(default=None, description='顧客との契約から生じる収益、セグメント')
    """ 顧客との契約から生じる収益、セグメント """
    sales_compensation_noi: Optional[IxNonFractionPublic] = Field(default=None, description='営業補償金、営業外収益')
    """ 営業補償金、営業外収益 """
    services_at_transferred_at_a_point_in_time: Optional[IxNonFractionPublic] = Field(default=None, description='一時点で移転されるサービス')
    """ 一時点で移転されるサービス """
    services_transferred_over_time: Optional[IxNonFractionPublic] = Field(default=None, description='一定の期間にわたり移転されるサービス')
    """ 一定の期間にわたり移転されるサービス """
    special_survey_costs_etc_el: Optional[IxNonFractionPublic] = Field(default=None, description='特別調査費用等、特別損失')
    """ 特別調査費用等、特別損失 """
    cost_of_electricity_sales_noe: Optional[IxNonFractionPublic] = Field(default=None, description='売電原価、営業外費用')
    """ 売電原価、営業外費用 """
    rental_income_from_employees_buildings_noi: Optional[IxNonFractionPublic] = Field(default=None, description='従業員受取家賃、営業外収益')
    """ 従業員受取家賃、営業外収益 """
    burden_charge_for_development_noi: Optional[IxNonFractionPublic] = Field(default=None, description='開発負担金収入、営業外収益')
    """ 開発負担金収入、営業外収益 """
    land_use_rights_ia: Optional[IxNonFractionPublic] = Field(default=None, description='土地使用権、無形固定資産')
    """ 土地使用権、無形固定資産 """
    loss_on_cancellation_of_membership_el: Optional[IxNonFractionPublic] = Field(default=None, description='会員権解約損、特別損失')
    """ 会員権解約損、特別損失 """
    post_retirement_benefits_payable_for_directors_ncl: Optional[IxNonFractionPublic] = Field(default=None, description='役員退職慰労未払金、固定負債')
    """ 役員退職慰労未払金、固定負債 """
    decrease_increase_in_money_held_in_trust_for_purchase_of_treasury_stock_fin_cf: Optional[IxNonFractionPublic] = Field(default=None, description='自己株式取得のための金銭の信託の増減額（△は増加）、財務活動によるキャッシュ・フロー')
    """ 自己株式取得のための金銭の信託の増減額（△は増加）、財務活動によるキャッシュ・フロー """
    decrease_increase_in_trade_receivables_and_contract_assets_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='売上債権及び契約資産の増減額（△は増加）、営業活動によるキャッシュ・フロー')
    """ 売上債権及び契約資産の増減額（△は増加）、営業活動によるキャッシュ・フロー """
    insurance_income_noib: Optional[IxNonFractionPublic] = Field(default=None, description='保険収入、営業外収益')
    """ 保険収入、営業外収益 """
    loss_on_retirement_of_intangible_assets_el: Optional[IxNonFractionPublic] = Field(default=None, description='無形固定資産除却損、特別損失')
    """ 無形固定資産除却損、特別損失 """
    loss_on_sales_and_retirement_of_property_plant_and_equipment_el: Optional[IxNonFractionPublic] = Field(default=None, description='有形固定資産除売却損、特別損失')
    """ 有形固定資産除売却損、特別損失 """
    factory_transfer_expenses_noe: Optional[IxNonFractionPublic] = Field(default=None, description='工場移転費用、営業外費用')
    """ 工場移転費用、営業外費用 """
    compensation_payment_el: Optional[IxNonFractionPublic] = Field(default=None, description='支払補償金、特別損失')
    """ 支払補償金、特別損失 """
    decrease_increase_in_deposit_paid_for_repurchase_of_treasury_stock_fin_cf: Optional[IxNonFractionPublic] = Field(default=None, description='自己株式取得のための預け金の増減額（△は増加）、財務活動によるキャッシュ・フロー')
    """ 自己株式取得のための預け金の増減額（△は増加）、財務活動によるキャッシュ・フロー """
    leasehold_right_ncl: Optional[IxNonFractionPublic] = Field(default=None, description='土地使用権、無形固定資産')
    """ 土地使用権、無形固定資産 """
    gain_on_sales_of_trial_pieces_noi: Optional[IxNonFractionPublic] = Field(default=None, description='試作品等売却代、営業外収益')
    """ 試作品等売却代、営業外収益 """
    borrowing_fee_noe: Optional[IxNonFractionPublic] = Field(default=None, description='借入手数料、営業外費用')
    """ 借入手数料、営業外費用 """
    expenses_for_purchases_of_goods_noe: Optional[IxNonFractionPublic] = Field(default=None, description='物品購入費用、営業外費用')
    """ 物品購入費用、営業外費用 """
    proceeds_from_sales_of_goods_noi: Optional[IxNonFractionPublic] = Field(default=None, description='物品売却収入、営業外収益')
    """ 物品売却収入、営業外収益 """
    rent_expenses_on_real_estate_for_investments_noe: Optional[IxNonFractionPublic] = Field(default=None, description='投資不動産賃貸費用、営業外費用')
    """ 投資不動産賃貸費用、営業外費用 """
    loss_on_overseas_business_noi: Optional[IxNonFractionPublic] = Field(default=None, description='海外事業関連損失、営業外費用')
    """ 海外事業関連損失、営業外費用 """
    loss_on_profit_structure_improvement_in_japan_el: Optional[IxNonFractionPublic] = Field(default=None, description='国内収益構造改善損、特別損失')
    """ 国内収益構造改善損、特別損失 """
    loss_on_profit_structure_improvement_in_overseas_el: Optional[IxNonFractionPublic] = Field(default=None, description='海外収益構造改善損、特別損失')
    """ 海外収益構造改善損、特別損失 """
    relocation_related_losses_el: Optional[IxNonFractionPublic] = Field(default=None, description='移転関連損失、特別損失')
    """ 移転関連損失、特別損失 """
    right_of_use_assets_ia: Optional[IxNonFractionPublic] = Field(default=None, description='使用権資産、無形固定資産')
    """ 使用権資産、無形固定資産 """
    provision_for_management_board_incentive_plan_trust: Optional[IxNonFractionPublic] = Field(default=None, description='役員株式給付引当金')
    """ 役員株式給付引当金 """
    provision_for_stocks_payment: Optional[IxNonFractionPublic] = Field(default=None, description='株式給付引当金')
    """ 株式給付引当金 """
    contract_loss_allowance_ncl: Optional[IxNonFractionPublic] = Field(default=None, description='契約損失引当金、固定負債')
    """ 契約損失引当金、固定負債 """
    contract_loss_el: Optional[IxNonFractionPublic] = Field(default=None, description='契約損失、特別損失')
    """ 契約損失、特別損失 """
    gain_on_reversal_of_allowance_for_contract_loss_ei: Optional[IxNonFractionPublic] = Field(default=None, description='契約損失引当金戻入額、特別利益')
    """ 契約損失引当金戻入額、特別利益 """
    provision_for_loss_on_contract_cl: Optional[IxNonFractionPublic] = Field(default=None, description='契約損失引当金、流動負債')
    """ 契約損失引当金、流動負債 """
    provision_of_allowance_for_contract_loss_el: Optional[IxNonFractionPublic] = Field(default=None, description='契約損失引当金繰入額、特別損失')
    """ 契約損失引当金繰入額、特別損失 """
    rents_noe: Optional[IxNonFractionPublic] = Field(default=None, description='地代家賃、営業外費用')
    """ 地代家賃、営業外費用 """
    gain_on_amortization_of_deposits_received_noi: Optional[IxNonFractionPublic] = Field(default=None, description='預り金償却益、営業外収益')
    """ 預り金償却益、営業外収益 """
    provision_for_loss_on_guarantees_for_rent_cl: Optional[IxNonFractionPublic] = Field(default=None, description='保証履行引当金、流動負債')
    """ 保証履行引当金、流動負債 """
    provision_for_loss_on_related_to_repair_work_cl: Optional[IxNonFractionPublic] = Field(default=None, description='補修工事関連損失引当金、流動負債')
    """ 補修工事関連損失引当金、流動負債 """
    provision_for_loss_on_related_to_repair_work_ncl: Optional[IxNonFractionPublic] = Field(default=None, description='補修工事関連損失引当金、固定負債')
    """ 補修工事関連損失引当金、固定負債 """
    provision_for_loss_on_vacancies_ncl: Optional[IxNonFractionPublic] = Field(default=None, description='空室損失引当金、固定負債')
    """ 空室損失引当金、固定負債 """
    reversal_of_provision_for_loss_on_related_to_repair_work_ei: Optional[IxNonFractionPublic] = Field(default=None, description='補修工事関連損失引当金戻入額、特別利益')
    """ 補修工事関連損失引当金戻入額、特別利益 """
    insurance_income_arose_from_disaster_ei: Optional[IxNonFractionPublic] = Field(default=None, description='災害に伴う受取保険金、特別利益')
    """ 災害に伴う受取保険金、特別利益 """
    trade_and_contract_assets_ca: Optional[IxNonFractionPublic] = Field(default=None, description='売掛金及び契約資産、流動資産')
    """ 売掛金及び契約資産、流動資産 """
    buildings_and_accompanying_facilities_in_trust_net_ppe: Optional[IxNonFractionPublic] = Field(default=None, description='信託建物附属設備（純額）、有形固定資産')
    """ 信託建物附属設備（純額）、有形固定資産 """
    buildings_in_trust_net_ppe: Optional[IxNonFractionPublic] = Field(default=None, description='信託建物（純額）、有形固定資産')
    """ 信託建物（純額）、有形固定資産 """
    earthquake_resistant_construction_expense_el: Optional[IxNonFractionPublic] = Field(default=None, description='耐震工事関連費用、特別損失')
    """ 耐震工事関連費用、特別損失 """
    land_in_trust_ppe: Optional[IxNonFractionPublic] = Field(default=None, description='信託土地、有形固定資産')
    """ 信託土地、有形固定資産 """
    long_term_advance_paid_ioa: Optional[IxNonFractionPublic] = Field(default=None, description='長期立替金、投資その他の資産')
    """ 長期立替金、投資その他の資産 """
    profit_related_to_employment_adjustment_subsides_etc_noi: Optional[IxNonFractionPublic] = Field(default=None, description='雇用調整助成金等、営業外収益')
    """ 雇用調整助成金等、営業外収益 """
    trade_notes_and_accounts_receivable_trade_and_contract_assets_ca: Optional[IxNonFractionPublic] = Field(default=None, description='受取手形、営業未収入金及び契約資産、流動資産')
    """ 受取手形、営業未収入金及び契約資産、流動資産 """
    gain_on_reversal_of_provision_for_loss_on_business_withdrawal_ei: Optional[IxNonFractionPublic] = Field(default=None, description='事業撤退損失引当金戻入額、特別利益')
    """ 事業撤退損失引当金戻入額、特別利益 """
    provision_for_loss_on_business_withdrawal_cl: Optional[IxNonFractionPublic] = Field(default=None, description='事業撤退損失引当金、流動負債')
    """ 事業撤退損失引当金、流動負債 """
    provision_for_loss_on_business_withdrawal_el: Optional[IxNonFractionPublic] = Field(default=None, description='事業撤退損失引当金繰入額、特別損失')
    """ 事業撤退損失引当金繰入額、特別損失 """
    provision_for_noncurrent_assets_removal_cost_cl: Optional[IxNonFractionPublic] = Field(default=None, description='固定資産撤去費用引当金、流動負債')
    """ 固定資産撤去費用引当金、流動負債 """
    provision_for_removal_expenses_of_noncurrent_assets_el: Optional[IxNonFractionPublic] = Field(default=None, description='固定資産撤去費用引当金繰入額、特別損失')
    """ 固定資産撤去費用引当金繰入額、特別損失 """
    investment_partnership_management_fee_noe: Optional[IxNonFractionPublic] = Field(default=None, description='投資事業組合管理費、営業外費用')
    """ 投資事業組合管理費、営業外費用 """
    claims_provable_in_bankruptcy_claims_provable_in_rehabilitation_and_other_ioa: Optional[IxNonFractionPublic] = Field(default=None, description='破産債権等に準ずる債権、投資その他の資産')
    """ 破産債権等に準ずる債権、投資その他の資産 """
    commission_income_noi: Optional[IxNonFractionPublic] = Field(default=None, description='手数料収入、営業外収益')
    """ 手数料収入、営業外収益 """
    compensation_for_damages_received_noi: Optional[IxNonFractionPublic] = Field(default=None, description='受取損害賠償金、営業外収益')
    """ 受取損害賠償金、営業外収益 """
    idle_assets_expense_noe: Optional[IxNonFractionPublic] = Field(default=None, description='遊休資産費用、営業外費用')
    """ 遊休資産費用、営業外費用 """
    material_profit_on_sale_noi: Optional[IxNonFractionPublic] = Field(default=None, description='資材売却益、営業外収益')
    """ 資材売却益、営業外収益 """
    provision_for_building_demolition_expense_ncl: Optional[IxNonFractionPublic] = Field(default=None, description='建物解体費用引当金、固定負債')
    """ 建物解体費用引当金、固定負債 """
    provision_of_allowance_for_building_demolition_expense: Optional[IxNonFractionPublic] = Field(default=None, description='建物解体費用引当金繰入額、特別損失')
    """ 建物解体費用引当金繰入額、特別損失 """
    supporting_expenses_for_subsidiaries_and_affiliates_noe: Optional[IxNonFractionPublic] = Field(default=None, description='関係会社支援費用、営業外費用')
    """ 関係会社支援費用、営業外費用 """
    various_facilities_use_rights_ia: Optional[IxNonFractionPublic] = Field(default=None, description='諸施設利用権、無形固定資産')
    """ 諸施設利用権、無形固定資産 """
    cash_back_income_noi: Optional[IxNonFractionPublic] = Field(default=None, description='キャッシュバック収入、営業外収益')
    """ キャッシュバック収入、営業外収益 """
    past_fiscal_years_consumption_tax_etc_noi: Optional[IxNonFractionPublic] = Field(default=None, description='過年度消費税等、営業外収益')
    """ 過年度消費税等、営業外収益 """
    handicapped_employment_levy_noe: Optional[IxNonFractionPublic] = Field(default=None, description='障害者雇用納付金、営業外費用')
    """ 障害者雇用納付金、営業外費用 """
    loss_on_anti_monopoly_act_el: Optional[IxNonFractionPublic] = Field(default=None, description='独占禁止法関連損失、特別損失')
    """ 独占禁止法関連損失、特別損失 """
    operating_profit_loss_operating_profit_loss: Optional[IxNonFractionPublic] = Field(default=None, description='営業損失（△）、営業利益又は営業損失（△）')
    """ 営業損失（△）、営業利益又は営業損失（△） """
    sales_commission_noi: Optional[IxNonFractionPublic] = Field(default=None, description='販売手数料、営業外収益')
    """ 販売手数料、営業外収益 """
    amortization_of_restricted_stock_remuneration_noe: Optional[IxNonFractionPublic] = Field(default=None, description='譲渡制限付株式報酬償却損、営業外費用')
    """ 譲渡制限付株式報酬償却損、営業外費用 """
    business_revenue: Optional[IxNonFractionPublic] = Field(default=None, description='事業収益')
    """ 事業収益 """
    cost_of_business_revenue: Optional[IxNonFractionPublic] = Field(default=None, description='事業原価')
    """ 事業原価 """
    lecture_s_fee_income_noi: Optional[IxNonFractionPublic] = Field(default=None, description='講演料等収入、営業外収益')
    """ 講演料等収入、営業外収益 """
    subsidy_income_etc_noi: Optional[IxNonFractionPublic] = Field(default=None, description='助成金等収入、営業外収益')
    """ 助成金等収入、営業外収益 """
    total_business_expenses: Optional[IxNonFractionPublic] = Field(default=None, description='事業費用合計')
    """ 事業費用合計 """
    trade_receivables_and_contract_asset_ca: Optional[IxNonFractionPublic] = Field(default=None, description='売掛金及び契約資産、流動資産')
    """ 売掛金及び契約資産、流動資産 """
    transportation_income_noi: Optional[IxNonFractionPublic] = Field(default=None, description='受取運送料、営業外収益')
    """ 受取運送料、営業外収益 """
    gain_on_sales_of_raw_materials_noi: Optional[IxNonFractionPublic] = Field(default=None, description='原材料売却益、営業外収益')
    """ 原材料売却益、営業外収益 """
    loss_on_extinguishment_of_share_based_remuneration_expenses_noe: Optional[IxNonFractionPublic] = Field(default=None, description='株式報酬費用消滅損、営業外費用')
    """ 株式報酬費用消滅損、営業外費用 """
    sales_engineering_expenses_sga: Optional[IxNonFractionPublic] = Field(default=None, description='受注前活動費、販売費及び一般管理費')
    """ 受注前活動費、販売費及び一般管理費 """
    received_incentive_noi: Optional[IxNonFractionPublic] = Field(default=None, description='受取報奨金、営業外収益')
    """ 受取報奨金、営業外収益 """
    goods_transfer_at_a_point_in_time: Optional[IxNonFractionPublic] = Field(default=None, description='一時点で移転される財')
    """ 一時点で移転される財 """
    goods_transfer_over_time: Optional[IxNonFractionPublic] = Field(default=None, description='一定の期間にわたり移転される財')
    """ 一定の期間にわたり移転される財 """
    tender_offer_related_expenses_el: Optional[IxNonFractionPublic] = Field(default=None, description='公開買付関連費用、特別損失')
    """ 公開買付関連費用、特別損失 """
    decrease_increase_in_deposits_paid_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='預け金の増減額（△は増加）、投資活動によるキャッシュ・フロー')
    """ 預け金の増減額（△は増加）、投資活動によるキャッシュ・フロー """
    increase_decrease_in_provision_for_mine_closure_expenses_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='閉山損失引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 閉山損失引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    product_compensation_loss_el: Optional[IxNonFractionPublic] = Field(default=None, description='製品補償損失、特別損失')
    """ 製品補償損失、特別損失 """
    product_compensation_loss_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='製品補償損失、営業活動によるキャッシュ・フロー')
    """ 製品補償損失、営業活動によるキャッシュ・フロー """
    provision_for_mine_closure_expenses_ncl: Optional[IxNonFractionPublic] = Field(default=None, description='閉山損失引当金、固定負債')
    """ 閉山損失引当金、固定負債 """
    business_restructuring_expenses_el: Optional[IxNonFractionPublic] = Field(default=None, description='事業構造改革費用、特別損失')
    """ 事業構造改革費用、特別損失 """
    compensation_for_damage_income_ei: Optional[IxNonFractionPublic] = Field(default=None, description='受取損害賠償金、特別利益')
    """ 受取損害賠償金、特別利益 """
    e00322000_insurance_return_ei: Optional[IxNonFractionPublic] = Field(default=None, description='保険返戻金、特別利益')
    """ 保険返戻金、特別利益 """
    unemployed_capital_cost_noe: Optional[IxNonFractionPublic] = Field(default=None, description='遊休資産費用、営業外費用')
    """ 遊休資産費用、営業外費用 """
    construction_guarantee_fee_noe: Optional[IxNonFractionPublic] = Field(default=None, description='工事保証料、営業外費用')
    """ 工事保証料、営業外費用 """
    accounts_payable_for_construction_contracts_and_other_clcns: Optional[IxNonFractionPublic] = Field(default=None, description='工事未払金等、流動負債、建設業')
    """ 工事未払金等、流動負債、建設業 """
    accounts_receivable_from_completed_construction_contracts_and_other_cns: Optional[IxNonFractionPublic] = Field(default=None, description='完成工事未収入金等、建設業')
    """ 完成工事未収入金等、建設業 """
    cost_of_transportation_business_cos: Optional[IxNonFractionPublic] = Field(default=None, description='運輸事業売上原価、売上原価')
    """ 運輸事業売上原価、売上原価 """
    gross_profit_on_transportation_business_gp: Optional[IxNonFractionPublic] = Field(default=None, description='運輸事業総利益、売上総利益')
    """ 運輸事業総利益、売上総利益 """
    provision_for_loss_on_litigation_noe: Optional[IxNonFractionPublic] = Field(default=None, description='訴訟損失引当金繰入額、営業外費用')
    """ 訴訟損失引当金繰入額、営業外費用 """
    sales_of_transportation_business_net_sales: Optional[IxNonFractionPublic] = Field(default=None, description='運輸事業売上高、売上高')
    """ 運輸事業売上高、売上高 """
    contract_assets_ca: Optional[IxNonFractionPublic] = Field(default=None, description='契約資産、流動資産')
    """ 契約資産、流動資産 """
    patent_enforcement_incom_noi: Optional[IxNonFractionPublic] = Field(default=None, description='特許実施収入、営業外収益')
    """ 特許実施収入、営業外収益 """
    repayments_of_installment_payables_and_lease_obligations_fin_cf: Optional[IxNonFractionPublic] = Field(default=None, description='割賦債務及びリース債務の返済による支出、財務活動によるキャッシュ・フロー')
    """ 割賦債務及びリース債務の返済による支出、財務活動によるキャッシュ・フロー """
    costs_on_real_estate_business_and_other_ca: Optional[IxNonFractionPublic] = Field(default=None, description='不動産事業等支出金、流動資産')
    """ 不動産事業等支出金、流動資産 """
    increase_decrease_in_provision_for_loss_on_real_estate_business_and_other_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='不動産事業等損失引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 不動産事業等損失引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    loss_on_support_to_subsidiaries_el: Optional[IxNonFractionPublic] = Field(default=None, description='子会社支援損、特別損失')
    """ 子会社支援損、特別損失 """
    provision_for_loss_on_real_estate_business_and_other_cl: Optional[IxNonFractionPublic] = Field(default=None, description='不動産事業等損失引当金、流動負債')
    """ 不動産事業等損失引当金、流動負債 """
    increase_decrease_in_net_defined_benefit_asset_or_liability_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='退職給付に係る資産又は負債の増減額、営業活動によるキャッシュ・フロー')
    """ 退職給付に係る資産又は負債の増減額、営業活動によるキャッシュ・フロー """
    notes_and_accounts_receivable_from_completed_construction_contracts_and_contract_assets_cns: Optional[IxNonFractionPublic] = Field(default=None, description='受取手形、完成工事未収入金等及び契約資産、建設業')
    """ 受取手形、完成工事未収入金等及び契約資産、建設業 """
    financial_commission_noe: Optional[IxNonFractionPublic] = Field(default=None, description='金融手数料、営業外費用')
    """ 金融手数料、営業外費用 """
    non_deducted_consumption_tax_noe: Optional[IxNonFractionPublic] = Field(default=None, description='控除対象外消費税等、営業外費用')
    """ 控除対象外消費税等、営業外費用 """
    notes_receivable_accounts_receivable_from_completed_construction_contracts_contract_assets_and_other: Optional[IxNonFractionPublic] = Field(default=None, description='受取手形・完成工事未収入金及び契約資産等')
    """ 受取手形・完成工事未収入金及び契約資産等 """
    provision_for_loss_on_compensation_for_damage_el: Optional[IxNonFractionPublic] = Field(default=None, description='損害補償損失引当金繰入、特別損失')
    """ 損害補償損失引当金繰入、特別損失 """
    license_income_noi: Optional[IxNonFractionPublic] = Field(default=None, description='特許関連収入、営業外収益')
    """ 特許関連収入、営業外収益 """
    animals: Optional[IxNonFractionPublic] = Field(default=None, description='動物')
    """ 動物 """
    commission_expenses_paid_fin_cf: Optional[IxNonFractionPublic] = Field(default=None, description='支払手数料の支払額、財務活動によるキャッシュ・フロー')
    """ 支払手数料の支払額、財務活動によるキャッシュ・フロー """
    head_office_relocation_expenses_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='本社移転費用、営業活動によるキャッシュ・フロー')
    """ 本社移転費用、営業活動によるキャッシュ・フロー """
    loss_on_closing_of_factory_el: Optional[IxNonFractionPublic] = Field(default=None, description='工場閉鎖損失、特別損失')
    """ 工場閉鎖損失、特別損失 """
    payments_for_head_office_relocation_expenses_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='本社移転費用の支払額、営業活動によるキャッシュ・フロー')
    """ 本社移転費用の支払額、営業活動によるキャッシュ・フロー """
    stockpile_storage_revenue_noi: Optional[IxNonFractionPublic] = Field(default=None, description='備蓄保管収入、営業外収益')
    """ 備蓄保管収入、営業外収益 """
    proceeds_from_state_subsidy_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='国庫補助金等の受入による収入、投資活動によるキャッシュ・フロー')
    """ 国庫補助金等の受入による収入、投資活動によるキャッシュ・フロー """
    repayments_of_deposits_received_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='預り敷金の返還による支出、投資活動によるキャッシュ・フロー')
    """ 預り敷金の返還による支出、投資活動によるキャッシュ・フロー """
    bounty_on_establishment_of_new_business_facilities_noi: Optional[IxNonFractionPublic] = Field(default=None, description='企業立地奨励金、営業外収益')
    """ 企業立地奨励金、営業外収益 """
    bounty_on_establishment_of_new_business_facilities_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='企業立地奨励金、営業活動によるキャッシュ・フロー')
    """ 企業立地奨励金、営業活動によるキャッシュ・フロー """
    bounty_on_establishment_of_new_business_facilities_received_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='企業立地奨励金の受取額、営業活動によるキャッシュ・フロー')
    """ 企業立地奨励金の受取額、営業活動によるキャッシュ・フロー """
    provision_for_noncurrent_assets_removal_cost_ncl: Optional[IxNonFractionPublic] = Field(default=None, description='固定資産撤去費用引当金、固定負債')
    """ 固定資産撤去費用引当金、固定負債 """
    removal_loss_of_property_plant_and_equipment_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='固定資産撤去に伴う支出、投資活動によるキャッシュ・フロー')
    """ 固定資産撤去に伴う支出、投資活動によるキャッシュ・フロー """
    compensation_income_received_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='受取補償金の受取額、営業活動によるキャッシュ・フロー')
    """ 受取補償金の受取額、営業活動によるキャッシュ・フロー """
    increase_decrease_in_provision_for_officers_retirement_benefits_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='執行役員退職慰労引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 執行役員退職慰労引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    provision_for_officer_retirement_benefits: Optional[IxNonFractionPublic] = Field(default=None, description='執行役員退職慰労引当金')
    """ 執行役員退職慰労引当金 """
    disbursement_to_the_hikari_foundation_el: Optional[IxNonFractionPublic] = Field(default=None, description='公益財団法人ひかり協会負担金、特別損失')
    """ 公益財団法人ひかり協会負担金、特別損失 """
    loss_related_to_rebuilding_el: Optional[IxNonFractionPublic] = Field(default=None, description='建替関連損失、特別損失')
    """ 建替関連損失、特別損失 """
    costs_related_to_voluntary_recovery_of_product_el: Optional[IxNonFractionPublic] = Field(default=None, description='製品自主回収関連費用、特別損失')
    """ 製品自主回収関連費用、特別損失 """
    provision_for_restructual_reforms_cl: Optional[IxNonFractionPublic] = Field(default=None, description='構造改革引当金、流動負債')
    """ 構造改革引当金、流動負債 """
    restructuring_expenses_el: Optional[IxNonFractionPublic] = Field(default=None, description='構造改革費用、特別損失')
    """ 構造改革費用、特別損失 """
    restructuring_expenses_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='構造改革費用、営業活動によるキャッシュ・フロー')
    """ 構造改革費用、営業活動によるキャッシュ・フロー """
    decreae_increase_in_deffered_consumer_tax_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='繰延消費税等の増減額（△は増加）、営業活動によるキャッシュ・フロー')
    """ 繰延消費税等の増減額（△は増加）、営業活動によるキャッシュ・フロー """
    expenses_related_to_the_proposed_tender_offer_el: Optional[IxNonFractionPublic] = Field(default=None, description='公開買付提案対応費用、特別損失')
    """ 公開買付提案対応費用、特別損失 """
    tv_exhibition_rights_and_videogram_rights: Optional[IxNonFractionPublic] = Field(default=None, description='映像使用権')
    """ 映像使用権 """
    accumulated_depreciation_assets_for_rent_ppe: Optional[IxNonFractionPublic] = Field(default=None, description='減価償却累計額、賃貸資産、有形固定資産')
    """ 減価償却累計額、賃貸資産、有形固定資産 """
    assets_for_rent_net_ppe: Optional[IxNonFractionPublic] = Field(default=None, description='賃貸資産（純額）、有形固定資産')
    """ 賃貸資産（純額）、有形固定資産 """
    assets_for_rent_ppe: Optional[IxNonFractionPublic] = Field(default=None, description='賃貸資産、有形固定資産')
    """ 賃貸資産、有形固定資産 """
    gain_on_sales_of_scrap_noi: Optional[IxNonFractionPublic] = Field(default=None, description='スクラップ売却収入、営業外収益')
    """ スクラップ売却収入、営業外収益 """
    loss_on_retirement_of_assets_for_rent_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='賃貸資産除却に伴う原価振替額、営業活動によるキャッシュ・フロー')
    """ 賃貸資産除却に伴う原価振替額、営業活動によるキャッシュ・フロー """
    loss_on_sales_of_assets_for_rent_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='賃貸資産売却に伴う原価振替額、営業活動によるキャッシュ・フロー')
    """ 賃貸資産売却に伴う原価振替額、営業活動によるキャッシュ・フロー """
    gain_on_exemption_of_consumption_taxes_noi: Optional[IxNonFractionPublic] = Field(default=None, description='消費税等免税益、営業外収益')
    """ 消費税等免税益、営業外収益 """
    customer_related_assets_of_goodwill_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='顧客関連資産償却額、営業活動によるキャッシュ・フロー')
    """ 顧客関連資産償却額、営業活動によるキャッシュ・フロー """
    loss_on_valuation_of_investment_securities_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='投資有価証券評価損、営業活動によるキャッシュ・フロー')
    """ 投資有価証券評価損、営業活動によるキャッシュ・フロー """
    increase_decrease_in_liquor_taxes_payable_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='未払酒税の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 未払酒税の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    loss_gain_on_sale_of_investments_in_capital_of_subsidiaries_and_associates_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='関係会社出資金売却損益（△は益）、営業活動によるキャッシュ・フロー')
    """ 関係会社出資金売却損益（△は益）、営業活動によるキャッシュ・フロー """
    loss_on_sale_of_investments_in_capital_of_subsidiaries_and_associates_el: Optional[IxNonFractionPublic] = Field(default=None, description='関係会社出資金売却損、特別損失')
    """ 関係会社出資金売却損、特別損失 """
    payments_for_sales_of_investments_in_capital_of_subsidiaries_and_affiliates_resulting_in_change_in_scope_of_consolidation_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='連結の範囲の変更を伴う関係会社出資金の売却による支出、投資活動によるキャッシュ・フロー')
    """ 連結の範囲の変更を伴う関係会社出資金の売却による支出、投資活動によるキャッシュ・フロー """
    increase_decrease_in_a_product_repair_reserve_fund_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='製品改修引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 製品改修引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    refunded_taxes_noi: Optional[IxNonFractionPublic] = Field(default=None, description='還付税金、営業外収益')
    """ 還付税金、営業外収益 """
    refunded_taxes_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='還付税金、営業活動によるキャッシュ・フロー')
    """ 還付税金、営業活動によるキャッシュ・フロー """
    cash_over_and_short_noe: Optional[IxNonFractionPublic] = Field(default=None, description='現金過不足、営業外費用')
    """ 現金過不足、営業外費用 """
    payments_for_repair_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='補修費用に伴う支払額、営業活動によるキャッシュ・フロー')
    """ 補修費用に伴う支払額、営業活動によるキャッシュ・フロー """
    borrowing_related_expenses_losses_noe: Optional[IxNonFractionPublic] = Field(default=None, description='借入関係費用、営業外費用')
    """ 借入関係費用、営業外費用 """
    advances_received_deposits_noe: Optional[IxNonFractionPublic] = Field(default=None, description='前受金保証料、営業外費用')
    """ 前受金保証料、営業外費用 """
    automotive_safety_systems_business_division_rev_oa: Optional[IxNonFractionPublic] = Field(default=None, description='自動車安全部品、営業活動による収益')
    """ 自動車安全部品、営業活動による収益 """
    disaster_prevention_division_rev_oa: Optional[IxNonFractionPublic] = Field(default=None, description='防災、営業活動による収益')
    """ 防災、営業活動による収益 """
    industrial_materials_division_rev_oa: Optional[IxNonFractionPublic] = Field(default=None, description='産業資材、営業活動による収益')
    """ 産業資材、営業活動による収益 """
    loss_on_product_compensation_el: Optional[IxNonFractionPublic] = Field(default=None, description='製品補償対策費、特別損失')
    """ 製品補償対策費、特別損失 """
    other_businesses_division_rev_oa: Optional[IxNonFractionPublic] = Field(default=None, description='その他')
    """ その他 """
    other_revenue: Optional[IxNonFractionPublic] = Field(default=None, description='その他の収益')
    """ その他の収益 """
    paltem_division_rev_oa: Optional[IxNonFractionPublic] = Field(default=None, description='パルテム、営業活動による収益')
    """ パルテム、営業活動による収益 """
    product_warranty_loss_el: Optional[IxNonFractionPublic] = Field(default=None, description='製品保証損失、特別損失')
    """ 製品保証損失、特別損失 """
    revenue_from_contracts_with_customers_rev_oa: Optional[IxNonFractionPublic] = Field(default=None, description='顧客との契約から生じる収益、営業活動による収益')
    """ 顧客との契約から生じる収益、営業活動による収益 """
    dismantlement_related_expenses_el: Optional[IxNonFractionPublic] = Field(default=None, description='解体撤去関連費用、特別損失')
    """ 解体撤去関連費用、特別損失 """
    good_output_ca: Optional[IxNonFractionPublic] = Field(default=None, description='完成品、流動資産')
    """ 完成品、流動資産 """
    payment_of_demolition_and_removal_costs_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='解体撤去関連費用の支払額、営業活動によるキャッシュフロー')
    """ 解体撤去関連費用の支払額、営業活動によるキャッシュフロー """
    payments_for_factory_transfer_expenses_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='工場移転費用の支払額、営業活動によるキャッシュ・フロー')
    """ 工場移転費用の支払額、営業活動によるキャッシュ・フロー """
    contents_assets_ca: Optional[IxNonFractionPublic] = Field(default=None, description='コンテンツ資産、流動資産')
    """ コンテンツ資産、流動資産 """
    provision_for_share_based_compensation: Optional[IxNonFractionPublic] = Field(default=None, description='株式報酬引当金')
    """ 株式報酬引当金 """
    revenue_from_unused_point_by_withdrawal_from_membership_noi: Optional[IxNonFractionPublic] = Field(default=None, description='退会者未使用課金収益、営業外収益')
    """ 退会者未使用課金収益、営業外収益 """
    work_in_process_contents_assets_ca: Optional[IxNonFractionPublic] = Field(default=None, description='仕掛コンテンツ資産、流動資産')
    """ 仕掛コンテンツ資産、流動資産 """
    directors_share_based_allowances_ncl: Optional[IxNonFractionPublic] = Field(default=None, description='役員株式報酬引当金、固定負債')
    """ 役員株式報酬引当金、固定負債 """
    directors_share_based_allowances_sga: Optional[IxNonFractionPublic] = Field(default=None, description='役員株式報酬引当金繰入額、販売費及び一般管理費')
    """ 役員株式報酬引当金繰入額、販売費及び一般管理費 """
    increase_decrease_in_directors_share_based_allowances_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='役員株式報酬引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 役員株式報酬引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    contents_assets_ia: Optional[IxNonFractionPublic] = Field(default=None, description='コンテンツ資産、無形固定資産')
    """ コンテンツ資産、無形固定資産 """
    money_held_in_trust_ioa: Optional[IxNonFractionPublic] = Field(default=None, description='金銭の信託、投資その他の資産')
    """ 金銭の信託、投資その他の資産 """
    proceeds_from_disposal_of_treasury_shares_from_exercise_of_share_acquisition_rights_fin_cf: Optional[IxNonFractionPublic] = Field(default=None, description='新株予約権の行使による自己株式の処分による収入、財務活動によるキャッシュ・フロー')
    """ 新株予約権の行使による自己株式の処分による収入、財務活動によるキャッシュ・フロー """
    proceeds_from_long_term_deposits_received_fin_cf: Optional[IxNonFractionPublic] = Field(default=None, description='長期預り金の受入による収入、財務活動によるキャッシュ・フロー')
    """ 長期預り金の受入による収入、財務活動によるキャッシュ・フロー """
    accounts_receivable_and_contract_assets_ca: Optional[IxNonFractionPublic] = Field(default=None, description='売掛金及び契約資産、流動資産')
    """ 売掛金及び契約資産、流動資産 """
    office_relocation_expenses_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='事務所移転費用、営業活動によるキャッシュ・フロー')
    """ 事務所移転費用、営業活動によるキャッシュ・フロー """
    increase_decrease_in_refund_liability_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='返金負債の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 返金負債の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    trial_products_income_noi: Optional[IxNonFractionPublic] = Field(default=None, description='試作品売却収入、営業外収益')
    """ 試作品売却収入、営業外収益 """
    gain_on_reversal_of_asset_retirement_obligations_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='資産除去債務戻入益、営業活動によるキャッシュ・フロー')
    """ 資産除去債務戻入益、営業活動によるキャッシュ・フロー """
    gain_on_sale_of_crypto_assets_noi: Optional[IxNonFractionPublic] = Field(default=None, description='暗号資産売却益、営業外収益')
    """ 暗号資産売却益、営業外収益 """
    loss_gain_on_sale_of_crypto_assets_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='暗号資産売却益、営業活動によるキャッシュ・フロー')
    """ 暗号資産売却益、営業活動によるキャッシュ・フロー """
    loss_gain_on_valuation_of_cryptocurrency_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='暗号資産評価損益（△は益）、営業活動によるキャッシュ・フロー')
    """ 暗号資産評価損益（△は益）、営業活動によるキャッシュ・フロー """
    loss_on_liquidation_of_investment_securities_el: Optional[IxNonFractionPublic] = Field(default=None, description='投資有価証券清算損、特別損失')
    """ 投資有価証券清算損、特別損失 """
    loss_on_liquidation_of_investment_securities_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='投資有価証券清算損、営業活動によるキャッシュ・フロー')
    """ 投資有価証券清算損、営業活動によるキャッシュ・フロー """
    loss_on_valuation_of_crypto_assets_noe: Optional[IxNonFractionPublic] = Field(default=None, description='暗号資産評価損、営業外費用')
    """ 暗号資産評価損、営業外費用 """
    proceeds_from_sales_of_crypto_assets_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='暗号資産の売却による収入、投資活動によるキャッシュ・フロー')
    """ 暗号資産の売却による収入、投資活動によるキャッシュ・フロー """
    gain_on_reversal_of_asset_retirement_obligations_noi: Optional[IxNonFractionPublic] = Field(default=None, description='資産除去債務戻入益、営業外収益')
    """ 資産除去債務戻入益、営業外収益 """
    reserve_for_implementation_of_environmental_and_safety_arrangement_ncl: Optional[IxNonFractionPublic] = Field(default=None, description='環境安全整備引当金、固定負債')
    """ 環境安全整備引当金、固定負債 """
    reserve_for_implementation_of_environmental_and_safety_arrangements_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='環境安全整備引当金の増減額(△は減少)、営業活動によるキャッシュ・フロー')
    """ 環境安全整備引当金の増減額(△は減少)、営業活動によるキャッシュ・フロー """
    cost_during_the_suspension_of_plant_operation_noe: Optional[IxNonFractionPublic] = Field(default=None, description='操業休止等経費、営業外費用')
    """ 操業休止等経費、営業外費用 """
    payments_for_issuance_of_bonds_fin_cf: Optional[IxNonFractionPublic] = Field(default=None, description='社債の発行による支出、財務活動によるキャッシュ・フロー')
    """ 社債の発行による支出、財務活動によるキャッシュ・フロー """
    tender_offer_related_expenses_noe: Optional[IxNonFractionPublic] = Field(default=None, description='公開買付関連費用、営業外費用')
    """ 公開買付関連費用、営業外費用 """
    proceeds_from_cancellation_of_life_insurance_funds_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='生命保険積立金の解約による収入、投資活動によるキャッシュ・フロー')
    """ 生命保険積立金の解約による収入、投資活動によるキャッシュ・フロー """
    purchase_of_insurance_funds: Optional[IxNonFractionPublic] = Field(default=None, description='生命保険積立金の積立による支出')
    """ 生命保険積立金の積立による支出 """
    loss_on_closing_of_plant_el: Optional[IxNonFractionPublic] = Field(default=None, description='工場閉鎖損失、特別損失')
    """ 工場閉鎖損失、特別損失 """
    loss_on_compensation_of_claims_noe: Optional[IxNonFractionPublic] = Field(default=None, description='クレーム弁償損、営業外費用')
    """ クレーム弁償損、営業外費用 """
    increase_decrease_in_provision_for_loss_compensation_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='損害補償損失引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 損害補償損失引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    provision_for_loss_compensation_cl: Optional[IxNonFractionPublic] = Field(default=None, description='損害補償損失引当金、流動負債')
    """ 損害補償損失引当金、流動負債 """
    provision_for_loss_compensation_noe: Optional[IxNonFractionPublic] = Field(default=None, description='損害補償損失引当金繰入額、営業外費用')
    """ 損害補償損失引当金繰入額、営業外費用 """
    personnel_expenses_for_seconded_employees_noe: Optional[IxNonFractionPublic] = Field(default=None, description='出向者労務費差額負担、営業外費用')
    """ 出向者労務費差額負担、営業外費用 """
    fixed_asset_removal_costs_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='固定資産撤去費用、営業活動によるキャッシュ・フロー')
    """ 固定資産撤去費用、営業活動によるキャッシュ・フロー """
    increase_decrease_in_refund_liabilities_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='返金負債の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 返金負債の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    loss_on_removal_of_noncurrent_assets_noe: Optional[IxNonFractionPublic] = Field(default=None, description='固定資産撤去費用、営業外費用')
    """ 固定資産撤去費用、営業外費用 """
    provision_for_assets_removal_ncl_liabilities: Optional[IxNonFractionPublic] = Field(default=None, description='固定資産撤去引当金、固定負債、負債の部')
    """ 固定資産撤去引当金、固定負債、負債の部 """
    repayments_of_long_term_deposits_received_fin_cf: Optional[IxNonFractionPublic] = Field(default=None, description='長期預り金の返還による支出、財務活動によるキャッシュ・フロー')
    """ 長期預り金の返還による支出、財務活動によるキャッシュ・フロー """
    account_receivable_medical_income_ca: Optional[IxNonFractionPublic] = Field(default=None, description='調剤報酬等購入債権、流動資産')
    """ 調剤報酬等購入債権、流動資産 """
    account_receivable_monetization_of_receivable_ca: Optional[IxNonFractionPublic] = Field(default=None, description='債権売却未収入金、流動資産')
    """ 債権売却未収入金、流動資産 """
    decrease_increase_in_account_receivable_medical_income_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='調剤報酬等購入債権の増減額（△は増加）、営業活動によるキャッシュフロー')
    """ 調剤報酬等購入債権の増減額（△は増加）、営業活動によるキャッシュフロー """
    decrease_increase_in_account_receivable_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='債権売却未収入金の増減額（△は増加）、営業活動によるキャッシュフロー')
    """ 債権売却未収入金の増減額（△は増加）、営業活動によるキャッシュフロー """
    communication_line_ia: Optional[IxNonFractionPublic] = Field(default=None, description='通信回線使用権、無形固定資産')
    """ 通信回線使用権、無形固定資産 """
    increase_decrease_in_unrealized_gain_on_deferred_revenue_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='繰延延払利益の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 繰延延払利益の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    interest_and_income_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='受取利息及び配当金、営業活動によるキャッシュ・フロー')
    """ 受取利息及び配当金、営業活動によるキャッシュ・フロー """
    payment_for_guarantee_deposits_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='保証金の差入による支出、投資活動によるキャッシュ・フロー')
    """ 保証金の差入による支出、投資活動によるキャッシュ・フロー """
    proceeds_from_collection_of_guarantee_deposits_fin_cf: Optional[IxNonFractionPublic] = Field(default=None, description='保証金の返戻による収入、投資活動によるキャッシュ・フロー')
    """ 保証金の返戻による収入、投資活動によるキャッシュ・フロー """
    unrealized_gain_on_deferred_revenue_cl: Optional[IxNonFractionPublic] = Field(default=None, description='繰延延払利益、流動負債')
    """ 繰延延払利益、流動負債 """
    bonuses_and_provision_for_bonuses_sga: Optional[IxNonFractionPublic] = Field(default=None, description='賞与及び賞与引当金繰入額、販売費及び一般管理費')
    """ 賞与及び賞与引当金繰入額、販売費及び一般管理費 """
    in_process_research_and_development_ia: Optional[IxNonFractionPublic] = Field(default=None, description='仕掛研究開発、無形固定資産')
    """ 仕掛研究開発、無形固定資産 """
    increase_decrease_in_retirement_benefit_asset_and_liability_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='退職給付に係る資産負債の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 退職給付に係る資産負債の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    net_sales_of_finished_goods_and_merchandise: Optional[IxNonFractionPublic] = Field(default=None, description='商品及び製品の販売')
    """ 商品及び製品の販売 """
    other_income: Optional[IxNonFractionPublic] = Field(default=None, description='その他の収益')
    """ その他の収益 """
    royalty: Optional[IxNonFractionPublic] = Field(default=None, description='製品の販売等に関するライセンス契約')
    """ 製品の販売等に関するライセンス契約 """
    customer_related_intangible_assets_ia: Optional[IxNonFractionPublic] = Field(default=None, description='顧客関連無形資産、無形固定資産')
    """ 顧客関連無形資産、無形固定資産 """
    payments_of_contingent_consideration_for_shares_of_subsidiaries_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='子会社株式の条件付取得対価の支払額、投資活動によるキャッシュ・フロー')
    """ 子会社株式の条件付取得対価の支払額、投資活動によるキャッシュ・フロー """
    provision_for_compensation_loss_ncl: Optional[IxNonFractionPublic] = Field(default=None, description='補償損失引当金、固定負債')
    """ 補償損失引当金、固定負債 """
    reversal_of_provision_for_compensation_loss_el: Optional[IxNonFractionPublic] = Field(default=None, description='補償損失引当金戻入額、特別利益')
    """ 補償損失引当金戻入額、特別利益 """
    reversal_of_provision_for_compensation_loss_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='補償損失引当金戻入額、営業活動によるキャッシュ・フロー')
    """ 補償損失引当金戻入額、営業活動によるキャッシュ・フロー """
    business_structure_improvement_expenses_noe: Optional[IxNonFractionPublic] = Field(default=None, description='事業構造改善費用、営業外費用')
    """ 事業構造改善費用、営業外費用 """
    compensation_income_for_damage_noi: Optional[IxNonFractionPublic] = Field(default=None, description='受取賠償金、営業外収益')
    """ 受取賠償金、営業外収益 """
    repayments_to_share_acquisition_rights_fin_cf: Optional[IxNonFractionPublic] = Field(default=None, description='自己新株予約権の取得による支出、財務活動によるキャッシュ・フロー')
    """ 自己新株予約権の取得による支出、財務活動によるキャッシュ・フロー """
    amends_for_product_warranties_cl: Optional[IxNonFractionPublic] = Field(default=None, description='製品補償引当金、流動負債')
    """ 製品補償引当金、流動負債 """
    increase_decrease_in_amends_for_product: Optional[IxNonFractionPublic] = Field(default=None, description='製品補償引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 製品補償引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    increase_decrease_in_net_defined_benefit_asset_liability_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='退職給付に係る資産負債の増減額、営業活動によるキャッシュ・フロー')
    """ 退職給付に係る資産負債の増減額、営業活動によるキャッシュ・フロー """
    payments_of_loss_related_to_quality_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='品質関連損失の支払額、営業活動によるキャッシュ・フロー')
    """ 品質関連損失の支払額、営業活動によるキャッシュ・フロー """
    product_amends_drawing_noe: Optional[IxNonFractionPublic] = Field(default=None, description='製品補償引当金繰入額、営業外費用')
    """ 製品補償引当金繰入額、営業外費用 """
    proceeds_from_payments_for_derivative_settlement_net_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='デリバティブ決済による収支（純額）、投資活動によるキャッシュ・フロー')
    """ デリバティブ決済による収支（純額）、投資活動によるキャッシュ・フロー """
    reversal_of_impairment_loss_ei: Optional[IxNonFractionPublic] = Field(default=None, description='減損損失戻入益、特別利益')
    """ 減損損失戻入益、特別利益 """
    reversal_of_impairment_loss_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='減損損失戻入益、営業活動によるキャッシュ・フロー')
    """ 減損損失戻入益、営業活動によるキャッシュ・フロー """
    segment_profit_segment_information: Optional[IxNonFractionPublic] = Field(default=None, description='セグメント利益、セグメント情報')
    """ セグメント利益、セグメント情報 """
    decrease_increase_in_longterm_accounts_receivable_other_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='長期未収入金の増減額（△は増加）、営業活動によるキャッシュ・フロー')
    """ 長期未収入金の増減額（△は増加）、営業活動によるキャッシュ・フロー """
    shareholder_benefit_program_expense_noe: Optional[IxNonFractionPublic] = Field(default=None, description='株主優待費用、営業外費用')
    """ 株主優待費用、営業外費用 """
    loss_on_operation_of_investment_noe: Optional[IxNonFractionPublic] = Field(default=None, description='投資運用損、営業外費用')
    """ 投資運用損、営業外費用 """
    gain_on_forfeiture_of_unclaimed_dividends: Optional[IxNonFractionPublic] = Field(default=None, description='除斥配当金受入益、営業外収益')
    """ 除斥配当金受入益、営業外収益 """
    long_term_account_receivable_fixed_assets: Optional[IxNonFractionPublic] = Field(default=None, description='滞留債権、投資その他の資産')
    """ 滞留債権、投資その他の資産 """
    fiduciary_obligation_income_noi: Optional[IxNonFractionPublic] = Field(default=None, description='業務受託収入、営業外収益')
    """ 業務受託収入、営業外収益 """
    office_renovation_expenses_el: Optional[IxNonFractionPublic] = Field(default=None, description='事務所改装費用、特別損失')
    """ 事務所改装費用、特別損失 """
    provision_for_bad_debts_bonuses_and_retirement_expenses_sga: Optional[IxNonFractionPublic] = Field(default=None, description='引当金繰入額、販売費及び一般管理費')
    """ 引当金繰入額、販売費及び一般管理費 """
    purchase_of_other_property_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='その他償却資産の取得による支出、投資活動によるキャッシュ・フロー')
    """ その他償却資産の取得による支出、投資活動によるキャッシュ・フロー """
    increase_or_decrease_in_refund_liabilities_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='返金負債の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 返金負債の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    increase_or_decrease_in_returned_assets_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='返品資産の増減額（△は増加）、営業活動によるキャッシュ・フロー')
    """ 返品資産の増減額（△は増加）、営業活動によるキャッシュ・フロー """
    refund_liability_cl: Optional[IxNonFractionPublic] = Field(default=None, description='返金負債、流動負債')
    """ 返金負債、流動負債 """
    returned_assets_ca: Optional[IxNonFractionPublic] = Field(default=None, description='返品資産、流動資産')
    """ 返品資産、流動資産 """
    technical_assets_ia: Optional[IxNonFractionPublic] = Field(default=None, description='技術資産、無形固定資産')
    """ 技術資産、無形固定資産 """
    accrued_gasoline_tax: Optional[IxNonFractionPublic] = Field(default=None, description='未払揮発油税')
    """ 未払揮発油税 """
    increase_decrease_in_accrued_gasoline_tax_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='未払揮発油税の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 未払揮発油税の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    payments_for_sales_of_shares_of_subsidiaries_resulting_in_change_in_scope_of_consolidation_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='連結範囲の変更を伴う子会社株式の売却による支出、投資活動によるキャッシュ・フロー')
    """ 連結範囲の変更を伴う子会社株式の売却による支出、投資活動によるキャッシュ・フロー """
    rent_of_oil_tanks: Optional[IxNonFractionPublic] = Field(default=None, description='タンク賃借料')
    """ タンク賃借料 """
    rental_income_of_oil_tanks: Optional[IxNonFractionPublic] = Field(default=None, description='タンク賃貸料')
    """ タンク賃貸料 """
    repayment_of_the_examination_by_the_regional_taxation_bureau_el: Optional[IxNonFractionPublic] = Field(default=None, description='国税局調査に基づく返納金、特別損失')
    """ 国税局調査に基づく返納金、特別損失 """
    storage_tanks_net: Optional[IxNonFractionPublic] = Field(default=None, description='油槽（純額）')
    """ 油槽（純額） """
    long_term_deposit_ioa: Optional[IxNonFractionPublic] = Field(default=None, description='長期性預金、投資その他の資産')
    """ 長期性預金、投資その他の資産 """
    remeasurements_of_defined_benefit_plans_oci: Optional[IxNonFractionPublic] = Field(default=None, description='退職給付に係る調整額、その他の包括利益')
    """ 退職給付に係る調整額、その他の包括利益 """
    cash_dividends_paid_by_parent_company_fin_cf: Optional[IxNonFractionPublic] = Field(default=None, description='親会社による配当金の支払額、財務活動によるキャッシュ・フロー')
    """ 親会社による配当金の支払額、財務活動によるキャッシュ・フロー """
    expenses_of_voluntary_recall_of_products_el: Optional[IxNonFractionPublic] = Field(default=None, description='製品自主回収関連費用、特別損失')
    """ 製品自主回収関連費用、特別損失 """
    fee_on_sales_of_notes_payable_noe: Optional[IxNonFractionPublic] = Field(default=None, description='手形売却費、営業外費用')
    """ 手形売却費、営業外費用 """
    gain_on_reversal_of_foreign_currency_translation_adjustment_ei: Optional[IxNonFractionPublic] = Field(default=None, description='為替換算調整勘定取崩益、特別利益')
    """ 為替換算調整勘定取崩益、特別利益 """
    gain_on_reversal_of_foreign_currency_translation_adjustment_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='為替換算調整勘定取崩益、営業活動によるキャッシュ・フロー')
    """ 為替換算調整勘定取崩益、営業活動によるキャッシュ・フロー """
    increase_decrease_in_provision_for_liquidation_of_subsidiaries_losses2_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='関係会社清算損失引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 関係会社清算損失引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    increase_decrease_in_provision_for_product_compensation_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='製品補償引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 製品補償引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    litigation_loss_ei: Optional[IxNonFractionPublic] = Field(default=None, description='訴訟損失、特別損失')
    """ 訴訟損失、特別損失 """
    provision_for_loss_on_closing_subsidiaries_and_affiliates_cl: Optional[IxNonFractionPublic] = Field(default=None, description='関係会社清算損失引当金、流動負債')
    """ 関係会社清算損失引当金、流動負債 """
    provision_for_product_compensation_cl: Optional[IxNonFractionPublic] = Field(default=None, description='製品補償引当金、流動負債')
    """ 製品補償引当金、流動負債 """
    increase_decrease_in_guarantee_deposited_fin_cf: Optional[IxNonFractionPublic] = Field(default=None, description='預り保証金の純増減額（△は減少）、財務活動によるキャッシュ・フロー')
    """ 預り保証金の純増減額（△は減少）、財務活動によるキャッシュ・フロー """
    increase_decrease_in_provision_for_special_compensation_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='従業員特別補償引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 従業員特別補償引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    operating_accounts_receivable_net_amount_ca: Optional[IxNonFractionPublic] = Field(default=None, description='営業未収入金（純額）、流動資産')
    """ 営業未収入金（純額）、流動資産 """
    provision_for_employee_special_amends_ncl: Optional[IxNonFractionPublic] = Field(default=None, description='従業員特別補償引当金、固定負債')
    """ 従業員特別補償引当金、固定負債 """
    provision_for_special_compensations_el: Optional[IxNonFractionPublic] = Field(default=None, description='従業員特別補償引当金繰入額、特別損失')
    """ 従業員特別補償引当金繰入額、特別損失 """
    refund_income_noi: Optional[IxNonFractionPublic] = Field(default=None, description='還付金収入、営業外収益')
    """ 還付金収入、営業外収益 """
    disaster_repair_expenses_noe: Optional[IxNonFractionPublic] = Field(default=None, description='災害修繕費、営業外費用')
    """ 災害修繕費、営業外費用 """
    increase_decrease_in_provision_for_employee_stock_ownership_plan_trust_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='従業員株式給付引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 従業員株式給付引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    provision_for_employee_stock_ownership_plan_trust_ncl: Optional[IxNonFractionPublic] = Field(default=None, description='従業員株式給付引当金、固定負債')
    """ 従業員株式給付引当金、固定負債 """
    listing_fees_noe: Optional[IxNonFractionPublic] = Field(default=None, description='上場賦課金、営業外費用')
    """ 上場賦課金、営業外費用 """
    payments_of_loss_on_workplace_closing_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='事業所閉鎖損失の支払額、営業活動によるキャッシュ・フロー')
    """ 事業所閉鎖損失の支払額、営業活動によるキャッシュ・フロー """
    provision_for_loss_on_workplace_closing_cl: Optional[IxNonFractionPublic] = Field(default=None, description='事業所閉鎖損失引当金、流動負債')
    """ 事業所閉鎖損失引当金、流動負債 """
    dividends_income_received_in_proportion_to_transactions_with_partnership_noi: Optional[IxNonFractionPublic] = Field(default=None, description='利用分量配当金、営業外収益')
    """ 利用分量配当金、営業外収益 """
    loss_on_cancellation_of_membership_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='会員権解約損、営業活動によるキャッシュ・フロー')
    """ 会員権解約損、営業活動によるキャッシュ・フロー """
    proceed_from_disposal_of_iron_scraps_noi: Optional[IxNonFractionPublic] = Field(default=None, description='鉄屑処分収入、営業外収益')
    """ 鉄屑処分収入、営業外収益 """
    accrued_liability_for_factoring: Optional[IxNonFractionPublic] = Field(default=None, description='ファクタリング未払金、流動負債')
    """ ファクタリング未払金、流動負債 """
    decrease_increase_in_deposits_for_purchase_of_treausury_shares_fin_cf: Optional[IxNonFractionPublic] = Field(default=None, description='自己株式取得のための預託金の増減額(△は増加)、財務活動によるキャッシュ・フロー')
    """ 自己株式取得のための預託金の増減額(△は増加)、財務活動によるキャッシュ・フロー """
    long_term_suspense_receipt_ncl: Optional[IxNonFractionPublic] = Field(default=None, description='長期仮受金、固定負債')
    """ 長期仮受金、固定負債 """
    share_based_payment_expenses_el: Optional[IxNonFractionPublic] = Field(default=None, description='株式報酬費用、特別損失')
    """ 株式報酬費用、特別損失 """
    foreign_withholding_tax_noe: Optional[IxNonFractionPublic] = Field(default=None, description='外国源泉税、営業外費用')
    """ 外国源泉税、営業外費用 """
    provision_for_loss_contract_ncl: Optional[IxNonFractionPublic] = Field(default=None, description='契約損失引当金、固定負債')
    """ 契約損失引当金、固定負債 """
    provision_of_restoration_cost_cl: Optional[IxNonFractionPublic] = Field(default=None, description='復旧費用引当金、流動負債')
    """ 復旧費用引当金、流動負債 """
    provision_of_restoration_cost_ncl: Optional[IxNonFractionPublic] = Field(default=None, description='復旧費用引当金、固定負債')
    """ 復旧費用引当金、固定負債 """
    gain_on_non_current_assets_rent_noi: Optional[IxNonFractionPublic] = Field(default=None, description='固定資産賃貸益、営業外収益')
    """ 固定資産賃貸益、営業外収益 """
    loss_on_inappropriate_conduct_in_quality_inspections_el: Optional[IxNonFractionPublic] = Field(default=None, description='品質不適切行為関連損失、特別損失')
    """ 品質不適切行為関連損失、特別損失 """
    provision_for_business_restructure_cl: Optional[IxNonFractionPublic] = Field(default=None, description='事業再構築引当金、流動負債')
    """ 事業再構築引当金、流動負債 """
    provision_for_loss_on_wind_power_generator_business_cl: Optional[IxNonFractionPublic] = Field(default=None, description='風力事業損失引当金、流動負債')
    """ 風力事業損失引当金、流動負債 """
    payment_amount_of_compensation_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='支払補償金の支払額、営業活動によるキャッシュ・フロー')
    """ 支払補償金の支払額、営業活動によるキャッシュ・フロー """
    payment_compensation_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='支払補償金、営業活動によるキャッシュ・フロー')
    """ 支払補償金、営業活動によるキャッシュ・フロー """
    accumulated_depreciation_land_used_for_mining_operations: Optional[IxNonFractionPublic] = Field(default=None, description='減価償却累計額、鉱業用地')
    """ 減価償却累計額、鉱業用地 """
    gain_on_sale_of_shares_of_subsidiaries_and_associates_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='関係会社株式売却益、営業活動によるキャッシュ・フロー')
    """ 関係会社株式売却益、営業活動によるキャッシュ・フロー """
    land_used_for_mining_operations_net: Optional[IxNonFractionPublic] = Field(default=None, description='鉱業用地（純額）')
    """ 鉱業用地（純額） """
    land_used_for_mining_operations_ppe: Optional[IxNonFractionPublic] = Field(default=None, description='鉱業用地、有形固定資産')
    """ 鉱業用地、有形固定資産 """
    compensation_for_payment_el: Optional[IxNonFractionPublic] = Field(default=None, description='支払補償金、特別損失')
    """ 支払補償金、特別損失 """
    deposited_gold_bullion_cl: Optional[IxNonFractionPublic] = Field(default=None, description='預り金地金、流動負債、負債の部')
    """ 預り金地金、流動負債、負債の部 """
    expense_for_the_maintenance_and_management_of_abandoned_mines: Optional[IxNonFractionPublic] = Field(default=None, description='鉱山残務整理費用、営業外費用')
    """ 鉱山残務整理費用、営業外費用 """
    increase_in_cash_and_cash_equivalents_from_newly_consolidated: Optional[IxNonFractionPublic] = Field(default=None, description='非連結子会社の連結に伴う現金及び現金同等物の増加額')
    """ 非連結子会社の連結に伴う現金及び現金同等物の増加額 """
    land_net_ppe: Optional[IxNonFractionPublic] = Field(default=None, description='土地（純額）、有形固定資産')
    """ 土地（純額）、有形固定資産 """
    leased_gold_bullion_receivable_ca: Optional[IxNonFractionPublic] = Field(default=None, description='貸付け金地金、流動資産、資産の部')
    """ 貸付け金地金、流動資産、資産の部 """
    losses_on_withdrawal_from_business_el: Optional[IxNonFractionPublic] = Field(default=None, description='事業撤退損失、特別損失')
    """ 事業撤退損失、特別損失 """
    payment_for_purchases_of_gold_bullion_from_market_for_customers_under_my_gold_plan_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='金地金購入による支出、営業活動によるキャッシュ・フロー')
    """ 金地金購入による支出、営業活動によるキャッシュ・フロー """
    proceeds_from_sales_of_gold_bullion_deposited_from_customers_under_consuming_bailment_my_gold_plan_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='金地金売却による収入、営業活動によるキャッシュ・フロー')
    """ 金地金売却による収入、営業活動によるキャッシュ・フロー """
    loss_on_disaster_noe: Optional[IxNonFractionPublic] = Field(default=None, description='災害損失、営業外費用')
    """ 災害損失、営業外費用 """
    allowance_for_demolition_of_non_current_assets_liabilities: Optional[IxNonFractionPublic] = Field(default=None, description='固定資産解体費用引当金、負債の部')
    """ 固定資産解体費用引当金、負債の部 """
    increase_decrease_in_allowance_for_demolition_of_non_current_assets_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='固定資産解体費用引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 固定資産解体費用引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    increase_decrease_in_provision_for_share_based_compensation_ope_cfbnk: Optional[IxNonFractionPublic] = Field(default=None, description='株式報酬引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー、銀行業')
    """ 株式報酬引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー、銀行業 """
    lease_receivables_and_investment_assets_assets_bnk: Optional[IxNonFractionPublic] = Field(default=None, description='リース債権及びリース投資資産、資産の部、銀行業')
    """ リース債権及びリース投資資産、資産の部、銀行業 """
    provision_for_share_based_compensation_liabilities_bnk: Optional[IxNonFractionPublic] = Field(default=None, description='株式報酬引当金、負債の部、銀行業')
    """ 株式報酬引当金、負債の部、銀行業 """
    provision_of_reserve_for_financial_instruments_transaction_liabilities: Optional[IxNonFractionPublic] = Field(default=None, description='金融商品取引責任準備金繰入額')
    """ 金融商品取引責任準備金繰入額 """
    provision_for_pollution_load_levy_cl: Optional[IxNonFractionPublic] = Field(default=None, description='汚染負荷量賦課金引当金、流動負債')
    """ 汚染負荷量賦課金引当金、流動負債 """
    provision_for_pollution_load_levy_ncl: Optional[IxNonFractionPublic] = Field(default=None, description='汚染負荷量賦課金引当金、固定負債')
    """ 汚染負荷量賦課金引当金、固定負債 """
    allowance_for_stock_benefit_for_employee_ncl: Optional[IxNonFractionPublic] = Field(default=None, description='従業員株式給付引当金、固定負債')
    """ 従業員株式給付引当金、固定負債 """
    condolence_money_noe: Optional[IxNonFractionPublic] = Field(default=None, description='弔慰金、営業外費用')
    """ 弔慰金、営業外費用 """
    increase_decrease_in_provision_for_decommissioning_of_inventories_goods_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='棚卸資産廃棄費用引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 棚卸資産廃棄費用引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    increase_decrease_in_provision_for_special_investigation_fees_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='特別調査費用引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 特別調査費用引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    payment_for_busines_restrucuring_expenses_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='事業構造改革費用の支払額、営業活動によるキャッシュ・フロー')
    """ 事業構造改革費用の支払額、営業活動によるキャッシュ・フロー """
    provision_for_business_restructuring_ncl: Optional[IxNonFractionPublic] = Field(default=None, description='事業構造改革引当金、固定負債')
    """ 事業構造改革引当金、固定負債 """
    provision_for_decommissioning_of_inventories_goods_cl: Optional[IxNonFractionPublic] = Field(default=None, description='棚卸資産廃棄費用引当金、流動負債')
    """ 棚卸資産廃棄費用引当金、流動負債 """
    provision_for_special_investigation_expenses_cl: Optional[IxNonFractionPublic] = Field(default=None, description='特別調査費用引当金、流動負債')
    """ 特別調査費用引当金、流動負債 """
    gain_on_reversal_of_liabilities_noi: Optional[IxNonFractionPublic] = Field(default=None, description='債務取崩益、営業外収益')
    """ 債務取崩益、営業外収益 """
    profit_on_cansellation_of_leases_ei: Optional[IxNonFractionPublic] = Field(default=None, description='リース解約益、特別利益')
    """ リース解約益、特別利益 """
    new_factory_construction_expenses_el: Optional[IxNonFractionPublic] = Field(default=None, description='新工場建設関連費用、特別損失')
    """ 新工場建設関連費用、特別損失 """
    litigation_expenses_el: Optional[IxNonFractionPublic] = Field(default=None, description='訴訟関連費用、特別損失')
    """ 訴訟関連費用、特別損失 """
    litigation_expenses_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='訴訟関連費用、営業活動によるキャッシュ・フロー')
    """ 訴訟関連費用、営業活動によるキャッシュ・フロー """
    litigation_expenses_paid_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='訴訟関連費用の支払額、営業活動によるキャッシュ・フロー')
    """ 訴訟関連費用の支払額、営業活動によるキャッシュ・フロー """
    rental_inventory_assets_ca: Optional[IxNonFractionPublic] = Field(default=None, description='レンタル商品、流動資産')
    """ レンタル商品、流動資産 """
    insurance_expenses_noe: Optional[IxNonFractionPublic] = Field(default=None, description='保険料、営業外費用')
    """ 保険料、営業外費用 """
    maintenance_cost_for_idle_assets_noe: Optional[IxNonFractionPublic] = Field(default=None, description='遊休資産維持管理費用、営業外費用')
    """ 遊休資産維持管理費用、営業外費用 """
    withholding_tax_burden_loss_noe: Optional[IxNonFractionPublic] = Field(default=None, description='源泉税負担損失、営業外費用')
    """ 源泉税負担損失、営業外費用 """
    use_quantity_dividend_noi: Optional[IxNonFractionPublic] = Field(default=None, description='利用分量配当金、営業外収益')
    """ 利用分量配当金、営業外収益 """
    gain_on_scrap_metal_noi: Optional[IxNonFractionPublic] = Field(default=None, description='原材料等売却益、営業外収益')
    """ 原材料等売却益、営業外収益 """
    system_failure_response_costs_el: Optional[IxNonFractionPublic] = Field(default=None, description='システム障害対応費用、特別損失')
    """ システム障害対応費用、特別損失 """
    provision_for_compensation_cl: Optional[IxNonFractionPublic] = Field(default=None, description='損害補償損失引当金、流動負債')
    """ 損害補償損失引当金、流動負債 """
    directors_compensations_salaries_allowances_bonuses_and_welfare_expenses_sga: Optional[IxNonFractionPublic] = Field(default=None, description='役員報酬及び従業員給与・諸手当・賞与・福利費、販売費及び一般管理費')
    """ 役員報酬及び従業員給与・諸手当・賞与・福利費、販売費及び一般管理費 """
    estimate_design_cost_sga: Optional[IxNonFractionPublic] = Field(default=None, description='見積設計費、販売費及び一般管理費')
    """ 見積設計費、販売費及び一般管理費 """
    increase_decrease_net_defined_benefit_asset_liability_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='退職給付に係る資産負債の増減額(△は減少）、営業活動によるキャッシュ・フロー')
    """ 退職給付に係る資産負債の増減額(△は減少）、営業活動によるキャッシュ・フロー """
    notes_receivable_accounts_receivable_from_completed_construction_contracts_and_contract_assets_ca: Optional[IxNonFractionPublic] = Field(default=None, description='受取手形、完成工事未収入金及び契約資産、流動資産')
    """ 受取手形、完成工事未収入金及び契約資産、流動資産 """
    payments_into_long_term_time_deposits_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='長期性預金の預け入れによる支出、投資活動によるキャッシュ・フロー')
    """ 長期性預金の預け入れによる支出、投資活動によるキャッシュ・フロー """
    proceeds_from_withdrawal_of_long_term_time_deposits_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='長期性預金の払戻による収入、投資活動によるキャッシュフロー')
    """ 長期性預金の払戻による収入、投資活動によるキャッシュフロー """
    notes_receivable_accounts_receivable_from_completed_construction_contracts_and_other_and_contract_assets_ca: Optional[IxNonFractionPublic] = Field(default=None, description='受取手形・完成工事未収入金等及び契約資産、流動資産')
    """ 受取手形・完成工事未収入金等及び契約資産、流動資産 """
    proceeds_from_issuance_of_convertible_bonds_with_stock_acquisition_rights_fin_cf: Optional[IxNonFractionPublic] = Field(default=None, description='転換社債型新株予約権付社債の発行による収入、財務活動によるキャッシュ・フロー')
    """ 転換社債型新株予約権付社債の発行による収入、財務活動によるキャッシュ・フロー """
    loss_on_investments_in_partenership_fund_noe: Optional[IxNonFractionPublic] = Field(default=None, description='組合投資損失、営業外費用')
    """ 組合投資損失、営業外費用 """
    increase_decrease_in_unearned_interest_on_installment_sale_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='割賦販売前受利息の増減額(△は減少)、営業活動によるキャッシュ・フロー')
    """ 割賦販売前受利息の増減額(△は減少)、営業活動によるキャッシュ・フロー """
    interest_income_on_installment_sale_noi: Optional[IxNonFractionPublic] = Field(default=None, description='割賦販売受取利息、営業外収益')
    """ 割賦販売受取利息、営業外収益 """
    payments_from_rental_of_real_estate_for_investment_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='投資不動産の賃貸による支出、投資活動によるキャッシュ・フロー')
    """ 投資不動産の賃貸による支出、投資活動によるキャッシュ・フロー """
    rent_expenses_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='賃貸費用、営業活動によるキャッシュ・フロー')
    """ 賃貸費用、営業活動によるキャッシュ・フロー """
    reversal_of_provision_for_product_warranties_noi: Optional[IxNonFractionPublic] = Field(default=None, description='製品保証引当金戻入額、営業外収益')
    """ 製品保証引当金戻入額、営業外収益 """
    directors_compensations_and_employees_salaries_sga: Optional[IxNonFractionPublic] = Field(default=None, description='役員・従業員給与手当、販売費及び一般管理費')
    """ 役員・従業員給与手当、販売費及び一般管理費 """
    refund_liabilities: Optional[IxNonFractionPublic] = Field(default=None, description='返金負債')
    """ 返金負債 """
    provision_for_loss_on_disaster_noe: Optional[IxNonFractionPublic] = Field(default=None, description='災害損失引当金繰入額、営業外費用')
    """ 災害損失引当金繰入額、営業外費用 """
    restructuring_expenses_noe: Optional[IxNonFractionPublic] = Field(default=None, description='事業再編費用、営業外費用')
    """ 事業再編費用、営業外費用 """
    loss_on_liquidation_of_non_current_assets_el: Optional[IxNonFractionPublic] = Field(default=None, description='固定資産整理損失、特別損失')
    """ 固定資産整理損失、特別損失 """
    provision_for_loss_on_liquidation_of_non_current_assets: Optional[IxNonFractionPublic] = Field(default=None, description='固定資産整理損失引当金')
    """ 固定資産整理損失引当金 """
    provision_for_product_warranties_cl: Optional[IxNonFractionPublic] = Field(default=None, description='製品保証引当金、流動負債')
    """ 製品保証引当金、流動負債 """
    minimum_pension_liability_adjustment_oci: Optional[IxNonFractionPublic] = Field(default=None, description='最小年金負債調整額、その他の包括利益')
    """ 最小年金負債調整額、その他の包括利益 """
    minimum_pension_liability_adjustments: Optional[IxNonFractionPublic] = Field(default=None, description='最小年金負債調整額')
    """ 最小年金負債調整額 """
    payment_for_extra_retirement_payments_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='割増退職金等の支払額、営業活動によるキャッシュ・フロー')
    """ 割増退職金等の支払額、営業活動によるキャッシュ・フロー """
    payments_for_litigation_expenses_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='訴訟損失費用の支払額、営業活動によるキャッシュ・フロー')
    """ 訴訟損失費用の支払額、営業活動によるキャッシュ・フロー """
    restructuring_cost_el: Optional[IxNonFractionPublic] = Field(default=None, description='事業構造改革費用、特別損失')
    """ 事業構造改革費用、特別損失 """
    restructuring_cost_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='事業構造改革費用、営業活動によるキャッシュ・フロー')
    """ 事業構造改革費用、営業活動によるキャッシュ・フロー """
    the_right_of_using_land_ia: Optional[IxNonFractionPublic] = Field(default=None, description='土地使用権、無形固定資産')
    """ 土地使用権、無形固定資産 """
    borrowing_fee_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='借入手数料、営業活動によるキャッシュ・フロー')
    """ 借入手数料、営業活動によるキャッシュ・フロー """
    decrease_increase_in_real_estate_for_sale_in_process_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='仕掛販売用不動産の増減額（△は増加）、営業活動によるキャッシュ・フロー')
    """ 仕掛販売用不動産の増減額（△は増加）、営業活動によるキャッシュ・フロー """
    deposits_form_silent_partnership_cl: Optional[IxNonFractionPublic] = Field(default=None, description='匿名組合預り金、流動負債')
    """ 匿名組合預り金、流動負債 """
    distributions_of_loss_on_silent_partnerships_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='匿名組合損益分配額、営業活動によるキャッシュ・フロー')
    """ 匿名組合損益分配額、営業活動によるキャッシュ・フロー """
    dividend_to_a_sleeping_partner_fin_cf: Optional[IxNonFractionPublic] = Field(default=None, description='匿名組合員への分配金、財務活動によるキャッシュ・フロー')
    """ 匿名組合員への分配金、財務活動によるキャッシュ・フロー """
    gain_on_reversal_of_provision_for_demolition_cost_ei: Optional[IxNonFractionPublic] = Field(default=None, description='解体費用引当金戻入額、特別利益')
    """ 解体費用引当金戻入額、特別利益 """
    gain_on_reversal_of_provision_for_demolition_cost_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='解体費用引当金戻入額、営業活動によるキャッシュ・フロー')
    """ 解体費用引当金戻入額、営業活動によるキャッシュ・フロー """
    increase_decrease_in_accrued_business_taxes_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='未払事業税等の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 未払事業税等の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    increase_or_decrease_in_the_trust_deposits_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='信託預金の増減額（△は増加）、営業活動によるキャッシュ・フロー')
    """ 信託預金の増減額（△は増加）、営業活動によるキャッシュ・フロー """
    payments_of_borrowing_fee_fin_cf: Optional[IxNonFractionPublic] = Field(default=None, description='借入手数料の支払額、財務活動によるキャッシュ・フロー')
    """ 借入手数料の支払額、財務活動によるキャッシュ・フロー """
    proceeds_from_withdrawal_of_investments_in_silent_partnership_fin_cf: Optional[IxNonFractionPublic] = Field(default=None, description='匿名組合員からの出資払込による収入、財務活動によるキャッシュ・フロー')
    """ 匿名組合員からの出資払込による収入、財務活動によるキャッシュ・フロー """
    rental_real_estate_expenses_noe: Optional[IxNonFractionPublic] = Field(default=None, description='賃貸不動産経費、営業外費用')
    """ 賃貸不動産経費、営業外費用 """
    reversal_of_allowance_for_doubtful_accounts_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='貸倒引当金戻入額、営業活動によるキャッシュ・フロー')
    """ 貸倒引当金戻入額、営業活動によるキャッシュ・フロー """
    sales_accrued_income_ca: Optional[IxNonFractionPublic] = Field(default=None, description='営業未収収益、流動資産')
    """ 営業未収収益、流動資産 """
    spending_funded_by_reimbursements_to_the_anonymous_members_fin_cf: Optional[IxNonFractionPublic] = Field(default=None, description='匿名組合員への出資払戻による支出、財務活動によるキャッシュ・フロー')
    """ 匿名組合員への出資払戻による支出、財務活動によるキャッシュ・フロー """
    trust_deposit: Optional[IxNonFractionPublic] = Field(default=None, description='信託預金')
    """ 信託預金 """
    trust_guarantee_deposits_received: Optional[IxNonFractionPublic] = Field(default=None, description='信託預り保証金')
    """ 信託預り保証金 """
    trust_unearned_revenue: Optional[IxNonFractionPublic] = Field(default=None, description='信託前受金')
    """ 信託前受金 """
    commission_for_purchase_of_treasury_shares_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='自己株式取得費用、営業活動によるキャッシュ・フロー')
    """ 自己株式取得費用、営業活動によるキャッシュ・フロー """
    reserve_for_repair_expenses_of_products_cl: Optional[IxNonFractionPublic] = Field(default=None, description='製品補修引当金、流動負債')
    """ 製品補修引当金、流動負債 """
    reseve_for_repair_expenses_of_products_ncl: Optional[IxNonFractionPublic] = Field(default=None, description='製品補修引当金、固定負債')
    """ 製品補修引当金、固定負債 """
    assets_for_lease_net: Optional[IxNonFractionPublic] = Field(default=None, description='賃貸資産（純額）')
    """ 賃貸資産（純額） """
    expenses_of_real_estate_for_rent_noe: Optional[IxNonFractionPublic] = Field(default=None, description='賃貸不動産関係費用、営業外費用')
    """ 賃貸不動産関係費用、営業外費用 """
    loss_on_sale_of_raw_materials_noe: Optional[IxNonFractionPublic] = Field(default=None, description='原材料売却損、営業外費用')
    """ 原材料売却損、営業外費用 """
    decrease_increase_in_operating_accounts_receivable_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='営業未収入金の増減額（△は増加）、営業活動によるキャッシュ・フロー')
    """ 営業未収入金の増減額（△は増加）、営業活動によるキャッシュ・フロー """
    redumption_of_bonds_with_share_acquisition_rights_fin_cf: Optional[IxNonFractionPublic] = Field(default=None, description='新株予約権付社債の償還による支出、財務活動によるキャッシュ・フロー')
    """ 新株予約権付社債の償還による支出、財務活動によるキャッシュ・フロー """
    compensation_income_for_damages_ei: Optional[IxNonFractionPublic] = Field(default=None, description='受取損害賠償金、特別利益')
    """ 受取損害賠償金、特別利益 """
    expenses_of_real_estate_noe: Optional[IxNonFractionPublic] = Field(default=None, description='不動産費用、営業外費用')
    """ 不動産費用、営業外費用 """
    gain_on_sale_of_investments_in_capital_of_subsidiaries_and_associates_ei: Optional[IxNonFractionPublic] = Field(default=None, description='関係会社出資金売却益、特別利益')
    """ 関係会社出資金売却益、特別利益 """
    increase_decrease_in_cash_and_cash_equivalents_resulting_from_change_in_accounting_period_of_subsidiaries_cce: Optional[IxNonFractionPublic] = Field(default=None, description='連結子会社の決算期変更に伴う現金及び現金同等物の増減額（△は減少）')
    """ 連結子会社の決算期変更に伴う現金及び現金同等物の増減額（△は減少） """
    proceeds_from_sale_of_investments_in_capital_of_subsidiaries_resulting_in_change_in_scope_of: Optional[IxNonFractionPublic] = Field(default=None, description='連結の範囲の変更を伴う子会社出資金の売却による収入、投資活動によるキャッシュ・フロー')
    """ 連結の範囲の変更を伴う子会社出資金の売却による収入、投資活動によるキャッシュ・フロー """
    electronically_recorded_obligations_operating_facilities_cl: Optional[IxNonFractionPublic] = Field(default=None, description='設備電子記録債務、流動負債')
    """ 設備電子記録債務、流動負債 """
    gain_on_sales_of_scraps_noi: Optional[IxNonFractionPublic] = Field(default=None, description='材料屑売却益、営業外収益')
    """ 材料屑売却益、営業外収益 """
    proceeds_from_acceptance_of_investment_to_non_controlling_interests_fin_cf: Optional[IxNonFractionPublic] = Field(default=None, description='投資事業組合等における非支配持分からの出資受入による収入、財務活動によるキャッシュフロー')
    """ 投資事業組合等における非支配持分からの出資受入による収入、財務活動によるキャッシュフロー """
    accumulated_depreciation_rental_assets: Optional[IxNonFractionPublic] = Field(default=None, description='減価償却累計額、レンタル資産')
    """ 減価償却累計額、レンタル資産 """
    income_of_rent_noi: Optional[IxNonFractionPublic] = Field(default=None, description='賃貸収入、営業外収益')
    """ 賃貸収入、営業外収益 """
    rental_assets_net: Optional[IxNonFractionPublic] = Field(default=None, description='レンタル資産（純額）')
    """ レンタル資産（純額） """
    rental_assets_ppe: Optional[IxNonFractionPublic] = Field(default=None, description='レンタル資産、有形固定資産')
    """ レンタル資産、有形固定資産 """
    loss_on_sales_of_notes_and_accounts_receivable_trade_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='売上債権売却損、営業活動によるキャッシュ・フロー')
    """ 売上債権売却損、営業活動によるキャッシュ・フロー """
    revenue_from_acceptance_of_development_services_noi: Optional[IxNonFractionPublic] = Field(default=None, description='受託研究収入、営業外収益')
    """ 受託研究収入、営業外収益 """
    sales_of_trade_receivables_paid: Optional[IxNonFractionPublic] = Field(default=None, description='売上債権売却による支払額、営業活動によるキャッシュ・フロー')
    """ 売上債権売却による支払額、営業活動によるキャッシュ・フロー """
    expenses_for_persons_of_temporary_transfer_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='出向者経費、営業活動によるキャッシュ・フロー')
    """ 出向者経費、営業活動によるキャッシュ・フロー """
    gain_on_reversal_of_loss_on_business_related_to_business_partners_el: Optional[IxNonFractionPublic] = Field(default=None, description='取引先関連事業損失戻入益、特別利益')
    """ 取引先関連事業損失戻入益、特別利益 """
    gain_on_reversal_of_loss_on_business_related_to_business_partners_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='取引先関連事業損失戻入益、、営業活動によるキャッシュ・フロー')
    """ 取引先関連事業損失戻入益、、営業活動によるキャッシュ・フロー """
    current_potion_of_long_term_loans_payable_cl: Optional[IxNonFractionPublic] = Field(default=None, description='一年以内返済長期借入金、流動負債')
    """ 一年以内返済長期借入金、流動負債 """
    increase_decrease_in_consumption_taxes_payable_consumption_taxes_refund_receivable_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='未払又は未収消費税等の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 未払又は未収消費税等の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    note_notes_and_accounts_receivable_trade_and_contract_assets_net_ca: Optional[IxNonFractionPublic] = Field(default=None, description='売掛金及び契約資産、流動資産')
    """ 売掛金及び契約資産、流動資産 """
    operations_cosignment_fee_noi: Optional[IxNonFractionPublic] = Field(default=None, description='業務受託収入、営業外収益')
    """ 業務受託収入、営業外収益 """
    commission_for_syndicate_loan_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='シンジケートローン手数料、営業活動によるキャッシュ・フロー')
    """ シンジケートローン手数料、営業活動によるキャッシュ・フロー """
    amortization_of_customer_related_assets_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='顧客関連資産償却額、営業活動によるキャッシュ・フロー')
    """ 顧客関連資産償却額、営業活動によるキャッシュ・フロー """
    expenses_etc_segment_information: Optional[IxNonFractionPublic] = Field(default=None, description='経費等、セグメント情報')
    """ 経費等、セグメント情報 """
    gross_operating_profit_segment_information: Optional[IxNonFractionPublic] = Field(default=None, description='連結業務粗利益、セグメント情報')
    """ 連結業務粗利益、セグメント情報 """
    reserve_for_point_program_liabilities_bnk: Optional[IxNonFractionPublic] = Field(default=None, description='ポイント引当金、負債の部、銀行業')
    """ ポイント引当金、負債の部、銀行業 """
    balance_of_purchase_and_sales_of_treasury_stock_fin_cf: Optional[IxNonFractionPublic] = Field(default=None, description='自己株式の取得・売却による収支、財務活動によるキャッシュ・フロー')
    """ 自己株式の取得・売却による収支、財務活動によるキャッシュ・フロー """
    increase_due_to_share_delivery: Optional[IxNonFractionPublic] = Field(default=None, description='株式交付による増加')
    """ 株式交付による増加 """
    lncrease_decrease_in_lease_receivables_and_investment_assets_ope_cfbnk: Optional[IxNonFractionPublic] = Field(default=None, description='リース債権及びリース投資資産の純増(△)減、営業活動によるキャッシュ・フロー、銀行業')
    """ リース債権及びリース投資資産の純増(△)減、営業活動によるキャッシュ・フロー、銀行業 """
    provision_for_loss_on_special_claims: Optional[IxNonFractionPublic] = Field(default=None, description='特別クレーム損失引当金')
    """ 特別クレーム損失引当金 """
    development_fiduciary_obligation_fee_noi: Optional[IxNonFractionPublic] = Field(default=None, description='開発業務受託料、営業外収益')
    """ 開発業務受託料、営業外収益 """
    lease_receivables_and_investments_in_leases_assets_bnk: Optional[IxNonFractionPublic] = Field(default=None, description='リース債権及びリース投資資産、資産の部、銀行業')
    """ リース債権及びリース投資資産、資産の部、銀行業 """
    provision_for_share_awards: Optional[IxNonFractionPublic] = Field(default=None, description='株式給付引当金')
    """ 株式給付引当金 """
    reversal_of_provision_for_loss_on_guarantees_noi: Optional[IxNonFractionPublic] = Field(default=None, description='債務保証損失引当金戻入額、営業外収益')
    """ 債務保証損失引当金戻入額、営業外収益 """
    increase_of_treasury_shares_by_increasing_of_entities_accounted_for_using_equity_method_ss: Optional[IxNonFractionPublic] = Field(default=None, description='持分法適用の関連会社の増加に伴う自己株式の増加 、株主資本等変動計算書')
    """ 持分法適用の関連会社の増加に伴う自己株式の増加 、株主資本等変動計算書 """
    lease_receivables_and_investments_in_leases_assets: Optional[IxNonFractionPublic] = Field(default=None, description='リース債権及びリース投資資産、資産の部')
    """ リース債権及びリース投資資産、資産の部 """
    provision_for_stockshares_liabilities: Optional[IxNonFractionPublic] = Field(default=None, description='株式給付引当金、負債の部')
    """ 株式給付引当金、負債の部 """
    retained_earnings_increased_sales_associated_with_a_increase_in_equity_method_affiliates_ss: Optional[IxNonFractionPublic] = Field(default=None, description='持分法適用の関連会社の増加に伴う利益剰余金の増加、株主資本等変動計算書')
    """ 持分法適用の関連会社の増加に伴う利益剰余金の増加、株主資本等変動計算書 """
    revaluation_reserve_for_land_changes_of_items_during_period: Optional[IxNonFractionPublic] = Field(default=None, description='土地再評価差額金取崩額、当期変動額')
    """ 土地再評価差額金取崩額、当期変動額 """
    net_decrease_increase_in_margin_for_central_counterparty_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='中央清算機関差入証拠金の純増（△）減、営業活動によるキャッシュ・フロー')
    """ 中央清算機関差入証拠金の純増（△）減、営業活動によるキャッシュ・フロー """
    provision_for_share_based_compensation_liabilities: Optional[IxNonFractionPublic] = Field(default=None, description='株式報酬引当金、負債の部')
    """ 株式報酬引当金、負債の部 """
    provision_for_shere_based_compensation_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='株式報酬引当金の増減（△）、営業活動によるキャッシュ・フロー')
    """ 株式報酬引当金の増減（△）、営業活動によるキャッシュ・フロー """
    retirement_of_treasury_stock_changes_during_period: Optional[IxNonFractionPublic] = Field(default=None, description='自己株式の消却、当期変動額')
    """ 自己株式の消却、当期変動額 """
    gain_on_sales_of_property_plant_and_equipment_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='有形固定資産売却益、営業活動によるキャッシュ・フロー')
    """ 有形固定資産売却益、営業活動によるキャッシュ・フロー """
    loss_on_sales_and_retirement_of_property_plant_and_equipment_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='有形固定資産除売却損、営業活動によるキャッシュ・フロー')
    """ 有形固定資産除売却損、営業活動によるキャッシュ・フロー """
    loss_on_cession_of_an_obligation_noe: Optional[IxNonFractionPublic] = Field(default=None, description='売掛債権譲渡損、営業外費用')
    """ 売掛債権譲渡損、営業外費用 """
    provision_for_compensation_ncl: Optional[IxNonFractionPublic] = Field(default=None, description='損害補償損失引当金、固定負債')
    """ 損害補償損失引当金、固定負債 """
    vending_machines_income_noi: Optional[IxNonFractionPublic] = Field(default=None, description='自動販売機収入、営業外収益')
    """ 自動販売機収入、営業外収益 """
    decrease_increase_in_bad_loans_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='固定化債権の増減額（△は増加）、営業活動によるキャッシュ・フロー')
    """ 固定化債権の増減額（△は増加）、営業活動によるキャッシュ・フロー """
    gain_on_sale_of_securities_of_other_subsidiaries_and_associates_ei: Optional[IxNonFractionPublic] = Field(default=None, description='その他の関係会社有価証券売却益、特別利益')
    """ その他の関係会社有価証券売却益、特別利益 """
    loss_gain_on_sale_of_securities_of_other_subsidiaries_and_associates_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='その他の関係会社有価証券売却損益（△は益）、営業活動によるキャッシュ・フロー')
    """ その他の関係会社有価証券売却損益（△は益）、営業活動によるキャッシュ・フロー """
    proceeds_from_sale_of_securities_of_other_subsidiaries_and_associates_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='その他の関係会社有価証券の売却による収入、投資活動によるキャッシュ・フロー')
    """ その他の関係会社有価証券の売却による収入、投資活動によるキャッシュ・フロー """
    accrued_retirement_benefits_for_directors_ncl: Optional[IxNonFractionPublic] = Field(default=None, description='未払役員退職慰労金、固定負債')
    """ 未払役員退職慰労金、固定負債 """
    investment_advisory_fee_noe: Optional[IxNonFractionPublic] = Field(default=None, description='投資顧問料、営業外費用')
    """ 投資顧問料、営業外費用 """
    demolition_and_removal_costs_el: Optional[IxNonFractionPublic] = Field(default=None, description='解体撤去費用、特別損失')
    """ 解体撤去費用、特別損失 """
    demolition_and_removal_costs_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='解体撤去費用、営業活動によるキャッシュ・フロー')
    """ 解体撤去費用、営業活動によるキャッシュ・フロー """
    expenses_for_demolition_and_removal_costs_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='解体撤去費用の支出、投資活動によるキャッシュ・フロー')
    """ 解体撤去費用の支出、投資活動によるキャッシュ・フロー """
    gain_on_sale_of_investment_in_affiliated_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='関係会社出資金売却による収入、投資活動によるキャッシュ・フロー')
    """ 関係会社出資金売却による収入、投資活動によるキャッシュ・フロー """
    gain_on_sale_of_investments_in_capital_of_subsidiaries_and_associates_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='関係会社出資金売却益、営業活動によるキャッシュ・フロー')
    """ 関係会社出資金売却益、営業活動によるキャッシュ・フロー """
    special_survey_costs_etc_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='特別調査費用等、営業活動によるキャッシュ・フロー')
    """ 特別調査費用等、営業活動によるキャッシュ・フロー """
    land_use_right_ia: Optional[IxNonFractionPublic] = Field(default=None, description='土地使用権、無形固定資産')
    """ 土地使用権、無形固定資産 """
    national_subsidies_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='国庫補助金、営業活動によるキャッシュ・フロー')
    """ 国庫補助金、営業活動によるキャッシュ・フロー """
    increase_decrease_in_net_defined_benefit_asset_and_lability_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='退職給付に係る資産及び負債の増減額、営業活動によるキャッシュ・フロー')
    """ 退職給付に係る資産及び負債の増減額、営業活動によるキャッシュ・フロー """
    increase_decrease_in_provision_for_loss_on_anti_monopoly_act_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='独占禁止法関連損失引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 独占禁止法関連損失引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    increase_decrease_in_provision_for_product_defect_compensation_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='製品補償引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 製品補償引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    provision_for_product_compensation_el: Optional[IxNonFractionPublic] = Field(default=None, description='製品補償引当金繰入額、特別損失')
    """ 製品補償引当金繰入額、特別損失 """
    provision_for_product_defect_compensation_ncl: Optional[IxNonFractionPublic] = Field(default=None, description='製品補償引当金、固定負債')
    """ 製品補償引当金、固定負債 """
    compensation_for_damage_income_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='受取損害賠償金、営業活動によるキャッシュ・フロー')
    """ 受取損害賠償金、営業活動によるキャッシュ・フロー """
    compensation_for_damage_income_received_ope_cf_fin_cf: Optional[IxNonFractionPublic] = Field(default=None, description='受取損害賠償金の受領額、営業活動によるキャッシュ・フロー又は投資活動によるキャッシュ・フロー')
    """ 受取損害賠償金の受領額、営業活動によるキャッシュ・フロー又は投資活動によるキャッシュ・フロー """
    provision_for_share_awards_for_employees_ncl: Optional[IxNonFractionPublic] = Field(default=None, description='従業員株式給付引当金、固定負債')
    """ 従業員株式給付引当金、固定負債 """
    provision_for_taxes_related_expenses_cl: Optional[IxNonFractionPublic] = Field(default=None, description='租税関連費用引当金、流動負債')
    """ 租税関連費用引当金、流動負債 """
    miscellaneous_expenses_of_assets_for_rent_noe: Optional[IxNonFractionPublic] = Field(default=None, description='貸与資産諸費用、営業外費用')
    """ 貸与資産諸費用、営業外費用 """
    paid_amount_of_bonus_for_directors_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='役員賞与の支払額、営業活動によるキャッシュ・フロー')
    """ 役員賞与の支払額、営業活動によるキャッシュ・フロー """
    right_of_use_assets_net_ppe: Optional[IxNonFractionPublic] = Field(default=None, description='使用権資産（純額）、有形固定資産')
    """ 使用権資産（純額）、有形固定資産 """
    incease_decrease_in_net_defined_benefit_asset_and_liability_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='退職給付に係る資産及び負債の増減額、営業活動によるキャッシュ・フロー')
    """ 退職給付に係る資産及び負債の増減額、営業活動によるキャッシュ・フロー """
    intersegment_revenue_and_transfers: Optional[IxNonFractionPublic] = Field(default=None, description='セグメント間の内部売上収益又は振替高')
    """ セグメント間の内部売上収益又は振替高 """
    revenue_from_external_customers: Optional[IxNonFractionPublic] = Field(default=None, description='外部顧客への売上収益')
    """ 外部顧客への売上収益 """
    gain_on_sales_of_investment_securities_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='投資有価証券売却益、営業活動によるキャッシュ・フロー')
    """ 投資有価証券売却益、営業活動によるキャッシュ・フロー """
    gain_on_sales_of_investments_in_capital_of_subsidiaries_and_associates_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='関係会社出資金売却益、営業活動によるキャッシュ・フロー')
    """ 関係会社出資金売却益、営業活動によるキャッシュ・フロー """
    increase_decrease_in_retirement_benefit_asset_or_liability_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='退職給付に係る資産又は負債の増減額、営業活動によるキャッシュ・フロー')
    """ 退職給付に係る資産又は負債の増減額、営業活動によるキャッシュ・フロー """
    loss_gain_on_sales_of_investment_in_capital_of_subsidiaries_and_associates_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='関係会社出資金売却損益（△は益）、営業活動によるキャッシュ・フロー')
    """ 関係会社出資金売却損益（△は益）、営業活動によるキャッシュ・フロー """
    loss_on_product_recall_el: Optional[IxNonFractionPublic] = Field(default=None, description='製品回収関連損失、特別損失')
    """ 製品回収関連損失、特別損失 """
    loss_on_sale_of_investment_in_affiliated_companies_el: Optional[IxNonFractionPublic] = Field(default=None, description='関係会社出資金売却損、特別損失')
    """ 関係会社出資金売却損、特別損失 """
    payments_for_sales_of_investments_in_capital_of_subsidiaries_resulting_in_change_in_scope_of_consolidation_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='連結の範囲の変更を伴う子会社出資金の売却による支出、投資活動によるキャッシュ・フロー')
    """ 連結の範囲の変更を伴う子会社出資金の売却による支出、投資活動によるキャッシュ・フロー """
    proceeds_from_governmental_subsideies_for_investment_in_property_and_equipment_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='設備投資助成金の受入による収入、投資活動によるキャッシュ・フロー')
    """ 設備投資助成金の受入による収入、投資活動によるキャッシュ・フロー """
    puschase_of_stocks_of_affiliates_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='関連会社株式の取得による支出、投資活動によるキャッシュ・フロー')
    """ 関連会社株式の取得による支出、投資活動によるキャッシュ・フロー """
    state_subsidy_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='国庫補助金、営業活動によるキャッシュ・フロー')
    """ 国庫補助金、営業活動によるキャッシュ・フロー """
    gain_on_cancellation_of_lease_obligations_ei: Optional[IxNonFractionPublic] = Field(default=None, description='リース債務解約益、特別利益')
    """ リース債務解約益、特別利益 """
    gain_on_forgiveness_of_lease_obligations_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='リース債務解約益、営業活動によるキャッシュ・フロー')
    """ リース債務解約益、営業活動によるキャッシュ・フロー """
    decrease_increase_in_guarantee_deposits_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='差入保証金の増減額（△は増加）、投資活動によるキャッシュ・フロー')
    """ 差入保証金の増減額（△は増加）、投資活動によるキャッシュ・フロー """
    restoration_cost_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='原状回復費用、営業活動によるキャッシュ・フロー')
    """ 原状回復費用、営業活動によるキャッシュ・フロー """
    restoration_costs_el: Optional[IxNonFractionPublic] = Field(default=None, description='原状回復費用、特別損失')
    """ 原状回復費用、特別損失 """
    gain_on_liquidation_of_subsidiaries_and_associates_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='関係会社清算益、営業活動によるキャッシュ・フロー')
    """ 関係会社清算益、営業活動によるキャッシュ・フロー """
    decrease_increase_in_deposits_for_purchase_of_treasury_shares_fin_cf: Optional[IxNonFractionPublic] = Field(default=None, description='自己株式取得のための預託金の増減額(△は増加)、財務活動によるキャッシュ・フロー')
    """ 自己株式取得のための預託金の増減額(△は増加)、財務活動によるキャッシュ・フロー """
    exepences_before_deduction_of_temporary_consumption_tax_payment_sga: Optional[IxNonFractionPublic] = Field(default=None, description='仮払消費税の未控除費用、販売費及び一般管理費')
    """ 仮払消費税の未控除費用、販売費及び一般管理費 """
    provision_for_loss_on_anti_monopoly_act_ncl: Optional[IxNonFractionPublic] = Field(default=None, description='独占禁止法関連損失引当金、固定負債')
    """ 独占禁止法関連損失引当金、固定負債 """
    loss_on_derivatives_trading_noe: Optional[IxNonFractionPublic] = Field(default=None, description='デリバティブ損失、営業外費用')
    """ デリバティブ損失、営業外費用 """
    advesory_cost: Optional[IxNonFractionPublic] = Field(default=None, description='アドバイザリー費用、特別損失')
    """ アドバイザリー費用、特別損失 """
    loss_on_cancellation_of_lease_agreements_noe: Optional[IxNonFractionPublic] = Field(default=None, description='差入保証金・敷金解約損、営業外費用')
    """ 差入保証金・敷金解約損、営業外費用 """
    net_decrease_increase_in_trust_beneficiary_right_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='信託受益権の純増減額（△は増加）、投資活動によるキャッシュ・フロー')
    """ 信託受益権の純増減額（△は増加）、投資活動によるキャッシュ・フロー """
    received_settlement_fee_ei: Optional[IxNonFractionPublic] = Field(default=None, description='受取解決金、特別利益')
    """ 受取解決金、特別利益 """
    received_settlement_fee_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='受取解決金、営業活動によるキャッシュ・フロー')
    """ 受取解決金、営業活動によるキャッシュ・フロー """
    the_receipt_of_settlement_fee_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='解決金の受取額、営業活動によるキャッシュ・フロー')
    """ 解決金の受取額、営業活動によるキャッシュ・フロー """
    commission_expenses_noe: Optional[IxNonFractionPublic] = Field(default=None, description='業務受託費用、営業外費用')
    """ 業務受託費用、営業外費用 """
    loss_on_sale_of_non_current_assets_open_cf: Optional[IxNonFractionPublic] = Field(default=None, description='固定資産売却損、営業活動によるキャッシュ・フロー')
    """ 固定資産売却損、営業活動によるキャッシュ・フロー """
    provision_for_executive_officers_retirement_benefits: Optional[IxNonFractionPublic] = Field(default=None, description='執行役員退職慰労引当金')
    """ 執行役員退職慰労引当金 """
    provision_for_stocks_payment_liabilities: Optional[IxNonFractionPublic] = Field(default=None, description='株式給付引当金、負債の部')
    """ 株式給付引当金、負債の部 """
    provision_for_share_based_remuneration: Optional[IxNonFractionPublic] = Field(default=None, description='株式給付引当金')
    """ 株式給付引当金 """
    increase_by_share_exchanges_changes_of_items_during_period: Optional[IxNonFractionPublic] = Field(default=None, description='株式交換による増加、当期変動額')
    """ 株式交換による増加、当期変動額 """
    provision_for_loss_on_cancellation_of_system_contracts_liabilities_bnk: Optional[IxNonFractionPublic] = Field(default=None, description='システム解約損失引当金、負債の部、銀行業')
    """ システム解約損失引当金、負債の部、銀行業 """
    provision_for_loss_on_cancellation_of_system_contracts_liabilities: Optional[IxNonFractionPublic] = Field(default=None, description='システム解約損失引当金、負債の部')
    """ システム解約損失引当金、負債の部 """
    reversal_of_provision_for_loss_on_cancellation_of_system_contracts_ei: Optional[IxNonFractionPublic] = Field(default=None, description='システム解約損失引当金戻入益、特別利益')
    """ システム解約損失引当金戻入益、特別利益 """
    transfer_to_other_capital_surplus_from_retained_earnings_brought_forward: Optional[IxNonFractionPublic] = Field(default=None, description='繰越利益剰余金からその他資本剰余金への振替')
    """ 繰越利益剰余金からその他資本剰余金への振替 """
    provision_of_reserve_for_cancellation_of_shares: Optional[IxNonFractionPublic] = Field(default=None, description='株式消却積立金の積立')
    """ 株式消却積立金の積立 """
    reserve_for_cancellation_of_shares: Optional[IxNonFractionPublic] = Field(default=None, description='株式消却積立金')
    """ 株式消却積立金 """
    balance_at_the_beginning_of_the_period_after_retroactive_processing: Optional[IxNonFractionPublic] = Field(default=None, description='遡及処理後当期首残高')
    """ 遡及処理後当期首残高 """
    atm_placement_fee_expenses_oebnk: Optional[IxNonFractionPublic] = Field(default=None, description='ＡＴＭ設置支払手数料、経常費用、銀行業')
    """ ＡＴＭ設置支払手数料、経常費用、銀行業 """
    atm_related_fee_expenses_oebnk: Optional[IxNonFractionPublic] = Field(default=None, description='ＡＴＭ支払手数料、経常費用、銀行業')
    """ ＡＴＭ支払手数料、経常費用、銀行業 """
    atm_related_fee_income_oibnk: Optional[IxNonFractionPublic] = Field(default=None, description='ＡＴＭ受入手数料、経常収益、銀行業')
    """ ＡＴＭ受入手数料、経常収益、銀行業 """
    atm_related_temporary_advances_liabilities_bnk: Optional[IxNonFractionPublic] = Field(default=None, description='ＡＴＭ仮受金、負債の部、銀行業')
    """ ＡＴＭ仮受金、負債の部、銀行業 """
    atm_related_temporary_payments_assets_bnk: Optional[IxNonFractionPublic] = Field(default=None, description='ＡＴＭ仮払金、資産の部、銀行業')
    """ ＡＴＭ仮払金、資産の部、銀行業 """
    accounts_payable_for_credit_card_business_liabilities: Optional[IxNonFractionPublic] = Field(default=None, description='クレジットカード事業未払金、負債の部')
    """ クレジットカード事業未払金、負債の部 """
    accounts_receivable_members_assets: Optional[IxNonFractionPublic] = Field(default=None, description='会員未収金、資産の部')
    """ 会員未収金、資産の部 """
    credit_card_operating_expense_oebnk: Optional[IxNonFractionPublic] = Field(default=None, description='クレジットカード業務経費、経常費用、銀行業')
    """ クレジットカード業務経費、経常費用、銀行業 """
    credit_card_operating_income_oibnk: Optional[IxNonFractionPublic] = Field(default=None, description='クレジットカード営業収入、経常収益、銀行業')
    """ クレジットカード営業収入、経常収益、銀行業 """
    decrease_increase_of_capital_surplus_by_change_of_share_to_consolidated_subsidiary: Optional[IxNonFractionPublic] = Field(default=None, description='連結子会社に対する持分変動に伴う資本剰余金の増減')
    """ 連結子会社に対する持分変動に伴う資本剰余金の増減 """
    deposits_for_electronic_money_liabilities: Optional[IxNonFractionPublic] = Field(default=None, description='電子マネー預り金、負債の部')
    """ 電子マネー預り金、負債の部 """
    electronic_money_operating_expense_oebnk: Optional[IxNonFractionPublic] = Field(default=None, description='電子マネー業務経費、経常費用、銀行業')
    """ 電子マネー業務経費、経常費用、銀行業 """
    electronic_money_operating_income_oibnk: Optional[IxNonFractionPublic] = Field(default=None, description='電子マネー営業収入、経常収益、銀行業')
    """ 電子マネー営業収入、経常収益、銀行業 """
    fluctuation_resulting_from_exclusion_of_equity_method_affiliates: Optional[IxNonFractionPublic] = Field(default=None, description='持分法適用会社の減少に伴う変動')
    """ 持分法適用会社の減少に伴う変動 """
    interest_expenses_segment_information: Optional[IxNonFractionPublic] = Field(default=None, description='資金調達費用、セグメント情報')
    """ 資金調達費用、セグメント情報 """
    interest_income_segment_information: Optional[IxNonFractionPublic] = Field(default=None, description='資金運用収益、セグメント情報')
    """ 資金運用収益、セグメント情報 """
    reserve_for_stocks_payment_liabilities: Optional[IxNonFractionPublic] = Field(default=None, description='株式給付引当金、負債の部')
    """ 株式給付引当金、負債の部 """
    provision_for_employee_stock_ownership_plan_trust_liabilities: Optional[IxNonFractionPublic] = Field(default=None, description='従業員株式給付引当金、負債の部')
    """ 従業員株式給付引当金、負債の部 """
    provision_for_management_board_benefit_trust_liabilities: Optional[IxNonFractionPublic] = Field(default=None, description='役員株式給付引当金、負債の部')
    """ 役員株式給付引当金、負債の部 """
    distributions_of_loss_on_silent_partnerships_noe: Optional[IxNonFractionPublic] = Field(default=None, description='匿名組合損益分配額、営業外費用')
    """ 匿名組合損益分配額、営業外費用 """
    other_operating_assets_ppe: Optional[IxNonFractionPublic] = Field(default=None, description='その他の営業資産、有形固定資産')
    """ その他の営業資産、有形固定資産 """
    provision_for_automobile_inspection_costs_ncl: Optional[IxNonFractionPublic] = Field(default=None, description='メンテナンス引当金、固定負債')
    """ メンテナンス引当金、固定負債 """
    operating_loan_receivables_ca: Optional[IxNonFractionPublic] = Field(default=None, description='営業貸付債権、流動資産')
    """ 営業貸付債権、流動資産 """
    other_operating_assets_ppelea: Optional[IxNonFractionPublic] = Field(default=None, description='その他の営業資産、有形固定資産、リース事業')
    """ その他の営業資産、有形固定資産、リース事業 """
    reserve_for_car_maintenance_ncl: Optional[IxNonFractionPublic] = Field(default=None, description='メンテナンス引当金、固定負債')
    """ メンテナンス引当金、固定負債 """
    commission_fee_rev_oa: Optional[IxNonFractionPublic] = Field(default=None, description='受取手数料、営業活動による収益の内訳')
    """ 受取手数料、営業活動による収益の内訳 """
    decrease_increase_in_operational_guarantee_deposits_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='営業保証金等の増減額（△は増加）、営業活動によるキャッシュ・フロー')
    """ 営業保証金等の増減額（△は増加）、営業活動によるキャッシュ・フロー """
    decrease_increase_in_other_operating_debentures_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='その他営業債権の増減額（△は増加）、営業活動によるキャッシュ・フロー')
    """ その他営業債権の増減額（△は増加）、営業活動によるキャッシュ・フロー """
    decrease_increase_in_purchased_receivables_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='買取債権の増減額（△は増加）、営業活動によるキャッシュ・フロー')
    """ 買取債権の増減額（△は増加）、営業活動によるキャッシュ・フロー """
    increase_decrease_in_reserve_for_insurance_policy_liabilities_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='保険契約準備金の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 保険契約準備金の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    insurance_expenses_cos_exp_oa: Optional[IxNonFractionPublic] = Field(default=None, description='保険費用、営業活動による費用・売上原価の内訳')
    """ 保険費用、営業活動による費用・売上原価の内訳 """
    insurance_revenue_rev_oa: Optional[IxNonFractionPublic] = Field(default=None, description='保険収益、営業活動による収益の内訳')
    """ 保険収益、営業活動による収益の内訳 """
    other_operating_debentures_ca: Optional[IxNonFractionPublic] = Field(default=None, description='その他営業債権、流動資産')
    """ その他営業債権、流動資産 """
    provision_for_management_board_benefit_trust_liabilities_bnk: Optional[IxNonFractionPublic] = Field(default=None, description='役員株式給付引当金、負債の部、銀行業')
    """ 役員株式給付引当金、負債の部、銀行業 """
    decrease_increase_in_futures_transaction_margin_customer_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='委託者先物取引差金の増減額（△は増加）、営業活動によるキャッシュ・フロー')
    """ 委託者先物取引差金の増減額（△は増加）、営業活動によるキャッシュ・フロー """
    equity_investments_in_properties_for_sale_ca: Optional[IxNonFractionPublic] = Field(default=None, description='営業出資金、流動資産')
    """ 営業出資金、流動資産 """
    land_held_for_development_ca: Optional[IxNonFractionPublic] = Field(default=None, description='開発用土地、流動資産')
    """ 開発用土地、流動資産 """
    long_term_non_recourse_loans_ncl: Optional[IxNonFractionPublic] = Field(default=None, description='ノンリコース長期借入金、固定負債')
    """ ノンリコース長期借入金、固定負債 """
    non_recourse_bonds_due_within_one_year_cl: Optional[IxNonFractionPublic] = Field(default=None, description='ノンリコース１年内償還予定の社債、流動負債')
    """ ノンリコース１年内償還予定の社債、流動負債 """
    non_recourse_bonds_ncl: Optional[IxNonFractionPublic] = Field(default=None, description='ノンリコース社債、固定負債')
    """ ノンリコース社債、固定負債 """
    payments_for_equity_transactions_with_non_controlling_shareholder_fin_cf: Optional[IxNonFractionPublic] = Field(default=None, description='非支配株主との資本取引による支出、財務活動によるキャッシュ・フロー')
    """ 非支配株主との資本取引による支出、財務活動によるキャッシュ・フロー """
    proceeds_from_lease_and_guarantee_deposits_received_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='預り敷金保証金の受入による収入、投資活動によるキャッシュ・フロー')
    """ 預り敷金保証金の受入による収入、投資活動によるキャッシュ・フロー """
    repayments_of_lease_and_guarantee_deposits_received_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='預り敷金保証金の返還による支出、投資活動によるキャッシュ・フロー')
    """ 預り敷金保証金の返還による支出、投資活動によるキャッシュ・フロー """
    short_term_non_recourse_loans_cl: Optional[IxNonFractionPublic] = Field(default=None, description='ノンリコース短期借入金、流動負債')
    """ ノンリコース短期借入金、流動負債 """
    current_portion_of_long_term_non_recourse_loans_payable_cl: Optional[IxNonFractionPublic] = Field(default=None, description='ノンリコース1年内返済予定長期借入金、流動負債')
    """ ノンリコース1年内返済予定長期借入金、流動負債 """
    current_portion_of_non_recourse_bonds_cl: Optional[IxNonFractionPublic] = Field(default=None, description='ノンリコース1年内償還予定社債、流動負債')
    """ ノンリコース1年内償還予定社債、流動負債 """
    lease_and_guarantee_deposited_ncl: Optional[IxNonFractionPublic] = Field(default=None, description='預り敷金及び保証金、固定負債')
    """ 預り敷金及び保証金、固定負債 """
    long_term_non_recourse_loans_payable_ncl: Optional[IxNonFractionPublic] = Field(default=None, description='ノンリコース長期借入金、固定負債')
    """ ノンリコース長期借入金、固定負債 """
    non_recourese_bonds_payable_ncl: Optional[IxNonFractionPublic] = Field(default=None, description='ノンリコース社債、固定負債')
    """ ノンリコース社債、固定負債 """
    repayment_of_long_term_non_recourse_loans_payable_fin_cf: Optional[IxNonFractionPublic] = Field(default=None, description='ノンリコース長期借入金の返済による支出、財務活動によるキャッシュ・フロー')
    """ ノンリコース長期借入金の返済による支出、財務活動によるキャッシュ・フロー """
    deposits_received_from_real_estate_specified_joint_enterprise_investment: Optional[IxNonFractionPublic] = Field(default=None, description='不動産特定共同事業出資受入金、流動負債')
    """ 不動産特定共同事業出資受入金、流動負債 """
    deposits_received_from_real_estate_specified_joint_enterprise_investment_ncl: Optional[IxNonFractionPublic] = Field(default=None, description='不動産特定共同事業出資受入金、固定負債')
    """ 不動産特定共同事業出資受入金、固定負債 """
    payables_under_fluidity_receivables_cl: Optional[IxNonFractionPublic] = Field(default=None, description='債権流動化債務、流動負債')
    """ 債権流動化債務、流動負債 """
    proceeds_from_deposits_received_from_real_estate_specified_joint_enterprise_investment_fin_cf: Optional[IxNonFractionPublic] = Field(default=None, description='不動産特定共同事業出資受入による収入、財務活動によるキャッシュ・フロー')
    """ 不動産特定共同事業出資受入による収入、財務活動によるキャッシュ・フロー """
    repayments_of_distribution_received_from_real_estate_specified_joint_enterprise_investment_fin_cf: Optional[IxNonFractionPublic] = Field(default=None, description='不動産特定共同事業出資返還による支出、財務活動によるキャッシュ・フロー')
    """ 不動産特定共同事業出資返還による支出、財務活動によるキャッシュ・フロー """
    loss_on_related_to_repair_work_el: Optional[IxNonFractionPublic] = Field(default=None, description='補修工事関連損失、特別損失')
    """ 補修工事関連損失、特別損失 """
    loss_on_related_to_repair_work_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='補修工事関連損失、営業活動によるキャッシュ・フロー')
    """ 補修工事関連損失、営業活動によるキャッシュ・フロー """
    payment_for_related_to_repair_work_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='補修工事関連支払額、営業活動によるキャッシュ・フロー')
    """ 補修工事関連支払額、営業活動によるキャッシュ・フロー """
    reversal_of_provision_for_loss_on_related_to_repair_work_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='補修工事関連損失引当金戻入額、営業活動によるキャッシュ・フロー')
    """ 補修工事関連損失引当金戻入額、営業活動によるキャッシュ・フロー """
    accounts_payable_trade_and_accounts_payable_for_construction_contracts_cl: Optional[IxNonFractionPublic] = Field(default=None, description='買掛金及び工事未払金、流動負債')
    """ 買掛金及び工事未払金、流動負債 """
    provision_for_loss_on_lease_business_ncl: Optional[IxNonFractionPublic] = Field(default=None, description='賃貸事業損失引当金、固定負債')
    """ 賃貸事業損失引当金、固定負債 """
    benefits_income_noi: Optional[IxNonFractionPublic] = Field(default=None, description='受取給付金、営業外収益')
    """ 受取給付金、営業外収益 """
    commission_for_a_financial_loan_noe: Optional[IxNonFractionPublic] = Field(default=None, description='財務手数料、営業外費用')
    """ 財務手数料、営業外費用 """
    decrease_increase_on_investments_in_silent_partnership_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='匿名組合出資金の増減額、営業活動によるキャッシュ・フロー')
    """ 匿名組合出資金の増減額、営業活動によるキャッシュ・フロー """
    gain_on_capital_reduction_with_compensation_of_subsidiaries_and_affiliates_ei: Optional[IxNonFractionPublic] = Field(default=None, description='関係会社有償減資払戻差益、特別利益')
    """ 関係会社有償減資払戻差益、特別利益 """
    gain_on_capital_reduction_with_compensation_of_subsidiaries_and_affiliates_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='関係会社有償減資払戻差益、営業活動によるキャッシュ・フロー')
    """ 関係会社有償減資払戻差益、営業活動によるキャッシュ・フロー """
    increase_decrease_in_lease_deposits_received_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='預り敷金の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 預り敷金の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    loss_on_liquidation_of_subsidiaries_and_affiliates_investments_el: Optional[IxNonFractionPublic] = Field(default=None, description='関係会社出資金清算損、特別損失')
    """ 関係会社出資金清算損、特別損失 """
    loss_on_liquidation_of_subsidiaries_and_affiliates_investments_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='関係会社出資金清算損、営業活動によるキャッシュ・フロー')
    """ 関係会社出資金清算損、営業活動によるキャッシュ・フロー """
    proceeds_from_capital_reduction_of_affiliated_company_stock_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='関係会社株式の有償減資による収入、投資活動によるキャッシュ・フロー')
    """ 関係会社株式の有償減資による収入、投資活動によるキャッシュ・フロー """
    proceeds_from_the_liquidation_of_subsidiaries_and_associates_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='関係会社の清算による収入、投資活動によるキャッシュ・フロー')
    """ 関係会社の清算による収入、投資活動によるキャッシュ・フロー """
    gain_on_cancellation_of_insurance_policies_noi: Optional[IxNonFractionPublic] = Field(default=None, description='保険解約益、営業外収益')
    """ 保険解約益、営業外収益 """
    proceeds_due_to_maturity_of_insurance_funds_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='保険積立金の返戻による収入、投資活動によるキャッシュ・フロー')
    """ 保険積立金の返戻による収入、投資活動によるキャッシュ・フロー """
    profit_loss_before_income_taxes_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='税金等調整前中間純利益又は税金等調整前中間純損失（△）、営業活動によるキャッシュ・フロー')
    """ 税金等調整前中間純利益又は税金等調整前中間純損失（△）、営業活動によるキャッシュ・フロー """
    allowance_for_construction_loss_cl: Optional[IxNonFractionPublic] = Field(default=None, description='工事損失引当金、流動負債')
    """ 工事損失引当金、流動負債 """
    increase_decrease_in_uneamed_fares_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='前受運賃の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 前受運賃の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    provision_for_dismantling_of_fixed_assets_cl: Optional[IxNonFractionPublic] = Field(default=None, description='解体費用引当金、流動負債')
    """ 解体費用引当金、流動負債 """
    reserve_for_dismantling_costs_ncl: Optional[IxNonFractionPublic] = Field(default=None, description='解体費用引当金、固定負債')
    """ 解体費用引当金、固定負債 """
    covid19_subsidies_noi: Optional[IxNonFractionPublic] = Field(default=None, description='新型コロナウイルス感染症対策補助金、営業外収益')
    """ 新型コロナウイルス感染症対策補助金、営業外収益 """
    proceeds_from_capital_reduction_of_affiliates_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='関係会社株式の有償減資による収入、投資活動によるキャッシュ・フロー')
    """ 関係会社株式の有償減資による収入、投資活動によるキャッシュ・フロー """
    increase_decrease_in_provision_for_loss_on_liquidation_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='整理損失引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 整理損失引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    provision_for_loss_on_liquidation_cl: Optional[IxNonFractionPublic] = Field(default=None, description='整理損失引当金、流動負債')
    """ 整理損失引当金、流動負債 """
    provision_for_loss_on_liquidation_ncl: Optional[IxNonFractionPublic] = Field(default=None, description='整理損失引当金、固定負債')
    """ 整理損失引当金、固定負債 """
    provision_for_redemption_of_gift_certificates_cl: Optional[IxNonFractionPublic] = Field(default=None, description='商品券等引換引当金、流動負債')
    """ 商品券等引換引当金、流動負債 """
    provision_for_return_of_subsidy_el: Optional[IxNonFractionPublic] = Field(default=None, description='助成金返還引当金繰入額、特別損失')
    """ 助成金返還引当金繰入額、特別損失 """
    trade_accounts_receivable_and_contract_assets_ca: Optional[IxNonFractionPublic] = Field(default=None, description='営業未収入金及び契約資産、流動資産')
    """ 営業未収入金及び契約資産、流動資産 """
    increase_decrease_in_retirement_benefits_asset_and_liability_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='退職給付に係る資産及び負債の増減額、営業活動によるキャッシュ・フロー')
    """ 退職給付に係る資産及び負債の増減額、営業活動によるキャッシュ・フロー """
    accumulated_depreciation_machinery_equipment_and_tools_furniture_and_fixtures_ppe: Optional[IxNonFractionPublic] = Field(default=None, description='減価償却累計額、機械装置及び工具器具備品、有形固定資産')
    """ 減価償却累計額、機械装置及び工具器具備品、有形固定資産 """
    machinery_equipment_and_tools_furniture_and_fixtures_net_ppe: Optional[IxNonFractionPublic] = Field(default=None, description='機械装置及び工具器具備品（純額）、有形固定資産')
    """ 機械装置及び工具器具備品（純額）、有形固定資産 """
    machinery_equipment_and_tools_furniture_and_fixtures_ppe: Optional[IxNonFractionPublic] = Field(default=None, description='機械装置及び工具器具備品、有形固定資産')
    """ 機械装置及び工具器具備品、有形固定資産 """
    provision_for_loss_on_business_of_subsidiaries_and_associates_noe: Optional[IxNonFractionPublic] = Field(default=None, description='関係会社事業損失引当金繰入額、営業外費用')
    """ 関係会社事業損失引当金繰入額、営業外費用 """
    provision_of_allowance_for_doubtful_accounts_for_subsidiaries_and_associates_noe: Optional[IxNonFractionPublic] = Field(default=None, description='関係会社貸倒引当金繰入額、営業外費用')
    """ 関係会社貸倒引当金繰入額、営業外費用 """
    subsidies_for_bus_ei: Optional[IxNonFractionPublic] = Field(default=None, description='車両等購入補助金、特別利益')
    """ 車両等購入補助金、特別利益 """
    notes_and_accounts_receivable_trade_and_contract_assets_ca: Optional[IxNonFractionPublic] = Field(default=None, description='受取手形、営業未収金及び契約資産、流動資産')
    """ 受取手形、営業未収金及び契約資産、流動資産 """
    decrease_increase_accruned_consumption_tax_refund_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='未収還付消費税の増減額（△は増加）、営業活動によるキャッシュ・フロー')
    """ 未収還付消費税の増減額（△は増加）、営業活動によるキャッシュ・フロー """
    proceeds_from_long_term_accounts_payable_other_fin_cf: Optional[IxNonFractionPublic] = Field(default=None, description='長期未払金の増加による収入、財務活動によるキャッシュ・フロー')
    """ 長期未払金の増加による収入、財務活動によるキャッシュ・フロー """
    depreciation_cos: Optional[IxNonFractionPublic] = Field(default=None, description='減価償却費、売上原価')
    """ 減価償却費、売上原価 """
    direct_operation_expense_cos: Optional[IxNonFractionPublic] = Field(default=None, description='作業直接費、売上原価')
    """ 作業直接費、売上原価 """
    notes_and_operation_accounts_receivable_trade_and_contract_assets: Optional[IxNonFractionPublic] = Field(default=None, description='受取手形、営業未収金及び契約資産')
    """ 受取手形、営業未収金及び契約資産 """
    port_terminal_operation_rev_oa: Optional[IxNonFractionPublic] = Field(default=None, description='港湾作業料、営業活動による収益')
    """ 港湾作業料、営業活動による収益 """
    rent_expenses_cos: Optional[IxNonFractionPublic] = Field(default=None, description='賃借料、売上原価')
    """ 賃借料、売上原価 """
    salaries_and_allowances_cos: Optional[IxNonFractionPublic] = Field(default=None, description='給料及び手当、売上原価')
    """ 給料及び手当、売上原価 """
    expenses_related_to_the100th_anniversary_of_foundation_el: Optional[IxNonFractionPublic] = Field(default=None, description='創業100周年記念関連費用、特別損失')
    """ 創業100周年記念関連費用、特別損失 """
    buildings_and_structures_in_trust_net: Optional[IxNonFractionPublic] = Field(default=None, description='信託建物及び信託構築物（純額）')
    """ 信託建物及び信託構築物（純額） """
    decrease_increase_in_deferred_and_prepaid_expenses_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='繰延及び前払費用の増減額（△は増加）、営業活動によるキャッシュ・フロー')
    """ 繰延及び前払費用の増減額（△は増加）、営業活動によるキャッシュ・フロー """
    decrease_increase_in_notes_and_accounts_receivable_contract_assets_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='契約資産の増減額（△は増加）、営業活動によるキャッシュ・フロー')
    """ 契約資産の増減額（△は増加）、営業活動によるキャッシュ・フロー """
    cost_of_sale_of_goods_noe: Optional[IxNonFractionPublic] = Field(default=None, description='物品売却費用、営業外費用')
    """ 物品売却費用、営業外費用 """
    decrease_increase_in_deposits_pledged_as_collateral_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='担保に供している預金の増減額（△は増加）、投資活動によるキャッシュ・フロー')
    """ 担保に供している預金の増減額（△は増加）、投資活動によるキャッシュ・フロー """
    landfills_net_ppe: Optional[IxNonFractionPublic] = Field(default=None, description='最終処分場（純額）、有形固定資産')
    """ 最終処分場（純額）、有形固定資産 """
    loss_gain_on_valuation_of_currency_swaps_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='通貨スワップ評価損益（△は益）、営業活動によるキャッシュ・フロー')
    """ 通貨スワップ評価損益（△は益）、営業活動によるキャッシュ・フロー """
    proceeds_on_sales_of_goods_noi: Optional[IxNonFractionPublic] = Field(default=None, description='物品売却収入、営業外収益')
    """ 物品売却収入、営業外収益 """
    provision_of_allowance_for_doubtful_accounts_of_golf_club_membership_noe: Optional[IxNonFractionPublic] = Field(default=None, description='ゴルフ会員権貸倒引当金繰入額、営業外費用')
    """ ゴルフ会員権貸倒引当金繰入額、営業外費用 """
    trade_notes_and_accounts_receivable_trade_and_contract_assets: Optional[IxNonFractionPublic] = Field(default=None, description='受取手形、営業未収入金及び契約資産')
    """ 受取手形、営業未収入金及び契約資産 """
    increase_decrease_in_provision_for_removal_expenses_of_non_current_assets_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='固定資産撤去費用引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 固定資産撤去費用引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    program_rights_and_work_in_process: Optional[IxNonFractionPublic] = Field(default=None, description='番組及び仕掛品')
    """ 番組及び仕掛品 """
    removal_expenses_of_non_current_assets_el: Optional[IxNonFractionPublic] = Field(default=None, description='固定資産撤去費、 特別損失')
    """ 固定資産撤去費、 特別損失 """
    provision_for_gas_appliance_warranties_ncl: Optional[IxNonFractionPublic] = Field(default=None, description='器具保証引当金、固定負債')
    """ 器具保証引当金、固定負債 """
    allowance_for_withdrawal_of_business_ncl: Optional[IxNonFractionPublic] = Field(default=None, description='事業撤退損失引当金、固定負債')
    """ 事業撤退損失引当金、固定負債 """
    loss_on_withdrawal_of_business_el: Optional[IxNonFractionPublic] = Field(default=None, description='事業撤退損失、特別損失')
    """ 事業撤退損失、特別損失 """
    loss_on_withdrawal_of_business_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='事業撤退損失、営業活動によるキャッシュ・フロー')
    """ 事業撤退損失、営業活動によるキャッシュ・フロー """
    business_restructuring_expenses_noe: Optional[IxNonFractionPublic] = Field(default=None, description='事業構造改善費用、営業外費用')
    """ 事業構造改善費用、営業外費用 """
    content_production_account_ca: Optional[IxNonFractionPublic] = Field(default=None, description='コンテンツ制作勘定、流動資産')
    """ コンテンツ制作勘定、流動資産 """
    provision_for_office_relocation_ncl: Optional[IxNonFractionPublic] = Field(default=None, description='事務所退去費用引当金、固定負債')
    """ 事務所退去費用引当金、固定負債 """
    relocation_related_costs_noe: Optional[IxNonFractionPublic] = Field(default=None, description='移転関連費用、営業外費用')
    """ 移転関連費用、営業外費用 """
    cost_of_food_and_beverage_cos: Optional[IxNonFractionPublic] = Field(default=None, description='飲食売上原価、売上原価')
    """ 飲食売上原価、売上原価 """
    facility_rent_income_rev_oa: Optional[IxNonFractionPublic] = Field(default=None, description='施設利用料収入、営業活動による収益')
    """ 施設利用料収入、営業活動による収益 """
    office_shop_rent_income_rev_oa: Optional[IxNonFractionPublic] = Field(default=None, description='家賃収入、営業活動による収益')
    """ 家賃収入、営業活動による収益 """
    sales_of_food_and_beverage_rev_oa: Optional[IxNonFractionPublic] = Field(default=None, description='飲食売上高、営業活動による収益')
    """ 飲食売上高、営業活動による収益 """
    rent_income_of_real_estate_noi: Optional[IxNonFractionPublic] = Field(default=None, description='不動産賃貸収入、営業外収益')
    """ 不動産賃貸収入、営業外収益 """
    acquisitions_of_subsidiaries_accompanied_with_change_in_scope_of_consolidation_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='連結の範囲の変更を伴う子会社株式の取得、投資活動によるキャッシュ・フロー')
    """ 連結の範囲の変更を伴う子会社株式の取得、投資活動によるキャッシュ・フロー """
    call_loan_ca: Optional[IxNonFractionPublic] = Field(default=None, description='コールローン、流動資産')
    """ コールローン、流動資産 """
    cash_deposits_for_cash_collection_and_deposit_services_ca: Optional[IxNonFractionPublic] = Field(default=None, description='現金護送業務用現金及び預金、流動資産')
    """ 現金護送業務用現金及び預金、流動資産 """
    damage_insurance_claim_gain_ei: Optional[IxNonFractionPublic] = Field(default=None, description='受取損害保険金、特別利益')
    """ 受取損害保険金、特別利益 """
    damage_insurance_claim_gain_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='受取損害保険金、営業活動によるキャッシュ・フロー')
    """ 受取損害保険金、営業活動によるキャッシュ・フロー """
    decrease_increase_in_investment_deposits_by_policyholders_unearned_premiums_and_other_insurance_liabilities_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='保険契約準備金の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 保険契約準備金の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    decrease_increase_in_net_defined_benefit_asset_and_liability_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='退職給付に係る負債及び資産の増減額、営業活動によるキャッシュ・フロー')
    """ 退職給付に係る負債及び資産の増減額、営業活動によるキャッシュ・フロー """
    deferred_revenue_cl: Optional[IxNonFractionPublic] = Field(default=None, description='前受契約料、流動負債')
    """ 前受契約料、流動負債 """
    deposits_received_for_cash_collection_and_deposit_services_cl: Optional[IxNonFractionPublic] = Field(default=None, description='現金護送業務用預り金、流動負債')
    """ 現金護送業務用預り金、流動負債 """
    dismantlement_expenses_el: Optional[IxNonFractionPublic] = Field(default=None, description='解体撤去費用、特別損失')
    """ 解体撤去費用、特別損失 """
    due_from_subscribers_ca: Optional[IxNonFractionPublic] = Field(default=None, description='未収契約料、流動資産')
    """ 未収契約料、流動資産 """
    gain_on_reversal_of_allowance_for_doubtful_accounts_ei: Optional[IxNonFractionPublic] = Field(default=None, description='貸倒引当金戻入益、特別利益')
    """ 貸倒引当金戻入益、特別利益 """
    increase_decrease_in_cash_deposits_for_cash_collection_and_deposit_services_and_deposits_received_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='現金護送業務用現金預金及び預り金の増減額、営業活動によるキャッシュ・フロー')
    """ 現金護送業務用現金預金及び預り金の増減額、営業活動によるキャッシュ・フロー """
    increase_decrease_in_deferred_revenue_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='前受契約料の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 前受契約料の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    long_term_deferred_revenue_ncl: Optional[IxNonFractionPublic] = Field(default=None, description='長期前受契約料、固定負債')
    """ 長期前受契約料、固定負債 """
    loss_on_disposal_of_fixed_assets_noe: Optional[IxNonFractionPublic] = Field(default=None, description='固定資産売却廃棄損、営業外費用')
    """ 固定資産売却廃棄損、営業外費用 """
    net_loss_gain_on_sales_and_disposal_of_assets_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='固定資産売却損益及び廃棄損益（△は益）、営業活動によるキャッシュ・フロー')
    """ 固定資産売却損益及び廃棄損益（△は益）、営業活動によるキャッシュ・フロー """
    payments_for_sales_of_shares_of_subsidiaries_resulting_in_change_in_scope_of_consolidation: Optional[IxNonFractionPublic] = Field(default=None, description='連結の範囲の変更を伴う子会社株式の売却')
    """ 連結の範囲の変更を伴う子会社株式の売却 """
    proceeds_from_damage_insurance_income_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='損害保険金の受取額、営業活動によるキャッシュ・フロー')
    """ 損害保険金の受取額、営業活動によるキャッシュ・フロー """
    purchase_of_stocks_of_affiliates_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='関連会社株式の取得による支出、投資活動によるキャッシュ・フロー')
    """ 関連会社株式の取得による支出、投資活動によるキャッシュ・フロー """
    security_equipment_and_control_stations_net_ppe: Optional[IxNonFractionPublic] = Field(default=None, description='警報機器及び設備（純額）、有形固定資産')
    """ 警報機器及び設備（純額）、有形固定資産 """
    long_term_lease_and_guarantee_deposits_ncl: Optional[IxNonFractionPublic] = Field(default=None, description='預り敷金保証金、固定負債')
    """ 預り敷金保証金、固定負債 """
    loss_on_cancellation_of_rental_contracts_noe: Optional[IxNonFractionPublic] = Field(default=None, description='賃貸借解約損、営業外費用')
    """ 賃貸借解約損、営業外費用 """
    settlement_money_noe: Optional[IxNonFractionPublic] = Field(default=None, description='解決金、営業外費用')
    """ 解決金、営業外費用 """
    construction_material_ca: Optional[IxNonFractionPublic] = Field(default=None, description='建設機材、流動資産')
    """ 建設機材、流動資産 """
    subsidy_refund_amount_noe: Optional[IxNonFractionPublic] = Field(default=None, description='助成金返還額、営業外費用')
    """ 助成金返還額、営業外費用 """
    provision_for_loss_on_disaster_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='災害損失引当金繰入額、営業活動によるキャッシュ・フロー')
    """ 災害損失引当金繰入額、営業活動によるキャッシュ・フロー """
    accounts_payable_for_construction_contracts: Optional[IxNonFractionPublic] = Field(default=None, description='工事未払金')
    """ 工事未払金 """
    accounts_receivable_from_completed_construction_contracts: Optional[IxNonFractionPublic] = Field(default=None, description='完成工事未収入金')
    """ 完成工事未収入金 """
    advances_received_on_construction_contracts_in_progress: Optional[IxNonFractionPublic] = Field(default=None, description='未成工事受入金')
    """ 未成工事受入金 """
    costs_on_construction_contracts_in_progress: Optional[IxNonFractionPublic] = Field(default=None, description='未成工事支出金')
    """ 未成工事支出金 """
    decrease_increase_in_inventories_and_advance_payments_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='棚卸資産及び前渡金の増減額（△は増加）、営業活動によるキャッシュ・フロー')
    """ 棚卸資産及び前渡金の増減額（△は増加）、営業活動によるキャッシュ・フロー """
    rent_expenses_on_real_estates_for_investment_noe: Optional[IxNonFractionPublic] = Field(default=None, description='投資不動産賃貸費用、営業外費用')
    """ 投資不動産賃貸費用、営業外費用 """
    provision_for_loss_on_project_contracts_cl: Optional[IxNonFractionPublic] = Field(default=None, description='プロジェクト損失引当金、流動負債')
    """ プロジェクト損失引当金、流動負債 """
    royalty_noe: Optional[IxNonFractionPublic] = Field(default=None, description='支払技術料、営業外費用')
    """ 支払技術料、営業外費用 """
    non_deductionable_consumption_tax_noe: Optional[IxNonFractionPublic] = Field(default=None, description='控除対象外消費税等、営業外費用')
    """ 控除対象外消費税等、営業外費用 """
    ritairemennt_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='役員退職慰労未払金の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 役員退職慰労未払金の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    decrease_increase_in_business_guaranty_money_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='営業保証金の増減額（△は増加）、営業活動によるキャッシュ・フロー')
    """ 営業保証金の増減額（△は増加）、営業活動によるキャッシュ・フロー """
    loss_on_removal_of_fixed_assets_el: Optional[IxNonFractionPublic] = Field(default=None, description='固定資産撤去費用、特別損失')
    """ 固定資産撤去費用、特別損失 """
    loss_on_removal_of_fixed_assets_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='有形固定資産撤去費用、営業活動によるキャッシュ・フロー')
    """ 有形固定資産撤去費用、営業活動によるキャッシュ・フロー """
    compensation_for_damage_income_received_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='損害賠償金の受取額、営業活動によるキャッシュ・フロー')
    """ 損害賠償金の受取額、営業活動によるキャッシュ・フロー """
    increase_decrease_in_provision_for_share_based_remuneration_for_employee_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='従業員株式給付引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー')
    """ 従業員株式給付引当金の増減額（△は減少）、営業活動によるキャッシュ・フロー """
    provision_for_share_based_remuneration_for_employee_ncl: Optional[IxNonFractionPublic] = Field(default=None, description='従業員株式給付引当金、固定負債')
    """ 従業員株式給付引当金、固定負債 """
    increase_decrease_in_provision_for_provision_for_performance_linked_incentive_compensation_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='業績連動報酬引当金の増減額(△は減少)、営業活動によるキャッシュ・フロー')
    """ 業績連動報酬引当金の増減額(△は減少)、営業活動によるキャッシュ・フロー """
    proceeds_from_disposal_of_treasury_shares_resulting_from_exercise_of_share_acquisition_rights_fin_cf: Optional[IxNonFractionPublic] = Field(default=None, description='新株予約権の行使による自己株式の処分による収入、財務活動によるキャッシュ・フロー')
    """ 新株予約権の行使による自己株式の処分による収入、財務活動によるキャッシュ・フロー """
    provision_for_performance_linked_incentive_compensation_ncl: Optional[IxNonFractionPublic] = Field(default=None, description='業績連動報酬引当金、固定負債')
    """ 業績連動報酬引当金、固定負債 """
    repayment_income_noi: Optional[IxNonFractionPublic] = Field(default=None, description='受取弁済金、営業外収益')
    """ 受取弁済金、営業外収益 """
    allowance_for_employee_stock_benefits_ncl: Optional[IxNonFractionPublic] = Field(default=None, description='従業員株式給付引当金、固定負債')
    """ 従業員株式給付引当金、固定負債 """
    employment_levy_system_for_persons_with_disabilities_noe: Optional[IxNonFractionPublic] = Field(default=None, description='障害者雇用納付金、営業外費用')
    """ 障害者雇用納付金、営業外費用 """
    payments_for_purchase_of_treasury_subscription_right_to_shares_fin_cf: Optional[IxNonFractionPublic] = Field(default=None, description='自己新株予約権の取得による支出、財務活動によるキャッシュ・フロー')
    """ 自己新株予約権の取得による支出、財務活動によるキャッシュ・フロー """
    settlement_received_noi: Optional[IxNonFractionPublic] = Field(default=None, description='受取和解金、営業外収益')
    """ 受取和解金、営業外収益 """
    purchase_of_shares_of_associates_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='関連会社株式の取得による支出、投資活動によるキャッシュ・フロー')
    """ 関連会社株式の取得による支出、投資活動によるキャッシュ・フロー """
    consignment_income_from_research_and_development_noi: Optional[IxNonFractionPublic] = Field(default=None, description='受託研究収入、営業外収益')
    """ 受託研究収入、営業外収益 """
    net_increase_decrease_in_restrictions_on_bank_deposit_withdrawals_fin_cf: Optional[IxNonFractionPublic] = Field(default=None, description='引出制限付預金の純増減額（△は増加）、財務活動によるキャッシュ・フロー')
    """ 引出制限付預金の純増減額（△は増加）、財務活動によるキャッシュ・フロー """
    expense_of_inactive_noncurrent_assets_noe: Optional[IxNonFractionPublic] = Field(default=None, description='生産休止費用、営業外費用')
    """ 生産休止費用、営業外費用 """
    interest_expenses_and_guarantee_commission_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='支払利息及び支払保証料、営業活動によるキャッシュ・フロー')
    """ 支払利息及び支払保証料、営業活動によるキャッシュ・フロー """
    interest_expenses_and_guarantee_commission_paid_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='利息及び保証料の支払額、営業活動によるキャッシュ・フロー')
    """ 利息及び保証料の支払額、営業活動によるキャッシュ・フロー """
    various_cost_according_to_factory_stop_noe: Optional[IxNonFractionPublic] = Field(default=None, description='工場休止に伴う諸費用、営業外費用')
    """ 工場休止に伴う諸費用、営業外費用 """
    provision_for_removal_loss_cl: Optional[IxNonFractionPublic] = Field(default=None, description='撤去損失引当金、流動負債')
    """ 撤去損失引当金、流動負債 """
    shareholder_benefit_program_noe: Optional[IxNonFractionPublic] = Field(default=None, description='株主優待費用、営業外費用')
    """ 株主優待費用、営業外費用 """
    decrease_increase_in_advance_payment_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='前払金の増減額（△は増加）、営業活動によるキャッシュ・フロー')
    """ 前払金の増減額（△は増加）、営業活動によるキャッシュ・フロー """
    non_operating_commission_fee_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='営業外支払手数料、営業活動によるキャッシュ・フロー')
    """ 営業外支払手数料、営業活動によるキャッシュ・フロー """
    payment_of_non_operating_commission_fee_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='営業外支払手数料の支払額、営業活動によるキャッシュ・フロー')
    """ 営業外支払手数料の支払額、営業活動によるキャッシュ・フロー """
    tax_refund_noi: Optional[IxNonFractionPublic] = Field(default=None, description='租税公課還付金、営業外収益')
    """ 租税公課還付金、営業外収益 """
    expenses_on_interest_subsidy_noi: Optional[IxNonFractionPublic] = Field(default=None, description='利子補給金、営業外収益')
    """ 利子補給金、営業外収益 """
    payments_into_periodical_deposits_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='定期積金の預入による支出、投資活動によるキャッシュ・フロー')
    """ 定期積金の預入による支出、投資活動によるキャッシュ・フロー """
    notes_and_accounts_payable_trade_and_contract_liabilities_cl: Optional[IxNonFractionPublic] = Field(default=None, description='支払手形、買掛金及び契約負債、流動負債')
    """ 支払手形、買掛金及び契約負債、流動負債 """
    provision_for_loss_on_anti_monopoly_act_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='独占禁止法関連損失、営業活動によるキャッシュ・フロー')
    """ 独占禁止法関連損失、営業活動によるキャッシュ・フロー """
    provision_for_loss_on_anti_monopoly_act_paid_ope_cf: Optional[IxNonFractionPublic] = Field(default=None, description='独占禁止法関連支払額、営業活動によるキャッシュ・フロー')
    """ 独占禁止法関連支払額、営業活動によるキャッシュ・フロー """
    consulting_income_noi: Optional[IxNonFractionPublic] = Field(default=None, description='コンサルティング収入、営業外収益')
    """ コンサルティング収入、営業外収益 """
    payments_from_collection_of_loans_receivable_from_directors_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='役員に対する貸付による支出、投資活動によるキャッシュ・フロー')
    """ 役員に対する貸付による支出、投資活動によるキャッシュ・フロー """
    proceeds_from_collection_of_loans_receivable_from_directors_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='役員に対する貸付金の回収による収入、投資活動によるキャッシュ・フロー')
    """ 役員に対する貸付金の回収による収入、投資活動によるキャッシュ・フロー """
    proceeds_from_sale_of_investment_securities_and_others_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='投資有価証券等の売却による収入、投資活動によるキャッシュ・フロー')
    """ 投資有価証券等の売却による収入、投資活動によるキャッシュ・フロー """
    purchase_of_investment_securities_and_others_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='投資有価証券等の取得による支出、投資活動によるキャッシュ・フロー')
    """ 投資有価証券等の取得による支出、投資活動によるキャッシュ・フロー """
    bounty_for_early_payments_sga: Optional[IxNonFractionPublic] = Field(default=None, description='完納奨励金、販売費及び一般管理費')
    """ 完納奨励金、販売費及び一般管理費 """
    bounty_for_suppliers_sga: Optional[IxNonFractionPublic] = Field(default=None, description='出荷奨励金、販売費及び一般管理費')
    """ 出荷奨励金、販売費及び一般管理費 """
    rent_of_the_markets_base_on_sales_sga: Optional[IxNonFractionPublic] = Field(default=None, description='売上高割市場使用料、販売費及び一般管理費')
    """ 売上高割市場使用料、販売費及び一般管理費 """
    collection_of_cooperation_money_of_cemetery_development_inv_cf: Optional[IxNonFractionPublic] = Field(default=None, description='霊園開発協力金の回収、投資活動によるキャッシュ・フロー')
    """ 霊園開発協力金の回収、投資活動によるキャッシュ・フロー """
    cooperation_money_o_fcemetery_development_ioa: Optional[IxNonFractionPublic] = Field(default=None, description='霊園開発協力金、投資その他の資産')
    """ 霊園開発協力金、投資その他の資産 """
    permanent_using_right_ca: Optional[IxNonFractionPublic] = Field(default=None, description='永代使用権、流動資産')
    """ 永代使用権、流動資産 """
    sales_incentive_income_noi: Optional[IxNonFractionPublic] = Field(default=None, description='受取販売奨励金、営業外収益')
    """ 受取販売奨励金、営業外収益 """
    antique_ppe: Optional[IxNonFractionPublic] = Field(default=None, description='美術骨董品、有形固定資産')
    """ 美術骨董品、有形固定資産 """
    net_increase_decrease_in_guarantee_deposits_received_fin_cf: Optional[IxNonFractionPublic] = Field(default=None, description='預り保証金の純増減額(△は減少)、財務活動によるキャッシュ・フロー')
    """ 預り保証金の純増減額(△は減少)、財務活動によるキャッシュ・フロー """
    current_portion_of_long_term_loans_payable_cl: Optional[IxNonFractionPublic] = Field(default=None, description='一年内返済予定長期借入金、流動負債')
    """ 一年内返済予定長期借入金、流動負債 """

