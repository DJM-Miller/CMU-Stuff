# Demonstration of Processes, Fork, and Shared Memory
## Fork
To run the Fork demo that creates a parent process and 9 child process outputing there pid
```
make test-fork
```

## Shared Memory
This demo creates shared memory for a parent process and it childern. The memory is then used for a shared cstring buffer and a shared int. The parent then spawns 3 child processes that increment the int by 3 and write "Hello from the child processes!" to the shared char buffer.  
To run the shared memory demo run the following command.
```
make test-shared_mem
```