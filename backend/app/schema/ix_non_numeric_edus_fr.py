from app.models import Field, SQLModel
from app.schema.ix_non_numeric import IxNonNumericPublic
from typing import Optional

class IxNonNumericEdusFr(SQLModel):
    quarterly_consolidated_balance_sheet_usgaap_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='四半期連結貸借対照表（US GAAP） [テキストブロック]')
    """ 四半期連結貸借対照表（US GAAP） [テキストブロック] """
    year_to_quarter_end_consolidated_statement_of_comprehensive_income_usgaap_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='四半期連結累計期間、四半期連結包括利益計算書（US GAAP） [テキストブロック]')
    """ 四半期連結累計期間、四半期連結包括利益計算書（US GAAP） [テキストブロック] """
    year_to_quarter_end_consolidated_statement_of_income_usgaap_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='四半期連結累計期間、四半期連結損益計算書（US GAAP） [テキストブロック]')
    """ 四半期連結累計期間、四半期連結損益計算書（US GAAP） [テキストブロック] """
    accounting_standards_dei: Optional[IxNonNumericPublic] = Field(default=None, description='会計基準、DEI')
    """ 会計基準、DEI """
    amendment_flag_dei: Optional[IxNonNumericPublic] = Field(default=None, description='訂正の有無、DEI')
    """ 訂正の有無、DEI """
    cabinet_office_ordinance_dei: Optional[IxNonNumericPublic] = Field(default=None, description='府令、DEI')
    """ 府令、DEI """
    comparative_period_end_date_dei: Optional[IxNonNumericPublic] = Field(default=None, description='比較対象会計期間終了日、DEI')
    """ 比較対象会計期間終了日、DEI """
    current_fiscal_year_end_date_dei: Optional[IxNonNumericPublic] = Field(default=None, description='当事業年度終了日、DEI')
    """ 当事業年度終了日、DEI """
    current_fiscal_year_start_date_dei: Optional[IxNonNumericPublic] = Field(default=None, description='当事業年度開始日、DEI')
    """ 当事業年度開始日、DEI """
    current_period_end_date_dei: Optional[IxNonNumericPublic] = Field(default=None, description='当会計期間終了日、DEI')
    """ 当会計期間終了日、DEI """
    document_type_dei: Optional[IxNonNumericPublic] = Field(default=None, description='様式、DEI')
    """ 様式、DEI """
    edinet_code_dei: Optional[IxNonNumericPublic] = Field(default=None, description='EDINETコード、DEI')
    """ EDINETコード、DEI """
    end_date_of_quarterly_or_semi_annual_period_of_next_fiscal_year_dei: Optional[IxNonNumericPublic] = Field(default=None, description='次の四半期又は中間期の会計期間終了日、DEI')
    """ 次の四半期又は中間期の会計期間終了日、DEI """
    filer_name_in_english_dei: Optional[IxNonNumericPublic] = Field(default=None, description='提出者名（英語表記）、DEI')
    """ 提出者名（英語表記）、DEI """
    filer_name_in_japanese_dei: Optional[IxNonNumericPublic] = Field(default=None, description='提出者名（日本語表記）、DEI')
    """ 提出者名（日本語表記）、DEI """
    fund_code_dei: Optional[IxNonNumericPublic] = Field(default=None, description='ファンドコード、DEI')
    """ ファンドコード、DEI """
    fund_name_in_english_dei: Optional[IxNonNumericPublic] = Field(default=None, description='ファンド名称（英語表記）、DEI')
    """ ファンド名称（英語表記）、DEI """
    fund_name_in_japanese_dei: Optional[IxNonNumericPublic] = Field(default=None, description='ファンド名称（日本語表記）、DEI')
    """ ファンド名称（日本語表記）、DEI """
    identification_of_document_subject_to_amendment_dei: Optional[IxNonNumericPublic] = Field(default=None, description='訂正対象書類の書類管理番号、DEI')
    """ 訂正対象書類の書類管理番号、DEI """
    industry_code_when_consolidated_financial_statements_are_prepared_in_accordance_with_industry_specific_regulations_dei: Optional[IxNonNumericPublic] = Field(default=None, description='別記事業（連結）、DEI')
    """ 別記事業（連結）、DEI """
    industry_code_when_financial_statements_are_prepared_in_accordance_with_industry_specific_regulations_dei: Optional[IxNonNumericPublic] = Field(default=None, description='別記事業（個別）、DEI')
    """ 別記事業（個別）、DEI """
    next_fiscal_year_start_date_dei: Optional[IxNonNumericPublic] = Field(default=None, description='次の事業年度開始日、DEI')
    """ 次の事業年度開始日、DEI """
    previous_fiscal_year_end_date_dei: Optional[IxNonNumericPublic] = Field(default=None, description='前事業年度終了日、DEI')
    """ 前事業年度終了日、DEI """
    previous_fiscal_year_start_date_dei: Optional[IxNonNumericPublic] = Field(default=None, description='前事業年度開始日、DEI')
    """ 前事業年度開始日、DEI """
    report_amendment_flag_dei: Optional[IxNonNumericPublic] = Field(default=None, description='記載事項訂正のフラグ、DEI')
    """ 記載事項訂正のフラグ、DEI """
    security_code_dei: Optional[IxNonNumericPublic] = Field(default=None, description='証券コード、DEI')
    """ 証券コード、DEI """
    type_of_current_period_dei: Optional[IxNonNumericPublic] = Field(default=None, description='当会計期間の種類、DEI')
    """ 当会計期間の種類、DEI """
    whether_consolidated_financial_statements_are_prepared_dei: Optional[IxNonNumericPublic] = Field(default=None, description='連結決算の有無、DEI')
    """ 連結決算の有無、DEI """
    xbrl_amendment_flag_dei: Optional[IxNonNumericPublic] = Field(default=None, description='XBRL訂正のフラグ、DEI')
    """ XBRL訂正のフラグ、DEI """

