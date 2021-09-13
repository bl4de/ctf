const should = require('should')
const express = require('express')
const supertest = require('supertest')

const basicAuth = require('./index.js')

var app = express()

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

//Uses a custom (synchronous) authorizer function
var customCompareAuth = basicAuth({
    authorizer: myComparingAuthorizer
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

app.get('/custom-compare', customCompareAuth, function(req, res) {
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

function myComparingAuthorizer(username, password) {
    return basicAuth.safeCompare(username, 'Testeroni') & basicAuth.safeCompare(password, 'testsecret')
}

function getUnauthorizedResponse(req) {
    return req.auth ? ('Credentials ' + req.auth.user + ':' + req.auth.password + ' rejected') : 'No credentials provided'
}

describe('express-basic-auth', function() {
    describe('safe compare', function() {
        const safeCompare = basicAuth.safeCompare

        it('should return false on different inputs', function() {
            (!!safeCompare('asdf', 'rftghe')).should.be.false()
        })

        it('should return false on prefix inputs', function() {
            (!!safeCompare('some', 'something')).should.be.false()
        })

        it('should return false on different inputs', function() {
            (!!safeCompare('anothersecret', 'anothersecret')).should.be.true()
        })
    })

    describe('static users', function() {
        const endpoint = '/static'

        it('should reject on missing header', function(done) {
            supertest(app)
                .get(endpoint)
                .expect(401, done)
        })

        it('should reject on wrong credentials', function(done) {
            supertest(app)
                .get(endpoint)
                .auth('dude', 'stuff')
                .expect(401, done)
        })

        it('should reject on shorter prefix', function(done) {
            supertest(app)
                .get(endpoint)
                .auth('Admin', 'secret')
                .expect(401, done)
        })

        it('should reject without challenge', function(done) {
            supertest(app)
                .get(endpoint)
                .auth('dude', 'stuff')
                .expect(function (res) {
                    if(res.headers['WWW-Authenticate'])
                        throw new Error('Response should not have a challenge')
                })
                .expect(401, done)
        })

        it('should accept correct credentials', function(done) {
            supertest(app)
                .get(endpoint)
                .auth('Admin', 'secret1234')
                .expect(200, 'You passed', done)
        })
    })

    describe('custom authorizer', function() {
        const endpoint = '/custom'

        it('should reject on missing header', function(done) {
            supertest(app)
                .get(endpoint)
                .expect(401, done)
        })

        it('should reject on wrong credentials', function(done) {
            supertest(app)
                .get(endpoint)
                .auth('dude', 'stuff')
                .expect(401, done)
        })

        it('should accept fitting credentials', function(done) {
            supertest(app)
                .get(endpoint)
                .auth('Aloha', 'secretverymuch')
                .expect(200, 'You passed', done)
        })

        describe('with safe compare', function() {
            const endpoint = '/custom-compare'
            
            it('should reject wrong credentials', function(done) {
                supertest(app)
                    .get(endpoint)
                    .auth('bla', 'blub')
                    .expect(401, done)
            })

            it('should reject prefix credentials', function(done) {
                supertest(app)
                    .get(endpoint)
                    .auth('Test', 'test')
                    .expect(401, done)
            })

            it('should accept fitting credentials', function(done) {
                supertest(app)
                    .get(endpoint)
                    .auth('Testeroni', 'testsecret')
                    .expect(200, 'You passed', done)
            })
        })
    })

    describe('async authorizer', function() {
        const endpoint = '/async'

        it('should reject on missing header', function(done) {
            supertest(app)
                .get(endpoint)
                .expect(401, done)
        })

        it('should reject on wrong credentials', function(done) {
            supertest(app)
                .get(endpoint)
                .auth('dude', 'stuff')
                .expect(401, done)
        })

        it('should accept fitting credentials', function(done) {
            supertest(app)
                .get(endpoint)
                .auth('Aererer', 'secretiveStuff')
                .expect(200, 'You passed', done)
        })
    })

    describe('custom response body', function() {
        it('should reject on missing header and generate resposne message', function(done) {
            supertest(app)
                .get('/custombody')
                .expect(401, 'No credentials provided', done)
        })

        it('should reject on wrong credentials and generate response message', function(done) {
            supertest(app)
                .get('/custombody')
                .auth('dude', 'stuff')
                .expect(401, 'Credentials dude:stuff rejected', done)
        })

        it('should accept fitting credentials', function(done) {
            supertest(app)
                .get('/custombody')
                .auth('Foo', 'bar')
                .expect(200, 'You passed', done)
        })

        it('should reject and send static custom resposne message', function(done) {
            supertest(app)
            .get('/staticbody')
            .expect(401, 'Haaaaaha', done)
        })

        it('should reject and send static custom json resposne message', function(done) {
            supertest(app)
            .get('/jsonbody')
            .expect(401, { foo: 'bar' }, done)
        })
    })

    describe('challenge', function() {
        it('should reject with blank challenge', function(done) {
            supertest(app)
                .get('/challenge')
                .expect('WWW-Authenticate', 'Basic')
                .expect(401, done)
        })

        it('should reject with custom realm challenge', function(done) {
            supertest(app)
                .get('/realm')
                .expect('WWW-Authenticate', 'Basic realm="test"')
                .expect(401, done)
        })

        it('should reject with custom generated realm challenge', function(done) {
            supertest(app)
                .get('/realmfunction')
                .expect('WWW-Authenticate', 'Basic realm="bla"')
                .expect(401, done)
        })
    })
})
