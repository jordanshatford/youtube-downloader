import os
import time

from .config import DownloadConfig
from .config import StatusHook
from .models import Download
from .models import DownloadFile
from .models import DownloadInput
from .thread import YoutubeDownloadThread


class DownloadManager:
    def __init__(
        self, output_dir: str,
        status_hook: StatusHook | None = None,
    ):
        self._status_hook = status_hook
        self._configs: dict[str, DownloadConfig] = {}
        self._downloads: dict[str, YoutubeDownloadThread] = {}
        self._output_dir = output_dir

    def __contains__(self, download_id: str) -> bool:
        return download_id in self._downloads

    def add(self, download: DownloadInput) -> Download:
        if download.video.id not in self._downloads:
            config = DownloadConfig(download, self._output_dir)
            if self._status_hook:
                config.add_status_hook(self._status_hook)
            self._configs[download.video.id] = config
            thread = YoutubeDownloadThread(self._configs[download.video.id])
            self._downloads[download.video.id] = thread
            thread.start()
        return self._configs[download.video.id].download

    def remove(self, download_id: str) -> None:
        if download_id in self._downloads:
            path = self._configs[download_id].path
            if os.path.exists(path):
                os.remove(path)
            self._downloads.pop(download_id, None)
            self._configs.pop(download_id, None)

    def get(self, download_id: str) -> Download | None:
        config = self._configs.get(download_id, None)
        return None if config is None else config.download

    def get_all(self) -> list[Download]:
        return [config.download for config in self._configs.values()]

    def get_file(self, download_id: str) -> DownloadFile | None:
        config = self._configs.get(download_id, None)
        if config is None or not os.path.exists(config.path):
            return None
        return DownloadFile(name=config.filename, path=config.path)

    def send_status_update(self, update: Download) -> None:
        if self._status_hook is not None:
            self._status_hook(update)

    def wait(self) -> None:
        for download in self._downloads.values():
            download.join()
        self._configs = {}
        self._downloads = {}
        time.sleep(1)
