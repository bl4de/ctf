#!/usr/bin/env python
import base64

print "\n[+] AlexCTF 2017 CR1: Ultracoded | by bl4de (Stack)"
print "\n[+] original content"
zeroone = open('zero_one', 'rw').read()

print zeroone

print "\n\n[+] change ZERO to 0 and ONE to 1"
zeroone = zeroone.replace('\n', '').replace(
    ' ', '').replace('ZERO', '0').replace('ONE', '1')

print zeroone

print "\n[+] split into 8-bit chunks; convert to decimal, then to ASCII"
zeroone_decoded = ''
for x in range(0, len(zeroone), 8):
    # print chr(int(zeroone[x:8], 2))
    zeroone_decoded += chr(int(zeroone[x:x + 8], 2))

print zeroone_decoded

print "\n\n[+] it's Base64 encoded Morse string"
print base64.b64decode(zeroone_decoded)

# .- .-.. . -..- -.-. - ..-. - .... .---- ..... --- .---- ... --- ..... ..- .--. ...-- .-. --- ..... . -.-. .-. ...-- - --- - -..- -
# using eg. http://morsecode.scphillips.com/translator.html
# Morse --> ALEXCTFTH15O1SO5UP3RO5ECR3TOTXT

print "\n\n[+] the flag after Morse encoded"
print "ALEXCTFTH15O1SO5UP3RO5ECR3TOTXT"

print "\n\n[+] the flag is: ALEXCTF{TH15_1S_5UP3R_5ECR3T_TXT}"
