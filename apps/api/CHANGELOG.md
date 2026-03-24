# @yd/api

## 1.5.0

### Minor Changes

- feat: remove output file in readable name option ([`39c40c8`](https://github.com/jordanshatford/youtube-downloader/commit/39c40c866564894d8e2328444fa774292b030144))

- feat: set default values for download options in api ([`43e603f`](https://github.com/jordanshatford/youtube-downloader/commit/43e603f24e8c09281b5024a54856b9c24d2befe0))

- feat: refactor download run handler ([`843e50e`](https://github.com/jordanshatford/youtube-downloader/commit/843e50ed8372f6433ad6dc6cca522a3ccef3c7b6))

- feat: get default download options from api ([`43e603f`](https://github.com/jordanshatford/youtube-downloader/commit/43e603f24e8c09281b5024a54856b9c24d2befe0))

- feat: use pathlib path when handling downloaded file ([`9b6c0c7`](https://github.com/jordanshatford/youtube-downloader/commit/9b6c0c791fa63e646221e5d2e874bc9b1625d36d))

- feat: add support for preferred subtitle language ([`286fbd7`](https://github.com/jordanshatford/youtube-downloader/commit/286fbd737f176e357d0b93a496d7bc1e2967260b))

### Patch Changes

- fix: use proper defaults for available download options ([`3014516`](https://github.com/jordanshatford/youtube-downloader/commit/30145163454a9bc183f4126bbc89f0bab5522ac4))

## 1.4.0

### Minor Changes

- feat: use yt-dlp to handle searching for youtube videos ([`cf98a97`](https://github.com/jordanshatford/youtube-downloader/commit/cf98a97fd83924e2d53331d41cd569ca591f9b5e))

- feat: update yt-dlp parameters to use node runtime ([`3a134ac`](https://github.com/jordanshatford/youtube-downloader/commit/3a134ac3626a867e09f26162a0b0774527113aad))

- feat: only allow one status hook per download ([`1963709`](https://github.com/jordanshatford/youtube-downloader/commit/1963709556ccc01bfa3cb661ab265943d7f3a8b4))

### Patch Changes

- fix: ensure progress is always none when status is not downloading ([`6498e12`](https://github.com/jordanshatford/youtube-downloader/commit/6498e12453950839ebda44bdf8023025bda45fd8))

## 1.3.0

### Minor Changes

- feat: remove channel thumbnail and make channel url optional ([`3b546b0`](https://github.com/jordanshatford/youtube-downloader/commit/3b546b0e236b908c527e5585f5d9f28e1242821a))

## 1.2.0

### Minor Changes

- feat: make python 3.13 the minimum supported version ([`c250236`](https://github.com/jordanshatford/youtube-downloader/commit/c250236590a6d2090c04d8b369372b556ad064d0))

## 1.1.0

### Minor Changes

- feat: expose download status endpoint in openapi spec ([`3cfd8c5`](https://github.com/jordanshatford/youtube-downloader/commit/3cfd8c546aefe51857b2b0cf6e2e011df4d51706))

- feat: replace sse-starlette with built in fastapi sse ([`9db9d7e`](https://github.com/jordanshatford/youtube-downloader/commit/9db9d7ea7ae89752557321d2a97c779310f9cdaf))

## 1.0.0

### Major Changes

- feat: initial release using changesets ([`c312038d585aecc5b0e43c5d35fe0f26c17d3273`](https://github.com/jordanshatford/youtube-downloader/commit/c312038d585aecc5b0e43c5d35fe0f26c17d3273))
