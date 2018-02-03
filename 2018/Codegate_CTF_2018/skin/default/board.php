<?php if(!defined('simple_cms')) exit(); ?>
				<table><tr><th>idx</th><th>title</th><th>id</th></tr>
					<?php
						for($i=0; $i<count($result); $i++){
					?>	
					<tr><td><a href='index.php?act=board&mid=read&idx=<?=xss_block($result[$i]['idx']);?>'><?=xss_block($result[$i]['idx']);?></a></td><td><?=xss_block($result[$i]['title']);?></td><td><?=xss_block($result[$i]['id']);?></td></tr>
					<?php
						}
					?>
				</table>
				<br/>
				<br/>
				<br/>
				<form action='index.php' method='GET'>
					Search : 
					<input type='hidden' name='act' value='board'>
					<input type='hidden' name='mid' value='search'>
					<input type='hidden' name='col' value='title'>
					<select name="type">
  						<option value="1">or</option>
  						<option value="2">and</option>
					</select>
					<input type='text' name='search' value=''>
					<input type='submit' value='search!'>
				</form>
				<br/>
				<a href='index.php?act=board&mid=write'><b>write</b></a>