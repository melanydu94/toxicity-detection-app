FROM node:14

WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install

RUN npm i apexcharts

COPY . .

EXPOSE 80

CMD [ "npm", "start" ]