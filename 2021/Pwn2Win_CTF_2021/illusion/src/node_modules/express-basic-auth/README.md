# express-basic-auth

[![npm version](https://badge.fury.io/js/express-basic-auth.svg)](https://badge.fury.io/js/express-basic-auth)
[![npm](https://img.shields.io/npm/dm/express-basic-auth.svg)]()
[![CircleCI](https://circleci.com/gh/LionC/express-basic-auth/tree/master.svg?style=shield&circle-token=74f7b1557100b45259e67d2492c263e4f99365d4)](https://circleci.com/gh/LionC/express-basic-auth/tree/master)
[![David](https://img.shields.io/david/strongloop/express.svg)]()
![TypeScript compatible](https://img.shields.io/badge/typescript-compatible-brightgreen.svg)
[![MIT Licence](https://badges.frapsoft.com/os/mit/mit.svg?v=103)](https://opensource.org/licenses/mit-license.php)

Simple plug & play HTTP basic auth middleware for Express.

## How to install

Just run

```shell
npm install express-basic-auth
```

## How to use

The module will export a function, that you can call with an options object to
get the middleware:

```js
const app = require('express')()
const basicAuth = require('express-basic-auth')

app.use(basicAuth({
    users: { 'admin': 'supersecret' }
}))
```

The middleware will now check incoming requests to match the credentials
`admin:supersecret`.

The middleware will check incoming requests for a basic auth (`Authorization`)
header, parse it and check if the credentials are legit. If there are any
credentials, an `auth` property will be added to the request, containing
an object with `user` and `password` properties, filled with the credentials,
no matter if they are legit or not.

**If a request is found to not be authorized**, it will respond with HTTP 401
and a configurable body (default empty).

### Static Users

If you simply want to check basic auth against one or multiple static credentials,
you can pass those credentials in the `users` option:

```js
app.use(basicAuth({
    users: {
        'admin': 'supersecret',
        'adam': 'password1234',
        'eve': 'asdfghjkl',
    }
}))
```

The middleware will check incoming requests to have a basic auth header matching
one of the three passed credentials.

### Custom authorization

Alternatively, you can pass your own `authorizer` function, to check the credentials
however you want. It will be called with a username and password and is expected to
return `true` or `false` to indicate that the credentials were approved or not.

When using your own `authorizer`, make sure **not to use standard string comparison (`==` / `===`)**
when comparing user input with secret credentials, as that would make you vulnerable against
[timing attacks](https://en.wikipedia.org/wiki/Timing_attack). Use the provided `safeCompare`
function instead - always provide the user input as its first argument. Also make sure to use bitwise
logic operators (`|` and `&`) instead of the standard ones (`||` and `&&`) for the same reason, as
the standard ones use shortcuts.

```js
app.use(basicAuth( { authorizer: myAuthorizer } ))

function myAuthorizer(username, password) {
    const userMatches = basicAuth.safeCompare(username, 'customuser')
    const passwordMatches = basicAuth.safeCompare(password, 'custompassword')

    return userMatches & passwordMatches
}
```

This will authorize all requests with the credentials 'customuser:custompassword'.
In an actual application you would likely look up some data instead ;-) You can do whatever you
want in custom authorizers, just return `true` or `false` in the end and stay aware of timing
attacks.

### Custom Async Authorization

Note that the `authorizer` function above is expected to be synchronous. This is
the default behavior, you can pass `authorizeAsync: true` in the options object to indicate
that your authorizer is asynchronous. In this case it will be passed a callback
as the third parameter, which is expected to be called by standard node convention
with an error and a boolean to indicate if the credentials have been approved or not.
Let's look at the same authorizer again, but this time asynchronous:

```js
app.use(basicAuth({
    authorizer: myAsyncAuthorizer,
    authorizeAsync: true,
}))

function myAsyncAuthorizer(username, password, cb) {
    if (username.startsWith('A') & password.startsWith('secret'))
        return cb(null, true)
    else
        return cb(null, false)
}
```

### Unauthorized Response Body

Per default, the response body for unauthorized responses will be empty. It can
be configured using the `unauthorizedResponse` option. You can either pass a
static response or a function that gets passed the express request object and is
expected to return the response body. If the response body is a string, it will
be used as-is, otherwise it will be sent as JSON:

```js
app.use(basicAuth({
    users: { 'Foo': 'bar' },
    unauthorizedResponse: getUnauthorizedResponse
}))

function getUnauthorizedResponse(req) {
    return req.auth
        ? ('Credentials ' + req.auth.user + ':' + req.auth.password + ' rejected')
        : 'No credentials provided'
}
```

### Challenge

Per default the middleware will not add a `WWW-Authenticate` challenge header to
responses of unauthorized requests. You can enable that by adding `challenge: true`
to the options object. This will cause most browsers to show a popup to enter
credentials on unauthorized responses. You can set the realm (the realm
identifies the system to authenticate against and can be used by clients to save
credentials) of the challenge by passing a static string or a function that gets
passed the request object and is expected to return the challenge:

```js
app.use(basicAuth({
    users: { 'someuser': 'somepassword' },
    challenge: true,
    realm: 'Imb4T3st4pp',
}))
```

## Try it

The repository contains an `example.js` that you can run to play around and try
the middleware. To use it just put it somewhere (or leave it where it is), run

```shell
npm install express express-basic-auth
node example.js
```

This will start a small express server listening at port 8080. Just look at the file,
try out the requests and play around with the options.

## TypeScript usage

A declaration file is bundled with the library. You don't have to install a `@types/` package.

```typescript
import * as basicAuth from 'express-basic-auth'
```

:bulb: **Using `req.auth`**

express-basic-auth sets `req.auth` to an object containing the authorized credentials like `{ user: 'admin', password: 'supersecret' }`.

In order to use that `req.auth` property in TypeScript without an unknown property error, use covariance to downcast the request type:

```typescript
app.use(basicAuth(options), (req: basicAuth.IBasicAuthedRequest, res, next) => {
    res.end(`Welcome ${req.auth.user} (your password is ${req.auth.password})`)
    next()
})
```

:bulb: **A note about type inference on synchronous authorizers**

Due to some TypeScript's type-system limitation, the arguments' type of the synchronous authorizers are not inferred.
For example, on an asynchronous authorizer, the three arguments are correctly inferred:

```typescript
basicAuth({
    authorizeAsync: true,
    authorizer: (user, password, authorize) => authorize(null, password == 'secret'),
})
```

However, on a synchronous authorizer, you'll have to type the arguments yourself:

```typescript
basicAuth({
    authorizer: (user: string, password: string) => (password == 'secret')
})
```

## Tests

The cases in the `example.js` are also used for automated testing. So if you want  
to contribute or just make sure that the package still works, simply run:

```shell
npm test
```
