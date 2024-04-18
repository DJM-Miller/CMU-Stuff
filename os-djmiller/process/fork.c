#include <stdio.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>
#include <stdlib.h>

void performTask() {
    printf("Child process: %d Parent Process: %d\n", getpid(), getppid());
    // Could insert some task for each child to preform
}

int main() {
    pid_t parent_pid = getpid();
    printf("Parent process id = %d\n", parent_pid);

    for (int i = 0; i < 10; ++i) {
        pid_t maybe_child_pid = fork();
        //Child processes do there thing from here
        if (maybe_child_pid < 0) {
            // Fork failed
            printf("Fork failed!\n");
            exit(EXIT_FAILURE);
        } else if (maybe_child_pid == 0) {
            // Child process
            performTask();
            return 0; // Terminate child process
        }
        // Parent process continues the loop
    }

    // Parent waits for all child processes to finish
    for (int i = 0; i < 10; ++i) {
        wait(NULL);
    }
    printf("From Parent process: %d, child processes have completed their tasks.\n",getpid());

    return 0;
}

