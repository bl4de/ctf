#!/usr/bin/python
import zlib
crc = 550274426

with open('/Users/bl4de/hacking/dictionaries/rockyou.txt', 'r') as f:
    for passwd in f:
        passwd = passwd.strip()
        if abs(zlib.crc32(passwd)) == crc:
            print "found '{}' with crc32({}) = {}".format(passwd, passwd, zlib.crc32(passwd))
            exit(0)

print "not found :("
