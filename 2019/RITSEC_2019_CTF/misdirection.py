#!/usr/bin/env python3

import requests

flag = ""
iterations = 0

r = requests.get('http://ctfchallenges.ritsec.club:5000/',
                 allow_redirects=False)

while r.headers['Location']:
    # extract last part of url as flag character
    c = r.headers['Location'][-1:]
    flag = flag + r.headers['Location'][-1:]

    print(flag)
    # exit if we reach end of flag
    if c == '}':
        break

    r = requests.get(r.headers['Location'],
                     allow_redirects=False)

