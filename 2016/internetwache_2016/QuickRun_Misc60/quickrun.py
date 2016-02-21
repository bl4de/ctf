#!/usr/bin/python
import base64

f = open("README.txt").read().split("\n")
qrcode = ""
fn = "qrcode_"
tmp = ""
i = 1

for p in f:
    tmp += p
    if len(p) < 77 and p.endswith(("ilogK","==","Ao=")):
        qrcode = base64.b64decode(tmp)
        filename = fn + str(i) + ".txt"
        print "[+] save QRcode file " + filename
        f = open(filename, "w")
        f.write(qrcode)
        f.close()
        tmp = ""
        i += 1

print "[+] end"

# IW{QR_C0DES_RUL3}