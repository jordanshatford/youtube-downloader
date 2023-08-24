import asyncio
import os
import queue

from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import Request
from fastapi import status
from fastapi.responses import FileResponse
from sse_starlette.sse import EventSourceResponse

from ..dependencies import depends_session_responses
from ..dependencies import DependsSession
from ..models import StatusUpdate
from ..models import Video
from ..utils.managers import Session
from ..utils.managers import session_manager

router = APIRouter(
    prefix='/downloads',
    tags=['downloads'],
    responses={
        **depends_session_responses,
        status.HTTP_404_NOT_FOUND: {},
    },
)


@router.post('', status_code=status.HTTP_201_CREATED)
def post_download(video: Video, session: DependsSession) -> Video:
    session.download_manager.add(video)
    return video


async def status_stream(request: Request, session: Session):
    try:
        while True:
            if await request.is_disconnected():
                break
            try:
                update = session.status_queue.get(block=False)
                yield dict(data=update.json())
            except queue.Empty:
                pass
            await asyncio.sleep(1)
    except (asyncio.CancelledError, asyncio.exceptions.InvalidStateError):
        session_manager.remove(session.id)


# Exclude from OpenAPI schema as there is no support for Server Sent Events.
@router.get('/status', include_in_schema=False)
async def get_downloads_status(request: Request, session_id: str):
    session = session_manager.get(session_id)
    if session is None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    event_source = status_stream(request, session)
    return EventSourceResponse(event_source)


@router.get('/{video_id}')
def get_download(video_id: str, session: DependsSession) -> Video:
    download = session.download_manager.get(video_id)
    if download is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    else:
        return download.video


@router.get(
    '/{video_id}/file', response_class=FileResponse, responses={
        status.HTTP_200_OK: {
            'content': {'audio/*': {'schema': {'type': 'file'}}},
        },
    },
)
def get_download_file(video_id: str, session: DependsSession):
    download = session.download_manager.get(video_id)
    if download is not None and os.path.exists(download.get_file_location()):
        return FileResponse(download.get_file_location())
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@router.get('/{video_id}/status')
def get_download_status(video_id: str, session: DependsSession) -> StatusUpdate:  # noqa: E501
    download = session.download_manager.get(video_id)
    if download is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    else:
        return StatusUpdate(id=download.video.id, status=download.status)


@router.delete('/{video_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_download(video_id: str, session: DependsSession) -> None:
    if video_id in session.download_manager:
        session.download_manager.remove(video_id)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
