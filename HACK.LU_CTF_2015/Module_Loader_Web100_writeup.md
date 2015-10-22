# Hack.lu CTF 2015 - Module Loader (Web, 100pts)

## Problem

100 Points by lucebac (Web)

Since his students never know what date it is and how much time they have until the next homework's deadline, Mr P. H. Porter wrote a little webapp for that.


## Solution

We get simple web application with two available options:

(1)

After quick research there's an obvious LFI (Local File Include)

(2)

It looks like we can see any file we want to as they are just printed out:

date

Also, we can display .htaccess, which contains some directory with quite "obvious" name :P


<!--
# seems to be not working, though
#<Directory "3cdcf3c63dc02f8e5c230943d9f1f4d75a4d88ae">
#    Options -Indexes
#</Directory>
# -->

Let's take a look there and here we go:

(3)

Last thing is to use LFI and see, what's in flag.php file:


school.fluxfingers.net:1522/?module=../3cdcf3c63dc02f8e5c230943d9f1f4d75a4d88ae/flag.php


flag{hidden_is_not_actually_hidden}