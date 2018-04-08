#!/usr/bin/python
import hashlib
# c.hackle yhbG f2b31b3a7a7c41093321d0c98c37f5ad
# md5 = md5($password + $salt)  => pizza

for passwd in open("/Users/bl4de/hacking/dictionaries/rockyou.txt", "r"):
    if hashlib.md5(passwd.strip() + "yhbG").hexdigest() == "f2b31b3a7a7c41093321d0c98c37f5ad":
        print "[+] password for Collins Hackle is {}".format(passwd.strip())
        exit(0)

print "[+] Done"