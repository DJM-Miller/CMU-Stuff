CC = gcc
CXX = g++
PY = python


all : sym-key-encrypt

run : sym-key-encrypt
	./sym-key-encrypt

clean :
	/bin/rm -rf sym-key-encrypt

sym-key-encrypt : sym-key-encrypt.c
	$(CC) -g -o $@ $^ -lgcrypt

test : sym-key-encrypt
	./sym-key-encrypt
	/bin/rm -rf sym-key-encrypt 

py-encrypt : sym_key_encrypt.py
	$(PY) sym_key_encrypt.py