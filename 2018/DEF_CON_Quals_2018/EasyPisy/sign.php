<?php

include 'common.php';

if ($_SERVER['REQUEST_METHOD'] === 'GET') {
    print highlight_string(file_get_contents("sign.php"), TRUE);
    exit(0);
}

$keys = get_keys();
$privkey = $keys[0];
$pubkey = $keys[1];

if ($privkey === FALSE || $pubkey === FALSE) {
    die("Could not load keys. Contact admin.<br/>");
}

$file_info = $_FILES['userfile'];
check_uploaded_file($file_info);

$text = pdf_to_text($file_info['tmp_name']);
print "Extracted text: \"$text\"<br/>";

$execute_query = "EXECUTE ";
$echo_query = "ECHO ";
if (substr($text, 0, strlen($execute_query)) === $execute_query) {
    print "I don't sign EXECUTE commands. Go away.<br/>";
} else if (substr($text, 0, strlen($echo_query)) === $echo_query) {
    print "I'm OK with ECHO commands. Here is the signature: <br/>";
    $data = file_get_contents($file_info['tmp_name']);
    openssl_sign($data, $signature, $privkey);
    print bin2hex($signature);
} else {
    print "I can't recognize the command type. Go away.<br/>";
}

?>