import datetime
from typing import Optional

from sqlmodel import SQLModel


class DocumentListPublic(SQLModel):
    id: int
    head_item_key: str
    insert_date: datetime.datetime
    securities_code: str
    company_name: str
    document_name: str
    document_short_name: str
    report_type: str
    url: Optional[str]
    period_index: Optional[int]
    current_period: Optional[str]


class DocumentListPublics(SQLModel):
    count: int
    data: list[DocumentListPublic]
