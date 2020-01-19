#!/usr/bin/env python
import ctfpwn
import socket
import re

HOST = 'welcome.insomnihack.ch'
PORT = 1337


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
data = s.recv(1024)

print(data)
# start of MD5 hash:
result = re.search(r'"[0-9a-z]{6}"', data, re.M |
                   re.I).group().replace('"', '')
print "[+] OK, we're looking something to match {}".format(result)

# let's bruteforce this :P
iv = ctfpwn.md5('xyz')
iterations = 0

print("[+] First check: {} == {} ? And the result is... {} :) ".format(
    result, iv[0:6], result == iv[0:6]))
while iv[0:6] != result:
    iv = ctfpwn.md5(result)
    iterations += 1

    if iterations % 1000000 == 0:
        print("[.] {} iterations so far, still searching...".format(iterations))

print("[+] FOUND HIT !!! after {} iterations -> {}".format(iterations, iv))

# send answer to InsomniHack server
s.sendall(iv)
data = s.recv(1024)

print("[+] Server's response is: {}".format(data))
