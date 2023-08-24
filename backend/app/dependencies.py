from typing import Annotated
from typing import Any
from typing import TypeAlias

from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from fastapi.security import HTTPAuthorizationCredentials
from fastapi.security import HTTPBearer

from .utils.managers import Session
from .utils.managers import session_manager


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

# Dependency that the request has a current session available


def get_request_session(credentials: HTTPBearerCredentials) -> Session:
    session = session_manager.get(credentials.credentials)
    if session is None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    return session


DependsSession: TypeAlias = Annotated[Session, Depends(get_request_session)]
