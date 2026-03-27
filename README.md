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

YouTube Downloader is an application created for downloading [YouTube](https://www.youtube.com/) videos with a variety of formats and configurable options available.

## Features

- Search YouTube directly using search terms or input direct video URL.
- Concurrently download and process many videos at once.
- Configurable audio download formats (AAC, FLAC, M4A, MP3, OPUS, WAV).
- Configurable video download formats (AVI, FLV, MKV, MOV, MP4, WEBM).
- Configurable quality options (best, worst).
- Configurable options to automatically embed video metadata, thumbnails, and subtitles.

# Developer Guide

Please refer to the [contributing guide](CONTRIBUTING.md) for how to install the project for development purposes.

## Monorepo structure:

### Apps:

- `api`: An API developed using [Python](https://www.python.org/) with [FastAPI](https://fastapi.tiangolo.com/) and [yt-dlp](https://github.com/yt-dlp/yt-dlp).
- `web`: A web application developed using [SvelteKit](https://kit.svelte.dev/).

### Packages:

- `client`: An API client generated using [TypeScript](https://www.typescriptlang.org/) with [openapi-ts](https://github.com/hey-api/openapi-ts).
- `ui`: A UI library developed using [Svelte](https://svelte.dev/).
