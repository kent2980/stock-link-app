import json
import os
from collections import defaultdict

import humps
import requests


def generate_module_non_fraction(base_url: str):

    url = f"{base_url}/generate/grouping/non_fraction/"
    response = requests.get(url)
    items = response.json().get("item")

    grouped_data = defaultdict(list)
    for item in items:
        if item["current_period"]:
            if item["specific_business"] is True:
                key = f"{item["report_type"]}_{item["xbrl_type"]}_{item["current_period"]}_specific_business"
            else:
                key = f"{item["report_type"]}_{item["xbrl_type"]}_{item["current_period"]}"
        else:
            if item["specific_business"] is True:
                key = f"{item["report_type"]}_{item["xbrl_type"]}_specific_business"
            else:
                key = f"{item["report_type"]}_{item["xbrl_type"]}"
        grouped_data[key].append(
            {"name": item["name"], "context": item["context"], "label": item["label"]}
        )

    # defaultdictを通常の辞書に変換
    grouped_data = {key: value for key, value in grouped_data.items()}

    json_path = os.path.join(
        os.path.dirname(__file__), "grouped_data_non_fraction.json"
    )
    with open(json_path, "w") as f:
        f.write(json.dumps(grouped_data, ensure_ascii=False, indent=4))

    return grouped_data


if __name__ == "__main__":

    base_url = "http://localhost:8000/api/v1"
    grouped_data = generate_module_non_fraction(base_url)
