# uncompyle6 version 3.6.5
# Python bytecode 3.6 (3379)
# Decompiled from: Python 3.7.7 (default, Mar 10 2020, 15:43:33)
# [Clang 11.0.0 (clang-1100.0.33.17)]
# Embedded file name: pybonhash.py
# Compiled at: 2020-03-28 13:11:38
# Size of source mod 2**32: 1017 bytes
import string
import sys
import hashlib
import binascii
from Crypto.Cipher import AES

# from flag import key
key = '234532542354246345646452645624353434543554'

if not len(key) == 42:
    raise AssertionError
else:
    data = open(sys.argv[1], 'rb').read()
    assert len(data) >= 1
FIBOFFSET = 4919
MAXFIBSIZE = len(key) + len(data) + FIBOFFSET


def fibseq(n):
    out = [
        0, 1]
    for i in range(2, n):
        out += [out[(i - 1)] + out[(i - 2)]]

    return out



FIB = fibseq(MAXFIBSIZE)
print(FIB)
i = 0
output = ''
while i < len(data):
    data1 = data[(FIB[i] % len(data))]
    key1 = key[((i + FIB[(FIBOFFSET + i)]) % len(key))]
    print(key1)
    i += 1
    data2 = data[(FIB[i] % len(data))]
    key2 = key[((i + FIB[(FIBOFFSET + i)]) % len(key))]
    print(key2)
    print (bytes([int(key1), int(key2)]))
    i += 1
    tohash = bytes([data1, data2])
    toencrypt = hashlib.md5(tohash).hexdigest()
    thiskey = (bytes([int(key1), int(key2)])) * 16
    cipher = AES.new(thiskey, AES.MODE_ECB)
    enc = cipher.encrypt(toencrypt.encode('utf-8'))
    output += binascii.hexlify(enc).decode('ascii')

print(output)
# okay decompiling pybonhash.cpython-36.pyc
