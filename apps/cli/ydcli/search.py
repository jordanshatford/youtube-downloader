import questionary
from ydcore import YouTubeSearch

from .utils import print_videos
from .utils import validate_value_entered


# Run search functionality. User will input term to search for.
def run() -> int:
    term = questionary.text(
        message='Search term:', validate=validate_value_entered,
    ).ask()
    search = YouTubeSearch(term)
    videos = search.results
    # If no search results found exit with error code 1.
    if len(videos) == 0:
        print('No search results found.')
        return 1
    # Print list of videos to the user
    print_videos(videos)
    return 0
