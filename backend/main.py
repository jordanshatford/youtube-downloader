import os

import uvicorn
from fastapi import FastAPI
from routers import downloads
from routers import search
from routers import session
from starlette.middleware.cors import CORSMiddleware
from utils.managers import session_manager

tags_metadata = [
    {'name': 'session', 'description': 'Get session id to use for future requests.'},
    {'name': 'search', 'description': 'Search youtube for videos.'},
    {'name': 'downloads', 'description': 'Manage downloads of videos from youtube.'},
]

description = """
Youtube to MP3 API works with the frontend website to
allow users to download specific videos as audio files.
"""

app = FastAPI(
    title='Youtube to MP3 API',
    description=description,
    contact={
        'name': 'Youtube to MP3',
        'url': 'https://github.com/jordanshatford/youtube-to-mp3',
    },
    license_info={
        'name': 'MIT License',
        'url': 'https://github.com/jordanshatford/youtube-to-mp3/blob/main/LICENSE',
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
def shutdown_cleanup():
    print('Cleaning up all session for shutdown', flush=True)
    session_manager.cleanup(force=True)


if __name__ == '__main__':
    host = os.environ.get('HOST', '0.0.0.0')
    port = int(os.environ.get('PORT', 8080))
    debug = int(os.environ.get('DEBUG', 0)) == 1
    print(f'Serving on {host}:{port}', flush=True)
    uvicorn.run('main:app', host=host, port=port, reload=debug)
