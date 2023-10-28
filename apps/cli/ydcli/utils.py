from ydcore import DownloadState
from ydcore import VideoWithOptionsAndStatus


def on_status_update(update: VideoWithOptionsAndStatus) -> None:
    state = update.status.state
    progress = update.status.progress
    postprocessor = update.status.postprocessor
    output: str = state.value
    if state == DownloadState.DOWNLOADING and progress is not None:
        output += f' - {progress:3.1f}%'
    elif state == DownloadState.PROCESSING and postprocessor is not None:
        output += f' - {postprocessor}'
    print('\033[K', end='\r')
    print(output, end='\n' if state == DownloadState.DONE else '\r')
