import datetime
from collections.abc import Sequence

from pydantic import HttpUrl

from .models import Channel
from .models import Video
from .ytdlp import Thumbnail
from .ytdlp import VideoInfo


# Parse yt-dlp VideoInfo dict into our pydantic Video.
def parse_video_info_to_video(entry: VideoInfo) -> Video:
    title = entry["title"]
    url = entry["url"]
    duration = entry["duration"]
    duration_str = (
        f"{datetime.timedelta(seconds=duration)}" if duration is not None else "???"
    )
    return Video(
        id=entry["id"],
        title=title if title is not None else "Unknown",
        url=HttpUrl(url) if url is not None else HttpUrl("https://www.youtube.com/"),
        duration=duration_str,
        thumbnail=parse_best_thumbnail_url(entry["thumbnails"]),
        channel=parse_video_info_to_channel(entry),
    )


# Parse yt-dlp VideoInfo dict into our pydantic Channel.
def parse_video_info_to_channel(entry: VideoInfo) -> Channel:
    # Attempt to read the channel name and url using the channel entries.
    # If for some reason that failed, use the uploader entries. Either way
    # fallback to unknown values as channel information is not as important.
    name = entry["channel"] or entry["uploader"]
    url = entry["channel_url"] or entry["uploader_url"]
    return Channel(
        name=name if name is not None else "Unknown",
        url=HttpUrl(url) if url is not None else url,
    )


# Parse the best thumbnail URL out of a yt-dlp list of thumbnails.
def parse_best_thumbnail_url(thumbnails: Sequence[Thumbnail] | None) -> HttpUrl:
    fallback = HttpUrl("https://www.youtube.com/")
    if thumbnails is None:
        return fallback

    # Get the best thumbnail out of available options. This returns the last
    # thumbnail in the list as they are sorted as such. As an improvement we
    # should check for the thumbnail with the best resolution.
    thumbnail = thumbnails[-1]
    if thumbnail is None:
        return fallback

    url = thumbnail["url"]
    return HttpUrl(url) if url is not None else fallback
