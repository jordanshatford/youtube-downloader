import json
import os
import shutil
from datetime import datetime
from datetime import timedelta
from queue import Queue
from typing import Callable
from typing import Dict
from typing import Union

from .helpers import format_status_update
from .helpers import Status
from .models import AudioOptions
from .threads import RepeatedTimer
from .threads import YoutubeDownloadThread


class AudioDownloadManager:
    def __init__(self, output_dir: str, announcer: Callable[[str, Status], None]):
        self._announcer = announcer
        self._downloads: Dict[str, YoutubeDownloadThread] = {}
        self._output_dir = output_dir

    def add(self, video_id: str, url: str, options: AudioOptions) -> None:
        if video_id not in self._downloads:
            download = YoutubeDownloadThread(
                video_id, url, options, self._output_dir, self.send_status_update
            )
            self._downloads[video_id] = download
            download.start()

    def remove(self, video_id: str) -> None:
        try:
            self._downloads[video_id].remove()
            self._downloads.pop(video_id, None)
        except KeyError:
            pass

    def get_download(self, video_id: str) -> Union[str, None]:
        try:
            path = self._downloads[video_id].get_file_location()
            return path
        except KeyError:
            return None

    def send_status_update(self, video_id: str, status: Status) -> None:
        self._announcer(video_id, status)


class Session:
    def __init__(self, id: str, session_dir: str):
        self._id = id
        self.output_dir = os.path.join(session_dir, id)
        self._last_use = datetime.now()
        self.download_manager = AudioDownloadManager(
            self.output_dir, announcer=self._status_update
        )
        self.status_queue: Queue[str] = Queue()

    def update_use_time(self):
        self._last_use = datetime.now()

    def session_older_than(self, seconds: int) -> bool:
        return self._last_use < datetime.now() - timedelta(seconds=seconds)

    def cleanup(self):
        try:
            if os.path.exists(self.output_dir):
                shutil.rmtree(self.output_dir)
        except FileNotFoundError:
            pass

    def _status_update(self, video_id: str, status: Status):
        self.status_queue.put(json.dumps(format_status_update(video_id, status)))


class SessionManager:
    def __init__(
        self,
        session_dir: str = os.path.join(os.getcwd(), "sessions"),
        cleanup_interval: int = 60 * 60 * 3,  # 3 hours
        session_to_old_duration: int = 60 * 60 * 2,  # 2 hours
    ):
        self._sessions: Dict[str, Session] = {}
        self.session_dir = session_dir
        self._session_too_old_duration = session_to_old_duration
        self._cleanup_interval = cleanup_interval
        self._cleanup_timer = RepeatedTimer(self._cleanup_interval, self.cleanup)

    def cleanup(self, force: bool = False):
        for session_id in self._sessions.copy():
            session_not_used = self._sessions[session_id].session_older_than(
                self._session_too_old_duration
            )
            if session_not_used or force:
                self.remove(session_id)

    def setup_session(self, id: str):
        self._sessions[id] = Session(id, self.session_dir)

    def remove(self, id: str):
        try:
            self._sessions[id].cleanup()
            self._sessions.pop(id, None)
        except KeyError:
            pass

    def get_download_manager(self, id: str) -> AudioDownloadManager:
        self._update_session_use_time(id)
        try:
            return self._sessions[id].download_manager
        except KeyError:
            self.setup_session(id)
            return self._sessions[id].download_manager

    def get_status_queue(self, id: str) -> Queue:
        self._update_session_use_time(id)
        try:
            return self._sessions[id].status_queue
        except KeyError:
            self.setup_session(id)
            return self._sessions[id].status_queue

    def _update_session_use_time(self, id: str):
        try:
            self._sessions[id].update_use_time()
        except KeyError:
            self.setup_session(id)


session_manager = SessionManager()
