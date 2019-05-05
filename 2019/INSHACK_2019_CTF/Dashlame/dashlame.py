#!/usr/bin/env python

# uncompyle6 version 3.3.2
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.16 (default, Mar  4 2019, 09:01:38)
# [GCC 4.2.1 Compatible Apple LLVM 10.0.0 (clang-1000.11.45.5)]
# Embedded file name: dashlame.py
# Compiled at: 2019-04-16 22:56:53
from Crypto.Cipher import AES
import os
import random
import sys
import sqlite3
import time
import zlib
HEADER = "      /.m.\\\n     /.mnnm.\\                                              ___\n    |.mmnvvnm.\\.                                     .,,,/`mmm.\\\n    |.mmnnvvnm.\\:;,.                           ..,,;;;/.mmnnnmm.\\\n    \\ mmnnnvvnm.\\::;;,                    .,;;;;;;;;/.mmmnnvvnnm.|\n     \\`mmnnnvvnm.\\::;::.sSSs      sSSs ,;;;;;;;;;;/.mmmnnvvvnnmm'/\n       \\`mmnnnvnm.\\:::::SSSS,,,,,,SSSS:::::::;;;/.mmmnnvvvnnmmm'/\n          \\`mnvvnm.\\::%%%;;;;;;;;;;;%%%%:::::;/.mnnvvvvnnmmmmm'/\n             \\`mmmm.%%;;;;;%%%%%%%%%%%%%%%::/.mnnvvvnnmmmmm'/ '\n                \\`%%;;;;%%%%s&&&&&&&&&s%%%%mmmnnnmmmmmm'/ '\n     |           `%;;;%%%%s&&.%%%%%%.%&&%mmmmmmmmmm'/ '\n\\    |    /       %;;%%%%&&.%;`    '%.&&%%%////// '\n  \\  |  /         %%%%%%s&.%%   x   %.&&%%%%%//%\n    \\  .:::::.  ,;%%%%s&&&&.%;     ;.&&%%%%%%%%/,\n-!!!- ::#:::::%%%%%%s&&&&&&&&&&&&&&&&&%%%%%%%%%%%\n    / :##:::::&&&&&&&&&&&&&&&&&&&&&%%%%%%%%%%%%%%,\n  /  | `:#:::&&&&&&&&&&&&&&&&&&&&&&&&%%%%%%%%%%%%%\n     |       `&&&&&&&&&,&&&&&&&&&&&&SS%%%%%%%%%%%%%\n               `~~~~~'~~        SSSSSSS%%%%%%%%%%%%%\n                               SSSSSSSS%%%%%%%%%%%%%%\n                              SSSSSSSSSS%%%%%%%%%%%%%.\n                            SSSSSSSSSSSS%%%%%%%%%%%%%%\n                          SSSSSSSSSSSSS%%%%%%%%%%%%%%%.\n                        SSSSSSSSSSSSSSS%%%%%%%%%%%%%%%%\n                      SSSSSSSSSSSSSSSS%%%%%%%%%%%%%%%%%.\n                    SSSSSSSSSSSSSSSSS%%%%%%%%%%%%%%%%%%%\n                  SSSSSSSSSSSSSSSSSS%%%%%%%%%%%%%%%%%%%%.\n\n                          WELCOME TO DASHLAME\n"
PEARSON_TABLE = [
    199, 229, 151, 178, 53, 6, 131, 42, 248, 110, 39, 28, 51, 216, 32, 14, 77, 34, 166, 213, 157, 150, 115, 197, 228, 221, 254, 172, 84, 27, 36, 156, 69, 96, 12, 220, 225, 137, 246, 141, 44, 208, 191, 109, 163, 21, 173, 250, 98, 227, 203, 162, 188, 3, 105, 171, 215, 15, 207, 218, 234, 56, 136, 235, 97, 79, 189, 102, 134, 11, 224, 117, 177, 222, 100, 129, 78, 18, 130, 187, 9, 184, 99, 108, 202, 13, 238, 17, 94, 70, 180, 144, 185, 168, 123, 71, 176, 91, 4, 153, 103, 242, 80, 127, 198, 82, 169, 148, 48, 120, 59, 55, 230, 209, 50, 73, 31, 49, 142, 149, 167, 249, 116, 1, 7, 86, 143, 101, 29, 52, 114, 154, 160, 128, 19, 170, 46, 214, 38, 67, 186, 252, 181, 145, 212, 183, 22, 231, 107, 43, 47, 122, 251, 217, 5, 62, 88, 244, 200, 93, 240, 219, 124, 58, 161, 89, 211, 158, 247, 60, 236, 65, 106, 113, 66, 81, 165, 194, 223, 40, 233, 126, 139, 72, 132, 61, 135, 57, 87, 182, 164, 35, 159, 118, 8, 83, 210, 243, 104, 76, 75, 119, 90, 138, 20, 206, 95, 16, 74, 33, 245, 237, 111, 64, 253, 125, 23, 232, 193, 37, 175, 92, 30, 241, 255, 133, 0, 140, 2, 155, 85, 10, 146, 179, 25, 26, 226, 201, 195, 121, 190, 63, 68, 152, 45, 147, 41, 204, 192, 205, 196, 54, 174, 239, 112, 24]


def pad(s):
    mark = chr(16 - len(s) % 16)
    while len(s) % 16 != 15:
        s += chr(random.randint(0, 255))

    return s + mark


def unpad(s):
    return s[:-ord(s[(-1)])]


def get_random_passphrase():
    sys.stdout.write(
        'Getting random data from atmospheric noise and mouse movements')
    sys.stdout.flush()
    for i in range(10):
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(random.randint(1, 20) / 10.0)

    print ''
    with open('wordlist.txt', 'rb') as (fi):
        passwords = fi.read().strip().split('\n')
    return (random.choice(passwords), random.choice(passwords))


def get_pearson_hash(passphrase):
    key, iv = ('', '')
    for i in range(32):
        h = (i + ord(passphrase[0])) % 256
        for c in passphrase[1:]:
            h = PEARSON_TABLE[(h ^ ord(c))]

        if i < 16:
            key += chr(h)
        else:
            iv += chr(h)

    return (
        key, iv)


def encrypt_stream(data, passphrase):
    key, iv = get_pearson_hash(passphrase)
    aes = AES.new(key, AES.MODE_CBC, iv)
    data = pad(data)
    return aes.encrypt(data)


def decrypt_stream(data, passphrase):
    key, iv = get_pearson_hash(passphrase)
    aes = AES.new(key, AES.MODE_CBC, iv)
    data = unpad(aes.decrypt(data))
    return data


def encrypt_archive(archive_filename, passphraseA, passphraseB):
    with open(archive_filename, 'rb') as (db_fd):
        with open(archive_filename.replace('.db', '.dla'), 'wb') as (dla_fd):
            enc1 = encrypt_stream(db_fd.read(), passphraseA)
            enc2 = encrypt_stream(enc1, passphraseB)
            dla_fd.write(enc2)
    os.unlink(archive_filename)


def decrypt_archive(archive_filename, passphraseA, passphraseB):
    with open(archive_filename, 'rb') as (dla_fd):
        with open(archive_filename.replace('.dla', '.db'), 'wb') as (db_fd):
            dec1 = decrypt_stream(dla_fd.read(), passphraseB)
            dec2 = decrypt_stream(dec1, passphraseA)
            db_fd.write(dec2)
    os.unlink(archive_filename)


def createArchive():
    archive_name = raw_input('Please enter your archive name: ')
    passphraseA, passphraseB = get_random_passphrase()
    print 'This is your passphrase :', passphraseA, passphraseB
    print 'Please remember it or you will lose all your passwords.'
    archive_filename = archive_name + '.db'
    with open(archive_filename, 'wb') as (db_fd):
        db_fd.write(zlib.decompress('x\x9c\x0b\x0e\xf4\xc9,IUH\xcb/\xcaM,Q0f`a`ddpPP````\x82b\x18`\x04b\x164>!\xc0\xc4\xa0\xfb\x8c\x9b\x17\xa4\x98y.\x03\x10\x8d\x82Q0\n\x88\x05\x89\x8c\xec\xe2\xf2\xf2\x8c\x8d\x82%\x89I9\xa9\x01\x89\xc5\xc5\xe5\xf9E)\xc5p\x06\x93s\x90\xabc\x88\xabB\x88\xa3\x93\x8f\xab\x02\\X\xa3<5\xa9\x18\x94\xabC\\#Bt\x14J\x8bS\x8b\xf2\x12sa\xdc\x02\xa820W\x13\x927\xcf0\x00\xd1(\x18\x05\xa3`\x08\x03#F\x16mYkh\xe6\x8fO\xadH\xcc-\xc8I\x85\xe5~O\xbf`\xc7\xea\x90\xcc\xe2\xf8\xa4\xd0\x92\xf8\xc4\xf8`\xe7"\x93\x92\xe4\x8cZ\x00\xa8&=\x8f'))
    encrypt_archive(archive_filename, passphraseA, passphraseB)
    print 'Archive created successfully.'


def updateArchive():
    archive_name = raw_input('Please enter your archive name: ')
    passphrase = raw_input('Please enter your passphrase: ')
    passphraseA, passphraseB = passphrase.split()
    website = raw_input('Website: ')
    username = raw_input('Username: ')
    password = raw_input('Password: ')
    dla_filename = archive_name + '.dla'
    db_filename = archive_name + '.db'
    decrypt_archive(dla_filename, passphraseA, passphraseB)
    conn = sqlite3.connect(db_filename)
    cur = conn.cursor()
    cur.execute('INSERT INTO Passwords VALUES(?,?,?)',
                (website, username, password))
    conn.commit()
    conn.close()
    encrypt_archive(db_filename, passphraseA, passphraseB)
    print 'Update done.'


def accessArchive():
    archive_name = raw_input('Please enter your archive name: ')
    passphrase = raw_input('Please enter your passphrase: ')
    passphraseA, passphraseB = passphrase.split()
    website = raw_input('Website: ')
    dla_filename = archive_name + '.dla'
    db_filename = archive_name + '.db'
    decrypt_archive(dla_filename, passphraseA, passphraseB)
    conn = sqlite3.connect(db_filename)
    cur = conn.cursor()
    cur.execute(
        'SELECT Username, Password FROM Passwords WHERE Website=?', (website,))
    results = cur.fetchall()
    conn.close()
    encrypt_archive(db_filename, passphraseA, passphraseB)
    if len(results) == 0:
        print 'No results.'
    else:
        for result in results:
            print result[0], ':', result[1]


if __name__ == '__main__':
    print HEADER
    print '1. Create a new password archive'
    print '2. Add a password to an archive'
    print '3. Access a password from an existing archive'
    try:
        res = raw_input()
        if res == '1':
            createArchive()
        else:
            if res == '2':
                updateArchive()
            else:
                if res == '3':
                    accessArchive()
                else:
                    print 'Wrong choice'
    except:
        print 'Error.'
# okay decompiling dashlame.pyc
