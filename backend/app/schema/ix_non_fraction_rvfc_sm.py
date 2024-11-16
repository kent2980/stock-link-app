from app.models import Field, SQLModel
from app.schema.ix_non_fraction import IxNonFractionPublic
from typing import Optional

class IxNonFractionRvfcSm(SQLModel):
    amount_change_net_income: Optional[IxNonFractionPublic] = Field(default=None, description='増減額、当期純利益')
    """ 増減額、当期純利益 """
    amount_change_net_sales: Optional[IxNonFractionPublic] = Field(default=None, description='増減額、売上高')
    """ 増減額、売上高 """
    amount_change_operating_income: Optional[IxNonFractionPublic] = Field(default=None, description='増減額、営業利益')
    """ 増減額、営業利益 """
    amount_change_operating_income_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='増減額、営業利益、IFRS')
    """ 増減額、営業利益、IFRS """
    amount_change_operating_revenues: Optional[IxNonFractionPublic] = Field(default=None, description='増減額、営業収益')
    """ 増減額、営業収益 """
    amount_change_ordinary_income: Optional[IxNonFractionPublic] = Field(default=None, description='増減額、経常利益')
    """ 増減額、経常利益 """
    amount_change_ordinary_revenues_bk: Optional[IxNonFractionPublic] = Field(default=None, description='増減額、経常収益、銀行')
    """ 増減額、経常収益、銀行 """
    amount_change_profit_attributable_to_owners_of_parent: Optional[IxNonFractionPublic] = Field(default=None, description='増減額、親会社株主に帰属する当期純利益')
    """ 増減額、親会社株主に帰属する当期純利益 """
    amount_change_profit_attributable_to_owners_of_parent_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='増減額、親会社の所有者に帰属する当期利益、IFRS')
    """ 増減額、親会社の所有者に帰属する当期利益、IFRS """
    amount_change_profit_before_tax_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='増減額、税引前利益、IFRS')
    """ 増減額、税引前利益、IFRS """
    amount_change_profit_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='増減額、当期利益、IFRS')
    """ 増減額、当期利益、IFRS """
    amount_change_revenue: Optional[IxNonFractionPublic] = Field(default=None, description='増減額、売上収益')
    """ 増減額、売上収益 """
    amount_change_sales_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='増減額、売上収益、IFRS')
    """ 増減額、売上収益、IFRS """
    basic_earnings_per_share_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='基本的1株当たり当期利益、IFRS')
    """ 基本的1株当たり当期利益、IFRS """
    change_in_net_income: Optional[IxNonFractionPublic] = Field(default=None, description='増減率、当期純利益')
    """ 増減率、当期純利益 """
    change_in_net_sales: Optional[IxNonFractionPublic] = Field(default=None, description='増減率、売上高')
    """ 増減率、売上高 """
    change_in_operating_income: Optional[IxNonFractionPublic] = Field(default=None, description='増減率、営業利益')
    """ 増減率、営業利益 """
    change_in_operating_income_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='増減率、営業利益、IFRS')
    """ 増減率、営業利益、IFRS """
    change_in_operating_revenues: Optional[IxNonFractionPublic] = Field(default=None, description='増減率、営業収益')
    """ 増減率、営業収益 """
    change_in_ordinary_income: Optional[IxNonFractionPublic] = Field(default=None, description='増減率、経常利益')
    """ 増減率、経常利益 """
    change_in_ordinary_revenues_bk: Optional[IxNonFractionPublic] = Field(default=None, description='増減率、経常収益、銀行')
    """ 増減率、経常収益、銀行 """
    change_in_profit_attributable_to_owners_of_parent: Optional[IxNonFractionPublic] = Field(default=None, description='増減率、親会社株主に帰属する当期純利益')
    """ 増減率、親会社株主に帰属する当期純利益 """
    change_in_profit_attributable_to_owners_of_parent_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='増減率、親会社の所有者に帰属する当期利益、IFRS')
    """ 増減率、親会社の所有者に帰属する当期利益、IFRS """
    change_in_profit_before_tax_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='増減率、税引前利益、IFRS')
    """ 増減率、税引前利益、IFRS """
    change_in_profit_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='増減率、当期利益、IFRS')
    """ 増減率、当期利益、IFRS """
    change_in_revenue: Optional[IxNonFractionPublic] = Field(default=None, description='増減率、売上収益')
    """ 増減率、売上収益 """
    change_in_sales_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='増減率、売上収益、IFRS')
    """ 増減率、売上収益、IFRS """
    dividend_per_share: Optional[IxNonFractionPublic] = Field(default=None, description='1株当たり配当金')
    """ 1株当たり配当金 """
    net_income: Optional[IxNonFractionPublic] = Field(default=None, description='当期純利益')
    """ 当期純利益 """
    net_income_per_share: Optional[IxNonFractionPublic] = Field(default=None, description='1株当たり当期純利益')
    """ 1株当たり当期純利益 """
    net_sales: Optional[IxNonFractionPublic] = Field(default=None, description='売上高')
    """ 売上高 """
    operating_income: Optional[IxNonFractionPublic] = Field(default=None, description='営業利益又は営業損失（△）')
    """ 営業利益又は営業損失（△） """
    operating_income_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='営業利益、IFRS')
    """ 営業利益、IFRS """
    operating_revenues: Optional[IxNonFractionPublic] = Field(default=None, description='営業収益')
    """ 営業収益 """
    ordinary_income: Optional[IxNonFractionPublic] = Field(default=None, description='経常利益又は経常損失（△）')
    """ 経常利益又は経常損失（△） """
    ordinary_revenues_bk: Optional[IxNonFractionPublic] = Field(default=None, description='経常収益、銀行')
    """ 経常収益、銀行 """
    profit_attributable_to_owners_of_parent: Optional[IxNonFractionPublic] = Field(default=None, description='親会社株主に帰属する当期純利益')
    """ 親会社株主に帰属する当期純利益 """
    profit_attributable_to_owners_of_parent_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='親会社の所有者に帰属する当期利益、IFRS')
    """ 親会社の所有者に帰属する当期利益、IFRS """
    profit_before_tax_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='税引前利益、IFRS')
    """ 税引前利益、IFRS """
    profit_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='当期利益、IFRS')
    """ 当期利益、IFRS """
    revenue: Optional[IxNonFractionPublic] = Field(default=None, description='売上収益')
    """ 売上収益 """
    sales_ifrs: Optional[IxNonFractionPublic] = Field(default=None, description='売上収益、IFRS')
    """ 売上収益、IFRS """

