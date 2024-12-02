from app.models import Field, SQLModel
from app.schema.ix_non_numeric import IxNonNumericPublic


class edif(SQLModel):
    type: str = Field(default="edif", description="型タイプ")
    """ 型タイプ """
    condensed_quarterly_consolidated_statement_of_cash_flows_ifrs_text_block:IxNonNumericPublic = Field(default=None, description="要約四半期連結キャッシュ・フロー計算書（IFRS） [テキストブロック]")
    """ 要約四半期連結キャッシュ・フロー計算書（IFRS） [テキストブロック] """
    condensed_quarterly_consolidated_statement_of_cash_flows_ifrs_text_block:IxNonNumericPublic = Field(default=None, description="要約四半期連結キャッシュ・フロー計算書（IFRS） [テキストブロック]")
    """ 要約四半期連結キャッシュ・フロー計算書（IFRS） [テキストブロック] """
    condensed_quarterly_consolidated_statement_of_changes_in_equity_ifrs_text_block:IxNonNumericPublic = Field(default=None, description="要約四半期連結持分変動計算書（IFRS） [テキストブロック]")
    """ 要約四半期連結持分変動計算書（IFRS） [テキストブロック] """
    accounting_standards_dei:IxNonNumericPublic = Field(default=None, description="会計基準、DEI")
    """ 会計基準、DEI """
    amendment_flag_dei:IxNonNumericPublic = Field(default=None, description="訂正の有無、DEI")
    """ 訂正の有無、DEI """
    cabinet_office_ordinance_dei:IxNonNumericPublic = Field(default=None, description="府令、DEI")
    """ 府令、DEI """
    comparative_period_end_date_dei:IxNonNumericPublic = Field(default=None, description="比較対象会計期間終了日、DEI")
    """ 比較対象会計期間終了日、DEI """
    current_fiscal_year_end_date_dei:IxNonNumericPublic = Field(default=None, description="当事業年度終了日、DEI")
    """ 当事業年度終了日、DEI """
    current_fiscal_year_start_date_dei:IxNonNumericPublic = Field(default=None, description="当事業年度開始日、DEI")
    """ 当事業年度開始日、DEI """
    current_period_end_date_dei:IxNonNumericPublic = Field(default=None, description="当会計期間終了日、DEI")
    """ 当会計期間終了日、DEI """
    document_type_dei:IxNonNumericPublic = Field(default=None, description="様式、DEI")
    """ 様式、DEI """
    edinet_code_dei:IxNonNumericPublic = Field(default=None, description="EDINETコード、DEI")
    """ EDINETコード、DEI """
    end_date_of_quarterly_or_semi_annual_period_of_next_fiscal_year_dei:IxNonNumericPublic = Field(default=None, description="次の四半期又は中間期の会計期間終了日、DEI")
    """ 次の四半期又は中間期の会計期間終了日、DEI """
    filer_name_in_english_dei:IxNonNumericPublic = Field(default=None, description="提出者名（英語表記）、DEI")
    """ 提出者名（英語表記）、DEI """
    filer_name_in_japanese_dei:IxNonNumericPublic = Field(default=None, description="提出者名（日本語表記）、DEI")
    """ 提出者名（日本語表記）、DEI """
    fund_code_dei:IxNonNumericPublic = Field(default=None, description="ファンドコード、DEI")
    """ ファンドコード、DEI """
    fund_name_in_english_dei:IxNonNumericPublic = Field(default=None, description="ファンド名称（英語表記）、DEI")
    """ ファンド名称（英語表記）、DEI """
    fund_name_in_japanese_dei:IxNonNumericPublic = Field(default=None, description="ファンド名称（日本語表記）、DEI")
    """ ファンド名称（日本語表記）、DEI """
    identification_of_document_subject_to_amendment_dei:IxNonNumericPublic = Field(default=None, description="訂正対象書類の書類管理番号、DEI")
    """ 訂正対象書類の書類管理番号、DEI """
    industry_code_when_consolidated_financial_statements_are_prepared_in_accordance_with_industry_specific_regulations_dei:IxNonNumericPublic = Field(default=None, description="別記事業（連結）、DEI")
    """ 別記事業（連結）、DEI """
    industry_code_when_financial_statements_are_prepared_in_accordance_with_industry_specific_regulations_dei:IxNonNumericPublic = Field(default=None, description="別記事業（個別）、DEI")
    """ 別記事業（個別）、DEI """
    next_fiscal_year_start_date_dei:IxNonNumericPublic = Field(default=None, description="次の事業年度開始日、DEI")
    """ 次の事業年度開始日、DEI """
    previous_fiscal_year_end_date_dei:IxNonNumericPublic = Field(default=None, description="前事業年度終了日、DEI")
    """ 前事業年度終了日、DEI """
    previous_fiscal_year_start_date_dei:IxNonNumericPublic = Field(default=None, description="前事業年度開始日、DEI")
    """ 前事業年度開始日、DEI """
    report_amendment_flag_dei:IxNonNumericPublic = Field(default=None, description="記載事項訂正のフラグ、DEI")
    """ 記載事項訂正のフラグ、DEI """
    security_code_dei:IxNonNumericPublic = Field(default=None, description="証券コード、DEI")
    """ 証券コード、DEI """
    type_of_current_period_dei:IxNonNumericPublic = Field(default=None, description="当会計期間の種類、DEI")
    """ 当会計期間の種類、DEI """
    whether_consolidated_financial_statements_are_prepared_dei:IxNonNumericPublic = Field(default=None, description="連結決算の有無、DEI")
    """ 連結決算の有無、DEI """
    xbrl_amendment_flag_dei:IxNonNumericPublic = Field(default=None, description="XBRL訂正のフラグ、DEI")
    """ XBRL訂正のフラグ、DEI """
    condensed_quarterly_consolidated_statement_of_financial_position_ifrs_text_block:IxNonNumericPublic = Field(default=None, description="要約四半期連結財政状態計算書（IFRS） [テキストブロック]")
    """ 要約四半期連結財政状態計算書（IFRS） [テキストブロック] """
    condensed_quarter_period_consolidated_statement_of_comprehensive_income_ifrs_text_block:IxNonNumericPublic = Field(default=None, description="四半期連結会計期間、要約四半期連結包括利益計算書（IFRS） [テキストブロック]")
    """ 四半期連結会計期間、要約四半期連結包括利益計算書（IFRS） [テキストブロック] """
    condensed_quarter_period_consolidated_statement_of_profit_or_loss_ifrs_text_block:IxNonNumericPublic = Field(default=None, description="四半期連結会計期間、要約四半期連結損益計算書（IFRS） [テキストブロック]")
    """ 四半期連結会計期間、要約四半期連結損益計算書（IFRS） [テキストブロック] """
    condensed_year_to_quarter_end_consolidated_statement_of_comprehensive_income_ifrs_text_block:IxNonNumericPublic = Field(default=None, description="四半期連結累計期間、要約四半期連結包括利益計算書（IFRS） [テキストブロック]")
    """ 四半期連結累計期間、要約四半期連結包括利益計算書（IFRS） [テキストブロック] """
    condensed_year_to_quarter_end_consolidated_statement_of_comprehensive_income_single_statement_ifrs_text_block:IxNonNumericPublic = Field(default=None, description="四半期連結累計期間、要約四半期連結包括利益計算書（１計算書）（IFRS） [テキストブロック]")
    """ 四半期連結累計期間、要約四半期連結包括利益計算書（１計算書）（IFRS） [テキストブロック] """
    accounting_standards_dei:IxNonNumericPublic = Field(default=None, description="会計基準、DEI")
    """ 会計基準、DEI """
    amendment_flag_dei:IxNonNumericPublic = Field(default=None, description="訂正の有無、DEI")
    """ 訂正の有無、DEI """
    cabinet_office_ordinance_dei:IxNonNumericPublic = Field(default=None, description="府令、DEI")
    """ 府令、DEI """
    comparative_period_end_date_dei:IxNonNumericPublic = Field(default=None, description="比較対象会計期間終了日、DEI")
    """ 比較対象会計期間終了日、DEI """
    current_fiscal_year_end_date_dei:IxNonNumericPublic = Field(default=None, description="当事業年度終了日、DEI")
    """ 当事業年度終了日、DEI """
    current_fiscal_year_start_date_dei:IxNonNumericPublic = Field(default=None, description="当事業年度開始日、DEI")
    """ 当事業年度開始日、DEI """
    current_period_end_date_dei:IxNonNumericPublic = Field(default=None, description="当会計期間終了日、DEI")
    """ 当会計期間終了日、DEI """
    document_type_dei:IxNonNumericPublic = Field(default=None, description="様式、DEI")
    """ 様式、DEI """
    edinet_code_dei:IxNonNumericPublic = Field(default=None, description="EDINETコード、DEI")
    """ EDINETコード、DEI """
    end_date_of_quarterly_or_semi_annual_period_of_next_fiscal_year_dei:IxNonNumericPublic = Field(default=None, description="次の四半期又は中間期の会計期間終了日、DEI")
    """ 次の四半期又は中間期の会計期間終了日、DEI """
    filer_name_in_english_dei:IxNonNumericPublic = Field(default=None, description="提出者名（英語表記）、DEI")
    """ 提出者名（英語表記）、DEI """
    filer_name_in_japanese_dei:IxNonNumericPublic = Field(default=None, description="提出者名（日本語表記）、DEI")
    """ 提出者名（日本語表記）、DEI """
    fund_code_dei:IxNonNumericPublic = Field(default=None, description="ファンドコード、DEI")
    """ ファンドコード、DEI """
    fund_name_in_english_dei:IxNonNumericPublic = Field(default=None, description="ファンド名称（英語表記）、DEI")
    """ ファンド名称（英語表記）、DEI """
    fund_name_in_japanese_dei:IxNonNumericPublic = Field(default=None, description="ファンド名称（日本語表記）、DEI")
    """ ファンド名称（日本語表記）、DEI """
    identification_of_document_subject_to_amendment_dei:IxNonNumericPublic = Field(default=None, description="訂正対象書類の書類管理番号、DEI")
    """ 訂正対象書類の書類管理番号、DEI """
    industry_code_when_consolidated_financial_statements_are_prepared_in_accordance_with_industry_specific_regulations_dei:IxNonNumericPublic = Field(default=None, description="別記事業（連結）、DEI")
    """ 別記事業（連結）、DEI """
    industry_code_when_financial_statements_are_prepared_in_accordance_with_industry_specific_regulations_dei:IxNonNumericPublic = Field(default=None, description="別記事業（個別）、DEI")
    """ 別記事業（個別）、DEI """
    next_fiscal_year_start_date_dei:IxNonNumericPublic = Field(default=None, description="次の事業年度開始日、DEI")
    """ 次の事業年度開始日、DEI """
    previous_fiscal_year_end_date_dei:IxNonNumericPublic = Field(default=None, description="前事業年度終了日、DEI")
    """ 前事業年度終了日、DEI """
    previous_fiscal_year_start_date_dei:IxNonNumericPublic = Field(default=None, description="前事業年度開始日、DEI")
    """ 前事業年度開始日、DEI """
    report_amendment_flag_dei:IxNonNumericPublic = Field(default=None, description="記載事項訂正のフラグ、DEI")
    """ 記載事項訂正のフラグ、DEI """
    security_code_dei:IxNonNumericPublic = Field(default=None, description="証券コード、DEI")
    """ 証券コード、DEI """
    type_of_current_period_dei:IxNonNumericPublic = Field(default=None, description="当会計期間の種類、DEI")
    """ 当会計期間の種類、DEI """
    whether_consolidated_financial_statements_are_prepared_dei:IxNonNumericPublic = Field(default=None, description="連結決算の有無、DEI")
    """ 連結決算の有無、DEI """
    xbrl_amendment_flag_dei:IxNonNumericPublic = Field(default=None, description="XBRL訂正のフラグ、DEI")
    """ XBRL訂正のフラグ、DEI """
    condensed_year_to_quarter_end_consolidated_statement_of_profit_or_loss_ifrs_text_block:IxNonNumericPublic = Field(default=None, description="四半期連結累計期間、要約四半期連結損益計算書（IFRS） [テキストブロック]")
    """ 四半期連結累計期間、要約四半期連結損益計算書（IFRS） [テキストブロック] """
    changes_in_accounting_estimates_ifrs:IxNonNumericPublic = Field(default=None, description="会計上の見積りの変更、IFRS")
    """ 会計上の見積りの変更、IFRS """
    changes_in_accounting_policies_other_than_ifrs_requirements_ifrs:IxNonNumericPublic = Field(default=None, description="IFRSにより要求される会計方針の変更以外の会計方針の変更、IFRS")
    """ IFRSにより要求される会計方針の変更以外の会計方針の変更、IFRS """
    changes_in_accounting_policies_required_by_ifrsifrs:IxNonNumericPublic = Field(default=None, description="IFRSにより要求される会計方針の変更、IFRS")
    """ IFRSにより要求される会計方針の変更、IFRS """
    company_name:IxNonNumericPublic = Field(default=None, description="上場会社名")
    """ 上場会社名 """
    convening_briefing_of_results:IxNonNumericPublic = Field(default=None, description="決算説明会開催の有無、期中")
    """ 決算説明会開催の有無、期中 """
    correction_of_consolidated_financial_forecast_in_this_quarter:IxNonNumericPublic = Field(default=None, description="直近に公表されている業績予想からの修正の有無、連結")
    """ 直近に公表されている業績予想からの修正の有無、連結 """
    correction_of_dividend_forecast_in_this_quarter:IxNonNumericPublic = Field(default=None, description="直近に公表されている配当予想からの修正の有無")
    """ 直近に公表されている配当予想からの修正の有無 """
    dividend_payable_date_as_planned:IxNonNumericPublic = Field(default=None, description="配当支払開始予定日")
    """ 配当支払開始予定日 """
    document_name:IxNonNumericPublic = Field(default=None, description="文書名")
    """ 文書名 """
    fasf_member_mark:IxNonNumericPublic = Field(default=None, description="財務会計基準機構会員マーク")
    """ 財務会計基準機構会員マーク """
    filing_date:IxNonNumericPublic = Field(default=None, description="提出日")
    """ 提出日 """
    fiscal_year_end:IxNonNumericPublic = Field(default=None, description="決算期")
    """ 決算期 """
    fukuoka_stock_exchange:IxNonNumericPublic = Field(default=None, description="福岡証券取引所")
    """ 福岡証券取引所 """
    fukuoka_stock_exchange_established:IxNonNumericPublic = Field(default=None, description="福岡証券取引所 既存市場")
    """ 福岡証券取引所 既存市場 """
    fukuoka_stock_exchange_others:IxNonNumericPublic = Field(default=None, description="福岡証券取引所 その他")
    """ 福岡証券取引所 その他 """
    fukuoka_stock_exchange_q_board:IxNonNumericPublic = Field(default=None, description="福岡証券取引所 Q-Board")
    """ 福岡証券取引所 Q-Board """
    general_business:IxNonNumericPublic = Field(default=None, description="一般事業会社")
    """ 一般事業会社 """
    japan_securities_dealers_association:IxNonNumericPublic = Field(default=None, description="フェニックス")
    """ フェニックス """
    japan_securities_dealers_association_green_sheet:IxNonNumericPublic = Field(default=None, description="日本証券業協会 フェニックス")
    """ 日本証券業協会 フェニックス """
    nagoya_stock_exchange:IxNonNumericPublic = Field(default=None, description="名古屋証券取引所")
    """ 名古屋証券取引所 """
    nagoya_stock_exchange1st_section:IxNonNumericPublic = Field(default=None, description="名古屋証券取引所 プレミア")
    """ 名古屋証券取引所 プレミア """
    nagoya_stock_exchange2nd_section:IxNonNumericPublic = Field(default=None, description="名古屋証券取引所 メイン")
    """ 名古屋証券取引所 メイン """
    nagoya_stock_exchange_centrex:IxNonNumericPublic = Field(default=None, description="名古屋証券取引所 ネクスト")
    """ 名古屋証券取引所 ネクスト """
    nagoya_stock_exchange_others:IxNonNumericPublic = Field(default=None, description="名古屋証券取引所 その他")
    """ 名古屋証券取引所 その他 """
    name_inquiries:IxNonNumericPublic = Field(default=None, description="氏名、問合せ先責任者")
    """ 氏名、問合せ先責任者 """
    name_of_subsidiaries_excluded_from_consolidation_ifrs:IxNonNumericPublic = Field(default=None, description="社名、除外、IFRS")
    """ 社名、除外、IFRS """
    name_of_subsidiaries_newly_consolidated_ifrs:IxNonNumericPublic = Field(default=None, description="社名、新規、IFRS")
    """ 社名、新規、IFRS """
    name_representative:IxNonNumericPublic = Field(default=None, description="氏名、代表者")
    """ 氏名、代表者 """
    notes_for_using_forecasted_information_and_others:IxNonNumericPublic = Field(default=None, description="業績予想の適切な利用に関する説明、その他特記事項")
    """ 業績予想の適切な利用に関する説明、その他特記事項 """
    note_to_changes_in_accounting_policies_and_accounting_estimates_ifrs:IxNonNumericPublic = Field(default=None, description="会計方針の変更・会計上の見積りの変更に関する注記、IFRS")
    """ 会計方針の変更・会計上の見積りの変更に関する注記、IFRS """
    note_to_consolidated_financial_results:IxNonNumericPublic = Field(default=None, description="連結業績に関する注記")
    """ 連結業績に関する注記 """
    note_to_dividends:IxNonNumericPublic = Field(default=None, description="配当の状況に関する注記")
    """ 配当の状況に関する注記 """
    note_to_financial_positions:IxNonNumericPublic = Field(default=None, description="財政状態に関する注記")
    """ 財政状態に関する注記 """
    note_to_forecasts:IxNonNumericPublic = Field(default=None, description="業績予想に関する事項、注記")
    """ 業績予想に関する事項、注記 """
    note_to_fraction_processing_method:IxNonNumericPublic = Field(default=None, description="端数処理方法に関する注記")
    """ 端数処理方法に関する注記 """
    note_to_number_of_issued_and_outstanding_shares_common_stock:IxNonNumericPublic = Field(default=None, description="発行済株式数（普通株式）に関する注記")
    """ 発行済株式数（普通株式）に関する注記 """
    note_to_operating_results:IxNonNumericPublic = Field(default=None, description="経営成績に関する注記")
    """ 経営成績に関する注記 """
    note_to_significant_changes_in_the_scope_of_consolidation_during_the_period:IxNonNumericPublic = Field(default=None, description="期中における連結範囲の重要な変更に関する注記")
    """ 期中における連結範囲の重要な変更に関する注記 """
    preamble_to_forecasts:IxNonNumericPublic = Field(default=None, description="業績予想に関する事項")
    """ 業績予想に関する事項 """
    review_of_attached_consolidated_quarterly_financial_statements_by_a_certified_public_accountant_or_an_audit_firm:IxNonNumericPublic = Field(default=None, description="添付される四半期連結財務諸表に対する公認会計士又は監査法人によるレビュー")
    """ 添付される四半期連結財務諸表に対する公認会計士又は監査法人によるレビュー """
    sapporo_stock_exchange:IxNonNumericPublic = Field(default=None, description="札幌証券取引所")
    """ 札幌証券取引所 """
    sapporo_stock_exchange_ambitious:IxNonNumericPublic = Field(default=None, description="札幌証券取引所 アンビシャス")
    """ 札幌証券取引所 アンビシャス """
    sapporo_stock_exchange_established:IxNonNumericPublic = Field(default=None, description="札幌証券取引所 既存市場")
    """ 札幌証券取引所 既存市場 """
    sapporo_stock_exchange_others:IxNonNumericPublic = Field(default=None, description="札幌証券取引所 その他")
    """ 札幌証券取引所 その他 """
    securities_code:IxNonNumericPublic = Field(default=None, description="コード番号")
    """ コード番号 """
    semi_annual_statement_filing_date_as_planned:IxNonNumericPublic = Field(default=None, description="半期報告書提出予定日")
    """ 半期報告書提出予定日 """
    significant_changes_in_the_scope_of_consolidation_during_the_period_ifrs:IxNonNumericPublic = Field(default=None, description="期中における連結範囲の重要な変更、IFRS")
    """ 期中における連結範囲の重要な変更、IFRS """
    specific_business:IxNonNumericPublic = Field(default=None, description="特定事業会社")
    """ 特定事業会社 """
    supplemental_material_of_results:IxNonNumericPublic = Field(default=None, description="決算補足説明資料作成の有無、期中")
    """ 決算補足説明資料作成の有無、期中 """
    target_for_briefing_of_results:IxNonNumericPublic = Field(default=None, description="決算説明会の対象者")
    """ 決算説明会の対象者 """
    tel:IxNonNumericPublic = Field(default=None, description="TEL")
    """ TEL """
    title_for_forecasts:IxNonNumericPublic = Field(default=None, description="業績予想タイトル名称")
    """ 業績予想タイトル名称 """
    title_inquiries:IxNonNumericPublic = Field(default=None, description="役職名、問合せ先責任者")
    """ 役職名、問合せ先責任者 """
    title_representative:IxNonNumericPublic = Field(default=None, description="役職名、代表者")
    """ 役職名、代表者 """
    tokyo_stock_exchange:IxNonNumericPublic = Field(default=None, description="東京証券取引所")
    """ 東京証券取引所 """
    tokyo_stock_exchange_growth:IxNonNumericPublic = Field(default=None, description="東京証券取引所 グロース")
    """ 東京証券取引所 グロース """
    tokyo_stock_exchange_others:IxNonNumericPublic = Field(default=None, description="東京証券取引所 その他")
    """ 東京証券取引所 その他 """
    tokyo_stock_exchange_prime:IxNonNumericPublic = Field(default=None, description="東京証券取引所 プライム")
    """ 東京証券取引所 プライム """
    tokyo_stock_exchange_pro_market:IxNonNumericPublic = Field(default=None, description="東京証券取引所 PRO Market")
    """ 東京証券取引所 PRO Market """
    tokyo_stock_exchange_standard:IxNonNumericPublic = Field(default=None, description="東京証券取引所 スタンダード")
    """ 東京証券取引所 スタンダード """
    URL:IxNonNumericPublic = Field(default=None, description="URL")
    """ URL """
    way_of_getting_supplemental_material_of_results:IxNonNumericPublic = Field(default=None, description="入手方法等、決算補足説明資料、期中")
    """ 入手方法等、決算補足説明資料、期中 """
    description_of_fact_that_companys_business_comprises_single_segment_ifrs:IxNonNumericPublic = Field(default=None, description="単一セグメントである旨（IFRS）")
    """ 単一セグメントである旨（IFRS） """
    disclosure_of_changes_in_reportable_segments_ifrs_text_block:IxNonNumericPublic = Field(default=None, description="報告セグメントの変更に関する事項（IFRS） [テキストブロック]")
    """ 報告セグメントの変更に関する事項（IFRS） [テキストブロック] """
    information_about_geographical_areas_ifrs_text_block:IxNonNumericPublic = Field(default=None, description="地域に関する情報（IFRS） [テキストブロック]")
    """ 地域に関する情報（IFRS） [テキストブロック] """
    information_about_products_and_services_ifrs_text_block:IxNonNumericPublic = Field(default=None, description="製品及びサービスに関する情報（IFRS） [テキストブロック]")
    """ 製品及びサービスに関する情報（IFRS） [テキストブロック] """
    notes_segment_information_condensed_quarterly_consolidated_financial_statements_ifrs_text_block:IxNonNumericPublic = Field(default=None, description="注記事項－セグメント情報、要約四半期連結財務諸表（IFRS） [テキストブロック]")
    """ 注記事項－セグメント情報、要約四半期連結財務諸表（IFRS） [テキストブロック] """


class edjp(SQLModel):
    type: str = Field(default="edjp", description="型タイプ")
    """ 型タイプ """
    balance_sheet_text_block:IxNonNumericPublic = Field(default=None, description="貸借対照表 [テキストブロック]")
    """ 貸借対照表 [テキストブロック] """
    accounting_standards_dei:IxNonNumericPublic = Field(default=None, description="会計基準、DEI")
    """ 会計基準、DEI """
    amendment_flag_dei:IxNonNumericPublic = Field(default=None, description="訂正の有無、DEI")
    """ 訂正の有無、DEI """
    cabinet_office_ordinance_dei:IxNonNumericPublic = Field(default=None, description="府令、DEI")
    """ 府令、DEI """
    comparative_period_end_date_dei:IxNonNumericPublic = Field(default=None, description="比較対象会計期間終了日、DEI")
    """ 比較対象会計期間終了日、DEI """
    current_fiscal_year_end_date_dei:IxNonNumericPublic = Field(default=None, description="当事業年度終了日、DEI")
    """ 当事業年度終了日、DEI """
    current_fiscal_year_start_date_dei:IxNonNumericPublic = Field(default=None, description="当事業年度開始日、DEI")
    """ 当事業年度開始日、DEI """
    current_period_end_date_dei:IxNonNumericPublic = Field(default=None, description="当会計期間終了日、DEI")
    """ 当会計期間終了日、DEI """
    document_type_dei:IxNonNumericPublic = Field(default=None, description="様式、DEI")
    """ 様式、DEI """
    edinet_code_dei:IxNonNumericPublic = Field(default=None, description="EDINETコード、DEI")
    """ EDINETコード、DEI """
    end_date_of_quarterly_or_semi_annual_period_of_next_fiscal_year_dei:IxNonNumericPublic = Field(default=None, description="次の四半期又は中間期の会計期間終了日、DEI")
    """ 次の四半期又は中間期の会計期間終了日、DEI """
    filer_name_in_english_dei:IxNonNumericPublic = Field(default=None, description="提出者名（英語表記）、DEI")
    """ 提出者名（英語表記）、DEI """
    filer_name_in_japanese_dei:IxNonNumericPublic = Field(default=None, description="提出者名（日本語表記）、DEI")
    """ 提出者名（日本語表記）、DEI """
    fund_code_dei:IxNonNumericPublic = Field(default=None, description="ファンドコード、DEI")
    """ ファンドコード、DEI """
    fund_name_in_english_dei:IxNonNumericPublic = Field(default=None, description="ファンド名称（英語表記）、DEI")
    """ ファンド名称（英語表記）、DEI """
    fund_name_in_japanese_dei:IxNonNumericPublic = Field(default=None, description="ファンド名称（日本語表記）、DEI")
    """ ファンド名称（日本語表記）、DEI """
    identification_of_document_subject_to_amendment_dei:IxNonNumericPublic = Field(default=None, description="訂正対象書類の書類管理番号、DEI")
    """ 訂正対象書類の書類管理番号、DEI """
    industry_code_when_consolidated_financial_statements_are_prepared_in_accordance_with_industry_specific_regulations_dei:IxNonNumericPublic = Field(default=None, description="別記事業（連結）、DEI")
    """ 別記事業（連結）、DEI """
    industry_code_when_financial_statements_are_prepared_in_accordance_with_industry_specific_regulations_dei:IxNonNumericPublic = Field(default=None, description="別記事業（個別）、DEI")
    """ 別記事業（個別）、DEI """
    next_fiscal_year_start_date_dei:IxNonNumericPublic = Field(default=None, description="次の事業年度開始日、DEI")
    """ 次の事業年度開始日、DEI """
    previous_fiscal_year_end_date_dei:IxNonNumericPublic = Field(default=None, description="前事業年度終了日、DEI")
    """ 前事業年度終了日、DEI """
    previous_fiscal_year_start_date_dei:IxNonNumericPublic = Field(default=None, description="前事業年度開始日、DEI")
    """ 前事業年度開始日、DEI """
    report_amendment_flag_dei:IxNonNumericPublic = Field(default=None, description="記載事項訂正のフラグ、DEI")
    """ 記載事項訂正のフラグ、DEI """
    security_code_dei:IxNonNumericPublic = Field(default=None, description="証券コード、DEI")
    """ 証券コード、DEI """
    type_of_current_period_dei:IxNonNumericPublic = Field(default=None, description="当会計期間の種類、DEI")
    """ 当会計期間の種類、DEI """
    whether_consolidated_financial_statements_are_prepared_dei:IxNonNumericPublic = Field(default=None, description="連結決算の有無、DEI")
    """ 連結決算の有無、DEI """
    xbrl_amendment_flag_dei:IxNonNumericPublic = Field(default=None, description="XBRL訂正のフラグ、DEI")
    """ XBRL訂正のフラグ、DEI """
    consolidated_balance_sheet_text_block:IxNonNumericPublic = Field(default=None, description="連結貸借対照表 [テキストブロック]")
    """ 連結貸借対照表 [テキストブロック] """
    accounting_standards_dei:IxNonNumericPublic = Field(default=None, description="会計基準、DEI")
    """ 会計基準、DEI """
    amendment_flag_dei:IxNonNumericPublic = Field(default=None, description="訂正の有無、DEI")
    """ 訂正の有無、DEI """
    cabinet_office_ordinance_dei:IxNonNumericPublic = Field(default=None, description="府令、DEI")
    """ 府令、DEI """
    comparative_period_end_date_dei:IxNonNumericPublic = Field(default=None, description="比較対象会計期間終了日、DEI")
    """ 比較対象会計期間終了日、DEI """
    current_fiscal_year_end_date_dei:IxNonNumericPublic = Field(default=None, description="当事業年度終了日、DEI")
    """ 当事業年度終了日、DEI """
    current_fiscal_year_start_date_dei:IxNonNumericPublic = Field(default=None, description="当事業年度開始日、DEI")
    """ 当事業年度開始日、DEI """
    current_period_end_date_dei:IxNonNumericPublic = Field(default=None, description="当会計期間終了日、DEI")
    """ 当会計期間終了日、DEI """
    document_type_dei:IxNonNumericPublic = Field(default=None, description="様式、DEI")
    """ 様式、DEI """
    edinet_code_dei:IxNonNumericPublic = Field(default=None, description="EDINETコード、DEI")
    """ EDINETコード、DEI """
    end_date_of_quarterly_or_semi_annual_period_of_next_fiscal_year_dei:IxNonNumericPublic = Field(default=None, description="次の四半期又は中間期の会計期間終了日、DEI")
    """ 次の四半期又は中間期の会計期間終了日、DEI """
    filer_name_in_english_dei:IxNonNumericPublic = Field(default=None, description="提出者名（英語表記）、DEI")
    """ 提出者名（英語表記）、DEI """
    filer_name_in_japanese_dei:IxNonNumericPublic = Field(default=None, description="提出者名（日本語表記）、DEI")
    """ 提出者名（日本語表記）、DEI """
    fund_code_dei:IxNonNumericPublic = Field(default=None, description="ファンドコード、DEI")
    """ ファンドコード、DEI """
    fund_name_in_english_dei:IxNonNumericPublic = Field(default=None, description="ファンド名称（英語表記）、DEI")
    """ ファンド名称（英語表記）、DEI """
    fund_name_in_japanese_dei:IxNonNumericPublic = Field(default=None, description="ファンド名称（日本語表記）、DEI")
    """ ファンド名称（日本語表記）、DEI """
    identification_of_document_subject_to_amendment_dei:IxNonNumericPublic = Field(default=None, description="訂正対象書類の書類管理番号、DEI")
    """ 訂正対象書類の書類管理番号、DEI """
    industry_code_when_consolidated_financial_statements_are_prepared_in_accordance_with_industry_specific_regulations_dei:IxNonNumericPublic = Field(default=None, description="別記事業（連結）、DEI")
    """ 別記事業（連結）、DEI """
    industry_code_when_financial_statements_are_prepared_in_accordance_with_industry_specific_regulations_dei:IxNonNumericPublic = Field(default=None, description="別記事業（個別）、DEI")
    """ 別記事業（個別）、DEI """
    next_fiscal_year_start_date_dei:IxNonNumericPublic = Field(default=None, description="次の事業年度開始日、DEI")
    """ 次の事業年度開始日、DEI """
    previous_fiscal_year_end_date_dei:IxNonNumericPublic = Field(default=None, description="前事業年度終了日、DEI")
    """ 前事業年度終了日、DEI """
    previous_fiscal_year_start_date_dei:IxNonNumericPublic = Field(default=None, description="前事業年度開始日、DEI")
    """ 前事業年度開始日、DEI """
    report_amendment_flag_dei:IxNonNumericPublic = Field(default=None, description="記載事項訂正のフラグ、DEI")
    """ 記載事項訂正のフラグ、DEI """
    security_code_dei:IxNonNumericPublic = Field(default=None, description="証券コード、DEI")
    """ 証券コード、DEI """
    type_of_current_period_dei:IxNonNumericPublic = Field(default=None, description="当会計期間の種類、DEI")
    """ 当会計期間の種類、DEI """
    whether_consolidated_financial_statements_are_prepared_dei:IxNonNumericPublic = Field(default=None, description="連結決算の有無、DEI")
    """ 連結決算の有無、DEI """
    xbrl_amendment_flag_dei:IxNonNumericPublic = Field(default=None, description="XBRL訂正のフラグ、DEI")
    """ XBRL訂正のフラグ、DEI """
    consolidated_statement_of_cash_flows_text_block:IxNonNumericPublic = Field(default=None, description="連結キャッシュ・フロー計算書 [テキストブロック]")
    """ 連結キャッシュ・フロー計算書 [テキストブロック] """
    consolidated_statement_of_changes_in_equity_text_block:IxNonNumericPublic = Field(default=None, description="連結株主資本等変動計算書 [テキストブロック]")
    """ 連結株主資本等変動計算書 [テキストブロック] """
    consolidated_statement_of_comprehensive_income_text_block:IxNonNumericPublic = Field(default=None, description="連結包括利益計算書 [テキストブロック]")
    """ 連結包括利益計算書 [テキストブロック] """
    consolidated_statement_of_income_text_block:IxNonNumericPublic = Field(default=None, description="連結損益計算書 [テキストブロック]")
    """ 連結損益計算書 [テキストブロック] """
    annual_securities_report_filing_date_as_planned:IxNonNumericPublic = Field(default=None, description="有価証券報告書提出予定日")
    """ 有価証券報告書提出予定日 """
    applying_of_specific_accounting_of_the_consolidated_quarterly_financial_statements:IxNonNumericPublic = Field(default=None, description="四半期連結財務諸表の作成に特有の会計処理の適用")
    """ 四半期連結財務諸表の作成に特有の会計処理の適用 """
    applying_of_specific_accounting_of_the_consolidated_semi_annual_financial_statements:IxNonNumericPublic = Field(default=None, description="中間連結財務諸表の作成に特有の会計処理の適用")
    """ 中間連結財務諸表の作成に特有の会計処理の適用 """
    applying_of_specific_accounting_of_the_quarterly_financial_statements:IxNonNumericPublic = Field(default=None, description="四半期財務諸表の作成に特有の会計処理の適用")
    """ 四半期財務諸表の作成に特有の会計処理の適用 """
    applying_of_specific_accounting_of_the_semi_annual_financial_statements:IxNonNumericPublic = Field(default=None, description="中間財務諸表の作成に特有の会計処理の適用")
    """ 中間財務諸表の作成に特有の会計処理の適用 """
    changes_based_on_revisions_of_accounting_standard:IxNonNumericPublic = Field(default=None, description="会計基準等の改正に伴う会計方針の変更")
    """ 会計基準等の改正に伴う会計方針の変更 """
    changes_in_accounting_estimates:IxNonNumericPublic = Field(default=None, description="会計上の見積りの変更")
    """ 会計上の見積りの変更 """
    changes_in_accounting_estimates_interim:IxNonNumericPublic = Field(default=None, description="会計上の見積りの変更、中間期")
    """ 会計上の見積りの変更、中間期 """
    changes_other_than_ones_based_on_revisions_of_accounting_standard:IxNonNumericPublic = Field(default=None, description="会計基準等の改正に伴う変更以外の会計方針の変更")
    """ 会計基準等の改正に伴う変更以外の会計方針の変更 """
    company_name:IxNonNumericPublic = Field(default=None, description="上場会社名")
    """ 上場会社名 """
    convening_briefing_of_annual_results:IxNonNumericPublic = Field(default=None, description="決算説明会開催の有無")
    """ 決算説明会開催の有無 """
    convening_briefing_of_results:IxNonNumericPublic = Field(default=None, description="決算説明会開催の有無、期中")
    """ 決算説明会開催の有無、期中 """
    correction_of_consolidated_financial_forecast_in_this_quarter:IxNonNumericPublic = Field(default=None, description="直近に公表されている業績予想からの修正の有無、連結")
    """ 直近に公表されている業績予想からの修正の有無、連結 """
    correction_of_dividend_forecast_in_this_quarter:IxNonNumericPublic = Field(default=None, description="直近に公表されている配当予想からの修正の有無")
    """ 直近に公表されている配当予想からの修正の有無 """
    correction_of_financial_forecast_in_this_quarter:IxNonNumericPublic = Field(default=None, description="直近に公表されている業績予想からの修正の有無")
    """ 直近に公表されている業績予想からの修正の有無 """
    date_of_general_shareholders_meeting_as_planned:IxNonNumericPublic = Field(default=None, description="定時株主総会開催予定日")
    """ 定時株主総会開催予定日 """
    dividend_payable_date_as_planned:IxNonNumericPublic = Field(default=None, description="配当支払開始予定日")
    """ 配当支払開始予定日 """
    document_name:IxNonNumericPublic = Field(default=None, description="文書名")
    """ 文書名 """
    fasf_member_mark:IxNonNumericPublic = Field(default=None, description="財務会計基準機構会員マーク")
    """ 財務会計基準機構会員マーク """
    filing_date:IxNonNumericPublic = Field(default=None, description="提出日")
    """ 提出日 """
    fiscal_year_end:IxNonNumericPublic = Field(default=None, description="決算期")
    """ 決算期 """
    fukuoka_stock_exchange:IxNonNumericPublic = Field(default=None, description="福岡証券取引所")
    """ 福岡証券取引所 """
    fukuoka_stock_exchange_established:IxNonNumericPublic = Field(default=None, description="福岡証券取引所 既存市場")
    """ 福岡証券取引所 既存市場 """
    fukuoka_stock_exchange_others:IxNonNumericPublic = Field(default=None, description="福岡証券取引所 その他")
    """ 福岡証券取引所 その他 """
    fukuoka_stock_exchange_q_board:IxNonNumericPublic = Field(default=None, description="福岡証券取引所 Q-Board")
    """ 福岡証券取引所 Q-Board """
    general_business:IxNonNumericPublic = Field(default=None, description="一般事業会社")
    """ 一般事業会社 """
    japan_securities_dealers_association:IxNonNumericPublic = Field(default=None, description="フェニックス")
    """ フェニックス """
    japan_securities_dealers_association_green_sheet:IxNonNumericPublic = Field(default=None, description="日本証券業協会 フェニックス")
    """ 日本証券業協会 フェニックス """
    nagoya_stock_exchange:IxNonNumericPublic = Field(default=None, description="名古屋証券取引所")
    """ 名古屋証券取引所 """
    nagoya_stock_exchange1st_section:IxNonNumericPublic = Field(default=None, description="名古屋証券取引所 プレミア")
    """ 名古屋証券取引所 プレミア """
    nagoya_stock_exchange2nd_section:IxNonNumericPublic = Field(default=None, description="名古屋証券取引所 メイン")
    """ 名古屋証券取引所 メイン """
    nagoya_stock_exchange_centrex:IxNonNumericPublic = Field(default=None, description="名古屋証券取引所 ネクスト")
    """ 名古屋証券取引所 ネクスト """
    nagoya_stock_exchange_others:IxNonNumericPublic = Field(default=None, description="名古屋証券取引所 その他")
    """ 名古屋証券取引所 その他 """
    name_inquiries:IxNonNumericPublic = Field(default=None, description="氏名、問合せ先責任者")
    """ 氏名、問合せ先責任者 """
    name_of_subsidiaries_excluded_from_consolidation:IxNonNumericPublic = Field(default=None, description="社名、除外")
    """ 社名、除外 """
    name_of_subsidiaries_newly_consolidated:IxNonNumericPublic = Field(default=None, description="社名、新規")
    """ 社名、新規 """
    name_representative:IxNonNumericPublic = Field(default=None, description="氏名、代表者")
    """ 氏名、代表者 """
    notes_for_using_forecasted_information_and_others:IxNonNumericPublic = Field(default=None, description="業績予想の適切な利用に関する説明、その他特記事項")
    """ 業績予想の適切な利用に関する説明、その他特記事項 """
    note_to_applying_of_specific_accounting_of_the_consolidated_quarterly_financial_statements:IxNonNumericPublic = Field(default=None, description="四半期連結財務諸表の作成に特有の会計処理の適用に関する注記")
    """ 四半期連結財務諸表の作成に特有の会計処理の適用に関する注記 """
    note_to_applying_of_specific_accounting_of_the_consolidated_semi_annual_financial_statements:IxNonNumericPublic = Field(default=None, description="中間連結財務諸表の作成に特有の会計処理の適用に関する注記")
    """ 中間連結財務諸表の作成に特有の会計処理の適用に関する注記 """
    note_to_applying_of_specific_accounting_of_the_quarterly_financial_statements:IxNonNumericPublic = Field(default=None, description="四半期財務諸表の作成に特有の会計処理の適用に関する注記")
    """ 四半期財務諸表の作成に特有の会計処理の適用に関する注記 """
    note_to_applying_of_specific_accounting_of_the_semi_annual_financial_statements:IxNonNumericPublic = Field(default=None, description="中間財務諸表の作成に特有の会計処理の適用に関する注記")
    """ 中間財務諸表の作成に特有の会計処理の適用に関する注記 """
    note_to_cash_flows:IxNonNumericPublic = Field(default=None, description="キャッシュ・フローの状況に関する注記")
    """ キャッシュ・フローの状況に関する注記 """
    note_to_changes_in_accounting_policies_accounting_estimates_and_retrospective_restatement_interim_consolidated:IxNonNumericPublic = Field(default=None, description="会計方針の変更・会計上の見積りの変更・修正再表示に関する注記、中間期")
    """ 会計方針の変更・会計上の見積りの変更・修正再表示に関する注記、中間期 """
    note_to_changes_in_accounting_policies_accounting_estimates_and_retrospective_restatement_quarterly_consolidated:IxNonNumericPublic = Field(default=None, description="会計方針の変更・会計上の見積りの変更・修正再表示に関する注記、四半期")
    """ 会計方針の変更・会計上の見積りの変更・修正再表示に関する注記、四半期 """
    note_to_changes_in_accounting_policies_and_accounting_estimates_retrospective_restatement:IxNonNumericPublic = Field(default=None, description="会計方針の変更・会計上の見積りの変更・修正再表示に関する注記")
    """ 会計方針の変更・会計上の見積りの変更・修正再表示に関する注記 """
    note_to_consolidated_financial_results:IxNonNumericPublic = Field(default=None, description="連結業績に関する注記")
    """ 連結業績に関する注記 """
    note_to_dividends:IxNonNumericPublic = Field(default=None, description="配当の状況に関する注記")
    """ 配当の状況に関する注記 """
    note_to_financial_positions:IxNonNumericPublic = Field(default=None, description="財政状態に関する注記")
    """ 財政状態に関する注記 """
    note_to_financial_results:IxNonNumericPublic = Field(default=None, description="業績に関する注記")
    """ 業績に関する注記 """
    note_to_forecasts:IxNonNumericPublic = Field(default=None, description="業績予想に関する事項、注記")
    """ 業績予想に関する事項、注記 """
    note_to_fraction_processing_method:IxNonNumericPublic = Field(default=None, description="端数処理方法に関する注記")
    """ 端数処理方法に関する注記 """
    note_to_number_of_issued_and_outstanding_shares_common_stock:IxNonNumericPublic = Field(default=None, description="発行済株式数（普通株式）に関する注記")
    """ 発行済株式数（普通株式）に関する注記 """
    note_to_operating_results:IxNonNumericPublic = Field(default=None, description="経営成績に関する注記")
    """ 経営成績に関する注記 """
    note_to_significant_changes_in_the_scope_of_consolidation_during_the_period:IxNonNumericPublic = Field(default=None, description="期中における連結範囲の重要な変更に関する注記")
    """ 期中における連結範囲の重要な変更に関する注記 """
    preamble_to_forecasts:IxNonNumericPublic = Field(default=None, description="業績予想に関する事項")
    """ 業績予想に関する事項 """
    retrospective_restatement:IxNonNumericPublic = Field(default=None, description="修正再表示")
    """ 修正再表示 """
    retrospective_restatement_interim:IxNonNumericPublic = Field(default=None, description="修正再表示、中間期")
    """ 修正再表示、中間期 """
    review_of_attached_consolidated_quarterly_financial_statements_by_a_certified_public_accountant_or_an_audit_firm:IxNonNumericPublic = Field(default=None, description="添付される四半期連結財務諸表に対する公認会計士又は監査法人によるレビュー")
    """ 添付される四半期連結財務諸表に対する公認会計士又は監査法人によるレビュー """
    review_of_attached_quarterly_financial_statements_by_a_certified_public_accountant_or_an_audit_firm:IxNonNumericPublic = Field(default=None, description="添付される四半期財務諸表に対する公認会計士又は監査法人によるレビュー")
    """ 添付される四半期財務諸表に対する公認会計士又は監査法人によるレビュー """
    sapporo_stock_exchange:IxNonNumericPublic = Field(default=None, description="札幌証券取引所")
    """ 札幌証券取引所 """
    sapporo_stock_exchange_ambitious:IxNonNumericPublic = Field(default=None, description="札幌証券取引所 アンビシャス")
    """ 札幌証券取引所 アンビシャス """
    sapporo_stock_exchange_established:IxNonNumericPublic = Field(default=None, description="札幌証券取引所 既存市場")
    """ 札幌証券取引所 既存市場 """
    sapporo_stock_exchange_others:IxNonNumericPublic = Field(default=None, description="札幌証券取引所 その他")
    """ 札幌証券取引所 その他 """
    securities_code:IxNonNumericPublic = Field(default=None, description="コード番号")
    """ コード番号 """
    semi_annual_statement_filing_date_as_planned:IxNonNumericPublic = Field(default=None, description="半期報告書提出予定日")
    """ 半期報告書提出予定日 """
    setting_of_specific_transaction_account_bk:IxNonNumericPublic = Field(default=None, description="特定取引勘定設置の有無、銀行")
    """ 特定取引勘定設置の有無、銀行 """
    significant_changes_in_the_scope_of_consolidation_during_the_period:IxNonNumericPublic = Field(default=None, description="期中における連結範囲の重要な変更")
    """ 期中における連結範囲の重要な変更 """
    specific_business:IxNonNumericPublic = Field(default=None, description="特定事業会社")
    """ 特定事業会社 """
    supplemental_material_of_annual_results:IxNonNumericPublic = Field(default=None, description="決算補足説明資料作成の有無")
    """ 決算補足説明資料作成の有無 """
    supplemental_material_of_results:IxNonNumericPublic = Field(default=None, description="決算補足説明資料作成の有無、期中")
    """ 決算補足説明資料作成の有無、期中 """
    target_audience_briefing_of_annual_results:IxNonNumericPublic = Field(default=None, description="対象者、決算説明会")
    """ 対象者、決算説明会 """
    target_for_briefing_of_results:IxNonNumericPublic = Field(default=None, description="決算説明会の対象者")
    """ 決算説明会の対象者 """
    tel:IxNonNumericPublic = Field(default=None, description="TEL")
    """ TEL """
    title_for_forecasts:IxNonNumericPublic = Field(default=None, description="業績予想タイトル名称")
    """ 業績予想タイトル名称 """
    title_inquiries:IxNonNumericPublic = Field(default=None, description="役職名、問合せ先責任者")
    """ 役職名、問合せ先責任者 """
    title_representative:IxNonNumericPublic = Field(default=None, description="役職名、代表者")
    """ 役職名、代表者 """
    tokyo_stock_exchange:IxNonNumericPublic = Field(default=None, description="東京証券取引所")
    """ 東京証券取引所 """
    tokyo_stock_exchange1st_section:IxNonNumericPublic = Field(default=None, description="東京証券取引所 第一部")
    """ 東京証券取引所 第一部 """
    tokyo_stock_exchange2nd_section:IxNonNumericPublic = Field(default=None, description="東京証券取引所 第二部")
    """ 東京証券取引所 第二部 """
    tokyo_stock_exchange_growth:IxNonNumericPublic = Field(default=None, description="東京証券取引所 グロース")
    """ 東京証券取引所 グロース """
    tokyo_stock_exchange_jasdaq:IxNonNumericPublic = Field(default=None, description="東京証券取引所 JASDAQ")
    """ 東京証券取引所 JASDAQ """
    tokyo_stock_exchange_mothers:IxNonNumericPublic = Field(default=None, description="東京証券取引所 マザーズ")
    """ 東京証券取引所 マザーズ """
    tokyo_stock_exchange_others:IxNonNumericPublic = Field(default=None, description="東京証券取引所 その他")
    """ 東京証券取引所 その他 """
    tokyo_stock_exchange_prime:IxNonNumericPublic = Field(default=None, description="東京証券取引所 プライム")
    """ 東京証券取引所 プライム """
    tokyo_stock_exchange_pro_market:IxNonNumericPublic = Field(default=None, description="東京証券取引所 PRO Market")
    """ 東京証券取引所 PRO Market """
    tokyo_stock_exchange_standard:IxNonNumericPublic = Field(default=None, description="東京証券取引所 スタンダード")
    """ 東京証券取引所 スタンダード """
    URL:IxNonNumericPublic = Field(default=None, description="URL")
    """ URL """
    way_of_getting_supplemental_material_of_annual_results:IxNonNumericPublic = Field(default=None, description="入手方法等、決算補足説明資料")
    """ 入手方法等、決算補足説明資料 """
    way_of_getting_supplemental_material_of_results:IxNonNumericPublic = Field(default=None, description="入手方法等、決算補足説明資料、期中")
    """ 入手方法等、決算補足説明資料、期中 """
    major_components_of_selling_general_and_administrative_expenses_text_block:IxNonNumericPublic = Field(default=None, description="主要な販売費及び一般管理費 [テキストブロック]")
    """ 主要な販売費及び一般管理費 [テキストブロック] """
    notes_regarding_guarantee_obligations_text_block:IxNonNumericPublic = Field(default=None, description="保証債務の注記 [テキストブロック]")
    """ 保証債務の注記 [テキストブロック] """
    notes_regarding_impairment_loss_text_block:IxNonNumericPublic = Field(default=None, description="減損損失に関する注記 [テキストブロック]")
    """ 減損損失に関する注記 [テキストブロック] """
    notes_regarding_promissory_notes_due_on_balance_sheet_date_text_block:IxNonNumericPublic = Field(default=None, description="期末日満期手形の会計処理 [テキストブロック]")
    """ 期末日満期手形の会計処理 [テキストブロック] """
    notes_regarding_impairment_loss_text_block:IxNonNumericPublic = Field(default=None, description="減損損失に関する注記 [テキストブロック]")
    """ 減損損失に関する注記 [テキストブロック] """
    description_of_factors_which_led_to_recognition_of_gain_on_bargain_purchase_text_block:IxNonNumericPublic = Field(default=None, description="報告セグメントごとの負ののれん発生益を認識する要因となった事象の概要 [テキストブロック]")
    """ 報告セグメントごとの負ののれん発生益を認識する要因となった事象の概要 [テキストブロック] """
    description_of_reportable_segments_text_block:IxNonNumericPublic = Field(default=None, description="報告セグメントの概要 [テキストブロック]")
    """ 報告セグメントの概要 [テキストブロック] """
    explanation_of_measurements_of_sales_profit_loss_asset_liability_and_other_items_for_each_reportable_segment_text_block:IxNonNumericPublic = Field(default=None, description="報告セグメントごとの売上高、利益又は損失、資産、負債その他の項目の金額の算定方法 [テキストブロック]")
    """ 報告セグメントごとの売上高、利益又は損失、資産、負債その他の項目の金額の算定方法 [テキストブロック] """
    footnotes_regarding_segment_information_table_text_block:IxNonNumericPublic = Field(default=None, description="セグメント表の脚注 [テキストブロック]")
    """ セグメント表の脚注 [テキストブロック] """
    information_for_each_of_main_customers_text_block:IxNonNumericPublic = Field(default=None, description="主要な顧客ごとの情報 [テキストブロック]")
    """ 主要な顧客ごとの情報 [テキストブロック] """
    information_for_each_product_or_service_text_block:IxNonNumericPublic = Field(default=None, description="製品及びサービスごとの情報 [テキストブロック]")
    """ 製品及びサービスごとの情報 [テキストブロック] """
    notes_segment_information_etc_consolidated_financial_statements_text_block:IxNonNumericPublic = Field(default=None, description="セグメント情報等、連結財務諸表 [テキストブロック]")
    """ セグメント情報等、連結財務諸表 [テキストブロック] """
    property_plant_and_equipment_information_for_each_region_text_block:IxNonNumericPublic = Field(default=None, description="有形固定資産、地域ごとの情報 [テキストブロック]")
    """ 有形固定資産、地域ごとの情報 [テキストブロック] """
    revenues_from_external_customers_information_for_each_region_text_block:IxNonNumericPublic = Field(default=None, description="売上高、地域ごとの情報 [テキストブロック]")
    """ 売上高、地域ごとの情報 [テキストブロック] """
    description_of_fact_that_companys_business_comprises_single_segment:IxNonNumericPublic = Field(default=None, description="単一セグメントである旨")
    """ 単一セグメントである旨 """
    notes_segment_information_etc_financial_statements_text_block:IxNonNumericPublic = Field(default=None, description="セグメント情報等、財務諸表 [テキストブロック]")
    """ セグメント情報等、財務諸表 [テキストブロック] """
    description_of_fact_that_companys_business_comprises_single_segment:IxNonNumericPublic = Field(default=None, description="単一セグメントである旨")
    """ 単一セグメントである旨 """
    description_of_nature_of_differences_between_profit_loss_of_reportable_segments_total_and_quarterly_financial_statements_text_block:IxNonNumericPublic = Field(default=None, description="報告セグメントごとの利益又は損失の金額の合計額と四半期損益計算書計上額との差額及び当該差額の主な内容（差異調整に関する事項） [テキストブロック]")
    """ 報告セグメントごとの利益又は損失の金額の合計額と四半期損益計算書計上額との差額及び当該差額の主な内容（差異調整に関する事項） [テキストブロック] """
    disclosure_of_changes_etc_in_reportable_segments_text_block:IxNonNumericPublic = Field(default=None, description="報告セグメントの変更等に関する事項 [テキストブロック]")
    """ 報告セグメントの変更等に関する事項 [テキストブロック] """
    footnotes_regarding_segment_information_table_text_block:IxNonNumericPublic = Field(default=None, description="セグメント表の脚注 [テキストブロック]")
    """ セグメント表の脚注 [テキストブロック] """
    information_about_assets_for_each_reportable_segment_text_block:IxNonNumericPublic = Field(default=None, description="報告セグメントごとの資産に関する情報 [テキストブロック]")
    """ 報告セグメントごとの資産に関する情報 [テキストブロック] """
    information_about_impairment_loss_of_non_current_assets_or_goodwill_etc_for_each_reportable_segment_text_block:IxNonNumericPublic = Field(default=None, description="報告セグメントごとの固定資産の減損損失又はのれん等に関する情報 [テキストブロック]")
    """ 報告セグメントごとの固定資産の減損損失又はのれん等に関する情報 [テキストブロック] """
    notes_segment_information_etc_quarterly_consolidated_financial_statements_text_block:IxNonNumericPublic = Field(default=None, description="セグメント情報等、四半期連結財務諸表 [テキストブロック]")
    """ セグメント情報等、四半期連結財務諸表 [テキストブロック] """
    revenues_from_external_customers_information_for_each_region_text_block:IxNonNumericPublic = Field(default=None, description="売上高、地域ごとの情報 [テキストブロック]")
    """ 売上高、地域ごとの情報 [テキストブロック] """
    description_of_fact_that_companys_business_comprises_single_segment:IxNonNumericPublic = Field(default=None, description="単一セグメントである旨")
    """ 単一セグメントである旨 """
    footnotes_regarding_segment_information_table_text_block:IxNonNumericPublic = Field(default=None, description="セグメント表の脚注 [テキストブロック]")
    """ セグメント表の脚注 [テキストブロック] """
    information_about_impairment_loss_of_non_current_assets_or_goodwill_etc_for_each_reportable_segment_text_block:IxNonNumericPublic = Field(default=None, description="報告セグメントごとの固定資産の減損損失又はのれん等に関する情報 [テキストブロック]")
    """ 報告セグメントごとの固定資産の減損損失又はのれん等に関する情報 [テキストブロック] """
    notes_segment_information_etc_quarterly_financial_statements_text_block:IxNonNumericPublic = Field(default=None, description="セグメント情報等、四半期財務諸表 [テキストブロック]")
    """ セグメント情報等、四半期財務諸表 [テキストブロック] """
    description_of_reportable_segments_text_block:IxNonNumericPublic = Field(default=None, description="報告セグメントの概要 [テキストブロック]")
    """ 報告セグメントの概要 [テキストブロック] """
    explanation_of_measurements_of_sales_profit_loss_asset_liability_and_other_items_for_each_reportable_segment_text_block:IxNonNumericPublic = Field(default=None, description="報告セグメントごとの売上高、利益又は損失、資産、負債その他の項目の金額の算定方法 [テキストブロック]")
    """ 報告セグメントごとの売上高、利益又は損失、資産、負債その他の項目の金額の算定方法 [テキストブロック] """
    footnotes_regarding_segment_information_table_text_block:IxNonNumericPublic = Field(default=None, description="セグメント表の脚注 [テキストブロック]")
    """ セグメント表の脚注 [テキストブロック] """
    information_for_each_of_main_customers_text_block:IxNonNumericPublic = Field(default=None, description="主要な顧客ごとの情報 [テキストブロック]")
    """ 主要な顧客ごとの情報 [テキストブロック] """
    information_for_each_product_or_service_text_block:IxNonNumericPublic = Field(default=None, description="製品及びサービスごとの情報 [テキストブロック]")
    """ 製品及びサービスごとの情報 [テキストブロック] """
    notes_segment_information_etc_semi_annual_consolidated_financial_statements_text_block:IxNonNumericPublic = Field(default=None, description="セグメント情報等、中間連結財務諸表 [テキストブロック]")
    """ セグメント情報等、中間連結財務諸表 [テキストブロック] """
    property_plant_and_equipment_information_for_each_region_text_block:IxNonNumericPublic = Field(default=None, description="有形固定資産、地域ごとの情報 [テキストブロック]")
    """ 有形固定資産、地域ごとの情報 [テキストブロック] """
    revenues_from_external_customers_information_for_each_region_text_block:IxNonNumericPublic = Field(default=None, description="売上高、地域ごとの情報 [テキストブロック]")
    """ 売上高、地域ごとの情報 [テキストブロック] """
    quarterly_balance_sheet_text_block:IxNonNumericPublic = Field(default=None, description="四半期貸借対照表 [テキストブロック]")
    """ 四半期貸借対照表 [テキストブロック] """
    accounting_standards_dei:IxNonNumericPublic = Field(default=None, description="会計基準、DEI")
    """ 会計基準、DEI """
    amendment_flag_dei:IxNonNumericPublic = Field(default=None, description="訂正の有無、DEI")
    """ 訂正の有無、DEI """
    cabinet_office_ordinance_dei:IxNonNumericPublic = Field(default=None, description="府令、DEI")
    """ 府令、DEI """
    comparative_period_end_date_dei:IxNonNumericPublic = Field(default=None, description="比較対象会計期間終了日、DEI")
    """ 比較対象会計期間終了日、DEI """
    current_fiscal_year_end_date_dei:IxNonNumericPublic = Field(default=None, description="当事業年度終了日、DEI")
    """ 当事業年度終了日、DEI """
    current_fiscal_year_start_date_dei:IxNonNumericPublic = Field(default=None, description="当事業年度開始日、DEI")
    """ 当事業年度開始日、DEI """
    current_period_end_date_dei:IxNonNumericPublic = Field(default=None, description="当会計期間終了日、DEI")
    """ 当会計期間終了日、DEI """
    document_type_dei:IxNonNumericPublic = Field(default=None, description="様式、DEI")
    """ 様式、DEI """
    edinet_code_dei:IxNonNumericPublic = Field(default=None, description="EDINETコード、DEI")
    """ EDINETコード、DEI """
    end_date_of_quarterly_or_semi_annual_period_of_next_fiscal_year_dei:IxNonNumericPublic = Field(default=None, description="次の四半期又は中間期の会計期間終了日、DEI")
    """ 次の四半期又は中間期の会計期間終了日、DEI """
    filer_name_in_english_dei:IxNonNumericPublic = Field(default=None, description="提出者名（英語表記）、DEI")
    """ 提出者名（英語表記）、DEI """
    filer_name_in_japanese_dei:IxNonNumericPublic = Field(default=None, description="提出者名（日本語表記）、DEI")
    """ 提出者名（日本語表記）、DEI """
    fund_code_dei:IxNonNumericPublic = Field(default=None, description="ファンドコード、DEI")
    """ ファンドコード、DEI """
    fund_name_in_english_dei:IxNonNumericPublic = Field(default=None, description="ファンド名称（英語表記）、DEI")
    """ ファンド名称（英語表記）、DEI """
    fund_name_in_japanese_dei:IxNonNumericPublic = Field(default=None, description="ファンド名称（日本語表記）、DEI")
    """ ファンド名称（日本語表記）、DEI """
    identification_of_document_subject_to_amendment_dei:IxNonNumericPublic = Field(default=None, description="訂正対象書類の書類管理番号、DEI")
    """ 訂正対象書類の書類管理番号、DEI """
    industry_code_when_consolidated_financial_statements_are_prepared_in_accordance_with_industry_specific_regulations_dei:IxNonNumericPublic = Field(default=None, description="別記事業（連結）、DEI")
    """ 別記事業（連結）、DEI """
    industry_code_when_financial_statements_are_prepared_in_accordance_with_industry_specific_regulations_dei:IxNonNumericPublic = Field(default=None, description="別記事業（個別）、DEI")
    """ 別記事業（個別）、DEI """
    next_fiscal_year_start_date_dei:IxNonNumericPublic = Field(default=None, description="次の事業年度開始日、DEI")
    """ 次の事業年度開始日、DEI """
    previous_fiscal_year_end_date_dei:IxNonNumericPublic = Field(default=None, description="前事業年度終了日、DEI")
    """ 前事業年度終了日、DEI """
    previous_fiscal_year_start_date_dei:IxNonNumericPublic = Field(default=None, description="前事業年度開始日、DEI")
    """ 前事業年度開始日、DEI """
    report_amendment_flag_dei:IxNonNumericPublic = Field(default=None, description="記載事項訂正のフラグ、DEI")
    """ 記載事項訂正のフラグ、DEI """
    security_code_dei:IxNonNumericPublic = Field(default=None, description="証券コード、DEI")
    """ 証券コード、DEI """
    type_of_current_period_dei:IxNonNumericPublic = Field(default=None, description="当会計期間の種類、DEI")
    """ 当会計期間の種類、DEI """
    whether_consolidated_financial_statements_are_prepared_dei:IxNonNumericPublic = Field(default=None, description="連結決算の有無、DEI")
    """ 連結決算の有無、DEI """
    xbrl_amendment_flag_dei:IxNonNumericPublic = Field(default=None, description="XBRL訂正のフラグ、DEI")
    """ XBRL訂正のフラグ、DEI """
    quarterly_consolidated_balance_sheet_text_block:IxNonNumericPublic = Field(default=None, description="四半期連結貸借対照表 [テキストブロック]")
    """ 四半期連結貸借対照表 [テキストブロック] """
    accounting_standards_dei:IxNonNumericPublic = Field(default=None, description="会計基準、DEI")
    """ 会計基準、DEI """
    amendment_flag_dei:IxNonNumericPublic = Field(default=None, description="訂正の有無、DEI")
    """ 訂正の有無、DEI """
    cabinet_office_ordinance_dei:IxNonNumericPublic = Field(default=None, description="府令、DEI")
    """ 府令、DEI """
    comparative_period_end_date_dei:IxNonNumericPublic = Field(default=None, description="比較対象会計期間終了日、DEI")
    """ 比較対象会計期間終了日、DEI """
    current_fiscal_year_end_date_dei:IxNonNumericPublic = Field(default=None, description="当事業年度終了日、DEI")
    """ 当事業年度終了日、DEI """
    current_fiscal_year_start_date_dei:IxNonNumericPublic = Field(default=None, description="当事業年度開始日、DEI")
    """ 当事業年度開始日、DEI """
    current_period_end_date_dei:IxNonNumericPublic = Field(default=None, description="当会計期間終了日、DEI")
    """ 当会計期間終了日、DEI """
    document_type_dei:IxNonNumericPublic = Field(default=None, description="様式、DEI")
    """ 様式、DEI """
    edinet_code_dei:IxNonNumericPublic = Field(default=None, description="EDINETコード、DEI")
    """ EDINETコード、DEI """
    end_date_of_quarterly_or_semi_annual_period_of_next_fiscal_year_dei:IxNonNumericPublic = Field(default=None, description="次の四半期又は中間期の会計期間終了日、DEI")
    """ 次の四半期又は中間期の会計期間終了日、DEI """
    filer_name_in_english_dei:IxNonNumericPublic = Field(default=None, description="提出者名（英語表記）、DEI")
    """ 提出者名（英語表記）、DEI """
    filer_name_in_japanese_dei:IxNonNumericPublic = Field(default=None, description="提出者名（日本語表記）、DEI")
    """ 提出者名（日本語表記）、DEI """
    fund_code_dei:IxNonNumericPublic = Field(default=None, description="ファンドコード、DEI")
    """ ファンドコード、DEI """
    fund_name_in_english_dei:IxNonNumericPublic = Field(default=None, description="ファンド名称（英語表記）、DEI")
    """ ファンド名称（英語表記）、DEI """
    fund_name_in_japanese_dei:IxNonNumericPublic = Field(default=None, description="ファンド名称（日本語表記）、DEI")
    """ ファンド名称（日本語表記）、DEI """
    identification_of_document_subject_to_amendment_dei:IxNonNumericPublic = Field(default=None, description="訂正対象書類の書類管理番号、DEI")
    """ 訂正対象書類の書類管理番号、DEI """
    industry_code_when_consolidated_financial_statements_are_prepared_in_accordance_with_industry_specific_regulations_dei:IxNonNumericPublic = Field(default=None, description="別記事業（連結）、DEI")
    """ 別記事業（連結）、DEI """
    industry_code_when_financial_statements_are_prepared_in_accordance_with_industry_specific_regulations_dei:IxNonNumericPublic = Field(default=None, description="別記事業（個別）、DEI")
    """ 別記事業（個別）、DEI """
    next_fiscal_year_start_date_dei:IxNonNumericPublic = Field(default=None, description="次の事業年度開始日、DEI")
    """ 次の事業年度開始日、DEI """
    previous_fiscal_year_end_date_dei:IxNonNumericPublic = Field(default=None, description="前事業年度終了日、DEI")
    """ 前事業年度終了日、DEI """
    previous_fiscal_year_start_date_dei:IxNonNumericPublic = Field(default=None, description="前事業年度開始日、DEI")
    """ 前事業年度開始日、DEI """
    report_amendment_flag_dei:IxNonNumericPublic = Field(default=None, description="記載事項訂正のフラグ、DEI")
    """ 記載事項訂正のフラグ、DEI """
    security_code_dei:IxNonNumericPublic = Field(default=None, description="証券コード、DEI")
    """ 証券コード、DEI """
    type_of_current_period_dei:IxNonNumericPublic = Field(default=None, description="当会計期間の種類、DEI")
    """ 当会計期間の種類、DEI """
    whether_consolidated_financial_statements_are_prepared_dei:IxNonNumericPublic = Field(default=None, description="連結決算の有無、DEI")
    """ 連結決算の有無、DEI """
    xbrl_amendment_flag_dei:IxNonNumericPublic = Field(default=None, description="XBRL訂正のフラグ、DEI")
    """ XBRL訂正のフラグ、DEI """
    quarterly_consolidated_statement_of_cash_flows_text_block:IxNonNumericPublic = Field(default=None, description="四半期連結キャッシュ・フロー計算書 [テキストブロック]")
    """ 四半期連結キャッシュ・フロー計算書 [テキストブロック] """
    quarterly_statement_of_cash_flows_text_block:IxNonNumericPublic = Field(default=None, description="四半期キャッシュ・フロー計算書 [テキストブロック]")
    """ 四半期キャッシュ・フロー計算書 [テキストブロック] """
    semi_annual_balance_sheet_text_block:IxNonNumericPublic = Field(default=None, description="中間貸借対照表 [テキストブロック]")
    """ 中間貸借対照表 [テキストブロック] """
    semi_annual_consolidated_balance_sheet_text_block:IxNonNumericPublic = Field(default=None, description="中間連結貸借対照表 [テキストブロック]")
    """ 中間連結貸借対照表 [テキストブロック] """
    accounting_standards_dei:IxNonNumericPublic = Field(default=None, description="会計基準、DEI")
    """ 会計基準、DEI """
    amendment_flag_dei:IxNonNumericPublic = Field(default=None, description="訂正の有無、DEI")
    """ 訂正の有無、DEI """
    cabinet_office_ordinance_dei:IxNonNumericPublic = Field(default=None, description="府令、DEI")
    """ 府令、DEI """
    comparative_period_end_date_dei:IxNonNumericPublic = Field(default=None, description="比較対象会計期間終了日、DEI")
    """ 比較対象会計期間終了日、DEI """
    current_fiscal_year_end_date_dei:IxNonNumericPublic = Field(default=None, description="当事業年度終了日、DEI")
    """ 当事業年度終了日、DEI """
    current_fiscal_year_start_date_dei:IxNonNumericPublic = Field(default=None, description="当事業年度開始日、DEI")
    """ 当事業年度開始日、DEI """
    current_period_end_date_dei:IxNonNumericPublic = Field(default=None, description="当会計期間終了日、DEI")
    """ 当会計期間終了日、DEI """
    document_type_dei:IxNonNumericPublic = Field(default=None, description="様式、DEI")
    """ 様式、DEI """
    edinet_code_dei:IxNonNumericPublic = Field(default=None, description="EDINETコード、DEI")
    """ EDINETコード、DEI """
    end_date_of_quarterly_or_semi_annual_period_of_next_fiscal_year_dei:IxNonNumericPublic = Field(default=None, description="次の四半期又は中間期の会計期間終了日、DEI")
    """ 次の四半期又は中間期の会計期間終了日、DEI """
    filer_name_in_english_dei:IxNonNumericPublic = Field(default=None, description="提出者名（英語表記）、DEI")
    """ 提出者名（英語表記）、DEI """
    filer_name_in_japanese_dei:IxNonNumericPublic = Field(default=None, description="提出者名（日本語表記）、DEI")
    """ 提出者名（日本語表記）、DEI """
    fund_code_dei:IxNonNumericPublic = Field(default=None, description="ファンドコード、DEI")
    """ ファンドコード、DEI """
    fund_name_in_english_dei:IxNonNumericPublic = Field(default=None, description="ファンド名称（英語表記）、DEI")
    """ ファンド名称（英語表記）、DEI """
    fund_name_in_japanese_dei:IxNonNumericPublic = Field(default=None, description="ファンド名称（日本語表記）、DEI")
    """ ファンド名称（日本語表記）、DEI """
    identification_of_document_subject_to_amendment_dei:IxNonNumericPublic = Field(default=None, description="訂正対象書類の書類管理番号、DEI")
    """ 訂正対象書類の書類管理番号、DEI """
    industry_code_when_consolidated_financial_statements_are_prepared_in_accordance_with_industry_specific_regulations_dei:IxNonNumericPublic = Field(default=None, description="別記事業（連結）、DEI")
    """ 別記事業（連結）、DEI """
    industry_code_when_financial_statements_are_prepared_in_accordance_with_industry_specific_regulations_dei:IxNonNumericPublic = Field(default=None, description="別記事業（個別）、DEI")
    """ 別記事業（個別）、DEI """
    next_fiscal_year_start_date_dei:IxNonNumericPublic = Field(default=None, description="次の事業年度開始日、DEI")
    """ 次の事業年度開始日、DEI """
    previous_fiscal_year_end_date_dei:IxNonNumericPublic = Field(default=None, description="前事業年度終了日、DEI")
    """ 前事業年度終了日、DEI """
    previous_fiscal_year_start_date_dei:IxNonNumericPublic = Field(default=None, description="前事業年度開始日、DEI")
    """ 前事業年度開始日、DEI """
    report_amendment_flag_dei:IxNonNumericPublic = Field(default=None, description="記載事項訂正のフラグ、DEI")
    """ 記載事項訂正のフラグ、DEI """
    security_code_dei:IxNonNumericPublic = Field(default=None, description="証券コード、DEI")
    """ 証券コード、DEI """
    type_of_current_period_dei:IxNonNumericPublic = Field(default=None, description="当会計期間の種類、DEI")
    """ 当会計期間の種類、DEI """
    whether_consolidated_financial_statements_are_prepared_dei:IxNonNumericPublic = Field(default=None, description="連結決算の有無、DEI")
    """ 連結決算の有無、DEI """
    xbrl_amendment_flag_dei:IxNonNumericPublic = Field(default=None, description="XBRL訂正のフラグ、DEI")
    """ XBRL訂正のフラグ、DEI """
    semi_annual_consolidated_statement_of_changes_in_equity_text_block:IxNonNumericPublic = Field(default=None, description="中間連結株主資本等変動計算書 [テキストブロック]")
    """ 中間連結株主資本等変動計算書 [テキストブロック] """
    semi_annual_consolidated_statement_of_comprehensive_income_text_block:IxNonNumericPublic = Field(default=None, description="中間連結包括利益計算書 [テキストブロック]")
    """ 中間連結包括利益計算書 [テキストブロック] """
    semi_annual_consolidated_statement_of_income_text_block:IxNonNumericPublic = Field(default=None, description="中間連結損益計算書 [テキストブロック]")
    """ 中間連結損益計算書 [テキストブロック] """
    semi_annual_statement_of_changes_in_equity_text_block:IxNonNumericPublic = Field(default=None, description="中間株主資本等変動計算書 [テキストブロック]")
    """ 中間株主資本等変動計算書 [テキストブロック] """
    semi_annual_statement_of_income_text_block:IxNonNumericPublic = Field(default=None, description="中間損益計算書 [テキストブロック]")
    """ 中間損益計算書 [テキストブロック] """
    statement_of_cash_flows_text_block:IxNonNumericPublic = Field(default=None, description="キャッシュ・フロー計算書 [テキストブロック]")
    """ キャッシュ・フロー計算書 [テキストブロック] """
    statement_of_changes_in_equity_text_block:IxNonNumericPublic = Field(default=None, description="株主資本等変動計算書 [テキストブロック]")
    """ 株主資本等変動計算書 [テキストブロック] """
    statement_of_income_text_block:IxNonNumericPublic = Field(default=None, description="損益計算書 [テキストブロック]")
    """ 損益計算書 [テキストブロック] """
    description_of_fact_that_companys_business_comprises_single_segment:IxNonNumericPublic = Field(default=None, description="単一セグメントである旨")
    """ 単一セグメントである旨 """
    major_components_of_selling_general_and_administrative_expenses_text_block:IxNonNumericPublic = Field(default=None, description="主要な販売費及び一般管理費 [テキストブロック]")
    """ 主要な販売費及び一般管理費 [テキストブロック] """
    notes_regarding_guarantee_obligations_text_block:IxNonNumericPublic = Field(default=None, description="保証債務の注記 [テキストブロック]")
    """ 保証債務の注記 [テキストブロック] """
    notes_regarding_shares_and_bonds_etc_of_unconsolidated_subsidiaries_and_associates_text_block:IxNonNumericPublic = Field(default=None, description="非連結子会社及び関連会社の株式及び社債等 [テキストブロック]")
    """ 非連結子会社及び関連会社の株式及び社債等 [テキストブロック] """
    notes_segment_information_etc_quarterly_consolidated_financial_statements_text_block:IxNonNumericPublic = Field(default=None, description="セグメント情報等、四半期連結財務諸表 [テキストブロック]")
    """ セグメント情報等、四半期連結財務諸表 [テキストブロック] """
    year_to_quarter_end_consolidated_statement_of_comprehensive_income_text_block:IxNonNumericPublic = Field(default=None, description="四半期連結累計期間、四半期連結包括利益計算書 [テキストブロック]")
    """ 四半期連結累計期間、四半期連結包括利益計算書 [テキストブロック] """
    year_to_quarter_end_consolidated_statement_of_comprehensive_income_single_statement_text_block:IxNonNumericPublic = Field(default=None, description="四半期連結累計期間、四半期連結損益及び包括利益計算書 [テキストブロック]")
    """ 四半期連結累計期間、四半期連結損益及び包括利益計算書 [テキストブロック] """
    year_to_quarter_end_consolidated_statement_of_income_text_block:IxNonNumericPublic = Field(default=None, description="四半期連結累計期間、四半期連結損益計算書 [テキストブロック]")
    """ 四半期連結累計期間、四半期連結損益計算書 [テキストブロック] """
    year_to_quarter_end_statement_of_income_text_block:IxNonNumericPublic = Field(default=None, description="四半期累計期間、四半期損益計算書 [テキストブロック]")
    """ 四半期累計期間、四半期損益計算書 [テキストブロック] """


class rvfc(SQLModel):
    type: str = Field(default="rvfc", description="型タイプ")
    """ 型タイプ """
    company_name:IxNonNumericPublic = Field(default=None, description="上場会社名")
    """ 上場会社名 """
    document_name:IxNonNumericPublic = Field(default=None, description="文書名")
    """ 文書名 """
    fasf_member_mark:IxNonNumericPublic = Field(default=None, description="財務会計基準機構会員マーク")
    """ 財務会計基準機構会員マーク """
    fiscal_year_end:IxNonNumericPublic = Field(default=None, description="決算期")
    """ 決算期 """
    fukuoka_stock_exchange:IxNonNumericPublic = Field(default=None, description="福岡証券取引所")
    """ 福岡証券取引所 """
    fukuoka_stock_exchange_established:IxNonNumericPublic = Field(default=None, description="福岡証券取引所 既存市場")
    """ 福岡証券取引所 既存市場 """
    fukuoka_stock_exchange_others:IxNonNumericPublic = Field(default=None, description="福岡証券取引所 その他")
    """ 福岡証券取引所 その他 """
    fukuoka_stock_exchange_q_board:IxNonNumericPublic = Field(default=None, description="福岡証券取引所 Q-Board")
    """ 福岡証券取引所 Q-Board """
    general_business:IxNonNumericPublic = Field(default=None, description="一般事業会社")
    """ 一般事業会社 """
    japan_securities_dealers_association:IxNonNumericPublic = Field(default=None, description="フェニックス")
    """ フェニックス """
    japan_securities_dealers_association_green_sheet:IxNonNumericPublic = Field(default=None, description="日本証券業協会 フェニックス")
    """ 日本証券業協会 フェニックス """
    nagoya_stock_exchange:IxNonNumericPublic = Field(default=None, description="名古屋証券取引所")
    """ 名古屋証券取引所 """
    nagoya_stock_exchange1st_section:IxNonNumericPublic = Field(default=None, description="名古屋証券取引所 プレミア")
    """ 名古屋証券取引所 プレミア """
    nagoya_stock_exchange2nd_section:IxNonNumericPublic = Field(default=None, description="名古屋証券取引所 メイン")
    """ 名古屋証券取引所 メイン """
    nagoya_stock_exchange_centrex:IxNonNumericPublic = Field(default=None, description="名古屋証券取引所 ネクスト")
    """ 名古屋証券取引所 ネクスト """
    nagoya_stock_exchange_others:IxNonNumericPublic = Field(default=None, description="名古屋証券取引所 その他")
    """ 名古屋証券取引所 その他 """
    name_inquiries:IxNonNumericPublic = Field(default=None, description="氏名、問合せ先責任者")
    """ 氏名、問合せ先責任者 """
    name_representative:IxNonNumericPublic = Field(default=None, description="氏名、代表者")
    """ 氏名、代表者 """
    note_to_dividends:IxNonNumericPublic = Field(default=None, description="配当の状況に関する注記")
    """ 配当の状況に関する注記 """
    note_to_financial_forecast:IxNonNumericPublic = Field(default=None, description="業績予想の状況に関する注記")
    """ 業績予想の状況に関する注記 """
    notice_of_forecast_correction:IxNonNumericPublic = Field(default=None, description="予想修正に関するお知らせ")
    """ 予想修正に関するお知らせ """
    preamble_to_forecasts:IxNonNumericPublic = Field(default=None, description="業績予想に関する事項")
    """ 業績予想に関する事項 """
    previous_reporting_date_of_dividend_forecast:IxNonNumericPublic = Field(default=None, description="前回予想発表日、配当予想の修正について")
    """ 前回予想発表日、配当予想の修正について """
    reason_for_dividend_forecast_correction:IxNonNumericPublic = Field(default=None, description="配当予想修正の理由")
    """ 配当予想修正の理由 """
    reason_for_forecast_correction:IxNonNumericPublic = Field(default=None, description="業績予想修正の理由")
    """ 業績予想修正の理由 """
    reporting_date_of_financial_forecast_correction:IxNonNumericPublic = Field(default=None, description="予想修正報告日")
    """ 予想修正報告日 """
    sapporo_stock_exchange:IxNonNumericPublic = Field(default=None, description="札幌証券取引所")
    """ 札幌証券取引所 """
    sapporo_stock_exchange_ambitious:IxNonNumericPublic = Field(default=None, description="札幌証券取引所 アンビシャス")
    """ 札幌証券取引所 アンビシャス """
    sapporo_stock_exchange_established:IxNonNumericPublic = Field(default=None, description="札幌証券取引所 既存市場")
    """ 札幌証券取引所 既存市場 """
    sapporo_stock_exchange_others:IxNonNumericPublic = Field(default=None, description="札幌証券取引所 その他")
    """ 札幌証券取引所 その他 """
    securities_code:IxNonNumericPublic = Field(default=None, description="コード番号")
    """ コード番号 """
    specific_business:IxNonNumericPublic = Field(default=None, description="特定事業会社")
    """ 特定事業会社 """
    tel:IxNonNumericPublic = Field(default=None, description="TEL")
    """ TEL """
    title_inquiries:IxNonNumericPublic = Field(default=None, description="役職名、問合せ先責任者")
    """ 役職名、問合せ先責任者 """
    title_representative:IxNonNumericPublic = Field(default=None, description="役職名、代表者")
    """ 役職名、代表者 """
    tokyo_stock_exchange:IxNonNumericPublic = Field(default=None, description="東京証券取引所")
    """ 東京証券取引所 """
    tokyo_stock_exchange_growth:IxNonNumericPublic = Field(default=None, description="東京証券取引所 グロース")
    """ 東京証券取引所 グロース """
    tokyo_stock_exchange_others:IxNonNumericPublic = Field(default=None, description="東京証券取引所 その他")
    """ 東京証券取引所 その他 """
    tokyo_stock_exchange_prime:IxNonNumericPublic = Field(default=None, description="東京証券取引所 プライム")
    """ 東京証券取引所 プライム """
    tokyo_stock_exchange_pro_market:IxNonNumericPublic = Field(default=None, description="東京証券取引所 PRO Market")
    """ 東京証券取引所 PRO Market """
    tokyo_stock_exchange_standard:IxNonNumericPublic = Field(default=None, description="東京証券取引所 スタンダード")
    """ 東京証券取引所 スタンダード """


