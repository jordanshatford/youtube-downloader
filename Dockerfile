FROM node:lts-alpine AS base
ARG VITE_SERVER_ADD
ENV VITE_SERVER_ADDR $VITE_SERVER_ADDR

WORKDIR /workspace

# Setup corepack with version of pnpm specified in package.json
COPY package.json pnpm-lock.yaml pnpm-workspace.yaml /workspace/
RUN corepack enable && \
    corepack prepare && \
    pnpm config set store-dir /tmp/cache/pnpm

# Fetch build and runtime dependencies
RUN --mount=type=cache,target=/tmp/cache \
    pnpm fetch --workspace-root

# Install required dependencies
COPY . /workspace/

# Install dependencies cached above
RUN --mount=type=cache,target=/tmp/cache \
    pnpm install -r --offline

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
