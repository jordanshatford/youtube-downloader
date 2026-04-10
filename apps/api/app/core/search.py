import logging
from typing import cast

from .models import Video
from .parse import parse_video_info_to_video
from .ytdlp import DEFAULT_YOUTUBE_DL_PARAMS
from .ytdlp import VideoInfo
from .ytdlp import YoutubeDL
from .ytdlp import YoutubeDLParams

logger = logging.getLogger("core")


class YouTubeSearch:
    def __init__(self, query: str, *, page_size: int = 20) -> None:
        self._query: str = query
        self._page_size: int = page_size
        self._page: int = 1
        self._results: list[Video] = []
        self._results = self._fetch_current_page()
        self._has_more: bool = len(self._results) != 0

    @property
    def query(self) -> str:
        return self._query

    @property
    def results(self) -> list[Video]:
        return self._results

    @property
    def has_more(self) -> bool:
        return self._has_more

    def next(self) -> list[Video]:
        if not self._has_more:
            logger.debug("No more search results for '%s'.", self._query)
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
                    "No entries returned from search '%s' page %d.",
                    self._query,
                    self._page,
                )
                return []

            # Only parse and include entries that are not already present in the list.
            parsed = [parse_video_info_to_video(entry) for entry in entries]
            existing = {v.id for v in self._results}
            return [video for video in parsed if video.id not in existing]
