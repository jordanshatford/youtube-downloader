import questionary
from questionary import Choice
from ydcore import AudioFormat
from ydcore import DownloadOptions
from ydcore import DownloadQuality
from ydcore import Video
from ydcore import VideoFormat
from ydcore import YouTubeSearch

from .validation import validate_value_entered


def prompt_for_video() -> Video:
    query = questionary.text(
        message='Search term or URL:', validate=validate_value_entered,
    ).unsafe_ask()
    search = YouTubeSearch(query)
    videos = search.results
    # If no search results found, print that info and ask for another term.
    if len(videos) == 0:
        questionary.print('No search results found.')
        return prompt_for_video()
    video = questionary.select(
        'Select a video:',
        [
            Choice(
                str(video),
                video,
            ) for video in videos
        ],
    ).unsafe_ask()
    return video


def prompt_for_download_options() -> DownloadOptions:
    fmt = questionary.select(
        'Format:',
        [
            *[Choice(f.name, f) for f in AudioFormat],
            *[Choice(f.name, f) for f in VideoFormat],
        ],
        default=VideoFormat.MP4,
    ).unsafe_ask()
    quality = questionary.select(
        'Quality:',
        [Choice(q.name, q) for q in DownloadQuality],
        default=DownloadQuality.BEST,
    ).unsafe_ask()
    embedding = questionary.checkbox(
        'Embed:',
        [
            Choice('Metadata', checked=True),
            Choice('Thumbnail'),
            Choice('Subtitles'),
        ],
    ).unsafe_ask()
    return DownloadOptions(
        format=fmt,
        quality=quality,
        embed_metadata='Metadata' in embedding,
        embed_thumbnail='Thumbnail' in embedding,
        embed_subtitles='Subtitles' in embedding,
    )
