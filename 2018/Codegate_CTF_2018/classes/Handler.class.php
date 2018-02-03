<?php
	if(!defined('simple_cms')) exit();
	class Handler{
		function mainModule(){
			$act = ucfirst(Context::get('act'));
			$mid = Context::get('mid');			
			if(!$act || !class_exists($act))
				$Module = new Main();
			else
				$Module = new $act();

			if(method_exists($Module, $mid)){
				$Module->{$mid}();
			}	
			else{	
				$Module->Default();
			}
		}
		function init(){
			$db = DB::getInstance();
			if(!$db){
				return false;
			}
			return true;
		}

	}
?>