#!/usr/bin/python
# diff = 0x17

import ct
#
# str = "36 36 2a 64 4b 4b 4a 21 1e 4b 1f 20 1f 21 4d 4b 1b 1d 19 4f 21 4c 1d 4a 4e 1c 4c 1b 22 4f 22 22 1b 21 4c 20 1d 4f 1f 4c 4a 19 22 1a 66";
ascii = ""
#
# for c in str.split(" "):
#     ascii += chr(int(c,16) + 0x17)
#
# print ascii; # MMA{bba85b6768db240f8c4ae3c29f9928c74f6ca091}

#
# str = "e3 e3 83 21 33 96 23 43 ef 9a 9a 05 18 c7 23 07 07 07 c7 9a 04 33 23 07 23 ef 12 c7 04 96 43 23 23 18 04 04 05 c7 fb 18 96 43 ef 43 ff";
#
# for c in str.split(" "):
#     s = "_"
#     for k in ct.convertion:
#         if ct.convertion[k] == c:
#             s = k
#     ascii += s
#
# print ascii # MMA{f52da776412888170f282a9105d2240061c45dad}

str = "60 00 0c 3a 1e 52 02 53 02 51 0c 5d 56 51 5a 5f 5f 5a 51 00 05 53 56 0a 5e 00 52 05 03 51 50 55 03 04 52 04 0f 0f 54 52 57 03 52 04 4e"
ascii = "M"
p = 0x4c
c = chr(p)

for x in str.split(" "):
    if x == "00":
        ascii += c
    else:
        delta = int(x, 16)

        c = chr(p - delta)
        ascii += c

print ascii
