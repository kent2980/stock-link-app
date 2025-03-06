from typing import Optional

from sqlmodel import Field, SQLModel


class DocumentListPublic(SQLModel):
    id: int
    securities_code: str
    company_name: str
    document_name: str


class DocumentListPublics(SQLModel):
    count: int
    data: list[DocumentListPublic]
