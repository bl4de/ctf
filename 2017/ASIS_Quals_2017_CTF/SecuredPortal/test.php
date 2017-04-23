<?php
class Test {
	
		public function __construct() {
		
				$sessionString = array(
				"login" => "715221491694709",
				"logged" => true,
				);
				$payload = serialize($sessionString);
		
				var_dump($this->__sessionKey);
				$realSign = md5($payload.$this->__sessionKey);
		
				var_dump($realSign);
		
	}
	
}

$t = new Test();

// $realSign = "abcdef";
// $signature = 00000000000000000000000000000000;

// echo ($realSign == $signature) ? "\n\ntrue\n\n" : "\n\nfalse\n\n";

// while(1) {
	
// 	$sessionString = array(
// 	    "login" => rand(0,100000) . time(),
// 	    "logged" => true,
// 	);
// 	$payload = serialize($sessionString);
// 	$signature = md5($payload);
// 	echo $signature . "\n";

// 	if (substr($signature,0,3) === "0e1") {
// 		var_dump($sessionString);
// 		var_dump($signature);
// 		break;
// 	}
// }


echo md5("some".NULL) . "\n";
echo md5("some");