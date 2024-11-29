from typing import Optional


def generate_key(item: dict, ixbrl_role: Optional[str] = None) -> str:
    if item.get("is_consolidated") is True:
        is_consolidated = "_consolidated"
    elif item.get("is_consolidated") is False:
        is_consolidated = "_Nonconsolidated"
    else:
        is_consolidated = ""

    if ixbrl_role is None:
        ixbrl_role = item.get("ixbrl_role", "")

    key = f"{item['report_type']}_{ixbrl_role}{is_consolidated}"
    if item["current_period"]:
        if item["specific_business"] is True:
            key = f"{key}_{item['current_period']}_specific_business"
        else:
            key = f"{key}_{item['current_period']}"
    else:
        if item["specific_business"] is True:
            key = f"{key}_specific_business"
        else:
            key = f"{key}"

    return key
