#!/usr/bin/python

ciphered = "VprPGS{jnvg_bar_cyhf_1_vf_3?}"
valid = ""
VALID = ""

for x in range(0, len(ciphered)):
    # ROT13 only for ASCII codes from 97 to 122 decimal:
    if ord(ciphered[x]) in range(97, 122):
        if (ord(ciphered[x]) + 13) > 122:
            valid += chr(ord(ciphered[x]) - 13)
        else:
            valid += chr(ord(ciphered[x]) + 13)
    else:
        valid += ciphered[x]

for x in range(0, len(valid)):
    if ord(valid[x]) in range(65, 90):
        if (ord(valid[x]) + 13) > 90:
            VALID += chr(ord(valid[x]) - 13)
        else:
            VALID += chr(ord(valid[x]) + 13)
    else:
        VALID += valid[x]

print VALID
