CC=gcc
CFLAGS=-Wall -O1

all: server

server: server.c billboard.so
	$(CC) -no-pie -DPORT=12345 -DLIB=\"billboard.so\" -o server server.c $(CFLAGS) -ldl

billboard.so: billboard.c
	$(CC) -o billboard.so -shared -fPIC billboard.c $(CFLAGS)
