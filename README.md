# Youtube To MP3 
## About
This is a website for converting youtube videos to MP3. It was created using Svelte.js + Tailwind CSS + Flask.

## Getting started
Install client and server dependencies.
```sh
npm install  # Install client
cd server; pip install -r requirements.txt  # Install server
```

## Serve in development mode
- Starts dev server on port 5000
- Hot reloading (server & client)
```sh
npm run serve
```

## Serve in production mode
```sh
npm run start [flask_run_options]
```
### flask_run_options
#### `--host` flask host (default 127.0.0.1)
#### `--port` flask port (default 8000)

## Deploy for production without node.js
Build the client app:
```sh
npm run build
```
The code can now be deployed on a server and run:
```sh
cd server && npm run start
```

## Using Docker
The client and server [Docker](https://www.docker.com/) containers can be setup and ran using [docker-compose](https://docs.docker.com/compose/). To start and build the containers run:
```sh
docker-compose up --build
```