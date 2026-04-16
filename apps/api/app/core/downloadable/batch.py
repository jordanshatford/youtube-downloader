import copy
import logging
import pathlib
import tempfile
import zipfile
from collections.abc import Callable

from app.core.models import BatchDownload
from app.core.models import BatchDownloadInput
from app.core.models import BatchDownloadStatus
from app.core.models import DownloadState
from app.core.models import DownloadStatus
from app.core.models import Video
from app.core.ytdlp import YoutubeDL

from .common import Downloadable

logger = logging.getLogger("core")


# Config used when downloading a batch of videos by URL using yt-dlp.
class BatchDownloadable(Downloadable):
    _name: str = "BatchDownloadable"
    _outtmpl: str = "%(title)s.%(ext)s"

    def __init__(
        self,
        batch: BatchDownloadInput,
        directory: pathlib.Path,
        tmp: tempfile.TemporaryDirectory,
        hook: Callable[[BatchDownload], None],
    ) -> None:
        super().__init__(
            "batch",
            batch.options,
            directory / "batch",
            tmp,
            self.__downloadable_hook,
        )
        self.batch = BatchDownload(
            **batch.model_dump(),
            status=BatchDownloadStatus(
                overall=DownloadStatus(
                    state=DownloadState.WAITING,
                    total_bytes=len(batch.urls),
                    downloaded_bytes=0,
                ),
                items={},
            ),
            videos={},
        )
        self._urls = batch.urls
        self._hook = hook
        self.__downloadable_hook(
            None,
            DownloadStatus(state=DownloadState.WAITING),
        )

    def run(self) -> None:
        try:
            params = super().as_ytdlp_params
            if self._contains_some_playlist:
                # Modify the parameters to better work with playlists and ensure that we
                # are not infinitely donwloading playlist items in the case that it is a
                # radio playlist.
                params["extract_flat"] = False
                params["noplaylist"] = False
                params["playlist_items"] = "1:20"

            with YoutubeDL(params) as ytdlp:
                self.__downloadable_hook(
                    None,
                    DownloadStatus(state=DownloadState.DOWNLOADING),
                )
                logger.debug("[%s]: %s is 'starting'.", self._name, self._identifier)
                ytdlp.download([str(url) for url in self._urls])
                logger.debug("[%s]: %s is 'completed'.", self._name, self._identifier)
                self._generate_zip_file()
                self.__downloadable_hook(
                    None,
                    DownloadStatus(state=DownloadState.DONE),
                )
        except Exception:
            logger.exception("[%s]: %s is 'failed'.", self._name, self._identifier)
            self.__downloadable_hook(
                None,
                DownloadStatus(state=DownloadState.ERROR),
            )

    @property
    def path(self) -> pathlib.Path:
        return self._directory.parent / "batch.zip"

    def remove(self) -> None:
        logger.debug("[%s]: %s is being removed.", self._name, self._identifier)
        # Remove the ZIP file generated for the user.
        if self.path.exists():
            logger.debug(
                "[%s]: %s file is being removed.", self._name, self._identifier
            )
            self.path.unlink()
        # Remove all files in the batch directory.
        if not self._directory.exists():
            return

        for item in self._directory.iterdir():
            if item.is_file():
                item.unlink()

    @property
    def _contains_some_playlist(self) -> bool:
        return any("list=" in str(url) for url in self._urls)

    def _generate_zip_file(self) -> None:
        # TODO(jordan): maybe attempt to use a postprocessor for this??
        with zipfile.ZipFile(self.path, "w", compression=zipfile.ZIP_DEFLATED) as z:
            for path in self._directory.rglob("*"):
                # Only include files that are in the format we wanted to download. This
                # ensures that any subtitle or other files we may have downloaded, but
                # the user does not need, are not included in the resulting ZIP file.
                if path.is_file() and path.suffix.endswith(self._options.format.value):
                    z.write(path, arcname=path.relative_to(self._directory))
        logger.debug("[%s]: %s ZIP file is generated.", self._name, self._identifier)

    def __downloadable_hook(self, video: Video | None, status: DownloadStatus) -> None:
        if video is not None:
            self.batch.videos[video.id] = video
            if self.batch.status.items.get(video.id) == status:
                return

            self.batch.status.items[video.id] = status
        else:
            if self.batch.status.overall == status:
                return
            self.batch.status.overall.state = status.state

        # Give rough overall progress details. This is used to display overall download
        # information in the web interface. In cases of a playlist URL we have one URL
        # that eventually becomes N videos based on the entries in the playlist.
        done = len(
            [
                item
                for item in self.batch.status.items.values()
                if item.state in {DownloadState.DONE, DownloadState.ERROR}
            ]
        )
        self.batch.status.overall.downloaded_bytes = done
        total = len(self.batch.status.items.values())
        if (
            self.batch.status.overall.total_bytes is not None
            and total > self.batch.status.overall.total_bytes
        ):
            self.batch.status.overall.total_bytes = total

        self._hook(copy.deepcopy(self.batch))
