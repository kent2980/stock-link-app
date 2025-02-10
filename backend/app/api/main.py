from fastapi import APIRouter

from app.api.routes import (
    items,
    ix_calculation,
    ix_check,
    ix_definition,
    ix_file_path,
    ix_head_title,
    ix_label,
    ix_non_fraction,
    ix_non_numeric,
    ix_presentation,
    ix_qualitative,
    ix_schema,
    ix_source,
    ix_summary,
    jpx_stock_info,
    login,
    users,
    utils,
)

api_router = APIRouter()
api_router.include_router(jpx_stock_info.router, prefix="/jpx/stock_info", tags=["jpx"])
api_router.include_router(ix_summary.router, prefix="/ix/summary", tags=["summary"])
api_router.include_router(
    ix_check.router, prefix="/xbrl/check", tags=["xbrl_check"], include_in_schema=False
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
    ix_calculation.router, prefix="/xbrl", tags=["xbrl_cal"], include_in_schema=False
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
api_router.include_router(login.router, tags=["login"], include_in_schema=False)
api_router.include_router(
    users.router, prefix="/users", tags=["users"], include_in_schema=False
)
api_router.include_router(
    utils.router, prefix="/utils", tags=["utils"], include_in_schema=False
)
api_router.include_router(
    items.router, prefix="/items", tags=["items"], include_in_schema=False
)
