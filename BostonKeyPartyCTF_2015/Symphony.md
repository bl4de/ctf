# Symphony
---

A less than four characters number, bigger than 999?Maybe the bug is elsewhere. : 25

## Source code

```
<html>
<head>
	<title>level2</title>
    <link rel='stylesheet' href='style.css' type='text/css'>
</head>
<body>

<?php
require 'flag.php';

if (isset($_GET['password'])) {
	if (is_numeric($_GET['password'])){
		if (strlen($_GET['password']) < 4){
			if ($_GET['password'] > 999)
				die('Flag: '.$flag);
			else
				print '<p class="alert">Too little</p>';
		} else
				print '<p class="alert">Too long</p>';
	} else
		print '<p class="alert">Password is not numeric</p>';
}
?>

<section class="login">
        <div class="title">
                <a href="./index.txt">Level 2</a>
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

We have to pass 3-digit number, but bigger than 999 :) Tricky.

But notice that is_numeric() allows exponential numbers (see )http://php.net/manual/en/function.is-numeric.php):


http://52.10.107.64:8002/?password=4e3

