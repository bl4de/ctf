# AlexCTF 2017 

This writeup presents my solutions for AlexCTF 2017 challenges including RE, Crypto and Forensic categories.

Unfortunately, AlexCTF did not provide any Web challenges, which is my favorite CTF category - even though I had a lot of fun as I had to code couple of handy Python scripts and learn some new cryptography concepts :)


## RE1: Gifted, 50pts (Reverse)

We get ```gifted``` file contains ELF binary.

Solution is trivial, just had to execute ```strings``` command and grep correct line:

![gifted]
(assets/gifted.png)

The flag was:
**AlexCTF{Y0u\_h4v3\_45t0n15h1ng\_futur3\_1n\_r3v3r5ing}**


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

## CR2: Many time secrets, 100pts (Crypto)

**This time Fady learned from his old mistake and decided to use onetime pad as his encryption technique, but he never knew why people call it one time pad!**

We get a file with a message. After some investigation and couple of quick tries with ASCII codes I identified it as a string contains 284 characters.

As challenge description mentioned about one-time pad, I found basic information about this method of encryption (https://en.wikipedia.org/wiki/One-time_pad):

```
In cryptography, the one-time pad (OTP) is an encryption 
technique that cannot be cracked, but requires the use of 
a one-time pre-shared key the same size as the message being sent.
In this technique, a plaintext is paired with a random secret key 
(also referred to as a one-time pad). Then, each bit or character of 
the plaintext is encrypted by combining it with the corresponding 
bit or character from the pad using modular addition.

```
So the solution was to find the key Fady used to encrypt his message. I've started from ```FADY``` and quickly realized I'm on the right path to find solution as some readable word appears at the beginning of encrypted string.

After some guessing, I decided to try string contains actual CTF name - ```ALEXCTF``` - and the beginning of encrypted message changed into ```Dear Fr```. BINGO!

Unfortunately, the rest of the key was the simple bruteforcing, character by character. I've created simple script for this, here's how it looks like after key contained twelve characters:

```python
#!/usr/bin/env python

msg = '0529242a631234122d2b36697f13272c207f2021283a6b0c79082f28202a302029142c653f3c7f2a2636273e3f2d653e25217908322921780c3a235b3c2c3f207f372e21733a3a2b37263b3130122f6c363b2b312b1e64651b6537222e37377f2020242b6b2c2d5d283f652c2b31661426292b653a292c372a2f20212a316b283c0929232178373c270f682c216532263b2d3632353c2c3c2a293504613c37373531285b3c2a72273a67212a277f373a243c20203d5d243a202a633d205b3c2d3765342236653a2c7423202f3f652a182239373d6f740a1e3c651f207f2c212a247f3d2e65262430791c263e203d63232f0f20653f207f332065262c31683137223679182f2f372133202f142665212637222220733e383f2426386b'

base_key = 'ALEXCTF{HERE'
msg_arr = [int(msg[x:x + 2], 16) for x in range(0, len(msg)) if x % 2 == 0]


for l in 'ABCDEFGHIJKLMNOPQRSTUWVXYZabcdefghijklmnopqrstuwvxyz{}0123456789_':
    key = base_key + l
    padded_key = key * (len(msg) / len(key))
    key_arr = [ord(x) for x in list(padded_key)]
    decrypted = ''
    for x in range(0, len(msg_arr)):
        decrypted = decrypted + chr(msg_arr[x] ^ key_arr[x])

    if 'Dear Friend, ' in decrypted:
		print '\nkey fragment: {} \ndecrypted so far:\n{}'.format(key,
                                                          decrypted)

```

Actual result was:


```
bl4de:~/hacking/ctf/2017/AlexCTF/CR2 $ ./secrets.py

key fragment: ALEXCTF{HERE
decrypted so far:
Dear Friend,>_btc+fZ`9I8Djpc~v[aQ~ ~p:rebaEwh7{dm<Pq}gDq}`zx<chZ;hnvj~isFi~~ytjR!=X1qYfre:alas(xk&`z7ij}#Le}mrl~rkceyie-StL{f`4rdd[.Wi `czasjvhjGblgA proven to b{+drd+qAlyre|abc~%Fhnhv)qzu1|W<frj~)o@amqF'1X[})Zx<xgQl:ok$jah:H`Ehx1fnCe=|t9Hh tip$toab?cgjedrljLe1g]gpe2r}ggr~
bl4de:~/hacking/ctf/2017/AlexCTF/CR2 $ ./secrets.py

key fragment: ALEXCTF{HERE_
decrypted so far:
Dear Friend, Rkix<tgSr.^<Wnderstood my kjs}kkv`s<Wsed One time vbd+ynmLn~cuMn scheme, I hcbro<tf_c.~his the only eh`rrltgQy.zyVhod that is mgwhnqazWto{p[ proven to be&mo<c|_terxever if the kcz bo e[gz7oGcure, Let Me mmo|<ihnab<Cgree with me rl ~oe.Jgd<Gncryption schcne+}ly_n}9
bl4de:~/hacking/ctf/2017/AlexCTF/CR2 $ ;2B
```

![zero-one]
(assets/onetimepad.png)


The final flag, used as an encryption key: **ALEXCTF{HERE\_GOES\_THE\_KEY}**

```
key fragment: ALEXCTF{HERE_GOES_THE_KEY}
decrypted so far:
Dear Friend, This time I understood my mistake and used One time pad
 encryption scheme, I heard that it is the only encryption method 
 that is mathematically proven to be not cracked ever if the key is 
 kept secure, Let Me know if you agree with me to use this 
 encryption scheme always.
```

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

