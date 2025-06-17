from fastapi import APIRouter, Query
from sqlmodel import select

from app.api.deps import SessionDep
from app.models import IxHeadTitle, IxHeadTitleSummary

from . import schema as sc
from . import utils
from .exceptions import HeadItemNotFound

router = APIRouter()


@router.post(
    "/ix_title_summary/all/",
    summary="iXBRLのヘッダー情報の要約レコードを書き込む",
    response_model=int,
)
def post_ix_title_summaries(
    *,
    session: SessionDep,
) -> int:
    """
    Get IX title summaries.
    """

    # 要約が取得されていない全てのKeyを取得
    statement = (
        select(IxHeadTitle)
        .outerjoin(
            IxHeadTitleSummary,
            IxHeadTitle.item_key == IxHeadTitleSummary.head_item_key,
        )
        .where(IxHeadTitleSummary.summary.is_(None))
    )

    items = session.exec(statement)
    if not items:
        raise HeadItemNotFound(
            status_code=404,
            detail="要約はすでに取得されています。",
        )

    # 要約を取得
    BATCH_SIZE = 1000  # 一度に処理するバッチサイズ
    buffer = []
    count = 0

    for item in items:
        try:
            try:
                summary = utils.get_financial_summary(
                    session=session, head_item_key=item.item_key, offset=0
                )
            except HeadItemNotFound:
                summary = ""
            try:
                ope = utils.get_operating_results(
                    session=session, head_item_key=item.item_key, offset=0
                )
            except HeadItemNotFound:
                ope = None
            try:
                forecast = utils.get_forecasts(
                    session=session, code=None, head_item_key=item.item_key, offset=0
                )
            except HeadItemNotFound:
                forecast = None
            try:
                cashflow = utils.get_cash_flows(
                    session=session,
                    code=item.securities_code,
                    year=item.fy_year_end[0:4] if item.fy_year_end else None,
                    offset=0 if item.current_period == "FY" else 1,
                )
            except HeadItemNotFound:
                cashflow = None
            data = sc.IxSummaryResponseCreate(
                head_item_key=item.item_key,
                summary=summary,
                operating_result_json=ope.model_dump_json() if ope else None,
                forecast_json=forecast.model_dump_json() if forecast else None,
                cashflow_json=cashflow.model_dump_json() if cashflow else None,
            )
            buffer.append(IxHeadTitleSummary.model_validate(data))
        except Exception as e:
            print(f"Error processing key {item.item_key}: {str(e)}")
            # ヘッドアイテムが見つからない場合はスキップ
            continue

        if len(buffer) >= BATCH_SIZE:
            session.bulk_save_objects(buffer)
            session.commit()
            count += len(buffer)
            buffer.clear()

    # 残りのデータを保存
    if buffer:
        session.bulk_save_objects(buffer)
        session.commit()
        count += len(buffer)

    return count


@router.post(
    "/ix_title_summary/item/",
    summary="iXBRLのヘッダー情報の要約レコードを作成",
    response_model=sc.IxSummaryResponseCreate,
)
def post_ix_title_summary_item(
    *,
    session: SessionDep,
    head_item_key: str = Query(..., description="ヘッドアイテムキー"),
) -> int:
    statement = select(IxHeadTitle).where(IxHeadTitle.item_key == head_item_key)
    result = session.exec(statement).first()
    code = result.securities_code if result else None
    fy_year_end = result.fy_year_end if result else None
    current_period = result.current_period if result else None
    item = sc.IxSummaryResponseCreate(head_item_key=head_item_key)

    print(
        f"Processing head_item_key: {head_item_key}, code: {code}, fy_year_end: {fy_year_end}, current_period: {current_period}"
    )
    try:
        try:
            summary = utils.get_financial_summary(
                session=session, head_item_key=head_item_key, offset=0
            )
        except HeadItemNotFound:
            summary = ""
        try:
            ope = utils.get_operating_results(
                session=session, code=None, head_item_key=head_item_key, offset=0
            )
        except HeadItemNotFound:
            ope = None
        try:
            forecast = utils.get_forecasts(
                session=session, code=None, head_item_key=head_item_key, offset=0
            )
        except HeadItemNotFound:
            forecast = None
        try:
            cashflow = utils.get_cash_flows(
                session=session,
                code=code,
                year=fy_year_end[0:4] if fy_year_end else None,
                offset=0 if current_period == "FY" else 1,
            )
        except HeadItemNotFound:
            cashflow = None
        item.summary = summary
        item.operating_result_json = ope.model_dump_json() if ope else None
        item.forecast_json = forecast.model_dump_json() if forecast else None
        item.cashflow_json = cashflow.model_dump_json() if cashflow else None
    except Exception as e:
        raise HeadItemNotFound(
            status_code=404,
            detail=f"ヘッドアイテムキー {head_item_key} の要約が見つかりません: {str(e)}",
        )

    new_item = IxHeadTitleSummary.model_validate(item)

    try:
        session.add(new_item)
        session.commit()
        session.refresh(new_item)
    except Exception as e:
        session.rollback()
        raise HeadItemNotFound(
            status_code=500,
            detail=f"要約の保存に失敗しました: {str(e)}",
        )

    return new_item


@router.patch(
    "/ix_title_summary/all/",
    summary="iXBRLのヘッダー情報の要約レコードを更新",
    response_model=int,
)
def patch_ix_title_summary_all(
    *,
    session: SessionDep,
) -> int:
    statement = (
        select(IxHeadTitleSummary, IxHeadTitle)
        .join(IxHeadTitle, IxHeadTitle.item_key == IxHeadTitleSummary.head_item_key)
        .where(IxHeadTitleSummary.summary.is_not(None))
    )

    count = 0
    BATCH_SIZE = 100
    batch = []

    for summary in session.exec(statement):
        try:
            head_item_key = summary[0].head_item_key
            code = summary[1].securities_code
            updated = False
            print(f"{count}.Processing head_item_key: {head_item_key}, code: {code}")
            if not summary[0].operating_result_json:
                try:
                    summary[0].operating_result_json = utils.get_operating_results(
                        session=session,
                        code=None,
                        head_item_key=head_item_key,
                        offset=0,
                    ).model_dump_json()
                    updated = True
                except Exception:
                    summary[0].operating_result_json = None
            if not summary[0].forecast_json:
                try:
                    summary[0].forecast_json = utils.get_forecasts(
                        session=session,
                        code=None,
                        head_item_key=head_item_key,
                        offset=0,
                    ).model_dump_json()
                    updated = True
                except Exception:
                    summary[0].forecast_json = None
            if not summary[0].cashflow_json:
                try:
                    summary[0].cashflow_json = utils.get_cash_flows(
                        session=session,
                        code=code,
                        year=summary[1].fy_year_end[0:4],
                        offset=0 if summary[1].current_period == "FY" else 1,
                    ).model_dump_json()
                    updated = True
                except Exception:
                    summary[0].cashflow_json = None
            if updated:
                batch.append(summary[0])
                count += 1
            if len(batch) >= BATCH_SIZE:
                print(f"Committing batch of {len(batch)} summaries...")
                session.commit()
                batch.clear()
                print(f"Updated {count} summaries so far...")
        except Exception as e:
            print(f"Error processing head_item_key {head_item_key}: {str(e)}")
            continue

    if batch:
        print(f"Committing final batch of {len(batch)} summaries...")
        session.commit()
        print(f"Updated {count} summaries so far...")

    return count
