import logging

from yt_dlp import YoutubeDL  # type: ignore

from .config import DownloadConfig
from .models import DownloadState
from .models import DownloadStatus


logger = logging.getLogger('ydcore')


def run_downloader(config: DownloadConfig) -> None:
    downloader = YoutubeDL(config.as_ytdlp_params)
    config.on_status_update(
        DownloadStatus(state=DownloadState.DOWNLOADING),
    )
    try:
        logger.debug(msg=f'Download started: {config.download.video.url}.')
        downloader.download(  # type: ignore
            [str(config.download.video.url)],
        )
        logger.debug(msg=f'Download completed: {config.download.video.url}.')
    except Exception as e:
        logger.error(f'Failed to download: {config.download.video.url} {e}.')
        config.on_status_update(
            DownloadStatus(state=DownloadState.ERROR),
        )
