<html>
<head>
    <title>Lawn Care Simulator 2015 - premium</title>
    <script src="//code.jquery.com/jquery-1.11.3.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script> 
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
</head>
<body>
    <nav class="navbar navbar-inverse navbar-fixed-top">
      <div class="container">
        <div class="navbar-header">
          <a class="navbar-brand" href="index.html">Lawn Care Simulator 2015</a>
        </div>
        <div id="navbar" class="navbar-collapse collapse">
        </div>
      </div>
    </nav>
<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST'){
    require_once 'db.php';
    $link = mysql_connect($DB_HOST, $SQL_USER, $SQL_PASSWORD) or die('Could not connect: ' . mysql_error());
    mysql_select_db('users') or die("Mysql error");
    $user = mysql_real_escape_string($_POST['username']);
    // check to see if the username is available
    $query = "SELECT username FROM users WHERE username LIKE '$user';";
    $result = mysql_query($query) or die('Query failed: ' . mysql_error());
    $line = mysql_fetch_row($result, MYSQL_ASSOC);
    if ($line == NULL){
        // Signing up for premium is still in development
        echo '<h2 style="margin: 60px;">Lawn Care Simulator 2015 is currently in a private beta. Please check back later</h2>';
    }
    else {
        echo '<h2 style="margin: 60px;">Username: ' . $line['username'] . " is not available</h2>";
    }
}
else {
?>

    <div class="jumbotron">
      <div class="container">
        <h1>Join the Lawn Care Simulator Premium beta!</h1>
        <p>Premium features</p>
        <ul>
            <li>Different breeds of grass!</li>
            <li>Plant fertilizer for faster growth!</li>
            <li>Shrubberies!</li>
            <li>Flags!</li>
            <li>Lawn mowers!</li>
      </div>
    </div>


     <div class="container">
      <h3>Sign up for premium!</h3>
      <form id='submit_form' class="form-signin" action='sign_up.php' method='post'>
        <label for="username" class="sr-only">Username</label>
        <input type="text" id="username" name="username" class="form-control" placeholder=" Your username" required autofocus>
        <label for="password" class="sr-only">Password</label>
        <input type="password" id="password" name="password" class="form-control" placeholder="password" required>
        <input type="hidden" id="version_hash" value="">
        <button class="btn btn-lg btn-primary btn-block" type="submit">Sign up!</button>
      </form>

    </div> <!-- /container --> 
<?php
}
?>
    
    <div class='container'>
    <footer>
        <p>&copy; 2014 &nbsp | &nbsp <a href='sign_up.php'>Sign Up For Lawn Care Simulator Premium</a> | &nbsp <a href='jobs.html'>Careers</a>&nbsp</p>
      </footer>
    </div> <!-- /container -->
    
</body>
</html>

