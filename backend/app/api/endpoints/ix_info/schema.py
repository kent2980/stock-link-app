import datetime
from typing import Optional

from sqlmodel import Field, SQLModel


class DocumentListPublic(SQLModel):
    id: int
    head_item_key: str
    insert_date: datetime.datetime
    securities_code: str
    company_name: str
    document_name: str
    document_short_name: str
    report_type: str


class DocumentListPublics(SQLModel):
    count: int
    data: list[DocumentListPublic]
