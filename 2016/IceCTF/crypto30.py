#!/usr/bin/python

s = """
Gyzvecy ke WvyVKT!

W'zz by reso dsbdkwksky tzjq teo kly ujr. Teo keujr, gy joy dksurwmq bjdwv
vorakeqojalr jmu wkd jaazwvjkwemd. Vorakeqojalr ljd j zemq lwdkeor,
jzklesql gwkl kly juxymk et vecaskyod wk ljd qekkym oyjzzr vecazwvjkyu.

Decy dwcazy ezu vwalyod joy kly Vjydjo vwalyo, kly Xwqymyoy vwalyo,
kly dsbdkwkskwem vwalyo, glwvl wd klwd emy, jmu de em.
Jzcedk jzz et klydy vwalyod joy yjdwzr boeiym keujr gwkl kly

lyza et vecaskyod. Decy myg ymvorakwem cykleud joy JYD, kly
vsooymk dkjmujou teo ymvorakwem, jzemq gwkl ODJ. Vorakeqojalr wd j

xjdk twyzu jmu wd xyor wmkyoydkwmq klesql. De iwvi bjvi,
oyju sa em decy veez vwalyod jmu ljxy tsm!

El jmu teo reso oyveoud cr mjcy wd
WvyVKT{jzgjrd_zwdkym_ke_reso_dsbdkwksky_tzjqd}.

"""

t = {
    "q": "g",
    "t": "f",
    "J": "A",
    "a": "p",
    "D": "S",
    "l": "h",
    "m": "n",
    "w": "i",
    "d": "s",
    "s": "u",
    "r": "y",
    "j": "a",
    "g": "w",
    "_": "_",
    "u": "d",
    "o": "r",
    "k": "t",
    "b": "b",
    ".": ".",
    ",": ",",
    "'": "'",
    "{": "{",
    "}": "}",
    "!": "!",
    " ": " ",
    "\n": "\n",
    "G": "W",
    "z": "l",
    "v": "c",
    "e": "o",
    "c": "m",
    "W": "I",
    "y": "e",
    "V": "C",
    "K": "T",
    "T": "F"
}

res = ""

for c in s:
    if c in t.keys():
        res += t[c]
    else:
        res += "-"

print res
