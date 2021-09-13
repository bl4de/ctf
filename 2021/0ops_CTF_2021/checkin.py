#!/usr/bin/env python3

from pwn import *

io = remote('111.186.59.11', 16256)
print(io.recvline())
formula = io.recvline().replace(b'mod', b'%').replace(b' = ?\n',b'')
res = eval(formula)

io.send(str(res))

print(io.recvline())