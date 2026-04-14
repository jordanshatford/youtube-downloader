import datetime
import logging
import pathlib
import shutil
import tempfile
import uuid
from multiprocessing.pool import ThreadPool

from .core import DownloadsManager
from .core import YouTubeSearchManager
from .timer import RepeatedTimer

logger = logging.getLogger("api")


class Session:
    def __init__(
        self,
        directory: pathlib.Path,
        *,
        processes: int | None = None,
    ) -> None:
        self.id = str(uuid.uuid4())
        self._directory = directory / self.id
        self._last_use = datetime.datetime.now(tz=datetime.UTC)
        # Temporary directory used for the session.
        self._tmp: tempfile.TemporaryDirectory = tempfile.TemporaryDirectory()
        # Thread pool for this users session, shared accross the various features.
        self._pool = ThreadPool(processes)
        # Track current search for each session so that we can more easily get
        # next page when requested.
        self.search = YouTubeSearchManager()
        # Each session has there own download manager that handles downloading
        # all requested files to its own location.
        self.downloads = DownloadsManager(self._directory, self._tmp, self._pool)

        logger.debug(
            "[Session]: initializing with output at %s and %s thread processes.",
            self._directory,
            processes,
        )

    # Update the use time of the session to now. To prevent it from being
    # cleaned up as it is currently being used.
    def update_use_time(self) -> None:
        self._last_use = datetime.datetime.now(tz=datetime.UTC)

    # Check if a session is older than some delta. Used to determin if it
    # should be cleaned up next cleanup cycle.
    def is_older_than(self, delta: datetime.timedelta) -> bool:
        return self._last_use < datetime.datetime.now(tz=datetime.UTC) - delta

    # Cleanup all files related to the session.
    def cleanup(self) -> None:
        logger.debug("[Session]: cleaning up %s.", self.id)
        self._tmp.cleanup()
        try:
            if self._directory.exists():
                shutil.rmtree(self._directory)
        except FileNotFoundError:
            pass


class SessionsManager:
    def __init__(
        self,
        *,
        directory: pathlib.Path | None = None,
        session_too_old_delta: datetime.timedelta | None = None,
    ) -> None:
        self._sessions: dict[str, Session] = {}
        # Location where all session related files will be downloaded. Default to the
        # current working directory where the API is being run.
        if directory is not None:
            self._directory = directory / "sessions"
        else:
            self._directory = pathlib.Path.cwd() / "sessions"
        # Time delta used to determine if a session has been inactive for too long,
        # after which case it will be cleaned up next cleanup check.
        if session_too_old_delta is not None:
            self._session_too_old_delta = session_too_old_delta
        else:
            self._session_too_old_delta = datetime.timedelta(hours=2)
        # Create a repeated task to attempt to cleanup any sessions that are too old.
        # This checks at a rate 1.5 times the session too old delta.
        self._cleanup_timer = RepeatedTimer(
            round(self._session_too_old_delta.total_seconds() * 1.5),
            self.cleanup,
        )

    # Check if the session manager contains a session with a given ID.
    def __contains__(self, session_id: str) -> bool:
        return session_id in self._sessions

    # Create a new session with a generated UUID for the session ID.
    def create(self) -> str:
        session = Session(self._directory)
        self._sessions[session.id] = session
        return session.id

    # Get the session. If it exists also update its latest use time to ensure that
    # it does not get cleaned up next time we do a cleanup check.
    def get(self, session_id: str) -> Session | None:
        session = self._sessions.get(session_id, None)
        if session is not None:
            session.update_use_time()
        return session

    # Remove a session from the manager, cleaning up anything it has created.
    def remove(self, session_id: str) -> None:
        session = self._sessions.pop(session_id, None)
        if session is not None:
            session.cleanup()

    # Attempt to cleanup all sessions. If it should be done with force, all
    # sessions will be force removed, and the session directory will be removed.
    def cleanup(self, *, force: bool = False) -> None:
        logger.debug(
            "[Sessions]: attempting to cleanup all sessions (force=%s).", force
        )
        for session_id, session in self._sessions.copy().items():
            if session.is_older_than(self._session_too_old_delta) or force:
                self.remove(session_id)
        if force:
            try:
                if self._directory.exists():
                    shutil.rmtree(self._directory)
            except FileNotFoundError:
                pass


session_manager = SessionsManager()
