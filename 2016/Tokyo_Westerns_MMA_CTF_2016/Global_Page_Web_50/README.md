# Global Page (Web, 50pts)

## Problem

Welcome to TokyoWesterns' CTF!
url: http://globalpage.chal.ctf.westerns.tokyo/

## Solution

GlobalPage welcomes us with a very short list of available links:

![Global Page]
(1.png)

After clicking one of them , we've got a list of PHP warnings from _include()_ function:

![Warnings]
(2.png)

What's most interesting here, a lot of them starting from language identifiers, like _pl_, _pl-PL_, _en-US_ and similar.

The only place where those identifiers exist is _Accept-Language_ header in HTTP request:

```
GET /?page=ctf HTTP/1.1
Host: globalpage.chal.ctf.westerns.tokyo
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2827.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Referer: http://globalpage.chal.ctf.westerns.tokyo/
Accept-Encoding: gzip, deflate, sdch
Accept-Language: pl-PL,pl;q=0.8,en-US;q=0.6,en;q=0.4
Connection: close

```

It seemed that application uses them to display user content in valid language (eg. for me it was Polish) and this feature is vulnerable to **LFI** (Local File Include).

At this moment the right solution was obvious - find the file with the flag and then display it using LFI in Accept-Language header.

First problem was to find the right file. First I tried to include existing file (and getting no error from _include()_ proved that file exists):

```
Accept-Language: ../index
```

Then after some guessing I found this one:

```
Accept-Language: ../flag
```
It was _flag.php_ file saved in web root of the application.

As it was PHP file, server parsed it instead of displaying its content. To bypass this, I used _php://filter_ wrapper which allows to read files and return them as Base64:

http://php.net/manual/en/wrappers.php.php

Last problem I've faced with was to find the right way to build valid path to flag.php

Using existing _page_ parameter like 'ctf', I get an error:

```
<b>Warning</b>:  
include(ctf/php://filter/convert.base64-encode/resource=flag.php): failed to open stream: No such file or directory in 
<b>/var/www/globalpage/index.php</b> 
on line <b>41</b><br />
```

![Include error]
(3.png)

The solution was quite simple, but I've spent some time before I get it right.
Application put _page_ parameter from URL as directory name. So using _php:/_ as directory name allowed me to build valid _php://filter_ command:


![Flag]
(4.png)

The flag.php in Base64:

```
PD9waHAKJGZsYWcgPSAiVFdDVEZ7SV9mb3VuZF9zaW1wbGVfTEZJfSI7Cg==
```

And in plain text:

```
<?php
$flag = "TWCTF{I_found_simple_LFI}";
```


