import asyncio
import queue
from collections.abc import AsyncIterable

from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import status
from fastapi.responses import FileResponse
from fastapi.sse import EventSourceResponse

from app.core import AvailableDownloadOptions
from app.core import Download
from app.core import DownloadInput
from app.core import DownloadOptions
from app.dependencies import DependsDownload
from app.dependencies import DependsSession
from app.dependencies import DependsSessionInQuery
from app.dependencies import depends_download_responses
from app.dependencies import depends_session_responses

router = APIRouter(tags=["downloads"], responses=depends_session_responses)


@router.get("/downloads")
def get_downloads(session: DependsSession) -> list[Download]:
    return session.downloads.get_list()


@router.post("/downloads", status_code=status.HTTP_201_CREATED)
def post_downloads(
    download: DownloadInput,
    session: DependsSession,
) -> Download:
    return session.downloads.add(download)


@router.get("/downloads/options/available")
def get_downloads_options_available(_: DependsSession) -> AvailableDownloadOptions:
    return AvailableDownloadOptions()


@router.get("/downloads/options/defaults")
def get_downloads_options_defaults(_: DependsSession) -> DownloadOptions:
    return DownloadOptions()


@router.get("/downloads/status", response_class=EventSourceResponse)
async def get_downloads_status(
    session: DependsSessionInQuery,
) -> AsyncIterable[Download]:
    try:
        while True:
            try:
                yield session.downloads.queue.get_nowait()
            except queue.Empty:
                await asyncio.sleep(1)
    except (asyncio.CancelledError, asyncio.exceptions.InvalidStateError):
        pass


@router.get("/downloads/{download_id}", responses=depends_download_responses)  # noqa: FAST003
def get_download(download: DependsDownload) -> Download:
    return download


@router.put("/downloads/{download_id}", responses=depends_download_responses)  # noqa: FAST003
def put_download(
    body: DownloadInput,
    download: DependsDownload,
    session: DependsSession,
) -> Download:
    session.downloads.remove(download.video.id)
    return session.downloads.add(body)


@router.delete(
    "/downloads/{download_id}",  # noqa: FAST003
    status_code=status.HTTP_204_NO_CONTENT,
    responses=depends_download_responses,
)
def delete_download(
    download: DependsDownload,
    session: DependsSession,
) -> None:
    session.downloads.remove(download.video.id)


@router.get(
    "/downloads/{download_id}/file",  # noqa: FAST003
    response_class=FileResponse,
    responses=depends_download_responses
    | {
        status.HTTP_200_OK: {
            "content": {
                "audio/*": {"schema": {"type": "string", "format": "binary"}},
                "video/*": {"schema": {"type": "string", "format": "binary"}},
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
