import sys

import requests

# FastAPIサーバーのURLを引数から取得
BASE_URL = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:8000"


def post_ix_title_summary_all():
    url = f"{BASE_URL}/api/v1/ix/summary/ix_title_summary/all/"
    try:
        print(f"POSTリクエストを送信: {url}")
        response = requests.post(url)
        response.raise_for_status()
        print(f"成功: {response.json()} 件の要約レコードを書き込みました。")
    except requests.HTTPError as e:
        print(f"HTTPエラー: {e.response.status_code} {e.response.text}")
    except Exception as e:
        print(f"エラー: {str(e)}")


if __name__ == "__main__":
    post_ix_title_summary_all()
