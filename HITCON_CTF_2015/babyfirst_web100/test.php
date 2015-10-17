<?php
	

$args = $_GET['args'];
var_dump($args);
for ( $i=0; $i<count($args); $i++ ){
	echo $args[$i];
    if ( !preg_match('/^\w+$/', $args[$i]) )
		echo "fail";
        exit();
}
var_dump(implode(" ", $args));
?>