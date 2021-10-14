#include <stdio.h>
#include <unistd.h>

int main() {
	int pid;
	
	printf("Prueba de clonacion de procesos:\n");

    pid = fork();
    if(pid == -1){
    	printf("\nError: no se pudo clonar el proceso.\n");
    }else{
         if(pid != 0){
    		printf("\nSoy el proceso padre con PID= %i y mi hijo es PID= %i\n",getppid(),getpid());
    	 }else{
    	 	printf("\nSoy el proceso hijo con PID= %i y mi padre es PID= %i\n",getpid(),getppid());
    	 }
    }

	return 0;
}
