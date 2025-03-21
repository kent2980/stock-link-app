import json
import os
from collections import defaultdict

import requests
from app.utils import summary


def get_grouping_dict(items):

    grouped_data = defaultdict(list)
    for item in items:
        key = summary.generate_non_numeric_key(item)
        grouped_data[key].append(
            {
                "name": item["name"],
                # "context": item["context"],
                "label": item["label"],
                # "context_label": item["context_label"],
            }
        )

    # defaultdictを通常の辞書に変換
    grouped_data = {key: value for key, value in grouped_data.items()}

    return grouped_data


def generate_module_non_numeric(base_url: str):

    url = f"{base_url}/generate/grouping/non_numeric/"
    response = requests.get(url)
    items = response.json().get("item")

    grouped_data = get_grouping_dict(items)

    base_dir = os.path.dirname(__file__)
    json_path = os.path.join(base_dir, "../../json/non_numeric/grouped_data.json")
    with open(json_path, "w") as f:
        f.write(json.dumps(grouped_data, ensure_ascii=False, indent=4))

    return grouped_data


if __name__ == "__main__":

    base_url = "http://localhost:8000/api/v1"
    grouped_data = generate_module_non_numeric(base_url)
