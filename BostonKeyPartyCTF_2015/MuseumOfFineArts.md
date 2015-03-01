# Museum of Fine Arts
---
Because cryptography is hard, we only implemented a hand-made PRNG. What could possibly go wrong? : 25

## Source code

Script generates sequence of four numbers on every login attempt. There are only three displayed, fourth is the password (see museumoffinearts.png)

```
<html>
<head>
	<title>level4</title>
    <link rel='stylesheet' href='style.css' type='text/css'>
</head>
<body>

<?php
session_start(); 

// require 'flag.php';

if (isset ($_GET['password'])) {
    if ($_GET['password'] == $_SESSION['password'])
        die ('Flag: '.$flag);
    else
        print '<p class="alert">Wrong guess.</p>';
}

// Unpredictable seed
$seed = (microtime() ^ rand(1, 10000)) % rand(1, 10000) + rand(1, 10000);
mt_srand($seed);
?>

<section class="login">
        <div class="title">
                <a href="./index.txt">Level 4</a>
        </div>

		<ul class="list">
		<?php
		for ($i=0; $i<3; $i++)
			print '<li>' . mt_rand (0, 0xffffff) . '</li>';
		$_SESSION['password'] = mt_rand (0, 0xffffff);
		?>
		</ul>

        <form method="get">
                <input type="text" required name="password" placeholder="Next number" /><br/>
                <input type="submit"/>
        </form>
</section>
</body>
</html>
```

## Solution

"Unpredictable seed" has only 5 digits, so it's possible to create simple "brute force" script to generate every combination of seed + four generated random numbers:

```

<?php

// $seed is 5-digit number (99999 possibilities)
//$seed = (microtime() ^ rand(1, 10000)) % rand(1, 10000) + rand(1, 10000);

$pass = $_GET['pass'];
$found = false;

for ($seed = 0; $seed <= 99999; $seed++) {
	mt_srand($seed);
	$found = false;
	for($i = 0; $i < 3; $i++) {
		$seq = mt_rand(0, 0xffffff);
		//found in sequence!
		if ($pass == $seq) {
			echo "Found!";
			$found = true;
		}
	}

	if ($found) {
		echo "<br /><strong>next: " . mt_rand (0, 0xffffff) . "</strong><hr />";
	}
}
```

When login page displays login form, we can use any of displayed number to find proper sequence and use 4th number to log in.

