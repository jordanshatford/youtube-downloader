import os
import time
from multiprocessing.pool import ThreadPool

from .config import DownloadConfig
from .config import StatusHook
from .downloader import run_downloader
from .models import Download
from .models import DownloadFile
from .models import DownloadInput


class DownloadManager:
    def __init__(
        self,
        output_dir: str,
        status_hook: StatusHook | None = None,
        *,
        num_threads: int | None = None,
    ):
        self._output_dir = output_dir
        self._status_hook = status_hook
        self._downloads: dict[str, DownloadConfig] = {}
        self._pool = ThreadPool(num_threads)

    def __contains__(self, download_id: str) -> bool:
        return download_id in self._downloads

    def add(self, download: DownloadInput) -> Download:
        if download.video.id not in self._downloads:
            config = DownloadConfig(download, self._output_dir)
            if self._status_hook:
                config.add_status_hook(self._status_hook)
            self._downloads[download.video.id] = config
            self._pool.apply_async(run_downloader, (config,))
        return self._downloads[download.video.id].download

    def remove(self, download_id: str) -> None:
        if download_id in self._downloads:
            path = self._downloads[download_id].path
            if os.path.exists(path):
                os.remove(path)
            self._downloads.pop(download_id, None)

    def get(self, download_id: str) -> Download | None:
        config = self._downloads.get(download_id, None)
        return None if config is None else config.download

    def get_all(self) -> list[Download]:
        return [config.download for config in self._downloads.values()]

    def get_file(self, download_id: str) -> DownloadFile | None:
        config = self._downloads.get(download_id, None)
        if config is None or not os.path.exists(config.path):
            return None
        return DownloadFile(name=config.filename, path=config.path)

    def wait(self) -> None:
        self._pool.close()
        self._pool.join()
        self._downloads = {}
        time.sleep(1)
