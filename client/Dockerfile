FROM node:14

WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install

RUN npm install axios@0.24.0

RUN npm i apexcharts

COPY . .

EXPOSE 3000

CMD [ "npm", "start" ]