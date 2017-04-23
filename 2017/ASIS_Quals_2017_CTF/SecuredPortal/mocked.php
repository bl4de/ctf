<?php
// ini_set('display_errors', 0);

$sessionString = array(
    "login" => "715221491694709",
    "logged" => true,
);

$payload = serialize($sessionString);

echo "\n\n" . $payload  . "\n\n";
$signature = md5($payload);

$payload = base64_encode($payload);
echo "\n\n PAYLOAD (encoded): " . $payload . "\n\n";

$sessionString = $payload.$signature;

echo "\n\n" . "sessionString: " . $sessionString . "\n\n";

// read in panel class
$signature = substr($sessionString, -32);
$payload = base64_decode(substr($sessionString, 0, -32));
echo "\n\n PAYLOAD (decoded): " . $payload . "\n\n";

$realSign = md5($payload.NULL);


echo "signature (read): " . $signature . "\n";
echo "realSign (read): " . substr($realSign,0,6). "\n\n";

echo ($realSign == $signature)? 'TRUE'."\n" : 'FALSE'."\n";


if(strlen($sessionString) > 32){
	$signature = substr($sessionString, -32);
	$payload = base64_decode(substr($sessionString, 0, -32));
	
	$realSign = md5($payload.NULL);
	
	
	// 	if(__MAINTENANCE__===true)
		            // 	$realSign = substr($realSign, 0, 6);
	
	
	if($realSign == $signature){
		$data = unserialize($payload);
		
		if(is_array($data)){
			
			if($data['logged']===true){
				$__auth = true;
				echo "LOGGED!";
			}
		}
	}
}
