<?php
	require("./functions.php");
?>
<?php
	$login = false;

	if ($_SERVER['REQUEST_METHOD'] == 'POST') {
		if (!(isset($_POST['username']) && isset($_POST['password']))) {
			exit();
		}

		if(username_exist($_POST['username'])) {
			$user_info = get_user($_POST['username']);
			if ($user_info[1] == $_POST['password']) {
				$login = true;
			}
		}

	}

?>
<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="utf-8">
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
		<meta name="description" content="">
		<meta name="author" content="">
		<link rel="icon" href="http://getbootstrap.com/favicon.ico">

		<title>Signin Template for Bootstrap</title>

		<!-- Bootstrap core CSS -->
		<link href="http://getbootstrap.com/dist/css/bootstrap.min.css" rel="stylesheet">

		<!-- Custom styles for this template -->
		<link href="http://getbootstrap.com/examples/signin/signin.css" rel="stylesheet">

		<!-- Just for debugging purposes. Don't actually copy these 2 lines! -->
		<!--[if lt IE 9]><script src="../../assets/js/ie8-responsive-file-warning.js"></script><![endif]-->
		<script src="http://getbootstrap.com/assets/js/ie-emulation-modes-warning.js"></script>

		<!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
		<!--[if lt IE 9]>
		<script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
		<script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
		<![endif]-->
	</head>

	<body>
		<div class="container">
<?php
	if ($login) {
?>
		<div>
			<h1>Flag is <?php echo file_get_contents("../flag.txt"); ?></h1>
		</div>
<?php
	} else {
?>
		<form class="form-signin" method="POST">
			<h2 class="form-signin-heading">Please login</h2>
			<label for="username" class="sr-only">Username</label>
			<input type="text" name= "username" id="username" class="form-control" placeholder="Username" required autofocus>
			<label for="password" class="sr-only">Password</label>
			<input type="password" name="password" id="password" class="form-control" placeholder="Password" required>
			<button class="btn btn-lg btn-primary btn-block" type="submit">Login</button>
			<a href="register.php">Register</a>
		</form>
<?php
	}
?>
		</div>
		<!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
		<script src="http://getbootstrap.com/assets/js/ie10-viewport-bug-workaround.js"></script>
	</body>
</html>

