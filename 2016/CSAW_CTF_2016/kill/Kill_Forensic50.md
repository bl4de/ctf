# Kill (Forensic, 50pts)

## Problem

Is kill can fix? Sign the autopsy file? [pcapng file attachement]

## Solution

This problem was quite weird - we got _kill.pcapng_ file, but when I've tried to open it in Wireshark, it refused with error because file was not in PCAPNG format.

When I checked filetype in the console it was totally new and unknown for me:

```
$ file kill.pcapng
kill.pcapng: Dyalog APL version 221 .170
```

I dig a little and found that it refers to (probably) APL language. I've started from ```head``` command and immediately spotted some plaintext ASCII strings:

```
$ head -n 10 kill.pcapng

��ݪ�M<+��������/Mac OS X 10.11.6, build 15G1004 (Darwin 15.6.0)4Dumpcap 1.12.4 (v1.12.4-0-gb4861da from master-1.12)�`vmnet8
                                        /Mac OS X 10.11.6, build 15G1004 (Darwin 15.6.0)`\lo0
        /Mac OS X 10.11.6, build 15G1004 (Darwin 15.6.0)\L�;��@A**������PV�����L\�;��@A<<PV�
  )��
   )�Ĭ��PV��\p�;݆@ANN
                    )��PE@��@@#ͬ�����7+����<8�
5�b+pl�;Q�@AJJPV�
                )�E<@@�ˬ�ͬ��7n[��+��q ���
%��5�b+ld�;��@ABB
                 )��PE4%K@@҈������7+�n[�ր@W*i
5�b+%��dx�;�@AVVPV�
                  )�EHY
                       @@����ͬ��7n[��+����
%��5�b+220 (vsFTPd 3.0.2)
xd�;=�@ABB
          )��PE4��@@9
                     ������7+�n[��@T*T
5�b.%��dp�;��AMM
                )��PE?�?@@&y������7+�n[��@To?
5�r�%��USER user
pd�;��ABBPV�
           )�E4Y
                @@�Ǭ�ͬ��7n[��+���U(
%��5�r�d��;[�AddPV�
�@����ͬ��7n[��+��� )�EVY
```
It looked like some communication with vsFTP server (```USER``` is one of FTP command).
Next step was just simple ```strings``` command with some ```grep``` support - and, surprisingly, it was more than enough:


```
$ strings kill.pcapng | grep flag{
=flag{roses_r_blue_violets_r_r3d_mayb3_harambae_is_not_kill}
```

I don't know if it was intended way to resolve this challenge, anyway it worked for me (my favorite quote by Mateusz 'y00ru' Jurczyk from Google Project Zero: "Whatever works, it works" :) ) and I got the flag and 50 points.

