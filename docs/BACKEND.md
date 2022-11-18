# Fast API Backend

The backend for this project is written using the [Python](https://www.python.org/) web application framework [FastAPI](https://fastapi.tiangolo.com/).

The backend also utilizes other technologies like:
  - [FFMPEG](https://www.ffmpeg.org/)
  - [YouTubeDL](https://youtube-dl.org/)

## Developing
To setup the backend for local development you must first ensure that you have the following dependencies installed:
  - [FFMPEG](https://www.ffmpeg.org/)
  - [Python](https://www.python.org/)
  - [PIP](https://pypi.org/project/pip/)

Now you can install the project specific dependencies using:
```bash
pip install -r requirements.txt
```

Once the project dependencies are installed you can start backend server using:
```bash
python main.py
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
