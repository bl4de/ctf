#!/usr/bin/python

r = {"a": "u",
     " ": " ",
     "b": "n",
     "c": "h",
     "d": "m",
     "e": "a",
     "f": "q",
     "g": "w",
     "h": "z",
     "i": "i",
     "j": "d",
     "k": "y",
     "l": "p",
     "m": "r",
     "n": "c",
     "o": "j",
     "p": "k",
     "q": "b",
     "r": "g",
     "s": "v",
     "t": "s",
     "u": "l",
     "w": "e",
     "v": "o",
     "x": "t",
     "y": "t",
     " ": " ",
     "!": " ",
     "z": "f"}
     
plain = raw_input("enter plain: ")
output = ""

for c in plain:
    output += r[c.lower()]

print output
