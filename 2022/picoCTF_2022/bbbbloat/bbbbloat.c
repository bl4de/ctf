#include <string.h>
#include <stdio.h>

// gcc bbbbloat.c -o bbbbloat
char* print_flag(int param_1, char* param_2) {
    char cVar1;
    char* __s;
    char* sVar2;
    long local_20;

    __s = strdup(param_2);
    sVar2 = strlen(__s);
    for (local_20 = 0; local_20 < sVar2; local_20 = local_20 + 1) {
        if ((' ' < __s[local_20]) && (__s[local_20] != '\x7f')) {
            cVar1 = (char)(__s[local_20] + 0x2f);
            if (__s[local_20] + 0x2f < 0x7f) {
                __s[local_20] = cVar1;
            } else {
                __s[local_20] = cVar1 + -0x5e;
            }
        }
    }
    return __s;
}

int main(void) {
    char* __s;
    long in_FS_OFFSET;
    int key;
    int local_38;
    int local_30;
    int local_28;
    int local_20;

    // local_38 = 0x4c752572; //picoCTF{cu7_7h3_bl047_695036e3}
    // local_38 = 0x30623966; //cu7_7h3_
    // local_38 = 0x68653066; // bl047_69
    local_38 = 0x4e6236; // 5036e3}
    printf("What\'s my favorite number? ");
    scanf(&key);
    if (key == 1) {
        __s = (char*)print_flag(0, &local_38);
        printf(__s);
        putchar(10);
    } else {
        puts("Sorry, that\'s not it!");
    }
    return 0;
}


