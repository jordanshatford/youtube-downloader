import asyncio
import os
import queue

from fastapi import APIRouter
from fastapi import Request
from fastapi import Response
from fastapi import status
from fastapi.responses import FileResponse
from sse_starlette.sse import EventSourceResponse
from utils.managers import session_manager
from utils.models import Message
from utils.models import Video

router = APIRouter()


@router.post('/downloads', tags=['downloads'], response_model=Message)
def post_download(video: Video, response: Response, session_id: str):
    download_manager = session_manager.get_download_manager(session_id)
    download_manager.add(video)
    return {
        'title': 'File Added',
        'message': 'The requested file has been successfully added to download.',   # noqa: E501
    }


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


@router.get('/downloads/{video_id}', tags=['downloads'], response_model=Message)   # noqa: E501
def get_download(video_id: str, response: Response, session_id: str):
    download_manager = session_manager.get_download_manager(session_id)
    path = download_manager.get_download(video_id)
    if path is not None and os.path.exists(path):
        return FileResponse(path)
    else:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {
            'title': 'File Missing',
            'message': 'This file was not found on the server. Try downloading again.',   # noqa: E501
        }


@router.delete('/downloads/{video_id}', tags=['downloads'], response_model=Message)  # noqa: E501
def delete_download(video_id: str, session_id: str):
    download_manager = session_manager.get_download_manager(session_id)
    download_manager.remove(video_id)
    return {
        'title': 'File Removed',
        'message': 'The requested file has been removed from the server.',
    }
