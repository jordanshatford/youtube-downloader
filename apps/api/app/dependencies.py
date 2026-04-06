from typing import Annotated
from typing import Any

from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from fastapi.security import HTTPAuthorizationCredentials
from fastapi.security import HTTPBearer

from .core import Download
from .session import Session
from .session import session_manager

type AdditionalResponses = dict[int | str, dict[str, Any]]

# Responses which should be included in all routes that depend on a session
depends_session_responses: AdditionalResponses = {
    status.HTTP_403_FORBIDDEN: {},
}

# Request will include header with session ID as the bearer token
security = HTTPBearer()

type HTTPBearerCredentials = Annotated[
    HTTPAuthorizationCredentials,
    Depends(
        security,
    ),
]


def get_request_session(credentials: HTTPBearerCredentials) -> Session:
    session = session_manager.get(credentials.credentials)
    if session is None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    return session


# Dependency that the request has a current session available
type DependsSession = Annotated[Session, Depends(get_request_session)]


def get_request_query_session(session_id: str) -> Session:
    session = session_manager.get(session_id)
    if session is None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    return session


# Dependency that the request has a current session available via query parameters
type DependsSessionInQuery = Annotated[Session, Depends(get_request_query_session)]


# Responses which should be included in all routes that depend on a download
depends_download_responses: AdditionalResponses = depends_session_responses | {
    status.HTTP_404_NOT_FOUND: {},
}


def get_request_download(
    download_id: str,
    session: DependsSession,
) -> Download:
    download = session.downloads.get(download_id)
    if download is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return download


# Dependency that the request has a current related download available
type DependsDownload = Annotated[
    Download,
    Depends(
        get_request_download,
    ),
]
