/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   threads.c
 * Author: rrigoni
 *
 * Created on April 23, 2020, 5:52 PM
 */

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>
#include "threads.h"

/*
 * 
 */

/*GLOBAL*/
;
process processes[5]; 
int current_execution = 0;
pthread_t ptid[5];

void* copy(void* arg);

int main(int argc, char** argv) {
    
    while(current_execution < 5) {
        
        //at every step, take the name and copy to another folder -> exploiting threads 
        //for parallel execution
        //1) lanch a thread -> as attribute it could see the struct relative to its number 
       
        /*
         In order to create an array of structures, and then access its own elements...
         * 1) create the array, and specify the number of elements
         * 2) create a pointer to the same type of the array (same structure)
         * 3) initialize the ptr to the initial cell of the array -> by assigning to the name
         *  which by default points to the first elements of the first structure
         * 4) increasing by 1 the pointer... increase by one row in the array (skip all the array)
         * 5( exploiting ptr-> <field_name> is it possible to get the pointer to these field...
         *  ptr-> <field_name> obtain a pointer, the *() to set its value
         *          
         */
        
        process *ptr = NULL;
        ptr = processes;
        *(ptr->name) = URL[current_execution];        
        ptr->current_copy = current_execution;
        
        printf("Launch coping the file %s\n", URL[current_execution]);
        
        int i = pthread_create(&ptid[current_execution], NULL, &copy, &processes[current_execution]);
        
        ptr = processes + 1; //-> goes to the next element
       
        current_execution++;
    }
 
        /*now another thread start executing the method void and it could access the structure*/
        
        //main flow continue there... for every 5 threads created, join() in order to wait for them finis
    printf("\nWaiting for terminating coping the files");
        for(current_execution; current_execution >= 0; current_execution--) 
            pthread_join(ptid[current_execution], NULL);
        
    return (EXIT_SUCCESS);
}

void* copy(void * arg) {
    FILE* source;
    FILE* target;
    int a;
    int current_value;
    process *ptr = processes;
    current_value = ptr->current_copy;
    printf("\nFrom the thread %d\n", current_value);
    char *sourcePath;
    char *targetPath;
    
    
    sourcePath = URL[current_value];
    targetPath = TARGET_URL[current_value];
    //check if we can correctly open the two files
    
    if((source = fopen(sourcePath, "r"))== NULL) {
        printf("\nCannot open source file");
        pthread_exit(NULL);
    }
    if((target = fopen(targetPath, "w")) == NULL) {
        printf("\nCannot create target file)");
        pthread_exit(NULL);
    }
    
    //correctly opened the two file...
    do {
        a = fgetc(source);
        fputc(a, target);
    } while(a != EOF);
    
    fclose(source);
    fclose(target);
    pthread_exit(NULL);
}