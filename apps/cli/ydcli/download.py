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


# Run the download for a video
def run() -> int:
    path = questionary.path(
        'Directory to store downloads:',
        only_directories=True,
        default='./downloads',
    ).unsafe_ask()
    output_dir = os.path.abspath(path)
    questionary.print(f'Downloading files to: {output_dir}')
    url = questionary.text(
        message='Video URL:', validate=validate_youtube_url,
    ).unsafe_ask()
    options = prompt_for_download_options()
    # Download and wait for video
    manager = DownloadManager(output_dir)
    manager.add_using_url(url, options)
    manager.wait_for_all()
    return 0
