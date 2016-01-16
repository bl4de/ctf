# Northeastern Univ.
---

Of course, a timing attack might be the answer, but Im quite sure that you can do better than that. : 25


## Source code

```
<html>
<head>
	<title>level3</title>
    <link rel='stylesheet' href='style.css' type='text/css'>
</head>
<body>

<?php
require 'flag.php';

if (isset($_GET['password'])) {
    if (strcmp($_GET['password'], $flag) == 0)
		die('Flag: '.$flag);
    else
		print '<p class="alert">Invalid password.</p>';
}
?>

<section class="login">
        <div class="title">
                <a href="./index.txt">Level 3</a>
        </div>

        <form method="get">
                <input type="text" required name="password" placeholder="Password" /><br/>
                <input type="submit"/>
        </form>
</section>
</body>
</html>
```

## Solution

If you are Wizard, you can simply guess the password :) 

Because I'm not, I've passed password $_GET varialble as array and strcmp() failed and returned false ( false == 0 is 'true', so we can see the flag)

```
http://52.10.107.64:8003/?password[]=aaa
```
