FROM node:12-slim

WORKDIR /usr/src/app

COPY / ./
RUN npm install
RUN npm run build:css
RUN npm run build:sapper

EXPOSE 3000

CMD [ "npm", "start" ]
