#!/usr/bin/python

str = "EOY XF, AY VMU M UKFNY TOY YF UFWHYKAXZ EAZZHN. UFWHYKAXZ ZNMXPHN. UFWHYKAXZ EHMOYACOI. VH'JH EHHX CFTOUHP FX VKMY'U AX CNFXY FC OU. EOY VH KMJHX'Y EHHX IFFQAXZ MY VKMY'U MEFJH OU."

repl = {
    "H": "e",
    "J": "v",
    "V": "w",
    "E": "b",
    "X": "n",
    "M": "a",
    "U": "s",
    "F": "o",
    "K": "h",
    "Y": "t",
    "A": "i",
    "N": "r",
    "W": "m",
    "Z": "g",
    "O": "u",
    "C": "f",
    "T": "c",
    "I": "l",
    "P": "d",
    "Q": "k"
}

decrypted = ""
for c in str:
    if c in repl.keys():
        decrypted += repl[c]
    else:
        decrypted += c
        
print str
print decrypted