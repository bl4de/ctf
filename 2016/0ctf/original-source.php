<?php
// include('config.php');
session_start();

if($_SESSION['time'] && time() - $_SESSION['time'] > 60) {
    session_destroy();
    die('timeout');
} else {
    $_SESSION['time'] = time();
}

echo rand();
if (isset($_GET['go'])) {
    $_SESSION['rand'] = array();
    $i = 5;
    $d = '';
    while($i--){
        $r = (string)rand();
        $_SESSION['rand'][] = $r;
        $d .= $r;
    }
    echo md5($d);
} else if (isset($_GET['check'])) {
	var_dump($_SESSION['rand']);
	var_dump($_GET['check']);
    if ($_GET['check'] === $_SESSION['rand']) {
        echo $flag;
    } else {
        echo 'die';
        session_destroy();
    }
} else {
    show_source(__FILE__);
}