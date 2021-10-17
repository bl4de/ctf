#!/usr/bin/env python3
from binascii import unhexlify as u


def get_flag():
    flag = '666c61677b30682d6c6f6f6b2d612d466c61477d'
    return u(flag).decode('utf-8')


print(f'The flag is: {get_flag()}')
