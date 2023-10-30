import os
import threading

from yt_dlp import YoutubeDL  # type: ignore

from .config import DownloadConfig
from .config import StatusHook
from .models import Download
from .models import DownloadState
from .models import DownloadStatus


class YoutubeDownloadThread(threading.Thread):
    def __init__(
        self,
        download: Download,
        output_directory: str,
        status_hook: StatusHook,
    ):
        self._output_directory = output_directory
        self._config = DownloadConfig(download, output_directory)
        self._config.add_status_hook(status_hook)
        self._downloader = YoutubeDL(self._config.as_ytdlp_params)
        super().__init__(
            group=None, target=None, name=None, daemon=True,
        )

    @property
    def download(self) -> Download:
        return self._config.download

    @property
    def filename(self) -> str:
        return self._config.filename

    @property
    def path(self) -> str:
        return self._config.path

    def remove(self) -> bool:
        if os.path.exists(self.path):
            os.remove(self.path)
            return True
        return False

    def run(self):
        self._config.on_status_update(
            DownloadStatus(state=DownloadState.DOWNLOADING),
        )
        try:
            self._downloader.download(  # type: ignore
                [str(self.download.video.url)],
            )
        except Exception:
            self._config.on_status_update(
                DownloadStatus(state=DownloadState.ERROR),
            )
