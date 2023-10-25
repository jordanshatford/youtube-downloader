import argparse
import os

from ydcore import AudioFormat
from ydcore import DownloadManager
from ydcore import DownloadOptions
from ydcore import DownloadQuality
from ydcore import VideoFormat
from ydcore import VideoWithOptions

from .utils import to_video

COMMAND_NAME = 'download'


# Add options relevant for downloading videos
def add_argparse_arguments(parser: argparse.ArgumentParser) -> None:
    parser.add_argument('url')
    parser.add_argument(
        '-f', '--format',
        choices=[
            *[f.value for f in VideoFormat],
            *[f.value for f in AudioFormat],
        ],
        type=str.lower,
        default=VideoFormat.MP4.value,
        help='format to download the YouTube video in.',
    )
    parser.add_argument(
        '-q', '--quality',
        choices=[q.value for q in DownloadQuality],
        type=str.lower,
        default=DownloadQuality.BEST.value,
        help='quality to download the YouTube video in.',
    )
    parser.add_argument(
        '-o', '--out-dir',
        default=os.path.join(os.getcwd(), '__downloads__'),
        help='directory to download files to.',
    )
    parser.add_argument(
        '--embed-metadata',
        action='store_true',
        help='embed metadata in the downloaded file.',
    )
    parser.add_argument(
        '--embed-thumbnail',
        action='store_true',
        help='embed the thumbnail in the downloaded file.',
    )
    parser.add_argument(
        '--embed-subtitles',
        action='store_true',
        help='embed the subtitles in the downloaded file.',
    )


# Convert passed arguments to DownloadOptions understandable by core
def to_download_options(args: argparse.Namespace) -> DownloadOptions:
    try:
        f = AudioFormat(args.format)
    except ValueError:
        f = VideoFormat(args.format)
    return DownloadOptions(
        format=f,
        quality=DownloadQuality.BEST,
        embed_metadata=args.embed_metadata,
        embed_thumbnail=args.embed_thumbnail,
        embed_subtitles=args.embed_subtitles,
    )


# Run the download for a video
def run(args: argparse.Namespace) -> int:
    url: str = args.url
    options = to_download_options(args)
    output_dir: str = args.out_dir
    video = to_video(url)
    # Could not find the video they were trying to download
    if video is None:
        print('Could not find video.')
        return 1
    # Get video and add download options we are using
    videoWithOptions = VideoWithOptions(
        **video.model_dump(),
        options=options,
    )
    # Download and wait for video
    manager = DownloadManager(output_dir)
    manager.add(videoWithOptions)
    manager.wait_for_all()
    return 0
