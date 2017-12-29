#define _GNU_SOURCE
#include <sys/types.h>
#include <sys/socket.h>
#include <sys/wait.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <stdio.h>
#include <dlfcn.h>
#include <string.h>
#include <pwd.h>
#include <grp.h>
#include <link.h>
#include <dlfcn.h>

#include "module.h"


#define BACKLOG 32

#define logf(...) fprintf(stderr, __VA_ARGS__)



module_t module;
struct sockaddr_in client;

void (*initialize_module)(module_t* m, registration_function r);

void module_info(int argc, char* argv[]) {
    printf("************************************\n");
    printf("Information about the loaded module:\n");
    printf("Name: %s\nBase address: %p\n", module.name, (void*) module.base);
    printf("************************************\n");
}

void register_command(const char* name, const char* usage, const char* desc, handle_command_function function) {
    command_t* command = malloc(sizeof(command_t));
    command->name = name;
    command->usage = usage;
    command->description = desc;
    command->function = function;
    command->next = NULL;

    if (module.commands == NULL) {
        module.commands = command;
        return;
    }

    // append to end of list
    command_t* cur = module.commands;
    while(cur->next != NULL) {
        cur = cur->next;
    }
    cur->next = command;
}

void help(int argc, char* argv[]) {
    command_t* command = module.commands;
    while (command != NULL) {
        printf("%s %s\t(%s)\n", command->name, command->usage, command->description);        
        command = command->next;
    }
}

void load_module() {
    char* error;
    void* handle = dlopen(LIB, RTLD_LAZY);
    if (!handle) {
        logf("Error on dlopen %s: %s\n", LIB, dlerror());
        exit(EXIT_FAILURE);
    }
    dlerror();
    struct link_map* lm = (struct link_map*) handle;
    module.base = lm->l_addr;

    initialize_module = dlsym(handle, "initialize_module");
    printf("%p\n", initialize_module);
    if ((error = dlerror()) != NULL)  {
        logf("%s\n", error);
        exit(1);
    }
    initialize_module(&module, register_command);

    register_command("help", "\t\t\t", "Show this information", help);
    register_command("modinfo", "\t\t", "Show information about the loaded module", module_info);
    logf("Module successfully loaded.\n");
}



int init_socket() {
    // create socket
    int sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd < 0) {
        perror("Unable to create socket.");
        exit(EXIT_FAILURE);
    }
    // reusable sockfd
    int val = 1;
    if (setsockopt(sockfd, SOL_SOCKET, SO_REUSEADDR, (void*) &val, sizeof val) < 0) {
        perror("Unable to set socket option REUSEADDR.");
        exit(EXIT_FAILURE);
    }
    // bind socket
    struct sockaddr_in addr;
    addr.sin_family = AF_INET;
    addr.sin_addr.s_addr = INADDR_ANY;
    addr.sin_port = htons(PORT);
    if (bind(sockfd, (struct sockaddr*) &addr, sizeof(addr)) < 0) {
        perror("Unable to bind socket.");
        exit(EXIT_FAILURE);
    }
    // set backlog
    if (listen(sockfd, BACKLOG) < 0) {
        perror("Unable to set backlog.");
        exit(EXIT_FAILURE);
    }
    return sockfd;
}



void handle_input(char* buf) {
    int argc = 0;
    char* argv[256];
    char* token = strtok(buf, " \n");
    if (!token) {
        return;
    }
    while (argc < sizeof(argv) && token) {
        argv[argc] = token;
        argc++;
        token = strtok(NULL, " \n");
    }

    command_t* cur = module.commands;
    while (cur != NULL) {
        if (!strcmp(cur->name, argv[0])) {
            cur->function(argc, argv);
            break;
        }
        cur = cur->next;
    }
    if (cur == NULL) {
        printf("Command not found.\n");
    }
    return;
}

void interact() {
    printf("*\n* %s\n*\n%s\n> ", module.name, module.info);
    fflush(stdout);
    static char buf[4096];
    while (1) {
        if (fgets(buf, 4096, stdin) != NULL) {
            handle_input(buf);
            printf("> ");
        } else {
            break;
        }
    }
}

void drop_privs() {
    char* user = "challenge";
    struct passwd* pw = getpwnam(user);
    if (pw == NULL) {
        logf("User \"%s\" does not exist", user);
        exit(EXIT_FAILURE);
    }
    if (setgroups(0, NULL) != 0) {
        perror("Error on setgroups");
        exit(EXIT_FAILURE);
    }
    if (setgid(pw->pw_gid) != 0) {
        perror("Error on setgid");
        exit(EXIT_FAILURE);
    }
    if (setuid(pw->pw_uid) != 0) {
        perror("Error on setuid");
        exit(EXIT_FAILURE);
    }
}

int main(int argc, char* argv[]) {
    
    int sockfd = init_socket();
    logf("Server listening on port %d\n", PORT);
  
    if (signal(SIGCHLD, SIG_IGN) == SIG_ERR) {
        perror("Error setting SIGCHILD handler.");
        return EXIT_FAILURE;
    }

    load_module();

    while (1) {
        socklen_t client_len = sizeof(client);
        int client_fd = accept(sockfd, (struct sockaddr*) &client, &client_len);
        if (client_fd < 0) {
            perror("Error creating socket for incoming connection");
            exit(EXIT_FAILURE);
        }
        logf("New connection from %s on port %d\n", inet_ntoa(client.sin_addr), htons(client.sin_port));

        int pid = fork();
        if (pid < 0) {
            perror("Unable to fork");
            exit(EXIT_FAILURE);
        }

        if (pid == 0) { // client
            alarm(300);
            close(sockfd);

            dup2(client_fd, 0);
            dup2(client_fd, 1);
            setvbuf(stdout, NULL, _IONBF, 0);

            drop_privs();

            interact();

            close(client_fd);
            logf("%s:%d disconnected\n", inet_ntoa(client.sin_addr), htons(client.sin_port));
            exit(EXIT_SUCCESS);
        } else {        // server
            logf("%s:%d forked new process with pid %d\n", inet_ntoa(client.sin_addr), htons(client.sin_port), pid);
            close(client_fd);
        }

    }
}
