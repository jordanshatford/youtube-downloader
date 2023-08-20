FROM node:lts-alpine

ENV NODE_ENV development

WORKDIR /frontend

RUN npm install -g pnpm

COPY package.json pnpm-lock.yaml svelte.config.js ./
RUN pnpm install

COPY . .

EXPOSE 5173
EXPOSE 24678
CMD [ "pnpm", "dev", "--host" ]
