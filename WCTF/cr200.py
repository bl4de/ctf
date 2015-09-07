#!/usr/bin/python
import sys

f = open('crypto200')
# l = f.read()

_sum = 0
_signs = []
_counter = 0
_step  = 23
_decimalString = ""
_hexString = ""

global offset
if len(sys.argv) == 2:
    offset = int(sys.argv[1])
else:
    offset = 0
    
for sign in f.readline():
    _sign = int(sign)
    _sum += _sign # offset
    _counter += 1
    if _counter == 23:
        _signs.append(_sum + offset)
        _sum = 0
        _counter = 0
 
print _signs   

for l in _signs:
    _decimalString += chr(l)
    _hexString += str(l).decode('hex')
    # print chr(hex(l))
    
print _decimalString
print _hexString