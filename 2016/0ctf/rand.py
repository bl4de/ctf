#!/usr/bin/python
import requests
import re
import time

rainbow_tables = open("rainbow_tables.txt").readlines()

def sendgo():
    print "\n\n[*] RESTART RANDOMS by sending ?go=1 parameter in GET"
    resp = requests.get('http://202.120.7.202:8888/?go=1')
    if resp.content != "":
        resp = requests.get('http://202.120.7.202:8888')
        return resp.content != "timeout"
    
    
def getn():
    print "\n[*] get actual rand() val from server"
    resp = requests.get('http://202.120.7.202:8888')
    if resp.content.startswith("timeout"):
        print "\n\n[*] TIMEOUT\n\n"
        return sendgo()        
    current = re.search("\d+", resp.content)
    return current.group(0)


# run Forest, run!

if sendgo():
    n = getn()
    ts = time.time()
    print "[*] let's go!"
    while n > 0:
        print "[*] n value = {}".format(n)
        print "[*] total time - {} sec.".format((str)(time.time() - ts))
        print "[*] search rainbow tables for n and n+1 ... n+5"
        for line in rainbow_tables:
            if line.startswith(n):
                print "[*] " + line
                v = line.split(" ")[1].split(",")
                url = 'http://202.120.7.202:8888/?check[]={}&check[]={}&check[]={}&check[]={}&check[]={}'.format(v[0],v[1],v[2],v[3],v[4])
                print "[*] check url is {}".format(url)
                resp = requests.get(url)
                print "\n[*] FLAG IS: {}".format(resp.content)
                exit(0)
        n = getn()
        
    print "\n[*] end"