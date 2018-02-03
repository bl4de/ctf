<?php
	if(!defined('simple_cms')) exit();
	class Context{
		function &getInstance()
		{
			static $theInstance = null;
			if(!$theInstance)
			{
				$theInstance = new Context();
			}
			return $theInstance;
		}
		function init(){
			$this->_setRequestArgument();
			$this->_filterArgument();
		}
		function _filterArgument(){
			$class_list = array('db', 'context', 'handler');
			$allow_class = get_class_list(CMS_PATH . 'classes/');
			if($this->get('act')){
				if(preg_match('/[^a-z0-9]/is', $this->get('act')) || strlen($this->get('act')) > 20 || strlen($this->get('act')) <= 3){
					$this->set('act', 'Main');
				}
				if(!in_array($this->get('act'), $allow_class)){
					$this->set('act', 'Main');
				}
				foreach ($class_list as $value) {
					if(stripos($this->get('act'), $value) !== false){
						$this->set('act', 'Main');
					}
				}
			}
			if($this->get('mid')){
				if(preg_match('/[^a-z0-9]/is', $this->get('mid')) || strlen($this->get('mid')) > 20){
					$this->set('mid', 'Default');
				}
				$this->set('mid', 'action_'.$this->get('mid'));
			}
		}
		function _setRequestArgument(){
			if(!count($_REQUEST))
			{
				return;
			}
			foreach($_REQUEST as $key => $val)
			{
				if($val === '' || self::get($key))
				{
					continue;
				}
				$key = htmlentities($key);
				$this->set($key, $val);
			}
		}
		function get($key){
			$self = self::getInstance();
			return $self->Context->{$key};
		}
		function set($key, $val){
			$self = self::getInstance();
			$self->Context->{$key} = $val;
		}
	}
?>