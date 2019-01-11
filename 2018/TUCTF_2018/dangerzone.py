#!/usr/bin/python
# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (default, Oct  2 2018, 11:42:04)
# [GCC 4.2.1 Compatible Apple LLVM 10.0.0 (clang-1000.11.45.2)]
# Embedded file name: ./dangerzone.py
# Compiled at: 2018-11-22 07:14:11
import base64


def reverse(s):
    return s[::-1]


def b32decode(s):
    return base64.b32decode(s)


def reversePigLatin(s):
    return s[-1] + s[:-1]


def rot13(s):
    return s.decode('rot13')


def main():
    print 'Something Something Danger Zone'
    return '=YR2XYRGQJ6KWZENQZXGTQFGZ3XCXZUM33UOEIBJ'


if __name__ == '__main__':
    s = main()
    s = reverse(s)
    s = b32decode(s)
    s = reversePigLatin(s)
    s = rot13(s)
    
    print s
# okay decompiling dangerzone.pyc
