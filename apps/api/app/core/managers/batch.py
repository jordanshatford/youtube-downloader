import logging
import pathlib
import queue
import tempfile
from multiprocessing.pool import ThreadPool

from app.core.downloadable import BatchDownloadable
from app.core.models import BatchDownload
from app.core.models import BatchDownloadInput

logger = logging.getLogger("core")


class BatchManager:
    def __init__(
        self,
        directory: pathlib.Path,
        tmp: tempfile.TemporaryDirectory,
        pool: ThreadPool,
    ) -> None:
        self._directory: pathlib.Path = directory
        self._tmp: tempfile.TemporaryDirectory = tmp
        self._pool: ThreadPool = pool
        self._batch: BatchDownloadable | None = None
        self.queue: queue.Queue[BatchDownload] = queue.Queue()

    def add(self, batch: BatchDownloadInput) -> BatchDownload:
        if self._batch is None:
            downloadable = BatchDownloadable(
                batch, self._directory, self._tmp, self.queue.put
            )
            self._batch = downloadable
            self._pool.apply_async(self._batch.run)
        return self._batch.batch

    def remove(self) -> None:
        if self._batch is not None:
            self._batch.remove()
        self._batch = None

    def get(self) -> BatchDownload | None:
        return None if self._batch is None else self._batch.batch

    def get_file_path(self) -> pathlib.Path | None:
        if self._batch is None:
            return None

        if not self._batch.path.exists():
            logger.debug(
                "[BatchManager]: file does not exist for %s.", self._batch.path
            )
            return None

        return self._batch.path
