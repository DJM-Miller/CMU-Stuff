CC = gcc
CXX = g++

all : fork shared_mem

clean :
	/bin/rm -rf fork shared_mem

fork : fork.c
	$(CC) -g -o $@ $^

shared_mem : shared_mem.c
	$(CC) -g -o $@ $^ -lrt

test-fork : fork
	./fork
	/bin/rm -rf fork

test-shared_mem : shared_mem
	./shared_mem
	/bin/rm -rf shared_mem

