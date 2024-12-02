from typing import Optional


def generate_non_fraction_key(item: dict, ixbrl_role: Optional[str] = None) -> str:
    if item.get("is_consolidated") is True:
        is_consolidated = "_Con"
    elif item.get("is_consolidated") is False:
        is_consolidated = "_NonCon"
    else:
        is_consolidated = ""

    if ixbrl_role is None:
        ixbrl_role = item.get("ixbrl_role", "")

    key = f"{item['report_type']}_{ixbrl_role}{is_consolidated}"
    if item["current_period"]:
        if item["specific_business"] is True:
            key = f"{key}_{item['current_period']}_spec"
        else:
            key = f"{key}_{item['current_period']}"
    else:
        if item["specific_business"] is True:
            key = f"{key}_spec"
        else:
            key = f"{key}"

    return key


def generate_non_numeric_key(item: dict) -> str:

    key = f"{item['report_type']}"

    return key
