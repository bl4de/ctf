# 0ldsk00lBlog (Web, 80pts)

---

## Problem

Description: I stumbled across this kinda oldskool blog. I bet it is unhackable, I mean, there's only static HTML.

Service: https://0ldsk00lblog.ctf.internetwache.org/

## Solution

The page is a very simple static HTML:

![Blog page]
(0ldsk00lblog_01.png)


No _robots.txt_, no _admin_, literally nothing :) But there's a mention about Git, so let's try path to _.git/logs/HEAD_ :


![Blog page]
(0ldsk00lblog_02.png)

Bingo!

As I was describing a few weeks ago, how to hack Git repositories (see https://github.com/bl4de/research/blob/master/hidden_directories_leaks/README.md#git) - I've just followed my way and I've got the flag very soon:


```
bl4de on Rafals-MacBook in ~/hacking/ctf/2016/internetwache_2016/0ldsk00lBlog $ git cat-file -p 3be70be50c04bab8cd5d115da10c3a9c784d6bae
100644 blob 5508adb31bf48ae5fe437bdeba60f83982356934	index.html
bl4de on Rafals-MacBook in ~/hacking/ctf/2016/internetwache_2016/0ldsk00lBlog $ mkdir .git/objects/55
bl4de on Rafals-MacBook in ~/hacking/ctf/2016/internetwache_2016/0ldsk00lBlog $ mv 08adb31bf48ae5fe437bdeba60f83982356934 $_
bl4de on Rafals-MacBook in ~/hacking/ctf/2016/internetwache_2016/0ldsk00lBlog $ git cat-file -p 5508adb31bf48ae5fe437bdeba60f83982356934


<html>
<head>
	<title>0ldsk00l</title>
</head>
<body>
	<h2>2000</h2>
	<p>
		Oh, did I say that I like kittens? I like flags, too: IW{G1T_1S_4W3SOME}
	</p>

	<h2>1990-2015</h2>
	<p>
		Hmm, looks like totally forgot about this page. I should start blogging more often.
	</p>

	<h2>1990</h2>
	<p>
		I proudly present to you the very first browser for the World Wide Web. Feel free to use it to view my awesome blog.
	</p>

	<h2>1989</h2>
	<p>
		So, yeah, I decided to invent the World Wide Web and now I'm sitting here and writing this. 
	</p>
</body>
</html>
```

So the flag is:

```
IW{G1T_1S_4W3SOME}
```