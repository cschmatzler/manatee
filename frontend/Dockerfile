FROM node:12-slim

WORKDIR /usr/src/frontend
COPY /frontend/ /usr/src/frontend/

RUN npm install && \
    npm run build:css && \
    npm run build:sapper

EXPOSE 8080
CMD [ "npm", "start" ]
