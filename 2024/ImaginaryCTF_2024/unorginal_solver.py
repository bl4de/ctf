#!/usr/bin/python
f = "lfqc~opvqZdkjqm`wZcidbZfm`fn`wZd6130a0`0``761gdx"
s = ''

for c in f:
    s += chr(ord(c) ^ 5)

print(s) # ictf{just_another_flag_checker_a3465d5e5ee234ba}
