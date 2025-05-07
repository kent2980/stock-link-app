from fastapi import APIRouter

from app.api.endpoints.ix_calc import router as ix_calc_router
from app.api.endpoints.ix_check import router as ix_check_router
from app.api.endpoints.ix_def import router as ix_def_router
from app.api.endpoints.ix_head import router as ix_head_router
from app.api.endpoints.ix_info import router as ix_info_router
from app.api.endpoints.ix_lab import router as ix_lab_router
from app.api.endpoints.ix_non_fraction import router as ix_non_fraction_router
from app.api.endpoints.ix_non_numeric import router as ix_non_numeric_router
from app.api.endpoints.ix_path import router as ix_path_router
from app.api.endpoints.ix_pre import router as ix_pre_router
from app.api.endpoints.ix_qual import router as ix_qual_router
from app.api.endpoints.ix_schema import router as ix_schema_router
from app.api.endpoints.ix_source import router as ix_source_router
from app.api.endpoints.ix_summary import router as ix_summary_router
from app.api.endpoints.ix_summary2 import router as ix_summary2_router
from app.api.endpoints.jpx_info import router as jpx_info_router
from app.api.endpoints.manager.router import items, login, users, utils
from app.api.endpoints.stock_wiki import router as stock_wiki_router

api_router = APIRouter()

api_router.include_router(
    ix_info_router.router, prefix="/ix/stock_info", tags=["Information"]
)
api_router.include_router(
    jpx_info_router.router, prefix="/jpx/stock_info", tags=["Jpx"]
)
api_router.include_router(
    ix_summary_router.router, prefix="/ix/summary", tags=["FinancialSummary"]
)
api_router.include_router(
    ix_summary2_router.router, prefix="/ix/summary2", tags=["FinancialSummary2"]
)
api_router.include_router(stock_wiki_router.router, prefix="/wiki", tags=["wiki"])
api_router.include_router(
    ix_check_router.router,
    prefix="/xbrl/check",
    tags=["xbrl_check"],
    include_in_schema=False,
)
api_router.include_router(
    ix_head_router.router,
    prefix="/xbrl",
    tags=["Information"],
    include_in_schema=True,
)
api_router.include_router(
    ix_non_fraction_router.router,
    prefix="/xbrl",
    tags=["xbrl_ix"],
    include_in_schema=False,
)
api_router.include_router(
    ix_non_numeric_router.router,
    prefix="/xbrl",
    tags=["xbrl_ix"],
    include_in_schema=False,
)
api_router.include_router(
    ix_lab_router.router, prefix="/xbrl", tags=["xbrl_lab"], include_in_schema=False
)
api_router.include_router(
    ix_calc_router.router, prefix="/xbrl", tags=["xbrl_cal"], include_in_schema=False
)
api_router.include_router(
    ix_def_router.router, prefix="/def", tags=["xbrl_def"], include_in_schema=False
)
api_router.include_router(
    ix_pre_router.router, prefix="/xbrl", tags=["xbrl_pre"], include_in_schema=False
)
api_router.include_router(
    ix_source_router.router,
    prefix="/xbrl",
    tags=["xbrl_source"],
    include_in_schema=False,
)
api_router.include_router(
    ix_schema_router.router,
    prefix="/xbrl",
    tags=["xbrl_schema"],
    include_in_schema=False,
)
api_router.include_router(
    ix_path_router.router,
    prefix="/xbrl",
    tags=["xbrl_file_path"],
    include_in_schema=False,
)
api_router.include_router(
    ix_qual_router.router,
    prefix="/xbrl",
    tags=["xbrl_qualitative"],
    include_in_schema=False,
)
api_router.include_router(login.router, tags=["login"], include_in_schema=True)
api_router.include_router(
    users.router, prefix="/users", tags=["users"], include_in_schema=True
)
api_router.include_router(
    utils.router, prefix="/utils", tags=["utils"], include_in_schema=True
)
api_router.include_router(
    items.router, prefix="/items", tags=["items"], include_in_schema=True
)

tags_metadata = [
    {
        "name": "Information",
        "description": "インフォメーションデータに関連する操作。",
    },
    {
        "name": "Jpx",
        "description": "マーケット情報に関連する操作。",
    },
    {
        "name": "FinancialSummary",
        "description": "財務要約データに関連する操作。",
    },
    {
        "name": "wiki",
        "description": "Wikipediaから銘柄の情報を取得する操作。",
    },
    {
        "name": "login",
        "description": "ユーザーログイン操作のエンドポイント。",
    },
    {
        "name": "users",
        "description": "ユーザー管理のエンドポイント。",
    },
    {
        "name": "utils",
        "description": "さまざまな操作のためのユーティリティエンドポイント。",
    },
    {
        "name": "items",
        "description": "アイテム管理のエンドポイント。",
    },
]
