#!/usr/bin/python

import requests
import re
import time

rainbow_tables = open("rainbow_tables_with_hashes.txt").readlines()

def sendgo():
    print "\n[*] RESTART RANDOMS by sending ?go=1 parameter in GET"
    resp = requests.get('http://202.120.7.202:8888/?go=1')
    if resp.content != "":
        return resp.content[-32:]
    
def gethash():
    resp = requests.get('http://202.120.7.202:8888/')
    if resp.content != "":
        current = re.search("\d+", resp.content)
        return current.group(0)
        

def iterate(h):
    cntr = 0
    for line in rainbow_tables:
        cntr += 1
        if h in line:
            print "[*] " + line
            v = line.split(" ")[2].split(",")
            url = 'http://202.120.7.202:8888/?check[]={}&check[]={}&check[]={}&check[]={}&check[]={}'.format(v[0],v[1],v[2],v[3],v[4])
            print "[*] check url is {}".format(url)
            resp = requests.get(url)
            print "\n[*] FLAG IS: {}".format(resp.content)
            exit(0)
    print "[*] verified {} sequences, not found".format(cntr)
    return True
    
sendgo()
x = True
while x:
    h = gethash()
    print "[*] start looking rand() sequence by hash " + h
    x = iterate(h)
    
    