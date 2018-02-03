<?php
	if(!defined('simple_cms')) exit();

	define('CMS_PATH', str_replace('config/config.inc.php', '', str_replace('\\', '/', __FILE__)));
	define('CMS_SKIN_PATH', CMS_PATH . 'skin/default/');
	if(!function_exists('mysqli_connect')){
		exit('<script>alert("plz use php7.x");</script>');
	}
	function __simple_cms_autoload($class_name) {
    	if(!preg_match('/[^a-z0-9_]/is', $class_name)){
    		include CMS_PATH.'classes/' . $class_name . '.class.php';
    	}
    	else{
    		exit('class error'); 
    	}
	}
	spl_autoload_register('__simple_cms_autoload');

	include(CMS_PATH. 'functions/waf.php');
	include(CMS_PATH. 'functions/lib.php');
?>