<?php if(!defined('simple_cms')) exit(); ?>
			<form method='POST' action='./?act=user&mid=register'>
				id : <input type='text' name='id'><br/>
				pw : <input type='text' name='pw'><br/>
				email : <input type='text' name='email'><br/>	
				<input type='submit' value='register' style='width:210px'>
			</form>
			<a href='./?act=user&mid=login'>click me if you have a account</a>