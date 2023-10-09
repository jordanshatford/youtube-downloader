from typing import Any, Sequence


class YoutubeDL:
    def __init__(self, params: dict[Any, Any] | None = None, auto_init: bool = True) -> None: ...
    def download(self, videos: Sequence[str]) -> None: ...