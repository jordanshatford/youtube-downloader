import asyncio
import os
import queue

from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import Request
from fastapi import status
from fastapi.responses import FileResponse
from sse_starlette.sse import EventSourceResponse
from yad_api.utils.managers import session_manager
from yad_api.utils.models import StatusUpdate
from yad_api.utils.models import Video

router = APIRouter(
    prefix='/downloads',
    tags=['downloads'],
    responses={
        status.HTTP_404_NOT_FOUND: {},
    },
)


@router.post('', status_code=status.HTTP_201_CREATED)
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


@router.get('/status', include_in_schema=False)
async def get_downloads_status(request: Request, session_id: str):
    event_source = status_stream(request, session_id=session_id)
    return EventSourceResponse(event_source)


@router.get('/{video_id}')
def get_download(video_id: str, session_id: str) -> Video:
    download_manager = session_manager.get_download_manager(session_id)
    download = download_manager.get(video_id)
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
def get_download_file(video_id: str, session_id: str):
    download_manager = session_manager.get_download_manager(session_id)
    download = download_manager.get(video_id)
    if download is not None and os.path.exists(download.get_file_location()):
        return FileResponse(download.get_file_location())
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@router.get('/{video_id}/status')
def get_download_status(video_id: str, session_id: str) -> StatusUpdate:
    download_manager = session_manager.get_download_manager(session_id)
    download = download_manager.get(video_id)
    if download is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    else:
        return StatusUpdate(id=download.video.id, status=download.status)


@router.delete('/{video_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_download(video_id: str, session_id: str) -> None:
    download_manager = session_manager.get_download_manager(session_id)
    if video_id in download_manager:
        download_manager.remove(video_id)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
