import datetime
import pathlib
import shutil
import uuid
from queue import Queue

from .core import Download
from .core import DownloadManager
from .core import YouTubeSearch
from .timer import RepeatedTimer


def now() -> datetime.datetime:
    return datetime.datetime.now(tz=datetime.UTC)


class Session:
    def __init__(self, session_id: str, sessions_dir: pathlib.Path) -> None:
        self.id = session_id
        self._output_dir = sessions_dir / session_id
        self._last_use = now()
        self.search: YouTubeSearch | None = None
        self.download_manager = DownloadManager(
            self._output_dir,
            self._status_hook,
        )
        self.status_queue: Queue[Download] = Queue()

    def update_use_time(self) -> None:
        self._last_use = now()

    def session_older_than(self, seconds: int) -> bool:
        return self._last_use < now() - datetime.timedelta(seconds=seconds)

    def cleanup(self) -> None:
        try:
            if self._output_dir.exists():
                shutil.rmtree(self._output_dir)
        except FileNotFoundError:
            pass

    def _status_hook(self, update: Download) -> None:
        self.status_queue.put(update)


class SessionsManager:
    def __init__(
        self,
        session_dir: pathlib.Path | None = None,
        session_to_old_duration: int = 60 * 60 * 2,  # 2 hours
        cleanup_interval: int = 60 * 60 * 3,  # 3 hours
    ) -> None:
        self._session_dir = (
            session_dir if session_dir is not None else pathlib.Path.cwd()
        ) / "sessions"
        self._session_too_old_duration = session_to_old_duration
        self._cleanup_timer = RepeatedTimer(
            cleanup_interval,
            self.cleanup,
        )
        self._sessions: dict[str, Session] = {}

    def __contains__(self, session_id: str) -> bool:
        return session_id in self._sessions

    def create(self) -> str:
        session_id = str(uuid.uuid4())
        self._sessions[session_id] = Session(session_id, self._session_dir)
        return session_id

    def get(self, session_id: str) -> Session | None:
        # Update use time of session
        if session_id in self._sessions:
            self._sessions[session_id].update_use_time()
        return self._sessions.get(session_id, None)

    def remove(self, session_id: str) -> None:
        if session_id in self._sessions:
            self._sessions[session_id].cleanup()
            self._sessions.pop(session_id, None)

    def cleanup(self, *, force: bool = False) -> None:
        for session_id in self._sessions.copy():
            session_not_used = self._sessions[session_id].session_older_than(
                self._session_too_old_duration,
            )
            if session_not_used or force:
                self.remove(session_id)
        if force:
            try:
                if self._session_dir.exists():
                    shutil.rmtree(self._session_dir)
            except FileNotFoundError:
                pass


session_manager = SessionsManager()
