<?php

session_start();

require "helpers.php";

if(! check_login())
    redirect($LOGIN_URL);

$id_type = $_SESSION['id_type'];
$id = $_SESSION['id'];

?>

<!DOCTYPE html>
<html>
<head>
    <title>Homepage</title>
</head>
<body style='background-color: #d6eaf8'>

<p style="float: right">
<a href='/logout.php'> Logout </a>
</p>
<p style="clear: both"></p>

<p style='height:30px; width:100%;'> </p>

<center>
    
<h2> Welcome User !! </h2>
<br><br>

<h3>
<?php
if($id_type === 'email') {
    echo "Email :- ".$id;
}
elseif ($id_type === 'team_name') 
{
    echo "Team Name :- ".$id ;
}
?>
</h3>
<br><br>

<h4>
Here's a random funny saying for you :) <br>
</h4>
<br><br>

<?php
    require "sayings.php";
    printf(get_random_saying());
    echo "<br><br>";
    if($id === 'admin' && $id_type === 'team_name')
        printf(output_flag());
?>

</center>

</body>
</html>
