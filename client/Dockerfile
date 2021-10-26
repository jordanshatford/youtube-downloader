FROM node:16-alpine

ARG VITE_SERVER_ADDR
ENV VITE_SERVER_ADDR ${VITE_SERVER_ADDR}

COPY package*.json /client/
WORKDIR /client
RUN npm install

COPY . /client
WORKDIR /client

RUN npm run-script build

ENV HOST=0.0.0.0
CMD [ "npm", "run", "preview" ]