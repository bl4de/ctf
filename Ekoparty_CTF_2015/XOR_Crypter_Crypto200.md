### XOR Crypter - Crypto 200pts

## Problem


Description: The state of art on encryption, can you defeat it?
CjBPewYGc2gdD3RpMRNfdDcQX3UGGmhpBxZhYhFlfQA=

## Solution

We get Python script used for encrypt the flag. Output of this script is Base64 string contains encrypted flag (CjBPewYGc2gdD3RpMRNfdDcQX3UGGmhpBxZhYhFlfQA=)

```python
import struct
import sys
import base64

if len(sys.argv) != 2:
    print "Usage: %s data" % sys.argv[0]
    exit(0)

data = sys.argv[1]
padding = 4 - len(data) % 4
if padding != 0:
    data = data + "\x00" * padding

result = []
blocks = struct.unpack("I" * (len(data) / 4), data)
for block in blocks:
    result += [block ^ block >> 16]

output = ''
for block in result:
    output += struct.pack("I", block)

print base64.b64encode(output)
```

To resolve this, we have to create "decrypter".

Here's my sample solution for this, maybe not state-of-the-art, but I was able to get the flag :)


```python
#!/usr/bin/env python

import struct
import sys
import base64

data = base64.b64decode(sys.argv[1])
padding = 4 - len(data) % 4

if padding != 0:
    data = data + "\x00" * padding

print data

i = 0
padding = 4
output = ''
result = ''
while i < len(data):
    junk = data[i:i + padding]
    print i, padding
    output = struct.unpack("I", junk)
    for s in output:
        r = s ^ s >> 16
        result += struct.pack("I", r)
    i += 4

print result
 
```


And here's output with flag:

```
$ ./test.py CjBPewYGc2gdD3RpMRNfdDcQX3UGGmhpBxZhYhFlfQA=
 
0O{♠♠sh↔☼ti1‼_t7►_u♠→hi▬ab◄e}
0 4
4 4
8 4
12 4
16 4
20 4
24 4
28 4
32 4
EKO{unshifting_the_unshiftable}
```
