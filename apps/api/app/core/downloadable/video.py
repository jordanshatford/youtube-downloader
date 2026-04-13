import copy
import logging
import pathlib
from collections.abc import Callable

from app.core.models import Download
from app.core.models import DownloadInput
from app.core.models import DownloadState
from app.core.models import DownloadStatus
from app.core.models import Video
from app.core.ytdlp import YoutubeDL
from app.core.ytdlp import YoutubeDLParams

from .common import Downloadable

logger = logging.getLogger("core")


# Config used when downloading single videos using yt-dlp.
class VideoDownloadable(Downloadable):
    _name: str = "VideoDownloadable"

    def __init__(
        self,
        download: DownloadInput,
        output_directory: pathlib.Path,
        status_hook: Callable[[Download], None],
    ) -> None:
        super().__init__(
            download.video.id,
            download.options,
            output_directory,
            self.__downloadable_hook,
        )
        self.download = Download(
            **download.model_dump(),
            status=DownloadStatus(
                state=DownloadState.WAITING,
            ),
        )
        self._status_hook = status_hook
        self.__downloadable_hook(
            self.download.video,
            DownloadStatus(state=DownloadState.WAITING),
        )

    def run(self) -> None:
        params: YoutubeDLParams = {
            **super().as_ytdlp_params,
            "outtmpl": "%(id)s.%(ext)s",
        }

        logger.debug(
            "Download parameters for %s are %s.",
            self.download.video.url,
            params,
        )

        try:
            with YoutubeDL(params) as downloader:
                self.__downloadable_hook(
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
            self.__downloadable_hook(
                self.download.video,
                DownloadStatus(state=DownloadState.ERROR),
            )

    @property
    def path(self) -> pathlib.Path:
        return (
            self._output_directory
            / f"{self.download.video.id}.{self.download.options.format.value}"
        )

    def remove(self) -> None:
        logger.debug("Removing download %s.", self._identifier)
        if self.path.exists():
            logger.debug("Removing download file %s.", self._identifier)
            self.path.unlink()

    def __downloadable_hook(self, _: Video | None, status: DownloadStatus) -> None:
        self.download.status = status
        self._status_hook(copy.deepcopy(self.download))
