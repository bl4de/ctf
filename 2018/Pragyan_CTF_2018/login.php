<?php

session_start();

require "helpers.php";

$type = $_POST['id_type'];
$identifier = $_POST['identifier'];
$password = $_POST['password'];
$_SESSION['id'] = $identifier;

if($type === 'team_name') {
    $team_name = $identifier;
    $_SESSION['id_type'] = 'team_name';

    if(verify_teamname_password($team_name, $password) === true) {
        $_SESSION['logged_in'] = true;
        redirect('/homepage.php');
    }
    else {
        die("Invalid Team Name-Password combination !!");
    }
}
elseif ($type === 'email') {
    $email = $identifier;
    $_SESSION['id_type'] = 'email';

    if(verify_email_password($email, $password) === true) {
        $_SESSION['logged_in'] = true;
        redirect('/homepage.php');
    }
    else {
        die("Invalid Email-Password combination !!");
    }
}

?>
