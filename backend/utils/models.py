import enum
from typing import Optional

from pydantic import BaseModel


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
    url: Optional[str] = None
    thumbnail: Optional[str] = None


class Video(BaseModel):
    id: str
    url: str
    options: Optional[AudioOptions] = None
    title: Optional[str] = None
    duration: Optional[str] = None
    thumbnail: Optional[str] = None
    channel: Optional[Channel] = None


class Session(BaseModel):
    id: str


class Message(BaseModel):
    title: str
    message: str


class StatusUpdate(BaseModel):
    id: str
    status: Status
