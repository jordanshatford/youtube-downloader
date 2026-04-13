import logging
import pathlib
from collections.abc import Callable
from multiprocessing.pool import ThreadPool

from .downloadable import VideoDownloadable
from .models import Download
from .models import DownloadInput

logger = logging.getLogger("core")


class DownloadManager:
    def __init__(
        self,
        output_dir: pathlib.Path,
        status_hook: Callable[[Download], None],
        *,
        num_threads: int | None = None,
    ) -> None:
        self._output_dir = output_dir
        self._status_hook = status_hook
        self._downloads: dict[str, VideoDownloadable] = {}
        self._pool = ThreadPool(num_threads)
        logger.debug(
            "Initializing download manager with output at %s and %s threads.",
            self._output_dir,
            num_threads,
        )

    def __contains__(self, download_id: str) -> bool:
        return download_id in self._downloads

    def add(self, download: DownloadInput) -> Download:
        if download.video.id not in self._downloads:
            config = VideoDownloadable(
                download,
                self._output_dir,
                self._status_hook,
            )
            logger.debug(
                "Added download %s with options %s ",
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
            logger.debug("Download file does not exist for %s.", download_id)
            return None
        return config.path
