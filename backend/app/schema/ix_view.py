import datetime
import re
from decimal import Decimal
from typing import List, Optional, Union

import app.schema as sc
from app.models import Field, SQLModel
from pydantic import BaseModel, validator


# region /stock/all endpoint
class StockRecordInfo(SQLModel):
    """iXBRLのヘッダー情報を表すクラス"""

    head_item_key: str = Field(default=None, description="iXBRLのソースID")
    company_name: str = Field(default=None, description="上場会社名")
    securities_code: str = Field(default=None, description="証券コード")
    current_period: Optional[str] = Field(default=None, description="四半期")
    report_type: str = Field(default=None, description="報告書種別")
    reporting_date: datetime.date = Field(default=None, description="提出日")
    document_name: str = Field(default=None, description="文書名")
    fiscal_year_end: str = Field(default=None, description="決算期")
    url: Optional[str] = Field(default=None, description="URL")


class StockRecordInfos(SQLModel):
    """iXBRLのヘッダー情報のリストを表すクラス"""

    count: int
    data: list[StockRecordInfo]
    nextOffset: Optional[int] = Field(
        default=None, description="次のページのオフセット"
    )


# endregion


# region /head_items/ endpoint
class HeadItem(SQLModel):
    """iXBRLのソースID情報を表すクラス"""

    head_item_key: str
    company_name: str
    securities_code: str
    document_name: str
    reporting_date: datetime.date
    current_period: Optional[str]
    report_type: Optional[str]
    listed_market: Optional[str]
    market_section: Optional[str]
    url: Optional[str]
    is_bs: Optional[bool]
    is_pl: Optional[bool]
    is_cf: Optional[bool]
    is_ci: Optional[bool]
    is_sce: Optional[bool]
    is_sfp: Optional[bool]
    fiscal_year_end: Optional[str]
    tel: Optional[str]


class HeadItems(SQLModel):
    """iXBRLのソースID情報のリストを表すクラス"""

    data: list[HeadItem]
    count: int


# endregion


# region /menu/ endpoint
class MenuTitle(SQLModel):
    label: Optional[str] = Field(default=None, description="タイトルラベル")
    jp: Optional[str] = Field(default=None, description="日本語ラベル")


class MenuTitles(SQLModel):
    count: int
    data: List[MenuTitle]


# endregion


# region /info/ endpoint
class ContextFilter(BaseModel):
    """正規表現を公開するためのクラス"""

    regex: Optional[str] = Field(default=None, description="正規表現", exclude=True)
    context: str = Field(default="", description="コンテキスト", exclude=True)


class abstractBase(ContextFilter):
    """概要を公開するためのクラス"""

    order: Optional[float] = Field(default=None, description="順序")
    Label: Optional[str] = Field(default=None, description="ラベル")


class stock(ContextFilter):
    is_valid: Optional[bool] = Field(default=False, description="有効なデータかどうか")
    label: Optional[str] = Field(default=None, description="ラベル")
    value: Optional[str] = Field(default=None, description="値")
    order: Optional[float] = Field(default=None, description="順序")

    def set_value(self, new_value: Optional[str]) -> None:
        self.value = new_value
        if new_value is not None:
            self.is_valid = True
        else:
            self.is_valid = False


class business_category(abstractBase):
    """事業会社種別を公開するためのクラス"""

    GeneralBusiness: Optional[stock] = Field(
        default_factory=lambda: stock(), description="一般事業会社の可否"
    )
    SpecificBusiness: Optional[stock] = Field(
        default_factory=lambda: stock(), description="特定事業会社の可否"
    )

    def __init__(self):
        super().__init__()
        for _, value in self.__dict__.items():
            if isinstance(value, ContextFilter):
                value.context = r"^Current"
        self.GeneralBusiness.regex = r"tse-ed-t_GeneralBusiness$"
        self.SpecificBusiness.regex = r"tse-ed-t_SpecificBusiness$"


class inquiries_abstract(abstractBase):
    NameInquiries: Optional[stock] = Field(
        default_factory=lambda: stock(), description="問合せ先責任者氏名"
    )
    TitleInquiries: Optional[stock] = Field(
        default_factory=lambda: stock(), description="問合せ先責任者役職名"
    )

    def __init__(self):
        super().__init__()
        for _, value in self.__dict__.items():
            if isinstance(value, ContextFilter):
                value.context = r"^Current"
        self.NameInquiries.regex = r"tse-ed-t_NameInquiries$"
        self.TitleInquiries.regex = r"tse-ed-t_TitleInquiries$"


class other_company_information_abstract(abstractBase):

    AnnualSecuritiesReportFilingDateAsPlanned: Optional[stock] = Field(
        default_factory=lambda: stock(), description="有価証券報告書提出予定日"
    )
    DateOfGeneralShareholdersMeetingAsPlanned: Optional[stock] = Field(
        default_factory=lambda: stock(), description="定時株主総会の開催予定日"
    )
    DividendPayableDateAsPlanned: Optional[stock] = Field(
        default_factory=lambda: stock(), description="配当支払予定日"
    )

    def __init__(self):
        super().__init__()
        for _, value in self.__dict__.items():
            if isinstance(value, ContextFilter):
                value.context = r"^Current"
        self.AnnualSecuritiesReportFilingDateAsPlanned.regex = (
            r"tse-ed-t_AnnualSecuritiesReportFilingDateAsPlanned$"
        )
        self.DateOfGeneralShareholdersMeetingAsPlanned.regex = (
            r"tse-ed-t_DateOfGeneralShareholdersMeetingAsPlanned$"
        )
        self.DividendPayableDateAsPlanned.regex = (
            r"tse-ed-t_DividendPayableDateAsPlanned$"
        )


class representative_abstract(abstractBase):

    NameRepresentative: Optional[stock] = Field(
        default_factory=lambda: stock(), description="代表者氏名"
    )
    TitleRepresentative: Optional[stock] = Field(
        default_factory=lambda: stock(), description="代表者役職名"
    )

    def __init__(self):
        super().__init__()
        for _, value in self.__dict__.items():
            if isinstance(value, ContextFilter):
                value.context = r"^Current"
        self.NameRepresentative.regex = r"tse-ed-t_NameRepresentative$"
        self.TitleRepresentative.regex = r"tse-ed-t_TitleRepresentative$"


class StockInfo(abstractBase):
    """株式情報を公開するためのクラス"""

    DocumentName: Optional[stock] = Field(
        default_factory=lambda: stock(), description="文書名"
    )
    FilingDate: Optional[stock] = Field(
        default_factory=lambda: stock(), description="提出日"
    )
    CompanyName: Optional[stock] = Field(
        default_factory=lambda: stock(), description="上場会社名"
    )
    SecuritiesCode: Optional[stock] = Field(
        default_factory=lambda: stock(), description="証券コード"
    )
    URL: Optional[stock] = Field(default_factory=lambda: stock(), description="URL")
    RepresentativeAbstract: Optional[representative_abstract] = Field(
        default_factory=lambda: representative_abstract(), description="代表者情報"
    )
    InquiriesAbstract: Optional[inquiries_abstract] = Field(
        default_factory=lambda: inquiries_abstract(), description="問合せ先情報"
    )
    Tel: Optional[stock] = Field(
        default_factory=lambda: stock(), description="電話番号"
    )
    OtherCompanyInformationAbstract: Optional[other_company_information_abstract] = (
        Field(
            default_factory=lambda: other_company_information_abstract(),
            description="その他の上場会社情報",
        )
    )
    SupplementalMaterialOfAnnualResults: Optional[stock] = Field(
        default_factory=lambda: stock(), description="決算補足資料"
    )
    WayOfGettingSupplementalMaterialOfAnnualResults: Optional[stock] = Field(
        default_factory=lambda: stock(), description="決算補足資料の入手方法"
    )
    ConveningBriefingOfAnnualResults: Optional[stock] = Field(
        default_factory=lambda: stock(), description="決算説明会の開催の有無"
    )
    TargetAudienceBriefingOfAnnualResults: Optional[stock] = Field(
        default_factory=lambda: stock(), description="決算説明会の対象者"
    )
    NoteToFractionProcessingMethod: Optional[stock] = Field(
        default_factory=lambda: stock(), description="端数処理方法に関する注記"
    )
    TokyoStockExchange: Optional[stock] = Field(
        default_factory=lambda: stock(), description="東京証券取引所の上場市場"
    )
    BusinessCategory: Optional[business_category] = Field(
        default_factory=lambda: business_category(), description="事業会社種別"
    )
    FiscalYearEnd: Optional[stock] = Field(
        default_factory=lambda: stock(), description="決算期"
    )
    QuarterlyPeriod: Optional[stock] = Field(
        default_factory=lambda: stock(), description="四半期"
    )

    def __init__(self):
        super().__init__()
        # すべての変数のregexに同じ値を設定
        for _, value in self.__dict__.items():
            if isinstance(value, ContextFilter):
                value.context = r"^Current"
        self.regex = r"tse-ed-t_DocumentEntityInformationHeading$"
        self.DocumentName.regex = r"tse-ed-t_DocumentName$"
        self.FilingDate.regex = r"tse-ed-t_FilingDate$"
        self.CompanyName.regex = r"tse-ed-t_CompanyName$"
        self.SecuritiesCode.regex = r"tse-ed-t_SecuritiesCode$"
        self.URL.regex = r"tse-ed-t_URL$"
        self.RepresentativeAbstract.regex = r"tse-ed-t_RepresentativeAbstract$"
        self.RepresentativeAbstract.NameRepresentative.regex = (
            r"tse-ed-t_NameRepresentative$"
        )
        self.RepresentativeAbstract.TitleRepresentative.regex = (
            r"tse-ed-t_TitleRepresentative$"
        )
        self.InquiriesAbstract.regex = r"tse-ed-t_InquiriesAbstract$"
        self.Tel.regex = r"tse-ed-t_Tel$"
        self.OtherCompanyInformationAbstract.regex = (
            r"tse-ed-t_OtherCompanyInformationAbstract$"
        )
        self.SupplementalMaterialOfAnnualResults.regex = (
            r"tse-ed-t_SupplementalMaterialOfAnnualResults$"
        )
        self.WayOfGettingSupplementalMaterialOfAnnualResults.regex = (
            r"tse-ed-t_WayOfGettingSupplementalMaterialOfAnnualResults$"
        )
        self.BusinessCategory.regex = r"tse-ed-t_BusinessCategoryAbstract$"
        self.FiscalYearEnd.regex = r"tse-ed-t_FiscalYearEnd$"
        self.QuarterlyPeriod.regex = r"tse-ed-t_QuarterlyPeriod$"
        self.NoteToFractionProcessingMethod.regex = (
            r"tse-ed-t_NoteToFractionProcessingMethod$"
        )
        self.TargetAudienceBriefingOfAnnualResults.regex = (
            r"tse-ed-t_TargetAudienceBriefingOfAnnualResults$"
        )
        self.ConveningBriefingOfAnnualResults.regex = (
            r"tse-ed-t_ConveningBriefingOfAnnualResults$"
        )


class FiscalYearStockInfo(StockInfo):
    """決算期情報を公開するためのクラス"""

    ConveningBriefingOfAnnualResults: Optional[stock] = Field(
        default_factory=lambda: stock(), description="決算説明会の開催の有無"
    )
    AnnualSecuritiesReportFilingDateAsPlanned: Optional[stock] = Field(
        default_factory=lambda: stock(), description="有価証券報告書提出予定日"
    )
    DateOfGeneralShareholdersMeetingAsPlanned: Optional[stock] = Field(
        default_factory=lambda: stock(), description="定時株主総会の開催予定日"
    )
    DividendPayableDateAsPlanned: Optional[stock] = Field(
        default_factory=lambda: stock(), description="配当支払予定日"
    )

    @classmethod
    def from_parent(cls, parent: StockInfo):
        return cls(**parent.model_dump())


# endregion


# region /ope/result endpoint
class stockNumeric(ContextFilter):
    order: Optional[float] = Field(default=None, description="順序")
    is_valid: Optional[bool] = Field(default=False, description="有効なデータかどうか")
    label: Optional[str] = Field(default=None, description="ラベル")
    numeric: Optional[float] = Field(default=None, description="数値データ")
    value: Optional[str] = Field(default=None, description="値")
    scale: Optional[str] = Field(default=None, description="スケール")

    def set_value(self, new_value: Optional[str]) -> None:
        self.value = new_value
        if new_value is not None:
            self.is_valid = True
        else:
            self.is_valid = False

    @validator("numeric", pre=True, always=True)
    def format_numeric(cls, value):
        """数値データを整数に変換する"""
        if value is not None:
            decimal_value = Decimal(value)
            # 小数部分が0の場合は整数に変換
            if decimal_value == decimal_value.to_integral_value():
                return decimal_value.to_integral_value()
            return decimal_value
        return value


class abstract(abstractBase):
    """概要を公開するためのクラス"""

    Values: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(), description="値"
    )
    ChangeIn: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(), description="増減"
    )


class TypeBase(ContextFilter):
    type: Optional[str] = Field(default=None, description="タイプ")

    def __init__(self, **data):
        super().__init__(**data)
        self.type = self.__class__.__name__


# region 日本基準のスキーマ
# region 一般事業会社
class OtherOperatingResultsAbstractJp(abstractBase):
    """その他の連結経営成績の概要を公開するためのクラス"""

    NetIncomePerShare: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(),
        description="1株当たり当期純利益（基本）",
    )
    DilutedNetIncomePerShare: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(), description="1株当たり当期純利益"
    )
    NetIncomeToShareholdersEquityRatio: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(), description="自己資本当期純利益率"
    )
    OrdinaryIncomeToTotalAssetsRatio: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(), description="総資産経常利益率"
    )
    OperatingIncomeToNetSalesRatio: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(), description="売上高営業利益率"
    )
    PeriodNetIncomePerShare: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(),
        description="昨年度1株当たり当期純利益（基本）",
    )
    PeriodDilutedNetIncomePerShare: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(), description="昨年度1株当たり当期純利益"
    )
    PeriodNetIncomeToShareholdersEquityRatio: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(), description="昨年度自己資本当期純利益率"
    )
    PeriodOrdinaryIncomeToTotalAssetsRatio: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(), description="昨年度総資産経常利益率"
    )
    PeriodOperatingIncomeToNetSalesRatio: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(), description="昨年度売上高営業利益率"
    )

    def __init__(self):
        super().__init__()
        for key, value in self.__dict__.items():
            if isinstance(value, ContextFilter):
                if "Period" in key:
                    value.context = r"(?=.*Prior.*)(?=.*ResultMember)"
                else:
                    value.context = r"(?=.*Current)(?=.*ResultMember)"
        self.NetIncomePerShare.regex = r"tse-ed-t_NetIncomePerShare$"
        self.DilutedNetIncomePerShare.regex = r"tse-ed-t_DilutedNetIncomePerShare$"
        self.NetIncomeToShareholdersEquityRatio.regex = (
            r"tse-ed-t_NetIncomeToShareholdersEquityRatio$"
        )
        self.OrdinaryIncomeToTotalAssetsRatio.regex = (
            r"tse-ed-t_OrdinaryIncomeToTotalAssetsRatio$"
        )
        self.OperatingIncomeToNetSalesRatio.regex = (
            r"tse-ed-t_OperatingIncomeToNetSalesRatio$"
        )
        self.PeriodNetIncomePerShare.regex = r"tse-ed-t_NetIncomePerShare$"
        self.PeriodDilutedNetIncomePerShare.regex = (
            r"tse-ed-t_DilutedNetIncomePerShare$"
        )
        self.PeriodNetIncomeToShareholdersEquityRatio.regex = (
            r"tse-ed-t_NetIncomeToShareholdersEquityRatio$"
        )
        self.PeriodOrdinaryIncomeToTotalAssetsRatio.regex = (
            r"tse-ed-t_OrdinaryIncomeToTotalAssetsRatio$"
        )
        self.PeriodOperatingIncomeToNetSalesRatio.regex = (
            r"tse-ed-t_OperatingIncomeToNetSalesRatio$"
        )


class IncomeStatementsInformationAbstractJp(abstractBase):
    """損益計算書情報を公開するためのクラス"""

    NetSales: abstract = Field(default_factory=lambda: abstract(), description="売上高")
    PeriodNetSales: abstract = Field(
        default_factory=lambda: abstract(), description="昨年度売上高"
    )
    OperatingIncome: abstract = Field(
        default_factory=lambda: abstract(), description="営業利益"
    )
    PeriodOperatingIncome: abstract = Field(
        default_factory=lambda: abstract(), description="昨年度営業利益"
    )
    OrdinaryIncome: abstract = Field(
        default_factory=lambda: abstract(), description="経常利益"
    )
    PeriodOrdinaryIncome: abstract = Field(
        default_factory=lambda: abstract(), description="昨年度経常利益"
    )
    Profit: abstract = Field(
        default_factory=lambda: abstract(),
        description="親会社株主に帰属する当期純利益",
    )
    PeriodProfit: abstract = Field(
        default_factory=lambda: abstract(),
        description="昨年度親会社株主に帰属する当期純利益",
    )

    def __init__(self):
        super().__init__()
        # すべての変数のregexに同じ値を設定
        for key, value in self.__dict__.items():
            if "Period" in key:
                context = r"(?=.*Prior.*)(?=.*ResultMember)"
                if isinstance(value, ContextFilter):
                    value.context = context
                elif isinstance(value, abstract):
                    value.ChangeIn.context = context
                    value.Values.context = context
            else:
                context = r"(?=.*Current)(?=.*ResultMember)"
                if isinstance(value, ContextFilter):
                    value.context = context
                elif isinstance(value, abstract):
                    value.ChangeIn.context = context
                    value.Values.context = context
        # 今年度の情報
        self.NetSales.regex = r"tse-ed-t_NetSalesAbstract$"
        self.NetSales.ChangeIn.regex = r"tse-ed-t_ChangeInNetSales$"
        self.NetSales.Values.regex = r"tse-ed-t_NetSales$"
        self.OperatingIncome.regex = r"tse-ed-t_OperatingIncomeAbstract$"
        self.OperatingIncome.ChangeIn.regex = r"tse-ed-t_ChangeInOperatingIncome$"
        self.OperatingIncome.Values.regex = r"tse-ed-t_OperatingIncome$"
        self.OrdinaryIncome.regex = r"tse-ed-t_OrdinaryIncomeAbstract$"
        self.OrdinaryIncome.ChangeIn.regex = r"tse-ed-t_ChangeInOrdinaryIncome$"
        self.OrdinaryIncome.Values.regex = r"tse-ed-t_OrdinaryIncome$"
        self.Profit.regex = r"tse-ed-t_ProfitAttributableToOwnersOfParentAbstract$"
        self.Profit.ChangeIn.regex = r"tse-ed-t_ChangeInProfitAttributableToOwnersOfParent$|tsm-td-t_ChangeInNetIncome$"
        self.Profit.Values.regex = (
            r"tse-ed-t_ProfitAttributableToOwnersOfParent$|tsm-td-t_NetIncome$"
        )
        # 昨年度の情報
        self.PeriodNetSales.regex = r"tse-ed-t_NetSalesAbstract$"
        self.PeriodNetSales.ChangeIn.regex = r"tse-ed-t_ChangeInNetSales$"
        self.PeriodNetSales.Values.regex = r"tse-ed-t_NetSales$"
        self.PeriodOperatingIncome.regex = r"tse-ed-t_OperatingIncomeAbstract$"
        self.PeriodOperatingIncome.ChangeIn.regex = r"tse-ed-t_ChangeInOperatingIncome$"
        self.PeriodOperatingIncome.Values.regex = r"tse-ed-t_OperatingIncome$"
        self.PeriodOrdinaryIncome.regex = r"tse-ed-t_OrdinaryIncomeAbstract$"
        self.PeriodOrdinaryIncome.ChangeIn.regex = r"tse-ed-t_ChangeInOrdinaryIncome$"
        self.PeriodOrdinaryIncome.Values.regex = r"tse-ed-t_OrdinaryIncome$"
        self.PeriodProfit.regex = (
            r"tse-ed-t_ProfitAttributableToOwnersOfParentAbstract$"
        )
        self.PeriodProfit.ChangeIn.regex = r"tse-ed-t_ChangeInProfitAttributableToOwnersOfParent$|tsm-td-t_ChangeInNetIncome$"
        self.PeriodProfit.Values.regex = (
            r"tse-ed-t_ProfitAttributableToOwnersOfParent$|tsm-td-t_NetIncome$"
        )


class NoteToIncomeStatementsInformationAbstractJp(abstractBase):
    """損益計算書情報に関する注記を公開するためのクラス"""

    ComprehensiveIncomeAbstract: abstract = Field(
        default_factory=lambda: abstract(), description="包括利益"
    )
    PeriodComprehensiveIncomeAbstract: abstract = Field(
        default_factory=lambda: abstract(), description="昨年度包括利益"
    )

    def __init__(self):
        super().__init__()
        # すべての変数のregexに同じ値を設定
        for key, value in self.__dict__.items():
            if "Period" in key:
                context = r"(?=.*Prior.*)(?=.*ResultMember)"
                if isinstance(value, ContextFilter):
                    value.context = context
                elif isinstance(value, abstract):
                    value.ChangeIn.context = context
                    value.Values.context = context
            else:
                context = r"(?=.*Current)(?=.*ResultMember)"
                if isinstance(value, ContextFilter):
                    value.context = context
                elif isinstance(value, abstract):
                    value.ChangeIn.context = context
                    value.Values.context = context
        self.ComprehensiveIncomeAbstract.regex = (
            r"tse-ed-t_ComprehensiveIncome.*Abstract$"
        )
        self.ComprehensiveIncomeAbstract.ChangeIn.regex = (
            r"tse-ed-t_ChangeInComprehensiveIncome.*$"
        )
        self.ComprehensiveIncomeAbstract.Values.regex = (
            r"tse-ed-t_ComprehensiveIncome.*$"
        )
        self.PeriodComprehensiveIncomeAbstract.regex = (
            r"tse-ed-t_ComprehensiveIncome.*Abstract$"
        )
        self.PeriodComprehensiveIncomeAbstract.ChangeIn.regex = (
            r"tse-ed-t_ChangeInComprehensiveIncome.*$"
        )
        self.PeriodComprehensiveIncomeAbstract.Values.regex = (
            r"tse-ed-t_ComprehensiveIncome.*$"
        )


class NoteToOperatingResultsAbstractJp(abstractBase):
    """業績情報に関する注記を公開するためのクラス"""

    NoteToOperatingResults: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(), description="業績情報に関する注記"
    )

    def __init__(self):
        super().__init__()
        # すべての変数のregexに同じ値を設定
        for _, value in self.__dict__.items():
            if isinstance(value, ContextFilter):
                value.context = r"^Current"
        self.NoteToOperatingResults.regex = r"tse-ed-t_NoteToOperatingResults$"


class OperatingResultsAbstractJp(abstractBase):
    """業績情報を公開するためのクラス"""

    IncomeStatementsInformationAbstract: IncomeStatementsInformationAbstractJp = Field(
        default_factory=lambda: IncomeStatementsInformationAbstractJp(),
        description="連結損益計算書情報",
    )
    NoteToIncomeStatementsInformationAbstract: (
        NoteToIncomeStatementsInformationAbstractJp
    ) = Field(
        default_factory=lambda: NoteToIncomeStatementsInformationAbstractJp(),
        description="連結損益計算書情報に関する注記",
    )
    OtherOperatingResultsAbstract: OtherOperatingResultsAbstractJp = Field(
        default_factory=lambda: OtherOperatingResultsAbstractJp(),
        description="その他の連結経営成績の概要",
    )

    def __init__(self):
        super().__init__()
        # すべての変数のregexに同じ値を設定
        for _, value in self.__dict__.items():
            if isinstance(value, ContextFilter):
                value.context = r"^Current"
        self.IncomeStatementsInformationAbstract.regex = (
            r"tse-ed-t_.*IncomeStatementsInformationAbstract$"
        )
        self.NoteToIncomeStatementsInformationAbstract.regex = (
            r"tse-ed-t_NoteTo.*IncomeStatementsInformationAbstract$"
        )
        self.OtherOperatingResultsAbstract.regex = (
            r"tse-ed-t_Other.*OperatingResultsAbstract$"
        )


class OperatingResultJp(abstractBase):
    """業績情報を公開するためのクラス"""

    OperatingResultsAbstract: OperatingResultsAbstractJp = Field(
        default_factory=lambda: OperatingResultsAbstractJp(), description="業績情報"
    )
    NoteToOperatingResultsAbstract: NoteToOperatingResultsAbstractJp = Field(
        default_factory=lambda: NoteToOperatingResultsAbstractJp(),
        description="業績情報に関する注記",
    )

    def __init__(self):
        super().__init__()
        # すべての変数のregexに同じ値を設定
        for _, value in self.__dict__.items():
            if isinstance(value, ContextFilter):
                value.context = r"^Current"
        self.regex = r"tse-ed-t_(?!NoteTo)(?!Other).*OperatingResultsHeading$"
        self.OperatingResultsAbstract.regex = (
            r"tse-ed-t_(?!NoteTo)(?!Other).*OperatingResultsAbstract$"
        )
        self.NoteToOperatingResultsAbstract.regex = (
            r"tse-ed-t_NoteTo.*OperatingResultsAbstract$"
        )


class NoteToFinancialResultsJp(abstractBase):
    """連結財務諸表に関する注記を公開するためのクラス"""

    NoteToFinancialResults: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(), description="連結財務諸表に関する注記"
    )

    def __init__(self):
        super().__init__()
        # すべての変数のregexに同じ値を設定
        for _, value in self.__dict__.items():
            if isinstance(value, ContextFilter):
                value.context = r"^Current"
        self.regex = r"tse-ed-t_BusinessResultsNoteOverview.*BusinessResultsHeading$"
        self.NoteToFinancialResults.regex = r"tse-ed-t_NoteToFinancialResults$"


class FinancialPositionsAbstractJp(abstractBase):
    """財政状態の概要を公開するためのクラス"""

    CapitalAdequacyRatio: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(), description="総資産"
    )
    NetAssets: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(), description="純資産"
    )
    TotalAssets: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(), description="自己資本"
    )
    PeriodCapitalAdequacyRatio: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(), description="昨年度総資産"
    )
    PeriodNetAssets: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(), description="昨年度純資産"
    )
    PeriodTotalAssets: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(), description="昨年度自己資本"
    )

    def __init__(self):
        super().__init__()
        for key, value in self.__dict__.items():
            if isinstance(value, ContextFilter):
                if "Period" in key:
                    value.context = r"^Prior"
                else:
                    value.context = r"^Current"
        self.CapitalAdequacyRatio.regex = r"tse-ed-t_CapitalAdequacyRatio$"
        self.NetAssets.regex = r"tse-ed-t_NetAssets$"
        self.TotalAssets.regex = r"tse-ed-t_TotalAssets$"
        self.PeriodCapitalAdequacyRatio.regex = r"tse-ed-t_CapitalAdequacyRatio$"
        self.PeriodNetAssets.regex = r"tse-ed-t_NetAssets$"
        self.PeriodTotalAssets.regex = r"tse-ed-t_TotalAssets$"


class NoteToFinancialPositionsAbstractJp(abstractBase):
    """連結財務諸表に関する注記を公開するためのクラス"""

    NoteToFinancialPositions: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(), description="連結財務諸表に関する注記"
    )
    OwnersEquity: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(), description="自己資本"
    )

    def __init__(self):
        super().__init__()
        for _, value in self.__dict__.items():
            if isinstance(value, ContextFilter):
                value.context = r"^Current"
        self.NoteToFinancialPositions.regex = r"tse-ed-t_NoteToFinancialPositions$"
        self.OwnersEquity.regex = r"tse-ed-t_OwnersEquity$"


class BusinessResultsFinancialPositionsJp(abstractBase):
    """業績及び財政状態に関する注記を公開するためのクラス"""

    FinancialPositions: FinancialPositionsAbstractJp = Field(
        default_factory=lambda: FinancialPositionsAbstractJp(),
        description="財政状態の概要",
    )
    NoteToFinancialPositions: NoteToFinancialPositionsAbstractJp = Field(
        default_factory=lambda: NoteToFinancialPositionsAbstractJp(),
        description="連結財務諸表に関する注記",
    )

    def __init__(self):
        super().__init__()
        # すべての変数のregexに同じ値を設定
        for _, value in self.__dict__.items():
            if isinstance(value, ContextFilter):
                value.context = r"^Current"
        self.regex = r"tse-ed-t_BusinessResultsFinancialPositionsHeading$"
        self.FinancialPositions.regex = (
            r"tse-ed-t_(?!NoteTo).*FinancialPositionsAbstract$"
        )
        self.NoteToFinancialPositions.regex = r"tse-ed-t_NoteToFinancialPositions$"


class NotesApplyingSpecificAccountingQuarterlyFinancialStatementsJp(abstractBase):
    """四半期連結財務諸表に適用する特定会計基準に関する注記を公開するためのクラス"""

    ApplyingOfSpecificAccountingOfTheConsolidatedQuarterlyFinancialStatements: Optional[
        stockNumeric
    ] = Field(
        default_factory=lambda: stockNumeric(),
        description="四半期連結財務諸表に適用する特定会計基準の適用状況",
    )
    NoteToApplyingOfSpecificAccountingOfTheConsolidatedQuarterlyFinancialStatements: (
        Optional[stockNumeric]
    ) = Field(
        default_factory=lambda: stockNumeric(),
        description="四半期連結財務諸表に適用する特定会計基準に関する注記",
    )

    def __init__(self):
        super().__init__()
        for _, value in self.__dict__.items():
            if isinstance(value, ContextFilter):
                value.context = r"^Current"
        self.ApplyingOfSpecificAccountingOfTheConsolidatedQuarterlyFinancialStatements.regex = (
            r"tse-ed-t_ApplyingOfSpecificAccountingOf.*QuarterlyFinancialStatements$"
        )
        self.NoteToApplyingOfSpecificAccountingOfTheConsolidatedQuarterlyFinancialStatements.regex = r"tse-ed-t_NoteToApplyingOfSpecificAccountingOf.*QuarterlyFinancialStatements$"


class NotesChangesAccountingPoliciesAccountingEstimatesRetrospectiveRestatementJp(
    abstractBase
):
    ChangesBasedOnRevisionsOfAccountingStandard: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(), description="会計基準の改正に基づく変更"
    )
    ChangesInAccountingEstimates: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(), description="会計上の見積りの変更"
    )
    ChangesOtherThanOnesBasedOnRevisionsOfAccountingStandard: Optional[stockNumeric] = (
        Field(
            default_factory=lambda: stockNumeric(),
            description="会計基準の改正以外の変更",
        )
    )
    RetrospectiveRestatement: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(), description="遡及的な再表示"
    )
    NoteToChangesInAccountingPoliciesAccountingEstimatesAndRetrospectiveRestatementQuarterly: Optional[
        stockNumeric
    ] = Field(
        default_factory=lambda: stockNumeric(),
        description="四半期連結財務諸表における会計方針の変更、会計上の見積りの変更及び遡及的な再表示に関する注記",
    )


class NotesNumberIssuedOutstandingSharesCommonStockJp(abstractBase):
    """四半期連結財務諸表における発行済株式数（普通株式）に関する注記を公開するためのクラス"""

    NoteToNumberOfIssuedAndOutstandingSharesCommonStock: Optional[stock] = Field(
        default_factory=lambda: stock(),
        description="四半期連結財務諸表における発行済株式数（普通株式）に関する注記",
    )
    AverageNumberOfShares: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(), description="平均発行株数"
    )
    NumberOfIssuedAndOutstandingSharesAtTheEndOfFiscalYearIncludingTreasuryStock: (
        Optional[stockNumeric]
    ) = Field(
        default_factory=lambda: stockNumeric(),
        description="期末発行済株式数（自己株式を含む）",
    )
    NumberOfTreasuryStockAtTheEndOfFiscalYear: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(), description="期末自己株式数"
    )

    def __init__(self):
        super().__init__()
        for _, value in self.__dict__.items():
            if isinstance(value, ContextFilter):
                value.context = r"^Current"
        self.NoteToNumberOfIssuedAndOutstandingSharesCommonStock.regex = (
            r"tse-ed-t_.*NumberOfIssuedAndOutstandingSharesCommonStockAbstract$"
        )
        self.AverageNumberOfShares.regex = r"tse-ed-t_AverageNumberOfShares$"
        self.NumberOfIssuedAndOutstandingSharesAtTheEndOfFiscalYearIncludingTreasuryStock.regex = r"tse-ed-t_NumberOfIssuedAndOutstandingSharesAtTheEndOfFiscalYearIncludingTreasuryStock$"
        self.NumberOfTreasuryStockAtTheEndOfFiscalYear.regex = (
            r"tse-ed-t_NumberOfTreasuryStockAtTheEndOfFiscalYear$"
        )


class DividendPerShareJp(abstractBase):
    """1株当たり配当に関する情報を公開するためのクラス"""

    FirstQuarterPriorYearResults: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(
            context=r"(?=.*PriorYearDuration)(?=.*FirstQuarter)(?=.*Result)",
        ),
        description="昨季Q1期末1株当たり配当実績",
    )
    SecondQuarterPriorYearResults: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(
            context=r"(?=.*PriorYearDuration)(?=.*SecondQuarter)(?=.*Result)",
        ),
        description="昨季中間期末1株当たり配当実績",
    )
    ThirdQuarterPriorYearResults: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(
            context=r"(?=.*PriorYearDuration)(?=.*ThirdQuarter)(?=.*Result)",
        ),
        description="昨季Q3期末1株当たり配当実績",
    )
    YearEndPriorYearResults: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(
            context=r"(?=.*PriorYearDuration)(?=.*YearEnd)(?=.*Result)",
        ),
        description="昨季期末1株当たり配当実績",
    )
    AnnualPriorYearResults: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(
            context=r"(?=.*PriorYearDuration)(?=.*Annual)(?=.*Result)",
        ),
        description="昨季年間1株当たり配当実績",
    )
    FirstQuarterCurrentYearResults: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(
            context=r"(?=.*CurrentYearDuration)(?=.*FirstQuarter)(?=.*Result)",
        ),
        description="今期Q1期末1株当たり配当実績",
    )
    SecondQuarterCurrentYearResults: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(
            context=r"(?=.*CurrentYearDuration)(?=.*SecondQuarter)(?=.*Result)",
        ),
        description="今期中間期末1株当たり配当実績",
    )
    ThirdQuarterCurrentYearResults: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(
            context=r"(?=.*CurrentYearDuration)(?=.*ThirdQuarter)(?=.*Result)",
        ),
        description="今期Q3期末1株当たり配当実績",
    )
    YearEndCurrentYearResults: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(
            context=r"(?=.*CurrentYearDuration)(?=.*YearEnd)(?=.*Result)",
        ),
        description="今期期末1株当たり配当実績",
    )
    AnnualCurrentYearResults: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(
            context=r"(?=.*CurrentYearDuration)(?=.*Annual)(?=.*Result)",
        ),
        description="今期年間1株当たり配当実績",
    )
    FirstQuarterCurrentYearForecasts: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(
            context=r"(?=.*CurrentYearDuration)(?=.*FirstQuarter)(?=.*Forecast)",
        ),
        description="今期Q1期末1株当たり配当予想",
    )
    SecondQuarterCurrentYearForecasts: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(
            context=r"(?=.*CurrentYearDuration)(?=.*SecondQuarter)(?=.*Forecast)",
        ),
        description="今期中間期末1株当たり配当予想",
    )
    ThirdQuarterCurrentYearForecasts: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(
            context=r"(?=.*CurrentYearDuration)(?=.*ThirdQuarter)(?=.*Forecast)",
        ),
        description="今期Q3期末1株当たり配当予想",
    )
    YearEndCurrentYearForecasts: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(
            context=r"(?=.*CurrentYearDuration)(?=.*YearEnd)(?=.*Forecast)",
        ),
        description="今期期末1株当たり配当予想",
    )
    AnnualCurrentYearForecasts: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(
            context=r"(?=.*CurrentYearDuration)(?=.*Annual)(?=.*Forecast)",
        ),
        description="今期年間1株当たり配当予想",
    )
    FirstQuarterNextYearForecasts: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(
            context=r"(?=.*NextYearDuration)(?=.*FirstQuarter)(?=.*Forecast)",
        ),
        description="来期Q1期末1株当たり配当予想",
    )
    SecondQuarterNextYearForecasts: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(
            context=r"(?=.*NextYearDuration)(?=.*SecondQuarter)(?=.*Forecast)",
        ),
        description="来期中間期末1株当たり配当予想",
    )
    ThirdQuarterNextYearForecasts: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(
            context=r"(?=.*NextYearDuration)(?=.*ThirdQuarter)(?=.*Forecast)",
        ),
        description="来期Q3期末1株当たり配当予想",
    )
    YearEndNextYearForecasts: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(
            context=r"(?=.*NextYearDuration)(?=.*YearEnd)(?=.*Forecast)",
        ),
        description="来期期末1株当たり配当予想",
    )
    AnnualNextYearForecasts: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(
            context=r"(?=.*NextYearDuration)(?=.*Annual)(?=.*Forecast)",
        ),
        description="来期年間1株当たり配当予想",
    )

    def __init__(self):
        super().__init__()
        # すべての変数のregexに同じ値を設定
        for _, value in self.__dict__.items():
            if isinstance(value, ContextFilter):
                value.regex = r"tse-ed-t_DividendPerShare$"


class DividendsJp(abstractBase):
    """四半期配当に関する注記を公開するためのクラス"""

    DividendPerShare: Optional[DividendPerShareJp] = Field(
        default_factory=lambda: DividendPerShareJp(), description="1株当たり配当"
    )
    CorrectionOfDividendForecast: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(),
        description="当四半期における配当予想の修正",
    )
    DetailOfDividendPerShareFiscalYearEndAbstract: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(), description="期末1株当たり配当の内訳"
    )
    NoteToDividends: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(), description="配当に関する注記"
    )
    DividendPayoutRatioPriorYear: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(
            regex=r"^tse-ed-t_PayoutRatio.*",
            context=r"(?=.*PriorYear)(?=.*ResultMember)",
        ),
        description="配当性向",
    )
    DividendPayoutRatioCurrentYear: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(
            regex=r"^tse-ed-t_PayoutRatio.*",
            context=r"(?=.*CurrentYear)(?=.*ResultMember)",
        ),
        description="配当性向",
    )
    DividendPayoutRatioNextYear: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(
            regex=r"^tse-ed-t_PayoutRatio.*",
            context=r"(?=.*NextYear)(?=.*ForecastMember)",
        ),
        description="配当性向",
    )
    RatioOfTotalAmountOfDividendsToNetAssets: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(), description="配当総額純資産比率"
    )

    def __init__(self):
        super().__init__()
        # for _, value in self.__dict__.items():
        #     if isinstance(value, ContextFilter):
        #         if value.context is None:
        #             value.context = r"^Current"

        self.CorrectionOfDividendForecast.regex = (
            r"tse-ed-t_CorrectionOfDividendForecast.*$"
        )
        self.DividendPerShare.regex = r"tse-ed-t_DividendPerShareAbstract$"
        self.DetailOfDividendPerShareFiscalYearEndAbstract.regex = (
            r"tse-ed-t_DetailOfDividendPerShareFiscalYearEndAbstract$"
        )
        self.NoteToDividends.regex = r"tse-ed-t_NoteToDividends$"
        self.RatioOfTotalAmountOfDividendsToNetAssets.regex = (
            r"tse-ed-t_RatioOfTotalAmountOfDividendsToNetAssets$"
        )


class ForecastsJp(abstractBase):
    """四半期予想に関する注記を公開するためのクラス"""

    TitleForForecasts: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(), description="予想のタイトル"
    )
    CorrectionOfFinancialForecastInThisQuarter: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(),
        description="当四半期における連結業績予想の修正",
    )
    NetSales: Optional[abstract] = Field(
        default_factory=lambda: abstract(), description="売上高"
    )
    OperatingIncome: Optional[abstract] = Field(
        default_factory=lambda: abstract(), description="営業利益"
    )
    OrdinaryIncome: Optional[abstract] = Field(
        default_factory=lambda: abstract(), description="経常利益"
    )
    ProfitAttributableToOwnersOfParent: Optional[abstract] = Field(
        default_factory=lambda: abstract(),
        description="親会社株主に帰属する当期純利益",
    )
    NetIncomePerShare: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(), description="1株当たり当期純利益"
    )
    NoteToForecasts: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(), description="予想に関する注記"
    )
    PreambleToForecasts: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(), description="予想の前文"
    )

    def __init__(self):
        super().__init__()
        for _, value in self.__dict__.items():
            if isinstance(value, ContextFilter):
                value.context = r"(?=.*Forecast)"
        self.CorrectionOfFinancialForecastInThisQuarter.regex = (
            r"tse-ed-t_CorrectionOf.*FinancialForecastInThisQuarter$"
        )
        self.NetIncomePerShare.regex = r"tse-ed-t_NetIncomePerShare$"
        self.NetSales.regex = r"tse-ed-t_NetSalesAbstract$"
        self.NetSales.ChangeIn.regex = r"tse-ed-t_ChangeInNetSales$"
        self.NetSales.Values.regex = r"tse-ed-t_NetSales$"
        self.OperatingIncome.regex = r"tse-ed-t_OperatingIncomeAbstract$"
        self.OperatingIncome.ChangeIn.regex = r"tse-ed-t_ChangeInOperatingIncome$"
        self.OperatingIncome.Values.regex = r"tse-ed-t_OperatingIncome$"
        self.OrdinaryIncome.regex = r"tse-ed-t_OrdinaryIncomeAbstract$"
        self.OrdinaryIncome.ChangeIn.regex = r"tse-ed-t_ChangeInOrdinaryIncome$"
        self.OrdinaryIncome.Values.regex = r"tse-ed-t_OrdinaryIncome$"
        self.ProfitAttributableToOwnersOfParent.regex = (
            r"tse-ed-t_ProfitAttributableToOwnersOfParentAbstract$"
        )
        self.ProfitAttributableToOwnersOfParent.ChangeIn.regex = (
            r"tse-ed-t_ChangeInProfitAttributableToOwnersOfParent$"
        )
        self.ProfitAttributableToOwnersOfParent.Values.regex = (
            r"tse-ed-t_ProfitAttributableToOwnersOfParent$"
        )
        self.NoteToForecasts.regex = r"tse-ed-t_NoteToForecasts$"
        self.PreambleToForecasts.regex = r"tse-ed-t_PreambleToForecasts$"
        self.TitleForForecasts.regex = r"tse-ed-t_TitleForForecasts$"


class SignificantChangesInTheScopeOfConsolidationDuringThePeriodJp(abstractBase):
    """期間中の連結の範囲における重要な変更を公開するためのクラス"""

    NoteToSignificantChangesInTheScopeOfConsolidationDuringThePeriod: Optional[
        stockNumeric
    ] = Field(
        default_factory=lambda: stockNumeric(),
        description="期間中の連結の範囲における重要な変更に関する注記",
    )
    NameOfSubsidiariesExcludedFromConsolidation: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(),
        description="連結から除外された子会社の名称",
    )
    NameOfSubsidiariesNewlyConsolidated: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(),
        description="新たに連結された子会社の名称",
    )
    NumberOfSubsidiariesExcludedFromConsolidation: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(),
        description="連結から除外された子会社の数",
    )
    NumberOfSubsidiariesNewlyConsolidated: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(), description="新たに連結された子会社の数"
    )

    def __init__(self):
        super().__init__()
        for _, value in self.__dict__.items():
            if isinstance(value, ContextFilter):
                value.context = r"^Current"
        self.NoteToSignificantChangesInTheScopeOfConsolidationDuringThePeriod.regex = r"tse-ed-t_NoteToSignificantChangesInTheScopeOfConsolidationDuringThePeriod$"
        self.NameOfSubsidiariesExcludedFromConsolidation.regex = (
            r"tse-ed-t_NameOfSubsidiariesExcludedFromConsolidation$"
        )
        self.NameOfSubsidiariesNewlyConsolidated.regex = (
            r"tse-ed-t_NameOfSubsidiariesNewlyConsolidated$"
        )
        self.NumberOfSubsidiariesExcludedFromConsolidation.regex = (
            r"tse-ed-t_NumberOfSubsidiariesExcludedFromConsolidation$"
        )
        self.NumberOfSubsidiariesNewlyConsolidated.regex = (
            r"tse-ed-t_NumberOfSubsidiariesNewlyConsolidated$"
        )


class SpecialNotesJp(abstractBase):
    """四半期決算概要に関する特記事項を公開するためのクラス"""

    NotesForUsingForecastedInformationAndOthers: Optional[stock] = Field(
        default_factory=lambda: stock(),
        description="予想情報の利用等に関する注記",
    )
    ReviewOfAttachedConsolidatedQuarterlyFinancialStatementsByACertifiedPublicAccountantOrAnAuditFirm: Optional[
        stockNumeric
    ] = Field(
        default_factory=lambda: stockNumeric(),
        description="公認会計士若しくは監査法人による四半期連結財務諸表の監査の実施の有無",
    )

    def __init__(self):
        super().__init__()
        for _, value in self.__dict__.items():
            if isinstance(value, ContextFilter):
                value.context = r"^Current"
        self.NotesForUsingForecastedInformationAndOthers.regex = (
            r"tse-ed-t_NotesForUsingForecastedInformationAndOthers$"
        )
        self.ReviewOfAttachedConsolidatedQuarterlyFinancialStatementsByACertifiedPublicAccountantOrAnAuditFirm.regex = r"tse-ed-t_ReviewOfAttachedConsolidatedQuarterlyFinancialStatementsByACertifiedPublicAccountantOrAnAuditFirm$"


class SummaryItemsAbstractJp(TypeBase):
    """概要情報を公開するためのクラス"""

    XbrlId: Optional[str] = Field(default=None, description="XBRL識別子")
    DocumentEntityInformation: Optional[StockInfo] = Field(
        default_factory=lambda: StockInfo(), description="上場会社情報"
    )
    OperatingResult: Optional[OperatingResultJp] = Field(
        default_factory=lambda: OperatingResultJp(), description="業績情報"
    )
    NoteToFinancialResults: Optional[NoteToFinancialResultsJp] = Field(
        default_factory=lambda: NoteToFinancialResultsJp(),
        description="連結財務諸表に関する注記",
    )
    BusinessResultsFinancialPositions: Optional[BusinessResultsFinancialPositionsJp] = (
        Field(
            default_factory=lambda: BusinessResultsFinancialPositionsJp(),
            description="業績及び財政状態に関する注記",
        )
    )
    NotesApplyingSpecificAccountingQuarterlyFinancialStatements: Optional[
        NotesApplyingSpecificAccountingQuarterlyFinancialStatementsJp
    ] = Field(
        default_factory=lambda: NotesApplyingSpecificAccountingQuarterlyFinancialStatementsJp(),
        description="四半期連結財務諸表に適用する特定会計基準に関する注記",
    )
    NotesChangesAccountingPoliciesAccountingEstimatesRetrospectiveRestatement: Optional[
        NotesChangesAccountingPoliciesAccountingEstimatesRetrospectiveRestatementJp
    ] = Field(
        default_factory=lambda: NotesChangesAccountingPoliciesAccountingEstimatesRetrospectiveRestatementJp(),
        description="四半期連結財務諸表における会計方針の変更、会計上の見積りの変更及び遡及的な再表示に関する注記",
    )
    NotesNumberIssuedOutstandingSharesCommonStock: Optional[
        NotesNumberIssuedOutstandingSharesCommonStockJp
    ] = Field(
        default_factory=lambda: NotesNumberIssuedOutstandingSharesCommonStockJp(),
        description="四半期連結財務諸表における発行済株式数（普通株式）に関する注記",
    )
    Dividends: Optional[DividendsJp] = Field(
        default_factory=lambda: DividendsJp(),
        description="配当に関する注記",
    )
    Forecasts: Optional[ForecastsJp] = Field(
        default_factory=lambda: ForecastsJp(),
        description="四半期予想に関する注記",
    )
    SignificantChangesInTheScopeOfConsolidationDuringThePeriod: Optional[
        SignificantChangesInTheScopeOfConsolidationDuringThePeriodJp
    ] = Field(
        default_factory=lambda: SignificantChangesInTheScopeOfConsolidationDuringThePeriodJp(),
        description="期間中の連結の範囲における重要な変更",
    )
    SpecialNotes: Optional[SpecialNotesJp] = Field(
        default_factory=lambda: SpecialNotesJp(),
        description="四半期決算概要に関する特記事項",
    )

    def __init__(self):
        super().__init__()
        for _, value in self.__dict__.items():
            if isinstance(value, TypeBase):
                value.context = r"^Current"
        self.DocumentEntityInformation.regex = (
            r"tse-ed-t_DocumentEntityInformationHeading$"
        )
        self.OperatingResult.regex = (
            r"tse-ed-t_BusinessResults.*OperatingResultsHeading$"
        )
        self.NoteToFinancialResults.regex = (
            r"tse-ed-t_BusinessResultsNoteOverview.*BusinessResultsHeading$"
        )
        self.BusinessResultsFinancialPositions.regex = (
            r"tse-ed-t_BusinessResults.*FinancialPositionsHeading$"
        )
        self.NotesApplyingSpecificAccountingQuarterlyFinancialStatements.regex = r"tse-ed-t_Notes.*ApplyingSpecificAccountingConsolidatedQuarterlyFinancialStatementsHeading$"
        self.NotesChangesAccountingPoliciesAccountingEstimatesRetrospectiveRestatement.regex = r"tse-ed-t_Notes.*ChangesAccountingPoliciesAccountingEstimatesRetrospectiveRestatementHeading$"
        self.NotesNumberIssuedOutstandingSharesCommonStock.regex = (
            r"tse-ed-t_Notes.*NumberIssuedOutstandingSharesCommonStockHeading$"
        )
        self.Dividends.regex = r"tse-ed-t_.*DividendsHeading$"
        self.Forecasts.regex = r"tse-ed-t_.*ForecastsHeading$"
        self.SignificantChangesInTheScopeOfConsolidationDuringThePeriod.regex = r"tse-ed-t_SignificantChangesInTheScopeOfConsolidationDuringThePeriodHeading$"
        self.SpecialNotes.regex = r"tse-ed-t_SpecialNotes.*Heading$"


class SummaryItemsAbstractJpList(BaseModel):
    count: int = Field(default=0, description="概要情報のリスト数")
    data: List[SummaryItemsAbstractJp] = Field(
        default_factory=list, description="概要情報"
    )


# endregion


# region 特定事業会社
class IncomeStatementsInformationAbstractSpecificJp(abstractBase):
    """損益計算書情報を公開するためのクラス"""

    OrdinaryRevenuesAbstract: abstract = Field(
        default_factory=lambda: abstract(), description="経常収益の概要"
    )
    OrdinaryIncomeAbstract: abstract = Field(
        default_factory=lambda: abstract(), description="経常利益の概要"
    )
    ProfitAttributableToOwnersOfParentAbstract: abstract = Field(
        default_factory=lambda: abstract(),
        description="親会社株主に帰属する当期純利益の概要",
    )


class NoteToIncomeStatementsInformationAbstractSpecificJp(abstractBase):
    """損益計算書情報に関する注記を公開するためのクラス"""

    ComprehensiveIncomeAbstract: abstract = Field(
        default_factory=lambda: abstract(), description="包括利益"
    )


class OtherOperatingResultsAbstractSpecificJp(abstractBase):
    """その他の連結経営成績の概要を公開するためのクラス"""

    NetIncomePerShare: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(),
        description="1株当たり当期純利益（基本）",
    )
    DilutedNetIncomePerShare: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(), description="1株当たり当期純利益"
    )
    NetIncomeToShareholdersEquityRatio: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(), description="自己資本当期純利益率"
    )
    OrdinaryIncomeToTotalAssetsRatio: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(), description="総資産経常利益率"
    )
    OperatingIncomeToNetSalesRatio: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(), description="売上高営業利益率"
    )


class NoteToOperatingResultsAbstractSpecificJp(abstractBase):
    """業績情報に関する注記を公開するためのクラス"""

    NoteToOperatingResults: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(), description="業績情報に関する注記"
    )


class OperatingResultsSpecificAbstractJp(abstractBase):
    """業績情報を公開するためのクラス"""

    IncomeStatementsInformationAbstract: (
        IncomeStatementsInformationAbstractSpecificJp
    ) = Field(
        default_factory=lambda: IncomeStatementsInformationAbstractSpecificJp(),
        description="連結損益計算書情報",
    )
    NoteToIncomeStatementsInformationAbstract: (
        NoteToIncomeStatementsInformationAbstractSpecificJp
    ) = Field(
        default_factory=lambda: NoteToIncomeStatementsInformationAbstractSpecificJp(),
        description="連結損益計算書情報に関する注記",
    )
    OtherOperatingResultsAbstract: OtherOperatingResultsAbstractSpecificJp = Field(
        default_factory=lambda: OtherOperatingResultsAbstractSpecificJp(),
        description="その他の連結経営成績の概要",
    )


class OperatingResultSpecificJp(TypeBase):
    """業績情報を公開するためのクラス"""

    OperatingResultsAbstract: OperatingResultsSpecificAbstractJp = Field(
        default_factory=lambda: OperatingResultsSpecificAbstractJp(),
        description="業績情報",
    )
    NoteToOperatingResultsAbstract: NoteToOperatingResultsAbstractSpecificJp = Field(
        default_factory=lambda: NoteToOperatingResultsAbstractSpecificJp(),
        description="業績情報に関する注記",
    )


class SummaryItemsSpecificAbstractJp(TypeBase):
    """概要情報を公開するためのクラス"""

    DocumentEntityInformation: Optional[Union[StockInfo, dict]] = Field(
        default_factory=lambda: StockInfo(), description="上場会社情報"
    )
    OperatingResult: Optional[OperatingResultSpecificJp] = Field(
        default_factory=lambda: OperatingResultSpecificJp(), description="業績情報"
    )


# endregion
# endregion

# region IFRSのスキーマ


class IncomeStatementAbstractIfrs(abstractBase):
    """IFRS基準の損益計算書情報を公開するためのクラス"""

    NetSalesAbstract: abstract = Field(
        default_factory=lambda: abstract(), description="売上収益の概要"
    )
    OperatingIncomeAbstract: abstract = Field(
        default_factory=lambda: abstract(), description="営業利益の概要"
    )
    ProfitBeforeTaxAbstract: abstract = Field(
        default_factory=lambda: abstract(), description="税引前利益の概要"
    )
    ProfitAbstract: abstract = Field(
        default_factory=lambda: abstract(), description="当期利益の概要"
    )
    ProfitAttributableToOwnersOfParentAbstract: abstract = Field(
        default_factory=lambda: abstract(),
        description="親会社株主に帰属する当期純利益の概要",
    )
    TotalComprehensiveIncomeAbstract: abstract = Field(
        default_factory=lambda: abstract(), description="包括利益合計額の概要"
    )


class OtherOperatingResultsAbstractIfrs(abstractBase):
    """IFRS基準のその他の連結経営成績の概要を公開するためのクラス"""

    BasicEarningsPerShare: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(), description="基本1株当たり当期利益"
    )
    DilutedEarningsPerShare: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(), description="希薄化1株当たり当期利益"
    )
    ProfitToEquityAttributableToOwnersOfParentRatio: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(),
        description="自己資本親会社株主に帰属する当期純利益率",
    )
    ProfitBeforeTaxToTotalAssetsRatio: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(), description="総資産税引前利益率"
    )
    OperatingIncomeToSalesRatio: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(), description="売上高営業利益率"
    )


class NoteToOperatingResultAbstractIfrs(abstractBase):
    """IFRS基準の業績情報に関する注記を公開するためのクラス"""

    InvestmentsAccountedForUsingEquityMethod: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(), description="持分法適用会社に対する投資"
    )
    NoteToOperatingResult: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(), description="業績情報に関する注記"
    )


class OperatingResultsAbstractIfrs(abstractBase):
    """IFRS基準の業績情報を公開するためのクラス"""

    IncomeStatementsInformationAbstract: IncomeStatementAbstractIfrs = Field(
        default_factory=lambda: IncomeStatementAbstractIfrs(),
        description="連結損益計算書情報",
    )
    OtherOperatingResultsAbstract: OtherOperatingResultsAbstractIfrs = Field(
        default_factory=lambda: OtherOperatingResultsAbstractIfrs(),
        description="その他の連結経営成績の概要",
    )


class OperatingResultIfrs(TypeBase):
    """IFRS基準の業績情報を公開するためのクラス"""

    OperatingResultsAbstract: OperatingResultsAbstractIfrs = Field(
        default_factory=lambda: OperatingResultsAbstractIfrs(), description="業績情報"
    )
    NoteToOperatingResultAbstract: NoteToOperatingResultAbstractIfrs = Field(
        default_factory=lambda: NoteToOperatingResultAbstractIfrs(),
        description="業績情報に関する注記",
    )


class SummaryItemsAbstractIfrs(TypeBase):
    """ """

    DocumentEntityInformation: Optional[StockInfo] = Field(
        default_factory=lambda: StockInfo(), description="上場会社情報"
    )
    OperatingResult: Optional[OperatingResultIfrs] = Field(
        default_factory=lambda: OperatingResultIfrs(), description="業績情報"
    )


# endregion


# region 米国基準のスキーマ
class IncomeStatementsInformationAbstractUs(abstractBase):
    """米国基準の連結損益計算書情報を公開するためのクラス"""

    OperatingRevenuesUSAbstract: abstract = Field(
        default_factory=lambda: abstract(), description="営業収益（米国基準）"
    )
    OperatingIncomeUSAbstract: abstract = Field(
        default_factory=lambda: abstract(), description="営業利益（米国基準）"
    )
    IncomeBeforeIncomeTaxesUSAbstract: abstract = Field(
        default_factory=lambda: abstract(), description="税引前利益（米国基準）"
    )
    NetIncomeUSAbstract: abstract = Field(
        default_factory=lambda: abstract(), description="当期純利益（米国基準）"
    )


class OtherOperatingResultsAbstractUs(abstractBase):
    """米国基準のその他の連結経営成績の概要を公開するためのクラス"""

    NetIncomePerShareUS: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(),
        description="1株当たり当期純利益（基本）",
    )
    DilutedNetIncomePerShare2US: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(), description="希薄化1株当たり当期純利益"
    )


class NoteToOperatingResultsAbstractUs(abstractBase):
    """米国基準の業績情報に関する注記を公開するためのクラス"""

    NoteToOperatingResults: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(), description="業績情報に関する注記"
    )


class NoteToIncomeStatementsInformationAbstractUs(abstractBase):
    """米国基準の連結損益計算書情報に関する注記を公開するためのクラス"""

    ComprehensiveIncomeUSAbstract: abstract = Field(
        default_factory=lambda: abstract(), description="包括利益（米国基準）"
    )


class OperatingResultsAbstractUs(abstractBase):
    IncomeStatementsInformationAbstract: IncomeStatementsInformationAbstractUs = Field(
        default_factory=lambda: IncomeStatementsInformationAbstractUs(),
        description="連結損益計算書情報",
    )
    NoteToIncomeStatementsInformationAbstract: (
        NoteToIncomeStatementsInformationAbstractUs
    ) = Field(
        default_factory=lambda: NoteToIncomeStatementsInformationAbstractUs(),
        description="連結損益計算書情報に関する注記",
    )
    OtherOperatingResultsAbstract: OtherOperatingResultsAbstractUs = Field(
        default_factory=lambda: OtherOperatingResultsAbstractUs(),
        description="その他の連結経営成績の概要",
    )


class OperatingResultUs(TypeBase):
    """米国基準の業績情報を公開するためのクラス"""

    OperatingResultsAbstract: OperatingResultsAbstractUs = Field(
        default_factory=lambda: OperatingResultsAbstractUs(), description="業績情報"
    )
    NoteToOperatingResultsAbstract: NoteToOperatingResultsAbstractUs = Field(
        default_factory=lambda: NoteToOperatingResultsAbstractUs(),
        description="業績情報に関する注記",
    )


class SummaryItemsAbstractUs(TypeBase):
    DocumentEntityInformation: Optional[StockInfo] = Field(
        default_factory=lambda: StockInfo(), description="上場会社情報"
    )
    OperatingResult: Optional[OperatingResultUs] = Field(
        default_factory=lambda: OperatingResultUs(), description="業績情報"
    )


# endregion

# endregion


class SimpleSummaryFractionItems(BaseModel):
    """概要情報を公開するためのクラス"""

    CompanyName: Optional[stock] = Field(
        default_factory=lambda: stock(
            label="会社名",
            regex=r"tse-ed-t_CompanyName$",
        ),
        description="会社名",
    )
    DocumentName: Optional[stock] = Field(
        default_factory=lambda: stock(
            label="文書名",
            regex=r"tse-ed-t_DocumentName$",
        ),
        description="文書名",
    )
    Securities_code: Optional[stock] = Field(
        default_factory=lambda: stock(
            label="証券コード",
            regex=r"tse-ed-t_SecuritiesCode$",
        ),
        description="証券コード",
    )

    def __init__(self, items: sc.ix_non_numeric.IxNonNumericsPublic):
        super().__init__()
        for item in items.data:
            regex = item.name
            context = item.context
            # クラスフィールドをループ処理
            for _, value in self.__dict__.items():
                # stock型の場合
                if isinstance(value, stock):
                    if value.context is None:
                        value.context = r"^Current"
                    if re.match(value.regex, regex):
                        if re.match(value.context, context):
                            value.value = item.value
                            break


class SimpleSummaryNumericItems(BaseModel):

    NetSales: Optional[abstract] = Field(
        default_factory=lambda: abstract(
            Label="売上高",
            Values=stockNumeric(
                label="売上高",
                regex=r"tse-ed-t_NetSales$",
            ),
            ChangeIn=stockNumeric(
                label="増益率",
                regex=r"tse-ed-t_ChangeInNetSales$",
            ),
        ),
        description="売上高",
    )
    OperatingIncome: Optional[abstract] = Field(
        default_factory=lambda: abstract(
            Label="営業利益",
            Values=stockNumeric(
                label="営業利益",
                regex=r"tse-ed-t_OperatingIncome$",
            ),
            ChangeIn=stockNumeric(
                label="増益率",
                regex=r"tse-ed-t_ChangeInOperatingIncome$",
            ),
        ),
        description="営業利益",
    )
    OrdinaryIncome: Optional[abstract] = Field(
        default_factory=lambda: abstract(
            Label="経常利益",
            Values=stockNumeric(
                label="経常利益",
                regex=r"tse-ed-t_OrdinaryIncome$",
            ),
            ChangeIn=stockNumeric(
                label="増益率",
                regex=r"tse-ed-t_ChangeInOrdinaryIncome$",
            ),
        ),
        description="経常利益",
    )
    Profit: Optional[abstract] = Field(
        default_factory=lambda: abstract(
            Label="当期純利益",
            Values=stockNumeric(
                label="当期純利益",
                regex=r"tse-ed-t_Profit.*$",
            ),
            ChangeIn=stockNumeric(
                label="増益率",
                regex=r"tse-ed-t_ChangeInProfit.*$",
            ),
        ),
        description="当期純利益",
    )
    TotalAsset: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(
            label="総資産",
            regex=r"tse-ed-t_TotalAssets$",
        ),
        description="総資産",
    )
    NetAssets: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(
            label="純資産",
            regex=r"tse-ed-t_NetAssets$",
        ),
        description="純資産",
    )
    NetIncomePerShare: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(
            label="1株当たり当期純利益",
            regex=r"tse-ed-t_NetIncomePerShare$",
        ),
        description="1株当たり当期純利益",
    )
    FirstQuarterDividendPerShare: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(
            label="1株当たり配当",
            regex=r"tse-ed-t_DividendPerShare$",
            context=r"(?=.*FirstQuarter)",
        ),
        description="第1四半期1株当たり配当",
    )
    SecondQuarterDividendPerShare: Optional[stockNumeric] = Field(
        default_factory=lambda: stockNumeric(
            label="1株当たり配当",
            regex=r"tse-ed-t_DividendPerShare$",
            context=r"(?=.*SecondQuarter)",
        ),
        description="第2四半期1株当たり配当",
    )

    def __init__(
        self,
        items: Optional[sc.ix_non_fraction.IxNonFractionsPublic],
        year: str,
        member: str,
    ):
        super().__init__()
        for item in items.data:
            regex = item.name
            context = item.context
            # クラスフィールドをループ処理
            for _, value in self.__dict__.items():
                # stock型の場合
                if isinstance(value, abstract):
                    # フィールド名が一致する場合
                    value.Values.context = (
                        r"(?=.*" + year + ")(?=.*" + member + ")" + value.Values.context
                    )
                    value.ChangeIn.context = (
                        r"(?=.*"
                        + year
                        + ")(?=.*"
                        + member
                        + ")"
                        + value.ChangeIn.context
                    )
                    if re.match(value.Values.regex, regex):
                        if re.match(value.Values.context, context):
                            value.Values.value = item.display_numeric
                            value.Values.numeric = item.numeric
                            value.Values.scale = item.display_scale
                    if re.match(value.ChangeIn.regex, regex):
                        if re.match(value.ChangeIn.context, context):
                            value.ChangeIn.value = item.display_numeric
                            value.ChangeIn.numeric = item.numeric
                            value.ChangeIn.scale = item.display_scale
                elif isinstance(value, stockNumeric):
                    value.context = (
                        r"(?=.*" + year + ")(?=.*" + member + ")" + value.context
                    )
                    if re.match(value.regex, regex):
                        if re.match(value.context, context):
                            value.value = item.display_numeric
                            value.numeric = item.numeric
                            value.scale = item.display_scale


class SimpleSummaryItems(BaseModel):

    FractionItems: Optional[SimpleSummaryFractionItems] = Field(
        default_factory=lambda: SimpleSummaryFractionItems(),
        description="非数値情報",
    )
    PriorResultNumericItems: Optional[SimpleSummaryNumericItems] = Field(
        description="昨年度実績",
    )
    CurrentResultNumericItems: Optional[SimpleSummaryNumericItems] = Field(
        description="今年度実績",
    )
    CurrentForecastNumericItems: Optional[SimpleSummaryNumericItems] = Field(
        description="今年度予想",
    )
    NextForecastNumericItems: Optional[SimpleSummaryNumericItems] = Field(
        description="来年度予想",
    )
