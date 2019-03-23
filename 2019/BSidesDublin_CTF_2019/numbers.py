#!/usr/bin/env python

# flag{5;1;19;25;0;1;19;0;15;14;5;0;20;23;15;0;20;8;18;5;5}

s = "5;1;19;25;0;1;19;0;15;14;5;0;20;23;15;0;20;8;18;5;5".split(";")

for step in range(10,100):
    flag = ''
    for c in s: 
        ascii = int(c) + step
        flag  = flag + chr(ascii)
    print flag