# Hosting

## Frontend
The frontend of this application is hosted using [Vercel](https://vercel.com/) and can be found at [Youtube to MP3](https://ytmp3.vercel.app/).

To host using [Vercel](https://vercel.com/), you must specify the following `Build & Development Settings`:

```
Framework Preset: SvelteKit
Build Command: `npm run build` or `svelte-kit build`
Output Directory: build
Install Command: `yarn install` or `npm install`
Development Command: svelte-kit dev
```

The `Root Directory` for the frontend should be set to `client`.

The following `Environment Variables` must be specified for the frontend to properly function:

```bash
# the address to the backend server for the application 
VITE_SERVER_ADDR=https://some-address.com
```

## Backend
The backend of this application is hosted using [Heroku](https://www.heroku.com/).

It is hosted as a container running the backend server as a web application.

The following `Config Vars` should be specified for the backend application:

```bash
# The number of threads used to process application logic (integer)
WAITRESS_THREAD=200

# NOTE: on Heroku this does not need to be specified as it is specifed by Heroku itself
PORT=8080
```