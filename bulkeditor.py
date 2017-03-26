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

print "[+] opening {} for edit\n\n".format(path)
lines = f.readlines()

for l in range(0, len(lines)-1):
    if "![" in lines[l]:
        corrected = lines[l].replace("\n","") + lines[l+1]
        lines[l+1] = ""
        print "[+] correct inline image Markdown tag -> {}".format(corrected)
    else:
        corrected = lines[l]

    n.write(corrected)

print "[+] remove original file"
os.remove(path)
print "[+] save edited copy with original filename -> {}".format(filename)
os.rename(dirname + "/" + tmpname, filename)
print "[+] done\n\n"
