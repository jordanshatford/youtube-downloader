import os
import threading
import time
from typing import Any
from typing import Callable
from typing import Literal
from typing import NotRequired
from typing import TypeAlias
from typing import TypedDict

from yt_dlp import YoutubeDL

from ..models import DownloadState
from ..models import DownloadStatus
from ..models import DownloadStatusUpdate
from ..models import VideoWithOptions
from .processors import FileProcessingComplete


# Basic type describing info_dict provided in hooks, Not specific as of now.
YoutubeDLInfoDict: TypeAlias = dict[str, Any]


# Info returned to a given download hook, excluding certain fields prefixed
# with underscore.
#
# Note: NotRequired fields are not present when download is 'finished'.
class DownloadHookInfo(TypedDict):
    status: Literal['downloading', 'finished']
    downloaded_bytes: int
    total_bytes: int
    filename: str
    tmpfilename: NotRequired[str]
    eta: NotRequired[int]
    speed: float
    elapsed: float
    info_dict: YoutubeDLInfoDict


def get_progress(info: DownloadHookInfo) -> float | None:
    downloaded_bytes = info.get('downloaded_bytes')
    total_bytes = info.get('total_bytes')
    if downloaded_bytes is None or total_bytes is None:
        return None
    return (downloaded_bytes / total_bytes) * 100


class YoutubeDownloadThread(threading.Thread):
    def __init__(
        self,
        video: VideoWithOptions,
        output_directory: str,
        status_update: Callable[[DownloadStatusUpdate], None],
    ):
        self.video = video
        self._output_directory = output_directory
        self._status_update = status_update
        self.status = DownloadStatus(state=DownloadState.WAITING)

        YOUTUBE_DL_OPTIONS = {
            'format': 'bestaudio/best',
            'progress_hooks': [self.download_progress_hook],
            'outtmpl': f'{self._output_directory}/{self.video.id}.%(ext)s',
            'quiet': True,
            'postprocessors': [
                {
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': self.video.options.format.value,
                    'preferredquality': '192',
                },
                {'key': 'FFmpegMetadata'},
            ],
        }
        self._downloader = YoutubeDL(YOUTUBE_DL_OPTIONS)
        self._downloader.add_post_processor(
            FileProcessingComplete(
                self._handle_status_update, downloader=self._downloader,
            ),
        )

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

    def download_progress_hook(self, progress_info: DownloadHookInfo) -> None:
        status = progress_info.get('status')
        if status == 'downloading':
            self._handle_status_update(
                DownloadStatus(
                    state=DownloadState.DOWNLOADING,
                    progress=get_progress(progress_info),
                ),
            )
        elif status == 'finished':
            self._handle_status_update(
                DownloadStatus(state=DownloadState.PROCESSING),
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
        self._status_update(
            DownloadStatusUpdate(
                id=self.video.id, **update.dict(),
            ),
        )


class RepeatedTimer:
    def __init__(self, interval: int, function: Callable, *args, **kwargs):
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
