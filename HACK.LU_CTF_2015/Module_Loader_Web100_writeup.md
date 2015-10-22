# Hack.lu CTF 2015 - Module Loader (Web, 100pts)

## Problem

100 Points by lucebac (Web)

Since his students never know what date it is and how much time they have until the next homework's deadline, Mr P. H. Porter wrote a little webapp for that.


## Solution

We get simple web application with two available options:

![Welcome screen]
(https://github.com/bl4de/ctf/blob/master/HACK.LU_CTF_2015/Module_Loader_web100/Module_Loader1.png)

After quick research there's an obvious LFI (Local File Include)

![LFI]
(https://github.com/bl4de/ctf/blob/master/HACK.LU_CTF_2015/Module_Loader_web100/Module_Loader2.png)


It looks like we can see any file we want to as they are just printed out, here's source code of date module:

```php
<?php 
if (isset($_GET['time']))
    $tmp = explode("-", $_GET['time']);
else
    $tmp = array(1970, 1, 1);
$y = (int)$tmp[0];
$m = (int)$tmp[1];
$d = (int)$tmp[2];

var_dump($y);
var_dump($m);
var_dump($d);
?>
<div id="clock"></div>
<!-- <script src="countdown.js"></script> -->
<script>
var clock = document.getElementById("clock");
var now = new Date();
clock.innerHTML = countdown(new Date(<?= $y; ?>, <?= $m; ?>, <?= $d; ?>)).toString();
setInterval(function(){clock.innerHTML = countdown(new Date(<?= $y; ?>, <?= $m; ?>, <?= $d ?>)).toString();}, 1000);
</script>

```

Also, we can display .htaccess, which contains some directory with quite "obvious" name :P


<!--
# seems to be not working, though
#<Directory "3cdcf3c63dc02f8e5c230943d9f1f4d75a4d88ae">
#    Options -Indexes
#</Directory>
# -->

Let's take a look there and here we go:

![3cdcf3c63dc02f8e5c230943d9f1f4d75a4d88ae content]
(https://github.com/bl4de/ctf/blob/master/HACK.LU_CTF_2015/Module_Loader_web100/Module_Loader3.png)


Last thing is to use LFI and see, what's in flag.php file:

![Flag]
(https://github.com/bl4de/ctf/blob/master/HACK.LU_CTF_2015/Module_Loader_web100/Module_Loader4.png)


school.fluxfingers.net:1522/?module=../3cdcf3c63dc02f8e5c230943d9f1f4d75a4d88ae/flag.php


flag{hidden_is_not_actually_hidden}
