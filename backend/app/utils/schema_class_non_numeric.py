import app.schema.ix_summary_non_numeric as sc


def get_schema_class(key: str):
    if key == "edif":
        return sc.edif
    if key == "edjp":
        return sc.edjp
    if key == "rvfc":
        return sc.rvfc


def get_response_schema_FinancialReportSummary_class():
    items = (
    sc.edif
    | sc.edjp
    | sc.rvfc
    )
    return items
