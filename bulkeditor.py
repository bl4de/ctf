#!/usr/bin/env python
import os
import sys

tmpname = "tmpname"
dirname = sys.argv[1]
filename = sys.argv[2]
path = dirname + "/" + filename

f = open(path, "rw+")
n = open(dirname + "/" + tmpname, "w")
filename = f.name

print filename

lines = f.readlines()

for l in range(0, len(lines)-1):
    if "![" in lines[l]:
        corrected = lines[l].replace("\n","") + lines[l+1]
        lines[l+1] = ""
    else:
        corrected = lines[l]

    n.write(corrected)

os.remove(path)
os.rename(dirname + "/" + tmpname, filename)
