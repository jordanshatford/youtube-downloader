# Hosting

## Frontend
The frontend of this application is hosted using [Vercel](https://vercel.com/) and can be found at [YouTube Audio Downloader](https://youtubeaudiodownloader.vercel.app/).

To host using [Vercel](https://vercel.com/), you must specify the following `Build & Development Settings`:

```
Framework Preset: SvelteKit
Build Command: `npm run build` or `svelte-kit build`
Output Directory: build
Install Command: `yarn install` or `npm install`
Development Command: svelte-kit dev
```

The `Root Directory` for the frontend should be set to `frontend`.

The following `Environment Variables` must be specified for the frontend to properly function:

```bash
# the address to the backend server for the application
VITE_SERVER_ADDR=https://some-address.com
```

## Backend
The backend of this application is hosted using [Render](https://render.com/).

It is hosted as a container running the backend server as a web application.

The following `Config Vars` should be specified for the backend application:

```bash
# the address of the frontend (used to allow CORS origin)
ALLOWED_ORIGIN=https://some-address.com

# NOTE: on Render this does not need to be specified as it is detected by Render itself
PORT=8080
```
