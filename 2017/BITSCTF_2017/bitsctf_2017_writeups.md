# BITSCTF 2017 

This writeup contains my solutions for some challenges from BITSCTF 2017.

## Banana Princess, Crypto 20pts

**The princess has been kidnapped! It is up to you to rescue her now, with the help of the minions. They have provided you with a letter (which may or may not have touched the kidnappers hands on its way to you).**

**Authors - Speeeddy, Blaze**

We get file ```MinionQuest.pdf```, but when we try to open it, it occurs file is corrupted.
Hex editor reveals it has structure which looks like legitimate PDF file, however it's encoded in some way.

When I opened valid PDF file an compared with ```MinionQuest.pdf``` I've spotted obvious differences:

![banana-princess]
(assets/banana1.png)

Let's compare first 128 words of both files:

```
bl4de:~/hacking/ctf/2017/BITSCTF_2017/Banana_Princess $ xxd -l 128 MinionQuest.pdf
00000000: 2543 5153 2d31 2e35 0d25 e2e3 cfd3 0d0a  %CQS-1.5.%......
00000010: 3420 3020 626f 770d 3c3c 2f59 7661 726e  4 0 bow.<</Yvarn
00000020: 6576 6d72 7120 312f 5920 3433 3031 3930  evmrq 1/Y 430190
00000030: 2f42 2036 2f52 2034 3034 3334 332f 4120  /B 6/R 404343/A
00000040: 312f 4720 3432 3939 3931 2f55 205b 2035  1/G 429991/U [ 5
00000050: 3736 2031 3535 5d3e 3e0d 7261 7162 6f77  76 155]>>.raqbow
00000060: 0d20 2020 2020 2020 2020 2020 2020 2020  .
00000070: 2020 0d0a 6b65 7273 0d0a 3420 3134 0d0a    ..kers..4 14..
bl4de:~/hacking/ctf/2017/BITSCTF_2017/Banana_Princess $ xxd -l 128 ~/Programowanie/manuals/promises_cheat_sheet.pdf
00000000: 2550 4446 2d31 2e33 0a25 c4e5 f2e5 eba7  %PDF-1.3.%......
00000010: f3a0 d0c4 c60a 3420 3020 6f62 6a0a 3c3c  ......4 0 obj.<<
00000020: 202f 4c65 6e67 7468 2035 2030 2052 202f   /Length 5 0 R /
00000030: 4669 6c74 6572 202f 466c 6174 6544 6563  Filter /FlateDec
00000040: 6f64 6520 3e3e 0a73 7472 6561 6d0a 7801  ode >>.stream.x.
00000050: ad9d db72 24c7 7186 effb 29fa 920a 8bc3  ...r$.q...).....
00000060: 3e1f 14e1 0b91 1223 ecb0 2224 72c3 8eb0  >......#.."$r...
00000070: e90b 10c4 8a2b 6181 5d00 24c5 c7f4 0be8  .....+a.].$.....
```

