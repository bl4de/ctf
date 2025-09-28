## HackerOne101 CTF

### Hackyholidays CTF

#### FLAG 1

https://2045c714ddf37d9fb7bc3dbbc22ddc24.ctf.hacker101.com/robots.txt

```
User-agent: *
Disallow: /s3cr3t-ar3a
Flag: ^FLAG^03d311a209e50461d26895691cb25ba4d6e98f98ef0d972aa22461f06fead55e$FLAG$
```

#### FLAG 2

https://2045c714ddf37d9fb7bc3dbbc22ddc24.ctf.hacker101.com/s3cr3t-ar3a/

jQuery (https://2045c714ddf37d9fb7bc3dbbc22ddc24.ctf.hacker101.com/assets/js/jquery.min.js) adds `data-info` with flag and `next-page` with path to next challenges to <div>:

```JavaScript
(...)
document.getElementById('alertbox').setAttribute('data-info', h1_1 + h1_2 + h1_3 + h1_1 + h3_0 + h3_1 + h3_2 + h3_3 + h3_4 + h3_5 + h3_6 + h3_7 + h3_8 + h3_9 + h3_10 + h3_11 + h3_12 + h1_4 + h1_2 + h1_3 + h1_4);
document.getElementById('alertbox').setAttribute('next-page', '/ap' + 'ps-' + 'h' + 'o' + 'me/');
(...)    
```

Result:

```html
<div class="alert alert-danger text-center" id="alertbox" 
data-info="^FLAG^8139549738bf3a9166922902cb26b2b8f66283e3b9cf8e3df19acdab5615f756$FLAG$" next-page="/apps-home/">
    <p>I've moved this page to keep people out!</p>
    <p>If you're allowed access you'll know where to look for the proper page!</p>
</div>
```


Starting point from here: https://6d7d1f7659a373c4de8b41398b20ec6d.ctf.hacker101.com/apps-home/


#### FLAG 3

Grinch People Rater:
https://6d7d1f7659a373c4de8b41398b20ec6d.ctf.hacker101.com/people-rater/


```
GET /people-rater/entry/?id=eyJpZCI6MX0= HTTP/2
Host: 2045c714ddf37d9fb7bc3dbbc22ddc24.ctf.hacker101.com
Pragma: no-cache
Cache-Control: no-cache
Sec-Ch-Ua-Platform: "macOS"
X-Requested-With: XMLHttpRequest
Accept-Language: pl-PL,pl;q=0.9
Accept: application/json, text/javascript, */*; q=0.01
Sec-Ch-Ua: "Not)A;Brand";v="8", "Chromium";v="138"
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36
Sec-Ch-Ua-Mobile: ?0
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://2045c714ddf37d9fb7bc3dbbc22ddc24.ctf.hacker101.com/people-rater/
Accept-Encoding: gzip, deflate, br
Priority: u=1, i
```

Response:

```
HTTP/2 200 OK
Date: Mon, 04 Aug 2025 21:19:19 GMT
Content-Type: application/json
Server: openresty/1.27.1.2

{"id":"eyJpZCI6MX0=","name":"The Grinch","rating":"Amazing in every possible way!","flag":"^FLAG^ac4214e9c905b1dd08f729ade7b7fde9d4c3be604c85743498703c3c756087ae$FLAG$"}
```

#### FLAG 4

Grinch Swag Shop
https://6d7d1f7659a373c4de8b41398b20ec6d.ctf.hacker101.com/swag-shop/




#### FLAG 5

Secure Login
https://6d7d1f7659a373c4de8b41398b20ec6d.ctf.hacker101.com/secure-login/



#### FLAG 6

#### FLAG 7

#### FLAG 8

#### FLAG 9

#### FLAG 10

#### FLAG 11

#### FLAG 12



