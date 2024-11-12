from app.models import Field, SQLModel
from app.schema.ix_non_fraction import IxNonFractionPublic
from typing import Optional

class IxNonFractionEdus(SQLModel):
    average_number_of_shares: Optional[IxNonFractionPublic] = Field(default=None, description='期中平均株式数')
    """ 期中平均株式数 """
    basic_net_income_per_share_us: Optional[IxNonFractionPublic] = Field(default=None, description='基本的1株当たり当社株主に帰属する当期純利益、米国基準')
    """ 基本的1株当たり当社株主に帰属する当期純利益、米国基準 """
    change_in_comprehensive_income_net_of_tax_including_portion_attributable_to_noncontrolling_interest5_us: Optional[IxNonFractionPublic] = Field(default=None, description='当社株主に帰属する包括利益増減率、米国基準')
    """ 当社株主に帰属する包括利益増減率、米国基準 """
    change_in_comprehensive_income_net_of_tax_including_portion_attributable_to_noncontrolling_interest_us: Optional[IxNonFractionPublic] = Field(default=None, description='当期包括利益増減率、米国基準')
    """ 当期包括利益増減率、米国基準 """
    change_in_income_before_income_taxes_us: Optional[IxNonFractionPublic] = Field(default=None, description='増減率、税引前当期純利益、米国基準')
    """ 増減率、税引前当期純利益、米国基準 """
    change_in_net_income_us: Optional[IxNonFractionPublic] = Field(default=None, description='増減率、当社株主に帰属する当期純利益、米国基準')
    """ 増減率、当社株主に帰属する当期純利益、米国基準 """
    change_in_net_sales_us: Optional[IxNonFractionPublic] = Field(default=None, description='増減率、売上高、米国基準')
    """ 増減率、売上高、米国基準 """
    change_in_operating_income_us: Optional[IxNonFractionPublic] = Field(default=None, description='増減率、営業利益、米国基準')
    """ 増減率、営業利益、米国基準 """
    change_in_operating_revenues_us: Optional[IxNonFractionPublic] = Field(default=None, description='増減率、営業収益、米国基準')
    """ 増減率、営業収益、米国基準 """
    comprehensive_income_net_of_tax_including_portion_attributable_to_noncontrolling_interest5_us: Optional[IxNonFractionPublic] = Field(default=None, description='当社株主に帰属する包括利益、米国基準')
    """ 当社株主に帰属する包括利益、米国基準 """
    comprehensive_income_net_of_tax_including_portion_attributable_to_noncontrolling_interest_us: Optional[IxNonFractionPublic] = Field(default=None, description='当期包括利益、米国基準')
    """ 当期包括利益、米国基準 """
    diluted_net_income_per_share2_us: Optional[IxNonFractionPublic] = Field(default=None, description='潜在株式調整後1株当たり当社株主に帰属する当期純利益、米国基準')
    """ 潜在株式調整後1株当たり当社株主に帰属する当期純利益、米国基準 """
    diluted_net_income_per_share_us: Optional[IxNonFractionPublic] = Field(default=None, description='希薄化後1株当たり当社株主に帰属する当期純利益、米国基準')
    """ 希薄化後1株当たり当社株主に帰属する当期純利益、米国基準 """
    dividend_per_share: Optional[IxNonFractionPublic] = Field(default=None, description='1株当たり配当金')
    """ 1株当たり配当金 """
    income_before_income_taxes_us: Optional[IxNonFractionPublic] = Field(default=None, description='税引前当期純利益、米国基準')
    """ 税引前当期純利益、米国基準 """
    net_assets_us: Optional[IxNonFractionPublic] = Field(default=None, description='資本合計（純資産）、米国基準')
    """ 資本合計（純資産）、米国基準 """
    net_income_per_share_us: Optional[IxNonFractionPublic] = Field(default=None, description='1株当たり当社株主に帰属する当期純利益、米国基準')
    """ 1株当たり当社株主に帰属する当期純利益、米国基準 """
    net_income_us: Optional[IxNonFractionPublic] = Field(default=None, description='当社株主に帰属する当期純利益、米国基準')
    """ 当社株主に帰属する当期純利益、米国基準 """
    net_sales_us: Optional[IxNonFractionPublic] = Field(default=None, description='売上高、米国基準')
    """ 売上高、米国基準 """
    number_of_issued_and_outstanding_shares_at_the_end_of_fiscal_year_including_treasury_stock: Optional[IxNonFractionPublic] = Field(default=None, description='期末発行済株式数（自己株式を含む）')
    """ 期末発行済株式数（自己株式を含む） """
    number_of_subsidiaries_excluded_from_consolidation_us: Optional[IxNonFractionPublic] = Field(default=None, description='除外、米国基準')
    """ 除外、米国基準 """
    number_of_subsidiaries_newly_consolidated_us: Optional[IxNonFractionPublic] = Field(default=None, description='新規、米国基準')
    """ 新規、米国基準 """
    number_of_treasury_stock_at_the_end_of_fiscal_year: Optional[IxNonFractionPublic] = Field(default=None, description='期末自己株式数')
    """ 期末自己株式数 """
    operating_income_us: Optional[IxNonFractionPublic] = Field(default=None, description='営業利益、米国基準')
    """ 営業利益、米国基準 """
    operating_revenues_us: Optional[IxNonFractionPublic] = Field(default=None, description='営業収益、米国基準')
    """ 営業収益、米国基準 """
    quarterly_period: Optional[IxNonFractionPublic] = Field(default=None, description='四半期')
    """ 四半期 """
    shareholders_equity_ratio_us: Optional[IxNonFractionPublic] = Field(default=None, description='株主資本比率、米国基準')
    """ 株主資本比率、米国基準 """
    shareholders_equity_us: Optional[IxNonFractionPublic] = Field(default=None, description='株主資本、米国基準')
    """ 株主資本、米国基準 """
    total_assets_us: Optional[IxNonFractionPublic] = Field(default=None, description='総資産、米国基準')
    """ 総資産、米国基準 """

