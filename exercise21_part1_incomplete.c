#include <stdio.h>
#include <stdbool.h>
#include <wait.h>
#include <stdlib.h>
#include <unistd.h> //allows calling System Calls... such as fork();

// Prototype of the function defining the menu to be shown to the user
// ***** INPUT PARAMETERS *****
// char** urls: the array of char* (passed by reference)
// int size: the size of the array (passed by value)
// ***** OUTPUT PARAMETER *****
// An integer denoting the choice made by the user
// 0 to exit
// a value > 0, to download a file
int prompt_user(char** urls, int size);

int activeDownloads = 0;

int main() {

    // Setting the size of the array of files to be downloaded
    int numberOfUrls = 5;
    // Array of files to be downloaded
    char* urls[] = {
            "http://www.gutenberg.org/files/10172/10172-m/10172-m-001.mp3",
            "http://www.gutenberg.org/files/10305/10305-m/10305-m-001.mp3",
            "http://www.gutenberg.org/files/10244/10244-m/10244-m-001.mp3",
            "http://www.gutenberg.org/files/10275/10275-m/10275-m-001.mp3",
            "http://www.gutenberg.org/files/10262/10262-m/10262-m-001.mp3"
    };    
    
    // Declaring the process identifier
    pid_t pid; //in the while loop the fork function will be called... passing 
    //passing address of this
    
    // In an infinite cycle...
    while (true) {
        
        if (activeDownloads < 3) {
            
            //print the prompt to the user 
            int choose = prompt_user(urls, numberOfUrls);
        
            switch(choose){
                case 0: 
                    wait(NULL); //will wait until all the childs have finisched to work
                    wait(NULL);
                    wait(NULL);
                    exit(0);
                    break;
                
                    //if int != 0 -> start downloading the file from the url creating a new child
                case 1: 
                    
                    pid = fork();
                    
                    if(pid == 0) {
                        activeDownloads++;
                        printf("\nBefore calling the second fork, %i %i\n", activeDownloads, pid);
                        pid = fork();
                        if(pid == 0){
                            execlp("curl", "curl", "-Os", "http://www.gutenberg.org/files/10172/10172-m/10172-m-001.mp3", NULL);
                        }
                        else {
                            wait(NULL);
                            activeDownloads = activeDownloads - 1;
                            printf("\nFinisch downloading, %i %i\n", activeDownloads, pid);
                            exit(0);
                        }//resume from the fork function
                        exit(0);
                    }
                    break;
                case 2:
                    pid = fork();
                    if(pid == 0) {
                        //working from the child... starts downloading
                        
                        //compute the download and exit 
                        exit(0);
                        //resume from the fork function
                    }
                    else {
                        //parent... 
                        break;
                        //continue running for getting new requests
                    }
                    break;
                case 3: 
                    pid = fork();
                    if(pid == 0) {
                        //working from the child... starts downloading
                        
                        //compute the download and exit 
                        exit(0);
                        //resume from the fork function
                    }
                    else {
                        //parent... 
                        break;
                        //continue running for getting new requests
                    }
                    break;
                case 4:
                    pid = fork();
                    if(pid == 0) {
                        //working from the child... starts downloading
                        
                        //compute the download and exit 
                        exit(0);
                        //resume from the fork function
                    }
                    else {
                        //parent... 
                        break;
                        //continue running for getting new requests
                    }
                    break;
                case 5: 
                    pid = fork();
                    if(pid == 0) {
                        //working from the child... starts downloading
                        
                        //compute the download and exit 
                        exit(0);
                        //resume from the fork function
                    }
                    else {
                        //parent... 
                        break;
                        //continue running for getting new requests
                    }
                    break;
            }   
        }
        else {
            printf("Cannot download another process... 3 are downloading yet");
            sleep(1);
        }
    }
}


// Implementation of the "prompt_user" function
int prompt_user(char** urls, int size) {
	
    int action;
    
    while (true) {
        // We list all the files to could be downloaded
    	// Then, we ask the user to type "0" to exit
    	// or the number corresponding to the file to be downloaded	
        printf("Type 0 to exit, or choose a file to download:\n");
        for (int i = 1; i <= size; i++) {
            printf("%i: %s\n", i, urls[i - 1]);
        }
        
        // "action" contains the choice made by the user
        scanf("%i", &action);
        
        // if the choice is a correct file to be downloaded, we exit from this function
        if (action >= 0 && action <= size) {
            break;
        }
    }
    // Returning the choice made by the user
    return action;
}
