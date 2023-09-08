FROM python:3.11 AS base

# Ensure FFMPEG is available
RUN apt-get update -y
RUN apt-get install -y ffmpeg

WORKDIR /workspace

# Install required python packages
COPY ./requirements.txt /workspace/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy over source and config files
COPY ./app /workspace/app
COPY ./pyproject.toml /workspace/pyproject.toml

# Expose port we are running the api on
EXPOSE 8080

# In development run the application with reload active
FROM base AS development
CMD [ "uvicorn", "app.main:app", "--host=0.0.0.0", "--port=8080", "--reload" ]

# In production run the application without reload
FROM base AS production
CMD [ "uvicorn", "app.main:app", "--host=0.0.0.0", "--port=8080" ]
