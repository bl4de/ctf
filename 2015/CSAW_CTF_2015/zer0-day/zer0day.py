#!/usr/bin/python
import base64
import re
print re.findall("{(.+)}", base64.b64decode(open("text.txt", "r").readline().replace("\\n","")))[0]

