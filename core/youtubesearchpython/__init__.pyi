from typing import Any






class __ResultMode:
    json = 0
    dict = 1

class VideosSearch:
    def __init__(self, term: str, limit: int = 20, language: str = 'en', region: str = 'US', timeout: int | None = None) -> None: ...
    def result(self, mode: int = __ResultMode.dict) -> dict[Any, Any]: ...
