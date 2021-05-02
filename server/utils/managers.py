import json
import os

from datetime import datetime
from queue import Queue

from .threads import YoutubeDownloadThread
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
        self._output_dir = os.path.join(session_dir, id)
        self._last_use = datetime.now()
        self.download_manager = AudioDownloadManager(self._output_dir, announcer=self._status_update)
        self.status_queue = Queue()

    def update_use_time(self):
        self._last_use = datetime.now()

    def _status_update(self, video_id, status):
        msg = ServerSentEvent(data=json.dumps({ "id": video_id, "status": status.value }))
        self.status_queue.put(msg.encode())


class SessionManager:
    def __init__(self, session_dir: str = os.path.join(os.getcwd(), "sessions")):
        self._sessions = {}
        self._session_dir = session_dir

    def cleanup(self):
        for session_id in self._sessions:
            self._clean_session_files(session_id)
            self._downloads.pop(session_id, None)

    def setup_session(self, id: str):
        self._sessions[id] = Session(id, self._session_dir)

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
        return # TODO: remove session folder


session_manager = SessionManager()