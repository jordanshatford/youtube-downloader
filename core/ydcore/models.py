import enum

from pydantic import BaseModel
from pydantic import HttpUrl


class Channel(BaseModel):
    name: str
    url: HttpUrl
    thumbnail: HttpUrl

    def __str__(self):
        return self.name


class Video(BaseModel):
    id: str
    url: HttpUrl
    title: str
    duration: str
    thumbnail: HttpUrl
    channel: Channel

    def __str__(self):
        return f'{self.title} - {str(self.channel)}'


class DownloadState(str, enum.Enum):
    WAITING = 'WAITING'
    DOWNLOADING = 'DOWNLOADING'
    PROCESSING = 'PROCESSING'
    DONE = 'DONE'
    ERROR = 'ERROR'


class DownloadStatus(BaseModel):
    state: DownloadState
    # The following are only valid when the state is DOWNLOADING
    downloaded_bytes: int | None = None  # Bytes downloaded
    total_bytes: int | None = None       # Bytes total (or estimate)
    progress: float | None = None        # Progress in percent
    elapsed: float | None = None         # Time elapsed in seconds
    eta: float | None = None             # ETA in seconds
    speed: float | None = None           # Speed of download (bytes/second)
    # The following are only valid when the state is PROCESSING
    postprocessor: str | None = None     # Postprocessor currently running


class AudioFormat(str, enum.Enum):
    AAC = 'aac'
    FLAC = 'flac'
    M4A = 'm4a'
    MP3 = 'mp3'
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
    format: list[AudioFormat | VideoFormat]
    quality: list[DownloadQuality]
    embed_metadata: list[bool]
    embed_thumbnail: list[bool]
    embed_subtitles: list[bool]


class DownloadOptions(BaseModel):
    format: AudioFormat | VideoFormat
    quality: DownloadQuality
    embed_metadata: bool
    embed_thumbnail: bool
    embed_subtitles: bool


class DownloadInput(BaseModel):
    video: Video
    options: DownloadOptions


class Download(DownloadInput):
    status: DownloadStatus


class DownloadFile(BaseModel):
    name: str
    path: str
