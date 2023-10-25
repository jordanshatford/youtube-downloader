from ydcore import Video
from ydcore import YouTubeSearch


# Take YouTube URL and return a Video with details if exists.
def to_video(url: str) -> Video | None:
    results = YouTubeSearch(url).results
    return results[0] if len(results) > 0 else None


# Print videos list to console. Start is the number to prepend on the first
# video. This function returns the next number in the sequence for future use.
def print_videos(videos: list[Video], start: int = 1) -> int:
    for index, video in enumerate(videos, start=start):
        print(f'{index}. {video.url} - {video.title}')
    return start + len(videos)
