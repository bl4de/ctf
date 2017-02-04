# AlexCTF 2017 

This writeup contains my solutions for some challenges from AlexCTF 2017, including Reverse Engineering, Crypto and Forensic categories.

Unfortunately, AlexCTF did not contain Web, which is my favorite CTF category - even though I had a lot of fun as I had to code couple of handy Python scripts :)


## RE1: Gifted, 50pts (Reverse)

We get ```gifted``` file contains ELF binary.

Solution:

![gifted]
(assets/gifted.png)

## CR1: Ultracoded, 50pts (Crypto)

**Fady didn't understand well the difference between encryption and encoding, so instead of encrypting some secret message to pass to his friend, he encoded it!
Hint: Fady's encoding doens't handly any special character**

We get ```zero-one``` file contains ZERO and ONE words.
First thing which came to my mind was it's simple binary string and it was correct.

Solution:

```python
#!/usr/bin/env python
import base64

print "\n[+] AlexCTF 2017 CR1: Ultracoded | by bl4de (Stack)"
print "\n[+] original content"
zeroone = open('zero_one', 'rw').read()

print zeroone

print "\n\n[+] change ZERO to 0 and ONE to 1"
zeroone = zeroone.replace('\n', '').replace(
    ' ', '').replace('ZERO', '0').replace('ONE', '1')

print zeroone

print "\n[+] split into 8-bit chunks; convert to decimal, then to ASCII"
zeroone_decoded = ''
for x in range(0, len(zeroone), 8):
    # print chr(int(zeroone[x:8], 2))
    zeroone_decoded += chr(int(zeroone[x:x + 8], 2))

print zeroone_decoded

print "\n\n[+] it's Base64 encoded Morse string"
print base64.b64decode(zeroone_decoded)

# .- .-.. . -..- -.-. - ..-. - .... .---- ..... --- .---- ... --- ..... ..- .--. ...-- .-. --- ..... . -.-. .-. ...-- - --- - -..- -
# using eg. http://morsecode.scphillips.com/translator.html
# Morse --> ALEXCTFTH15O1SO5UP3RO5ECR3TOTXT

print "\n\n[+] the flag after Morse encoded"
print "ALEXCTFTH15O1SO5UP3RO5ECR3TOTXT"

print "\n\n[+] the flag is: ALEXCTF{TH15_1S_5UP3R_5ECR3T_TXT}"
```

Output:

![zero-one]
(assets/zero-one.png)

## Fore1: Hit the core, 50pts

We get ```fore1.core``` file, which is memory dump from binary file named ```code```. However, we did not get ```code``` itself, so we can't read core file with ```gdb```:

```
bl4de:~/hacking/ctf/2017/AlexCTF/Fore1 $ file fore1.core
fore1.core: ELF 64-bit LSB core file x86-64, version 1 (SYSV), SVR4-style, from './code'
```

Simple ```strings``` call reveals something which looks like encoded flag:

```
bl4de:~/hacking/ctf/2017/AlexCTF/Fore1 $ strings fore1.core | grep {
cvqAeqacLtqazEigwiXobxrCrtuiTzahfFreqc{bnjrKwgk83kgd43j85ePgb_e_rwqr7fvbmHjklo3tews_hmkogooyf0vbnk0ii87Drfgh_n kiwutfb0ghk9ro987k5tfb_hjiouo087ptfcv}
h{9e
X{9e
8{9e
0{9e
X{9e
```

We can notice capital A,L,E,X,C,T,F chars at the beginning, each one followed by four random ASCII chars. This is ```ALEXCTF``` string, which began every flag in AlexCTF

Solution:

```python
#!/usr/bin/env python

encoded_flag = 'cvqAeqacLtqazEigwiXobxrCrtuiTzahfFreqc{bnjrKwgk83kgd43j85ePgb_e_rwqr7fvbmHjklo3tews_hmkogooyf0vbnk0ii87Drfgh_n kiwutfb0ghk9ro987k5tfb_hjiouo087ptfcv}'

# cut first 3 chars and create list
encoded_flag = encoded_flag[3:]

print ''.join([encoded_flag[x]
               for x in range(0, len(encoded_flag)) if x % 5 == 0])

```

And we get the flag:

```
bl4de:~/hacking/ctf/2017/AlexCTF/Fore1 $ ./htc.py
ALEXCTF{K33P_7H3_g00D_w0rk_up}
```

## SC1: Math bot, 100pts

**It is well known that computers can do tedious math faster than human.**

**nc 195.154.53.62 1337**

After connect to the server, there's welcome screen with some mathematical expression to solve. Expression is not something we can calculate on the fly.

After first response, next expression is presented and so forth.
It's clear that manual solution to this is not possible :), so some scripting has to be involved.

![SC1]
(assets/scripting1.png)

My solution contains simple expression parser, which extracts and calculates each presented Question and sends response back.

```python
#!/usr/bin/env python
#
# SC1: Math bot
# 100

# It is well known that computers can do tedious math faster than human.

# bl4de:~/hacking/ctf/2017/AlexCTF/SC1 $ nc 195.154.53.62 1337
#                 __________
#          ______/ ________ \______
#        _/      ____________      \_
#      _/____________    ____________\_
#     /  ___________ \  / ___________  \
#    /  /XXXXXXXXXXX\ \/ /XXXXXXXXXXX\  \
#   /  /############/    \############\  \
#   |  \XXXXXXXXXXX/ _  _ \XXXXXXXXXXX/  |
# __|\_____   ___   //  \\   ___   _____/|__
# [_       \     \  X    X  /     /       _]
# __|     \ \                    / /     |__
# [____  \ \ \   ____________   / / /  ____]
#      \  \ \ \/||.||.||.||.||\/ / /  /
#       \_ \ \  ||.||.||.||.||  / / _/
#         \ \   ||.||.||.||.||   / /
#          \_   ||_||_||_||_||   _/
#            \     ........     /
#             \________________/

# Our system system has detected human traffic from your IP!
# Please prove you are a bot
# Question  1 :
# 228043638282408858648301419721978 - 310465980175195857961096584143820 =


import socket


def get_expr(resp):
    resp = resp.split('\n')
    return resp[len(resp) - 2]


def parse_expr(expr):
    expr = expr.split(' ')
    x = int(expr[0])
    y = int(expr[2])
    math = expr[1]
    if math == '+':
        return x + y
    if math == '-':
        return x - y
    if math == '*':
        return x * y
    if math == '/':
        return x / y
    if math == '%':
        return x % y


conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(('195.154.53.62', 1337))
resp = conn.recv(4096)

while 'ALEXCTF' not in resp:
    res = parse_expr(get_expr(resp))
    print res
    conn.send(str(res) + '\n')
    resp = conn.recv(4096)

print resp
```

The output:

```
bl4de:~/hacking/ctf/2017/AlexCTF/SC1 $ ./script.py
7599075891543951372675463864679945221178182504800701267948627140
0
74578530942050417609284440054047
0

(...lot of similar output...)

36632663643271902140682355297787
074025097248713696435826835588817521727202555382307526929910166
281165729405099941932587388148564
551933140171975251953737762019661
Well no human got time to solve 500 ridiculous math challenges
Congrats MR bot!
Tell your human operator flag is: ALEXCTF{1_4M_l33t_b0t}
```

