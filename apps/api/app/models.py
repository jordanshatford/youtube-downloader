import enum

from pydantic import BaseModel
from pydantic import HttpUrl


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


class DownloadState(str, enum.Enum):
    WAITING = 'WAITING'
    DOWNLOADING = 'DOWNLOADING'
    PROCESSING = 'PROCESSING'
    DONE = 'DONE'
    ERROR = 'ERROR'


class DownloadStatus(BaseModel):
    state: DownloadState
    # Progress in percent (Only valid when state is DOWNLOADING)
    progress: float | None = None
    # ETA in seconds (Only valid when state is DOWNLOADING)
    eta: int | None = None
    # Postprocessor currently running (Only valid when state is PROCESSING)
    postprocessor: str | None = None


class DownloadType(str, enum.Enum):
    AUDIO = 'audio'
    VIDEO = 'video'


class AudioFormat(str, enum.Enum):
    MP3 = 'mp3'
    AAC = 'aac'
    FLAC = 'flac'
    M4A = 'm4a'
    OPUS = 'opus'
    WAV = 'wav'


class VideoFormat(str, enum.Enum):
    AVI = 'avi'
    FLV = 'flv'
    MKV = 'mkv'
    MOV = 'mov'
    MP4 = 'mp4'
    WEBM = 'webm'


class DownloadQuality(str, enum.Enum):
    BEST = 'best'
    WORST = 'worst'


class AvailableDownloadOptions(BaseModel):
    type: list[DownloadType]
    format: list[AudioFormat | VideoFormat]
    quality: list[DownloadQuality]
    embed_metadata: list[bool]


class DownloadOptions(BaseModel):
    type: DownloadType
    format: AudioFormat | VideoFormat
    quality: DownloadQuality
    embed_metadata: bool


class VideoWithOptions(Video):
    options: DownloadOptions


class VideoWithOptionsAndStatus(VideoWithOptions):
    status: DownloadStatus


class Session(BaseModel):
    id: str
