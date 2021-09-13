/// <reference types="express" />

import { Request, RequestHandler } from 'express'

/**
 * This is the middleware builder.
 *
 * Example:
 *     const users = { alice: '1234', bob: 'correcthorsebatterystaple' }
 *     app.use(basicAuth({ users, challenge: true }), myHandler)
 *
 * @param options The middleware's options (at least 'users' or 'authorizer' are mandatory).
 */
declare function expressBasicAuth(options: expressBasicAuth.BasicAuthMiddlewareOptions): RequestHandler

declare namespace expressBasicAuth {
    /**
     * Time safe string comparison function to protect against timing attacks.
     * 
     * It is important to provide the arguments in the correct order, as the runtime
     * depends only on the `userInput` argument. Switching the order would expose the `secret`
     * to timing attacks.
     * 
     * @param userInput The user input to be compared
     * @param secret The secret value the user input should be compared with
     * 
     * @returns true if `userInput` matches `secret`, false if not
     */
    export function safeCompare(userInput: string, secret: string): boolean

    /**
     * The configuration you pass to the middleware can take three forms, either:
     *  - A map of static users ({ bob: 'pa$$w0rd', ... }) ;
     *  - An authorizer function
     *  - An asynchronous authorizer function
     */
    export type BasicAuthMiddlewareOptions = IUsersOptions | (IAuthorizerOptions | IAsyncAuthorizerOptions)

    /**
     * express-basic-auth patches the request object to set an `auth` property that lets you retrieve the authed user.
     *
     * Example (TypeScript):
     *     app.use(basicAuth({ ... }), (req: basicAuth.IBasicAuthedRequest, res, next) => {
     *         res.end(`Welcome ${req.auth.user} (your password is ${req.auth.password})`)
     *         next()
     *     })
     */
    export interface IBasicAuthedRequest extends Request {
        auth: { user: string, password: string }
    }

    type Authorizer = (username: string, password: string) => boolean

    type AsyncAuthorizerCallback = (err: any, authed?: boolean) => void

    type AsyncAuthorizer = (username: string, password: string, callback: AsyncAuthorizerCallback) => void

    type ValueOrFunction<T> = T | ((req: IBasicAuthedRequest) => T)

    interface IBaseOptions {
        /**
         * Per default the middleware will not add a WWW-Authenticate challenge header to responses of unauthorized requests.
         * You can enable that by setting this to true, causing most browsers to show a popup to enter credentials
         * on unauthorized responses.
         *
         * @default false
         */
        challenge?: boolean

        /**
         * You can set the realm (the realm identifies the system to authenticate against and can be used by clients to
         * save credentials) of the challenge by passing a string or a function that gets passed the request and is
         * expected to return the realm.
         *
         * @default undefined
         */
        realm?: ValueOrFunction<string>

        /**
         * Per default, the response body for unauthorized responses will be empty.
         * It can be configured using the unauthorizedResponse option. You can either pass a static response or a
         * function that gets passed the express request object and is expected to return the response body.
         * If the response body is a string, it will be used as-is, otherwise it will be sent as JSON.
         *
         * @default ''
         */
        unauthorizedResponse?: ValueOrFunction<any>
    }

    interface IUsersOptions extends IBaseOptions {
        /**
         * If you simply want to check basic auth against one or multiple static credentials, you can pass those
         * credentials in the users option.
         *
         * Example:
         *     const users = { alice: '1234', bob: 'correcthorsebatterystaple' }
         *     app.use(basicAuth({ users, challenge: true }), myHandler)
         */
        users: { [username: string]: string }
    }

    interface IAuthorizerOptions extends IBaseOptions {
        /**
         * Set to true if your authorizer is asynchronous.
         */
        authorizeAsync?: false

        /**
         * You can pass your own authorizer function, to check the credentials however you want.
         * It will be called with a username and password and is expected to return true or false to indicate that the
         * credentials were approved or not:
         *
         * Example:
         *     app.use(basicAuth({ authorizer }))
         *
         *     function myAuthorizer(username: string, password: string) {
         *         return username.startsWith('A') && password.startsWith('secret');
         *     }
         *
         * This will authorize all requests with credentials where the username begins with 'A' and the password begins
         * with 'secret'. In an actual application you would likely look up some data instead ;-)
         */
        authorizer: Authorizer
    }

    interface IAsyncAuthorizerOptions extends IBaseOptions {
        /**
         * Set it to true to use a asynchronous authorizer.
         */
        authorizeAsync: true

        /**
         * You can pass an asynchronous authorizer. It will be passed a callback as the third parameter, which is
         * expected to be called by standard node convention with an error and a boolean to indicate if the credentials
         * have been approved or not.
         *
         * Example:
         *     app.use(basicAuth({ authorizer, authorizeAsync: true }));
         *
         *     function authorizer(username, password, authorize) {
         *         if(username.startsWith('A') && password.startsWith('secret'))
         *             return authorize(null, true)
         *         
         *         return authorize(null, false)
         *     }
         */
        authorizer: AsyncAuthorizer
    }
}

export = expressBasicAuth
