<?php
  session_start();
  include("5f0c2baaa2c0426eed9a958e3fe0ff94.php");
  $page = $_GET['page'];
  if($page == "login"){
?>
    <h3>Login</h3>
    <p>
      <form action="./?page=login_chk" method="POST">
      <table>
      <tr><td>ID</td><td><input type="text" name="uid" id="uid"></td>
      <td rowspan="3"><img src="./images/login.jpg" width="270" style="margin-left: 20px; margin-top: -38px; position:fixed;"></td></tr>
      <tr><td>PW</td><td colspan="2"><input type="text" name="upw" id="upw"></td></tr>
      <tr><td colspan="2"><input type="submit" value="Login" style="width: 100%;"></td></tr>
      </table>
      </form>
    </p>
<?php
  }
  elseif($page == "join"){
?>
    <h3>Join</h3>
    <p>
      <form action="./?page=join_chk" method="POST">
      <table>
      <tr><td>ID</td><td><input type="text" name="uid" id="uid"></td>
      <td rowspan="3"><img src="./images/login.jpg" width="270" style="margin-left: 20px; margin-top: -38px; position:fixed;"></td></tr>
      <tr><td>MAIL</td><td colspan="2"><input type="text" name="umail" id="uid"></td></tr>
      <tr><td>PW</td><td colspan="2"><input type="text" name="upw" id="upw"></td></tr>
      <tr><td colspan="2"><input type="submit" value="Join" style="width: 100%;"></td></tr>
      </table>
      </form>
    </p>
<?php
  }
  elseif($page == "login_chk"){
    $uid = $_POST['uid'];
    $upw = $_POST['upw'];
    if(($uid) && ($upw)){
      include "dbconn.php";
      $result = rbSql("select","member_".$uid,["pw",md5($upw)]);
      if(is_string($result)) error("login fail");
      $_SESSION['uid'] = $result['0'];
      $_SESSION['lvl'] = $result['4'];
      exit("<script>location.href='./';</script>");
    }
    else error("login fail");
  }      
  elseif($page == "join_chk"){
    $uid = $_POST['uid'];
    $umail = $_POST['umail'];
    $upw = $_POST['upw'];
    if(($uid) && ($upw) && ($umail)){
      if(strlen($uid) < 3) error("id too short");
      if(strlen($uid) > 16) error("id too long");
      if(!ctype_alnum($uid)) error("id must be alnum!");
      if(strlen($umail) > 256) error("email too long");
      include "dbconn.php";
      $upw = md5($upw);
      $uip = $_SERVER['REMOTE_ADDR'];
      if(rbGetPath("member_".$uid)) error("id already existed");
      $ret = rbSql("create","member_".$uid,["id","mail","pw","ip","lvl"]);
      if(is_string($ret)) error("error");
      $ret = rbSql("insert","member_".$uid,[$uid,$umail,$upw,$uip,"1"]);
      if(is_string($ret)) error("error");
      exit("<script>location.href='./?page=login';</script>");
    }
    else error("join fail");
  }
  elseif($page == "photo"){
?>
    <h3>Photo</h3>
    <p><img src="./images/1.jpg" width="430"></p>
    <p><img src="./images/2.jpg" width="430"></p>
    <p><img src="./images/3.png" width="430"></p>
    <p><img src="./images/4.gif" width="430"></p>
<?php
  }      
  elseif($page == "video"){
?>
    <h3>Music Video</h3>
    <p><iframe width="520" height="293" src="//www.youtube.com/embed/iv-8-EgPEY0?rel=0" frameborder="0" allowfullscreen></iframe></p>
    <p><iframe width="520" height="293" src="//www.youtube.com/embed/xnku4o3tRB4?rel=0" frameborder="0" allowfullscreen></iframe></p>
    <p><iframe width="520" height="293" src="//www.youtube.com/embed/n8I8QGFA1oM?rel=0" frameborder="0" allowfullscreen></iframe></p>
    <p><iframe width="520" height="293" src="//www.youtube.com/embed/kKS12iGFyEA?rel=0" frameborder="0" allowfullscreen></iframe></p>
<?php
  }      
  elseif($page == "me"){
    echo "<p>uid : {$_SESSION['uid']}</p><p>level : ";
    if($_SESSION['lvl'] == 1) echo "Guest";
    elseif($_SESSION['lvl'] == 2) echo "Admin";
    echo "</p>";
    include "dbconn.php";
    $ret = rbSql("select","member_".$_SESSION['uid'],["id",$_SESSION['uid']]);
    echo "<p>mail : {$ret['1']}</p><p>ip : {$ret['3']}</p>";
    if($_SESSION['lvl'] === "2"){
      echo "<p>Flag : </p>";
      include "/flag";
      rbSql("delete","member_".$_SESSION['uid'],["id",$_SESSION['uid']]);
    }
  }
  elseif($page == "logout"){
    session_destroy();
    exit("<script>location.href='./';</script>");
  }
  else{
?>
    <h3>ㅋrystal :/</h3>
    <p><img src="./images/k_03.jpg" width="430" style="position:fixed;"></p>
<?php
  }
  include("4bbc327f5b0fd076e005961bcfc4a9ee.php");
?>