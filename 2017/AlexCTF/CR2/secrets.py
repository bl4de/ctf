#!/usr/bin/env python

msg = '0529242a631234122d2b36697f13272c207f2021283a6b0c79082f28202a302029142c653f3c7f2a2636273e3f2d653e25217908322921780c3a235b3c2c3f207f372e21733a3a2b37263b3130122f6c363b2b312b1e64651b6537222e37377f2020242b6b2c2d5d283f652c2b31661426292b653a292c372a2f20212a316b283c0929232178373c270f682c216532263b2d3632353c2c3c2a293504613c37373531285b3c2a72273a67212a277f373a243c20203d5d243a202a633d205b3c2d3765342236653a2c7423202f3f652a182239373d6f740a1e3c651f207f2c212a247f3d2e65262430791c263e203d63232f0f20653f207f332065262c31683137223679182f2f372133202f142665212637222220733e383f2426386b'

base_key = 'ALEXCTF{HERE_GOES_THE_KEY}'
msg_arr = [int(msg[x:x + 2], 16) for x in range(0, len(msg)) if x % 2 == 0]


for l in 'ABCDEFGHIJKLMNOPQRSTUWVXYZabcdefghijklmnopqrstuwvxyz{}0123456789_-':
    key = base_key  # + l + 'aaaaaaaaaa'
    padded_key = key * int(len(msg) / len(key))
    key_arr = [ord(x) for x in list(padded_key)]
    decrypted = ''
    for x in range(0, len(msg_arr)):
        decrypted = decrypted + chr(msg_arr[x] ^ key_arr[x])

    if 'ncryption scheme' in decrypted:
        print '\nkey fragment: {} \ndecrypted so far:\n{}'.format(key,
                                                                  decrypted)


# Dear Friend, Rkix<tgSr.^<Wnderstood my kjs}kkv`s<Wsed One time
# vbd+ynmLn~cuMn scheme, I hcbro<tf_c.~his the only eh`rrltgQy.zyVhod that
# is mgwhnqazWto{p[ proven to be&mo<c|_terxever if the kcz bo
# e[gz7oGcure, Let Me mmo|<ihnab<Cgree with me rl ~oe.Jgd<Gncryption
# schcne+}ly_n}9
