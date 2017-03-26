# Rock With The Shark (Misc, 70pts)

---

## Problem

The shark won't bite you. Don't worry, it's wired!

## Solution

We get _pcap_ file with some HTTP transmission. Using Wireshark we can extract _flag.zip_ file, which is secured by password.

When we take a look closer at one of HTTP request and response, we find HTTP Basic Authorization header:

```
GET /flag.zip HTTP/1.1
Host: 192.168.1.41:8080
Connection: keep-alive
Authorization: Basic ZmxhZzphenVsY3JlbWE=
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36
DNT: 1
Referer: http://192.168.1.41:8080/
Accept-Encoding: gzip, deflate, sdch
Accept-Language: en-US,en;q=0.8,ht;q=0.6

HTTP/1.0 200 OK
Server: servefile/0.4.4 Python/2.7.10
Date: Fri, 13 Nov 2015 18:41:09 GMT
Content-Length: 222
Connection: close
Last-Modified: Fri, 13 Nov 2015 18:41:09 GMT
Content-Type: application/octet-stream
Content-Disposition: attachment; filename="flag.zip"
Content-Transfer-Encoding: binary

PK..
.....x.mG....(...........flag.txtUT	...-FV.-FVux..............;......q.........9.....H.!...	>B.....+:PK......(.......PK....
.....x.mG....(.........................flag.txtUT....-FVux.............PK..........N...z.....

```

Base64-encoded credentials (ZmxhZzphenVsY3JlbWE=) are _flag:azulcrema_
Password is valid for _flag.zip_ and we can get _flag.txt_ file with the flag:

```
IW{HTTP_BASIC_AUTH_IS_EASY}
