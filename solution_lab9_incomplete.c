#include <stdio.h>
#include <semaphore.h>
#include <pthread.h>
#include <unistd.h>
#include <stdlib.h>

// Struct "Task" containing two fields
// 1) actions: the number of actions to be executed
// 2) type: the type of the Task ("0" or "1")
typedef struct {
    int actions;
    int type;
} Task;

// Array of counters (one for each type)
// 'operation' -> increment by n the number stored
int counters[2];

// Array of semaphores guaranteeing the mutual exclusion of tasks of the same type
// (one for each type)
sem_t counter_mutexes[2];

// Semaphore to synchronize the tasks of different types
sem_t condStart_semaphore;


// Prototype of the function implementing the behavior of each task (executed in a thread)
void* runner(void*);

// Main function
int main() {
    // Array of tasks (statically defined) of two different types ("0" and "1")
	// Clearly, for each couple:
	// the first value is the number of actions to be performed
	// the second value is the task type ("0" or "1") 
    Task tasks[] = {
            {5, 1},
            {6, 0},
            {2, 0},
            {5, 1},
            {9, 0},
            {6, 0},
            {7, 1}
    };

    // Computing "size", which is the number of items stored in the array,
    // as the ratio between the dimension of the whole array
    // and the size of each stored item
    int size = sizeof(tasks) / sizeof(Task);
    
    //check if the number of type 0 > type 1
    int number_process[] = {0, 0};
    int index;
    for (index = 0; index < size; index++) {
        if (tasks[index].type == 0) 
            number_process[0]++;
        else 
            number_process[1]++;                
    }
    
    if (number_process[0] < number_process[1])
        exit(1);
    
    printf("Types 0 > Types 1\n");
    // initializing the counters (to 0)
    // ...
    counters[0] = 0;
    counters[1] = 0;
    // initializing the semaphores related to the counters (both to 1, free)
    // ...
    sem_init(&counter_mutexes[0], 0, 1);
    sem_init(&counter_mutexes[1], 0, 1);
    // initializing the semaphore for synchronizing the tasks of different types
    // to 0 (occupied)
    // ...
    
    sem_init(&condStart_semaphore, 0, 0);
    
    // declaring an array of thread identifiers
    // ...
    
    pthread_t thread_identifiers[size];
    
    // running each thread (in a for cycle)
    // ...
    
    for(index = 0; index < size; index++) {
        switch(pthread_create(&thread_identifiers[index], NULL, &runner, &tasks[index])) {
            case 0:
                break;
            default:
                printf("Error while creating the new thread!\n");
                exit(1);
        }
    }
    // waiting for termination of each thread (in a for cycle)
    // ...
    for(index = 0; index < size; index++) {
        pthread_join(thread_identifiers[index], NULL);
    }
    // deallocating semaphores
    // ...
    sem_destroy(&counter_mutexes[0]);
    sem_destroy(&counter_mutexes[1]);
    sem_destroy(&condStart_semaphore);

    // printing the final values of the two counters
    // ...
    printf("\nFinal value for counter 0: %d\tcounter 1: %d\n", counters[0], counters[1]);
    return 0;
}


// implementation of the behavior of each thread
void* runner(void* param) {
    Task * task = param;
    int actions;
    if(task->type == 0) {
        sem_wait(&counter_mutexes[0]); //wait until semaphore is available
        for (actions = 0; actions < task->actions; actions++)
            counters[0]++;
        printf("Type 0 incrementing by %d\n", task->actions);
        sem_post(&counter_mutexes[0]); //leave the semaphore
        sem_post(&condStart_semaphore); //let another process of type 1 to execute   
    }
    else {
        sem_wait(&condStart_semaphore);
        sem_wait(&counter_mutexes[1]);
        printf("Type 1 incrementing by %d\n", task->actions);
        for (actions = 0; actions < task->actions; actions++)
            counters[1]++;
	sem_post(&counter_mutexes[1]);
    }
    return 0;
}
