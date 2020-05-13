/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   threads.h
 * Author: rrigoni
 *
 * Created on April 23, 2020, 5:49 PM
 */

#ifndef THREADS_H
#define THREADS_H

#ifdef __cplusplus
extern "C" {
#endif

#define MAX 5;
typedef struct {
    char *name[15]; //-> contains the name of the file that has to be copied
    time_t init;
    time_t end;
    int current_copy;
} process;

char *URL[5] = {
            "10172-m-001.mp3",
            "10305-m-001.mp3",
            "10244-m-001.mp3",
            "10275-m-001.mp3",
            "10262-m-001.mp3"
    };

char *TARGET_URL[5] = {
        "/home/students/rrigoni/Documents/C_Exercises/C_Programming/10172-m-001.mp3",
        "/home/students/rrigoni/Documents/C_Exercises/C_Programming/10305-m-001.mp3",
        "/home/students/rrigoni/Documents/C_Exercises/C_Programming/10244-m-001.mp3",
        "/home/students/rrigoni/Documents/C_Exercises/C_Programming/10275-m-001.mp3",
        "/home/students/rrigoni/Documents/C_Exercises/C_Programming/110262-m-001.mp3"
    };

#ifdef __cplusplus
}
#endif

#endif /* THREADS_H */