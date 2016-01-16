<?php
	require("./functions.php");
?>
<?php
	
	$check = true;

	$result = 0;
	$title = "Forum - Registration";
	$user_info = array();

	if ($_SERVER['REQUEST_METHOD'] == 'POST') {
		if (!(isset($_POST['username']) && isset($_POST['email']) && isset($_POST['password']))) {
			exit();
		}
		$check = preg_match("/^[a-zA-Z0-9]+$/", $_POST['username']);
		if (!$check) {
		} elseif (username_exist($_POST['username'])) {
			$result = 1;
			$title = "Registration Failed";
		} else {
			add_user($_POST['username'], $_POST['email'], $_POST['password']);
			$user_info = get_user($_POST['username']);
			$result = 2;
			$title = "Registration Complete";
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

		<title><?php echo $title; ?>s</title>

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
	if ($result == 0) {
?>
			<form class="form-signin" method="POST">
				<h2 class="form-signin-heading">Please register</h2><?php echo (!$check)?"<h4>Username is not in correct format.</h4>":""; ?>
				<label for="username" class="sr-only">Username</label>
				<input type="text" name="username" id="username" class="form-control" placeholder="Username" required autofocus>
				<label for="email" class="sr-only">Email address</label>
        		<input type="email" name="email" id="email" class="form-control" placeholder="Email address" required>
				<label for="password" class="sr-only">Password</label>
				<input type="password" name="password" id="password" class="form-control" placeholder="Password" required>
				<button class="btn btn-lg btn-primary btn-block" type="submit">Register</button>
			</form>
<?php
	} elseif ($result == 1) {
?>
			<h1>Registration Failed!</h1>
			<h3>Username already exists.</h3>
<?php
	} elseif ($result == 2) {
?>
			<h1>Registration Complete!</h1>
			<h3>username: <?php echo $user_info[0]; ?></h3>
			<h3>password: <?php echo $user_info[1]; ?></h3>
			<h4>Your account will be activated later.</h4>
<?php
	}
?>
		</div> <!-- /container -->


		<!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
		<script src="http://getbootstrap.com/assets/js/ie10-viewport-bug-workaround.js"></script>
	</body>
</html>


