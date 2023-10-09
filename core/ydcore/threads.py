import os
import threading
import time
from collections.abc import Callable
from typing import Any

from yt_dlp import YoutubeDL

from .config.ytdlp import PostprocessorHookInfo
from .config.ytdlp import ProgressHookInfo
from .config.ytdlp import YoutubeDLParams
from .models import DownloadOptions
from .models import DownloadState
from .models import DownloadStatus
from .models import DownloadType
from .models import VideoWithOptions
from .models import VideoWithOptionsAndStatus


def get_progress(info: ProgressHookInfo) -> float | None:
    downloaded_bytes = info.get('downloaded_bytes')
    total_bytes = info.get('total_bytes')
    if total_bytes is None:
        total_bytes = info.get('total_bytes_estimate')
    if downloaded_bytes is None or total_bytes is None:
        return None
    return (downloaded_bytes / total_bytes) * 100


def get_ytdlp_format(options: DownloadOptions) -> str:
    quality = options.quality.value
    extension = options.format.value
    # bestvideo*[ext=X]+bestaudio/bestvideo*+bestaudio/best or
    # worstvideo*[ext=X]+worstaudio/worstvideo*+worstaudio/worst
    if (options.type == DownloadType.VIDEO):
        proper_ext = f'{quality}video*[ext={extension}]+{quality}audio'
        return f'{proper_ext}/{quality}video*+{quality}audio/{quality}'
    # bestaudio[ext=X]/bestaudio/best or worstaudio[ext=X]/worstaudio/worst
    elif (options.type == DownloadType.AUDIO):
        return f'{quality}audio[ext={extension}]/{quality}audio/{quality}'
    # Default to returning the quality (ie 'best' or 'worst')
    return quality


class YoutubeDownloadThread(threading.Thread):
    def __init__(
        self,
        video: VideoWithOptions,
        output_directory: str,
        status_hook: Callable[[VideoWithOptionsAndStatus], None],
    ):
        self.video = video
        self._output_directory = output_directory
        self._status_hook = status_hook
        self.status = DownloadStatus(state=DownloadState.WAITING)
        postprocessors: list[dict[str, str]] = []
        # Only append audio postprocessor if we are downloading audio format.
        if self.video.options.type == DownloadType.AUDIO:
            postprocessors.append({
                'key': 'FFmpegExtractAudio',
                'preferredcodec': self.video.options.format.value,
                'preferredquality': '192',
            })
        # Only append video postprocessor if we are downloading video format.
        if self.video.options.type == DownloadType.VIDEO:
            postprocessors.append(
                {
                    'key': 'FFmpegVideoConvertor',
                    'preferedformat': self.video.options.format.value,
                },
            )
        # Only append metadata to the video if enabled by user
        if self.video.options.embed_metadata:
            postprocessors.append({'key': 'FFmpegMetadata'})
        YOUTUBE_DL_OPTIONS: YoutubeDLParams = {
            'format': get_ytdlp_format(self.video.options),
            'progress_hooks': [self.progress_hook],
            'postprocessor_hooks': [self.postprocessor_hook],
            'post_hooks': [self.post_hook],
            'outtmpl': f'{self._output_directory}/{self.video.id}.%(ext)s',
            'quiet': True,
            'postprocessors': postprocessors,
        }
        self._downloader = YoutubeDL(YOUTUBE_DL_OPTIONS)

        super().__init__(
            group=None, target=None, name=None, daemon=True,
        )

    @property
    def filename(self) -> str:
        return f'{self.video.id}.{self.video.options.format.value}'

    @property
    def path(self) -> str:
        return os.path.join(self._output_directory, self.filename)

    @property
    def filename_using_title(self) -> str:
        return f'{self.video.title}.{self.video.options.format.value}'

    def progress_hook(self, info: ProgressHookInfo) -> None:
        status = info.get('status')
        if status == 'downloading':
            self._handle_status_update(
                DownloadStatus(
                    state=DownloadState.DOWNLOADING,
                    progress=get_progress(info),
                    eta=info.get('eta'),
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

    def postprocessor_hook(self, info: PostprocessorHookInfo) -> None:
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

    def post_hook(self, _filepath: str) -> None:
        self._handle_status_update(
            DownloadStatus(
                state=DownloadState.DONE,
            ),
        )

    def remove(self) -> bool:
        if os.path.exists(self.path):
            os.remove(self.path)
            return True
        return False

    def run(self):
        self._handle_status_update(
            DownloadStatus(state=DownloadState.DOWNLOADING),
        )
        try:
            self._downloader.download([str(self.video.url)])
        except Exception:
            self._handle_status_update(
                DownloadStatus(state=DownloadState.ERROR),
            )

    def _handle_status_update(self, update: DownloadStatus) -> None:
        self.status = update
        self._status_hook(
            VideoWithOptionsAndStatus(
                **self.video.model_dump(), status=update,
            ),
        )


class RepeatedTimer:
    def __init__(
        self, interval: int, function: Callable[..., None],
        *args: Any, **kwargs: Any,
    ):
        self._timer: threading.Timer | None = None
        self.interval = interval
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.is_running = False
        self.next_call = time.time()
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self.next_call += self.interval
            self._timer = threading.Timer(
                self.next_call - time.time(), self._run,
            )
            self._timer.daemon = True
            self._timer.start()
            self.is_running = True

    def stop(self):
        if self._timer is not None:
            self._timer.cancel()
        self.is_running = False
