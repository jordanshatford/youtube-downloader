import logging
from collections.abc import Callable
from collections.abc import Iterable
from collections.abc import Mapping
from collections.abc import Sequence
from typing import Any
from typing import Literal
from typing import Required
from typing import TypedDict

from yt_dlp import YoutubeDL


# Represents thumbnail information returned by yt-dlp.
# This only represents the fields that we use and may be missing some fields
# that yt-dlp provides.
class Thumbnail(TypedDict, total=False):
    url: str | None
    height: int | None
    width: int | None


# Get the best thumbnail out of available options. This returns the last
# thumbnail in the list as they are sorted as such. As an improvement we
# should check for the thumbnail with the best resolution.
def get_best_thumbnail(thumbnails: Sequence[Thumbnail]) -> Thumbnail:
    return thumbnails[-1]


# Represents the video information returned by yt-dlp.
# This only represents the fields that we use and may be missing some fields
# that yt-dlp provides.
class VideoInfo(TypedDict, total=False):
    id: Required[str]
    title: str | None
    url: str | None
    thumbnails: list[Thumbnail] | None
    description: str | None
    uploader: str | None
    uploader_id: str | None
    uploader_url: str | None
    channel: str | None
    channel_id: str | None
    channel_url: str | None
    duration: int | None
    view_count: int | None
    entries: Iterable["VideoInfo"]


# Represents progress information provided to progress_hooks in yt-dlp.
# This only represents the fields that we use and may be missing some fields
# that yt-dlp provides.
class ProgressHookInfo(TypedDict, total=False):
    status: Required[Literal["downloading", "finished", "error"]]
    info_dict: VideoInfo
    downloaded_bytes: float | None
    total_bytes: float | None
    total_bytes_estimate: float | None
    elapsed: float | None
    eta: float | None
    speed: float | None


# Represents progress information provided to postprocessor_hooks in yt-dlp.
# This only represents the fields that we use and may be missing some fields
# that yt-dlp provides.
class PostprocessorHookInfo(TypedDict, total=False):
    status: Required[Literal["started", "processing", "finished"]]
    postprocessor: str
    info_dict: VideoInfo


# Represents parameters passed to the yt-dlp api.
# This only represents the fields that we use and may be missing some fields
# that yt-dlp provides.
class YoutubeDLParams(TypedDict, total=False):
    # Print additional info to stdout.
    verbose: bool | None
    # Do not print messages to stdout.
    quiet: bool | None
    # Do not print out anything for warnings.
    no_warnings: bool | None
    # Video format code. see "FORMAT SELECTION" for more details. You can
    # also pass a function. The function takes 'ctx' as argument and
    # returns the formats to download. See "build_format_selector" for an
    # implementation.
    format: str | Callable[[Any], Mapping[str, Any]] | None
    # Dictionary of templates for output names. Allowed keys are 'default'
    # and the keys of OUTTMPL_TYPES (in utils/_utils.py). For compatibility
    # with youtube-dl, a single string can also be used
    outtmpl: (
        str
        | Mapping[
            Literal[
                "default",
                "chapter",
                "subtitle",
                "thumbnail",
                "description",
                "annotation",
                "infojson",
                "link",
                "pl_video",
                "pl_thumbnail",
                "pl_description",
                "pl_infojson",
            ],
            str,
        ]
        | None
    )
    # Specific indices of playlist to download.
    playlist_items: str | None
    # Log messages to a logging.Logger instance.
    logger: Any | None
    #: Write the thumbnail image to a file.
    writethumbnail: bool | None
    # Write all thumbnail formats to files
    write_all_thumbnails: bool | None
    # Write the video subtitles to a file.
    writesubtitles: bool | None
    # Write the automatically generated subtitles to a file.
    writeautomaticsub: bool | None
    # The format code for subtitles.
    subtitlesformat: str | None
    # List of languages of the subtitles to download (can be regex). The list
    # may contain "all" to refer to all the available subtitles. The language
    # can be prefixed with a "-" to exclude it from the requested languages,
    # e.g. ['all', '-live_chat'].
    subtitleslangs: Sequence[str] | None
    # Skip the actual download of the video file.
    skip_download: bool | None
    # Download single video instead of a playlist if in doubt.
    noplaylist: bool | None
    # File name or text stream from where cookies should be read and dumped to
    cookiefile: str | None
    # A tuple containing the name of the browser, the profile name/path from
    # where cookies are loaded, the name of the keyring, and the container
    # name, e.g. ('chrome', ) or ('vivaldi', 'default', 'BASICTEXT') or
    # ('firefox', 'default', None, 'Meta')
    cookiesfrombrowser: tuple[str, ...] | None
    # Do not verify SSL certificates.
    nocheckcertificate: bool | None
    # Path to client certificate file in PEM format. May include the private
    # key.
    client_certificate: str | None
    # Path to private key file for client certificate.
    client_certificate_key: str | None
    # Password for client certificate private key, if encrypted.
    client_certificate_password: str | None
    # A dictionary of custom headers to be used for all requests.
    http_headers: Mapping[str, str] | None
    # Whether to resolve and process url_results further
    #   * False:     Always process. Default for API
    #   * True:      Never process
    #   * 'in_playlist': Do not process inside playlist/multi_video
    #   * 'discard': Always process, but don't return the result from
    #                inside playlist/multi_video
    #   * 'discard_in_playlist': Same as "discard", but only for playlists
    #                            (not multi_video). Default for CLI
    extract_flat: (
        bool
        | Literal[
            "in_playlist",
            "discard",
            "discard_in_playlist",
        ]
        | None
    )
    # A list of dictionaries, each with an entry
    #   * key:  The name of the postprocessor. See
    #           yt_dlp/postprocessor/__init__.py for a list.
    #   * when: When to run the postprocessor. Allowed values are the entries
    #           of utils.POSTPROCESS_WHEN Assumed to be 'post_process' if not
    #           given
    postprocessors: list[dict[str, Any]] | None
    # A list of functions that get called on download progress, with a
    # dictionary with the entries
    #   * status: One of "downloading", "error", or "finished". Check this
    #             first and ignore unknown values.
    #   * info_dict: The extracted info_dict
    # If status is one of "downloading", or "finished", the following
    # properties may also be present:
    #   * filename: The final filename (always present)
    #   * tmpfilename: The filename we're currently writing to
    #   * downloaded_bytes: Bytes on disk
    #   * total_bytes: Size of the whole file, None if unknown
    #   * total_bytes_estimate: Guess of the eventual file size, None if
    #                           unavailable.
    #   * elapsed: The number of seconds since download started.
    #   * eta: The estimated time in seconds, None if unknown
    #   * speed: The download speed in bytes/second, None if unknown
    #   * fragment_index: The counter of the currently downloaded video
    #                     fragment.
    #   * fragment_count: The number of fragments (= individual files
    #                     that will be merged)
    # Progress hooks are guaranteed to be called at least once (with status
    # "finished") if the download is successful.
    progress_hooks: (
        Sequence[
            Callable[
                [
                    ProgressHookInfo,
                ],
                None,
            ]
        ]
        | None
    )
    # A list of functions that get called on postprocessing progress, with a
    # dictionary with the entries
    #   * status: One of "started", "processing", or "finished".
    #             Check this first and ignore unknown values.
    #   * postprocessor: Name of the postprocessor
    #   * info_dict: The extracted info_dict
    # Progress hooks are guaranteed to be called at least twice (with status
    # "started" and "finished") if the processing is successful.
    postprocessor_hooks: (
        Sequence[
            Callable[
                [
                    PostprocessorHookInfo,
                ],
                None,
            ]
        ]
        | None
    )
    # Do not print the progress bar.
    noprogress: bool | None
    """
    The following parameters are not used by YoutubeDL itself, they are used
    by the downloader (see yt_dlp/downloader/common.py):
    """
    # Number of times to retry for expected network errors. Default is 0
    # for API, but 10 for CLI.
    retries: int | Literal["infinite"] | None
    """
    The following options are used by the post processors:
    """
    # A dictionary of postprocessor/executable keys (in lower case) and a
    # list of additional command-line arguments for the
    # postprocessor/executable. The dict can also have "PP+EXE" keys which
    # are used when the given exe is used by the given PP. Use 'default' as
    # the name for arguments to passed to all PP. For compatibility with
    # youtube-dl, a single list of args can also be used.
    postprocessor_args: (
        Mapping[
            str,
            Sequence[str],
        ]
        | Sequence[str]
        | None
    )
    """
    The following options are deprecated and may be removed in the future:
    """
    # Register a custom postprocessor, A list of functions that get called
    # as the final step for each video file, after all postprocessors have
    # been called. The filename will be passed as the only argument
    post_hooks: Sequence[Callable[[str], None] | None]


# Default parameters we use when interacting with the yt-dlp python api.
DEFAULT_YOUTUBE_DL_PARAMS: YoutubeDLParams = {
    "extract_flat": True,
    "logger": logging.getLogger("yt-dlp"),
    "noprogress": True,
    "noplaylist": True,
    "quiet": True,
    "retries": 5,
    "verbose": False,
}


__all__ = ["YoutubeDL"]
