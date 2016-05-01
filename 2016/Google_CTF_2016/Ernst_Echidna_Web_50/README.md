# Ernst Echidna (Web, 50pts)

## Problem

Can you hack (url provided) website? The robots.txt sure looks interesting.

## Solution


We've got simple web page, which allows us to register an account:

![Ernst Echidna]
(assets/1.png)

Register form:

![Ernst Echidna]
(assets/2.png)

_robots.txt_ reveals one hidden path:

```
Disallow: /admin
```

At above url there's hidden administration panel and we need to has administration rights to access it.

After successful registration a cookie with MD5 hash of our login is set:

![Ernst Echidna]
(assets/3.png)

Simple change cookie content to MD5('admin') and refreshing browser tab allows to access panel:

![Ernst Echidna]
(assets/4.png)


...and reveals the flag:

![Ernst Echidna]
(assets/5.png)
