import os
from typing import Callable

from yt_dlp.postprocessor import PostProcessor

from ..models import Status


class FileProcessingComplete(PostProcessor):
    def __init__(
        self, status_update: Callable[[Status], None], downloader=None,  # noqa: E501
    ):
        self._status_update = status_update
        super().__init__(downloader=downloader)

    def run(self, information: dict[str, str]):
        filepath = information['filepath']
        if os.path.exists(filepath):
            self._status_update(Status.DONE)
        return [], information
