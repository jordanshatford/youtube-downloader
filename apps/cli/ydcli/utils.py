import questionary

from ydcore import DownloadState
from ydcore import VideoWithOptionsAndStatus


def on_status_update(update: VideoWithOptionsAndStatus) -> None:
    state = update.status.state
    if state in [DownloadState.WAITING, DownloadState.ERROR, DownloadState.DONE]:
        questionary.print(state)
    elif state == DownloadState.DOWNLOADING:
        progress = update.status.progress
        questionary.print(f'{state} - {progress}%' if progress else state)
    elif state == DownloadState.PROCESSING:
        postprocessor = update.status.postprocessor
        questionary.print(
            f'{state} - {postprocessor}%' if postprocessor else state
        )
