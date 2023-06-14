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
  - [NodeJS](https://nodejs.org/en/)
  - [PNPM](https://pnpm.io/)

Now you can install the project specific dependencies using:
```bash
pnpm install
```

Then you must specify a value for the following environment variables:
```bash
# the address to the backend server for the application
VITE_SERVER_ADDR=https://some-address.com
```
This can be done by filling out and copying the `example.env` file to a `.env` file.

Once the project dependencies are installed and environment variables specified you can start a development server using:
```bash
pnpm dev

# the following command line args can be used
# 1. start the server and open in a new browser tab
pnpm dev -- --open

# 2. expose the server to other devices on the network
pnpm dev -- --host
```

## Building
The production build for this application uses a static adapter in SPA (Single Page Application) mode. You can build a production version of the application using:

```bash
pnpm build

# if you want to preview the build, you can do so by running
# NOTE: this should not be used in production
pnpm preview
```

## Docker
Docker has not yet been implemented for the SvelteKit frontend.
