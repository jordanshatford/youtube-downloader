from fastapi import APIRouter
from fastapi import Request
from fastapi import status

from app.core import CORE_VERSIONS
from app.core import Version
from app.dependencies import DependsSession
from app.dependencies import depends_session_responses

router = APIRouter(
    prefix="/versions",
    tags=["versions"],
    responses=depends_session_responses
    | {
        status.HTTP_404_NOT_FOUND: {},
    },
)


@router.get("")
def get_versions(_: DependsSession, request: Request) -> list[Version]:
    return [
        *CORE_VERSIONS,
        Version(component="API", version=request.app.version),
    ]
