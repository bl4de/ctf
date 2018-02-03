<?php
	if(!defined('simple_cms')) exit();
	class User extends User_lib{
		public $mid = null;
		function __construct(){
			$this->mid = Context::get('mid');
			if(($this->mid === 'action_login' || $this->mid === 'action_register') && is_login()){
				alert('already login', 'back');
			}
			else if($this->mid === 'action_myinfo' && !is_login()){
				alert('plz login first', '?act=user&mid=login');
			}
		}
		function Default(){
			if(!is_login()){
				alert('login first', './?act=user&mid=login');
			}
			else{
				alert('page not found', './');
			}
		}
		function action_myinfo(){
			if($_SERVER['REQUEST_METHOD'] === 'GET'){
				$result = DB::fetch_row('users', array('idx'=>$_SESSION['idx']));
				include(CMS_SKIN_PATH . 'myinfo.php');
			}
			else if($_SERVER['REQUEST_METHOD'] === 'POST'){
				$this->do_change_info();
			}
		}
		function action_login(){
			if(!is_login() && $_SERVER['REQUEST_METHOD'] === 'GET'){
				include(CMS_SKIN_PATH . 'login.php');
			}
			else if(!is_login() && $_SERVER['REQUEST_METHOD'] === 'POST'){
				$this->do_login();
			}
		}
		function action_register(){
			if(!is_login() && $_SERVER['REQUEST_METHOD'] === 'GET'){
				include(CMS_SKIN_PATH . 'register.php');
			}
			else if(!is_login() && $_SERVER['REQUEST_METHOD'] === 'POST'){
				$this->do_register();
			}
		}
		function action_logout(){
			$this->do_logout();
		}
	}
?>