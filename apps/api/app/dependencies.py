from typing import Annotated
from typing import Any
from typing import TypeAlias

from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from fastapi.security import HTTPAuthorizationCredentials
from fastapi.security import HTTPBearer

from .core import Download
from .session import Session
from .session import session_manager

AdditionResponses: TypeAlias = dict[int | str, dict[str, Any]]

# Responses which should be included in all routes that depend on a session
depends_session_responses: AdditionResponses = {
    status.HTTP_403_FORBIDDEN: {},
}

# Request will include header with session ID as the bearer token
security = HTTPBearer()

HTTPBearerCredentials: TypeAlias = Annotated[
    HTTPAuthorizationCredentials, Depends(
        security,
    ),
]


def get_request_session(credentials: HTTPBearerCredentials) -> Session:
    session = session_manager.get(credentials.credentials)
    if session is None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    return session


# Dependency that the request has a current session available
DependsSession: TypeAlias = Annotated[Session, Depends(get_request_session)]


# Responses which should be included in all routes that depend on a download
depends_download_responses: AdditionResponses = depends_session_responses | {
    status.HTTP_404_NOT_FOUND: {},
}


def get_request_download(
    download_id: str, session: DependsSession,
) -> Download:
    download = session.download_manager.get(download_id)
    if download is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return download


# Dependency that the request has a current related download available
DependsDownload: TypeAlias = Annotated[
    Download, Depends(
        get_request_download,
    ),
]
