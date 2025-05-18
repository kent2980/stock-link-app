import datetime

from sqlmodel import Field, SQLModel


class DocumentListPublic(SQLModel):
    id: int
    head_item_key: str
    insert_date: datetime.datetime
    securities_code: str
    company_name: str
    document_name: str
    document_short_name: str | None = Field(default=None)
    report_type: str
    url: str | None = Field(default=None)
    period_index: int | None = Field(default=None)
    current_period: str | None = Field(default=None)
    report_date: datetime.date | None = Field(default=None)


class DocumentListPublics(SQLModel):
    count: int
    data: list[DocumentListPublic]


class UrlSchema(SQLModel):
    """URLを表すクラス"""

    url: str = Field(description="URL")
    securities_code: str = Field(description="証券コード")


class UrlSchemaList(SQLModel):
    """URLのリストを表すクラス"""

    data: list[UrlSchema]
    count: int


class PublicCalender(SQLModel):
    reporting_date: datetime.date
    count: int


class PublicCalenders(SQLModel):
    count: int
    data: list[PublicCalender]


class PublicLatestReportingDate(SQLModel):
    """最新の報告日を表すクラス"""

    reporting_date: datetime.date = Field(description="最新の報告日")
    count: int = Field(description="件数")
