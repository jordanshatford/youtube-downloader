import asyncio
import queue
from collections.abc import AsyncIterable

from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import Request
from fastapi import status
from fastapi.responses import FileResponse
from fastapi.sse import EventSourceResponse

from app.core import AvailableDownloadOptions
from app.core import Download
from app.core import DownloadInput
from app.core import DownloadOptions
from app.dependencies import DependsDownload
from app.dependencies import DependsSession
from app.dependencies import depends_download_responses
from app.dependencies import depends_session_responses
from app.session import session_manager

router = APIRouter(
    prefix="/downloads",
    tags=["downloads"],
    responses=depends_session_responses,
)


@router.get("")
def get_downloads(session: DependsSession) -> list[Download]:
    return session.downloads.get_list()


@router.post("", status_code=status.HTTP_201_CREATED)
def post_downloads(
    download: DownloadInput,
    session: DependsSession,
) -> Download:
    return session.downloads.add(download)


@router.put("")
def put_downloads(
    download: DownloadInput,
    session: DependsSession,
) -> Download:
    session.downloads.remove(download.video.id)
    return session.downloads.add(download)


@router.get("/options/available")
def get_downloads_options_available(_: DependsSession) -> AvailableDownloadOptions:
    return AvailableDownloadOptions()


@router.get("/options/defaults")
def get_downloads_options_defaults(_: DependsSession) -> DownloadOptions:
    return DownloadOptions()


@router.get("/status", response_class=EventSourceResponse)
async def get_downloads_status(
    request: Request,
    session_id: str,
) -> AsyncIterable[Download]:
    session = session_manager.get(session_id)
    if session is None:
        return
    try:
        while True:
            if await request.is_disconnected():
                break
            try:
                yield session.downloads_statuses.get_nowait()
            except queue.Empty:
                await asyncio.sleep(1)
    except (asyncio.CancelledError, asyncio.exceptions.InvalidStateError):
        pass


@router.get("/{download_id}", responses=depends_download_responses)  # noqa: FAST003
def get_download(download: DependsDownload) -> Download:
    return download


@router.get(
    "/{download_id}/file",  # noqa: FAST003
    response_class=FileResponse,
    responses=depends_download_responses
    | {
        status.HTTP_200_OK: {
            "content": {
                "audio/*": {"schema": {"type": "file"}},
                "video/*": {"schema": {"type": "file"}},
            },
        },
    },
)
def get_download_file(
    download: DependsDownload,
    session: DependsSession,
) -> FileResponse:
    path = session.downloads.get_file_path(download.video.id)
    if path is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return FileResponse(
        path,
        filename=path.name,
    )


@router.delete(
    "/{download_id}",  # noqa: FAST003
    status_code=status.HTTP_204_NO_CONTENT,
    responses=depends_download_responses,
)
def delete_download(
    download: DependsDownload,
    session: DependsSession,
) -> None:
    session.downloads.remove(download.video.id)
