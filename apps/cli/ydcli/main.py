import questionary

from . import download
from . import search


def main() -> int:
    try:
        # Run comamnd based on user input
        command = questionary.select(
            'What do you want to do?',
            ['Download', 'Search'],
            default='Download',
        ).unsafe_ask()
        if command == 'Search':
            search.run()
        elif command == 'Download':
            download.run()
        # Exit successful if an error has not occurred
        return 0
    except KeyboardInterrupt:
        questionary.print('\nCancelled by user\n')
        return 0
    except Exception as e:
        questionary.print(f'\nError: {e}')
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
