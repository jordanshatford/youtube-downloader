import os
from collections.abc import Callable
from typing import TypeAlias

from .models import AudioFormat
from .models import Download
from .models import DownloadState
from .models import DownloadStatus
from .models import VideoFormat
from .utilities import get_ytdlp_progress
from .ytdlp import PostprocessorHookInfo
from .ytdlp import ProgressHookInfo
from .ytdlp import YoutubeDLParams

StatusHook: TypeAlias = Callable[[Download], None]

# Default params used with yt-dlp. These may be overriden by our download
# options.
# Note: if a default isnt provided then the yt-dlp default will be used.
DEFAULT_YTDLP_PARAMS: YoutubeDLParams = {
    'quiet': True,
    'retries': 5,
    'verbose': False,
    'noprogress': True,
}


class DownloadConfig:
    def __init__(self, download: Download, output_directory: str) -> None:
        self.download = download
        self._output_directory = output_directory
        self._status_hooks: list[StatusHook] = []
        self._overrides: YoutubeDLParams = {}

    def add_status_hook(self, hook: StatusHook) -> None:
        self._status_hooks.append(hook)

    def on_status_update(self, status: DownloadStatus) -> None:
        self._handle_status_update(status)

    def add_ytdlp_params_overrides(self, params: YoutubeDLParams) -> None:
        self._overrides = params

    @property
    def filename(self) -> str:
        return f'{self.download.video.id}.{self.download.options.format.value}'

    @property
    def path(self) -> str:
        return os.path.join(self._output_directory, self.filename)

    @property
    def _is_audio_download(self) -> bool:
        return self.download.options.format in AudioFormat

    @property
    def _is_video_download(self) -> bool:
        return self.download.options.format in VideoFormat

    @property
    def as_ytdlp_params(self) -> YoutubeDLParams:
        postprocessors: list[dict[str, str | bool | int]] = []
        # Only append audio postprocessor if we are downloading audio format.
        if self._is_audio_download:
            postprocessors.append({
                'key': 'FFmpegExtractAudio',
                'preferredcodec': self.download.options.format.value,
                'preferredquality': '192',
            })
        # Only append video postprocessor if we are downloading video format.
        if self._is_video_download:
            postprocessors.append(
                {
                    'key': 'FFmpegVideoConvertor',
                    'preferedformat': self.download.options.format.value,
                },
            )
        # Only append metadata to the video if enabled by user
        if self.download.options.embed_metadata:
            postprocessors.append({'key': 'FFmpegMetadata'})
        # Only append thumbnail embedding if enabled by user
        if self.download.options.embed_thumbnail:
            postprocessors.append({
                'key': 'EmbedThumbnail',
                'already_have_thumbnail': False,
            })
            self._overrides['writethumbnail'] = True
        if self.download.options.embed_subtitles:
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
            'outtmpl': f'{self._output_directory}/{self.download.video.id}.%(ext)s',  # noqa
            'postprocessors': postprocessors,
        }

    @property
    def _ytdlp_format(self) -> str:
        options = self.download.options
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
                    progress=get_ytdlp_progress(info),
                    eta=eta,
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
        self.download.status = update
        # Call each hook with the update
        for h in self._status_hooks:
            h(self.download)
