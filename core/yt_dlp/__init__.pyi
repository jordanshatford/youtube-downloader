from typing import Sequence

from ydcore.config.ytdlp import YoutubeDLParams


class YoutubeDL:
    def __init__(self, params: YoutubeDLParams | None = None, auto_init: bool = True) -> None: ...
    def download(self, videos: Sequence[str]) -> None: ...


__all__ = ['YoutubeDL']
