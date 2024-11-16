from app.models import Field, SQLModel
from app.schema.ix_non_numeric import IxNonNumericPublic
from typing import Optional

class IxNonNumericEdjpFr(SQLModel):
    balance_sheet_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='貸借対照表 [テキストブロック]')
    """ 貸借対照表 [テキストブロック] """
    consolidated_balance_sheet_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='連結貸借対照表 [テキストブロック]')
    """ 連結貸借対照表 [テキストブロック] """
    consolidated_statement_of_cash_flows_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='連結キャッシュ・フロー計算書 [テキストブロック]')
    """ 連結キャッシュ・フロー計算書 [テキストブロック] """
    consolidated_statement_of_changes_in_equity_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='連結株主資本等変動計算書 [テキストブロック]')
    """ 連結株主資本等変動計算書 [テキストブロック] """
    consolidated_statement_of_comprehensive_income_single_statement_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='連結損益及び包括利益計算書 [テキストブロック]')
    """ 連結損益及び包括利益計算書 [テキストブロック] """
    consolidated_statement_of_comprehensive_income_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='連結包括利益計算書 [テキストブロック]')
    """ 連結包括利益計算書 [テキストブロック] """
    consolidated_statement_of_income_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='連結損益計算書 [テキストブロック]')
    """ 連結損益計算書 [テキストブロック] """
    debtors_notes_regarding_overdraft_contracts_and_or_loan_commitments_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='当座貸越契約及び（又は）貸出コミットメントに関する借手の注記 [テキストブロック]')
    """ 当座貸越契約及び（又は）貸出コミットメントに関する借手の注記 [テキストブロック] """
    description_of_fact_that_companys_business_comprises_single_segment: Optional[IxNonNumericPublic] = Field(default=None, description='単一セグメントである旨')
    """ 単一セグメントである旨 """
    description_of_factors_which_led_to_recognition_of_gain_on_bargain_purchase_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='報告セグメントごとの負ののれん発生益を認識する要因となった事象の概要 [テキストブロック]')
    """ 報告セグメントごとの負ののれん発生益を認識する要因となった事象の概要 [テキストブロック] """
    description_of_nature_and_amounts_of_differences_between_reportable_segments_total_and_financial_statements_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='報告セグメント合計額と財務諸表計上額との差額及び当該差額の主な内容（差異調整に関する事項） [テキストブロック]')
    """ 報告セグメント合計額と財務諸表計上額との差額及び当該差額の主な内容（差異調整に関する事項） [テキストブロック] """
    description_of_nature_of_differences_between_profit_loss_of_reportable_segments_total_and_quarterly_financial_statements_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='報告セグメントごとの利益又は損失の金額の合計額と四半期損益計算書計上額との差額及び当該差額の主な内容（差異調整に関する事項） [テキストブロック]')
    """ 報告セグメントごとの利益又は損失の金額の合計額と四半期損益計算書計上額との差額及び当該差額の主な内容（差異調整に関する事項） [テキストブロック] """
    description_of_reportable_segments_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='報告セグメントの概要 [テキストブロック]')
    """ 報告セグメントの概要 [テキストブロック] """
    detailed_schedule_of_manufacturing_cost_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='製造原価明細書 [テキストブロック]')
    """ 製造原価明細書 [テキストブロック] """
    disclosure_of_changes_etc_in_reportable_segments_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='報告セグメントの変更等に関する事項 [テキストブロック]')
    """ 報告セグメントの変更等に関する事項 [テキストブロック] """
    disclosure_of_changes_in_reportable_segments_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='報告セグメントの変更に関する事項 [テキストブロック]')
    """ 報告セグメントの変更に関する事項 [テキストブロック] """
    explanation_of_measurements_of_sales_profit_loss_asset_liability_and_other_items_for_each_reportable_segment_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='報告セグメントごとの売上高、利益又は損失、資産、負債その他の項目の金額の算定方法 [テキストブロック]')
    """ 報告セグメントごとの売上高、利益又は損失、資産、負債その他の項目の金額の算定方法 [テキストブロック] """
    footnotes_regarding_segment_information_table_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='セグメント表の脚注 [テキストブロック]')
    """ セグメント表の脚注 [テキストブロック] """
    information_about_assets_for_each_reportable_segment_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='報告セグメントごとの資産に関する情報 [テキストブロック]')
    """ 報告セグメントごとの資産に関する情報 [テキストブロック] """
    information_about_impairment_loss_of_non_current_assets_or_goodwill_etc_for_each_reportable_segment_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='報告セグメントごとの固定資産の減損損失又はのれん等に関する情報 [テキストブロック]')
    """ 報告セグメントごとの固定資産の減損損失又はのれん等に関する情報 [テキストブロック] """
    information_for_each_of_main_customers_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='主要な顧客ごとの情報 [テキストブロック]')
    """ 主要な顧客ごとの情報 [テキストブロック] """
    information_for_each_product_or_service_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='製品及びサービスごとの情報 [テキストブロック]')
    """ 製品及びサービスごとの情報 [テキストブロック] """
    major_components_of_selling_general_and_administrative_expenses_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='主要な販売費及び一般管理費 [テキストブロック]')
    """ 主要な販売費及び一般管理費 [テキストブロック] """
    notes_regarding_accumulated_depreciation_of_property_plant_and_equipment_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='有形固定資産の減価償却累計額の注記 [テキストブロック]')
    """ 有形固定資産の減価償却累計額の注記 [テキストブロック] """
    notes_regarding_allowances_directly_deducted_from_balances_of_assets_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='資産の金額から直接控除している引当金の注記 [テキストブロック]')
    """ 資産の金額から直接控除している引当金の注記 [テキストブロック] """
    notes_regarding_amounts_of_reduction_entry_of_property_plant_and_equipment_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='有形固定資産の圧縮記帳額の注記 [テキストブロック]')
    """ 有形固定資産の圧縮記帳額の注記 [テキストブロック] """
    notes_regarding_gain_on_sales_of_property_plant_and_equipment_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='固定資産売却益の注記 [テキストブロック]')
    """ 固定資産売却益の注記 [テキストブロック] """
    notes_regarding_guarantee_obligations_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='保証債務の注記 [テキストブロック]')
    """ 保証債務の注記 [テキストブロック] """
    notes_regarding_impairment_loss_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='減損損失に関する注記 [テキストブロック]')
    """ 減損損失に関する注記 [テキストブロック] """
    notes_regarding_inventories_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='棚卸資産の内訳の注記 [テキストブロック]')
    """ 棚卸資産の内訳の注記 [テキストブロック] """
    notes_regarding_loss_on_disposal_of_property_plant_and_equipment_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='固定資産除却損の注記 [テキストブロック]')
    """ 固定資産除却損の注記 [テキストブロック] """
    notes_regarding_loss_on_sales_of_property_plant_and_equipment_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='固定資産売却損の注記 [テキストブロック]')
    """ 固定資産売却損の注記 [テキストブロック] """
    notes_regarding_pledged_assets_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='担保に供している資産の注記 [テキストブロック]')
    """ 担保に供している資産の注記 [テキストブロック] """
    notes_regarding_promissory_notes_due_on_balance_sheet_date_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='期末日満期手形の会計処理 [テキストブロック]')
    """ 期末日満期手形の会計処理 [テキストブロック] """
    notes_regarding_shares_and_bonds_etc_of_unconsolidated_subsidiaries_and_associates_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='非連結子会社及び関連会社の株式及び社債等 [テキストブロック]')
    """ 非連結子会社及び関連会社の株式及び社債等 [テキストブロック] """
    notes_segment_information_etc_consolidated_financial_statements_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='セグメント情報等、連結財務諸表 [テキストブロック]')
    """ セグメント情報等、連結財務諸表 [テキストブロック] """
    notes_segment_information_etc_financial_statements_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='セグメント情報等、財務諸表 [テキストブロック]')
    """ セグメント情報等、財務諸表 [テキストブロック] """
    notes_segment_information_etc_quarterly_consolidated_financial_statements_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='セグメント情報等、四半期連結財務諸表 [テキストブロック]')
    """ セグメント情報等、四半期連結財務諸表 [テキストブロック] """
    notes_segment_information_etc_quarterly_financial_statements_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='セグメント情報等、四半期財務諸表 [テキストブロック]')
    """ セグメント情報等、四半期財務諸表 [テキストブロック] """
    notes_segment_information_etc_semi_annual_consolidated_financial_statements_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='セグメント情報等、中間連結財務諸表 [テキストブロック]')
    """ セグメント情報等、中間連結財務諸表 [テキストブロック] """
    notes_when_there_is_significant_seasonal_fluctuation_in_sales_or_operating_expenses_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='売上高又は営業費用に著しい季節的変動がある場合の注記 [テキストブロック]')
    """ 売上高又は営業費用に著しい季節的変動がある場合の注記 [テキストブロック] """
    property_plant_and_equipment_information_for_each_region_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='有形固定資産、地域ごとの情報 [テキストブロック]')
    """ 有形固定資産、地域ごとの情報 [テキストブロック] """
    quarterly_balance_sheet_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='四半期貸借対照表 [テキストブロック]')
    """ 四半期貸借対照表 [テキストブロック] """
    quarterly_consolidated_balance_sheet_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='四半期連結貸借対照表 [テキストブロック]')
    """ 四半期連結貸借対照表 [テキストブロック] """
    quarterly_consolidated_statement_of_cash_flows_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='四半期連結キャッシュ・フロー計算書 [テキストブロック]')
    """ 四半期連結キャッシュ・フロー計算書 [テキストブロック] """
    quarterly_statement_of_cash_flows_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='四半期キャッシュ・フロー計算書 [テキストブロック]')
    """ 四半期キャッシュ・フロー計算書 [テキストブロック] """
    research_and_development_expenses_included_in_general_and_administrative_expenses_and_manufacturing_cost_for_current_period_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='一般管理費及び当期製造費用に含まれる研究開発費 [テキストブロック]')
    """ 一般管理費及び当期製造費用に含まれる研究開発費 [テキストブロック] """
    revenues_from_external_customers_information_for_each_region_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='売上高、地域ごとの情報 [テキストブロック]')
    """ 売上高、地域ごとの情報 [テキストブロック] """
    semi_annual_balance_sheet_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='中間貸借対照表 [テキストブロック]')
    """ 中間貸借対照表 [テキストブロック] """
    semi_annual_consolidated_balance_sheet_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='中間連結貸借対照表 [テキストブロック]')
    """ 中間連結貸借対照表 [テキストブロック] """
    semi_annual_consolidated_statement_of_cash_flows_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='中間連結キャッシュ・フロー計算書 [テキストブロック]')
    """ 中間連結キャッシュ・フロー計算書 [テキストブロック] """
    semi_annual_consolidated_statement_of_changes_in_equity_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='中間連結株主資本等変動計算書 [テキストブロック]')
    """ 中間連結株主資本等変動計算書 [テキストブロック] """
    semi_annual_consolidated_statement_of_comprehensive_income_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='中間連結包括利益計算書 [テキストブロック]')
    """ 中間連結包括利益計算書 [テキストブロック] """
    semi_annual_consolidated_statement_of_income_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='中間連結損益計算書 [テキストブロック]')
    """ 中間連結損益計算書 [テキストブロック] """
    semi_annual_statement_of_changes_in_equity_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='中間株主資本等変動計算書 [テキストブロック]')
    """ 中間株主資本等変動計算書 [テキストブロック] """
    semi_annual_statement_of_income_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='中間損益計算書 [テキストブロック]')
    """ 中間損益計算書 [テキストブロック] """
    statement_of_cash_flows_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='キャッシュ・フロー計算書 [テキストブロック]')
    """ キャッシュ・フロー計算書 [テキストブロック] """
    statement_of_changes_in_equity_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='株主資本等変動計算書 [テキストブロック]')
    """ 株主資本等変動計算書 [テキストブロック] """
    statement_of_income_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='損益計算書 [テキストブロック]')
    """ 損益計算書 [テキストブロック] """
    year_to_quarter_end_consolidated_statement_of_comprehensive_income_single_statement_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='四半期連結累計期間、四半期連結損益及び包括利益計算書 [テキストブロック]')
    """ 四半期連結累計期間、四半期連結損益及び包括利益計算書 [テキストブロック] """
    year_to_quarter_end_consolidated_statement_of_comprehensive_income_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='四半期連結累計期間、四半期連結包括利益計算書 [テキストブロック]')
    """ 四半期連結累計期間、四半期連結包括利益計算書 [テキストブロック] """
    year_to_quarter_end_consolidated_statement_of_income_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='四半期連結累計期間、四半期連結損益計算書 [テキストブロック]')
    """ 四半期連結累計期間、四半期連結損益計算書 [テキストブロック] """
    year_to_quarter_end_statement_of_income_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='四半期累計期間、四半期損益計算書 [テキストブロック]')
    """ 四半期累計期間、四半期損益計算書 [テキストブロック] """
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
    notes_regarding_amortization_of_goodwill_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='のれん償却額の注記 [テキストブロック]')
    """ のれん償却額の注記 [テキストブロック] """
    notes_regarding_loss_on_abandonment_of_inventories_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='棚卸資産廃棄損の注記 [テキストブロック]')
    """ 棚卸資産廃棄損の注記 [テキストブロック] """
    notes_regarding_loss_on_disaster_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='災害による損失の注記 [テキストブロック]')
    """ 災害による損失の注記 [テキストブロック] """
    notes_regarding_restructuring_loss_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='事業再編損の注記 [テキストブロック]')
    """ 事業再編損の注記 [テキストブロック] """
    notes_regarding_subsidy_income_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='補助金収入の注記 [テキストブロック]')
    """ 補助金収入の注記 [テキストブロック] """
    notes_regarding_financial_covenant_clauses_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='財務制限条項に関する注記 [テキストブロック]')
    """ 財務制限条項に関する注記 [テキストブロック] """
    notes_regarding_details_of_extraordinary_losses_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='特別損失の内容に関する注記 [テキストブロック]')
    """ 特別損失の内容に関する注記 [テキストブロック] """
    notes_regarding_relocation_related_losses_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='移転関連損失についての注記 [テキストブロック]')
    """ 移転関連損失についての注記 [テキストブロック] """
    notes_and_accounts_receivable_trede_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='受取手形及び売掛金に関する注記 [テキストブロック]')
    """ 受取手形及び売掛金に関する注記 [テキストブロック] """
    notes_regarding_gain_on_transfer_of_business_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='事業譲渡益の注記 [テキストブロック]')
    """ 事業譲渡益の注記 [テキストブロック] """
    notes_regarding_loss_on_liquidation_of_subsidiaries_and_associates_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='関係会社清算損の注記 [テキストブロック]')
    """ 関係会社清算損の注記 [テキストブロック] """
    notes_regarding_reduction_entry_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='圧縮記帳額に関する注記 [テキストブロック]')
    """ 圧縮記帳額に関する注記 [テキストブロック] """
    notes_regarding_reversal_of_provision_for_loss_on_compensation_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='補償損失引当金戻入額に関する注記 [テキストブロック]')
    """ 補償損失引当金戻入額に関する注記 [テキストブロック] """
    notes_regarding_loss_on_litigation_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='訴訟関連損失の注記 [テキストブロック]')
    """ 訴訟関連損失の注記 [テキストブロック] """
    notes_regarding_provision_for_loss_on_litigation_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='訴訟損失引当金に関する注記 [テキストブロック]')
    """ 訴訟損失引当金に関する注記 [テキストブロック] """
    notes_regarding_loss_on_inappropriate_conduct_in_quality_inspections_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='品質不適切行為関連損失に関する注記 [テキストブロック]')
    """ 品質不適切行為関連損失に関する注記 [テキストブロック] """
    notes_system_failure_response_cost_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='システム障害対応費用の注記 [テキストブロック]')
    """ システム障害対応費用の注記 [テキストブロック] """
    notes_on_contingent_liabilities_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='偶発債務に関する注記 [テキストブロック]')
    """ 偶発債務に関する注記 [テキストブロック] """
    disclosure_of_impairment_loss_on_non_current_assets_for_each_reportable_segment_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='報告セグメントごとの固定資産の減損損失に関する情報 [テキストブロック]')
    """ 報告セグメントごとの固定資産の減損損失に関する情報 [テキストブロック] """
    notes_regarding_provision_for_return_of_subsidy_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='助成金返還引当金繰入額に関する注記 [テキストブロック]')
    """ 助成金返還引当金繰入額に関する注記 [テキストブロック] """
    notes_regarding_materials_supplied_for_value_text_block: Optional[IxNonNumericPublic] = Field(default=None, description='有償支給材料に関する注記 [テキストブロック]')
    """ 有償支給材料に関する注記 [テキストブロック] """

