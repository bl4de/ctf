#!/usr/bin/python
import zipfile

for i in range(1,100):
    zip_ref = zipfile.ZipFile('flag.zip', 'r')
    zip_ref.extractall('./')
    zip_ref.close()