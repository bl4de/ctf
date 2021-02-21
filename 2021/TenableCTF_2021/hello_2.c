#include <stdio.h>
int main()
{
    char name[100] = { '\0' };
    fgets(name, 99, stdin);
    printf("Hello %s", name);
    return 0;
}