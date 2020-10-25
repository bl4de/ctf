/**
 * A demo application.
 */

const express = require('express');
const morgan = require('morgan');

const FLAG = process.env.FLAG || 'fakeflag{}';

const router = express.Router();
router.use(morgan('dev'));

router.get('/', (req, res) => {
    res.send('<code><h1>Hello World!</h1><p>Your FluxCloud Serverless deployment works!<p>And it is unhackable™ :)').end();
});

router.get('/flag', (req, res) => {
    res.send(FLAG).end();
});

router.get('/blocked', (req, res) => {
    res.send('<body style="margin:0"><img style="width:100%;height:100%" alt="wait. thats illegal." src="https://i.kym-cdn.com/entries/icons/original/000/028/207/Screen_Shot_2019-01-17_at_4.22.43_PM.jpg"/></body>').end();
});

// wrap in named function for better logging
module.exports = function app(...args) {
    return router(...args);
};
