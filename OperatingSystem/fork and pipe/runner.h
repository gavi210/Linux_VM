/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   runner.h
 * Author: rrigoni
 *
 * Created on April 23, 2020, 4:05 PM
 */

#ifndef RUNNER_H
#define RUNNER_H

#ifdef __cplusplus
extern "C" {
#endif

#define PROCESSES 5
    typedef struct {
        int id;
        int sleep_time;
    } process_descriptor;


#ifdef __cplusplus
}
#endif

#endif /* RUNNER_H */

