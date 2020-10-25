const express = require('express');
const bodyParser = require('body-parser');
const compression = require('compression');
const redis = require('./redis');

const serverless = require('./serverless');

const BIND_ADDR = process.env.BIND_ADDR || '127.0.0.1';
const PORT = process.env.PORT || '3000';
const REDIS_HOST = process.env.REDIS_HOST || '127.0.0.1';
const REDIS_PORT = process.env.REDIS_PORT || '6379';

const app = express();
app.use(bodyParser.text());
app.use(compression());
app.use(express.static('./static'));

const redisClient = redis.createClient({
    host: REDIS_HOST,
    port: REDIS_PORT,
});
app.set('db', redisClient);

app.use('/demo', serverless);

app.listen(PORT, BIND_ADDR, () => {
    console.log(`FluxCloud Serverless listening on ${BIND_ADDR}:${PORT}`);
});
