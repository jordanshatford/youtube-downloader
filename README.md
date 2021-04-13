# Youtube To MP3 
## About
This is a website for converting youtube videos to MP3. It was created using Svelte.js + Tailwind CSS + Flask.

## Getting started
Install client and server dependencies.
```sh
yarn  # Install client
cd server; pip install -r requirements.txt  # Install server
```

## Serve in development mode
- Starts dev server on port 5000
- Hot reloading (server & client)
```sh
yarn serve
```

## Serve in production mode
```sh
yarn start [flask_run_options]
```
### flask_run_options
#### `--host` flask host (default 127.0.0.1)
#### `--port` flask port (default 5000)

## Deploy for production without node.js
Build the client app:
```sh
yarn build
```
The code can now be deployed on a server and run:
```sh
cd server && flask run --host 0.0.0.0
```
