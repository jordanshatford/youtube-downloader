import json
import logging
import os
from contextlib import asynccontextmanager
from logging.handlers import RotatingFileHandler
from typing import Any

from fastapi import FastAPI
from fastapi import routing
from fastapi.middleware.cors import CORSMiddleware

from .routers import downloads
from .routers import search
from .routers import session
from .session import session_manager


handler = RotatingFileHandler(
    'output.log',
    maxBytes=1024 * 1024 * 5,  # 5 MB
    backupCount=5,
)
logging.basicConfig(
    format='[%(asctime)s] %(levelname)s ' +
           ' - %(name)s - %(module)s - %(funcName)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.WARNING,
    handlers=[handler],
)
logging.getLogger('sse_starlette').setLevel(logging.ERROR)


# Read data from package.json file
project_data: dict[str, Any] = {}
project_data_path = os.path.join(
    os.path.dirname(__file__), '..', 'package.json',
)
with open(project_data_path, 'rb') as f:
    project_data = json.load(f)


# Note: this requires that function names for each route are unique. If not
#       the openapi spec will have duplicate unique ID's. We use this to ensure
#       the generated client has reasonable function names.
def generate_custom_unique_id(route: routing.APIRoute):
    return route.name


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    # Clean up all sessions
    print('Cleaning up all session for shutdown', flush=True)
    session_manager.cleanup(force=True)


app = FastAPI(
    title=project_data['name'],
    summary=project_data['description'],
    contact={
        'name': 'GitHub',
        'url': project_data['repository']['url'],
    },
    license_info={
        'name': project_data['license'],
        'url': f'{project_data["repository"]["url"]}/blob/main/LICENSE',
    },
    openapi_tags=[
        {'name': 'session', 'description': 'Session management.'},
        {'name': 'search', 'description': 'Search YouTube.'},
        {'name': 'downloads', 'description': 'Download management.'},
    ],
    version=project_data['version'],
    generate_unique_id_function=generate_custom_unique_id,
    lifespan=lifespan,
)

# Default localhost to be allowed.
allow_origins = [
    'http://localhost',
    'http://localhost:5173',
    'http://127.0.0.1',
    'http://127.0.0.1:5173',
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
