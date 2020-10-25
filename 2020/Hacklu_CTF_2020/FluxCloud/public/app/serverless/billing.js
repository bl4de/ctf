exports.billed = (account, cost, handler) => async (req, res, next) => {
    // charge invocation cost
    req.balances[account] -= cost;
    if (req.balances[account] < 0) {
        console.log('[Billing]', `[${req.params.deploymentId}]`, `${account} does not have enough credits to invoke ${handler.name}`);
        return res.status(402).set('X-Billing-Account', account);
    }
    console.log('[Billing]', `[${req.params.deploymentId}]`, `${account} has ${req.balances[account]} credits left!`);

    // execute the function
    await handler(req, res, next);
};
