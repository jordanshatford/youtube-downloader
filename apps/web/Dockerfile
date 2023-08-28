FROM node:lts-alpine as base

# Install PNPM the package manager we use
RUN npm install -g pnpm

WORKDIR /frontend

# Install required dependencies
COPY package.json svelte.config.js ./
RUN pnpm install

# Copy over project files
COPY . .

# Expose port we are running the frontend on
EXPOSE 5173

# In development we expose the Vite hot reload port and install all dependencies
FROM base as development
EXPOSE 24678
CMD [ "pnpm", "dev", "--host" ]

# In production we run the build version of code without hot reload
FROM base as production
RUN pnpm build
CMD [ "pnpm", "preview", "--host", "--port=5173" ]
