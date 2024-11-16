from app.models import IxNonNumeric
from sqlmodel import Session, select

def balance_sheet_text_block(session: Session, head_item_key:str):
    """
    貸借対照表 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpcrp_cor_BalanceSheetTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def consolidated_balance_sheet_text_block(session: Session, head_item_key:str):
    """
    連結貸借対照表 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpcrp_cor_ConsolidatedBalanceSheetTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def consolidated_statement_of_cash_flows_text_block(session: Session, head_item_key:str):
    """
    連結キャッシュ・フロー計算書 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpcrp_cor_ConsolidatedStatementOfCashFlowsTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def consolidated_statement_of_changes_in_equity_text_block(session: Session, head_item_key:str):
    """
    連結株主資本等変動計算書 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpcrp_cor_ConsolidatedStatementOfChangesInEquityTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def consolidated_statement_of_comprehensive_income_single_statement_text_block(session: Session, head_item_key:str):
    """
    連結損益及び包括利益計算書 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpcrp_cor_ConsolidatedStatementOfComprehensiveIncomeSingleStatementTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def consolidated_statement_of_comprehensive_income_text_block(session: Session, head_item_key:str):
    """
    連結包括利益計算書 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpcrp_cor_ConsolidatedStatementOfComprehensiveIncomeTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def consolidated_statement_of_income_text_block(session: Session, head_item_key:str):
    """
    連結損益計算書 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpcrp_cor_ConsolidatedStatementOfIncomeTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def debtors_notes_regarding_overdraft_contracts_and_or_loan_commitments_text_block(session: Session, head_item_key:str):
    """
    当座貸越契約及び（又は）貸出コミットメントに関する借手の注記 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpcrp_cor_DebtorsNotesRegardingOverdraftContractsAndOrLoanCommitmentsTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def description_of_fact_that_companys_business_comprises_single_segment(session: Session, head_item_key:str):
    """
    単一セグメントである旨
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpcrp_cor_DescriptionOfFactThatCompanysBusinessComprisesSingleSegment',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def description_of_factors_which_led_to_recognition_of_gain_on_bargain_purchase_text_block(session: Session, head_item_key:str):
    """
    報告セグメントごとの負ののれん発生益を認識する要因となった事象の概要 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpcrp_cor_DescriptionOfFactorsWhichLedToRecognitionOfGainOnBargainPurchaseTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def description_of_nature_and_amounts_of_differences_between_reportable_segments_total_and_financial_statements_text_block(session: Session, head_item_key:str):
    """
    報告セグメント合計額と財務諸表計上額との差額及び当該差額の主な内容（差異調整に関する事項） [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpcrp_cor_DescriptionOfNatureAndAmountsOfDifferencesBetweenReportableSegmentsTotalAndFinancialStatementsTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def description_of_nature_of_differences_between_profit_loss_of_reportable_segments_total_and_quarterly_financial_statements_text_block(session: Session, head_item_key:str):
    """
    報告セグメントごとの利益又は損失の金額の合計額と四半期損益計算書計上額との差額及び当該差額の主な内容（差異調整に関する事項） [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpcrp_cor_DescriptionOfNatureOfDifferencesBetweenProfitLossOfReportableSegmentsTotalAndQuarterlyFinancialStatementsTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def description_of_reportable_segments_text_block(session: Session, head_item_key:str):
    """
    報告セグメントの概要 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpcrp_cor_DescriptionOfReportableSegmentsTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def detailed_schedule_of_manufacturing_cost_text_block(session: Session, head_item_key:str):
    """
    製造原価明細書 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpcrp_cor_DetailedScheduleOfManufacturingCostTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def disclosure_of_changes_etc_in_reportable_segments_text_block(session: Session, head_item_key:str):
    """
    報告セグメントの変更等に関する事項 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpcrp_cor_DisclosureOfChangesEtcInReportableSegmentsTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def disclosure_of_changes_in_reportable_segments_text_block(session: Session, head_item_key:str):
    """
    報告セグメントの変更に関する事項 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpcrp_cor_DisclosureOfChangesInReportableSegmentsTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def explanation_of_measurements_of_sales_profit_loss_asset_liability_and_other_items_for_each_reportable_segment_text_block(session: Session, head_item_key:str):
    """
    報告セグメントごとの売上高、利益又は損失、資産、負債その他の項目の金額の算定方法 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpcrp_cor_ExplanationOfMeasurementsOfSalesProfitLossAssetLiabilityAndOtherItemsForEachReportableSegmentTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def footnotes_regarding_segment_information_table_text_block(session: Session, head_item_key:str):
    """
    セグメント表の脚注 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpcrp_cor_FootnotesRegardingSegmentInformationTableTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def information_about_assets_for_each_reportable_segment_text_block(session: Session, head_item_key:str):
    """
    報告セグメントごとの資産に関する情報 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpcrp_cor_InformationAboutAssetsForEachReportableSegmentTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def information_about_impairment_loss_of_non_current_assets_or_goodwill_etc_for_each_reportable_segment_text_block(session: Session, head_item_key:str):
    """
    報告セグメントごとの固定資産の減損損失又はのれん等に関する情報 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpcrp_cor_InformationAboutImpairmentLossOfNonCurrentAssetsOrGoodwillEtcForEachReportableSegmentTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def information_for_each_of_main_customers_text_block(session: Session, head_item_key:str):
    """
    主要な顧客ごとの情報 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpcrp_cor_InformationForEachOfMainCustomersTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def information_for_each_product_or_service_text_block(session: Session, head_item_key:str):
    """
    製品及びサービスごとの情報 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpcrp_cor_InformationForEachProductOrServiceTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def major_components_of_selling_general_and_administrative_expenses_text_block(session: Session, head_item_key:str):
    """
    主要な販売費及び一般管理費 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpcrp_cor_MajorComponentsOfSellingGeneralAndAdministrativeExpensesTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def notes_regarding_accumulated_depreciation_of_property_plant_and_equipment_text_block(session: Session, head_item_key:str):
    """
    有形固定資産の減価償却累計額の注記 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpcrp_cor_NotesRegardingAccumulatedDepreciationOfPropertyPlantAndEquipmentTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def notes_regarding_allowances_directly_deducted_from_balances_of_assets_text_block(session: Session, head_item_key:str):
    """
    資産の金額から直接控除している引当金の注記 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpcrp_cor_NotesRegardingAllowancesDirectlyDeductedFromBalancesOfAssetsTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def notes_regarding_amounts_of_reduction_entry_of_property_plant_and_equipment_text_block(session: Session, head_item_key:str):
    """
    有形固定資産の圧縮記帳額の注記 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpcrp_cor_NotesRegardingAmountsOfReductionEntryOfPropertyPlantAndEquipmentTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def notes_regarding_gain_on_sales_of_property_plant_and_equipment_text_block(session: Session, head_item_key:str):
    """
    固定資産売却益の注記 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpcrp_cor_NotesRegardingGainOnSalesOfPropertyPlantAndEquipmentTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def notes_regarding_guarantee_obligations_text_block(session: Session, head_item_key:str):
    """
    保証債務の注記 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpcrp_cor_NotesRegardingGuaranteeObligationsTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def notes_regarding_impairment_loss_text_block(session: Session, head_item_key:str):
    """
    減損損失に関する注記 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpcrp_cor_NotesRegardingImpairmentLossTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def notes_regarding_inventories_text_block(session: Session, head_item_key:str):
    """
    棚卸資産の内訳の注記 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpcrp_cor_NotesRegardingInventoriesTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def notes_regarding_loss_on_disposal_of_property_plant_and_equipment_text_block(session: Session, head_item_key:str):
    """
    固定資産除却損の注記 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpcrp_cor_NotesRegardingLossOnDisposalOfPropertyPlantAndEquipmentTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def notes_regarding_loss_on_sales_of_property_plant_and_equipment_text_block(session: Session, head_item_key:str):
    """
    固定資産売却損の注記 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpcrp_cor_NotesRegardingLossOnSalesOfPropertyPlantAndEquipmentTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def notes_regarding_pledged_assets_text_block(session: Session, head_item_key:str):
    """
    担保に供している資産の注記 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpcrp_cor_NotesRegardingPledgedAssetsTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def notes_regarding_promissory_notes_due_on_balance_sheet_date_text_block(session: Session, head_item_key:str):
    """
    期末日満期手形の会計処理 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpcrp_cor_NotesRegardingPromissoryNotesDueOnBalanceSheetDateTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def notes_regarding_shares_and_bonds_etc_of_unconsolidated_subsidiaries_and_associates_text_block(session: Session, head_item_key:str):
    """
    非連結子会社及び関連会社の株式及び社債等 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpcrp_cor_NotesRegardingSharesAndBondsEtcOfUnconsolidatedSubsidiariesAndAssociatesTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def notes_segment_information_etc_consolidated_financial_statements_text_block(session: Session, head_item_key:str):
    """
    セグメント情報等、連結財務諸表 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpcrp_cor_NotesSegmentInformationEtcConsolidatedFinancialStatementsTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def notes_segment_information_etc_financial_statements_text_block(session: Session, head_item_key:str):
    """
    セグメント情報等、財務諸表 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpcrp_cor_NotesSegmentInformationEtcFinancialStatementsTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def notes_segment_information_etc_quarterly_consolidated_financial_statements_text_block(session: Session, head_item_key:str):
    """
    セグメント情報等、四半期連結財務諸表 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpcrp_cor_NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatementsTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def notes_segment_information_etc_quarterly_financial_statements_text_block(session: Session, head_item_key:str):
    """
    セグメント情報等、四半期財務諸表 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpcrp_cor_NotesSegmentInformationEtcQuarterlyFinancialStatementsTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def notes_segment_information_etc_semi_annual_consolidated_financial_statements_text_block(session: Session, head_item_key:str):
    """
    セグメント情報等、中間連結財務諸表 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpcrp_cor_NotesSegmentInformationEtcSemiAnnualConsolidatedFinancialStatementsTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def notes_when_there_is_significant_seasonal_fluctuation_in_sales_or_operating_expenses_text_block(session: Session, head_item_key:str):
    """
    売上高又は営業費用に著しい季節的変動がある場合の注記 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpcrp_cor_NotesWhenThereIsSignificantSeasonalFluctuationInSalesOrOperatingExpensesTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def property_plant_and_equipment_information_for_each_region_text_block(session: Session, head_item_key:str):
    """
    有形固定資産、地域ごとの情報 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpcrp_cor_PropertyPlantAndEquipmentInformationForEachRegionTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def quarterly_balance_sheet_text_block(session: Session, head_item_key:str):
    """
    四半期貸借対照表 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpcrp_cor_QuarterlyBalanceSheetTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def quarterly_consolidated_balance_sheet_text_block(session: Session, head_item_key:str):
    """
    四半期連結貸借対照表 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpcrp_cor_QuarterlyConsolidatedBalanceSheetTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def quarterly_consolidated_statement_of_cash_flows_text_block(session: Session, head_item_key:str):
    """
    四半期連結キャッシュ・フロー計算書 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpcrp_cor_QuarterlyConsolidatedStatementOfCashFlowsTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def quarterly_statement_of_cash_flows_text_block(session: Session, head_item_key:str):
    """
    四半期キャッシュ・フロー計算書 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpcrp_cor_QuarterlyStatementOfCashFlowsTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def research_and_development_expenses_included_in_general_and_administrative_expenses_and_manufacturing_cost_for_current_period_text_block(session: Session, head_item_key:str):
    """
    一般管理費及び当期製造費用に含まれる研究開発費 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpcrp_cor_ResearchAndDevelopmentExpensesIncludedInGeneralAndAdministrativeExpensesAndManufacturingCostForCurrentPeriodTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def revenues_from_external_customers_information_for_each_region_text_block(session: Session, head_item_key:str):
    """
    売上高、地域ごとの情報 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpcrp_cor_RevenuesFromExternalCustomersInformationForEachRegionTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def semi_annual_balance_sheet_text_block(session: Session, head_item_key:str):
    """
    中間貸借対照表 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpcrp_cor_SemiAnnualBalanceSheetTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def semi_annual_consolidated_balance_sheet_text_block(session: Session, head_item_key:str):
    """
    中間連結貸借対照表 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpcrp_cor_SemiAnnualConsolidatedBalanceSheetTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def semi_annual_consolidated_statement_of_cash_flows_text_block(session: Session, head_item_key:str):
    """
    中間連結キャッシュ・フロー計算書 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpcrp_cor_SemiAnnualConsolidatedStatementOfCashFlowsTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def semi_annual_consolidated_statement_of_changes_in_equity_text_block(session: Session, head_item_key:str):
    """
    中間連結株主資本等変動計算書 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpcrp_cor_SemiAnnualConsolidatedStatementOfChangesInEquityTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def semi_annual_consolidated_statement_of_comprehensive_income_text_block(session: Session, head_item_key:str):
    """
    中間連結包括利益計算書 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpcrp_cor_SemiAnnualConsolidatedStatementOfComprehensiveIncomeTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def semi_annual_consolidated_statement_of_income_text_block(session: Session, head_item_key:str):
    """
    中間連結損益計算書 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpcrp_cor_SemiAnnualConsolidatedStatementOfIncomeTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def semi_annual_statement_of_changes_in_equity_text_block(session: Session, head_item_key:str):
    """
    中間株主資本等変動計算書 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpcrp_cor_SemiAnnualStatementOfChangesInEquityTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def semi_annual_statement_of_income_text_block(session: Session, head_item_key:str):
    """
    中間損益計算書 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpcrp_cor_SemiAnnualStatementOfIncomeTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def statement_of_cash_flows_text_block(session: Session, head_item_key:str):
    """
    キャッシュ・フロー計算書 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpcrp_cor_StatementOfCashFlowsTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def statement_of_changes_in_equity_text_block(session: Session, head_item_key:str):
    """
    株主資本等変動計算書 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpcrp_cor_StatementOfChangesInEquityTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def statement_of_income_text_block(session: Session, head_item_key:str):
    """
    損益計算書 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpcrp_cor_StatementOfIncomeTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def year_to_quarter_end_consolidated_statement_of_comprehensive_income_single_statement_text_block(session: Session, head_item_key:str):
    """
    四半期連結累計期間、四半期連結損益及び包括利益計算書 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpcrp_cor_YearToQuarterEndConsolidatedStatementOfComprehensiveIncomeSingleStatementTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def year_to_quarter_end_consolidated_statement_of_comprehensive_income_text_block(session: Session, head_item_key:str):
    """
    四半期連結累計期間、四半期連結包括利益計算書 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpcrp_cor_YearToQuarterEndConsolidatedStatementOfComprehensiveIncomeTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def year_to_quarter_end_consolidated_statement_of_income_text_block(session: Session, head_item_key:str):
    """
    四半期連結累計期間、四半期連結損益計算書 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpcrp_cor_YearToQuarterEndConsolidatedStatementOfIncomeTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def year_to_quarter_end_statement_of_income_text_block(session: Session, head_item_key:str):
    """
    四半期累計期間、四半期損益計算書 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpcrp_cor_YearToQuarterEndStatementOfIncomeTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def accounting_standards_dei(session: Session, head_item_key:str):
    """
    会計基準、DEI
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpdei_cor_AccountingStandardsDEI',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def amendment_flag_dei(session: Session, head_item_key:str):
    """
    訂正の有無、DEI
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpdei_cor_AmendmentFlagDEI',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def cabinet_office_ordinance_dei(session: Session, head_item_key:str):
    """
    府令、DEI
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpdei_cor_CabinetOfficeOrdinanceDEI',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def comparative_period_end_date_dei(session: Session, head_item_key:str):
    """
    比較対象会計期間終了日、DEI
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpdei_cor_ComparativePeriodEndDateDEI',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def current_fiscal_year_end_date_dei(session: Session, head_item_key:str):
    """
    当事業年度終了日、DEI
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpdei_cor_CurrentFiscalYearEndDateDEI',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def current_fiscal_year_start_date_dei(session: Session, head_item_key:str):
    """
    当事業年度開始日、DEI
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpdei_cor_CurrentFiscalYearStartDateDEI',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def current_period_end_date_dei(session: Session, head_item_key:str):
    """
    当会計期間終了日、DEI
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpdei_cor_CurrentPeriodEndDateDEI',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def document_type_dei(session: Session, head_item_key:str):
    """
    様式、DEI
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpdei_cor_DocumentTypeDEI',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def edinet_code_dei(session: Session, head_item_key:str):
    """
    EDINETコード、DEI
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpdei_cor_EDINETCodeDEI',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def end_date_of_quarterly_or_semi_annual_period_of_next_fiscal_year_dei(session: Session, head_item_key:str):
    """
    次の四半期又は中間期の会計期間終了日、DEI
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpdei_cor_EndDateOfQuarterlyOrSemiAnnualPeriodOfNextFiscalYearDEI',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def filer_name_in_english_dei(session: Session, head_item_key:str):
    """
    提出者名（英語表記）、DEI
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpdei_cor_FilerNameInEnglishDEI',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def filer_name_in_japanese_dei(session: Session, head_item_key:str):
    """
    提出者名（日本語表記）、DEI
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpdei_cor_FilerNameInJapaneseDEI',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def fund_code_dei(session: Session, head_item_key:str):
    """
    ファンドコード、DEI
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpdei_cor_FundCodeDEI',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def fund_name_in_english_dei(session: Session, head_item_key:str):
    """
    ファンド名称（英語表記）、DEI
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpdei_cor_FundNameInEnglishDEI',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def fund_name_in_japanese_dei(session: Session, head_item_key:str):
    """
    ファンド名称（日本語表記）、DEI
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpdei_cor_FundNameInJapaneseDEI',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def identification_of_document_subject_to_amendment_dei(session: Session, head_item_key:str):
    """
    訂正対象書類の書類管理番号、DEI
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpdei_cor_IdentificationOfDocumentSubjectToAmendmentDEI',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def industry_code_when_consolidated_financial_statements_are_prepared_in_accordance_with_industry_specific_regulations_dei(session: Session, head_item_key:str):
    """
    別記事業（連結）、DEI
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpdei_cor_IndustryCodeWhenConsolidatedFinancialStatementsArePreparedInAccordanceWithIndustrySpecificRegulationsDEI',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def industry_code_when_financial_statements_are_prepared_in_accordance_with_industry_specific_regulations_dei(session: Session, head_item_key:str):
    """
    別記事業（個別）、DEI
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpdei_cor_IndustryCodeWhenFinancialStatementsArePreparedInAccordanceWithIndustrySpecificRegulationsDEI',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def next_fiscal_year_start_date_dei(session: Session, head_item_key:str):
    """
    次の事業年度開始日、DEI
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpdei_cor_NextFiscalYearStartDateDEI',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def previous_fiscal_year_end_date_dei(session: Session, head_item_key:str):
    """
    前事業年度終了日、DEI
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpdei_cor_PreviousFiscalYearEndDateDEI',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def previous_fiscal_year_start_date_dei(session: Session, head_item_key:str):
    """
    前事業年度開始日、DEI
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpdei_cor_PreviousFiscalYearStartDateDEI',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def report_amendment_flag_dei(session: Session, head_item_key:str):
    """
    記載事項訂正のフラグ、DEI
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpdei_cor_ReportAmendmentFlagDEI',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def security_code_dei(session: Session, head_item_key:str):
    """
    証券コード、DEI
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpdei_cor_SecurityCodeDEI',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def type_of_current_period_dei(session: Session, head_item_key:str):
    """
    当会計期間の種類、DEI
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpdei_cor_TypeOfCurrentPeriodDEI',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def whether_consolidated_financial_statements_are_prepared_dei(session: Session, head_item_key:str):
    """
    連結決算の有無、DEI
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpdei_cor_WhetherConsolidatedFinancialStatementsArePreparedDEI',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def xbrl_amendment_flag_dei(session: Session, head_item_key:str):
    """
    XBRL訂正のフラグ、DEI
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'jpdei_cor_XBRLAmendmentFlagDEI',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def notes_regarding_amortization_of_goodwill_text_block(session: Session, head_item_key:str):
    """
    のれん償却額の注記 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-acedjpfr-43200_NotesRegardingAmortizationOfGoodwillTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def notes_regarding_loss_on_abandonment_of_inventories_text_block(session: Session, head_item_key:str):
    """
    棚卸資産廃棄損の注記 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-acedjpfr-98690_NotesRegardingLossOnAbandonmentOfInventoriesTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def notes_regarding_loss_on_disaster_text_block(session: Session, head_item_key:str):
    """
    災害による損失の注記 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-acedjpfr-98690_NotesRegardingLossOnDisasterTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def notes_regarding_restructuring_loss_text_block(session: Session, head_item_key:str):
    """
    事業再編損の注記 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-acedjpfr-98690_NotesRegardingRestructuringLossTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def notes_regarding_subsidy_income_text_block(session: Session, head_item_key:str):
    """
    補助金収入の注記 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-acedjpfr-98690_NotesRegardingSubsidyIncomeTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def notes_regarding_financial_covenant_clauses_text_block(session: Session, head_item_key:str):
    """
    財務制限条項に関する注記 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-qcedjpfr-27880_NotesRegardingFinancialCovenantClausesTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def notes_regarding_details_of_extraordinary_losses_text_block(session: Session, head_item_key:str):
    """
    特別損失の内容に関する注記 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-qcedjpfr-49670_NotesRegardingDetailsOfExtraordinaryLossesTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def notes_regarding_relocation_related_losses_text_block(session: Session, head_item_key:str):
    """
    移転関連損失についての注記 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-qcedjpfr-79360_NotesRegardingRelocationRelatedLossesTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def notes_and_accounts_receivable_trede_text_block(session: Session, head_item_key:str):
    """
    受取手形及び売掛金に関する注記 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-scedjpfr-27540_NotesAndAccountsReceivableTredeTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def notes_regarding_gain_on_transfer_of_business_text_block(session: Session, head_item_key:str):
    """
    事業譲渡益の注記 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-scedjpfr-45440_NotesRegardingGainOnTransferOfBusinessTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def notes_regarding_loss_on_liquidation_of_subsidiaries_and_associates_text_block(session: Session, head_item_key:str):
    """
    関係会社清算損の注記 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-scedjpfr-45440_NotesRegardingLossOnLiquidationOfSubsidiariesAndAssociatesTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def notes_regarding_reduction_entry_text_block(session: Session, head_item_key:str):
    """
    圧縮記帳額に関する注記 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-scedjpfr-45440_NotesRegardingReductionEntryTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def notes_regarding_reversal_of_provision_for_loss_on_compensation_text_block(session: Session, head_item_key:str):
    """
    補償損失引当金戻入額に関する注記 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-scedjpfr-45440_NotesRegardingReversalOfProvisionForLossOnCompensationTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def notes_regarding_loss_on_litigation_text_block(session: Session, head_item_key:str):
    """
    訴訟関連損失の注記 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-scedjpfr-52370_NotesRegardingLossOnLitigationTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def notes_regarding_provision_for_loss_on_litigation_text_block(session: Session, head_item_key:str):
    """
    訴訟損失引当金に関する注記 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-scedjpfr-52370_NotesRegardingProvisionForLossOnLitigationTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def notes_regarding_loss_on_inappropriate_conduct_in_quality_inspections_text_block(session: Session, head_item_key:str):
    """
    品質不適切行為関連損失に関する注記 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-scedjpfr-56310_NotesRegardingLossOnInappropriateConductInQualityInspectionsTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def notes_system_failure_response_cost_text_block(session: Session, head_item_key:str):
    """
    システム障害対応費用の注記 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-scedjpfr-62820_NotesSystemFailureResponseCostTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def notes_on_contingent_liabilities_text_block(session: Session, head_item_key:str):
    """
    偶発債務に関する注記 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-scedjpfr-79140_NotesOnContingentLiabilitiesTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def disclosure_of_impairment_loss_on_non_current_assets_for_each_reportable_segment_text_block(session: Session, head_item_key:str):
    """
    報告セグメントごとの固定資産の減損損失に関する情報 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-scedjpfr-80930_DisclosureOfImpairmentLossOnNonCurrentAssetsForEachReportableSegmentTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def notes_regarding_provision_for_return_of_subsidy_text_block(session: Session, head_item_key:str):
    """
    助成金返還引当金繰入額に関する注記 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-scedjpfr-90480_NotesRegardingProvisionForReturnOfSubsidyTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

def notes_regarding_materials_supplied_for_value_text_block(session: Session, head_item_key:str):
    """
    有償支給材料に関する注記 [テキストブロック]
    """
    statement = (
        select(IxNonNumeric)
        .where(
            IxNonNumeric.name == 'tse-snedjpfr-69070_NotesRegardingMaterialsSuppliedForValueTextBlock',
            IxNonNumeric.head_item_key == head_item_key,
            IxNonNumeric.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

