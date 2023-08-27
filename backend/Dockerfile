FROM python:3.11 as base

# Ensure FFMPEG is available
RUN apt-get update -y
RUN apt-get install -y ffmpeg

WORKDIR /backend

# Install required python packages
COPY ./requirements.txt /backend/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy over source and config files
COPY ./app /backend/app
COPY ./pyproject.toml /backend/pyproject.toml

# Expose port we are running the backend on
EXPOSE 8080

# In development run the application with reload active
FROM base as development
CMD [ "uvicorn", "app.main:app", "--host=0.0.0.0", "--port=8080", "--reload" ]

# In production run the application without reload
FROM base as production
CMD [ "uvicorn", "app.main:app", "--host=0.0.0.0", "--port=8080" ]
