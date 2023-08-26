import os
import threading
import time
from typing import Callable

from yt_dlp import YoutubeDL

from ..models import Status
from ..models import Video
from .processors import FileProcessingComplete


class YoutubeDownloadThread(threading.Thread):
    def __init__(
        self,
        video: Video,
        output_directory: str,
        status_update: Callable[[str, Status], None],
    ):
        self.video = video
        self._output_directory = output_directory
        self._status_update = status_update
        self.status = Status.WAITING

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

    def download_progress_hook(self, progress_info: dict[str, str]) -> None:
        if progress_info.get('status', None) == 'finished':
            self._handle_status_update(Status.PROCESSING)

    def get_file_location(self) -> str:
        filename = f'{self.video.id}.{self.video.options.format.value}'
        return os.path.join(self._output_directory, filename)

    def remove(self) -> bool:
        path = self.get_file_location()
        if os.path.exists(path):
            os.remove(path)
            return True
        return False

    def run(self):
        self._handle_status_update(Status.DOWNLOADING)
        try:
            self._downloader.download([str(self.video.url)])
        except Exception:
            self._handle_status_update(Status.ERROR)

    def _handle_status_update(self, status: Status) -> None:
        self.status = status
        self._status_update(self.video.id, status)


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
