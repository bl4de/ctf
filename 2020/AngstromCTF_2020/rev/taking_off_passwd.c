#include <stdio.h>

char desired[] = {'46','4f','4b','59','4f','0a','4d','43','5c','4f','0a','4c','46','4b','4d','2a'};

void main()
{
    char *local_98;
    char *local_a0;

    puts("Well, you found the arguments, but what\'s the password?");
    fgets((char *)local_98, 0x80, stdin);
    local_a0 = strchr((char *)local_98, 10);

    puts(local_a0);
    
    if (local_a0 != (char *)0x0)
    {
        *local_a0 = '\0';
    }
    int sVar3 = strlen((char *)local_98);
    int local_a4 = (int)sVar3;
    int local_a8 = 0;
    while (local_a8 <= local_a4)
    {
        if ((local_98[local_a8] ^ 0x2a) != desired[local_a8])
        {
            puts("I\'m sure it\'s just a typo. Try again.");
            int uVar2 = 1;
            exit(0);
        }
        local_a8 = local_a8 + 1;
    }
    puts("Good job! You\'re ready to move on to bigger and badder rev!");
    puts("FLAG HERE");
    exit(0);
}
