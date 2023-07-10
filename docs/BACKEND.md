# Fast API Backend

The backend for this project is written using the [Python](https://www.python.org/) web application framework [FastAPI](https://fastapi.tiangolo.com/).

The backend also utilizes other technologies like:
  - [FFMPEG](https://www.ffmpeg.org/)
  - [YouTubeDL](https://youtube-dl.org/)
  - [YT DLP](https://github.com/yt-dlp/yt-dlp)

## Developing
To setup the backend for local development you must first ensure that you have the following dependencies installed:
  - [FFMPEG](https://www.ffmpeg.org/)
  - [Python](https://www.python.org/)
  - [PIP](https://pypi.org/project/pip/)

Optionally: create and activate the Venv to use:
```
python3 -m venv venv
source venv/bin/activate
```

Now you can install the project specific dependencies using:
```bash
python3 -m pip install -r requirements.txt
```

Once the project dependencies are installed you can start backend server using:
```bash
python3 main.py
```

## Using PNPM
The backend can be run using [PNPM](https://pnpm.io/) to handle setting up the Venv, installing dependencies, and running the server. You can run the backend using:
```bash
pnpm dev
```

## Using Docker
The backend can be run using [Docker](https://www.docker.com) and the provided Dockerfile.

You can build the Docker container using the following command from within the backend folder:
```bash
docker build -t youtubeaudiodownloader-backend .
```

You can run the Docker container using the following command:
```bash
# NOTE: you can specify whichever port you want to run the backend on
docker run -p 8000:8000 youtubeaudiodownloader-backend
```
