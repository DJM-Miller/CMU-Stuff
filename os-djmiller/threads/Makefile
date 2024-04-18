CC = gcc
CXX = g++


all : mat_multi

run : mat_multi
	./mat_multi

clean :
	/bin/rm -rf mat_multi

mat_multi : double_matrix_multi.c
	$(CC) -g -o $@ $^

test : mat_multi
	./mat_multi