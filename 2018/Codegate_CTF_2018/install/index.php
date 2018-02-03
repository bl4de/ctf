<?php
	function rand_str($length = 10) {
	    $char_list = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
	    $_length = strlen($char_list);
	    $result = '';
	    for ($i = 0; $i < $length; $i++) {
	        $result .= $char_list[rand(0, $_length - 1)];
	    }
	    return $result;
	}
	if(is_dir('../data/')){
		if(is_file('../data/config.php')){
			die('already install');
		}
	}
	if(!is_writeable('../data') || !is_dir('../data')){
		die('plz check data directory');
	}
	if($_POST){
		$database = $_POST['database'];
		$mysql_host = $_POST['mysql_host'];
		$mysql_user = $_POST['mysql_user'];
		$mysql_password = $_POST['mysql_password'];

		$con = mysqli_connect($mysql_host, $mysql_user, $mysql_password, $database);

		if(!$con){
			die('connection error');
		}


		$sql = file_get_contents('simple_cms.sql');

		$sql = explode(';', $sql);

		$prefix = bin2hex(rand_str(10)) . '_';
		$blind_col = bin2hex(rand_str(10));
		for($i=0; $i<count($sql)-1; $i++){
			$query = trim($sql[$i]).';';
			$query = str_replace('{table_prefix}', $prefix, $query);
			$query = str_replace('{blind_column}', $blind_col, $query);
			$query = mysqli_query($con, $query);
			if(!$query){
				echo mysqli_error($con);
				echo "<br/>";
				die('mysql error!');
			}
		}

		$tmp=<<<EOF
<?php
	if(!defined('simple_cms')) exit();
	\$db_name = '$database';
	\$db_host = '$mysql_host';
	\$db_user = '$mysql_user';
	\$db_password = '$mysql_password';
	\$table_prefix = '$prefix';
?>
EOF;
		file_put_contents('../data/config.php', $tmp);
		exit('<script>alert("install!");location.href="../";</script>');
	}
	else{
		echo file_get_contents('install.tpl');
		exit;
	}
?>