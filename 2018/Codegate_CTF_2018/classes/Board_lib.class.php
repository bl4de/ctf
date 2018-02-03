<?php
	if(!defined('simple_cms')) exit();
	class Board_lib{
		function do_write(){
			$title = Context::get('title');
			$content = Context::get('title');
			$id = $_SESSION['id'];

			$query = array(
				'title'=>$title,
				'content'=>$content,
				'id'=>$id,
				'date'=>date('Y-m-d h:i:s')
			);

			if(DB::insert('board', $query)){
				alert('write!', 'index.php?act=board&mid=Default');
			}
			else{
				alert('some error!', 'back');
			}
		}
	}
?>