from fastapi.routing import APIRouter

from manatee.api.endpoints import sessions, organizations

router = APIRouter()

router.include_router(sessions.router, prefix="/sessions")
router.include_router(organizations.router, prefix="/organizations")
