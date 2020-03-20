#!/usr/bin/env python

# agqr{yue_stdcgciup_padas}

# ANGSTROMCTFANGSTROMCTFAN

# actf{
import ctfpwn


ciphered = "agqr{yue_stdcgciup_padas}"
key = "ANGSTROMCTF"

l = len(ciphered)
current = 0

p = 0
plain = ""

for c in ciphered:
    # print p
    if current % 3 != 0:
        plain = plain + chr(ord(c) | ord(key[p]))
    else:
        plain = plain + ciphered[current]

    if p == len(key) - 1:
        p = 0
    else:
        p = p + 1

    current = current + 1

print plain