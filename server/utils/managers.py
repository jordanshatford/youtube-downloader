import json
import os
import shutil

from datetime import datetime
from datetime import timedelta
from queue import Queue

from .threads import YoutubeDownloadThread, RepeatedTimer
from .sse import ServerSentEvent


class AudioDownloadManager:
    def __init__(self, output_dir: str, announcer: callable):
        self._announcer = announcer
        self._downloads = {}
        self._output_dir = output_dir

    def add(self, video_id: str, url: str) -> None:
        if video_id not in self._downloads:
            download = YoutubeDownloadThread(video_id, url, self._output_dir, self.send_status_update)
            self._downloads[video_id] = download
            download.start()

    def remove(self, video_id: str) -> None:
        self._downloads[video_id].remove()
        self._downloads.pop(video_id, None)

    def get_download(self, video_id: str) -> str:
        path = self._downloads[video_id].get_file_location() # TODO: prevent errors here
        return path

    def send_status_update(self, video_id: str, status: str) -> None:
        self._announcer(video_id, status)


class Session:
    def __init__(self, id: str, session_dir: str):
        self._id = id
        self.output_dir = os.path.join(session_dir, id)
        self._last_use = datetime.now()
        self.download_manager = AudioDownloadManager(self.output_dir, announcer=self._status_update)
        self.status_queue = Queue()

    def update_use_time(self):
        self._last_use = datetime.now()

    def session_older_than(self, seconds: int) -> bool:
        return self._last_use < datetime.now() - timedelta(seconds=seconds)

    def _status_update(self, video_id: str, status: str):
        msg = ServerSentEvent(data=json.dumps({ "id": video_id, "status": status.value }))
        self.status_queue.put(msg.encode())


class SessionManager:
    def __init__(
        self,
        session_dir: str = os.path.join(os.getcwd(), "sessions"),
        cleanup_interval: int = 60 * 60 * 3,
        session_to_old_duration: int = 60 * 60 * 2,
    ):
        self._sessions = {}
        self.session_dir = session_dir
        self._session_too_old_duration = session_to_old_duration
        self._cleanup_interval = cleanup_interval
        self._cleanup_timer = RepeatedTimer(self._cleanup_interval, self.cleanup)

    def cleanup(self):
        for session_id in self._sessions.copy():
            session_not_used = self._sessions[session_id].session_older_than(self._session_too_old_duration)
            if session_not_used:
                self._clean_session_files(session_id)
                self._sessions.pop(session_id, None)

    def setup_session(self, id: str):
        self._sessions[id] = Session(id, self.session_dir)

    def remove(self, id: str):
        self._clean_session_files(id)
        self._sessions.pop(id, None)

    def get_download_manager(self, id: str) -> AudioDownloadManager:
        return self._sessions[id].download_manager

    def get_status_queue(self, id: str) -> Queue:
        return self._sessions[id].status_queue

    def update_session_use_time(self, id: str):
        self._sessions[id].update_use_time()

    def _clean_session_files(self, id: str):
        shutil.rmtree(self._sessions[id].output_dir)


session_manager = SessionManager()