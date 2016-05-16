#!/usr/bin/python
import base64
import hashlib

# Generate SHA:
# sha256(b64(username) + "." + b64(cookie) + "." + b64(token))

username = "DuckDuckGoose"
token = "d4rkw1ng"
cookie = '{"username":"DuckDuckGoose","admin":1}'

print hashlib.sha256(base64.b64encode(username) + "." + base64.b64encode(
    cookie) + "." + base64.b64encode(token)).hexdigest()

# Result: d626290acdc6a948a5f2b5c2850730f4e4b2bdbd36da01226a192985d20d787d
