import enum

from pydantic import BaseModel
from pydantic import HttpUrl


# NOTE: this needs to be synced with the frontend enum
class Status(str, enum.Enum):
    WAITING = 'WAITING'
    DOWNLOADING = 'DOWNLOADING'
    PROCESSING = 'PROCESSING'
    DONE = 'DONE'
    ERROR = 'ERROR'
    UNDEFINED = 'UNDEFINED'


class AudioFormat(str, enum.Enum):
    MP3 = 'mp3'
    AAC = 'aac'
    FLAC = 'flac'
    M4A = 'm4a'
    OPUS = 'opus'
    WAV = 'wav'


class AudioOptions(BaseModel):
    format: AudioFormat


class Channel(BaseModel):
    name: str
    url: HttpUrl | None = None
    thumbnail: HttpUrl | None = None


class Video(BaseModel):
    id: str
    url: HttpUrl
    options: AudioOptions = AudioOptions(format=AudioFormat.MP3)
    title: str | None = None
    duration: str | None = None
    thumbnail: HttpUrl | None = None
    channel: Channel | None = None


class Session(BaseModel):
    id: str


class StatusUpdate(BaseModel):
    id: str
    status: Status
