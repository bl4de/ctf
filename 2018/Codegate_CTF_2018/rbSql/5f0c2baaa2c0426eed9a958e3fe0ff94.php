<?php
function error($msg){
	exit("<script>alert('{$msg}');history.go(-1);</script>");
}
?><!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html lang="en" xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>Krystal Fan Site krybiya.kr</title>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<link href="style.css" rel="stylesheet" type="text/css" />
</head>
<body>
<div id="container">
  <div id="banner">
    <h1>krybiya.kr</h1>
    <p class="slogan">Krytal Fan Site </p>
  </div>
  <div id="navbar">
    <ul>
      <li><a href="./">Home</a></li>
      <li><a href="./?page=photo">Photo</a></li>
      <li><a href="./?page=video">M/V</a></li>
    </ul>
  </div>
  <div class="clear">&nbsp;</div>
  <div id="sidebar">
    <h2>Sub Menu</h2>
    <ul>
      <li><a href="./">Home</a></li>
<?php
if($_SESSION['uid']) echo "      <li><a href=\"./?page=me\">MyPage</a></li>\n      <li><a href=\"./?page=logout\">Logout</a></li>";
  else echo "      <li><a href=\"./?page=login\">Login</a></li>\n      <li><a href=\"./?page=join\">Join</a></li>";
?>
    </ul>
  </div>
  <div id="content">
  
