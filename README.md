<p align="center">
  <br />
  <img width="150" height="150" src="./apps/web/static/icon.png" alt="Logo">
  <h1 align="center"><b>YouTube Downloader</b></h1>
  <p align="center">
    Fast, high quality YouTube downloads.
    <br />
    <a href="https://youtubedownloader.duckdns.org"><strong>youtubedownloader.duckdns.org »</strong></a>
    <br />
    <br />
  </p>
</p>

YouTube Downloader is a full stack application created to allow users to download [YouTube](https://www.youtube.com/) videos. The user is able to select from a variety of audio and video formats and other configuration options.

## Features

- Directly search YouTube for videos.
- Download and convert multiple videos concurrently.
- Download quality options (best, worst).
- Option to automatically embed video metadata, thumbnail, and subtitles.
- Variety of audio formats supported (AAC, FLAC, M4A, MP3, OPUS, WAV).
- Variety of video formats supported (AVI, FLV, MKV, MOV, MP4, WEBM).
- Web UI with support for dark and light themes.

# Developer Guide

Please refer to the [contributing guide](CONTRIBUTING.md) for how to install the project for development purposes.

## Monorepo structure:

### Apps:

- `api`: An API developed in [Python](https://www.python.org/) using [FastAPI](https://fastapi.tiangolo.com/).
- `extension`: A browser extension developed using [WXT](https://wxt.dev/) and [Svelte](https://svelte.dev/).
- `web`: A web application developed in [SvelteKit](https://kit.svelte.dev/).

### Packages:

- `client`: A TypeScript API client generated from the OpenAPI specification for the API using [openapi-ts](https://github.com/hey-api/openapi-ts).
- `config`: Common configs shared between other packages and apps in the monorepo.
- `ui`: A UI library used by the project developed in [Svelte](https://svelte.dev/).
