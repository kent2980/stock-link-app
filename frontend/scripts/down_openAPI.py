from pathlib import Path

import requests

json_url = "http://localhost:8000/api/v1/openapi.json"
json_file = "openapi.json"
download_dir = Path(__file__).resolve().parent.parent.parent / "frontend"

# 既にファイルが存在する場合は削除
import os

if os.path.exists(f"{download_dir}/{json_file}"):
    os.remove(f"{download_dir}/{json_file}")

r = requests.get(json_url)
with open(f"{download_dir}/{json_file}", "wb") as f:
    f.write(r.content)
    print(f"{json_file} downloaded")
