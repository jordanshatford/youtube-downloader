import re

from ydcore import Video


# Validate that a user has actually entered a value
def validate_value_entered(value: str) -> str | bool:
    return True if len(value) > 0 else 'Please enter a value.'


# Validate that user entered a youtube url
def validate_youtube_url(value: str) -> str | bool:
    regex = (
        r'(https?://)?(www\.)?'
        r'(youtube|youtu|youtube-nocookie)\.(com|be)/'
        r'(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})'
    )
    match = re.match(regex, value)
    return True if bool(match) else 'Please enter a valid YouTube URL.'


# Print list of videos to the console
def print_videos(videos: list[Video]) -> None:
    for index, video in enumerate(videos, start=1):
        print(f'{index}. {video.url} - {video.title}')
