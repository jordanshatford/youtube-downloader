import os
import shutil
import uuid
from datetime import datetime
from datetime import timedelta
from queue import Queue

from .core import Download
from .core import DownloadManager
from .core import YouTubeSearch
from .timer import RepeatedTimer


class Session:
    def __init__(self, id: str, session_dir: str) -> None:
        self.id = id
        self._output_dir = os.path.join(session_dir, id)
        self._last_use = datetime.now()
        self.search: YouTubeSearch | None = None
        self.download_manager = DownloadManager(
            self._output_dir, self._status_hook,
        )
        self.status_queue: Queue[Download] = Queue()

    def update_use_time(self) -> None:
        self._last_use = datetime.now()

    def session_older_than(self, seconds: int) -> bool:
        return self._last_use < datetime.now() - timedelta(seconds=seconds)

    def cleanup(self) -> None:
        try:
            if os.path.exists(self._output_dir):
                shutil.rmtree(self._output_dir)
        except FileNotFoundError:
            pass

    def _status_hook(self, update: Download) -> None:
        self.status_queue.put(update)


class SessionManager:
    def __init__(
        self,
        session_dir: str = os.path.join(os.getcwd(), 'sessions'),
        session_to_old_duration: int = 60 * 60 * 2,  # 2 hours
        cleanup_interval: int = 60 * 60 * 3,  # 3 hours
    ) -> None:
        self._session_dir = session_dir
        self._session_too_old_duration = session_to_old_duration
        self._cleanup_interval = cleanup_interval
        self._cleanup_timer = RepeatedTimer(
            self._cleanup_interval, self.cleanup,
        )
        self._sessions: dict[str, Session] = {}

    def __contains__(self, id: str) -> bool:
        return id in self._sessions

    def create(self) -> str:
        session_id = str(uuid.uuid4())
        self._sessions[session_id] = Session(session_id, self._session_dir)
        return session_id

    def get(self, id: str) -> Session | None:
        # Update use time of session
        if id in self._sessions:
            self._sessions[id].update_use_time()
        return self._sessions.get(id, None)

    def remove(self, id: str) -> None:
        if id in self._sessions:
            self._sessions[id].cleanup()
            self._sessions.pop(id, None)

    def cleanup(self, force: bool = False) -> None:
        for session_id in self._sessions.copy():
            session_not_used = self._sessions[session_id].session_older_than(
                self._session_too_old_duration,
            )
            if session_not_used or force:
                self.remove(session_id)
        if force:
            try:
                if os.path.exists(self._session_dir):
                    shutil.rmtree(self._session_dir)
            except FileNotFoundError:
                pass


session_manager = SessionManager()
