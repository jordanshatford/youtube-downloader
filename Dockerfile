FROM node:lts-alpine as base

RUN corepack enable

WORKDIR /code

# Install required dependencies
COPY package.json pnpm-lock.yaml pnpm-workspace.yaml ./

# Copy over project files
COPY apps/ /code/apps/
COPY packages/ /code/packages/

RUN pnpm install

# Expose port we are running the frontend on
EXPOSE 5173

# In development we expose the Vite hot reload port and install all dependencies
FROM base as development
EXPOSE 24678
CMD [ "pnpm", "web", "dev", "--host" ]

# In production we run the build version of code without hot reload
FROM base as production
RUN pnpm web build
CMD [ "pnpm", "web", "preview", "--host", "--port=5173" ]
