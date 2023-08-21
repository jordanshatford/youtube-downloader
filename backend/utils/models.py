import enum
from typing import Optional

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
    url: Optional[HttpUrl] = None
    thumbnail: Optional[HttpUrl] = None


class Video(BaseModel):
    id: str
    url: HttpUrl
    options: AudioOptions = AudioOptions(format=AudioFormat.MP3)
    title: Optional[str] = None
    duration: Optional[str] = None
    thumbnail: Optional[HttpUrl] = None
    channel: Optional[Channel] = None


class Session(BaseModel):
    id: str


class StatusUpdate(BaseModel):
    id: str
    status: Status
