from app.models import Field, SQLModel
from app.schema.ix_non_fraction import IxNonFractionPublic
from typing import Optional

class IxNonFractionEdif(SQLModel):
    average_number_of_shares: Optional[IxNonFractionPublic] = Field(default=None, description='期中平均株式数')
    """ 期中平均株式数 """
    basic_earnings_per_share_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='基本的1株当たり当期利益、IFRS')
    """ 基本的1株当たり当期利益、IFRS """
    cash_and_cash_equivalents_at_end_of_period_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='現金及び現金同等物期末残高、IFRS')
    """ 現金及び現金同等物期末残高、IFRS """
    cash_flows_from_financing_activities_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='財務活動によるキャッシュ・フロー、IFRS')
    """ 財務活動によるキャッシュ・フロー、IFRS """
    cash_flows_from_investing_activities_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='投資活動によるキャッシュ・フロー、IFRS')
    """ 投資活動によるキャッシュ・フロー、IFRS """
    cash_flows_from_operating_activities_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='営業活動によるキャッシュ・フロー、IFRS')
    """ 営業活動によるキャッシュ・フロー、IFRS """
    change_in_net_sales_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='増減率、売上高、IFRS')
    """ 増減率、売上高、IFRS """
    change_in_operating_income_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='増減率、営業利益、IFRS')
    """ 増減率、営業利益、IFRS """
    change_in_profit_attributable_to_owners_of_parent_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='増減率、親会社の所有者に帰属する当期利益、IFRS')
    """ 増減率、親会社の所有者に帰属する当期利益、IFRS """
    change_in_profit_before_tax_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='増減率、税引前利益、IFRS')
    """ 増減率、税引前利益、IFRS """
    change_in_profit_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='増減率、当期利益、IFRS')
    """ 増減率、当期利益、IFRS """
    change_in_revenue_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='増減率、収益、IFRS')
    """ 増減率、収益、IFRS """
    change_in_sales_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='増減率、売上収益、IFRS')
    """ 増減率、売上収益、IFRS """
    changes_in_total_comprehensive_income_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='当期包括利益合計額増減率、IFRS')
    """ 当期包括利益合計額増減率、IFRS """
    diluted_earnings_per_share_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='希薄化後1株当たり当期利益、IFRS')
    """ 希薄化後1株当たり当期利益、IFRS """
    dividend_per_share: Optional[IxNonFractionPublic] = Field(default=None, description='1株当たり配当金')
    """ 1株当たり配当金 """
    equity_attributable_to_owners_of_parent_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='親会社の所有者に帰属する持分（IFRS）')
    """ 親会社の所有者に帰属する持分（IFRS） """
    equity_attributable_to_owners_of_parent_per_share_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='1株当たり親会社所有者帰属持分、IFRS')
    """ 1株当たり親会社所有者帰属持分、IFRS """
    equity_attributable_to_owners_of_parent_to_total_assets_ratio_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='親会社所有者帰属持分比率、IFRS')
    """ 親会社所有者帰属持分比率、IFRS """
    investments_accounted_for_using_equity_method_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='持分法で会計処理されている投資（IFRS）')
    """ 持分法で会計処理されている投資（IFRS） """
    net_sales_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='売上高、IFRS')
    """ 売上高、IFRS """
    number_of_issued_and_outstanding_shares_at_the_end_of_fiscal_year_including_treasury_stock: Optional[IxNonFractionPublic] = Field(default=None, description='期末発行済株式数（自己株式を含む）')
    """ 期末発行済株式数（自己株式を含む） """
    number_of_subsidiaries_excluded_from_consolidation_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='除外、IFRS')
    """ 除外、IFRS """
    number_of_subsidiaries_newly_consolidated_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='新規、IFRS')
    """ 新規、IFRS """
    number_of_treasury_stock_at_the_end_of_fiscal_year: Optional[IxNonFractionPublic] = Field(default=None, description='期末自己株式数')
    """ 期末自己株式数 """
    operating_income_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='営業利益、IFRS')
    """ 営業利益、IFRS """
    operating_income_to_sales_ratio_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='売上収益営業利益率、IFRS')
    """ 売上収益営業利益率、IFRS """
    payout_ratio_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='配当性向、IFRS')
    """ 配当性向、IFRS """
    profit_attributable_to_owners_of_parent_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='親会社の所有者に帰属する当期利益、IFRS')
    """ 親会社の所有者に帰属する当期利益、IFRS """
    profit_before_tax_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='税引前利益、IFRS')
    """ 税引前利益、IFRS """
    profit_before_tax_to_total_assets_ratio_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='資産合計税引前利益率、IFRS')
    """ 資産合計税引前利益率、IFRS """
    profit_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='当期利益、IFRS')
    """ 当期利益、IFRS """
    profit_to_equity_attributable_to_owners_of_parent_ratio_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='親会社所有者帰属持分当期利益率、IFRS')
    """ 親会社所有者帰属持分当期利益率、IFRS """
    quarterly_period: Optional[IxNonFractionPublic] = Field(default=None, description='四半期')
    """ 四半期 """
    ratio_of_total_amount_of_dividends_to_equity_attributable_to_owner_of_parent_consolidated_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='親会社所有者帰属持分配当率（連結）、IFRS')
    """ 親会社所有者帰属持分配当率（連結）、IFRS """
    revenue_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='収益、IFRS')
    """ 収益、IFRS """
    sales_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='売上収益、IFRS')
    """ 売上収益、IFRS """
    total_assets_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='資産合計、IFRS')
    """ 資産合計、IFRS """
    total_comprehensive_income_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='当期包括利益合計額、IFRS')
    """ 当期包括利益合計額、IFRS """
    total_dividend_paid_annual: Optional[IxNonFractionPublic] = Field(default=None, description='配当金総額（合計）')
    """ 配当金総額（合計） """
    total_equity_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='資本合計、IFRS')
    """ 資本合計、IFRS """

