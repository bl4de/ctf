#!/usr/bin/env python

import requests

byte_array = list(range(2048))
for i in range(0, len(byte_array)):
    byte_array[i] = ''

url = "http://167.71.246.232:8080/rabbit_hole.php?page="

resp = requests.get(url + "cE4g5bWZtYCuovEgYSO1")
res = resp.content.split('\n')
# extract byte:
byte = res[0].replace('[','').replace(']','').replace(' ','').replace('\'','').split(',')
byte_pos = int(byte[0])
# add byte to byte_array
byte_array[byte_pos] = byte[1]

while resp.status_code == 200:
# for i in range(0, 10):
    resp = requests.get(url + res[1].strip())
    res = resp.content.split('\n')
    # extract byte:
    byte = res[0].replace('[','').replace(']','').replace(' ','').replace('\'','').split(',')

    if byte[0] == 'end':
        print(byte_array)
        print(''.join(byte_array)) 
        exit(0)
    byte_pos = int(byte[0])
    # add byte to byte_array
    byte_array[byte_pos] = byte[1]
