import os
from typing import Callable

from youtube_dl.postprocessor.common import PostProcessor

from .helpers import Status


class FileProcessingComplete(PostProcessor):
    def __init__(
        self, id: str, status_update: Callable[[str, Status], None], downloader=None
    ):
        self._id = id
        self._status_update = status_update
        super(FileProcessingComplete, self).__init__(downloader=downloader)

    def run(self, information: dict):
        filepath = information["filepath"]
        if os.path.exists(filepath):
            self._status_update(self._id, Status.DONE)
        return [], information
