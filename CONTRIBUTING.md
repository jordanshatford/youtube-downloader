# Contributing

## Local development requirements

Setting up the project for local development will require all of the following the be installed:

- [git](https://git-scm.com/) (version `2.39` or higher)
- [ffmpeg](https://ffmpeg.org/) (version `6.0` or higher)
- [python](https://www.python.org/) (version `3.11` or higher)
- [node](https://nodejs.org/en) (version `18.0` or higher)
- *optionally* [docker](https://www.docker.com/) (version `24.0` or higher)

> NOTE: docker is an optional but preferred way to develop. If you are using docker, all other dependencies above will not be required except for git.

## Setting up for development

### Docker

Setting up the project using docker is simple. Simply run the following command with docker installed:

```sh
# NOTE: ensure to specify the dev docker compose file for features like hot reload when code changes
docker compose -f docker-compose.dev.yml up --build
```

To run the CLI application using docker you can run the following command:

```sh
docker compose run cli --build
```

> NOTE: using this method will only allow running the project. You must setup the project without docker to be able to generate, format, lint, and check the project.

### Without Docker

Setting up the project without docker will require that the above dependencies are all installed. After which you can run the following commands:

```sh
# Enable corepack, it is disabled by default in the supported versions of NodeJS
corepack enable
# Prepare corepack based on the packageManager specified in the projects package.json
corepack prepare
# Install all dependencies
pnpm install
# Run the projects API and web app in development mode
pnpm dev:web
# Run the projects API and extension in development mode
pnpm dev:extension
# Run the projects CLI in development mode
pnpm cli dev
```

#### Generating the client package

The project uses a generated client to interact with the api based on its [OpenAPI](https://www.openapis.org/) specification.

To generate an up to date client, run the following command:

```sh
pnpm generate
```

> NOTE: this will first generate the openapi.json specification in the api, then generate the client, and apply any patches we have made. These generated files should be committed to source control.

#### Running formatting, linting, and checking

Running formatting on the project can be done using the following command:

```sh
pnpm format
```

Running linting on the project can be done using the following command:

```sh
pnpm lint
```

Running checking on the project can be done using the following command:

```sh
pnpm check
```

## Fixing bugs

If you plan to fix a bug with the project, please start by putting in a bug report issue in the GitHub repository.

## Adding features

If you plan to add a new feature to the project, please start by putting in a feature request issue in the GitHub repository. This will ensure tracking of the feature request, as well as provide information about what you are attempting to implement.

After developing a new feature it is important that you test it thoroughly locally first before submitting a pull request.
