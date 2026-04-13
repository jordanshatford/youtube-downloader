import datetime
from collections.abc import Sequence

from pydantic import HttpUrl

from .models import Channel
from .models import Video
from .ytdlp import Thumbnail
from .ytdlp import VideoInfo

FALLBACK = HttpUrl("https://www.youtube.com/")


# Parse yt-dlp VideoInfo dict into our pydantic Video.
def parse_video_info_to_video(entry: VideoInfo | None) -> Video | None:
    try:
        if entry is None:
            return None

        title = entry.get("title")
        url = entry.get("url")
        duration = entry.get("duration")
        duration_str = (
            f"{datetime.timedelta(seconds=duration)}" if duration is not None else "???"
        )
        thumbnails = entry.get("thumbnails")
        return Video(
            id=entry["id"],
            title=title if title is not None else "Unknown",
            url=HttpUrl(url) if url is not None else FALLBACK,
            duration=duration_str,
            thumbnail=parse_best_thumbnail_url(thumbnails),
            channel=parse_video_info_to_channel(entry),
        )
    except KeyError:
        return None


# Parse yt-dlp VideoInfo dict into our pydantic Channel.
def parse_video_info_to_channel(entry: VideoInfo) -> Channel:
    # Attempt to read the channel name and url using the channel entries.
    # If for some reason that failed, use the uploader entries. Either way
    # fallback to unknown values as channel information is not as important.
    name = entry.get("channel", entry.get("uploader"))
    url = entry.get("channel_url", entry.get("uploader_url"))
    return Channel(
        name=name if name is not None else "Unknown",
        url=HttpUrl(url) if url is not None else url,
    )


# Parse the best thumbnail URL out of a yt-dlp list of thumbnails.
def parse_best_thumbnail_url(thumbnails: Sequence[Thumbnail] | None) -> HttpUrl:
    if thumbnails is None:
        return FALLBACK

    # Get the best thumbnail out of available options. This returns the last
    # thumbnail in the list as they are sorted as such. As an improvement we
    # should check for the thumbnail with the best resolution.
    thumbnail = thumbnails[-1]
    if thumbnail is None:
        return FALLBACK

    url = thumbnail.get("url")
    return HttpUrl(url) if url is not None else FALLBACK
