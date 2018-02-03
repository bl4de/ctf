<?php
	if(!defined('simple_cms')) exit();
	class Main{
		function __construct(){
			if(!is_login()){
				alert('login first', '?act=user&mid=login');
			}
			if($_SERVER['REQUEST_METHOD'] !== 'GET'){
				exit('~_~');
			}
		}
		function Default(){
			include(CMS_SKIN_PATH . 'main.php');
		}
	}
?>