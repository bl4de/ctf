<?php
	if(!defined('simple_cms')) exit();
	function str_check($str, $type){
		if($type === 'id'){
			if(!preg_match('/[^a-z0-9]/', $str) && strlen($str)<=10){
				return true;
			}
		}
		else if($type === 'email' && strlen($str) <= 50){		
			if(filter_var($str, FILTER_VALIDATE_EMAIL)){
				return true;
			}
		}
		return false;
	}
	function get_search_query($column, $search, $operator){
		$column = explode('|', $column);
		$result = '';
		for($i=0; $i<count($column); $i++){
			if(trim($column[$i]) === ''){
				continue;				
			}
			$result .= " LOWER({$column[$i]}) like '%{$search}%' {$operator}";
		}
		$result = trim(substr($result, 0 , strrpos($result, $operator)));
		return $result;
	}
	function xss_block($str){
		return htmlspecialchars($str, ENT_QUOTES);
	}
	function is_login(){
		if($_SESSION['is_login']){
			return true;
		}
		return false;
	}
	function get_class_list($path){
		$result = array();
		$i = 0;
		foreach (scandir($path) as $file) {
			if($file === '.' || $file === '..'){
				continue;
			}
			$result[$i++] = strtolower(substr($file, 0, strpos($file, '.')));
		}
		return $result;
	}
	function alert($msg, $move=''){
		$result = '<script>';
		$result .= 'alert(\''.$msg.'\');'; 
		if($move && $move !== 'back'){
			$result .= 'location.href=\''.$move.'\';';
		}
		else if($move === 'back'){
			$result .= 'history.back();';
		}
		$result .= '</script>';
		exit($result);
	}
?>