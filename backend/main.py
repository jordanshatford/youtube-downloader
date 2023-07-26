import os

import uvicorn
from fastapi import FastAPI
from routers import downloads
from routers import search
from routers import session
from starlette.middleware.cors import CORSMiddleware
from utils.managers import session_manager

tags_metadata = [
    {'name': 'session', 'description': 'Get session id to use for future requests.'},   # noqa: E501
    {'name': 'search', 'description': 'Search YouTube for videos.'},
    {'name': 'downloads', 'description': 'Manage downloads of videos from YouTube.'},   # noqa: E501
]

description = """
YouTube Audio Downloader API works with the frontend website to
allow users to download specific videos as audio files.
"""

app = FastAPI(
    title='YouTube Audio Downloader API',
    description=description,
    contact={
        'name': 'YouTube Audio Downloader',
        'url': 'https://github.com/jordanshatford/youtube-audio-downloader',
    },
    license_info={
        'name': 'MIT License',
        'url': 'https://github.com/jordanshatford/youtube-audio-downloader/blob/main/LICENSE',   # noqa: E501
    },
    openapi_tags=tags_metadata,
)

allowed_origin = os.environ.get('ALLOWED_ORIGIN', 'http://localhost:5173')

app.add_middleware(
    CORSMiddleware,
    allow_origins=[allowed_origin],
    allow_credentials=True,
    allow_methods=['POST', 'GET', 'DELETE'],
    allow_headers=['*'],
)

app.include_router(search.router)
app.include_router(session.router)
app.include_router(downloads.router)


@app.on_event('shutdown')
def shutdown_cleanup() -> None:
    print('Cleaning up all session for shutdown', flush=True)
    session_manager.cleanup(force=True)


if __name__ == '__main__':
    host = os.environ.get('HOST', '0.0.0.0')
    port = int(os.environ.get('PORT', 8080))
    debug = int(os.environ.get('DEBUG', 0)) == 1
    print(f'Serving on {host}:{port}', flush=True)
    uvicorn.run('main:app', host=host, port=port, reload=debug)
