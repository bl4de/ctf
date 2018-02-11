#!/usr/bin/python

import jwt

tries = 0
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjpudWxsfQ.XtOMOm8hQojkGZCCpRnu1S09R5HTnUKdaPRQBAt_Wuc"

alphabet = "01234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

sl = 5
l = len(alphabet)
t = pow(l, sl)
print "alphabet lenght: {}, secret length: {}; total number of tries: {}".format(l, sl, t)

for a in alphabet:
    for b in alphabet:
        for c in alphabet:
            for d in alphabet:
                for e in alphabet:
                    tries += 1
                    secret = a + b + c + d + e
                    # print secret
                    encoded = jwt.encode({'user': None}, secret, algorithm='HS256')

                    if encoded == token:
                        print "secret found!!! {}".format(secret)
                        exit(0)
                    if tries % 1000000 == 0:
                        print "{} tries so far, continuing...".format(tries)

print "I've tried {} secrets, but the right one not found :(".format(tries)


# with open('/Users/bl4de/hacking/dictionaries/crackstation.txt', 'r') as f:
#     for secret in f:
#         tries += 1
#         secret = secret.strip()
#         encoded = jwt.encode({'user': None}, secret, algorithm='HS256')

#         if encoded == token:
#             print "secret found!!! {}".format(secret)
#             exit(0)
#         if tries % 1000000 == 0:
#             print "{} tries so far, continuing...".format(tries)

# print "I've tried {} secrets, but the right one not found :(\nTry
# another dictionary... :(".format(tries)
