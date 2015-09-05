#!/usr/bin/python
# diff = 0x17

str = "36 36 2a 64 4b 4b 4a 21 1e 4b 1f 20 1f 21 4d 4b 1b 1d 19 4f 21 4c 1d 4a 4e 1c 4c 1b 22 4f 22 22 1b 21 4c 20 1d 4f 1f 4c 4a 19 22 1a 66";
ascii = ""

for c in str.split(" "):
    ascii += chr(int(c,16) + 0x17)
    
print ascii; # MMA{bba85b6768db240f8c4ae3c29f9928c74f6ca091}