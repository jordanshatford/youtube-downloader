import argparse
import sys
from collections.abc import Sequence

from . import download
from . import search


def main(argv: Sequence[str] | None = None) -> int:
    argv = argv if argv is not None else sys.argv[1:]
    parser = argparse.ArgumentParser(
        'ydcli',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    subparsers = parser.add_subparsers(
        dest='command',
        required=True,
    )
    search_parser = subparsers.add_parser(
        search.COMMAND_NAME,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    search.add_argparse_arguments(search_parser)
    download_parser = subparsers.add_parser(
        download.COMMAND_NAME,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    download.add_argparse_arguments(download_parser)
    args = parser.parse_args(argv)

    if args.command == 'search':
        return search.run(args)
    elif args.command == 'download':
        return download.run(args)
    return 1


if __name__ == '__main__':
    raise SystemExit(main())
