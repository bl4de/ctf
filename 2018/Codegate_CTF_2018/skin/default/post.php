<?php
	if(!defined('simple_cms')) exit();

	echo '<b>uploader</b> : '.xss_block($result['id']).'<br/>';
	echo '<b>title</b> : '.xss_block($result['title']).'<br/>';
	echo '<b>content</b> : <br/>'.xss_block($result['content']);
?>