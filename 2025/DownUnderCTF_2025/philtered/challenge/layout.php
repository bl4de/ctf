<?php
function render_layout($title, $content) {
    echo "<!DOCTYPE html>\n";
    echo "<html lang='en'>\n<head>\n<meta charset='UTF-8'>\n<title>" . htmlspecialchars($title) . "</title>\n";
    echo "<meta name='viewport' content='width=device-width, initial-scale=1.0'>\n";
    echo "<style>body{font-family:sans-serif;background:#f7f7f7;margin:0;}header{background:#222;color:#fff;padding:1em;text-align:center;}main{max-width:700px;margin:2em auto;background:#fff;padding:2em;border-radius:8px;box-shadow:0 2px 8px #0001;}footer{text-align:center;color:#888;padding:1em 0;}a{color:#0077cc;text-decoration:none;}a:hover{text-decoration:underline;}</style>\n";
    echo "</head>\n<body>\n<header><h1>Philtered</h1><p>Filtered Solutions for a Digital World</p></header>\n<main>\n";
    echo $content;
    echo "</main>\n<footer>&copy; ".date('Y')." Philtered. All rights reserved.</footer>\n</body>\n</html>";
}
