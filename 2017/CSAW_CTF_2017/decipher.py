#!/usr/bin/env python

import hashlib
import sys


def dexor(s1,s2):
    # print zip(s1,s2)

    unzipedcipher = [s2[i:i+2] for i in range(0, len(s2), 2)]
    # print chr(int(unzipedcipher[0], 16))

    retval = ''.join(ord(a) ^ chr(int(b,16)) for a,b in (s1,unzipedcipher))
    
    # print "\t[+] in dexor(s1,s2): retval = {}".format(retval)
    # return retval

def repeat(s, l):
    retval = (s*(int(l/len(s))+1))[:l]
    print "\t[+] in repeat(s,l): retval = {}".format(retval)
    return retval

key = "key"
plaintext = "plain"

cipher = "1b0918020b120e1c485f511d5d061f08501b09564d5d52415d01495b574c0e524f0855410a5d4f09"
processedkey = "plainkey144d6cfc5bb346786d0025e76c08a86b"



decipher = dexor(processedkey,cipher)

print "\n [+] DECODE phase 1: xor(cipher, processedkey))  {}".format(decipher)
