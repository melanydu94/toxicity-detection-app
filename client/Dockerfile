FROM node:14

WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install

RUN npm i react-advanced-gauge-chart

RUN npm install axios@0.24.0

COPY . .

EXPOSE 80

CMD [ "npm", "start" ]