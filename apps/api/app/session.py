import os
import shutil
import threading
import time
import uuid
from collections.abc import Callable
from datetime import datetime
from datetime import timedelta
from queue import Queue
from typing import Any

from ydcore import DownloadManager
from ydcore import VideoWithOptionsAndStatus


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


class Session:
    def __init__(self, id: str, session_dir: str):
        self.id = id
        self._output_dir = os.path.join(session_dir, id)
        self._last_use = datetime.now()
        self.download_manager = DownloadManager(
            self._output_dir, self._status_hook,
        )
        self.status_queue: Queue[VideoWithOptionsAndStatus] = Queue()

    def update_use_time(self):
        self._last_use = datetime.now()

    def session_older_than(self, seconds: int) -> bool:
        return self._last_use < datetime.now() - timedelta(seconds=seconds)

    def cleanup(self):
        try:
            if os.path.exists(self._output_dir):
                shutil.rmtree(self._output_dir)
        except FileNotFoundError:
            pass

    def _status_hook(self, update: VideoWithOptionsAndStatus):
        self.status_queue.put(update)


class SessionManager:
    def __init__(
        self,
        session_dir: str = os.path.join(os.getcwd(), 'sessions'),
        cleanup_interval: int = 60 * 60 * 3,  # 3 hours
        session_to_old_duration: int = 60 * 60 * 2,  # 2 hours
    ):
        self._sessions: dict[str, Session] = {}
        self._session_dir = session_dir
        self._session_too_old_duration = session_to_old_duration
        self._cleanup_interval = cleanup_interval
        self._cleanup_timer = RepeatedTimer(
            self._cleanup_interval, self.cleanup,
        )

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

    def remove(self, id: str):
        if id in self._sessions:
            self._sessions[id].cleanup()
            self._sessions.pop(id, None)

    def cleanup(self, force: bool = False):
        for session_id in self._sessions.copy():
            session_not_used = self._sessions[session_id].session_older_than(
                self._session_too_old_duration,
            )
            if session_not_used or force:
                self.remove(session_id)


session_manager = SessionManager()
