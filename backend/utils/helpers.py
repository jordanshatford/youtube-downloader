import enum


# NOTE: this needs to be synced with the frontend enum
class Status(str, enum.Enum):
    WAITING = "WAITING"
    DOWNLOADING = "DOWNLOADING"
    PROCESSING = "PROCESSING"
    DONE = "DONE"
    ERROR = "ERROR"
    UNDEFINED = "UNDEFINED"


def format_status_update(video_id: str, status: Status) -> dict:
    return {"id": video_id, "status": status.value}
