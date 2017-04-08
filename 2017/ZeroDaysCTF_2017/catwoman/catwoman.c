#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main(int argc, char **argv) {

    size_t size_of_answer = sizeof(int32_t)*2+2;
    char* submitted_answer = calloc(1, size_of_answer);

    printf("Please Enter Your Access Code to gain flag : ");
    fgets(submitted_answer, size_of_answer, stdin);

    //trim(submitted_answer);
    int32_t* answer = (int32_t*)submitted_answer;

    printf ("%x, %x\n\n", answer[0], answer[1]);
    
    if(answer[0] == 0x5F743047 && answer[1] == 0x6B31694D) {
        printf("Access Code Correct!\n");}


    free(submitted_answer);
    return 0;
}
