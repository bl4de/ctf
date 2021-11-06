#!/usr/bin/env python3
import string


def load_strings() -> list[str]:
    ''' 
        loads file with XOR-ed strings
    '''
    strings = open('flags.txt', 'r').readlines()
    return strings


def xor_string(s: str) -> str:
    '''
        perform XOR on string with one character at the time
        as long as three first characters are equal to 'dam'
        then xors entire string and returns (hopefuly) flag
    '''

    s_len = len(s)
    c_arr = [s[iter] + s[iter + 1] for iter in range(0, s_len, 2)]

    for x in string.printable:
        xored_s = ''
        for c in c_arr[0:3]:
            xored_s += chr(int(c, 16) ^ ord(x))

        if xored_s == 'dam':
            print(
                "[+] Found correct string: {} \n   and XOR character is: {}".format(s, x))
            xored_s = ''
            for c in c_arr:
                xored_s += chr(int(c, 16) ^ ord(x))
            return(xored_s)
    return 'NO_FLAG'
    

if __name__ == '__main__':

    strings = load_strings()

    for s in strings:
        s = s.strip()
        xored_s = xor_string(s)
        print(xored_s)
