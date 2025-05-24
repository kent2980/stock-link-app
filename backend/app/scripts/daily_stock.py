import datetime
import sys

import requests

if __name__ == "__main__":

    # 引数からAPIベースURLを取得
    if len(sys.argv) > 1:
        api_base_url = sys.argv[1]
    else:
        api_base_url = "http://localhost:8000"
    if len(sys.argv) > 2:
        date_str = sys.argv[2]
    else:
        date_str = datetime.datetime.now().strftime("%Y-%m-%d")
    # APIエンドポイントを指定
    api_endpoint = "/api/v1/ix/stock/daily_stock_price"

    def fetch_stock_price(ticker, api_base_url, api_endpoint, date_str):
        url = f"{api_base_url}{api_endpoint}"
        params = {
            "code": ticker,
            "date_str": date_str,
        }
        response = requests.post(url, params=params)
        if response.status_code == 200:
            print(f"{ticker}を取得しました({date_str})")
        else:
            print(
                f"{ticker}の取得に失敗しました: {response.status_code} {response.text}"
            )

    # 日経平均株価とTOPIXを取得
    for ticker in ["^N225"]:
        fetch_stock_price(ticker, api_base_url, api_endpoint, date_str)
