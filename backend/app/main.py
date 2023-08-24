import os
import tomllib
from typing import Any

import uvicorn
from fastapi import FastAPI
from fastapi import routing
from starlette.middleware.cors import CORSMiddleware

from .routers import downloads
from .routers import search
from .routers import session
from .utils.managers import session_manager

# Read data from pyproject.toml file
pyproject_data: dict[str, Any] = {}
pyproject_path = os.path.join(
    os.path.dirname(__file__), '..', 'pyproject.toml',
)
with open(pyproject_path, 'rb') as f:
    pyproject_data = tomllib.load(f)['project']


# Note: this requires that function names for each route are unique. If not
#       the openapi spec will have duplicate unique ID's. We use this to ensure
#       the generated client has reasonable function names.
def generate_custom_unique_id(route: routing.APIRoute):
    return route.name


app = FastAPI(
    title=pyproject_data['name'],
    summary=pyproject_data['description'],
    contact={
        'name': pyproject_data['authors'][0]['name'],
        'url': pyproject_data['urls']['Repository'],
    },
    license_info={
        'name': pyproject_data['license']['text'],
        'url': f'{pyproject_data["urls"]["Repository"]}/blob/main/LICENSE',
    },
    openapi_tags=[
        {'name': 'session', 'description': 'Session management.'},
        {'name': 'search', 'description': 'Search YouTube.'},
        {'name': 'downloads', 'description': 'Download management.'},
    ],
    version=pyproject_data['version'],
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


def main():
    host = os.environ.get('HOST', '0.0.0.0')
    port = int(os.environ.get('PORT', 8080))
    dev = os.environ.get('DEV') is not None
    print(f'Serving on {host}:{port} (reload={dev})', flush=True)
    uvicorn.run('app.main:app', host=host, port=port, reload=dev)


if __name__ == '__main__':
    main()
