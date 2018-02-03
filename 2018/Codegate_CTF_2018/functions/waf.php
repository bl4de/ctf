<?php 
	if(!defined('simple_cms')) exit();

	$method = $_SERVER['REQUEST_METHOD'];

	if($method !== 'GET' && $method !== 'POST'){
			exit('are you hacker?');
	}

	$filter_str = array('or', 'and', 'information', 'schema', 'procedure', 'analyse', 'order', 'by', 'group', 'into');

	function escape_str($array)
	{
	    if(is_array($array)) {
	        foreach($array as $key => $value) {
	            if(is_array($value)) {
	                $array[$key] = escape_str($value);
	            } else {
	                $array[$key] = filter($value);
	            }
	        }
	    } 
	    else {
	        $array = filter($array);
	    }
	    return $array;
	}
	function filter($str){
		global $filter_str;

		foreach ($filter_str as $value) {
			if(stripos($str, $value) !== false){
				die('are you hacker?');
			}
		}
		return addslashes($str);
	}

	$_GET = escape_str($_GET);
	$_POST = escape_str($_POST);
	$_COOKIE = escape_str($_COOKIE);
	$_REQUEST = escape_str($_REQUEST);	
?>