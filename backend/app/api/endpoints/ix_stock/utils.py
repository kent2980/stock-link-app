import datetime
import time

import yfinance as yf


def get_stock_data(code: str, days: datetime.date) -> dict:
    """
    yfinanceから株価情報を取得
    """
    # APIサーバーの負荷を考慮して１秒待機
    time.sleep(1)

    # yfinanceから株価情報を取得
    ticker = yf.Ticker(code)
    stock_data = ticker.history(start=days, end=days + datetime.timedelta(days=1))
    return stock_data
