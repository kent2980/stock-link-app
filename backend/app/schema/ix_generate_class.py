from typing import List, Optional

from app.models import SQLModel


class NameItem(SQLModel):
    name: str
    label: str


class ContextItem(SQLModel):
    context: str
    label: str


class ContextList(SQLModel):
    item: List[ContextItem]
    label: str


class GroupingNonFraction(SQLModel):
    report_type: Optional[str]
    specific_business: Optional[bool]
    xbrl_type: Optional[str]
    current_period: Optional[str]
    name: str
    context: str
    label: Optional[str]


class GroupingNonFractionList(SQLModel):
    count: int
    item: List[GroupingNonFraction]
