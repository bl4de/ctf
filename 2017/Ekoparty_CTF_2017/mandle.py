#!/usr/bin/env python
import socket

# malbolge.ctf.site 40111

code = """
D'`A_#"=6ZGX2h65uR?rr`.L]8$G(4EfedcyQ=<;)([Zp6WVlqpih.ONjiha'H^]\[Z~^W\[ZYRvVOTSLp3INGFjJ,BAe?'=<;_?8=<;4X216543,P0p(-,+*#G'&f|{"y?}|ut:[qvutml2poQPlejc)gfedFb[!_X]V[ZSRvP8TSLpJ2NMLEDhU
"""

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('malbolge.ctf.site', 40111))

resp = sock.recv(2048)

sock.send(code)
resp = sock.recv(4096)

print resp

