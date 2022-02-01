FROM node:16-alpine

ARG VITE_SERVER_ADDR
ENV VITE_SERVER_ADDR ${VITE_SERVER_ADDR}

COPY package*.json /frontend/
WORKDIR /frontend
RUN npm install

COPY . /frontend
WORKDIR /frontend

RUN npm run-script build

EXPOSE 3000
CMD [ "npm", "run", "preview", "--", "--host" ]
