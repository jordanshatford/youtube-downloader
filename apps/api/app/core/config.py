import copy
import logging
import pathlib
from collections.abc import Callable

from .models import AudioFormat
from .models import Download
from .models import DownloadInput
from .models import DownloadState
from .models import DownloadStatus
from .models import VideoFormat
from .ytdlp import DEFAULT_YOUTUBE_DL_PARAMS
from .ytdlp import PostprocessorHookInfo
from .ytdlp import ProgressHookInfo
from .ytdlp import YoutubeDL
from .ytdlp import YoutubeDLParams

logger = logging.getLogger("core")


# Config used when downloading videos using yt-dlp.
class DownloadConfig:
    def __init__(
        self,
        download: DownloadInput,
        output_directory: pathlib.Path,
        status_hook: Callable[[Download], None],
    ) -> None:
        self.download = Download(
            **download.model_dump(),
            status=DownloadStatus(
                state=DownloadState.WAITING,
            ),
        )
        self._output_directory = output_directory
        self._status_hook = status_hook
        self._handle_status_update(
            DownloadStatus(state=DownloadState.WAITING),
        )

    def run(self) -> None:
        try:
            with YoutubeDL(self._as_ytdlp_params) as downloader:
                self._handle_status_update(
                    DownloadStatus(state=DownloadState.DOWNLOADING),
                )
                logger.debug("Download started: %s.", self.download.video.url)
                downloader.download(
                    [str(self.download.video.url)],
                )
                logger.debug("Download completed: %s.", self.download.video.url)
        except Exception:
            logger.exception("Failed to download: %s.", self.download.video.url)
            self._handle_status_update(
                DownloadStatus(state=DownloadState.ERROR),
            )

    @property
    def path(self) -> pathlib.Path:
        return (
            self._output_directory
            / f"{self.download.video.id}.{self.download.options.format.value}"
        )

    @property
    def _is_audio_download(self) -> bool:
        return self.download.options.format in AudioFormat

    @property
    def _is_video_download(self) -> bool:
        return self.download.options.format in VideoFormat

    @property
    def _as_ytdlp_params(self) -> YoutubeDLParams:
        modifications: YoutubeDLParams = {}
        postprocessors: list[dict[str, str | bool | int]] = []
        # Only append audio postprocessor if we are downloading audio format.
        if self._is_audio_download:
            postprocessors.append(
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": self.download.options.format.value,
                    "preferredquality": "192",
                },
            )
        # Only append video postprocessor if we are downloading video format.
        if self._is_video_download:
            postprocessors.append(
                {
                    "key": "FFmpegVideoConvertor",
                    # This is deliberately spelled incorrectly as that is how
                    # the option is named in yt-dlp.
                    "preferedformat": self.download.options.format.value,
                },
            )
        # Only append metadata to the video if enabled by user
        if self.download.options.embed_metadata:
            postprocessors.append({"key": "FFmpegMetadata"})
        # Only append thumbnail embedding if enabled by user
        if self.download.options.embed_thumbnail:
            postprocessors.append(
                {
                    "key": "EmbedThumbnail",
                    "already_have_thumbnail": False,
                },
            )
            modifications["writethumbnail"] = True
        if self.download.options.embed_subtitles:
            postprocessors.append(
                {
                    "key": "FFmpegEmbedSubtitle",
                    "already_have_subtitle": False,
                },
            )
            modifications["writesubtitles"] = True
            modifications["subtitleslangs"] = [
                f"{self.download.options.preferred_subtitles_language}.*"
            ]
            modifications["subtitlesformat"] = "best"

        params: YoutubeDLParams = {
            **DEFAULT_YOUTUBE_DL_PARAMS,
            **modifications,
            "format": self._ytdlp_format,
            "progress_hooks": [self._progress_hook],
            "postprocessor_hooks": [self._postprocessor_hook],
            "post_hooks": [self._post_hook],
            "outtmpl": f"{self._output_directory}/%(id)s.%(ext)s",
            "postprocessors": postprocessors,
        }

        logger.debug(
            "Download parameters for %s are %s.",
            self.download.video.url,
            params,
        )

        return params

    @property
    def _ytdlp_format(self) -> str:
        options = self.download.options
        quality = options.quality.value
        extension = options.format.value
        # bestvideo*[ext=X]+bestaudio/bestvideo*+bestaudio/best or
        # worstvideo*[ext=X]+worstaudio/worstvideo*+worstaudio/worst
        if self._is_video_download:
            proper_ext = f"{quality}video*[ext={extension}]+{quality}audio"
            return f"{proper_ext}/{quality}video*+{quality}audio/{quality}"
        # bestaudio[ext=X]/bestaudio/best or worstaudio[ext=X]/worstaudio/worst
        if self._is_audio_download:
            return f"{quality}audio[ext={extension}]/{quality}audio/{quality}"
        # Default to returning the quality (ie 'best' or 'worst')
        return quality

    def _progress_hook(self, info: ProgressHookInfo) -> None:
        url = self.download.video.url
        status = info.get("status")
        if status == "downloading":
            logger.debug("Download %s status DOWNLOADING.", url)
            update = DownloadStatus(
                state=DownloadState.DOWNLOADING,
                downloaded_bytes=info.get("downloaded_bytes"),
                total_bytes=info.get(
                    "total_bytes",
                    info.get("total_bytes_estimate"),
                ),
                elapsed=info.get("elapsed"),
                eta=info.get("eta"),
                speed=info.get("speed"),
            )
            logger.debug(
                "Download %s progress %s.",
                url,
                update.progress,
            )
            self._handle_status_update(update)
        elif status == "error":
            logger.error("Download %s status ERROR.", url)
            self._handle_status_update(
                DownloadStatus(state=DownloadState.ERROR),
            )
        elif status == "finished":
            logger.debug("Download %s status FINISHED.", url)
            self._handle_status_update(
                DownloadStatus(state=DownloadState.PROCESSING),
            )

    def _postprocessor_hook(self, info: PostprocessorHookInfo) -> None:
        url = self.download.video.url
        status = info.get("status")
        postprocessor: str | None = None
        if status in {"started", "processing"}:
            postprocessor = info.get("postprocessor")
        elif status == "finished":
            postprocessor = None
        else:
            postprocessor = None

        logger.debug(
            "Download %s postprocessing %s is %s.",
            url,
            postprocessor,
            status.upper(),
        )
        self._handle_status_update(
            DownloadStatus(
                state=DownloadState.PROCESSING,
                postprocessor=postprocessor,
            ),
        )

    def _post_hook(self, filepath: str) -> None:
        logger.debug("Download %s has completed.", self.download.video.url)
        state = DownloadState.DONE
        if not pathlib.Path(filepath).exists():
            logger.error(
                "Download %s does not have file at %s.",
                self.download.video.url,
                filepath,
            )
            state = DownloadState.ERROR
        self._handle_status_update(
            DownloadStatus(
                state=state,
            ),
        )

    def _handle_status_update(self, update: DownloadStatus) -> None:
        self.download.status = update
        self._status_hook(copy.deepcopy(self.download))
