import os

import uvicorn
from fastapi import FastAPI
from fastapi import routing
from routers import downloads
from routers import search
from routers import session
from starlette.middleware.cors import CORSMiddleware
from utils.managers import session_manager


GITHUB_URL: str = 'https://github.com/jordanshatford/youtube-audio-downloader'


# Note: this requires that function names for each route are unique. If not
#       the openapi spec will have duplicate unique ID's. We use this to ensure
#       the generated client has reasonable function names.
def generate_custom_unique_id(route: routing.APIRoute):
    return route.name


app = FastAPI(
    title='YouTube Audio Downloader API',
    summary='Search and download YouTube videos in various audio formats.',
    contact={
        'name': 'YouTube Audio Downloader',
        'url': GITHUB_URL,
    },
    license_info={
        'name': 'MIT License',
        'url': f'{GITHUB_URL}/blob/main/LICENSE',
    },
    openapi_tags=[
        {'name': 'session', 'description': 'Session management.'},
        {'name': 'search', 'description': 'Search YouTube.'},
        {'name': 'downloads', 'description': 'Download management.'},
    ],
    generate_unique_id_function=generate_custom_unique_id,
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
    dev = os.environ.get('DEV') is not None
    print(f'Serving on {host}:{port} (reload={dev})', flush=True)
    uvicorn.run('main:app', host=host, port=port, reload=dev)
