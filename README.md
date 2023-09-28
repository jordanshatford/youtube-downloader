<p align="center">
  <br />
  <img width="150" height="150" src="./apps/web/static/images/logo.png" alt="Logo">
  <h1 align="center"><b>YouTube Downloader</b></h1>
  <div align="center">
    <a href="https://kit.svelte.dev/">
      <img src="https://img.shields.io/badge/Powered%20by-Svelte-%23FF3E00.svg?style=flat&logo=svelte" alt="Powered by SvelteKit">
    </a>
    <a href="https://www.typescriptlang.org/">
      <img src="https://img.shields.io/badge/Language-Typescript-%233178C6.svg?style=flat&logo=typescript" alt="Language: TypeScript">
    </a>
    <a href="https://tailwindcss.com">
      <img src="https://img.shields.io/badge/CSS%20Framework-TailwindCSS-%2306B6D4?logo=tailwindcss" alt="CSS Framework: TailwindCSS">
    </a>
    <a href="https://fastapi.tiangolo.com/">
      <img src="https://img.shields.io/badge/Powered%20by-FastAPI-%23009688.svg?style=flat&logo=fastapi" alt="Powered by FastAPI">
    </a>
    <a href="https://www.python.org/">
      <img src="https://img.shields.io/badge/Language-Python-%233776AB.svg?style=flat&logo=python" alt="Language: Python">
    </a>
    <a href="https://www.ffmpeg.org/">
      <img src="https://img.shields.io/badge/Powered%20by-FFMPEG-%23007808.svg?style=flat&logo=ffmpeg" alt="Powered by FFMPEG">
    </a>
    <a href="https://github.com/yt-dlp/yt-dlp">
      <img src="https://img.shields.io/badge/Powered%20by-yt--dlp-%23FF0000.svg?style=flat&logo=youtube" alt="Powered by yt-dlp">
    </a>
    <a href="https://github.com/jordanshatford/youtube-audio-downloader/blob/main/LICENSE">
      <img src="https://img.shields.io/badge/License-MIT-black.svg?style=flat&logo=license" alt="License: MIT">
    </a>
  </div>
  <p align="center">
    Fast, high quality YouTube downloads
    <br />
    <a href="https://youtubeaudiodownloader.vercel.app/"><strong>youtubeaudiodownloader.vercel »</strong></a>
    <br />
    <br />
  </p>
</p>

YouTube Downloader is a full stack application created to allow users to download [YouTube](https://www.youtube.com/) videos. The user is able to select from a variety of audio and video formats and other configuration options.

## Features
  - Directly search YouTube for videos.
  - Download and convert multiple videos concurrently.
  - Download quality options (best, worst).
  - Options to automatically embed video metadata.
  - Variety of audio formats supported (AAC, FLAC, M4A, MP3, OPUS, WAV).
  - Variety of video formats supported (AVI, FLV, MKV, MOV, MP4, WEBM).
  - Web UI with support for dark and light themes.

# Developer Guide
Please refer to the [contributing guide](CONTRIBUTING.md) for how to install the project for development purposes.

## Monorepo structure:

### Apps:
- `api`: An API developed in Python using [FastAPI](https://fastapi.tiangolo.com/).
- `web`: A web application developed in [SvelteKit](https://kit.svelte.dev/).

### Packages:
- `client`: A TypeScript API client generated from the OpenAPI specification for the API using [OpenAPI TypeScript Codegen](https://github.com/ferdikoomen/openapi-typescript-codegen/blob/master/docs/basic-usage.md).
- `config`: Common configs shared between other packages and apps in the monorepo.
- `ui`: A UI library used by the project developed in [Svelte](https://svelte.dev/).
