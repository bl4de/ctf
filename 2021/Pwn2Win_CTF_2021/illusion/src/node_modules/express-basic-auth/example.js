const express = require('express')

var app = express()

const basicAuth = require('./index.js')

/**
* express-basic-auth
*
* Example server. Just run in the same folder:
*
* npm install express express-basic-auth
*
* and then run this file with node ('node example.js')
*
* You can send GET requests to localhost:8080/async , /custom, /challenge or /static
* and see how it refuses or accepts your request matching the basic auth settings.
*/

//TODO: Implement some form of automatic testing against the example server

//Requires basic auth with username 'Admin' and password 'secret1234'
var staticUserAuth = basicAuth({
    users: {
        'Admin': 'secret1234'
    },
    challenge: false
})

//Uses a custom (synchronous) authorizer function
var customAuthorizerAuth = basicAuth({
    authorizer: myAuthorizer
})

//Same, but sends a basic auth challenge header when authorization fails
var challengeAuth = basicAuth({
    authorizer: myAuthorizer,
    challenge: true
})

//Uses a custom asynchronous authorizer function
var asyncAuth = basicAuth({
    authorizer: myAsyncAuthorizer,
    authorizeAsync: true
})

//Uses a custom response body function
var customBodyAuth = basicAuth({
    users: { 'Foo': 'bar' },
    unauthorizedResponse: getUnauthorizedResponse
})

//Uses a static response body
var staticBodyAuth = basicAuth({
    unauthorizedResponse: 'Haaaaaha'
})

//Uses a JSON response body
var jsonBodyAuth = basicAuth({
    unauthorizedResponse: { foo: 'bar' }
})

//Uses a custom realm
var realmAuth = basicAuth({
    challenge: true,
    realm: 'test'
})

//Uses a custom realm function
var realmFunctionAuth = basicAuth({
    challenge: true,
    realm: function (req) {
        return 'bla'
    }
})

app.get('/static', staticUserAuth, function(req, res) {
    res.status(200).send('You passed')
})

app.get('/custom', customAuthorizerAuth, function(req, res) {
    res.status(200).send('You passed')
})

app.get('/challenge', challengeAuth, function(req, res) {
    res.status(200).send('You passed')
})

app.get('/async', asyncAuth, function(req, res) {
    res.status(200).send('You passed')
})

app.get('/custombody', customBodyAuth, function(req, res) {
    res.status(200).send('You passed')
})

app.get('/staticbody', staticBodyAuth, function(req, res) {
    res.status(200).send('You passed')
})

app.get('/jsonbody', jsonBodyAuth, function(req, res) {
    res.status(200).send('You passed')
})

app.get('/realm', realmAuth, function(req, res) {
    res.status(200).send('You passed')
})

app.get('/realmfunction', realmFunctionAuth, function(req, res) {
    res.status(200).send('You passed')
})

app.listen(8080, function() {
    console.log("Listening!")
})

//Custom authorizer checking if the username starts with 'A' and the password with 'secret'
function myAuthorizer(username, password) {
    return username.startsWith('A') && password.startsWith('secret')
}

//Same but asynchronous
function myAsyncAuthorizer(username, password, cb) {
    if(username.startsWith('A') && password.startsWith('secret'))
        return cb(null, true)
    else
        return cb(null, false)
}

function getUnauthorizedResponse(req) {
    return req.auth ? ('Credentials ' + req.auth.user + ':' + req.auth.password + ' rejected') : 'No credentials provided'
}
