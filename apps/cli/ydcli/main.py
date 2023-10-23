import sys
from collections.abc import Sequence


def main(argv: Sequence[str] | None = None) -> int:
    argv = argv if argv is not None else sys.argv[1:]
    print('NOT IMPLEMENTED')
    return 1


if __name__ == '__main__':
    raise SystemExit(main())
