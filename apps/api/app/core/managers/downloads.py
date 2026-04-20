import logging
import pathlib
import queue
import tempfile
from multiprocessing.pool import ThreadPool

from app.core.downloadable import SingleDownloadable
from app.core.models import Download
from app.core.models import DownloadInput

logger = logging.getLogger("core")


class DownloadsManager:
    def __init__(
        self,
        directory: pathlib.Path,
        tmp: tempfile.TemporaryDirectory,
        pool: ThreadPool,
    ) -> None:
        self._directory: pathlib.Path = directory
        self._tmp: tempfile.TemporaryDirectory = tmp
        self._pool: ThreadPool = pool
        self._downloads: dict[str, SingleDownloadable] = {}
        self.queue: queue.Queue[Download] = queue.Queue()

    def __contains__(self, download_id: str) -> bool:
        return download_id in self._downloads

    def add(self, download: DownloadInput) -> Download:
        if download.video.id not in self._downloads:
            config = SingleDownloadable(
                download,
                self._directory,
                self._tmp,
                self.queue.put,
            )
            logger.debug(
                "[DownloadsManager]: Added download %s with options %s ",
                download.video.url,
                download.options,
            )
            self._downloads[download.video.id] = config
            self._pool.apply_async(config.run)
        return self._downloads[download.video.id].download

    def remove(self, download_id: str) -> None:
        download = self._downloads.pop(download_id, None)
        if download is not None:
            download.remove()

    def get(self, download_id: str) -> Download | None:
        config = self._downloads.get(download_id, None)
        return None if config is None else config.download

    def get_list(self) -> list[Download]:
        return [config.download for config in self._downloads.values()]

    def get_file_path(self, download_id: str) -> pathlib.Path | None:
        config = self._downloads.get(download_id, None)
        if config is None or not config.path.exists():
            logger.debug("[DownloadsManager]: file does not exist for %s.", download_id)
            return None
        return config.path
