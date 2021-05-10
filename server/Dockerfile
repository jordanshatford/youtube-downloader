FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y \
    && apt-get install -y --no-install-recommends \
       python3-pip python-dev ffmpeg \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /server/requirements.txt
WORKDIR /server
RUN pip3 install --no-cache-dir --upgrade pip \
    && pip3 install --no-cache-dir -r requirements.txt

COPY . /server
WORKDIR /server

ENTRYPOINT ["waitress-serve"]
CMD ["--call", "app:create_app"]