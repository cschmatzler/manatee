FROM node:12-slim

COPY . /

RUN npm install && \
    npm run build:css && \
    npm run build:sapper

EXPOSE 8080
CMD [ "npm", "start" ]
