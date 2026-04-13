import contextlib
import functools
import subprocess
import sys

from yt_dlp import version

from .models import Version


@functools.lru_cache(maxsize=1)
def get_ffmpeg_version() -> str | None:
    with contextlib.suppress(Exception):
        result = subprocess.run(
            ["ffmpeg", "-version"],
            capture_output=True,
            text=True,
            check=True,
        )
        first_line = result.stdout.splitlines()[0]
        # Example: "ffmpeg version 6.1.1 ..."
        return first_line.split(" ")[2]
    return None


@functools.lru_cache(maxsize=1)
def get_node_version() -> str | None:
    with contextlib.suppress(Exception):
        result = subprocess.run(
            ["node", "--version"],
            capture_output=True,
            text=True,
            check=True,
        )
        # Example: "v20.11.1"
        return result.stdout.strip().lstrip("v")
    return None


@functools.lru_cache(maxsize=1)
def get_python_version() -> str | None:
    with contextlib.suppress(Exception):
        v = sys.version_info
        return f"{v.major}.{v.minor}.{v.micro}"
    return None


CORE_VERSIONS: list[Version] = [
    Version(component="ffmpeg", version=get_ffmpeg_version()),
    Version(component="NodeJS", version=get_node_version()),
    Version(component="Python", version=get_python_version()),
    Version(component="yt-dlp", version=version.__version__),
]
