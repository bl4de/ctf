<?php
	function username_exist($username) {
		$data = file_get_contents('../users.dat');
		$users = explode("\n", $data);
		foreach ($users as $key => $value) {
			$user_data = explode(",", $value);
			if ($user_data[2] == '1' && base64_encode($username) == $user_data[0]) {
				return true;
			}
		}
		return false;
	}

	function add_user($username, $email, $password) {
		file_put_contents("../users.dat", base64_encode($username) . "," . base64_encode($email) . ",0\n", $flag = FILE_APPEND);
		file_put_contents("../passwords.dat", md5($username) . "," . base64_encode($password) . "\n", $flag = FILE_APPEND);
	}

	function get_user($username) {
		$data = file_get_contents('../passwords.dat');
		$passwords = explode("\n", $data);
		foreach ($passwords as $key => $value) {
			$user_data = explode(",", $value);
			if (md5($username) == $user_data[0]) {
				return array($username, base64_decode($user_data[1]));
			}
		}
		return array("", "");
	}
?>
