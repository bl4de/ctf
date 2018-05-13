<?php

include 'common.php';

if ($_SERVER['REQUEST_METHOD'] === 'GET') {
    print highlight_string(file_get_contents("execute.php"), TRUE);
    exit(0);
}

$keys = get_keys();
$privkey = $keys[0];
$pubkey = $keys[1];

$file_info = $_FILES['userfile'];
check_uploaded_file($file_info);

$data = file_get_contents($file_info['tmp_name']);
$signature = hex2bin($_POST['signature']);
if (openssl_verify($data, $signature, $pubkey)) {
    print 'Signature is OK.<br/>';
} else {
    die('Bad signature.');
}

$text = pdf_to_text($file_info['tmp_name']);
print "Text: \"$text\"<br/>";

$execute_query = "EXECUTE ";
$echo_query = "ECHO ";
if (substr($text, 0, strlen($execute_query)) === $execute_query) {
    $payload = substr($text, strlen($execute_query));
    print "About to execute: \"$payload\".<br/>";
    $out = shell_exec($payload);
    print "Output: $out";
} else if (substr($text, 0, strlen($echo_query)) === $echo_query) {
    $payload = substr($text, strlen($echo_query));
    print "About to echo: \"$payload\".<br/>";
    echo $payload;
} else {
    print "I can't recognize the command type. Go away.<br/>";
}

?>