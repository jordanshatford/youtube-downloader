FROM node:18-alpine

ENV NODE_ENV development

WORKDIR /frontend

COPY package*.json svelte.config.js ./
RUN npm install

COPY . .

EXPOSE 5173
EXPOSE 24678
CMD [ "npm", "run", "dev", "--", "--host" ]
