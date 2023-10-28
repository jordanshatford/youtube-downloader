import questionary
from questionary import Choice
from ydcore import YouTubeSearch

from .validation import validate_value_entered


# Run search functionality. User will input term to search for.
def run() -> None:
    term = questionary.text(
        message='Search term:', validate=validate_value_entered,
    ).unsafe_ask()
    search = YouTubeSearch(term)
    videos = search.results
    # If no search results found, print that info and ask for another term.
    if len(videos) == 0:
        questionary.print('No search results found.')
        return run()
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
