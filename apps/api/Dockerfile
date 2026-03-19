FROM python:3.14 AS base

# Ensure FFMPEG is available
RUN apt-get update -y
RUN apt-get install -y ffmpeg

WORKDIR /workspace

# Install uv
RUN apt-get install -y pipx && pipx ensurepath
RUN pipx install "uv>=0.10.11,<0.11.0"
ENV PATH=/root/.local/bin:$PATH

# Install dependencies
COPY pyproject.toml uv.lock /workspace/
RUN uv sync --no-dev

# Copy over source and config files
COPY ./app /workspace/app
COPY ./package.json /workspace/package.json

# Expose port we are running the api on
EXPOSE 8000

# In development run the application with reload active
FROM base AS development
CMD [ "uv", "run", "fastapi", "dev" ]

# In production run the application without reload
FROM base AS production
CMD [ "uv", "run", "fastapi", "run" ]
