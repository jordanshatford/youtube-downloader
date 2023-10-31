from yt_dlp import YoutubeDL  # type: ignore

from .config import DownloadConfig
from .models import DownloadState
from .models import DownloadStatus


def run_downloader(config: DownloadConfig) -> None:
    downloader = YoutubeDL(config.as_ytdlp_params)
    config.on_status_update(
        DownloadStatus(state=DownloadState.DOWNLOADING),
    )
    try:
        downloader.download(  # type: ignore
            [str(config.download.video.url)],
        )
    except Exception:
        config.on_status_update(
            DownloadStatus(state=DownloadState.ERROR),
        )
