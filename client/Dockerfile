FROM node:16-alpine

COPY package*.json /client/
WORKDIR /client
RUN npm install

COPY . /client
WORKDIR /client

RUN npm run-script build

EXPOSE 5000
ENV HOST=0.0.0.0
CMD [ "npm", "run", "start" ]