from app.api.routes import (
    items,
    ix_calculation,
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
    ix_view,
    login,
    users,
    utils,
)
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(ix_view.router, prefix="/xbrl/view", tags=["xbrl_view"])
api_router.include_router(ix_head_title.router, prefix="/xbrl", tags=["xbrl_ix"])
api_router.include_router(ix_non_numeric.router, prefix="/xbrl", tags=["xbrl_ix"])
api_router.include_router(ix_non_fraction.router, prefix="/xbrl", tags=["xbrl_ix"])
api_router.include_router(ix_label.router, prefix="/xbrl", tags=["xbrl_lab"])
api_router.include_router(ix_calculation.router, prefix="/xbrl", tags=["xbrl_cal"])
api_router.include_router(ix_definition.router, prefix="/xbrl", tags=["xbrl_def"])
api_router.include_router(ix_presentation.router, prefix="/xbrl", tags=["xbrl_pre"])
api_router.include_router(ix_source.router, prefix="/xbrl", tags=["xbrl_source"])
api_router.include_router(ix_schema.router, prefix="/xbrl", tags=["xbrl_schema"])
api_router.include_router(ix_file_path.router, prefix="/xbrl", tags=["xbrl_file_path"])
api_router.include_router(
    ix_qualitative.router, prefix="/xbrl", tags=["xbrl_qualitative"]
)
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(utils.router, prefix="/utils", tags=["utils"])
api_router.include_router(items.router, prefix="/items", tags=["items"])
