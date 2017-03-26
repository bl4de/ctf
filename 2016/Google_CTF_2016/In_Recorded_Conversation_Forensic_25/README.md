# In Recorded Conversation (Forensic, 25pts)

## Problem

Can you find the flag?

## Solution

We get _pcap_ (irc.pcap) file with some IRC conversation.

Quick "Follow the stream" reveals this fragment:

```
:andrewg!~poppopret@agriffiths.c.gctf-2015-admins.google.com.internal PRIVMSG #ctf :CTF{
PING irc.capturetheflag.withgoogle.com
:irc.capturetheflag.withgoogle.com PONG irc.capturetheflag.withgoogle.com :irc.capturetheflag.withgoogle.com
:itsl0wk3y!~poppopret@itsl0wk3y.c.gctf-2015-admins.google.com.internal PRIVMSG #ctf :some_
PRIVMSG #ctf :leaks_
:andrewg!~poppopret@agriffiths.c.gctf-2015-admins.google.com.internal PRIVMSG #ctf :are_
PRIVMSG #ctf :good_
:itsl0wk3y!~poppopret@itsl0wk3y.c.gctf-2015-admins.google.com.internal PRIVMSG #ctf :leaks_
:andrewg!~poppopret@agriffiths.c.gctf-2015-admins.google.com.internal PRIVMSG #ctf :}
PING irc.capturetheflag.withgoogle.com
```

And we can simply collect fragments of the flag:

```
CTF{some_leaks_are_good_leaks_}
