#!/usr/bin/python
import base64

f = open("README.txt").read().split("\n")
qrcode = ""
tmp = ""
i = 1

fout = open("qrcodes.txt", "a+")

for p in f:
    tmp += p
    if len(p) < 77 and p.endswith(("ilogK","==","Ao=")):
        qrcode = base64.b64decode(tmp)
        print "[+] save QRcode to file"
        fout.write(qrcode + "\n\n\n")
        tmp = ""
        
fout.close()

print "[+] end"

# IW{QR_C0DES_RUL3}