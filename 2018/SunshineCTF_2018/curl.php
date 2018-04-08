<?php

$ch = curl_init("http://www.example.com/\0");
$fp = fopen("example_homepage.txt", "w");

curl_setopt($ch, CURLOPT_FILE, $fp);
curl_setopt($ch, CURLOPT_HEADER, 0);
echo $fp;

curl_exec($ch);
curl_close($ch);
fclose($fp);
?>