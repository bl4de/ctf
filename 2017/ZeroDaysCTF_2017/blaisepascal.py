#!/usr/bin/env python
import math


def gen(n, r=[]):
    for x in range(n):
        l = len(r)
        r = [1 if i == 0 or i == l else r[i - 1] + r[i] for i in range(l + 1)]
        yield r

sum = 0
# now we can print a result:

for row in list(gen(2017)):
    if len(row) == 1:
        sum = sum + 1

    if len(row) > 1 and len(row) % 2 != 0:  # odd row
        el = ((len(row) + 1) / 2) - 1
        sum = sum + row[el]

print sum
