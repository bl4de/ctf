<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST'){
?>
<html>
<head>
    <title>Lawn Care Simulator 2015</title>
    <script src="//code.jquery.com/jquery-1.11.3.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script> 
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
</head>
<body>
<?php
    require_once 'validate_pass.php';
    require_once 'flag.php';
    if (isset($_POST['password']) && isset($_POST['username'])) {
        $auth = validate($_POST['username'], $_POST['password']); 
        if ($auth){
            echo "<h1>" . $flag . "</h1>";
        }
        else {
            echo "<h1>Not Authorized</h1>";
        }
    }
    else {
        echo "<h1>You must supply a username and password</h1>";
    }
?>
</body>
</html>
<?php
}
else {
    header("Location: /index.html");
    die();
}
?>