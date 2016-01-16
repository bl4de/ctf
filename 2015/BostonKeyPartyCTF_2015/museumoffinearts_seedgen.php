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
