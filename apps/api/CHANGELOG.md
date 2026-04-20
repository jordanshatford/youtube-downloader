# @yd/api

## 2.3.0

### Minor Changes

- refactor: remove available download options endpoint ([`60e3ef2`](https://github.com/jordanshatford/youtube-downloader/commit/60e3ef2c110d3bcbe07067bc0f77b029e316176a))

### Patch Changes

- fix: only use extract flat when searching for videos ([`cfde8eb`](https://github.com/jordanshatford/youtube-downloader/commit/cfde8eb1bc6cd22ed97398dcf8b69cf8e119f804))

## 2.2.1

### Patch Changes

- fix: handle batch remove when directory does not exist ([`e7d7cc6`](https://github.com/jordanshatford/youtube-downloader/commit/e7d7cc6031fde31bb977853374e8e8ed4bbd026a))

## 2.2.0

### Minor Changes

- feat: use shared thread pool for each session ([`0f257c9`](https://github.com/jordanshatford/youtube-downloader/commit/0f257c93feaa5f7651b3ad80c17fb8d4fd44c884))

- feat: use property tmp directory for downloads ([`c34ed6f`](https://github.com/jordanshatford/youtube-downloader/commit/c34ed6fcc6a927c822e900867cf244a44942eebf))

- feat: generate session id in init rather than passing to session ([`3c13dca`](https://github.com/jordanshatford/youtube-downloader/commit/3c13dcacaf6874d9ac4fac7c3200f1f6c82b18ec))

- feat: add support for batch downloading videos and playlists ([`8d76401`](https://github.com/jordanshatford/youtube-downloader/commit/8d764019e09dc0d9ef965f5fadd792c7ff0c6f2a))

- feat: refactor search into a search manager ([`0907595`](https://github.com/jordanshatford/youtube-downloader/commit/09075957bb6e9d57bf22e83a0563d6426516110e))

- feat: enable ignoreerrors in yt-dlp commands ([`fd5175d`](https://github.com/jordanshatford/youtube-downloader/commit/fd5175db8895f056094f8d0b673636c328da41b5))

- feat: move downloads status queue to download manager ([`8f3637a`](https://github.com/jordanshatford/youtube-downloader/commit/8f3637a1caff4aac3bb3f9325b5ca23047bccf49))

- feat: move downloadable to own handling and unify functionality ([`e238dbe`](https://github.com/jordanshatford/youtube-downloader/commit/e238dbe411d72f12340e11237b312f3b935693ed))

### Patch Changes

- fix: do not send updates when status has not changed ([`fd813ae`](https://github.com/jordanshatford/youtube-downloader/commit/fd813ae73bc31de8f881411abbebb33e7b81ba20))

- fix: update download put endpoint to use download id path parameter ([`2e250fa`](https://github.com/jordanshatford/youtube-downloader/commit/2e250fa9083660f79d99640e4adc542ad6f8bc1e))

## 2.1.0

### Minor Changes

- feat: use movefiles postprocessor to detect completed ([`0accf9d`](https://github.com/jordanshatford/youtube-downloader/commit/0accf9da30d237453440858dbaa78e2a777fe556))

- feat: make yt-dlp handling generic for reuse with batch downloads ([`0accf9d`](https://github.com/jordanshatford/youtube-downloader/commit/0accf9da30d237453440858dbaa78e2a777fe556))

- feat: add ability to see component versions in application ([`dc842b0`](https://github.com/jordanshatford/youtube-downloader/commit/dc842b06651f1b581d7c50898c833a9b1e788a3d))

- feat: use lazy playlist with yt-dlp ([`4c8d8ab`](https://github.com/jordanshatford/youtube-downloader/commit/4c8d8abda24d8e1032afe7fc19a955947b55c42a))

### Patch Changes

- fix: use paths and outtmpl together ([`52337ee`](https://github.com/jordanshatford/youtube-downloader/commit/52337ee5f5027e07c5ead6d72c2e4cb93fa85981))

- fix: improve information parsing from yt-dlp ([`70e951a`](https://github.com/jordanshatford/youtube-downloader/commit/70e951abb5b8aba79efdd5ac04c2dac7de6b1166))

## 2.0.1

### Patch Changes

- fix: typing for download get file endpoint ([`577e43c`](https://github.com/jordanshatford/youtube-downloader/commit/577e43c87902989545361203b2d022a697f95b4f))

## 2.0.0

### Major Changes

- feat: update path for next search result endpoint ([`59f03af`](https://github.com/jordanshatford/youtube-downloader/commit/59f03afd9d1a488cf13abfb81aa25aa171b6fee9))

### Minor Changes

- feat: exclude active live streams from search and downloads ([`e28cc38`](https://github.com/jordanshatford/youtube-downloader/commit/e28cc380d51db142c0cd741fec52f2a472ec0fde))

- feat: add endpoints to get current search state ([`59f03af`](https://github.com/jordanshatford/youtube-downloader/commit/59f03afd9d1a488cf13abfb81aa25aa171b6fee9))

### Patch Changes

- fix: raise http exception in sse endpoints ([`cd29934`](https://github.com/jordanshatford/youtube-downloader/commit/cd299342ce21442bf78c6024642435c5ed884da9))

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
