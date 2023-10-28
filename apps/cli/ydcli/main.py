import questionary

from . import download
from . import search


def main() -> int:
    command = questionary.select(
        'What do you want to do?',
        ['Search', 'Download'],
        default='Download',
    ).ask()

    if command == 'Search':
        return search.run()
    elif command == 'Download':
        return download.run()
    return 1


if __name__ == '__main__':
    raise SystemExit(main())
