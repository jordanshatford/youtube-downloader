import os
from collections.abc import Callable
from typing import TypeAlias

from ..models import AudioFormat
from ..models import DownloadState
from ..models import DownloadStatus
from ..models import VideoFormat
from ..models import VideoWithOptions
from ..models import VideoWithOptionsAndStatus
from .ytdlp import PostprocessorHookInfo
from .ytdlp import ProgressHookInfo
from .ytdlp import YoutubeDLParams

StatusHook: TypeAlias = Callable[[VideoWithOptionsAndStatus], None]

# Default params used with yt-dlp. These may be overriden by our download
# options.
# Note: if a default isnt provided then the yt-dlp default will be used.
DEFAULT_YTDLP_PARAMS: YoutubeDLParams = {
    'quiet': True,
    'retries': 5,
    'verbose': False,
    'noprogress': True,
}


def get_progress(info: ProgressHookInfo) -> float | None:
    downloaded_bytes = info.get('downloaded_bytes')
    total_bytes = info.get('total_bytes')
    if total_bytes is None:
        total_bytes = info.get('total_bytes_estimate')
    if downloaded_bytes is None or total_bytes is None or total_bytes <= 0:
        return None
    return (downloaded_bytes / total_bytes) * 100


class DownloadConfig:
    def __init__(self, video: VideoWithOptions, output_directory: str) -> None:
        self.video = video
        self._output_directory = output_directory
        self._status_hooks: list[StatusHook] = []
        self._overrides: YoutubeDLParams = {}
        self.status = DownloadStatus(state=DownloadState.WAITING)

    def add_status_hook(self, hook: StatusHook) -> None:
        self._status_hooks.append(hook)

    def on_status_update(self, status: DownloadStatus) -> None:
        self._handle_status_update(status)

    def add_ytdlp_params_overrides(self, params: YoutubeDLParams) -> None:
        self._overrides = params

    @property
    def _is_audio_download(self) -> bool:
        return self.video.options.format in AudioFormat

    @property
    def _is_video_download(self) -> bool:
        return self.video.options.format in VideoFormat

    @property
    def as_ytdlp_params(self) -> YoutubeDLParams:
        postprocessors: list[dict[str, str | bool | int]] = []
        # Only append audio postprocessor if we are downloading audio format.
        if self._is_audio_download:
            postprocessors.append({
                'key': 'FFmpegExtractAudio',
                'preferredcodec': self.video.options.format.value,
                'preferredquality': '192',
            })
        # Only append video postprocessor if we are downloading video format.
        if self._is_video_download:
            postprocessors.append(
                {
                    'key': 'FFmpegVideoConvertor',
                    'preferedformat': self.video.options.format.value,
                },
            )
        # Only append metadata to the video if enabled by user
        if self.video.options.embed_metadata:
            postprocessors.append({'key': 'FFmpegMetadata'})
        # Only append thumbnail embedding if enabled by user
        if self.video.options.embed_thumbnail:
            postprocessors.append({
                'key': 'EmbedThumbnail',
                'already_have_thumbnail': False,
            })
            self._overrides['writethumbnail'] = True
        if self.video.options.embed_subtitles:
            postprocessors.append({
                'key': 'FFmpegEmbedSubtitle',
                'already_have_subtitle': False,
            })
            self._overrides['writesubtitles'] = True
            self._overrides['subtitlesformat'] = 'best'

        return {
            **DEFAULT_YTDLP_PARAMS,
            **self._overrides,
            'format': self._ytdlp_format,
            'progress_hooks': [self._progress_hook],
            'postprocessor_hooks': [self._postprocessor_hook],
            'post_hooks': [self._post_hook],
            'outtmpl': f'{self._output_directory}/{self.video.id}.%(ext)s',
            'postprocessors': postprocessors,
        }

    @property
    def _ytdlp_format(self) -> str:
        options = self.video.options
        quality = options.quality.value
        extension = options.format.value
        # bestvideo*[ext=X]+bestaudio/bestvideo*+bestaudio/best or
        # worstvideo*[ext=X]+worstaudio/worstvideo*+worstaudio/worst
        if self._is_video_download:
            proper_ext = f'{quality}video*[ext={extension}]+{quality}audio'
            return f'{proper_ext}/{quality}video*+{quality}audio/{quality}'
        # bestaudio[ext=X]/bestaudio/best or worstaudio[ext=X]/worstaudio/worst
        elif self._is_audio_download:
            return f'{quality}audio[ext={extension}]/{quality}audio/{quality}'
        # Default to returning the quality (ie 'best' or 'worst')
        return quality

    def _progress_hook(self, info: ProgressHookInfo) -> None:
        status = info.get('status')
        if status == 'downloading':
            eta = info.get('eta')
            self._handle_status_update(
                DownloadStatus(
                    state=DownloadState.DOWNLOADING,
                    progress=get_progress(info),
                    eta=int(eta) if eta else None,
                ),
            )
        elif status == 'error':
            self._handle_status_update(
                DownloadStatus(state=DownloadState.ERROR),
            )
        elif status == 'finished':
            self._handle_status_update(
                DownloadStatus(state=DownloadState.PROCESSING),
            )

    def _postprocessor_hook(self, info: PostprocessorHookInfo) -> None:
        status = info.get('status')
        postprocessor: str | None = None
        if status == 'started' or status == 'processing':
            postprocessor = info.get('postprocessor')
        elif status == 'finished':
            postprocessor = None
        self._handle_status_update(
            DownloadStatus(
                state=DownloadState.PROCESSING,
                postprocessor=postprocessor,
            ),
        )

    def _post_hook(self, filepath: str) -> None:
        state = DownloadState.DONE
        if not os.path.exists(filepath):
            state = DownloadState.ERROR
        self._handle_status_update(
            DownloadStatus(
                state=state,
            ),
        )

    def _handle_status_update(self, update: DownloadStatus) -> None:
        self.status = update
        # Call each hook with the update
        value = VideoWithOptionsAndStatus(
            **self.video.model_dump(), status=update,
        )
        for h in self._status_hooks:
            h(value)
