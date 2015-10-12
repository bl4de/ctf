# ASIS CTF Final 2015 - Biglie (Forensic, 100pts)

## Problem

We've got pcap file. This is network communication with 0bin.asis.io server, which is a service with encrypted pastebins.

Our goal is to find the flag.

## Solution

Uloaded pastebins are encrypted with Stanford Javascript Crypto Library (SJCL) library (https://crypto.stanford.edu/sjcl/).
It uses AES algorithm at 128, 192 or 256 bits. The key needed to decrypt pastebin is added to url after # (hash) mark what means that is not sent to the server.

Full url of encoded pastebin look like this example:
```
http://0bin.asis.io/paste/TINcoc0f#-krvZ7lGwZ4e2JQ8n+3dfsMBqyN6Xk6SUzY7i0JKbpo
```

But in pcap file we can only reveal fragment without the key, for example:

```
http://0bin.asis.io/paste/TINcoc0f
```

It returns us encrypted pastebin:

{"iv":"adzR1bn929d5vf53R6BuDg","salt":"4SYEnmaSS58","ct":"J7QU491qMea5JTkR1y5MSH/UBp5QHIjHq7PeRRaqYn/rPsY1h1wiPbFp/gMufQ1w"}

![Pastebin]
(https://github.com/bl4de/ctf/blob/master/ASIS_CTF_2015/Biglie_Forensic100/biglie-packet.png)

To see decrypted content, we need to figure out what the key was used.

When we take a look at pcap file, we can find requests to some web statistic tool, Piwik. After each request, Piwik sends its own request to statistic server with full information about original request, inluding full url (as it is only the one of Piwik's GET request it's complete including part after # sign):

```
/piwik.php?action_name=0bin%20-%20encrypted%20pastebin&idsite=1&rec=1&r=776276&h=11&m=27&s=12&url=http%3A%2F%2F0bin.asis.io%2Fpaste%2FTINcoc0f%23-krvZ7lGwZ4e2JQ8n%2B3dfsMBqyN6Xk6SUzY7i0JKbpo&urlref=http%3A%2F%2F0bin.asis.io%2F&_id=dd17974841486b63&_idts=1443081356&_idvc=1&_idn=0&_refts=0&_viewts=1443081356&send_image=0&pdf=1&qt=0&realp=0&wma=0&dir=0&fla=1&java=1&gears=0&ag=0&cookie=1&res=1440x900&gt_ms=108
```

We can see key used to encrypt this pastebin - *-krvZ7lGwZ4e2JQ8n+3dfsMBqyN6Xk6SUzY7i0JKbpo*

![Piwik request]
(https://github.com/bl4de/ctf/blob/master/ASIS_CTF_2015/Biglie_Forensic100/biglie-packet-to-piwik-with-flag.png)

After use this key we can reveal decrypted content of pastebin:

``` 
http://0bin.asis.io/paste/TINcoc0f#-krvZ7lGwZ4e2JQ8n+3dfsMBqyN6Xk6SUzY7i0JKbpo
hi all,
Where is the flag? :-)
```


When we take a look for all of such requests in pcap file, we found three of them:


1.
```
http://0bin.asis.io/paste/TINcoc0f
{"iv":"adzR1bn929d5vf53R6BuDg","salt":"4SYEnmaSS58","ct":"J7QU491qMea5JTkR1y5MSH/UBp5QHIjHq7PeRRaqYn/rPsY1h1wiPbFp/gMufQ1w"}

http://0bin.asis.io/paste/TINcoc0f#-krvZ7lGwZ4e2JQ8n+3dfsMBqyN6Xk6SUzY7i0JKbpo
hi all,
Where is the flag? :-)
```

2.
```
http://0bin.asis.io/paste/Vyk5W274
{"iv":"cg0Ep/SMSSG13vFJj5qj5Q","salt":"iGWh0On71+I","ct":"0ImBWPypPj4a/dzTJaN36zVlCkNF8GDvEME1QoKncwqGpa0KPAc8m7CkAs7Z3+FhyW/eqbw4xNG4WJ+VOTWVnGA6sXFfjmRA4VdwgZritXNATi1CLueSuw"}

http://0bin.asis.io/paste/Vyk5W274#1L8OT3oT7Xr0ryJlS5ASprAqgsQysKeebbSK90gGyQo
this is not flag :|
ASIS{64672fabdbd51e841c54c53b9c83c6fd}
```

3.
```
http://0bin.asis.io/paste/1ThAoKv4#Zz-nHPnr0vGGg3s/7/RWD2pnZPZl580x9Y2G3IUehfc

```

Last one contains the flag:

![Flag]
(https://github.com/bl4de/ctf/blob/master/ASIS_CTF_2015/Biglie_Forensic100/biglie-flag.png)


*ASIS{e29a3ef6f1d71d04c5f107eb3c64bbbb}*
