<?php if(!defined('simple_cms')) exit(); ?>
			<form method='POST' action='./?act=user&mid=login'>
				<input type='text' name='id'>
				<input type='text' name='pw'>
				<input type='submit' value='login'>
			</form>
			<a href='./?act=user&mid=register'>click me if you don't have a account</a>