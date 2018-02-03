<?php if(!defined('simple_cms')) exit(); ?>
			<form action='?act=user&mid=myinfo' method='POST'>
				Hello <b><?=$result['id'];?></b>
				<br/>
				pw : <input type='text' name='pw'>
				<br/>
				<input type='submit' value='change' style='width:250px'>
			</form>