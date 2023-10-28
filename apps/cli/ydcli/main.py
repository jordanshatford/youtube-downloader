import questionary

from . import download
from . import search


def main() -> int:
    try:
        command = questionary.select(
            'What do you want to do?',
            ['Download', 'Search'],
            default='Download',
        ).unsafe_ask()
        if command == 'Search':
            return search.run()
        elif command == 'Download':
            return download.run()
    except KeyboardInterrupt:
        questionary.print('\nCancelled by user\n')
        return 1
    return 1


if __name__ == '__main__':
    raise SystemExit(main())
