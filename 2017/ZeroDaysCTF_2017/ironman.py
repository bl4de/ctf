#!/usr/bin/env python

import socket

def get_expr(resp):
    resp = resp.split('\n')
    print resp
    return resp[13]

def parse_expr(expr):
    expr = expr.split('+')
    x = int(expr[0])
    y = int(expr[1])
    z = int(expr[2])

    return x+y+z

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(('54.246.249.189', 2017))
resp = conn.recv(4096)
print resp

