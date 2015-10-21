<?php 
if (isset($_GET['time']))
    $tmp = explode("-", $_GET['time']);
else
    $tmp = array(1970, 1, 1);
$y = (int)$tmp[0];
$m = (int)$tmp[1];
$d = (int)$tmp[2];

var_dump($y);
var_dump($m);
var_dump($d);
?>
<div id="clock"></div>
<!-- <script src="countdown.js"></script> -->
<script>
var clock = document.getElementById("clock");
var now = new Date();
clock.innerHTML = countdown(new Date(<?= $y; ?>, <?= $m; ?>, <?= $d; ?>)).toString();
setInterval(function(){clock.innerHTML = countdown(new Date(<?= $y; ?>, <?= $m; ?>, <?= $d ?>)).toString();}, 1000);
</script>
