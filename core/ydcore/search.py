import logging
from typing import Any

from pydantic import HttpUrl

from .innertube import InnerTubeClient
from .models import Channel
from .models import Video


logger = logging.getLogger('ydcore')


_YOUTUBE_BASE_URL = 'https://www.youtube.com'


# Get entry from nested dict based on key path
def _get(source: dict[Any, Any], path: list[Any]) -> Any:
    value = source
    for key in path:
        # If the key is for a dict
        if type(key) is str:
            if key in value:
                value = value[key]
            else:
                raise KeyError(key)
        # If the key is for a list
        elif type(key) is int:
            if len(value) != 0:
                value = value[key]
            else:
                raise KeyError(key)
    return value


class YouTubeSearch:
    def __init__(self, query: str) -> None:
        self._query = query
        self._innertube_client = InnerTubeClient()
        self._results: list[Video] = []
        self._continuation: str | None = None
        # Get initial results.
        results, continuation = self._fetch_and_parse()
        self._results = results
        self._continuation = continuation

    @property
    def results(self) -> list[Video]:
        return self._results

    def next(self) -> bool:
        # If continuation exists, fetch new results to replace existing ones.
        if self._continuation:
            results, continuation = self._fetch_and_parse()
            self._results = results
            self._continuation = continuation
            logger.debug(
                f'Found {len(results)} results for search: {self._query}.',
            )
            return True
        else:
            logger.debug(f'No more results for search: {self._query}.')
            return False

    def _fetch_and_parse(self) -> tuple[list[Video], str | None]:
        response = self._innertube_client.search(
            self._query, self._continuation,
        )

        sections: dict[Any, Any] = {}
        # Initial result is handled by try block, continuations handled
        # by except block.
        try:
            sections = _get(
                response, [
                    'contents', 'twoColumnSearchResultsRenderer',
                    'primaryContents', 'sectionListRenderer', 'contents',
                ],
            )
        except KeyError:
            sections = _get(
                response, [
                    'onResponseReceivedCommands', 0,
                    'appendContinuationItemsAction', 'continuationItems',
                ],
            )

        item_renderer: dict[str, Any] | None = None
        continuation_renderer: dict[str, Any] | None = None

        for section in sections:
            if 'itemSectionRenderer' in section:
                item_renderer = section['itemSectionRenderer']
            if 'continuationItemRenderer' in section:
                continuation_renderer = section['continuationItemRenderer']

        # If the continuationItemRenderer doesn't exist,
        # assume no further results
        continuation: str | None = None
        if continuation_renderer:
            continuation = _get(
                continuation_renderer, [
                    'continuationEndpoint', 'continuationCommand', 'token',
                ],
            )

        videos: list[Video] = []

        # If the itemSectionRenderer doesn't exist, assume no results.
        if item_renderer:
            raw_videos = item_renderer['contents']
            for raw_content in raw_videos:
                # Skip over anything that is not a video.
                if 'videoRenderer' not in raw_content:
                    continue
                raw_video = raw_content['videoRenderer']
                v = self._parse_video(raw_video)
                videos.append(v)

        return videos, continuation

    def _parse_video(self, source: dict[Any, Any]) -> Video:
        video_id = source['videoId']
        url = HttpUrl(f'{_YOUTUBE_BASE_URL}/watch?v={video_id}')
        title = _get(source, ['title', 'runs', 0, 'text'])
        duration = _get(source, ['lengthText', 'simpleText'])
        if duration is None:
            duration = '--:--'
        thumbnails = _get(source, ['thumbnail', 'thumbnails'])
        thumbnail = HttpUrl(thumbnails[0]['url'])
        channel = self._parse_channel(source)
        return Video(
            id=video_id,
            url=url,
            title=title,
            duration=duration,
            thumbnail=thumbnail,
            channel=channel,
        )

    def _parse_channel(self, source: dict[Any, Any]) -> Channel:
        name = _get(source, ['ownerText', 'runs', 0, 'text'])
        # First attempt to get channel url in format youtube.com/@channel
        # If that fails, instead get the url in format youtube.com/channel/id
        try:
            uri = _get(
                source, [
                    'ownerText', 'runs', 0, 'navigationEndpoint',
                    'commandMetadata', 'webCommandMetadata', 'url',
                ],
            )
            url = HttpUrl(f'{_YOUTUBE_BASE_URL}{uri}')
        except KeyError:
            uri = _get(
                source, [
                    'ownerText', 'runs', 0, 'navigationEndpoint',
                    'browseEndpoint', 'browseId',
                ],
            )
            url = HttpUrl(f'{_YOUTUBE_BASE_URL}/channel/{uri}')

        thumbnails = _get(
            source, [
                'channelThumbnailSupportedRenderers',
                'channelThumbnailWithLinkRenderer',
                'thumbnail',
                'thumbnails',
            ],
        )
        thumbnail = HttpUrl(thumbnails[0]['url'])
        return Channel(
            name=name,
            url=url,
            thumbnail=thumbnail,
        )
