import json
import os
from collections import defaultdict

import requests
from app.utils import summary


def get_grouping_dict(items):

    grouped_data = defaultdict(list)
    for item in items:
        key = summary.generate_non_fraction_key(item)
        grouped_data[key].append(
            {
                "name": item["name"],
                "context": item["context"],
                "label": item["label"],
                "context_label": item["context_label"],
            }
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
        grouped_context = {}
        for item in grouping_data[key]:
            if item["name"] not in grouped_context:
                grouped_context[item["name"]] = {"label": item["label"], "item": []}
            grouped_context[item["name"]]["item"].append(
                {"context": item["context"], "context_label": item["context_label"]}
            )
        grouped_keys[key] = grouped_context

    base_dir = os.path.dirname(__file__)
    json_path = os.path.join(base_dir, "../../json/non_fraction/name_context.json")
    with open(json_path, "w") as f:
        f.write(json.dumps(grouped_keys, ensure_ascii=False, indent=4))


if __name__ == "__main__":
    base_url = "http://localhost:8000/api/v1"
    generate_schema(base_url)
