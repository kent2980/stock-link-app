from app.models import Field, SQLModel
from app.schema.ix_non_numeric import IxNonNumericPublic
from typing import Optional

class IxNonNumericEdjpSm(SQLModel):
    annual_securities_report_filing_date_as_planned: Optional[IxNonNumericPublic] = Field(default=None, description='有価証券報告書提出予定日')
    """ 有価証券報告書提出予定日 """
    applying_of_specific_accounting_of_the_consolidated_quarterly_financial_statements: Optional[IxNonNumericPublic] = Field(default=None, description='四半期連結財務諸表の作成に特有の会計処理の適用')
    """ 四半期連結財務諸表の作成に特有の会計処理の適用 """
    applying_of_specific_accounting_of_the_consolidated_semi_annual_financial_statements: Optional[IxNonNumericPublic] = Field(default=None, description='中間連結財務諸表の作成に特有の会計処理の適用')
    """ 中間連結財務諸表の作成に特有の会計処理の適用 """
    applying_of_specific_accounting_of_the_quarterly_financial_statements: Optional[IxNonNumericPublic] = Field(default=None, description='四半期財務諸表の作成に特有の会計処理の適用')
    """ 四半期財務諸表の作成に特有の会計処理の適用 """
    applying_of_specific_accounting_of_the_semi_annual_financial_statements: Optional[IxNonNumericPublic] = Field(default=None, description='中間財務諸表の作成に特有の会計処理の適用')
    """ 中間財務諸表の作成に特有の会計処理の適用 """
    changes_based_on_revisions_of_accounting_standard: Optional[IxNonNumericPublic] = Field(default=None, description='会計基準等の改正に伴う会計方針の変更')
    """ 会計基準等の改正に伴う会計方針の変更 """
    changes_in_accounting_estimates: Optional[IxNonNumericPublic] = Field(default=None, description='会計上の見積りの変更')
    """ 会計上の見積りの変更 """
    changes_in_accounting_estimates_interim: Optional[IxNonNumericPublic] = Field(default=None, description='会計上の見積りの変更、中間期')
    """ 会計上の見積りの変更、中間期 """
    changes_other_than_ones_based_on_revisions_of_accounting_standard: Optional[IxNonNumericPublic] = Field(default=None, description='会計基準等の改正に伴う変更以外の会計方針の変更')
    """ 会計基準等の改正に伴う変更以外の会計方針の変更 """
    company_name: Optional[IxNonNumericPublic] = Field(default=None, description='上場会社名')
    """ 上場会社名 """
    convening_briefing_of_annual_results: Optional[IxNonNumericPublic] = Field(default=None, description='決算説明会開催の有無')
    """ 決算説明会開催の有無 """
    convening_briefing_of_results: Optional[IxNonNumericPublic] = Field(default=None, description='決算説明会開催の有無、期中')
    """ 決算説明会開催の有無、期中 """
    correction_of_consolidated_financial_forecast_in_this_quarter: Optional[IxNonNumericPublic] = Field(default=None, description='直近に公表されている業績予想からの修正の有無、連結')
    """ 直近に公表されている業績予想からの修正の有無、連結 """
    correction_of_dividend_forecast_in_this_quarter: Optional[IxNonNumericPublic] = Field(default=None, description='直近に公表されている配当予想からの修正の有無')
    """ 直近に公表されている配当予想からの修正の有無 """
    correction_of_financial_forecast_in_this_quarter: Optional[IxNonNumericPublic] = Field(default=None, description='直近に公表されている業績予想からの修正の有無')
    """ 直近に公表されている業績予想からの修正の有無 """
    date_of_general_shareholders_meeting_as_planned: Optional[IxNonNumericPublic] = Field(default=None, description='定時株主総会開催予定日')
    """ 定時株主総会開催予定日 """
    dividend_payable_date_as_planned: Optional[IxNonNumericPublic] = Field(default=None, description='配当支払開始予定日')
    """ 配当支払開始予定日 """
    document_name: Optional[IxNonNumericPublic] = Field(default=None, description='文書名')
    """ 文書名 """
    fasf_member_mark: Optional[IxNonNumericPublic] = Field(default=None, description='財務会計基準機構会員マーク')
    """ 財務会計基準機構会員マーク """
    filing_date: Optional[IxNonNumericPublic] = Field(default=None, description='提出日')
    """ 提出日 """
    fiscal_year_end: Optional[IxNonNumericPublic] = Field(default=None, description='決算期')
    """ 決算期 """
    fukuoka_stock_exchange: Optional[IxNonNumericPublic] = Field(default=None, description='福岡証券取引所')
    """ 福岡証券取引所 """
    fukuoka_stock_exchange_established: Optional[IxNonNumericPublic] = Field(default=None, description='福岡証券取引所 既存市場')
    """ 福岡証券取引所 既存市場 """
    fukuoka_stock_exchange_others: Optional[IxNonNumericPublic] = Field(default=None, description='福岡証券取引所 その他')
    """ 福岡証券取引所 その他 """
    fukuoka_stock_exchange_q_board: Optional[IxNonNumericPublic] = Field(default=None, description='福岡証券取引所 Q-Board')
    """ 福岡証券取引所 Q-Board """
    general_business: Optional[IxNonNumericPublic] = Field(default=None, description='一般事業会社')
    """ 一般事業会社 """
    japan_securities_dealers_association: Optional[IxNonNumericPublic] = Field(default=None, description='フェニックス')
    """ フェニックス """
    japan_securities_dealers_association_green_sheet: Optional[IxNonNumericPublic] = Field(default=None, description='日本証券業協会 フェニックス')
    """ 日本証券業協会 フェニックス """
    material_changes_in_subsidiaries_during_this_period_changes_in_scope_of_consolidations_resulting_from_change_is_subsidiaries: Optional[IxNonNumericPublic] = Field(default=None, description='期中における重要な子会社の異動（連結範囲の変更を伴う特定子会社の異動）')
    """ 期中における重要な子会社の異動（連結範囲の変更を伴う特定子会社の異動） """
    nagoya_stock_exchange: Optional[IxNonNumericPublic] = Field(default=None, description='名古屋証券取引所')
    """ 名古屋証券取引所 """
    nagoya_stock_exchange1st_section: Optional[IxNonNumericPublic] = Field(default=None, description='名古屋証券取引所 プレミア')
    """ 名古屋証券取引所 プレミア """
    nagoya_stock_exchange2nd_section: Optional[IxNonNumericPublic] = Field(default=None, description='名古屋証券取引所 メイン')
    """ 名古屋証券取引所 メイン """
    nagoya_stock_exchange_centrex: Optional[IxNonNumericPublic] = Field(default=None, description='名古屋証券取引所 ネクスト')
    """ 名古屋証券取引所 ネクスト """
    nagoya_stock_exchange_others: Optional[IxNonNumericPublic] = Field(default=None, description='名古屋証券取引所 その他')
    """ 名古屋証券取引所 その他 """
    name_inquiries: Optional[IxNonNumericPublic] = Field(default=None, description='氏名、問合せ先責任者')
    """ 氏名、問合せ先責任者 """
    name_of_subsidiaries_excluded_from_consolidation: Optional[IxNonNumericPublic] = Field(default=None, description='社名、除外')
    """ 社名、除外 """
    name_of_subsidiaries_newly_consolidated: Optional[IxNonNumericPublic] = Field(default=None, description='社名、新規')
    """ 社名、新規 """
    name_representative: Optional[IxNonNumericPublic] = Field(default=None, description='氏名、代表者')
    """ 氏名、代表者 """
    note_to_applying_of_specific_accounting_of_the_consolidated_quarterly_financial_statements: Optional[IxNonNumericPublic] = Field(default=None, description='四半期連結財務諸表の作成に特有の会計処理の適用に関する注記')
    """ 四半期連結財務諸表の作成に特有の会計処理の適用に関する注記 """
    note_to_applying_of_specific_accounting_of_the_consolidated_semi_annual_financial_statements: Optional[IxNonNumericPublic] = Field(default=None, description='中間連結財務諸表の作成に特有の会計処理の適用に関する注記')
    """ 中間連結財務諸表の作成に特有の会計処理の適用に関する注記 """
    note_to_applying_of_specific_accounting_of_the_quarterly_financial_statements: Optional[IxNonNumericPublic] = Field(default=None, description='四半期財務諸表の作成に特有の会計処理の適用に関する注記')
    """ 四半期財務諸表の作成に特有の会計処理の適用に関する注記 """
    note_to_applying_of_specific_accounting_of_the_semi_annual_financial_statements: Optional[IxNonNumericPublic] = Field(default=None, description='中間財務諸表の作成に特有の会計処理の適用に関する注記')
    """ 中間財務諸表の作成に特有の会計処理の適用に関する注記 """
    note_to_cash_flows: Optional[IxNonNumericPublic] = Field(default=None, description='キャッシュ・フローの状況に関する注記')
    """ キャッシュ・フローの状況に関する注記 """
    note_to_changes_in_accounting_policies_accounting_estimates_and_retrospective_restatement_interim_consolidated: Optional[IxNonNumericPublic] = Field(default=None, description='会計方針の変更・会計上の見積りの変更・修正再表示に関する注記、中間期')
    """ 会計方針の変更・会計上の見積りの変更・修正再表示に関する注記、中間期 """
    note_to_changes_in_accounting_policies_accounting_estimates_and_retrospective_restatement_quarterly_consolidated: Optional[IxNonNumericPublic] = Field(default=None, description='会計方針の変更・会計上の見積りの変更・修正再表示に関する注記、四半期')
    """ 会計方針の変更・会計上の見積りの変更・修正再表示に関する注記、四半期 """
    note_to_changes_in_accounting_policies_and_accounting_estimates_retrospective_restatement: Optional[IxNonNumericPublic] = Field(default=None, description='会計方針の変更・会計上の見積りの変更・修正再表示に関する注記')
    """ 会計方針の変更・会計上の見積りの変更・修正再表示に関する注記 """
    note_to_consolidated_financial_results: Optional[IxNonNumericPublic] = Field(default=None, description='連結業績に関する注記')
    """ 連結業績に関する注記 """
    note_to_dividends: Optional[IxNonNumericPublic] = Field(default=None, description='配当の状況に関する注記')
    """ 配当の状況に関する注記 """
    note_to_financial_positions: Optional[IxNonNumericPublic] = Field(default=None, description='財政状態に関する注記')
    """ 財政状態に関する注記 """
    note_to_financial_results: Optional[IxNonNumericPublic] = Field(default=None, description='業績に関する注記')
    """ 業績に関する注記 """
    note_to_forecasts: Optional[IxNonNumericPublic] = Field(default=None, description='業績予想に関する事項、注記')
    """ 業績予想に関する事項、注記 """
    note_to_fraction_processing_method: Optional[IxNonNumericPublic] = Field(default=None, description='端数処理方法に関する注記')
    """ 端数処理方法に関する注記 """
    note_to_material_changes_in_subsidiaries_during_this_period: Optional[IxNonNumericPublic] = Field(default=None, description='期中における重要な子会社の異動に関する注記')
    """ 期中における重要な子会社の異動に関する注記 """
    note_to_number_of_issued_and_outstanding_shares_common_stock: Optional[IxNonNumericPublic] = Field(default=None, description='発行済株式数（普通株式）に関する注記')
    """ 発行済株式数（普通株式）に関する注記 """
    note_to_operating_results: Optional[IxNonNumericPublic] = Field(default=None, description='経営成績に関する注記')
    """ 経営成績に関する注記 """
    note_to_significant_changes_in_the_scope_of_consolidation_during_the_period: Optional[IxNonNumericPublic] = Field(default=None, description='期中における連結範囲の重要な変更に関する注記')
    """ 期中における連結範囲の重要な変更に関する注記 """
    notes_for_using_forecasted_information_and_others: Optional[IxNonNumericPublic] = Field(default=None, description='業績予想の適切な利用に関する説明、その他特記事項')
    """ 業績予想の適切な利用に関する説明、その他特記事項 """
    preamble_to_forecasts: Optional[IxNonNumericPublic] = Field(default=None, description='業績予想に関する事項')
    """ 業績予想に関する事項 """
    retrospective_restatement: Optional[IxNonNumericPublic] = Field(default=None, description='修正再表示')
    """ 修正再表示 """
    retrospective_restatement_interim: Optional[IxNonNumericPublic] = Field(default=None, description='修正再表示、中間期')
    """ 修正再表示、中間期 """
    review_of_attached_consolidated_quarterly_financial_statements_by_a_certified_public_accountant_or_an_audit_firm: Optional[IxNonNumericPublic] = Field(default=None, description='添付される四半期連結財務諸表に対する公認会計士又は監査法人によるレビュー')
    """ 添付される四半期連結財務諸表に対する公認会計士又は監査法人によるレビュー """
    review_of_attached_quarterly_financial_statements_by_a_certified_public_accountant_or_an_audit_firm: Optional[IxNonNumericPublic] = Field(default=None, description='添付される四半期財務諸表に対する公認会計士又は監査法人によるレビュー')
    """ 添付される四半期財務諸表に対する公認会計士又は監査法人によるレビュー """
    sapporo_stock_exchange: Optional[IxNonNumericPublic] = Field(default=None, description='札幌証券取引所')
    """ 札幌証券取引所 """
    sapporo_stock_exchange_ambitious: Optional[IxNonNumericPublic] = Field(default=None, description='札幌証券取引所 アンビシャス')
    """ 札幌証券取引所 アンビシャス """
    sapporo_stock_exchange_established: Optional[IxNonNumericPublic] = Field(default=None, description='札幌証券取引所 既存市場')
    """ 札幌証券取引所 既存市場 """
    sapporo_stock_exchange_others: Optional[IxNonNumericPublic] = Field(default=None, description='札幌証券取引所 その他')
    """ 札幌証券取引所 その他 """
    securities_code: Optional[IxNonNumericPublic] = Field(default=None, description='コード番号')
    """ コード番号 """
    semi_annual_statement_filing_date_as_planned: Optional[IxNonNumericPublic] = Field(default=None, description='半期報告書提出予定日')
    """ 半期報告書提出予定日 """
    setting_of_specific_transaction_account_bk: Optional[IxNonNumericPublic] = Field(default=None, description='特定取引勘定設置の有無、銀行')
    """ 特定取引勘定設置の有無、銀行 """
    significant_changes_in_the_scope_of_consolidation_during_the_period: Optional[IxNonNumericPublic] = Field(default=None, description='期中における連結範囲の重要な変更')
    """ 期中における連結範囲の重要な変更 """
    specific_business: Optional[IxNonNumericPublic] = Field(default=None, description='特定事業会社')
    """ 特定事業会社 """
    supplemental_material_of_annual_results: Optional[IxNonNumericPublic] = Field(default=None, description='決算補足説明資料作成の有無')
    """ 決算補足説明資料作成の有無 """
    supplemental_material_of_results: Optional[IxNonNumericPublic] = Field(default=None, description='決算補足説明資料作成の有無、期中')
    """ 決算補足説明資料作成の有無、期中 """
    target_audience_briefing_of_annual_results: Optional[IxNonNumericPublic] = Field(default=None, description='対象者、決算説明会')
    """ 対象者、決算説明会 """
    target_for_briefing_of_results: Optional[IxNonNumericPublic] = Field(default=None, description='決算説明会の対象者')
    """ 決算説明会の対象者 """
    tel: Optional[IxNonNumericPublic] = Field(default=None, description='TEL')
    """ TEL """
    title_for_forecasts: Optional[IxNonNumericPublic] = Field(default=None, description='業績予想タイトル名称')
    """ 業績予想タイトル名称 """
    title_inquiries: Optional[IxNonNumericPublic] = Field(default=None, description='役職名、問合せ先責任者')
    """ 役職名、問合せ先責任者 """
    title_representative: Optional[IxNonNumericPublic] = Field(default=None, description='役職名、代表者')
    """ 役職名、代表者 """
    tokyo_stock_exchange: Optional[IxNonNumericPublic] = Field(default=None, description='東京証券取引所')
    """ 東京証券取引所 """
    tokyo_stock_exchange1st_section: Optional[IxNonNumericPublic] = Field(default=None, description='東京証券取引所 第一部')
    """ 東京証券取引所 第一部 """
    tokyo_stock_exchange2nd_section: Optional[IxNonNumericPublic] = Field(default=None, description='東京証券取引所 第二部')
    """ 東京証券取引所 第二部 """
    tokyo_stock_exchange_growth: Optional[IxNonNumericPublic] = Field(default=None, description='東京証券取引所 グロース')
    """ 東京証券取引所 グロース """
    tokyo_stock_exchange_jasdaq: Optional[IxNonNumericPublic] = Field(default=None, description='東京証券取引所 JASDAQ')
    """ 東京証券取引所 JASDAQ """
    tokyo_stock_exchange_mothers: Optional[IxNonNumericPublic] = Field(default=None, description='東京証券取引所 マザーズ')
    """ 東京証券取引所 マザーズ """
    tokyo_stock_exchange_others: Optional[IxNonNumericPublic] = Field(default=None, description='東京証券取引所 その他')
    """ 東京証券取引所 その他 """
    tokyo_stock_exchange_pro_market: Optional[IxNonNumericPublic] = Field(default=None, description='東京証券取引所 PRO Market')
    """ 東京証券取引所 PRO Market """
    tokyo_stock_exchange_prime: Optional[IxNonNumericPublic] = Field(default=None, description='東京証券取引所 プライム')
    """ 東京証券取引所 プライム """
    tokyo_stock_exchange_standard: Optional[IxNonNumericPublic] = Field(default=None, description='東京証券取引所 スタンダード')
    """ 東京証券取引所 スタンダード """
    URL: Optional[IxNonNumericPublic] = Field(default=None, description='URL')
    """ URL """
    way_of_getting_supplemental_material_of_annual_results: Optional[IxNonNumericPublic] = Field(default=None, description='入手方法等、決算補足説明資料')
    """ 入手方法等、決算補足説明資料 """
    way_of_getting_supplemental_material_of_results: Optional[IxNonNumericPublic] = Field(default=None, description='入手方法等、決算補足説明資料、期中')
    """ 入手方法等、決算補足説明資料、期中 """

