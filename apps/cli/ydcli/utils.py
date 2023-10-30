from ydcore import Download
from ydcore import DownloadState


POSTPROCESSOR_LOOKUP = {
    'extractaudio': 'EXTRACTING AUDIO',
    'videoconvertor': 'CONVERTING VIDEO',
    'metadata': 'EMBEDDING',
    'embedthumbnail': 'EMBEDDING',
    'embedsubtitle': 'EMBEDDING',
    'movefiles': 'FINALIZING',
}


def on_status_update(update: Download) -> None:
    state = update.status.state
    progress = update.status.progress
    postprocessor = update.status.postprocessor
    output: str = state.value
    if state == DownloadState.DOWNLOADING and progress is not None:
        output += f' - {progress:3.1f}%'
    elif state == DownloadState.PROCESSING and postprocessor is not None:
        postprocessor_text = POSTPROCESSOR_LOOKUP.get(
            postprocessor.lower(),
        )
        if postprocessor_text is not None:
            output += f' - {postprocessor_text}'
    print('\033[K', end='\r')
    print(output, end='\n' if state == DownloadState.DONE else '\r')
