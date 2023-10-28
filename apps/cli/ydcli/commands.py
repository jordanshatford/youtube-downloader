import os

import questionary
from ydcore import DownloadManager

from .prompts import prompt_for_download_options
from .prompts import prompt_for_video
from .utils import on_status_update
from .validation import validate_youtube_url


# Interactive search on CLI with various prompts for information
def interactive_search() -> None:
    video = prompt_for_video()
    print(video)


# Interactive download on CLI with various prompts for information
def interactive_download() -> None:
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
    manager = DownloadManager(output_dir, on_status_update)
    manager.add_using_url(url, options)
    manager.wait_for_all()
