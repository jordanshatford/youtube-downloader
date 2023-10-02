import os
import tomllib
from typing import Any

from fastapi import FastAPI
from fastapi import routing
from fastapi.middleware.cors import CORSMiddleware

from .routers import downloads
from .routers import search
from .routers import session
from .session import session_manager

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
    separate_input_output_schemas=False,
)

# Default localhost to be allowed.
allow_origins = [
    'http://localhost',
    'http://localhost:5173',
]

# Allow additional origin specfied in env variable if present.
additional_origin = os.environ.get('ALLOWED_ORIGIN', None)
if additional_origin is not None:
    allow_origins.append(additional_origin)

app.add_middleware(
    CORSMiddleware,
    allow_origins=allow_origins,
    allow_credentials=True,
    allow_methods=['POST', 'PUT', 'GET', 'DELETE'],
    allow_headers=['*'],
)

app.include_router(search.router)
app.include_router(session.router)
app.include_router(downloads.router)


@app.on_event('shutdown')
def shutdown_cleanup() -> None:
    print('Cleaning up all session for shutdown', flush=True)
    session_manager.cleanup(force=True)
