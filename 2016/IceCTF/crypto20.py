#!/usr/bin/python

s = "VprPGS{jnvg_bar_cyhf_1_vf_3?}"


def rot(str, franction, direction):
    flag = ""

    for c in str:
        if c not in "{}_":
            char = ord(c)
            if direction == "+":
                char += franction
            else:
                char -= franction
            c = chr(char)
        flag += c
    return flag


f = rot(s, 5, "+")
print f
f = rot(f, 8, "-")
print f

print "-" * 40

f = rot(s, 5, "-")
print f
f = rot(f, 8, "-")
print f

print "-" * 40

f = rot(s, 5, "+")
print f
f = rot(f, 8, "+")
print f

print "-" * 40

f = rot(s, 5, "-")
print f
f = rot(f, 8, "+")
print f
