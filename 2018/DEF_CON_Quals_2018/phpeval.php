<!DOCTYPE html>
<html>
<head>
  <title>php as a service</title>
  <link rel='stylesheet' href='bootstrap.min.css' />
</head>
  <body>
    <div id='main'>
      <div class='container'>
        <div class='row'>
          <h1>PHP<small> - Custom <code>eval</code> whitelisting!</small></h1>
        </div>
        <div class='row'>
					<p class='lead'>
						PHP is dangerous, so we wrote a <a href="./websec_eval_wl.so">custom php extension</a> to 
						improve its security. We're also taking advantage of the <a href="https://secure.php.net/manual/en/ini.core.php#ini.open-basedir">open_basedir</a>
						directive to prevent you from accessing the <code>flag</code> binary up the current folder.
						You can check the source of the page <a href='./source.php'>here</a>.
          </p>
        </div>
      </div>
      <div class='container '>
        <div class='row '>
          <form action='' method='post' class="form-inline">
					  <div class="form-group">
					    <div class="input-group">
                <div class="input-group-addon">Code to eval</div>
                <input type='text' name='d' id='d' class="form-control" value='printf(1+1);'> <br>
              </div>
            </div>
            <div class="form-group">
              <input type='submit' value='Run!' class="btn btn-default" name='submit'>
            </div>
          </form>
        </div>
      </div>

      <br/>

      <div class='container'>
				<p class="well">
					<?php
						if (isset($_POST['d'])) {
							eval($_POST['d']);
						} else {
							echo 'Can you execute the <code>./flag</code> binary?';
						}?>
				</p>
      </div>
    </div>
  </body>
</html>