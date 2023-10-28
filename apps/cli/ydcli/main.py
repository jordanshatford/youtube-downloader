import os

import questionary
from ydcore import DownloadManager
from ydcore import VideoWithOptions

from .prompts import prompt_for_download_options
from .prompts import prompt_for_video
from .utils import on_status_update


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
        # Get a video based on user input
        video = prompt_for_video()
        # Get options for downloading the video
        options = prompt_for_download_options()
        # Download and wait for video to finish
        manager = DownloadManager(output_dir, on_status_update)
        manager.add(
            VideoWithOptions(
                **video.model_dump(),
                options=options,
            ),
        )
        manager.wait_for_all()
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
