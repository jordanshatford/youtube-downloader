FROM node:16-alpine

ARG SERVER_ADDR
ENV SERVER_ADDR ${SERVER_ADDR}

COPY package*.json /client/
WORKDIR /client
RUN npm install

COPY . /client
WORKDIR /client

RUN npm run-script build

ENV HOST=0.0.0.0
CMD [ "npm", "run", "start" ]