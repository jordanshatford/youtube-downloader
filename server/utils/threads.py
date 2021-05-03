import os
import threading
import time

from youtube_dl import YoutubeDL

from .enums import Status
from .processors import FileProcessingComplete

class YoutubeDownloadThread(threading.Thread):
    def __init__(self, id: str, url: str, output_directory: str, status_update: callable):
        self._id = id
        self._url = url
        self._output_directory = output_directory
        self._status_update = status_update

        YOUTUBE_DL_OPTIONS = {
            "format": "bestaudio/best",
            "progress_hooks": [self.download_progress_hook],
            "outtmpl": f"{self._output_directory}/{self._id}.%(ext)s",
            "quiet": True,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
        }
        self._downloader = YoutubeDL(YOUTUBE_DL_OPTIONS)
        self._downloader.add_post_processor(FileProcessingComplete(self._id, self._status_update, downloader=self._downloader))

        super(YoutubeDownloadThread, self).__init__(group=None, target=None, name=None)

    def download_progress_hook(self, progress_info: dict) -> None:
        if progress_info.get("status", None) == "finished":
            self._status_update(self._id, Status.PROCESSING)

    def get_file_location(self) -> str:
        path = os.path.join(self._output_directory, f"{self._id}.mp3")
        return path

    def remove(self) -> bool:
        path = self.get_file_location()
        if os.path.exists(path):
            os.remove(path)
            return True
        return False

    def run(self):
        self._status_update(self._id, Status.DOWNLOADING)
        self._downloader.download([self._url])


class RepeatedTimer:
  def __init__(self, interval: int, function: callable, *args, **kwargs):
    self._timer = None
    self.interval = interval
    self.function = function
    self.args = args
    self.kwargs = kwargs
    self.is_running = False
    self.next_call = time.time()
    self.start()

  def _run(self):
    self.is_running = False
    self.start()
    self.function(*self.args, **self.kwargs)

  def start(self):
    if not self.is_running:
      self.next_call += self.interval
      self._timer = threading.Timer(self.next_call - time.time(), self._run)
      self._timer.daemon = True
      self._timer.start()
      self.is_running = True

  def stop(self):
    self._timer.cancel()
    self.is_running = False