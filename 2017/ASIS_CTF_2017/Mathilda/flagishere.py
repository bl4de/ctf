#!/usr/bin/env python
import requests

resp = requests.get('http://178.62.48.181:80', headers={
    'Host':'flagishere',
    'Referer': 'tilda'
})

print resp.content