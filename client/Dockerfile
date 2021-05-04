FROM node:14-alpine

COPY . /app
WORKDIR /app

RUN npm install
RUN npm run-script build

EXPOSE 5000

ENV HOST=0.0.0.0

CMD [ "npm", "run", "start" ]