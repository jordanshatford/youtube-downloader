import abc
import logging
import pathlib
from collections.abc import Callable

from app.core.models import AudioFormat
from app.core.models import DownloadOptions
from app.core.models import DownloadState
from app.core.models import DownloadStatus
from app.core.models import Video
from app.core.models import VideoFormat
from app.core.parse import parse_video_info_to_video
from app.core.ytdlp import DEFAULT_YOUTUBE_DL_PARAMS
from app.core.ytdlp import PostprocessorHookInfo
from app.core.ytdlp import ProgressHookInfo
from app.core.ytdlp import YoutubeDLParams

logger = logging.getLogger("core")


# Generic downloadable that we use to convert out options into the format
# that yt-dlp is expecting. This is generic to allow use with different
# types of downloads we support (i.e batch and video).
class Downloadable(abc.ABC):
    _name: str = "Downloadable"

    def __init__(
        self,
        identifier: str,
        options: DownloadOptions,
        output_directory: pathlib.Path,
        hook: Callable[[Video | None, DownloadStatus], None],
    ) -> None:
        self._identifier: str = f"{self._name}+{identifier}"
        self._options: DownloadOptions = options
        self._output_directory: pathlib.Path = output_directory
        self._hook: Callable[[Video | None, DownloadStatus], None] = hook

    @abc.abstractmethod
    def run(self) -> None:
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def path(self) -> pathlib.Path:
        raise NotImplementedError

    @abc.abstractmethod
    def remove(self) -> None:
        raise NotImplementedError

    @property
    def as_ytdlp_params(self) -> YoutubeDLParams:
        modifications: YoutubeDLParams = {}
        postprocessors: list[dict[str, str | bool | int]] = []
        # Only append audio postprocessor if we are downloading audio format.
        if self.__is_audio_download:
            postprocessors.append(
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": self._options.format.value,
                    "preferredquality": "192",
                },
            )
        # Only append video postprocessor if we are downloading video format.
        if self.__is_video_download:
            postprocessors.append(
                {
                    "key": "FFmpegVideoConvertor",
                    # This is deliberately spelled incorrectly as that is how
                    # the option is named in yt-dlp.
                    "preferedformat": self._options.format.value,
                },
            )
        # Only append metadata to the video if enabled by user.
        if self._options.embed_metadata:
            postprocessors.append({"key": "FFmpegMetadata"})
        # Only append thumbnail embedding if enabled by user.
        if self._options.embed_thumbnail:
            postprocessors.append(
                {
                    "key": "EmbedThumbnail",
                    "already_have_thumbnail": False,
                },
            )
            modifications["writethumbnail"] = True
        if self._options.embed_subtitles:
            postprocessors.append(
                {
                    "key": "FFmpegEmbedSubtitle",
                    "already_have_subtitle": False,
                },
            )
            modifications["writesubtitles"] = True
            modifications["subtitleslangs"] = [
                f"{self._options.preferred_subtitles_language}.*"
            ]
            modifications["subtitlesformat"] = "best"

        params: YoutubeDLParams = {
            **DEFAULT_YOUTUBE_DL_PARAMS,
            **modifications,
            "format": self.__ytdlp_format,
            "postprocessors": postprocessors,
            "progress_hooks": [self.__progress_hook],
            "postprocessor_hooks": [self.__postprocessor_hook],
            "paths": {
                "home": str(self._output_directory),
                "temp": str(self._output_directory / "temp"),
            },
        }

        return params

    @property
    def __is_audio_download(self) -> bool:
        return self._options.format in AudioFormat

    @property
    def __is_video_download(self) -> bool:
        return self._options.format in VideoFormat

    @property
    def __ytdlp_format(self) -> str:
        quality = self._options.quality.value
        extension = self._options.format.value
        # bestvideo*[ext=X]+bestaudio/bestvideo*+bestaudio/best or
        # worstvideo*[ext=X]+worstaudio/worstvideo*+worstaudio/worst
        if self.__is_video_download:
            proper_ext = f"{quality}video*[ext={extension}]+{quality}audio"
            return f"{proper_ext}/{quality}video*+{quality}audio/{quality}"
        # bestaudio[ext=X]/bestaudio/best or worstaudio[ext=X]/worstaudio/worst
        if self.__is_audio_download:
            return f"{quality}audio[ext={extension}]/{quality}audio/{quality}"
        # Default to returning the quality (ie 'best' or 'worst')
        return quality

    def __progress_hook(self, info: ProgressHookInfo) -> None:
        # Attempt to parse video information from the progress hook.
        info_dict = info.get("info_dict")
        video = None if info_dict is None else parse_video_info_to_video(info_dict)
        status = info.get("status")
        update = DownloadStatus(state=DownloadState.DOWNLOADING)
        if status == "downloading":
            logger.debug("Download %s status DOWNLOADING.", self._identifier)
            # Get all relevant download details to provide feedback to the user.
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
                self._identifier,
                update.progress,
            )
        elif status == "finished":
            logger.debug("Download %s status FINISHED.", self._identifier)
            update = DownloadStatus(state=DownloadState.PROCESSING)
        elif status == "error":
            logger.error("Download %s status ERROR.", self._identifier)
            update = DownloadStatus(state=DownloadState.ERROR)

        self._hook(video, update)

    def __postprocessor_hook(self, info: PostprocessorHookInfo) -> None:
        # Attempt to parse video information from the progress or postprocessor hook.
        info_dict = info.get("info_dict")
        video = None if info_dict is None else parse_video_info_to_video(info_dict)

        status = info.get("status")
        postprocessor = info.get("postprocessor")

        logger.debug(
            "Download %s postprocessing %s is %s.",
            self._identifier,
            postprocessor,
            status.upper(),
        )

        update = DownloadStatus(
            state=DownloadState.PROCESSING,
            postprocessor=postprocessor,
        )

        # Handle MoveFile postprocess. This runs at the very end and we use it to
        # detect if the download is done.
        if postprocessor == "MoveFiles" and status == "finished":
            update = DownloadStatus(state=DownloadState.DONE)

        self._hook(video, update)
