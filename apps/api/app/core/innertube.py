import enum
import json
import logging
from collections.abc import MutableMapping
from typing import Any
from typing import Literal
from typing import TypedDict
from urllib import parse
from urllib.request import Request
from urllib.request import urlopen


logger = logging.getLogger('core')


_INNERTUBE_BASE_URL = 'https://www.youtube.com/youtubei/v1'


class InnerTubeClientType(enum.Enum):
    WEB = 'web'


class InnerTubeClientInfo(TypedDict):
    api_key: str
    context: dict[Literal['client'], dict[str, str]]
    headers: dict[str, str]


# List of innertube clients available for use. Only WEB is supported.
_INNERTUBE_CLIENTS: dict[InnerTubeClientType, InnerTubeClientInfo] = {
    InnerTubeClientType.WEB: {
        'api_key': 'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8',
        'context': {
            'client': {
                'clientName': 'WEB',
                'clientVersion': '2.20220801.00.00',
            },
        },
        'headers': {
            'User-Agent': 'Mozilla/5.0',
        },
    },
}


class InnerTubeClient:
    def __init__(
        self,
        type: InnerTubeClientType = InnerTubeClientType.WEB,
        *,
        language: str = 'en',
        region: str = 'US',
    ) -> None:
        client = _INNERTUBE_CLIENTS[type]
        self._api_key = client['api_key']
        self._client_context = client['context']['client']
        self._headers = client['headers']
        self._language = language
        self._region = region
        logger.debug(
            'Initialize InnerTubeClient with: ' +
            f'api_key={self._api_key}, context={self._client_context}, ' +
            f'headers={self._headers}, lang={self._language}, ' +
            f'region={self._region}.',
        )

    @property
    def _base_params(self) -> dict[str, Any]:
        return {
            'key': self._api_key,
            'contentCheckOk': True,
            'racyCheckOk': True,
        }

    @property
    def _base_data(self) -> dict[str, Any]:
        return {
            'context': {
                'client': {
                    **self._client_context,
                    'hl': self._language,
                    'gl': self._region,
                },

            },
        }

    @property
    def _base_headers(self) -> dict[str, str]:
        return {
            **self._headers,
        }

    def search(
        self, query: str, continuation: str | None = None,
    ) -> dict[str, Any]:
        logger.debug(
            'Attempting to search innertube API: ' +
            f'query={query}, continuation={continuation}.',
        )
        params: dict[str, Any] = {
            'query': query,
        }
        data: dict[str, Any] = {}
        if continuation:
            data.update({
                'continuation': continuation,
            })
        return self._call_innertube_api(
            '/search',
            data=data,
            params=params,
        )

    def _call_innertube_api(
        self,
        endpoint: str,
        *,
        data: MutableMapping[str, Any] = {},
        params: MutableMapping[str, Any] = {},
        headers: MutableMapping[str, str] = {},
        timeout: float | None = None,
    ) -> Any:
        url = f'{_INNERTUBE_BASE_URL}{endpoint}'
        data.update(self._base_data)
        data_bytes = json.dumps(data).encode('utf-8')
        request = Request(
            f'{url}?{parse.urlencode(params)}',
            data=data_bytes,
            headers={
                **self._base_headers,
                **headers,
                'Content-Type': 'application/json; charset=utf-8',
                'Content-Length': str(len(data_bytes)),
            },
        )
        logger.debug(
            f'Calling innertube API with: url={url}, ' +
            f'data={request.data}, headers={request.headers}.',
        )
        response = urlopen(request, timeout=timeout)
        response_data = json.loads(response.read().decode('utf-8'))
        logger.debug(f'Innertube API responded to: url={url}.')
        return response_data
