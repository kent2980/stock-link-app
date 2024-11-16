from app.models import Field, SQLModel
from app.schema.ix_non_numeric import IxNonNumericPublic
from typing import Optional

class IxNonNumericEdifFr(SQLModel):
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
    condensed_quarter_period_consolidated_statement_of_comprehensive_income_ifrs_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='四半期連結会計期間、要約四半期連結包括利益計算書（IFRS） [テキストブロック]')
    """ 四半期連結会計期間、要約四半期連結包括利益計算書（IFRS） [テキストブロック] """
    condensed_quarter_period_consolidated_statement_of_profit_or_loss_ifrs_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='四半期連結会計期間、要約四半期連結損益計算書（IFRS） [テキストブロック]')
    """ 四半期連結会計期間、要約四半期連結損益計算書（IFRS） [テキストブロック] """
    condensed_quarterly_consolidated_statement_of_cash_flows_ifrs_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='要約四半期連結キャッシュ・フロー計算書（IFRS） [テキストブロック]')
    """ 要約四半期連結キャッシュ・フロー計算書（IFRS） [テキストブロック] """
    condensed_quarterly_consolidated_statement_of_changes_in_equity_ifrs_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='要約四半期連結持分変動計算書（IFRS） [テキストブロック]')
    """ 要約四半期連結持分変動計算書（IFRS） [テキストブロック] """
    condensed_quarterly_consolidated_statement_of_financial_position_ifrs_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='要約四半期連結財政状態計算書（IFRS） [テキストブロック]')
    """ 要約四半期連結財政状態計算書（IFRS） [テキストブロック] """
    condensed_year_to_quarter_end_consolidated_statement_of_comprehensive_income_ifrs_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='四半期連結累計期間、要約四半期連結包括利益計算書（IFRS） [テキストブロック]')
    """ 四半期連結累計期間、要約四半期連結包括利益計算書（IFRS） [テキストブロック] """
    condensed_year_to_quarter_end_consolidated_statement_of_comprehensive_income_single_statement_ifrs_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='四半期連結累計期間、要約四半期連結包括利益計算書（１計算書）（IFRS） [テキストブロック]')
    """ 四半期連結累計期間、要約四半期連結包括利益計算書（１計算書）（IFRS） [テキストブロック] """
    condensed_year_to_quarter_end_consolidated_statement_of_profit_or_loss_ifrs_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='四半期連結累計期間、要約四半期連結損益計算書（IFRS） [テキストブロック]')
    """ 四半期連結累計期間、要約四半期連結損益計算書（IFRS） [テキストブロック] """
    consolidated_statement_of_cash_flows_ifrs_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='連結キャッシュ・フロー計算書（IFRS） [テキストブロック]')
    """ 連結キャッシュ・フロー計算書（IFRS） [テキストブロック] """
    consolidated_statement_of_changes_in_equity_ifrs_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='連結持分変動計算書（IFRS） [テキストブロック]')
    """ 連結持分変動計算書（IFRS） [テキストブロック] """
    consolidated_statement_of_comprehensive_income_ifrs_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='連結包括利益計算書（IFRS） [テキストブロック]')
    """ 連結包括利益計算書（IFRS） [テキストブロック] """
    consolidated_statement_of_financial_position_ifrs_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='連結財政状態計算書（IFRS） [テキストブロック]')
    """ 連結財政状態計算書（IFRS） [テキストブロック] """
    consolidated_statement_of_profit_or_loss_ifrs_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='連結損益計算書（IFRS） [テキストブロック]')
    """ 連結損益計算書（IFRS） [テキストブロック] """
    description_of_fact_that_companys_business_comprises_single_segment_ifrs: Optional[IxNonNumericPublic] = Field(default=None, description='単一セグメントである旨（IFRS）')
    """ 単一セグメントである旨（IFRS） """
    disclosure_of_changes_in_reportable_segments_ifrs_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='報告セグメントの変更に関する事項（IFRS） [テキストブロック]')
    """ 報告セグメントの変更に関する事項（IFRS） [テキストブロック] """
    information_about_geographical_areas_ifrs_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='地域に関する情報（IFRS） [テキストブロック]')
    """ 地域に関する情報（IFRS） [テキストブロック] """
    information_about_major_customers_ifrs_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='主要な顧客に関する情報（IFRS） [テキストブロック]')
    """ 主要な顧客に関する情報（IFRS） [テキストブロック] """
    information_about_products_and_services_ifrs_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='製品及びサービスに関する情報（IFRS） [テキストブロック]')
    """ 製品及びサービスに関する情報（IFRS） [テキストブロック] """
    notes_segment_information_condensed_quarterly_consolidated_financial_statements_ifrs_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='注記事項－セグメント情報、要約四半期連結財務諸表（IFRS） [テキストブロック]')
    """ 注記事項－セグメント情報、要約四半期連結財務諸表（IFRS） [テキストブロック] """
    notes_segment_information_consolidated_financial_statements_ifrs_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='注記事項－セグメント情報、連結財務諸表（IFRS） [テキストブロック]')
    """ 注記事項－セグメント情報、連結財務諸表（IFRS） [テキストブロック] """

