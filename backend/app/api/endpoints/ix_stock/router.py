import datetime

import sqlalchemy.exc
import yfinance as yf
from app.api.deps import SessionDep
from app.models import DailyStockPrice
from fastapi import APIRouter, HTTPException, Query
from sqlmodel import desc, select

from . import schema as sc
from . import utils

router = APIRouter()


@router.post("/daily_stock_price")
def create_daily_stock_price(
    *, session: SessionDep, date_str: str | None = Query(None), code: str
):
    """
    日次株価情報を作成
    """
    # date_strをdatetime.date型に変換
    if date_str:
        days = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    else:
        days = datetime.date.today()
    # yfinanceから株価情報を取得
    stock_data = utils.get_stock_data(code, days)
    if stock_data.empty:
        raise HTTPException(status_code=404, detail="Stock data not found")

    # # DataFrameを辞書に変換
    item_in = sc.DailyStockPriceCreate(
        code=code,
        days=days,
        open=stock_data["Open"].iloc[0],
        high=stock_data["High"].iloc[0],
        low=stock_data["Low"].iloc[0],
        close=stock_data["Close"].iloc[0],
        volume=stock_data["Volume"].iloc[0],
    )

    # # データベースに保存
    try:
        item = DailyStockPrice.model_validate(item_in)
        session.add(item)
        session.commit()
        session.refresh(item)
        return item_in
    except sqlalchemy.exc.IntegrityError as e:
        session.rollback()
        if "UNIQUE constraint failed" in str(e):
            raise HTTPException(
                status_code=400, detail="Stock data for this date already exists"
            )
        elif "duplicate key value violates unique constraint" in str(e):
            raise HTTPException(
                status_code=400, detail="Stock data for this date already exists"
            )
        else:
            raise HTTPException(status_code=500, detail="Database error")


@router.get(
    "/select_daily_stock_price",
    summary="日次株価情報を取得",
    response_model=sc.DailyStockPricePublic,
)
def get_daily_stock_price(
    *,
    session: SessionDep,
    date_str: str | None = Query(None, description="YYYY-MM-DD形式の日付"),
    stock_code: str | None = Query(None, description="株式コード"),
) -> sc.DailyStockPricePublic:
    """
    日次株価情報を取得
    """

    statement = select(DailyStockPrice).order_by(desc(DailyStockPrice.days))
    if date_str:
        days = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        statement = statement.where(DailyStockPrice.days == days)
    if stock_code:
        statement = statement.where(DailyStockPrice.code == stock_code)

    results = session.exec(statement)
    item = results.first()

    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    # Rowオブジェクトから辞書アクセスで値を取得
    return sc.DailyStockPricePublic.model_validate(item)
