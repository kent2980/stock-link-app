import app.schema as sc
from app.api.deps import SessionDep
from app.models import (
    IxHeadTitle,
    IxLabelArc,
    IxLabelLoc,
    IxLabelValue,
    IxNonFraction,
    ScLinkBaseRef,
)
from fastapi import APIRouter
from sqlmodel import and_, select

router = APIRouter()


@router.get(
    "/grouping/non_fraction/",
    response_model=sc.ix_generate_class.GroupingNonFractionList,
)
def get_grouping_non_fraction(
    *,
    session: SessionDep,
) -> sc.ix_generate_class.GroupingNonFractionList:
    """分数でないグルーピングされた項目名とコンテキストを取得する"""
    statement = (
        select(
            IxHeadTitle.report_type,
            IxHeadTitle.specific_business,
            IxNonFraction.xbrl_type,
            IxHeadTitle.current_period,
            IxNonFraction.name,
            IxNonFraction.context,
            IxLabelValue.label,
        )
        .join(IxHeadTitle, IxNonFraction.head_item_key == IxHeadTitle.item_key)
        .join(ScLinkBaseRef, ScLinkBaseRef.head_item_key == IxNonFraction.head_item_key)
        .join(
            IxLabelLoc,
            and_(
                ScLinkBaseRef.href_source_file_id == IxLabelLoc.source_file_id,
                IxNonFraction.name == IxLabelLoc.xlink_href,
            ),
        )
        .join(
            IxLabelArc,
            and_(
                ScLinkBaseRef.href_source_file_id == IxLabelArc.source_file_id,
                IxLabelLoc.xlink_label == IxLabelArc.xlink_from,
            ),
        )
        .join(
            IxLabelValue,
            and_(
                ScLinkBaseRef.href_source_file_id == IxLabelValue.source_file_id,
                IxLabelArc.xlink_to == IxLabelValue.xlink_label,
            ),
        )
        .where(
            IxNonFraction.name.op("!~")("^tse-[a-z]{8}-[0-9]{5}.*"),
            IxNonFraction.context.op("!~")(".*tse-[a-z]{8}-[0-9]{5}.*"),
            IxLabelValue.xlink_role == "http://www.xbrl.org/2003/role/verboseLabel",
        )
        .group_by(
            IxHeadTitle.report_type,
            IxHeadTitle.specific_business,
            IxNonFraction.xbrl_type,
            IxHeadTitle.current_period,
            IxNonFraction.name,
            IxNonFraction.context,
            IxLabelValue.label,
        )
        .order_by(
            IxHeadTitle.report_type.asc(),
            IxHeadTitle.specific_business.asc(),
            IxNonFraction.xbrl_type.asc(),
            IxHeadTitle.current_period.asc(),
            IxNonFraction.name.asc(),
            IxNonFraction.context.asc(),
        )
    )
    result = session.exec(statement)
    name_list = result.all()

    return sc.ix_generate_class.GroupingNonFractionList(
        item=name_list, count=len(name_list)
    )
