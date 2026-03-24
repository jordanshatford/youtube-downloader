import datetime
import logging
from collections.abc import Sequence
from typing import cast

from pydantic import HttpUrl

from .models import Channel
from .models import Video
from .ytdlp import DEFAULT_YOUTUBE_DL_PARAMS
from .ytdlp import Thumbnail
from .ytdlp import VideoInfo
from .ytdlp import YoutubeDL
from .ytdlp import YoutubeDLParams

logger = logging.getLogger("core")


class YouTubeSearch:
    def __init__(self, query: str, *, page_size: int = 20) -> None:
        self._query = query
        self._page_size = page_size
        self._page = 1
        self._results = self._fetch_current_page()

    @property
    def results(self) -> list[Video]:
        return self._results

    @property
    def _has_more(self) -> bool:
        return len(self._results) != 0

    def next(self) -> bool:
        if not self._has_more:
            logger.debug("No more search results for '%s'.", self._query)
            return False

        self._page += 1
        self._results = self._fetch_current_page()
        return self._has_more

    @property
    def _playlist_items(self) -> str:
        # Get the lower and upper bounds to search yt-dlp with based on the
        # page we are currently on and our page size. yt-dlp expects it in
        # the format 1:20 which would return the first to twentieth videos.
        base = (self._page - 1) * self._page_size
        lower = base + 1
        upper = base + self._page_size
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

            return [self._parse_entry_to_video(entry) for entry in entries]

    def _parse_entry_to_video(self, entry: VideoInfo) -> Video:
        title = entry["title"]
        url = entry["url"]
        duration = entry["duration"]
        duration_str = (
            f"{datetime.timedelta(seconds=duration)}" if duration is not None else "???"
        )
        return Video(
            id=entry["id"],
            title=title if title is not None else "Unknown",
            url=HttpUrl(url)
            if url is not None
            else HttpUrl("https://www.youtube.com/"),
            duration=duration_str,
            thumbnail=self._parse_entry_to_thumbnail(entry["thumbnails"]),
            channel=self._parse_entry_to_channel(entry),
        )

    def _parse_entry_to_channel(self, entry: VideoInfo) -> Channel:
        # Attempt to read the channel name and url using the channel entries.
        # If for some reason that failed, use the uploader entries. Either way
        # fallback to unknown values as channel information is not as important.
        name = entry["channel"] or entry["uploader"]
        url = entry["channel_url"] or entry["uploader_url"]
        return Channel(
            name=name if name is not None else "Unknown",
            url=HttpUrl(url) if url is not None else url,
        )

    def _parse_entry_to_thumbnail(
        self, thumbnails: Sequence[Thumbnail] | None
    ) -> HttpUrl:
        fallback = HttpUrl("https://www.youtube.com/")
        if thumbnails is None:
            return fallback

        # Get the best thumbnail out of available options. This returns the last
        # thumbnail in the list as they are sorted as such. As an improvement we
        # should check for the thumbnail with the best resolution.
        thumbnail = thumbnails[-1]
        if thumbnail is None:
            return fallback

        url = thumbnail["url"]
        return HttpUrl(url) if url is not None else fallback
