FROM node:lts-alpine AS base

RUN corepack enable

# Install required dependencies
COPY . /code/

WORKDIR /code
RUN corepack prepare && pnpm install

# Expose port we are running the frontend on
EXPOSE 5173

# In development we expose the Vite hot reload port and install all dependencies
FROM base AS development
EXPOSE 24678
CMD [ "pnpm", "web", "dev", "--host" ]

# In production we run the build version of code without hot reload
FROM base AS production
RUN pnpm web build
CMD [ "pnpm", "web", "preview", "--host", "--port=5173" ]
