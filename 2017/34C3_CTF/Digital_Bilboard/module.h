#ifndef MODULE_H
#define MODULE_H

#define MIN(a,b) (((a)<(b))?(a):(b))

#include <link.h>

typedef void (*handle_command_function)(int, char**);
typedef void (*registration_function)(const char*, const char*, const char*, handle_command_function);



typedef struct command {
    const char* name;
    const char* usage;
    const char* description;
    handle_command_function function;
    struct command* next;
} command_t;

typedef struct module {
    const char* name;
    const char* info;
    Elf64_Addr base;
    command_t* commands;
} module_t;


#endif
