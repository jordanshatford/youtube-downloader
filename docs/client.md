# SvelteKit Frontend

The frontend for this project is written using the javascript framework [SvelteKit](https://kit.svelte.dev/).

The frontend also utilizes other technologies like:
  - [ESLint](https://eslint.org/)
  - [PostCSS](https://postcss.org/)
  - [Prettier](https://prettier.io/)
  - [Tailwind](https://tailwindcss.com/)
  - [TypeScript](https://www.typescriptlang.org/)

## Developing
To setup the frontend for local development you must first ensure that you have the following dependencies installed:
  - [NodeJS](https://nodejs.org/en/) (version v14.18.1 or above)
  - [NPM](https://www.npmjs.com/) (version 6.14.15 or above) `this will be installed with NodeJS`

Now you can install the project specific dependencies using:
```bash
npm install
```

Once the project dependencies are installed you can start a development server using:
```bash
npm run dev

# the following command line args can be used
# 1. start the server and open in a new browser tab
npm run dev -- --open

# 2. expose the server to other devices on the network
npm run dev -- --host
```

## Building
The production build for this application uses a static adapter in SPA (Single Page Application) mode. You can build a production version of the application using:

```bash
npm run build

# if you want to preview the build, you can do so by running
# NOTE: this should not be used in production
npm run preview
```

## Docker
Docker has not yet been implemented for the SvelteKit frontend.