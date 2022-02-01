FROM node:16-alpine

ENV NODE_ENV development

WORKDIR /frontend

COPY package*.json ./
RUN npm install

COPY . .

EXPOSE 3000
EXPOSE 24678
CMD [ "npm", "run", "dev", "--", "--host" ]
