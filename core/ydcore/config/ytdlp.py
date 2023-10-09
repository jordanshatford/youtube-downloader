from collections.abc import Callable
from collections.abc import Iterator
from collections.abc import Mapping
from collections.abc import Sequence
from typing import Any
from typing import Literal
from typing import NotRequired
from typing import TypeAlias
from typing import TypedDict


# TODO: make total=False and Requried for anything actually
#       required for all below TypedDicts
# TODO: cleanup most of Any types where possible
# TODO: better type this later
class InfoDict(TypedDict):
    pass


# Represents progress information provided to progress_hooks in yt-dlp
class ProgressHookInfo(TypedDict):
    status: Literal['downloading', 'finished', 'error']
    info_dict: InfoDict
    filename: NotRequired[str]
    tmpfilename: NotRequired[str]
    downloaded_bytes: NotRequired[int]
    total_bytes: NotRequired[int | None]
    total_bytes_estimate: NotRequired[int | None]
    elapsed: NotRequired[float | None]
    eta: NotRequired[int | None]
    speed: NotRequired[float | None]
    fragment_index: NotRequired[int | None]
    fragment_count: NotRequired[int | None]


# Represents progress information provided to postprocessor_hooks in yt-dlp
class PostprocessorHookInfo(TypedDict):
    status: Literal['started', 'processing', 'finished']
    postprocessor: str
    info_dict: InfoDict


OutTmplTypesKeys: TypeAlias = Literal[
    'chapter',
    'subtitle',
    'thumbnail',
    'description',
    'annotation',
    'infojson',
    'link',
    'pl_video',
    'pl_thumbnail',
    'pl_description',
    'pl_infojson',
]


class YoutubeDLParams(TypedDict):
    # Username for authentication purposes.
    username: NotRequired[str | None]
    # Password for authentication purposes.
    password: NotRequired[str | None]
    # Password for accessing a video.
    videopassword: NotRequired[str | None]
    # Adobe Pass multiple-system operator identifier.
    ap_mso: NotRequired[str | None]
    # Multiple-system operator account username.
    ap_username: NotRequired[str | None]
    # Multiple-system operator account password.
    ap_password: NotRequired[str | None]
    # Use netrc for authentication instead.
    usenetrc: NotRequired[bool | None]
    # Location of the netrc file. Defaults to ~/.netrc.
    netrc_location: NotRequired[str | None]
    # Use a shell command to get credentials
    netrc_cmd: NotRequired[str | None]
    # Print additional info to stdout.
    verbose: NotRequired[bool | None]
    # Do not print messages to stdout.
    quiet: NotRequired[bool | None]
    # Do not print out anything for warnings.
    no_warnings: NotRequired[bool | None]
    # A dict with keys WHEN mapped to a list of templates to print to stdout.
    # The allowed keys are video or any of theitems in utils.POSTPROCESS_WHEN.
    # For compatibility, a single list is also accepted.
    forceprint: NotRequired[Mapping[str, Sequence[str]] | Sequence[str] | None]
    # A dict with keys WHEN (same as forceprint) mapped to a list of tuples
    # with (template, filename).
    print_to_file: NotRequired[Mapping[str, tuple[str, str]] | None]
    # Force printing info_dict as JSON.
    forcejson: NotRequired[bool | None]
    # Force printing the info_dict of the whole playlist (or video) as a
    # single JSON line.
    dump_single_json: NotRequired[bool | None]
    # Force writing download archive regardless of 'skip_download' or
    # 'simulate'.
    force_write_download_archive: NotRequired[bool | None]
    # Do not download the video files. If unset (or None), simulate only
    # if listsubtitles, listformats or list_thumbnails is used.
    simulate: NotRequired[bool | None]
    # Video format code. see "FORMAT SELECTION" for more details. You can
    # also pass a function. The function takes 'ctx' as argument and
    # returns the formats to download. See "build_format_selector" for an
    # implementation.
    format: NotRequired[str | Callable[[Any], Mapping[str, Any]] | None]
    # Allow unplayable formats to be extracted and downloaded.
    allow_unplayable_formats: NotRequired[bool | None]
    # Ignore "No video formats" error. Usefull for extracting metadata even
    # if the video is not actually available for download (experimental).
    ignore_no_formats_error: NotRequired[bool | None]
    # A list of fields by which to sort the video formats. See
    # "Sorting Formats" for more details.
    format_sort: NotRequired[Sequence[str] | None]
    # Force the given format_sort. see "Sorting Formats" for more details.
    format_sort_force: NotRequired[bool | None]
    # Whether to prefer video formats with free containers over non-free ones
    # of same quality.
    prefer_free_formats: NotRequired[bool | None]
    # Allow multiple video streams to be merged into a single file
    allow_multiple_video_streams: NotRequired[bool | None]
    # Allow multiple audio streams to be merged into a single file
    allow_multiple_audio_streams: NotRequired[bool | None]
    # Whether to test if the formats are downloadable. Can be True
    # (check all), False (check none), 'selected' (check selected formats),
    # or None (check only if requested by extractor)
    check_formats: NotRequired[bool | Literal['selected'] | None]
    # Dictionary of output paths. The allowed keys are 'home', 'temp' and
    # the keys of OUTTMPL_TYPES (in utils/_utils.py)
    paths:  NotRequired[
        Mapping[
            Literal['home', 'temp']
            | OutTmplTypesKeys, str,
        ] | None
    ]
    # Dictionary of templates for output names. Allowed keys are 'default'
    # and the keys of OUTTMPL_TYPES (in utils/_utils.py). For compatibility
    # with youtube-dl, a single string can also be used
    outtmpl: NotRequired[
        str | Mapping[
            Literal['default']
            | OutTmplTypesKeys, str,
        ] | None
    ]
    # Placeholder for unavailable meta fields.
    outtmpl_na_placeholder: NotRequired[str | None]
    # Do not allow "&" and spaces in file names
    restrictfilenames: NotRequired[bool | None]
    # Limit length of filename (extension excluded)
    trim_file_name: NotRequired[int | None]
    # Force the filenames to be windows compatible
    windowsfilenames: NotRequired[bool | None]
    # Do not stop on download/postprocessing errors. Can be 'only_download'
    # to ignore only download errors. Default is 'only_download' for CLI, but
    # False for API.
    ignoreerrors: NotRequired[bool | Literal['only_download'] | None]
    # Number of allowed failures until the rest of the playlist is skipped
    skip_playlist_after_errors: NotRequired[int | None]
    # List of regexes to match against extractor names that are allowed
    allowed_extractors: NotRequired[Sequence[str] | None]
    # Overwrite all video and metadata files if True, overwrite only non-video
    # files if None and don't overwrite any file if False.
    overwrites: NotRequired[bool | None]
    # Specific indices of playlist to download.
    playlist_items: NotRequired[Sequence[int] | None]
    # Download playlist items in random order.
    playlistrandom: NotRequired[bool | None]
    # Process playlist entries as they are received.
    lazy_playlist: NotRequired[bool | None]
    # Download only matching titles.
    matchtitle: NotRequired[bool | None]
    # Reject downloads for matching titles.
    rejecttitle: NotRequired[bool | None]
    # Log messages to a logging.Logger instance.
    logger: NotRequired[Any | None]
    # Print everything to stderr instead of stdout.
    logtostderr: NotRequired[bool | None]
    # Display progress in console window's titlebar.
    consoletitle: NotRequired[str | None]
    # Write the video description to a .description file
    writedescription: NotRequired[bool | None]
    # Write the video description to a .info.json file
    writeinfojson: NotRequired[bool | None]
    # Remove internal metadata from the infojson.
    clean_infojson: NotRequired[bool | None]
    # Extract video comments. This will not be written to disk unless
    # writeinfojson is also given
    getcomments: NotRequired[bool | None]
    # Write the video annotations to a .annotations.xml file
    writeannotations: NotRequired[bool | None]
    #: Write the thumbnail image to a file.
    writethumbnail: NotRequired[bool | None]
    # Whether to write playlists' description, infojson etc also to
    # disk when using the 'write*' options
    allow_playlist_files: NotRequired[bool | None]
    # Write all thumbnail formats to files
    write_all_thumbnails: NotRequired[bool | None]
    # Write an internet shortcut file, depending on the current platform
    # (.url/.webloc/.desktop)
    writelink: NotRequired[bool | None]
    # Write a Windows internet shortcut file (``.url``).
    writeurllink: NotRequired[bool | None]
    # Write a macOS internet shortcut file (``.webloc``).
    writewebloclink: NotRequired[bool | None]
    # Write a Linux internet shortcut file (``.desktop``).
    writedesktoplink: NotRequired[bool | None]
    # Write the video subtitles to a file.
    writesubtitles: NotRequired[bool | None]
    # Write the automatically generated subtitles to a file.
    writeautomaticsub: NotRequired[bool | None]
    # Lists all available subtitles for the video.
    listsubtitles: NotRequired[bool | None]
    # The format code for subtitles.
    subtitlesformat: NotRequired[str | None]
    # List of languages of the subtitles to download (can be regex). The list
    # may contain "all" to refer to all the available subtitles. The language
    # can be prefixed with a "-" to exclude it from the requested languages,
    # e.g. ['all', '-live_chat'].
    subtitleslangs: NotRequired[Sequence[str] | None]
    # Keep the video file after post-processing.
    keepvideo: NotRequired[bool | None]
    # A utils.DateRange object, download only if the upload_date is in the
    # range.
    daterange: NotRequired[Any | None]
    # Skip the actual download of the video file.
    skip_download: NotRequired[bool | None]
    # Location of the cache files in the filesystem. False to disable
    # filesystem cache.
    cachedir: NotRequired[str | Literal[False] | None]
    # Download single video instead of a playlist if in doubt.
    noplaylist: NotRequired[bool | None]
    # An integer representing the user's age in years. Unsuitable videos for
    # the given age are skipped.
    age_limit: NotRequired[int | None]
    # An integer representing the minimum view count the video must have in
    # order to not be skipped. Videos without view count information are
    # always downloaded. None for no limit.
    min_views: NotRequired[int | None]
    # An integer representing the maximum view count the video must have in
    # order to not be skipped. Videos without view count information are
    # always downloaded. None for no limit.
    max_views: NotRequired[int | None]
    # A set, or the name of a file where all downloads are recorded. Videos
    # already present in the file are not downloaded again.
    download_archive: NotRequired[str | Sequence[str] | None]
    # Stop the download process after attempting to download a file that
    # is in the archive.
    break_on_existing: NotRequired[bool | None]
    # Whether break_on_reject and break_on_existing should act on each input
    # URL as opposed to for the entire queue
    break_per_url: NotRequired[bool | None]
    # File name or text stream from where cookies should be read and dumped to
    cookiefile: NotRequired[str | None]
    # A tuple containing the name of the browser, the profile name/path from
    # where cookies are loaded, the name of the keyring, and the container
    # name, e.g. ('chrome', ) or ('vivaldi', 'default', 'BASICTEXT') or
    # ('firefox', 'default', None, 'Meta')
    cookiesfrombrowser: NotRequired[tuple[str, ...] | None]
    # Explicitly allow HTTPS connection to servers that do not support
    # RFC 5746 secure renegotiation
    legacyserverconnect: NotRequired[bool | None]
    # Do not verify SSL certificates.
    nocheckcertificate: NotRequired[bool | None]
    # Path to client certificate file in PEM format. May include the private
    # key.
    client_certificate: NotRequired[str | None]
    # Path to private key file for client certificate.
    client_certificate_key: NotRequired[str | None]
    # Password for client certificate private key, if encrypted.
    client_certificate_password: NotRequired[str | None]
    # Use HTTP instead of HTTPS to retrieve information. Only supported by
    # some extractors.
    prefer_insecure: NotRequired[bool | None]
    # Enable file:// URLs. This is disabled by default for security reasons.
    enable_file_urls: NotRequired[bool | None]
    # A dictionary of custom headers to be used for all requests.
    http_headers: NotRequired[Mapping[str, str] | None]
    # URL of the proxy server to use.
    proxy: NotRequired[str | None]
    # URL of the proxy to use for IP address verification on geo-restricted
    # sites.
    geo_verification_proxy: NotRequired[str | None]
    # Time to wait for unresponsive hosts, in seconds.
    socket_timeout: NotRequired[int | None]
    # Work around buggy terminals without bidirectional text support,
    # using fridibi.
    bidi_workaround: NotRequired[bool | None]
    # Print out sent and received HTTP traffic
    debug_printtraffic: NotRequired[bool | None]
    # Prepend this string if an input url is not valid. 'auto' for
    # elaborate guessing.
    default_search: NotRequired[str | None]
    # Use this encoding instead of the system-specified.
    encoding: NotRequired[str | None]
    # Whether to resolve and process url_results further
    #   * False:     Always process. Default for API
    #   * True:      Never process
    #   * 'in_playlist': Do not process inside playlist/multi_video
    #   * 'discard': Always process, but don't return the result from
    #                inside playlist/multi_video
    #   * 'discard_in_playlist': Same as "discard", but only for playlists
    #                            (not multi_video). Default for CLI
    extract_flat: NotRequired[
        bool | Literal[
            'in_playlist',
            'discard', 'discard_in_playlist',
        ] | None
    ]
    # If given, wait for scheduled streams to become available. The value
    # should be a tuple containing the range (min_secs, max_secs) to wait
    # between retries.
    wait_for_video: NotRequired[tuple[int, int] | None]
    # A list of dictionaries, each with an entry
    #   * key:  The name of the postprocessor. See
    #           yt_dlp/postprocessor/__init__.py for a list.
    #   * when: When to run the postprocessor. Allowed values are the entries
    #           of utils.POSTPROCESS_WHEN Assumed to be 'post_process' if not
    #           given
    postprocessors: NotRequired[list[dict[str, Any]] | None]
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
    progress_hooks: NotRequired[
        Sequence[
            Callable[
                [
                    ProgressHookInfo,
                ], None,
            ]
        ] | None
    ]
    # A list of functions that get called on postprocessing progress, with a
    # dictionary with the entries
    #   * status: One of "started", "processing", or "finished".
    #             Check this first and ignore unknown values.
    #   * postprocessor: Name of the postprocessor
    #   * info_dict: The extracted info_dict
    # Progress hooks are guaranteed to be called at least twice (with status
    # "started" and "finished") if the processing is successful.
    postprocessor_hooks: NotRequired[
        Sequence[
            Callable[
                [
                    PostprocessorHookInfo,
                ], None,
            ]
        ] | None
    ]
    # "/" separated list of extensions to use when merging formats.
    merge_output_format: NotRequired[str | None]
    # Expected final extension; used to detect when the file was already
    # downloaded and converted.
    final_ext: NotRequired[str | None]
    # Automatically correct known faults of the file.
    # One of:
    #   - "never": do nothing
    #   - "warn": only emit a warning
    #   - "detect_or_warn": check whether we can do anything about it,
    #                       warn otherwise (default)
    fixup: NotRequired[Literal['never', 'warn', 'detect_or_warn'] | None]
    # Client-side IP address to bind to.
    source_address: NotRequired[str | None]
    # Number of seconds to sleep between requests .during extraction
    sleep_interval_requests: NotRequired[int | None]
    # Number of seconds to sleep before each download when used alone or
    # a lower bound of a range for randomized sleep before each download
    # (minimum possible number of seconds to sleep) when used along with
    # max_sleep_interval.
    sleep_interval: NotRequired[int | None]
    # Upper bound of a range for randomized sleep before each download
    # (maximum possible number of seconds to sleep). Must only be used along
    # with sleep_interval. Actual sleep time will be a random float from range
    # [sleep_interval; max_sleep_interval].
    max_sleep_interval: NotRequired[int | None]
    # Number of seconds to sleep before each subtitle download.
    sleep_interval_subtitles: NotRequired[int | None]
    # Print an overview of available video formats and exit.
    listformats: NotRequired[bool | None]
    # Print a table of all thumbnails and exit.
    list_thumbnails: NotRequired[bool | None]
    # A function that gets called for every video with the signature
    # (info_dict, *, incomplete: bool) -> str | None
    # For backward compatibility with youtube-dl, the signature
    # (info_dict) -> str | None is also allowed.
    # If it returns a message, the video is ignored.
    # If it returns None, the video is downloaded.
    # If it returns utils.NO_DEFAULT, the user is interactively asked whether
    # to download the video.
    # Raise utils.DownloadCancelled(msg) to abort remaining downloads when
    # a video is rejected.
    # match_filter_func in utils.py is one example for this.
    match_filter: NotRequired[
        Callable[
            [InfoDict, bool],
            str | None,
        ] | Callable[[InfoDict], str | None] | None
    ]
    # A Dictionary with output stream names as keys and their respective color
    # policy as values. Can also just be a single color policy, in which case
    # it applies to all outputs.
    # Valid stream names are 'stdout' and 'stderr'. Valid color policies are
    # one of 'always', 'auto', 'no_color' or 'never'.
    color: NotRequired[Mapping[Any, Any] | None]
    # Bypass geographic restriction via faking X-Forwarded-For HTTP header
    geo_bypass: NotRequired[bool | None]
    # Two-letter ISO 3166-2 country code that will be used for explicit
    # geographic restriction bypassing via faking X-Forwarded-For HTTP header.
    geo_bypass_country: NotRequired[str | None]
    # IP range in CIDR notation that will be used similarly to
    # geo_bypass_country.
    geo_bypass_ip_block: NotRequired[str | None]
    # A dictionary of protocol keys and the executable of the external
    # downloader to use for it. The allowed protocols are
    # default|http|ftp|m3u8|dash|rtsp|rtmp|mms. Set the value to 'native'
    # to use the native downloader.
    external_downloader: NotRequired[Mapping[Any, Any] | None]
    # Compatibility options. See "Differences in default behavior". The
    # following options do not work when used through the API: filename,
    # abort-on-error, multistreams, no-live-chat, format-sort,
    # no-clean-infojson, no-playlist-metafiles, no-keep-subs,
    # no-attach-info-json.
    # Refer __init__.py for their implementation
    compat_opts: NotRequired[Mapping[str, Any] | None]
    # Dictionary of templates for progress outputs. Allowed keys are
    # 'download', 'postprocess', 'download-title' (console title) and
    # 'postprocess-title'. The template is mapped on a dictionary with
    # keys 'progress' and 'info'.
    progress_template: NotRequired[Mapping[str, Any] | None]
    # Dictionary of functions that takes the number of attempts as argument
    # and returns the time to sleep in seconds. Allowed keys are 'http',
    # 'fragment', 'file_access'.
    retry_sleep_functions: NotRequired[Mapping[Any, Any] | None]
    # A callback function that gets called for every video with the signature
    # (info_dict, ydl) -> Iterable[Section]. Only the returned sections will
    # be downloaded.
    # Each Section is a dict with the following keys:
    #   * start_time: Start time of the section in seconds
    #   * end_time: End time of the section in seconds
    #   * title: Section title (Optional)
    #   * index: Section number (Optional)
    download_ranges: NotRequired[Callable[[Any, Any], Iterator[Any]] | None]
    # Re-encode the video when downloading ranges to get precise cuts
    force_keyframes_at_cuts: NotRequired[bool | None]
    # Do not print the progress bar.
    noprogress: NotRequired[bool | None]
    # Whether to download livestreams videos from the start.
    live_from_start: NotRequired[bool | None]
    """
    The following parameters are not used by YoutubeDL itself, they are used
    by the downloader (see yt_dlp/downloader/common.py):
    """
    # Do not use temporary .part files.
    nopart: NotRequired[bool | None]
    # Use the 'Last-modified' header to set output file timestamps.
    updatetime: NotRequired[bool | None]
    # Size of download buffer in bytes.
    buffersize: NotRequired[int | None]
    # Download speed limit, in bytes/sec.
    ratelimit: NotRequired[int | None]
    # Assume the download is being throttled below this speed (bytes/sec).
    throttledratelimit: NotRequired[int | None]
    # Skip files smaller than this size.
    min_filesize: NotRequired[int | None]
    # Skip files larger than this size.
    max_filesize: NotRequired[int | None]
    # Download only first bytes to test the downloader.
    test: NotRequired[bool | None]
    # Do not automatically resize the download buffer.
    noresizebuffer: NotRequired[bool | None]
    # Number of times to retry for expected network errors. Default is 0
    # for API, but 10 for CLI.
    retries: NotRequired[int | None]
    # Number of times to retry on file access error (default: 3)
    file_access_retries: NotRequired[int | None]
    # Try to continue downloads if possible.
    continuedl: NotRequired[bool | None]
    # Set ytdl.filesize user xattribute with expected size.
    xattr_set_filesize: NotRequired[bool | None]
    # Use the mpegts container for HLS videos.
    hls_use_mpegts: NotRequired[bool | None]
    # Size of a chunk for chunk-based HTTP downloading. May be useful for
    # bypassing bandwidth throttling imposed by a webserver (experimental).
    http_chunk_size: NotRequired[int | None]
    # A dictionary of downloader keys (in lower case) and a list of additional
    # command-line arguments for the executable. Use 'default' as the name for
    # arguments to be passed to all downloaders. For compatibility with
    # youtube-dl, a single list of args can also be used.
    external_downloader_args: NotRequired[
        Literal['default']
        | Mapping[str, Sequence[str]] | Sequence[str] | None
    ]
    # Number of fragments of a dash/hlsnative video that should be downloaded
    # concurrently.
    concurrent_fragment_downloads: NotRequired[int | None]
    """
    The following options are used by the post processors:
    """
    # Location of the ffmpeg binary; either the path to the binary or its
    # containing directory.
    ffmpeg_location: NotRequired[str | None]
    # A dictionary of postprocessor/executable keys (in lower case) and a
    # list of additional command-line arguments for the
    # postprocessor/executable. The dict can also have "PP+EXE" keys which
    # are used when the given exe is used by the given PP. Use 'default' as
    # the name for arguments to passed to all PP. For compatibility with
    # youtube-dl, a single list of args can also be used.
    postprocessor_args: NotRequired[
        Mapping[
            str,
            Sequence[str],
        ] | Sequence[str] | None
    ]
    """
    The following options are used by the extractors:
    """
    # Number of times to retry for known errors (default: 3).
    extractor_retries: NotRequired[int | None]
    # Whether to process dynamic DASH manifests (default: True).
    dynamic_mpd: NotRequired[bool | None]
    # Split HLS playlists to different formats at discontinuities such as
    # ad breaks (default: False).
    hls_split_discontinuity: NotRequired[bool | None]
    # A dictionary of arguments to be passed to the extractors. See
    # "EXTRACTOR ARGUMENTS" for details.
    # Example: {'youtube': {'skip': ['dash', 'hls']}}.
    extractor_args: NotRequired[Mapping[str, Mapping[str, Any]] | None]
    # Mark videos watched (even with --simulate). Only for YouTube.
    mark_watched: NotRequired[bool | None]
    """
    The following options are deprecated and may be removed in the future:
    """
    # Stop the download process when encountering a video that has been
    # filtered out.
    #   - `raise DownloadCancelled(msg)` in match_filter instead
    break_on_reject: NotRequired[bool | None]
    # Force downloader to use the generic extractor.
    # Deprecated. Use allowed_extractors = ['generic', 'default'].
    force_generic_extractor: NotRequired[bool | None]
    # Playlist item to start at. Use playlist_items.
    playliststart: NotRequired[int | None]
    # Playlist item to end at. Use playlist_items.
    playlistend: NotRequired[int | None]
    # Download playlist items in reverse order. Use playlist_items.
    playlistreverse: NotRequired[bool | None]
    # Force printing final URL. Use forceprint.
    forceurl: NotRequired[bool | None]
    # Force printing title. Use forceprint.
    forcetitle: NotRequired[str | None]
    # Force printing ID. Use forceprint.
    forceid: NotRequired[bool | None]
    # Force printing thumbnail URL. Use forceprint.
    forcethumbnail: NotRequired[bool | None]
    # Force printing description. Use forceprint.
    forcedescription: NotRequired[bool | None]
    # Force printing final filename. Use forceprint.
    forcefilename: NotRequired[bool | None]
    # Force printing duration. Use forceprint.
    forceduration: NotRequired[str | None]
    # Use subtitleslangs = ['all']. Downloads all the subtitles of the video
    # (requires writesubtitles or writeautomaticsub).
    allsubtitles: NotRequired[bool | None]
    # Download ads as well (does not work).
    include_ads: NotRequired[bool | None]
    # Not implemented Boolean, true iff we are allowed to contact the yt-dlp
    # servers for debugging.
    call_home: NotRequired[Callable[[str], None] | None]
    # Register a custom postprocessor, A list of functions that get called
    # as the final step for each video file, after all postprocessors have
    # been called. The filename will be passed as the only argument
    post_hooks: NotRequired[Sequence[Any] | None]
    # Use external_downloader = {'m3u8': 'native'} or {'m3u8': 'ffmpeg'}.
    # Use the native HLS downloader instead of ffmpeg/avconv if True, otherwise
    # use ffmpeg/avconv if False, otherwise use downloader suggested by
    # extractor if None.
    hls_prefer_native: NotRequired[bool | None]
    # avconv support is deprecated If False, use avconv instead of ffmpeg
    # if both are available, otherwise prefer ffmpeg.
    prefer_ffmpeg: NotRequired[bool | None]
    # Use extractor_args. If True (default), DASH manifests and related data
    # will be downloaded and processed by extractor. You can reduce network
    # I/O by disabling it if you don't care about DASH. Only for YouTube.
    youtube_include_dash_manifest: NotRequired[bool | None]
    # Use extractor_args. If True (default), DASH manifests and related data
    # will be downloaded and processed by extractor. You can reduce network
    # I/O by disabling it if you don't care about HLS. Only for YouTube.
    youtube_include_hls_manifest: NotRequired[bool | None]
    # Same as `color='no_color'`
    no_color: NotRequired[bool | None]
    # Same as `overwrites=False`
    no_overwrites: NotRequired[bool | None]
