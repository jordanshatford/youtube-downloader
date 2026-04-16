import asyncio
import queue
from collections.abc import AsyncIterable

from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import status
from fastapi.responses import FileResponse
from fastapi.sse import EventSourceResponse

from app.core import BatchDownload
from app.core import BatchDownloadInput
from app.dependencies import DependsBatch
from app.dependencies import DependsSession
from app.dependencies import DependsSessionInQuery
from app.dependencies import depends_batch_responses
from app.dependencies import depends_session_responses

router = APIRouter(
    tags=["batch"],
    responses=depends_session_responses,
)


@router.post("/batch", status_code=status.HTTP_201_CREATED)
def post_batch(batch: BatchDownloadInput, session: DependsSession) -> BatchDownload:
    return session.batch.add(batch)


@router.get("/batch", responses=depends_batch_responses)
def get_batch(batch: DependsBatch) -> BatchDownload:
    return batch


@router.put("/batch", responses=depends_batch_responses)
def put_batch(
    body: BatchDownloadInput, _: DependsBatch, session: DependsSession
) -> BatchDownload:
    session.batch.remove()
    return session.batch.add(body)


@router.delete(
    "/batch", status_code=status.HTTP_204_NO_CONTENT, responses=depends_batch_responses
)
def delete_batch(_: DependsBatch, session: DependsSession) -> None:
    session.batch.remove()


@router.get("/batch/status", response_class=EventSourceResponse)
async def get_batch_status(
    session: DependsSessionInQuery,
) -> AsyncIterable[BatchDownload]:
    try:
        while True:
            try:
                yield session.batch.queue.get_nowait()
            except queue.Empty:
                await asyncio.sleep(1)
    except (asyncio.CancelledError, asyncio.exceptions.InvalidStateError):
        pass


@router.get(
    "/batch/file",
    response_class=FileResponse,
    responses=depends_batch_responses
    | {
        status.HTTP_200_OK: {
            "content": {
                "application/zip": {"schema": {"type": "string", "format": "binary"}},
            },
        },
    },
)
def get_batch_file(_: DependsBatch, session: DependsSession) -> FileResponse:
    path = session.batch.get_file_path()
    if path is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return FileResponse(
        path,
        filename=path.name,
    )
