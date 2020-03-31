#include <stdio.h>

char *deobfuscate(char *param_1)

{
    printf("param_1: %s\n", param_1);

    char cVar1;
    int iVar2;
    size_t sVar3;
    int local_18;
    int local_14;
    int local_10;
    int local_c;

    sVar3 = strlen(param_1);
    iVar2 = (int)sVar3;
    local_c = 0;

    while (local_c < iVar2)
    {
        cVar1 = param_1[local_c];
        param_1[local_c] = param_1[(long)local_c + 1];
        param_1[(long)local_c + 1] = cVar1;
        local_c = local_c + 2;        
    }

    local_10 = 0;
    while (local_10 < iVar2)
    {
        param_1[local_10] = param_1[local_10] + -0xf;
        local_10 = local_10 + 1;
    }

    local_14 = 0;
    while (local_18 = iVar2, local_14 < iVar2)
    {
        param_1[local_14] = param_1[local_14] ^ 0x2b;
        local_14 = local_14 + 1;
    }

    while (0 < local_18)
    {
        param_1[(long)local_18 + -1] = param_1[(long)local_18 + -1] ^ param_1[local_18 % iVar2];
        local_18 = local_18 + -1;
    }
    return param_1;
}

void main(void)
{
    int iVar1;
    char *__s1;
    char *__s;

    __s1 = (char *)malloc(0x1a);
    *__s1 = 0x7e394c2f38323434;
    __s1[1] = 0x54834c1f7b783a78;
    __s1[2] = 0x2f72857884842928;
    *(char *)(__s1 + 3) = 0x7667;
    *(char *)((long)__s1 + 0x1a) = 0;
    deobfuscate((char *)__s1);

    
    
    __s = (char *)malloc(0x1b);
    printf("%s", "Enter password: ");
    fgets(__s, 0x1b, stdin);
    printf("TU: __s1: %s\n", (char *)__s1);
    printf("TU: __s: %s\n", (char *)__s);
    iVar1 = strcmp((char *)__s1, __s);
    if (iVar1 == 0)
    {
        puts("Correct!  That\'s the password!");
    }
    else
    {
        puts("Sorry, that isn\'t the right password.");
    }
    exit(0);
}