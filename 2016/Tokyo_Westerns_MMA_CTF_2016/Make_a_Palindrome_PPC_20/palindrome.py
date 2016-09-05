#!/usr/bin/env python

# sample palindroms from stage 2:
#
# ir u u rie zilwp p k wliz te k
# q qbqqbbqqb bbqqqqb qbbqqbbqqbqqbqqqqb q bqb bqbbq qqbbbqqqqbq b q
# ccucuucc cuuccc ccccu ucccuucuc cuuuuu ccu uc uccuc cccucu uccc
# rryyyy r yy yyr ryyyyyryy ryyy ryrrryr rrr yrrryrr yyyyy
# d i zgb vy pxt v yvb it bhbvbgzdb xp


import random
import socket
import sys

def check_palindrom(s):
    is_palindrom = True
    first = s[:len(s)/2]

    if len(input_words) % 2 != 0:
        second = s[len(s):len(s)/2:-1]
    else:
        second = s[len(s):len(s)/2-1:-1]
    return first == second

def randomize_words(w):    
    words = w.split(" ")
    words_len = len(words)
    rand_words = []
    for i in range(0, words_len):
        index = words_len + 1
        while index > words_len:
            index = random.randint(0, words_len - 1)

        rand_words.append(words.pop(index))
        words_len = len(words)
    return (" ").join(rand_words)


def perform_atempt(words):
    atempts = 1
    found = False
    while found != True:
        palindrom = randomize_words(words)
        # print palindrom
        found = check_palindrom(palindrom.replace(" ",""))
        # print "check {}".format(atempts)
        atempts += 1    

    print "Found after {} atempts: {} \n".format(atempts, palindrom)
    return palindrom.split(" ")




host = 'ppc1.chal.ctf.westerns.tokyo'
if len(sys.argv) > 1:
    host = sys.argv[1]
port = 31111
if len(sys.argv) > 2:
    host = int(sys.argv[2])

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

client_file = client.makefile('b')

while client_file.readline().strip() != "Let's play!":
    pass

client_file.readline()
for case in range(0, 30):
    client_file.readline()
    
    input_words = client_file.readline().split()[2:]
    input_words = " ".join(input_words)
    print "\n[+] {}".format(input_words)
    answer = perform_atempt(input_words)
    
    client_file.write(' '.join(answer) + "\n")
    client_file.flush()
    ret = client_file.readline()[8:-1]
    print(ret)
    if 'Wrong Answer' in ret:
        print(client_file.readline())
        sys.exit(1)
