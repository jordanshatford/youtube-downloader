import asyncio
import os
import queue

from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import Request
from fastapi import status
from fastapi.responses import FileResponse
from sse_starlette.sse import EventSourceResponse
from utils.managers import session_manager
from utils.models import StatusUpdate
from utils.models import Video

router = APIRouter()


@router.post('/downloads', tags=['downloads'], status_code=status.HTTP_201_CREATED)  # noqa E501
def post_download(video: Video, session_id: str) -> Video:
    download_manager = session_manager.get_download_manager(session_id)
    download_manager.add(video)
    return video


async def status_stream(request: Request, session_id: str):
    try:
        while True:
            if await request.is_disconnected():
                break
            try:
                update = session_manager.get_status_queue(
                    session_id,
                ).get(block=False)
                yield dict(data=update.json())
            except queue.Empty:
                pass
            await asyncio.sleep(1)
    except (asyncio.CancelledError, asyncio.exceptions.InvalidStateError):
        session_manager.remove(session_id)


@router.get('/downloads/status', tags=['downloads'], include_in_schema=False)
async def get_downloads_status(request: Request, session_id: str):
    event_source = status_stream(request, session_id=session_id)
    return EventSourceResponse(event_source)


@router.get(
    '/downloads/{video_id}', tags=['downloads'], responses={
        status.HTTP_404_NOT_FOUND: {
            'description': 'Download not found.',
        },
    },
)
def get_download(video_id: str, session_id: str) -> Video:
    download_manager = session_manager.get_download_manager(session_id)
    download = download_manager.get(video_id)
    if download is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    else:
        return download.video


@router.get(
    '/downloads/{video_id}/file', tags=['downloads'], response_class=FileResponse, responses={  # noqa E501
        status.HTTP_200_OK: {
            'content': {'audio/*': {'schema': {'type': 'file'}}},
        },
        status.HTTP_404_NOT_FOUND: {
            'description': 'File not found.',
        },
    },
)
def get_download_file(video_id: str, session_id: str):
    download_manager = session_manager.get_download_manager(session_id)
    download = download_manager.get(video_id)
    if download is not None and os.path.exists(download.get_file_location()):
        return FileResponse(download.get_file_location())
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@router.get(
    '/downloads/{video_id}/status', tags=['downloads'], responses={
        status.HTTP_404_NOT_FOUND: {
            'description': 'Download not found.',
        },
    },
)
def get_download_status(video_id: str, session_id: str) -> StatusUpdate:
    download_manager = session_manager.get_download_manager(session_id)
    download = download_manager.get(video_id)
    if download is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    else:
        return StatusUpdate(id=download.video.id, status=download.status)


@router.delete(
    '/downloads/{video_id}', tags=['downloads'], status_code=status.HTTP_204_NO_CONTENT, responses={  # noqa E501
        status.HTTP_404_NOT_FOUND: {
            'description': 'Download not found.',
        },
    },
)
def delete_download(video_id: str, session_id: str) -> None:
    download_manager = session_manager.get_download_manager(session_id)
    if video_id in download_manager:
        download_manager.remove(video_id)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
