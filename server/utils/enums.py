import enum

# NOTE: this needs to be synced with the client enum
class Status(str, enum.Enum):
    WAITING = "WAITING"
    DOWNLOADING = "DOWNLOADING"
    PROCESSING = "PROCESSING"
    DONE = "DONE"
    UNDEFINED = "UNDEFINED"