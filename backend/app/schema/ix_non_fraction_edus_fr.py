from app.models import Field, SQLModel
from app.schema.ix_non_fraction import IxNonFractionPublic
from typing import Optional

class IxNonFractionEdusFr(SQLModel):
    number_of_submission_dei: Optional[IxNonFractionPublic] = Field(default=None, description='提出回数、DEI')
    """ 提出回数、DEI """

