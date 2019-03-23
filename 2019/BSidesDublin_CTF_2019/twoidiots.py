#!/usr/bin/python

f = open('twoatatime', 'rb')
file_content = f.read()
good_file = open('goodfile.png', 'wb')
good_file_2 = open('goodfile2.png', 'wb')

print len(file_content)
for c in range(0, len(file_content)):
    if c % 2 == 0:
        good_file.write(file_content[c])
    else:
        good_file_2.write(file_content[c])

good_file_2.close()
good_file.close()
