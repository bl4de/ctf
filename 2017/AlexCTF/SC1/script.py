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
# bl4de:~/hacking/ctf/2017/AlexCTF/SC1 $ ./script.py
# 7599075891543951372675463864679945221178182504800701267948627140
# 0
# 74578530942050417609284440054047
# 0
# (...lot of similar output...)
# 36632663643271902140682355297787
# 074025097248713696435826835588817521727202555382307526929910166
# 281165729405099941932587388148564
# 551933140171975251953737762019661
# Well no human got time to solve 500 ridiculous math challenges
# Congrats MR bot!
# Tell your human operator flag is: ALEXCTF{1_4M_l33t_b0t}
