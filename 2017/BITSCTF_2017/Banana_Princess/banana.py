#!/usr/bin/env python

banana = open('MinionQuest.pdf', 'rw').read()
new_banana = open('FixedMinionQuest.pdf', 'w+')

buff = ''


def rot13(c):
    # ROT13 only for ASCII codes from 97 to 122 decimal:
    res = c
    if ord(c) in range(97, 122):
        if (ord(c) + 13) > 122:
            res = chr(ord(c) - 13)
        else:
            res = chr(ord(c) + 13)
    else:
        if ord(c) in range(65, 90):
            if (ord(c) + 13) > 90:
                res = chr(ord(c) - 13)
            else:
                res = chr(ord(c) + 13)
        else:
            res = chr(ord(c))

    return res


for c in banana:
    if ord(c) == 47:
        buff = buff + ' '
    buff = buff + rot13(c)

# buff = buff.replace('Izage', 'Image').replace(
#     'LastZodified', 'LastModified').replace('endstreaz', 'endstream').replace('Zetadata', 'Metadata').replace('ZediaBox', 'MediaBox').replace('BitsPerCozponent', 'BitsPerComponent').replace('DecodeParzs', 'DecodeParms').replace('ColorTransforz', 'ColorTransform').replace('Coluzns', 'Columns').replace('azples', 'amples').replace('aze', 'ame').replace('streaz', 'stream').replace('<< /', '<</').replace('endobj', '\nendobj\n').replace('stream', '\nstream').replace('end\nstream', 'endstream').replace(' /', '\n/')

new_banana.write(buff)
