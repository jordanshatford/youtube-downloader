FROM node:lts-alpine AS web-base

WORKDIR /workspace

# Setup corepack with version of pnpm specified in package.json
COPY package.json pnpm-lock.yaml pnpm-workspace.yaml /workspace/
RUN corepack enable && \
    corepack prepare && \
    pnpm config set store-dir /tmp/cache/pnpm

# Fetch build and runtime dependencies
RUN --mount=type=cache,target=/tmp/cache \
    pnpm fetch --workspace-root

# Install required dependencies
COPY . /workspace/

# Install dependencies cached above
RUN --mount=type=cache,target=/tmp/cache \
    pnpm install -r --offline

# Expose port we are running the frontend on
EXPOSE 5173

# In development we expose the Vite hot reload port and install all dependencies
FROM web-base AS web-development
EXPOSE 24678
CMD [ "pnpm", "web", "dev", "--host" ]

# In production we run the build version of code without hot reload
FROM web-base AS web-production
RUN pnpm web build
CMD [ "pnpm", "web", "preview", "--host", "--port=5173" ]


FROM python:3.12 AS api-base

# Ensure FFMPEG is available
RUN apt-get update -y
RUN apt-get install -y ffmpeg

WORKDIR /workspace/apps/api

# Copy core functionality
COPY ./core /workspace/core/

# Install required python packages
COPY ./apps/api/requirements.txt /workspace/apps/api/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy over source and config files
COPY ./apps/api/app /workspace/apps/api/app
COPY ./apps/api/pyproject.toml /workspace/apps/api/pyproject.toml

# Expose port we are running the api on
EXPOSE 8080

# In development run the application with reload active
FROM api-base AS api-development
CMD [ "uvicorn", "app.main:app", "--host=0.0.0.0", "--port=8080", "--reload", "--reload-dir", "../../" ]

# In production run the application without reload
FROM api-base AS api-production
CMD [ "uvicorn", "app.main:app", "--host=0.0.0.0", "--port=8080" ]
