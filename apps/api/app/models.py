import enum

from pydantic import BaseModel
from pydantic import HttpUrl


class DownloadState(str, enum.Enum):
    WAITING = 'WAITING'
    DOWNLOADING = 'DOWNLOADING'
    PROCESSING = 'PROCESSING'
    DONE = 'DONE'
    ERROR = 'ERROR'
    UNDEFINED = 'UNDEFINED'


class DownloadStatus(BaseModel):
    state: DownloadState


class DownloadStatusUpdate(DownloadStatus):
    id: str


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
    url: HttpUrl
    thumbnail: HttpUrl


class Video(BaseModel):
    id: str
    url: HttpUrl
    title: str
    duration: str
    thumbnail: HttpUrl
    channel: Channel


class VideoWithOptions(Video):
    options: AudioOptions


class Session(BaseModel):
    id: str
