/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   runner.c
 * Author: rrigoni
 *
 * Created on April 23, 2020, 4:04 PM
 */

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <wait.h>
#include "runner.h"

process_descriptor process; //ARRAY contining the description of all the different processes
int current_process = 0;
int fd[2];
pid_t pid;

/*
 * 
 */
int main(int argc, char** argv) {
    
    //create a pipe 
    if(pipe(fd) < 0) {
        printf("Error occurs while generating the pipe...");
        exit(1);
    }
    
    //pipe correctly generated
    while(current_process < PROCESSES) {
       switch(pid = fork()) {
           case -1: 
               printf("\nError while calling the fork");
               exit(1);
               break; //even if it does not do anything -> cannot join here
           case 0: 
               /*the value child has of current_processes is its own id*/
               close(fd[0]); // close read entry
               process.id = current_process;
               //process.sleep_time = random() % 10; //create a random number from 0 to 9
               process.sleep_time = 5;
               sleep(process.sleep_time);
               
               //write on the pipe the id and the correspondent sleep time
               char output[2];
               output[0] = (char)process.id;
               output[1] = (char)process.sleep_time;
               
               int check = write(fd[1], output, 2);
               exit(0);
               break;
           default: 
               /*PARENT*/
               current_process++;
               break;
       }
    }  
       //now we have generated the child... still waiting for the to finisch
       //read input from the pipe
       while(current_process > 0){
           //read, print and decrement the index
           char input[2];
           read(fd[0], input, 2);
           
           printf("\nProcess number %d: waited %d seconds", (int)input[0], (int)input[1]);
           current_process--;
       }   
    
    printf("\n");
    return (EXIT_SUCCESS);
}

