const { Router } = require('express');
const { nanoid } = require('nanoid');
const { billed } = require('./billing');

const DEMO_TTL = parseInt(process.env.DEMO_TTL || '3600');
const DEMO_CREDITS = parseInt(process.env.DEMO_CREDITS || '1337');
const ACCOUNT_PRODUCTS = 'team-products';
const ACCOUNT_SECURITY = 'team-security';

// all invocations must be billed! $$$ Stonks $$$
const app = billed(ACCOUNT_PRODUCTS, 100, require('./functions/app'));
const waf = billed(ACCOUNT_SECURITY, 100, require('./functions/waf'));

const deploymentRouter = async (req, res, next) => {
    const deploymentId = req.params.deploymentId;
    if (typeof deploymentId !== 'string') {
        return res.status(400).send('deploymentId required!').end();
    }

    const db = req.app.get('db');
    const deploymentExists = await db.existsAsync(deploymentId);
    if (!deploymentExists) {
        return res.status(404).send('deployment not found!').end();
    }

    // load account balances
    const balances = await db.hgetallAsync(deploymentId);
    req.balances = {
        ...balances,
        async save() {
            // save account balances
            const multi = db.multi();
            for (const account in this) {
                if (typeof this[account] !== 'number') {
                    continue;
                }
                const balance = this[account];
                multi.hset(deploymentId, account, balance);
            }
            await multi.execAsync();
        },
    };

    next();
};

const router = Router();

// redirect to the actual / path, not the one of this router
router.get('/', (req, res) => res.redirect('/'));

// create a new demo deployment
router.post('/', async (req, res) => {
    const deploymentId = nanoid();

    // give demo credits
    const db = req.app.get('db');
    await db.multi()
            .hset(deploymentId, ACCOUNT_PRODUCTS, DEMO_CREDITS)
            .hset(deploymentId, ACCOUNT_SECURITY, DEMO_CREDITS)
            .expire(deploymentId, DEMO_TTL)
            .execAsync();

    // fake slow deployment :^)
    res.send(`
        <meta http-equiv="refresh" content="3; URL=/demo/${deploymentId}/">
        Deploying demo, please wait...
    `);
});

// forward request to deployment
router.use('/:deploymentId/', deploymentRouter, async (req, res, next) => {
    try {
        await waf(req, res, next);
        await app(req, res, next);
        res.end();
    } catch (e) {
        console.error('[Error]', `[${req.params.deploymentId}]`, e.message);
        res.status(500).send('rip');
    } finally {
        await req.balances.save();
    }
});

module.exports = router;
