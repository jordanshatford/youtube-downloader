import enum

from typing import Optional


# NOTE: this needs to be synced with the client enum
class Status(str, enum.Enum):
    WAITING = "WAITING"
    DOWNLOADING = "DOWNLOADING"
    PROCESSING = "PROCESSING"
    DONE = "DONE"
    ERROR = "ERROR"
    UNDEFINED = "UNDEFINED"


def format_status_update(video_id: str, status: Status) -> dict:
    return {"id": video_id, "status": status.value}


def format_response_message(
    message: Optional[str] = None,
    detail: Optional[str] = None,
) -> dict:
    response = {}
    if message is not None:
        response["message"] = message
    if detail is not None:
        response["detail"] = detail
    return response
