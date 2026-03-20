import logging

from .config import DownloadConfig
from .models import DownloadState
from .models import DownloadStatus
from .ytdlp import YoutubeDL

logger = logging.getLogger("core")


def run_downloader(config: DownloadConfig) -> None:
    downloader = YoutubeDL(config.as_ytdlp_params)
    config.on_status_update(
        DownloadStatus(state=DownloadState.DOWNLOADING),
    )
    try:
        logger.debug("Download started: %s.", config.download.video.url)
        downloader.download(
            [str(config.download.video.url)],
        )
        logger.debug("Download completed: %s.", config.download.video.url)
    except Exception:
        logger.exception("Failed to download: %s.", config.download.video.url)
        config.on_status_update(
            DownloadStatus(state=DownloadState.ERROR),
        )
