import logging
import os

import questionary

from .prompts import prompt_for_video_and_download


logging.basicConfig(
    format='%(levelname)s: %(message)s',
    level=logging.INFO,
)


def main() -> int:
    try:
        # Get directory to output downloaded files to
        path = questionary.path(
            'Directory to store downloads:',
            only_directories=True,
            default='./downloads',
        ).unsafe_ask()
        output_dir = os.path.abspath(path)
        questionary.print(f'Downloading files to: {output_dir}')
        return prompt_for_video_and_download(output_dir)
    except KeyboardInterrupt:
        questionary.print('\nCancelled by user\n')
        return 0
    except Exception as e:
        questionary.print(f'\nError: {e}')
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
