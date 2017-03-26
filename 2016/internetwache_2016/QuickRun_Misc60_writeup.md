# Quick Run (Misc, 60pts)

---

## Problem

Get the flag ! :)

## Solution

We get text file contains long Base64 strings (see README.txt).  Each string is one QR code (27 in total) and every QR code equals one sign in flag.

Using simple Python script I've ripped all QR codes into single file:

```python
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
        print "[+] save {} QRcode to file".format(i)
        fout.write(qrcode + "\n\n\n")
        tmp = ""
        i += 1
        
fout.close()

print "[+] end"

```

Then I've just scanned them one by one directly from my laptop screen using my smartphone and simple QR code reader.

Finally I've get the flag:

```
IW{QR_C0DES_RUL3}
```

