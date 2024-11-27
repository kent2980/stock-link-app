import json
import os
from collections import defaultdict

import requests


def get_grouping_dict(items):

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

    return grouped_data


def generate_schema(base_url: str):

    url = f"{base_url}/generate/grouping/non_fraction/"
    response = requests.get(url)
    items = response.json().get("item")

    grouping_data = get_grouping_dict(items)

    grouped_keys = defaultdict(list)
    for key in grouping_data.keys():
        grouped_context = defaultdict(list)
        print(key)
        for item in grouping_data[key]:
            print(item)
            grouped_context[item["name"]].append(item["context"])
        grouped_keys[key] = grouped_context

    print(grouped_keys)

    base_dir = os.path.dirname(__file__)
    json_path = os.path.join(base_dir, "../json/grouped_data_non_fraction_name.json")
    with open(json_path, "w") as f:
        f.write(json.dumps(grouped_keys, ensure_ascii=False, indent=4))


if __name__ == "__main__":
    base_url = "http://localhost:8000/api/v1"
    generate_schema(base_url)
