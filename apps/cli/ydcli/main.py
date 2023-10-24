import argparse
import sys
from collections.abc import Sequence

from .utils import search_youtube


def main(argv: Sequence[str] | None = None) -> int:
    argv = argv if argv is not None else sys.argv[1:]
    parser = argparse.ArgumentParser(
        'ydcli', formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    subparsers = parser.add_subparsers(dest='command', required=True)
    search_parser = subparsers.add_parser('search')
    search_parser.add_argument('term')
    search_parser.add_argument(
        '--interactive', action=argparse.BooleanOptionalAction,
    )
    args = parser.parse_args(argv)
    if args.command == 'search':
        return search_youtube(args.term, args.interactive)
    return 1


if __name__ == '__main__':
    raise SystemExit(main())
