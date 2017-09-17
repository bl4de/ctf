#!/usr/bin/env python
import hashlib
import sys

def xor(s1,s2):
    retval = ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))
    print "\t[+] in xor(s1,s2): retval = {}".format(retval)
    return retval

def repeat(s, l):
    retval = (s*(int(l/len(s))+1))[:l]
    print "\t[+] in repeat(s,l): retval = {}".format(retval)
    return retval

key = "key" # sys.argv[1]
plaintext = "plain" # sys.argv[2] + key


print "[+] Phase 0: args: key->{}  plain->{}".format(key,plaintext)
print "[+] Phase 1: palintext: {}".format(plaintext)


plaintext += hashlib.md5(plaintext).hexdigest()

print "[+] Phase 2: palintext+md5(plaintext): {}".format(plaintext)

processedkey = repeat(key, len(plaintext))
print "[+] Phase 3: create processedkey (from repeat(key, len(plaintext))): {}".format(processedkey)


cipher = xor(plaintext, processedkey)



print "\n\n\n" + cipher.encode('hex')
