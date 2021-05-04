FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y
RUN apt-get install -y python3-pip python-dev build-essential

RUN apt-get install -y ffmpeg

COPY . /app
WORKDIR /app

RUN pip3 install -r requirements.txt

ENTRYPOINT ["waitress-serve"]
CMD ["--call", "--host=0.0.0.0", "--port=8000", "app:create_app"]