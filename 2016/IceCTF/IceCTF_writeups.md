# IceCTF 2016 writeups

As most of challenges were trivial to resolve (especially from Stage 1, Stage 2 and most of challenges from Stage 3) I put here just some challenges I had to spend a little more than 30 seconds to 3 minutes :)

--

### Hidden in Plain Sight (RE, 45pts)

#### Challenge

Make sure you take a real close look at it, it should be right there! /home/plain_sight/ or download it here [link]

#### Solution


I've downloaded simple ELF executable and there's a flag hidden somewhere.
_strings_ does not return anything interesting, so I decided to take a look at the source code in Hopper Disassembler. As RE is not my strongest side, I tried to find something obvious, and I was lucky:

![Code]
(assets/re45.png)

There's a list of _mov al, 0xXX_ instructions, obviously handle flag character by character (first three chars was just 'Ice', all flags start from 'IceCTF', so I assumed that this had to be flag). Quick Python script allows me to get the right solution:

```Python
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
```

And there's the flag:

```
bl4de:~/hacking/ctf/2016/IceCTF $ ./re45.py
IceCTF{look_mom_I_found_it}
```

--


