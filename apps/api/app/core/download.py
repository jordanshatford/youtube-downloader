import copy
import logging
import pathlib
from collections.abc import Callable

from .config import DownloadConfig
from .models import Download
from .models import DownloadInput
from .models import DownloadState
from .models import DownloadStatus
from .models import Video
from .ytdlp import YoutubeDL
from .ytdlp import YoutubeDLParams

logger = logging.getLogger("core")


# Config used when downloading single videos using yt-dlp.
class VideoDownloadConfig(DownloadConfig):
    def __init__(
        self,
        download: DownloadInput,
        output_directory: pathlib.Path,
        status_hook: Callable[[Download], None],
    ) -> None:
        super().__init__(
            f"{download.video.id}", download.options, self._status_update_hook
        )
        self.download = Download(
            **download.model_dump(),
            status=DownloadStatus(
                state=DownloadState.WAITING,
            ),
        )
        self._output_directory = output_directory
        self._status_hook = status_hook
        self._status_update_hook(
            self.download.video,
            DownloadStatus(state=DownloadState.WAITING),
        )

    def run(self) -> None:
        params: YoutubeDLParams = {
            **super()._as_ytdlp_params,
            "outtmpl": f"{self._output_directory}/%(id)s.%(ext)s",
        }

        logger.debug(
            "Download parameters for %s are %s.",
            self.download.video.url,
            params,
        )

        try:
            with YoutubeDL(params) as downloader:
                self._status_update_hook(
                    self.download.video,
                    DownloadStatus(state=DownloadState.DOWNLOADING),
                )
                logger.debug("Download started: %s.", self.download.video.url)
                downloader.download(
                    [str(self.download.video.url)],
                )
                logger.debug("Download completed: %s.", self.download.video.url)
        except Exception:
            logger.exception("Failed to download: %s.", self.download.video.url)
            self._status_update_hook(
                self.download.video,
                DownloadStatus(state=DownloadState.ERROR),
            )

    @property
    def path(self) -> pathlib.Path:
        return (
            self._output_directory
            / f"{self.download.video.id}.{self.download.options.format.value}"
        )

    def _status_update_hook(self, _: Video | None, status: DownloadStatus) -> None:
        self.download.status = status
        self._status_hook(copy.deepcopy(self.download))
