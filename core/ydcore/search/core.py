import json
from typing import Any
from urllib.parse import urlencode
from urllib.request import Request
from urllib.request import urlopen


VIDEO_URL = 'https://www.youtube.com/watch?v={id}'
CHANNEL_URL = 'https://www.youtube.com/channel/{id}'
API_KEY = 'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8'


class SearchMode:
    videos = 'EgIQAQ%3D%3D'
    channels = 'EgIQAg%3D%3D'
    playlists = 'EgIQAw%3D%3D'
    livestreams = 'EgJAAQ%3D%3D'


class SearchCore:
    response: Any = None
    response_source: Any = None
    result_components: list[Any] = []

    def __init__(
        self, query: str,
        language: str, region: str,
        search_mode: str, timeout: int | None,
    ):
        self.query = query
        self.language = language
        self.region = region
        self.search_mode = search_mode
        self.timeout = timeout
        self.continuation_key: str | None = None

    def sync_create(self):
        self._make_request()
        self._parse_source()

    def result(self) -> dict[str, Any]:
        '''Returns the search result.'''
        return {'result': self.result_components}

    def _next(self) -> bool:
        if self.continuation_key:
            self.response = None
            self.response_source = None
            self.result_components: list[Any] = []
            self._make_request()
            self._parse_source()
            self._get_components()
            return True
        else:
            return False

    def _get_components(self) -> None:
        self.result_components = []
        for element in self.response_source:
            if 'videoRenderer' in element.keys():
                video = element['videoRenderer']
                self.result_components.append(self._get_video_component(video))

    def _make_request(self) -> None:
        request_body: dict[str, Any] = {
            'context': {
                'client': {
                    'clientName': 'WEB',
                    'clientVersion': '2.20210224.06.00',
                    'newVisitorCookie': True,
                },
                'user': {
                    'lockedSafetyMode': False,
                },
            },
        }
        request_body['query'] = self.query
        request_body['context']['client'].update({
            'hl': self.language,
            'gl': self.region,
        })
        if self.search_mode:
            request_body['params'] = self.search_mode
        if self.continuation_key:
            request_body['continuation'] = self.continuation_key
        request_body_bytes = json.dumps(request_body).encode('utf-8')
        request = Request(
            'https://www.youtube.com/youtubei/v1/search' + '?' + urlencode({
                'key': API_KEY,
            }),
            data=request_body_bytes,
            headers={
                'Content-Type': 'application/json; charset=utf-8',
                'Content-Length': str(len(request_body_bytes)),
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',  # noqa: E501
            },
        )
        try:
            self.response = urlopen(
                request, timeout=self.timeout,
            ).read().decode('utf_8')
        except Exception:
            raise Exception('ERROR: Could not make request.')

    def _parse_source(self) -> None:
        try:
            if not self.continuation_key:
                response_content = self._getValue(
                    json.loads(self.response), [
                        'contents', 'twoColumnSearchResultsRenderer',
                        'primaryContents', 'sectionListRenderer', 'contents',
                    ],
                )
            else:
                response_content = self._getValue(
                    json.loads(
                        self.response,
                    ), [
                        'onResponseReceivedCommands',
                        0, 'appendContinuationItemsAction',
                        'continuationItems',
                    ],
                )
            if response_content:
                for element in response_content:
                    if 'itemSectionRenderer' in element.keys():
                        self.response_source = self._getValue(
                            element, ['itemSectionRenderer', 'contents'],
                        )
                    if 'continuationItemRenderer' in element.keys():
                        self._get_continuation(element)
            else:
                self.response_source = self._getValue(
                    json.loads(
                        self.response,
                    ), [
                        'contents', 'twoColumnSearchResultsRenderer',
                        'primaryContents', 'richGridRenderer', 'contents',
                    ],
                )
                if self.response_source:
                    self._get_continuation(self.response_source[-1])
        except Exception:
            raise Exception('ERROR: Could not parse YouTube response.')

    def _get_continuation(self, element: dict[Any, Any]) -> None:
        temp = self._getValue(
            element, [
                'continuationItemRenderer',
                'continuationEndpoint', 'continuationCommand', 'token',
            ],
        )
        self.continuation_key = str(temp) if temp is not None else temp

    def _get_video_component(self, video: dict[Any, Any]) -> dict[Any, Any]:
        component: dict[Any, Any] = {
            'type': 'video',
            'id': self._getValue(video, ['videoId']),
            'title': self._getValue(video, ['title', 'runs', 0, 'text']),
            'publishedTime': self._getValue(
                video, [
                    'publishedTimeText', 'simpleText',
                ],
            ),
            'duration': self._getValue(video, ['lengthText', 'simpleText']),
            'viewCount': {
                'text': self._getValue(
                    video, [
                        'viewCountText', 'simpleText',
                    ],
                ),
                'short': self._getValue(
                    video, [
                        'shortViewCountText', 'simpleText',
                    ],
                ),
            },
            'thumbnails': self._getValue(video, ['thumbnail', 'thumbnails']),
            'richThumbnail': self._getValue(
                video, [
                    'richThumbnail', 'movingThumbnailRenderer',
                    'movingThumbnailDetails', 'thumbnails', 0,
                ],
            ),
            'descriptionSnippet': self._getValue(
                video, [
                    'detailedMetadataSnippets', 0, 'snippetText', 'runs',
                ],
            ),
            'channel': {
                'name': self._getValue(
                    video, [
                        'ownerText', 'runs', 0, 'text',
                    ],
                ),
                'id': self._getValue(
                    video, [
                        'ownerText', 'runs', 0, 'navigationEndpoint',
                        'browseEndpoint', 'browseId',
                    ],
                ),
                'thumbnails': self._getValue(
                    video, [
                        'channelThumbnailSupportedRenderers',
                        'channelThumbnailWithLinkRenderer',
                        'thumbnail', 'thumbnails',
                    ],
                ),
            },
        }
        component['link'] = VIDEO_URL.format(id=component['id'])
        component['channel']['link'] = CHANNEL_URL.format(
            id=component['channel']['id'],
        )
        return component

    def _getValue(
            self, source: dict[Any, Any], path: list[Any],
    ) -> Any | dict[Any, Any] | None:
        value = source

        for key in path:
            if type(key) is str:
                if key in value.keys():
                    value = value[key]
                else:
                    return None
            elif type(key) is int:
                if len(value) != 0:
                    value = value[key]
                else:
                    return None
        return value


class VideosSearch(SearchCore):
    def __init__(
        self, query: str,
        language: str = 'en', region: str = 'US',
        timeout: int | None = None,
    ):
        super().__init__(
            query,
            language, region,
            SearchMode.videos, timeout,
        )
        self.sync_create()
        self._get_components()

    def next(self) -> bool:
        return self._next()
