import logging
from typing import cast

from app.core.models import Video
from app.core.parse import parse_video_info_to_video
from app.core.ytdlp import DEFAULT_YOUTUBE_DL_PARAMS
from app.core.ytdlp import VideoInfo
from app.core.ytdlp import YoutubeDL
from app.core.ytdlp import YoutubeDLParams

logger = logging.getLogger("core")


class YouTubeSearchManager:
    def __init__(self, *, page_size: int = 20) -> None:
        self._query: str | None = None
        self._page_size: int = page_size
        self._page: int = 1
        self._results: list[Video] = []
        self._has_more = False

    @property
    def query(self) -> str:
        return "" if self._query is None else self._query

    @property
    def results(self) -> list[Video]:
        return self._results

    @property
    def has_more(self) -> bool:
        return self._has_more

    def get(self, query: str) -> list[Video]:
        self._query = query
        self._page = 1
        results = self._fetch_current_page()
        self._results = results
        self._has_more = len(results) != 0
        return results

    def get_next(self) -> list[Video]:
        if not self._has_more:
            logger.debug(
                "[YouTubeSearchManager]: No more search results for '%s'.", self._query
            )
            return []

        self._page += 1
        results = self._fetch_current_page()
        self._has_more = len(results) != 0
        self._results = [*self.results, *results]
        return results

    @property
    def _playlist_items(self) -> str:
        # Get the lower and upper bounds to search yt-dlp with based on the
        # page we are currently on and our page size. yt-dlp expects it in
        # the format 1:20 which would return the first to twentieth videos.
        base: int = (self._page - 1) * self._page_size
        lower: int = base + 1
        upper: int = base + self._page_size
        return f"{lower}:{upper}"

    def _fetch_current_page(self) -> list[Video]:
        params: YoutubeDLParams = {
            **DEFAULT_YOUTUBE_DL_PARAMS,
            "extract_flat": True,
            "playlist_items": self._playlist_items,
        }
        with YoutubeDL(params) as ydl:
            result = cast(
                "VideoInfo",
                ydl.extract_info(f"ytsearchall:{self._query}", download=False),
            )
            entries = result.get("entries")

            if entries is None:
                logger.debug(
                    "[YouTubeSearchManager]: No entries for '%s' page %d.",
                    self._query,
                    self._page,
                )
                return []

            # Only parse and include entries that are not already present in the list.
            parsed = [parse_video_info_to_video(entry) for entry in entries]
            existing = {v.id for v in self._results}
            return [
                video
                for video in parsed
                if video is not None and video.id not in existing
            ]
