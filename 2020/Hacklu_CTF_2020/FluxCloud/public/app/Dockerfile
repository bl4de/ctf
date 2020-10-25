FROM node:14-alpine

# prepare dependencies
WORKDIR /app
ADD package.json package-lock.json /app/
RUN npm install

# add the rest of the app
ADD . /app

USER 1000
ENV BIND_ADDR=0.0.0.0 PORT=8080

CMD [ "node", "index.js" ]
