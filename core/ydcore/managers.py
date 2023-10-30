import os
import time

from .config import StatusHook
from .models import Download
from .models import DownloadFile
from .threads import YoutubeDownloadThread


class DownloadManager:
    def __init__(
        self, output_dir: str,
        status_hook: StatusHook | None = None,
    ):
        self._status_hook = status_hook
        self._downloads: dict[str, YoutubeDownloadThread] = {}
        self._output_dir = output_dir

    def __contains__(self, download_id: str) -> bool:
        return download_id in self._downloads

    def add(self, download: Download) -> Download:
        if download.video.id not in self._downloads:
            thread = YoutubeDownloadThread(
                download, self._output_dir, self.send_status_update,
            )
            self._downloads[download.video.id] = thread
            thread.start()
        return download

    def remove(self, download_id: str) -> None:
        if download_id in self._downloads:
            self._downloads[download_id].remove()
            self._downloads.pop(download_id, None)

    def get(self, download_id: str) -> Download | None:
        thread = self._downloads.get(download_id, None)
        return None if thread is None else thread.download

    def get_all(self) -> list[Download]:
        return [thread.download for thread in self._downloads.values()]

    def get_file(self, download_id: str) -> DownloadFile | None:
        thread = self._downloads.get(download_id, None)
        if thread is None or not os.path.exists(thread.path):
            return None
        return DownloadFile(name=thread.filename, path=thread.path)

    def send_status_update(self, update: Download) -> None:
        if self._status_hook is not None:
            self._status_hook(update)

    def wait(self) -> None:
        for download in self._downloads.values():
            download.join()
        time.sleep(1)
