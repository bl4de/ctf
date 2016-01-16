#!/usr/bin/python
import re

f = open("file.txt", "r")
chars = re.findall('[01]{8}', f.readline())
s = ""
for c in chars:
    s += chr(int(c,2))    
print s
# flat{People always make the best exploits.} I've never found it hard to hack most people. If you listen to them, watch them, their vulnerabilities are like a neon sign screwed into their heads.