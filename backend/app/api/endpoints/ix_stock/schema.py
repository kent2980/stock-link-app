import datetime

from app.models import Field, SQLModel


class DailyStockPricePublic(SQLModel):
    """日次株価情報を公開するためのクラス"""

    code: str
    days: datetime.date
    open: float
    high: float
    low: float
    close: float
    volume: int | None = Field(default=None)
    adjusted_close: float | None = Field(default=None)

    class Config:
        """Config for SQLModel"""

        orm_mode = True


class DailyStockPricePublicList(SQLModel):
    """日次株価情報を公開するためのクラス"""

    data: list[DailyStockPricePublic]
    count: int


class DailyStockPriceCreate(SQLModel):
    """日次株価情報を作成するためのクラス"""

    code: str
    days: datetime.date
    open: float
    high: float
    low: float
    close: float
    volume: int | None = Field(default=None)
    adjusted_close: float | None = Field(default=None)
