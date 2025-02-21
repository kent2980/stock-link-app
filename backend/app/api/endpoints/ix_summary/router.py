from fastapi import APIRouter, HTTPException, Query

from app.api.deps import SessionDep

from . import crud
from . import schema as sc
from . import utils
from .exceptions import HeadItemNotFound, NotDictKeyError

router = APIRouter()


@router.get(
    "/items/operating_results/{code}",
    summary="経営成績情報を取得",
    response_model=sc.FinancialResponseListSchema,
)
def get_operating_results(
    *,
    session: SessionDep,
    code: str,
) -> sc.FinancialResponseListSchema:

    headItems = crud.get_ix_head_title_by_code(session=session, code=code)

    if len(headItems) == 0:
        raise HTTPException(status_code=404, detail="Item not found")

    head_item_keys = [item.item_key for item in headItems]

    attr_value_dict = {
        "FY": "BusinessResultsOperatingResults",
        "QU": "BusinessResultsQuarterlyOperatingResults",
    }

    from_name_dict = {
        "consolidated": "tse-ed-t_ConsolidatedIncomeStatementsInformationAbstract",
        "non_consolidated": "tse-ed-t_IncomeStatementsInformationAbstract",
    }

    items_list = []
    from_labels = None
    for head_item_key in head_item_keys:
        try:
            items = utils.get_summary_items(
                session=session,
                head_item_key=head_item_key,
                attr_value_dict=attr_value_dict,
                from_name_dict=from_name_dict,
            )
            items_list.append(items[0])
            from_labels = items[1]
        except HeadItemNotFound as e:
            continue
        except NotDictKeyError as e:
            raise HTTPException(status_code=400, detail=str(e))

    return sc.FinancialResponseListSchema(
        data=items_list, count=len(items_list), labels=from_labels
    )
