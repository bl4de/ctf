<?php
echo intval('0e123' == '0e999'); // result 1, which means TRUE
echo "\n";
echo intval('0e123' === '0e999'); // result 0, which means FALSE
echo "\n";