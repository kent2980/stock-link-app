from app.models import Field, SQLModel
from app.schema.ix_non_fraction import IxNonFractionPublic
from typing import Optional

class IxNonFractionEdjpSm(SQLModel):
    average_number_of_shares: Optional[IxNonFractionPublic] = Field(default=None, description='期中平均株式数')
    """ 期中平均株式数 """
    capital_adequacy_ratio: Optional[IxNonFractionPublic] = Field(default=None, description='自己資本比率')
    """ 自己資本比率 """
    cash_and_equivalents_end_of_period: Optional[IxNonFractionPublic] = Field(default=None, description='現金及び現金同等物期末残高')
    """ 現金及び現金同等物期末残高 """
    cash_flows_from_financing_activities: Optional[IxNonFractionPublic] = Field(default=None, description='財務活動によるキャッシュ・フロー')
    """ 財務活動によるキャッシュ・フロー """
    cash_flows_from_investing_activities: Optional[IxNonFractionPublic] = Field(default=None, description='投資活動によるキャッシュ・フロー')
    """ 投資活動によるキャッシュ・フロー """
    cash_flows_from_operating_activities: Optional[IxNonFractionPublic] = Field(default=None, description='営業活動によるキャッシュ・フロー')
    """ 営業活動によるキャッシュ・フロー """
    change_in_comprehensive_income: Optional[IxNonFractionPublic] = Field(default=None, description='包括利益増減率')
    """ 包括利益増減率 """
    change_in_net_income: Optional[IxNonFractionPublic] = Field(default=None, description='増減率、当期純利益')
    """ 増減率、当期純利益 """
    change_in_net_sales: Optional[IxNonFractionPublic] = Field(default=None, description='増減率、売上高')
    """ 増減率、売上高 """
    change_in_operating_income: Optional[IxNonFractionPublic] = Field(default=None, description='増減率、営業利益')
    """ 増減率、営業利益 """
    change_in_operating_revenues: Optional[IxNonFractionPublic] = Field(default=None, description='増減率、営業収益')
    """ 増減率、営業収益 """
    change_in_ordinary_income: Optional[IxNonFractionPublic] = Field(default=None, description='増減率、経常利益')
    """ 増減率、経常利益 """
    change_in_ordinary_revenues_bk: Optional[IxNonFractionPublic] = Field(default=None, description='増減率、経常収益、銀行')
    """ 増減率、経常収益、銀行 """
    change_in_ordinary_revenues_in: Optional[IxNonFractionPublic] = Field(default=None, description='増減率、経常収益、保険')
    """ 増減率、経常収益、保険 """
    change_in_profit_attributable_to_owners_of_parent: Optional[IxNonFractionPublic] = Field(default=None, description='増減率、親会社株主に帰属する当期純利益')
    """ 増減率、親会社株主に帰属する当期純利益 """
    change_in_revenue: Optional[IxNonFractionPublic] = Field(default=None, description='増減率、売上収益')
    """ 増減率、売上収益 """
    commemorative_dividend: Optional[IxNonFractionPublic] = Field(default=None, description='記念配当')
    """ 記念配当 """
    comprehensive_income: Optional[IxNonFractionPublic] = Field(default=None, description='包括利益')
    """ 包括利益 """
    diluted_net_income_per_share: Optional[IxNonFractionPublic] = Field(default=None, description='潜在株式調整後1株当たり当期純利益')
    """ 潜在株式調整後1株当たり当期純利益 """
    dividend_per_share: Optional[IxNonFractionPublic] = Field(default=None, description='1株当たり配当金')
    """ 1株当たり配当金 """
    extra_dividend: Optional[IxNonFractionPublic] = Field(default=None, description='特別配当')
    """ 特別配当 """
    investment_profit_loss_on_equity_method: Optional[IxNonFractionPublic] = Field(default=None, description='持分法投資損益')
    """ 持分法投資損益 """
    net_assets: Optional[IxNonFractionPublic] = Field(default=None, description='純資産')
    """ 純資産 """
    net_assets_per_share: Optional[IxNonFractionPublic] = Field(default=None, description='1株当たり純資産')
    """ 1株当たり純資産 """
    net_income: Optional[IxNonFractionPublic] = Field(default=None, description='当期純利益')
    """ 当期純利益 """
    net_income_per_share: Optional[IxNonFractionPublic] = Field(default=None, description='1株当たり当期純利益')
    """ 1株当たり当期純利益 """
    net_income_to_shareholders_equity_ratio: Optional[IxNonFractionPublic] = Field(default=None, description='自己資本当期純利益率')
    """ 自己資本当期純利益率 """
    net_sales: Optional[IxNonFractionPublic] = Field(default=None, description='売上高')
    """ 売上高 """
    number_of_issued_and_outstanding_shares_at_the_end_of_fiscal_year_including_treasury_stock: Optional[IxNonFractionPublic] = Field(default=None, description='期末発行済株式数（自己株式を含む）')
    """ 期末発行済株式数（自己株式を含む） """
    number_of_subsidiaries_excluded_from_consolidation: Optional[IxNonFractionPublic] = Field(default=None, description='除外')
    """ 除外 """
    number_of_subsidiaries_newly_consolidated: Optional[IxNonFractionPublic] = Field(default=None, description='新規')
    """ 新規 """
    number_of_treasury_stock_at_the_end_of_fiscal_year: Optional[IxNonFractionPublic] = Field(default=None, description='期末自己株式数')
    """ 期末自己株式数 """
    operating_income: Optional[IxNonFractionPublic] = Field(default=None, description='営業利益')
    """ 営業利益 """
    operating_income_to_net_sales_ratio: Optional[IxNonFractionPublic] = Field(default=None, description='売上高営業利益率')
    """ 売上高営業利益率 """
    operating_income_to_operating_revenues_ratio: Optional[IxNonFractionPublic] = Field(default=None, description='営業収益営業利益率')
    """ 営業収益営業利益率 """
    operating_revenues: Optional[IxNonFractionPublic] = Field(default=None, description='営業収益')
    """ 営業収益 """
    ordinary_income: Optional[IxNonFractionPublic] = Field(default=None, description='経常利益')
    """ 経常利益 """
    ordinary_income_to_total_assets_ratio: Optional[IxNonFractionPublic] = Field(default=None, description='総資産経常利益率')
    """ 総資産経常利益率 """
    ordinary_revenues_bk: Optional[IxNonFractionPublic] = Field(default=None, description='経常収益、銀行')
    """ 経常収益、銀行 """
    ordinary_revenues_in: Optional[IxNonFractionPublic] = Field(default=None, description='経常収益、保険')
    """ 経常収益、保険 """
    owners_equity: Optional[IxNonFractionPublic] = Field(default=None, description='自己資本')
    """ 自己資本 """
    payout_ratio: Optional[IxNonFractionPublic] = Field(default=None, description='配当性向')
    """ 配当性向 """
    profit_attributable_to_owners_of_parent: Optional[IxNonFractionPublic] = Field(default=None, description='親会社株主に帰属する当期純利益')
    """ 親会社株主に帰属する当期純利益 """
    quarterly_period: Optional[IxNonFractionPublic] = Field(default=None, description='四半期')
    """ 四半期 """
    ratio_of_total_amount_of_dividends_to_net_assets: Optional[IxNonFractionPublic] = Field(default=None, description='純資産配当率')
    """ 純資産配当率 """
    revenue: Optional[IxNonFractionPublic] = Field(default=None, description='売上収益')
    """ 売上収益 """
    total_assets: Optional[IxNonFractionPublic] = Field(default=None, description='総資産')
    """ 総資産 """
    total_dividend_paid_annual: Optional[IxNonFractionPublic] = Field(default=None, description='配当金総額（合計）')
    """ 配当金総額（合計） """

