#include <stdio.h>
#include <stdlib.h>

#define schleife(n) for (int i = n; i--;)
#define bitrverschieb(n, m) (n) >> (m)
// #define diskreteAddition(n, m) (n) ^ (m)

int diskreteAddition(n, m) {
    printf("n: %d\n", (n));
    printf("m: %d\n", (m));

    printf("(n) ^ (m): %d\n", (n) ^ (m));

    return (n) ^ (m);
}


void main(void) {
    int i = 1804289383;
    int k;
    int e;
    int * p = & i;

    printf("%d\n", i);
    fflush(stdout);
    scanf("%d %d", & k, & e);

    k = i;

    printf("%d\n", k);
    
    k = diskreteAddition(k, e);
    printf("%d\n", k);

    if(k == 53225)
        puts("FLAG");
    else
        puts("War wohl void!");
}
