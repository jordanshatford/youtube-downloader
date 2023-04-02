FROM ubuntu:23.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y

RUN apt-get install -y --no-install-recommends python3-dev python3-pip python3-venv ffmpeg \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /backend

RUN python3 -m venv /opt/venv

COPY requirements.txt ./

RUN . /opt/venv/bin/activate

RUN /opt/venv/bin/python3 -m pip install --no-cache-dir --upgrade pip \
    && /opt/venv/bin/python3 -m pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["/opt/venv/bin/python3"]
CMD ["main.py"]
