import os

import questionary
from questionary import Choice
from ydcore import DownloadManager
from ydcore import YouTubeSearch

from .prompts import prompt_for_download_options
from .utils import on_status_update
from .validation import validate_youtube_url


# Interactive search on CLI with various prompts for information
def interactive_search() -> None:
    term = questionary.text(
        message='Search term:', validate=validate_value_entered,
    ).unsafe_ask()
    search = YouTubeSearch(term)
    videos = search.results
    # If no search results found, print that info and ask for another term.
    if len(videos) == 0:
        questionary.print('No search results found.')
        return interactive_search()
    video = questionary.select(
        'Select a video:',
        [
            Choice(
                str(video),
                video,
            ) for video in videos
        ],
    ).unsafe_ask()
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
