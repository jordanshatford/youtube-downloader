import os

from .threads import YoutubeDownloadThread

DEFAULT_OUTPUT_DIR = os.getcwd() + "/sessions"

class AudioDownloadManager:
    def __init__(self, id: str, announcer: callable):
        self._id = id
        self._announcer = announcer
        self._downloads = {}
        self._download_dir = DEFAULT_OUTPUT_DIR + "/" + id

    def add(self, video_id: str, url: str) -> None:
        if video_id not in self._downloads:
            download = YoutubeDownloadThread(video_id, url, self._download_dir, self.send_status_update)
            self._downloads[video_id] = download
            download.start()

    def remove(self, video_id: str) -> None:
        self._downloads[video_id].remove()
        self._downloads.pop(video_id, None)

    def get_download(self, video_id: str) -> str:
        path = self._downloads[video_id].get_file_location() # TODO: prevent errors here
        return path

    def get_all_downloads(self) -> str:
        # TODO: zip downloads and return zip file path
        print("Error: Not implemented yet!")

    def send_status_update(self, video_id: str, status: str) -> None:
        self._announcer(status, video_id)
