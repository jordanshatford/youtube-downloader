import argparse

from ydcore import YouTubeSearch

from .utils import print_videos

COMMAND_NAME = 'search'


# Add options relevant for searching for videos
def add_argparse_arguments(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        'term',
        help='search YouTube for videos with the provided term.',
    )
    parser.add_argument(
        '--interactive',
        action='store_true',
        help='run shell for additional results for the search.',
    )


# Run seach for a term. If iterative, the user can get more results
def run(args: argparse.Namespace) -> int:
    term = args.term
    interactive = args.interactive
    search = YouTubeSearch(term)
    videos = search.results
    # If no search results found exit with error code 1.
    if len(videos) == 0:
        print('No search results found.')
        return 1
    # Print list of videos to the user
    next_index = print_videos(videos)
    # In interactive mode continue getting results until user quits
    if interactive:
        quit = input(': ')
        while quit.lower() not in ['q', 'quit', 'exit']:
            has_more = search.next()
            if not has_more:
                print('No more search results found.')
                return 0
            else:
                videos = search.results
                next_index = print_videos(videos, next_index)
            quit = input(': ')
    return 0
