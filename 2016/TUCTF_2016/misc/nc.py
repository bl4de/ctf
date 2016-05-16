#!/usr/bin/python
import socket

import time

morseAlphabet = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    " ": "/"
}
inverseMorseAlphabet = dict((v, k) for (k, v) in morseAlphabet.items())


def con(remote_host):
    # create TCP socket
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect(remote_host)

    return conn


def sendsomething(conn, data):
    conn.send(data)


def receivesomething(conn, howmany):
    return conn.recv(howmany)


def round1():
    c = con(('146.148.102.236', 24069))

    sendsomething(c, "text")
    time.sleep(1)
    r = receivesomething(c, 1024)

    line = r.split("\n")[5]

    morse = str.replace(line, "What is", "").replace("decrypted?", "").split(
        " ")

    res = ""
    for i in morse:
        if i:
            res += inverseMorseAlphabet[i]

    sendsomething(c, res.lower())
    time.sleep(1)
    r = receivesomething(c, 1024)

    return r


def main():
    print round1()


main()
