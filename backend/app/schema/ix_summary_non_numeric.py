from app.models import Field, SQLModel
from app.schema.ix_non_numeric import IxNonNumericPublic


class IxbrlBase(SQLModel):
    key: str = Field(default=None, description="識別キー")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.key = self.__class__.__name__


class CondensedQuarterlyConsolidatedStatementOfCashFlowsIFRSTextBlock_edif_CondensedQuarterlyConsolidatedStatementOfCashFlowsIFRS_consolidated_Q2(SQLModel):
    """ 要約四半期連結キャッシュ・フロー計算書（IFRS） [テキストブロック] """

    current_ytd_duration: IxNonNumericPublic = Field(default=None, description="当年度期初から当日まで")
    """ 当年度期初から当日まで """


class CondensedQuarterlyConsolidatedStatementOfCashFlowsIFRSTextBlock_edif_CondensedQuarterlyConsolidatedStatementOfCashFlowsIFRS_consolidated_Q3(SQLModel):
    """ 要約四半期連結キャッシュ・フロー計算書（IFRS） [テキストブロック] """

    current_ytd_duration: IxNonNumericPublic = Field(default=None, description="当年度期初から当日まで")
    """ 当年度期初から当日まで """


class CondensedQuarterlyConsolidatedStatementOfCashFlowsIFRSTextBlock_edif_CondensedQuarterlyConsolidatedStatementOfChangesInEquityIFRS_consolidated_Q2(SQLModel):
    """ 要約四半期連結キャッシュ・フロー計算書（IFRS） [テキストブロック] """

    current_ytd_duration: IxNonNumericPublic = Field(default=None, description="当年度期初から当日まで")
    """ 当年度期初から当日まで """


class CondensedQuarterlyConsolidatedStatementOfChangesInEquityIFRSTextBlock_edif_CondensedQuarterlyConsolidatedStatementOfChangesInEquityIFRS_consolidated_Q2(SQLModel):
    """ 要約四半期連結持分変動計算書（IFRS） [テキストブロック] """

    current_ytd_duration: IxNonNumericPublic = Field(default=None, description="当年度期初から当日まで")
    """ 当年度期初から当日まで """


class CondensedQuarterlyConsolidatedStatementOfChangesInEquityIFRSTextBlock_edif_CondensedQuarterlyConsolidatedStatementOfChangesInEquityIFRS_consolidated_Q3(SQLModel):
    """ 要約四半期連結持分変動計算書（IFRS） [テキストブロック] """

    current_ytd_duration: IxNonNumericPublic = Field(default=None, description="当年度期初から当日まで")
    """ 当年度期初から当日まで """


class AccountingStandardsDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q2(SQLModel):
    """ 会計基準、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class AmendmentFlagDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q2(SQLModel):
    """ 訂正の有無、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class CabinetOfficeOrdinanceDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q2(SQLModel):
    """ 府令、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class ComparativePeriodEndDateDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q2(SQLModel):
    """ 比較対象会計期間終了日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class CurrentFiscalYearEndDateDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q2(SQLModel):
    """ 当事業年度終了日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class CurrentFiscalYearStartDateDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q2(SQLModel):
    """ 当事業年度開始日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class CurrentPeriodEndDateDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q2(SQLModel):
    """ 当会計期間終了日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class DocumentTypeDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q2(SQLModel):
    """ 様式、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class EDINETCodeDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q2(SQLModel):
    """ EDINETコード、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class EndDateOfQuarterlyOrSemiAnnualPeriodOfNextFiscalYearDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q2(SQLModel):
    """ 次の四半期又は中間期の会計期間終了日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class FilerNameInEnglishDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q2(SQLModel):
    """ 提出者名（英語表記）、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class FilerNameInJapaneseDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q2(SQLModel):
    """ 提出者名（日本語表記）、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class FundCodeDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q2(SQLModel):
    """ ファンドコード、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class FundNameInEnglishDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q2(SQLModel):
    """ ファンド名称（英語表記）、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class FundNameInJapaneseDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q2(SQLModel):
    """ ファンド名称（日本語表記）、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class IdentificationOfDocumentSubjectToAmendmentDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q2(SQLModel):
    """ 訂正対象書類の書類管理番号、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class IndustryCodeWhenConsolidatedFinancialStatementsArePreparedInAccordanceWithIndustrySpecificRegulationsDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q2(SQLModel):
    """ 別記事業（連結）、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class IndustryCodeWhenFinancialStatementsArePreparedInAccordanceWithIndustrySpecificRegulationsDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q2(SQLModel):
    """ 別記事業（個別）、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class NextFiscalYearStartDateDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q2(SQLModel):
    """ 次の事業年度開始日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class PreviousFiscalYearEndDateDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q2(SQLModel):
    """ 前事業年度終了日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class PreviousFiscalYearStartDateDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q2(SQLModel):
    """ 前事業年度開始日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class ReportAmendmentFlagDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q2(SQLModel):
    """ 記載事項訂正のフラグ、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class SecurityCodeDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q2(SQLModel):
    """ 証券コード、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class TypeOfCurrentPeriodDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q2(SQLModel):
    """ 当会計期間の種類、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class WhetherConsolidatedFinancialStatementsArePreparedDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q2(SQLModel):
    """ 連結決算の有無、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class XBRLAmendmentFlagDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q2(SQLModel):
    """ XBRL訂正のフラグ、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRSTextBlock_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q2(SQLModel):
    """ 要約四半期連結財政状態計算書（IFRS） [テキストブロック] """

    current_ytd_duration: IxNonNumericPublic = Field(default=None, description="当年度期初から当日まで")
    """ 当年度期初から当日まで """


class AccountingStandardsDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q3(SQLModel):
    """ 会計基準、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class AmendmentFlagDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q3(SQLModel):
    """ 訂正の有無、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class CabinetOfficeOrdinanceDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q3(SQLModel):
    """ 府令、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class ComparativePeriodEndDateDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q3(SQLModel):
    """ 比較対象会計期間終了日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class CurrentFiscalYearEndDateDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q3(SQLModel):
    """ 当事業年度終了日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class CurrentFiscalYearStartDateDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q3(SQLModel):
    """ 当事業年度開始日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class CurrentPeriodEndDateDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q3(SQLModel):
    """ 当会計期間終了日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class DocumentTypeDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q3(SQLModel):
    """ 様式、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class EDINETCodeDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q3(SQLModel):
    """ EDINETコード、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class EndDateOfQuarterlyOrSemiAnnualPeriodOfNextFiscalYearDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q3(SQLModel):
    """ 次の四半期又は中間期の会計期間終了日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class FilerNameInEnglishDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q3(SQLModel):
    """ 提出者名（英語表記）、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class FilerNameInJapaneseDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q3(SQLModel):
    """ 提出者名（日本語表記）、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class FundCodeDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q3(SQLModel):
    """ ファンドコード、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class FundNameInEnglishDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q3(SQLModel):
    """ ファンド名称（英語表記）、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class FundNameInJapaneseDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q3(SQLModel):
    """ ファンド名称（日本語表記）、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class IdentificationOfDocumentSubjectToAmendmentDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q3(SQLModel):
    """ 訂正対象書類の書類管理番号、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class IndustryCodeWhenConsolidatedFinancialStatementsArePreparedInAccordanceWithIndustrySpecificRegulationsDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q3(SQLModel):
    """ 別記事業（連結）、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class IndustryCodeWhenFinancialStatementsArePreparedInAccordanceWithIndustrySpecificRegulationsDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q3(SQLModel):
    """ 別記事業（個別）、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class NextFiscalYearStartDateDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q3(SQLModel):
    """ 次の事業年度開始日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class PreviousFiscalYearEndDateDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q3(SQLModel):
    """ 前事業年度終了日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class PreviousFiscalYearStartDateDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q3(SQLModel):
    """ 前事業年度開始日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class ReportAmendmentFlagDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q3(SQLModel):
    """ 記載事項訂正のフラグ、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class SecurityCodeDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q3(SQLModel):
    """ 証券コード、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class TypeOfCurrentPeriodDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q3(SQLModel):
    """ 当会計期間の種類、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class WhetherConsolidatedFinancialStatementsArePreparedDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q3(SQLModel):
    """ 連結決算の有無、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class XBRLAmendmentFlagDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q3(SQLModel):
    """ XBRL訂正のフラグ、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRSTextBlock_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q3(SQLModel):
    """ 要約四半期連結財政状態計算書（IFRS） [テキストブロック] """

    current_ytd_duration: IxNonNumericPublic = Field(default=None, description="当年度期初から当日まで")
    """ 当年度期初から当日まで """


class CondensedQuarterPeriodConsolidatedStatementOfComprehensiveIncomeIFRSTextBlock_edif_CondensedQuarterPeriodConsolidatedStatementOfComprehensiveIncomeIFRS_consolidated_Q3(SQLModel):
    """ 四半期連結会計期間、要約四半期連結包括利益計算書（IFRS） [テキストブロック] """

    current_quarter_duration: IxNonNumericPublic = Field(default=None, description="当四半期会計期間")
    """ 当四半期会計期間 """


class CondensedQuarterPeriodConsolidatedStatementOfProfitOrLossIFRSTextBlock_edif_CondensedQuarterPeriodConsolidatedStatementOfProfitOrLossIFRS_consolidated_Q3(SQLModel):
    """ 四半期連結会計期間、要約四半期連結損益計算書（IFRS） [テキストブロック] """

    current_quarter_duration: IxNonNumericPublic = Field(default=None, description="当四半期会計期間")
    """ 当四半期会計期間 """


class CondensedYearToQuarterEndConsolidatedStatementOfComprehensiveIncomeIFRSTextBlock_edif_CondensedYearToQuarterEndConsolidatedStatementOfComprehensiveIncomeIFRS_consolidated_Q2(SQLModel):
    """ 四半期連結累計期間、要約四半期連結包括利益計算書（IFRS） [テキストブロック] """

    current_ytd_duration: IxNonNumericPublic = Field(default=None, description="当年度期初から当日まで")
    """ 当年度期初から当日まで """


class CondensedYearToQuarterEndConsolidatedStatementOfComprehensiveIncomeIFRSTextBlock_edif_CondensedYearToQuarterEndConsolidatedStatementOfComprehensiveIncomeIFRS_consolidated_Q3(SQLModel):
    """ 四半期連結累計期間、要約四半期連結包括利益計算書（IFRS） [テキストブロック] """

    current_ytd_duration: IxNonNumericPublic = Field(default=None, description="当年度期初から当日まで")
    """ 当年度期初から当日まで """


class CondensedYearToQuarterEndConsolidatedStatementOfComprehensiveIncomeSingleStatementIFRSTextBlock_edif_CondensedYearToQuarterEndConsolidatedStatementOfComprehensiveIncomeSingleStatementIFRS_consolidated_Q2(SQLModel):
    """ 四半期連結累計期間、要約四半期連結包括利益計算書（１計算書）（IFRS） [テキストブロック] """

    current_ytd_duration: IxNonNumericPublic = Field(default=None, description="当年度期初から当日まで")
    """ 当年度期初から当日まで """


class AccountingStandardsDEI_edif_CondensedYearToQuarterEndConsolidatedStatementOfProfitOrLossIFRS_consolidated_Q2(SQLModel):
    """ 会計基準、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class AmendmentFlagDEI_edif_CondensedYearToQuarterEndConsolidatedStatementOfProfitOrLossIFRS_consolidated_Q2(SQLModel):
    """ 訂正の有無、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class CabinetOfficeOrdinanceDEI_edif_CondensedYearToQuarterEndConsolidatedStatementOfProfitOrLossIFRS_consolidated_Q2(SQLModel):
    """ 府令、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class ComparativePeriodEndDateDEI_edif_CondensedYearToQuarterEndConsolidatedStatementOfProfitOrLossIFRS_consolidated_Q2(SQLModel):
    """ 比較対象会計期間終了日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class CurrentFiscalYearEndDateDEI_edif_CondensedYearToQuarterEndConsolidatedStatementOfProfitOrLossIFRS_consolidated_Q2(SQLModel):
    """ 当事業年度終了日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class CurrentFiscalYearStartDateDEI_edif_CondensedYearToQuarterEndConsolidatedStatementOfProfitOrLossIFRS_consolidated_Q2(SQLModel):
    """ 当事業年度開始日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class CurrentPeriodEndDateDEI_edif_CondensedYearToQuarterEndConsolidatedStatementOfProfitOrLossIFRS_consolidated_Q2(SQLModel):
    """ 当会計期間終了日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class DocumentTypeDEI_edif_CondensedYearToQuarterEndConsolidatedStatementOfProfitOrLossIFRS_consolidated_Q2(SQLModel):
    """ 様式、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class EDINETCodeDEI_edif_CondensedYearToQuarterEndConsolidatedStatementOfProfitOrLossIFRS_consolidated_Q2(SQLModel):
    """ EDINETコード、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class EndDateOfQuarterlyOrSemiAnnualPeriodOfNextFiscalYearDEI_edif_CondensedYearToQuarterEndConsolidatedStatementOfProfitOrLossIFRS_consolidated_Q2(SQLModel):
    """ 次の四半期又は中間期の会計期間終了日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class FilerNameInEnglishDEI_edif_CondensedYearToQuarterEndConsolidatedStatementOfProfitOrLossIFRS_consolidated_Q2(SQLModel):
    """ 提出者名（英語表記）、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class FilerNameInJapaneseDEI_edif_CondensedYearToQuarterEndConsolidatedStatementOfProfitOrLossIFRS_consolidated_Q2(SQLModel):
    """ 提出者名（日本語表記）、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class FundCodeDEI_edif_CondensedYearToQuarterEndConsolidatedStatementOfProfitOrLossIFRS_consolidated_Q2(SQLModel):
    """ ファンドコード、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class FundNameInEnglishDEI_edif_CondensedYearToQuarterEndConsolidatedStatementOfProfitOrLossIFRS_consolidated_Q2(SQLModel):
    """ ファンド名称（英語表記）、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class FundNameInJapaneseDEI_edif_CondensedYearToQuarterEndConsolidatedStatementOfProfitOrLossIFRS_consolidated_Q2(SQLModel):
    """ ファンド名称（日本語表記）、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class IdentificationOfDocumentSubjectToAmendmentDEI_edif_CondensedYearToQuarterEndConsolidatedStatementOfProfitOrLossIFRS_consolidated_Q2(SQLModel):
    """ 訂正対象書類の書類管理番号、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class IndustryCodeWhenConsolidatedFinancialStatementsArePreparedInAccordanceWithIndustrySpecificRegulationsDEI_edif_CondensedYearToQuarterEndConsolidatedStatementOfProfitOrLossIFRS_consolidated_Q2(SQLModel):
    """ 別記事業（連結）、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class IndustryCodeWhenFinancialStatementsArePreparedInAccordanceWithIndustrySpecificRegulationsDEI_edif_CondensedYearToQuarterEndConsolidatedStatementOfProfitOrLossIFRS_consolidated_Q2(SQLModel):
    """ 別記事業（個別）、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class NextFiscalYearStartDateDEI_edif_CondensedYearToQuarterEndConsolidatedStatementOfProfitOrLossIFRS_consolidated_Q2(SQLModel):
    """ 次の事業年度開始日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class PreviousFiscalYearEndDateDEI_edif_CondensedYearToQuarterEndConsolidatedStatementOfProfitOrLossIFRS_consolidated_Q2(SQLModel):
    """ 前事業年度終了日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class PreviousFiscalYearStartDateDEI_edif_CondensedYearToQuarterEndConsolidatedStatementOfProfitOrLossIFRS_consolidated_Q2(SQLModel):
    """ 前事業年度開始日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class ReportAmendmentFlagDEI_edif_CondensedYearToQuarterEndConsolidatedStatementOfProfitOrLossIFRS_consolidated_Q2(SQLModel):
    """ 記載事項訂正のフラグ、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class SecurityCodeDEI_edif_CondensedYearToQuarterEndConsolidatedStatementOfProfitOrLossIFRS_consolidated_Q2(SQLModel):
    """ 証券コード、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class TypeOfCurrentPeriodDEI_edif_CondensedYearToQuarterEndConsolidatedStatementOfProfitOrLossIFRS_consolidated_Q2(SQLModel):
    """ 当会計期間の種類、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class WhetherConsolidatedFinancialStatementsArePreparedDEI_edif_CondensedYearToQuarterEndConsolidatedStatementOfProfitOrLossIFRS_consolidated_Q2(SQLModel):
    """ 連結決算の有無、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class XBRLAmendmentFlagDEI_edif_CondensedYearToQuarterEndConsolidatedStatementOfProfitOrLossIFRS_consolidated_Q2(SQLModel):
    """ XBRL訂正のフラグ、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class CondensedYearToQuarterEndConsolidatedStatementOfProfitOrLossIFRSTextBlock_edif_CondensedYearToQuarterEndConsolidatedStatementOfProfitOrLossIFRS_consolidated_Q2(SQLModel):
    """ 四半期連結累計期間、要約四半期連結損益計算書（IFRS） [テキストブロック] """

    current_ytd_duration: IxNonNumericPublic = Field(default=None, description="当年度期初から当日まで")
    """ 当年度期初から当日まで """


class CondensedYearToQuarterEndConsolidatedStatementOfProfitOrLossIFRSTextBlock_edif_CondensedYearToQuarterEndConsolidatedStatementOfProfitOrLossIFRS_consolidated_Q3(SQLModel):
    """ 四半期連結累計期間、要約四半期連結損益計算書（IFRS） [テキストブロック] """

    current_ytd_duration: IxNonNumericPublic = Field(default=None, description="当年度期初から当日まで")
    """ 当年度期初から当日まで """


class ChangesInAccountingEstimatesIFRS_edif_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 会計上の見積りの変更、IFRS """

    current_accumulated_q2_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間_連結_実績")
    """ 当年度期初から第２四半期間_連結_実績 """


class ChangesInAccountingPoliciesOtherThanIFRSRequirementsIFRS_edif_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ IFRSにより要求される会計方針の変更以外の会計方針の変更、IFRS """

    current_accumulated_q2_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間_連結_実績")
    """ 当年度期初から第２四半期間_連結_実績 """


class ChangesInAccountingPoliciesRequiredByIFRSIFRS_edif_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ IFRSにより要求される会計方針の変更、IFRS """

    current_accumulated_q2_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間_連結_実績")
    """ 当年度期初から第２四半期間_連結_実績 """


class CompanyName_edif_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 上場会社名 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class ConveningBriefingOfResults_edif_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 決算説明会開催の有無、期中 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class CorrectionOfConsolidatedFinancialForecastInThisQuarter_edif_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 直近に公表されている業績予想からの修正の有無、連結 """

    current_year_duration_consolidated_member_forecast_member: IxNonNumericPublic = Field(default=None, description="当年度会計期間_連結_予想")
    """ 当年度会計期間_連結_予想 """


class CorrectionOfDividendForecastInThisQuarter_edif_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 直近に公表されている配当予想からの修正の有無 """

    current_year_duration_annual_member_non_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度会計期間_年間_非連結又は個別_実績")
    """ 当年度会計期間_年間_非連結又は個別_実績 """


class DividendPayableDateAsPlanned_edif_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 配当支払開始予定日 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class DocumentName_edif_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 文書名 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class FASFMemberMark_edif_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 財務会計基準機構会員マーク """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class FilingDate_edif_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 提出日 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class FiscalYearEnd_edif_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 決算期 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class FukuokaStockExchange_edif_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 福岡証券取引所 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class FukuokaStockExchangeEstablished_edif_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 福岡証券取引所 既存市場 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class FukuokaStockExchangeOthers_edif_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 福岡証券取引所 その他 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class FukuokaStockExchangeQBoard_edif_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 福岡証券取引所 Q-Board """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class GeneralBusiness_edif_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 一般事業会社 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class JapanSecuritiesDealersAssociation_edif_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ フェニックス """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class JapanSecuritiesDealersAssociationGreenSheet_edif_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 日本証券業協会 フェニックス """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class NagoyaStockExchange_edif_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 名古屋証券取引所 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class NagoyaStockExchange1stSection_edif_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 名古屋証券取引所 プレミア """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class NagoyaStockExchange2ndSection_edif_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 名古屋証券取引所 メイン """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class NagoyaStockExchangeCentrex_edif_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 名古屋証券取引所 ネクスト """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class NagoyaStockExchangeOthers_edif_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 名古屋証券取引所 その他 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class NameInquiries_edif_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 氏名、問合せ先責任者 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class NameOfSubsidiariesExcludedFromConsolidationIFRS_edif_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 社名、除外、IFRS """

    current_accumulated_q2_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間_連結_実績")
    """ 当年度期初から第２四半期間_連結_実績 """


class NameOfSubsidiariesNewlyConsolidatedIFRS_edif_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 社名、新規、IFRS """

    current_accumulated_q2_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間_連結_実績")
    """ 当年度期初から第２四半期間_連結_実績 """


class NameRepresentative_edif_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 氏名、代表者 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class NotesForUsingForecastedInformationAndOthers_edif_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 業績予想の適切な利用に関する説明、その他特記事項 """

    current_year_duration: IxNonNumericPublic = Field(default=None, description="当年度会計期間")
    """ 当年度会計期間 """


class NoteToChangesInAccountingPoliciesAndAccountingEstimatesIFRS_edif_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 会計方針の変更・会計上の見積りの変更に関する注記、IFRS """

    current_accumulated_q2_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間_連結_実績")
    """ 当年度期初から第２四半期間_連結_実績 """


class NoteToConsolidatedFinancialResults_edif_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 連結業績に関する注記 """

    current_accumulated_q2_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間_連結_実績")
    """ 当年度期初から第２四半期間_連結_実績 """


class NoteToDividends_edif_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 配当の状況に関する注記 """

    current_accumulated_q2_duration_annual_member_non_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間_年間_非連結又は個別_実績")
    """ 当年度期初から第２四半期間_年間_非連結又は個別_実績 """


class NoteToFinancialPositions_edif_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 財政状態に関する注記 """

    current_accumulated_q2_instant_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点_連結_実績")
    """ 当年度期初から第２四半期間時点_連結_実績 """


class NoteToForecasts_edif_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 業績予想に関する事項、注記 """

    current_year_duration_consolidated_member_forecast_member: IxNonNumericPublic = Field(default=None, description="当年度会計期間_連結_予想")
    """ 当年度会計期間_連結_予想 """


class NoteToFractionProcessingMethod_edif_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 端数処理方法に関する注記 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class NoteToNumberOfIssuedAndOutstandingSharesCommonStock_edif_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 発行済株式数（普通株式）に関する注記 """

    current_accumulated_q2_instant_non_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点_非連結又は個別_実績")
    """ 当年度期初から第２四半期間時点_非連結又は個別_実績 """


class NoteToOperatingResults_edif_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 経営成績に関する注記 """

    current_accumulated_q2_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間_連結_実績")
    """ 当年度期初から第２四半期間_連結_実績 """


class NoteToSignificantChangesInTheScopeOfConsolidationDuringThePeriod_edif_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 期中における連結範囲の重要な変更に関する注記 """

    current_accumulated_q2_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間_連結_実績")
    """ 当年度期初から第２四半期間_連結_実績 """


class PreambleToForecasts_edif_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 業績予想に関する事項 """

    current_year_duration_consolidated_member_forecast_member: IxNonNumericPublic = Field(default=None, description="当年度会計期間_連結_予想")
    """ 当年度会計期間_連結_予想 """


class SapporoStockExchange_edif_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 札幌証券取引所 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class SapporoStockExchangeAmbitious_edif_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 札幌証券取引所 アンビシャス """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class SapporoStockExchangeEstablished_edif_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 札幌証券取引所 既存市場 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class SapporoStockExchangeOthers_edif_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 札幌証券取引所 その他 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class SecuritiesCode_edif_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ コード番号 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class SemiAnnualStatementFilingDateAsPlanned_edif_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 半期報告書提出予定日 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class SignificantChangesInTheScopeOfConsolidationDuringThePeriodIFRS_edif_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 期中における連結範囲の重要な変更、IFRS """

    current_accumulated_q2_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間_連結_実績")
    """ 当年度期初から第２四半期間_連結_実績 """


class SpecificBusiness_edif_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 特定事業会社 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class SupplementalMaterialOfResults_edif_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 決算補足説明資料作成の有無、期中 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class TargetForBriefingOfResults_edif_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 決算説明会の対象者 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class Tel_edif_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ TEL """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class TitleForForecasts_edif_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 業績予想タイトル名称 """

    current_year_duration_consolidated_member_forecast_member: IxNonNumericPublic = Field(default=None, description="当年度会計期間_連結_予想")
    """ 当年度会計期間_連結_予想 """


class TitleInquiries_edif_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 役職名、問合せ先責任者 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class TitleRepresentative_edif_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 役職名、代表者 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class TokyoStockExchange_edif_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 東京証券取引所 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class TokyoStockExchangeGrowth_edif_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 東京証券取引所 グロース """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class TokyoStockExchangeOthers_edif_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 東京証券取引所 その他 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class TokyoStockExchangePrime_edif_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 東京証券取引所 プライム """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class TokyoStockExchangePROMarket_edif_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 東京証券取引所 PRO Market """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class TokyoStockExchangeStandard_edif_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 東京証券取引所 スタンダード """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class URL_edif_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ URL """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class WayOfGettingSupplementalMaterialOfResults_edif_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 入手方法等、決算補足説明資料、期中 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class ChangesInAccountingEstimatesIFRS_edif_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 会計上の見積りの変更、IFRS """

    current_accumulated_q3_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間_連結_実績")
    """ 当年度期初から第３四半期間_連結_実績 """


class ChangesInAccountingPoliciesOtherThanIFRSRequirementsIFRS_edif_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ IFRSにより要求される会計方針の変更以外の会計方針の変更、IFRS """

    current_accumulated_q3_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間_連結_実績")
    """ 当年度期初から第３四半期間_連結_実績 """


class ChangesInAccountingPoliciesRequiredByIFRSIFRS_edif_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ IFRSにより要求される会計方針の変更、IFRS """

    current_accumulated_q3_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間_連結_実績")
    """ 当年度期初から第３四半期間_連結_実績 """


class CompanyName_edif_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 上場会社名 """

    current_accumulated_q3_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点")
    """ 当年度期初から第３四半期間時点 """


class ConveningBriefingOfResults_edif_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 決算説明会開催の有無、期中 """

    current_accumulated_q3_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点")
    """ 当年度期初から第３四半期間時点 """


class CorrectionOfConsolidatedFinancialForecastInThisQuarter_edif_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 直近に公表されている業績予想からの修正の有無、連結 """

    current_year_duration_consolidated_member_forecast_member: IxNonNumericPublic = Field(default=None, description="当年度会計期間_連結_予想")
    """ 当年度会計期間_連結_予想 """


class CorrectionOfDividendForecastInThisQuarter_edif_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 直近に公表されている配当予想からの修正の有無 """

    current_year_duration_annual_member_non_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度会計期間_年間_非連結又は個別_実績")
    """ 当年度会計期間_年間_非連結又は個別_実績 """


class DividendPayableDateAsPlanned_edif_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 配当支払開始予定日 """

    current_accumulated_q3_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点")
    """ 当年度期初から第３四半期間時点 """


class DocumentName_edif_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 文書名 """

    current_accumulated_q3_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点")
    """ 当年度期初から第３四半期間時点 """


class FASFMemberMark_edif_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 財務会計基準機構会員マーク """

    current_accumulated_q3_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点")
    """ 当年度期初から第３四半期間時点 """


class FilingDate_edif_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 提出日 """

    current_accumulated_q3_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点")
    """ 当年度期初から第３四半期間時点 """


class FiscalYearEnd_edif_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 決算期 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class FukuokaStockExchange_edif_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 福岡証券取引所 """

    current_accumulated_q3_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点")
    """ 当年度期初から第３四半期間時点 """


class FukuokaStockExchangeEstablished_edif_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 福岡証券取引所 既存市場 """

    current_accumulated_q3_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点")
    """ 当年度期初から第３四半期間時点 """


class FukuokaStockExchangeOthers_edif_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 福岡証券取引所 その他 """

    current_accumulated_q3_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点")
    """ 当年度期初から第３四半期間時点 """


class FukuokaStockExchangeQBoard_edif_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 福岡証券取引所 Q-Board """

    current_accumulated_q3_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点")
    """ 当年度期初から第３四半期間時点 """


class GeneralBusiness_edif_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 一般事業会社 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class JapanSecuritiesDealersAssociation_edif_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ フェニックス """

    current_accumulated_q3_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点")
    """ 当年度期初から第３四半期間時点 """


class JapanSecuritiesDealersAssociationGreenSheet_edif_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 日本証券業協会 フェニックス """

    current_accumulated_q3_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点")
    """ 当年度期初から第３四半期間時点 """


class NagoyaStockExchange_edif_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 名古屋証券取引所 """

    current_accumulated_q3_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点")
    """ 当年度期初から第３四半期間時点 """


class NagoyaStockExchange1stSection_edif_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 名古屋証券取引所 プレミア """

    current_accumulated_q3_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点")
    """ 当年度期初から第３四半期間時点 """


class NagoyaStockExchange2ndSection_edif_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 名古屋証券取引所 メイン """

    current_accumulated_q3_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点")
    """ 当年度期初から第３四半期間時点 """


class NagoyaStockExchangeCentrex_edif_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 名古屋証券取引所 ネクスト """

    current_accumulated_q3_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点")
    """ 当年度期初から第３四半期間時点 """


class NagoyaStockExchangeOthers_edif_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 名古屋証券取引所 その他 """

    current_accumulated_q3_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点")
    """ 当年度期初から第３四半期間時点 """


class NameInquiries_edif_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 氏名、問合せ先責任者 """

    current_accumulated_q3_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点")
    """ 当年度期初から第３四半期間時点 """


class NameOfSubsidiariesExcludedFromConsolidationIFRS_edif_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 社名、除外、IFRS """

    current_accumulated_q3_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間_連結_実績")
    """ 当年度期初から第３四半期間_連結_実績 """


class NameOfSubsidiariesNewlyConsolidatedIFRS_edif_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 社名、新規、IFRS """

    current_accumulated_q3_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間_連結_実績")
    """ 当年度期初から第３四半期間_連結_実績 """


class NameRepresentative_edif_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 氏名、代表者 """

    current_accumulated_q3_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点")
    """ 当年度期初から第３四半期間時点 """


class NotesForUsingForecastedInformationAndOthers_edif_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 業績予想の適切な利用に関する説明、その他特記事項 """

    current_year_duration: IxNonNumericPublic = Field(default=None, description="当年度会計期間")
    """ 当年度会計期間 """


class NoteToChangesInAccountingPoliciesAndAccountingEstimatesIFRS_edif_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 会計方針の変更・会計上の見積りの変更に関する注記、IFRS """

    current_accumulated_q3_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間_連結_実績")
    """ 当年度期初から第３四半期間_連結_実績 """


class NoteToConsolidatedFinancialResults_edif_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 連結業績に関する注記 """

    current_accumulated_q3_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間_連結_実績")
    """ 当年度期初から第３四半期間_連結_実績 """


class NoteToDividends_edif_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 配当の状況に関する注記 """

    current_accumulated_q3_duration_annual_member_non_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間_年間_非連結又は個別_実績")
    """ 当年度期初から第３四半期間_年間_非連結又は個別_実績 """


class NoteToFinancialPositions_edif_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 財政状態に関する注記 """

    current_accumulated_q3_instant_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点_連結_実績")
    """ 当年度期初から第３四半期間時点_連結_実績 """


class NoteToForecasts_edif_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 業績予想に関する事項、注記 """

    current_year_duration_consolidated_member_forecast_member: IxNonNumericPublic = Field(default=None, description="当年度会計期間_連結_予想")
    """ 当年度会計期間_連結_予想 """


class NoteToFractionProcessingMethod_edif_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 端数処理方法に関する注記 """

    current_accumulated_q3_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点")
    """ 当年度期初から第３四半期間時点 """


class NoteToNumberOfIssuedAndOutstandingSharesCommonStock_edif_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 発行済株式数（普通株式）に関する注記 """

    current_accumulated_q3_instant_non_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点_非連結又は個別_実績")
    """ 当年度期初から第３四半期間時点_非連結又は個別_実績 """


class NoteToOperatingResults_edif_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 経営成績に関する注記 """

    current_accumulated_q3_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間_連結_実績")
    """ 当年度期初から第３四半期間_連結_実績 """


class NoteToSignificantChangesInTheScopeOfConsolidationDuringThePeriod_edif_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 期中における連結範囲の重要な変更に関する注記 """

    current_accumulated_q3_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間_連結_実績")
    """ 当年度期初から第３四半期間_連結_実績 """


class PreambleToForecasts_edif_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 業績予想に関する事項 """

    current_year_duration_consolidated_member_forecast_member: IxNonNumericPublic = Field(default=None, description="当年度会計期間_連結_予想")
    """ 当年度会計期間_連結_予想 """


class ReviewOfAttachedConsolidatedQuarterlyFinancialStatementsByACertifiedPublicAccountantOrAnAuditFirm_edif_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 添付される四半期連結財務諸表に対する公認会計士又は監査法人によるレビュー """

    current_accumulated_q3_duration: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間")
    """ 当年度期初から第３四半期間 """


class SapporoStockExchange_edif_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 札幌証券取引所 """

    current_accumulated_q3_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点")
    """ 当年度期初から第３四半期間時点 """


class SapporoStockExchangeAmbitious_edif_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 札幌証券取引所 アンビシャス """

    current_accumulated_q3_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点")
    """ 当年度期初から第３四半期間時点 """


class SapporoStockExchangeEstablished_edif_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 札幌証券取引所 既存市場 """

    current_accumulated_q3_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点")
    """ 当年度期初から第３四半期間時点 """


class SapporoStockExchangeOthers_edif_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 札幌証券取引所 その他 """

    current_accumulated_q3_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点")
    """ 当年度期初から第３四半期間時点 """


class SecuritiesCode_edif_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ コード番号 """

    current_accumulated_q3_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点")
    """ 当年度期初から第３四半期間時点 """


class SignificantChangesInTheScopeOfConsolidationDuringThePeriodIFRS_edif_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 期中における連結範囲の重要な変更、IFRS """

    current_accumulated_q3_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間_連結_実績")
    """ 当年度期初から第３四半期間_連結_実績 """


class SpecificBusiness_edif_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 特定事業会社 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class SupplementalMaterialOfResults_edif_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 決算補足説明資料作成の有無、期中 """

    current_accumulated_q3_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点")
    """ 当年度期初から第３四半期間時点 """


class TargetForBriefingOfResults_edif_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 決算説明会の対象者 """

    current_accumulated_q3_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点")
    """ 当年度期初から第３四半期間時点 """


class Tel_edif_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ TEL """

    current_accumulated_q3_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点")
    """ 当年度期初から第３四半期間時点 """


class TitleForForecasts_edif_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 業績予想タイトル名称 """

    current_year_duration_consolidated_member_forecast_member: IxNonNumericPublic = Field(default=None, description="当年度会計期間_連結_予想")
    """ 当年度会計期間_連結_予想 """


class TitleInquiries_edif_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 役職名、問合せ先責任者 """

    current_accumulated_q3_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点")
    """ 当年度期初から第３四半期間時点 """


class TitleRepresentative_edif_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 役職名、代表者 """

    current_accumulated_q3_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点")
    """ 当年度期初から第３四半期間時点 """


class TokyoStockExchange_edif_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 東京証券取引所 """

    current_accumulated_q3_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点")
    """ 当年度期初から第３四半期間時点 """


class TokyoStockExchangeGrowth_edif_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 東京証券取引所 グロース """

    current_accumulated_q3_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点")
    """ 当年度期初から第３四半期間時点 """


class TokyoStockExchangeOthers_edif_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 東京証券取引所 その他 """

    current_accumulated_q3_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点")
    """ 当年度期初から第３四半期間時点 """


class TokyoStockExchangePrime_edif_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 東京証券取引所 プライム """

    current_accumulated_q3_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点")
    """ 当年度期初から第３四半期間時点 """


class TokyoStockExchangePROMarket_edif_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 東京証券取引所 PRO Market """

    current_accumulated_q3_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点")
    """ 当年度期初から第３四半期間時点 """


class TokyoStockExchangeStandard_edif_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 東京証券取引所 スタンダード """

    current_accumulated_q3_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点")
    """ 当年度期初から第３四半期間時点 """


class URL_edif_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ URL """

    current_accumulated_q3_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点")
    """ 当年度期初から第３四半期間時点 """


class WayOfGettingSupplementalMaterialOfResults_edif_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 入手方法等、決算補足説明資料、期中 """

    current_accumulated_q3_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点")
    """ 当年度期初から第３四半期間時点 """


class DescriptionOfFactThatCompanysBusinessComprisesSingleSegmentIFRS_edif_NotesSegmentInformationCondensedQuarterlyConsolidatedFinancialStatementsIFRS_consolidated_Q2(SQLModel):
    """ 単一セグメントである旨（IFRS） """

    current_ytd_duration: IxNonNumericPublic = Field(default=None, description="当年度期初から当日まで")
    """ 当年度期初から当日まで """


class DisclosureOfChangesInReportableSegmentsIFRSTextBlock_edif_NotesSegmentInformationCondensedQuarterlyConsolidatedFinancialStatementsIFRS_consolidated_Q2(SQLModel):
    """ 報告セグメントの変更に関する事項（IFRS） [テキストブロック] """

    current_ytd_duration: IxNonNumericPublic = Field(default=None, description="当年度期初から当日まで")
    """ 当年度期初から当日まで """


class InformationAboutGeographicalAreasIFRSTextBlock_edif_NotesSegmentInformationCondensedQuarterlyConsolidatedFinancialStatementsIFRS_consolidated_Q2(SQLModel):
    """ 地域に関する情報（IFRS） [テキストブロック] """

    current_ytd_duration: IxNonNumericPublic = Field(default=None, description="当年度期初から当日まで")
    """ 当年度期初から当日まで """


class InformationAboutProductsAndServicesIFRSTextBlock_edif_NotesSegmentInformationCondensedQuarterlyConsolidatedFinancialStatementsIFRS_consolidated_Q2(SQLModel):
    """ 製品及びサービスに関する情報（IFRS） [テキストブロック] """

    current_ytd_duration: IxNonNumericPublic = Field(default=None, description="当年度期初から当日まで")
    """ 当年度期初から当日まで """


class NotesSegmentInformationCondensedQuarterlyConsolidatedFinancialStatementsIFRSTextBlock_edif_NotesSegmentInformationCondensedQuarterlyConsolidatedFinancialStatementsIFRS_consolidated_Q2(SQLModel):
    """ 注記事項－セグメント情報、要約四半期連結財務諸表（IFRS） [テキストブロック] """

    current_ytd_duration: IxNonNumericPublic = Field(default=None, description="当年度期初から当日まで")
    """ 当年度期初から当日まで """


class DisclosureOfChangesInReportableSegmentsIFRSTextBlock_edif_NotesSegmentInformationCondensedQuarterlyConsolidatedFinancialStatementsIFRS_consolidated_Q3(SQLModel):
    """ 報告セグメントの変更に関する事項（IFRS） [テキストブロック] """

    current_ytd_duration: IxNonNumericPublic = Field(default=None, description="当年度期初から当日まで")
    """ 当年度期初から当日まで """


class NotesSegmentInformationCondensedQuarterlyConsolidatedFinancialStatementsIFRSTextBlock_edif_NotesSegmentInformationCondensedQuarterlyConsolidatedFinancialStatementsIFRS_consolidated_Q3(SQLModel):
    """ 注記事項－セグメント情報、要約四半期連結財務諸表（IFRS） [テキストブロック] """

    current_ytd_duration: IxNonNumericPublic = Field(default=None, description="当年度期初から当日まで")
    """ 当年度期初から当日まで """


class BalanceSheetTextBlock_edjp_BalanceSheet_Nonconsolidated_FY(SQLModel):
    """ 貸借対照表 [テキストブロック] """

    current_year_duration: IxNonNumericPublic = Field(default=None, description="当年度会計期間")
    """ 当年度会計期間 """


class AccountingStandardsDEI_edjp_BalanceSheet_Nonconsolidated_FY(SQLModel):
    """ 会計基準、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class AmendmentFlagDEI_edjp_BalanceSheet_Nonconsolidated_FY(SQLModel):
    """ 訂正の有無、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class CabinetOfficeOrdinanceDEI_edjp_BalanceSheet_Nonconsolidated_FY(SQLModel):
    """ 府令、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class ComparativePeriodEndDateDEI_edjp_BalanceSheet_Nonconsolidated_FY(SQLModel):
    """ 比較対象会計期間終了日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class CurrentFiscalYearEndDateDEI_edjp_BalanceSheet_Nonconsolidated_FY(SQLModel):
    """ 当事業年度終了日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class CurrentFiscalYearStartDateDEI_edjp_BalanceSheet_Nonconsolidated_FY(SQLModel):
    """ 当事業年度開始日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class CurrentPeriodEndDateDEI_edjp_BalanceSheet_Nonconsolidated_FY(SQLModel):
    """ 当会計期間終了日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class DocumentTypeDEI_edjp_BalanceSheet_Nonconsolidated_FY(SQLModel):
    """ 様式、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class EDINETCodeDEI_edjp_BalanceSheet_Nonconsolidated_FY(SQLModel):
    """ EDINETコード、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class EndDateOfQuarterlyOrSemiAnnualPeriodOfNextFiscalYearDEI_edjp_BalanceSheet_Nonconsolidated_FY(SQLModel):
    """ 次の四半期又は中間期の会計期間終了日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class FilerNameInEnglishDEI_edjp_BalanceSheet_Nonconsolidated_FY(SQLModel):
    """ 提出者名（英語表記）、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class FilerNameInJapaneseDEI_edjp_BalanceSheet_Nonconsolidated_FY(SQLModel):
    """ 提出者名（日本語表記）、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class FundCodeDEI_edjp_BalanceSheet_Nonconsolidated_FY(SQLModel):
    """ ファンドコード、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class FundNameInEnglishDEI_edjp_BalanceSheet_Nonconsolidated_FY(SQLModel):
    """ ファンド名称（英語表記）、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class FundNameInJapaneseDEI_edjp_BalanceSheet_Nonconsolidated_FY(SQLModel):
    """ ファンド名称（日本語表記）、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class IdentificationOfDocumentSubjectToAmendmentDEI_edjp_BalanceSheet_Nonconsolidated_FY(SQLModel):
    """ 訂正対象書類の書類管理番号、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class IndustryCodeWhenConsolidatedFinancialStatementsArePreparedInAccordanceWithIndustrySpecificRegulationsDEI_edjp_BalanceSheet_Nonconsolidated_FY(SQLModel):
    """ 別記事業（連結）、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class IndustryCodeWhenFinancialStatementsArePreparedInAccordanceWithIndustrySpecificRegulationsDEI_edjp_BalanceSheet_Nonconsolidated_FY(SQLModel):
    """ 別記事業（個別）、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class NextFiscalYearStartDateDEI_edjp_BalanceSheet_Nonconsolidated_FY(SQLModel):
    """ 次の事業年度開始日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class PreviousFiscalYearEndDateDEI_edjp_BalanceSheet_Nonconsolidated_FY(SQLModel):
    """ 前事業年度終了日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class PreviousFiscalYearStartDateDEI_edjp_BalanceSheet_Nonconsolidated_FY(SQLModel):
    """ 前事業年度開始日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class ReportAmendmentFlagDEI_edjp_BalanceSheet_Nonconsolidated_FY(SQLModel):
    """ 記載事項訂正のフラグ、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class SecurityCodeDEI_edjp_BalanceSheet_Nonconsolidated_FY(SQLModel):
    """ 証券コード、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class TypeOfCurrentPeriodDEI_edjp_BalanceSheet_Nonconsolidated_FY(SQLModel):
    """ 当会計期間の種類、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class WhetherConsolidatedFinancialStatementsArePreparedDEI_edjp_BalanceSheet_Nonconsolidated_FY(SQLModel):
    """ 連結決算の有無、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class XBRLAmendmentFlagDEI_edjp_BalanceSheet_Nonconsolidated_FY(SQLModel):
    """ XBRL訂正のフラグ、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class BalanceSheetTextBlock_edjp_BalanceSheet_consolidated_FY(SQLModel):
    """ 貸借対照表 [テキストブロック] """

    current_year_duration: IxNonNumericPublic = Field(default=None, description="当年度会計期間")
    """ 当年度会計期間 """


class ConsolidatedBalanceSheetTextBlock_edjp_ConsolidatedBalanceSheet_consolidated_FY(SQLModel):
    """ 連結貸借対照表 [テキストブロック] """

    current_year_duration: IxNonNumericPublic = Field(default=None, description="当年度会計期間")
    """ 当年度会計期間 """


class AccountingStandardsDEI_edjp_ConsolidatedBalanceSheet_consolidated_FY(SQLModel):
    """ 会計基準、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class AmendmentFlagDEI_edjp_ConsolidatedBalanceSheet_consolidated_FY(SQLModel):
    """ 訂正の有無、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class CabinetOfficeOrdinanceDEI_edjp_ConsolidatedBalanceSheet_consolidated_FY(SQLModel):
    """ 府令、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class ComparativePeriodEndDateDEI_edjp_ConsolidatedBalanceSheet_consolidated_FY(SQLModel):
    """ 比較対象会計期間終了日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class CurrentFiscalYearEndDateDEI_edjp_ConsolidatedBalanceSheet_consolidated_FY(SQLModel):
    """ 当事業年度終了日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class CurrentFiscalYearStartDateDEI_edjp_ConsolidatedBalanceSheet_consolidated_FY(SQLModel):
    """ 当事業年度開始日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class CurrentPeriodEndDateDEI_edjp_ConsolidatedBalanceSheet_consolidated_FY(SQLModel):
    """ 当会計期間終了日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class DocumentTypeDEI_edjp_ConsolidatedBalanceSheet_consolidated_FY(SQLModel):
    """ 様式、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class EDINETCodeDEI_edjp_ConsolidatedBalanceSheet_consolidated_FY(SQLModel):
    """ EDINETコード、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class EndDateOfQuarterlyOrSemiAnnualPeriodOfNextFiscalYearDEI_edjp_ConsolidatedBalanceSheet_consolidated_FY(SQLModel):
    """ 次の四半期又は中間期の会計期間終了日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class FilerNameInEnglishDEI_edjp_ConsolidatedBalanceSheet_consolidated_FY(SQLModel):
    """ 提出者名（英語表記）、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class FilerNameInJapaneseDEI_edjp_ConsolidatedBalanceSheet_consolidated_FY(SQLModel):
    """ 提出者名（日本語表記）、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class FundCodeDEI_edjp_ConsolidatedBalanceSheet_consolidated_FY(SQLModel):
    """ ファンドコード、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class FundNameInEnglishDEI_edjp_ConsolidatedBalanceSheet_consolidated_FY(SQLModel):
    """ ファンド名称（英語表記）、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class FundNameInJapaneseDEI_edjp_ConsolidatedBalanceSheet_consolidated_FY(SQLModel):
    """ ファンド名称（日本語表記）、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class IdentificationOfDocumentSubjectToAmendmentDEI_edjp_ConsolidatedBalanceSheet_consolidated_FY(SQLModel):
    """ 訂正対象書類の書類管理番号、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class IndustryCodeWhenConsolidatedFinancialStatementsArePreparedInAccordanceWithIndustrySpecificRegulationsDEI_edjp_ConsolidatedBalanceSheet_consolidated_FY(SQLModel):
    """ 別記事業（連結）、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class IndustryCodeWhenFinancialStatementsArePreparedInAccordanceWithIndustrySpecificRegulationsDEI_edjp_ConsolidatedBalanceSheet_consolidated_FY(SQLModel):
    """ 別記事業（個別）、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class NextFiscalYearStartDateDEI_edjp_ConsolidatedBalanceSheet_consolidated_FY(SQLModel):
    """ 次の事業年度開始日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class PreviousFiscalYearEndDateDEI_edjp_ConsolidatedBalanceSheet_consolidated_FY(SQLModel):
    """ 前事業年度終了日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class PreviousFiscalYearStartDateDEI_edjp_ConsolidatedBalanceSheet_consolidated_FY(SQLModel):
    """ 前事業年度開始日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class ReportAmendmentFlagDEI_edjp_ConsolidatedBalanceSheet_consolidated_FY(SQLModel):
    """ 記載事項訂正のフラグ、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class SecurityCodeDEI_edjp_ConsolidatedBalanceSheet_consolidated_FY(SQLModel):
    """ 証券コード、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class TypeOfCurrentPeriodDEI_edjp_ConsolidatedBalanceSheet_consolidated_FY(SQLModel):
    """ 当会計期間の種類、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class WhetherConsolidatedFinancialStatementsArePreparedDEI_edjp_ConsolidatedBalanceSheet_consolidated_FY(SQLModel):
    """ 連結決算の有無、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class XBRLAmendmentFlagDEI_edjp_ConsolidatedBalanceSheet_consolidated_FY(SQLModel):
    """ XBRL訂正のフラグ、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class ConsolidatedStatementOfCashFlowsTextBlock_edjp_ConsolidatedStatementOfCashFlows_consolidated_FY(SQLModel):
    """ 連結キャッシュ・フロー計算書 [テキストブロック] """

    current_year_duration: IxNonNumericPublic = Field(default=None, description="当年度会計期間")
    """ 当年度会計期間 """


class ConsolidatedStatementOfChangesInEquityTextBlock_edjp_ConsolidatedStatementOfChangesInEquity_consolidated_FY(SQLModel):
    """ 連結株主資本等変動計算書 [テキストブロック] """

    current_year_duration: IxNonNumericPublic = Field(default=None, description="当年度会計期間")
    """ 当年度会計期間 """


class ConsolidatedStatementOfComprehensiveIncomeTextBlock_edjp_ConsolidatedStatementOfComprehensiveIncome_consolidated_FY(SQLModel):
    """ 連結包括利益計算書 [テキストブロック] """

    current_year_duration: IxNonNumericPublic = Field(default=None, description="当年度会計期間")
    """ 当年度会計期間 """


class ConsolidatedStatementOfIncomeTextBlock_edjp_ConsolidatedStatementOfIncome_consolidated_FY(SQLModel):
    """ 連結損益計算書 [テキストブロック] """

    current_year_duration: IxNonNumericPublic = Field(default=None, description="当年度会計期間")
    """ 当年度会計期間 """


class AnnualSecuritiesReportFilingDateAsPlanned_edjp_FinancialReportSummary_Nonconsolidated_FY(SQLModel):
    """ 有価証券報告書提出予定日 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class ChangesBasedOnRevisionsOfAccountingStandard_edjp_FinancialReportSummary_Nonconsolidated_FY(SQLModel):
    """ 会計基準等の改正に伴う会計方針の変更 """

    current_year_duration_non_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度会計期間_非連結又は個別_実績")
    """ 当年度会計期間_非連結又は個別_実績 """


class ChangesInAccountingEstimates_edjp_FinancialReportSummary_Nonconsolidated_FY(SQLModel):
    """ 会計上の見積りの変更 """

    current_year_duration_non_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度会計期間_非連結又は個別_実績")
    """ 当年度会計期間_非連結又は個別_実績 """


class ChangesOtherThanOnesBasedOnRevisionsOfAccountingStandard_edjp_FinancialReportSummary_Nonconsolidated_FY(SQLModel):
    """ 会計基準等の改正に伴う変更以外の会計方針の変更 """

    current_year_duration_non_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度会計期間_非連結又は個別_実績")
    """ 当年度会計期間_非連結又は個別_実績 """


class CompanyName_edjp_FinancialReportSummary_Nonconsolidated_FY(SQLModel):
    """ 上場会社名 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class ConveningBriefingOfAnnualResults_edjp_FinancialReportSummary_Nonconsolidated_FY(SQLModel):
    """ 決算説明会開催の有無 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class DateOfGeneralShareholdersMeetingAsPlanned_edjp_FinancialReportSummary_Nonconsolidated_FY(SQLModel):
    """ 定時株主総会開催予定日 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class DividendPayableDateAsPlanned_edjp_FinancialReportSummary_Nonconsolidated_FY(SQLModel):
    """ 配当支払開始予定日 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class DocumentName_edjp_FinancialReportSummary_Nonconsolidated_FY(SQLModel):
    """ 文書名 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class FASFMemberMark_edjp_FinancialReportSummary_Nonconsolidated_FY(SQLModel):
    """ 財務会計基準機構会員マーク """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class FilingDate_edjp_FinancialReportSummary_Nonconsolidated_FY(SQLModel):
    """ 提出日 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class FiscalYearEnd_edjp_FinancialReportSummary_Nonconsolidated_FY(SQLModel):
    """ 決算期 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class FukuokaStockExchange_edjp_FinancialReportSummary_Nonconsolidated_FY(SQLModel):
    """ 福岡証券取引所 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class FukuokaStockExchangeEstablished_edjp_FinancialReportSummary_Nonconsolidated_FY(SQLModel):
    """ 福岡証券取引所 既存市場 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class FukuokaStockExchangeOthers_edjp_FinancialReportSummary_Nonconsolidated_FY(SQLModel):
    """ 福岡証券取引所 その他 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class FukuokaStockExchangeQBoard_edjp_FinancialReportSummary_Nonconsolidated_FY(SQLModel):
    """ 福岡証券取引所 Q-Board """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class GeneralBusiness_edjp_FinancialReportSummary_Nonconsolidated_FY(SQLModel):
    """ 一般事業会社 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class JapanSecuritiesDealersAssociation_edjp_FinancialReportSummary_Nonconsolidated_FY(SQLModel):
    """ フェニックス """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class JapanSecuritiesDealersAssociationGreenSheet_edjp_FinancialReportSummary_Nonconsolidated_FY(SQLModel):
    """ 日本証券業協会 フェニックス """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class NagoyaStockExchange_edjp_FinancialReportSummary_Nonconsolidated_FY(SQLModel):
    """ 名古屋証券取引所 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class NagoyaStockExchange1stSection_edjp_FinancialReportSummary_Nonconsolidated_FY(SQLModel):
    """ 名古屋証券取引所 プレミア """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class NagoyaStockExchange2ndSection_edjp_FinancialReportSummary_Nonconsolidated_FY(SQLModel):
    """ 名古屋証券取引所 メイン """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class NagoyaStockExchangeCentrex_edjp_FinancialReportSummary_Nonconsolidated_FY(SQLModel):
    """ 名古屋証券取引所 ネクスト """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class NagoyaStockExchangeOthers_edjp_FinancialReportSummary_Nonconsolidated_FY(SQLModel):
    """ 名古屋証券取引所 その他 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class NameInquiries_edjp_FinancialReportSummary_Nonconsolidated_FY(SQLModel):
    """ 氏名、問合せ先責任者 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class NameRepresentative_edjp_FinancialReportSummary_Nonconsolidated_FY(SQLModel):
    """ 氏名、代表者 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class NotesForUsingForecastedInformationAndOthers_edjp_FinancialReportSummary_Nonconsolidated_FY(SQLModel):
    """ 業績予想の適切な利用に関する説明、その他特記事項 """

    next_year_duration: IxNonNumericPublic = Field(default=None, description="次年度会計期間")
    """ 次年度会計期間 """


class NoteToChangesInAccountingPoliciesAndAccountingEstimatesRetrospectiveRestatement_edjp_FinancialReportSummary_Nonconsolidated_FY(SQLModel):
    """ 会計方針の変更・会計上の見積りの変更・修正再表示に関する注記 """

    current_year_duration_non_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度会計期間_非連結又は個別_実績")
    """ 当年度会計期間_非連結又は個別_実績 """


class NoteToFinancialPositions_edjp_FinancialReportSummary_Nonconsolidated_FY(SQLModel):
    """ 財政状態に関する注記 """

    current_year_instant_non_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度時点_非連結又は個別_実績")
    """ 当年度時点_非連結又は個別_実績 """


class NoteToForecasts_edjp_FinancialReportSummary_Nonconsolidated_FY(SQLModel):
    """ 業績予想に関する事項、注記 """

    next_year_duration_non_consolidated_member_forecast_member: IxNonNumericPublic = Field(default=None, description="次年度会計期間_非連結又は個別_予想")
    """ 次年度会計期間_非連結又は個別_予想 """


class NoteToFractionProcessingMethod_edjp_FinancialReportSummary_Nonconsolidated_FY(SQLModel):
    """ 端数処理方法に関する注記 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class NoteToNumberOfIssuedAndOutstandingSharesCommonStock_edjp_FinancialReportSummary_Nonconsolidated_FY(SQLModel):
    """ 発行済株式数（普通株式）に関する注記 """

    current_year_instant_non_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度時点_非連結又は個別_実績")
    """ 当年度時点_非連結又は個別_実績 """


class NoteToOperatingResults_edjp_FinancialReportSummary_Nonconsolidated_FY(SQLModel):
    """ 経営成績に関する注記 """

    current_year_duration_non_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度会計期間_非連結又は個別_実績")
    """ 当年度会計期間_非連結又は個別_実績 """


class PreambleToForecasts_edjp_FinancialReportSummary_Nonconsolidated_FY(SQLModel):
    """ 業績予想に関する事項 """

    next_year_duration_non_consolidated_member_forecast_member: IxNonNumericPublic = Field(default=None, description="次年度会計期間_非連結又は個別_予想")
    """ 次年度会計期間_非連結又は個別_予想 """


class RetrospectiveRestatement_edjp_FinancialReportSummary_Nonconsolidated_FY(SQLModel):
    """ 修正再表示 """

    current_year_duration_non_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度会計期間_非連結又は個別_実績")
    """ 当年度会計期間_非連結又は個別_実績 """


class SapporoStockExchange_edjp_FinancialReportSummary_Nonconsolidated_FY(SQLModel):
    """ 札幌証券取引所 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class SapporoStockExchangeAmbitious_edjp_FinancialReportSummary_Nonconsolidated_FY(SQLModel):
    """ 札幌証券取引所 アンビシャス """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class SapporoStockExchangeEstablished_edjp_FinancialReportSummary_Nonconsolidated_FY(SQLModel):
    """ 札幌証券取引所 既存市場 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class SapporoStockExchangeOthers_edjp_FinancialReportSummary_Nonconsolidated_FY(SQLModel):
    """ 札幌証券取引所 その他 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class SecuritiesCode_edjp_FinancialReportSummary_Nonconsolidated_FY(SQLModel):
    """ コード番号 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class SpecificBusiness_edjp_FinancialReportSummary_Nonconsolidated_FY(SQLModel):
    """ 特定事業会社 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class SupplementalMaterialOfAnnualResults_edjp_FinancialReportSummary_Nonconsolidated_FY(SQLModel):
    """ 決算補足説明資料作成の有無 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class TargetAudienceBriefingOfAnnualResults_edjp_FinancialReportSummary_Nonconsolidated_FY(SQLModel):
    """ 対象者、決算説明会 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class Tel_edjp_FinancialReportSummary_Nonconsolidated_FY(SQLModel):
    """ TEL """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class TitleForForecasts_edjp_FinancialReportSummary_Nonconsolidated_FY(SQLModel):
    """ 業績予想タイトル名称 """

    next_year_duration_non_consolidated_member_forecast_member: IxNonNumericPublic = Field(default=None, description="次年度会計期間_非連結又は個別_予想")
    """ 次年度会計期間_非連結又は個別_予想 """


class TitleInquiries_edjp_FinancialReportSummary_Nonconsolidated_FY(SQLModel):
    """ 役職名、問合せ先責任者 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class TitleRepresentative_edjp_FinancialReportSummary_Nonconsolidated_FY(SQLModel):
    """ 役職名、代表者 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class TokyoStockExchange_edjp_FinancialReportSummary_Nonconsolidated_FY(SQLModel):
    """ 東京証券取引所 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class TokyoStockExchange1stSection_edjp_FinancialReportSummary_Nonconsolidated_FY(SQLModel):
    """ 東京証券取引所 第一部 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class TokyoStockExchange2ndSection_edjp_FinancialReportSummary_Nonconsolidated_FY(SQLModel):
    """ 東京証券取引所 第二部 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class TokyoStockExchangeGrowth_edjp_FinancialReportSummary_Nonconsolidated_FY(SQLModel):
    """ 東京証券取引所 グロース """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class TokyoStockExchangeJASDAQ_edjp_FinancialReportSummary_Nonconsolidated_FY(SQLModel):
    """ 東京証券取引所 JASDAQ """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class TokyoStockExchangeMothers_edjp_FinancialReportSummary_Nonconsolidated_FY(SQLModel):
    """ 東京証券取引所 マザーズ """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class TokyoStockExchangeOthers_edjp_FinancialReportSummary_Nonconsolidated_FY(SQLModel):
    """ 東京証券取引所 その他 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class TokyoStockExchangePrime_edjp_FinancialReportSummary_Nonconsolidated_FY(SQLModel):
    """ 東京証券取引所 プライム """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class TokyoStockExchangePROMarket_edjp_FinancialReportSummary_Nonconsolidated_FY(SQLModel):
    """ 東京証券取引所 PRO Market """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class TokyoStockExchangeStandard_edjp_FinancialReportSummary_Nonconsolidated_FY(SQLModel):
    """ 東京証券取引所 スタンダード """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class URL_edjp_FinancialReportSummary_Nonconsolidated_FY(SQLModel):
    """ URL """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class WayOfGettingSupplementalMaterialOfAnnualResults_edjp_FinancialReportSummary_Nonconsolidated_FY(SQLModel):
    """ 入手方法等、決算補足説明資料 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class AnnualSecuritiesReportFilingDateAsPlanned_edjp_FinancialReportSummary_consolidated_FY(SQLModel):
    """ 有価証券報告書提出予定日 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class ChangesBasedOnRevisionsOfAccountingStandard_edjp_FinancialReportSummary_consolidated_FY(SQLModel):
    """ 会計基準等の改正に伴う会計方針の変更 """

    current_year_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度会計期間_連結_実績")
    """ 当年度会計期間_連結_実績 """


class ChangesInAccountingEstimates_edjp_FinancialReportSummary_consolidated_FY(SQLModel):
    """ 会計上の見積りの変更 """

    current_year_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度会計期間_連結_実績")
    """ 当年度会計期間_連結_実績 """


class ChangesOtherThanOnesBasedOnRevisionsOfAccountingStandard_edjp_FinancialReportSummary_consolidated_FY(SQLModel):
    """ 会計基準等の改正に伴う変更以外の会計方針の変更 """

    current_year_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度会計期間_連結_実績")
    """ 当年度会計期間_連結_実績 """


class CompanyName_edjp_FinancialReportSummary_consolidated_FY(SQLModel):
    """ 上場会社名 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class ConveningBriefingOfAnnualResults_edjp_FinancialReportSummary_consolidated_FY(SQLModel):
    """ 決算説明会開催の有無 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class DateOfGeneralShareholdersMeetingAsPlanned_edjp_FinancialReportSummary_consolidated_FY(SQLModel):
    """ 定時株主総会開催予定日 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class DividendPayableDateAsPlanned_edjp_FinancialReportSummary_consolidated_FY(SQLModel):
    """ 配当支払開始予定日 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class DocumentName_edjp_FinancialReportSummary_consolidated_FY(SQLModel):
    """ 文書名 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class FASFMemberMark_edjp_FinancialReportSummary_consolidated_FY(SQLModel):
    """ 財務会計基準機構会員マーク """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class FilingDate_edjp_FinancialReportSummary_consolidated_FY(SQLModel):
    """ 提出日 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class FiscalYearEnd_edjp_FinancialReportSummary_consolidated_FY(SQLModel):
    """ 決算期 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class FukuokaStockExchange_edjp_FinancialReportSummary_consolidated_FY(SQLModel):
    """ 福岡証券取引所 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class FukuokaStockExchangeEstablished_edjp_FinancialReportSummary_consolidated_FY(SQLModel):
    """ 福岡証券取引所 既存市場 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class FukuokaStockExchangeOthers_edjp_FinancialReportSummary_consolidated_FY(SQLModel):
    """ 福岡証券取引所 その他 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class FukuokaStockExchangeQBoard_edjp_FinancialReportSummary_consolidated_FY(SQLModel):
    """ 福岡証券取引所 Q-Board """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class GeneralBusiness_edjp_FinancialReportSummary_consolidated_FY(SQLModel):
    """ 一般事業会社 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class JapanSecuritiesDealersAssociation_edjp_FinancialReportSummary_consolidated_FY(SQLModel):
    """ フェニックス """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class JapanSecuritiesDealersAssociationGreenSheet_edjp_FinancialReportSummary_consolidated_FY(SQLModel):
    """ 日本証券業協会 フェニックス """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class NagoyaStockExchange_edjp_FinancialReportSummary_consolidated_FY(SQLModel):
    """ 名古屋証券取引所 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class NagoyaStockExchange1stSection_edjp_FinancialReportSummary_consolidated_FY(SQLModel):
    """ 名古屋証券取引所 プレミア """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class NagoyaStockExchange2ndSection_edjp_FinancialReportSummary_consolidated_FY(SQLModel):
    """ 名古屋証券取引所 メイン """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class NagoyaStockExchangeCentrex_edjp_FinancialReportSummary_consolidated_FY(SQLModel):
    """ 名古屋証券取引所 ネクスト """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class NagoyaStockExchangeOthers_edjp_FinancialReportSummary_consolidated_FY(SQLModel):
    """ 名古屋証券取引所 その他 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class NameInquiries_edjp_FinancialReportSummary_consolidated_FY(SQLModel):
    """ 氏名、問合せ先責任者 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class NameOfSubsidiariesExcludedFromConsolidation_edjp_FinancialReportSummary_consolidated_FY(SQLModel):
    """ 社名、除外 """

    current_year_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度会計期間_連結_実績")
    """ 当年度会計期間_連結_実績 """


class NameOfSubsidiariesNewlyConsolidated_edjp_FinancialReportSummary_consolidated_FY(SQLModel):
    """ 社名、新規 """

    current_year_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度会計期間_連結_実績")
    """ 当年度会計期間_連結_実績 """


class NameRepresentative_edjp_FinancialReportSummary_consolidated_FY(SQLModel):
    """ 氏名、代表者 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class NotesForUsingForecastedInformationAndOthers_edjp_FinancialReportSummary_consolidated_FY(SQLModel):
    """ 業績予想の適切な利用に関する説明、その他特記事項 """

    next_year_duration: IxNonNumericPublic = Field(default=None, description="次年度会計期間")
    """ 次年度会計期間 """


class NoteToCashFlows_edjp_FinancialReportSummary_consolidated_FY(SQLModel):
    """ キャッシュ・フローの状況に関する注記 """

    current_year_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度会計期間_連結_実績")
    """ 当年度会計期間_連結_実績 """


class NoteToChangesInAccountingPoliciesAndAccountingEstimatesRetrospectiveRestatement_edjp_FinancialReportSummary_consolidated_FY(SQLModel):
    """ 会計方針の変更・会計上の見積りの変更・修正再表示に関する注記 """

    current_year_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度会計期間_連結_実績")
    """ 当年度会計期間_連結_実績 """


class NoteToConsolidatedFinancialResults_edjp_FinancialReportSummary_consolidated_FY(SQLModel):
    """ 連結業績に関する注記 """

    current_year_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度会計期間_連結_実績")
    """ 当年度会計期間_連結_実績 """


class NoteToDividends_edjp_FinancialReportSummary_consolidated_FY(SQLModel):
    """ 配当の状況に関する注記 """

    current_year_duration_annual_member_non_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度会計期間_年間_非連結又は個別_実績")
    """ 当年度会計期間_年間_非連結又は個別_実績 """


class NoteToFinancialPositions_edjp_FinancialReportSummary_consolidated_FY(SQLModel):
    """ 財政状態に関する注記 """

    current_year_instant_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度時点_連結_実績")
    """ 当年度時点_連結_実績 """
    current_year_instant_non_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度時点_非連結又は個別_実績")
    """ 当年度時点_非連結又は個別_実績 """


class NoteToFinancialResults_edjp_FinancialReportSummary_consolidated_FY(SQLModel):
    """ 業績に関する注記 """

    current_year_duration_non_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度会計期間_非連結又は個別_実績")
    """ 当年度会計期間_非連結又は個別_実績 """


class NoteToForecasts_edjp_FinancialReportSummary_consolidated_FY(SQLModel):
    """ 業績予想に関する事項、注記 """

    next_year_duration_consolidated_member_forecast_member: IxNonNumericPublic = Field(default=None, description="次年度会計期間_連結_予想")
    """ 次年度会計期間_連結_予想 """
    next_year_duration_non_consolidated_member_forecast_member: IxNonNumericPublic = Field(default=None, description="次年度会計期間_非連結又は個別_予想")
    """ 次年度会計期間_非連結又は個別_予想 """


class NoteToFractionProcessingMethod_edjp_FinancialReportSummary_consolidated_FY(SQLModel):
    """ 端数処理方法に関する注記 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class NoteToNumberOfIssuedAndOutstandingSharesCommonStock_edjp_FinancialReportSummary_consolidated_FY(SQLModel):
    """ 発行済株式数（普通株式）に関する注記 """

    current_year_instant_non_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度時点_非連結又は個別_実績")
    """ 当年度時点_非連結又は個別_実績 """


class NoteToOperatingResults_edjp_FinancialReportSummary_consolidated_FY(SQLModel):
    """ 経営成績に関する注記 """

    current_year_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度会計期間_連結_実績")
    """ 当年度会計期間_連結_実績 """
    current_year_duration_non_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度会計期間_非連結又は個別_実績")
    """ 当年度会計期間_非連結又は個別_実績 """


class NoteToSignificantChangesInTheScopeOfConsolidationDuringThePeriod_edjp_FinancialReportSummary_consolidated_FY(SQLModel):
    """ 期中における連結範囲の重要な変更に関する注記 """

    current_year_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度会計期間_連結_実績")
    """ 当年度会計期間_連結_実績 """


class PreambleToForecasts_edjp_FinancialReportSummary_consolidated_FY(SQLModel):
    """ 業績予想に関する事項 """

    next_year_duration_consolidated_member_forecast_member: IxNonNumericPublic = Field(default=None, description="次年度会計期間_連結_予想")
    """ 次年度会計期間_連結_予想 """
    next_year_duration_non_consolidated_member_forecast_member: IxNonNumericPublic = Field(default=None, description="次年度会計期間_非連結又は個別_予想")
    """ 次年度会計期間_非連結又は個別_予想 """


class RetrospectiveRestatement_edjp_FinancialReportSummary_consolidated_FY(SQLModel):
    """ 修正再表示 """

    current_year_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度会計期間_連結_実績")
    """ 当年度会計期間_連結_実績 """


class SapporoStockExchange_edjp_FinancialReportSummary_consolidated_FY(SQLModel):
    """ 札幌証券取引所 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class SapporoStockExchangeAmbitious_edjp_FinancialReportSummary_consolidated_FY(SQLModel):
    """ 札幌証券取引所 アンビシャス """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class SapporoStockExchangeEstablished_edjp_FinancialReportSummary_consolidated_FY(SQLModel):
    """ 札幌証券取引所 既存市場 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class SapporoStockExchangeOthers_edjp_FinancialReportSummary_consolidated_FY(SQLModel):
    """ 札幌証券取引所 その他 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class SecuritiesCode_edjp_FinancialReportSummary_consolidated_FY(SQLModel):
    """ コード番号 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class SignificantChangesInTheScopeOfConsolidationDuringThePeriod_edjp_FinancialReportSummary_consolidated_FY(SQLModel):
    """ 期中における連結範囲の重要な変更 """

    current_year_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度会計期間_連結_実績")
    """ 当年度会計期間_連結_実績 """


class SpecificBusiness_edjp_FinancialReportSummary_consolidated_FY(SQLModel):
    """ 特定事業会社 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class SupplementalMaterialOfAnnualResults_edjp_FinancialReportSummary_consolidated_FY(SQLModel):
    """ 決算補足説明資料作成の有無 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class TargetAudienceBriefingOfAnnualResults_edjp_FinancialReportSummary_consolidated_FY(SQLModel):
    """ 対象者、決算説明会 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class Tel_edjp_FinancialReportSummary_consolidated_FY(SQLModel):
    """ TEL """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class TitleForForecasts_edjp_FinancialReportSummary_consolidated_FY(SQLModel):
    """ 業績予想タイトル名称 """

    next_year_duration_consolidated_member_forecast_member: IxNonNumericPublic = Field(default=None, description="次年度会計期間_連結_予想")
    """ 次年度会計期間_連結_予想 """


class TitleInquiries_edjp_FinancialReportSummary_consolidated_FY(SQLModel):
    """ 役職名、問合せ先責任者 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class TitleRepresentative_edjp_FinancialReportSummary_consolidated_FY(SQLModel):
    """ 役職名、代表者 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class TokyoStockExchange_edjp_FinancialReportSummary_consolidated_FY(SQLModel):
    """ 東京証券取引所 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class TokyoStockExchange1stSection_edjp_FinancialReportSummary_consolidated_FY(SQLModel):
    """ 東京証券取引所 第一部 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class TokyoStockExchange2ndSection_edjp_FinancialReportSummary_consolidated_FY(SQLModel):
    """ 東京証券取引所 第二部 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class TokyoStockExchangeGrowth_edjp_FinancialReportSummary_consolidated_FY(SQLModel):
    """ 東京証券取引所 グロース """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class TokyoStockExchangeJASDAQ_edjp_FinancialReportSummary_consolidated_FY(SQLModel):
    """ 東京証券取引所 JASDAQ """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class TokyoStockExchangeMothers_edjp_FinancialReportSummary_consolidated_FY(SQLModel):
    """ 東京証券取引所 マザーズ """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class TokyoStockExchangeOthers_edjp_FinancialReportSummary_consolidated_FY(SQLModel):
    """ 東京証券取引所 その他 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class TokyoStockExchangePrime_edjp_FinancialReportSummary_consolidated_FY(SQLModel):
    """ 東京証券取引所 プライム """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class TokyoStockExchangePROMarket_edjp_FinancialReportSummary_consolidated_FY(SQLModel):
    """ 東京証券取引所 PRO Market """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class TokyoStockExchangeStandard_edjp_FinancialReportSummary_consolidated_FY(SQLModel):
    """ 東京証券取引所 スタンダード """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class URL_edjp_FinancialReportSummary_consolidated_FY(SQLModel):
    """ URL """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class WayOfGettingSupplementalMaterialOfAnnualResults_edjp_FinancialReportSummary_consolidated_FY(SQLModel):
    """ 入手方法等、決算補足説明資料 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class ApplyingOfSpecificAccountingOfTheConsolidatedQuarterlyFinancialStatements_edjp_FinancialReportSummary_consolidated_Q1(SQLModel):
    """ 四半期連結財務諸表の作成に特有の会計処理の適用 """

    current_accumulated_q1_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間_連結_実績")
    """ 当年度期初から第１四半期間_連結_実績 """


class ChangesBasedOnRevisionsOfAccountingStandard_edjp_FinancialReportSummary_consolidated_Q1(SQLModel):
    """ 会計基準等の改正に伴う会計方針の変更 """

    current_accumulated_q1_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間_連結_実績")
    """ 当年度期初から第１四半期間_連結_実績 """


class ChangesInAccountingEstimates_edjp_FinancialReportSummary_consolidated_Q1(SQLModel):
    """ 会計上の見積りの変更 """

    current_accumulated_q1_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間_連結_実績")
    """ 当年度期初から第１四半期間_連結_実績 """


class ChangesOtherThanOnesBasedOnRevisionsOfAccountingStandard_edjp_FinancialReportSummary_consolidated_Q1(SQLModel):
    """ 会計基準等の改正に伴う変更以外の会計方針の変更 """

    current_accumulated_q1_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間_連結_実績")
    """ 当年度期初から第１四半期間_連結_実績 """


class CompanyName_edjp_FinancialReportSummary_consolidated_Q1(SQLModel):
    """ 上場会社名 """

    current_accumulated_q1_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間時点")
    """ 当年度期初から第１四半期間時点 """


class ConveningBriefingOfResults_edjp_FinancialReportSummary_consolidated_Q1(SQLModel):
    """ 決算説明会開催の有無、期中 """

    current_accumulated_q1_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間時点")
    """ 当年度期初から第１四半期間時点 """


class CorrectionOfConsolidatedFinancialForecastInThisQuarter_edjp_FinancialReportSummary_consolidated_Q1(SQLModel):
    """ 直近に公表されている業績予想からの修正の有無、連結 """

    current_year_duration_consolidated_member_forecast_member: IxNonNumericPublic = Field(default=None, description="当年度会計期間_連結_予想")
    """ 当年度会計期間_連結_予想 """


class CorrectionOfDividendForecastInThisQuarter_edjp_FinancialReportSummary_consolidated_Q1(SQLModel):
    """ 直近に公表されている配当予想からの修正の有無 """

    current_year_duration_annual_member_non_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度会計期間_年間_非連結又は個別_実績")
    """ 当年度会計期間_年間_非連結又は個別_実績 """


class DividendPayableDateAsPlanned_edjp_FinancialReportSummary_consolidated_Q1(SQLModel):
    """ 配当支払開始予定日 """

    current_accumulated_q1_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間時点")
    """ 当年度期初から第１四半期間時点 """


class DocumentName_edjp_FinancialReportSummary_consolidated_Q1(SQLModel):
    """ 文書名 """

    current_accumulated_q1_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間時点")
    """ 当年度期初から第１四半期間時点 """


class FASFMemberMark_edjp_FinancialReportSummary_consolidated_Q1(SQLModel):
    """ 財務会計基準機構会員マーク """

    current_accumulated_q1_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間時点")
    """ 当年度期初から第１四半期間時点 """


class FilingDate_edjp_FinancialReportSummary_consolidated_Q1(SQLModel):
    """ 提出日 """

    current_accumulated_q1_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間時点")
    """ 当年度期初から第１四半期間時点 """


class FiscalYearEnd_edjp_FinancialReportSummary_consolidated_Q1(SQLModel):
    """ 決算期 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class FukuokaStockExchange_edjp_FinancialReportSummary_consolidated_Q1(SQLModel):
    """ 福岡証券取引所 """

    current_accumulated_q1_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間時点")
    """ 当年度期初から第１四半期間時点 """


class FukuokaStockExchangeEstablished_edjp_FinancialReportSummary_consolidated_Q1(SQLModel):
    """ 福岡証券取引所 既存市場 """

    current_accumulated_q1_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間時点")
    """ 当年度期初から第１四半期間時点 """


class FukuokaStockExchangeOthers_edjp_FinancialReportSummary_consolidated_Q1(SQLModel):
    """ 福岡証券取引所 その他 """

    current_accumulated_q1_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間時点")
    """ 当年度期初から第１四半期間時点 """


class FukuokaStockExchangeQBoard_edjp_FinancialReportSummary_consolidated_Q1(SQLModel):
    """ 福岡証券取引所 Q-Board """

    current_accumulated_q1_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間時点")
    """ 当年度期初から第１四半期間時点 """


class GeneralBusiness_edjp_FinancialReportSummary_consolidated_Q1(SQLModel):
    """ 一般事業会社 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class JapanSecuritiesDealersAssociation_edjp_FinancialReportSummary_consolidated_Q1(SQLModel):
    """ フェニックス """

    current_accumulated_q1_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間時点")
    """ 当年度期初から第１四半期間時点 """


class JapanSecuritiesDealersAssociationGreenSheet_edjp_FinancialReportSummary_consolidated_Q1(SQLModel):
    """ 日本証券業協会 フェニックス """

    current_accumulated_q1_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間時点")
    """ 当年度期初から第１四半期間時点 """


class NagoyaStockExchange_edjp_FinancialReportSummary_consolidated_Q1(SQLModel):
    """ 名古屋証券取引所 """

    current_accumulated_q1_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間時点")
    """ 当年度期初から第１四半期間時点 """


class NagoyaStockExchange1stSection_edjp_FinancialReportSummary_consolidated_Q1(SQLModel):
    """ 名古屋証券取引所 プレミア """

    current_accumulated_q1_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間時点")
    """ 当年度期初から第１四半期間時点 """


class NagoyaStockExchange2ndSection_edjp_FinancialReportSummary_consolidated_Q1(SQLModel):
    """ 名古屋証券取引所 メイン """

    current_accumulated_q1_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間時点")
    """ 当年度期初から第１四半期間時点 """


class NagoyaStockExchangeCentrex_edjp_FinancialReportSummary_consolidated_Q1(SQLModel):
    """ 名古屋証券取引所 ネクスト """

    current_accumulated_q1_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間時点")
    """ 当年度期初から第１四半期間時点 """


class NagoyaStockExchangeOthers_edjp_FinancialReportSummary_consolidated_Q1(SQLModel):
    """ 名古屋証券取引所 その他 """

    current_accumulated_q1_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間時点")
    """ 当年度期初から第１四半期間時点 """


class NameInquiries_edjp_FinancialReportSummary_consolidated_Q1(SQLModel):
    """ 氏名、問合せ先責任者 """

    current_accumulated_q1_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間時点")
    """ 当年度期初から第１四半期間時点 """


class NameRepresentative_edjp_FinancialReportSummary_consolidated_Q1(SQLModel):
    """ 氏名、代表者 """

    current_accumulated_q1_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間時点")
    """ 当年度期初から第１四半期間時点 """


class NotesForUsingForecastedInformationAndOthers_edjp_FinancialReportSummary_consolidated_Q1(SQLModel):
    """ 業績予想の適切な利用に関する説明、その他特記事項 """

    current_year_duration: IxNonNumericPublic = Field(default=None, description="当年度会計期間")
    """ 当年度会計期間 """


class NoteToApplyingOfSpecificAccountingOfTheConsolidatedQuarterlyFinancialStatements_edjp_FinancialReportSummary_consolidated_Q1(SQLModel):
    """ 四半期連結財務諸表の作成に特有の会計処理の適用に関する注記 """

    current_accumulated_q1_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間_連結_実績")
    """ 当年度期初から第１四半期間_連結_実績 """


class NoteToChangesInAccountingPoliciesAccountingEstimatesAndRetrospectiveRestatementQuarterlyConsolidated_edjp_FinancialReportSummary_consolidated_Q1(SQLModel):
    """ 会計方針の変更・会計上の見積りの変更・修正再表示に関する注記、四半期 """

    current_accumulated_q1_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間_連結_実績")
    """ 当年度期初から第１四半期間_連結_実績 """


class NoteToConsolidatedFinancialResults_edjp_FinancialReportSummary_consolidated_Q1(SQLModel):
    """ 連結業績に関する注記 """

    current_accumulated_q1_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間_連結_実績")
    """ 当年度期初から第１四半期間_連結_実績 """


class NoteToDividends_edjp_FinancialReportSummary_consolidated_Q1(SQLModel):
    """ 配当の状況に関する注記 """

    current_accumulated_q1_duration_annual_member_non_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間_年間_非連結又は個別_実績")
    """ 当年度期初から第１四半期間_年間_非連結又は個別_実績 """


class NoteToFinancialPositions_edjp_FinancialReportSummary_consolidated_Q1(SQLModel):
    """ 財政状態に関する注記 """

    current_accumulated_q1_instant_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間時点_連結_実績")
    """ 当年度期初から第１四半期間時点_連結_実績 """


class NoteToForecasts_edjp_FinancialReportSummary_consolidated_Q1(SQLModel):
    """ 業績予想に関する事項、注記 """

    current_year_duration_consolidated_member_forecast_member: IxNonNumericPublic = Field(default=None, description="当年度会計期間_連結_予想")
    """ 当年度会計期間_連結_予想 """


class NoteToFractionProcessingMethod_edjp_FinancialReportSummary_consolidated_Q1(SQLModel):
    """ 端数処理方法に関する注記 """

    current_accumulated_q1_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間時点")
    """ 当年度期初から第１四半期間時点 """


class NoteToNumberOfIssuedAndOutstandingSharesCommonStock_edjp_FinancialReportSummary_consolidated_Q1(SQLModel):
    """ 発行済株式数（普通株式）に関する注記 """

    current_accumulated_q1_instant_non_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間時点_非連結又は個別_実績")
    """ 当年度期初から第１四半期間時点_非連結又は個別_実績 """


class NoteToOperatingResults_edjp_FinancialReportSummary_consolidated_Q1(SQLModel):
    """ 経営成績に関する注記 """

    current_accumulated_q1_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間_連結_実績")
    """ 当年度期初から第１四半期間_連結_実績 """


class NoteToSignificantChangesInTheScopeOfConsolidationDuringThePeriod_edjp_FinancialReportSummary_consolidated_Q1(SQLModel):
    """ 期中における連結範囲の重要な変更に関する注記 """

    current_accumulated_q1_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間_連結_実績")
    """ 当年度期初から第１四半期間_連結_実績 """


class PreambleToForecasts_edjp_FinancialReportSummary_consolidated_Q1(SQLModel):
    """ 業績予想に関する事項 """

    current_year_duration_consolidated_member_forecast_member: IxNonNumericPublic = Field(default=None, description="当年度会計期間_連結_予想")
    """ 当年度会計期間_連結_予想 """


class RetrospectiveRestatement_edjp_FinancialReportSummary_consolidated_Q1(SQLModel):
    """ 修正再表示 """

    current_accumulated_q1_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間_連結_実績")
    """ 当年度期初から第１四半期間_連結_実績 """


class ReviewOfAttachedConsolidatedQuarterlyFinancialStatementsByACertifiedPublicAccountantOrAnAuditFirm_edjp_FinancialReportSummary_consolidated_Q1(SQLModel):
    """ 添付される四半期連結財務諸表に対する公認会計士又は監査法人によるレビュー """

    current_accumulated_q1_duration: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間")
    """ 当年度期初から第１四半期間 """


class SapporoStockExchange_edjp_FinancialReportSummary_consolidated_Q1(SQLModel):
    """ 札幌証券取引所 """

    current_accumulated_q1_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間時点")
    """ 当年度期初から第１四半期間時点 """


class SapporoStockExchangeAmbitious_edjp_FinancialReportSummary_consolidated_Q1(SQLModel):
    """ 札幌証券取引所 アンビシャス """

    current_accumulated_q1_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間時点")
    """ 当年度期初から第１四半期間時点 """


class SapporoStockExchangeEstablished_edjp_FinancialReportSummary_consolidated_Q1(SQLModel):
    """ 札幌証券取引所 既存市場 """

    current_accumulated_q1_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間時点")
    """ 当年度期初から第１四半期間時点 """


class SapporoStockExchangeOthers_edjp_FinancialReportSummary_consolidated_Q1(SQLModel):
    """ 札幌証券取引所 その他 """

    current_accumulated_q1_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間時点")
    """ 当年度期初から第１四半期間時点 """


class SecuritiesCode_edjp_FinancialReportSummary_consolidated_Q1(SQLModel):
    """ コード番号 """

    current_accumulated_q1_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間時点")
    """ 当年度期初から第１四半期間時点 """


class SignificantChangesInTheScopeOfConsolidationDuringThePeriod_edjp_FinancialReportSummary_consolidated_Q1(SQLModel):
    """ 期中における連結範囲の重要な変更 """

    current_accumulated_q1_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間_連結_実績")
    """ 当年度期初から第１四半期間_連結_実績 """


class SpecificBusiness_edjp_FinancialReportSummary_consolidated_Q1(SQLModel):
    """ 特定事業会社 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class SupplementalMaterialOfResults_edjp_FinancialReportSummary_consolidated_Q1(SQLModel):
    """ 決算補足説明資料作成の有無、期中 """

    current_accumulated_q1_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間時点")
    """ 当年度期初から第１四半期間時点 """


class TargetForBriefingOfResults_edjp_FinancialReportSummary_consolidated_Q1(SQLModel):
    """ 決算説明会の対象者 """

    current_accumulated_q1_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間時点")
    """ 当年度期初から第１四半期間時点 """


class Tel_edjp_FinancialReportSummary_consolidated_Q1(SQLModel):
    """ TEL """

    current_accumulated_q1_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間時点")
    """ 当年度期初から第１四半期間時点 """


class TitleForForecasts_edjp_FinancialReportSummary_consolidated_Q1(SQLModel):
    """ 業績予想タイトル名称 """

    current_year_duration_consolidated_member_forecast_member: IxNonNumericPublic = Field(default=None, description="当年度会計期間_連結_予想")
    """ 当年度会計期間_連結_予想 """


class TitleInquiries_edjp_FinancialReportSummary_consolidated_Q1(SQLModel):
    """ 役職名、問合せ先責任者 """

    current_accumulated_q1_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間時点")
    """ 当年度期初から第１四半期間時点 """


class TitleRepresentative_edjp_FinancialReportSummary_consolidated_Q1(SQLModel):
    """ 役職名、代表者 """

    current_accumulated_q1_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間時点")
    """ 当年度期初から第１四半期間時点 """


class TokyoStockExchange_edjp_FinancialReportSummary_consolidated_Q1(SQLModel):
    """ 東京証券取引所 """

    current_accumulated_q1_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間時点")
    """ 当年度期初から第１四半期間時点 """


class TokyoStockExchangeGrowth_edjp_FinancialReportSummary_consolidated_Q1(SQLModel):
    """ 東京証券取引所 グロース """

    current_accumulated_q1_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間時点")
    """ 当年度期初から第１四半期間時点 """


class TokyoStockExchangeOthers_edjp_FinancialReportSummary_consolidated_Q1(SQLModel):
    """ 東京証券取引所 その他 """

    current_accumulated_q1_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間時点")
    """ 当年度期初から第１四半期間時点 """


class TokyoStockExchangePrime_edjp_FinancialReportSummary_consolidated_Q1(SQLModel):
    """ 東京証券取引所 プライム """

    current_accumulated_q1_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間時点")
    """ 当年度期初から第１四半期間時点 """


class TokyoStockExchangePROMarket_edjp_FinancialReportSummary_consolidated_Q1(SQLModel):
    """ 東京証券取引所 PRO Market """

    current_accumulated_q1_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間時点")
    """ 当年度期初から第１四半期間時点 """


class TokyoStockExchangeStandard_edjp_FinancialReportSummary_consolidated_Q1(SQLModel):
    """ 東京証券取引所 スタンダード """

    current_accumulated_q1_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間時点")
    """ 当年度期初から第１四半期間時点 """


class URL_edjp_FinancialReportSummary_consolidated_Q1(SQLModel):
    """ URL """

    current_accumulated_q1_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間時点")
    """ 当年度期初から第１四半期間時点 """


class WayOfGettingSupplementalMaterialOfResults_edjp_FinancialReportSummary_consolidated_Q1(SQLModel):
    """ 入手方法等、決算補足説明資料、期中 """

    current_accumulated_q1_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間時点")
    """ 当年度期初から第１四半期間時点 """


class ApplyingOfSpecificAccountingOfTheQuarterlyFinancialStatements_edjp_FinancialReportSummary_Nonconsolidated_Q1(SQLModel):
    """ 四半期財務諸表の作成に特有の会計処理の適用 """

    current_accumulated_q1_duration_non_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間_非連結又は個別_実績")
    """ 当年度期初から第１四半期間_非連結又は個別_実績 """


class ChangesBasedOnRevisionsOfAccountingStandard_edjp_FinancialReportSummary_Nonconsolidated_Q1(SQLModel):
    """ 会計基準等の改正に伴う会計方針の変更 """

    current_accumulated_q1_duration_non_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間_非連結又は個別_実績")
    """ 当年度期初から第１四半期間_非連結又は個別_実績 """


class ChangesInAccountingEstimates_edjp_FinancialReportSummary_Nonconsolidated_Q1(SQLModel):
    """ 会計上の見積りの変更 """

    current_accumulated_q1_duration_non_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間_非連結又は個別_実績")
    """ 当年度期初から第１四半期間_非連結又は個別_実績 """


class ChangesOtherThanOnesBasedOnRevisionsOfAccountingStandard_edjp_FinancialReportSummary_Nonconsolidated_Q1(SQLModel):
    """ 会計基準等の改正に伴う変更以外の会計方針の変更 """

    current_accumulated_q1_duration_non_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間_非連結又は個別_実績")
    """ 当年度期初から第１四半期間_非連結又は個別_実績 """


class CompanyName_edjp_FinancialReportSummary_Nonconsolidated_Q1(SQLModel):
    """ 上場会社名 """

    current_accumulated_q1_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間時点")
    """ 当年度期初から第１四半期間時点 """


class ConveningBriefingOfResults_edjp_FinancialReportSummary_Nonconsolidated_Q1(SQLModel):
    """ 決算説明会開催の有無、期中 """

    current_accumulated_q1_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間時点")
    """ 当年度期初から第１四半期間時点 """


class CorrectionOfDividendForecastInThisQuarter_edjp_FinancialReportSummary_Nonconsolidated_Q1(SQLModel):
    """ 直近に公表されている配当予想からの修正の有無 """

    current_year_duration_annual_member_non_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度会計期間_年間_非連結又は個別_実績")
    """ 当年度会計期間_年間_非連結又は個別_実績 """


class CorrectionOfFinancialForecastInThisQuarter_edjp_FinancialReportSummary_Nonconsolidated_Q1(SQLModel):
    """ 直近に公表されている業績予想からの修正の有無 """

    current_year_duration_non_consolidated_member_forecast_member: IxNonNumericPublic = Field(default=None, description="当年度会計期間_非連結又は個別_予想")
    """ 当年度会計期間_非連結又は個別_予想 """


class DocumentName_edjp_FinancialReportSummary_Nonconsolidated_Q1(SQLModel):
    """ 文書名 """

    current_accumulated_q1_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間時点")
    """ 当年度期初から第１四半期間時点 """


class FASFMemberMark_edjp_FinancialReportSummary_Nonconsolidated_Q1(SQLModel):
    """ 財務会計基準機構会員マーク """

    current_accumulated_q1_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間時点")
    """ 当年度期初から第１四半期間時点 """


class FilingDate_edjp_FinancialReportSummary_Nonconsolidated_Q1(SQLModel):
    """ 提出日 """

    current_accumulated_q1_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間時点")
    """ 当年度期初から第１四半期間時点 """


class FiscalYearEnd_edjp_FinancialReportSummary_Nonconsolidated_Q1(SQLModel):
    """ 決算期 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class FukuokaStockExchange_edjp_FinancialReportSummary_Nonconsolidated_Q1(SQLModel):
    """ 福岡証券取引所 """

    current_accumulated_q1_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間時点")
    """ 当年度期初から第１四半期間時点 """


class FukuokaStockExchangeEstablished_edjp_FinancialReportSummary_Nonconsolidated_Q1(SQLModel):
    """ 福岡証券取引所 既存市場 """

    current_accumulated_q1_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間時点")
    """ 当年度期初から第１四半期間時点 """


class FukuokaStockExchangeOthers_edjp_FinancialReportSummary_Nonconsolidated_Q1(SQLModel):
    """ 福岡証券取引所 その他 """

    current_accumulated_q1_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間時点")
    """ 当年度期初から第１四半期間時点 """


class FukuokaStockExchangeQBoard_edjp_FinancialReportSummary_Nonconsolidated_Q1(SQLModel):
    """ 福岡証券取引所 Q-Board """

    current_accumulated_q1_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間時点")
    """ 当年度期初から第１四半期間時点 """


class GeneralBusiness_edjp_FinancialReportSummary_Nonconsolidated_Q1(SQLModel):
    """ 一般事業会社 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class JapanSecuritiesDealersAssociation_edjp_FinancialReportSummary_Nonconsolidated_Q1(SQLModel):
    """ フェニックス """

    current_accumulated_q1_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間時点")
    """ 当年度期初から第１四半期間時点 """


class JapanSecuritiesDealersAssociationGreenSheet_edjp_FinancialReportSummary_Nonconsolidated_Q1(SQLModel):
    """ 日本証券業協会 フェニックス """

    current_accumulated_q1_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間時点")
    """ 当年度期初から第１四半期間時点 """


class NagoyaStockExchange_edjp_FinancialReportSummary_Nonconsolidated_Q1(SQLModel):
    """ 名古屋証券取引所 """

    current_accumulated_q1_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間時点")
    """ 当年度期初から第１四半期間時点 """


class NagoyaStockExchange1stSection_edjp_FinancialReportSummary_Nonconsolidated_Q1(SQLModel):
    """ 名古屋証券取引所 プレミア """

    current_accumulated_q1_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間時点")
    """ 当年度期初から第１四半期間時点 """


class NagoyaStockExchange2ndSection_edjp_FinancialReportSummary_Nonconsolidated_Q1(SQLModel):
    """ 名古屋証券取引所 メイン """

    current_accumulated_q1_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間時点")
    """ 当年度期初から第１四半期間時点 """


class NagoyaStockExchangeCentrex_edjp_FinancialReportSummary_Nonconsolidated_Q1(SQLModel):
    """ 名古屋証券取引所 ネクスト """

    current_accumulated_q1_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間時点")
    """ 当年度期初から第１四半期間時点 """


class NagoyaStockExchangeOthers_edjp_FinancialReportSummary_Nonconsolidated_Q1(SQLModel):
    """ 名古屋証券取引所 その他 """

    current_accumulated_q1_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間時点")
    """ 当年度期初から第１四半期間時点 """


class NameInquiries_edjp_FinancialReportSummary_Nonconsolidated_Q1(SQLModel):
    """ 氏名、問合せ先責任者 """

    current_accumulated_q1_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間時点")
    """ 当年度期初から第１四半期間時点 """


class NameRepresentative_edjp_FinancialReportSummary_Nonconsolidated_Q1(SQLModel):
    """ 氏名、代表者 """

    current_accumulated_q1_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間時点")
    """ 当年度期初から第１四半期間時点 """


class NotesForUsingForecastedInformationAndOthers_edjp_FinancialReportSummary_Nonconsolidated_Q1(SQLModel):
    """ 業績予想の適切な利用に関する説明、その他特記事項 """

    current_year_duration: IxNonNumericPublic = Field(default=None, description="当年度会計期間")
    """ 当年度会計期間 """


class NoteToApplyingOfSpecificAccountingOfTheQuarterlyFinancialStatements_edjp_FinancialReportSummary_Nonconsolidated_Q1(SQLModel):
    """ 四半期財務諸表の作成に特有の会計処理の適用に関する注記 """

    current_accumulated_q1_duration_non_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間_非連結又は個別_実績")
    """ 当年度期初から第１四半期間_非連結又は個別_実績 """


class NoteToChangesInAccountingPoliciesAccountingEstimatesAndRetrospectiveRestatementQuarterlyConsolidated_edjp_FinancialReportSummary_Nonconsolidated_Q1(SQLModel):
    """ 会計方針の変更・会計上の見積りの変更・修正再表示に関する注記、四半期 """

    current_accumulated_q1_duration_non_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間_非連結又は個別_実績")
    """ 当年度期初から第１四半期間_非連結又は個別_実績 """


class NoteToDividends_edjp_FinancialReportSummary_Nonconsolidated_Q1(SQLModel):
    """ 配当の状況に関する注記 """

    current_accumulated_q1_duration_annual_member_non_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間_年間_非連結又は個別_実績")
    """ 当年度期初から第１四半期間_年間_非連結又は個別_実績 """


class NoteToFinancialPositions_edjp_FinancialReportSummary_Nonconsolidated_Q1(SQLModel):
    """ 財政状態に関する注記 """

    current_accumulated_q1_instant_non_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間時点_非連結又は個別_実績")
    """ 当年度期初から第１四半期間時点_非連結又は個別_実績 """


class NoteToFinancialResults_edjp_FinancialReportSummary_Nonconsolidated_Q1(SQLModel):
    """ 業績に関する注記 """

    current_accumulated_q1_duration_non_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間_非連結又は個別_実績")
    """ 当年度期初から第１四半期間_非連結又は個別_実績 """


class NoteToForecasts_edjp_FinancialReportSummary_Nonconsolidated_Q1(SQLModel):
    """ 業績予想に関する事項、注記 """

    current_year_duration_non_consolidated_member_forecast_member: IxNonNumericPublic = Field(default=None, description="当年度会計期間_非連結又は個別_予想")
    """ 当年度会計期間_非連結又は個別_予想 """


class NoteToFractionProcessingMethod_edjp_FinancialReportSummary_Nonconsolidated_Q1(SQLModel):
    """ 端数処理方法に関する注記 """

    current_accumulated_q1_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間時点")
    """ 当年度期初から第１四半期間時点 """


class NoteToNumberOfIssuedAndOutstandingSharesCommonStock_edjp_FinancialReportSummary_Nonconsolidated_Q1(SQLModel):
    """ 発行済株式数（普通株式）に関する注記 """

    current_accumulated_q1_instant_non_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間時点_非連結又は個別_実績")
    """ 当年度期初から第１四半期間時点_非連結又は個別_実績 """


class NoteToOperatingResults_edjp_FinancialReportSummary_Nonconsolidated_Q1(SQLModel):
    """ 経営成績に関する注記 """

    current_accumulated_q1_duration_non_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間_非連結又は個別_実績")
    """ 当年度期初から第１四半期間_非連結又は個別_実績 """


class PreambleToForecasts_edjp_FinancialReportSummary_Nonconsolidated_Q1(SQLModel):
    """ 業績予想に関する事項 """

    current_year_duration_non_consolidated_member_forecast_member: IxNonNumericPublic = Field(default=None, description="当年度会計期間_非連結又は個別_予想")
    """ 当年度会計期間_非連結又は個別_予想 """


class RetrospectiveRestatement_edjp_FinancialReportSummary_Nonconsolidated_Q1(SQLModel):
    """ 修正再表示 """

    current_accumulated_q1_duration_non_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間_非連結又は個別_実績")
    """ 当年度期初から第１四半期間_非連結又は個別_実績 """


class ReviewOfAttachedQuarterlyFinancialStatementsByACertifiedPublicAccountantOrAnAuditFirm_edjp_FinancialReportSummary_Nonconsolidated_Q1(SQLModel):
    """ 添付される四半期財務諸表に対する公認会計士又は監査法人によるレビュー """

    current_accumulated_q1_duration: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間")
    """ 当年度期初から第１四半期間 """


class SapporoStockExchange_edjp_FinancialReportSummary_Nonconsolidated_Q1(SQLModel):
    """ 札幌証券取引所 """

    current_accumulated_q1_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間時点")
    """ 当年度期初から第１四半期間時点 """


class SapporoStockExchangeAmbitious_edjp_FinancialReportSummary_Nonconsolidated_Q1(SQLModel):
    """ 札幌証券取引所 アンビシャス """

    current_accumulated_q1_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間時点")
    """ 当年度期初から第１四半期間時点 """


class SapporoStockExchangeEstablished_edjp_FinancialReportSummary_Nonconsolidated_Q1(SQLModel):
    """ 札幌証券取引所 既存市場 """

    current_accumulated_q1_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間時点")
    """ 当年度期初から第１四半期間時点 """


class SapporoStockExchangeOthers_edjp_FinancialReportSummary_Nonconsolidated_Q1(SQLModel):
    """ 札幌証券取引所 その他 """

    current_accumulated_q1_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間時点")
    """ 当年度期初から第１四半期間時点 """


class SecuritiesCode_edjp_FinancialReportSummary_Nonconsolidated_Q1(SQLModel):
    """ コード番号 """

    current_accumulated_q1_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間時点")
    """ 当年度期初から第１四半期間時点 """


class SpecificBusiness_edjp_FinancialReportSummary_Nonconsolidated_Q1(SQLModel):
    """ 特定事業会社 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class SupplementalMaterialOfResults_edjp_FinancialReportSummary_Nonconsolidated_Q1(SQLModel):
    """ 決算補足説明資料作成の有無、期中 """

    current_accumulated_q1_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間時点")
    """ 当年度期初から第１四半期間時点 """


class TargetForBriefingOfResults_edjp_FinancialReportSummary_Nonconsolidated_Q1(SQLModel):
    """ 決算説明会の対象者 """

    current_accumulated_q1_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間時点")
    """ 当年度期初から第１四半期間時点 """


class Tel_edjp_FinancialReportSummary_Nonconsolidated_Q1(SQLModel):
    """ TEL """

    current_accumulated_q1_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間時点")
    """ 当年度期初から第１四半期間時点 """


class TitleForForecasts_edjp_FinancialReportSummary_Nonconsolidated_Q1(SQLModel):
    """ 業績予想タイトル名称 """

    current_year_duration_non_consolidated_member_forecast_member: IxNonNumericPublic = Field(default=None, description="当年度会計期間_非連結又は個別_予想")
    """ 当年度会計期間_非連結又は個別_予想 """


class TitleInquiries_edjp_FinancialReportSummary_Nonconsolidated_Q1(SQLModel):
    """ 役職名、問合せ先責任者 """

    current_accumulated_q1_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間時点")
    """ 当年度期初から第１四半期間時点 """


class TitleRepresentative_edjp_FinancialReportSummary_Nonconsolidated_Q1(SQLModel):
    """ 役職名、代表者 """

    current_accumulated_q1_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間時点")
    """ 当年度期初から第１四半期間時点 """


class TokyoStockExchange_edjp_FinancialReportSummary_Nonconsolidated_Q1(SQLModel):
    """ 東京証券取引所 """

    current_accumulated_q1_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間時点")
    """ 当年度期初から第１四半期間時点 """


class TokyoStockExchangeGrowth_edjp_FinancialReportSummary_Nonconsolidated_Q1(SQLModel):
    """ 東京証券取引所 グロース """

    current_accumulated_q1_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間時点")
    """ 当年度期初から第１四半期間時点 """


class TokyoStockExchangeOthers_edjp_FinancialReportSummary_Nonconsolidated_Q1(SQLModel):
    """ 東京証券取引所 その他 """

    current_accumulated_q1_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間時点")
    """ 当年度期初から第１四半期間時点 """


class TokyoStockExchangePrime_edjp_FinancialReportSummary_Nonconsolidated_Q1(SQLModel):
    """ 東京証券取引所 プライム """

    current_accumulated_q1_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間時点")
    """ 当年度期初から第１四半期間時点 """


class TokyoStockExchangePROMarket_edjp_FinancialReportSummary_Nonconsolidated_Q1(SQLModel):
    """ 東京証券取引所 PRO Market """

    current_accumulated_q1_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間時点")
    """ 当年度期初から第１四半期間時点 """


class TokyoStockExchangeStandard_edjp_FinancialReportSummary_Nonconsolidated_Q1(SQLModel):
    """ 東京証券取引所 スタンダード """

    current_accumulated_q1_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間時点")
    """ 当年度期初から第１四半期間時点 """


class URL_edjp_FinancialReportSummary_Nonconsolidated_Q1(SQLModel):
    """ URL """

    current_accumulated_q1_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間時点")
    """ 当年度期初から第１四半期間時点 """


class WayOfGettingSupplementalMaterialOfResults_edjp_FinancialReportSummary_Nonconsolidated_Q1(SQLModel):
    """ 入手方法等、決算補足説明資料、期中 """

    current_accumulated_q1_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間時点")
    """ 当年度期初から第１四半期間時点 """


class ApplyingOfSpecificAccountingOfTheConsolidatedSemiAnnualFinancialStatements_edjp_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 中間連結財務諸表の作成に特有の会計処理の適用 """

    current_accumulated_q2_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間_連結_実績")
    """ 当年度期初から第２四半期間_連結_実績 """


class ChangesBasedOnRevisionsOfAccountingStandard_edjp_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 会計基準等の改正に伴う会計方針の変更 """

    current_accumulated_q2_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間_連結_実績")
    """ 当年度期初から第２四半期間_連結_実績 """


class ChangesInAccountingEstimates_edjp_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 会計上の見積りの変更 """

    current_accumulated_q2_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間_連結_実績")
    """ 当年度期初から第２四半期間_連結_実績 """


class ChangesOtherThanOnesBasedOnRevisionsOfAccountingStandard_edjp_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 会計基準等の改正に伴う変更以外の会計方針の変更 """

    current_accumulated_q2_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間_連結_実績")
    """ 当年度期初から第２四半期間_連結_実績 """


class CompanyName_edjp_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 上場会社名 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class ConveningBriefingOfResults_edjp_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 決算説明会開催の有無、期中 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class CorrectionOfConsolidatedFinancialForecastInThisQuarter_edjp_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 直近に公表されている業績予想からの修正の有無、連結 """

    current_year_duration_consolidated_member_forecast_member: IxNonNumericPublic = Field(default=None, description="当年度会計期間_連結_予想")
    """ 当年度会計期間_連結_予想 """


class CorrectionOfDividendForecastInThisQuarter_edjp_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 直近に公表されている配当予想からの修正の有無 """

    current_year_duration_annual_member_non_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度会計期間_年間_非連結又は個別_実績")
    """ 当年度会計期間_年間_非連結又は個別_実績 """


class DividendPayableDateAsPlanned_edjp_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 配当支払開始予定日 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class DocumentName_edjp_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 文書名 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class FASFMemberMark_edjp_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 財務会計基準機構会員マーク """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class FilingDate_edjp_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 提出日 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class FiscalYearEnd_edjp_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 決算期 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class FukuokaStockExchange_edjp_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 福岡証券取引所 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class FukuokaStockExchangeEstablished_edjp_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 福岡証券取引所 既存市場 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class FukuokaStockExchangeOthers_edjp_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 福岡証券取引所 その他 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class FukuokaStockExchangeQBoard_edjp_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 福岡証券取引所 Q-Board """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class GeneralBusiness_edjp_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 一般事業会社 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class JapanSecuritiesDealersAssociation_edjp_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ フェニックス """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class JapanSecuritiesDealersAssociationGreenSheet_edjp_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 日本証券業協会 フェニックス """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class NagoyaStockExchange_edjp_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 名古屋証券取引所 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class NagoyaStockExchange1stSection_edjp_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 名古屋証券取引所 プレミア """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class NagoyaStockExchange2ndSection_edjp_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 名古屋証券取引所 メイン """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class NagoyaStockExchangeCentrex_edjp_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 名古屋証券取引所 ネクスト """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class NagoyaStockExchangeOthers_edjp_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 名古屋証券取引所 その他 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class NameInquiries_edjp_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 氏名、問合せ先責任者 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class NameOfSubsidiariesExcludedFromConsolidation_edjp_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 社名、除外 """

    current_accumulated_q2_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間_連結_実績")
    """ 当年度期初から第２四半期間_連結_実績 """


class NameOfSubsidiariesNewlyConsolidated_edjp_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 社名、新規 """

    current_accumulated_q2_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間_連結_実績")
    """ 当年度期初から第２四半期間_連結_実績 """


class NameRepresentative_edjp_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 氏名、代表者 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class NotesForUsingForecastedInformationAndOthers_edjp_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 業績予想の適切な利用に関する説明、その他特記事項 """

    current_year_duration: IxNonNumericPublic = Field(default=None, description="当年度会計期間")
    """ 当年度会計期間 """


class NoteToApplyingOfSpecificAccountingOfTheConsolidatedSemiAnnualFinancialStatements_edjp_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 中間連結財務諸表の作成に特有の会計処理の適用に関する注記 """

    current_accumulated_q1_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間_連結_実績")
    """ 当年度期初から第１四半期間_連結_実績 """
    current_accumulated_q2_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間_連結_実績")
    """ 当年度期初から第２四半期間_連結_実績 """


class NoteToChangesInAccountingPoliciesAccountingEstimatesAndRetrospectiveRestatementQuarterlyConsolidated_edjp_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 会計方針の変更・会計上の見積りの変更・修正再表示に関する注記、四半期 """

    current_accumulated_q2_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間_連結_実績")
    """ 当年度期初から第２四半期間_連結_実績 """


class NoteToConsolidatedFinancialResults_edjp_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 連結業績に関する注記 """

    current_accumulated_q2_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間_連結_実績")
    """ 当年度期初から第２四半期間_連結_実績 """


class NoteToDividends_edjp_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 配当の状況に関する注記 """

    current_accumulated_q1_duration_annual_member_non_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第１四半期間_年間_非連結又は個別_実績")
    """ 当年度期初から第１四半期間_年間_非連結又は個別_実績 """
    current_accumulated_q2_duration_annual_member_non_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間_年間_非連結又は個別_実績")
    """ 当年度期初から第２四半期間_年間_非連結又は個別_実績 """


class NoteToFinancialPositions_edjp_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 財政状態に関する注記 """

    current_accumulated_q2_instant_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点_連結_実績")
    """ 当年度期初から第２四半期間時点_連結_実績 """


class NoteToForecasts_edjp_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 業績予想に関する事項、注記 """

    current_year_duration_consolidated_member_forecast_member: IxNonNumericPublic = Field(default=None, description="当年度会計期間_連結_予想")
    """ 当年度会計期間_連結_予想 """


class NoteToFractionProcessingMethod_edjp_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 端数処理方法に関する注記 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class NoteToNumberOfIssuedAndOutstandingSharesCommonStock_edjp_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 発行済株式数（普通株式）に関する注記 """

    current_accumulated_q2_instant_non_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点_非連結又は個別_実績")
    """ 当年度期初から第２四半期間時点_非連結又は個別_実績 """


class NoteToOperatingResults_edjp_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 経営成績に関する注記 """

    current_accumulated_q2_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間_連結_実績")
    """ 当年度期初から第２四半期間_連結_実績 """


class NoteToSignificantChangesInTheScopeOfConsolidationDuringThePeriod_edjp_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 期中における連結範囲の重要な変更に関する注記 """

    current_accumulated_q2_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間_連結_実績")
    """ 当年度期初から第２四半期間_連結_実績 """


class PreambleToForecasts_edjp_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 業績予想に関する事項 """

    current_year_duration_consolidated_member_forecast_member: IxNonNumericPublic = Field(default=None, description="当年度会計期間_連結_予想")
    """ 当年度会計期間_連結_予想 """


class RetrospectiveRestatement_edjp_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 修正再表示 """

    current_accumulated_q2_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間_連結_実績")
    """ 当年度期初から第２四半期間_連結_実績 """


class SapporoStockExchange_edjp_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 札幌証券取引所 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class SapporoStockExchangeAmbitious_edjp_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 札幌証券取引所 アンビシャス """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class SapporoStockExchangeEstablished_edjp_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 札幌証券取引所 既存市場 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class SapporoStockExchangeOthers_edjp_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 札幌証券取引所 その他 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class SecuritiesCode_edjp_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ コード番号 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class SemiAnnualStatementFilingDateAsPlanned_edjp_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 半期報告書提出予定日 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class SignificantChangesInTheScopeOfConsolidationDuringThePeriod_edjp_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 期中における連結範囲の重要な変更 """

    current_accumulated_q2_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間_連結_実績")
    """ 当年度期初から第２四半期間_連結_実績 """


class SpecificBusiness_edjp_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 特定事業会社 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class SupplementalMaterialOfResults_edjp_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 決算補足説明資料作成の有無、期中 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class TargetForBriefingOfResults_edjp_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 決算説明会の対象者 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class Tel_edjp_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ TEL """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class TitleForForecasts_edjp_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 業績予想タイトル名称 """

    current_year_duration_consolidated_member_forecast_member: IxNonNumericPublic = Field(default=None, description="当年度会計期間_連結_予想")
    """ 当年度会計期間_連結_予想 """


class TitleInquiries_edjp_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 役職名、問合せ先責任者 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class TitleRepresentative_edjp_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 役職名、代表者 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class TokyoStockExchange_edjp_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 東京証券取引所 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class TokyoStockExchangeGrowth_edjp_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 東京証券取引所 グロース """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class TokyoStockExchangeOthers_edjp_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 東京証券取引所 その他 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class TokyoStockExchangePrime_edjp_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 東京証券取引所 プライム """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class TokyoStockExchangePROMarket_edjp_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 東京証券取引所 PRO Market """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class TokyoStockExchangeStandard_edjp_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 東京証券取引所 スタンダード """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class URL_edjp_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ URL """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class WayOfGettingSupplementalMaterialOfResults_edjp_FinancialReportSummary_consolidated_Q2(SQLModel):
    """ 入手方法等、決算補足説明資料、期中 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class ApplyingOfSpecificAccountingOfTheSemiAnnualFinancialStatements_edjp_FinancialReportSummary_Nonconsolidated_Q2(SQLModel):
    """ 中間財務諸表の作成に特有の会計処理の適用 """

    current_accumulated_q2_duration_non_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間_非連結又は個別_実績")
    """ 当年度期初から第２四半期間_非連結又は個別_実績 """


class ChangesBasedOnRevisionsOfAccountingStandard_edjp_FinancialReportSummary_Nonconsolidated_Q2(SQLModel):
    """ 会計基準等の改正に伴う会計方針の変更 """

    current_accumulated_q2_duration_non_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間_非連結又は個別_実績")
    """ 当年度期初から第２四半期間_非連結又は個別_実績 """


class ChangesInAccountingEstimates_edjp_FinancialReportSummary_Nonconsolidated_Q2(SQLModel):
    """ 会計上の見積りの変更 """

    current_accumulated_q2_duration_non_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間_非連結又は個別_実績")
    """ 当年度期初から第２四半期間_非連結又は個別_実績 """


class ChangesOtherThanOnesBasedOnRevisionsOfAccountingStandard_edjp_FinancialReportSummary_Nonconsolidated_Q2(SQLModel):
    """ 会計基準等の改正に伴う変更以外の会計方針の変更 """

    current_accumulated_q2_duration_non_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間_非連結又は個別_実績")
    """ 当年度期初から第２四半期間_非連結又は個別_実績 """


class CompanyName_edjp_FinancialReportSummary_Nonconsolidated_Q2(SQLModel):
    """ 上場会社名 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class ConveningBriefingOfResults_edjp_FinancialReportSummary_Nonconsolidated_Q2(SQLModel):
    """ 決算説明会開催の有無、期中 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class CorrectionOfDividendForecastInThisQuarter_edjp_FinancialReportSummary_Nonconsolidated_Q2(SQLModel):
    """ 直近に公表されている配当予想からの修正の有無 """

    current_year_duration_annual_member_non_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度会計期間_年間_非連結又は個別_実績")
    """ 当年度会計期間_年間_非連結又は個別_実績 """


class CorrectionOfFinancialForecastInThisQuarter_edjp_FinancialReportSummary_Nonconsolidated_Q2(SQLModel):
    """ 直近に公表されている業績予想からの修正の有無 """

    current_year_duration_non_consolidated_member_forecast_member: IxNonNumericPublic = Field(default=None, description="当年度会計期間_非連結又は個別_予想")
    """ 当年度会計期間_非連結又は個別_予想 """


class DividendPayableDateAsPlanned_edjp_FinancialReportSummary_Nonconsolidated_Q2(SQLModel):
    """ 配当支払開始予定日 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class DocumentName_edjp_FinancialReportSummary_Nonconsolidated_Q2(SQLModel):
    """ 文書名 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class FASFMemberMark_edjp_FinancialReportSummary_Nonconsolidated_Q2(SQLModel):
    """ 財務会計基準機構会員マーク """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class FilingDate_edjp_FinancialReportSummary_Nonconsolidated_Q2(SQLModel):
    """ 提出日 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class FiscalYearEnd_edjp_FinancialReportSummary_Nonconsolidated_Q2(SQLModel):
    """ 決算期 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class FukuokaStockExchange_edjp_FinancialReportSummary_Nonconsolidated_Q2(SQLModel):
    """ 福岡証券取引所 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class FukuokaStockExchangeEstablished_edjp_FinancialReportSummary_Nonconsolidated_Q2(SQLModel):
    """ 福岡証券取引所 既存市場 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class FukuokaStockExchangeOthers_edjp_FinancialReportSummary_Nonconsolidated_Q2(SQLModel):
    """ 福岡証券取引所 その他 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class FukuokaStockExchangeQBoard_edjp_FinancialReportSummary_Nonconsolidated_Q2(SQLModel):
    """ 福岡証券取引所 Q-Board """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class GeneralBusiness_edjp_FinancialReportSummary_Nonconsolidated_Q2(SQLModel):
    """ 一般事業会社 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class JapanSecuritiesDealersAssociation_edjp_FinancialReportSummary_Nonconsolidated_Q2(SQLModel):
    """ フェニックス """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class JapanSecuritiesDealersAssociationGreenSheet_edjp_FinancialReportSummary_Nonconsolidated_Q2(SQLModel):
    """ 日本証券業協会 フェニックス """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class NagoyaStockExchange_edjp_FinancialReportSummary_Nonconsolidated_Q2(SQLModel):
    """ 名古屋証券取引所 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class NagoyaStockExchange1stSection_edjp_FinancialReportSummary_Nonconsolidated_Q2(SQLModel):
    """ 名古屋証券取引所 プレミア """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class NagoyaStockExchange2ndSection_edjp_FinancialReportSummary_Nonconsolidated_Q2(SQLModel):
    """ 名古屋証券取引所 メイン """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class NagoyaStockExchangeCentrex_edjp_FinancialReportSummary_Nonconsolidated_Q2(SQLModel):
    """ 名古屋証券取引所 ネクスト """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class NagoyaStockExchangeOthers_edjp_FinancialReportSummary_Nonconsolidated_Q2(SQLModel):
    """ 名古屋証券取引所 その他 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class NameInquiries_edjp_FinancialReportSummary_Nonconsolidated_Q2(SQLModel):
    """ 氏名、問合せ先責任者 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class NameRepresentative_edjp_FinancialReportSummary_Nonconsolidated_Q2(SQLModel):
    """ 氏名、代表者 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class NotesForUsingForecastedInformationAndOthers_edjp_FinancialReportSummary_Nonconsolidated_Q2(SQLModel):
    """ 業績予想の適切な利用に関する説明、その他特記事項 """

    current_year_duration: IxNonNumericPublic = Field(default=None, description="当年度会計期間")
    """ 当年度会計期間 """


class NoteToApplyingOfSpecificAccountingOfTheSemiAnnualFinancialStatements_edjp_FinancialReportSummary_Nonconsolidated_Q2(SQLModel):
    """ 中間財務諸表の作成に特有の会計処理の適用に関する注記 """

    current_accumulated_q2_duration_non_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間_非連結又は個別_実績")
    """ 当年度期初から第２四半期間_非連結又は個別_実績 """


class NoteToChangesInAccountingPoliciesAccountingEstimatesAndRetrospectiveRestatementQuarterlyConsolidated_edjp_FinancialReportSummary_Nonconsolidated_Q2(SQLModel):
    """ 会計方針の変更・会計上の見積りの変更・修正再表示に関する注記、四半期 """

    current_accumulated_q2_duration_non_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間_非連結又は個別_実績")
    """ 当年度期初から第２四半期間_非連結又は個別_実績 """


class NoteToDividends_edjp_FinancialReportSummary_Nonconsolidated_Q2(SQLModel):
    """ 配当の状況に関する注記 """

    current_accumulated_q2_duration_annual_member_non_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間_年間_非連結又は個別_実績")
    """ 当年度期初から第２四半期間_年間_非連結又は個別_実績 """


class NoteToFinancialPositions_edjp_FinancialReportSummary_Nonconsolidated_Q2(SQLModel):
    """ 財政状態に関する注記 """

    current_accumulated_q2_instant_non_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点_非連結又は個別_実績")
    """ 当年度期初から第２四半期間時点_非連結又は個別_実績 """


class NoteToFinancialResults_edjp_FinancialReportSummary_Nonconsolidated_Q2(SQLModel):
    """ 業績に関する注記 """

    current_accumulated_q2_duration_non_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間_非連結又は個別_実績")
    """ 当年度期初から第２四半期間_非連結又は個別_実績 """


class NoteToForecasts_edjp_FinancialReportSummary_Nonconsolidated_Q2(SQLModel):
    """ 業績予想に関する事項、注記 """

    current_year_duration_non_consolidated_member_forecast_member: IxNonNumericPublic = Field(default=None, description="当年度会計期間_非連結又は個別_予想")
    """ 当年度会計期間_非連結又は個別_予想 """


class NoteToFractionProcessingMethod_edjp_FinancialReportSummary_Nonconsolidated_Q2(SQLModel):
    """ 端数処理方法に関する注記 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class NoteToNumberOfIssuedAndOutstandingSharesCommonStock_edjp_FinancialReportSummary_Nonconsolidated_Q2(SQLModel):
    """ 発行済株式数（普通株式）に関する注記 """

    current_accumulated_q2_instant_non_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点_非連結又は個別_実績")
    """ 当年度期初から第２四半期間時点_非連結又は個別_実績 """


class NoteToOperatingResults_edjp_FinancialReportSummary_Nonconsolidated_Q2(SQLModel):
    """ 経営成績に関する注記 """

    current_accumulated_q2_duration_non_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間_非連結又は個別_実績")
    """ 当年度期初から第２四半期間_非連結又は個別_実績 """


class PreambleToForecasts_edjp_FinancialReportSummary_Nonconsolidated_Q2(SQLModel):
    """ 業績予想に関する事項 """

    current_year_duration_non_consolidated_member_forecast_member: IxNonNumericPublic = Field(default=None, description="当年度会計期間_非連結又は個別_予想")
    """ 当年度会計期間_非連結又は個別_予想 """


class RetrospectiveRestatement_edjp_FinancialReportSummary_Nonconsolidated_Q2(SQLModel):
    """ 修正再表示 """

    current_accumulated_q2_duration_non_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間_非連結又は個別_実績")
    """ 当年度期初から第２四半期間_非連結又は個別_実績 """


class SapporoStockExchange_edjp_FinancialReportSummary_Nonconsolidated_Q2(SQLModel):
    """ 札幌証券取引所 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class SapporoStockExchangeAmbitious_edjp_FinancialReportSummary_Nonconsolidated_Q2(SQLModel):
    """ 札幌証券取引所 アンビシャス """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class SapporoStockExchangeEstablished_edjp_FinancialReportSummary_Nonconsolidated_Q2(SQLModel):
    """ 札幌証券取引所 既存市場 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class SapporoStockExchangeOthers_edjp_FinancialReportSummary_Nonconsolidated_Q2(SQLModel):
    """ 札幌証券取引所 その他 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class SecuritiesCode_edjp_FinancialReportSummary_Nonconsolidated_Q2(SQLModel):
    """ コード番号 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class SemiAnnualStatementFilingDateAsPlanned_edjp_FinancialReportSummary_Nonconsolidated_Q2(SQLModel):
    """ 半期報告書提出予定日 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class SpecificBusiness_edjp_FinancialReportSummary_Nonconsolidated_Q2(SQLModel):
    """ 特定事業会社 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class SupplementalMaterialOfResults_edjp_FinancialReportSummary_Nonconsolidated_Q2(SQLModel):
    """ 決算補足説明資料作成の有無、期中 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class TargetForBriefingOfResults_edjp_FinancialReportSummary_Nonconsolidated_Q2(SQLModel):
    """ 決算説明会の対象者 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class Tel_edjp_FinancialReportSummary_Nonconsolidated_Q2(SQLModel):
    """ TEL """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class TitleForForecasts_edjp_FinancialReportSummary_Nonconsolidated_Q2(SQLModel):
    """ 業績予想タイトル名称 """

    current_year_duration_non_consolidated_member_forecast_member: IxNonNumericPublic = Field(default=None, description="当年度会計期間_非連結又は個別_予想")
    """ 当年度会計期間_非連結又は個別_予想 """


class TitleInquiries_edjp_FinancialReportSummary_Nonconsolidated_Q2(SQLModel):
    """ 役職名、問合せ先責任者 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class TitleRepresentative_edjp_FinancialReportSummary_Nonconsolidated_Q2(SQLModel):
    """ 役職名、代表者 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class TokyoStockExchange_edjp_FinancialReportSummary_Nonconsolidated_Q2(SQLModel):
    """ 東京証券取引所 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class TokyoStockExchangeGrowth_edjp_FinancialReportSummary_Nonconsolidated_Q2(SQLModel):
    """ 東京証券取引所 グロース """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class TokyoStockExchangeOthers_edjp_FinancialReportSummary_Nonconsolidated_Q2(SQLModel):
    """ 東京証券取引所 その他 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class TokyoStockExchangePrime_edjp_FinancialReportSummary_Nonconsolidated_Q2(SQLModel):
    """ 東京証券取引所 プライム """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class TokyoStockExchangePROMarket_edjp_FinancialReportSummary_Nonconsolidated_Q2(SQLModel):
    """ 東京証券取引所 PRO Market """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class TokyoStockExchangeStandard_edjp_FinancialReportSummary_Nonconsolidated_Q2(SQLModel):
    """ 東京証券取引所 スタンダード """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class URL_edjp_FinancialReportSummary_Nonconsolidated_Q2(SQLModel):
    """ URL """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class WayOfGettingSupplementalMaterialOfResults_edjp_FinancialReportSummary_Nonconsolidated_Q2(SQLModel):
    """ 入手方法等、決算補足説明資料、期中 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class ApplyingOfSpecificAccountingOfTheConsolidatedQuarterlyFinancialStatements_edjp_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 四半期連結財務諸表の作成に特有の会計処理の適用 """

    current_accumulated_q3_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間_連結_実績")
    """ 当年度期初から第３四半期間_連結_実績 """


class ChangesBasedOnRevisionsOfAccountingStandard_edjp_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 会計基準等の改正に伴う会計方針の変更 """

    current_accumulated_q3_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間_連結_実績")
    """ 当年度期初から第３四半期間_連結_実績 """


class ChangesInAccountingEstimates_edjp_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 会計上の見積りの変更 """

    current_accumulated_q3_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間_連結_実績")
    """ 当年度期初から第３四半期間_連結_実績 """


class ChangesOtherThanOnesBasedOnRevisionsOfAccountingStandard_edjp_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 会計基準等の改正に伴う変更以外の会計方針の変更 """

    current_accumulated_q3_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間_連結_実績")
    """ 当年度期初から第３四半期間_連結_実績 """


class CompanyName_edjp_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 上場会社名 """

    current_accumulated_q3_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点")
    """ 当年度期初から第３四半期間時点 """


class ConveningBriefingOfResults_edjp_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 決算説明会開催の有無、期中 """

    current_accumulated_q3_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点")
    """ 当年度期初から第３四半期間時点 """


class CorrectionOfConsolidatedFinancialForecastInThisQuarter_edjp_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 直近に公表されている業績予想からの修正の有無、連結 """

    current_year_duration_consolidated_member_forecast_member: IxNonNumericPublic = Field(default=None, description="当年度会計期間_連結_予想")
    """ 当年度会計期間_連結_予想 """


class CorrectionOfDividendForecastInThisQuarter_edjp_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 直近に公表されている配当予想からの修正の有無 """

    current_year_duration_annual_member_non_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度会計期間_年間_非連結又は個別_実績")
    """ 当年度会計期間_年間_非連結又は個別_実績 """


class DividendPayableDateAsPlanned_edjp_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 配当支払開始予定日 """

    current_accumulated_q3_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点")
    """ 当年度期初から第３四半期間時点 """


class DocumentName_edjp_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 文書名 """

    current_accumulated_q3_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点")
    """ 当年度期初から第３四半期間時点 """


class FASFMemberMark_edjp_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 財務会計基準機構会員マーク """

    current_accumulated_q3_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点")
    """ 当年度期初から第３四半期間時点 """


class FilingDate_edjp_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 提出日 """

    current_accumulated_q3_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点")
    """ 当年度期初から第３四半期間時点 """


class FiscalYearEnd_edjp_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 決算期 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class FukuokaStockExchange_edjp_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 福岡証券取引所 """

    current_accumulated_q3_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点")
    """ 当年度期初から第３四半期間時点 """


class FukuokaStockExchangeEstablished_edjp_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 福岡証券取引所 既存市場 """

    current_accumulated_q3_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点")
    """ 当年度期初から第３四半期間時点 """


class FukuokaStockExchangeOthers_edjp_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 福岡証券取引所 その他 """

    current_accumulated_q3_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点")
    """ 当年度期初から第３四半期間時点 """


class FukuokaStockExchangeQBoard_edjp_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 福岡証券取引所 Q-Board """

    current_accumulated_q3_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点")
    """ 当年度期初から第３四半期間時点 """


class GeneralBusiness_edjp_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 一般事業会社 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class JapanSecuritiesDealersAssociation_edjp_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ フェニックス """

    current_accumulated_q3_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点")
    """ 当年度期初から第３四半期間時点 """


class JapanSecuritiesDealersAssociationGreenSheet_edjp_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 日本証券業協会 フェニックス """

    current_accumulated_q3_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点")
    """ 当年度期初から第３四半期間時点 """


class NagoyaStockExchange_edjp_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 名古屋証券取引所 """

    current_accumulated_q3_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点")
    """ 当年度期初から第３四半期間時点 """


class NagoyaStockExchange1stSection_edjp_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 名古屋証券取引所 プレミア """

    current_accumulated_q3_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点")
    """ 当年度期初から第３四半期間時点 """


class NagoyaStockExchange2ndSection_edjp_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 名古屋証券取引所 メイン """

    current_accumulated_q3_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点")
    """ 当年度期初から第３四半期間時点 """


class NagoyaStockExchangeCentrex_edjp_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 名古屋証券取引所 ネクスト """

    current_accumulated_q3_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点")
    """ 当年度期初から第３四半期間時点 """


class NagoyaStockExchangeOthers_edjp_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 名古屋証券取引所 その他 """

    current_accumulated_q3_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点")
    """ 当年度期初から第３四半期間時点 """


class NameInquiries_edjp_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 氏名、問合せ先責任者 """

    current_accumulated_q3_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点")
    """ 当年度期初から第３四半期間時点 """


class NameOfSubsidiariesExcludedFromConsolidation_edjp_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 社名、除外 """

    current_accumulated_q3_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間_連結_実績")
    """ 当年度期初から第３四半期間_連結_実績 """


class NameOfSubsidiariesNewlyConsolidated_edjp_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 社名、新規 """

    current_accumulated_q3_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間_連結_実績")
    """ 当年度期初から第３四半期間_連結_実績 """


class NameRepresentative_edjp_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 氏名、代表者 """

    current_accumulated_q3_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点")
    """ 当年度期初から第３四半期間時点 """


class NotesForUsingForecastedInformationAndOthers_edjp_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 業績予想の適切な利用に関する説明、その他特記事項 """

    current_year_duration: IxNonNumericPublic = Field(default=None, description="当年度会計期間")
    """ 当年度会計期間 """


class NoteToApplyingOfSpecificAccountingOfTheConsolidatedQuarterlyFinancialStatements_edjp_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 四半期連結財務諸表の作成に特有の会計処理の適用に関する注記 """

    current_accumulated_q3_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間_連結_実績")
    """ 当年度期初から第３四半期間_連結_実績 """


class NoteToChangesInAccountingPoliciesAccountingEstimatesAndRetrospectiveRestatementQuarterlyConsolidated_edjp_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 会計方針の変更・会計上の見積りの変更・修正再表示に関する注記、四半期 """

    current_accumulated_q3_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間_連結_実績")
    """ 当年度期初から第３四半期間_連結_実績 """


class NoteToConsolidatedFinancialResults_edjp_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 連結業績に関する注記 """

    current_accumulated_q3_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間_連結_実績")
    """ 当年度期初から第３四半期間_連結_実績 """


class NoteToDividends_edjp_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 配当の状況に関する注記 """

    current_accumulated_q3_duration_annual_member_non_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間_年間_非連結又は個別_実績")
    """ 当年度期初から第３四半期間_年間_非連結又は個別_実績 """


class NoteToFinancialPositions_edjp_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 財政状態に関する注記 """

    current_accumulated_q3_instant_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点_連結_実績")
    """ 当年度期初から第３四半期間時点_連結_実績 """


class NoteToForecasts_edjp_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 業績予想に関する事項、注記 """

    current_year_duration_consolidated_member_forecast_member: IxNonNumericPublic = Field(default=None, description="当年度会計期間_連結_予想")
    """ 当年度会計期間_連結_予想 """


class NoteToFractionProcessingMethod_edjp_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 端数処理方法に関する注記 """

    current_accumulated_q3_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点")
    """ 当年度期初から第３四半期間時点 """


class NoteToNumberOfIssuedAndOutstandingSharesCommonStock_edjp_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 発行済株式数（普通株式）に関する注記 """

    current_accumulated_q3_instant_non_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点_非連結又は個別_実績")
    """ 当年度期初から第３四半期間時点_非連結又は個別_実績 """


class NoteToOperatingResults_edjp_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 経営成績に関する注記 """

    current_accumulated_q3_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間_連結_実績")
    """ 当年度期初から第３四半期間_連結_実績 """


class NoteToSignificantChangesInTheScopeOfConsolidationDuringThePeriod_edjp_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 期中における連結範囲の重要な変更に関する注記 """

    current_accumulated_q3_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間_連結_実績")
    """ 当年度期初から第３四半期間_連結_実績 """


class PreambleToForecasts_edjp_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 業績予想に関する事項 """

    current_year_duration_consolidated_member_forecast_member: IxNonNumericPublic = Field(default=None, description="当年度会計期間_連結_予想")
    """ 当年度会計期間_連結_予想 """


class RetrospectiveRestatement_edjp_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 修正再表示 """

    current_accumulated_q3_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間_連結_実績")
    """ 当年度期初から第３四半期間_連結_実績 """


class ReviewOfAttachedConsolidatedQuarterlyFinancialStatementsByACertifiedPublicAccountantOrAnAuditFirm_edjp_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 添付される四半期連結財務諸表に対する公認会計士又は監査法人によるレビュー """

    current_accumulated_q3_duration: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間")
    """ 当年度期初から第３四半期間 """


class SapporoStockExchange_edjp_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 札幌証券取引所 """

    current_accumulated_q3_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点")
    """ 当年度期初から第３四半期間時点 """


class SapporoStockExchangeAmbitious_edjp_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 札幌証券取引所 アンビシャス """

    current_accumulated_q3_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点")
    """ 当年度期初から第３四半期間時点 """


class SapporoStockExchangeEstablished_edjp_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 札幌証券取引所 既存市場 """

    current_accumulated_q3_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点")
    """ 当年度期初から第３四半期間時点 """


class SapporoStockExchangeOthers_edjp_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 札幌証券取引所 その他 """

    current_accumulated_q3_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点")
    """ 当年度期初から第３四半期間時点 """


class SecuritiesCode_edjp_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ コード番号 """

    current_accumulated_q3_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点")
    """ 当年度期初から第３四半期間時点 """


class SignificantChangesInTheScopeOfConsolidationDuringThePeriod_edjp_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 期中における連結範囲の重要な変更 """

    current_accumulated_q3_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間_連結_実績")
    """ 当年度期初から第３四半期間_連結_実績 """


class SpecificBusiness_edjp_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 特定事業会社 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class SupplementalMaterialOfResults_edjp_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 決算補足説明資料作成の有無、期中 """

    current_accumulated_q3_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点")
    """ 当年度期初から第３四半期間時点 """


class TargetForBriefingOfResults_edjp_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 決算説明会の対象者 """

    current_accumulated_q3_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点")
    """ 当年度期初から第３四半期間時点 """


class Tel_edjp_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ TEL """

    current_accumulated_q3_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点")
    """ 当年度期初から第３四半期間時点 """


class TitleForForecasts_edjp_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 業績予想タイトル名称 """

    current_year_duration_consolidated_member_forecast_member: IxNonNumericPublic = Field(default=None, description="当年度会計期間_連結_予想")
    """ 当年度会計期間_連結_予想 """


class TitleInquiries_edjp_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 役職名、問合せ先責任者 """

    current_accumulated_q3_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点")
    """ 当年度期初から第３四半期間時点 """


class TitleRepresentative_edjp_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 役職名、代表者 """

    current_accumulated_q3_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点")
    """ 当年度期初から第３四半期間時点 """


class TokyoStockExchange_edjp_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 東京証券取引所 """

    current_accumulated_q3_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点")
    """ 当年度期初から第３四半期間時点 """


class TokyoStockExchangeGrowth_edjp_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 東京証券取引所 グロース """

    current_accumulated_q3_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点")
    """ 当年度期初から第３四半期間時点 """


class TokyoStockExchangeOthers_edjp_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 東京証券取引所 その他 """

    current_accumulated_q3_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点")
    """ 当年度期初から第３四半期間時点 """


class TokyoStockExchangePrime_edjp_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 東京証券取引所 プライム """

    current_accumulated_q3_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点")
    """ 当年度期初から第３四半期間時点 """


class TokyoStockExchangePROMarket_edjp_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 東京証券取引所 PRO Market """

    current_accumulated_q3_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点")
    """ 当年度期初から第３四半期間時点 """


class TokyoStockExchangeStandard_edjp_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 東京証券取引所 スタンダード """

    current_accumulated_q3_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点")
    """ 当年度期初から第３四半期間時点 """


class URL_edjp_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ URL """

    current_accumulated_q3_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点")
    """ 当年度期初から第３四半期間時点 """


class WayOfGettingSupplementalMaterialOfResults_edjp_FinancialReportSummary_consolidated_Q3(SQLModel):
    """ 入手方法等、決算補足説明資料、期中 """

    current_accumulated_q3_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第３四半期間時点")
    """ 当年度期初から第３四半期間時点 """


class ApplyingOfSpecificAccountingOfTheConsolidatedSemiAnnualFinancialStatements_edjp_FinancialReportSummary(SQLModel):
    """ 中間連結財務諸表の作成に特有の会計処理の適用 """

    current_accumulated_q2_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間_連結_実績")
    """ 当年度期初から第２四半期間_連結_実績 """


class ChangesBasedOnRevisionsOfAccountingStandard_edjp_FinancialReportSummary(SQLModel):
    """ 会計基準等の改正に伴う会計方針の変更 """

    current_accumulated_q2_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間_連結_実績")
    """ 当年度期初から第２四半期間_連結_実績 """


class ChangesInAccountingEstimates_edjp_FinancialReportSummary(SQLModel):
    """ 会計上の見積りの変更 """

    current_accumulated_q2_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間_連結_実績")
    """ 当年度期初から第２四半期間_連結_実績 """


class ChangesOtherThanOnesBasedOnRevisionsOfAccountingStandard_edjp_FinancialReportSummary(SQLModel):
    """ 会計基準等の改正に伴う変更以外の会計方針の変更 """

    current_accumulated_q2_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間_連結_実績")
    """ 当年度期初から第２四半期間_連結_実績 """


class CompanyName_edjp_FinancialReportSummary(SQLModel):
    """ 上場会社名 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class ConveningBriefingOfResults_edjp_FinancialReportSummary(SQLModel):
    """ 決算説明会開催の有無、期中 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class CorrectionOfConsolidatedFinancialForecastInThisQuarter_edjp_FinancialReportSummary(SQLModel):
    """ 直近に公表されている業績予想からの修正の有無、連結 """

    current_year_duration_consolidated_member_forecast_member: IxNonNumericPublic = Field(default=None, description="当年度会計期間_連結_予想")
    """ 当年度会計期間_連結_予想 """


class CorrectionOfDividendForecastInThisQuarter_edjp_FinancialReportSummary(SQLModel):
    """ 直近に公表されている配当予想からの修正の有無 """

    current_year_duration_annual_member_non_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度会計期間_年間_非連結又は個別_実績")
    """ 当年度会計期間_年間_非連結又は個別_実績 """


class DividendPayableDateAsPlanned_edjp_FinancialReportSummary(SQLModel):
    """ 配当支払開始予定日 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class DocumentName_edjp_FinancialReportSummary(SQLModel):
    """ 文書名 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class FASFMemberMark_edjp_FinancialReportSummary(SQLModel):
    """ 財務会計基準機構会員マーク """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class FilingDate_edjp_FinancialReportSummary(SQLModel):
    """ 提出日 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class FiscalYearEnd_edjp_FinancialReportSummary(SQLModel):
    """ 決算期 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class FukuokaStockExchange_edjp_FinancialReportSummary(SQLModel):
    """ 福岡証券取引所 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class FukuokaStockExchangeEstablished_edjp_FinancialReportSummary(SQLModel):
    """ 福岡証券取引所 既存市場 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class FukuokaStockExchangeOthers_edjp_FinancialReportSummary(SQLModel):
    """ 福岡証券取引所 その他 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class FukuokaStockExchangeQBoard_edjp_FinancialReportSummary(SQLModel):
    """ 福岡証券取引所 Q-Board """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class GeneralBusiness_edjp_FinancialReportSummary(SQLModel):
    """ 一般事業会社 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class JapanSecuritiesDealersAssociation_edjp_FinancialReportSummary(SQLModel):
    """ フェニックス """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class JapanSecuritiesDealersAssociationGreenSheet_edjp_FinancialReportSummary(SQLModel):
    """ 日本証券業協会 フェニックス """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class NagoyaStockExchange_edjp_FinancialReportSummary(SQLModel):
    """ 名古屋証券取引所 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class NagoyaStockExchange1stSection_edjp_FinancialReportSummary(SQLModel):
    """ 名古屋証券取引所 プレミア """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class NagoyaStockExchange2ndSection_edjp_FinancialReportSummary(SQLModel):
    """ 名古屋証券取引所 メイン """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class NagoyaStockExchangeCentrex_edjp_FinancialReportSummary(SQLModel):
    """ 名古屋証券取引所 ネクスト """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class NagoyaStockExchangeOthers_edjp_FinancialReportSummary(SQLModel):
    """ 名古屋証券取引所 その他 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class NameInquiries_edjp_FinancialReportSummary(SQLModel):
    """ 氏名、問合せ先責任者 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class NameRepresentative_edjp_FinancialReportSummary(SQLModel):
    """ 氏名、代表者 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class NotesForUsingForecastedInformationAndOthers_edjp_FinancialReportSummary(SQLModel):
    """ 業績予想の適切な利用に関する説明、その他特記事項 """

    current_year_duration: IxNonNumericPublic = Field(default=None, description="当年度会計期間")
    """ 当年度会計期間 """


class NoteToApplyingOfSpecificAccountingOfTheConsolidatedSemiAnnualFinancialStatements_edjp_FinancialReportSummary(SQLModel):
    """ 中間連結財務諸表の作成に特有の会計処理の適用に関する注記 """

    current_accumulated_q2_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間_連結_実績")
    """ 当年度期初から第２四半期間_連結_実績 """


class NoteToChangesInAccountingPoliciesAccountingEstimatesAndRetrospectiveRestatementQuarterlyConsolidated_edjp_FinancialReportSummary(SQLModel):
    """ 会計方針の変更・会計上の見積りの変更・修正再表示に関する注記、四半期 """

    current_accumulated_q2_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間_連結_実績")
    """ 当年度期初から第２四半期間_連結_実績 """


class NoteToConsolidatedFinancialResults_edjp_FinancialReportSummary(SQLModel):
    """ 連結業績に関する注記 """

    current_accumulated_q2_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間_連結_実績")
    """ 当年度期初から第２四半期間_連結_実績 """


class NoteToDividends_edjp_FinancialReportSummary(SQLModel):
    """ 配当の状況に関する注記 """

    current_accumulated_q2_duration_annual_member_non_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間_年間_非連結又は個別_実績")
    """ 当年度期初から第２四半期間_年間_非連結又は個別_実績 """


class NoteToFinancialPositions_edjp_FinancialReportSummary(SQLModel):
    """ 財政状態に関する注記 """

    current_accumulated_q2_instant_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点_連結_実績")
    """ 当年度期初から第２四半期間時点_連結_実績 """


class NoteToForecasts_edjp_FinancialReportSummary(SQLModel):
    """ 業績予想に関する事項、注記 """

    current_year_duration_consolidated_member_forecast_member: IxNonNumericPublic = Field(default=None, description="当年度会計期間_連結_予想")
    """ 当年度会計期間_連結_予想 """


class NoteToFractionProcessingMethod_edjp_FinancialReportSummary(SQLModel):
    """ 端数処理方法に関する注記 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class NoteToNumberOfIssuedAndOutstandingSharesCommonStock_edjp_FinancialReportSummary(SQLModel):
    """ 発行済株式数（普通株式）に関する注記 """

    current_accumulated_q2_instant_non_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点_非連結又は個別_実績")
    """ 当年度期初から第２四半期間時点_非連結又は個別_実績 """


class NoteToOperatingResults_edjp_FinancialReportSummary(SQLModel):
    """ 経営成績に関する注記 """

    current_accumulated_q2_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間_連結_実績")
    """ 当年度期初から第２四半期間_連結_実績 """


class NoteToSignificantChangesInTheScopeOfConsolidationDuringThePeriod_edjp_FinancialReportSummary(SQLModel):
    """ 期中における連結範囲の重要な変更に関する注記 """

    current_accumulated_q2_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間_連結_実績")
    """ 当年度期初から第２四半期間_連結_実績 """


class PreambleToForecasts_edjp_FinancialReportSummary(SQLModel):
    """ 業績予想に関する事項 """

    current_year_duration_consolidated_member_forecast_member: IxNonNumericPublic = Field(default=None, description="当年度会計期間_連結_予想")
    """ 当年度会計期間_連結_予想 """


class RetrospectiveRestatement_edjp_FinancialReportSummary(SQLModel):
    """ 修正再表示 """

    current_accumulated_q2_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間_連結_実績")
    """ 当年度期初から第２四半期間_連結_実績 """


class SapporoStockExchange_edjp_FinancialReportSummary(SQLModel):
    """ 札幌証券取引所 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class SapporoStockExchangeAmbitious_edjp_FinancialReportSummary(SQLModel):
    """ 札幌証券取引所 アンビシャス """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class SapporoStockExchangeEstablished_edjp_FinancialReportSummary(SQLModel):
    """ 札幌証券取引所 既存市場 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class SapporoStockExchangeOthers_edjp_FinancialReportSummary(SQLModel):
    """ 札幌証券取引所 その他 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class SecuritiesCode_edjp_FinancialReportSummary(SQLModel):
    """ コード番号 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class SemiAnnualStatementFilingDateAsPlanned_edjp_FinancialReportSummary(SQLModel):
    """ 半期報告書提出予定日 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class SignificantChangesInTheScopeOfConsolidationDuringThePeriod_edjp_FinancialReportSummary(SQLModel):
    """ 期中における連結範囲の重要な変更 """

    current_accumulated_q2_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間_連結_実績")
    """ 当年度期初から第２四半期間_連結_実績 """


class SpecificBusiness_edjp_FinancialReportSummary(SQLModel):
    """ 特定事業会社 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class SupplementalMaterialOfResults_edjp_FinancialReportSummary(SQLModel):
    """ 決算補足説明資料作成の有無、期中 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class TargetForBriefingOfResults_edjp_FinancialReportSummary(SQLModel):
    """ 決算説明会の対象者 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class Tel_edjp_FinancialReportSummary(SQLModel):
    """ TEL """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class TitleForForecasts_edjp_FinancialReportSummary(SQLModel):
    """ 業績予想タイトル名称 """

    current_year_duration_consolidated_member_forecast_member: IxNonNumericPublic = Field(default=None, description="当年度会計期間_連結_予想")
    """ 当年度会計期間_連結_予想 """


class TitleInquiries_edjp_FinancialReportSummary(SQLModel):
    """ 役職名、問合せ先責任者 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class TitleRepresentative_edjp_FinancialReportSummary(SQLModel):
    """ 役職名、代表者 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class TokyoStockExchange_edjp_FinancialReportSummary(SQLModel):
    """ 東京証券取引所 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class TokyoStockExchangeGrowth_edjp_FinancialReportSummary(SQLModel):
    """ 東京証券取引所 グロース """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class TokyoStockExchangeOthers_edjp_FinancialReportSummary(SQLModel):
    """ 東京証券取引所 その他 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class TokyoStockExchangePrime_edjp_FinancialReportSummary(SQLModel):
    """ 東京証券取引所 プライム """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class TokyoStockExchangePROMarket_edjp_FinancialReportSummary(SQLModel):
    """ 東京証券取引所 PRO Market """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class TokyoStockExchangeStandard_edjp_FinancialReportSummary(SQLModel):
    """ 東京証券取引所 スタンダード """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class URL_edjp_FinancialReportSummary(SQLModel):
    """ URL """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class WayOfGettingSupplementalMaterialOfResults_edjp_FinancialReportSummary(SQLModel):
    """ 入手方法等、決算補足説明資料、期中 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class MajorComponentsOfSellingGeneralAndAdministrativeExpensesTextBlock_edjp_MajorComponentsOfSellingGeneralAndAdministrativeExpenses_consolidated_Q2(SQLModel):
    """ 主要な販売費及び一般管理費 [テキストブロック] """

    current_ytd_duration: IxNonNumericPublic = Field(default=None, description="当年度期初から当日まで")
    """ 当年度期初から当日まで """


class NotesRegardingGuaranteeObligationsTextBlock_edjp_NotesRegardingGuaranteeObligations_consolidated_Q2(SQLModel):
    """ 保証債務の注記 [テキストブロック] """

    current_quarter_instant: IxNonNumericPublic = Field(default=None, description="当四半期時点")
    """ 当四半期時点 """


class NotesRegardingImpairmentLossTextBlock_edjp_NotesRegardingImpairmentLoss_consolidated_Q2(SQLModel):
    """ 減損損失に関する注記 [テキストブロック] """

    current_ytd_duration: IxNonNumericPublic = Field(default=None, description="当年度期初から当日まで")
    """ 当年度期初から当日まで """


class NotesRegardingPromissoryNotesDueOnBalanceSheetDateTextBlock_edjp_NotesRegardingPromissoryNotesDueOnBalanceSheetDate_consolidated_Q2(SQLModel):
    """ 期末日満期手形の会計処理 [テキストブロック] """

    current_quarter_instant: IxNonNumericPublic = Field(default=None, description="当四半期時点")
    """ 当四半期時点 """


class NotesRegardingImpairmentLossTextBlock_edjp_NotesRegardingProvisionOfReservesIncludedInCostOfSales_consolidated_Q2(SQLModel):
    """ 減損損失に関する注記 [テキストブロック] """

    current_ytd_duration: IxNonNumericPublic = Field(default=None, description="当年度期初から当日まで")
    """ 当年度期初から当日まで """


class DescriptionOfFactorsWhichLedToRecognitionOfGainOnBargainPurchaseTextBlock_edjp_NotesSegmentInformationEtcConsolidatedFinancialStatements_consolidated_FY(SQLModel):
    """ 報告セグメントごとの負ののれん発生益を認識する要因となった事象の概要 [テキストブロック] """

    current_year_duration: IxNonNumericPublic = Field(default=None, description="当年度会計期間")
    """ 当年度会計期間 """


class DescriptionOfReportableSegmentsTextBlock_edjp_NotesSegmentInformationEtcConsolidatedFinancialStatements_consolidated_FY(SQLModel):
    """ 報告セグメントの概要 [テキストブロック] """

    current_year_duration: IxNonNumericPublic = Field(default=None, description="当年度会計期間")
    """ 当年度会計期間 """


class ExplanationOfMeasurementsOfSalesProfitLossAssetLiabilityAndOtherItemsForEachReportableSegmentTextBlock_edjp_NotesSegmentInformationEtcConsolidatedFinancialStatements_consolidated_FY(SQLModel):
    """ 報告セグメントごとの売上高、利益又は損失、資産、負債その他の項目の金額の算定方法 [テキストブロック] """

    current_year_duration: IxNonNumericPublic = Field(default=None, description="当年度会計期間")
    """ 当年度会計期間 """


class FootnotesRegardingSegmentInformationTableTextBlock_edjp_NotesSegmentInformationEtcConsolidatedFinancialStatements_consolidated_FY(SQLModel):
    """ セグメント表の脚注 [テキストブロック] """

    current_year_duration: IxNonNumericPublic = Field(default=None, description="当年度会計期間")
    """ 当年度会計期間 """
    prior1_year_duration: IxNonNumericPublic = Field(default=None, description="前々年度会計期間")
    """ 前々年度会計期間 """


class InformationForEachOfMainCustomersTextBlock_edjp_NotesSegmentInformationEtcConsolidatedFinancialStatements_consolidated_FY(SQLModel):
    """ 主要な顧客ごとの情報 [テキストブロック] """

    current_year_duration: IxNonNumericPublic = Field(default=None, description="当年度会計期間")
    """ 当年度会計期間 """
    prior1_year_duration: IxNonNumericPublic = Field(default=None, description="前々年度会計期間")
    """ 前々年度会計期間 """


class InformationForEachProductOrServiceTextBlock_edjp_NotesSegmentInformationEtcConsolidatedFinancialStatements_consolidated_FY(SQLModel):
    """ 製品及びサービスごとの情報 [テキストブロック] """

    current_year_duration: IxNonNumericPublic = Field(default=None, description="当年度会計期間")
    """ 当年度会計期間 """
    prior1_year_duration: IxNonNumericPublic = Field(default=None, description="前々年度会計期間")
    """ 前々年度会計期間 """


class NotesSegmentInformationEtcConsolidatedFinancialStatementsTextBlock_edjp_NotesSegmentInformationEtcConsolidatedFinancialStatements_consolidated_FY(SQLModel):
    """ セグメント情報等、連結財務諸表 [テキストブロック] """

    current_year_duration: IxNonNumericPublic = Field(default=None, description="当年度会計期間")
    """ 当年度会計期間 """


class PropertyPlantAndEquipmentInformationForEachRegionTextBlock_edjp_NotesSegmentInformationEtcConsolidatedFinancialStatements_consolidated_FY(SQLModel):
    """ 有形固定資産、地域ごとの情報 [テキストブロック] """

    current_year_duration: IxNonNumericPublic = Field(default=None, description="当年度会計期間")
    """ 当年度会計期間 """
    prior1_year_duration: IxNonNumericPublic = Field(default=None, description="前々年度会計期間")
    """ 前々年度会計期間 """


class RevenuesFromExternalCustomersInformationForEachRegionTextBlock_edjp_NotesSegmentInformationEtcConsolidatedFinancialStatements_consolidated_FY(SQLModel):
    """ 売上高、地域ごとの情報 [テキストブロック] """

    current_year_duration: IxNonNumericPublic = Field(default=None, description="当年度会計期間")
    """ 当年度会計期間 """
    prior1_year_duration: IxNonNumericPublic = Field(default=None, description="前々年度会計期間")
    """ 前々年度会計期間 """


class DescriptionOfFactThatCompanysBusinessComprisesSingleSegment_edjp_NotesSegmentInformationEtcFinancialStatements_Nonconsolidated_FY(SQLModel):
    """ 単一セグメントである旨 """

    current_year_duration_non_consolidated_member: IxNonNumericPublic = Field(default=None, description="当年度会計期間_非連結又は個別")
    """ 当年度会計期間_非連結又は個別 """


class NotesSegmentInformationEtcFinancialStatementsTextBlock_edjp_NotesSegmentInformationEtcFinancialStatements_Nonconsolidated_FY(SQLModel):
    """ セグメント情報等、財務諸表 [テキストブロック] """

    current_year_duration: IxNonNumericPublic = Field(default=None, description="当年度会計期間")
    """ 当年度会計期間 """


class DescriptionOfFactThatCompanysBusinessComprisesSingleSegment_edjp_NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatements_consolidated_Q1(SQLModel):
    """ 単一セグメントである旨 """

    current_ytd_duration: IxNonNumericPublic = Field(default=None, description="当年度期初から当日まで")
    """ 当年度期初から当日まで """


class DisclosureOfChangesEtcInReportableSegmentsTextBlock_edjp_NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatements_consolidated_Q1(SQLModel):
    """ 報告セグメントの変更等に関する事項 [テキストブロック] """

    current_ytd_duration: IxNonNumericPublic = Field(default=None, description="当年度期初から当日まで")
    """ 当年度期初から当日まで """


class FootnotesRegardingSegmentInformationTableTextBlock_edjp_NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatements_consolidated_Q1(SQLModel):
    """ セグメント表の脚注 [テキストブロック] """

    current_ytd_duration: IxNonNumericPublic = Field(default=None, description="当年度期初から当日まで")
    """ 当年度期初から当日まで """
    prior1_ytd_duration: IxNonNumericPublic = Field(default=None, description="前々年度期初から当日まで")
    """ 前々年度期初から当日まで """


class NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatementsTextBlock_edjp_NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatements_consolidated_Q1(SQLModel):
    """ セグメント情報等、四半期連結財務諸表 [テキストブロック] """

    current_ytd_duration: IxNonNumericPublic = Field(default=None, description="当年度期初から当日まで")
    """ 当年度期初から当日まで """


class DescriptionOfFactThatCompanysBusinessComprisesSingleSegment_edjp_NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatements_consolidated_Q2(SQLModel):
    """ 単一セグメントである旨 """

    current_ytd_duration: IxNonNumericPublic = Field(default=None, description="当年度期初から当日まで")
    """ 当年度期初から当日まで """
    prior1_ytd_duration: IxNonNumericPublic = Field(default=None, description="前々年度期初から当日まで")
    """ 前々年度期初から当日まで """


class DescriptionOfNatureOfDifferencesBetweenProfitLossOfReportableSegmentsTotalAndQuarterlyFinancialStatementsTextBlock_edjp_NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatements_consolidated_Q2(SQLModel):
    """ 報告セグメントごとの利益又は損失の金額の合計額と四半期損益計算書計上額との差額及び当該差額の主な内容（差異調整に関する事項） [テキストブロック] """

    current_ytd_duration: IxNonNumericPublic = Field(default=None, description="当年度期初から当日まで")
    """ 当年度期初から当日まで """
    prior1_ytd_duration: IxNonNumericPublic = Field(default=None, description="前々年度期初から当日まで")
    """ 前々年度期初から当日まで """


class DisclosureOfChangesEtcInReportableSegmentsTextBlock_edjp_NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatements_consolidated_Q2(SQLModel):
    """ 報告セグメントの変更等に関する事項 [テキストブロック] """

    current_ytd_duration: IxNonNumericPublic = Field(default=None, description="当年度期初から当日まで")
    """ 当年度期初から当日まで """
    prior1_ytd_duration: IxNonNumericPublic = Field(default=None, description="前々年度期初から当日まで")
    """ 前々年度期初から当日まで """


class FootnotesRegardingSegmentInformationTableTextBlock_edjp_NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatements_consolidated_Q2(SQLModel):
    """ セグメント表の脚注 [テキストブロック] """

    current_ytd_duration: IxNonNumericPublic = Field(default=None, description="当年度期初から当日まで")
    """ 当年度期初から当日まで """
    prior1_ytd_duration: IxNonNumericPublic = Field(default=None, description="前々年度期初から当日まで")
    """ 前々年度期初から当日まで """


class InformationAboutAssetsForEachReportableSegmentTextBlock_edjp_NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatements_consolidated_Q2(SQLModel):
    """ 報告セグメントごとの資産に関する情報 [テキストブロック] """

    current_ytd_duration: IxNonNumericPublic = Field(default=None, description="当年度期初から当日まで")
    """ 当年度期初から当日まで """
    prior1_ytd_duration: IxNonNumericPublic = Field(default=None, description="前々年度期初から当日まで")
    """ 前々年度期初から当日まで """


class InformationAboutImpairmentLossOfNonCurrentAssetsOrGoodwillEtcForEachReportableSegmentTextBlock_edjp_NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatements_consolidated_Q2(SQLModel):
    """ 報告セグメントごとの固定資産の減損損失又はのれん等に関する情報 [テキストブロック] """

    current_ytd_duration: IxNonNumericPublic = Field(default=None, description="当年度期初から当日まで")
    """ 当年度期初から当日まで """
    prior1_ytd_duration: IxNonNumericPublic = Field(default=None, description="前々年度期初から当日まで")
    """ 前々年度期初から当日まで """


class NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatementsTextBlock_edjp_NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatements_consolidated_Q2(SQLModel):
    """ セグメント情報等、四半期連結財務諸表 [テキストブロック] """

    current_ytd_duration: IxNonNumericPublic = Field(default=None, description="当年度期初から当日まで")
    """ 当年度期初から当日まで """


class RevenuesFromExternalCustomersInformationForEachRegionTextBlock_edjp_NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatements_consolidated_Q2(SQLModel):
    """ 売上高、地域ごとの情報 [テキストブロック] """

    current_ytd_duration: IxNonNumericPublic = Field(default=None, description="当年度期初から当日まで")
    """ 当年度期初から当日まで """
    prior1_ytd_duration: IxNonNumericPublic = Field(default=None, description="前々年度期初から当日まで")
    """ 前々年度期初から当日まで """


class DescriptionOfFactThatCompanysBusinessComprisesSingleSegment_edjp_NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatements_consolidated_Q3(SQLModel):
    """ 単一セグメントである旨 """

    current_ytd_duration: IxNonNumericPublic = Field(default=None, description="当年度期初から当日まで")
    """ 当年度期初から当日まで """


class DescriptionOfNatureOfDifferencesBetweenProfitLossOfReportableSegmentsTotalAndQuarterlyFinancialStatementsTextBlock_edjp_NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatements_consolidated_Q3(SQLModel):
    """ 報告セグメントごとの利益又は損失の金額の合計額と四半期損益計算書計上額との差額及び当該差額の主な内容（差異調整に関する事項） [テキストブロック] """

    current_ytd_duration: IxNonNumericPublic = Field(default=None, description="当年度期初から当日まで")
    """ 当年度期初から当日まで """
    prior1_ytd_duration: IxNonNumericPublic = Field(default=None, description="前々年度期初から当日まで")
    """ 前々年度期初から当日まで """


class DisclosureOfChangesEtcInReportableSegmentsTextBlock_edjp_NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatements_consolidated_Q3(SQLModel):
    """ 報告セグメントの変更等に関する事項 [テキストブロック] """

    current_ytd_duration: IxNonNumericPublic = Field(default=None, description="当年度期初から当日まで")
    """ 当年度期初から当日まで """


class FootnotesRegardingSegmentInformationTableTextBlock_edjp_NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatements_consolidated_Q3(SQLModel):
    """ セグメント表の脚注 [テキストブロック] """

    current_ytd_duration: IxNonNumericPublic = Field(default=None, description="当年度期初から当日まで")
    """ 当年度期初から当日まで """
    prior1_ytd_duration: IxNonNumericPublic = Field(default=None, description="前々年度期初から当日まで")
    """ 前々年度期初から当日まで """


class InformationAboutImpairmentLossOfNonCurrentAssetsOrGoodwillEtcForEachReportableSegmentTextBlock_edjp_NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatements_consolidated_Q3(SQLModel):
    """ 報告セグメントごとの固定資産の減損損失又はのれん等に関する情報 [テキストブロック] """

    current_ytd_duration: IxNonNumericPublic = Field(default=None, description="当年度期初から当日まで")
    """ 当年度期初から当日まで """
    prior1_ytd_duration: IxNonNumericPublic = Field(default=None, description="前々年度期初から当日まで")
    """ 前々年度期初から当日まで """


class NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatementsTextBlock_edjp_NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatements_consolidated_Q3(SQLModel):
    """ セグメント情報等、四半期連結財務諸表 [テキストブロック] """

    current_ytd_duration: IxNonNumericPublic = Field(default=None, description="当年度期初から当日まで")
    """ 当年度期初から当日まで """


class DescriptionOfFactThatCompanysBusinessComprisesSingleSegment_edjp_NotesSegmentInformationEtcQuarterlyFinancialStatements_Nonconsolidated_Q1(SQLModel):
    """ 単一セグメントである旨 """

    current_ytd_duration_non_consolidated_member: IxNonNumericPublic = Field(default=None, description="当年度期初から当日まで_非連結又は個別")
    """ 当年度期初から当日まで_非連結又は個別 """
    prior1_ytd_duration_non_consolidated_member: IxNonNumericPublic = Field(default=None, description="前々年度期初から当日まで_非連結又は個別")
    """ 前々年度期初から当日まで_非連結又は個別 """


class NotesSegmentInformationEtcQuarterlyFinancialStatementsTextBlock_edjp_NotesSegmentInformationEtcQuarterlyFinancialStatements_Nonconsolidated_Q1(SQLModel):
    """ セグメント情報等、四半期財務諸表 [テキストブロック] """

    current_ytd_duration: IxNonNumericPublic = Field(default=None, description="当年度期初から当日まで")
    """ 当年度期初から当日まで """


class FootnotesRegardingSegmentInformationTableTextBlock_edjp_NotesSegmentInformationEtcQuarterlyFinancialStatements_Nonconsolidated_Q2(SQLModel):
    """ セグメント表の脚注 [テキストブロック] """

    current_ytd_duration_non_consolidated_member: IxNonNumericPublic = Field(default=None, description="当年度期初から当日まで_非連結又は個別")
    """ 当年度期初から当日まで_非連結又は個別 """
    prior1_ytd_duration_non_consolidated_member: IxNonNumericPublic = Field(default=None, description="前々年度期初から当日まで_非連結又は個別")
    """ 前々年度期初から当日まで_非連結又は個別 """


class InformationAboutImpairmentLossOfNonCurrentAssetsOrGoodwillEtcForEachReportableSegmentTextBlock_edjp_NotesSegmentInformationEtcQuarterlyFinancialStatements_Nonconsolidated_Q2(SQLModel):
    """ 報告セグメントごとの固定資産の減損損失又はのれん等に関する情報 [テキストブロック] """

    current_ytd_duration_non_consolidated_member: IxNonNumericPublic = Field(default=None, description="当年度期初から当日まで_非連結又は個別")
    """ 当年度期初から当日まで_非連結又は個別 """
    prior1_ytd_duration_non_consolidated_member: IxNonNumericPublic = Field(default=None, description="前々年度期初から当日まで_非連結又は個別")
    """ 前々年度期初から当日まで_非連結又は個別 """


class NotesSegmentInformationEtcQuarterlyFinancialStatementsTextBlock_edjp_NotesSegmentInformationEtcQuarterlyFinancialStatements_Nonconsolidated_Q2(SQLModel):
    """ セグメント情報等、四半期財務諸表 [テキストブロック] """

    current_ytd_duration: IxNonNumericPublic = Field(default=None, description="当年度期初から当日まで")
    """ 当年度期初から当日まで """


class QuarterlyBalanceSheetTextBlock_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q1(SQLModel):
    """ 四半期貸借対照表 [テキストブロック] """

    current_ytd_duration: IxNonNumericPublic = Field(default=None, description="当年度期初から当日まで")
    """ 当年度期初から当日まで """


class AccountingStandardsDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q1(SQLModel):
    """ 会計基準、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class AmendmentFlagDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q1(SQLModel):
    """ 訂正の有無、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class CabinetOfficeOrdinanceDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q1(SQLModel):
    """ 府令、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class ComparativePeriodEndDateDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q1(SQLModel):
    """ 比較対象会計期間終了日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class CurrentFiscalYearEndDateDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q1(SQLModel):
    """ 当事業年度終了日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class CurrentFiscalYearStartDateDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q1(SQLModel):
    """ 当事業年度開始日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class CurrentPeriodEndDateDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q1(SQLModel):
    """ 当会計期間終了日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class DocumentTypeDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q1(SQLModel):
    """ 様式、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class EDINETCodeDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q1(SQLModel):
    """ EDINETコード、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class EndDateOfQuarterlyOrSemiAnnualPeriodOfNextFiscalYearDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q1(SQLModel):
    """ 次の四半期又は中間期の会計期間終了日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class FilerNameInEnglishDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q1(SQLModel):
    """ 提出者名（英語表記）、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class FilerNameInJapaneseDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q1(SQLModel):
    """ 提出者名（日本語表記）、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class FundCodeDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q1(SQLModel):
    """ ファンドコード、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class FundNameInEnglishDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q1(SQLModel):
    """ ファンド名称（英語表記）、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class FundNameInJapaneseDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q1(SQLModel):
    """ ファンド名称（日本語表記）、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class IdentificationOfDocumentSubjectToAmendmentDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q1(SQLModel):
    """ 訂正対象書類の書類管理番号、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class IndustryCodeWhenConsolidatedFinancialStatementsArePreparedInAccordanceWithIndustrySpecificRegulationsDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q1(SQLModel):
    """ 別記事業（連結）、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class IndustryCodeWhenFinancialStatementsArePreparedInAccordanceWithIndustrySpecificRegulationsDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q1(SQLModel):
    """ 別記事業（個別）、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class NextFiscalYearStartDateDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q1(SQLModel):
    """ 次の事業年度開始日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class PreviousFiscalYearEndDateDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q1(SQLModel):
    """ 前事業年度終了日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class PreviousFiscalYearStartDateDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q1(SQLModel):
    """ 前事業年度開始日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class ReportAmendmentFlagDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q1(SQLModel):
    """ 記載事項訂正のフラグ、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class SecurityCodeDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q1(SQLModel):
    """ 証券コード、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class TypeOfCurrentPeriodDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q1(SQLModel):
    """ 当会計期間の種類、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class WhetherConsolidatedFinancialStatementsArePreparedDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q1(SQLModel):
    """ 連結決算の有無、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class XBRLAmendmentFlagDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q1(SQLModel):
    """ XBRL訂正のフラグ、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class QuarterlyBalanceSheetTextBlock_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q2(SQLModel):
    """ 四半期貸借対照表 [テキストブロック] """

    current_ytd_duration: IxNonNumericPublic = Field(default=None, description="当年度期初から当日まで")
    """ 当年度期初から当日まで """


class AccountingStandardsDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q2(SQLModel):
    """ 会計基準、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class AmendmentFlagDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q2(SQLModel):
    """ 訂正の有無、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class CabinetOfficeOrdinanceDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q2(SQLModel):
    """ 府令、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class ComparativePeriodEndDateDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q2(SQLModel):
    """ 比較対象会計期間終了日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class CurrentFiscalYearEndDateDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q2(SQLModel):
    """ 当事業年度終了日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class CurrentFiscalYearStartDateDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q2(SQLModel):
    """ 当事業年度開始日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class CurrentPeriodEndDateDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q2(SQLModel):
    """ 当会計期間終了日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class DocumentTypeDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q2(SQLModel):
    """ 様式、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class EDINETCodeDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q2(SQLModel):
    """ EDINETコード、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class EndDateOfQuarterlyOrSemiAnnualPeriodOfNextFiscalYearDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q2(SQLModel):
    """ 次の四半期又は中間期の会計期間終了日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class FilerNameInEnglishDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q2(SQLModel):
    """ 提出者名（英語表記）、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class FilerNameInJapaneseDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q2(SQLModel):
    """ 提出者名（日本語表記）、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class FundCodeDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q2(SQLModel):
    """ ファンドコード、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class FundNameInEnglishDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q2(SQLModel):
    """ ファンド名称（英語表記）、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class FundNameInJapaneseDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q2(SQLModel):
    """ ファンド名称（日本語表記）、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class IdentificationOfDocumentSubjectToAmendmentDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q2(SQLModel):
    """ 訂正対象書類の書類管理番号、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class IndustryCodeWhenConsolidatedFinancialStatementsArePreparedInAccordanceWithIndustrySpecificRegulationsDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q2(SQLModel):
    """ 別記事業（連結）、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class IndustryCodeWhenFinancialStatementsArePreparedInAccordanceWithIndustrySpecificRegulationsDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q2(SQLModel):
    """ 別記事業（個別）、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class NextFiscalYearStartDateDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q2(SQLModel):
    """ 次の事業年度開始日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class PreviousFiscalYearEndDateDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q2(SQLModel):
    """ 前事業年度終了日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class PreviousFiscalYearStartDateDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q2(SQLModel):
    """ 前事業年度開始日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class ReportAmendmentFlagDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q2(SQLModel):
    """ 記載事項訂正のフラグ、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class SecurityCodeDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q2(SQLModel):
    """ 証券コード、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class TypeOfCurrentPeriodDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q2(SQLModel):
    """ 当会計期間の種類、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class WhetherConsolidatedFinancialStatementsArePreparedDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q2(SQLModel):
    """ 連結決算の有無、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class XBRLAmendmentFlagDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q2(SQLModel):
    """ XBRL訂正のフラグ、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class QuarterlyConsolidatedBalanceSheetTextBlock_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q1(SQLModel):
    """ 四半期連結貸借対照表 [テキストブロック] """

    current_ytd_duration: IxNonNumericPublic = Field(default=None, description="当年度期初から当日まで")
    """ 当年度期初から当日まで """


class AccountingStandardsDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q1(SQLModel):
    """ 会計基準、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class AmendmentFlagDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q1(SQLModel):
    """ 訂正の有無、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class CabinetOfficeOrdinanceDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q1(SQLModel):
    """ 府令、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class ComparativePeriodEndDateDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q1(SQLModel):
    """ 比較対象会計期間終了日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class CurrentFiscalYearEndDateDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q1(SQLModel):
    """ 当事業年度終了日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class CurrentFiscalYearStartDateDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q1(SQLModel):
    """ 当事業年度開始日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class CurrentPeriodEndDateDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q1(SQLModel):
    """ 当会計期間終了日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class DocumentTypeDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q1(SQLModel):
    """ 様式、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class EDINETCodeDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q1(SQLModel):
    """ EDINETコード、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class EndDateOfQuarterlyOrSemiAnnualPeriodOfNextFiscalYearDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q1(SQLModel):
    """ 次の四半期又は中間期の会計期間終了日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class FilerNameInEnglishDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q1(SQLModel):
    """ 提出者名（英語表記）、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class FilerNameInJapaneseDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q1(SQLModel):
    """ 提出者名（日本語表記）、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class FundCodeDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q1(SQLModel):
    """ ファンドコード、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class FundNameInEnglishDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q1(SQLModel):
    """ ファンド名称（英語表記）、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class FundNameInJapaneseDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q1(SQLModel):
    """ ファンド名称（日本語表記）、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class IdentificationOfDocumentSubjectToAmendmentDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q1(SQLModel):
    """ 訂正対象書類の書類管理番号、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class IndustryCodeWhenConsolidatedFinancialStatementsArePreparedInAccordanceWithIndustrySpecificRegulationsDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q1(SQLModel):
    """ 別記事業（連結）、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class IndustryCodeWhenFinancialStatementsArePreparedInAccordanceWithIndustrySpecificRegulationsDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q1(SQLModel):
    """ 別記事業（個別）、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class NextFiscalYearStartDateDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q1(SQLModel):
    """ 次の事業年度開始日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class PreviousFiscalYearEndDateDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q1(SQLModel):
    """ 前事業年度終了日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class PreviousFiscalYearStartDateDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q1(SQLModel):
    """ 前事業年度開始日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class ReportAmendmentFlagDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q1(SQLModel):
    """ 記載事項訂正のフラグ、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class SecurityCodeDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q1(SQLModel):
    """ 証券コード、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class TypeOfCurrentPeriodDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q1(SQLModel):
    """ 当会計期間の種類、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class WhetherConsolidatedFinancialStatementsArePreparedDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q1(SQLModel):
    """ 連結決算の有無、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class XBRLAmendmentFlagDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q1(SQLModel):
    """ XBRL訂正のフラグ、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class QuarterlyConsolidatedBalanceSheetTextBlock_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q2(SQLModel):
    """ 四半期連結貸借対照表 [テキストブロック] """

    current_ytd_duration: IxNonNumericPublic = Field(default=None, description="当年度期初から当日まで")
    """ 当年度期初から当日まで """


class AccountingStandardsDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q2(SQLModel):
    """ 会計基準、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class AmendmentFlagDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q2(SQLModel):
    """ 訂正の有無、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class CabinetOfficeOrdinanceDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q2(SQLModel):
    """ 府令、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class ComparativePeriodEndDateDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q2(SQLModel):
    """ 比較対象会計期間終了日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class CurrentFiscalYearEndDateDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q2(SQLModel):
    """ 当事業年度終了日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class CurrentFiscalYearStartDateDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q2(SQLModel):
    """ 当事業年度開始日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class CurrentPeriodEndDateDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q2(SQLModel):
    """ 当会計期間終了日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class DocumentTypeDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q2(SQLModel):
    """ 様式、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class EDINETCodeDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q2(SQLModel):
    """ EDINETコード、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class EndDateOfQuarterlyOrSemiAnnualPeriodOfNextFiscalYearDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q2(SQLModel):
    """ 次の四半期又は中間期の会計期間終了日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class FilerNameInEnglishDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q2(SQLModel):
    """ 提出者名（英語表記）、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class FilerNameInJapaneseDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q2(SQLModel):
    """ 提出者名（日本語表記）、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class FundCodeDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q2(SQLModel):
    """ ファンドコード、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class FundNameInEnglishDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q2(SQLModel):
    """ ファンド名称（英語表記）、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class FundNameInJapaneseDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q2(SQLModel):
    """ ファンド名称（日本語表記）、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class IdentificationOfDocumentSubjectToAmendmentDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q2(SQLModel):
    """ 訂正対象書類の書類管理番号、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class IndustryCodeWhenConsolidatedFinancialStatementsArePreparedInAccordanceWithIndustrySpecificRegulationsDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q2(SQLModel):
    """ 別記事業（連結）、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class IndustryCodeWhenFinancialStatementsArePreparedInAccordanceWithIndustrySpecificRegulationsDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q2(SQLModel):
    """ 別記事業（個別）、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class NextFiscalYearStartDateDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q2(SQLModel):
    """ 次の事業年度開始日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class PreviousFiscalYearEndDateDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q2(SQLModel):
    """ 前事業年度終了日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class PreviousFiscalYearStartDateDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q2(SQLModel):
    """ 前事業年度開始日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class ReportAmendmentFlagDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q2(SQLModel):
    """ 記載事項訂正のフラグ、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class SecurityCodeDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q2(SQLModel):
    """ 証券コード、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class TypeOfCurrentPeriodDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q2(SQLModel):
    """ 当会計期間の種類、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class WhetherConsolidatedFinancialStatementsArePreparedDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q2(SQLModel):
    """ 連結決算の有無、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class XBRLAmendmentFlagDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q2(SQLModel):
    """ XBRL訂正のフラグ、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class QuarterlyConsolidatedBalanceSheetTextBlock_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q3(SQLModel):
    """ 四半期連結貸借対照表 [テキストブロック] """

    current_ytd_duration: IxNonNumericPublic = Field(default=None, description="当年度期初から当日まで")
    """ 当年度期初から当日まで """


class AccountingStandardsDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q3(SQLModel):
    """ 会計基準、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class AmendmentFlagDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q3(SQLModel):
    """ 訂正の有無、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class CabinetOfficeOrdinanceDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q3(SQLModel):
    """ 府令、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class ComparativePeriodEndDateDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q3(SQLModel):
    """ 比較対象会計期間終了日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class CurrentFiscalYearEndDateDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q3(SQLModel):
    """ 当事業年度終了日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class CurrentFiscalYearStartDateDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q3(SQLModel):
    """ 当事業年度開始日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class CurrentPeriodEndDateDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q3(SQLModel):
    """ 当会計期間終了日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class DocumentTypeDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q3(SQLModel):
    """ 様式、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class EDINETCodeDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q3(SQLModel):
    """ EDINETコード、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class EndDateOfQuarterlyOrSemiAnnualPeriodOfNextFiscalYearDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q3(SQLModel):
    """ 次の四半期又は中間期の会計期間終了日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class FilerNameInEnglishDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q3(SQLModel):
    """ 提出者名（英語表記）、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class FilerNameInJapaneseDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q3(SQLModel):
    """ 提出者名（日本語表記）、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class FundCodeDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q3(SQLModel):
    """ ファンドコード、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class FundNameInEnglishDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q3(SQLModel):
    """ ファンド名称（英語表記）、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class FundNameInJapaneseDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q3(SQLModel):
    """ ファンド名称（日本語表記）、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class IdentificationOfDocumentSubjectToAmendmentDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q3(SQLModel):
    """ 訂正対象書類の書類管理番号、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class IndustryCodeWhenConsolidatedFinancialStatementsArePreparedInAccordanceWithIndustrySpecificRegulationsDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q3(SQLModel):
    """ 別記事業（連結）、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class IndustryCodeWhenFinancialStatementsArePreparedInAccordanceWithIndustrySpecificRegulationsDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q3(SQLModel):
    """ 別記事業（個別）、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class NextFiscalYearStartDateDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q3(SQLModel):
    """ 次の事業年度開始日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class PreviousFiscalYearEndDateDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q3(SQLModel):
    """ 前事業年度終了日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class PreviousFiscalYearStartDateDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q3(SQLModel):
    """ 前事業年度開始日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class ReportAmendmentFlagDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q3(SQLModel):
    """ 記載事項訂正のフラグ、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class SecurityCodeDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q3(SQLModel):
    """ 証券コード、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class TypeOfCurrentPeriodDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q3(SQLModel):
    """ 当会計期間の種類、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class WhetherConsolidatedFinancialStatementsArePreparedDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q3(SQLModel):
    """ 連結決算の有無、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class XBRLAmendmentFlagDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q3(SQLModel):
    """ XBRL訂正のフラグ、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class QuarterlyConsolidatedStatementOfCashFlowsTextBlock_edjp_QuarterlyConsolidatedStatementOfCashFlows_consolidated_Q2(SQLModel):
    """ 四半期連結キャッシュ・フロー計算書 [テキストブロック] """

    current_ytd_duration: IxNonNumericPublic = Field(default=None, description="当年度期初から当日まで")
    """ 当年度期初から当日まで """


class QuarterlyConsolidatedStatementOfCashFlowsTextBlock_edjp_QuarterlyConsolidatedStatementOfCashFlows_consolidated_Q3(SQLModel):
    """ 四半期連結キャッシュ・フロー計算書 [テキストブロック] """

    current_ytd_duration: IxNonNumericPublic = Field(default=None, description="当年度期初から当日まで")
    """ 当年度期初から当日まで """


class QuarterlyStatementOfCashFlowsTextBlock_edjp_QuarterlyStatementOfCashFlows_Nonconsolidated_Q2(SQLModel):
    """ 四半期キャッシュ・フロー計算書 [テキストブロック] """

    current_ytd_duration: IxNonNumericPublic = Field(default=None, description="当年度期初から当日まで")
    """ 当年度期初から当日まで """


class StatementOfCashFlowsTextBlock_edjp_StatementOfCashFlows_Nonconsolidated_FY(SQLModel):
    """ キャッシュ・フロー計算書 [テキストブロック] """

    current_year_duration: IxNonNumericPublic = Field(default=None, description="当年度会計期間")
    """ 当年度会計期間 """


class StatementOfChangesInEquityTextBlock_edjp_StatementOfChangesInEquity_Nonconsolidated_FY(SQLModel):
    """ 株主資本等変動計算書 [テキストブロック] """

    current_year_duration: IxNonNumericPublic = Field(default=None, description="当年度会計期間")
    """ 当年度会計期間 """


class StatementOfChangesInEquityTextBlock_edjp_StatementOfChangesInEquity_consolidated_FY(SQLModel):
    """ 株主資本等変動計算書 [テキストブロック] """

    current_year_duration: IxNonNumericPublic = Field(default=None, description="当年度会計期間")
    """ 当年度会計期間 """


class StatementOfIncomeTextBlock_edjp_StatementOfIncome_Nonconsolidated_FY(SQLModel):
    """ 損益計算書 [テキストブロック] """

    current_year_duration: IxNonNumericPublic = Field(default=None, description="当年度会計期間")
    """ 当年度会計期間 """


class StatementOfIncomeTextBlock_edjp_StatementOfIncome_consolidated_FY(SQLModel):
    """ 損益計算書 [テキストブロック] """

    current_year_duration: IxNonNumericPublic = Field(default=None, description="当年度会計期間")
    """ 当年度会計期間 """


class YearToQuarterEndConsolidatedStatementOfComprehensiveIncomeTextBlock_edjp_YearToQuarterEndConsolidatedStatementOfComprehensiveIncome_consolidated_Q1(SQLModel):
    """ 四半期連結累計期間、四半期連結包括利益計算書 [テキストブロック] """

    current_ytd_duration: IxNonNumericPublic = Field(default=None, description="当年度期初から当日まで")
    """ 当年度期初から当日まで """


class DescriptionOfFactThatCompanysBusinessComprisesSingleSegment_edjp_YearToQuarterEndConsolidatedStatementOfComprehensiveIncome_consolidated_Q2(SQLModel):
    """ 単一セグメントである旨 """

    current_ytd_duration: IxNonNumericPublic = Field(default=None, description="当年度期初から当日まで")
    """ 当年度期初から当日まで """
    prior1_ytd_duration: IxNonNumericPublic = Field(default=None, description="前々年度期初から当日まで")
    """ 前々年度期初から当日まで """


class MajorComponentsOfSellingGeneralAndAdministrativeExpensesTextBlock_edjp_YearToQuarterEndConsolidatedStatementOfComprehensiveIncome_consolidated_Q2(SQLModel):
    """ 主要な販売費及び一般管理費 [テキストブロック] """

    current_ytd_duration: IxNonNumericPublic = Field(default=None, description="当年度期初から当日まで")
    """ 当年度期初から当日まで """


class NotesRegardingGuaranteeObligationsTextBlock_edjp_YearToQuarterEndConsolidatedStatementOfComprehensiveIncome_consolidated_Q2(SQLModel):
    """ 保証債務の注記 [テキストブロック] """

    current_quarter_instant: IxNonNumericPublic = Field(default=None, description="当四半期時点")
    """ 当四半期時点 """


class NotesRegardingSharesAndBondsEtcOfUnconsolidatedSubsidiariesAndAssociatesTextBlock_edjp_YearToQuarterEndConsolidatedStatementOfComprehensiveIncome_consolidated_Q2(SQLModel):
    """ 非連結子会社及び関連会社の株式及び社債等 [テキストブロック] """

    current_quarter_instant: IxNonNumericPublic = Field(default=None, description="当四半期時点")
    """ 当四半期時点 """


class NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatementsTextBlock_edjp_YearToQuarterEndConsolidatedStatementOfComprehensiveIncome_consolidated_Q2(SQLModel):
    """ セグメント情報等、四半期連結財務諸表 [テキストブロック] """

    current_ytd_duration: IxNonNumericPublic = Field(default=None, description="当年度期初から当日まで")
    """ 当年度期初から当日まで """


class YearToQuarterEndConsolidatedStatementOfComprehensiveIncomeTextBlock_edjp_YearToQuarterEndConsolidatedStatementOfComprehensiveIncome_consolidated_Q2(SQLModel):
    """ 四半期連結累計期間、四半期連結包括利益計算書 [テキストブロック] """

    current_ytd_duration: IxNonNumericPublic = Field(default=None, description="当年度期初から当日まで")
    """ 当年度期初から当日まで """


class YearToQuarterEndConsolidatedStatementOfComprehensiveIncomeTextBlock_edjp_YearToQuarterEndConsolidatedStatementOfComprehensiveIncome_consolidated_Q3(SQLModel):
    """ 四半期連結累計期間、四半期連結包括利益計算書 [テキストブロック] """

    current_ytd_duration: IxNonNumericPublic = Field(default=None, description="当年度期初から当日まで")
    """ 当年度期初から当日まで """


class YearToQuarterEndConsolidatedStatementOfComprehensiveIncomeSingleStatementTextBlock_edjp_YearToQuarterEndConsolidatedStatementOfComprehensiveIncomeSingleStatement_consolidated_Q2(SQLModel):
    """ 四半期連結累計期間、四半期連結損益及び包括利益計算書 [テキストブロック] """

    current_ytd_duration: IxNonNumericPublic = Field(default=None, description="当年度期初から当日まで")
    """ 当年度期初から当日まで """


class YearToQuarterEndConsolidatedStatementOfIncomeTextBlock_edjp_YearToQuarterEndConsolidatedStatementOfIncome_consolidated_Q1(SQLModel):
    """ 四半期連結累計期間、四半期連結損益計算書 [テキストブロック] """

    current_ytd_duration: IxNonNumericPublic = Field(default=None, description="当年度期初から当日まで")
    """ 当年度期初から当日まで """


class YearToQuarterEndConsolidatedStatementOfIncomeTextBlock_edjp_YearToQuarterEndConsolidatedStatementOfIncome_consolidated_Q2(SQLModel):
    """ 四半期連結累計期間、四半期連結損益計算書 [テキストブロック] """

    current_ytd_duration: IxNonNumericPublic = Field(default=None, description="当年度期初から当日まで")
    """ 当年度期初から当日まで """


class YearToQuarterEndConsolidatedStatementOfIncomeTextBlock_edjp_YearToQuarterEndConsolidatedStatementOfIncome_consolidated_Q3(SQLModel):
    """ 四半期連結累計期間、四半期連結損益計算書 [テキストブロック] """

    current_ytd_duration: IxNonNumericPublic = Field(default=None, description="当年度期初から当日まで")
    """ 当年度期初から当日まで """


class YearToQuarterEndStatementOfIncomeTextBlock_edjp_YearToQuarterEndStatementOfIncome_Nonconsolidated_Q1(SQLModel):
    """ 四半期累計期間、四半期損益計算書 [テキストブロック] """

    current_ytd_duration: IxNonNumericPublic = Field(default=None, description="当年度期初から当日まで")
    """ 当年度期初から当日まで """


class YearToQuarterEndStatementOfIncomeTextBlock_edjp_YearToQuarterEndStatementOfIncome_Nonconsolidated_Q2(SQLModel):
    """ 四半期累計期間、四半期損益計算書 [テキストブロック] """

    current_ytd_duration: IxNonNumericPublic = Field(default=None, description="当年度期初から当日まで")
    """ 当年度期初から当日まで """


class ChangesBasedOnRevisionsOfAccountingStandard_edjp_FinancialReportSummary_consolidated_HY_specific_business(SQLModel):
    """ 会計基準等の改正に伴う会計方針の変更 """

    current_accumulated_q2_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間_連結_実績")
    """ 当年度期初から第２四半期間_連結_実績 """


class ChangesInAccountingEstimatesInterim_edjp_FinancialReportSummary_consolidated_HY_specific_business(SQLModel):
    """ 会計上の見積りの変更、中間期 """

    current_accumulated_q2_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間_連結_実績")
    """ 当年度期初から第２四半期間_連結_実績 """


class ChangesOtherThanOnesBasedOnRevisionsOfAccountingStandard_edjp_FinancialReportSummary_consolidated_HY_specific_business(SQLModel):
    """ 会計基準等の改正に伴う変更以外の会計方針の変更 """

    current_accumulated_q2_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間_連結_実績")
    """ 当年度期初から第２四半期間_連結_実績 """


class CompanyName_edjp_FinancialReportSummary_consolidated_HY_specific_business(SQLModel):
    """ 上場会社名 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class ConveningBriefingOfResults_edjp_FinancialReportSummary_consolidated_HY_specific_business(SQLModel):
    """ 決算説明会開催の有無、期中 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class CorrectionOfConsolidatedFinancialForecastInThisQuarter_edjp_FinancialReportSummary_consolidated_HY_specific_business(SQLModel):
    """ 直近に公表されている業績予想からの修正の有無、連結 """

    current_year_duration_consolidated_member_forecast_member: IxNonNumericPublic = Field(default=None, description="当年度会計期間_連結_予想")
    """ 当年度会計期間_連結_予想 """


class CorrectionOfDividendForecastInThisQuarter_edjp_FinancialReportSummary_consolidated_HY_specific_business(SQLModel):
    """ 直近に公表されている配当予想からの修正の有無 """

    current_year_duration_annual_member_non_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度会計期間_年間_非連結又は個別_実績")
    """ 当年度会計期間_年間_非連結又は個別_実績 """


class DividendPayableDateAsPlanned_edjp_FinancialReportSummary_consolidated_HY_specific_business(SQLModel):
    """ 配当支払開始予定日 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class DocumentName_edjp_FinancialReportSummary_consolidated_HY_specific_business(SQLModel):
    """ 文書名 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class FASFMemberMark_edjp_FinancialReportSummary_consolidated_HY_specific_business(SQLModel):
    """ 財務会計基準機構会員マーク """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class FilingDate_edjp_FinancialReportSummary_consolidated_HY_specific_business(SQLModel):
    """ 提出日 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class FiscalYearEnd_edjp_FinancialReportSummary_consolidated_HY_specific_business(SQLModel):
    """ 決算期 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class FukuokaStockExchange_edjp_FinancialReportSummary_consolidated_HY_specific_business(SQLModel):
    """ 福岡証券取引所 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class FukuokaStockExchangeEstablished_edjp_FinancialReportSummary_consolidated_HY_specific_business(SQLModel):
    """ 福岡証券取引所 既存市場 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class FukuokaStockExchangeOthers_edjp_FinancialReportSummary_consolidated_HY_specific_business(SQLModel):
    """ 福岡証券取引所 その他 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class FukuokaStockExchangeQBoard_edjp_FinancialReportSummary_consolidated_HY_specific_business(SQLModel):
    """ 福岡証券取引所 Q-Board """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class GeneralBusiness_edjp_FinancialReportSummary_consolidated_HY_specific_business(SQLModel):
    """ 一般事業会社 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class JapanSecuritiesDealersAssociation_edjp_FinancialReportSummary_consolidated_HY_specific_business(SQLModel):
    """ フェニックス """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class JapanSecuritiesDealersAssociationGreenSheet_edjp_FinancialReportSummary_consolidated_HY_specific_business(SQLModel):
    """ 日本証券業協会 フェニックス """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class NagoyaStockExchange_edjp_FinancialReportSummary_consolidated_HY_specific_business(SQLModel):
    """ 名古屋証券取引所 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class NagoyaStockExchange1stSection_edjp_FinancialReportSummary_consolidated_HY_specific_business(SQLModel):
    """ 名古屋証券取引所 プレミア """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class NagoyaStockExchange2ndSection_edjp_FinancialReportSummary_consolidated_HY_specific_business(SQLModel):
    """ 名古屋証券取引所 メイン """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class NagoyaStockExchangeCentrex_edjp_FinancialReportSummary_consolidated_HY_specific_business(SQLModel):
    """ 名古屋証券取引所 ネクスト """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class NagoyaStockExchangeOthers_edjp_FinancialReportSummary_consolidated_HY_specific_business(SQLModel):
    """ 名古屋証券取引所 その他 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class NameInquiries_edjp_FinancialReportSummary_consolidated_HY_specific_business(SQLModel):
    """ 氏名、問合せ先責任者 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class NameRepresentative_edjp_FinancialReportSummary_consolidated_HY_specific_business(SQLModel):
    """ 氏名、代表者 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class NotesForUsingForecastedInformationAndOthers_edjp_FinancialReportSummary_consolidated_HY_specific_business(SQLModel):
    """ 業績予想の適切な利用に関する説明、その他特記事項 """

    current_year_duration: IxNonNumericPublic = Field(default=None, description="当年度会計期間")
    """ 当年度会計期間 """


class NoteToChangesInAccountingPoliciesAccountingEstimatesAndRetrospectiveRestatementInterimConsolidated_edjp_FinancialReportSummary_consolidated_HY_specific_business(SQLModel):
    """ 会計方針の変更・会計上の見積りの変更・修正再表示に関する注記、中間期 """

    current_accumulated_q2_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間_連結_実績")
    """ 当年度期初から第２四半期間_連結_実績 """


class NoteToConsolidatedFinancialResults_edjp_FinancialReportSummary_consolidated_HY_specific_business(SQLModel):
    """ 連結業績に関する注記 """

    current_accumulated_q2_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間_連結_実績")
    """ 当年度期初から第２四半期間_連結_実績 """


class NoteToDividends_edjp_FinancialReportSummary_consolidated_HY_specific_business(SQLModel):
    """ 配当の状況に関する注記 """

    current_accumulated_q2_duration_annual_member_non_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間_年間_非連結又は個別_実績")
    """ 当年度期初から第２四半期間_年間_非連結又は個別_実績 """


class NoteToFinancialPositions_edjp_FinancialReportSummary_consolidated_HY_specific_business(SQLModel):
    """ 財政状態に関する注記 """

    current_accumulated_q2_instant_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点_連結_実績")
    """ 当年度期初から第２四半期間時点_連結_実績 """
    current_accumulated_q2_instant_non_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点_非連結又は個別_実績")
    """ 当年度期初から第２四半期間時点_非連結又は個別_実績 """


class NoteToFinancialResults_edjp_FinancialReportSummary_consolidated_HY_specific_business(SQLModel):
    """ 業績に関する注記 """

    current_accumulated_q2_duration_non_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間_非連結又は個別_実績")
    """ 当年度期初から第２四半期間_非連結又は個別_実績 """


class NoteToForecasts_edjp_FinancialReportSummary_consolidated_HY_specific_business(SQLModel):
    """ 業績予想に関する事項、注記 """

    current_year_duration_consolidated_member_forecast_member: IxNonNumericPublic = Field(default=None, description="当年度会計期間_連結_予想")
    """ 当年度会計期間_連結_予想 """
    current_year_duration_non_consolidated_member_forecast_member: IxNonNumericPublic = Field(default=None, description="当年度会計期間_非連結又は個別_予想")
    """ 当年度会計期間_非連結又は個別_予想 """


class NoteToFractionProcessingMethod_edjp_FinancialReportSummary_consolidated_HY_specific_business(SQLModel):
    """ 端数処理方法に関する注記 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class NoteToNumberOfIssuedAndOutstandingSharesCommonStock_edjp_FinancialReportSummary_consolidated_HY_specific_business(SQLModel):
    """ 発行済株式数（普通株式）に関する注記 """

    current_accumulated_q2_instant_non_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点_非連結又は個別_実績")
    """ 当年度期初から第２四半期間時点_非連結又は個別_実績 """


class NoteToOperatingResults_edjp_FinancialReportSummary_consolidated_HY_specific_business(SQLModel):
    """ 経営成績に関する注記 """

    current_accumulated_q2_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間_連結_実績")
    """ 当年度期初から第２四半期間_連結_実績 """
    current_accumulated_q2_duration_non_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間_非連結又は個別_実績")
    """ 当年度期初から第２四半期間_非連結又は個別_実績 """


class NoteToSignificantChangesInTheScopeOfConsolidationDuringThePeriod_edjp_FinancialReportSummary_consolidated_HY_specific_business(SQLModel):
    """ 期中における連結範囲の重要な変更に関する注記 """

    current_accumulated_q2_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間_連結_実績")
    """ 当年度期初から第２四半期間_連結_実績 """


class PreambleToForecasts_edjp_FinancialReportSummary_consolidated_HY_specific_business(SQLModel):
    """ 業績予想に関する事項 """

    current_year_duration_consolidated_member_forecast_member: IxNonNumericPublic = Field(default=None, description="当年度会計期間_連結_予想")
    """ 当年度会計期間_連結_予想 """
    current_year_duration_non_consolidated_member_forecast_member: IxNonNumericPublic = Field(default=None, description="当年度会計期間_非連結又は個別_予想")
    """ 当年度会計期間_非連結又は個別_予想 """


class RetrospectiveRestatementInterim_edjp_FinancialReportSummary_consolidated_HY_specific_business(SQLModel):
    """ 修正再表示、中間期 """

    current_accumulated_q2_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間_連結_実績")
    """ 当年度期初から第２四半期間_連結_実績 """


class SapporoStockExchange_edjp_FinancialReportSummary_consolidated_HY_specific_business(SQLModel):
    """ 札幌証券取引所 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class SapporoStockExchangeAmbitious_edjp_FinancialReportSummary_consolidated_HY_specific_business(SQLModel):
    """ 札幌証券取引所 アンビシャス """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class SapporoStockExchangeEstablished_edjp_FinancialReportSummary_consolidated_HY_specific_business(SQLModel):
    """ 札幌証券取引所 既存市場 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class SapporoStockExchangeOthers_edjp_FinancialReportSummary_consolidated_HY_specific_business(SQLModel):
    """ 札幌証券取引所 その他 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class SecuritiesCode_edjp_FinancialReportSummary_consolidated_HY_specific_business(SQLModel):
    """ コード番号 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class SemiAnnualStatementFilingDateAsPlanned_edjp_FinancialReportSummary_consolidated_HY_specific_business(SQLModel):
    """ 半期報告書提出予定日 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class SettingOfSpecificTransactionAccountBK_edjp_FinancialReportSummary_consolidated_HY_specific_business(SQLModel):
    """ 特定取引勘定設置の有無、銀行 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class SignificantChangesInTheScopeOfConsolidationDuringThePeriod_edjp_FinancialReportSummary_consolidated_HY_specific_business(SQLModel):
    """ 期中における連結範囲の重要な変更 """

    current_accumulated_q2_duration_consolidated_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間_連結_実績")
    """ 当年度期初から第２四半期間_連結_実績 """


class SpecificBusiness_edjp_FinancialReportSummary_consolidated_HY_specific_business(SQLModel):
    """ 特定事業会社 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class SupplementalMaterialOfResults_edjp_FinancialReportSummary_consolidated_HY_specific_business(SQLModel):
    """ 決算補足説明資料作成の有無、期中 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class TargetForBriefingOfResults_edjp_FinancialReportSummary_consolidated_HY_specific_business(SQLModel):
    """ 決算説明会の対象者 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class Tel_edjp_FinancialReportSummary_consolidated_HY_specific_business(SQLModel):
    """ TEL """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class TitleForForecasts_edjp_FinancialReportSummary_consolidated_HY_specific_business(SQLModel):
    """ 業績予想タイトル名称 """

    current_year_duration_consolidated_member_forecast_member: IxNonNumericPublic = Field(default=None, description="当年度会計期間_連結_予想")
    """ 当年度会計期間_連結_予想 """
    current_year_duration_non_consolidated_member_forecast_member: IxNonNumericPublic = Field(default=None, description="当年度会計期間_非連結又は個別_予想")
    """ 当年度会計期間_非連結又は個別_予想 """


class TitleInquiries_edjp_FinancialReportSummary_consolidated_HY_specific_business(SQLModel):
    """ 役職名、問合せ先責任者 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class TitleRepresentative_edjp_FinancialReportSummary_consolidated_HY_specific_business(SQLModel):
    """ 役職名、代表者 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class TokyoStockExchange_edjp_FinancialReportSummary_consolidated_HY_specific_business(SQLModel):
    """ 東京証券取引所 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class TokyoStockExchangeGrowth_edjp_FinancialReportSummary_consolidated_HY_specific_business(SQLModel):
    """ 東京証券取引所 グロース """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class TokyoStockExchangeOthers_edjp_FinancialReportSummary_consolidated_HY_specific_business(SQLModel):
    """ 東京証券取引所 その他 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class TokyoStockExchangePrime_edjp_FinancialReportSummary_consolidated_HY_specific_business(SQLModel):
    """ 東京証券取引所 プライム """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class TokyoStockExchangePROMarket_edjp_FinancialReportSummary_consolidated_HY_specific_business(SQLModel):
    """ 東京証券取引所 PRO Market """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class TokyoStockExchangeStandard_edjp_FinancialReportSummary_consolidated_HY_specific_business(SQLModel):
    """ 東京証券取引所 スタンダード """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class URL_edjp_FinancialReportSummary_consolidated_HY_specific_business(SQLModel):
    """ URL """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class WayOfGettingSupplementalMaterialOfResults_edjp_FinancialReportSummary_consolidated_HY_specific_business(SQLModel):
    """ 入手方法等、決算補足説明資料、期中 """

    current_accumulated_q2_instant: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間時点")
    """ 当年度期初から第２四半期間時点 """


class DescriptionOfReportableSegmentsTextBlock_edjp_NotesSegmentInformationEtcSemiAnnualConsolidatedFinancialStatements_consolidated_HY_specific_business(SQLModel):
    """ 報告セグメントの概要 [テキストブロック] """

    interim_duration: IxNonNumericPublic = Field(default=None, description="中間期間")
    """ 中間期間 """


class ExplanationOfMeasurementsOfSalesProfitLossAssetLiabilityAndOtherItemsForEachReportableSegmentTextBlock_edjp_NotesSegmentInformationEtcSemiAnnualConsolidatedFinancialStatements_consolidated_HY_specific_business(SQLModel):
    """ 報告セグメントごとの売上高、利益又は損失、資産、負債その他の項目の金額の算定方法 [テキストブロック] """

    interim_duration: IxNonNumericPublic = Field(default=None, description="中間期間")
    """ 中間期間 """


class FootnotesRegardingSegmentInformationTableTextBlock_edjp_NotesSegmentInformationEtcSemiAnnualConsolidatedFinancialStatements_consolidated_HY_specific_business(SQLModel):
    """ セグメント表の脚注 [テキストブロック] """

    interim_duration: IxNonNumericPublic = Field(default=None, description="中間期間")
    """ 中間期間 """
    prior1_interim_duration: IxNonNumericPublic = Field(default=None, description="前々中間期間")
    """ 前々中間期間 """


class InformationForEachOfMainCustomersTextBlock_edjp_NotesSegmentInformationEtcSemiAnnualConsolidatedFinancialStatements_consolidated_HY_specific_business(SQLModel):
    """ 主要な顧客ごとの情報 [テキストブロック] """

    interim_duration: IxNonNumericPublic = Field(default=None, description="中間期間")
    """ 中間期間 """
    prior1_interim_duration: IxNonNumericPublic = Field(default=None, description="前々中間期間")
    """ 前々中間期間 """


class InformationForEachProductOrServiceTextBlock_edjp_NotesSegmentInformationEtcSemiAnnualConsolidatedFinancialStatements_consolidated_HY_specific_business(SQLModel):
    """ 製品及びサービスごとの情報 [テキストブロック] """

    interim_duration: IxNonNumericPublic = Field(default=None, description="中間期間")
    """ 中間期間 """
    prior1_interim_duration: IxNonNumericPublic = Field(default=None, description="前々中間期間")
    """ 前々中間期間 """


class NotesSegmentInformationEtcSemiAnnualConsolidatedFinancialStatementsTextBlock_edjp_NotesSegmentInformationEtcSemiAnnualConsolidatedFinancialStatements_consolidated_HY_specific_business(SQLModel):
    """ セグメント情報等、中間連結財務諸表 [テキストブロック] """

    interim_duration: IxNonNumericPublic = Field(default=None, description="中間期間")
    """ 中間期間 """


class PropertyPlantAndEquipmentInformationForEachRegionTextBlock_edjp_NotesSegmentInformationEtcSemiAnnualConsolidatedFinancialStatements_consolidated_HY_specific_business(SQLModel):
    """ 有形固定資産、地域ごとの情報 [テキストブロック] """

    interim_duration: IxNonNumericPublic = Field(default=None, description="中間期間")
    """ 中間期間 """
    prior1_interim_duration: IxNonNumericPublic = Field(default=None, description="前々中間期間")
    """ 前々中間期間 """


class RevenuesFromExternalCustomersInformationForEachRegionTextBlock_edjp_NotesSegmentInformationEtcSemiAnnualConsolidatedFinancialStatements_consolidated_HY_specific_business(SQLModel):
    """ 売上高、地域ごとの情報 [テキストブロック] """

    interim_duration: IxNonNumericPublic = Field(default=None, description="中間期間")
    """ 中間期間 """
    prior1_interim_duration: IxNonNumericPublic = Field(default=None, description="前々中間期間")
    """ 前々中間期間 """


class SemiAnnualBalanceSheetTextBlock_edjp_SemiAnnualBalanceSheet_consolidated_HY_specific_business(SQLModel):
    """ 中間貸借対照表 [テキストブロック] """

    interim_duration: IxNonNumericPublic = Field(default=None, description="中間期間")
    """ 中間期間 """


class SemiAnnualConsolidatedBalanceSheetTextBlock_edjp_SemiAnnualConsolidatedBalanceSheet_consolidated_HY_specific_business(SQLModel):
    """ 中間連結貸借対照表 [テキストブロック] """

    interim_duration: IxNonNumericPublic = Field(default=None, description="中間期間")
    """ 中間期間 """


class AccountingStandardsDEI_edjp_SemiAnnualConsolidatedBalanceSheet_consolidated_HY_specific_business(SQLModel):
    """ 会計基準、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class AmendmentFlagDEI_edjp_SemiAnnualConsolidatedBalanceSheet_consolidated_HY_specific_business(SQLModel):
    """ 訂正の有無、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class CabinetOfficeOrdinanceDEI_edjp_SemiAnnualConsolidatedBalanceSheet_consolidated_HY_specific_business(SQLModel):
    """ 府令、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class ComparativePeriodEndDateDEI_edjp_SemiAnnualConsolidatedBalanceSheet_consolidated_HY_specific_business(SQLModel):
    """ 比較対象会計期間終了日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class CurrentFiscalYearEndDateDEI_edjp_SemiAnnualConsolidatedBalanceSheet_consolidated_HY_specific_business(SQLModel):
    """ 当事業年度終了日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class CurrentFiscalYearStartDateDEI_edjp_SemiAnnualConsolidatedBalanceSheet_consolidated_HY_specific_business(SQLModel):
    """ 当事業年度開始日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class CurrentPeriodEndDateDEI_edjp_SemiAnnualConsolidatedBalanceSheet_consolidated_HY_specific_business(SQLModel):
    """ 当会計期間終了日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class DocumentTypeDEI_edjp_SemiAnnualConsolidatedBalanceSheet_consolidated_HY_specific_business(SQLModel):
    """ 様式、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class EDINETCodeDEI_edjp_SemiAnnualConsolidatedBalanceSheet_consolidated_HY_specific_business(SQLModel):
    """ EDINETコード、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class EndDateOfQuarterlyOrSemiAnnualPeriodOfNextFiscalYearDEI_edjp_SemiAnnualConsolidatedBalanceSheet_consolidated_HY_specific_business(SQLModel):
    """ 次の四半期又は中間期の会計期間終了日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class FilerNameInEnglishDEI_edjp_SemiAnnualConsolidatedBalanceSheet_consolidated_HY_specific_business(SQLModel):
    """ 提出者名（英語表記）、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class FilerNameInJapaneseDEI_edjp_SemiAnnualConsolidatedBalanceSheet_consolidated_HY_specific_business(SQLModel):
    """ 提出者名（日本語表記）、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class FundCodeDEI_edjp_SemiAnnualConsolidatedBalanceSheet_consolidated_HY_specific_business(SQLModel):
    """ ファンドコード、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class FundNameInEnglishDEI_edjp_SemiAnnualConsolidatedBalanceSheet_consolidated_HY_specific_business(SQLModel):
    """ ファンド名称（英語表記）、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class FundNameInJapaneseDEI_edjp_SemiAnnualConsolidatedBalanceSheet_consolidated_HY_specific_business(SQLModel):
    """ ファンド名称（日本語表記）、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class IdentificationOfDocumentSubjectToAmendmentDEI_edjp_SemiAnnualConsolidatedBalanceSheet_consolidated_HY_specific_business(SQLModel):
    """ 訂正対象書類の書類管理番号、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class IndustryCodeWhenConsolidatedFinancialStatementsArePreparedInAccordanceWithIndustrySpecificRegulationsDEI_edjp_SemiAnnualConsolidatedBalanceSheet_consolidated_HY_specific_business(SQLModel):
    """ 別記事業（連結）、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class IndustryCodeWhenFinancialStatementsArePreparedInAccordanceWithIndustrySpecificRegulationsDEI_edjp_SemiAnnualConsolidatedBalanceSheet_consolidated_HY_specific_business(SQLModel):
    """ 別記事業（個別）、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class NextFiscalYearStartDateDEI_edjp_SemiAnnualConsolidatedBalanceSheet_consolidated_HY_specific_business(SQLModel):
    """ 次の事業年度開始日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class PreviousFiscalYearEndDateDEI_edjp_SemiAnnualConsolidatedBalanceSheet_consolidated_HY_specific_business(SQLModel):
    """ 前事業年度終了日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class PreviousFiscalYearStartDateDEI_edjp_SemiAnnualConsolidatedBalanceSheet_consolidated_HY_specific_business(SQLModel):
    """ 前事業年度開始日、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class ReportAmendmentFlagDEI_edjp_SemiAnnualConsolidatedBalanceSheet_consolidated_HY_specific_business(SQLModel):
    """ 記載事項訂正のフラグ、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class SecurityCodeDEI_edjp_SemiAnnualConsolidatedBalanceSheet_consolidated_HY_specific_business(SQLModel):
    """ 証券コード、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class TypeOfCurrentPeriodDEI_edjp_SemiAnnualConsolidatedBalanceSheet_consolidated_HY_specific_business(SQLModel):
    """ 当会計期間の種類、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class WhetherConsolidatedFinancialStatementsArePreparedDEI_edjp_SemiAnnualConsolidatedBalanceSheet_consolidated_HY_specific_business(SQLModel):
    """ 連結決算の有無、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class XBRLAmendmentFlagDEI_edjp_SemiAnnualConsolidatedBalanceSheet_consolidated_HY_specific_business(SQLModel):
    """ XBRL訂正のフラグ、DEI """

    filing_date_instant: IxNonNumericPublic = Field(default=None, description="提出日時点")
    """ 提出日時点 """


class SemiAnnualConsolidatedStatementOfChangesInEquityTextBlock_edjp_SemiAnnualConsolidatedStatementOfChangesInEquity_consolidated_HY_specific_business(SQLModel):
    """ 中間連結株主資本等変動計算書 [テキストブロック] """

    interim_duration: IxNonNumericPublic = Field(default=None, description="中間期間")
    """ 中間期間 """


class SemiAnnualConsolidatedStatementOfComprehensiveIncomeTextBlock_edjp_SemiAnnualConsolidatedStatementOfComprehensiveIncome_consolidated_HY_specific_business(SQLModel):
    """ 中間連結包括利益計算書 [テキストブロック] """

    interim_duration: IxNonNumericPublic = Field(default=None, description="中間期間")
    """ 中間期間 """


class SemiAnnualConsolidatedStatementOfIncomeTextBlock_edjp_SemiAnnualConsolidatedStatementOfIncome_consolidated_HY_specific_business(SQLModel):
    """ 中間連結損益計算書 [テキストブロック] """

    interim_duration: IxNonNumericPublic = Field(default=None, description="中間期間")
    """ 中間期間 """


class SemiAnnualStatementOfChangesInEquityTextBlock_edjp_SemiAnnualStatementOfChangesInEquity_consolidated_HY_specific_business(SQLModel):
    """ 中間株主資本等変動計算書 [テキストブロック] """

    interim_duration: IxNonNumericPublic = Field(default=None, description="中間期間")
    """ 中間期間 """


class SemiAnnualStatementOfIncomeTextBlock_edjp_SemiAnnualStatementOfIncome_consolidated_HY_specific_business(SQLModel):
    """ 中間損益計算書 [テキストブロック] """

    interim_duration: IxNonNumericPublic = Field(default=None, description="中間期間")
    """ 中間期間 """


class CompanyName_rvfc_FinancialReportSummary(SQLModel):
    """ 上場会社名 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class DocumentName_rvfc_FinancialReportSummary(SQLModel):
    """ 文書名 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class FASFMemberMark_rvfc_FinancialReportSummary(SQLModel):
    """ 財務会計基準機構会員マーク """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class FiscalYearEnd_rvfc_FinancialReportSummary(SQLModel):
    """ 決算期 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class FukuokaStockExchange_rvfc_FinancialReportSummary(SQLModel):
    """ 福岡証券取引所 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class FukuokaStockExchangeEstablished_rvfc_FinancialReportSummary(SQLModel):
    """ 福岡証券取引所 既存市場 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class FukuokaStockExchangeOthers_rvfc_FinancialReportSummary(SQLModel):
    """ 福岡証券取引所 その他 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class FukuokaStockExchangeQBoard_rvfc_FinancialReportSummary(SQLModel):
    """ 福岡証券取引所 Q-Board """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class GeneralBusiness_rvfc_FinancialReportSummary(SQLModel):
    """ 一般事業会社 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class JapanSecuritiesDealersAssociation_rvfc_FinancialReportSummary(SQLModel):
    """ フェニックス """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class JapanSecuritiesDealersAssociationGreenSheet_rvfc_FinancialReportSummary(SQLModel):
    """ 日本証券業協会 フェニックス """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class NagoyaStockExchange_rvfc_FinancialReportSummary(SQLModel):
    """ 名古屋証券取引所 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class NagoyaStockExchange1stSection_rvfc_FinancialReportSummary(SQLModel):
    """ 名古屋証券取引所 プレミア """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class NagoyaStockExchange2ndSection_rvfc_FinancialReportSummary(SQLModel):
    """ 名古屋証券取引所 メイン """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class NagoyaStockExchangeCentrex_rvfc_FinancialReportSummary(SQLModel):
    """ 名古屋証券取引所 ネクスト """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class NagoyaStockExchangeOthers_rvfc_FinancialReportSummary(SQLModel):
    """ 名古屋証券取引所 その他 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class NameInquiries_rvfc_FinancialReportSummary(SQLModel):
    """ 氏名、問合せ先責任者 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class NameRepresentative_rvfc_FinancialReportSummary(SQLModel):
    """ 氏名、代表者 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class NoteToDividends_rvfc_FinancialReportSummary(SQLModel):
    """ 配当の状況に関する注記 """

    current_year_duration: IxNonNumericPublic = Field(default=None, description="当年度会計期間")
    """ 当年度会計期間 """


class NoteToFinancialForecast_rvfc_FinancialReportSummary(SQLModel):
    """ 業績予想の状況に関する注記 """

    current_year_duration: IxNonNumericPublic = Field(default=None, description="当年度会計期間")
    """ 当年度会計期間 """


class NoticeOfForecastCorrection_rvfc_FinancialReportSummary(SQLModel):
    """ 予想修正に関するお知らせ """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class PreambleToForecasts_rvfc_FinancialReportSummary(SQLModel):
    """ 業績予想に関する事項 """

    current_accumulated_q2_duration_consolidated_member_current_member_forecast_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間_連結_今回_予想")
    """ 当年度期初から第２四半期間_連結_今回_予想 """
    current_accumulated_q2_duration_non_consolidated_member_current_member_forecast_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間_非連結又は個別_今回_予想")
    """ 当年度期初から第２四半期間_非連結又は個別_今回_予想 """
    current_year_duration_consolidated_member_current_member_forecast_member: IxNonNumericPublic = Field(default=None, description="当年度会計期間_連結_今回_予想")
    """ 当年度会計期間_連結_今回_予想 """
    current_year_duration_non_consolidated_member_current_member_forecast_member: IxNonNumericPublic = Field(default=None, description="当年度会計期間_非連結又は個別_今回_予想")
    """ 当年度会計期間_非連結又は個別_今回_予想 """


class PreviousReportingDateOfDividendForecast_rvfc_FinancialReportSummary(SQLModel):
    """ 前回予想発表日、配当予想の修正について """

    current_year_instant_annual_member_non_consolidated_member_previous_member_result_member: IxNonNumericPublic = Field(default=None, description="当年度時点_年間_非連結又は個別_前回_実績")
    """ 当年度時点_年間_非連結又は個別_前回_実績 """


class ReasonForDividendForecastCorrection_rvfc_FinancialReportSummary(SQLModel):
    """ 配当予想修正の理由 """

    current_year_duration: IxNonNumericPublic = Field(default=None, description="当年度会計期間")
    """ 当年度会計期間 """


class ReasonForForecastCorrection_rvfc_FinancialReportSummary(SQLModel):
    """ 業績予想修正の理由 """

    current_year_duration: IxNonNumericPublic = Field(default=None, description="当年度会計期間")
    """ 当年度会計期間 """


class ReportingDateOfFinancialForecastCorrection_rvfc_FinancialReportSummary(SQLModel):
    """ 予想修正報告日 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class SapporoStockExchange_rvfc_FinancialReportSummary(SQLModel):
    """ 札幌証券取引所 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class SapporoStockExchangeAmbitious_rvfc_FinancialReportSummary(SQLModel):
    """ 札幌証券取引所 アンビシャス """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class SapporoStockExchangeEstablished_rvfc_FinancialReportSummary(SQLModel):
    """ 札幌証券取引所 既存市場 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class SapporoStockExchangeOthers_rvfc_FinancialReportSummary(SQLModel):
    """ 札幌証券取引所 その他 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class SecuritiesCode_rvfc_FinancialReportSummary(SQLModel):
    """ コード番号 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class SpecificBusiness_rvfc_FinancialReportSummary(SQLModel):
    """ 特定事業会社 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class Tel_rvfc_FinancialReportSummary(SQLModel):
    """ TEL """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class TitleInquiries_rvfc_FinancialReportSummary(SQLModel):
    """ 役職名、問合せ先責任者 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class TitleRepresentative_rvfc_FinancialReportSummary(SQLModel):
    """ 役職名、代表者 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class TokyoStockExchange_rvfc_FinancialReportSummary(SQLModel):
    """ 東京証券取引所 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class TokyoStockExchangeGrowth_rvfc_FinancialReportSummary(SQLModel):
    """ 東京証券取引所 グロース """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class TokyoStockExchangeOthers_rvfc_FinancialReportSummary(SQLModel):
    """ 東京証券取引所 その他 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class TokyoStockExchangePrime_rvfc_FinancialReportSummary(SQLModel):
    """ 東京証券取引所 プライム """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class TokyoStockExchangePROMarket_rvfc_FinancialReportSummary(SQLModel):
    """ 東京証券取引所 PRO Market """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class TokyoStockExchangeStandard_rvfc_FinancialReportSummary(SQLModel):
    """ 東京証券取引所 スタンダード """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class CompanyName_rvfc_FinancialReportSummary_specific_business(SQLModel):
    """ 上場会社名 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class DocumentName_rvfc_FinancialReportSummary_specific_business(SQLModel):
    """ 文書名 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class FASFMemberMark_rvfc_FinancialReportSummary_specific_business(SQLModel):
    """ 財務会計基準機構会員マーク """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class FiscalYearEnd_rvfc_FinancialReportSummary_specific_business(SQLModel):
    """ 決算期 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class FukuokaStockExchange_rvfc_FinancialReportSummary_specific_business(SQLModel):
    """ 福岡証券取引所 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class FukuokaStockExchangeEstablished_rvfc_FinancialReportSummary_specific_business(SQLModel):
    """ 福岡証券取引所 既存市場 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class FukuokaStockExchangeOthers_rvfc_FinancialReportSummary_specific_business(SQLModel):
    """ 福岡証券取引所 その他 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class FukuokaStockExchangeQBoard_rvfc_FinancialReportSummary_specific_business(SQLModel):
    """ 福岡証券取引所 Q-Board """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class GeneralBusiness_rvfc_FinancialReportSummary_specific_business(SQLModel):
    """ 一般事業会社 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class JapanSecuritiesDealersAssociation_rvfc_FinancialReportSummary_specific_business(SQLModel):
    """ フェニックス """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class JapanSecuritiesDealersAssociationGreenSheet_rvfc_FinancialReportSummary_specific_business(SQLModel):
    """ 日本証券業協会 フェニックス """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class NagoyaStockExchange_rvfc_FinancialReportSummary_specific_business(SQLModel):
    """ 名古屋証券取引所 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class NagoyaStockExchange1stSection_rvfc_FinancialReportSummary_specific_business(SQLModel):
    """ 名古屋証券取引所 プレミア """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class NagoyaStockExchange2ndSection_rvfc_FinancialReportSummary_specific_business(SQLModel):
    """ 名古屋証券取引所 メイン """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class NagoyaStockExchangeCentrex_rvfc_FinancialReportSummary_specific_business(SQLModel):
    """ 名古屋証券取引所 ネクスト """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class NagoyaStockExchangeOthers_rvfc_FinancialReportSummary_specific_business(SQLModel):
    """ 名古屋証券取引所 その他 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class NameInquiries_rvfc_FinancialReportSummary_specific_business(SQLModel):
    """ 氏名、問合せ先責任者 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class NameRepresentative_rvfc_FinancialReportSummary_specific_business(SQLModel):
    """ 氏名、代表者 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class NoteToFinancialForecast_rvfc_FinancialReportSummary_specific_business(SQLModel):
    """ 業績予想の状況に関する注記 """

    current_year_duration: IxNonNumericPublic = Field(default=None, description="当年度会計期間")
    """ 当年度会計期間 """


class NoticeOfForecastCorrection_rvfc_FinancialReportSummary_specific_business(SQLModel):
    """ 予想修正に関するお知らせ """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class PreambleToForecasts_rvfc_FinancialReportSummary_specific_business(SQLModel):
    """ 業績予想に関する事項 """

    current_accumulated_q2_duration_consolidated_member_current_member_forecast_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間_連結_今回_予想")
    """ 当年度期初から第２四半期間_連結_今回_予想 """
    current_accumulated_q2_duration_non_consolidated_member_current_member_forecast_member: IxNonNumericPublic = Field(default=None, description="当年度期初から第２四半期間_非連結又は個別_今回_予想")
    """ 当年度期初から第２四半期間_非連結又は個別_今回_予想 """


class ReasonForForecastCorrection_rvfc_FinancialReportSummary_specific_business(SQLModel):
    """ 業績予想修正の理由 """

    current_year_duration: IxNonNumericPublic = Field(default=None, description="当年度会計期間")
    """ 当年度会計期間 """


class ReportingDateOfFinancialForecastCorrection_rvfc_FinancialReportSummary_specific_business(SQLModel):
    """ 予想修正報告日 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class SapporoStockExchange_rvfc_FinancialReportSummary_specific_business(SQLModel):
    """ 札幌証券取引所 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class SapporoStockExchangeAmbitious_rvfc_FinancialReportSummary_specific_business(SQLModel):
    """ 札幌証券取引所 アンビシャス """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class SapporoStockExchangeEstablished_rvfc_FinancialReportSummary_specific_business(SQLModel):
    """ 札幌証券取引所 既存市場 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class SapporoStockExchangeOthers_rvfc_FinancialReportSummary_specific_business(SQLModel):
    """ 札幌証券取引所 その他 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class SecuritiesCode_rvfc_FinancialReportSummary_specific_business(SQLModel):
    """ コード番号 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class SpecificBusiness_rvfc_FinancialReportSummary_specific_business(SQLModel):
    """ 特定事業会社 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class Tel_rvfc_FinancialReportSummary_specific_business(SQLModel):
    """ TEL """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class TitleInquiries_rvfc_FinancialReportSummary_specific_business(SQLModel):
    """ 役職名、問合せ先責任者 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class TitleRepresentative_rvfc_FinancialReportSummary_specific_business(SQLModel):
    """ 役職名、代表者 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class TokyoStockExchange_rvfc_FinancialReportSummary_specific_business(SQLModel):
    """ 東京証券取引所 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class TokyoStockExchangeGrowth_rvfc_FinancialReportSummary_specific_business(SQLModel):
    """ 東京証券取引所 グロース """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class TokyoStockExchangeOthers_rvfc_FinancialReportSummary_specific_business(SQLModel):
    """ 東京証券取引所 その他 """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class TokyoStockExchangePrime_rvfc_FinancialReportSummary_specific_business(SQLModel):
    """ 東京証券取引所 プライム """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class TokyoStockExchangePROMarket_rvfc_FinancialReportSummary_specific_business(SQLModel):
    """ 東京証券取引所 PRO Market """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class TokyoStockExchangeStandard_rvfc_FinancialReportSummary_specific_business(SQLModel):
    """ 東京証券取引所 スタンダード """

    current_year_instant: IxNonNumericPublic = Field(default=None, description="当年度時点")
    """ 当年度時点 """


class edif_CondensedQuarterlyConsolidatedStatementOfCashFlowsIFRS_consolidated_Q2(IxbrlBase):
    condensed_quarterly_consolidated_statement_of_cash_flows_ifrs_text_block:CondensedQuarterlyConsolidatedStatementOfCashFlowsIFRSTextBlock_edif_CondensedQuarterlyConsolidatedStatementOfCashFlowsIFRS_consolidated_Q2 = Field(default=None, description="要約四半期連結キャッシュ・フロー計算書（IFRS） [テキストブロック]")
    """ 要約四半期連結キャッシュ・フロー計算書（IFRS） [テキストブロック] """


class edif_CondensedQuarterlyConsolidatedStatementOfCashFlowsIFRS_consolidated_Q3(IxbrlBase):
    condensed_quarterly_consolidated_statement_of_cash_flows_ifrs_text_block:CondensedQuarterlyConsolidatedStatementOfCashFlowsIFRSTextBlock_edif_CondensedQuarterlyConsolidatedStatementOfCashFlowsIFRS_consolidated_Q3 = Field(default=None, description="要約四半期連結キャッシュ・フロー計算書（IFRS） [テキストブロック]")
    """ 要約四半期連結キャッシュ・フロー計算書（IFRS） [テキストブロック] """


class edif_CondensedQuarterlyConsolidatedStatementOfChangesInEquityIFRS_consolidated_Q2(IxbrlBase):
    condensed_quarterly_consolidated_statement_of_cash_flows_ifrs_text_block:CondensedQuarterlyConsolidatedStatementOfCashFlowsIFRSTextBlock_edif_CondensedQuarterlyConsolidatedStatementOfChangesInEquityIFRS_consolidated_Q2 = Field(default=None, description="要約四半期連結キャッシュ・フロー計算書（IFRS） [テキストブロック]")
    """ 要約四半期連結キャッシュ・フロー計算書（IFRS） [テキストブロック] """
    condensed_quarterly_consolidated_statement_of_changes_in_equity_ifrs_text_block:CondensedQuarterlyConsolidatedStatementOfChangesInEquityIFRSTextBlock_edif_CondensedQuarterlyConsolidatedStatementOfChangesInEquityIFRS_consolidated_Q2 = Field(default=None, description="要約四半期連結持分変動計算書（IFRS） [テキストブロック]")
    """ 要約四半期連結持分変動計算書（IFRS） [テキストブロック] """


class edif_CondensedQuarterlyConsolidatedStatementOfChangesInEquityIFRS_consolidated_Q3(IxbrlBase):
    condensed_quarterly_consolidated_statement_of_changes_in_equity_ifrs_text_block:CondensedQuarterlyConsolidatedStatementOfChangesInEquityIFRSTextBlock_edif_CondensedQuarterlyConsolidatedStatementOfChangesInEquityIFRS_consolidated_Q3 = Field(default=None, description="要約四半期連結持分変動計算書（IFRS） [テキストブロック]")
    """ 要約四半期連結持分変動計算書（IFRS） [テキストブロック] """


class edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q2(IxbrlBase):
    accounting_standards_dei:AccountingStandardsDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q2 = Field(default=None, description="会計基準、DEI")
    """ 会計基準、DEI """
    amendment_flag_dei:AmendmentFlagDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q2 = Field(default=None, description="訂正の有無、DEI")
    """ 訂正の有無、DEI """
    cabinet_office_ordinance_dei:CabinetOfficeOrdinanceDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q2 = Field(default=None, description="府令、DEI")
    """ 府令、DEI """
    comparative_period_end_date_dei:ComparativePeriodEndDateDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q2 = Field(default=None, description="比較対象会計期間終了日、DEI")
    """ 比較対象会計期間終了日、DEI """
    current_fiscal_year_end_date_dei:CurrentFiscalYearEndDateDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q2 = Field(default=None, description="当事業年度終了日、DEI")
    """ 当事業年度終了日、DEI """
    current_fiscal_year_start_date_dei:CurrentFiscalYearStartDateDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q2 = Field(default=None, description="当事業年度開始日、DEI")
    """ 当事業年度開始日、DEI """
    current_period_end_date_dei:CurrentPeriodEndDateDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q2 = Field(default=None, description="当会計期間終了日、DEI")
    """ 当会計期間終了日、DEI """
    document_type_dei:DocumentTypeDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q2 = Field(default=None, description="様式、DEI")
    """ 様式、DEI """
    edinet_code_dei:EDINETCodeDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q2 = Field(default=None, description="EDINETコード、DEI")
    """ EDINETコード、DEI """
    end_date_of_quarterly_or_semi_annual_period_of_next_fiscal_year_dei:EndDateOfQuarterlyOrSemiAnnualPeriodOfNextFiscalYearDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q2 = Field(default=None, description="次の四半期又は中間期の会計期間終了日、DEI")
    """ 次の四半期又は中間期の会計期間終了日、DEI """
    filer_name_in_english_dei:FilerNameInEnglishDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q2 = Field(default=None, description="提出者名（英語表記）、DEI")
    """ 提出者名（英語表記）、DEI """
    filer_name_in_japanese_dei:FilerNameInJapaneseDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q2 = Field(default=None, description="提出者名（日本語表記）、DEI")
    """ 提出者名（日本語表記）、DEI """
    fund_code_dei:FundCodeDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q2 = Field(default=None, description="ファンドコード、DEI")
    """ ファンドコード、DEI """
    fund_name_in_english_dei:FundNameInEnglishDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q2 = Field(default=None, description="ファンド名称（英語表記）、DEI")
    """ ファンド名称（英語表記）、DEI """
    fund_name_in_japanese_dei:FundNameInJapaneseDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q2 = Field(default=None, description="ファンド名称（日本語表記）、DEI")
    """ ファンド名称（日本語表記）、DEI """
    identification_of_document_subject_to_amendment_dei:IdentificationOfDocumentSubjectToAmendmentDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q2 = Field(default=None, description="訂正対象書類の書類管理番号、DEI")
    """ 訂正対象書類の書類管理番号、DEI """
    industry_code_when_consolidated_financial_statements_are_prepared_in_accordance_with_industry_specific_regulations_dei:IndustryCodeWhenConsolidatedFinancialStatementsArePreparedInAccordanceWithIndustrySpecificRegulationsDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q2 = Field(default=None, description="別記事業（連結）、DEI")
    """ 別記事業（連結）、DEI """
    industry_code_when_financial_statements_are_prepared_in_accordance_with_industry_specific_regulations_dei:IndustryCodeWhenFinancialStatementsArePreparedInAccordanceWithIndustrySpecificRegulationsDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q2 = Field(default=None, description="別記事業（個別）、DEI")
    """ 別記事業（個別）、DEI """
    next_fiscal_year_start_date_dei:NextFiscalYearStartDateDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q2 = Field(default=None, description="次の事業年度開始日、DEI")
    """ 次の事業年度開始日、DEI """
    previous_fiscal_year_end_date_dei:PreviousFiscalYearEndDateDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q2 = Field(default=None, description="前事業年度終了日、DEI")
    """ 前事業年度終了日、DEI """
    previous_fiscal_year_start_date_dei:PreviousFiscalYearStartDateDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q2 = Field(default=None, description="前事業年度開始日、DEI")
    """ 前事業年度開始日、DEI """
    report_amendment_flag_dei:ReportAmendmentFlagDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q2 = Field(default=None, description="記載事項訂正のフラグ、DEI")
    """ 記載事項訂正のフラグ、DEI """
    security_code_dei:SecurityCodeDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q2 = Field(default=None, description="証券コード、DEI")
    """ 証券コード、DEI """
    type_of_current_period_dei:TypeOfCurrentPeriodDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q2 = Field(default=None, description="当会計期間の種類、DEI")
    """ 当会計期間の種類、DEI """
    whether_consolidated_financial_statements_are_prepared_dei:WhetherConsolidatedFinancialStatementsArePreparedDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q2 = Field(default=None, description="連結決算の有無、DEI")
    """ 連結決算の有無、DEI """
    xbrl_amendment_flag_dei:XBRLAmendmentFlagDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q2 = Field(default=None, description="XBRL訂正のフラグ、DEI")
    """ XBRL訂正のフラグ、DEI """
    condensed_quarterly_consolidated_statement_of_financial_position_ifrs_text_block:CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRSTextBlock_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q2 = Field(default=None, description="要約四半期連結財政状態計算書（IFRS） [テキストブロック]")
    """ 要約四半期連結財政状態計算書（IFRS） [テキストブロック] """


class edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q3(IxbrlBase):
    accounting_standards_dei:AccountingStandardsDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q3 = Field(default=None, description="会計基準、DEI")
    """ 会計基準、DEI """
    amendment_flag_dei:AmendmentFlagDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q3 = Field(default=None, description="訂正の有無、DEI")
    """ 訂正の有無、DEI """
    cabinet_office_ordinance_dei:CabinetOfficeOrdinanceDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q3 = Field(default=None, description="府令、DEI")
    """ 府令、DEI """
    comparative_period_end_date_dei:ComparativePeriodEndDateDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q3 = Field(default=None, description="比較対象会計期間終了日、DEI")
    """ 比較対象会計期間終了日、DEI """
    current_fiscal_year_end_date_dei:CurrentFiscalYearEndDateDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q3 = Field(default=None, description="当事業年度終了日、DEI")
    """ 当事業年度終了日、DEI """
    current_fiscal_year_start_date_dei:CurrentFiscalYearStartDateDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q3 = Field(default=None, description="当事業年度開始日、DEI")
    """ 当事業年度開始日、DEI """
    current_period_end_date_dei:CurrentPeriodEndDateDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q3 = Field(default=None, description="当会計期間終了日、DEI")
    """ 当会計期間終了日、DEI """
    document_type_dei:DocumentTypeDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q3 = Field(default=None, description="様式、DEI")
    """ 様式、DEI """
    edinet_code_dei:EDINETCodeDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q3 = Field(default=None, description="EDINETコード、DEI")
    """ EDINETコード、DEI """
    end_date_of_quarterly_or_semi_annual_period_of_next_fiscal_year_dei:EndDateOfQuarterlyOrSemiAnnualPeriodOfNextFiscalYearDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q3 = Field(default=None, description="次の四半期又は中間期の会計期間終了日、DEI")
    """ 次の四半期又は中間期の会計期間終了日、DEI """
    filer_name_in_english_dei:FilerNameInEnglishDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q3 = Field(default=None, description="提出者名（英語表記）、DEI")
    """ 提出者名（英語表記）、DEI """
    filer_name_in_japanese_dei:FilerNameInJapaneseDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q3 = Field(default=None, description="提出者名（日本語表記）、DEI")
    """ 提出者名（日本語表記）、DEI """
    fund_code_dei:FundCodeDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q3 = Field(default=None, description="ファンドコード、DEI")
    """ ファンドコード、DEI """
    fund_name_in_english_dei:FundNameInEnglishDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q3 = Field(default=None, description="ファンド名称（英語表記）、DEI")
    """ ファンド名称（英語表記）、DEI """
    fund_name_in_japanese_dei:FundNameInJapaneseDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q3 = Field(default=None, description="ファンド名称（日本語表記）、DEI")
    """ ファンド名称（日本語表記）、DEI """
    identification_of_document_subject_to_amendment_dei:IdentificationOfDocumentSubjectToAmendmentDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q3 = Field(default=None, description="訂正対象書類の書類管理番号、DEI")
    """ 訂正対象書類の書類管理番号、DEI """
    industry_code_when_consolidated_financial_statements_are_prepared_in_accordance_with_industry_specific_regulations_dei:IndustryCodeWhenConsolidatedFinancialStatementsArePreparedInAccordanceWithIndustrySpecificRegulationsDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q3 = Field(default=None, description="別記事業（連結）、DEI")
    """ 別記事業（連結）、DEI """
    industry_code_when_financial_statements_are_prepared_in_accordance_with_industry_specific_regulations_dei:IndustryCodeWhenFinancialStatementsArePreparedInAccordanceWithIndustrySpecificRegulationsDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q3 = Field(default=None, description="別記事業（個別）、DEI")
    """ 別記事業（個別）、DEI """
    next_fiscal_year_start_date_dei:NextFiscalYearStartDateDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q3 = Field(default=None, description="次の事業年度開始日、DEI")
    """ 次の事業年度開始日、DEI """
    previous_fiscal_year_end_date_dei:PreviousFiscalYearEndDateDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q3 = Field(default=None, description="前事業年度終了日、DEI")
    """ 前事業年度終了日、DEI """
    previous_fiscal_year_start_date_dei:PreviousFiscalYearStartDateDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q3 = Field(default=None, description="前事業年度開始日、DEI")
    """ 前事業年度開始日、DEI """
    report_amendment_flag_dei:ReportAmendmentFlagDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q3 = Field(default=None, description="記載事項訂正のフラグ、DEI")
    """ 記載事項訂正のフラグ、DEI """
    security_code_dei:SecurityCodeDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q3 = Field(default=None, description="証券コード、DEI")
    """ 証券コード、DEI """
    type_of_current_period_dei:TypeOfCurrentPeriodDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q3 = Field(default=None, description="当会計期間の種類、DEI")
    """ 当会計期間の種類、DEI """
    whether_consolidated_financial_statements_are_prepared_dei:WhetherConsolidatedFinancialStatementsArePreparedDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q3 = Field(default=None, description="連結決算の有無、DEI")
    """ 連結決算の有無、DEI """
    xbrl_amendment_flag_dei:XBRLAmendmentFlagDEI_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q3 = Field(default=None, description="XBRL訂正のフラグ、DEI")
    """ XBRL訂正のフラグ、DEI """
    condensed_quarterly_consolidated_statement_of_financial_position_ifrs_text_block:CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRSTextBlock_edif_CondensedQuarterlyConsolidatedStatementOfFinancialPositionIFRS_consolidated_Q3 = Field(default=None, description="要約四半期連結財政状態計算書（IFRS） [テキストブロック]")
    """ 要約四半期連結財政状態計算書（IFRS） [テキストブロック] """


class edif_CondensedQuarterPeriodConsolidatedStatementOfComprehensiveIncomeIFRS_consolidated_Q3(IxbrlBase):
    condensed_quarter_period_consolidated_statement_of_comprehensive_income_ifrs_text_block:CondensedQuarterPeriodConsolidatedStatementOfComprehensiveIncomeIFRSTextBlock_edif_CondensedQuarterPeriodConsolidatedStatementOfComprehensiveIncomeIFRS_consolidated_Q3 = Field(default=None, description="四半期連結会計期間、要約四半期連結包括利益計算書（IFRS） [テキストブロック]")
    """ 四半期連結会計期間、要約四半期連結包括利益計算書（IFRS） [テキストブロック] """


class edif_CondensedQuarterPeriodConsolidatedStatementOfProfitOrLossIFRS_consolidated_Q3(IxbrlBase):
    condensed_quarter_period_consolidated_statement_of_profit_or_loss_ifrs_text_block:CondensedQuarterPeriodConsolidatedStatementOfProfitOrLossIFRSTextBlock_edif_CondensedQuarterPeriodConsolidatedStatementOfProfitOrLossIFRS_consolidated_Q3 = Field(default=None, description="四半期連結会計期間、要約四半期連結損益計算書（IFRS） [テキストブロック]")
    """ 四半期連結会計期間、要約四半期連結損益計算書（IFRS） [テキストブロック] """


class edif_CondensedYearToQuarterEndConsolidatedStatementOfComprehensiveIncomeIFRS_consolidated_Q2(IxbrlBase):
    condensed_year_to_quarter_end_consolidated_statement_of_comprehensive_income_ifrs_text_block:CondensedYearToQuarterEndConsolidatedStatementOfComprehensiveIncomeIFRSTextBlock_edif_CondensedYearToQuarterEndConsolidatedStatementOfComprehensiveIncomeIFRS_consolidated_Q2 = Field(default=None, description="四半期連結累計期間、要約四半期連結包括利益計算書（IFRS） [テキストブロック]")
    """ 四半期連結累計期間、要約四半期連結包括利益計算書（IFRS） [テキストブロック] """


class edif_CondensedYearToQuarterEndConsolidatedStatementOfComprehensiveIncomeIFRS_consolidated_Q3(IxbrlBase):
    condensed_year_to_quarter_end_consolidated_statement_of_comprehensive_income_ifrs_text_block:CondensedYearToQuarterEndConsolidatedStatementOfComprehensiveIncomeIFRSTextBlock_edif_CondensedYearToQuarterEndConsolidatedStatementOfComprehensiveIncomeIFRS_consolidated_Q3 = Field(default=None, description="四半期連結累計期間、要約四半期連結包括利益計算書（IFRS） [テキストブロック]")
    """ 四半期連結累計期間、要約四半期連結包括利益計算書（IFRS） [テキストブロック] """


class edif_CondensedYearToQuarterEndConsolidatedStatementOfComprehensiveIncomeSingleStatementIFRS_consolidated_Q2(IxbrlBase):
    condensed_year_to_quarter_end_consolidated_statement_of_comprehensive_income_single_statement_ifrs_text_block:CondensedYearToQuarterEndConsolidatedStatementOfComprehensiveIncomeSingleStatementIFRSTextBlock_edif_CondensedYearToQuarterEndConsolidatedStatementOfComprehensiveIncomeSingleStatementIFRS_consolidated_Q2 = Field(default=None, description="四半期連結累計期間、要約四半期連結包括利益計算書（１計算書）（IFRS） [テキストブロック]")
    """ 四半期連結累計期間、要約四半期連結包括利益計算書（１計算書）（IFRS） [テキストブロック] """


class edif_CondensedYearToQuarterEndConsolidatedStatementOfProfitOrLossIFRS_consolidated_Q2(IxbrlBase):
    accounting_standards_dei:AccountingStandardsDEI_edif_CondensedYearToQuarterEndConsolidatedStatementOfProfitOrLossIFRS_consolidated_Q2 = Field(default=None, description="会計基準、DEI")
    """ 会計基準、DEI """
    amendment_flag_dei:AmendmentFlagDEI_edif_CondensedYearToQuarterEndConsolidatedStatementOfProfitOrLossIFRS_consolidated_Q2 = Field(default=None, description="訂正の有無、DEI")
    """ 訂正の有無、DEI """
    cabinet_office_ordinance_dei:CabinetOfficeOrdinanceDEI_edif_CondensedYearToQuarterEndConsolidatedStatementOfProfitOrLossIFRS_consolidated_Q2 = Field(default=None, description="府令、DEI")
    """ 府令、DEI """
    comparative_period_end_date_dei:ComparativePeriodEndDateDEI_edif_CondensedYearToQuarterEndConsolidatedStatementOfProfitOrLossIFRS_consolidated_Q2 = Field(default=None, description="比較対象会計期間終了日、DEI")
    """ 比較対象会計期間終了日、DEI """
    current_fiscal_year_end_date_dei:CurrentFiscalYearEndDateDEI_edif_CondensedYearToQuarterEndConsolidatedStatementOfProfitOrLossIFRS_consolidated_Q2 = Field(default=None, description="当事業年度終了日、DEI")
    """ 当事業年度終了日、DEI """
    current_fiscal_year_start_date_dei:CurrentFiscalYearStartDateDEI_edif_CondensedYearToQuarterEndConsolidatedStatementOfProfitOrLossIFRS_consolidated_Q2 = Field(default=None, description="当事業年度開始日、DEI")
    """ 当事業年度開始日、DEI """
    current_period_end_date_dei:CurrentPeriodEndDateDEI_edif_CondensedYearToQuarterEndConsolidatedStatementOfProfitOrLossIFRS_consolidated_Q2 = Field(default=None, description="当会計期間終了日、DEI")
    """ 当会計期間終了日、DEI """
    document_type_dei:DocumentTypeDEI_edif_CondensedYearToQuarterEndConsolidatedStatementOfProfitOrLossIFRS_consolidated_Q2 = Field(default=None, description="様式、DEI")
    """ 様式、DEI """
    edinet_code_dei:EDINETCodeDEI_edif_CondensedYearToQuarterEndConsolidatedStatementOfProfitOrLossIFRS_consolidated_Q2 = Field(default=None, description="EDINETコード、DEI")
    """ EDINETコード、DEI """
    end_date_of_quarterly_or_semi_annual_period_of_next_fiscal_year_dei:EndDateOfQuarterlyOrSemiAnnualPeriodOfNextFiscalYearDEI_edif_CondensedYearToQuarterEndConsolidatedStatementOfProfitOrLossIFRS_consolidated_Q2 = Field(default=None, description="次の四半期又は中間期の会計期間終了日、DEI")
    """ 次の四半期又は中間期の会計期間終了日、DEI """
    filer_name_in_english_dei:FilerNameInEnglishDEI_edif_CondensedYearToQuarterEndConsolidatedStatementOfProfitOrLossIFRS_consolidated_Q2 = Field(default=None, description="提出者名（英語表記）、DEI")
    """ 提出者名（英語表記）、DEI """
    filer_name_in_japanese_dei:FilerNameInJapaneseDEI_edif_CondensedYearToQuarterEndConsolidatedStatementOfProfitOrLossIFRS_consolidated_Q2 = Field(default=None, description="提出者名（日本語表記）、DEI")
    """ 提出者名（日本語表記）、DEI """
    fund_code_dei:FundCodeDEI_edif_CondensedYearToQuarterEndConsolidatedStatementOfProfitOrLossIFRS_consolidated_Q2 = Field(default=None, description="ファンドコード、DEI")
    """ ファンドコード、DEI """
    fund_name_in_english_dei:FundNameInEnglishDEI_edif_CondensedYearToQuarterEndConsolidatedStatementOfProfitOrLossIFRS_consolidated_Q2 = Field(default=None, description="ファンド名称（英語表記）、DEI")
    """ ファンド名称（英語表記）、DEI """
    fund_name_in_japanese_dei:FundNameInJapaneseDEI_edif_CondensedYearToQuarterEndConsolidatedStatementOfProfitOrLossIFRS_consolidated_Q2 = Field(default=None, description="ファンド名称（日本語表記）、DEI")
    """ ファンド名称（日本語表記）、DEI """
    identification_of_document_subject_to_amendment_dei:IdentificationOfDocumentSubjectToAmendmentDEI_edif_CondensedYearToQuarterEndConsolidatedStatementOfProfitOrLossIFRS_consolidated_Q2 = Field(default=None, description="訂正対象書類の書類管理番号、DEI")
    """ 訂正対象書類の書類管理番号、DEI """
    industry_code_when_consolidated_financial_statements_are_prepared_in_accordance_with_industry_specific_regulations_dei:IndustryCodeWhenConsolidatedFinancialStatementsArePreparedInAccordanceWithIndustrySpecificRegulationsDEI_edif_CondensedYearToQuarterEndConsolidatedStatementOfProfitOrLossIFRS_consolidated_Q2 = Field(default=None, description="別記事業（連結）、DEI")
    """ 別記事業（連結）、DEI """
    industry_code_when_financial_statements_are_prepared_in_accordance_with_industry_specific_regulations_dei:IndustryCodeWhenFinancialStatementsArePreparedInAccordanceWithIndustrySpecificRegulationsDEI_edif_CondensedYearToQuarterEndConsolidatedStatementOfProfitOrLossIFRS_consolidated_Q2 = Field(default=None, description="別記事業（個別）、DEI")
    """ 別記事業（個別）、DEI """
    next_fiscal_year_start_date_dei:NextFiscalYearStartDateDEI_edif_CondensedYearToQuarterEndConsolidatedStatementOfProfitOrLossIFRS_consolidated_Q2 = Field(default=None, description="次の事業年度開始日、DEI")
    """ 次の事業年度開始日、DEI """
    previous_fiscal_year_end_date_dei:PreviousFiscalYearEndDateDEI_edif_CondensedYearToQuarterEndConsolidatedStatementOfProfitOrLossIFRS_consolidated_Q2 = Field(default=None, description="前事業年度終了日、DEI")
    """ 前事業年度終了日、DEI """
    previous_fiscal_year_start_date_dei:PreviousFiscalYearStartDateDEI_edif_CondensedYearToQuarterEndConsolidatedStatementOfProfitOrLossIFRS_consolidated_Q2 = Field(default=None, description="前事業年度開始日、DEI")
    """ 前事業年度開始日、DEI """
    report_amendment_flag_dei:ReportAmendmentFlagDEI_edif_CondensedYearToQuarterEndConsolidatedStatementOfProfitOrLossIFRS_consolidated_Q2 = Field(default=None, description="記載事項訂正のフラグ、DEI")
    """ 記載事項訂正のフラグ、DEI """
    security_code_dei:SecurityCodeDEI_edif_CondensedYearToQuarterEndConsolidatedStatementOfProfitOrLossIFRS_consolidated_Q2 = Field(default=None, description="証券コード、DEI")
    """ 証券コード、DEI """
    type_of_current_period_dei:TypeOfCurrentPeriodDEI_edif_CondensedYearToQuarterEndConsolidatedStatementOfProfitOrLossIFRS_consolidated_Q2 = Field(default=None, description="当会計期間の種類、DEI")
    """ 当会計期間の種類、DEI """
    whether_consolidated_financial_statements_are_prepared_dei:WhetherConsolidatedFinancialStatementsArePreparedDEI_edif_CondensedYearToQuarterEndConsolidatedStatementOfProfitOrLossIFRS_consolidated_Q2 = Field(default=None, description="連結決算の有無、DEI")
    """ 連結決算の有無、DEI """
    xbrl_amendment_flag_dei:XBRLAmendmentFlagDEI_edif_CondensedYearToQuarterEndConsolidatedStatementOfProfitOrLossIFRS_consolidated_Q2 = Field(default=None, description="XBRL訂正のフラグ、DEI")
    """ XBRL訂正のフラグ、DEI """
    condensed_year_to_quarter_end_consolidated_statement_of_profit_or_loss_ifrs_text_block:CondensedYearToQuarterEndConsolidatedStatementOfProfitOrLossIFRSTextBlock_edif_CondensedYearToQuarterEndConsolidatedStatementOfProfitOrLossIFRS_consolidated_Q2 = Field(default=None, description="四半期連結累計期間、要約四半期連結損益計算書（IFRS） [テキストブロック]")
    """ 四半期連結累計期間、要約四半期連結損益計算書（IFRS） [テキストブロック] """


class edif_CondensedYearToQuarterEndConsolidatedStatementOfProfitOrLossIFRS_consolidated_Q3(IxbrlBase):
    condensed_year_to_quarter_end_consolidated_statement_of_profit_or_loss_ifrs_text_block:CondensedYearToQuarterEndConsolidatedStatementOfProfitOrLossIFRSTextBlock_edif_CondensedYearToQuarterEndConsolidatedStatementOfProfitOrLossIFRS_consolidated_Q3 = Field(default=None, description="四半期連結累計期間、要約四半期連結損益計算書（IFRS） [テキストブロック]")
    """ 四半期連結累計期間、要約四半期連結損益計算書（IFRS） [テキストブロック] """


class edif_FinancialReportSummary_consolidated_Q2(IxbrlBase):
    changes_in_accounting_estimates_ifrs:ChangesInAccountingEstimatesIFRS_edif_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="会計上の見積りの変更、IFRS")
    """ 会計上の見積りの変更、IFRS """
    changes_in_accounting_policies_other_than_ifrs_requirements_ifrs:ChangesInAccountingPoliciesOtherThanIFRSRequirementsIFRS_edif_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="IFRSにより要求される会計方針の変更以外の会計方針の変更、IFRS")
    """ IFRSにより要求される会計方針の変更以外の会計方針の変更、IFRS """
    changes_in_accounting_policies_required_by_ifrsifrs:ChangesInAccountingPoliciesRequiredByIFRSIFRS_edif_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="IFRSにより要求される会計方針の変更、IFRS")
    """ IFRSにより要求される会計方針の変更、IFRS """
    company_name:CompanyName_edif_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="上場会社名")
    """ 上場会社名 """
    convening_briefing_of_results:ConveningBriefingOfResults_edif_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="決算説明会開催の有無、期中")
    """ 決算説明会開催の有無、期中 """
    correction_of_consolidated_financial_forecast_in_this_quarter:CorrectionOfConsolidatedFinancialForecastInThisQuarter_edif_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="直近に公表されている業績予想からの修正の有無、連結")
    """ 直近に公表されている業績予想からの修正の有無、連結 """
    correction_of_dividend_forecast_in_this_quarter:CorrectionOfDividendForecastInThisQuarter_edif_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="直近に公表されている配当予想からの修正の有無")
    """ 直近に公表されている配当予想からの修正の有無 """
    dividend_payable_date_as_planned:DividendPayableDateAsPlanned_edif_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="配当支払開始予定日")
    """ 配当支払開始予定日 """
    document_name:DocumentName_edif_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="文書名")
    """ 文書名 """
    fasf_member_mark:FASFMemberMark_edif_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="財務会計基準機構会員マーク")
    """ 財務会計基準機構会員マーク """
    filing_date:FilingDate_edif_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="提出日")
    """ 提出日 """
    fiscal_year_end:FiscalYearEnd_edif_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="決算期")
    """ 決算期 """
    fukuoka_stock_exchange:FukuokaStockExchange_edif_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="福岡証券取引所")
    """ 福岡証券取引所 """
    fukuoka_stock_exchange_established:FukuokaStockExchangeEstablished_edif_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="福岡証券取引所 既存市場")
    """ 福岡証券取引所 既存市場 """
    fukuoka_stock_exchange_others:FukuokaStockExchangeOthers_edif_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="福岡証券取引所 その他")
    """ 福岡証券取引所 その他 """
    fukuoka_stock_exchange_q_board:FukuokaStockExchangeQBoard_edif_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="福岡証券取引所 Q-Board")
    """ 福岡証券取引所 Q-Board """
    general_business:GeneralBusiness_edif_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="一般事業会社")
    """ 一般事業会社 """
    japan_securities_dealers_association:JapanSecuritiesDealersAssociation_edif_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="フェニックス")
    """ フェニックス """
    japan_securities_dealers_association_green_sheet:JapanSecuritiesDealersAssociationGreenSheet_edif_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="日本証券業協会 フェニックス")
    """ 日本証券業協会 フェニックス """
    nagoya_stock_exchange:NagoyaStockExchange_edif_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="名古屋証券取引所")
    """ 名古屋証券取引所 """
    nagoya_stock_exchange1st_section:NagoyaStockExchange1stSection_edif_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="名古屋証券取引所 プレミア")
    """ 名古屋証券取引所 プレミア """
    nagoya_stock_exchange2nd_section:NagoyaStockExchange2ndSection_edif_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="名古屋証券取引所 メイン")
    """ 名古屋証券取引所 メイン """
    nagoya_stock_exchange_centrex:NagoyaStockExchangeCentrex_edif_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="名古屋証券取引所 ネクスト")
    """ 名古屋証券取引所 ネクスト """
    nagoya_stock_exchange_others:NagoyaStockExchangeOthers_edif_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="名古屋証券取引所 その他")
    """ 名古屋証券取引所 その他 """
    name_inquiries:NameInquiries_edif_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="氏名、問合せ先責任者")
    """ 氏名、問合せ先責任者 """
    name_of_subsidiaries_excluded_from_consolidation_ifrs:NameOfSubsidiariesExcludedFromConsolidationIFRS_edif_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="社名、除外、IFRS")
    """ 社名、除外、IFRS """
    name_of_subsidiaries_newly_consolidated_ifrs:NameOfSubsidiariesNewlyConsolidatedIFRS_edif_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="社名、新規、IFRS")
    """ 社名、新規、IFRS """
    name_representative:NameRepresentative_edif_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="氏名、代表者")
    """ 氏名、代表者 """
    notes_for_using_forecasted_information_and_others:NotesForUsingForecastedInformationAndOthers_edif_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="業績予想の適切な利用に関する説明、その他特記事項")
    """ 業績予想の適切な利用に関する説明、その他特記事項 """
    note_to_changes_in_accounting_policies_and_accounting_estimates_ifrs:NoteToChangesInAccountingPoliciesAndAccountingEstimatesIFRS_edif_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="会計方針の変更・会計上の見積りの変更に関する注記、IFRS")
    """ 会計方針の変更・会計上の見積りの変更に関する注記、IFRS """
    note_to_consolidated_financial_results:NoteToConsolidatedFinancialResults_edif_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="連結業績に関する注記")
    """ 連結業績に関する注記 """
    note_to_dividends:NoteToDividends_edif_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="配当の状況に関する注記")
    """ 配当の状況に関する注記 """
    note_to_financial_positions:NoteToFinancialPositions_edif_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="財政状態に関する注記")
    """ 財政状態に関する注記 """
    note_to_forecasts:NoteToForecasts_edif_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="業績予想に関する事項、注記")
    """ 業績予想に関する事項、注記 """
    note_to_fraction_processing_method:NoteToFractionProcessingMethod_edif_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="端数処理方法に関する注記")
    """ 端数処理方法に関する注記 """
    note_to_number_of_issued_and_outstanding_shares_common_stock:NoteToNumberOfIssuedAndOutstandingSharesCommonStock_edif_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="発行済株式数（普通株式）に関する注記")
    """ 発行済株式数（普通株式）に関する注記 """
    note_to_operating_results:NoteToOperatingResults_edif_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="経営成績に関する注記")
    """ 経営成績に関する注記 """
    note_to_significant_changes_in_the_scope_of_consolidation_during_the_period:NoteToSignificantChangesInTheScopeOfConsolidationDuringThePeriod_edif_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="期中における連結範囲の重要な変更に関する注記")
    """ 期中における連結範囲の重要な変更に関する注記 """
    preamble_to_forecasts:PreambleToForecasts_edif_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="業績予想に関する事項")
    """ 業績予想に関する事項 """
    sapporo_stock_exchange:SapporoStockExchange_edif_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="札幌証券取引所")
    """ 札幌証券取引所 """
    sapporo_stock_exchange_ambitious:SapporoStockExchangeAmbitious_edif_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="札幌証券取引所 アンビシャス")
    """ 札幌証券取引所 アンビシャス """
    sapporo_stock_exchange_established:SapporoStockExchangeEstablished_edif_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="札幌証券取引所 既存市場")
    """ 札幌証券取引所 既存市場 """
    sapporo_stock_exchange_others:SapporoStockExchangeOthers_edif_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="札幌証券取引所 その他")
    """ 札幌証券取引所 その他 """
    securities_code:SecuritiesCode_edif_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="コード番号")
    """ コード番号 """
    semi_annual_statement_filing_date_as_planned:SemiAnnualStatementFilingDateAsPlanned_edif_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="半期報告書提出予定日")
    """ 半期報告書提出予定日 """
    significant_changes_in_the_scope_of_consolidation_during_the_period_ifrs:SignificantChangesInTheScopeOfConsolidationDuringThePeriodIFRS_edif_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="期中における連結範囲の重要な変更、IFRS")
    """ 期中における連結範囲の重要な変更、IFRS """
    specific_business:SpecificBusiness_edif_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="特定事業会社")
    """ 特定事業会社 """
    supplemental_material_of_results:SupplementalMaterialOfResults_edif_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="決算補足説明資料作成の有無、期中")
    """ 決算補足説明資料作成の有無、期中 """
    target_for_briefing_of_results:TargetForBriefingOfResults_edif_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="決算説明会の対象者")
    """ 決算説明会の対象者 """
    tel:Tel_edif_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="TEL")
    """ TEL """
    title_for_forecasts:TitleForForecasts_edif_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="業績予想タイトル名称")
    """ 業績予想タイトル名称 """
    title_inquiries:TitleInquiries_edif_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="役職名、問合せ先責任者")
    """ 役職名、問合せ先責任者 """
    title_representative:TitleRepresentative_edif_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="役職名、代表者")
    """ 役職名、代表者 """
    tokyo_stock_exchange:TokyoStockExchange_edif_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="東京証券取引所")
    """ 東京証券取引所 """
    tokyo_stock_exchange_growth:TokyoStockExchangeGrowth_edif_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="東京証券取引所 グロース")
    """ 東京証券取引所 グロース """
    tokyo_stock_exchange_others:TokyoStockExchangeOthers_edif_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="東京証券取引所 その他")
    """ 東京証券取引所 その他 """
    tokyo_stock_exchange_prime:TokyoStockExchangePrime_edif_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="東京証券取引所 プライム")
    """ 東京証券取引所 プライム """
    tokyo_stock_exchange_pro_market:TokyoStockExchangePROMarket_edif_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="東京証券取引所 PRO Market")
    """ 東京証券取引所 PRO Market """
    tokyo_stock_exchange_standard:TokyoStockExchangeStandard_edif_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="東京証券取引所 スタンダード")
    """ 東京証券取引所 スタンダード """
    URL:URL_edif_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="URL")
    """ URL """
    way_of_getting_supplemental_material_of_results:WayOfGettingSupplementalMaterialOfResults_edif_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="入手方法等、決算補足説明資料、期中")
    """ 入手方法等、決算補足説明資料、期中 """


class edif_FinancialReportSummary_consolidated_Q3(IxbrlBase):
    changes_in_accounting_estimates_ifrs:ChangesInAccountingEstimatesIFRS_edif_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="会計上の見積りの変更、IFRS")
    """ 会計上の見積りの変更、IFRS """
    changes_in_accounting_policies_other_than_ifrs_requirements_ifrs:ChangesInAccountingPoliciesOtherThanIFRSRequirementsIFRS_edif_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="IFRSにより要求される会計方針の変更以外の会計方針の変更、IFRS")
    """ IFRSにより要求される会計方針の変更以外の会計方針の変更、IFRS """
    changes_in_accounting_policies_required_by_ifrsifrs:ChangesInAccountingPoliciesRequiredByIFRSIFRS_edif_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="IFRSにより要求される会計方針の変更、IFRS")
    """ IFRSにより要求される会計方針の変更、IFRS """
    company_name:CompanyName_edif_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="上場会社名")
    """ 上場会社名 """
    convening_briefing_of_results:ConveningBriefingOfResults_edif_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="決算説明会開催の有無、期中")
    """ 決算説明会開催の有無、期中 """
    correction_of_consolidated_financial_forecast_in_this_quarter:CorrectionOfConsolidatedFinancialForecastInThisQuarter_edif_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="直近に公表されている業績予想からの修正の有無、連結")
    """ 直近に公表されている業績予想からの修正の有無、連結 """
    correction_of_dividend_forecast_in_this_quarter:CorrectionOfDividendForecastInThisQuarter_edif_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="直近に公表されている配当予想からの修正の有無")
    """ 直近に公表されている配当予想からの修正の有無 """
    dividend_payable_date_as_planned:DividendPayableDateAsPlanned_edif_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="配当支払開始予定日")
    """ 配当支払開始予定日 """
    document_name:DocumentName_edif_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="文書名")
    """ 文書名 """
    fasf_member_mark:FASFMemberMark_edif_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="財務会計基準機構会員マーク")
    """ 財務会計基準機構会員マーク """
    filing_date:FilingDate_edif_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="提出日")
    """ 提出日 """
    fiscal_year_end:FiscalYearEnd_edif_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="決算期")
    """ 決算期 """
    fukuoka_stock_exchange:FukuokaStockExchange_edif_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="福岡証券取引所")
    """ 福岡証券取引所 """
    fukuoka_stock_exchange_established:FukuokaStockExchangeEstablished_edif_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="福岡証券取引所 既存市場")
    """ 福岡証券取引所 既存市場 """
    fukuoka_stock_exchange_others:FukuokaStockExchangeOthers_edif_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="福岡証券取引所 その他")
    """ 福岡証券取引所 その他 """
    fukuoka_stock_exchange_q_board:FukuokaStockExchangeQBoard_edif_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="福岡証券取引所 Q-Board")
    """ 福岡証券取引所 Q-Board """
    general_business:GeneralBusiness_edif_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="一般事業会社")
    """ 一般事業会社 """
    japan_securities_dealers_association:JapanSecuritiesDealersAssociation_edif_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="フェニックス")
    """ フェニックス """
    japan_securities_dealers_association_green_sheet:JapanSecuritiesDealersAssociationGreenSheet_edif_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="日本証券業協会 フェニックス")
    """ 日本証券業協会 フェニックス """
    nagoya_stock_exchange:NagoyaStockExchange_edif_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="名古屋証券取引所")
    """ 名古屋証券取引所 """
    nagoya_stock_exchange1st_section:NagoyaStockExchange1stSection_edif_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="名古屋証券取引所 プレミア")
    """ 名古屋証券取引所 プレミア """
    nagoya_stock_exchange2nd_section:NagoyaStockExchange2ndSection_edif_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="名古屋証券取引所 メイン")
    """ 名古屋証券取引所 メイン """
    nagoya_stock_exchange_centrex:NagoyaStockExchangeCentrex_edif_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="名古屋証券取引所 ネクスト")
    """ 名古屋証券取引所 ネクスト """
    nagoya_stock_exchange_others:NagoyaStockExchangeOthers_edif_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="名古屋証券取引所 その他")
    """ 名古屋証券取引所 その他 """
    name_inquiries:NameInquiries_edif_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="氏名、問合せ先責任者")
    """ 氏名、問合せ先責任者 """
    name_of_subsidiaries_excluded_from_consolidation_ifrs:NameOfSubsidiariesExcludedFromConsolidationIFRS_edif_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="社名、除外、IFRS")
    """ 社名、除外、IFRS """
    name_of_subsidiaries_newly_consolidated_ifrs:NameOfSubsidiariesNewlyConsolidatedIFRS_edif_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="社名、新規、IFRS")
    """ 社名、新規、IFRS """
    name_representative:NameRepresentative_edif_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="氏名、代表者")
    """ 氏名、代表者 """
    notes_for_using_forecasted_information_and_others:NotesForUsingForecastedInformationAndOthers_edif_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="業績予想の適切な利用に関する説明、その他特記事項")
    """ 業績予想の適切な利用に関する説明、その他特記事項 """
    note_to_changes_in_accounting_policies_and_accounting_estimates_ifrs:NoteToChangesInAccountingPoliciesAndAccountingEstimatesIFRS_edif_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="会計方針の変更・会計上の見積りの変更に関する注記、IFRS")
    """ 会計方針の変更・会計上の見積りの変更に関する注記、IFRS """
    note_to_consolidated_financial_results:NoteToConsolidatedFinancialResults_edif_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="連結業績に関する注記")
    """ 連結業績に関する注記 """
    note_to_dividends:NoteToDividends_edif_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="配当の状況に関する注記")
    """ 配当の状況に関する注記 """
    note_to_financial_positions:NoteToFinancialPositions_edif_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="財政状態に関する注記")
    """ 財政状態に関する注記 """
    note_to_forecasts:NoteToForecasts_edif_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="業績予想に関する事項、注記")
    """ 業績予想に関する事項、注記 """
    note_to_fraction_processing_method:NoteToFractionProcessingMethod_edif_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="端数処理方法に関する注記")
    """ 端数処理方法に関する注記 """
    note_to_number_of_issued_and_outstanding_shares_common_stock:NoteToNumberOfIssuedAndOutstandingSharesCommonStock_edif_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="発行済株式数（普通株式）に関する注記")
    """ 発行済株式数（普通株式）に関する注記 """
    note_to_operating_results:NoteToOperatingResults_edif_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="経営成績に関する注記")
    """ 経営成績に関する注記 """
    note_to_significant_changes_in_the_scope_of_consolidation_during_the_period:NoteToSignificantChangesInTheScopeOfConsolidationDuringThePeriod_edif_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="期中における連結範囲の重要な変更に関する注記")
    """ 期中における連結範囲の重要な変更に関する注記 """
    preamble_to_forecasts:PreambleToForecasts_edif_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="業績予想に関する事項")
    """ 業績予想に関する事項 """
    review_of_attached_consolidated_quarterly_financial_statements_by_a_certified_public_accountant_or_an_audit_firm:ReviewOfAttachedConsolidatedQuarterlyFinancialStatementsByACertifiedPublicAccountantOrAnAuditFirm_edif_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="添付される四半期連結財務諸表に対する公認会計士又は監査法人によるレビュー")
    """ 添付される四半期連結財務諸表に対する公認会計士又は監査法人によるレビュー """
    sapporo_stock_exchange:SapporoStockExchange_edif_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="札幌証券取引所")
    """ 札幌証券取引所 """
    sapporo_stock_exchange_ambitious:SapporoStockExchangeAmbitious_edif_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="札幌証券取引所 アンビシャス")
    """ 札幌証券取引所 アンビシャス """
    sapporo_stock_exchange_established:SapporoStockExchangeEstablished_edif_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="札幌証券取引所 既存市場")
    """ 札幌証券取引所 既存市場 """
    sapporo_stock_exchange_others:SapporoStockExchangeOthers_edif_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="札幌証券取引所 その他")
    """ 札幌証券取引所 その他 """
    securities_code:SecuritiesCode_edif_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="コード番号")
    """ コード番号 """
    significant_changes_in_the_scope_of_consolidation_during_the_period_ifrs:SignificantChangesInTheScopeOfConsolidationDuringThePeriodIFRS_edif_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="期中における連結範囲の重要な変更、IFRS")
    """ 期中における連結範囲の重要な変更、IFRS """
    specific_business:SpecificBusiness_edif_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="特定事業会社")
    """ 特定事業会社 """
    supplemental_material_of_results:SupplementalMaterialOfResults_edif_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="決算補足説明資料作成の有無、期中")
    """ 決算補足説明資料作成の有無、期中 """
    target_for_briefing_of_results:TargetForBriefingOfResults_edif_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="決算説明会の対象者")
    """ 決算説明会の対象者 """
    tel:Tel_edif_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="TEL")
    """ TEL """
    title_for_forecasts:TitleForForecasts_edif_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="業績予想タイトル名称")
    """ 業績予想タイトル名称 """
    title_inquiries:TitleInquiries_edif_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="役職名、問合せ先責任者")
    """ 役職名、問合せ先責任者 """
    title_representative:TitleRepresentative_edif_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="役職名、代表者")
    """ 役職名、代表者 """
    tokyo_stock_exchange:TokyoStockExchange_edif_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="東京証券取引所")
    """ 東京証券取引所 """
    tokyo_stock_exchange_growth:TokyoStockExchangeGrowth_edif_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="東京証券取引所 グロース")
    """ 東京証券取引所 グロース """
    tokyo_stock_exchange_others:TokyoStockExchangeOthers_edif_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="東京証券取引所 その他")
    """ 東京証券取引所 その他 """
    tokyo_stock_exchange_prime:TokyoStockExchangePrime_edif_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="東京証券取引所 プライム")
    """ 東京証券取引所 プライム """
    tokyo_stock_exchange_pro_market:TokyoStockExchangePROMarket_edif_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="東京証券取引所 PRO Market")
    """ 東京証券取引所 PRO Market """
    tokyo_stock_exchange_standard:TokyoStockExchangeStandard_edif_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="東京証券取引所 スタンダード")
    """ 東京証券取引所 スタンダード """
    URL:URL_edif_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="URL")
    """ URL """
    way_of_getting_supplemental_material_of_results:WayOfGettingSupplementalMaterialOfResults_edif_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="入手方法等、決算補足説明資料、期中")
    """ 入手方法等、決算補足説明資料、期中 """


class edif_NotesSegmentInformationCondensedQuarterlyConsolidatedFinancialStatementsIFRS_consolidated_Q2(IxbrlBase):
    description_of_fact_that_companys_business_comprises_single_segment_ifrs:DescriptionOfFactThatCompanysBusinessComprisesSingleSegmentIFRS_edif_NotesSegmentInformationCondensedQuarterlyConsolidatedFinancialStatementsIFRS_consolidated_Q2 = Field(default=None, description="単一セグメントである旨（IFRS）")
    """ 単一セグメントである旨（IFRS） """
    disclosure_of_changes_in_reportable_segments_ifrs_text_block:DisclosureOfChangesInReportableSegmentsIFRSTextBlock_edif_NotesSegmentInformationCondensedQuarterlyConsolidatedFinancialStatementsIFRS_consolidated_Q2 = Field(default=None, description="報告セグメントの変更に関する事項（IFRS） [テキストブロック]")
    """ 報告セグメントの変更に関する事項（IFRS） [テキストブロック] """
    information_about_geographical_areas_ifrs_text_block:InformationAboutGeographicalAreasIFRSTextBlock_edif_NotesSegmentInformationCondensedQuarterlyConsolidatedFinancialStatementsIFRS_consolidated_Q2 = Field(default=None, description="地域に関する情報（IFRS） [テキストブロック]")
    """ 地域に関する情報（IFRS） [テキストブロック] """
    information_about_products_and_services_ifrs_text_block:InformationAboutProductsAndServicesIFRSTextBlock_edif_NotesSegmentInformationCondensedQuarterlyConsolidatedFinancialStatementsIFRS_consolidated_Q2 = Field(default=None, description="製品及びサービスに関する情報（IFRS） [テキストブロック]")
    """ 製品及びサービスに関する情報（IFRS） [テキストブロック] """
    notes_segment_information_condensed_quarterly_consolidated_financial_statements_ifrs_text_block:NotesSegmentInformationCondensedQuarterlyConsolidatedFinancialStatementsIFRSTextBlock_edif_NotesSegmentInformationCondensedQuarterlyConsolidatedFinancialStatementsIFRS_consolidated_Q2 = Field(default=None, description="注記事項－セグメント情報、要約四半期連結財務諸表（IFRS） [テキストブロック]")
    """ 注記事項－セグメント情報、要約四半期連結財務諸表（IFRS） [テキストブロック] """


class edif_NotesSegmentInformationCondensedQuarterlyConsolidatedFinancialStatementsIFRS_consolidated_Q3(IxbrlBase):
    disclosure_of_changes_in_reportable_segments_ifrs_text_block:DisclosureOfChangesInReportableSegmentsIFRSTextBlock_edif_NotesSegmentInformationCondensedQuarterlyConsolidatedFinancialStatementsIFRS_consolidated_Q3 = Field(default=None, description="報告セグメントの変更に関する事項（IFRS） [テキストブロック]")
    """ 報告セグメントの変更に関する事項（IFRS） [テキストブロック] """
    notes_segment_information_condensed_quarterly_consolidated_financial_statements_ifrs_text_block:NotesSegmentInformationCondensedQuarterlyConsolidatedFinancialStatementsIFRSTextBlock_edif_NotesSegmentInformationCondensedQuarterlyConsolidatedFinancialStatementsIFRS_consolidated_Q3 = Field(default=None, description="注記事項－セグメント情報、要約四半期連結財務諸表（IFRS） [テキストブロック]")
    """ 注記事項－セグメント情報、要約四半期連結財務諸表（IFRS） [テキストブロック] """


class edjp_BalanceSheet_Nonconsolidated_FY(IxbrlBase):
    balance_sheet_text_block:BalanceSheetTextBlock_edjp_BalanceSheet_Nonconsolidated_FY = Field(default=None, description="貸借対照表 [テキストブロック]")
    """ 貸借対照表 [テキストブロック] """
    accounting_standards_dei:AccountingStandardsDEI_edjp_BalanceSheet_Nonconsolidated_FY = Field(default=None, description="会計基準、DEI")
    """ 会計基準、DEI """
    amendment_flag_dei:AmendmentFlagDEI_edjp_BalanceSheet_Nonconsolidated_FY = Field(default=None, description="訂正の有無、DEI")
    """ 訂正の有無、DEI """
    cabinet_office_ordinance_dei:CabinetOfficeOrdinanceDEI_edjp_BalanceSheet_Nonconsolidated_FY = Field(default=None, description="府令、DEI")
    """ 府令、DEI """
    comparative_period_end_date_dei:ComparativePeriodEndDateDEI_edjp_BalanceSheet_Nonconsolidated_FY = Field(default=None, description="比較対象会計期間終了日、DEI")
    """ 比較対象会計期間終了日、DEI """
    current_fiscal_year_end_date_dei:CurrentFiscalYearEndDateDEI_edjp_BalanceSheet_Nonconsolidated_FY = Field(default=None, description="当事業年度終了日、DEI")
    """ 当事業年度終了日、DEI """
    current_fiscal_year_start_date_dei:CurrentFiscalYearStartDateDEI_edjp_BalanceSheet_Nonconsolidated_FY = Field(default=None, description="当事業年度開始日、DEI")
    """ 当事業年度開始日、DEI """
    current_period_end_date_dei:CurrentPeriodEndDateDEI_edjp_BalanceSheet_Nonconsolidated_FY = Field(default=None, description="当会計期間終了日、DEI")
    """ 当会計期間終了日、DEI """
    document_type_dei:DocumentTypeDEI_edjp_BalanceSheet_Nonconsolidated_FY = Field(default=None, description="様式、DEI")
    """ 様式、DEI """
    edinet_code_dei:EDINETCodeDEI_edjp_BalanceSheet_Nonconsolidated_FY = Field(default=None, description="EDINETコード、DEI")
    """ EDINETコード、DEI """
    end_date_of_quarterly_or_semi_annual_period_of_next_fiscal_year_dei:EndDateOfQuarterlyOrSemiAnnualPeriodOfNextFiscalYearDEI_edjp_BalanceSheet_Nonconsolidated_FY = Field(default=None, description="次の四半期又は中間期の会計期間終了日、DEI")
    """ 次の四半期又は中間期の会計期間終了日、DEI """
    filer_name_in_english_dei:FilerNameInEnglishDEI_edjp_BalanceSheet_Nonconsolidated_FY = Field(default=None, description="提出者名（英語表記）、DEI")
    """ 提出者名（英語表記）、DEI """
    filer_name_in_japanese_dei:FilerNameInJapaneseDEI_edjp_BalanceSheet_Nonconsolidated_FY = Field(default=None, description="提出者名（日本語表記）、DEI")
    """ 提出者名（日本語表記）、DEI """
    fund_code_dei:FundCodeDEI_edjp_BalanceSheet_Nonconsolidated_FY = Field(default=None, description="ファンドコード、DEI")
    """ ファンドコード、DEI """
    fund_name_in_english_dei:FundNameInEnglishDEI_edjp_BalanceSheet_Nonconsolidated_FY = Field(default=None, description="ファンド名称（英語表記）、DEI")
    """ ファンド名称（英語表記）、DEI """
    fund_name_in_japanese_dei:FundNameInJapaneseDEI_edjp_BalanceSheet_Nonconsolidated_FY = Field(default=None, description="ファンド名称（日本語表記）、DEI")
    """ ファンド名称（日本語表記）、DEI """
    identification_of_document_subject_to_amendment_dei:IdentificationOfDocumentSubjectToAmendmentDEI_edjp_BalanceSheet_Nonconsolidated_FY = Field(default=None, description="訂正対象書類の書類管理番号、DEI")
    """ 訂正対象書類の書類管理番号、DEI """
    industry_code_when_consolidated_financial_statements_are_prepared_in_accordance_with_industry_specific_regulations_dei:IndustryCodeWhenConsolidatedFinancialStatementsArePreparedInAccordanceWithIndustrySpecificRegulationsDEI_edjp_BalanceSheet_Nonconsolidated_FY = Field(default=None, description="別記事業（連結）、DEI")
    """ 別記事業（連結）、DEI """
    industry_code_when_financial_statements_are_prepared_in_accordance_with_industry_specific_regulations_dei:IndustryCodeWhenFinancialStatementsArePreparedInAccordanceWithIndustrySpecificRegulationsDEI_edjp_BalanceSheet_Nonconsolidated_FY = Field(default=None, description="別記事業（個別）、DEI")
    """ 別記事業（個別）、DEI """
    next_fiscal_year_start_date_dei:NextFiscalYearStartDateDEI_edjp_BalanceSheet_Nonconsolidated_FY = Field(default=None, description="次の事業年度開始日、DEI")
    """ 次の事業年度開始日、DEI """
    previous_fiscal_year_end_date_dei:PreviousFiscalYearEndDateDEI_edjp_BalanceSheet_Nonconsolidated_FY = Field(default=None, description="前事業年度終了日、DEI")
    """ 前事業年度終了日、DEI """
    previous_fiscal_year_start_date_dei:PreviousFiscalYearStartDateDEI_edjp_BalanceSheet_Nonconsolidated_FY = Field(default=None, description="前事業年度開始日、DEI")
    """ 前事業年度開始日、DEI """
    report_amendment_flag_dei:ReportAmendmentFlagDEI_edjp_BalanceSheet_Nonconsolidated_FY = Field(default=None, description="記載事項訂正のフラグ、DEI")
    """ 記載事項訂正のフラグ、DEI """
    security_code_dei:SecurityCodeDEI_edjp_BalanceSheet_Nonconsolidated_FY = Field(default=None, description="証券コード、DEI")
    """ 証券コード、DEI """
    type_of_current_period_dei:TypeOfCurrentPeriodDEI_edjp_BalanceSheet_Nonconsolidated_FY = Field(default=None, description="当会計期間の種類、DEI")
    """ 当会計期間の種類、DEI """
    whether_consolidated_financial_statements_are_prepared_dei:WhetherConsolidatedFinancialStatementsArePreparedDEI_edjp_BalanceSheet_Nonconsolidated_FY = Field(default=None, description="連結決算の有無、DEI")
    """ 連結決算の有無、DEI """
    xbrl_amendment_flag_dei:XBRLAmendmentFlagDEI_edjp_BalanceSheet_Nonconsolidated_FY = Field(default=None, description="XBRL訂正のフラグ、DEI")
    """ XBRL訂正のフラグ、DEI """


class edjp_BalanceSheet_consolidated_FY(IxbrlBase):
    balance_sheet_text_block:BalanceSheetTextBlock_edjp_BalanceSheet_consolidated_FY = Field(default=None, description="貸借対照表 [テキストブロック]")
    """ 貸借対照表 [テキストブロック] """


class edjp_ConsolidatedBalanceSheet_consolidated_FY(IxbrlBase):
    consolidated_balance_sheet_text_block:ConsolidatedBalanceSheetTextBlock_edjp_ConsolidatedBalanceSheet_consolidated_FY = Field(default=None, description="連結貸借対照表 [テキストブロック]")
    """ 連結貸借対照表 [テキストブロック] """
    accounting_standards_dei:AccountingStandardsDEI_edjp_ConsolidatedBalanceSheet_consolidated_FY = Field(default=None, description="会計基準、DEI")
    """ 会計基準、DEI """
    amendment_flag_dei:AmendmentFlagDEI_edjp_ConsolidatedBalanceSheet_consolidated_FY = Field(default=None, description="訂正の有無、DEI")
    """ 訂正の有無、DEI """
    cabinet_office_ordinance_dei:CabinetOfficeOrdinanceDEI_edjp_ConsolidatedBalanceSheet_consolidated_FY = Field(default=None, description="府令、DEI")
    """ 府令、DEI """
    comparative_period_end_date_dei:ComparativePeriodEndDateDEI_edjp_ConsolidatedBalanceSheet_consolidated_FY = Field(default=None, description="比較対象会計期間終了日、DEI")
    """ 比較対象会計期間終了日、DEI """
    current_fiscal_year_end_date_dei:CurrentFiscalYearEndDateDEI_edjp_ConsolidatedBalanceSheet_consolidated_FY = Field(default=None, description="当事業年度終了日、DEI")
    """ 当事業年度終了日、DEI """
    current_fiscal_year_start_date_dei:CurrentFiscalYearStartDateDEI_edjp_ConsolidatedBalanceSheet_consolidated_FY = Field(default=None, description="当事業年度開始日、DEI")
    """ 当事業年度開始日、DEI """
    current_period_end_date_dei:CurrentPeriodEndDateDEI_edjp_ConsolidatedBalanceSheet_consolidated_FY = Field(default=None, description="当会計期間終了日、DEI")
    """ 当会計期間終了日、DEI """
    document_type_dei:DocumentTypeDEI_edjp_ConsolidatedBalanceSheet_consolidated_FY = Field(default=None, description="様式、DEI")
    """ 様式、DEI """
    edinet_code_dei:EDINETCodeDEI_edjp_ConsolidatedBalanceSheet_consolidated_FY = Field(default=None, description="EDINETコード、DEI")
    """ EDINETコード、DEI """
    end_date_of_quarterly_or_semi_annual_period_of_next_fiscal_year_dei:EndDateOfQuarterlyOrSemiAnnualPeriodOfNextFiscalYearDEI_edjp_ConsolidatedBalanceSheet_consolidated_FY = Field(default=None, description="次の四半期又は中間期の会計期間終了日、DEI")
    """ 次の四半期又は中間期の会計期間終了日、DEI """
    filer_name_in_english_dei:FilerNameInEnglishDEI_edjp_ConsolidatedBalanceSheet_consolidated_FY = Field(default=None, description="提出者名（英語表記）、DEI")
    """ 提出者名（英語表記）、DEI """
    filer_name_in_japanese_dei:FilerNameInJapaneseDEI_edjp_ConsolidatedBalanceSheet_consolidated_FY = Field(default=None, description="提出者名（日本語表記）、DEI")
    """ 提出者名（日本語表記）、DEI """
    fund_code_dei:FundCodeDEI_edjp_ConsolidatedBalanceSheet_consolidated_FY = Field(default=None, description="ファンドコード、DEI")
    """ ファンドコード、DEI """
    fund_name_in_english_dei:FundNameInEnglishDEI_edjp_ConsolidatedBalanceSheet_consolidated_FY = Field(default=None, description="ファンド名称（英語表記）、DEI")
    """ ファンド名称（英語表記）、DEI """
    fund_name_in_japanese_dei:FundNameInJapaneseDEI_edjp_ConsolidatedBalanceSheet_consolidated_FY = Field(default=None, description="ファンド名称（日本語表記）、DEI")
    """ ファンド名称（日本語表記）、DEI """
    identification_of_document_subject_to_amendment_dei:IdentificationOfDocumentSubjectToAmendmentDEI_edjp_ConsolidatedBalanceSheet_consolidated_FY = Field(default=None, description="訂正対象書類の書類管理番号、DEI")
    """ 訂正対象書類の書類管理番号、DEI """
    industry_code_when_consolidated_financial_statements_are_prepared_in_accordance_with_industry_specific_regulations_dei:IndustryCodeWhenConsolidatedFinancialStatementsArePreparedInAccordanceWithIndustrySpecificRegulationsDEI_edjp_ConsolidatedBalanceSheet_consolidated_FY = Field(default=None, description="別記事業（連結）、DEI")
    """ 別記事業（連結）、DEI """
    industry_code_when_financial_statements_are_prepared_in_accordance_with_industry_specific_regulations_dei:IndustryCodeWhenFinancialStatementsArePreparedInAccordanceWithIndustrySpecificRegulationsDEI_edjp_ConsolidatedBalanceSheet_consolidated_FY = Field(default=None, description="別記事業（個別）、DEI")
    """ 別記事業（個別）、DEI """
    next_fiscal_year_start_date_dei:NextFiscalYearStartDateDEI_edjp_ConsolidatedBalanceSheet_consolidated_FY = Field(default=None, description="次の事業年度開始日、DEI")
    """ 次の事業年度開始日、DEI """
    previous_fiscal_year_end_date_dei:PreviousFiscalYearEndDateDEI_edjp_ConsolidatedBalanceSheet_consolidated_FY = Field(default=None, description="前事業年度終了日、DEI")
    """ 前事業年度終了日、DEI """
    previous_fiscal_year_start_date_dei:PreviousFiscalYearStartDateDEI_edjp_ConsolidatedBalanceSheet_consolidated_FY = Field(default=None, description="前事業年度開始日、DEI")
    """ 前事業年度開始日、DEI """
    report_amendment_flag_dei:ReportAmendmentFlagDEI_edjp_ConsolidatedBalanceSheet_consolidated_FY = Field(default=None, description="記載事項訂正のフラグ、DEI")
    """ 記載事項訂正のフラグ、DEI """
    security_code_dei:SecurityCodeDEI_edjp_ConsolidatedBalanceSheet_consolidated_FY = Field(default=None, description="証券コード、DEI")
    """ 証券コード、DEI """
    type_of_current_period_dei:TypeOfCurrentPeriodDEI_edjp_ConsolidatedBalanceSheet_consolidated_FY = Field(default=None, description="当会計期間の種類、DEI")
    """ 当会計期間の種類、DEI """
    whether_consolidated_financial_statements_are_prepared_dei:WhetherConsolidatedFinancialStatementsArePreparedDEI_edjp_ConsolidatedBalanceSheet_consolidated_FY = Field(default=None, description="連結決算の有無、DEI")
    """ 連結決算の有無、DEI """
    xbrl_amendment_flag_dei:XBRLAmendmentFlagDEI_edjp_ConsolidatedBalanceSheet_consolidated_FY = Field(default=None, description="XBRL訂正のフラグ、DEI")
    """ XBRL訂正のフラグ、DEI """


class edjp_ConsolidatedStatementOfCashFlows_consolidated_FY(IxbrlBase):
    consolidated_statement_of_cash_flows_text_block:ConsolidatedStatementOfCashFlowsTextBlock_edjp_ConsolidatedStatementOfCashFlows_consolidated_FY = Field(default=None, description="連結キャッシュ・フロー計算書 [テキストブロック]")
    """ 連結キャッシュ・フロー計算書 [テキストブロック] """


class edjp_ConsolidatedStatementOfChangesInEquity_consolidated_FY(IxbrlBase):
    consolidated_statement_of_changes_in_equity_text_block:ConsolidatedStatementOfChangesInEquityTextBlock_edjp_ConsolidatedStatementOfChangesInEquity_consolidated_FY = Field(default=None, description="連結株主資本等変動計算書 [テキストブロック]")
    """ 連結株主資本等変動計算書 [テキストブロック] """


class edjp_ConsolidatedStatementOfComprehensiveIncome_consolidated_FY(IxbrlBase):
    consolidated_statement_of_comprehensive_income_text_block:ConsolidatedStatementOfComprehensiveIncomeTextBlock_edjp_ConsolidatedStatementOfComprehensiveIncome_consolidated_FY = Field(default=None, description="連結包括利益計算書 [テキストブロック]")
    """ 連結包括利益計算書 [テキストブロック] """


class edjp_ConsolidatedStatementOfIncome_consolidated_FY(IxbrlBase):
    consolidated_statement_of_income_text_block:ConsolidatedStatementOfIncomeTextBlock_edjp_ConsolidatedStatementOfIncome_consolidated_FY = Field(default=None, description="連結損益計算書 [テキストブロック]")
    """ 連結損益計算書 [テキストブロック] """


class edjp_FinancialReportSummary_Nonconsolidated_FY(IxbrlBase):
    annual_securities_report_filing_date_as_planned:AnnualSecuritiesReportFilingDateAsPlanned_edjp_FinancialReportSummary_Nonconsolidated_FY = Field(default=None, description="有価証券報告書提出予定日")
    """ 有価証券報告書提出予定日 """
    changes_based_on_revisions_of_accounting_standard:ChangesBasedOnRevisionsOfAccountingStandard_edjp_FinancialReportSummary_Nonconsolidated_FY = Field(default=None, description="会計基準等の改正に伴う会計方針の変更")
    """ 会計基準等の改正に伴う会計方針の変更 """
    changes_in_accounting_estimates:ChangesInAccountingEstimates_edjp_FinancialReportSummary_Nonconsolidated_FY = Field(default=None, description="会計上の見積りの変更")
    """ 会計上の見積りの変更 """
    changes_other_than_ones_based_on_revisions_of_accounting_standard:ChangesOtherThanOnesBasedOnRevisionsOfAccountingStandard_edjp_FinancialReportSummary_Nonconsolidated_FY = Field(default=None, description="会計基準等の改正に伴う変更以外の会計方針の変更")
    """ 会計基準等の改正に伴う変更以外の会計方針の変更 """
    company_name:CompanyName_edjp_FinancialReportSummary_Nonconsolidated_FY = Field(default=None, description="上場会社名")
    """ 上場会社名 """
    convening_briefing_of_annual_results:ConveningBriefingOfAnnualResults_edjp_FinancialReportSummary_Nonconsolidated_FY = Field(default=None, description="決算説明会開催の有無")
    """ 決算説明会開催の有無 """
    date_of_general_shareholders_meeting_as_planned:DateOfGeneralShareholdersMeetingAsPlanned_edjp_FinancialReportSummary_Nonconsolidated_FY = Field(default=None, description="定時株主総会開催予定日")
    """ 定時株主総会開催予定日 """
    dividend_payable_date_as_planned:DividendPayableDateAsPlanned_edjp_FinancialReportSummary_Nonconsolidated_FY = Field(default=None, description="配当支払開始予定日")
    """ 配当支払開始予定日 """
    document_name:DocumentName_edjp_FinancialReportSummary_Nonconsolidated_FY = Field(default=None, description="文書名")
    """ 文書名 """
    fasf_member_mark:FASFMemberMark_edjp_FinancialReportSummary_Nonconsolidated_FY = Field(default=None, description="財務会計基準機構会員マーク")
    """ 財務会計基準機構会員マーク """
    filing_date:FilingDate_edjp_FinancialReportSummary_Nonconsolidated_FY = Field(default=None, description="提出日")
    """ 提出日 """
    fiscal_year_end:FiscalYearEnd_edjp_FinancialReportSummary_Nonconsolidated_FY = Field(default=None, description="決算期")
    """ 決算期 """
    fukuoka_stock_exchange:FukuokaStockExchange_edjp_FinancialReportSummary_Nonconsolidated_FY = Field(default=None, description="福岡証券取引所")
    """ 福岡証券取引所 """
    fukuoka_stock_exchange_established:FukuokaStockExchangeEstablished_edjp_FinancialReportSummary_Nonconsolidated_FY = Field(default=None, description="福岡証券取引所 既存市場")
    """ 福岡証券取引所 既存市場 """
    fukuoka_stock_exchange_others:FukuokaStockExchangeOthers_edjp_FinancialReportSummary_Nonconsolidated_FY = Field(default=None, description="福岡証券取引所 その他")
    """ 福岡証券取引所 その他 """
    fukuoka_stock_exchange_q_board:FukuokaStockExchangeQBoard_edjp_FinancialReportSummary_Nonconsolidated_FY = Field(default=None, description="福岡証券取引所 Q-Board")
    """ 福岡証券取引所 Q-Board """
    general_business:GeneralBusiness_edjp_FinancialReportSummary_Nonconsolidated_FY = Field(default=None, description="一般事業会社")
    """ 一般事業会社 """
    japan_securities_dealers_association:JapanSecuritiesDealersAssociation_edjp_FinancialReportSummary_Nonconsolidated_FY = Field(default=None, description="フェニックス")
    """ フェニックス """
    japan_securities_dealers_association_green_sheet:JapanSecuritiesDealersAssociationGreenSheet_edjp_FinancialReportSummary_Nonconsolidated_FY = Field(default=None, description="日本証券業協会 フェニックス")
    """ 日本証券業協会 フェニックス """
    nagoya_stock_exchange:NagoyaStockExchange_edjp_FinancialReportSummary_Nonconsolidated_FY = Field(default=None, description="名古屋証券取引所")
    """ 名古屋証券取引所 """
    nagoya_stock_exchange1st_section:NagoyaStockExchange1stSection_edjp_FinancialReportSummary_Nonconsolidated_FY = Field(default=None, description="名古屋証券取引所 プレミア")
    """ 名古屋証券取引所 プレミア """
    nagoya_stock_exchange2nd_section:NagoyaStockExchange2ndSection_edjp_FinancialReportSummary_Nonconsolidated_FY = Field(default=None, description="名古屋証券取引所 メイン")
    """ 名古屋証券取引所 メイン """
    nagoya_stock_exchange_centrex:NagoyaStockExchangeCentrex_edjp_FinancialReportSummary_Nonconsolidated_FY = Field(default=None, description="名古屋証券取引所 ネクスト")
    """ 名古屋証券取引所 ネクスト """
    nagoya_stock_exchange_others:NagoyaStockExchangeOthers_edjp_FinancialReportSummary_Nonconsolidated_FY = Field(default=None, description="名古屋証券取引所 その他")
    """ 名古屋証券取引所 その他 """
    name_inquiries:NameInquiries_edjp_FinancialReportSummary_Nonconsolidated_FY = Field(default=None, description="氏名、問合せ先責任者")
    """ 氏名、問合せ先責任者 """
    name_representative:NameRepresentative_edjp_FinancialReportSummary_Nonconsolidated_FY = Field(default=None, description="氏名、代表者")
    """ 氏名、代表者 """
    notes_for_using_forecasted_information_and_others:NotesForUsingForecastedInformationAndOthers_edjp_FinancialReportSummary_Nonconsolidated_FY = Field(default=None, description="業績予想の適切な利用に関する説明、その他特記事項")
    """ 業績予想の適切な利用に関する説明、その他特記事項 """
    note_to_changes_in_accounting_policies_and_accounting_estimates_retrospective_restatement:NoteToChangesInAccountingPoliciesAndAccountingEstimatesRetrospectiveRestatement_edjp_FinancialReportSummary_Nonconsolidated_FY = Field(default=None, description="会計方針の変更・会計上の見積りの変更・修正再表示に関する注記")
    """ 会計方針の変更・会計上の見積りの変更・修正再表示に関する注記 """
    note_to_financial_positions:NoteToFinancialPositions_edjp_FinancialReportSummary_Nonconsolidated_FY = Field(default=None, description="財政状態に関する注記")
    """ 財政状態に関する注記 """
    note_to_forecasts:NoteToForecasts_edjp_FinancialReportSummary_Nonconsolidated_FY = Field(default=None, description="業績予想に関する事項、注記")
    """ 業績予想に関する事項、注記 """
    note_to_fraction_processing_method:NoteToFractionProcessingMethod_edjp_FinancialReportSummary_Nonconsolidated_FY = Field(default=None, description="端数処理方法に関する注記")
    """ 端数処理方法に関する注記 """
    note_to_number_of_issued_and_outstanding_shares_common_stock:NoteToNumberOfIssuedAndOutstandingSharesCommonStock_edjp_FinancialReportSummary_Nonconsolidated_FY = Field(default=None, description="発行済株式数（普通株式）に関する注記")
    """ 発行済株式数（普通株式）に関する注記 """
    note_to_operating_results:NoteToOperatingResults_edjp_FinancialReportSummary_Nonconsolidated_FY = Field(default=None, description="経営成績に関する注記")
    """ 経営成績に関する注記 """
    preamble_to_forecasts:PreambleToForecasts_edjp_FinancialReportSummary_Nonconsolidated_FY = Field(default=None, description="業績予想に関する事項")
    """ 業績予想に関する事項 """
    retrospective_restatement:RetrospectiveRestatement_edjp_FinancialReportSummary_Nonconsolidated_FY = Field(default=None, description="修正再表示")
    """ 修正再表示 """
    sapporo_stock_exchange:SapporoStockExchange_edjp_FinancialReportSummary_Nonconsolidated_FY = Field(default=None, description="札幌証券取引所")
    """ 札幌証券取引所 """
    sapporo_stock_exchange_ambitious:SapporoStockExchangeAmbitious_edjp_FinancialReportSummary_Nonconsolidated_FY = Field(default=None, description="札幌証券取引所 アンビシャス")
    """ 札幌証券取引所 アンビシャス """
    sapporo_stock_exchange_established:SapporoStockExchangeEstablished_edjp_FinancialReportSummary_Nonconsolidated_FY = Field(default=None, description="札幌証券取引所 既存市場")
    """ 札幌証券取引所 既存市場 """
    sapporo_stock_exchange_others:SapporoStockExchangeOthers_edjp_FinancialReportSummary_Nonconsolidated_FY = Field(default=None, description="札幌証券取引所 その他")
    """ 札幌証券取引所 その他 """
    securities_code:SecuritiesCode_edjp_FinancialReportSummary_Nonconsolidated_FY = Field(default=None, description="コード番号")
    """ コード番号 """
    specific_business:SpecificBusiness_edjp_FinancialReportSummary_Nonconsolidated_FY = Field(default=None, description="特定事業会社")
    """ 特定事業会社 """
    supplemental_material_of_annual_results:SupplementalMaterialOfAnnualResults_edjp_FinancialReportSummary_Nonconsolidated_FY = Field(default=None, description="決算補足説明資料作成の有無")
    """ 決算補足説明資料作成の有無 """
    target_audience_briefing_of_annual_results:TargetAudienceBriefingOfAnnualResults_edjp_FinancialReportSummary_Nonconsolidated_FY = Field(default=None, description="対象者、決算説明会")
    """ 対象者、決算説明会 """
    tel:Tel_edjp_FinancialReportSummary_Nonconsolidated_FY = Field(default=None, description="TEL")
    """ TEL """
    title_for_forecasts:TitleForForecasts_edjp_FinancialReportSummary_Nonconsolidated_FY = Field(default=None, description="業績予想タイトル名称")
    """ 業績予想タイトル名称 """
    title_inquiries:TitleInquiries_edjp_FinancialReportSummary_Nonconsolidated_FY = Field(default=None, description="役職名、問合せ先責任者")
    """ 役職名、問合せ先責任者 """
    title_representative:TitleRepresentative_edjp_FinancialReportSummary_Nonconsolidated_FY = Field(default=None, description="役職名、代表者")
    """ 役職名、代表者 """
    tokyo_stock_exchange:TokyoStockExchange_edjp_FinancialReportSummary_Nonconsolidated_FY = Field(default=None, description="東京証券取引所")
    """ 東京証券取引所 """
    tokyo_stock_exchange1st_section:TokyoStockExchange1stSection_edjp_FinancialReportSummary_Nonconsolidated_FY = Field(default=None, description="東京証券取引所 第一部")
    """ 東京証券取引所 第一部 """
    tokyo_stock_exchange2nd_section:TokyoStockExchange2ndSection_edjp_FinancialReportSummary_Nonconsolidated_FY = Field(default=None, description="東京証券取引所 第二部")
    """ 東京証券取引所 第二部 """
    tokyo_stock_exchange_growth:TokyoStockExchangeGrowth_edjp_FinancialReportSummary_Nonconsolidated_FY = Field(default=None, description="東京証券取引所 グロース")
    """ 東京証券取引所 グロース """
    tokyo_stock_exchange_jasdaq:TokyoStockExchangeJASDAQ_edjp_FinancialReportSummary_Nonconsolidated_FY = Field(default=None, description="東京証券取引所 JASDAQ")
    """ 東京証券取引所 JASDAQ """
    tokyo_stock_exchange_mothers:TokyoStockExchangeMothers_edjp_FinancialReportSummary_Nonconsolidated_FY = Field(default=None, description="東京証券取引所 マザーズ")
    """ 東京証券取引所 マザーズ """
    tokyo_stock_exchange_others:TokyoStockExchangeOthers_edjp_FinancialReportSummary_Nonconsolidated_FY = Field(default=None, description="東京証券取引所 その他")
    """ 東京証券取引所 その他 """
    tokyo_stock_exchange_prime:TokyoStockExchangePrime_edjp_FinancialReportSummary_Nonconsolidated_FY = Field(default=None, description="東京証券取引所 プライム")
    """ 東京証券取引所 プライム """
    tokyo_stock_exchange_pro_market:TokyoStockExchangePROMarket_edjp_FinancialReportSummary_Nonconsolidated_FY = Field(default=None, description="東京証券取引所 PRO Market")
    """ 東京証券取引所 PRO Market """
    tokyo_stock_exchange_standard:TokyoStockExchangeStandard_edjp_FinancialReportSummary_Nonconsolidated_FY = Field(default=None, description="東京証券取引所 スタンダード")
    """ 東京証券取引所 スタンダード """
    URL:URL_edjp_FinancialReportSummary_Nonconsolidated_FY = Field(default=None, description="URL")
    """ URL """
    way_of_getting_supplemental_material_of_annual_results:WayOfGettingSupplementalMaterialOfAnnualResults_edjp_FinancialReportSummary_Nonconsolidated_FY = Field(default=None, description="入手方法等、決算補足説明資料")
    """ 入手方法等、決算補足説明資料 """


class edjp_FinancialReportSummary_consolidated_FY(IxbrlBase):
    annual_securities_report_filing_date_as_planned:AnnualSecuritiesReportFilingDateAsPlanned_edjp_FinancialReportSummary_consolidated_FY = Field(default=None, description="有価証券報告書提出予定日")
    """ 有価証券報告書提出予定日 """
    changes_based_on_revisions_of_accounting_standard:ChangesBasedOnRevisionsOfAccountingStandard_edjp_FinancialReportSummary_consolidated_FY = Field(default=None, description="会計基準等の改正に伴う会計方針の変更")
    """ 会計基準等の改正に伴う会計方針の変更 """
    changes_in_accounting_estimates:ChangesInAccountingEstimates_edjp_FinancialReportSummary_consolidated_FY = Field(default=None, description="会計上の見積りの変更")
    """ 会計上の見積りの変更 """
    changes_other_than_ones_based_on_revisions_of_accounting_standard:ChangesOtherThanOnesBasedOnRevisionsOfAccountingStandard_edjp_FinancialReportSummary_consolidated_FY = Field(default=None, description="会計基準等の改正に伴う変更以外の会計方針の変更")
    """ 会計基準等の改正に伴う変更以外の会計方針の変更 """
    company_name:CompanyName_edjp_FinancialReportSummary_consolidated_FY = Field(default=None, description="上場会社名")
    """ 上場会社名 """
    convening_briefing_of_annual_results:ConveningBriefingOfAnnualResults_edjp_FinancialReportSummary_consolidated_FY = Field(default=None, description="決算説明会開催の有無")
    """ 決算説明会開催の有無 """
    date_of_general_shareholders_meeting_as_planned:DateOfGeneralShareholdersMeetingAsPlanned_edjp_FinancialReportSummary_consolidated_FY = Field(default=None, description="定時株主総会開催予定日")
    """ 定時株主総会開催予定日 """
    dividend_payable_date_as_planned:DividendPayableDateAsPlanned_edjp_FinancialReportSummary_consolidated_FY = Field(default=None, description="配当支払開始予定日")
    """ 配当支払開始予定日 """
    document_name:DocumentName_edjp_FinancialReportSummary_consolidated_FY = Field(default=None, description="文書名")
    """ 文書名 """
    fasf_member_mark:FASFMemberMark_edjp_FinancialReportSummary_consolidated_FY = Field(default=None, description="財務会計基準機構会員マーク")
    """ 財務会計基準機構会員マーク """
    filing_date:FilingDate_edjp_FinancialReportSummary_consolidated_FY = Field(default=None, description="提出日")
    """ 提出日 """
    fiscal_year_end:FiscalYearEnd_edjp_FinancialReportSummary_consolidated_FY = Field(default=None, description="決算期")
    """ 決算期 """
    fukuoka_stock_exchange:FukuokaStockExchange_edjp_FinancialReportSummary_consolidated_FY = Field(default=None, description="福岡証券取引所")
    """ 福岡証券取引所 """
    fukuoka_stock_exchange_established:FukuokaStockExchangeEstablished_edjp_FinancialReportSummary_consolidated_FY = Field(default=None, description="福岡証券取引所 既存市場")
    """ 福岡証券取引所 既存市場 """
    fukuoka_stock_exchange_others:FukuokaStockExchangeOthers_edjp_FinancialReportSummary_consolidated_FY = Field(default=None, description="福岡証券取引所 その他")
    """ 福岡証券取引所 その他 """
    fukuoka_stock_exchange_q_board:FukuokaStockExchangeQBoard_edjp_FinancialReportSummary_consolidated_FY = Field(default=None, description="福岡証券取引所 Q-Board")
    """ 福岡証券取引所 Q-Board """
    general_business:GeneralBusiness_edjp_FinancialReportSummary_consolidated_FY = Field(default=None, description="一般事業会社")
    """ 一般事業会社 """
    japan_securities_dealers_association:JapanSecuritiesDealersAssociation_edjp_FinancialReportSummary_consolidated_FY = Field(default=None, description="フェニックス")
    """ フェニックス """
    japan_securities_dealers_association_green_sheet:JapanSecuritiesDealersAssociationGreenSheet_edjp_FinancialReportSummary_consolidated_FY = Field(default=None, description="日本証券業協会 フェニックス")
    """ 日本証券業協会 フェニックス """
    nagoya_stock_exchange:NagoyaStockExchange_edjp_FinancialReportSummary_consolidated_FY = Field(default=None, description="名古屋証券取引所")
    """ 名古屋証券取引所 """
    nagoya_stock_exchange1st_section:NagoyaStockExchange1stSection_edjp_FinancialReportSummary_consolidated_FY = Field(default=None, description="名古屋証券取引所 プレミア")
    """ 名古屋証券取引所 プレミア """
    nagoya_stock_exchange2nd_section:NagoyaStockExchange2ndSection_edjp_FinancialReportSummary_consolidated_FY = Field(default=None, description="名古屋証券取引所 メイン")
    """ 名古屋証券取引所 メイン """
    nagoya_stock_exchange_centrex:NagoyaStockExchangeCentrex_edjp_FinancialReportSummary_consolidated_FY = Field(default=None, description="名古屋証券取引所 ネクスト")
    """ 名古屋証券取引所 ネクスト """
    nagoya_stock_exchange_others:NagoyaStockExchangeOthers_edjp_FinancialReportSummary_consolidated_FY = Field(default=None, description="名古屋証券取引所 その他")
    """ 名古屋証券取引所 その他 """
    name_inquiries:NameInquiries_edjp_FinancialReportSummary_consolidated_FY = Field(default=None, description="氏名、問合せ先責任者")
    """ 氏名、問合せ先責任者 """
    name_of_subsidiaries_excluded_from_consolidation:NameOfSubsidiariesExcludedFromConsolidation_edjp_FinancialReportSummary_consolidated_FY = Field(default=None, description="社名、除外")
    """ 社名、除外 """
    name_of_subsidiaries_newly_consolidated:NameOfSubsidiariesNewlyConsolidated_edjp_FinancialReportSummary_consolidated_FY = Field(default=None, description="社名、新規")
    """ 社名、新規 """
    name_representative:NameRepresentative_edjp_FinancialReportSummary_consolidated_FY = Field(default=None, description="氏名、代表者")
    """ 氏名、代表者 """
    notes_for_using_forecasted_information_and_others:NotesForUsingForecastedInformationAndOthers_edjp_FinancialReportSummary_consolidated_FY = Field(default=None, description="業績予想の適切な利用に関する説明、その他特記事項")
    """ 業績予想の適切な利用に関する説明、その他特記事項 """
    note_to_cash_flows:NoteToCashFlows_edjp_FinancialReportSummary_consolidated_FY = Field(default=None, description="キャッシュ・フローの状況に関する注記")
    """ キャッシュ・フローの状況に関する注記 """
    note_to_changes_in_accounting_policies_and_accounting_estimates_retrospective_restatement:NoteToChangesInAccountingPoliciesAndAccountingEstimatesRetrospectiveRestatement_edjp_FinancialReportSummary_consolidated_FY = Field(default=None, description="会計方針の変更・会計上の見積りの変更・修正再表示に関する注記")
    """ 会計方針の変更・会計上の見積りの変更・修正再表示に関する注記 """
    note_to_consolidated_financial_results:NoteToConsolidatedFinancialResults_edjp_FinancialReportSummary_consolidated_FY = Field(default=None, description="連結業績に関する注記")
    """ 連結業績に関する注記 """
    note_to_dividends:NoteToDividends_edjp_FinancialReportSummary_consolidated_FY = Field(default=None, description="配当の状況に関する注記")
    """ 配当の状況に関する注記 """
    note_to_financial_positions:NoteToFinancialPositions_edjp_FinancialReportSummary_consolidated_FY = Field(default=None, description="財政状態に関する注記")
    """ 財政状態に関する注記 """
    note_to_financial_results:NoteToFinancialResults_edjp_FinancialReportSummary_consolidated_FY = Field(default=None, description="業績に関する注記")
    """ 業績に関する注記 """
    note_to_forecasts:NoteToForecasts_edjp_FinancialReportSummary_consolidated_FY = Field(default=None, description="業績予想に関する事項、注記")
    """ 業績予想に関する事項、注記 """
    note_to_fraction_processing_method:NoteToFractionProcessingMethod_edjp_FinancialReportSummary_consolidated_FY = Field(default=None, description="端数処理方法に関する注記")
    """ 端数処理方法に関する注記 """
    note_to_number_of_issued_and_outstanding_shares_common_stock:NoteToNumberOfIssuedAndOutstandingSharesCommonStock_edjp_FinancialReportSummary_consolidated_FY = Field(default=None, description="発行済株式数（普通株式）に関する注記")
    """ 発行済株式数（普通株式）に関する注記 """
    note_to_operating_results:NoteToOperatingResults_edjp_FinancialReportSummary_consolidated_FY = Field(default=None, description="経営成績に関する注記")
    """ 経営成績に関する注記 """
    note_to_significant_changes_in_the_scope_of_consolidation_during_the_period:NoteToSignificantChangesInTheScopeOfConsolidationDuringThePeriod_edjp_FinancialReportSummary_consolidated_FY = Field(default=None, description="期中における連結範囲の重要な変更に関する注記")
    """ 期中における連結範囲の重要な変更に関する注記 """
    preamble_to_forecasts:PreambleToForecasts_edjp_FinancialReportSummary_consolidated_FY = Field(default=None, description="業績予想に関する事項")
    """ 業績予想に関する事項 """
    retrospective_restatement:RetrospectiveRestatement_edjp_FinancialReportSummary_consolidated_FY = Field(default=None, description="修正再表示")
    """ 修正再表示 """
    sapporo_stock_exchange:SapporoStockExchange_edjp_FinancialReportSummary_consolidated_FY = Field(default=None, description="札幌証券取引所")
    """ 札幌証券取引所 """
    sapporo_stock_exchange_ambitious:SapporoStockExchangeAmbitious_edjp_FinancialReportSummary_consolidated_FY = Field(default=None, description="札幌証券取引所 アンビシャス")
    """ 札幌証券取引所 アンビシャス """
    sapporo_stock_exchange_established:SapporoStockExchangeEstablished_edjp_FinancialReportSummary_consolidated_FY = Field(default=None, description="札幌証券取引所 既存市場")
    """ 札幌証券取引所 既存市場 """
    sapporo_stock_exchange_others:SapporoStockExchangeOthers_edjp_FinancialReportSummary_consolidated_FY = Field(default=None, description="札幌証券取引所 その他")
    """ 札幌証券取引所 その他 """
    securities_code:SecuritiesCode_edjp_FinancialReportSummary_consolidated_FY = Field(default=None, description="コード番号")
    """ コード番号 """
    significant_changes_in_the_scope_of_consolidation_during_the_period:SignificantChangesInTheScopeOfConsolidationDuringThePeriod_edjp_FinancialReportSummary_consolidated_FY = Field(default=None, description="期中における連結範囲の重要な変更")
    """ 期中における連結範囲の重要な変更 """
    specific_business:SpecificBusiness_edjp_FinancialReportSummary_consolidated_FY = Field(default=None, description="特定事業会社")
    """ 特定事業会社 """
    supplemental_material_of_annual_results:SupplementalMaterialOfAnnualResults_edjp_FinancialReportSummary_consolidated_FY = Field(default=None, description="決算補足説明資料作成の有無")
    """ 決算補足説明資料作成の有無 """
    target_audience_briefing_of_annual_results:TargetAudienceBriefingOfAnnualResults_edjp_FinancialReportSummary_consolidated_FY = Field(default=None, description="対象者、決算説明会")
    """ 対象者、決算説明会 """
    tel:Tel_edjp_FinancialReportSummary_consolidated_FY = Field(default=None, description="TEL")
    """ TEL """
    title_for_forecasts:TitleForForecasts_edjp_FinancialReportSummary_consolidated_FY = Field(default=None, description="業績予想タイトル名称")
    """ 業績予想タイトル名称 """
    title_inquiries:TitleInquiries_edjp_FinancialReportSummary_consolidated_FY = Field(default=None, description="役職名、問合せ先責任者")
    """ 役職名、問合せ先責任者 """
    title_representative:TitleRepresentative_edjp_FinancialReportSummary_consolidated_FY = Field(default=None, description="役職名、代表者")
    """ 役職名、代表者 """
    tokyo_stock_exchange:TokyoStockExchange_edjp_FinancialReportSummary_consolidated_FY = Field(default=None, description="東京証券取引所")
    """ 東京証券取引所 """
    tokyo_stock_exchange1st_section:TokyoStockExchange1stSection_edjp_FinancialReportSummary_consolidated_FY = Field(default=None, description="東京証券取引所 第一部")
    """ 東京証券取引所 第一部 """
    tokyo_stock_exchange2nd_section:TokyoStockExchange2ndSection_edjp_FinancialReportSummary_consolidated_FY = Field(default=None, description="東京証券取引所 第二部")
    """ 東京証券取引所 第二部 """
    tokyo_stock_exchange_growth:TokyoStockExchangeGrowth_edjp_FinancialReportSummary_consolidated_FY = Field(default=None, description="東京証券取引所 グロース")
    """ 東京証券取引所 グロース """
    tokyo_stock_exchange_jasdaq:TokyoStockExchangeJASDAQ_edjp_FinancialReportSummary_consolidated_FY = Field(default=None, description="東京証券取引所 JASDAQ")
    """ 東京証券取引所 JASDAQ """
    tokyo_stock_exchange_mothers:TokyoStockExchangeMothers_edjp_FinancialReportSummary_consolidated_FY = Field(default=None, description="東京証券取引所 マザーズ")
    """ 東京証券取引所 マザーズ """
    tokyo_stock_exchange_others:TokyoStockExchangeOthers_edjp_FinancialReportSummary_consolidated_FY = Field(default=None, description="東京証券取引所 その他")
    """ 東京証券取引所 その他 """
    tokyo_stock_exchange_prime:TokyoStockExchangePrime_edjp_FinancialReportSummary_consolidated_FY = Field(default=None, description="東京証券取引所 プライム")
    """ 東京証券取引所 プライム """
    tokyo_stock_exchange_pro_market:TokyoStockExchangePROMarket_edjp_FinancialReportSummary_consolidated_FY = Field(default=None, description="東京証券取引所 PRO Market")
    """ 東京証券取引所 PRO Market """
    tokyo_stock_exchange_standard:TokyoStockExchangeStandard_edjp_FinancialReportSummary_consolidated_FY = Field(default=None, description="東京証券取引所 スタンダード")
    """ 東京証券取引所 スタンダード """
    URL:URL_edjp_FinancialReportSummary_consolidated_FY = Field(default=None, description="URL")
    """ URL """
    way_of_getting_supplemental_material_of_annual_results:WayOfGettingSupplementalMaterialOfAnnualResults_edjp_FinancialReportSummary_consolidated_FY = Field(default=None, description="入手方法等、決算補足説明資料")
    """ 入手方法等、決算補足説明資料 """


class edjp_FinancialReportSummary_consolidated_Q1(IxbrlBase):
    applying_of_specific_accounting_of_the_consolidated_quarterly_financial_statements:ApplyingOfSpecificAccountingOfTheConsolidatedQuarterlyFinancialStatements_edjp_FinancialReportSummary_consolidated_Q1 = Field(default=None, description="四半期連結財務諸表の作成に特有の会計処理の適用")
    """ 四半期連結財務諸表の作成に特有の会計処理の適用 """
    changes_based_on_revisions_of_accounting_standard:ChangesBasedOnRevisionsOfAccountingStandard_edjp_FinancialReportSummary_consolidated_Q1 = Field(default=None, description="会計基準等の改正に伴う会計方針の変更")
    """ 会計基準等の改正に伴う会計方針の変更 """
    changes_in_accounting_estimates:ChangesInAccountingEstimates_edjp_FinancialReportSummary_consolidated_Q1 = Field(default=None, description="会計上の見積りの変更")
    """ 会計上の見積りの変更 """
    changes_other_than_ones_based_on_revisions_of_accounting_standard:ChangesOtherThanOnesBasedOnRevisionsOfAccountingStandard_edjp_FinancialReportSummary_consolidated_Q1 = Field(default=None, description="会計基準等の改正に伴う変更以外の会計方針の変更")
    """ 会計基準等の改正に伴う変更以外の会計方針の変更 """
    company_name:CompanyName_edjp_FinancialReportSummary_consolidated_Q1 = Field(default=None, description="上場会社名")
    """ 上場会社名 """
    convening_briefing_of_results:ConveningBriefingOfResults_edjp_FinancialReportSummary_consolidated_Q1 = Field(default=None, description="決算説明会開催の有無、期中")
    """ 決算説明会開催の有無、期中 """
    correction_of_consolidated_financial_forecast_in_this_quarter:CorrectionOfConsolidatedFinancialForecastInThisQuarter_edjp_FinancialReportSummary_consolidated_Q1 = Field(default=None, description="直近に公表されている業績予想からの修正の有無、連結")
    """ 直近に公表されている業績予想からの修正の有無、連結 """
    correction_of_dividend_forecast_in_this_quarter:CorrectionOfDividendForecastInThisQuarter_edjp_FinancialReportSummary_consolidated_Q1 = Field(default=None, description="直近に公表されている配当予想からの修正の有無")
    """ 直近に公表されている配当予想からの修正の有無 """
    dividend_payable_date_as_planned:DividendPayableDateAsPlanned_edjp_FinancialReportSummary_consolidated_Q1 = Field(default=None, description="配当支払開始予定日")
    """ 配当支払開始予定日 """
    document_name:DocumentName_edjp_FinancialReportSummary_consolidated_Q1 = Field(default=None, description="文書名")
    """ 文書名 """
    fasf_member_mark:FASFMemberMark_edjp_FinancialReportSummary_consolidated_Q1 = Field(default=None, description="財務会計基準機構会員マーク")
    """ 財務会計基準機構会員マーク """
    filing_date:FilingDate_edjp_FinancialReportSummary_consolidated_Q1 = Field(default=None, description="提出日")
    """ 提出日 """
    fiscal_year_end:FiscalYearEnd_edjp_FinancialReportSummary_consolidated_Q1 = Field(default=None, description="決算期")
    """ 決算期 """
    fukuoka_stock_exchange:FukuokaStockExchange_edjp_FinancialReportSummary_consolidated_Q1 = Field(default=None, description="福岡証券取引所")
    """ 福岡証券取引所 """
    fukuoka_stock_exchange_established:FukuokaStockExchangeEstablished_edjp_FinancialReportSummary_consolidated_Q1 = Field(default=None, description="福岡証券取引所 既存市場")
    """ 福岡証券取引所 既存市場 """
    fukuoka_stock_exchange_others:FukuokaStockExchangeOthers_edjp_FinancialReportSummary_consolidated_Q1 = Field(default=None, description="福岡証券取引所 その他")
    """ 福岡証券取引所 その他 """
    fukuoka_stock_exchange_q_board:FukuokaStockExchangeQBoard_edjp_FinancialReportSummary_consolidated_Q1 = Field(default=None, description="福岡証券取引所 Q-Board")
    """ 福岡証券取引所 Q-Board """
    general_business:GeneralBusiness_edjp_FinancialReportSummary_consolidated_Q1 = Field(default=None, description="一般事業会社")
    """ 一般事業会社 """
    japan_securities_dealers_association:JapanSecuritiesDealersAssociation_edjp_FinancialReportSummary_consolidated_Q1 = Field(default=None, description="フェニックス")
    """ フェニックス """
    japan_securities_dealers_association_green_sheet:JapanSecuritiesDealersAssociationGreenSheet_edjp_FinancialReportSummary_consolidated_Q1 = Field(default=None, description="日本証券業協会 フェニックス")
    """ 日本証券業協会 フェニックス """
    nagoya_stock_exchange:NagoyaStockExchange_edjp_FinancialReportSummary_consolidated_Q1 = Field(default=None, description="名古屋証券取引所")
    """ 名古屋証券取引所 """
    nagoya_stock_exchange1st_section:NagoyaStockExchange1stSection_edjp_FinancialReportSummary_consolidated_Q1 = Field(default=None, description="名古屋証券取引所 プレミア")
    """ 名古屋証券取引所 プレミア """
    nagoya_stock_exchange2nd_section:NagoyaStockExchange2ndSection_edjp_FinancialReportSummary_consolidated_Q1 = Field(default=None, description="名古屋証券取引所 メイン")
    """ 名古屋証券取引所 メイン """
    nagoya_stock_exchange_centrex:NagoyaStockExchangeCentrex_edjp_FinancialReportSummary_consolidated_Q1 = Field(default=None, description="名古屋証券取引所 ネクスト")
    """ 名古屋証券取引所 ネクスト """
    nagoya_stock_exchange_others:NagoyaStockExchangeOthers_edjp_FinancialReportSummary_consolidated_Q1 = Field(default=None, description="名古屋証券取引所 その他")
    """ 名古屋証券取引所 その他 """
    name_inquiries:NameInquiries_edjp_FinancialReportSummary_consolidated_Q1 = Field(default=None, description="氏名、問合せ先責任者")
    """ 氏名、問合せ先責任者 """
    name_representative:NameRepresentative_edjp_FinancialReportSummary_consolidated_Q1 = Field(default=None, description="氏名、代表者")
    """ 氏名、代表者 """
    notes_for_using_forecasted_information_and_others:NotesForUsingForecastedInformationAndOthers_edjp_FinancialReportSummary_consolidated_Q1 = Field(default=None, description="業績予想の適切な利用に関する説明、その他特記事項")
    """ 業績予想の適切な利用に関する説明、その他特記事項 """
    note_to_applying_of_specific_accounting_of_the_consolidated_quarterly_financial_statements:NoteToApplyingOfSpecificAccountingOfTheConsolidatedQuarterlyFinancialStatements_edjp_FinancialReportSummary_consolidated_Q1 = Field(default=None, description="四半期連結財務諸表の作成に特有の会計処理の適用に関する注記")
    """ 四半期連結財務諸表の作成に特有の会計処理の適用に関する注記 """
    note_to_changes_in_accounting_policies_accounting_estimates_and_retrospective_restatement_quarterly_consolidated:NoteToChangesInAccountingPoliciesAccountingEstimatesAndRetrospectiveRestatementQuarterlyConsolidated_edjp_FinancialReportSummary_consolidated_Q1 = Field(default=None, description="会計方針の変更・会計上の見積りの変更・修正再表示に関する注記、四半期")
    """ 会計方針の変更・会計上の見積りの変更・修正再表示に関する注記、四半期 """
    note_to_consolidated_financial_results:NoteToConsolidatedFinancialResults_edjp_FinancialReportSummary_consolidated_Q1 = Field(default=None, description="連結業績に関する注記")
    """ 連結業績に関する注記 """
    note_to_dividends:NoteToDividends_edjp_FinancialReportSummary_consolidated_Q1 = Field(default=None, description="配当の状況に関する注記")
    """ 配当の状況に関する注記 """
    note_to_financial_positions:NoteToFinancialPositions_edjp_FinancialReportSummary_consolidated_Q1 = Field(default=None, description="財政状態に関する注記")
    """ 財政状態に関する注記 """
    note_to_forecasts:NoteToForecasts_edjp_FinancialReportSummary_consolidated_Q1 = Field(default=None, description="業績予想に関する事項、注記")
    """ 業績予想に関する事項、注記 """
    note_to_fraction_processing_method:NoteToFractionProcessingMethod_edjp_FinancialReportSummary_consolidated_Q1 = Field(default=None, description="端数処理方法に関する注記")
    """ 端数処理方法に関する注記 """
    note_to_number_of_issued_and_outstanding_shares_common_stock:NoteToNumberOfIssuedAndOutstandingSharesCommonStock_edjp_FinancialReportSummary_consolidated_Q1 = Field(default=None, description="発行済株式数（普通株式）に関する注記")
    """ 発行済株式数（普通株式）に関する注記 """
    note_to_operating_results:NoteToOperatingResults_edjp_FinancialReportSummary_consolidated_Q1 = Field(default=None, description="経営成績に関する注記")
    """ 経営成績に関する注記 """
    note_to_significant_changes_in_the_scope_of_consolidation_during_the_period:NoteToSignificantChangesInTheScopeOfConsolidationDuringThePeriod_edjp_FinancialReportSummary_consolidated_Q1 = Field(default=None, description="期中における連結範囲の重要な変更に関する注記")
    """ 期中における連結範囲の重要な変更に関する注記 """
    preamble_to_forecasts:PreambleToForecasts_edjp_FinancialReportSummary_consolidated_Q1 = Field(default=None, description="業績予想に関する事項")
    """ 業績予想に関する事項 """
    retrospective_restatement:RetrospectiveRestatement_edjp_FinancialReportSummary_consolidated_Q1 = Field(default=None, description="修正再表示")
    """ 修正再表示 """
    review_of_attached_consolidated_quarterly_financial_statements_by_a_certified_public_accountant_or_an_audit_firm:ReviewOfAttachedConsolidatedQuarterlyFinancialStatementsByACertifiedPublicAccountantOrAnAuditFirm_edjp_FinancialReportSummary_consolidated_Q1 = Field(default=None, description="添付される四半期連結財務諸表に対する公認会計士又は監査法人によるレビュー")
    """ 添付される四半期連結財務諸表に対する公認会計士又は監査法人によるレビュー """
    sapporo_stock_exchange:SapporoStockExchange_edjp_FinancialReportSummary_consolidated_Q1 = Field(default=None, description="札幌証券取引所")
    """ 札幌証券取引所 """
    sapporo_stock_exchange_ambitious:SapporoStockExchangeAmbitious_edjp_FinancialReportSummary_consolidated_Q1 = Field(default=None, description="札幌証券取引所 アンビシャス")
    """ 札幌証券取引所 アンビシャス """
    sapporo_stock_exchange_established:SapporoStockExchangeEstablished_edjp_FinancialReportSummary_consolidated_Q1 = Field(default=None, description="札幌証券取引所 既存市場")
    """ 札幌証券取引所 既存市場 """
    sapporo_stock_exchange_others:SapporoStockExchangeOthers_edjp_FinancialReportSummary_consolidated_Q1 = Field(default=None, description="札幌証券取引所 その他")
    """ 札幌証券取引所 その他 """
    securities_code:SecuritiesCode_edjp_FinancialReportSummary_consolidated_Q1 = Field(default=None, description="コード番号")
    """ コード番号 """
    significant_changes_in_the_scope_of_consolidation_during_the_period:SignificantChangesInTheScopeOfConsolidationDuringThePeriod_edjp_FinancialReportSummary_consolidated_Q1 = Field(default=None, description="期中における連結範囲の重要な変更")
    """ 期中における連結範囲の重要な変更 """
    specific_business:SpecificBusiness_edjp_FinancialReportSummary_consolidated_Q1 = Field(default=None, description="特定事業会社")
    """ 特定事業会社 """
    supplemental_material_of_results:SupplementalMaterialOfResults_edjp_FinancialReportSummary_consolidated_Q1 = Field(default=None, description="決算補足説明資料作成の有無、期中")
    """ 決算補足説明資料作成の有無、期中 """
    target_for_briefing_of_results:TargetForBriefingOfResults_edjp_FinancialReportSummary_consolidated_Q1 = Field(default=None, description="決算説明会の対象者")
    """ 決算説明会の対象者 """
    tel:Tel_edjp_FinancialReportSummary_consolidated_Q1 = Field(default=None, description="TEL")
    """ TEL """
    title_for_forecasts:TitleForForecasts_edjp_FinancialReportSummary_consolidated_Q1 = Field(default=None, description="業績予想タイトル名称")
    """ 業績予想タイトル名称 """
    title_inquiries:TitleInquiries_edjp_FinancialReportSummary_consolidated_Q1 = Field(default=None, description="役職名、問合せ先責任者")
    """ 役職名、問合せ先責任者 """
    title_representative:TitleRepresentative_edjp_FinancialReportSummary_consolidated_Q1 = Field(default=None, description="役職名、代表者")
    """ 役職名、代表者 """
    tokyo_stock_exchange:TokyoStockExchange_edjp_FinancialReportSummary_consolidated_Q1 = Field(default=None, description="東京証券取引所")
    """ 東京証券取引所 """
    tokyo_stock_exchange_growth:TokyoStockExchangeGrowth_edjp_FinancialReportSummary_consolidated_Q1 = Field(default=None, description="東京証券取引所 グロース")
    """ 東京証券取引所 グロース """
    tokyo_stock_exchange_others:TokyoStockExchangeOthers_edjp_FinancialReportSummary_consolidated_Q1 = Field(default=None, description="東京証券取引所 その他")
    """ 東京証券取引所 その他 """
    tokyo_stock_exchange_prime:TokyoStockExchangePrime_edjp_FinancialReportSummary_consolidated_Q1 = Field(default=None, description="東京証券取引所 プライム")
    """ 東京証券取引所 プライム """
    tokyo_stock_exchange_pro_market:TokyoStockExchangePROMarket_edjp_FinancialReportSummary_consolidated_Q1 = Field(default=None, description="東京証券取引所 PRO Market")
    """ 東京証券取引所 PRO Market """
    tokyo_stock_exchange_standard:TokyoStockExchangeStandard_edjp_FinancialReportSummary_consolidated_Q1 = Field(default=None, description="東京証券取引所 スタンダード")
    """ 東京証券取引所 スタンダード """
    URL:URL_edjp_FinancialReportSummary_consolidated_Q1 = Field(default=None, description="URL")
    """ URL """
    way_of_getting_supplemental_material_of_results:WayOfGettingSupplementalMaterialOfResults_edjp_FinancialReportSummary_consolidated_Q1 = Field(default=None, description="入手方法等、決算補足説明資料、期中")
    """ 入手方法等、決算補足説明資料、期中 """


class edjp_FinancialReportSummary_Nonconsolidated_Q1(IxbrlBase):
    applying_of_specific_accounting_of_the_quarterly_financial_statements:ApplyingOfSpecificAccountingOfTheQuarterlyFinancialStatements_edjp_FinancialReportSummary_Nonconsolidated_Q1 = Field(default=None, description="四半期財務諸表の作成に特有の会計処理の適用")
    """ 四半期財務諸表の作成に特有の会計処理の適用 """
    changes_based_on_revisions_of_accounting_standard:ChangesBasedOnRevisionsOfAccountingStandard_edjp_FinancialReportSummary_Nonconsolidated_Q1 = Field(default=None, description="会計基準等の改正に伴う会計方針の変更")
    """ 会計基準等の改正に伴う会計方針の変更 """
    changes_in_accounting_estimates:ChangesInAccountingEstimates_edjp_FinancialReportSummary_Nonconsolidated_Q1 = Field(default=None, description="会計上の見積りの変更")
    """ 会計上の見積りの変更 """
    changes_other_than_ones_based_on_revisions_of_accounting_standard:ChangesOtherThanOnesBasedOnRevisionsOfAccountingStandard_edjp_FinancialReportSummary_Nonconsolidated_Q1 = Field(default=None, description="会計基準等の改正に伴う変更以外の会計方針の変更")
    """ 会計基準等の改正に伴う変更以外の会計方針の変更 """
    company_name:CompanyName_edjp_FinancialReportSummary_Nonconsolidated_Q1 = Field(default=None, description="上場会社名")
    """ 上場会社名 """
    convening_briefing_of_results:ConveningBriefingOfResults_edjp_FinancialReportSummary_Nonconsolidated_Q1 = Field(default=None, description="決算説明会開催の有無、期中")
    """ 決算説明会開催の有無、期中 """
    correction_of_dividend_forecast_in_this_quarter:CorrectionOfDividendForecastInThisQuarter_edjp_FinancialReportSummary_Nonconsolidated_Q1 = Field(default=None, description="直近に公表されている配当予想からの修正の有無")
    """ 直近に公表されている配当予想からの修正の有無 """
    correction_of_financial_forecast_in_this_quarter:CorrectionOfFinancialForecastInThisQuarter_edjp_FinancialReportSummary_Nonconsolidated_Q1 = Field(default=None, description="直近に公表されている業績予想からの修正の有無")
    """ 直近に公表されている業績予想からの修正の有無 """
    document_name:DocumentName_edjp_FinancialReportSummary_Nonconsolidated_Q1 = Field(default=None, description="文書名")
    """ 文書名 """
    fasf_member_mark:FASFMemberMark_edjp_FinancialReportSummary_Nonconsolidated_Q1 = Field(default=None, description="財務会計基準機構会員マーク")
    """ 財務会計基準機構会員マーク """
    filing_date:FilingDate_edjp_FinancialReportSummary_Nonconsolidated_Q1 = Field(default=None, description="提出日")
    """ 提出日 """
    fiscal_year_end:FiscalYearEnd_edjp_FinancialReportSummary_Nonconsolidated_Q1 = Field(default=None, description="決算期")
    """ 決算期 """
    fukuoka_stock_exchange:FukuokaStockExchange_edjp_FinancialReportSummary_Nonconsolidated_Q1 = Field(default=None, description="福岡証券取引所")
    """ 福岡証券取引所 """
    fukuoka_stock_exchange_established:FukuokaStockExchangeEstablished_edjp_FinancialReportSummary_Nonconsolidated_Q1 = Field(default=None, description="福岡証券取引所 既存市場")
    """ 福岡証券取引所 既存市場 """
    fukuoka_stock_exchange_others:FukuokaStockExchangeOthers_edjp_FinancialReportSummary_Nonconsolidated_Q1 = Field(default=None, description="福岡証券取引所 その他")
    """ 福岡証券取引所 その他 """
    fukuoka_stock_exchange_q_board:FukuokaStockExchangeQBoard_edjp_FinancialReportSummary_Nonconsolidated_Q1 = Field(default=None, description="福岡証券取引所 Q-Board")
    """ 福岡証券取引所 Q-Board """
    general_business:GeneralBusiness_edjp_FinancialReportSummary_Nonconsolidated_Q1 = Field(default=None, description="一般事業会社")
    """ 一般事業会社 """
    japan_securities_dealers_association:JapanSecuritiesDealersAssociation_edjp_FinancialReportSummary_Nonconsolidated_Q1 = Field(default=None, description="フェニックス")
    """ フェニックス """
    japan_securities_dealers_association_green_sheet:JapanSecuritiesDealersAssociationGreenSheet_edjp_FinancialReportSummary_Nonconsolidated_Q1 = Field(default=None, description="日本証券業協会 フェニックス")
    """ 日本証券業協会 フェニックス """
    nagoya_stock_exchange:NagoyaStockExchange_edjp_FinancialReportSummary_Nonconsolidated_Q1 = Field(default=None, description="名古屋証券取引所")
    """ 名古屋証券取引所 """
    nagoya_stock_exchange1st_section:NagoyaStockExchange1stSection_edjp_FinancialReportSummary_Nonconsolidated_Q1 = Field(default=None, description="名古屋証券取引所 プレミア")
    """ 名古屋証券取引所 プレミア """
    nagoya_stock_exchange2nd_section:NagoyaStockExchange2ndSection_edjp_FinancialReportSummary_Nonconsolidated_Q1 = Field(default=None, description="名古屋証券取引所 メイン")
    """ 名古屋証券取引所 メイン """
    nagoya_stock_exchange_centrex:NagoyaStockExchangeCentrex_edjp_FinancialReportSummary_Nonconsolidated_Q1 = Field(default=None, description="名古屋証券取引所 ネクスト")
    """ 名古屋証券取引所 ネクスト """
    nagoya_stock_exchange_others:NagoyaStockExchangeOthers_edjp_FinancialReportSummary_Nonconsolidated_Q1 = Field(default=None, description="名古屋証券取引所 その他")
    """ 名古屋証券取引所 その他 """
    name_inquiries:NameInquiries_edjp_FinancialReportSummary_Nonconsolidated_Q1 = Field(default=None, description="氏名、問合せ先責任者")
    """ 氏名、問合せ先責任者 """
    name_representative:NameRepresentative_edjp_FinancialReportSummary_Nonconsolidated_Q1 = Field(default=None, description="氏名、代表者")
    """ 氏名、代表者 """
    notes_for_using_forecasted_information_and_others:NotesForUsingForecastedInformationAndOthers_edjp_FinancialReportSummary_Nonconsolidated_Q1 = Field(default=None, description="業績予想の適切な利用に関する説明、その他特記事項")
    """ 業績予想の適切な利用に関する説明、その他特記事項 """
    note_to_applying_of_specific_accounting_of_the_quarterly_financial_statements:NoteToApplyingOfSpecificAccountingOfTheQuarterlyFinancialStatements_edjp_FinancialReportSummary_Nonconsolidated_Q1 = Field(default=None, description="四半期財務諸表の作成に特有の会計処理の適用に関する注記")
    """ 四半期財務諸表の作成に特有の会計処理の適用に関する注記 """
    note_to_changes_in_accounting_policies_accounting_estimates_and_retrospective_restatement_quarterly_consolidated:NoteToChangesInAccountingPoliciesAccountingEstimatesAndRetrospectiveRestatementQuarterlyConsolidated_edjp_FinancialReportSummary_Nonconsolidated_Q1 = Field(default=None, description="会計方針の変更・会計上の見積りの変更・修正再表示に関する注記、四半期")
    """ 会計方針の変更・会計上の見積りの変更・修正再表示に関する注記、四半期 """
    note_to_dividends:NoteToDividends_edjp_FinancialReportSummary_Nonconsolidated_Q1 = Field(default=None, description="配当の状況に関する注記")
    """ 配当の状況に関する注記 """
    note_to_financial_positions:NoteToFinancialPositions_edjp_FinancialReportSummary_Nonconsolidated_Q1 = Field(default=None, description="財政状態に関する注記")
    """ 財政状態に関する注記 """
    note_to_financial_results:NoteToFinancialResults_edjp_FinancialReportSummary_Nonconsolidated_Q1 = Field(default=None, description="業績に関する注記")
    """ 業績に関する注記 """
    note_to_forecasts:NoteToForecasts_edjp_FinancialReportSummary_Nonconsolidated_Q1 = Field(default=None, description="業績予想に関する事項、注記")
    """ 業績予想に関する事項、注記 """
    note_to_fraction_processing_method:NoteToFractionProcessingMethod_edjp_FinancialReportSummary_Nonconsolidated_Q1 = Field(default=None, description="端数処理方法に関する注記")
    """ 端数処理方法に関する注記 """
    note_to_number_of_issued_and_outstanding_shares_common_stock:NoteToNumberOfIssuedAndOutstandingSharesCommonStock_edjp_FinancialReportSummary_Nonconsolidated_Q1 = Field(default=None, description="発行済株式数（普通株式）に関する注記")
    """ 発行済株式数（普通株式）に関する注記 """
    note_to_operating_results:NoteToOperatingResults_edjp_FinancialReportSummary_Nonconsolidated_Q1 = Field(default=None, description="経営成績に関する注記")
    """ 経営成績に関する注記 """
    preamble_to_forecasts:PreambleToForecasts_edjp_FinancialReportSummary_Nonconsolidated_Q1 = Field(default=None, description="業績予想に関する事項")
    """ 業績予想に関する事項 """
    retrospective_restatement:RetrospectiveRestatement_edjp_FinancialReportSummary_Nonconsolidated_Q1 = Field(default=None, description="修正再表示")
    """ 修正再表示 """
    review_of_attached_quarterly_financial_statements_by_a_certified_public_accountant_or_an_audit_firm:ReviewOfAttachedQuarterlyFinancialStatementsByACertifiedPublicAccountantOrAnAuditFirm_edjp_FinancialReportSummary_Nonconsolidated_Q1 = Field(default=None, description="添付される四半期財務諸表に対する公認会計士又は監査法人によるレビュー")
    """ 添付される四半期財務諸表に対する公認会計士又は監査法人によるレビュー """
    sapporo_stock_exchange:SapporoStockExchange_edjp_FinancialReportSummary_Nonconsolidated_Q1 = Field(default=None, description="札幌証券取引所")
    """ 札幌証券取引所 """
    sapporo_stock_exchange_ambitious:SapporoStockExchangeAmbitious_edjp_FinancialReportSummary_Nonconsolidated_Q1 = Field(default=None, description="札幌証券取引所 アンビシャス")
    """ 札幌証券取引所 アンビシャス """
    sapporo_stock_exchange_established:SapporoStockExchangeEstablished_edjp_FinancialReportSummary_Nonconsolidated_Q1 = Field(default=None, description="札幌証券取引所 既存市場")
    """ 札幌証券取引所 既存市場 """
    sapporo_stock_exchange_others:SapporoStockExchangeOthers_edjp_FinancialReportSummary_Nonconsolidated_Q1 = Field(default=None, description="札幌証券取引所 その他")
    """ 札幌証券取引所 その他 """
    securities_code:SecuritiesCode_edjp_FinancialReportSummary_Nonconsolidated_Q1 = Field(default=None, description="コード番号")
    """ コード番号 """
    specific_business:SpecificBusiness_edjp_FinancialReportSummary_Nonconsolidated_Q1 = Field(default=None, description="特定事業会社")
    """ 特定事業会社 """
    supplemental_material_of_results:SupplementalMaterialOfResults_edjp_FinancialReportSummary_Nonconsolidated_Q1 = Field(default=None, description="決算補足説明資料作成の有無、期中")
    """ 決算補足説明資料作成の有無、期中 """
    target_for_briefing_of_results:TargetForBriefingOfResults_edjp_FinancialReportSummary_Nonconsolidated_Q1 = Field(default=None, description="決算説明会の対象者")
    """ 決算説明会の対象者 """
    tel:Tel_edjp_FinancialReportSummary_Nonconsolidated_Q1 = Field(default=None, description="TEL")
    """ TEL """
    title_for_forecasts:TitleForForecasts_edjp_FinancialReportSummary_Nonconsolidated_Q1 = Field(default=None, description="業績予想タイトル名称")
    """ 業績予想タイトル名称 """
    title_inquiries:TitleInquiries_edjp_FinancialReportSummary_Nonconsolidated_Q1 = Field(default=None, description="役職名、問合せ先責任者")
    """ 役職名、問合せ先責任者 """
    title_representative:TitleRepresentative_edjp_FinancialReportSummary_Nonconsolidated_Q1 = Field(default=None, description="役職名、代表者")
    """ 役職名、代表者 """
    tokyo_stock_exchange:TokyoStockExchange_edjp_FinancialReportSummary_Nonconsolidated_Q1 = Field(default=None, description="東京証券取引所")
    """ 東京証券取引所 """
    tokyo_stock_exchange_growth:TokyoStockExchangeGrowth_edjp_FinancialReportSummary_Nonconsolidated_Q1 = Field(default=None, description="東京証券取引所 グロース")
    """ 東京証券取引所 グロース """
    tokyo_stock_exchange_others:TokyoStockExchangeOthers_edjp_FinancialReportSummary_Nonconsolidated_Q1 = Field(default=None, description="東京証券取引所 その他")
    """ 東京証券取引所 その他 """
    tokyo_stock_exchange_prime:TokyoStockExchangePrime_edjp_FinancialReportSummary_Nonconsolidated_Q1 = Field(default=None, description="東京証券取引所 プライム")
    """ 東京証券取引所 プライム """
    tokyo_stock_exchange_pro_market:TokyoStockExchangePROMarket_edjp_FinancialReportSummary_Nonconsolidated_Q1 = Field(default=None, description="東京証券取引所 PRO Market")
    """ 東京証券取引所 PRO Market """
    tokyo_stock_exchange_standard:TokyoStockExchangeStandard_edjp_FinancialReportSummary_Nonconsolidated_Q1 = Field(default=None, description="東京証券取引所 スタンダード")
    """ 東京証券取引所 スタンダード """
    URL:URL_edjp_FinancialReportSummary_Nonconsolidated_Q1 = Field(default=None, description="URL")
    """ URL """
    way_of_getting_supplemental_material_of_results:WayOfGettingSupplementalMaterialOfResults_edjp_FinancialReportSummary_Nonconsolidated_Q1 = Field(default=None, description="入手方法等、決算補足説明資料、期中")
    """ 入手方法等、決算補足説明資料、期中 """


class edjp_FinancialReportSummary_consolidated_Q2(IxbrlBase):
    applying_of_specific_accounting_of_the_consolidated_semi_annual_financial_statements:ApplyingOfSpecificAccountingOfTheConsolidatedSemiAnnualFinancialStatements_edjp_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="中間連結財務諸表の作成に特有の会計処理の適用")
    """ 中間連結財務諸表の作成に特有の会計処理の適用 """
    changes_based_on_revisions_of_accounting_standard:ChangesBasedOnRevisionsOfAccountingStandard_edjp_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="会計基準等の改正に伴う会計方針の変更")
    """ 会計基準等の改正に伴う会計方針の変更 """
    changes_in_accounting_estimates:ChangesInAccountingEstimates_edjp_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="会計上の見積りの変更")
    """ 会計上の見積りの変更 """
    changes_other_than_ones_based_on_revisions_of_accounting_standard:ChangesOtherThanOnesBasedOnRevisionsOfAccountingStandard_edjp_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="会計基準等の改正に伴う変更以外の会計方針の変更")
    """ 会計基準等の改正に伴う変更以外の会計方針の変更 """
    company_name:CompanyName_edjp_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="上場会社名")
    """ 上場会社名 """
    convening_briefing_of_results:ConveningBriefingOfResults_edjp_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="決算説明会開催の有無、期中")
    """ 決算説明会開催の有無、期中 """
    correction_of_consolidated_financial_forecast_in_this_quarter:CorrectionOfConsolidatedFinancialForecastInThisQuarter_edjp_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="直近に公表されている業績予想からの修正の有無、連結")
    """ 直近に公表されている業績予想からの修正の有無、連結 """
    correction_of_dividend_forecast_in_this_quarter:CorrectionOfDividendForecastInThisQuarter_edjp_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="直近に公表されている配当予想からの修正の有無")
    """ 直近に公表されている配当予想からの修正の有無 """
    dividend_payable_date_as_planned:DividendPayableDateAsPlanned_edjp_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="配当支払開始予定日")
    """ 配当支払開始予定日 """
    document_name:DocumentName_edjp_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="文書名")
    """ 文書名 """
    fasf_member_mark:FASFMemberMark_edjp_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="財務会計基準機構会員マーク")
    """ 財務会計基準機構会員マーク """
    filing_date:FilingDate_edjp_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="提出日")
    """ 提出日 """
    fiscal_year_end:FiscalYearEnd_edjp_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="決算期")
    """ 決算期 """
    fukuoka_stock_exchange:FukuokaStockExchange_edjp_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="福岡証券取引所")
    """ 福岡証券取引所 """
    fukuoka_stock_exchange_established:FukuokaStockExchangeEstablished_edjp_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="福岡証券取引所 既存市場")
    """ 福岡証券取引所 既存市場 """
    fukuoka_stock_exchange_others:FukuokaStockExchangeOthers_edjp_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="福岡証券取引所 その他")
    """ 福岡証券取引所 その他 """
    fukuoka_stock_exchange_q_board:FukuokaStockExchangeQBoard_edjp_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="福岡証券取引所 Q-Board")
    """ 福岡証券取引所 Q-Board """
    general_business:GeneralBusiness_edjp_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="一般事業会社")
    """ 一般事業会社 """
    japan_securities_dealers_association:JapanSecuritiesDealersAssociation_edjp_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="フェニックス")
    """ フェニックス """
    japan_securities_dealers_association_green_sheet:JapanSecuritiesDealersAssociationGreenSheet_edjp_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="日本証券業協会 フェニックス")
    """ 日本証券業協会 フェニックス """
    nagoya_stock_exchange:NagoyaStockExchange_edjp_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="名古屋証券取引所")
    """ 名古屋証券取引所 """
    nagoya_stock_exchange1st_section:NagoyaStockExchange1stSection_edjp_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="名古屋証券取引所 プレミア")
    """ 名古屋証券取引所 プレミア """
    nagoya_stock_exchange2nd_section:NagoyaStockExchange2ndSection_edjp_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="名古屋証券取引所 メイン")
    """ 名古屋証券取引所 メイン """
    nagoya_stock_exchange_centrex:NagoyaStockExchangeCentrex_edjp_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="名古屋証券取引所 ネクスト")
    """ 名古屋証券取引所 ネクスト """
    nagoya_stock_exchange_others:NagoyaStockExchangeOthers_edjp_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="名古屋証券取引所 その他")
    """ 名古屋証券取引所 その他 """
    name_inquiries:NameInquiries_edjp_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="氏名、問合せ先責任者")
    """ 氏名、問合せ先責任者 """
    name_of_subsidiaries_excluded_from_consolidation:NameOfSubsidiariesExcludedFromConsolidation_edjp_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="社名、除外")
    """ 社名、除外 """
    name_of_subsidiaries_newly_consolidated:NameOfSubsidiariesNewlyConsolidated_edjp_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="社名、新規")
    """ 社名、新規 """
    name_representative:NameRepresentative_edjp_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="氏名、代表者")
    """ 氏名、代表者 """
    notes_for_using_forecasted_information_and_others:NotesForUsingForecastedInformationAndOthers_edjp_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="業績予想の適切な利用に関する説明、その他特記事項")
    """ 業績予想の適切な利用に関する説明、その他特記事項 """
    note_to_applying_of_specific_accounting_of_the_consolidated_semi_annual_financial_statements:NoteToApplyingOfSpecificAccountingOfTheConsolidatedSemiAnnualFinancialStatements_edjp_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="中間連結財務諸表の作成に特有の会計処理の適用に関する注記")
    """ 中間連結財務諸表の作成に特有の会計処理の適用に関する注記 """
    note_to_changes_in_accounting_policies_accounting_estimates_and_retrospective_restatement_quarterly_consolidated:NoteToChangesInAccountingPoliciesAccountingEstimatesAndRetrospectiveRestatementQuarterlyConsolidated_edjp_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="会計方針の変更・会計上の見積りの変更・修正再表示に関する注記、四半期")
    """ 会計方針の変更・会計上の見積りの変更・修正再表示に関する注記、四半期 """
    note_to_consolidated_financial_results:NoteToConsolidatedFinancialResults_edjp_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="連結業績に関する注記")
    """ 連結業績に関する注記 """
    note_to_dividends:NoteToDividends_edjp_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="配当の状況に関する注記")
    """ 配当の状況に関する注記 """
    note_to_financial_positions:NoteToFinancialPositions_edjp_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="財政状態に関する注記")
    """ 財政状態に関する注記 """
    note_to_forecasts:NoteToForecasts_edjp_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="業績予想に関する事項、注記")
    """ 業績予想に関する事項、注記 """
    note_to_fraction_processing_method:NoteToFractionProcessingMethod_edjp_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="端数処理方法に関する注記")
    """ 端数処理方法に関する注記 """
    note_to_number_of_issued_and_outstanding_shares_common_stock:NoteToNumberOfIssuedAndOutstandingSharesCommonStock_edjp_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="発行済株式数（普通株式）に関する注記")
    """ 発行済株式数（普通株式）に関する注記 """
    note_to_operating_results:NoteToOperatingResults_edjp_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="経営成績に関する注記")
    """ 経営成績に関する注記 """
    note_to_significant_changes_in_the_scope_of_consolidation_during_the_period:NoteToSignificantChangesInTheScopeOfConsolidationDuringThePeriod_edjp_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="期中における連結範囲の重要な変更に関する注記")
    """ 期中における連結範囲の重要な変更に関する注記 """
    preamble_to_forecasts:PreambleToForecasts_edjp_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="業績予想に関する事項")
    """ 業績予想に関する事項 """
    retrospective_restatement:RetrospectiveRestatement_edjp_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="修正再表示")
    """ 修正再表示 """
    sapporo_stock_exchange:SapporoStockExchange_edjp_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="札幌証券取引所")
    """ 札幌証券取引所 """
    sapporo_stock_exchange_ambitious:SapporoStockExchangeAmbitious_edjp_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="札幌証券取引所 アンビシャス")
    """ 札幌証券取引所 アンビシャス """
    sapporo_stock_exchange_established:SapporoStockExchangeEstablished_edjp_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="札幌証券取引所 既存市場")
    """ 札幌証券取引所 既存市場 """
    sapporo_stock_exchange_others:SapporoStockExchangeOthers_edjp_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="札幌証券取引所 その他")
    """ 札幌証券取引所 その他 """
    securities_code:SecuritiesCode_edjp_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="コード番号")
    """ コード番号 """
    semi_annual_statement_filing_date_as_planned:SemiAnnualStatementFilingDateAsPlanned_edjp_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="半期報告書提出予定日")
    """ 半期報告書提出予定日 """
    significant_changes_in_the_scope_of_consolidation_during_the_period:SignificantChangesInTheScopeOfConsolidationDuringThePeriod_edjp_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="期中における連結範囲の重要な変更")
    """ 期中における連結範囲の重要な変更 """
    specific_business:SpecificBusiness_edjp_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="特定事業会社")
    """ 特定事業会社 """
    supplemental_material_of_results:SupplementalMaterialOfResults_edjp_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="決算補足説明資料作成の有無、期中")
    """ 決算補足説明資料作成の有無、期中 """
    target_for_briefing_of_results:TargetForBriefingOfResults_edjp_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="決算説明会の対象者")
    """ 決算説明会の対象者 """
    tel:Tel_edjp_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="TEL")
    """ TEL """
    title_for_forecasts:TitleForForecasts_edjp_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="業績予想タイトル名称")
    """ 業績予想タイトル名称 """
    title_inquiries:TitleInquiries_edjp_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="役職名、問合せ先責任者")
    """ 役職名、問合せ先責任者 """
    title_representative:TitleRepresentative_edjp_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="役職名、代表者")
    """ 役職名、代表者 """
    tokyo_stock_exchange:TokyoStockExchange_edjp_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="東京証券取引所")
    """ 東京証券取引所 """
    tokyo_stock_exchange_growth:TokyoStockExchangeGrowth_edjp_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="東京証券取引所 グロース")
    """ 東京証券取引所 グロース """
    tokyo_stock_exchange_others:TokyoStockExchangeOthers_edjp_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="東京証券取引所 その他")
    """ 東京証券取引所 その他 """
    tokyo_stock_exchange_prime:TokyoStockExchangePrime_edjp_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="東京証券取引所 プライム")
    """ 東京証券取引所 プライム """
    tokyo_stock_exchange_pro_market:TokyoStockExchangePROMarket_edjp_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="東京証券取引所 PRO Market")
    """ 東京証券取引所 PRO Market """
    tokyo_stock_exchange_standard:TokyoStockExchangeStandard_edjp_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="東京証券取引所 スタンダード")
    """ 東京証券取引所 スタンダード """
    URL:URL_edjp_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="URL")
    """ URL """
    way_of_getting_supplemental_material_of_results:WayOfGettingSupplementalMaterialOfResults_edjp_FinancialReportSummary_consolidated_Q2 = Field(default=None, description="入手方法等、決算補足説明資料、期中")
    """ 入手方法等、決算補足説明資料、期中 """


class edjp_FinancialReportSummary_Nonconsolidated_Q2(IxbrlBase):
    applying_of_specific_accounting_of_the_semi_annual_financial_statements:ApplyingOfSpecificAccountingOfTheSemiAnnualFinancialStatements_edjp_FinancialReportSummary_Nonconsolidated_Q2 = Field(default=None, description="中間財務諸表の作成に特有の会計処理の適用")
    """ 中間財務諸表の作成に特有の会計処理の適用 """
    changes_based_on_revisions_of_accounting_standard:ChangesBasedOnRevisionsOfAccountingStandard_edjp_FinancialReportSummary_Nonconsolidated_Q2 = Field(default=None, description="会計基準等の改正に伴う会計方針の変更")
    """ 会計基準等の改正に伴う会計方針の変更 """
    changes_in_accounting_estimates:ChangesInAccountingEstimates_edjp_FinancialReportSummary_Nonconsolidated_Q2 = Field(default=None, description="会計上の見積りの変更")
    """ 会計上の見積りの変更 """
    changes_other_than_ones_based_on_revisions_of_accounting_standard:ChangesOtherThanOnesBasedOnRevisionsOfAccountingStandard_edjp_FinancialReportSummary_Nonconsolidated_Q2 = Field(default=None, description="会計基準等の改正に伴う変更以外の会計方針の変更")
    """ 会計基準等の改正に伴う変更以外の会計方針の変更 """
    company_name:CompanyName_edjp_FinancialReportSummary_Nonconsolidated_Q2 = Field(default=None, description="上場会社名")
    """ 上場会社名 """
    convening_briefing_of_results:ConveningBriefingOfResults_edjp_FinancialReportSummary_Nonconsolidated_Q2 = Field(default=None, description="決算説明会開催の有無、期中")
    """ 決算説明会開催の有無、期中 """
    correction_of_dividend_forecast_in_this_quarter:CorrectionOfDividendForecastInThisQuarter_edjp_FinancialReportSummary_Nonconsolidated_Q2 = Field(default=None, description="直近に公表されている配当予想からの修正の有無")
    """ 直近に公表されている配当予想からの修正の有無 """
    correction_of_financial_forecast_in_this_quarter:CorrectionOfFinancialForecastInThisQuarter_edjp_FinancialReportSummary_Nonconsolidated_Q2 = Field(default=None, description="直近に公表されている業績予想からの修正の有無")
    """ 直近に公表されている業績予想からの修正の有無 """
    dividend_payable_date_as_planned:DividendPayableDateAsPlanned_edjp_FinancialReportSummary_Nonconsolidated_Q2 = Field(default=None, description="配当支払開始予定日")
    """ 配当支払開始予定日 """
    document_name:DocumentName_edjp_FinancialReportSummary_Nonconsolidated_Q2 = Field(default=None, description="文書名")
    """ 文書名 """
    fasf_member_mark:FASFMemberMark_edjp_FinancialReportSummary_Nonconsolidated_Q2 = Field(default=None, description="財務会計基準機構会員マーク")
    """ 財務会計基準機構会員マーク """
    filing_date:FilingDate_edjp_FinancialReportSummary_Nonconsolidated_Q2 = Field(default=None, description="提出日")
    """ 提出日 """
    fiscal_year_end:FiscalYearEnd_edjp_FinancialReportSummary_Nonconsolidated_Q2 = Field(default=None, description="決算期")
    """ 決算期 """
    fukuoka_stock_exchange:FukuokaStockExchange_edjp_FinancialReportSummary_Nonconsolidated_Q2 = Field(default=None, description="福岡証券取引所")
    """ 福岡証券取引所 """
    fukuoka_stock_exchange_established:FukuokaStockExchangeEstablished_edjp_FinancialReportSummary_Nonconsolidated_Q2 = Field(default=None, description="福岡証券取引所 既存市場")
    """ 福岡証券取引所 既存市場 """
    fukuoka_stock_exchange_others:FukuokaStockExchangeOthers_edjp_FinancialReportSummary_Nonconsolidated_Q2 = Field(default=None, description="福岡証券取引所 その他")
    """ 福岡証券取引所 その他 """
    fukuoka_stock_exchange_q_board:FukuokaStockExchangeQBoard_edjp_FinancialReportSummary_Nonconsolidated_Q2 = Field(default=None, description="福岡証券取引所 Q-Board")
    """ 福岡証券取引所 Q-Board """
    general_business:GeneralBusiness_edjp_FinancialReportSummary_Nonconsolidated_Q2 = Field(default=None, description="一般事業会社")
    """ 一般事業会社 """
    japan_securities_dealers_association:JapanSecuritiesDealersAssociation_edjp_FinancialReportSummary_Nonconsolidated_Q2 = Field(default=None, description="フェニックス")
    """ フェニックス """
    japan_securities_dealers_association_green_sheet:JapanSecuritiesDealersAssociationGreenSheet_edjp_FinancialReportSummary_Nonconsolidated_Q2 = Field(default=None, description="日本証券業協会 フェニックス")
    """ 日本証券業協会 フェニックス """
    nagoya_stock_exchange:NagoyaStockExchange_edjp_FinancialReportSummary_Nonconsolidated_Q2 = Field(default=None, description="名古屋証券取引所")
    """ 名古屋証券取引所 """
    nagoya_stock_exchange1st_section:NagoyaStockExchange1stSection_edjp_FinancialReportSummary_Nonconsolidated_Q2 = Field(default=None, description="名古屋証券取引所 プレミア")
    """ 名古屋証券取引所 プレミア """
    nagoya_stock_exchange2nd_section:NagoyaStockExchange2ndSection_edjp_FinancialReportSummary_Nonconsolidated_Q2 = Field(default=None, description="名古屋証券取引所 メイン")
    """ 名古屋証券取引所 メイン """
    nagoya_stock_exchange_centrex:NagoyaStockExchangeCentrex_edjp_FinancialReportSummary_Nonconsolidated_Q2 = Field(default=None, description="名古屋証券取引所 ネクスト")
    """ 名古屋証券取引所 ネクスト """
    nagoya_stock_exchange_others:NagoyaStockExchangeOthers_edjp_FinancialReportSummary_Nonconsolidated_Q2 = Field(default=None, description="名古屋証券取引所 その他")
    """ 名古屋証券取引所 その他 """
    name_inquiries:NameInquiries_edjp_FinancialReportSummary_Nonconsolidated_Q2 = Field(default=None, description="氏名、問合せ先責任者")
    """ 氏名、問合せ先責任者 """
    name_representative:NameRepresentative_edjp_FinancialReportSummary_Nonconsolidated_Q2 = Field(default=None, description="氏名、代表者")
    """ 氏名、代表者 """
    notes_for_using_forecasted_information_and_others:NotesForUsingForecastedInformationAndOthers_edjp_FinancialReportSummary_Nonconsolidated_Q2 = Field(default=None, description="業績予想の適切な利用に関する説明、その他特記事項")
    """ 業績予想の適切な利用に関する説明、その他特記事項 """
    note_to_applying_of_specific_accounting_of_the_semi_annual_financial_statements:NoteToApplyingOfSpecificAccountingOfTheSemiAnnualFinancialStatements_edjp_FinancialReportSummary_Nonconsolidated_Q2 = Field(default=None, description="中間財務諸表の作成に特有の会計処理の適用に関する注記")
    """ 中間財務諸表の作成に特有の会計処理の適用に関する注記 """
    note_to_changes_in_accounting_policies_accounting_estimates_and_retrospective_restatement_quarterly_consolidated:NoteToChangesInAccountingPoliciesAccountingEstimatesAndRetrospectiveRestatementQuarterlyConsolidated_edjp_FinancialReportSummary_Nonconsolidated_Q2 = Field(default=None, description="会計方針の変更・会計上の見積りの変更・修正再表示に関する注記、四半期")
    """ 会計方針の変更・会計上の見積りの変更・修正再表示に関する注記、四半期 """
    note_to_dividends:NoteToDividends_edjp_FinancialReportSummary_Nonconsolidated_Q2 = Field(default=None, description="配当の状況に関する注記")
    """ 配当の状況に関する注記 """
    note_to_financial_positions:NoteToFinancialPositions_edjp_FinancialReportSummary_Nonconsolidated_Q2 = Field(default=None, description="財政状態に関する注記")
    """ 財政状態に関する注記 """
    note_to_financial_results:NoteToFinancialResults_edjp_FinancialReportSummary_Nonconsolidated_Q2 = Field(default=None, description="業績に関する注記")
    """ 業績に関する注記 """
    note_to_forecasts:NoteToForecasts_edjp_FinancialReportSummary_Nonconsolidated_Q2 = Field(default=None, description="業績予想に関する事項、注記")
    """ 業績予想に関する事項、注記 """
    note_to_fraction_processing_method:NoteToFractionProcessingMethod_edjp_FinancialReportSummary_Nonconsolidated_Q2 = Field(default=None, description="端数処理方法に関する注記")
    """ 端数処理方法に関する注記 """
    note_to_number_of_issued_and_outstanding_shares_common_stock:NoteToNumberOfIssuedAndOutstandingSharesCommonStock_edjp_FinancialReportSummary_Nonconsolidated_Q2 = Field(default=None, description="発行済株式数（普通株式）に関する注記")
    """ 発行済株式数（普通株式）に関する注記 """
    note_to_operating_results:NoteToOperatingResults_edjp_FinancialReportSummary_Nonconsolidated_Q2 = Field(default=None, description="経営成績に関する注記")
    """ 経営成績に関する注記 """
    preamble_to_forecasts:PreambleToForecasts_edjp_FinancialReportSummary_Nonconsolidated_Q2 = Field(default=None, description="業績予想に関する事項")
    """ 業績予想に関する事項 """
    retrospective_restatement:RetrospectiveRestatement_edjp_FinancialReportSummary_Nonconsolidated_Q2 = Field(default=None, description="修正再表示")
    """ 修正再表示 """
    sapporo_stock_exchange:SapporoStockExchange_edjp_FinancialReportSummary_Nonconsolidated_Q2 = Field(default=None, description="札幌証券取引所")
    """ 札幌証券取引所 """
    sapporo_stock_exchange_ambitious:SapporoStockExchangeAmbitious_edjp_FinancialReportSummary_Nonconsolidated_Q2 = Field(default=None, description="札幌証券取引所 アンビシャス")
    """ 札幌証券取引所 アンビシャス """
    sapporo_stock_exchange_established:SapporoStockExchangeEstablished_edjp_FinancialReportSummary_Nonconsolidated_Q2 = Field(default=None, description="札幌証券取引所 既存市場")
    """ 札幌証券取引所 既存市場 """
    sapporo_stock_exchange_others:SapporoStockExchangeOthers_edjp_FinancialReportSummary_Nonconsolidated_Q2 = Field(default=None, description="札幌証券取引所 その他")
    """ 札幌証券取引所 その他 """
    securities_code:SecuritiesCode_edjp_FinancialReportSummary_Nonconsolidated_Q2 = Field(default=None, description="コード番号")
    """ コード番号 """
    semi_annual_statement_filing_date_as_planned:SemiAnnualStatementFilingDateAsPlanned_edjp_FinancialReportSummary_Nonconsolidated_Q2 = Field(default=None, description="半期報告書提出予定日")
    """ 半期報告書提出予定日 """
    specific_business:SpecificBusiness_edjp_FinancialReportSummary_Nonconsolidated_Q2 = Field(default=None, description="特定事業会社")
    """ 特定事業会社 """
    supplemental_material_of_results:SupplementalMaterialOfResults_edjp_FinancialReportSummary_Nonconsolidated_Q2 = Field(default=None, description="決算補足説明資料作成の有無、期中")
    """ 決算補足説明資料作成の有無、期中 """
    target_for_briefing_of_results:TargetForBriefingOfResults_edjp_FinancialReportSummary_Nonconsolidated_Q2 = Field(default=None, description="決算説明会の対象者")
    """ 決算説明会の対象者 """
    tel:Tel_edjp_FinancialReportSummary_Nonconsolidated_Q2 = Field(default=None, description="TEL")
    """ TEL """
    title_for_forecasts:TitleForForecasts_edjp_FinancialReportSummary_Nonconsolidated_Q2 = Field(default=None, description="業績予想タイトル名称")
    """ 業績予想タイトル名称 """
    title_inquiries:TitleInquiries_edjp_FinancialReportSummary_Nonconsolidated_Q2 = Field(default=None, description="役職名、問合せ先責任者")
    """ 役職名、問合せ先責任者 """
    title_representative:TitleRepresentative_edjp_FinancialReportSummary_Nonconsolidated_Q2 = Field(default=None, description="役職名、代表者")
    """ 役職名、代表者 """
    tokyo_stock_exchange:TokyoStockExchange_edjp_FinancialReportSummary_Nonconsolidated_Q2 = Field(default=None, description="東京証券取引所")
    """ 東京証券取引所 """
    tokyo_stock_exchange_growth:TokyoStockExchangeGrowth_edjp_FinancialReportSummary_Nonconsolidated_Q2 = Field(default=None, description="東京証券取引所 グロース")
    """ 東京証券取引所 グロース """
    tokyo_stock_exchange_others:TokyoStockExchangeOthers_edjp_FinancialReportSummary_Nonconsolidated_Q2 = Field(default=None, description="東京証券取引所 その他")
    """ 東京証券取引所 その他 """
    tokyo_stock_exchange_prime:TokyoStockExchangePrime_edjp_FinancialReportSummary_Nonconsolidated_Q2 = Field(default=None, description="東京証券取引所 プライム")
    """ 東京証券取引所 プライム """
    tokyo_stock_exchange_pro_market:TokyoStockExchangePROMarket_edjp_FinancialReportSummary_Nonconsolidated_Q2 = Field(default=None, description="東京証券取引所 PRO Market")
    """ 東京証券取引所 PRO Market """
    tokyo_stock_exchange_standard:TokyoStockExchangeStandard_edjp_FinancialReportSummary_Nonconsolidated_Q2 = Field(default=None, description="東京証券取引所 スタンダード")
    """ 東京証券取引所 スタンダード """
    URL:URL_edjp_FinancialReportSummary_Nonconsolidated_Q2 = Field(default=None, description="URL")
    """ URL """
    way_of_getting_supplemental_material_of_results:WayOfGettingSupplementalMaterialOfResults_edjp_FinancialReportSummary_Nonconsolidated_Q2 = Field(default=None, description="入手方法等、決算補足説明資料、期中")
    """ 入手方法等、決算補足説明資料、期中 """


class edjp_FinancialReportSummary_consolidated_Q3(IxbrlBase):
    applying_of_specific_accounting_of_the_consolidated_quarterly_financial_statements:ApplyingOfSpecificAccountingOfTheConsolidatedQuarterlyFinancialStatements_edjp_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="四半期連結財務諸表の作成に特有の会計処理の適用")
    """ 四半期連結財務諸表の作成に特有の会計処理の適用 """
    changes_based_on_revisions_of_accounting_standard:ChangesBasedOnRevisionsOfAccountingStandard_edjp_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="会計基準等の改正に伴う会計方針の変更")
    """ 会計基準等の改正に伴う会計方針の変更 """
    changes_in_accounting_estimates:ChangesInAccountingEstimates_edjp_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="会計上の見積りの変更")
    """ 会計上の見積りの変更 """
    changes_other_than_ones_based_on_revisions_of_accounting_standard:ChangesOtherThanOnesBasedOnRevisionsOfAccountingStandard_edjp_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="会計基準等の改正に伴う変更以外の会計方針の変更")
    """ 会計基準等の改正に伴う変更以外の会計方針の変更 """
    company_name:CompanyName_edjp_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="上場会社名")
    """ 上場会社名 """
    convening_briefing_of_results:ConveningBriefingOfResults_edjp_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="決算説明会開催の有無、期中")
    """ 決算説明会開催の有無、期中 """
    correction_of_consolidated_financial_forecast_in_this_quarter:CorrectionOfConsolidatedFinancialForecastInThisQuarter_edjp_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="直近に公表されている業績予想からの修正の有無、連結")
    """ 直近に公表されている業績予想からの修正の有無、連結 """
    correction_of_dividend_forecast_in_this_quarter:CorrectionOfDividendForecastInThisQuarter_edjp_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="直近に公表されている配当予想からの修正の有無")
    """ 直近に公表されている配当予想からの修正の有無 """
    dividend_payable_date_as_planned:DividendPayableDateAsPlanned_edjp_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="配当支払開始予定日")
    """ 配当支払開始予定日 """
    document_name:DocumentName_edjp_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="文書名")
    """ 文書名 """
    fasf_member_mark:FASFMemberMark_edjp_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="財務会計基準機構会員マーク")
    """ 財務会計基準機構会員マーク """
    filing_date:FilingDate_edjp_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="提出日")
    """ 提出日 """
    fiscal_year_end:FiscalYearEnd_edjp_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="決算期")
    """ 決算期 """
    fukuoka_stock_exchange:FukuokaStockExchange_edjp_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="福岡証券取引所")
    """ 福岡証券取引所 """
    fukuoka_stock_exchange_established:FukuokaStockExchangeEstablished_edjp_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="福岡証券取引所 既存市場")
    """ 福岡証券取引所 既存市場 """
    fukuoka_stock_exchange_others:FukuokaStockExchangeOthers_edjp_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="福岡証券取引所 その他")
    """ 福岡証券取引所 その他 """
    fukuoka_stock_exchange_q_board:FukuokaStockExchangeQBoard_edjp_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="福岡証券取引所 Q-Board")
    """ 福岡証券取引所 Q-Board """
    general_business:GeneralBusiness_edjp_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="一般事業会社")
    """ 一般事業会社 """
    japan_securities_dealers_association:JapanSecuritiesDealersAssociation_edjp_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="フェニックス")
    """ フェニックス """
    japan_securities_dealers_association_green_sheet:JapanSecuritiesDealersAssociationGreenSheet_edjp_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="日本証券業協会 フェニックス")
    """ 日本証券業協会 フェニックス """
    nagoya_stock_exchange:NagoyaStockExchange_edjp_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="名古屋証券取引所")
    """ 名古屋証券取引所 """
    nagoya_stock_exchange1st_section:NagoyaStockExchange1stSection_edjp_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="名古屋証券取引所 プレミア")
    """ 名古屋証券取引所 プレミア """
    nagoya_stock_exchange2nd_section:NagoyaStockExchange2ndSection_edjp_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="名古屋証券取引所 メイン")
    """ 名古屋証券取引所 メイン """
    nagoya_stock_exchange_centrex:NagoyaStockExchangeCentrex_edjp_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="名古屋証券取引所 ネクスト")
    """ 名古屋証券取引所 ネクスト """
    nagoya_stock_exchange_others:NagoyaStockExchangeOthers_edjp_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="名古屋証券取引所 その他")
    """ 名古屋証券取引所 その他 """
    name_inquiries:NameInquiries_edjp_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="氏名、問合せ先責任者")
    """ 氏名、問合せ先責任者 """
    name_of_subsidiaries_excluded_from_consolidation:NameOfSubsidiariesExcludedFromConsolidation_edjp_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="社名、除外")
    """ 社名、除外 """
    name_of_subsidiaries_newly_consolidated:NameOfSubsidiariesNewlyConsolidated_edjp_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="社名、新規")
    """ 社名、新規 """
    name_representative:NameRepresentative_edjp_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="氏名、代表者")
    """ 氏名、代表者 """
    notes_for_using_forecasted_information_and_others:NotesForUsingForecastedInformationAndOthers_edjp_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="業績予想の適切な利用に関する説明、その他特記事項")
    """ 業績予想の適切な利用に関する説明、その他特記事項 """
    note_to_applying_of_specific_accounting_of_the_consolidated_quarterly_financial_statements:NoteToApplyingOfSpecificAccountingOfTheConsolidatedQuarterlyFinancialStatements_edjp_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="四半期連結財務諸表の作成に特有の会計処理の適用に関する注記")
    """ 四半期連結財務諸表の作成に特有の会計処理の適用に関する注記 """
    note_to_changes_in_accounting_policies_accounting_estimates_and_retrospective_restatement_quarterly_consolidated:NoteToChangesInAccountingPoliciesAccountingEstimatesAndRetrospectiveRestatementQuarterlyConsolidated_edjp_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="会計方針の変更・会計上の見積りの変更・修正再表示に関する注記、四半期")
    """ 会計方針の変更・会計上の見積りの変更・修正再表示に関する注記、四半期 """
    note_to_consolidated_financial_results:NoteToConsolidatedFinancialResults_edjp_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="連結業績に関する注記")
    """ 連結業績に関する注記 """
    note_to_dividends:NoteToDividends_edjp_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="配当の状況に関する注記")
    """ 配当の状況に関する注記 """
    note_to_financial_positions:NoteToFinancialPositions_edjp_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="財政状態に関する注記")
    """ 財政状態に関する注記 """
    note_to_forecasts:NoteToForecasts_edjp_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="業績予想に関する事項、注記")
    """ 業績予想に関する事項、注記 """
    note_to_fraction_processing_method:NoteToFractionProcessingMethod_edjp_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="端数処理方法に関する注記")
    """ 端数処理方法に関する注記 """
    note_to_number_of_issued_and_outstanding_shares_common_stock:NoteToNumberOfIssuedAndOutstandingSharesCommonStock_edjp_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="発行済株式数（普通株式）に関する注記")
    """ 発行済株式数（普通株式）に関する注記 """
    note_to_operating_results:NoteToOperatingResults_edjp_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="経営成績に関する注記")
    """ 経営成績に関する注記 """
    note_to_significant_changes_in_the_scope_of_consolidation_during_the_period:NoteToSignificantChangesInTheScopeOfConsolidationDuringThePeriod_edjp_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="期中における連結範囲の重要な変更に関する注記")
    """ 期中における連結範囲の重要な変更に関する注記 """
    preamble_to_forecasts:PreambleToForecasts_edjp_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="業績予想に関する事項")
    """ 業績予想に関する事項 """
    retrospective_restatement:RetrospectiveRestatement_edjp_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="修正再表示")
    """ 修正再表示 """
    review_of_attached_consolidated_quarterly_financial_statements_by_a_certified_public_accountant_or_an_audit_firm:ReviewOfAttachedConsolidatedQuarterlyFinancialStatementsByACertifiedPublicAccountantOrAnAuditFirm_edjp_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="添付される四半期連結財務諸表に対する公認会計士又は監査法人によるレビュー")
    """ 添付される四半期連結財務諸表に対する公認会計士又は監査法人によるレビュー """
    sapporo_stock_exchange:SapporoStockExchange_edjp_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="札幌証券取引所")
    """ 札幌証券取引所 """
    sapporo_stock_exchange_ambitious:SapporoStockExchangeAmbitious_edjp_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="札幌証券取引所 アンビシャス")
    """ 札幌証券取引所 アンビシャス """
    sapporo_stock_exchange_established:SapporoStockExchangeEstablished_edjp_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="札幌証券取引所 既存市場")
    """ 札幌証券取引所 既存市場 """
    sapporo_stock_exchange_others:SapporoStockExchangeOthers_edjp_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="札幌証券取引所 その他")
    """ 札幌証券取引所 その他 """
    securities_code:SecuritiesCode_edjp_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="コード番号")
    """ コード番号 """
    significant_changes_in_the_scope_of_consolidation_during_the_period:SignificantChangesInTheScopeOfConsolidationDuringThePeriod_edjp_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="期中における連結範囲の重要な変更")
    """ 期中における連結範囲の重要な変更 """
    specific_business:SpecificBusiness_edjp_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="特定事業会社")
    """ 特定事業会社 """
    supplemental_material_of_results:SupplementalMaterialOfResults_edjp_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="決算補足説明資料作成の有無、期中")
    """ 決算補足説明資料作成の有無、期中 """
    target_for_briefing_of_results:TargetForBriefingOfResults_edjp_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="決算説明会の対象者")
    """ 決算説明会の対象者 """
    tel:Tel_edjp_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="TEL")
    """ TEL """
    title_for_forecasts:TitleForForecasts_edjp_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="業績予想タイトル名称")
    """ 業績予想タイトル名称 """
    title_inquiries:TitleInquiries_edjp_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="役職名、問合せ先責任者")
    """ 役職名、問合せ先責任者 """
    title_representative:TitleRepresentative_edjp_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="役職名、代表者")
    """ 役職名、代表者 """
    tokyo_stock_exchange:TokyoStockExchange_edjp_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="東京証券取引所")
    """ 東京証券取引所 """
    tokyo_stock_exchange_growth:TokyoStockExchangeGrowth_edjp_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="東京証券取引所 グロース")
    """ 東京証券取引所 グロース """
    tokyo_stock_exchange_others:TokyoStockExchangeOthers_edjp_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="東京証券取引所 その他")
    """ 東京証券取引所 その他 """
    tokyo_stock_exchange_prime:TokyoStockExchangePrime_edjp_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="東京証券取引所 プライム")
    """ 東京証券取引所 プライム """
    tokyo_stock_exchange_pro_market:TokyoStockExchangePROMarket_edjp_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="東京証券取引所 PRO Market")
    """ 東京証券取引所 PRO Market """
    tokyo_stock_exchange_standard:TokyoStockExchangeStandard_edjp_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="東京証券取引所 スタンダード")
    """ 東京証券取引所 スタンダード """
    URL:URL_edjp_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="URL")
    """ URL """
    way_of_getting_supplemental_material_of_results:WayOfGettingSupplementalMaterialOfResults_edjp_FinancialReportSummary_consolidated_Q3 = Field(default=None, description="入手方法等、決算補足説明資料、期中")
    """ 入手方法等、決算補足説明資料、期中 """


class edjp_FinancialReportSummary(IxbrlBase):
    applying_of_specific_accounting_of_the_consolidated_semi_annual_financial_statements:ApplyingOfSpecificAccountingOfTheConsolidatedSemiAnnualFinancialStatements_edjp_FinancialReportSummary = Field(default=None, description="中間連結財務諸表の作成に特有の会計処理の適用")
    """ 中間連結財務諸表の作成に特有の会計処理の適用 """
    changes_based_on_revisions_of_accounting_standard:ChangesBasedOnRevisionsOfAccountingStandard_edjp_FinancialReportSummary = Field(default=None, description="会計基準等の改正に伴う会計方針の変更")
    """ 会計基準等の改正に伴う会計方針の変更 """
    changes_in_accounting_estimates:ChangesInAccountingEstimates_edjp_FinancialReportSummary = Field(default=None, description="会計上の見積りの変更")
    """ 会計上の見積りの変更 """
    changes_other_than_ones_based_on_revisions_of_accounting_standard:ChangesOtherThanOnesBasedOnRevisionsOfAccountingStandard_edjp_FinancialReportSummary = Field(default=None, description="会計基準等の改正に伴う変更以外の会計方針の変更")
    """ 会計基準等の改正に伴う変更以外の会計方針の変更 """
    company_name:CompanyName_edjp_FinancialReportSummary = Field(default=None, description="上場会社名")
    """ 上場会社名 """
    convening_briefing_of_results:ConveningBriefingOfResults_edjp_FinancialReportSummary = Field(default=None, description="決算説明会開催の有無、期中")
    """ 決算説明会開催の有無、期中 """
    correction_of_consolidated_financial_forecast_in_this_quarter:CorrectionOfConsolidatedFinancialForecastInThisQuarter_edjp_FinancialReportSummary = Field(default=None, description="直近に公表されている業績予想からの修正の有無、連結")
    """ 直近に公表されている業績予想からの修正の有無、連結 """
    correction_of_dividend_forecast_in_this_quarter:CorrectionOfDividendForecastInThisQuarter_edjp_FinancialReportSummary = Field(default=None, description="直近に公表されている配当予想からの修正の有無")
    """ 直近に公表されている配当予想からの修正の有無 """
    dividend_payable_date_as_planned:DividendPayableDateAsPlanned_edjp_FinancialReportSummary = Field(default=None, description="配当支払開始予定日")
    """ 配当支払開始予定日 """
    document_name:DocumentName_edjp_FinancialReportSummary = Field(default=None, description="文書名")
    """ 文書名 """
    fasf_member_mark:FASFMemberMark_edjp_FinancialReportSummary = Field(default=None, description="財務会計基準機構会員マーク")
    """ 財務会計基準機構会員マーク """
    filing_date:FilingDate_edjp_FinancialReportSummary = Field(default=None, description="提出日")
    """ 提出日 """
    fiscal_year_end:FiscalYearEnd_edjp_FinancialReportSummary = Field(default=None, description="決算期")
    """ 決算期 """
    fukuoka_stock_exchange:FukuokaStockExchange_edjp_FinancialReportSummary = Field(default=None, description="福岡証券取引所")
    """ 福岡証券取引所 """
    fukuoka_stock_exchange_established:FukuokaStockExchangeEstablished_edjp_FinancialReportSummary = Field(default=None, description="福岡証券取引所 既存市場")
    """ 福岡証券取引所 既存市場 """
    fukuoka_stock_exchange_others:FukuokaStockExchangeOthers_edjp_FinancialReportSummary = Field(default=None, description="福岡証券取引所 その他")
    """ 福岡証券取引所 その他 """
    fukuoka_stock_exchange_q_board:FukuokaStockExchangeQBoard_edjp_FinancialReportSummary = Field(default=None, description="福岡証券取引所 Q-Board")
    """ 福岡証券取引所 Q-Board """
    general_business:GeneralBusiness_edjp_FinancialReportSummary = Field(default=None, description="一般事業会社")
    """ 一般事業会社 """
    japan_securities_dealers_association:JapanSecuritiesDealersAssociation_edjp_FinancialReportSummary = Field(default=None, description="フェニックス")
    """ フェニックス """
    japan_securities_dealers_association_green_sheet:JapanSecuritiesDealersAssociationGreenSheet_edjp_FinancialReportSummary = Field(default=None, description="日本証券業協会 フェニックス")
    """ 日本証券業協会 フェニックス """
    nagoya_stock_exchange:NagoyaStockExchange_edjp_FinancialReportSummary = Field(default=None, description="名古屋証券取引所")
    """ 名古屋証券取引所 """
    nagoya_stock_exchange1st_section:NagoyaStockExchange1stSection_edjp_FinancialReportSummary = Field(default=None, description="名古屋証券取引所 プレミア")
    """ 名古屋証券取引所 プレミア """
    nagoya_stock_exchange2nd_section:NagoyaStockExchange2ndSection_edjp_FinancialReportSummary = Field(default=None, description="名古屋証券取引所 メイン")
    """ 名古屋証券取引所 メイン """
    nagoya_stock_exchange_centrex:NagoyaStockExchangeCentrex_edjp_FinancialReportSummary = Field(default=None, description="名古屋証券取引所 ネクスト")
    """ 名古屋証券取引所 ネクスト """
    nagoya_stock_exchange_others:NagoyaStockExchangeOthers_edjp_FinancialReportSummary = Field(default=None, description="名古屋証券取引所 その他")
    """ 名古屋証券取引所 その他 """
    name_inquiries:NameInquiries_edjp_FinancialReportSummary = Field(default=None, description="氏名、問合せ先責任者")
    """ 氏名、問合せ先責任者 """
    name_representative:NameRepresentative_edjp_FinancialReportSummary = Field(default=None, description="氏名、代表者")
    """ 氏名、代表者 """
    notes_for_using_forecasted_information_and_others:NotesForUsingForecastedInformationAndOthers_edjp_FinancialReportSummary = Field(default=None, description="業績予想の適切な利用に関する説明、その他特記事項")
    """ 業績予想の適切な利用に関する説明、その他特記事項 """
    note_to_applying_of_specific_accounting_of_the_consolidated_semi_annual_financial_statements:NoteToApplyingOfSpecificAccountingOfTheConsolidatedSemiAnnualFinancialStatements_edjp_FinancialReportSummary = Field(default=None, description="中間連結財務諸表の作成に特有の会計処理の適用に関する注記")
    """ 中間連結財務諸表の作成に特有の会計処理の適用に関する注記 """
    note_to_changes_in_accounting_policies_accounting_estimates_and_retrospective_restatement_quarterly_consolidated:NoteToChangesInAccountingPoliciesAccountingEstimatesAndRetrospectiveRestatementQuarterlyConsolidated_edjp_FinancialReportSummary = Field(default=None, description="会計方針の変更・会計上の見積りの変更・修正再表示に関する注記、四半期")
    """ 会計方針の変更・会計上の見積りの変更・修正再表示に関する注記、四半期 """
    note_to_consolidated_financial_results:NoteToConsolidatedFinancialResults_edjp_FinancialReportSummary = Field(default=None, description="連結業績に関する注記")
    """ 連結業績に関する注記 """
    note_to_dividends:NoteToDividends_edjp_FinancialReportSummary = Field(default=None, description="配当の状況に関する注記")
    """ 配当の状況に関する注記 """
    note_to_financial_positions:NoteToFinancialPositions_edjp_FinancialReportSummary = Field(default=None, description="財政状態に関する注記")
    """ 財政状態に関する注記 """
    note_to_forecasts:NoteToForecasts_edjp_FinancialReportSummary = Field(default=None, description="業績予想に関する事項、注記")
    """ 業績予想に関する事項、注記 """
    note_to_fraction_processing_method:NoteToFractionProcessingMethod_edjp_FinancialReportSummary = Field(default=None, description="端数処理方法に関する注記")
    """ 端数処理方法に関する注記 """
    note_to_number_of_issued_and_outstanding_shares_common_stock:NoteToNumberOfIssuedAndOutstandingSharesCommonStock_edjp_FinancialReportSummary = Field(default=None, description="発行済株式数（普通株式）に関する注記")
    """ 発行済株式数（普通株式）に関する注記 """
    note_to_operating_results:NoteToOperatingResults_edjp_FinancialReportSummary = Field(default=None, description="経営成績に関する注記")
    """ 経営成績に関する注記 """
    note_to_significant_changes_in_the_scope_of_consolidation_during_the_period:NoteToSignificantChangesInTheScopeOfConsolidationDuringThePeriod_edjp_FinancialReportSummary = Field(default=None, description="期中における連結範囲の重要な変更に関する注記")
    """ 期中における連結範囲の重要な変更に関する注記 """
    preamble_to_forecasts:PreambleToForecasts_edjp_FinancialReportSummary = Field(default=None, description="業績予想に関する事項")
    """ 業績予想に関する事項 """
    retrospective_restatement:RetrospectiveRestatement_edjp_FinancialReportSummary = Field(default=None, description="修正再表示")
    """ 修正再表示 """
    sapporo_stock_exchange:SapporoStockExchange_edjp_FinancialReportSummary = Field(default=None, description="札幌証券取引所")
    """ 札幌証券取引所 """
    sapporo_stock_exchange_ambitious:SapporoStockExchangeAmbitious_edjp_FinancialReportSummary = Field(default=None, description="札幌証券取引所 アンビシャス")
    """ 札幌証券取引所 アンビシャス """
    sapporo_stock_exchange_established:SapporoStockExchangeEstablished_edjp_FinancialReportSummary = Field(default=None, description="札幌証券取引所 既存市場")
    """ 札幌証券取引所 既存市場 """
    sapporo_stock_exchange_others:SapporoStockExchangeOthers_edjp_FinancialReportSummary = Field(default=None, description="札幌証券取引所 その他")
    """ 札幌証券取引所 その他 """
    securities_code:SecuritiesCode_edjp_FinancialReportSummary = Field(default=None, description="コード番号")
    """ コード番号 """
    semi_annual_statement_filing_date_as_planned:SemiAnnualStatementFilingDateAsPlanned_edjp_FinancialReportSummary = Field(default=None, description="半期報告書提出予定日")
    """ 半期報告書提出予定日 """
    significant_changes_in_the_scope_of_consolidation_during_the_period:SignificantChangesInTheScopeOfConsolidationDuringThePeriod_edjp_FinancialReportSummary = Field(default=None, description="期中における連結範囲の重要な変更")
    """ 期中における連結範囲の重要な変更 """
    specific_business:SpecificBusiness_edjp_FinancialReportSummary = Field(default=None, description="特定事業会社")
    """ 特定事業会社 """
    supplemental_material_of_results:SupplementalMaterialOfResults_edjp_FinancialReportSummary = Field(default=None, description="決算補足説明資料作成の有無、期中")
    """ 決算補足説明資料作成の有無、期中 """
    target_for_briefing_of_results:TargetForBriefingOfResults_edjp_FinancialReportSummary = Field(default=None, description="決算説明会の対象者")
    """ 決算説明会の対象者 """
    tel:Tel_edjp_FinancialReportSummary = Field(default=None, description="TEL")
    """ TEL """
    title_for_forecasts:TitleForForecasts_edjp_FinancialReportSummary = Field(default=None, description="業績予想タイトル名称")
    """ 業績予想タイトル名称 """
    title_inquiries:TitleInquiries_edjp_FinancialReportSummary = Field(default=None, description="役職名、問合せ先責任者")
    """ 役職名、問合せ先責任者 """
    title_representative:TitleRepresentative_edjp_FinancialReportSummary = Field(default=None, description="役職名、代表者")
    """ 役職名、代表者 """
    tokyo_stock_exchange:TokyoStockExchange_edjp_FinancialReportSummary = Field(default=None, description="東京証券取引所")
    """ 東京証券取引所 """
    tokyo_stock_exchange_growth:TokyoStockExchangeGrowth_edjp_FinancialReportSummary = Field(default=None, description="東京証券取引所 グロース")
    """ 東京証券取引所 グロース """
    tokyo_stock_exchange_others:TokyoStockExchangeOthers_edjp_FinancialReportSummary = Field(default=None, description="東京証券取引所 その他")
    """ 東京証券取引所 その他 """
    tokyo_stock_exchange_prime:TokyoStockExchangePrime_edjp_FinancialReportSummary = Field(default=None, description="東京証券取引所 プライム")
    """ 東京証券取引所 プライム """
    tokyo_stock_exchange_pro_market:TokyoStockExchangePROMarket_edjp_FinancialReportSummary = Field(default=None, description="東京証券取引所 PRO Market")
    """ 東京証券取引所 PRO Market """
    tokyo_stock_exchange_standard:TokyoStockExchangeStandard_edjp_FinancialReportSummary = Field(default=None, description="東京証券取引所 スタンダード")
    """ 東京証券取引所 スタンダード """
    URL:URL_edjp_FinancialReportSummary = Field(default=None, description="URL")
    """ URL """
    way_of_getting_supplemental_material_of_results:WayOfGettingSupplementalMaterialOfResults_edjp_FinancialReportSummary = Field(default=None, description="入手方法等、決算補足説明資料、期中")
    """ 入手方法等、決算補足説明資料、期中 """


class edjp_MajorComponentsOfSellingGeneralAndAdministrativeExpenses_consolidated_Q2(IxbrlBase):
    major_components_of_selling_general_and_administrative_expenses_text_block:MajorComponentsOfSellingGeneralAndAdministrativeExpensesTextBlock_edjp_MajorComponentsOfSellingGeneralAndAdministrativeExpenses_consolidated_Q2 = Field(default=None, description="主要な販売費及び一般管理費 [テキストブロック]")
    """ 主要な販売費及び一般管理費 [テキストブロック] """


class edjp_NotesRegardingGuaranteeObligations_consolidated_Q2(IxbrlBase):
    notes_regarding_guarantee_obligations_text_block:NotesRegardingGuaranteeObligationsTextBlock_edjp_NotesRegardingGuaranteeObligations_consolidated_Q2 = Field(default=None, description="保証債務の注記 [テキストブロック]")
    """ 保証債務の注記 [テキストブロック] """


class edjp_NotesRegardingImpairmentLoss_consolidated_Q2(IxbrlBase):
    notes_regarding_impairment_loss_text_block:NotesRegardingImpairmentLossTextBlock_edjp_NotesRegardingImpairmentLoss_consolidated_Q2 = Field(default=None, description="減損損失に関する注記 [テキストブロック]")
    """ 減損損失に関する注記 [テキストブロック] """


class edjp_NotesRegardingPromissoryNotesDueOnBalanceSheetDate_consolidated_Q2(IxbrlBase):
    notes_regarding_promissory_notes_due_on_balance_sheet_date_text_block:NotesRegardingPromissoryNotesDueOnBalanceSheetDateTextBlock_edjp_NotesRegardingPromissoryNotesDueOnBalanceSheetDate_consolidated_Q2 = Field(default=None, description="期末日満期手形の会計処理 [テキストブロック]")
    """ 期末日満期手形の会計処理 [テキストブロック] """


class edjp_NotesRegardingProvisionOfReservesIncludedInCostOfSales_consolidated_Q2(IxbrlBase):
    notes_regarding_impairment_loss_text_block:NotesRegardingImpairmentLossTextBlock_edjp_NotesRegardingProvisionOfReservesIncludedInCostOfSales_consolidated_Q2 = Field(default=None, description="減損損失に関する注記 [テキストブロック]")
    """ 減損損失に関する注記 [テキストブロック] """


class edjp_NotesSegmentInformationEtcConsolidatedFinancialStatements_consolidated_FY(IxbrlBase):
    description_of_factors_which_led_to_recognition_of_gain_on_bargain_purchase_text_block:DescriptionOfFactorsWhichLedToRecognitionOfGainOnBargainPurchaseTextBlock_edjp_NotesSegmentInformationEtcConsolidatedFinancialStatements_consolidated_FY = Field(default=None, description="報告セグメントごとの負ののれん発生益を認識する要因となった事象の概要 [テキストブロック]")
    """ 報告セグメントごとの負ののれん発生益を認識する要因となった事象の概要 [テキストブロック] """
    description_of_reportable_segments_text_block:DescriptionOfReportableSegmentsTextBlock_edjp_NotesSegmentInformationEtcConsolidatedFinancialStatements_consolidated_FY = Field(default=None, description="報告セグメントの概要 [テキストブロック]")
    """ 報告セグメントの概要 [テキストブロック] """
    explanation_of_measurements_of_sales_profit_loss_asset_liability_and_other_items_for_each_reportable_segment_text_block:ExplanationOfMeasurementsOfSalesProfitLossAssetLiabilityAndOtherItemsForEachReportableSegmentTextBlock_edjp_NotesSegmentInformationEtcConsolidatedFinancialStatements_consolidated_FY = Field(default=None, description="報告セグメントごとの売上高、利益又は損失、資産、負債その他の項目の金額の算定方法 [テキストブロック]")
    """ 報告セグメントごとの売上高、利益又は損失、資産、負債その他の項目の金額の算定方法 [テキストブロック] """
    footnotes_regarding_segment_information_table_text_block:FootnotesRegardingSegmentInformationTableTextBlock_edjp_NotesSegmentInformationEtcConsolidatedFinancialStatements_consolidated_FY = Field(default=None, description="セグメント表の脚注 [テキストブロック]")
    """ セグメント表の脚注 [テキストブロック] """
    information_for_each_of_main_customers_text_block:InformationForEachOfMainCustomersTextBlock_edjp_NotesSegmentInformationEtcConsolidatedFinancialStatements_consolidated_FY = Field(default=None, description="主要な顧客ごとの情報 [テキストブロック]")
    """ 主要な顧客ごとの情報 [テキストブロック] """
    information_for_each_product_or_service_text_block:InformationForEachProductOrServiceTextBlock_edjp_NotesSegmentInformationEtcConsolidatedFinancialStatements_consolidated_FY = Field(default=None, description="製品及びサービスごとの情報 [テキストブロック]")
    """ 製品及びサービスごとの情報 [テキストブロック] """
    notes_segment_information_etc_consolidated_financial_statements_text_block:NotesSegmentInformationEtcConsolidatedFinancialStatementsTextBlock_edjp_NotesSegmentInformationEtcConsolidatedFinancialStatements_consolidated_FY = Field(default=None, description="セグメント情報等、連結財務諸表 [テキストブロック]")
    """ セグメント情報等、連結財務諸表 [テキストブロック] """
    property_plant_and_equipment_information_for_each_region_text_block:PropertyPlantAndEquipmentInformationForEachRegionTextBlock_edjp_NotesSegmentInformationEtcConsolidatedFinancialStatements_consolidated_FY = Field(default=None, description="有形固定資産、地域ごとの情報 [テキストブロック]")
    """ 有形固定資産、地域ごとの情報 [テキストブロック] """
    revenues_from_external_customers_information_for_each_region_text_block:RevenuesFromExternalCustomersInformationForEachRegionTextBlock_edjp_NotesSegmentInformationEtcConsolidatedFinancialStatements_consolidated_FY = Field(default=None, description="売上高、地域ごとの情報 [テキストブロック]")
    """ 売上高、地域ごとの情報 [テキストブロック] """


class edjp_NotesSegmentInformationEtcFinancialStatements_Nonconsolidated_FY(IxbrlBase):
    description_of_fact_that_companys_business_comprises_single_segment:DescriptionOfFactThatCompanysBusinessComprisesSingleSegment_edjp_NotesSegmentInformationEtcFinancialStatements_Nonconsolidated_FY = Field(default=None, description="単一セグメントである旨")
    """ 単一セグメントである旨 """
    notes_segment_information_etc_financial_statements_text_block:NotesSegmentInformationEtcFinancialStatementsTextBlock_edjp_NotesSegmentInformationEtcFinancialStatements_Nonconsolidated_FY = Field(default=None, description="セグメント情報等、財務諸表 [テキストブロック]")
    """ セグメント情報等、財務諸表 [テキストブロック] """


class edjp_NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatements_consolidated_Q1(IxbrlBase):
    description_of_fact_that_companys_business_comprises_single_segment:DescriptionOfFactThatCompanysBusinessComprisesSingleSegment_edjp_NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatements_consolidated_Q1 = Field(default=None, description="単一セグメントである旨")
    """ 単一セグメントである旨 """
    disclosure_of_changes_etc_in_reportable_segments_text_block:DisclosureOfChangesEtcInReportableSegmentsTextBlock_edjp_NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatements_consolidated_Q1 = Field(default=None, description="報告セグメントの変更等に関する事項 [テキストブロック]")
    """ 報告セグメントの変更等に関する事項 [テキストブロック] """
    footnotes_regarding_segment_information_table_text_block:FootnotesRegardingSegmentInformationTableTextBlock_edjp_NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatements_consolidated_Q1 = Field(default=None, description="セグメント表の脚注 [テキストブロック]")
    """ セグメント表の脚注 [テキストブロック] """
    notes_segment_information_etc_quarterly_consolidated_financial_statements_text_block:NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatementsTextBlock_edjp_NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatements_consolidated_Q1 = Field(default=None, description="セグメント情報等、四半期連結財務諸表 [テキストブロック]")
    """ セグメント情報等、四半期連結財務諸表 [テキストブロック] """


class edjp_NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatements_consolidated_Q2(IxbrlBase):
    description_of_fact_that_companys_business_comprises_single_segment:DescriptionOfFactThatCompanysBusinessComprisesSingleSegment_edjp_NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatements_consolidated_Q2 = Field(default=None, description="単一セグメントである旨")
    """ 単一セグメントである旨 """
    description_of_nature_of_differences_between_profit_loss_of_reportable_segments_total_and_quarterly_financial_statements_text_block:DescriptionOfNatureOfDifferencesBetweenProfitLossOfReportableSegmentsTotalAndQuarterlyFinancialStatementsTextBlock_edjp_NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatements_consolidated_Q2 = Field(default=None, description="報告セグメントごとの利益又は損失の金額の合計額と四半期損益計算書計上額との差額及び当該差額の主な内容（差異調整に関する事項） [テキストブロック]")
    """ 報告セグメントごとの利益又は損失の金額の合計額と四半期損益計算書計上額との差額及び当該差額の主な内容（差異調整に関する事項） [テキストブロック] """
    disclosure_of_changes_etc_in_reportable_segments_text_block:DisclosureOfChangesEtcInReportableSegmentsTextBlock_edjp_NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatements_consolidated_Q2 = Field(default=None, description="報告セグメントの変更等に関する事項 [テキストブロック]")
    """ 報告セグメントの変更等に関する事項 [テキストブロック] """
    footnotes_regarding_segment_information_table_text_block:FootnotesRegardingSegmentInformationTableTextBlock_edjp_NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatements_consolidated_Q2 = Field(default=None, description="セグメント表の脚注 [テキストブロック]")
    """ セグメント表の脚注 [テキストブロック] """
    information_about_assets_for_each_reportable_segment_text_block:InformationAboutAssetsForEachReportableSegmentTextBlock_edjp_NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatements_consolidated_Q2 = Field(default=None, description="報告セグメントごとの資産に関する情報 [テキストブロック]")
    """ 報告セグメントごとの資産に関する情報 [テキストブロック] """
    information_about_impairment_loss_of_non_current_assets_or_goodwill_etc_for_each_reportable_segment_text_block:InformationAboutImpairmentLossOfNonCurrentAssetsOrGoodwillEtcForEachReportableSegmentTextBlock_edjp_NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatements_consolidated_Q2 = Field(default=None, description="報告セグメントごとの固定資産の減損損失又はのれん等に関する情報 [テキストブロック]")
    """ 報告セグメントごとの固定資産の減損損失又はのれん等に関する情報 [テキストブロック] """
    notes_segment_information_etc_quarterly_consolidated_financial_statements_text_block:NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatementsTextBlock_edjp_NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatements_consolidated_Q2 = Field(default=None, description="セグメント情報等、四半期連結財務諸表 [テキストブロック]")
    """ セグメント情報等、四半期連結財務諸表 [テキストブロック] """
    revenues_from_external_customers_information_for_each_region_text_block:RevenuesFromExternalCustomersInformationForEachRegionTextBlock_edjp_NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatements_consolidated_Q2 = Field(default=None, description="売上高、地域ごとの情報 [テキストブロック]")
    """ 売上高、地域ごとの情報 [テキストブロック] """


class edjp_NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatements_consolidated_Q3(IxbrlBase):
    description_of_fact_that_companys_business_comprises_single_segment:DescriptionOfFactThatCompanysBusinessComprisesSingleSegment_edjp_NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatements_consolidated_Q3 = Field(default=None, description="単一セグメントである旨")
    """ 単一セグメントである旨 """
    description_of_nature_of_differences_between_profit_loss_of_reportable_segments_total_and_quarterly_financial_statements_text_block:DescriptionOfNatureOfDifferencesBetweenProfitLossOfReportableSegmentsTotalAndQuarterlyFinancialStatementsTextBlock_edjp_NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatements_consolidated_Q3 = Field(default=None, description="報告セグメントごとの利益又は損失の金額の合計額と四半期損益計算書計上額との差額及び当該差額の主な内容（差異調整に関する事項） [テキストブロック]")
    """ 報告セグメントごとの利益又は損失の金額の合計額と四半期損益計算書計上額との差額及び当該差額の主な内容（差異調整に関する事項） [テキストブロック] """
    disclosure_of_changes_etc_in_reportable_segments_text_block:DisclosureOfChangesEtcInReportableSegmentsTextBlock_edjp_NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatements_consolidated_Q3 = Field(default=None, description="報告セグメントの変更等に関する事項 [テキストブロック]")
    """ 報告セグメントの変更等に関する事項 [テキストブロック] """
    footnotes_regarding_segment_information_table_text_block:FootnotesRegardingSegmentInformationTableTextBlock_edjp_NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatements_consolidated_Q3 = Field(default=None, description="セグメント表の脚注 [テキストブロック]")
    """ セグメント表の脚注 [テキストブロック] """
    information_about_impairment_loss_of_non_current_assets_or_goodwill_etc_for_each_reportable_segment_text_block:InformationAboutImpairmentLossOfNonCurrentAssetsOrGoodwillEtcForEachReportableSegmentTextBlock_edjp_NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatements_consolidated_Q3 = Field(default=None, description="報告セグメントごとの固定資産の減損損失又はのれん等に関する情報 [テキストブロック]")
    """ 報告セグメントごとの固定資産の減損損失又はのれん等に関する情報 [テキストブロック] """
    notes_segment_information_etc_quarterly_consolidated_financial_statements_text_block:NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatementsTextBlock_edjp_NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatements_consolidated_Q3 = Field(default=None, description="セグメント情報等、四半期連結財務諸表 [テキストブロック]")
    """ セグメント情報等、四半期連結財務諸表 [テキストブロック] """


class edjp_NotesSegmentInformationEtcQuarterlyFinancialStatements_Nonconsolidated_Q1(IxbrlBase):
    description_of_fact_that_companys_business_comprises_single_segment:DescriptionOfFactThatCompanysBusinessComprisesSingleSegment_edjp_NotesSegmentInformationEtcQuarterlyFinancialStatements_Nonconsolidated_Q1 = Field(default=None, description="単一セグメントである旨")
    """ 単一セグメントである旨 """
    notes_segment_information_etc_quarterly_financial_statements_text_block:NotesSegmentInformationEtcQuarterlyFinancialStatementsTextBlock_edjp_NotesSegmentInformationEtcQuarterlyFinancialStatements_Nonconsolidated_Q1 = Field(default=None, description="セグメント情報等、四半期財務諸表 [テキストブロック]")
    """ セグメント情報等、四半期財務諸表 [テキストブロック] """


class edjp_NotesSegmentInformationEtcQuarterlyFinancialStatements_Nonconsolidated_Q2(IxbrlBase):
    footnotes_regarding_segment_information_table_text_block:FootnotesRegardingSegmentInformationTableTextBlock_edjp_NotesSegmentInformationEtcQuarterlyFinancialStatements_Nonconsolidated_Q2 = Field(default=None, description="セグメント表の脚注 [テキストブロック]")
    """ セグメント表の脚注 [テキストブロック] """
    information_about_impairment_loss_of_non_current_assets_or_goodwill_etc_for_each_reportable_segment_text_block:InformationAboutImpairmentLossOfNonCurrentAssetsOrGoodwillEtcForEachReportableSegmentTextBlock_edjp_NotesSegmentInformationEtcQuarterlyFinancialStatements_Nonconsolidated_Q2 = Field(default=None, description="報告セグメントごとの固定資産の減損損失又はのれん等に関する情報 [テキストブロック]")
    """ 報告セグメントごとの固定資産の減損損失又はのれん等に関する情報 [テキストブロック] """
    notes_segment_information_etc_quarterly_financial_statements_text_block:NotesSegmentInformationEtcQuarterlyFinancialStatementsTextBlock_edjp_NotesSegmentInformationEtcQuarterlyFinancialStatements_Nonconsolidated_Q2 = Field(default=None, description="セグメント情報等、四半期財務諸表 [テキストブロック]")
    """ セグメント情報等、四半期財務諸表 [テキストブロック] """


class edjp_QuarterlyBalanceSheet_Nonconsolidated_Q1(IxbrlBase):
    quarterly_balance_sheet_text_block:QuarterlyBalanceSheetTextBlock_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q1 = Field(default=None, description="四半期貸借対照表 [テキストブロック]")
    """ 四半期貸借対照表 [テキストブロック] """
    accounting_standards_dei:AccountingStandardsDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q1 = Field(default=None, description="会計基準、DEI")
    """ 会計基準、DEI """
    amendment_flag_dei:AmendmentFlagDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q1 = Field(default=None, description="訂正の有無、DEI")
    """ 訂正の有無、DEI """
    cabinet_office_ordinance_dei:CabinetOfficeOrdinanceDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q1 = Field(default=None, description="府令、DEI")
    """ 府令、DEI """
    comparative_period_end_date_dei:ComparativePeriodEndDateDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q1 = Field(default=None, description="比較対象会計期間終了日、DEI")
    """ 比較対象会計期間終了日、DEI """
    current_fiscal_year_end_date_dei:CurrentFiscalYearEndDateDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q1 = Field(default=None, description="当事業年度終了日、DEI")
    """ 当事業年度終了日、DEI """
    current_fiscal_year_start_date_dei:CurrentFiscalYearStartDateDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q1 = Field(default=None, description="当事業年度開始日、DEI")
    """ 当事業年度開始日、DEI """
    current_period_end_date_dei:CurrentPeriodEndDateDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q1 = Field(default=None, description="当会計期間終了日、DEI")
    """ 当会計期間終了日、DEI """
    document_type_dei:DocumentTypeDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q1 = Field(default=None, description="様式、DEI")
    """ 様式、DEI """
    edinet_code_dei:EDINETCodeDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q1 = Field(default=None, description="EDINETコード、DEI")
    """ EDINETコード、DEI """
    end_date_of_quarterly_or_semi_annual_period_of_next_fiscal_year_dei:EndDateOfQuarterlyOrSemiAnnualPeriodOfNextFiscalYearDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q1 = Field(default=None, description="次の四半期又は中間期の会計期間終了日、DEI")
    """ 次の四半期又は中間期の会計期間終了日、DEI """
    filer_name_in_english_dei:FilerNameInEnglishDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q1 = Field(default=None, description="提出者名（英語表記）、DEI")
    """ 提出者名（英語表記）、DEI """
    filer_name_in_japanese_dei:FilerNameInJapaneseDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q1 = Field(default=None, description="提出者名（日本語表記）、DEI")
    """ 提出者名（日本語表記）、DEI """
    fund_code_dei:FundCodeDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q1 = Field(default=None, description="ファンドコード、DEI")
    """ ファンドコード、DEI """
    fund_name_in_english_dei:FundNameInEnglishDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q1 = Field(default=None, description="ファンド名称（英語表記）、DEI")
    """ ファンド名称（英語表記）、DEI """
    fund_name_in_japanese_dei:FundNameInJapaneseDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q1 = Field(default=None, description="ファンド名称（日本語表記）、DEI")
    """ ファンド名称（日本語表記）、DEI """
    identification_of_document_subject_to_amendment_dei:IdentificationOfDocumentSubjectToAmendmentDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q1 = Field(default=None, description="訂正対象書類の書類管理番号、DEI")
    """ 訂正対象書類の書類管理番号、DEI """
    industry_code_when_consolidated_financial_statements_are_prepared_in_accordance_with_industry_specific_regulations_dei:IndustryCodeWhenConsolidatedFinancialStatementsArePreparedInAccordanceWithIndustrySpecificRegulationsDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q1 = Field(default=None, description="別記事業（連結）、DEI")
    """ 別記事業（連結）、DEI """
    industry_code_when_financial_statements_are_prepared_in_accordance_with_industry_specific_regulations_dei:IndustryCodeWhenFinancialStatementsArePreparedInAccordanceWithIndustrySpecificRegulationsDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q1 = Field(default=None, description="別記事業（個別）、DEI")
    """ 別記事業（個別）、DEI """
    next_fiscal_year_start_date_dei:NextFiscalYearStartDateDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q1 = Field(default=None, description="次の事業年度開始日、DEI")
    """ 次の事業年度開始日、DEI """
    previous_fiscal_year_end_date_dei:PreviousFiscalYearEndDateDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q1 = Field(default=None, description="前事業年度終了日、DEI")
    """ 前事業年度終了日、DEI """
    previous_fiscal_year_start_date_dei:PreviousFiscalYearStartDateDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q1 = Field(default=None, description="前事業年度開始日、DEI")
    """ 前事業年度開始日、DEI """
    report_amendment_flag_dei:ReportAmendmentFlagDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q1 = Field(default=None, description="記載事項訂正のフラグ、DEI")
    """ 記載事項訂正のフラグ、DEI """
    security_code_dei:SecurityCodeDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q1 = Field(default=None, description="証券コード、DEI")
    """ 証券コード、DEI """
    type_of_current_period_dei:TypeOfCurrentPeriodDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q1 = Field(default=None, description="当会計期間の種類、DEI")
    """ 当会計期間の種類、DEI """
    whether_consolidated_financial_statements_are_prepared_dei:WhetherConsolidatedFinancialStatementsArePreparedDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q1 = Field(default=None, description="連結決算の有無、DEI")
    """ 連結決算の有無、DEI """
    xbrl_amendment_flag_dei:XBRLAmendmentFlagDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q1 = Field(default=None, description="XBRL訂正のフラグ、DEI")
    """ XBRL訂正のフラグ、DEI """


class edjp_QuarterlyBalanceSheet_Nonconsolidated_Q2(IxbrlBase):
    quarterly_balance_sheet_text_block:QuarterlyBalanceSheetTextBlock_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q2 = Field(default=None, description="四半期貸借対照表 [テキストブロック]")
    """ 四半期貸借対照表 [テキストブロック] """
    accounting_standards_dei:AccountingStandardsDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q2 = Field(default=None, description="会計基準、DEI")
    """ 会計基準、DEI """
    amendment_flag_dei:AmendmentFlagDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q2 = Field(default=None, description="訂正の有無、DEI")
    """ 訂正の有無、DEI """
    cabinet_office_ordinance_dei:CabinetOfficeOrdinanceDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q2 = Field(default=None, description="府令、DEI")
    """ 府令、DEI """
    comparative_period_end_date_dei:ComparativePeriodEndDateDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q2 = Field(default=None, description="比較対象会計期間終了日、DEI")
    """ 比較対象会計期間終了日、DEI """
    current_fiscal_year_end_date_dei:CurrentFiscalYearEndDateDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q2 = Field(default=None, description="当事業年度終了日、DEI")
    """ 当事業年度終了日、DEI """
    current_fiscal_year_start_date_dei:CurrentFiscalYearStartDateDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q2 = Field(default=None, description="当事業年度開始日、DEI")
    """ 当事業年度開始日、DEI """
    current_period_end_date_dei:CurrentPeriodEndDateDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q2 = Field(default=None, description="当会計期間終了日、DEI")
    """ 当会計期間終了日、DEI """
    document_type_dei:DocumentTypeDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q2 = Field(default=None, description="様式、DEI")
    """ 様式、DEI """
    edinet_code_dei:EDINETCodeDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q2 = Field(default=None, description="EDINETコード、DEI")
    """ EDINETコード、DEI """
    end_date_of_quarterly_or_semi_annual_period_of_next_fiscal_year_dei:EndDateOfQuarterlyOrSemiAnnualPeriodOfNextFiscalYearDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q2 = Field(default=None, description="次の四半期又は中間期の会計期間終了日、DEI")
    """ 次の四半期又は中間期の会計期間終了日、DEI """
    filer_name_in_english_dei:FilerNameInEnglishDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q2 = Field(default=None, description="提出者名（英語表記）、DEI")
    """ 提出者名（英語表記）、DEI """
    filer_name_in_japanese_dei:FilerNameInJapaneseDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q2 = Field(default=None, description="提出者名（日本語表記）、DEI")
    """ 提出者名（日本語表記）、DEI """
    fund_code_dei:FundCodeDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q2 = Field(default=None, description="ファンドコード、DEI")
    """ ファンドコード、DEI """
    fund_name_in_english_dei:FundNameInEnglishDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q2 = Field(default=None, description="ファンド名称（英語表記）、DEI")
    """ ファンド名称（英語表記）、DEI """
    fund_name_in_japanese_dei:FundNameInJapaneseDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q2 = Field(default=None, description="ファンド名称（日本語表記）、DEI")
    """ ファンド名称（日本語表記）、DEI """
    identification_of_document_subject_to_amendment_dei:IdentificationOfDocumentSubjectToAmendmentDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q2 = Field(default=None, description="訂正対象書類の書類管理番号、DEI")
    """ 訂正対象書類の書類管理番号、DEI """
    industry_code_when_consolidated_financial_statements_are_prepared_in_accordance_with_industry_specific_regulations_dei:IndustryCodeWhenConsolidatedFinancialStatementsArePreparedInAccordanceWithIndustrySpecificRegulationsDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q2 = Field(default=None, description="別記事業（連結）、DEI")
    """ 別記事業（連結）、DEI """
    industry_code_when_financial_statements_are_prepared_in_accordance_with_industry_specific_regulations_dei:IndustryCodeWhenFinancialStatementsArePreparedInAccordanceWithIndustrySpecificRegulationsDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q2 = Field(default=None, description="別記事業（個別）、DEI")
    """ 別記事業（個別）、DEI """
    next_fiscal_year_start_date_dei:NextFiscalYearStartDateDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q2 = Field(default=None, description="次の事業年度開始日、DEI")
    """ 次の事業年度開始日、DEI """
    previous_fiscal_year_end_date_dei:PreviousFiscalYearEndDateDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q2 = Field(default=None, description="前事業年度終了日、DEI")
    """ 前事業年度終了日、DEI """
    previous_fiscal_year_start_date_dei:PreviousFiscalYearStartDateDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q2 = Field(default=None, description="前事業年度開始日、DEI")
    """ 前事業年度開始日、DEI """
    report_amendment_flag_dei:ReportAmendmentFlagDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q2 = Field(default=None, description="記載事項訂正のフラグ、DEI")
    """ 記載事項訂正のフラグ、DEI """
    security_code_dei:SecurityCodeDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q2 = Field(default=None, description="証券コード、DEI")
    """ 証券コード、DEI """
    type_of_current_period_dei:TypeOfCurrentPeriodDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q2 = Field(default=None, description="当会計期間の種類、DEI")
    """ 当会計期間の種類、DEI """
    whether_consolidated_financial_statements_are_prepared_dei:WhetherConsolidatedFinancialStatementsArePreparedDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q2 = Field(default=None, description="連結決算の有無、DEI")
    """ 連結決算の有無、DEI """
    xbrl_amendment_flag_dei:XBRLAmendmentFlagDEI_edjp_QuarterlyBalanceSheet_Nonconsolidated_Q2 = Field(default=None, description="XBRL訂正のフラグ、DEI")
    """ XBRL訂正のフラグ、DEI """


class edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q1(IxbrlBase):
    quarterly_consolidated_balance_sheet_text_block:QuarterlyConsolidatedBalanceSheetTextBlock_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q1 = Field(default=None, description="四半期連結貸借対照表 [テキストブロック]")
    """ 四半期連結貸借対照表 [テキストブロック] """
    accounting_standards_dei:AccountingStandardsDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q1 = Field(default=None, description="会計基準、DEI")
    """ 会計基準、DEI """
    amendment_flag_dei:AmendmentFlagDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q1 = Field(default=None, description="訂正の有無、DEI")
    """ 訂正の有無、DEI """
    cabinet_office_ordinance_dei:CabinetOfficeOrdinanceDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q1 = Field(default=None, description="府令、DEI")
    """ 府令、DEI """
    comparative_period_end_date_dei:ComparativePeriodEndDateDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q1 = Field(default=None, description="比較対象会計期間終了日、DEI")
    """ 比較対象会計期間終了日、DEI """
    current_fiscal_year_end_date_dei:CurrentFiscalYearEndDateDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q1 = Field(default=None, description="当事業年度終了日、DEI")
    """ 当事業年度終了日、DEI """
    current_fiscal_year_start_date_dei:CurrentFiscalYearStartDateDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q1 = Field(default=None, description="当事業年度開始日、DEI")
    """ 当事業年度開始日、DEI """
    current_period_end_date_dei:CurrentPeriodEndDateDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q1 = Field(default=None, description="当会計期間終了日、DEI")
    """ 当会計期間終了日、DEI """
    document_type_dei:DocumentTypeDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q1 = Field(default=None, description="様式、DEI")
    """ 様式、DEI """
    edinet_code_dei:EDINETCodeDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q1 = Field(default=None, description="EDINETコード、DEI")
    """ EDINETコード、DEI """
    end_date_of_quarterly_or_semi_annual_period_of_next_fiscal_year_dei:EndDateOfQuarterlyOrSemiAnnualPeriodOfNextFiscalYearDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q1 = Field(default=None, description="次の四半期又は中間期の会計期間終了日、DEI")
    """ 次の四半期又は中間期の会計期間終了日、DEI """
    filer_name_in_english_dei:FilerNameInEnglishDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q1 = Field(default=None, description="提出者名（英語表記）、DEI")
    """ 提出者名（英語表記）、DEI """
    filer_name_in_japanese_dei:FilerNameInJapaneseDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q1 = Field(default=None, description="提出者名（日本語表記）、DEI")
    """ 提出者名（日本語表記）、DEI """
    fund_code_dei:FundCodeDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q1 = Field(default=None, description="ファンドコード、DEI")
    """ ファンドコード、DEI """
    fund_name_in_english_dei:FundNameInEnglishDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q1 = Field(default=None, description="ファンド名称（英語表記）、DEI")
    """ ファンド名称（英語表記）、DEI """
    fund_name_in_japanese_dei:FundNameInJapaneseDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q1 = Field(default=None, description="ファンド名称（日本語表記）、DEI")
    """ ファンド名称（日本語表記）、DEI """
    identification_of_document_subject_to_amendment_dei:IdentificationOfDocumentSubjectToAmendmentDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q1 = Field(default=None, description="訂正対象書類の書類管理番号、DEI")
    """ 訂正対象書類の書類管理番号、DEI """
    industry_code_when_consolidated_financial_statements_are_prepared_in_accordance_with_industry_specific_regulations_dei:IndustryCodeWhenConsolidatedFinancialStatementsArePreparedInAccordanceWithIndustrySpecificRegulationsDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q1 = Field(default=None, description="別記事業（連結）、DEI")
    """ 別記事業（連結）、DEI """
    industry_code_when_financial_statements_are_prepared_in_accordance_with_industry_specific_regulations_dei:IndustryCodeWhenFinancialStatementsArePreparedInAccordanceWithIndustrySpecificRegulationsDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q1 = Field(default=None, description="別記事業（個別）、DEI")
    """ 別記事業（個別）、DEI """
    next_fiscal_year_start_date_dei:NextFiscalYearStartDateDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q1 = Field(default=None, description="次の事業年度開始日、DEI")
    """ 次の事業年度開始日、DEI """
    previous_fiscal_year_end_date_dei:PreviousFiscalYearEndDateDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q1 = Field(default=None, description="前事業年度終了日、DEI")
    """ 前事業年度終了日、DEI """
    previous_fiscal_year_start_date_dei:PreviousFiscalYearStartDateDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q1 = Field(default=None, description="前事業年度開始日、DEI")
    """ 前事業年度開始日、DEI """
    report_amendment_flag_dei:ReportAmendmentFlagDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q1 = Field(default=None, description="記載事項訂正のフラグ、DEI")
    """ 記載事項訂正のフラグ、DEI """
    security_code_dei:SecurityCodeDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q1 = Field(default=None, description="証券コード、DEI")
    """ 証券コード、DEI """
    type_of_current_period_dei:TypeOfCurrentPeriodDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q1 = Field(default=None, description="当会計期間の種類、DEI")
    """ 当会計期間の種類、DEI """
    whether_consolidated_financial_statements_are_prepared_dei:WhetherConsolidatedFinancialStatementsArePreparedDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q1 = Field(default=None, description="連結決算の有無、DEI")
    """ 連結決算の有無、DEI """
    xbrl_amendment_flag_dei:XBRLAmendmentFlagDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q1 = Field(default=None, description="XBRL訂正のフラグ、DEI")
    """ XBRL訂正のフラグ、DEI """


class edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q2(IxbrlBase):
    quarterly_consolidated_balance_sheet_text_block:QuarterlyConsolidatedBalanceSheetTextBlock_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q2 = Field(default=None, description="四半期連結貸借対照表 [テキストブロック]")
    """ 四半期連結貸借対照表 [テキストブロック] """
    accounting_standards_dei:AccountingStandardsDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q2 = Field(default=None, description="会計基準、DEI")
    """ 会計基準、DEI """
    amendment_flag_dei:AmendmentFlagDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q2 = Field(default=None, description="訂正の有無、DEI")
    """ 訂正の有無、DEI """
    cabinet_office_ordinance_dei:CabinetOfficeOrdinanceDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q2 = Field(default=None, description="府令、DEI")
    """ 府令、DEI """
    comparative_period_end_date_dei:ComparativePeriodEndDateDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q2 = Field(default=None, description="比較対象会計期間終了日、DEI")
    """ 比較対象会計期間終了日、DEI """
    current_fiscal_year_end_date_dei:CurrentFiscalYearEndDateDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q2 = Field(default=None, description="当事業年度終了日、DEI")
    """ 当事業年度終了日、DEI """
    current_fiscal_year_start_date_dei:CurrentFiscalYearStartDateDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q2 = Field(default=None, description="当事業年度開始日、DEI")
    """ 当事業年度開始日、DEI """
    current_period_end_date_dei:CurrentPeriodEndDateDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q2 = Field(default=None, description="当会計期間終了日、DEI")
    """ 当会計期間終了日、DEI """
    document_type_dei:DocumentTypeDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q2 = Field(default=None, description="様式、DEI")
    """ 様式、DEI """
    edinet_code_dei:EDINETCodeDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q2 = Field(default=None, description="EDINETコード、DEI")
    """ EDINETコード、DEI """
    end_date_of_quarterly_or_semi_annual_period_of_next_fiscal_year_dei:EndDateOfQuarterlyOrSemiAnnualPeriodOfNextFiscalYearDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q2 = Field(default=None, description="次の四半期又は中間期の会計期間終了日、DEI")
    """ 次の四半期又は中間期の会計期間終了日、DEI """
    filer_name_in_english_dei:FilerNameInEnglishDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q2 = Field(default=None, description="提出者名（英語表記）、DEI")
    """ 提出者名（英語表記）、DEI """
    filer_name_in_japanese_dei:FilerNameInJapaneseDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q2 = Field(default=None, description="提出者名（日本語表記）、DEI")
    """ 提出者名（日本語表記）、DEI """
    fund_code_dei:FundCodeDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q2 = Field(default=None, description="ファンドコード、DEI")
    """ ファンドコード、DEI """
    fund_name_in_english_dei:FundNameInEnglishDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q2 = Field(default=None, description="ファンド名称（英語表記）、DEI")
    """ ファンド名称（英語表記）、DEI """
    fund_name_in_japanese_dei:FundNameInJapaneseDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q2 = Field(default=None, description="ファンド名称（日本語表記）、DEI")
    """ ファンド名称（日本語表記）、DEI """
    identification_of_document_subject_to_amendment_dei:IdentificationOfDocumentSubjectToAmendmentDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q2 = Field(default=None, description="訂正対象書類の書類管理番号、DEI")
    """ 訂正対象書類の書類管理番号、DEI """
    industry_code_when_consolidated_financial_statements_are_prepared_in_accordance_with_industry_specific_regulations_dei:IndustryCodeWhenConsolidatedFinancialStatementsArePreparedInAccordanceWithIndustrySpecificRegulationsDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q2 = Field(default=None, description="別記事業（連結）、DEI")
    """ 別記事業（連結）、DEI """
    industry_code_when_financial_statements_are_prepared_in_accordance_with_industry_specific_regulations_dei:IndustryCodeWhenFinancialStatementsArePreparedInAccordanceWithIndustrySpecificRegulationsDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q2 = Field(default=None, description="別記事業（個別）、DEI")
    """ 別記事業（個別）、DEI """
    next_fiscal_year_start_date_dei:NextFiscalYearStartDateDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q2 = Field(default=None, description="次の事業年度開始日、DEI")
    """ 次の事業年度開始日、DEI """
    previous_fiscal_year_end_date_dei:PreviousFiscalYearEndDateDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q2 = Field(default=None, description="前事業年度終了日、DEI")
    """ 前事業年度終了日、DEI """
    previous_fiscal_year_start_date_dei:PreviousFiscalYearStartDateDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q2 = Field(default=None, description="前事業年度開始日、DEI")
    """ 前事業年度開始日、DEI """
    report_amendment_flag_dei:ReportAmendmentFlagDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q2 = Field(default=None, description="記載事項訂正のフラグ、DEI")
    """ 記載事項訂正のフラグ、DEI """
    security_code_dei:SecurityCodeDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q2 = Field(default=None, description="証券コード、DEI")
    """ 証券コード、DEI """
    type_of_current_period_dei:TypeOfCurrentPeriodDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q2 = Field(default=None, description="当会計期間の種類、DEI")
    """ 当会計期間の種類、DEI """
    whether_consolidated_financial_statements_are_prepared_dei:WhetherConsolidatedFinancialStatementsArePreparedDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q2 = Field(default=None, description="連結決算の有無、DEI")
    """ 連結決算の有無、DEI """
    xbrl_amendment_flag_dei:XBRLAmendmentFlagDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q2 = Field(default=None, description="XBRL訂正のフラグ、DEI")
    """ XBRL訂正のフラグ、DEI """


class edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q3(IxbrlBase):
    quarterly_consolidated_balance_sheet_text_block:QuarterlyConsolidatedBalanceSheetTextBlock_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q3 = Field(default=None, description="四半期連結貸借対照表 [テキストブロック]")
    """ 四半期連結貸借対照表 [テキストブロック] """
    accounting_standards_dei:AccountingStandardsDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q3 = Field(default=None, description="会計基準、DEI")
    """ 会計基準、DEI """
    amendment_flag_dei:AmendmentFlagDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q3 = Field(default=None, description="訂正の有無、DEI")
    """ 訂正の有無、DEI """
    cabinet_office_ordinance_dei:CabinetOfficeOrdinanceDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q3 = Field(default=None, description="府令、DEI")
    """ 府令、DEI """
    comparative_period_end_date_dei:ComparativePeriodEndDateDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q3 = Field(default=None, description="比較対象会計期間終了日、DEI")
    """ 比較対象会計期間終了日、DEI """
    current_fiscal_year_end_date_dei:CurrentFiscalYearEndDateDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q3 = Field(default=None, description="当事業年度終了日、DEI")
    """ 当事業年度終了日、DEI """
    current_fiscal_year_start_date_dei:CurrentFiscalYearStartDateDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q3 = Field(default=None, description="当事業年度開始日、DEI")
    """ 当事業年度開始日、DEI """
    current_period_end_date_dei:CurrentPeriodEndDateDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q3 = Field(default=None, description="当会計期間終了日、DEI")
    """ 当会計期間終了日、DEI """
    document_type_dei:DocumentTypeDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q3 = Field(default=None, description="様式、DEI")
    """ 様式、DEI """
    edinet_code_dei:EDINETCodeDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q3 = Field(default=None, description="EDINETコード、DEI")
    """ EDINETコード、DEI """
    end_date_of_quarterly_or_semi_annual_period_of_next_fiscal_year_dei:EndDateOfQuarterlyOrSemiAnnualPeriodOfNextFiscalYearDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q3 = Field(default=None, description="次の四半期又は中間期の会計期間終了日、DEI")
    """ 次の四半期又は中間期の会計期間終了日、DEI """
    filer_name_in_english_dei:FilerNameInEnglishDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q3 = Field(default=None, description="提出者名（英語表記）、DEI")
    """ 提出者名（英語表記）、DEI """
    filer_name_in_japanese_dei:FilerNameInJapaneseDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q3 = Field(default=None, description="提出者名（日本語表記）、DEI")
    """ 提出者名（日本語表記）、DEI """
    fund_code_dei:FundCodeDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q3 = Field(default=None, description="ファンドコード、DEI")
    """ ファンドコード、DEI """
    fund_name_in_english_dei:FundNameInEnglishDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q3 = Field(default=None, description="ファンド名称（英語表記）、DEI")
    """ ファンド名称（英語表記）、DEI """
    fund_name_in_japanese_dei:FundNameInJapaneseDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q3 = Field(default=None, description="ファンド名称（日本語表記）、DEI")
    """ ファンド名称（日本語表記）、DEI """
    identification_of_document_subject_to_amendment_dei:IdentificationOfDocumentSubjectToAmendmentDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q3 = Field(default=None, description="訂正対象書類の書類管理番号、DEI")
    """ 訂正対象書類の書類管理番号、DEI """
    industry_code_when_consolidated_financial_statements_are_prepared_in_accordance_with_industry_specific_regulations_dei:IndustryCodeWhenConsolidatedFinancialStatementsArePreparedInAccordanceWithIndustrySpecificRegulationsDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q3 = Field(default=None, description="別記事業（連結）、DEI")
    """ 別記事業（連結）、DEI """
    industry_code_when_financial_statements_are_prepared_in_accordance_with_industry_specific_regulations_dei:IndustryCodeWhenFinancialStatementsArePreparedInAccordanceWithIndustrySpecificRegulationsDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q3 = Field(default=None, description="別記事業（個別）、DEI")
    """ 別記事業（個別）、DEI """
    next_fiscal_year_start_date_dei:NextFiscalYearStartDateDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q3 = Field(default=None, description="次の事業年度開始日、DEI")
    """ 次の事業年度開始日、DEI """
    previous_fiscal_year_end_date_dei:PreviousFiscalYearEndDateDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q3 = Field(default=None, description="前事業年度終了日、DEI")
    """ 前事業年度終了日、DEI """
    previous_fiscal_year_start_date_dei:PreviousFiscalYearStartDateDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q3 = Field(default=None, description="前事業年度開始日、DEI")
    """ 前事業年度開始日、DEI """
    report_amendment_flag_dei:ReportAmendmentFlagDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q3 = Field(default=None, description="記載事項訂正のフラグ、DEI")
    """ 記載事項訂正のフラグ、DEI """
    security_code_dei:SecurityCodeDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q3 = Field(default=None, description="証券コード、DEI")
    """ 証券コード、DEI """
    type_of_current_period_dei:TypeOfCurrentPeriodDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q3 = Field(default=None, description="当会計期間の種類、DEI")
    """ 当会計期間の種類、DEI """
    whether_consolidated_financial_statements_are_prepared_dei:WhetherConsolidatedFinancialStatementsArePreparedDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q3 = Field(default=None, description="連結決算の有無、DEI")
    """ 連結決算の有無、DEI """
    xbrl_amendment_flag_dei:XBRLAmendmentFlagDEI_edjp_QuarterlyConsolidatedBalanceSheet_consolidated_Q3 = Field(default=None, description="XBRL訂正のフラグ、DEI")
    """ XBRL訂正のフラグ、DEI """


class edjp_QuarterlyConsolidatedStatementOfCashFlows_consolidated_Q2(IxbrlBase):
    quarterly_consolidated_statement_of_cash_flows_text_block:QuarterlyConsolidatedStatementOfCashFlowsTextBlock_edjp_QuarterlyConsolidatedStatementOfCashFlows_consolidated_Q2 = Field(default=None, description="四半期連結キャッシュ・フロー計算書 [テキストブロック]")
    """ 四半期連結キャッシュ・フロー計算書 [テキストブロック] """


class edjp_QuarterlyConsolidatedStatementOfCashFlows_consolidated_Q3(IxbrlBase):
    quarterly_consolidated_statement_of_cash_flows_text_block:QuarterlyConsolidatedStatementOfCashFlowsTextBlock_edjp_QuarterlyConsolidatedStatementOfCashFlows_consolidated_Q3 = Field(default=None, description="四半期連結キャッシュ・フロー計算書 [テキストブロック]")
    """ 四半期連結キャッシュ・フロー計算書 [テキストブロック] """


class edjp_QuarterlyStatementOfCashFlows_Nonconsolidated_Q2(IxbrlBase):
    quarterly_statement_of_cash_flows_text_block:QuarterlyStatementOfCashFlowsTextBlock_edjp_QuarterlyStatementOfCashFlows_Nonconsolidated_Q2 = Field(default=None, description="四半期キャッシュ・フロー計算書 [テキストブロック]")
    """ 四半期キャッシュ・フロー計算書 [テキストブロック] """


class edjp_StatementOfCashFlows_Nonconsolidated_FY(IxbrlBase):
    statement_of_cash_flows_text_block:StatementOfCashFlowsTextBlock_edjp_StatementOfCashFlows_Nonconsolidated_FY = Field(default=None, description="キャッシュ・フロー計算書 [テキストブロック]")
    """ キャッシュ・フロー計算書 [テキストブロック] """


class edjp_StatementOfChangesInEquity_Nonconsolidated_FY(IxbrlBase):
    statement_of_changes_in_equity_text_block:StatementOfChangesInEquityTextBlock_edjp_StatementOfChangesInEquity_Nonconsolidated_FY = Field(default=None, description="株主資本等変動計算書 [テキストブロック]")
    """ 株主資本等変動計算書 [テキストブロック] """


class edjp_StatementOfChangesInEquity_consolidated_FY(IxbrlBase):
    statement_of_changes_in_equity_text_block:StatementOfChangesInEquityTextBlock_edjp_StatementOfChangesInEquity_consolidated_FY = Field(default=None, description="株主資本等変動計算書 [テキストブロック]")
    """ 株主資本等変動計算書 [テキストブロック] """


class edjp_StatementOfIncome_Nonconsolidated_FY(IxbrlBase):
    statement_of_income_text_block:StatementOfIncomeTextBlock_edjp_StatementOfIncome_Nonconsolidated_FY = Field(default=None, description="損益計算書 [テキストブロック]")
    """ 損益計算書 [テキストブロック] """


class edjp_StatementOfIncome_consolidated_FY(IxbrlBase):
    statement_of_income_text_block:StatementOfIncomeTextBlock_edjp_StatementOfIncome_consolidated_FY = Field(default=None, description="損益計算書 [テキストブロック]")
    """ 損益計算書 [テキストブロック] """


class edjp_YearToQuarterEndConsolidatedStatementOfComprehensiveIncome_consolidated_Q1(IxbrlBase):
    year_to_quarter_end_consolidated_statement_of_comprehensive_income_text_block:YearToQuarterEndConsolidatedStatementOfComprehensiveIncomeTextBlock_edjp_YearToQuarterEndConsolidatedStatementOfComprehensiveIncome_consolidated_Q1 = Field(default=None, description="四半期連結累計期間、四半期連結包括利益計算書 [テキストブロック]")
    """ 四半期連結累計期間、四半期連結包括利益計算書 [テキストブロック] """


class edjp_YearToQuarterEndConsolidatedStatementOfComprehensiveIncome_consolidated_Q2(IxbrlBase):
    description_of_fact_that_companys_business_comprises_single_segment:DescriptionOfFactThatCompanysBusinessComprisesSingleSegment_edjp_YearToQuarterEndConsolidatedStatementOfComprehensiveIncome_consolidated_Q2 = Field(default=None, description="単一セグメントである旨")
    """ 単一セグメントである旨 """
    major_components_of_selling_general_and_administrative_expenses_text_block:MajorComponentsOfSellingGeneralAndAdministrativeExpensesTextBlock_edjp_YearToQuarterEndConsolidatedStatementOfComprehensiveIncome_consolidated_Q2 = Field(default=None, description="主要な販売費及び一般管理費 [テキストブロック]")
    """ 主要な販売費及び一般管理費 [テキストブロック] """
    notes_regarding_guarantee_obligations_text_block:NotesRegardingGuaranteeObligationsTextBlock_edjp_YearToQuarterEndConsolidatedStatementOfComprehensiveIncome_consolidated_Q2 = Field(default=None, description="保証債務の注記 [テキストブロック]")
    """ 保証債務の注記 [テキストブロック] """
    notes_regarding_shares_and_bonds_etc_of_unconsolidated_subsidiaries_and_associates_text_block:NotesRegardingSharesAndBondsEtcOfUnconsolidatedSubsidiariesAndAssociatesTextBlock_edjp_YearToQuarterEndConsolidatedStatementOfComprehensiveIncome_consolidated_Q2 = Field(default=None, description="非連結子会社及び関連会社の株式及び社債等 [テキストブロック]")
    """ 非連結子会社及び関連会社の株式及び社債等 [テキストブロック] """
    notes_segment_information_etc_quarterly_consolidated_financial_statements_text_block:NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatementsTextBlock_edjp_YearToQuarterEndConsolidatedStatementOfComprehensiveIncome_consolidated_Q2 = Field(default=None, description="セグメント情報等、四半期連結財務諸表 [テキストブロック]")
    """ セグメント情報等、四半期連結財務諸表 [テキストブロック] """
    year_to_quarter_end_consolidated_statement_of_comprehensive_income_text_block:YearToQuarterEndConsolidatedStatementOfComprehensiveIncomeTextBlock_edjp_YearToQuarterEndConsolidatedStatementOfComprehensiveIncome_consolidated_Q2 = Field(default=None, description="四半期連結累計期間、四半期連結包括利益計算書 [テキストブロック]")
    """ 四半期連結累計期間、四半期連結包括利益計算書 [テキストブロック] """


class edjp_YearToQuarterEndConsolidatedStatementOfComprehensiveIncome_consolidated_Q3(IxbrlBase):
    year_to_quarter_end_consolidated_statement_of_comprehensive_income_text_block:YearToQuarterEndConsolidatedStatementOfComprehensiveIncomeTextBlock_edjp_YearToQuarterEndConsolidatedStatementOfComprehensiveIncome_consolidated_Q3 = Field(default=None, description="四半期連結累計期間、四半期連結包括利益計算書 [テキストブロック]")
    """ 四半期連結累計期間、四半期連結包括利益計算書 [テキストブロック] """


class edjp_YearToQuarterEndConsolidatedStatementOfComprehensiveIncomeSingleStatement_consolidated_Q2(IxbrlBase):
    year_to_quarter_end_consolidated_statement_of_comprehensive_income_single_statement_text_block:YearToQuarterEndConsolidatedStatementOfComprehensiveIncomeSingleStatementTextBlock_edjp_YearToQuarterEndConsolidatedStatementOfComprehensiveIncomeSingleStatement_consolidated_Q2 = Field(default=None, description="四半期連結累計期間、四半期連結損益及び包括利益計算書 [テキストブロック]")
    """ 四半期連結累計期間、四半期連結損益及び包括利益計算書 [テキストブロック] """


class edjp_YearToQuarterEndConsolidatedStatementOfIncome_consolidated_Q1(IxbrlBase):
    year_to_quarter_end_consolidated_statement_of_income_text_block:YearToQuarterEndConsolidatedStatementOfIncomeTextBlock_edjp_YearToQuarterEndConsolidatedStatementOfIncome_consolidated_Q1 = Field(default=None, description="四半期連結累計期間、四半期連結損益計算書 [テキストブロック]")
    """ 四半期連結累計期間、四半期連結損益計算書 [テキストブロック] """


class edjp_YearToQuarterEndConsolidatedStatementOfIncome_consolidated_Q2(IxbrlBase):
    year_to_quarter_end_consolidated_statement_of_income_text_block:YearToQuarterEndConsolidatedStatementOfIncomeTextBlock_edjp_YearToQuarterEndConsolidatedStatementOfIncome_consolidated_Q2 = Field(default=None, description="四半期連結累計期間、四半期連結損益計算書 [テキストブロック]")
    """ 四半期連結累計期間、四半期連結損益計算書 [テキストブロック] """


class edjp_YearToQuarterEndConsolidatedStatementOfIncome_consolidated_Q3(IxbrlBase):
    year_to_quarter_end_consolidated_statement_of_income_text_block:YearToQuarterEndConsolidatedStatementOfIncomeTextBlock_edjp_YearToQuarterEndConsolidatedStatementOfIncome_consolidated_Q3 = Field(default=None, description="四半期連結累計期間、四半期連結損益計算書 [テキストブロック]")
    """ 四半期連結累計期間、四半期連結損益計算書 [テキストブロック] """


class edjp_YearToQuarterEndStatementOfIncome_Nonconsolidated_Q1(IxbrlBase):
    year_to_quarter_end_statement_of_income_text_block:YearToQuarterEndStatementOfIncomeTextBlock_edjp_YearToQuarterEndStatementOfIncome_Nonconsolidated_Q1 = Field(default=None, description="四半期累計期間、四半期損益計算書 [テキストブロック]")
    """ 四半期累計期間、四半期損益計算書 [テキストブロック] """


class edjp_YearToQuarterEndStatementOfIncome_Nonconsolidated_Q2(IxbrlBase):
    year_to_quarter_end_statement_of_income_text_block:YearToQuarterEndStatementOfIncomeTextBlock_edjp_YearToQuarterEndStatementOfIncome_Nonconsolidated_Q2 = Field(default=None, description="四半期累計期間、四半期損益計算書 [テキストブロック]")
    """ 四半期累計期間、四半期損益計算書 [テキストブロック] """


class edjp_FinancialReportSummary_consolidated_HY_specific_business(IxbrlBase):
    changes_based_on_revisions_of_accounting_standard:ChangesBasedOnRevisionsOfAccountingStandard_edjp_FinancialReportSummary_consolidated_HY_specific_business = Field(default=None, description="会計基準等の改正に伴う会計方針の変更")
    """ 会計基準等の改正に伴う会計方針の変更 """
    changes_in_accounting_estimates_interim:ChangesInAccountingEstimatesInterim_edjp_FinancialReportSummary_consolidated_HY_specific_business = Field(default=None, description="会計上の見積りの変更、中間期")
    """ 会計上の見積りの変更、中間期 """
    changes_other_than_ones_based_on_revisions_of_accounting_standard:ChangesOtherThanOnesBasedOnRevisionsOfAccountingStandard_edjp_FinancialReportSummary_consolidated_HY_specific_business = Field(default=None, description="会計基準等の改正に伴う変更以外の会計方針の変更")
    """ 会計基準等の改正に伴う変更以外の会計方針の変更 """
    company_name:CompanyName_edjp_FinancialReportSummary_consolidated_HY_specific_business = Field(default=None, description="上場会社名")
    """ 上場会社名 """
    convening_briefing_of_results:ConveningBriefingOfResults_edjp_FinancialReportSummary_consolidated_HY_specific_business = Field(default=None, description="決算説明会開催の有無、期中")
    """ 決算説明会開催の有無、期中 """
    correction_of_consolidated_financial_forecast_in_this_quarter:CorrectionOfConsolidatedFinancialForecastInThisQuarter_edjp_FinancialReportSummary_consolidated_HY_specific_business = Field(default=None, description="直近に公表されている業績予想からの修正の有無、連結")
    """ 直近に公表されている業績予想からの修正の有無、連結 """
    correction_of_dividend_forecast_in_this_quarter:CorrectionOfDividendForecastInThisQuarter_edjp_FinancialReportSummary_consolidated_HY_specific_business = Field(default=None, description="直近に公表されている配当予想からの修正の有無")
    """ 直近に公表されている配当予想からの修正の有無 """
    dividend_payable_date_as_planned:DividendPayableDateAsPlanned_edjp_FinancialReportSummary_consolidated_HY_specific_business = Field(default=None, description="配当支払開始予定日")
    """ 配当支払開始予定日 """
    document_name:DocumentName_edjp_FinancialReportSummary_consolidated_HY_specific_business = Field(default=None, description="文書名")
    """ 文書名 """
    fasf_member_mark:FASFMemberMark_edjp_FinancialReportSummary_consolidated_HY_specific_business = Field(default=None, description="財務会計基準機構会員マーク")
    """ 財務会計基準機構会員マーク """
    filing_date:FilingDate_edjp_FinancialReportSummary_consolidated_HY_specific_business = Field(default=None, description="提出日")
    """ 提出日 """
    fiscal_year_end:FiscalYearEnd_edjp_FinancialReportSummary_consolidated_HY_specific_business = Field(default=None, description="決算期")
    """ 決算期 """
    fukuoka_stock_exchange:FukuokaStockExchange_edjp_FinancialReportSummary_consolidated_HY_specific_business = Field(default=None, description="福岡証券取引所")
    """ 福岡証券取引所 """
    fukuoka_stock_exchange_established:FukuokaStockExchangeEstablished_edjp_FinancialReportSummary_consolidated_HY_specific_business = Field(default=None, description="福岡証券取引所 既存市場")
    """ 福岡証券取引所 既存市場 """
    fukuoka_stock_exchange_others:FukuokaStockExchangeOthers_edjp_FinancialReportSummary_consolidated_HY_specific_business = Field(default=None, description="福岡証券取引所 その他")
    """ 福岡証券取引所 その他 """
    fukuoka_stock_exchange_q_board:FukuokaStockExchangeQBoard_edjp_FinancialReportSummary_consolidated_HY_specific_business = Field(default=None, description="福岡証券取引所 Q-Board")
    """ 福岡証券取引所 Q-Board """
    general_business:GeneralBusiness_edjp_FinancialReportSummary_consolidated_HY_specific_business = Field(default=None, description="一般事業会社")
    """ 一般事業会社 """
    japan_securities_dealers_association:JapanSecuritiesDealersAssociation_edjp_FinancialReportSummary_consolidated_HY_specific_business = Field(default=None, description="フェニックス")
    """ フェニックス """
    japan_securities_dealers_association_green_sheet:JapanSecuritiesDealersAssociationGreenSheet_edjp_FinancialReportSummary_consolidated_HY_specific_business = Field(default=None, description="日本証券業協会 フェニックス")
    """ 日本証券業協会 フェニックス """
    nagoya_stock_exchange:NagoyaStockExchange_edjp_FinancialReportSummary_consolidated_HY_specific_business = Field(default=None, description="名古屋証券取引所")
    """ 名古屋証券取引所 """
    nagoya_stock_exchange1st_section:NagoyaStockExchange1stSection_edjp_FinancialReportSummary_consolidated_HY_specific_business = Field(default=None, description="名古屋証券取引所 プレミア")
    """ 名古屋証券取引所 プレミア """
    nagoya_stock_exchange2nd_section:NagoyaStockExchange2ndSection_edjp_FinancialReportSummary_consolidated_HY_specific_business = Field(default=None, description="名古屋証券取引所 メイン")
    """ 名古屋証券取引所 メイン """
    nagoya_stock_exchange_centrex:NagoyaStockExchangeCentrex_edjp_FinancialReportSummary_consolidated_HY_specific_business = Field(default=None, description="名古屋証券取引所 ネクスト")
    """ 名古屋証券取引所 ネクスト """
    nagoya_stock_exchange_others:NagoyaStockExchangeOthers_edjp_FinancialReportSummary_consolidated_HY_specific_business = Field(default=None, description="名古屋証券取引所 その他")
    """ 名古屋証券取引所 その他 """
    name_inquiries:NameInquiries_edjp_FinancialReportSummary_consolidated_HY_specific_business = Field(default=None, description="氏名、問合せ先責任者")
    """ 氏名、問合せ先責任者 """
    name_representative:NameRepresentative_edjp_FinancialReportSummary_consolidated_HY_specific_business = Field(default=None, description="氏名、代表者")
    """ 氏名、代表者 """
    notes_for_using_forecasted_information_and_others:NotesForUsingForecastedInformationAndOthers_edjp_FinancialReportSummary_consolidated_HY_specific_business = Field(default=None, description="業績予想の適切な利用に関する説明、その他特記事項")
    """ 業績予想の適切な利用に関する説明、その他特記事項 """
    note_to_changes_in_accounting_policies_accounting_estimates_and_retrospective_restatement_interim_consolidated:NoteToChangesInAccountingPoliciesAccountingEstimatesAndRetrospectiveRestatementInterimConsolidated_edjp_FinancialReportSummary_consolidated_HY_specific_business = Field(default=None, description="会計方針の変更・会計上の見積りの変更・修正再表示に関する注記、中間期")
    """ 会計方針の変更・会計上の見積りの変更・修正再表示に関する注記、中間期 """
    note_to_consolidated_financial_results:NoteToConsolidatedFinancialResults_edjp_FinancialReportSummary_consolidated_HY_specific_business = Field(default=None, description="連結業績に関する注記")
    """ 連結業績に関する注記 """
    note_to_dividends:NoteToDividends_edjp_FinancialReportSummary_consolidated_HY_specific_business = Field(default=None, description="配当の状況に関する注記")
    """ 配当の状況に関する注記 """
    note_to_financial_positions:NoteToFinancialPositions_edjp_FinancialReportSummary_consolidated_HY_specific_business = Field(default=None, description="財政状態に関する注記")
    """ 財政状態に関する注記 """
    note_to_financial_results:NoteToFinancialResults_edjp_FinancialReportSummary_consolidated_HY_specific_business = Field(default=None, description="業績に関する注記")
    """ 業績に関する注記 """
    note_to_forecasts:NoteToForecasts_edjp_FinancialReportSummary_consolidated_HY_specific_business = Field(default=None, description="業績予想に関する事項、注記")
    """ 業績予想に関する事項、注記 """
    note_to_fraction_processing_method:NoteToFractionProcessingMethod_edjp_FinancialReportSummary_consolidated_HY_specific_business = Field(default=None, description="端数処理方法に関する注記")
    """ 端数処理方法に関する注記 """
    note_to_number_of_issued_and_outstanding_shares_common_stock:NoteToNumberOfIssuedAndOutstandingSharesCommonStock_edjp_FinancialReportSummary_consolidated_HY_specific_business = Field(default=None, description="発行済株式数（普通株式）に関する注記")
    """ 発行済株式数（普通株式）に関する注記 """
    note_to_operating_results:NoteToOperatingResults_edjp_FinancialReportSummary_consolidated_HY_specific_business = Field(default=None, description="経営成績に関する注記")
    """ 経営成績に関する注記 """
    note_to_significant_changes_in_the_scope_of_consolidation_during_the_period:NoteToSignificantChangesInTheScopeOfConsolidationDuringThePeriod_edjp_FinancialReportSummary_consolidated_HY_specific_business = Field(default=None, description="期中における連結範囲の重要な変更に関する注記")
    """ 期中における連結範囲の重要な変更に関する注記 """
    preamble_to_forecasts:PreambleToForecasts_edjp_FinancialReportSummary_consolidated_HY_specific_business = Field(default=None, description="業績予想に関する事項")
    """ 業績予想に関する事項 """
    retrospective_restatement_interim:RetrospectiveRestatementInterim_edjp_FinancialReportSummary_consolidated_HY_specific_business = Field(default=None, description="修正再表示、中間期")
    """ 修正再表示、中間期 """
    sapporo_stock_exchange:SapporoStockExchange_edjp_FinancialReportSummary_consolidated_HY_specific_business = Field(default=None, description="札幌証券取引所")
    """ 札幌証券取引所 """
    sapporo_stock_exchange_ambitious:SapporoStockExchangeAmbitious_edjp_FinancialReportSummary_consolidated_HY_specific_business = Field(default=None, description="札幌証券取引所 アンビシャス")
    """ 札幌証券取引所 アンビシャス """
    sapporo_stock_exchange_established:SapporoStockExchangeEstablished_edjp_FinancialReportSummary_consolidated_HY_specific_business = Field(default=None, description="札幌証券取引所 既存市場")
    """ 札幌証券取引所 既存市場 """
    sapporo_stock_exchange_others:SapporoStockExchangeOthers_edjp_FinancialReportSummary_consolidated_HY_specific_business = Field(default=None, description="札幌証券取引所 その他")
    """ 札幌証券取引所 その他 """
    securities_code:SecuritiesCode_edjp_FinancialReportSummary_consolidated_HY_specific_business = Field(default=None, description="コード番号")
    """ コード番号 """
    semi_annual_statement_filing_date_as_planned:SemiAnnualStatementFilingDateAsPlanned_edjp_FinancialReportSummary_consolidated_HY_specific_business = Field(default=None, description="半期報告書提出予定日")
    """ 半期報告書提出予定日 """
    setting_of_specific_transaction_account_bk:SettingOfSpecificTransactionAccountBK_edjp_FinancialReportSummary_consolidated_HY_specific_business = Field(default=None, description="特定取引勘定設置の有無、銀行")
    """ 特定取引勘定設置の有無、銀行 """
    significant_changes_in_the_scope_of_consolidation_during_the_period:SignificantChangesInTheScopeOfConsolidationDuringThePeriod_edjp_FinancialReportSummary_consolidated_HY_specific_business = Field(default=None, description="期中における連結範囲の重要な変更")
    """ 期中における連結範囲の重要な変更 """
    specific_business:SpecificBusiness_edjp_FinancialReportSummary_consolidated_HY_specific_business = Field(default=None, description="特定事業会社")
    """ 特定事業会社 """
    supplemental_material_of_results:SupplementalMaterialOfResults_edjp_FinancialReportSummary_consolidated_HY_specific_business = Field(default=None, description="決算補足説明資料作成の有無、期中")
    """ 決算補足説明資料作成の有無、期中 """
    target_for_briefing_of_results:TargetForBriefingOfResults_edjp_FinancialReportSummary_consolidated_HY_specific_business = Field(default=None, description="決算説明会の対象者")
    """ 決算説明会の対象者 """
    tel:Tel_edjp_FinancialReportSummary_consolidated_HY_specific_business = Field(default=None, description="TEL")
    """ TEL """
    title_for_forecasts:TitleForForecasts_edjp_FinancialReportSummary_consolidated_HY_specific_business = Field(default=None, description="業績予想タイトル名称")
    """ 業績予想タイトル名称 """
    title_inquiries:TitleInquiries_edjp_FinancialReportSummary_consolidated_HY_specific_business = Field(default=None, description="役職名、問合せ先責任者")
    """ 役職名、問合せ先責任者 """
    title_representative:TitleRepresentative_edjp_FinancialReportSummary_consolidated_HY_specific_business = Field(default=None, description="役職名、代表者")
    """ 役職名、代表者 """
    tokyo_stock_exchange:TokyoStockExchange_edjp_FinancialReportSummary_consolidated_HY_specific_business = Field(default=None, description="東京証券取引所")
    """ 東京証券取引所 """
    tokyo_stock_exchange_growth:TokyoStockExchangeGrowth_edjp_FinancialReportSummary_consolidated_HY_specific_business = Field(default=None, description="東京証券取引所 グロース")
    """ 東京証券取引所 グロース """
    tokyo_stock_exchange_others:TokyoStockExchangeOthers_edjp_FinancialReportSummary_consolidated_HY_specific_business = Field(default=None, description="東京証券取引所 その他")
    """ 東京証券取引所 その他 """
    tokyo_stock_exchange_prime:TokyoStockExchangePrime_edjp_FinancialReportSummary_consolidated_HY_specific_business = Field(default=None, description="東京証券取引所 プライム")
    """ 東京証券取引所 プライム """
    tokyo_stock_exchange_pro_market:TokyoStockExchangePROMarket_edjp_FinancialReportSummary_consolidated_HY_specific_business = Field(default=None, description="東京証券取引所 PRO Market")
    """ 東京証券取引所 PRO Market """
    tokyo_stock_exchange_standard:TokyoStockExchangeStandard_edjp_FinancialReportSummary_consolidated_HY_specific_business = Field(default=None, description="東京証券取引所 スタンダード")
    """ 東京証券取引所 スタンダード """
    URL:URL_edjp_FinancialReportSummary_consolidated_HY_specific_business = Field(default=None, description="URL")
    """ URL """
    way_of_getting_supplemental_material_of_results:WayOfGettingSupplementalMaterialOfResults_edjp_FinancialReportSummary_consolidated_HY_specific_business = Field(default=None, description="入手方法等、決算補足説明資料、期中")
    """ 入手方法等、決算補足説明資料、期中 """


class edjp_NotesSegmentInformationEtcSemiAnnualConsolidatedFinancialStatements_consolidated_HY_specific_business(IxbrlBase):
    description_of_reportable_segments_text_block:DescriptionOfReportableSegmentsTextBlock_edjp_NotesSegmentInformationEtcSemiAnnualConsolidatedFinancialStatements_consolidated_HY_specific_business = Field(default=None, description="報告セグメントの概要 [テキストブロック]")
    """ 報告セグメントの概要 [テキストブロック] """
    explanation_of_measurements_of_sales_profit_loss_asset_liability_and_other_items_for_each_reportable_segment_text_block:ExplanationOfMeasurementsOfSalesProfitLossAssetLiabilityAndOtherItemsForEachReportableSegmentTextBlock_edjp_NotesSegmentInformationEtcSemiAnnualConsolidatedFinancialStatements_consolidated_HY_specific_business = Field(default=None, description="報告セグメントごとの売上高、利益又は損失、資産、負債その他の項目の金額の算定方法 [テキストブロック]")
    """ 報告セグメントごとの売上高、利益又は損失、資産、負債その他の項目の金額の算定方法 [テキストブロック] """
    footnotes_regarding_segment_information_table_text_block:FootnotesRegardingSegmentInformationTableTextBlock_edjp_NotesSegmentInformationEtcSemiAnnualConsolidatedFinancialStatements_consolidated_HY_specific_business = Field(default=None, description="セグメント表の脚注 [テキストブロック]")
    """ セグメント表の脚注 [テキストブロック] """
    information_for_each_of_main_customers_text_block:InformationForEachOfMainCustomersTextBlock_edjp_NotesSegmentInformationEtcSemiAnnualConsolidatedFinancialStatements_consolidated_HY_specific_business = Field(default=None, description="主要な顧客ごとの情報 [テキストブロック]")
    """ 主要な顧客ごとの情報 [テキストブロック] """
    information_for_each_product_or_service_text_block:InformationForEachProductOrServiceTextBlock_edjp_NotesSegmentInformationEtcSemiAnnualConsolidatedFinancialStatements_consolidated_HY_specific_business = Field(default=None, description="製品及びサービスごとの情報 [テキストブロック]")
    """ 製品及びサービスごとの情報 [テキストブロック] """
    notes_segment_information_etc_semi_annual_consolidated_financial_statements_text_block:NotesSegmentInformationEtcSemiAnnualConsolidatedFinancialStatementsTextBlock_edjp_NotesSegmentInformationEtcSemiAnnualConsolidatedFinancialStatements_consolidated_HY_specific_business = Field(default=None, description="セグメント情報等、中間連結財務諸表 [テキストブロック]")
    """ セグメント情報等、中間連結財務諸表 [テキストブロック] """
    property_plant_and_equipment_information_for_each_region_text_block:PropertyPlantAndEquipmentInformationForEachRegionTextBlock_edjp_NotesSegmentInformationEtcSemiAnnualConsolidatedFinancialStatements_consolidated_HY_specific_business = Field(default=None, description="有形固定資産、地域ごとの情報 [テキストブロック]")
    """ 有形固定資産、地域ごとの情報 [テキストブロック] """
    revenues_from_external_customers_information_for_each_region_text_block:RevenuesFromExternalCustomersInformationForEachRegionTextBlock_edjp_NotesSegmentInformationEtcSemiAnnualConsolidatedFinancialStatements_consolidated_HY_specific_business = Field(default=None, description="売上高、地域ごとの情報 [テキストブロック]")
    """ 売上高、地域ごとの情報 [テキストブロック] """


class edjp_SemiAnnualBalanceSheet_consolidated_HY_specific_business(IxbrlBase):
    semi_annual_balance_sheet_text_block:SemiAnnualBalanceSheetTextBlock_edjp_SemiAnnualBalanceSheet_consolidated_HY_specific_business = Field(default=None, description="中間貸借対照表 [テキストブロック]")
    """ 中間貸借対照表 [テキストブロック] """


class edjp_SemiAnnualConsolidatedBalanceSheet_consolidated_HY_specific_business(IxbrlBase):
    semi_annual_consolidated_balance_sheet_text_block:SemiAnnualConsolidatedBalanceSheetTextBlock_edjp_SemiAnnualConsolidatedBalanceSheet_consolidated_HY_specific_business = Field(default=None, description="中間連結貸借対照表 [テキストブロック]")
    """ 中間連結貸借対照表 [テキストブロック] """
    accounting_standards_dei:AccountingStandardsDEI_edjp_SemiAnnualConsolidatedBalanceSheet_consolidated_HY_specific_business = Field(default=None, description="会計基準、DEI")
    """ 会計基準、DEI """
    amendment_flag_dei:AmendmentFlagDEI_edjp_SemiAnnualConsolidatedBalanceSheet_consolidated_HY_specific_business = Field(default=None, description="訂正の有無、DEI")
    """ 訂正の有無、DEI """
    cabinet_office_ordinance_dei:CabinetOfficeOrdinanceDEI_edjp_SemiAnnualConsolidatedBalanceSheet_consolidated_HY_specific_business = Field(default=None, description="府令、DEI")
    """ 府令、DEI """
    comparative_period_end_date_dei:ComparativePeriodEndDateDEI_edjp_SemiAnnualConsolidatedBalanceSheet_consolidated_HY_specific_business = Field(default=None, description="比較対象会計期間終了日、DEI")
    """ 比較対象会計期間終了日、DEI """
    current_fiscal_year_end_date_dei:CurrentFiscalYearEndDateDEI_edjp_SemiAnnualConsolidatedBalanceSheet_consolidated_HY_specific_business = Field(default=None, description="当事業年度終了日、DEI")
    """ 当事業年度終了日、DEI """
    current_fiscal_year_start_date_dei:CurrentFiscalYearStartDateDEI_edjp_SemiAnnualConsolidatedBalanceSheet_consolidated_HY_specific_business = Field(default=None, description="当事業年度開始日、DEI")
    """ 当事業年度開始日、DEI """
    current_period_end_date_dei:CurrentPeriodEndDateDEI_edjp_SemiAnnualConsolidatedBalanceSheet_consolidated_HY_specific_business = Field(default=None, description="当会計期間終了日、DEI")
    """ 当会計期間終了日、DEI """
    document_type_dei:DocumentTypeDEI_edjp_SemiAnnualConsolidatedBalanceSheet_consolidated_HY_specific_business = Field(default=None, description="様式、DEI")
    """ 様式、DEI """
    edinet_code_dei:EDINETCodeDEI_edjp_SemiAnnualConsolidatedBalanceSheet_consolidated_HY_specific_business = Field(default=None, description="EDINETコード、DEI")
    """ EDINETコード、DEI """
    end_date_of_quarterly_or_semi_annual_period_of_next_fiscal_year_dei:EndDateOfQuarterlyOrSemiAnnualPeriodOfNextFiscalYearDEI_edjp_SemiAnnualConsolidatedBalanceSheet_consolidated_HY_specific_business = Field(default=None, description="次の四半期又は中間期の会計期間終了日、DEI")
    """ 次の四半期又は中間期の会計期間終了日、DEI """
    filer_name_in_english_dei:FilerNameInEnglishDEI_edjp_SemiAnnualConsolidatedBalanceSheet_consolidated_HY_specific_business = Field(default=None, description="提出者名（英語表記）、DEI")
    """ 提出者名（英語表記）、DEI """
    filer_name_in_japanese_dei:FilerNameInJapaneseDEI_edjp_SemiAnnualConsolidatedBalanceSheet_consolidated_HY_specific_business = Field(default=None, description="提出者名（日本語表記）、DEI")
    """ 提出者名（日本語表記）、DEI """
    fund_code_dei:FundCodeDEI_edjp_SemiAnnualConsolidatedBalanceSheet_consolidated_HY_specific_business = Field(default=None, description="ファンドコード、DEI")
    """ ファンドコード、DEI """
    fund_name_in_english_dei:FundNameInEnglishDEI_edjp_SemiAnnualConsolidatedBalanceSheet_consolidated_HY_specific_business = Field(default=None, description="ファンド名称（英語表記）、DEI")
    """ ファンド名称（英語表記）、DEI """
    fund_name_in_japanese_dei:FundNameInJapaneseDEI_edjp_SemiAnnualConsolidatedBalanceSheet_consolidated_HY_specific_business = Field(default=None, description="ファンド名称（日本語表記）、DEI")
    """ ファンド名称（日本語表記）、DEI """
    identification_of_document_subject_to_amendment_dei:IdentificationOfDocumentSubjectToAmendmentDEI_edjp_SemiAnnualConsolidatedBalanceSheet_consolidated_HY_specific_business = Field(default=None, description="訂正対象書類の書類管理番号、DEI")
    """ 訂正対象書類の書類管理番号、DEI """
    industry_code_when_consolidated_financial_statements_are_prepared_in_accordance_with_industry_specific_regulations_dei:IndustryCodeWhenConsolidatedFinancialStatementsArePreparedInAccordanceWithIndustrySpecificRegulationsDEI_edjp_SemiAnnualConsolidatedBalanceSheet_consolidated_HY_specific_business = Field(default=None, description="別記事業（連結）、DEI")
    """ 別記事業（連結）、DEI """
    industry_code_when_financial_statements_are_prepared_in_accordance_with_industry_specific_regulations_dei:IndustryCodeWhenFinancialStatementsArePreparedInAccordanceWithIndustrySpecificRegulationsDEI_edjp_SemiAnnualConsolidatedBalanceSheet_consolidated_HY_specific_business = Field(default=None, description="別記事業（個別）、DEI")
    """ 別記事業（個別）、DEI """
    next_fiscal_year_start_date_dei:NextFiscalYearStartDateDEI_edjp_SemiAnnualConsolidatedBalanceSheet_consolidated_HY_specific_business = Field(default=None, description="次の事業年度開始日、DEI")
    """ 次の事業年度開始日、DEI """
    previous_fiscal_year_end_date_dei:PreviousFiscalYearEndDateDEI_edjp_SemiAnnualConsolidatedBalanceSheet_consolidated_HY_specific_business = Field(default=None, description="前事業年度終了日、DEI")
    """ 前事業年度終了日、DEI """
    previous_fiscal_year_start_date_dei:PreviousFiscalYearStartDateDEI_edjp_SemiAnnualConsolidatedBalanceSheet_consolidated_HY_specific_business = Field(default=None, description="前事業年度開始日、DEI")
    """ 前事業年度開始日、DEI """
    report_amendment_flag_dei:ReportAmendmentFlagDEI_edjp_SemiAnnualConsolidatedBalanceSheet_consolidated_HY_specific_business = Field(default=None, description="記載事項訂正のフラグ、DEI")
    """ 記載事項訂正のフラグ、DEI """
    security_code_dei:SecurityCodeDEI_edjp_SemiAnnualConsolidatedBalanceSheet_consolidated_HY_specific_business = Field(default=None, description="証券コード、DEI")
    """ 証券コード、DEI """
    type_of_current_period_dei:TypeOfCurrentPeriodDEI_edjp_SemiAnnualConsolidatedBalanceSheet_consolidated_HY_specific_business = Field(default=None, description="当会計期間の種類、DEI")
    """ 当会計期間の種類、DEI """
    whether_consolidated_financial_statements_are_prepared_dei:WhetherConsolidatedFinancialStatementsArePreparedDEI_edjp_SemiAnnualConsolidatedBalanceSheet_consolidated_HY_specific_business = Field(default=None, description="連結決算の有無、DEI")
    """ 連結決算の有無、DEI """
    xbrl_amendment_flag_dei:XBRLAmendmentFlagDEI_edjp_SemiAnnualConsolidatedBalanceSheet_consolidated_HY_specific_business = Field(default=None, description="XBRL訂正のフラグ、DEI")
    """ XBRL訂正のフラグ、DEI """


class edjp_SemiAnnualConsolidatedStatementOfChangesInEquity_consolidated_HY_specific_business(IxbrlBase):
    semi_annual_consolidated_statement_of_changes_in_equity_text_block:SemiAnnualConsolidatedStatementOfChangesInEquityTextBlock_edjp_SemiAnnualConsolidatedStatementOfChangesInEquity_consolidated_HY_specific_business = Field(default=None, description="中間連結株主資本等変動計算書 [テキストブロック]")
    """ 中間連結株主資本等変動計算書 [テキストブロック] """


class edjp_SemiAnnualConsolidatedStatementOfComprehensiveIncome_consolidated_HY_specific_business(IxbrlBase):
    semi_annual_consolidated_statement_of_comprehensive_income_text_block:SemiAnnualConsolidatedStatementOfComprehensiveIncomeTextBlock_edjp_SemiAnnualConsolidatedStatementOfComprehensiveIncome_consolidated_HY_specific_business = Field(default=None, description="中間連結包括利益計算書 [テキストブロック]")
    """ 中間連結包括利益計算書 [テキストブロック] """


class edjp_SemiAnnualConsolidatedStatementOfIncome_consolidated_HY_specific_business(IxbrlBase):
    semi_annual_consolidated_statement_of_income_text_block:SemiAnnualConsolidatedStatementOfIncomeTextBlock_edjp_SemiAnnualConsolidatedStatementOfIncome_consolidated_HY_specific_business = Field(default=None, description="中間連結損益計算書 [テキストブロック]")
    """ 中間連結損益計算書 [テキストブロック] """


class edjp_SemiAnnualStatementOfChangesInEquity_consolidated_HY_specific_business(IxbrlBase):
    semi_annual_statement_of_changes_in_equity_text_block:SemiAnnualStatementOfChangesInEquityTextBlock_edjp_SemiAnnualStatementOfChangesInEquity_consolidated_HY_specific_business = Field(default=None, description="中間株主資本等変動計算書 [テキストブロック]")
    """ 中間株主資本等変動計算書 [テキストブロック] """


class edjp_SemiAnnualStatementOfIncome_consolidated_HY_specific_business(IxbrlBase):
    semi_annual_statement_of_income_text_block:SemiAnnualStatementOfIncomeTextBlock_edjp_SemiAnnualStatementOfIncome_consolidated_HY_specific_business = Field(default=None, description="中間損益計算書 [テキストブロック]")
    """ 中間損益計算書 [テキストブロック] """


class rvfc_FinancialReportSummary(IxbrlBase):
    company_name:CompanyName_rvfc_FinancialReportSummary = Field(default=None, description="上場会社名")
    """ 上場会社名 """
    document_name:DocumentName_rvfc_FinancialReportSummary = Field(default=None, description="文書名")
    """ 文書名 """
    fasf_member_mark:FASFMemberMark_rvfc_FinancialReportSummary = Field(default=None, description="財務会計基準機構会員マーク")
    """ 財務会計基準機構会員マーク """
    fiscal_year_end:FiscalYearEnd_rvfc_FinancialReportSummary = Field(default=None, description="決算期")
    """ 決算期 """
    fukuoka_stock_exchange:FukuokaStockExchange_rvfc_FinancialReportSummary = Field(default=None, description="福岡証券取引所")
    """ 福岡証券取引所 """
    fukuoka_stock_exchange_established:FukuokaStockExchangeEstablished_rvfc_FinancialReportSummary = Field(default=None, description="福岡証券取引所 既存市場")
    """ 福岡証券取引所 既存市場 """
    fukuoka_stock_exchange_others:FukuokaStockExchangeOthers_rvfc_FinancialReportSummary = Field(default=None, description="福岡証券取引所 その他")
    """ 福岡証券取引所 その他 """
    fukuoka_stock_exchange_q_board:FukuokaStockExchangeQBoard_rvfc_FinancialReportSummary = Field(default=None, description="福岡証券取引所 Q-Board")
    """ 福岡証券取引所 Q-Board """
    general_business:GeneralBusiness_rvfc_FinancialReportSummary = Field(default=None, description="一般事業会社")
    """ 一般事業会社 """
    japan_securities_dealers_association:JapanSecuritiesDealersAssociation_rvfc_FinancialReportSummary = Field(default=None, description="フェニックス")
    """ フェニックス """
    japan_securities_dealers_association_green_sheet:JapanSecuritiesDealersAssociationGreenSheet_rvfc_FinancialReportSummary = Field(default=None, description="日本証券業協会 フェニックス")
    """ 日本証券業協会 フェニックス """
    nagoya_stock_exchange:NagoyaStockExchange_rvfc_FinancialReportSummary = Field(default=None, description="名古屋証券取引所")
    """ 名古屋証券取引所 """
    nagoya_stock_exchange1st_section:NagoyaStockExchange1stSection_rvfc_FinancialReportSummary = Field(default=None, description="名古屋証券取引所 プレミア")
    """ 名古屋証券取引所 プレミア """
    nagoya_stock_exchange2nd_section:NagoyaStockExchange2ndSection_rvfc_FinancialReportSummary = Field(default=None, description="名古屋証券取引所 メイン")
    """ 名古屋証券取引所 メイン """
    nagoya_stock_exchange_centrex:NagoyaStockExchangeCentrex_rvfc_FinancialReportSummary = Field(default=None, description="名古屋証券取引所 ネクスト")
    """ 名古屋証券取引所 ネクスト """
    nagoya_stock_exchange_others:NagoyaStockExchangeOthers_rvfc_FinancialReportSummary = Field(default=None, description="名古屋証券取引所 その他")
    """ 名古屋証券取引所 その他 """
    name_inquiries:NameInquiries_rvfc_FinancialReportSummary = Field(default=None, description="氏名、問合せ先責任者")
    """ 氏名、問合せ先責任者 """
    name_representative:NameRepresentative_rvfc_FinancialReportSummary = Field(default=None, description="氏名、代表者")
    """ 氏名、代表者 """
    note_to_dividends:NoteToDividends_rvfc_FinancialReportSummary = Field(default=None, description="配当の状況に関する注記")
    """ 配当の状況に関する注記 """
    note_to_financial_forecast:NoteToFinancialForecast_rvfc_FinancialReportSummary = Field(default=None, description="業績予想の状況に関する注記")
    """ 業績予想の状況に関する注記 """
    notice_of_forecast_correction:NoticeOfForecastCorrection_rvfc_FinancialReportSummary = Field(default=None, description="予想修正に関するお知らせ")
    """ 予想修正に関するお知らせ """
    preamble_to_forecasts:PreambleToForecasts_rvfc_FinancialReportSummary = Field(default=None, description="業績予想に関する事項")
    """ 業績予想に関する事項 """
    previous_reporting_date_of_dividend_forecast:PreviousReportingDateOfDividendForecast_rvfc_FinancialReportSummary = Field(default=None, description="前回予想発表日、配当予想の修正について")
    """ 前回予想発表日、配当予想の修正について """
    reason_for_dividend_forecast_correction:ReasonForDividendForecastCorrection_rvfc_FinancialReportSummary = Field(default=None, description="配当予想修正の理由")
    """ 配当予想修正の理由 """
    reason_for_forecast_correction:ReasonForForecastCorrection_rvfc_FinancialReportSummary = Field(default=None, description="業績予想修正の理由")
    """ 業績予想修正の理由 """
    reporting_date_of_financial_forecast_correction:ReportingDateOfFinancialForecastCorrection_rvfc_FinancialReportSummary = Field(default=None, description="予想修正報告日")
    """ 予想修正報告日 """
    sapporo_stock_exchange:SapporoStockExchange_rvfc_FinancialReportSummary = Field(default=None, description="札幌証券取引所")
    """ 札幌証券取引所 """
    sapporo_stock_exchange_ambitious:SapporoStockExchangeAmbitious_rvfc_FinancialReportSummary = Field(default=None, description="札幌証券取引所 アンビシャス")
    """ 札幌証券取引所 アンビシャス """
    sapporo_stock_exchange_established:SapporoStockExchangeEstablished_rvfc_FinancialReportSummary = Field(default=None, description="札幌証券取引所 既存市場")
    """ 札幌証券取引所 既存市場 """
    sapporo_stock_exchange_others:SapporoStockExchangeOthers_rvfc_FinancialReportSummary = Field(default=None, description="札幌証券取引所 その他")
    """ 札幌証券取引所 その他 """
    securities_code:SecuritiesCode_rvfc_FinancialReportSummary = Field(default=None, description="コード番号")
    """ コード番号 """
    specific_business:SpecificBusiness_rvfc_FinancialReportSummary = Field(default=None, description="特定事業会社")
    """ 特定事業会社 """
    tel:Tel_rvfc_FinancialReportSummary = Field(default=None, description="TEL")
    """ TEL """
    title_inquiries:TitleInquiries_rvfc_FinancialReportSummary = Field(default=None, description="役職名、問合せ先責任者")
    """ 役職名、問合せ先責任者 """
    title_representative:TitleRepresentative_rvfc_FinancialReportSummary = Field(default=None, description="役職名、代表者")
    """ 役職名、代表者 """
    tokyo_stock_exchange:TokyoStockExchange_rvfc_FinancialReportSummary = Field(default=None, description="東京証券取引所")
    """ 東京証券取引所 """
    tokyo_stock_exchange_growth:TokyoStockExchangeGrowth_rvfc_FinancialReportSummary = Field(default=None, description="東京証券取引所 グロース")
    """ 東京証券取引所 グロース """
    tokyo_stock_exchange_others:TokyoStockExchangeOthers_rvfc_FinancialReportSummary = Field(default=None, description="東京証券取引所 その他")
    """ 東京証券取引所 その他 """
    tokyo_stock_exchange_prime:TokyoStockExchangePrime_rvfc_FinancialReportSummary = Field(default=None, description="東京証券取引所 プライム")
    """ 東京証券取引所 プライム """
    tokyo_stock_exchange_pro_market:TokyoStockExchangePROMarket_rvfc_FinancialReportSummary = Field(default=None, description="東京証券取引所 PRO Market")
    """ 東京証券取引所 PRO Market """
    tokyo_stock_exchange_standard:TokyoStockExchangeStandard_rvfc_FinancialReportSummary = Field(default=None, description="東京証券取引所 スタンダード")
    """ 東京証券取引所 スタンダード """


class rvfc_FinancialReportSummary_specific_business(IxbrlBase):
    company_name:CompanyName_rvfc_FinancialReportSummary_specific_business = Field(default=None, description="上場会社名")
    """ 上場会社名 """
    document_name:DocumentName_rvfc_FinancialReportSummary_specific_business = Field(default=None, description="文書名")
    """ 文書名 """
    fasf_member_mark:FASFMemberMark_rvfc_FinancialReportSummary_specific_business = Field(default=None, description="財務会計基準機構会員マーク")
    """ 財務会計基準機構会員マーク """
    fiscal_year_end:FiscalYearEnd_rvfc_FinancialReportSummary_specific_business = Field(default=None, description="決算期")
    """ 決算期 """
    fukuoka_stock_exchange:FukuokaStockExchange_rvfc_FinancialReportSummary_specific_business = Field(default=None, description="福岡証券取引所")
    """ 福岡証券取引所 """
    fukuoka_stock_exchange_established:FukuokaStockExchangeEstablished_rvfc_FinancialReportSummary_specific_business = Field(default=None, description="福岡証券取引所 既存市場")
    """ 福岡証券取引所 既存市場 """
    fukuoka_stock_exchange_others:FukuokaStockExchangeOthers_rvfc_FinancialReportSummary_specific_business = Field(default=None, description="福岡証券取引所 その他")
    """ 福岡証券取引所 その他 """
    fukuoka_stock_exchange_q_board:FukuokaStockExchangeQBoard_rvfc_FinancialReportSummary_specific_business = Field(default=None, description="福岡証券取引所 Q-Board")
    """ 福岡証券取引所 Q-Board """
    general_business:GeneralBusiness_rvfc_FinancialReportSummary_specific_business = Field(default=None, description="一般事業会社")
    """ 一般事業会社 """
    japan_securities_dealers_association:JapanSecuritiesDealersAssociation_rvfc_FinancialReportSummary_specific_business = Field(default=None, description="フェニックス")
    """ フェニックス """
    japan_securities_dealers_association_green_sheet:JapanSecuritiesDealersAssociationGreenSheet_rvfc_FinancialReportSummary_specific_business = Field(default=None, description="日本証券業協会 フェニックス")
    """ 日本証券業協会 フェニックス """
    nagoya_stock_exchange:NagoyaStockExchange_rvfc_FinancialReportSummary_specific_business = Field(default=None, description="名古屋証券取引所")
    """ 名古屋証券取引所 """
    nagoya_stock_exchange1st_section:NagoyaStockExchange1stSection_rvfc_FinancialReportSummary_specific_business = Field(default=None, description="名古屋証券取引所 プレミア")
    """ 名古屋証券取引所 プレミア """
    nagoya_stock_exchange2nd_section:NagoyaStockExchange2ndSection_rvfc_FinancialReportSummary_specific_business = Field(default=None, description="名古屋証券取引所 メイン")
    """ 名古屋証券取引所 メイン """
    nagoya_stock_exchange_centrex:NagoyaStockExchangeCentrex_rvfc_FinancialReportSummary_specific_business = Field(default=None, description="名古屋証券取引所 ネクスト")
    """ 名古屋証券取引所 ネクスト """
    nagoya_stock_exchange_others:NagoyaStockExchangeOthers_rvfc_FinancialReportSummary_specific_business = Field(default=None, description="名古屋証券取引所 その他")
    """ 名古屋証券取引所 その他 """
    name_inquiries:NameInquiries_rvfc_FinancialReportSummary_specific_business = Field(default=None, description="氏名、問合せ先責任者")
    """ 氏名、問合せ先責任者 """
    name_representative:NameRepresentative_rvfc_FinancialReportSummary_specific_business = Field(default=None, description="氏名、代表者")
    """ 氏名、代表者 """
    note_to_financial_forecast:NoteToFinancialForecast_rvfc_FinancialReportSummary_specific_business = Field(default=None, description="業績予想の状況に関する注記")
    """ 業績予想の状況に関する注記 """
    notice_of_forecast_correction:NoticeOfForecastCorrection_rvfc_FinancialReportSummary_specific_business = Field(default=None, description="予想修正に関するお知らせ")
    """ 予想修正に関するお知らせ """
    preamble_to_forecasts:PreambleToForecasts_rvfc_FinancialReportSummary_specific_business = Field(default=None, description="業績予想に関する事項")
    """ 業績予想に関する事項 """
    reason_for_forecast_correction:ReasonForForecastCorrection_rvfc_FinancialReportSummary_specific_business = Field(default=None, description="業績予想修正の理由")
    """ 業績予想修正の理由 """
    reporting_date_of_financial_forecast_correction:ReportingDateOfFinancialForecastCorrection_rvfc_FinancialReportSummary_specific_business = Field(default=None, description="予想修正報告日")
    """ 予想修正報告日 """
    sapporo_stock_exchange:SapporoStockExchange_rvfc_FinancialReportSummary_specific_business = Field(default=None, description="札幌証券取引所")
    """ 札幌証券取引所 """
    sapporo_stock_exchange_ambitious:SapporoStockExchangeAmbitious_rvfc_FinancialReportSummary_specific_business = Field(default=None, description="札幌証券取引所 アンビシャス")
    """ 札幌証券取引所 アンビシャス """
    sapporo_stock_exchange_established:SapporoStockExchangeEstablished_rvfc_FinancialReportSummary_specific_business = Field(default=None, description="札幌証券取引所 既存市場")
    """ 札幌証券取引所 既存市場 """
    sapporo_stock_exchange_others:SapporoStockExchangeOthers_rvfc_FinancialReportSummary_specific_business = Field(default=None, description="札幌証券取引所 その他")
    """ 札幌証券取引所 その他 """
    securities_code:SecuritiesCode_rvfc_FinancialReportSummary_specific_business = Field(default=None, description="コード番号")
    """ コード番号 """
    specific_business:SpecificBusiness_rvfc_FinancialReportSummary_specific_business = Field(default=None, description="特定事業会社")
    """ 特定事業会社 """
    tel:Tel_rvfc_FinancialReportSummary_specific_business = Field(default=None, description="TEL")
    """ TEL """
    title_inquiries:TitleInquiries_rvfc_FinancialReportSummary_specific_business = Field(default=None, description="役職名、問合せ先責任者")
    """ 役職名、問合せ先責任者 """
    title_representative:TitleRepresentative_rvfc_FinancialReportSummary_specific_business = Field(default=None, description="役職名、代表者")
    """ 役職名、代表者 """
    tokyo_stock_exchange:TokyoStockExchange_rvfc_FinancialReportSummary_specific_business = Field(default=None, description="東京証券取引所")
    """ 東京証券取引所 """
    tokyo_stock_exchange_growth:TokyoStockExchangeGrowth_rvfc_FinancialReportSummary_specific_business = Field(default=None, description="東京証券取引所 グロース")
    """ 東京証券取引所 グロース """
    tokyo_stock_exchange_others:TokyoStockExchangeOthers_rvfc_FinancialReportSummary_specific_business = Field(default=None, description="東京証券取引所 その他")
    """ 東京証券取引所 その他 """
    tokyo_stock_exchange_prime:TokyoStockExchangePrime_rvfc_FinancialReportSummary_specific_business = Field(default=None, description="東京証券取引所 プライム")
    """ 東京証券取引所 プライム """
    tokyo_stock_exchange_pro_market:TokyoStockExchangePROMarket_rvfc_FinancialReportSummary_specific_business = Field(default=None, description="東京証券取引所 PRO Market")
    """ 東京証券取引所 PRO Market """
    tokyo_stock_exchange_standard:TokyoStockExchangeStandard_rvfc_FinancialReportSummary_specific_business = Field(default=None, description="東京証券取引所 スタンダード")
    """ 東京証券取引所 スタンダード """


