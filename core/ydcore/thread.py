import threading

from yt_dlp import YoutubeDL  # type: ignore

from .config import DownloadConfig
from .models import DownloadState
from .models import DownloadStatus


class YoutubeDownloadThread(threading.Thread):
    def __init__(
        self,
        config: DownloadConfig,
    ):
        self._config = config
        self._downloader = YoutubeDL(self._config.as_ytdlp_params)
        super().__init__(
            group=None, target=None, name=None, daemon=True,
        )

    def run(self):
        self._config.on_status_update(
            DownloadStatus(state=DownloadState.DOWNLOADING),
        )
        try:
            self._downloader.download(  # type: ignore
                [str(self._config.download.video.url)],
            )
        except Exception:
            self._config.on_status_update(
                DownloadStatus(state=DownloadState.ERROR),
            )
