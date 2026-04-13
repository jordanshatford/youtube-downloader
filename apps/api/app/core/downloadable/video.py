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
    _outtmpl: str = "%(id)s.%(ext)s"

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
        try:
            with YoutubeDL(super().as_ytdlp_params) as ytdlp:
                self.__downloadable_hook(
                    self.download.video,
                    DownloadStatus(state=DownloadState.DOWNLOADING),
                )
                logger.debug("[%s]: %s is 'starting'.", self._name, self._identifier)
                ytdlp.download(
                    [str(self.download.video.url)],
                )
                logger.debug("[%s]: %s is 'completed'.", self._name, self._identifier)
        except Exception:
            logger.exception("[%s]: %s is 'failed'.", self._name, self._identifier)
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
        logger.debug("[%s]: %s is being removed.", self._name, self._identifier)
        if self.path.exists():
            logger.debug(
                "[%s]: %s file is being removed.", self._name, self._identifier
            )
            self.path.unlink()

    def __downloadable_hook(self, _: Video | None, status: DownloadStatus) -> None:
        self.download.status = status
        self._status_hook(copy.deepcopy(self.download))
