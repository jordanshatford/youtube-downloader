import os

import questionary
from questionary import Choice
from ydcore import AudioFormat
from ydcore import DownloadManager
from ydcore import DownloadOptions
from ydcore import DownloadQuality
from ydcore import VideoFormat

from .utils import validate_youtube_url


def prompt_for_download_options() -> DownloadOptions:
    fmt = questionary.select(
        'Format:',
        [
            *[Choice(f.name, f) for f in AudioFormat],
            *[Choice(f.name, f) for f in VideoFormat],
        ],
        default=VideoFormat.MP4,
    ).ask()
    quality = questionary.select(
        'Quality:',
        [Choice(q.name, q) for q in DownloadQuality],
        default=DownloadQuality.BEST,
    ).ask()
    embedding = questionary.checkbox(
        'Embed:',
        [
            Choice('Metadata', checked=True),
            Choice('Thumbnail'),
            Choice('Subtitles'),
        ],
    ).ask()
    return DownloadOptions(
        format=fmt,
        quality=quality,
        embed_metadata='Metadata' in embedding,
        embed_thumbnail='Thumbnail' in embedding,
        embed_subtitles='Subtitles' in embedding,
    )


# Run the download for a video
def run() -> int:
    url = questionary.text(
        message='Video URL:', validate=validate_youtube_url,
    ).ask()
    options = prompt_for_download_options()
    # Download and wait for video
    output_dir = os.path.join(os.getcwd(), '__downloads__')
    manager = DownloadManager(output_dir)
    manager.add_using_url(url, options)
    manager.wait_for_all()
    return 0
