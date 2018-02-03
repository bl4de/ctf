<?php if(!defined('simple_cms')) exit(); ?>
			<form action='index.php?act=board&mid=write' id='form' method='POST'>
				title : <input type='text' name='title' style="width:500px"><br/>
				content : <textarea name='content' rows='10' style="width:500px"></textarea><br/>
				<input type='submit' value="write" style="width:500px"><br/>
			</form>