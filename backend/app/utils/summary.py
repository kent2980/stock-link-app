import re
from typing import Optional

import humps


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


def get_short_context(context: str) -> str:
    context = humps.decamelize(context)
    context = re.sub(r"_q\d|_FY|_HY", "", context)  # 期間を削除
    context = re.sub(r"_member", "", context)  # memberを削除
    context = re.sub(r"_accumulated", "", context)  # accumulatedを削除
    context = re.sub(r"_year", "", context)  # yearを削除
    context = re.sub(r"consolidated", "cons", context)  # consolidatedをconsに変換
    context = re.sub(r"duration", "dur", context)  # durationをdurに変換
    context = re.sub(r"current", "cur", context)  # currentをcurに変換
    context = re.sub(r"prior", "pri", context)  # priorをpriに変換
    context = re.sub(r"result", "res", context)  # resultをresに変換
    context = re.sub(r"forecast", "fore", context)  # forecastをforeに変換
    context = context.replace("__", "_")  # 連続するアンダースコアを1つに変換

    return context
