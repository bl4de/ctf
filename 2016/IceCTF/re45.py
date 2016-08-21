#!/usr/bin/python

f = """
0804851b         mov        al, 0x49
0804851d         mov        al, 0x63
0804851f         mov        al, 0x65
08048521         mov        al, 0x43
08048523         mov        al, 0x54
08048525         mov        al, 0x46
08048527         mov        al, 0x7b
08048529         mov        al, 0x6c
0804852b         mov        al, 0x6f
0804852d         mov        al, 0x6f
0804852f         mov        al, 0x6b
08048531         mov        al, 0x5f
08048533         mov        al, 0x6d
08048535         mov        al, 0x6f
08048537         mov        al, 0x6d
08048539         mov        al, 0x5f
0804853b         mov        al, 0x49
0804853d         mov        al, 0x5f
0804853f         mov        al, 0x66
08048541         mov        al, 0x6f
08048543         mov        al, 0x75
08048545         mov        al, 0x6e
08048547         mov        al, 0x64
08048549         mov        al, 0x5f
0804854b         mov        al, 0x69
0804854d         mov        al, 0x74
0804854f         mov        al, 0x7d
"""

flag = ""
for c in f.split("\n"):
    flag = flag + chr(int(c[-4:],16)) if c != "" else flag
            
print flag