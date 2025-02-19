FROM python:3.13 AS base

# Ensure FFMPEG is available
RUN apt-get update -y
RUN apt-get install -y ffmpeg

WORKDIR /workspace

# Install Poetry
ENV POETRY_VERSION=2.1.1
RUN apt-get install -y pipx && pipx ensurepath
RUN pipx install "poetry==$POETRY_VERSION"
ENV PATH=/root/.local/bin:$PATH

# Install dependencies
COPY pyproject.toml poetry.lock /workspace/
RUN poetry install --without dev

# Copy over source and config files
COPY ./app /workspace/app
COPY ./package.json /workspace/package.json

# Expose port we are running the api on
EXPOSE 8080

# In development run the application with reload active
FROM base AS development
CMD [ "poetry", "run", "uvicorn", "app.main:app", "--host=0.0.0.0", "--port=8080", "--reload", "--reload-dir", "../../" ]

# In production run the application without reload
FROM base AS production
CMD [ "poetry", "run", "uvicorn", "app.main:app", "--host=0.0.0.0", "--port=8080" ]
