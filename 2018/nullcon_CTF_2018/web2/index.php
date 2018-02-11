// diggit.py by @bl4de | 2fe7e986096174eaa215846ae64ea83409594840 content
<html>
    <head>
        <link rel="stylesheet" type="text/css" media="screen" href="style.css" />
    </head>
    <body>
    <form class="login" method="post">
    <h1 class="login-title">Login for flag</h1>
        <input name="user" id="user" type="text" class="login-input" placeholder="Username" autofocus>
        <input name="pass" id="pass" type="password" class="login-input" placeholder="Password">
        <input type="submit" value="Lets Go" class="login-button">


  <?php
error_reporting(0);
$FLAG = readfile('/var/flags/level1.txt');
if (!empty($_POST['user']) && !empty($_POST['pass'])) {
    if(checklogin($_POST['user'],$_POST['pass'])){
        echo "<font style=\"color:#FF0000\"><h3>The flag is: $FLAG</h3><br\></font\>";
    }else{
        echo "<br /><font style=\"color:#FF0000\">Invalid credentials! Please try again!<br\></font\>";
    }
}


function checklogin($u,$p)
{
    if (($u) === "passwordisinrockyou" && crc32($p) == "550274426"){ //
        return true;
        }
    }
?>
</form>

</body>
</html>
