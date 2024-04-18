#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <sys/wait.h>
#include <fcntl.h>
#include <string.h>

#define SHARED_MEM_NAME "/my_shared_memory"
#define BUFFER_SIZE 100
#define INT_SIZE sizeof(int)

int create_shared_memory(int *shm_fd, int size) {
    *shm_fd = shm_open(SHARED_MEM_NAME, O_CREAT | O_RDWR, 0666);
    if (*shm_fd == -1) {
        perror("shm_open");
        return 0;
    }

    if (ftruncate(*shm_fd, size) == -1) {
        perror("ftruncate");
        return 0;
    }

    return 1;
}

int main() {
    int shm_fd;
    char *shared_buffer;
    int *shared_int;

    if(!create_shared_memory(&shm_fd, BUFFER_SIZE+INT_SIZE)){
        perror("create");
        return 1;
    }

    // Map the shared memory segment to the address space of the process
    void *shared_mem = mmap(NULL, BUFFER_SIZE + INT_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, shm_fd, 0);
    if (shared_mem == MAP_FAILED) {
        perror("mmap");
        return 1;
    }

    shared_buffer = (char *)shared_mem;
    shared_int = (int *)(shared_buffer + BUFFER_SIZE); // Set shared_int to the address right after the buffer

    *shared_int = 3;

   for(int i = 0; i < 3; i++){
        // Fork a child process
        pid_t pid = fork();

        if (pid < 0) {
            perror("fork");
            return 1;
        } else if (pid == 0) {  // Child process
            printf("Child process %d writing to shared memory...\n", i+1);
            sprintf(shared_buffer, "Hello from the child processes!");
            printf("Child process %d wrote: %s\n", i+1, shared_buffer);
            *shared_int += 3;
            printf("Child process %d int value: %d\n", i+1, *shared_int);
            exit(0); // Terminate child process
        }
    }

    // Parent process waits for all children to finish
    for(int i = 0; i < 3; i++){
        wait(NULL);
    }

    printf("Parent process reading from shared memory...\n");
    printf("Parent process read: %s\n", shared_buffer);
    printf("Parent process int value: %d\n", *shared_int);

    // Unmap and close shared memory
    if (munmap(shared_mem, BUFFER_SIZE + INT_SIZE) == -1) {
        perror("munmap");
        return 1;
    }

    if (shm_unlink(SHARED_MEM_NAME) == -1) {
        perror("shm_unlink");
        return 1;
    }


    return 0;
}
