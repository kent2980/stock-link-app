from app.models import IxNonFraction
from sqlmodel import Session, select, func

def number_of_submission_dei(session: Session, head_item_key:str, context:str):
    """
    提出回数、DEI
    """
    statement = (
        select(IxNonFraction)
        .where(
            IxNonFraction.name == 'jpdei_cor_NumberOfSubmissionDEI',
            IxNonFraction.head_item_key == head_item_key,
            IxNonFraction.context == context,
        )
    )
    result = session.exec(statement)
    item = result.all()
    if len(item) > 1:
        raise ValueError('複数のデータが取得されました。contextが不足しています。')
    elif len(item) < 1:
        raise ValueError('データが取得されませんでした。')
    return item[0]

