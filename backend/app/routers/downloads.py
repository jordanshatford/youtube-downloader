import asyncio
import os
import queue

from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import Request
from fastapi import status
from fastapi.responses import FileResponse
from sse_starlette.sse import EventSourceResponse

from ..dependencies import depends_download_responses
from ..dependencies import depends_session_responses
from ..dependencies import DependsDownload
from ..dependencies import DependsSession
from ..models import StatusUpdate
from ..models import Video
from ..utils.managers import Session
from ..utils.managers import session_manager

router = APIRouter(
    prefix='/downloads',
    tags=['downloads'],
    responses=depends_session_responses,
)


@router.get('')
def get_downloads(session: DependsSession) -> list[Video]:
    return session.download_manager.get_all_videos()


@router.post('', status_code=status.HTTP_201_CREATED)
def post_downloads(video: Video, session: DependsSession) -> Video:
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


@router.get('/{video_id}', responses=depends_download_responses)
def get_download(download: DependsDownload) -> Video:
    return download.video


@router.get(
    '/{video_id}/file', response_class=FileResponse, responses={
        **depends_download_responses,
        status.HTTP_200_OK: {
            'content': {'audio/*': {'schema': {'type': 'file'}}},
        },
    },
)
def get_download_file(download: DependsDownload):
    if os.path.exists(download.get_file_location()):
        return FileResponse(download.get_file_location())
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@router.get('/{video_id}/status', responses=depends_download_responses)
def get_download_status(download: DependsDownload) -> StatusUpdate:
    return StatusUpdate(id=download.video.id, status=download.status)


@router.delete(
    '/{video_id}', status_code=status.HTTP_204_NO_CONTENT,
    responses=depends_download_responses,
)
def delete_download(
    download: DependsDownload,
    session: DependsSession,
) -> None:
    session.download_manager.remove(download.video.id)