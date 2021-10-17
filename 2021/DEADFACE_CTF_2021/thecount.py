# connect to code.deadface.io:50000
# read word
# count based on position
# send result
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.connect(('code.deadface.io', 50000))
    word = sock.recv(1024).decode('utf-8').split(':')[3].strip()
    sum = 0
    for c in word:
        sum += (ord(c) - 97)

    print(sum)

    answer = str(sum)
    sock.send(answer.encode('utf-8'))

    resp = sock.recv(1024)
    print(resp)

except Exception as e:
    print(e)
