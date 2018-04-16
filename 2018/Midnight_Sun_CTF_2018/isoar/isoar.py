#!/usr/bin/python
import requests

urls = open('urls', 'r').readlines()

for i in urls:
    resp = requests.get(i.strip(), headers={
        "Accept": "application/json",
        "Host": "web.midnightsunctf.se:8000",
        "Referer": "http://web.midnightsunctf.se:8000/",
        "USer-Agent": "Stack"
    })
    print resp.content
