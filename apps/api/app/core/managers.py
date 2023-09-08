from typing import Callable

from ..models import DownloadStatusUpdate
from ..models import VideoWithOptions
from ..models import VideoWithOptionsAndStatus
from .threads import YoutubeDownloadThread


class AudioDownloadManager:
    def __init__(
        self, output_dir: str,
        status_hook: Callable[[DownloadStatusUpdate], None],
    ):
        self._status_hook = status_hook
        self._downloads: dict[str, YoutubeDownloadThread] = {}
        self._output_dir = output_dir

    def __contains__(self, video_id: str) -> bool:
        return video_id in self._downloads

    def add(self, video: VideoWithOptions) -> None:
        if video.id not in self._downloads:
            download = YoutubeDownloadThread(
                video, self._output_dir, self.send_status_update,
            )
            self._downloads[video.id] = download
            download.start()

    def remove(self, video_id: str) -> None:
        if video_id in self._downloads:
            self._downloads[video_id].remove()
            self._downloads.pop(video_id, None)

    def get(self, video_id: str) -> YoutubeDownloadThread | None:
        return self._downloads.get(video_id, None)

    def get_all_videos(self) -> list[VideoWithOptionsAndStatus]:
        return [
            VideoWithOptionsAndStatus(**d.video.dict(), status=d.status)
            for d in self._downloads.values()
        ]

    def send_status_update(self, update: DownloadStatusUpdate) -> None:
        self._status_hook(update)
