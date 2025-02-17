from fastapi import APIRouter

from app.api.endpoints.ix_calc import router as ix_calc_router
from app.api.endpoints.ix_check import router as ix_check_router
from app.api.endpoints.ix_def import ix_definition
from app.api.endpoints.ix_head import ix_head_title
from app.api.endpoints.ix_lab import ix_label
from app.api.endpoints.ix_non_fraction import ix_non_fraction
from app.api.endpoints.ix_non_numeric import ix_non_numeric
from app.api.endpoints.ix_path import ix_file_path
from app.api.endpoints.ix_pre import ix_presentation
from app.api.endpoints.ix_qual import ix_qualitative
from app.api.endpoints.ix_schema import ix_schema
from app.api.endpoints.ix_source import ix_source
from app.api.endpoints.ix_summary import ix_summary
from app.api.endpoints.manager import items, login, users, utils
from app.api.endpoints.stock_wiki import jpx_stock_info, stock_wiki

api_router = APIRouter()

api_router.include_router(jpx_stock_info.router, prefix="/jpx/stock_info", tags=["jpx"])
api_router.include_router(ix_summary.router, prefix="/ix/summary", tags=["summary"])
api_router.include_router(stock_wiki.router, prefix="/wiki", tags=["wiki"])
api_router.include_router(
    ix_check_router.router,
    prefix="/xbrl/check",
    tags=["xbrl_check"],
    include_in_schema=False,
)
api_router.include_router(
    ix_head_title.router, prefix="/xbrl", tags=["xbrl_ix_head"], include_in_schema=False
)
api_router.include_router(
    ix_non_numeric.router, prefix="/xbrl", tags=["xbrl_ix"], include_in_schema=False
)
api_router.include_router(
    ix_non_fraction.router, prefix="/xbrl", tags=["xbrl_ix"], include_in_schema=False
)
api_router.include_router(
    ix_label.router, prefix="/xbrl", tags=["xbrl_lab"], include_in_schema=False
)
api_router.include_router(
    ix_calc_router.router, prefix="/xbrl", tags=["xbrl_cal"], include_in_schema=False
)
api_router.include_router(
    ix_definition.router, prefix="/def", tags=["xbrl_def"], include_in_schema=False
)
api_router.include_router(
    ix_presentation.router, prefix="/xbrl", tags=["xbrl_pre"], include_in_schema=False
)
api_router.include_router(
    ix_source.router, prefix="/xbrl", tags=["xbrl_source"], include_in_schema=False
)
api_router.include_router(
    ix_schema.router, prefix="/xbrl", tags=["xbrl_schema"], include_in_schema=False
)
api_router.include_router(
    ix_file_path.router,
    prefix="/xbrl",
    tags=["xbrl_file_path"],
    include_in_schema=False,
)
api_router.include_router(
    ix_qualitative.router,
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
