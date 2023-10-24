from ydcore import Video
from ydcore import YouTubeSearch


# Print videos list to console. Start is the number to prepend on the first
# video. This function returns the next number in the sequence for future use.
def print_videos_list(videos: list[Video], start: int = 1) -> int:
    for index, video in enumerate(videos, start=start):
        print(f'{index}. {video.url} - {video.title}')
    return start + len(videos)


# Command that will quit out of interactive CLI shell.
QUIT_COMMANDS = ['q', 'quit', 'exit']


# Search youtube based on term. In interactive mode the user will have the
# ability to continuing getting the next continuation of results rather than
# just seeing the first set of results.
def search_youtube(term: str, interactive: bool) -> int:
    youtube_search = YouTubeSearch(term)
    videos = youtube_search.results
    # If no search results found exit with error code 1.
    if len(videos) == 0:
        print('No search results found.')
        return 1
    # Print list of videos to the user
    next_index = print_videos_list(videos)
    # In interactive mode continue getting results until user quits
    if interactive:
        quit = input(': ')
        while quit.lower() not in QUIT_COMMANDS:
            has_more = youtube_search.next()
            if not has_more:
                print('No more search results found.')
                return 0
            else:
                videos = youtube_search.results
                next_index = print_videos_list(videos, next_index)
            quit = input(': ')
    return 0
