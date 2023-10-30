from .ytdlp import ProgressHookInfo


# Calculate progress based on progress hook from yt-dlp
def get_ytdlp_progress(info: ProgressHookInfo) -> float | None:
    downloaded_bytes = info.get('downloaded_bytes')
    total_bytes = info.get('total_bytes')
    # If total bytes not available, use estimate if provided
    if total_bytes is None:
        total_bytes = info.get('total_bytes_estimate')
    # Return None when calculation cannot be done properly
    if downloaded_bytes is None or total_bytes is None or total_bytes <= 0:
        return None
    return (downloaded_bytes / total_bytes) * 100
