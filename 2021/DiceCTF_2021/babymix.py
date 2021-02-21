#!/usr/bin/python

password = ''.join([
    'A',    # 0x00
    'A',    # 0x01
    'A',    # 0x02
    'A',    # 0x03
    'A',    # 0x04
    'A',    # 0x05
    'A',    # 0x06
    'A',    # 0x07
    'P',    # 0x08
    'A',    # 0x09
    'd',    # 0x0a
    'A',    # 0x0b
    '<',    # 0x0c
    'A',    # 0x0d
    'A',    # 0x0e
    'A',    # 0x0f
    'A',    # 0x10
    '/',    # 0x11
    'A',    # 0x12
    'A',    # 0x13
    'A',    # 0x14
    'u',    # 0x15
    'A',    # 0x16
    'A',    # 0x17
    'A',    # 0x18
    'A',    # 0x19
    'A',    # 0x1a
    'A',    # 0x1b
    'A'    # 0x1c
])

def found(passwd):
    print("\nPassword found: {}".format(passwd))
    exit(0)

# 1
def check815546(passwd):
    if ord(passwd[0x8]) + ord(passwd[0xc]) + ord(passwd[0xc]) - + ord(passwd[0x11]) == 153:
        check921708(passwd)
    else:
        print('check815546: not found')
        return False

# 2
def check921708(passwd):
    if (ord(passwd[0x2]) ^ ord(passwd[0x13])) + ord(passwd[0x15]) + ord(passwd[10]) == 217:
        found(passwd)
    else:
        print('check921708: not found')
        return False


def main():
    print(check815546(password))


main()