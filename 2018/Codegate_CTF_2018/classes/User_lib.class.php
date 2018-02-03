<?php
	if(!defined('simple_cms')) exit();
	class User_lib{
		function do_logout(){
			session_destroy();
			alert('bye', './');
		}
		function do_change_info(){
			if(Context::get('pw') && is_string(Context::get('pw'))){
				$pw = sha1(Context::get('pw'));
				
				$replace = array(
					'pw'=>$pw,
				);
				$query = array(
					'idx'=>$_SESSION['idx'],
				);

				$result = DB::update('users', $replace, $query);
				if($result){
					alert('success!', './');
				}
				else{
					alert('erro!', 'back');
				}
			}
		}
		function do_login(){
			if(Context::get('id') && Context::get('pw') && is_string(Context::get('id')) && is_string(Context::get('pw'))){
				$id = Context::get('id');
				$pw = sha1(Context::get('pw'));

				if(!str_check($id, 'id')) alert('do not hack me!', 'back');
				$query = array(
					'id'=>$id,
					'pw'=>$pw
				);
				$result = DB::fetch_row('users', $query, 'and');
				if($result['id']){
					$_SESSION['idx'] = $result['idx'];
					$_SESSION['id'] = addslashes($result['id']);
					$_SESSION['is_login'] = true;
					alert('login success', './');
				}
				else{
					alert('login fail', 'back');
				}
			}
			else{
				alert('check your parameter', 'back');
			}			
		}
		function do_register(){
			if(Context::get('id') && Context::get('pw') && is_string(Context::get('id')) && is_string(Context::get('pw')) && is_string(Context::get('email'))){
				$id = Context::get('id');
				$pw = sha1(Context::get('pw'));
				$email = Context::get('email');				
				if(!str_check($id, 'id') || !str_check($email, 'email')) alert('do not hack me!', 'back');
				
				$query = array(
					'id'=>$id,
					'email'=>$email
				);
				$result = DB::fetch_row('users', $query, 'or');
				if($result['id']){
					alert('already join', 'back');
				}
				$query = array(
					'id'=>$id,
					'pw'=>$pw,
					'email'=>$email,
					'ip'=>$_SERVER['REMOTE_ADDR']
				);
				if(DB::insert('users', $query)){
					alert('welcome!', './');
				}
				else{
					alert('something error', 'back');
				}
			}
			else{
				alert('check your parameter', 'back');
			}
		}
	}
?>