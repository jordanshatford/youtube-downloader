import queue

from typing import Optional


class ServerSentEvent:
    def __init__(
        self,
        data: str,
        *,
        event: Optional[str] = None,
        id: Optional[int] = None,
        retry: Optional[int] = None,
    ) -> None:
        self._data = data
        self._event = event
        self._id = id
        self._retry = retry

    def encode(self) -> bytes:
        message = f"data: {self._data}"
        if self._event is not None:
            message = f"{message}\nevent: {self._event}"
        if self._id is not None:
            message = f"{message}\nid: {self._id}"
        if self._retry is not None:
            message = f"{message}\nretry: {self._retry}"
        message = f"{message}\r\n\r\n"
        return message.encode("utf-8")
