import enum
import logging

from pydantic import BaseModel
from pydantic import HttpUrl
from pydantic import computed_field

logger = logging.getLogger("core")


class Channel(BaseModel):
    name: str
    url: HttpUrl | None

    def __str__(self) -> str:
        return self.name


class Video(BaseModel):
    id: str
    url: HttpUrl
    title: str
    duration: str
    thumbnail: HttpUrl
    channel: Channel

    def __str__(self) -> str:
        return f"{self.title} - {self.channel}"


class DownloadState(enum.StrEnum):
    WAITING = "WAITING"
    DOWNLOADING = "DOWNLOADING"
    PROCESSING = "PROCESSING"
    DONE = "DONE"
    ERROR = "ERROR"


class DownloadStatus(BaseModel):
    # Current state of the download. This should always be checked to determine
    # if other fields in this status are relevant.
    state: DownloadState

    # The following fields are only valid when the state is downloading.
    #   downloaded_bytes: the amount of bytes downloaded.
    #   total_bytes: the amount of total bytes (potentially estimated).
    #   elapsed: time elapsed in seconds.
    #   eta: time to complete in seconds.
    #   speed: speed of the download in bytes per second.
    #   progress: computed progress of the download as a percentage.
    downloaded_bytes: float | None = None
    total_bytes: float | None = None
    elapsed: float | None = None
    eta: float | None = None
    speed: float | None = None

    @computed_field
    def progress(self) -> float | None:
        if self.state is not DownloadState.DOWNLOADING:
            return None
        if self.downloaded_bytes is None or self.total_bytes is None:
            logger.debug(
                "Could not calculate progress, downloaded_bytes or total_bytes is None."
            )
            return None
        if self.total_bytes <= 0:
            logger.debug("Could not calculate progress, total_bytes <= 0.")
            return None
        return (self.downloaded_bytes / self.total_bytes) * 100

    # The following field is only valid when the state is processing.
    #   postprocessor: the name of the post processor currently running.
    postprocessor: str | None = None


class AudioFormat(enum.StrEnum):
    AAC = "aac"
    FLAC = "flac"
    M4A = "m4a"
    MP3 = "mp3"
    OPUS = "opus"
    WAV = "wav"


class VideoFormat(enum.StrEnum):
    AVI = "avi"
    FLV = "flv"
    MKV = "mkv"
    MOV = "mov"
    MP4 = "mp4"
    WEBM = "webm"


class DownloadQuality(enum.StrEnum):
    BEST = "best"
    WORST = "worst"


class AvailableDownloadOptions(BaseModel):
    format: list[AudioFormat | VideoFormat] = list(AudioFormat) + list(VideoFormat)
    quality: list[DownloadQuality] = list(DownloadQuality)
    embed_metadata: list[bool] = [True, False]
    embed_thumbnail: list[bool] = [True, False]
    embed_subtitles: list[bool] = [True, False]


class DownloadOptions(BaseModel):
    format: AudioFormat | VideoFormat = VideoFormat.MP4
    quality: DownloadQuality = DownloadQuality.BEST
    embed_metadata: bool = True
    embed_thumbnail: bool = False
    embed_subtitles: bool = False


class DownloadInput(BaseModel):
    video: Video
    options: DownloadOptions


class Download(DownloadInput):
    status: DownloadStatus
