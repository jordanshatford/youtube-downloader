import os

import questionary
from ydcore import DownloadManager

from .prompts import prompt_for_download_options
from .validation import validate_youtube_url


# Run the download for a video
def run() -> None:
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
