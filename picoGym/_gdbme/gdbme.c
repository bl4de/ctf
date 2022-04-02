#include <stdio.h>
#include <string.h>
#include <unistd.h>


char* rotate_encrypt(int param_1, char* param_2)

{
    char cVar1;
    char* __s;
    size_t sVar2;
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



int main(void)
{
    char* __s;
    long in_FS_OFFSET;
    long local_38;
    long local_30;
    long local_28;
    long local_20;
    long local_18;
    long local_10;

    local_10 = in_FS_OFFSET + 0x28;
    local_20 = 0x4c75257240343a41;
    local_28 = 0x4362383846336235;
    local_30 = 0x6630624760433530;
    local_38 = 0x4e64646267353361;
    local_18 = 0;
    __s = (char*)rotate_encrypt(0, &local_20);
    fputs(__s, stdout); // picoCTF{d3bugg3r_dr1v3_72bd8355}
    putchar(10);
    return 0;
}
